---
name: gds-config-audit
description: "Use when Game Design Suite is invoked to audit game configuration or data tables: Excel/CSV/JSON rows, keys, IDs, fields, references, missing entries, duplicates, types, targets, buffs, groups, stacking, weights, random pools, or schema/value consistency."
user-invocable: true
disable-model-invocation: false
---

# Config Audit

## Runtime role

This is a self-contained Game Design Suite specialist Skill. It must be useful when loaded directly; it does not depend on a parent router and must not assume another Skill was invoked.

Before substantive work, read [Canonical detailed guidance](references/canonical-guidance.md) and then read any supporting references/templates it points to that are relevant to the task.

## Scope

Excel/CSV/JSON配置、Row/Key/ID、字段归属、引用、漏配、重复、类型、Target、Buff、Group/Stack与权重一致性。

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
主责：配置审计（gds-config-audit）
协同：仅列当前结果中实际加载并使用的专业；没有则写“无”
证据边界：写明当前最高证据层级与关键缺口
```

Do not require the user to ask for this header.

## Domain workflow

1. 先锁定 Schema 与字段归属
2. 再做 Row/Value Pass
3. 检查引用与缺失/重复
4. 验证 Group/Target/Stack/Weight
5. 输出字段级 current→change→reason

## Evidence states

Use the smallest accurate label needed: `confirmed`, `supported-inference`, `candidate`, `assumed`, `unknown`, `verified-config`, `verified-code`, `verified-runtime`, `verified-data`, `not-yet-playtested`, `externally-blocked`.

## Done criteria

A complete answer should contain the decision, rationale, concrete rules/values/fields when appropriate, risks, and the minimum next validation needed. Use the canonical guidance for domain-specific completion criteria and anti-pattern checks.
