# Game Design Suite Chat Edition — Itemization Deep Reference

> Deep reference bundle for Chat Edition. These materials preserve detailed reasoning patterns from the canonical Game Design Suite. External commercial-game values remain benchmark/reference evidence, never current-project truth.


---

## Canonical source: references/reference-extraction-and-normalization.md

# Reference Extraction & Normalization

本文件定义如何从公开装备图鉴、Wiki、数据库和游戏内截图中抽取可比较的 Itemization 数据。

## 1. Snapshot Schema

每个参考实体至少记录：

```text
Game
System            # Weapon / Relic / Artifact / Echo / Set
EntityName
Rarity
Slot / Type
Level
MaxLevel
AscensionStage
RefinementOrResonance
BaseStat
SecondaryStat
MainStat
Substats
Passive / Set Effect
UpgradeCadence
RandomRules
SourceURL
SourceDate
GameVersion
EvidenceType
```

不要把页面上的展示顺序当成系统字段顺序。

## 2. Slider / Level Curve Capture

存在等级进度条时，不只截满级。

推荐采样：

- 起始等级；
- 每个突破前；
- 每个突破后；
- 25% / 50% / 75%进度；
- 满级；
- 强化触发词条的节点；
- 精炼/谐振每一级。

输出：

```text
Level | Value | Delta | Delta% | NormalizedToMax | BreakpointFlag
```

### 基础曲线

`NormalizedToMax = Value(level) / Value(max)`

用于比较不同游戏的曲线形状，不比较绝对数值。

### 局部增量

`Delta(level) = Value(level) - Value(previous level)`

用于识别：

- 线性；
- 分段线性；
- 突破跳变；
- 后置成长；
- 前置成长。

## 3. Weapon Budget Snapshot

武器至少拆：

```text
BaseStat Curve
SecondaryStat Curve
Passive Rank 1~N
Ascension/Breakthrough
```

不要只比较白值。

可计算：

`BaseToSecondaryIndex = NormalizedBaseStat / NormalizedSecondaryStat`

该指标只能用于同一游戏内部或经过项目内价值换算后的跨游戏比较。

## 4. Relic / Artifact / Echo Snapshot

至少拆：

```text
Slot/Cost
Main Stat Pool
Main Stat Growth
Initial Substat Count
Substat Pool
Substat Roll Tiers
Upgrade Roll Cadence
Duplicate/Exclusion Rules
Set/Sonata Threshold
Salvage/Reuse Rules
```

特别注意：

- 主属性池可能按槽位/Cost限制；
- 副词条可能与主属性互斥，也可能允许同类；
- 初始副词条数量可能按品质不同；
- 强化节点可能是新增词条或升级旧词条；
- Roll档可能离散但非等概率。

## 5. Cross-Game Normalization

跨游戏禁止直接比较绝对属性。

优先比较：

### Curve Shape
`V(level)/V(max)`

### Random Layer Count
主属性随机、词条类型随机、Roll档随机、强化命中随机分别计一层。

### Upgrade Event Density
`MeaningfulUpgradeEvents / MaxEnhancementLevel`

### Useful Affix Ratio
`UsefulAffixesForBuild / EligibleAffixes`

### Set Pressure
`ExpectedSetValue / ExpectedTotalBuildValue`

### Signature Pressure
`SignatureIncrement / BaselineAlternativeValue`

只有当前项目建立了统一 Power Budget 后，才可以进一步比较强度。

## 6. Evidence Labels

推荐使用现有证据状态：

- 页面直接值：`verified-data`（仅表示该外部来源事实）；
- 多个事实归纳出的模式：`supported-inference`；
- 拟迁移到项目：`candidate`；
- 无法读取页面：`externally-blocked`。

不要把外部 `verified-data` 写成当前项目 `verified-*`。

## 7. Conflict Handling

两个来源冲突时记录：

```text
Field
Source A
Source B
Version / Date
Possible Cause
Resolution Status
```

优先排查：

- 版本不同；
- 品质不同；
- Lv0 vs Lv1；
- 突破前后；
- 显示取整；
- 社区样本估计 vs 数据表；
- 同名不同实体。

冲突未解决前不合并为一个“正确值”。



---

## Canonical source: references/hsr-relic-patterns.md

# Honkai: Star Rail Relic Patterns

用途：记录《崩坏：星穹铁道》遗器系统中对通用 Itemization 设计有参考价值的公开结构。这里只保存**参考事实与可迁移模式**，不把具体数值当成项目标准。

## 1. 公开可验证结构

公开资料与图鉴支持以下模式：

- 遗器存在明确槽位，不同槽位可出现的主属性不同；
- 头部主属性固定为生命，手部主属性固定为攻击；
- 躯干、脚部、位面球、连结绳承担更高的主属性选择空间；
- 5★遗器最高强化为 +15；
- 5★遗器主属性随强化等级固定成长；
- 5★遗器初始副词条通常为 3~4 条；
- 每 +3 级发生一次副词条新增或强化事件；
- 5★副词条每次 Roll 常见为 Low / Mid / High 三档离散值；
- 副词条不能重复，同名主属性与副属性存在排除规则；
- 功能性属性不仅有攻击/生命/防御，还包括速度、暴击、暴伤、效果命中、效果抵抗、击破等。

公开参考中，5★主属性满级常见示例包括：

- HP% / ATK%：43.2%；
- DEF%：54%；
- 属性伤害提高：约38.88%；
- CRIT Rate：32.4%；
- CRIT DMG / Break Effect：64.8%。

这些数字只用于说明**同一系统内的属性预算关系和离散梯度**，禁止复制到其他项目。

## 2. 可迁移模式

### Fixed Slot + Choice Slot

固定主属性槽位减少早期随机压力；可选主属性槽位负责 Build 分化。

可迁移问题：

- 项目是否需要部分槽位“稳定供给基础属性”；
- Build 自由度是否集中在少数槽位更易理解；
- 如果所有槽位都完全随机，玩家认知和毕业成本是否过高。

### Upgrade Event Cadence

+15 与每3级一次副词条事件形成 5 次关键升级节点。

可迁移的是：

> 强化等级总长与“有意义升级事件”的密度应该匹配。

不可迁移的是：

> 所有游戏都应该 +15、每3级Roll。

### Three-Tier Roll

三档离散 Roll 提供随机质量差异，同时保持数值可读性。

验证问题：

- Roll档太多是否导致玩家难以判断好坏；
- Roll档太少是否使随机成长缺乏追求；
- 各档概率是否等权；
- 极端高Roll组合是否形成尾部爆炸。

### Functional Stat Slots

速度、命中、抵抗、击破等属性进入主/副词条后，可以把装备从“纯面板增长”变成“循环/可靠性/机制达标工具”。

项目迁移前必须先确认这些功能属性在当前战斗公式中存在真实价值。

## 3. 设计风险

- **Breakpoint Dominance**：速度等属性跨过行动阈值后价值非线性；
- **Crit Convergence**：大量输出角色同时追暴击/暴伤，词条池看似丰富但有效选择趋同；
- **Dead Flat Stat**：固定数值词条在后期可能明显弱于百分比；
- **Set Pressure**：套装与主词条同时限制时，真实有效掉落率会快速下降；
- **Tail Roll Variance**：高Roll集中到关键词条时，成品差距可能远大于“同主词条同套装”。

## 4. Benchmark 使用

对项目遗器/装备做对标时，优先比较：

```text
槽位固定度
主属性池宽度
初始副词条数
强化事件次数
副词条Roll档数
功能属性占比
套装门槛
有效掉落漏斗
```

不要直接比较“43.2% vs 项目40%”。

## 5. 主要来源

- https://sr.appfeng.com/relic
- https://honkai-star-rail.fandom.com/wiki/Relic/Stats
- https://www.hoyolab.com/article/17486374

使用时应记录抓取日期和版本；社区概率/权重数据尤其需要注意样本和版本敏感性。



---

## Canonical source: references/genshin-weapon-artifact-patterns.md

# Genshin Impact Weapon & Artifact Patterns

用途：记录《原神》武器与圣遗物系统中对通用 Itemization 设计有参考价值的公开结构。只用于参考和验证，不把具体数值直接迁移到其他项目。

## 1. 武器结构

公开资料支持以下稳定结构：

- 武器按类型区分单手剑、双手剑、长柄、弓、法器；
- 3★及以上武器通常具有基础攻击、一个副属性和一个被动；
- 武器等级成长至 90 级，并存在突破节点；
- 副属性随武器等级成长；
- 被动通过精炼 Rank 1~5 成长；
- 不同武器会形成不同的“基础攻击 / 副属性”组合，而不只是所有武器共享同一白值曲线；
- 被动可能是常驻增益、条件增益、触发效果、资源效果或角色行为联动。

可迁移模式：

### Base Stat / Secondary Stat Budget Family

同一品质武器可以通过：

- 高基础 / 低副属性；
- 中基础 / 中副属性；
- 低基础 / 高副属性；

形成不同预算家族。

但在其他项目中必须先用自己的伤害公式、基础属性和角色成长验证交换率。

### Refinement as Duplicate Value

重复武器不是简单返还资源，而是可以提高被动参数。

可迁移问题：

- 重复品是否应该提高基础属性、特效，还是转为其他资源；
- Rank 1 是否已经完整可用；
- Rank 5 是否只是纵向强化，还是会改变机制；
- 重复品价值是否导致付费/获取压力过高。

### Ascension Breakpoints

1~90 不是纯线性一条线，突破承担：

- 等级上限；
- 材料门槛；
- 数值成长阶段；
- 长线节奏节点。

对标时应采样突破前后，而不是只看 Lv1 / Lv90。

## 2. 圣遗物结构

公开资料支持：

- 圣遗物有 5 个槽位；
- 花与羽具有固定主属性；
- 沙、杯、冠承担随机主属性选择；
- 5★圣遗物最高 +20；
- 5★圣遗物初始通常有 3~4 条副词条；
- 每 +4 级发生一次副词条新增或强化事件；
- 副词条不能重复，也不能与主属性完全同名；
- 套装常见为 2 件 / 4 件效果；
- 主属性、套装、初始副词条、强化命中共同构成多层随机。

## 3. 可迁移模式

### Fixed + Variable Slot Architecture

固定槽位降低一部分搜装随机，随机槽位承担 Build差异。

### +20 / Every-4-Level Event

+20 对应 5 个关键副词条事件节点。

值得对比 HSR 的 +15 / 每3级节点：

```text
不同最大强化等级
可以拥有相近的有意义升级事件数量
```

可迁移的是“事件密度”的概念，而不是 +20 本身。

### Main Stat Gating

不同槽位主属性池不同，使：

- 某些功能属性只有特定槽位能拿；
- Build选择被压缩到可理解的槽位决策；
- 同时也会提高特定主属性的刷取压力。

### Set Lock vs Off-Piece Flexibility

2/4件套装允许一个非套装槽位承担高质量散件，这是一种“套装压力与单件质量”之间的结构平衡。

是否适合其他项目，要看：

- 总槽位数；
- 套装门槛；
- 单件随机深度；
- 玩家获取频率。

## 4. 设计风险

- **Crit Convergence**：输出Build大量追暴击/暴伤；
- **Elemental Goblet Scarcity**：功能/伤害类型主属性池过宽会放大目标掉落稀缺；
- **Set + Main + Substat Multiplication**：多层随机相乘后，实际升级率远低于名义掉率；
- **Signature Weapon Pressure**：专武被动若同时覆盖基础属性、关键副属性和角色专属机制，可能形成完成度税；
- **Refinement Scaling Pressure**：重复品继续提高被动，需评估付费/获取差距和边际价值。

## 5. Benchmark 使用

武器对标时比较：

```text
Base Attack Curve
Secondary Stat Curve
Ascension Breakpoints
Passive R1~R5 Delta
Signature Fit
Alternative Coverage
```

圣遗物对标时比较：

```text
Slot Main-stat Gating
Initial Substat Count
Upgrade Event Count
Roll Tier Spread
Set Threshold
Off-piece Flexibility
Effective Upgrade Funnel
```

不要只拿某把90级武器或某件+20圣遗物的满级值直接作为项目候选。

## 6. 主要来源

- https://ys.appfeng.com/weapon
- https://ys.appfeng.com/reliquary
- https://genshin-impact.fandom.com/wiki/Weapon
- https://genshin-impact.fandom.com/wiki/Artifact/Stats

AppFeng 适合通过详情页和等级进度条查看 Lv1~90 武器、突破与精炼，以及不同强化等级的圣遗物属性；若详情页当前无法抓取，应标 `externally-blocked`，不要从记忆补值。



---

## Canonical source: references/wuwa-weapon-echo-patterns.md

# Wuthering Waves Weapon & Echo Patterns

用途：记录《鸣潮》武器与声骸系统中对通用 Itemization 设计有参考价值的公开结构。只用于外部参考与项目验证，不把具体值直接迁移。

## 1. 武器结构

公开图鉴支持以下模式：

- 武器分长刃、臂铠、迅刀、佩枪、音感仪等类型；
- 终局武器可成长至 90 级；
- 武器具有基础攻击、一个副属性和“谐振”特效；
- 谐振存在 Rank 1~5；
- 5★武器存在不同的基础攻击 / 副属性档位组合；
- 副属性可包含暴击、暴伤、攻击、共鸣效率等；
- 特效经常与变奏、共鸣技能、共鸣解放、声骸技能、特定状态或属性伤害联动。

公开详情页中可见的 90 级代表性组合包括：

- 500 基础攻击 + 36% 暴击；
- 500 基础攻击 + 72% 暴击伤害；
- 587.5 基础攻击 + 24.3% 暴击；
- 587.5 基础攻击 + 48.6% 暴击伤害；
- 587.5 基础攻击 + 38.9% 共鸣效率。

这些值只用于证明同品质武器存在不同预算家族，不是通用平衡标准。

## 2. 武器可迁移模式

### Base/Secondary Tradeoff Families

同品质武器可以通过不同白值与副属性组合维持总预算差异化。

对项目的验证问题：

- 高白值是否对所有角色都更优；
- 副属性是否能真正补偿白值差；
- 某些角色是否因基础属性倍率而系统性偏爱某预算家族；
- 同时拥有高白值、高暴击和强专属特效时是否出现 Signature Tax。

### Passive as Rotation Hook

大量武器被动不是常驻面板，而是与：

- 变奏；
- 共鸣技能；
- 共鸣解放；
- 声骸技能；
- 状态附加；
- 切换角色；

联动。

这说明武器可以成为“Rotation Component”，但迁移时必须和当前项目技能循环、触发可靠性一起预算。

## 3. Echo / 声骸结构

公开资料支持：

- 声骸存在 Rarity、Sonata、Cost、Echo Skill、Stats 等维度；
- Cost 常见为 1 / 3 / 4；
- 角色有总 Cost 上限，公开资料中终局常见上限为 12；
- 5★声骸最高可强化至 +25；
- 声骸存在两条主属性，主属性池与 Cost 相关；
- 1-Cost、3-Cost、4-Cost 承担不同主属性池；
- 每 +5 级可以开放一次调谐副词条位置，5★最多 5 条；
- 副词条与主属性可以同类，但副词条自身不能重复；
- Sonata / 合鸣承担套装效果；
- Echo Skill 让装备实体同时具备主动战斗行为。

## 4. Cost-Constrained Loadout

这是与传统固定槽位装备最不同的结构之一。

其核心不是：

```text
头 / 手 / 衣 / 鞋固定6槽
```

而是：

```text
多个可装备实体
+ 每个实体有 Cost
+ 总 Cost Budget
```

可迁移价值：

- 用 Budget 而非固定槽位控制强度；
- 允许“少量高Cost + 多个低Cost”形成阵容式搭配；
- Cost 与主属性池、技能价值、稀有实体形成组合选择。

迁移前必须验证：

- 高Cost是否自然成为必选；
- 低Cost是否只是填空位；
- Cost预算是否产生真实组合，还是迅速收敛到固定模板；
- 主属性与Echo Skill是否双重抬高高Cost价值。

## 5. Dual Main Stat

声骸的双主属性结构与 Genshin/HSR 的单主属性思路不同。

这可以用于研究：

- 一个装备是否同时承担基础稳定值 + Build主轴；
- 固定副主属性能否降低随机压力；
- 两条主属性会不会造成过强的单件Power Budget。

不要因为鸣潮采用双主属性，就默认所有项目都应该增加第二主属性。

## 6. Tuning / 每5级副词条节点

+25 对应最多 5 个调谐节点。

与 HSR +15/每3级、Genshin +20/每4级对比，可以观察：

```text
三个系统虽然最大强化等级不同
但都能形成约5次主要副词条成长事件
```

这是非常有价值的跨游戏 Pattern：

> 玩家感知的“有意义升级次数”可能比表面最大等级更值得对标。

不可迁移的是具体 +25 或每5级本身。

## 7. Sonata / 合鸣

公开页面可见：

- 2件 / 5件结构；
- 部分新系统存在 1件 / 3件等其他门槛；
- 套装效果可包含属性伤害、暴击/暴伤、攻击、治疗、共鸣效率、团队增益、状态触发等；
- 套装效果越来越多与特定状态、技能类型和队伍行为联动。

这对项目设计的启发是：

- 套装可以从“静态加成”进化为“Build规则放大器”；
- 但越具体的触发条件，越容易造成角色/套装硬绑定；
- 需要检查 Set Lock、Pair Lock 和版本淘汰风险。

## 8. 设计风险

- **Cost Meta Lock**：某个 Cost 组合长期成为唯一模板；
- **Double Budgeting**：高Cost同时拿更强主属性和更强主动技能，预算重复；
- **Tuning Friction**：主属性正确后仍要处理5层副词条随机，实际毕业成本高；
- **Passive Rotation Lock**：武器或套装与特定角色循环绑定过深；
- **Signature Pressure**：专武提供关键状态、减抗、穿防或团队收益时，替代空间显著收缩；
- **Sonata Power Creep**：新套装通过更高条件收益逐步替代旧套装。

## 9. 主要来源

- https://mc.appfeng.com/weapon
- https://mc.appfeng.com/echo
- https://wutheringwaves.fandom.com/wiki/Echo/Stats
- https://wutheringwaves.fandom.com/wiki/Echo/Leveling
- https://www.prydwen.gg/wuthering-waves/guides/echo-stats

AppFeng 的武器详情页适合读取 90级属性、谐振 Rank 和突破材料；Echo 总页适合读取合鸣门槛与触发结构。



---

## Canonical source: references/cross-game-itemization-benchmark.md

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



---

## Canonical source: references/source-map.md

# Itemization Benchmark Source Map

本文件记录外部 Itemization 参考来源。精确数值使用前应重新检查页面日期/版本。

## Honkai: Star Rail

### AppFeng Relic Index
- URL: https://sr.appfeng.com/relic
- Type: structured community database / index
- Useful for: relic sets, filters, interactive detail navigation, level/stat inspection
- Evidence role: reference-data
- Version-sensitive: yes

### HSR Wiki Relic Stats
- URL: https://honkai-star-rail.fandom.com/wiki/Relic/Stats
- Type: community wiki / structured stat tables
- Useful for: slot main-stat availability, rarity/max level, main-stat curves, initial substat counts, +3 cadence, substat tiers/weights
- Evidence role: reference-data; probability/weight claims require community-data caution
- Version-sensitive: yes

### HoYoLAB Relic Guide
- URL: https://www.hoyolab.com/article/17486374
- Type: community guide hosted on HoYoLAB
- Useful for: slot/main/substat explanatory cross-check
- Evidence role: secondary reference

## Genshin Impact

### AppFeng Weapon Index
- URL: https://ys.appfeng.com/weapon
- Type: structured community database / index
- Useful for: weapon list, rarity/type/stat filters, interactive detail pages, level slider, refinement
- Evidence role: reference-data
- Version-sensitive: yes

### AppFeng Artifact Index
- URL: https://ys.appfeng.com/reliquary
- Type: structured community database / index
- Useful for: artifact sets, filters, detail pages, enhancement-level inspection
- Evidence role: reference-data
- Version-sensitive: yes

### Genshin Wiki Weapon
- URL: https://genshin-impact.fandom.com/wiki/Weapon
- Type: community wiki
- Useful for: base ATK, secondary stat, passive, weapon rarity/type structure
- Evidence role: reference-data

### Genshin Wiki Artifact Stats
- URL: https://genshin-impact.fandom.com/wiki/Artifact/Stats
- Type: community wiki / structured stat tables
- Useful for: max levels by rarity, initial substats, +4 upgrade cadence, duplicate/exclusion rules, roll tiers
- Evidence role: reference-data

## Wuthering Waves

### AppFeng Weapon Index
- URL: https://mc.appfeng.com/weapon
- Type: structured community database / index/detail pages
- Useful for: weapon types, rarity/stat filters, Lv90 stats, resonance 1~5, breakthrough materials
- Evidence role: reference-data
- Version-sensitive: yes

Representative detail pages observed by public search/indexing include weapon families with different Lv90 base ATK / secondary-stat combinations. Exact items should be refetched when used in a formal comparison.

### AppFeng Echo / Sonata Index
- URL: https://mc.appfeng.com/echo
- Type: structured community database / set index
- Useful for: Sonata thresholds, set effects, Cost 1/3/4 members, trigger wording
- Evidence role: reference-data
- Version-sensitive: yes

### Wuthering Waves Wiki Echo Stats
- URL: https://wutheringwaves.fandom.com/wiki/Echo/Stats
- Type: community wiki / structured stat tables
- Useful for: Cost classes, rarity, +25 cap, dual mainstats, mainstat pools, substat ranges, tuning structure
- Evidence role: reference-data; sampled probability distributions require sample-size caution

### Wuthering Waves Wiki Echo Leveling
- URL: https://wutheringwaves.fandom.com/wiki/Echo/Leveling
- Type: community wiki
- Useful for: EXP/currency/tuning cost and refund rules
- Evidence role: reference-data

### Prydwen Echo Stats
- URL: https://www.prydwen.gg/wuthering-waves/guides/echo-stats
- Type: community theorycraft/reference
- Useful for: Echo main/substat structure and level/tuning cross-check
- Evidence role: secondary cross-check

## Accessed / Reviewed

Initial benchmark pack assembled: 2026-09-15.

Important: the source map is not a frozen truth table. Live-service games change. When a user asks for exact current values, refetch current pages rather than relying only on this reference file.

## Source Conflict Rule

When sources disagree:

1. check game version/date;
2. check rarity/level/breakthrough/refinement context;
3. prefer official or game-verifiable data where available;
4. keep both values visible until resolved;
5. do not silently average or select one.

