from pathlib import Path
import re, sys

root = Path(__file__).resolve().parent
errors = []
skills = sorted((root / "skills").glob("*/SKILL.md"))
if not skills:
    errors.append("No SKILL.md files found")

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

if errors:
    print("FAILED")
    for e in errors:
        print("-", e)
    sys.exit(1)

print(f"OK: {len(skills)} skills validated")
for p in skills:
    print("-", p.parent.name)
