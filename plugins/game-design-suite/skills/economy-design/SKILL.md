---
name: economy-design
description: 负责游戏经济策划，包括资源 Sources/Sinks、库存、流速、价值锚点、兑换、价格、奖励投放、产销闭环、通胀、囤积、付费边界和长期资源健康度。用于签到、任务、商店、抽卡、体力、养成资源等经济问题。
---

# 游戏经济策划

经济设计的核心是控制资源在时间中的产生、持有、转换和消耗，而不是单独给某个奖励“看起来很多”。

资源过剩、跨系统消耗、模拟经营资源、长期库存或新 Sink 设计时，优先读取 [Resource Role & Sink Legitimacy](references/resource-role-and-sink-legitimacy.md)。

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
