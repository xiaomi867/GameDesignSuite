---
name: skill-design
description: 负责角色/英雄技能设计、诊断和改造，包括角色循环、普攻、主动、被动、大招、Target、触发、资源、状态机、Buff/Debuff、持续、叠加、技能等级、升星影响、技能树、队伍协同和构筑关系。已有项目默认不改变用户要求保持的技能机制。
---

# 技能策划

目标不是“把技能栏填满”，而是让角色拥有清晰的玩法身份、资源循环、触发逻辑、团队职责和可成长空间。

复杂角色、新英雄、角色重做、技能树、升星/命座/影画、队伍协同时按需读取：

- 角色循环、状态机、资源图、Team Hook、Field-Time、Trigger Reliability -> [Hero Kit Architecture](references/hero-kit-architecture.md)
- 技能等级、技能树、被动节点、升星/里程碑升级 -> [Skill Progression & Upgrade Topology](references/skill-progression-and-upgrade-topology.md)
- 角色池定位、横向差异、团队槽位和角色生态 -> [Hero Roster Architecture](../game-production/references/hero-roster-architecture.md)

## Result-Level Professional Context

每一个独立英雄/技能机制、Target、触发、状态机、Buff、升级或构筑结论前，按 `../game-design/references/professional-context-header.md` 输出一次结果级 Header。

技能机制本身由 `skill-design` 主责；具体倍率/强度转由 `balance-design` 主责；真实表字段不一致转由 `config-audit` 主责；代码语义转由 `code-verification` 主责；团队底层战斗规则可由 `combat-design` 主责。相邻结果即使专业组合相同，也重复显示 Header。

## 0. 机制保护

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

发现配置/实现错误时区分：

- **Fix Bug**：让实际行为回到已确认设计；
- **Change Mechanic**：改变原设计规则。

不要把修错和改机制混为一谈。

## 1. 先写角色循环，再写技能

新角色/重做角色先用一句话描述：

> 角色通过【生成条件/资源】进入【关键状态】，在【收益窗口】中用【核心动作】兑现收益，再通过【恢复/重置】重新进入循环。

再确认：

- Core Fantasy；
- Primary Role；
- Phase Ownership；
- Generator；
- Setup；
- Consumer/Payoff；
- Recovery；
- Team Hook；
- Failure Case。

如果角色只能描述成“普攻伤害、技能伤害、大招伤害、被动加伤”，优先判定为 Kit Identity 不足，而不是继续加倍率。

## 2. Skill Grammar / 技能语法

每个技能尽量拆成：

`Input/Trigger -> Acquire Target -> Cost -> Cast -> Resolve -> Damage/Heal -> Buff/Debuff -> Secondary Trigger -> Resource/CD Update`

这样可以明确：

- Target 何时确定；
- Cost 何时扣；
- Damage 与 Buff 的先后；
- Secondary Effect 是否会重复触发；
- 死亡/击杀/破盾等事件在何时判定；
- Buff 读取施法前还是施法后属性。

每个技能还建议标记职能：

- Generator；
- Setup；
- Converter；
- Consumer；
- Payoff；
- Amplifier；
- Safety；
- Mobility/Position；
- Finisher。

技能槽位多不代表每个槽位都必须承担同等数值价值或使用频率。

## 3. State Machine / 状态机

复杂角色必须显式写状态，而不是把状态藏在描述里。

例如：

`Normal -> Setup -> Empowered -> Payoff -> Recovery`

每个状态明确：

- 进入条件；
- 退出条件；
- Duration；
- 可否刷新/覆盖；
- 技能是否替换；
- 资源规则是否变化；
- Target/Trigger 是否变化；
- 被控制/死亡/换人时如何处理。

强化状态如果没有清晰结束与 Recovery，会很容易退化成“永久 Burst”。

## 4. Resource Graph / 资源图

角色资源至少画成：

`Source -> Storage -> Converter -> Sink -> Reset`

资源可以是：

- 能量/怒气；
- 层数；
- 弹药；
- 标记；
- 生命/护盾；
- 敌方状态；
- 队友行动；
- 受击次数；
- Break/异常状态。

必须检查：

- 生成速度；
- 上限；
- 溢出；
- 消费时机；
- 是否有垃圾资源；
- 是否有 Source 无 Sink 或 Sink 无 Source；
- 玩家是否真的能决定何时消费。

## 5. 技能检查清单

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
- State Transition
- Field/Action Time
- Team Hook
- Payoff Window
- Edge Cases

## 6. Scaling Source / 倍率基准属性

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
- 同一属性同时无限提高输出、生存、资源时是否形成 Double/Triple Scaling；
- 目标生命倍率是否对 Boss 有上限或特殊规则。

## 7. Skill Rotation / 技能循环

技能不能只单独看倍率，应放进完整 Rotation：

- 普攻频率；
- 技能频率；
- 大招周期；
- 被动触发频率；
- 追击/反击次数；
- Buff 覆盖；
- 资源净流；
- 强化状态时长；
- Setup / Payoff 占用；
- 是否因为速度/额外行动改变循环。

### 角色资源标签

可以根据团队共享资源把角色标记为：

- Resource Positive；
- Resource Neutral；
- Resource Negative；
- Burst Consumer；
- Emergency Consumer。

这会直接影响队伍搭配与角色真实价值。

## 8. Field-Time / Action-Time Budget

团队角色不能只看个人技能表。

检查：

- On-field Time；
- Setup Time；
- Payoff Time；
- Swap/Action Cost；
- 公共资源占用；
- 是否抢队友 Burst Window；
- 动画/连段是否把纸面收益拖出真实窗口。

“多一段攻击”不自动等于整段倍率都能兑现。

## 9. Buff/Debuff Duration Semantics

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

## 10. Trigger Reliability / 触发可靠性

反击、受击回能、队友行动触发、击杀触发、Break 触发等不能只看“能触发”。

必须检查：

- 事件频率；
- 是否依赖敌方 AI；
- 是否依赖指定队友动作；
- 每回合/CD 限制；
- 单体/群体差异；
- 目标死亡是否吞触发；
- Boss 无敌/长演出是否饿死循环；
- 是否有手动/保底替代触发。

高收益可以对应低可靠性，但这必须是有意识的 Risk/Reward，而不是事故。

## 11. 状态可靠性

Debuff/控制类技能不能只看 Base Chance。

应协作 `balance-design` 检查：

- 普通怪实际命中率；
- Elite；
- Boss；
- Specific Resist；
- Immunity；
- 多段判定；
- 是否存在 100% 文本但实际不稳定的情况。

## 12. Team Hook / 队伍关系

角色与队伍的关系优先通过：

- 创建状态；
- 消费队友状态；
- 放大某类行为；
- 提供行动/资源；
- 保护窗口；
- 改变敌方状态；
- 触发追加/协同行动。

属性/阵营/职业条件可以作为 Soft Synergy，但不要默认做成 Hard Pair Lock。

如果角色没有唯一队友就无法完成基础循环，标记 `Pair Lock / Team Tax` 风险。

## 13. 技能等级、技能树与升星

升星/升级必须回答：

- 影响哪个技能；
- 改哪个维度；
- 单次收益；
- 累积收益；
- 是否改变机制；
- 是否出现关键断层；
- 是否符合品质/稀有度定位；
- 是否跨过 Rotation / Energy / Hit / Stack Breakpoint；
- 是否改善 Reliability / Cycle / Team Hook；
- 是否只是修复基础角色的人为缺陷。

建议把成长分成：

- Skill Rank：稳定纵向数值；
- Major Passive：循环、条件、可靠性；
- Minor Stat：Build 支撑；
- Milestone：关键玩法变化；
- Capstone：突破上限或完成角色身份。

避免每次升星同时提升过多技能，除非项目规则明确如此。

### 节点价值

升级不应该只是把所有倍率同步 +X%。可以区分：

- 稳定数值成长；
- 条件改善；
- 覆盖率改善；
- 资源效率；
- Target Coverage；
- Team Synergy；
- Execution/QoL；
- Build 联动；
- 关键 Breakpoint；
- Mechanic Transformation。

但用户明确要求“不改机制”时，只能在允许的 Tunables 内实现，不通过新增行为制造假“成长”。

## 14. 构筑价值

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
- Target 改变让被动无法稳定触发；
- 长连段溢出敌方失衡/易伤窗口。

## 15. 与数值协作

具体倍率与强度交给 `balance-design`。技能策划负责定义参数影响方向、允许范围和角色行为目标。

对于跨类型能力，应共同检查：

- Action Economy；
- Resource Economy；
- Target Value；
- Buff Uptime；
- Reliability；
- Secondary Gauge；
- Context Discount；
- Window Realization。

## 16. 与战斗/关卡协作

复杂角色必须与 `combat-design + level-design` 检查：

- 角色依赖的敌人行为是否稳定存在；
- Counter/DoT/Break/状态体系有没有内容承载；
- Burst Window 是否被 Boss 转场/无敌频繁偷走；
- 单体/群体内容是否都存在；
- 教学关是否教角色循环，而不是逐个按钮。

## 17. 与配置协作

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

## 18. 输出要求

用户要求落表时不能只写“加强/削弱”。至少给：

| 表/对象 | Key/ID | 字段 | 当前值 | 改后值 | 影响 | 理由 | 验证 |
|---|---|---|---|---|---|---|---|

新英雄/复杂技能建议补：

- Core Loop；
- State Machine；
- Resource Graph；
- Scaling Source；
- Rotation；
- Field/Action Time；
- Resource Net Flow；
- Buff Uptime；
- Trigger/Hit Reliability；
- Breakpoint；
- Team Hook；
- Failure Case；
- Negative Synergy；
- Config/Code Evidence Status。

当前值未知时标 `unknown`。

## 19. 技能设计反模式

- **Multiplier-only Design**：只调倍率不看循环与资源；
- **Button Zoo**：技能很多但没有共同循环；
- **Passive Soup**：大量规则不改变决策；
- **Resource Orphan**：资源存在但没有有意义的消费；
- **Hidden Scaling**：倍率对象不明确，文本/配置/代码不一致；
- **Duration Ambiguity**：回合持续语义不清；
- **Resource Bankruptcy**：单角色很强但团队资源循环崩溃；
- **Guaranteed-on-Paper CC**：忽略敌方抗性；
- **Trigger Lottery/Starvation**：核心收益依赖不可控触发或敌人不配合；
- **Pair Lock**：必须绑唯一队友；
- **Stat Split Tax**：核心属性互不协同；
- **Window Spill**：升级/连段收益溢出真实窗口；
- **Overloaded Skill**：单技能承担太多职能；
- **Dead Slot/Dead Rank**：技能/技能等级长期没有使用价值；
- **Upgrade Soup**：一次升星同时强化多个维度，无法判断价值来源；
- **Problem-Sell-Solution**：先制造基础缺陷，再用高阶节点修复；
- **Synergy Trap**：表面联动，实际触发条件互相冲突。
