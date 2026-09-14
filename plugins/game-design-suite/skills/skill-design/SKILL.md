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

## Skill Grammar / 技能语法

每个技能尽量拆成：

`Input/Trigger -> Acquire Target -> Cost -> Cast -> Resolve -> Damage/Heal -> Buff/Debuff -> Secondary Trigger -> Resource/CD Update`

这样可以明确：

- Target 何时确定；
- Cost 何时扣；
- Damage 与 Buff 的先后；
- Secondary Effect 是否会重复触发；
- 死亡/击杀/破盾等事件在何时判定；
- Buff 读取施法前还是施法后属性。

## 技能检查清单

每个技能根据任务检查：

- Skill Definition
- Target / Target Selector
- Trigger
- Scaling Source：ATK / DEF / HP / Fixed / Mixed
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
- Action Advance / Extra Action / Follow-up / Counter
- Energy / Rage Cycle
- Hit / Resist Reliability
- Secondary Gauge Contribution
- Edge Cases

## Scaling Source / 倍率基准属性

必须明确每段效果到底引用：

- 自身攻击；
- 自身防御；
- 自身生命；
- 目标生命；
- 已损生命；
- 固定值；
- 混合属性。

不要只看到 `DamageCfg` 就假设倍率对象。已有项目需要结合 `config-audit + code-verification` 确认枚举、解析与运行时对象。

### 设计检查

- Scaling Source 是否符合角色职责；
- 是否形成有意义的配装方向；
- 是否让 Tank/Healer 为了输出被迫堆不相关属性；
- Mixed Scaling 是否只是增加复杂度而没有决策价值；
- 目标生命倍率是否对 Boss 有上限或特殊规则。

## Skill Rotation / 技能循环

技能不能只单独看倍率，应放进完整 Rotation：

- 普攻频率；
- 技能频率；
- 大招周期；
- 被动触发频率；
- 追击/反击次数；
- Buff 覆盖；
- 资源净流；
- 是否因为速度/额外行动改变循环。

### 角色资源标签

可以根据团队共享资源把角色标记为：

- Resource Positive；
- Resource Neutral；
- Resource Negative；
- Burst Consumer；
- Emergency Consumer。

这会直接影响队伍搭配与角色真实价值。

## Buff/Debuff Duration Semantics

“持续 2 回合”必须明确是谁的回合：

- 施法者行动；
- 目标行动；
- 全局 Round；
- 固定时间；
- 触发次数。

当游戏存在：

- 加速；
- 行动提前；
- 额外行动；
- 插队；

时，不同 Duration Semantics 会产生完全不同的实际覆盖率。

## 状态可靠性

Debuff/控制类技能不能只看 Base Chance。

应协作 `balance-design` 检查：

- 普通怪实际命中率；
- Elite；
- Boss；
- Specific Resist；
- Immunity；
- 多段判定；
- 是否存在 100% 文本但实际不稳定的情况。

## 技能等级与升星

升星/升级必须回答：

- 影响哪个技能；
- 改哪个维度；
- 单次收益；
- 累积收益；
- 是否改变机制；
- 是否出现关键断层；
- 是否符合品质/稀有度定位；
- 是否跨过 Rotation / Energy / Hit / Stack Breakpoint。

避免每次升星同时提升过多技能，除非项目规则明确如此。

### 节点价值

升级不应该只是把所有倍率同步 +X%。可以区分：

- 稳定数值成长；
- 条件改善；
- 覆盖率改善；
- 资源效率；
- Build 联动；
- 关键 Breakpoint。

但用户明确要求“不改机制”时，只能在允许的 Tunables 内实现，不通过新增行为制造假“成长”。

## 构筑价值

检查技能是否：

- 支撑角色定位；
- 与队友形成互补；
- 存在主核/副核；
- 有明确适用场景；
- 不形成无条件主导策略；
- 不依赖不可控 RNG 才能成立；
- 不因另一技能的速度/资源行为导致隐藏负协同。

### 负协同检查

例如：

- 控制让反击无法触发；
- 治疗把低血 Build 永久抬出阈值；
- 加速导致 Buff 提前过期；
- 额外行动让共享资源快速转负；
- 秒杀小怪让叠层技能失去目标；
- Target 改变让被动无法稳定触发。

## 与数值协作

具体倍率与强度交给 `balance-design`。技能策划负责定义参数影响方向、允许范围和角色行为目标。

对于跨类型能力，应共同检查：

- Action Economy；
- Resource Economy；
- Target Value；
- Buff Uptime；
- Reliability；
- Secondary Gauge；
- Context Discount。

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

复杂技能建议补：

- Scaling Source；
- Rotation；
- Resource Net Flow；
- Buff Uptime；
- Hit Reliability；
- Breakpoint；
- Negative Synergy；
- Config/Code Evidence Status。

当前值未知时标 `unknown`。

## 技能设计反模式

- **Multiplier-only Design**：只调倍率不看循环与资源；
- **Hidden Scaling**：倍率对象不明确，文本/配置/代码不一致；
- **Duration Ambiguity**：回合持续语义不清；
- **Resource Bankruptcy**：单角色很强但团队资源循环崩溃；
- **Guaranteed-on-Paper CC**：忽略敌方抗性；
- **Upgrade Soup**：一次升星同时强化多个维度，无法判断价值来源；
- **Synergy Trap**：表面联动，实际触发条件互相冲突。
