#!/usr/bin/env python3
"""Generate/check host-specific skill discovery adapters from canonical Game Design Suite skills.

Canonical source of truth:
    plugins/game-design-suite/skills/<name>/SKILL.md

Currently generated adapter:
    .deepcode/skills/<name>/SKILL.md

The adapter intentionally contains only discovery metadata plus a pointer to the canonical
SKILL.md. Professional instructions and references stay in one place.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_ROOT = ROOT / "plugins" / "game-design-suite" / "skills"
DEEPCODE_ROOT = ROOT / ".deepcode" / "skills"


def parse_frontmatter(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"missing YAML frontmatter: {path}")
    end = text.find("\n---", 4)
    if end < 0:
        raise ValueError(f"unterminated YAML frontmatter: {path}")
    header = text[4:end]
    name_match = re.search(r"(?m)^name:\s*(.+?)\s*$", header)
    desc_match = re.search(r"(?m)^description:\s*(.+?)\s*$", header)
    if not name_match or not desc_match:
        raise ValueError(f"name/description missing in frontmatter: {path}")
    return name_match.group(1).strip().strip('"'), desc_match.group(1).strip().strip('"')


def deepcode_adapter(name: str, description: str) -> str:
    canonical = f"../../../plugins/game-design-suite/skills/{name}/SKILL.md"
    return f"""---
name: {name}
description: {description}
---

# Deep Code Adapter

这是 Game Design Suite 的 Deep Code 发现适配文件，不是独立知识副本。

在执行本 Skill 前，必须完整读取并遵循唯一真源：

`{canonical}`

真源中引用的 `references/`、模板、脚本和其他 Skill 路径，应相对于真源文件所在目录解析。

如果真源缺失或不可读取，明确报告安装/仓库不完整；不要根据本适配文件重建、猜测或简化专业规则。
"""


def expected_adapters() -> dict[Path, str]:
    if not CANONICAL_ROOT.is_dir():
        raise FileNotFoundError(f"canonical skill root not found: {CANONICAL_ROOT}")
    result: dict[Path, str] = {}
    for skill_dir in sorted(p for p in CANONICAL_ROOT.iterdir() if p.is_dir()):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            continue
        name, description = parse_frontmatter(skill_md)
        if name != skill_dir.name:
            raise ValueError(f"skill name/path mismatch: {skill_dir.name} != {name}")
        result[DEEPCODE_ROOT / name / "SKILL.md"] = deepcode_adapter(name, description)
    return result


def check() -> int:
    expected = expected_adapters()
    problems: list[str] = []
    for path, content in expected.items():
        if not path.is_file():
            problems.append(f"missing: {path.relative_to(ROOT)}")
            continue
        current = path.read_text(encoding="utf-8")
        if current != content:
            problems.append(f"stale: {path.relative_to(ROOT)}")

    existing = set(DEEPCODE_ROOT.glob("*/SKILL.md")) if DEEPCODE_ROOT.exists() else set()
    extra = existing - set(expected)
    for path in sorted(extra):
        problems.append(f"orphan adapter: {path.relative_to(ROOT)}")

    if problems:
        print("Adapter check failed:")
        for problem in problems:
            print(f"  - {problem}")
        print("Run: python scripts/sync_agent_skills.py")
        return 1

    print(f"OK: {len(expected)} Deep Code adapters match canonical skills.")
    return 0


def write() -> int:
    expected = expected_adapters()
    for path, content in expected.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
    print(f"Synced {len(expected)} Deep Code adapters from canonical skills.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync Game Design Suite agent skill adapters")
    parser.add_argument("--check", action="store_true", help="check adapters without modifying files")
    args = parser.parse_args()
    return check() if args.check else write()


if __name__ == "__main__":
    sys.exit(main())
