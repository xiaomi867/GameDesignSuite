from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parent
PLUGIN = ROOT / "plugins" / "game-design-suite-runtime-v2"
RUNTIME = PLUGIN / "runtime-skills"
KNOWLEDGE = PLUGIN / "skills"
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"

EXPECTED_RUNTIME = {
    "gds-core",
    "gds-hero-skill",
    "gds-balance-simulation",
    "gds-itemization",
    "gds-combat",
    "gds-economy-progression",
    "gds-level-ux",
    "gds-audit-verification",
}

EXPECTED_KNOWLEDGE = {
    "gds-game-design",
    "gds-game-production",
    "gds-design-frameworks",
    "gds-design-review",
    "gds-game-design-doc",
    "gds-hero-concept-design",
    "gds-hero-kit-design",
    "gds-hero-stat-progression",
    "gds-skill-design",
    "gds-skill-value-design",
    "gds-balance-design",
    "gds-formula-verification",
    "gds-simulation-design",
    "gds-telemetry-experiment-design",
    "gds-meta-balance",
    "gds-itemization-design",
    "gds-itemization-benchmark",
    "gds-combat-design",
    "gds-economy-design",
    "gds-progression-design",
    "gds-level-design",
    "gds-game-interface-design",
    "gds-config-audit",
    "gds-code-verification",
}

errors = []

manifest_path = PLUGIN / ".codex-plugin" / "plugin.json"
if not manifest_path.exists():
    errors.append("missing plugin manifest")
else:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("name") != "game-design-suite-consolidated-v3":
        errors.append("plugin name must be game-design-suite-consolidated-v3")
    if manifest.get("skills") != "./runtime-skills/":
        errors.append("manifest must expose only ./runtime-skills/")
    if not str(manifest.get("version", "")).startswith("3.0.0-preview."):
        errors.append("consolidated runtime must use 3.0.0-preview.x versioning")

plugin_agent = PLUGIN / "agents" / "openai.yaml"
if not plugin_agent.exists():
    errors.append("missing plugin-level agents/openai.yaml")

runtime_files = sorted(RUNTIME.glob("*/SKILL.md"))
runtime_names = {p.parent.name for p in runtime_files}
if runtime_names != EXPECTED_RUNTIME:
    errors.append(f"runtime skill set mismatch: {sorted(runtime_names)}")

diagnostic_pattern = re.compile(r"GDS_(?:CANARY|ROUTER|DIRECT|REFRESH|ITEMIZATION_PROBE)", re.I)
descriptions = []

for skill_file in runtime_files:
    text = skill_file.read_text(encoding="utf-8")
    rel = skill_file.relative_to(ROOT)
    if not text.startswith("---\n"):
        errors.append(f"{rel}: missing frontmatter")
        continue
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        errors.append(f"{rel}: malformed frontmatter")
        continue
    fm, body = parts
    name_match = re.search(r"^name:\s*(.+)$", fm, re.M)
    desc_match = re.search(r'^description:\s*["\']?(.*?)["\']?$', fm, re.M)
    if not name_match or name_match.group(1).strip() != skill_file.parent.name:
        errors.append(f"{rel}: name must match directory")
    if not desc_match:
        errors.append(f"{rel}: missing description")
    else:
        desc = desc_match.group(1).strip().strip('"').strip("'")
        descriptions.append((skill_file.parent.name, desc))
        if not desc.lower().startswith("use when"):
            errors.append(f"{rel}: description must start with 'Use when'")
        if len(desc) > 240:
            errors.append(f"{rel}: description too long ({len(desc)} > 240)")
        if len(desc) < 70:
            errors.append(f"{rel}: description too short to disambiguate ({len(desc)} < 70)")
    if "user-invocable:" in fm or "disable-model-invocation:" in fm:
        errors.append(f"{rel}: remove cross-harness invocation fields; use agents/openai.yaml policy")
    if len(text.splitlines()) > 140:
        errors.append(f"{rel}: runtime wrapper too large; move detail to preserved knowledge")
    agent = skill_file.parent / "agents" / "openai.yaml"
    if not agent.exists():
        errors.append(f"{rel}: missing agents/openai.yaml")
    else:
        agent_text = agent.read_text(encoding="utf-8")
        if "allow_implicit_invocation: true" not in agent_text:
            errors.append(f"{rel}: implicit invocation must be true")
        if "default_prompt:" not in agent_text:
            errors.append(f"{rel}: missing default_prompt")
    if diagnostic_pattern.search(text):
        errors.append(f"{rel}: diagnostic token leaked into production runtime")

TOTAL_DESCRIPTION_BUDGET = 1800
total_desc = sum(len(desc) for _, desc in descriptions)
if total_desc > TOTAL_DESCRIPTION_BUDGET:
    errors.append(f"aggregate runtime description budget exceeded: {total_desc} > {TOTAL_DESCRIPTION_BUDGET}")

knowledge_dirs = {p.name for p in KNOWLEDGE.iterdir() if p.is_dir()} if KNOWLEDGE.exists() else set()
missing_knowledge = EXPECTED_KNOWLEDGE - knowledge_dirs
if missing_knowledge:
    errors.append(f"missing preserved knowledge modules: {sorted(missing_knowledge)}")

for name in EXPECTED_KNOWLEDGE:
    canonical = KNOWLEDGE / name / "references" / "canonical-guidance.md"
    if not canonical.exists():
        errors.append(f"{name}: missing preserved canonical-guidance.md")
    elif canonical.stat().st_size < 300:
        errors.append(f"{name}: canonical guidance unexpectedly small")

knowledge_map = PLUGIN / "references" / "runtime-knowledge-map.md"
if not knowledge_map.exists():
    errors.append("missing runtime knowledge map")

if MARKETPLACE.exists():
    market = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    entries = {row.get("name"): row for row in market.get("plugins", [])}
    if "game-design-suite-consolidated-v3" not in entries:
        errors.append("marketplace missing game-design-suite-consolidated-v3")
else:
    errors.append("missing marketplace")

if errors:
    print("FAILED: consolidated runtime validation")
    for error in errors:
        print("-", error)
    sys.exit(1)

print(f"OK: consolidated runtime validated ({len(runtime_files)} runtime entries, 24 preserved modules, {total_desc} description chars)")
