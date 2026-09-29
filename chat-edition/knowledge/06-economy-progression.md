# Game Design Suite Chat Edition — Economy & Progression

> Purpose: project knowledge for ordinary Chat mode. This file is NOT a Skill and does not depend on Skill/Plugin runtime.
> Use it for resource loops, sources/sinks, pricing, reward cadence, progression curves, gates, upgrades, replacement cadence, and long-term pacing.

## Usage
- Start from the whole production/consumption loop, not one sink in isolation.
- Preserve resource meaning; do not create sinks merely to consume surplus.
- Treat user-fixed economy rules as constraints unless reopened.
- Do not claim a Skill was invoked.


---

# Source Module: gds-economy-design

# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# 游戏经济策划

经济设计的核心是控制资源在时间中的产生、持有、转换和消耗，而不是单独给某个奖励“看起来很多”。

资源过剩、跨系统消耗、模拟经营资源、长期库存或新 Sink 设计时，优先读取 [Resource Role & Sink Legitimacy](resource-role-and-sink-legitimacy.md)。

## Result-Level Professional Context

每一个独立经济根因、资源处理方向、奖励投放结论或 Sink/Source 调整建议前，按 `../game-design/references/professional-context-header.md` 输出一次结果级 Header。

经济问题本身由 `economy-design` 主责；如果当前结果切换到“英雄升级成本结构”，应让 `progression-design` 主责；如果切换到“具体倍率/价格点值是否平衡”，`balance-design` 可主责；如果切换到“玩法循环为什么需要这个资源”，`game-production` 可主责。

相邻结果即使专业组合相同，也重复显示 Header，不因前文已有而省略。

## 先定义 Resource Role

在谈 Source/Sink 前，先明确每种资源为什么存在。

至少记录：

| Resource | Fantasy Role | System Role | Primary Loop | Primary Sources | Primary Sinks | Secondary Sinks | Stock Purpose | Scarcity Intent | Conversion | Lifecycle |
|---|---|---|---|---|---|---|---|---|---|---|

如果资源的系统职责尚未明确，不允许仅因为“库存很多”就给它寻找新消费。

## No Sink For Sink's Sake

**禁止为了消耗而消耗。**

“资源后期很多”“某资源暂时没有出口”“某系统升级没有消耗”都只是症状，不自动推出“新增 Sink”。

新增 Sink 前必须通过以下合法性检查：

1. **Fantasy Fit**：玩家能否理解为什么在这里消耗这个资源；
2. **System Fit**：消费是否属于该资源的主循环或合理相邻循环；
3. **Decision Value**：是否产生真实取舍，而不是强制税；
4. **Timing Fit**：该阶段引入该成本是否合理；
5. **Economy Need**：问题究竟是 Sink 不足，还是 Source 过高、内容生命周期结束、库存上限、兑换结构或产出节奏有问题；
6. **Better Alternative**：是否存在更自然的 Sink、Source 调整、转换、扩展内容或允许健康盈余的方案。

前 3 项明显不成立时，默认拒绝新增该 Sink。

## 健康盈余不是错误

并非每种资源都必须长期维持“产出=消耗”。

允许存在：

- 安全库存；
- 阶段性富余；
- 为未来内容预留的 Stock；
- 表达经营成功的财富积累；
- 低价值基础资源的自然过剩。

只有当库存导致选择失效、奖励失去意义、系统参与度崩溃、价格体系失真或长期内容无法维持时，才需要处理。

## 经济清单

对每个资源记录：

| Resource | Source | Sink | Stock | Flow | Function | Gate | Conversion | Stage |
|---|---|---|---|---|---|---|---|---|

## 诊断顺序

资源过剩或短缺时按以下顺序诊断：

1. **Role**：资源职责是否清楚；
2. **Source**：产出是否过高/过低；
3. **Stock**：库存目标和上限是否合理；
4. **Sink**：现有消费是否不足或时序不对；
5. **Conversion**：是否需要兑换/制造/转化；
6. **Lifecycle**：是否是该系统中后期内容断层；
7. **Cross-system**：是否需要合理联动，而不是强行跨系统收费；
8. **New Sink**：只有前面检查后仍有必要才新增。

不要直接从第 8 步开始。

## 必查维度

### Sources
一次性、循环、活动、付费、补偿、挂机、关卡、任务等来源。

### Sinks
升级、抽卡、商店、合成、强化、刷新、解锁等消耗。

### Stock
玩家库存和上限。无上限资源要检查囤积与失效，但不要默认把高库存视为错误。

### Flow
按 Session / 日 / 周 / 版本估算流入与流出。

### Value Anchor
确定资源相对价值，不同货币兑换必须有锚点。

### Gates
资源是否控制进度；硬门槛还是软门槛。

### Recovery
资源耗尽、连续失败后是否可恢复。

### Inflation
中后期是否大量积压、奖励失去意义。

### Dominant Farming
是否存在明显最优刷法，导致其他内容失效。

## 跨系统联动边界

**跨系统联动不等于跨系统互相收费。**

优先通过以下方式联动：

- 解锁能力；
- 提高效率；
- 改变选项；
- 提供制造能力；
- 改变生产结构；
- 提供风险/收益权衡；
- 改变内容访问权。

只有当资源语义和系统逻辑都成立时，才允许直接作为另一个系统的升级成本。

例如模拟经营资源属于基地运营时，英雄养成更自然的联动通常是“基地设施提供训练/制造/恢复能力”，而不是“英雄每升一级直接扣水、电、食物”。

## 模拟经营资源特别检查

模拟经营资源常用于：

- 建筑建设/升级；
- 设施运行/维护；
- 生产与制造；
- 人员/驻扎；
- 科技与扩张；
- 仓储与物流；
- 派遣/事件；
- 转换与加工。

若中后期资源失去用途，先检查是否是经营内容生命周期断层，不要优先把它们塞进英雄升级、战斗强化或其他不相干养成。

## 奖励设计

单个奖励不能孤立判断。调整签到、任务、章节、活动等奖励时至少检查：

- 同期其他产出；
- 关键消费；
- 抽卡/商店价格；
- 成长需求；
- 新手阶段库存；
- 中后期库存；
- 付费价值（若存在）；
- 奖励之间的相对吸引力。

## 产销模型

根据项目需要计算：

- Daily Net Flow；
- Weekly Net Flow；
- Time-to-Purchase；
- Time-to-Upgrade；
- Resource Coverage Days；
- Sink Coverage；
- Value per Session；
- Expected Currency per Chapter；
- Safety Buffer。

## 常见反模式

- **Sink for Sink's Sake**：只因为库存多就新增消费；
- **Mandatory Tax**：玩家没有选择的持续强制扣费；
- **Resource Everywhere**：一种资源被所有系统消费，职责失焦；
- **Currency Soup**：多种资源功能高度重叠；
- **Progression Hostage**：为了提高系统参与度，强行把另一个系统的核心成长锁进来；
- **Production Inflation Patch**：产出过高却不调整 Source，只不断添加 Sink；
- **Late-game Dead Currency**：后期资源完全失去选择价值；
- **Forced Coupling**：用收费代替真正的系统联动。

发现反模式时先定位根因，不自动新增功能。

## 资源层级

避免资源功能高度重叠。每种资源应有清晰用途、价值和阶段意义。

若一个资源：

- 没有稳定 Sink；
- 只在前期有用；
- 能完全被另一资源替代；

需评估其 Role、生命周期、产出和自然用途。可以合并、转换、减少 Source、扩展原系统内容或允许阶段性富余；不要为了“消耗资源”硬塞到无关系统。

## 商业化边界

若项目涉及付费，明确：

- 玩家购买的价值；
- 免费与付费节奏；
- Currency Conversion；
- Fairness Boundary；
- 不售卖项（如项目需要）。

不自行设计未确认商业模式。

## 输出

正式经济建议应给：

- Resource Role；
- 当前状态；
- 目标状态；
- 根因判断；
- 关键公式；
- 产出；
- 消耗；
- 日/周净流；
- 玩家阶段；
- Sink Legitimacy；
- 风险；
- 验证计划。

与 `balance-design`、`progression-design` 协作验证成长需求与奖励强度。


---

# Source Module: gds-progression-design

# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

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
