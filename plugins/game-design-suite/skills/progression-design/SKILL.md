---
name: progression-design
description: 负责角色、账户、装备、技能、星级、突破、技能树、解锁和长期成长设计。用于成长路径、等级曲线、技能节点、星级收益、解锁节奏、追赶机制、卡点、成长上限和资源需求等问题。
---

# 成长策划

成长不是单纯“数字变大”，需要明确玩家获得的是强度、能力、选择、内容权限还是收藏完成度。

涉及角色基础属性、等级/突破采样、装备基础值与百分比属性分层时，与 `balance-design` 的 HSR-style theorycrafting reference 协作，只学习结构，不照抄外部游戏成长率。

涉及技能等级、技能树、关键被动、升星/命座/影画式里程碑时，优先读取 [Skill Progression & Upgrade Topology](../skill-design/references/skill-progression-and-upgrade-topology.md)。

## Result-Level Professional Context

每一个独立成长节点、成本结构、解锁节奏、成长曲线或追赶机制结论前，按 `../game-design/references/professional-context-header.md` 输出一次结果级 Header。

成长结构本身由 `progression-design` 主责；资源长期健康度转由 `economy-design` 主责；具体 Power Delta、倍率、曲线点值是否合理可由 `balance-design` 主责；技能节点机制含义可由 `skill-design` 主责。相邻结果即使专业组合相同，也重复显示 Header。

## 成长类型

区分：

- Power Progression
- Capability Progression
- Content Progression
- Collection Progression
- System Progression
- Player Mastery

## 成长对象

对每个对象明确：

- 起点；
- 上限；
- 阶段节点；
- 升级条件；
- 成本；
- 收益；
- 解锁；
- 失败/回退；
- 重置；
- 追赶；
- 与内容难度关系。

## Base / Percent / Flat 分层

如果项目有角色基础属性、武器/装备基础属性、百分比加成、固定加成，必须先明确层级。

推荐显式定义类似：

`Total = Base × (1 + PercentBonus) + FlatBonus`

并说明 Base 来自哪些来源。

### 设计价值

- 等级/突破负责基础成长；
- 装备百分比放大基础值；
- 固定值提供低阶段稳定收益；
- 角色差异可以通过初始 Base 与成长系数体现；
- 不需要所有属性都随等级增长。

速度、能量上限、攻击间隔、嘲讽权重等可作为固定/半固定维度，除非项目有明确成长需求。

## Progression Cost Semantics

成长成本必须先回答“为什么这个成长会消耗这个资源”。

不得因为某资源库存高、缺少 Sink，或某成长系统当前没有消耗，就自动把资源加入升级成本。

每个成长成本至少通过：

1. **Role Fit**：资源职责与成长对象一致；
2. **Player Model Fit**：玩家能理解这项投入为什么发生；
3. **System Fit**：属于该成长系统或合理相邻系统；
4. **Decision Value**：会产生资源分配选择，而不是纯税；
5. **Pacing Fit**：不会破坏已有成长节奏；
6. **Switching Cost Check**：不会让新角色/新 Build 切换成本失控。

若成本只是为了回收另一个系统的资源，默认标记为 `candidate-risky`，需要 `economy-design + game-production` 共同评审。

## 禁止 Progression Hostage

不要为了提高系统 A 的参与度，把系统 B 的核心成长强行绑到 A 的资源或玩法上。

例如：基地经营资源富余，不自动意味着英雄升级应该直接吃基地资源。

更优先考虑：

- 基地提供训练能力/效率；
- 解锁制造/培养设施；
- 提供可选的加速或额外产出；
- 通过能力解锁连接系统；

而不是直接将跨系统资源改成强制升级税。

## 等级成长与突破跳变

成熟角色成长通常同时包含：

- 平滑的每级成长；
- 明确的突破节点；
- 突破前/后的离散差值；
- 技能/系统解锁；
- 成本跳变。

不要把所有成长压力都塞进“每级 +X%”，也不要让突破只是“多交一次材料”。

### 采样要求

正式成长曲线至少采样：

- Lv1；
- 每个突破前；
- 每个突破后；
- 中期代表等级；
- 满级。

每个采样点记录：

- Base Stats；
- Power Delta；
- Cost Delta；
- Content Target；
- 解锁；
- Time-to-Upgrade；
- 玩家可感知收益。

## Skill Tree / 技能树拓扑

技能树要同时承担“稳定成长”和“关键里程碑”，不能只是把线性升级画成树。

建议区分：

- **Skill Rank**：倍率、护盾、治疗、概率等稳定纵向成长；
- **Major Passive**：补循环、条件、可靠性、资源关系；
- **Minor Stat Node**：提供 Build 支撑；
- **Milestone Node**：关键等级/星级改变技能交互；
- **Capstone**：完成角色玩法身份或突破上限。

### 核心身份应尽早成立

角色的主循环不应被拆到后期才完整。

早期：让玩家看懂角色是谁、怎么玩。

中期：提高可靠性、资源效率、Build 空间。

后期：扩大上限、改变交互、提供更高执行/组合空间。

如果“没点到某高阶节点前角色像残缺品”，标记 `Identity Locked Late / Problem-Sell-Solution` 风险。

## Upgrade Value Classes

关键节点至少标记它主要改善什么：

- Vertical Power；
- Reliability；
- Rotation/Cycle；
- Resource Economy；
- Target Coverage；
- Survivability；
- Team Synergy；
- Execution/QoL；
- Mechanic Transformation。

不要把不同升级全部压成“等效伤害提升”后结束。

## Milestone Cohesion / 节点主题一致性

同一角色的成长节点最好围绕它的核心循环逐步深化。

例如反击角色可以按：

`循环成立 -> 触发更可靠 -> 反击转资源 -> 场景覆盖扩大 -> 高阶突破触发限制`

而不是：

`+攻击 -> +生命 -> 随机控制 -> +暴击 -> 再+攻击`

后者会导致成长没有玩法方向。

## Window Fit / 实际兑现

技能/星级节点增加：

- 额外攻击次数；
- 额外行动；
- 状态持续；
- Burst Length；

都必须与真实战斗窗口检查。

纸面增加 3 段攻击，但只能有 1 段落在敌方失衡/易伤期，不应把 3 段全部当成实战提升。

与 `skill-design + combat-design + balance-design` 联合验证。

## 节奏

检查：

- 首次升级多久；
- 前期升级频率；
- 中期停滞；
- 后期长线；
- 关键里程碑；
- 卡点持续时间；
- 成长目标可见性；
- 下一步目标是否清楚。

## 三曲线联动

成长设计至少联动检查：

- **Power Curve**：玩家强度如何增长；
- **Cost Curve**：成长成本如何增长；
- **Content Curve**：内容难度/解锁如何增长。

必要时观察：

- `Player Power / Enemy Power`；
- Time-to-Upgrade；
- 单节点 Power Delta；
- 单位时间成长收益；
- 同阶段横向角色差距。

避免成本和强度脱节。

## Benchmark Panel / 标准面板

做角色横向比较时必须建立统一面板规则，例如：

- 同等级；
- 同突破；
- 同技能等级；
- 同装备品质；
- 固定有效词条预算；
- 固定星级/命座/升星条件；
- 固定队伍与敌人环境。

可以准备多个面板：

- New Player；
- Midgame；
- Endgame Standard；
- High Investment；
- Extreme Ceiling。

不要拿“一个角色毕业装”和“另一个角色普通装”比较基础强度。

## 节点收益

突破、星级等重要节点必须有可感知价值。检查：

- 单节点收益是否过小；
- 某节点是否异常爆发；
- 技能解锁与数值成长是否冲突；
- 是否存在“投入大量资源但体验不变”；
- 节点价值是否与成本同步；
- 是否出现“低级频繁交税，高级才有真正收益”的坏节奏；
- 是否跨过 Action / Energy / Hit / Stack Breakpoint；
- 是否只是修复基础角色人为制造的资源/触发缺陷。

## 成长成本

与 `economy-design` 协作，检查：

- 资源需求；
- 资源 Role；
- 日/周获取；
- 多角色并养；
- 单核集中投入；
- 追赶成本；
- 新角色切换成本；
- 资源沉没；
- 是否产生 Mandatory Tax；
- 是否只是为了消耗库存。

## 强度曲线

与 `balance-design` 协作验证：

- 属性曲线；
- 技能等级；
- 星级；
- 装备；
- 外部 Buff；
- 行动次数；
- 资源循环；

是否叠加成失控增长。

## 常见反模式

- **Progression Hostage**：其他系统资源被强制塞进成长；
- **Treadmill**：数字涨但能力/决策不变；
- **Tax Ladder**：等级越高只是交更多资源，没有新价值；
- **Switching Punishment**：新角色/新 Build 切换成本过高；
- **Node Dilution**：关键节点收益被切碎到无感；
- **Resource Pile-on**：为了体现复杂度不断叠加升级材料；
- **All-Stats Inflation**：所有属性一起涨，导致角色定位与系统阈值失控；
- **Benchmark Drift**：不同角色用不同养成标准比较强度；
- **Breakpoint Accident**：某节点无意跨过关键速度/能量/控制阈值造成异常爆发；
- **Linear Tree Cosplay**：树形 UI，实际全是线性加数；
- **Identity Locked Late**：核心玩法太晚才完整；
- **Problem-Sell-Solution**：高阶节点只是修基础缺陷；
- **Upgrade Soup**：节点价值类型混乱；
- **Window Spill**：纸面升级无法在实际窗口兑现；
- **Dead Rank**：升级了几乎不用的技能。

发现这些问题时，不通过再加材料或再加层级解决。

## 输出

对正式成长方案至少给：

| 阶段/节点 | 条件 | 成本 | Cost Role | Base/Power Delta | 升级类型 | 解锁/交互 | Benchmark | 玩家目标 | 风险 | 验证 |
|---|---|---|---|---|---|---|---|---|---|---|

未知数值标 `TBD/candidate`，不虚构。
