---
name: gds-game-interface-design
description: "Use when Game Design Suite is invoked for game UI/UX: HUD, menus, information hierarchy, interaction flows, onboarding, feedback, input prompts, accessibility, state communication, or interface requirements for game systems."
user-invocable: true
disable-model-invocation: false
---

# Game Interface Design

## Runtime role

This is a self-contained Game Design Suite specialist Skill. It must be useful when loaded directly; it does not depend on a parent router and must not assume another Skill was invoked.

Before substantive work, read [Canonical detailed guidance](references/canonical-guidance.md) and then read any supporting references/templates it points to that are relevant to the task.

## Scope

HUD、菜单、信息层级、交互流程、引导、反馈、输入提示、Accessibility 与系统状态表达。

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
主责：游戏 UI/UX 策划（gds-game-interface-design）
协同：仅列当前结果中实际加载并使用的专业；没有则写“无”
证据边界：写明当前最高证据层级与关键缺口
```

Do not require the user to ask for this header.

## Domain workflow

1. 定义用户任务与信息优先级
2. 建立界面流程与状态
3. 设计反馈和错误恢复
4. 检查输入与可访问性
5. 验证信息负荷与操作成本

## Evidence states

Use the smallest accurate label needed: `confirmed`, `supported-inference`, `candidate`, `assumed`, `unknown`, `verified-config`, `verified-code`, `verified-runtime`, `verified-data`, `not-yet-playtested`, `externally-blocked`.

## Done criteria

A complete answer should contain the decision, rationale, concrete rules/values/fields when appropriate, risks, and the minimum next validation needed. Use the canonical guidance for domain-specific completion criteria and anti-pattern checks.
