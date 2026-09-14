---
name: economy-design
description: 负责游戏经济策划，包括资源 Sources/Sinks、库存、流速、价值锚点、兑换、价格、奖励投放、产销闭环、通胀、囤积、付费边界和长期资源健康度。用于签到、任务、商店、抽卡、体力、养成资源等经济问题。
---

# 游戏经济策划

经济设计的核心是控制资源在时间中的产生、持有、转换和消耗，而不是单独给某个奖励“看起来很多”。

## 经济清单

对每个资源记录：

| Resource | Source | Sink | Stock | Flow | Function | Gate | Conversion | Stage |
|---|---|---|---|---|---|---|---|---|

## 必查维度

### Sources
一次性、循环、活动、付费、补偿、挂机、关卡、任务等来源。

### Sinks
升级、抽卡、商店、合成、强化、刷新、解锁等消耗。

### Stock
玩家库存和上限。无上限资源要检查囤积与失效。

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

## 资源层级

避免资源功能高度重叠。每种资源应有清晰用途、价值和阶段意义。

若一个资源：

- 没有稳定 Sink；
- 只在前期有用；
- 能完全被另一资源替代；

需评估合并或新增合理用途，但不要为了“消耗资源”硬塞系统。

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

- 当前状态；
- 目标状态；
- 关键公式；
- 产出；
- 消耗；
- 日/周净流；
- 玩家阶段；
- 风险；
- 验证计划。

与 `balance-design`、`progression-design` 协作验证成长需求与奖励强度。
