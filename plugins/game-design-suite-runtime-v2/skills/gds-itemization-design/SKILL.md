---
name: gds-itemization-design
description: "Use when Game Design Suite is invoked for equipment or itemization design: slots, rarity, base/main/substats, affix pools, roll ranges, enhancement, sets, unique effects, loot targeting, replacement, graduation, salvage, crafting, Best-in-Slot, or build ecology."
user-invocable: true
disable-model-invocation: false
---

# Itemization Design

## Runtime role

This is a self-contained Game Design Suite specialist Skill. It must be useful when loaded directly; it does not depend on a parent router and must not assume another Skill was invoked.

Before substantive work, read [Canonical detailed guidance](references/canonical-guidance.md) and then read any supporting references/templates it points to that are relevant to the task.

## Scope

装备槽位、品质、基础/主/副词条、Affix、Roll、强化、套装、唯一特效、掉落、替换、毕业、分解与Build生态。

## Execution contract

- Answer the user's actual task; do not stop at routing.
- Respect user-fixed rules and project constraints.
- Existing projects: inspect real docs/config/code/data before redesign when those sources are required and available.
- Missing evidence: mark dependent claims `unverified` or `externally-blocked`; do not invent project facts.
- Distinguish facts, symptoms, constraints, assumptions, candidate changes, and verified findings.
- Simulation/spreadsheets/theory are not Playtest evidence.
- Do not claim another specialist Skill executed unless its content was actually loaded.
- Use outside commercial-game data only as reference evidence, never as automatic project truth.

## Professional context

For every independent formal result, put this block immediately before the result:

```text
【本次专业视角】
主责：装备 / Itemization 策划（gds-itemization-design）
协同：仅列当前结果中实际加载并使用的专业；没有则写“无”
证据边界：写明当前最高证据层级与关键缺口
```

Do not require the user to ask for this header.

## Domain workflow

1. 定义 Itemization Job 与槽位职责
2. 建立 Item Power Budget
3. 设计主副属性与 Affix/Roll
4. 设计强化/套装/唯一特效
5. 验证实际升级率、替换、分解与Build生态

## Evidence states

Use the smallest accurate label needed: `confirmed`, `supported-inference`, `candidate`, `assumed`, `unknown`, `verified-config`, `verified-code`, `verified-runtime`, `verified-data`, `not-yet-playtested`, `externally-blocked`.

## Done criteria

A complete answer should contain the decision, rationale, concrete rules/values/fields when appropriate, risks, and the minimum next validation needed. Use the canonical guidance for domain-specific completion criteria and anti-pattern checks.
