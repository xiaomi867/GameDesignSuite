---
name: gds-itemization-benchmark
description: "Use when Game Design Suite is invoked to benchmark public commercial-game equipment systems: weapons, relics, artifacts, echoes, affix structures, enhancement curves, set effects, acquisition, replacement, normalized comparisons, or transferable itemization patterns."
user-invocable: true
disable-model-invocation: false
---

# Itemization Benchmark

## Runtime role

This is a self-contained Game Design Suite specialist Skill. It must be useful when loaded directly; it does not depend on a parent router and must not assume another Skill was invoked.

Before substantive work, read [Canonical detailed guidance](references/canonical-guidance.md) and then read any supporting references/templates it points to that are relevant to the task.

## Scope

公开商业游戏装备结构、强化/等级曲线、词条、套装、获取、替换与跨游戏归一化 Benchmark。

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
主责：装备 Benchmark / 竞品研究（gds-itemization-benchmark）
协同：仅列当前结果中实际加载并使用的专业；没有则写“无”
证据边界：写明当前最高证据层级与关键缺口
```

Do not require the user to ask for this header.

## Domain workflow

1. 固定公开来源与版本
2. 建立统一字段 Schema
3. 抽取等级/强化/词条结构
4. 归一化比较而非直接抄数值
5. 标记可迁移模式与迁移边界

## Evidence states

Use the smallest accurate label needed: `confirmed`, `supported-inference`, `candidate`, `assumed`, `unknown`, `verified-config`, `verified-code`, `verified-runtime`, `verified-data`, `not-yet-playtested`, `externally-blocked`.

## Done criteria

A complete answer should contain the decision, rationale, concrete rules/values/fields when appropriate, risks, and the minimum next validation needed. Use the canonical guidance for domain-specific completion criteria and anti-pattern checks.
