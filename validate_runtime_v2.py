from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parent
PLUGIN = ROOT / "plugins" / "game-design-suite-runtime-v2"
SKILLS = PLUGIN / "skills"
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"

errors = []

if not PLUGIN.exists():
    print("SKIP: rebuilt runtime plugin not generated yet")
    sys.exit(0)

manifest_path = PLUGIN / ".codex-plugin" / "plugin.json"
if not manifest_path.exists():
    errors.append("missing rebuilt plugin manifest")
else:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("name") != "game-design-suite-runtime-v2":
        errors.append("rebuilt plugin name mismatch")
    if manifest.get("skills") != "./skills/":
        errors.append("rebuilt plugin skills path must be ./skills/")

skill_files = sorted(SKILLS.glob("*/SKILL.md"))
if len(skill_files) != 24:
    errors.append(f"expected 24 rebuilt runtime skills, found {len(skill_files)}")

diagnostic_pattern = re.compile(r"GDS_(?:CANARY|ROUTER|DIRECT|REFRESH|ITEMIZATION_PROBE)", re.I)

for skill_file in skill_files:
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
    desc_match = re.search(r"^description:\s*(.+)$", fm, re.M)
    user_match = re.search(r"^user-invocable:\s*(.+)$", fm, re.M)
    model_match = re.search(r"^disable-model-invocation:\s*(.+)$", fm, re.M)

    if not name_match:
        errors.append(f"{rel}: missing name")
        continue
    name = name_match.group(1).strip()
    if name != skill_file.parent.name:
        errors.append(f"{rel}: directory/name mismatch: {name}")
    if not name.startswith("gds-"):
        errors.append(f"{rel}: runtime skill name must start with gds-")

    if not desc_match:
        errors.append(f"{rel}: missing description")
    else:
        desc = desc_match.group(1).strip().strip('"').strip("'")
        if not desc.lower().startswith("use when"):
            errors.append(f"{rel}: description must start with 'Use when'")
        if len(desc) > 1024:
            errors.append(f"{rel}: description too long ({len(desc)})")

    if not user_match or user_match.group(1).strip().lower() != "true":
        errors.append(f"{rel}: user-invocable must be true")
    if not model_match or model_match.group(1).strip().lower() != "false":
        errors.append(f"{rel}: disable-model-invocation must be false")

    if len(text.splitlines()) > 220:
        errors.append(f"{rel}: runtime SKILL.md too large; use progressive disclosure")

    agents = skill_file.parent / "agents" / "openai.yaml"
    if not agents.exists():
        errors.append(f"{rel}: missing agents/openai.yaml")
    else:
        agent_text = agents.read_text(encoding="utf-8")
        if "allow_implicit_invocation: true" not in agent_text:
            errors.append(f"{rel}: implicit invocation must be true")
        if "default_prompt:" not in agent_text:
            errors.append(f"{rel}: missing default_prompt in agents/openai.yaml")

    canonical = skill_file.parent / "references" / "canonical-guidance.md"
    if not canonical.exists():
        errors.append(f"{rel}: missing references/canonical-guidance.md")
    elif canonical.stat().st_size < 300:
        errors.append(f"{rel}: canonical guidance unexpectedly small")

    if diagnostic_pattern.search(text):
        errors.append(f"{rel}: diagnostic token leaked into rebuilt runtime wrapper")

if MARKETPLACE.exists():
    market = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    entries = {row.get("name"): row for row in market.get("plugins", [])}
    if "game-design-suite-runtime-v2" not in entries:
        errors.append("marketplace missing game-design-suite-runtime-v2")
else:
    errors.append("missing marketplace")

if errors:
    print("FAILED: rebuilt runtime validation")
    for error in errors:
        print("-", error)
    sys.exit(1)

print(f"OK: rebuilt runtime validated ({len(skill_files)} skills)")
