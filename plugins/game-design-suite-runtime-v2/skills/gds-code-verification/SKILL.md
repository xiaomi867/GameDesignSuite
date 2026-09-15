---
name: gds-code-verification
description: "Use when Game Design Suite is invoked to verify implementation semantics in client or server code: parsers, enums, defaults, field reads, target selection, buffs, stacking, random logic, upgrade inheritance, runtime execution paths, or config-to-code parity."
user-invocable: true
disable-model-invocation: false
---

# Code Verification

## Runtime role

This is a self-contained Game Design Suite specialist Skill. It must be useful when loaded directly; it does not depend on a parent router and must not assume another Skill was invoked.

Before substantive work, read [Canonical detailed guidance](references/canonical-guidance.md) and then read any supporting references/templates it points to that are relevant to the task.

## Scope

客户端/服务器读取、Parser、Enum、默认值、字段语义、Target、Buff、随机、继承与真实运行链路。

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
主责：代码 / 实现验证（gds-code-verification）
协同：仅列当前结果中实际加载并使用的专业；没有则写“无”
证据边界：写明当前最高证据层级与关键缺口
```

Do not require the user to ask for this header.

## Domain workflow

1. 定位真实读取入口
2. 追踪字段→Parser→运行对象
3. 核对 Enum/默认值/分支
4. 验证调用链和生效时机
5. 区分 verified-code 与 runtime 未验证

## Evidence states

Use the smallest accurate label needed: `confirmed`, `supported-inference`, `candidate`, `assumed`, `unknown`, `verified-config`, `verified-code`, `verified-runtime`, `verified-data`, `not-yet-playtested`, `externally-blocked`.

## Done criteria

A complete answer should contain the decision, rationale, concrete rules/values/fields when appropriate, risks, and the minimum next validation needed. Use the canonical guidance for domain-specific completion criteria and anti-pattern checks.
