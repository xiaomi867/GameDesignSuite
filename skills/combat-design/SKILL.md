---
name: combat-design
description: 负责战斗系统与遭遇规则，包括攻击、受击、目标选择、资源、状态、AI、战斗节奏、敌我职责、Boss/小怪战斗行为和战斗可读性。具体技能机制交给 skill-design，具体参数交给 balance-design。
---

# 战斗策划

目标是让玩家能理解战斗状态、做出有意义决策，并通过规则与反馈形成可控节奏。

## 战斗模型

明确：

- 战斗开始/结束条件；
- 单位状态；
- 攻击流程；
- Target 规则；
- 命中/暴击/伤害；
- 治疗；
- 控制；
- Buff/Debuff；
- 资源与大招；
- 死亡/复活；
- 波次；
- Boss 阶段；
- AI 决策。

## 决策与可读性

检查玩家是否能：

- 看懂威胁来源；
- 识别前后排/优先级；
- 理解技能释放结果；
- 预判 Boss 行为；
- 通过构筑或操作响应。

Telegraph 不应与实际结果冲突。

## 角色职责

区分：

- Carry / Burst / Sustained DPS
- Tank
- Healer
- Control
- Support
- Hybrid

职责可以混合，但应明确主要价值和代价。

## 遭遇设计

每种敌人/组合要提出不同问题，而不是只加血加攻。检查：

- Threat Priority；
- Target Pressure；
- Timing Window；
- Counterplay；
- Composition Synergy；
- Recovery Window。

## Boss

Boss 至少明确：

- 核心考题；
- 阶段；
- 关键招式；
- Telegraph；
- Counterplay；
- Enrage/Pressure；
- 失败原因可读性；
- 是否依赖特定角色才能通过。

## 与其他 Skill 协作

- 具体技能 -> `skill-design`
- 参数与强度 -> `balance-design`
- 场地空间 -> `level-design`
- 配置 -> `config-audit`
- 实际实现 -> `code-verification`

不要通过偷改技能机制解决单纯数值问题。
