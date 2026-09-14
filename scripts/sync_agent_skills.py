#!/usr/bin/env python3
"""Generate/check host-specific skill discovery adapters from canonical Game Design Suite skills.

Canonical source of truth:
    plugins/game-design-suite/skills/<name>/SKILL.md

Currently generated adapter:
    .deepcode/skills/<name>/SKILL.md

Adapters contain discovery metadata plus a pointer to the canonical SKILL.md. Professional
instructions and references stay in one place. Adapter descriptions may be shortened for
host routing, so the default check validates identity + canonical linkage rather than exact
byte equality. Use --strict to require generated adapters to match canonical descriptions.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_ROOT = ROOT / "plugins" / "game-design-suite" / "skills"
DEEPCODE_ROOT = ROOT / ".deepcode" / "skills"


def parse_frontmatter_text(text: str, source: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        raise ValueError(f"missing YAML frontmatter: {source}")
    end = text.find("\n---", 4)
    if end < 0:
        raise ValueError(f"unterminated YAML frontmatter: {source}")
    header = text[4:end]
    name_match = re.search(r"(?m)^name:\s*(.+?)\s*$", header)
    desc_match = re.search(r"(?m)^description:\s*(.+?)\s*$", header)
    if not name_match or not desc_match:
        raise ValueError(f"name/description missing in frontmatter: {source}")
    return name_match.group(1).strip().strip('"'), desc_match.group(1).strip().strip('"')


def parse_frontmatter(path: Path) -> tuple[str, str]:
    return parse_frontmatter_text(path.read_text(encoding="utf-8"), str(path))


def canonical_pointer(name: str) -> str:
    return f"../../../plugins/game-design-suite/skills/{name}/SKILL.md"


def deepcode_adapter(name: str, description: str) -> str:
    canonical = canonical_pointer(name)
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


def canonical_skills() -> dict[str, tuple[Path, str]]:
    if not CANONICAL_ROOT.is_dir():
        raise FileNotFoundError(f"canonical skill root not found: {CANONICAL_ROOT}")
    result: dict[str, tuple[Path, str]] = {}
    for skill_dir in sorted(p for p in CANONICAL_ROOT.iterdir() if p.is_dir()):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            continue
        name, description = parse_frontmatter(skill_md)
        if name != skill_dir.name:
            raise ValueError(f"skill name/path mismatch: {skill_dir.name} != {name}")
        result[name] = (skill_md, description)
    return result


def expected_adapters() -> dict[Path, str]:
    return {
        DEEPCODE_ROOT / name / "SKILL.md": deepcode_adapter(name, description)
        for name, (_, description) in canonical_skills().items()
    }


def check(strict: bool = False) -> int:
    canonical = canonical_skills()
    problems: list[str] = []

    for name, (_, description) in canonical.items():
        path = DEEPCODE_ROOT / name / "SKILL.md"
        if not path.is_file():
            problems.append(f"missing: {path.relative_to(ROOT)}")
            continue

        current = path.read_text(encoding="utf-8")
        try:
            adapter_name, _ = parse_frontmatter_text(current, str(path))
        except ValueError as exc:
            problems.append(str(exc))
            continue

        if adapter_name != name:
            problems.append(f"name mismatch: {path.relative_to(ROOT)} -> {adapter_name!r}, expected {name!r}")

        pointer = canonical_pointer(name)
        if pointer not in current:
            problems.append(f"missing canonical pointer: {path.relative_to(ROOT)} -> {pointer}")

        if strict and current != deepcode_adapter(name, description):
            problems.append(f"non-generated/stale adapter: {path.relative_to(ROOT)}")

    existing = set(DEEPCODE_ROOT.glob("*/SKILL.md")) if DEEPCODE_ROOT.exists() else set()
    expected = {DEEPCODE_ROOT / name / "SKILL.md" for name in canonical}
    for path in sorted(existing - expected):
        problems.append(f"orphan adapter: {path.relative_to(ROOT)}")

    if problems:
        print("Adapter check failed:")
        for problem in problems:
            print(f"  - {problem}")
        if strict:
            print("Run: python scripts/sync_agent_skills.py")
        return 1

    mode = "strict" if strict else "linkage"
    print(f"OK: {len(canonical)} Deep Code adapters pass {mode} validation.")
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
    parser.add_argument("--strict", action="store_true", help="with --check, require exact generated descriptions/body")
    args = parser.parse_args()
    if args.strict and not args.check:
        parser.error("--strict requires --check")
    return check(strict=args.strict) if args.check else write()


if __name__ == "__main__":
    sys.exit(main())
