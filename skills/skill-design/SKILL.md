---
name: skill-design
description: 负责角色/英雄技能设计、诊断和改造，包括普攻、主动、被动、大招、Target、触发、Buff/Debuff、持续、叠加、技能等级、升星影响和构筑关系。已有项目默认不改变用户要求保持的技能机制。
---

# 技能策划

## 机制保护

先区分：

### Fixed Rules
- 技能类型；
- Target 逻辑；
- 触发条件；
- 状态关系；
- 技能行为；
- 玩家明确要求保留的机制。

### Tunables
- 倍率；
- CD；
- 持续；
- 概率；
- 阈值；
- Buff 数值；
- 消耗；
- 初始资源。

用户说“不改机制”时，不通过改 Target、触发、状态或技能结构绕过约束。

## 技能检查清单

每个技能根据任务检查：

- Skill Definition
- Target / Target Selector
- Trigger
- Damage / Heal Source
- Multiplier
- Damage Type
- Crit
- Resource Cost/Gain
- Buff / Debuff
- Duration
- Stack / Refresh / Exclusive
- Group / Mutual Exclusion
- Cooldown / Interval
- Condition
- Priority
- Level Mapping
- Star Mapping
- Interaction with Passive/Ultimate
- Edge Cases

## 技能等级与升星

升星/升级必须回答：

- 影响哪个技能；
- 改哪个维度；
- 单次收益；
- 累积收益；
- 是否改变机制；
- 是否出现关键断层；
- 是否符合品质/稀有度定位。

避免每次升星同时提升过多技能，除非项目规则明确如此。

## 构筑价值

检查技能是否：

- 支撑角色定位；
- 与队友形成互补；
- 存在主核/副核；
- 有明确适用场景；
- 不形成无条件主导策略；
- 不依赖不可控 RNG 才能成立。

## 与数值协作

具体倍率与强度交给 `balance-design`。技能策划负责定义参数影响方向与允许范围。

## 与配置协作

已有配置项目应与 `config-audit` 检查：

- Skill Key/ID；
- BuffCfg；
- Target；
- GroupKey；
- Damage/Heal 字段；
- Level/Star 映射；
- 缺失行；
- 关联引用。

若需要确认运行时行为，与 `code-verification` 协作。

## 输出要求

用户要求落表时不能只写“加强/削弱”。至少给：

| 表/对象 | Key/ID | 字段 | 当前值 | 改后值 | 影响 | 理由 | 验证 |
|---|---|---|---|---|---|---|---|

当前值未知时标 `unknown`。
