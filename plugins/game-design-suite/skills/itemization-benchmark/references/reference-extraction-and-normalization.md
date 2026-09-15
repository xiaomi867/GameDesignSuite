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
