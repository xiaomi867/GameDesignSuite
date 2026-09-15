---
name: gds-economy-design
description: "Use when Game Design Suite is invoked for game economy design: currencies, resource roles, sources and sinks, production, inventory, exchange rates, shops, rewards, inflation, hoarding, scarcity, or long-term resource circulation."
user-invocable: true
disable-model-invocation: false
---

# Economy Design

## Runtime role

This is a self-contained Game Design Suite specialist Skill. It must be useful when loaded directly; it does not depend on a parent router and must not assume another Skill was invoked.

Before substantive work, read [Canonical detailed guidance](references/canonical-guidance.md) and then read any supporting references/templates it points to that are relevant to the task.

## Scope

资源角色、Sources/Sinks、库存、产出、消耗、兑换、商店、奖励、通胀与生命周期。

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
主责：经济策划（gds-economy-design）
协同：仅列当前结果中实际加载并使用的专业；没有则写“无”
证据边界：写明当前最高证据层级与关键缺口
```

Do not require the user to ask for this header.

## Domain workflow

1. 定义资源角色与价值锚
2. 列 Sources/Sinks 与流速
3. 检查库存与生命周期
4. 验证 Sink 合法性和健康盈余
5. 建立经济监控与调参指标

## Evidence states

Use the smallest accurate label needed: `confirmed`, `supported-inference`, `candidate`, `assumed`, `unknown`, `verified-config`, `verified-code`, `verified-runtime`, `verified-data`, `not-yet-playtested`, `externally-blocked`.

## Done criteria

A complete answer should contain the decision, rationale, concrete rules/values/fields when appropriate, risks, and the minimum next validation needed. Use the canonical guidance for domain-specific completion criteria and anti-pattern checks.
