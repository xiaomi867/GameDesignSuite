# HSR Formula Reference

> 用途：作为回合制 RPG 战斗公式的参考样本，不作为本项目标准。
>
> 证据属性：主要来自 HoYoLAB 社区理论计算与 KQM 社区研究，不等同于官方源码。使用时按 `reference-community` 处理，并在本项目中重新验证。

## 1. 直接伤害乘区结构

常见社区理论模型：

`DMG = BaseDMG × Crit × DMGBonus × DEF × RES × Vulnerability × DMGReduction × Broken/State`

其中：

`BaseDMG = ScalingStat × SkillMultiplier + ExtraDMG`

### 暴击

单次暴击：

`CritMultiplier = 1 + CritDMG`

期望暴击乘区：

`ExpectedCrit = 1 + CritRate × CritDMG`

前提：该伤害允许暴击，且暴击率已按项目规则 Clamp。

### 增伤

常见做法是把同一 DMG Bonus Bucket 内的相关增伤先加总：

`DMGBonusMultiplier = 1 + ΣRelevantDMGBonus`

### 易伤

`VulnerabilityMultiplier = 1 + ΣRelevantVulnerability`

### 减伤

多个独立减伤若按乘算：

`ReductionMultiplier = Π(1 - DR_i)`

实际项目必须由代码确认是否真的如此。

## 2. 基础属性组成

社区常见模型：

```text
BaseHP  = CharacterHP  + EquipmentHP
BaseATK = CharacterATK + EquipmentATK
BaseDEF = CharacterDEF + EquipmentDEF

FinalStat = BaseStat × (1 + StatBonus%) + FlatBonus
```

可用于检查“基础属性 / 百分比属性 / 固定属性”是否分层。

## 3. 防御乘区

HSR 常见理论模型把攻击者等级与目标防御共同放入防御乘区。

一种等价表达思路：

`DEFMultiplier = AttackerLevelFactor / (EffectiveTargetDEF + AttackerLevelFactor)`

其中目标防御又会受减防/无视防御等影响。

关键不是照抄常数，而是学习三个设计点：

1. 防御收益通常是非线性的；
2. 等级差可以进入防御效率；
3. 减防/无视防御的位置会显著影响边际收益。

本项目验证时必须写出自己的：

- `LevelFactor`；
- `EffectiveDEF`；
- Clamp；
- 减防与穿透的顺序。

## 4. 抗性乘区

社区常见抽象：

`RESMultiplier = f(BaseRES - RESReduction - RESPEN)`

不要默认是无限线性。必须确认：

- 抗性上下限；
- 负抗收益；
- 减抗与穿透是否同层；
- 是否存在分段函数。

## 5. 行动值 / 速度

KQM 社区整理的行动条模型：

`BaseAV = 10000 / SPD`

当前行动条：

`CurrentActionGauge = CurrentAV × CurrentSPD`

行动提前/延后：

`NewActionGauge = max(0, CurrentActionGauge - 10000 × (Advance% - Delay%))`

速度变化：

`NewAV = CurrentAV × CurrentSPD / NewSPD`

同时存在速度变化和行动条改动时，可整理为：

`NewAV = CurrentAV × CurrentSPD / NewSPD - 10000 × (Advance% - Delay%) / NewSPD`

### 设计启示

速度收益最终应转换成：

- 某个战斗窗口内多几次行动；
- 多几个技能点；
- 多多少能量；
- 是否跨过离散 Breakpoint。

不能只看“SPD +5%”。

## 6. 效果命中 / 效果抵抗

较新的社区研究常用：

`RealChance = BaseChance × (1 + EffectHitRate) × (1 - EffectRES) × (1 - SpecificRES)`

这比“基础概率 + 命中 - 抵抗”的旧简化模型更适合作为校验参考。

需要检查：

- 每段独立 Roll 还是整技能一次 Roll；
- Boss 特殊抗性；
- 免疫是否是 SpecificRES=100%，还是单独 Boolean；
- 最终概率是否 Clamp。

## 7. 仇恨权重

常见抽象：

`P(target i) = Aggro_i / ΣAggro`

若存在嘲讽/强制锁定，必须区分“权重修改”和“强制 Target”。

## 8. 击破 / 第二 Gauge

崩铁类体系把 HP 与 Toughness 分成两个不同战斗轴。

参考时重点验证：

- Toughness Damage 是否与普通伤害同公式；
- Break Trigger；
- Break 后是否解除某个减伤乘区；
- Break Effect 影响哪些结果；
- Delay 是否与 Break Effect 联动；
- Boss 是否有特殊韧性规则。

不要把第二 Gauge 设计成“第二条血量”。

## 9. DoT

DoT 常见特征：

- 不一定允许暴击；
- 可能沿用 DEF/RES/Vulnerability；
- 可能在施加时快照部分攻击者属性；
- 目标侧减益/抗性可能在 Tick 时动态读取；
- “引爆”可能提前结算现有 DoT，而不是重新生成一份独立 DoT。

本项目必须通过代码确认 Snapshot / Dynamic。

## 10. 参考来源

- HoYoLAB 3.0 Theorycrafting Guide: https://www.hoyolab.com/article/36700608
- HoYoLAB Damage Multiplier Blocks: https://www.hoyolab.com/article/18126946
- HoYoLAB Effect Hit / Effect RES: https://www.hoyolab.com/article/19460061
- HoYoLAB Toughness/Break: https://www.hoyolab.com/article/18981104
- KQM Speed Guide: https://hsr.keqingmains.com/misc/speed-guide/

### Source Status

这些来源主要是社区理论研究，不是官方服务端源码。若与游戏版本更新、代码实测或官方说明冲突，以更高等级证据为准。
