# Cross-Game Itemization Benchmark

本文件把 HSR / Genshin / Wuthering Waves 的公开装备结构抽象成可比较的设计维度。

## 1. 不比较绝对值，比较系统结构

跨游戏优先比较：

| 维度 | HSR Relic | Genshin Artifact / Weapon | Wuthering Waves Echo / Weapon |
|---|---|---|---|
| 强化上限 | Relic 常见 +15 | Artifact +20 / Weapon 90 | Echo +25 / Weapon 90 |
| 关键副词条事件 | 每3级 | 每4级 | 每5级调谐 |
| 主要事件数 | 约5次 | 约5次 | 约5次 |
| 固定主属性槽位 | 有 | 有 | Echo按Cost与双主属性规则 |
| 词条随机 | 有 | 有 | 有 |
| 套装门槛 | 2/4、位面2 | 2/4 | 2/5及其他新门槛 |
| 武器重复成长 | 非本表重点 | 精炼1~5 | 谐振1~5 |
| 特殊Build结构 | SPD/命中/击破 | 元素/充能/暴击等 | Cost Budget + Echo Skill |

表中是结构对照，不代表数值等价。

## 2. 关键跨游戏 Pattern

### Pattern A: Meaningful Upgrade Event Count

虽然 +15 / +20 / +25 表面不同，但副词条成长都可以形成约5次关键事件。

设计问题：

- 玩家到底感知“等级数”，还是“有意义事件数”？
- 强化20级却只有2次关键节点，会不会显得空；
- 强化10级却有10次随机，会不会过于频繁。

### Pattern B: Deterministic Core + Random Optimization

成熟装备系统常把：

- 基础成长；
- 主属性成长；

做成可预测，把：

- 副词条类型；
- Roll质量；
- 强化命中；

作为优化层随机。

如果核心生存/伤害也完全依赖随机，玩家可能无法建立稳定成长预期。

### Pattern C: Slot/Cost Gating Reduces Search Space

不同项目通过不同方式限制组合空间：

- HSR/Genshin：槽位主属性池；
- Wuthering Waves：Cost + 主属性池。

共同目的之一是避免所有属性在所有位置完全自由组合导致搜索空间爆炸。

### Pattern D: Weapon Power Is Multi-Part

武器不能只看 Base ATK。

至少拆：

```text
Base Stat
Secondary Stat
Passive
Refinement/Resonance
Character Fit
Rotation Reliability
```

同一满级白值不等于同一真实价值。

### Pattern E: Set Bonus as Build Commitment

套装不是免费额外收益。

它同时带来：

- 行为奖励；
- 槽位锁定；
- 掉落限制；
- Off-piece自由度损失；
- Build硬绑定风险。

评价套装时必须算机会成本。

## 3. Benchmark Scorecard

对一个项目建立以下 0~5 级观察量，不直接打“好坏分”。

### Determinism
核心属性有多可预测？

### RNG Depth
主属性、词条、Roll、强化等随机层有几层？

### Slot Constraint
槽位/Cost对属性组合限制多强？

### Build Expression
装备是否真正改变Build或只是叠面板？

### Replacement Friction
换装是否因强化、套装、沉没成本而困难？

### Signature Pressure
专武/专属套装是否显著高于替代品？

### Set Pressure
套装门槛对自由搭配限制多强？

### Tail Variance
极品与普通可用装备差距多大？

### Recovery / Salvage
坏掉落是否有回收价值？

### Progression Clarity
玩家能否理解“下一步为什么变强”？

分数只用于对比设计倾向，不是行业标准。

## 4. Project Distance Matrix

输出项目与参考系的差异：

```text
Dimension | Project | HSR | Genshin | Wuthering Waves | Risk/Intent
```

示例维度：

- Max enhancement；
- Upgrade event count；
- Initial substat count；
- Mainstat pool width；
- Roll tier count；
- Set threshold；
- Random layers；
- Effective upgrade rate；
- Signature increment；
- Replacement loss；
- Recovery rate。

“距离大”不是问题，必须解释是否符合项目目标。

## 5. 什么时候应该借鉴，什么时候不该

### 更适合借鉴结构

- 新项目尚未确定装备随机深度；
- 需要检查强化节奏是否过空/过密；
- 需要建立词条池和槽位职责；
- 需要设计武器基础/副属性预算家族；
- 需要判断套装门槛是否压迫Build。

### 不适合直接借鉴数值

- 战斗公式不同；
- 角色基础属性规模不同；
- 游戏时长/刷取频率不同；
- 单人/多人环境不同；
- 付费与获取方式不同；
- 装备在总战力中的占比不同；
- 当前项目已经存在更高层的Roguelite/卡牌随机。

## 6. Transfer Gate

任何外部设计准备迁移时，必须回答：

1. 它在原游戏解决什么问题？
2. 当前项目是否有同样的问题？
3. 当前项目有哪些不同约束？
4. 迁移的是结构、节奏还是数值？
5. 如果不采用这个设计，会发生什么？
6. 怎样通过公式/模拟/Playtest验证？

无法回答时，不应进入正式配置。
