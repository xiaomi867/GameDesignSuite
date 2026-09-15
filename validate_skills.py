from pathlib import Path
import json, re, sys

root = Path(__file__).resolve().parent
errors = []

market_path = root / ".agents" / "plugins" / "marketplace.json"
canonical_plugin_name = "game-design-suite"
canonical_plugin_path = root / "plugins" / canonical_plugin_name

semver_re = re.compile(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?")


def validate_skill_tree(plugin_name: str, skills_root: Path) -> int:
    skills = sorted(skills_root.glob("*/SKILL.md")) if skills_root.exists() else []
    if not skills:
        errors.append(f"{plugin_name}: no SKILL.md files found under {skills_root.relative_to(root)}")
        return 0

    names = set()
    for p in skills:
        text = p.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"{p.relative_to(root)}: missing YAML frontmatter start")
            continue
        parts = text.split("\n---\n", 1)
        if len(parts) != 2:
            errors.append(f"{p.relative_to(root)}: missing YAML frontmatter end")
            continue
        fm = parts[0][4:]
        m_name = re.search(r"^name:\s*(.+)$", fm, re.M)
        m_desc = re.search(r"^description:\s*(.+)$", fm, re.M)
        if not m_name:
            errors.append(f"{p.relative_to(root)}: missing name")
        else:
            name = m_name.group(1).strip()
            if name in names:
                errors.append(f"{plugin_name}: duplicate skill name {name}")
            names.add(name)
            if p.parent.name != name:
                errors.append(f"{p.relative_to(root)}: directory name != skill name ({name})")
        if not m_desc:
            errors.append(f"{p.relative_to(root)}: missing description")
    return len(skills)


plugin_summaries = []

# Marketplace + every listed local plugin
if not market_path.exists():
    errors.append("missing .agents/plugins/marketplace.json")
else:
    try:
        market = json.loads(market_path.read_text(encoding="utf-8"))
        if market.get("name") != "game-design-suite-marketplace":
            errors.append("marketplace name mismatch")

        entries = market.get("plugins", [])
        if not entries:
            errors.append("marketplace has no plugins")

        if not any(x.get("name") == canonical_plugin_name for x in entries):
            errors.append("marketplace missing game-design-suite entry")

        seen_plugins = set()
        for entry in entries:
            plugin_name = entry.get("name")
            if not plugin_name:
                errors.append("marketplace plugin entry missing name")
                continue
            if plugin_name in seen_plugins:
                errors.append(f"duplicate marketplace plugin name: {plugin_name}")
                continue
            seen_plugins.add(plugin_name)

            source = entry.get("source", {})
            if source.get("source") != "local":
                errors.append(f"{plugin_name}: marketplace source must be local")
                continue
            source_path = source.get("path")
            if not source_path:
                errors.append(f"{plugin_name}: marketplace source path missing")
                continue

            plugin_root = (root / source_path).resolve()
            try:
                plugin_root.relative_to(root.resolve())
            except ValueError:
                errors.append(f"{plugin_name}: plugin path escapes repository")
                continue

            policy = entry.get("policy", {})
            if policy.get("installation") not in {"AVAILABLE", "INSTALLED_BY_DEFAULT", "NOT_AVAILABLE"}:
                errors.append(f"{plugin_name}: invalid marketplace installation policy")
            if policy.get("authentication") not in {"ON_INSTALL", "ON_USE"}:
                errors.append(f"{plugin_name}: invalid marketplace authentication policy")

            manifest_path = plugin_root / ".codex-plugin" / "plugin.json"
            if not manifest_path.exists():
                errors.append(f"{plugin_name}: missing .codex-plugin/plugin.json")
                continue

            try:
                plugin = json.loads(manifest_path.read_text(encoding="utf-8"))
                if plugin.get("name") != plugin_name:
                    errors.append(f"{plugin_name}: plugin manifest name mismatch ({plugin.get('name')})")
                if plugin.get("skills") != "./skills/":
                    errors.append(f"{plugin_name}: plugin skills path must be ./skills/")
                if not semver_re.fullmatch(str(plugin.get("version", ""))):
                    errors.append(f"{plugin_name}: plugin version must be semver x.y.z or prerelease")
            except Exception as e:
                errors.append(f"{plugin_name}: invalid plugin.json: {e}")
                continue

            skill_count = validate_skill_tree(plugin_name, plugin_root / "skills")
            plugin_summaries.append((plugin_name, skill_count))

    except Exception as e:
        errors.append(f"invalid marketplace.json: {e}")

# Canonical index still points only at the canonical Game Design Suite knowledge source.
idx_path = root / "skills-index.json"
if idx_path.exists():
    try:
        index = json.loads(idx_path.read_text(encoding="utf-8"))
        for row in index:
            p = root / row.get("path", "")
            if not p.exists():
                errors.append(f"skills-index path missing: {row.get('path')}")
    except Exception as e:
        errors.append(f"invalid skills-index.json: {e}")

if errors:
    print("FAILED")
    for e in errors:
        print("-", e)
    sys.exit(1)

print(f"OK: marketplace + {len(plugin_summaries)} plugin manifests validated")
for plugin_name, skill_count in plugin_summaries:
    print(f"- {plugin_name}: {skill_count} runtime skill(s)")
