from pathlib import Path
import json, re, sys

root = Path(__file__).resolve().parent
errors = []

market_path = root / ".agents" / "plugins" / "marketplace.json"
plugin_root = root / "plugins" / "game-design-suite"
plugin_manifest_path = plugin_root / ".codex-plugin" / "plugin.json"
skills_root = plugin_root / "skills"

# Marketplace
if not market_path.exists():
    errors.append("missing .agents/plugins/marketplace.json")
else:
    try:
        market = json.loads(market_path.read_text(encoding="utf-8"))
        if market.get("name") != "xiaomi867-game-design-suite":
            errors.append("marketplace name mismatch")
        entries = market.get("plugins", [])
        entry = next((x for x in entries if x.get("name") == "game-design-suite"), None)
        if not entry:
            errors.append("marketplace missing game-design-suite entry")
        else:
            if entry.get("source", {}).get("path") != "./plugins/game-design-suite":
                errors.append("marketplace plugin source path mismatch")
            policy = entry.get("policy", {})
            if policy.get("installation") not in {"AVAILABLE", "INSTALLED_BY_DEFAULT", "NOT_AVAILABLE"}:
                errors.append("invalid marketplace installation policy")
            if policy.get("authentication") not in {"ON_INSTALL", "ON_USE"}:
                errors.append("invalid marketplace authentication policy")
    except Exception as e:
        errors.append(f"invalid marketplace.json: {e}")

# Plugin manifest
if not plugin_manifest_path.exists():
    errors.append("missing plugins/game-design-suite/.codex-plugin/plugin.json")
else:
    try:
        plugin = json.loads(plugin_manifest_path.read_text(encoding="utf-8"))
        if plugin.get("name") != "game-design-suite":
            errors.append("plugin name mismatch")
        if plugin.get("skills") != "./skills/":
            errors.append("plugin skills path must be ./skills/")
        if not re.fullmatch(r"\d+\.\d+\.\d+", str(plugin.get("version", ""))):
            errors.append("plugin version must be semver x.y.z")
    except Exception as e:
        errors.append(f"invalid plugin.json: {e}")

# Skills
skills = sorted(skills_root.glob("*/SKILL.md")) if skills_root.exists() else []
if not skills:
    errors.append("No SKILL.md files found under plugin skills path")

names = set()
for p in skills:
    text = p.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{p}: missing YAML frontmatter start")
        continue
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        errors.append(f"{p}: missing YAML frontmatter end")
        continue
    fm = parts[0][4:]
    m_name = re.search(r"^name:\s*(.+)$", fm, re.M)
    m_desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    if not m_name:
        errors.append(f"{p}: missing name")
    else:
        name = m_name.group(1).strip()
        if name in names:
            errors.append(f"{p}: duplicate name {name}")
        names.add(name)
        if p.parent.name != name:
            errors.append(f"{p}: directory name != skill name ({name})")
    if not m_desc:
        errors.append(f"{p}: missing description")

# Index paths
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

print(f"OK: marketplace + plugin manifest + {len(skills)} skills validated")
for p in skills:
    print("-", p.parent.name)
