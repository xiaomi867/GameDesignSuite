# Game Design Suite Chat Edition — RPG Numerical Deep Reference

> Deep reference bundle for Chat Edition. These materials preserve detailed reasoning patterns from the canonical Game Design Suite. External commercial-game values remain benchmark/reference evidence, never current-project truth.


---

## Canonical source: references/hsr-theorycrafting-patterns.md

# HSR-Inspired Theorycrafting Patterns

> 用途：把《崩坏：星穹铁道》社区长期形成的数值分析方法抽象成可复用的数值策划工具。
>
> 边界：这是“方法参考”，不是要求项目复制《崩铁》的具体公式、成长率、速度阈值、遗器词条或角色模板。任何具体值进入当前项目前，都必须重新基于项目代码、内容、玩家节奏与目标体验验证。

## 1. 先拆乘区，再谈倍率

复杂 RPG 的最终伤害不要只写成“攻击 × 技能倍率”。更稳健的分析方式是拆成相互独立的乘区：

`FinalValue = Base × Critical × DamageBonus × Defense × Resistance × Vulnerability × Mitigation × State`

其中每个乘区都要说明：

- 来源；
- 是否加算/乘算；
- 上下限；
- 作用对象；
- 是否只对某伤害类型生效；
- 是否存在稀释；
- 是否与其他乘区重复。

### 设计意义

当一个角色已经堆叠大量同乘区属性时，再增加同乘区往往边际收益下降；而稀缺乘区、减防、抗性穿透、易伤等可能产生更高边际价值。

因此不能用“+20%”直接比较两个不同乘区的收益。

### 输出建议

正式比较 Buff 时同时给：

- 表面增幅；
- 当前 Build 下边际增幅；
- 满配 Build 下边际增幅；
- 是否依赖特定乘区稀缺性；
- 与队友叠加后的实际收益。

---

## 2. 基础属性层与进阶属性层分开

可采用类似：

`TotalStat = BaseStat × (1 + PercentBonus) + FlatBonus`

其中 BaseStat 可以由多个“基础来源”组成，例如角色基础值 + 武器/装备基础值。

### 设计意义

这能清楚区分：

- 等级/突破：改变 Base；
- 百分比装备：放大 Base；
- 固定值装备：最后加算；
- Buff：根据规则进入相应层。

不要让“基础值”“百分比”“固定值”混在同一层，否则成长曲线、装备价值和角色差异很难维护。

---

## 3. 平滑成长 + 离散突破

参考成熟角色养成模型时，可把成长拆为：

- 每级稳定增长；
- 突破节点一次跳变；
- 突破同时承担内容门槛/能力解锁；
- 速度、能量上限、攻击间隔等可作为固定维度，不必跟等级同步增长。

### 检查项

对 Lv1→Max 至少检查：

- Base Growth；
- Ascension Delta；
- 每段 Power Delta；
- 突破前/突破后差值；
- Cost Delta；
- Content Difficulty Delta；
- 是否存在某段“花费增加但强度不变”。

不要机械复制任何外部游戏的“每级增长率”。应只学习“平滑成长 + 节点跳变”的结构。

---

## 4. 有效词条 / Stat Budget

把装备、被动、套装、Buff 的属性价值转换成统一的“有效词条单位”是一种很实用的 Benchmark 方法。

### 方法

1. 选一个标准单位，例如“一次平均副词条强化”；
2. 将暴击、暴伤、攻击%、生命%、防御%、速度、命中、抵抗等换算为该单位；
3. 用它比较装备主词条、套装效果、角色被动和 Buff 的“预算”；
4. 再通过角色 Build 做 Context Discount。

### 必须注意

“等效词条”只能表示**资源预算近似**，不能直接证明不同属性实战价值相同。

原因包括：

- 乘区稀释；
- 速度/命中存在阈值；
- 暴击存在 EV 与方差；
- 防御/生命对不同敌人有不同 EHP；
- 属性只对特定技能生效；
- 角色已有属性不同；
- 套装有条件与覆盖率。

因此必须区分：

`Stat Budget ≠ Effective Combat Value`

---

## 5. Breakpoint 优先于“连续收益”幻觉

速度、命中、能量回复、控制覆盖等属性经常不是连续线性收益，而是存在离散 Breakpoint。

### 通用模型

若某属性决定周期内可执行次数，可写：

`ActionInterval = K / Speed`

然后基于真实内容时间窗计算：

- 1 个战斗窗口能行动几次；
- 下一点速度是否真的多一次行动；
- 达不到下个 Breakpoint 时，速度的局部价值是否低于其他属性。

不要脱离内容时长追求“神圣速度阈值”。阈值必须绑定：

- 战斗时长；
- 波次切换；
- Boss 阶段；
- Buff 持续；
- 技能 CD；
- 资源循环。

---

## 6. Action Economy / 行动经济

单回合制或自动战斗中，行动次数本身就是一种资源。

分析角色价值时，应记录：

- 每周期行动数；
- 额外行动；
- 提前行动；
- 延后敌人；
- 插队；
- 追击/反击；
- 动作是否消耗共享资源；
- 动作是否触发队友收益。

### Action Value

可将角色的有效价值拆成：

`Per Action Value × Actions per Window`

而不是只比较“单次技能倍率”。

一个单次倍率低但行动频率高、能触发队友或恢复资源的角色，可能比高倍率慢角色更强。

---

## 7. Shared Resource Economy / 团队共享资源

《崩铁》的战技点体系提供一个很重要的方法论：团队成员不能只按“个人 DPS”评价，还要按共享资源净流量评价。

### 通用指标

`Net Resource per Rotation = Generated - Consumed`

可将角色分为：

- Resource Positive；
- Resource Neutral；
- Resource Negative；
- Burst Consumer；
- Emergency Consumer。

### 组队检查

每个 Team Rotation 至少检查：

- 总产出；
- 总消耗；
- 初始库存；
- Burst Window 需要多少；
- 紧急治疗/控制是否会打破循环；
- 是否过量溢出；
- 是否因某角色加速/追加行动导致资源突然转负。

这类资源模型同样适用于怒气、卡牌点数、技能点、弹药、行动点。

---

## 8. Energy Cycle / 终结技循环

大招不能只看“能量上限”，需要计算回能循环。

### 基础模型

`TurnsToUltimate = ceil((EnergyCap - StartEnergy - FixedGains) / EffectiveGainPerAction)`

若存在回能效率，可写：

`EffectiveGain = BaseGain × RegenMultiplier`

但必须逐项确认：

- 哪些能量来源受回能效率影响；
- 哪些是固定回能；
- 击杀/受击/追击是否回能；
- 大招自身是否返能；
- 溢出能量是否浪费；
- Buff 是否覆盖大招窗口。

### 设计经验

“差一点够一次大招”的属性提升可能比表面 EV 更有价值，因为它跨过了 Rotation Breakpoint。

---

## 9. Hit vs Resist / 状态可靠性

Debuff、控制、特殊状态必须用“实际命中概率”而不是 Base Chance 判断。

可使用通用结构：

`RealChance = BaseChance × AttackerHitFactor × TargetResistFactor × SpecificResistFactor`

### 必查

- 普通怪；
- Elite；
- Boss；
- 高抗性模式；
- 是否有专属免疫；
- 达到 90% / 95% / 100% 可靠性的属性门槛；
- 多次判定时累计成功概率。

控制类角色尤其不能只比较“技能写 100%”。

---

## 10. Aggro / Target Weight

目标选择若采用概率权重，应显式建模：

`P(i) = Weight(i) / Σ Weight(team)`

这比“坦克更容易被打”更可验证。

### 应用

- Tank 的嘲讽价值；
- 受击回能；
- 反击触发；
- 后排生存；
- 队伍站位；
- Bounce/随机攻击是否绕过权重。

只要 Target 不是强制锁定，就应该考虑概率而不是绝对结论。

---

## 11. Toughness / Secondary Gauge

《崩铁》的韧性/击破提供一种可复用的“第二战斗轴”：玩家除了削减 HP，还能通过另一个 Gauge 获得控制、爆发或状态收益。

设计类似系统时要同时建立：

- Gauge Max；
- 每技能 Gauge Damage；
- Break Trigger；
- Break Reward；
- Recovery Time；
- Boss Resistance；
- Build Synergy；
- 是否形成“只打 HP / 只打 Gauge”的主导策略。

Secondary Gauge 的价值必须计入角色 Power Budget，否则功能角色会被低估。

---

## 12. Standardized Benchmark Loadout

做横向角色比较时必须固定测试环境。

建立类似：

- 同等级；
- 同突破；
- 同技能等级；
- 同稀有度装备；
- 固定副词条预算；
- 固定星级/命座规则；
- 固定敌人等级、防御、抗性；
- 固定战斗时间窗；
- 固定队友或 Solo Benchmark。

### 原则

Benchmark 不是“现实玩家平均练度”，而是一个**可重复对照实验基准**。

若测试目的不同，应准备多个 Benchmark：

- New Player；
- Midgame；
- Endgame Standard；
- High Investment；
- Extreme Ceiling。

---

## 13. 不从参考游戏照抄结论

外部参考最值得学习的是：

- 变量分层；
- 乘区拆分；
- Breakpoint；
- 共享资源循环；
- 标准化 Benchmark；
- 有效词条预算；
- 概率可靠性；
- 行动经济。

最不应该照抄的是：

- 具体成长率；
- 具体倍率；
- 固定速度阈值；
- 具体词条数；
- 角色稀有度差值；
- 终局内容时间窗；
- 外部游戏版本特有公式。

先抽象“为什么这样设计”，再映射到当前项目。

## 参考来源（方法论提炼）

- HoYoLAB / 米游社社区的伤害乘区、速度、战技点、模拟宇宙等理论文章；
- Honkai: Star Rail Wiki 的 DEF、RES、Effect Hit、Aggro、Toughness、Relic Stats 条目；
- KQM 的 Speed / Action Value 方法；
- 社区“有效词条”与标准面板方法。

这些来源用于建立分析方法，不作为当前项目的直接数值真值。


---

## Canonical source: references/hsr-formula-reference.md

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



---

## Canonical source: references/zzz-formula-reference.md

# ZZZ Formula Reference

> 用途：作为动作 RPG、失衡/异常体系、穿透/防御公式的参考样本，不作为本项目标准。
>
> 证据属性：主要来自 HoYoLAB 社区理论计算、Prydwen 与社区 Wiki，不等同于官方源码。版本更新后需重新核对。

## 1. 标准直伤结构

社区常见抽象：

`StandardDMG = BaseDMG × DMGBonus × Crit × DEF × RES × DMGTaken × Stun/State`

其中：

`BaseDMG = ScalingStat × SkillMultiplier + FlatExtra`

期望暴击：

`ExpectedCrit = 1 + CritRate × CritDMG`

### 设计启示

- 技能倍率、增伤、暴击、防御、抗性、易伤/承伤、失衡窗口分属不同层；
- 如果所有增伤都塞同一个加算区，容易产生明显稀释；
- 如果过多独立乘区无限叠加，容易产生极端爆炸增长。

## 2. 防御、减防与穿透

社区常见结构：

```text
EnemyDEF_AfterShred = TargetDEF × (1 - DEFReduction - DEFIgnore)
EffectiveDEF = max(EnemyDEF_AfterShred × (1 - PENRatio) - FlatPEN, 0)
DEFMultiplier = AttackerLevelFactor / (AttackerLevelFactor + EffectiveDEF)
```

具体版本可能存在实现细节差异，项目验证必须以当前代码为准。

### 设计启示

减防与穿透若不在同一层：

- 组合收益可能不是简单相加；
- 高防 Boss 与低防小怪下收益不同；
- Flat PEN 的价值高度依赖剩余有效防御；
- 必须测试 EffectiveDEF 是否允许负值。

## 3. 抗性

社区常见抽象：

`RESMultiplier = f(TargetRES - RESReduction - RESPEN)`

需要确认：

- 负抗区间；
- 抗性上下限；
- 弱点/抗性是否直接进同一乘区；
- 是否存在分段收益。

## 4. 角色最终属性组成

社区 Wiki 常见模型：

```text
FrozenStat = BaseValue × (1 + Unconditional%) + UnconditionalFlat
FinalStat = FrozenStat × (1 + Conditional%) + ConditionalFlat
```

这类结构适合检查：

- 战斗外面板与战斗内 Buff 是否分层；
- 战斗内百分比 Buff 取哪个 Base；
- 进入战斗时是否冻结某层属性；
- Buff 叠加是否重复乘 Base。

## 5. 异常精通 / Anomaly Proficiency

社区理论常见：

`AnomalyProficiencyMultiplier = AnomalyProficiency / 100`

例如 AP=150 -> 1.5 倍异常精通乘区。

异常伤害常见乘区结构：

`AnomalyDMG = AnomalyBase × Proficiency × Level × DMGBonus × DEF × RES × DMGTaken × Stun/State × Special`

具体异常是否允许暴击，要按角色/版本确认，不应统一假定。

## 6. 异常积蓄 / Anomaly Buildup

Anomaly Mastery 主要影响积蓄效率，而 Anomaly Proficiency 主要影响异常伤害。

验证时分开：

- Buildup per Hit；
- Buildup Rate Bonus；
- Target Buildup Resistance；
- Same-Anomaly Reapply Rule；
- Internal Cooldown；
- Threshold；
- Trigger Timing。

不要把“积蓄快”直接等同于“单次异常伤害高”。

## 7. 多角色共同异常贡献

社区研究常见一个重要模式：若多个角色共同贡献同属性异常积蓄，最终异常伤害可能按各自积蓄贡献比例加权部分攻击者属性。

抽象形式：

`WeightedStat = Σ(ContributionShare_i × Stat_i)`

例如：

`WeightedAP = Σ(BuildupShare_i × AP_i)`

本项目若存在“多人共同积累同一 Gauge/状态”，应明确：

- 谁拥有最终实例；
- 谁的属性被快照；
- 是最后一击决定，还是贡献加权；
- 非角色单位是否参与权重；
- Buff 在施加时还是触发时读取。

## 8. Disorder / Cross-State Interaction

绝区零的异常系统适合作为“状态 A + 状态 B 产生额外结算”的参考。

验证这类公式时要拆：

1. 状态 A 的剩余价值；
2. 状态 B 的施加；
3. Cross-State Trigger；
4. 是否提前结算旧状态；
5. 是否清除/覆盖旧状态；
6. 额外伤害是否重新吃 DEF/RES/易伤；
7. 内置 CD 与重复触发限制。

不要用一个“状态共存时 +X% 伤害”概括复杂交互。

## 9. 失衡 / Daze / Stun

对第二 Gauge 类系统至少拆：

- Daze/Gauge Buildup；
- Impact/相关属性对积蓄的影响；
- Stun Threshold；
- Stun Duration；
- Stun Damage Taken Multiplier；
- Boss/Elite Resistance；
- 是否能连续锁定；
- Stun 结束后的恢复/免疫窗口。

公式验证要同时看“积蓄速度”和“窗口收益”，不能只看其中一侧。

## 10. 时间与动作实现

动作游戏实际收益还受：

- 前摇；
- 后摇；
- Cancel；
- Swap；
- Assist；
- 敌人位移；
- Stun Window；
- 动画锁；
- Hitstop；

影响。

所以：

`Paper Motion Value / animation time`

只是一层理论 DPS，不能直接当真实战斗 DPS。

## 11. 参考来源

- HoYoLAB 战斗机制整理: https://www.hoyolab.com/article/28987778
- HoYoLAB 伤害构成、喧响值与能量值: https://www.hoyolab.com/article/37522351
- HoYoLAB 异常与紊乱体系: https://www.hoyolab.com/article/35508795
- HoYoLAB 防御削减与 PEN Ratio: https://www.hoyolab.com/article/41060247
- Prydwen Anomalies and Disorders: https://www.prydwen.gg/zenless/guides/anomalies-and-disorders
- Prydwen Attributes & Specialties: https://www.prydwen.gg/zenless/guides/agents-attributes

### Source Status

以上主要是公开社区研究。Skill 使用这些公式时必须标为参考样本；如果本项目真实代码、运行时日志或当前版本实测冲突，以更高等级证据为准。



---

## Canonical source: references/formula-source-map.md

# Formula Source Map

用于记录外部公式来源、证据等级和适用边界。目标不是“收藏链接”，而是防止把社区推导、旧版本资料和本项目事实混为一谈。

## Evidence Tags

| Tag | Meaning |
|---|---|
| `official-doc` | 官方明确文档/说明 |
| `official-data` | 官方可见数据，但公式仍可能是推导 |
| `community-theorycraft` | 社区理论计算/反推 |
| `community-wiki` | 社区 Wiki 汇总 |
| `tool-derived` | 计算器/工具项目推导 |
| `version-sensitive` | 明显依赖版本 |
| `pattern-only` | 只借结构，不借常数 |

外部公式默认不能直接升级成本项目 `verified-code` 或 `verified-runtime`。

## Honkai: Star Rail / 崩坏：星穹铁道

| Topic | Source | Tag | Use |
|---|---|---|---|
| General DMG blocks / stats | https://www.hoyolab.com/article/36700608 | community-theorycraft, version-sensitive | 乘区结构、基础属性组成、DEF/RES/易伤 |
| Damage multiplier blocks | https://www.hoyolab.com/article/18126946 | community-theorycraft | 乘区拆分、Break、早期资料对照 |
| Speed / Action Value | https://hsr.keqingmains.com/misc/speed-guide/ | community-theorycraft | AV、SPD、Advance/Delay、Breakpoint |
| Effect Hit / Effect RES | https://www.hoyolab.com/article/19460061 | community-theorycraft | BaseChance、EHR、RES、Specific RES |
| Toughness / Break | https://www.hoyolab.com/article/18981104 | community-theorycraft | 第二 Gauge、Break 状态与减伤 |
| Incoming DMG example | https://hsr.keqingmains.com/fu-xuan/ | community-theorycraft | DEF/RES/DR/Vulnerability、伤害转移 |
| Character mechanics | https://wiki.biligame.com/sr/%E8%A7%92%E8%89%B2%E5%9B%BE%E9%89%B4 | community-wiki, version-sensitive | 技能倍率/等级/机制样本 |
| Character database | https://sr.appfeng.com/character | community-wiki, version-sensitive | 角色与技能数据交叉参考 |

## Zenless Zone Zero / 绝区零

| Topic | Source | Tag | Use |
|---|---|---|---|
| Combat mechanics | https://www.hoyolab.com/article/28987778 | community-theorycraft | 基础伤害、异常、战斗属性 |
| Damage / Energy overview | https://www.hoyolab.com/article/37522351 | community-theorycraft | 直伤乘区、防御、抗性、暴击 |
| Anomaly / Disorder | https://www.hoyolab.com/article/35508795 | community-theorycraft | 异常伤害、AP、等级、多人贡献 |
| DEF Shred vs PEN Ratio | https://www.hoyolab.com/article/41060247 | community-theorycraft | 减防、无视、防穿顺序 |
| Anomalies and Disorders | https://www.prydwen.gg/zenless/guides/anomalies-and-disorders | community-theorycraft | 异常积蓄、触发、ICD、Disorder |
| Agent stats | https://www.prydwen.gg/zenless/guides/agents-attributes | community-theorycraft | PEN、AP、AM、Energy 等属性职责 |
| General formulas | https://github-wiki-see.page/m/Night-Sky-Studio/interknot-calculator/wiki/ZZZ-Formulas | tool-derived | 公式块交叉对照 |

## 用户此前提供的米游社资料

用户此前提供了多篇崩铁/绝区零的米游社文章，包含数值理论、角色技能、局内玩法、英雄设计等内容。部分页面是动态加载，无法稳定抓取正文时：

- 保留 URL 作为线索；
- 不声称已完整阅读；
- 不把无法读取正文的文章当公式证据；
- 优先用可稳定读取的同主题来源交叉验证。

## 使用规则

1. 外部来源只用于 Reference / Pattern Comparison。
2. 本项目真实配置、真实代码、Runtime 日志优先级更高。
3. 同一公式若多个社区来源冲突：
   - 记录版本；
   - 记录差异；
   - 不强行选一个当真；
   - 必要时用实测或源码验证。
4. 任何常数、Clamp、分段点都视为 `version-sensitive`，除非有更强证据。
5. 公式结构可以借鉴，参数规模必须按本项目重建。



---

## Canonical source: references/cross-game-character-stat-growth-patterns.md

# Cross-Game Character Stat Growth Patterns

本参考用于比较崩坏：星穹铁道、原神、鸣潮的角色等级/突破/基础属性结构。只提炼曲线与投放模式，不把具体外部数值当作当前项目标准。

## Source Boundary

首批公开来源：

- `https://sr.appfeng.com/character`
- `https://ys.appfeng.com/character`
- `https://mc.appfeng.com/avatar`
- 公开Wiki的 Character/Level Scaling、Ascension、Trace/Talent 等页面用于交叉验证。

详情页通常有等级滑杆；精确快照必须记录页面时间与版本。

## HSR Pattern

常见角色基础面板：

- HP；
- ATK；
- DEF；
- SPD；
- Energy Max；
- Taunt；
- Crit Rate / Crit DMG基础值。

角色通常以 Lv80 为传统满级基准，突破节点分布于20/30/40/50/60/70等阶段；Trace系统还独立提供 Stat Bonus 与 Bonus Ability。公开角色页显示速度、能量、嘲讽等往往作为固定身份参数存在，而HP/ATK/DEF随等级成长。

设计启发：

- 把“体质成长”和“循环参数”分离；
- 通过Trace/Bonus Ability提供离散成长节点；
- 行动速度若固定，更容易形成稳定角色节奏与配速Breakpoint。

## Genshin Pattern

公开角色等级体系长期采用多阶段Ascension，基础 HP/ATK/DEF 随等级成长，并有 Character Bonus Attribute 在部分突破阶段增加。公开 Level Scaling 数据显示，角色基础属性常使用基于稀有度与等级的Multiplier表，而不是每个角色单独手工画完全不同曲线。

设计启发：

- 可用“角色基础模板 × 等级Multiplier”统一曲线形状；
- 用Bonus Stat让角色在突破阶段强化配装/定位；
- Talent Level Cap 与Ascension阶段联动，使等级成长和技能成长有明确门槛。

Version Guard：公开资料可能随版本开放更高等级上限；引用时必须写明Source Date，不能固定认为“原神永远90级”。

## Wuthering Waves Pattern

公开角色页常见：

- HP；
- ATK；
- DEF；
- Crit Rate；
- Crit DMG；
- Resonance Efficiency；
- Resonance Energy Max；
- 部分角色/版本还会有其他节点属性。

角色常以 Lv90 页面快照展示，突破材料按阶段投放。技能节点与角色属性节点在同一成长树中，并存在多个个人/公共资源。

设计启发：

- 等级基础属性、资源上限、技能节点应分开建模；
- 动作游戏中固定暴击/共鸣效率基线与装备/声骸成长之间需要明确分工；
- 不同角色的Energy Max可以作为循环身份参数，而不是单纯Power属性。

## Cross-Game Shared Patterns

可观察到：

1. HP/ATK/DEF通常是主要等级成长属性；
2. 速度、能量、暴击基线等更常被当成角色身份/循环参数，而不是全部随等级同步增长；
3. 突破不仅提升上限，还承担技能等级上限、被动节点或Bonus Stat；
4. 角色满级数值不能单独评估，必须结合技能Scaling Source和装备系统；
5. 稀有度/职业可以共享成长曲线形状，但最终基准仍应以项目自身Benchmark验证。

以上为 `supported-inference`。

## Normalization Checklist

跨项目比较时至少记录：

- Level Cap；
- Ascension Levels；
- Lv1 values；
- pre/post-ascension values；
- LvMax values；
- fixed stats；
- bonus stat schedule；
- skill-cap unlock schedule；
- passive unlock schedule。

再计算：

- `V(L)/Vmax`；
- `V(L)/V1`；
- phase delta；
- growth density；
- roster percentile。

绝对值不可直接跨游戏比较。



---

## Canonical source: references/cross-game-skill-scaling-patterns.md

# Cross-Game Skill Scaling Patterns

本参考从崩坏：星穹铁道、原神、鸣潮公开角色与技能页提炼技能等级数值成长模式。只用于 Benchmark 与验证思路，不直接迁移倍率。

## Source Boundary

首批来源：

- `https://sr.appfeng.com/character`
- `https://ys.appfeng.com/character`
- `https://mc.appfeng.com/avatar`
- 公开Wiki的 Ability/Talent/Forte Scaling 页面用于交叉验证技能等级表。

任何精确倍率必须记录角色、技能、技能等级、来源日期和版本。

## HSR Pattern

公开技能数据可观察到：

- Basic ATK 常有独立较短等级区间；
- Skill / Ultimate / Talent 常有更长等级区间；
- Eidolon/Trace可提供额外技能等级，使Extended Level超过常规上限；
- 同一技能中，Damage、Base Chance、Action Delay、Buff等字段可以采用不同成长速度；
- 有些Utility字段保持固定。

示例性公开曲线：

- 多个Basic ATK可见 50% -> 100%（常规等级）并有更高Extended值；
- 飞霄Skill公开数据可见 100% 在常规高等级增长至约200%，Extended继续到更高值；
- Welt Skill同时存在Damage成长与Base Chance缓慢成长，说明“同一技能不同字段不同曲线”是可行模式。

这些只是具体角色事实，不是项目标准。

## Genshin Pattern

公开 Talent Level Scaling 数据显示存在多个Scaling Family：

- Normal/Physical Attack类；
- Elemental Percentage类；
- Flat Heal/Shield/Effect类；
- 少量特殊曲线。

同一技能里百分比值和Flat值可以使用不同Level Multiplier；某些机制的数值并非纯粹按通用曲线放大。

可迁移模式：

- 先按Parameter Type选择成长族；
- Throughput与Utility分离；
- 普攻与元素技能未必共享曲线；
- 特殊技能允许例外，但需要明确原因与回归测试。

不可直接迁移：具体1~15级Multiplier表、Talent上限、资源成本。

## Wuthering Waves Pattern

公开Forte/Skill页面常给出 Lv1~10 的完整Attribute Scaling表。

可观察到：

- 多个Damage字段从Lv1到Lv10接近约2倍量级，但每一级并非简单固定百分比；
- 不同Damage段可以保持相同曲线形状；
- Concerto Regen、Energy Cost、Cooldown等Utility/Economy字段经常保持固定；
- 多段技能、重击、共鸣技能、Forte等会共享或区分伤害分类；
- Sequence/共鸣链再叠加独立的倍率、触发、资源或规则升级。

公开例子中，Roccia Forte与其他技能页面可看到完整1~10数值表，同时Concerto Regen保持固定，说明“只成长Throughput、不成长所有字段”是一种常见结构。

## Cross-Game Shared Pattern

三个项目共同提示：

1. 技能等级不是“所有数字一起乘系数”；
2. Throughput参数最常持续成长；
3. Utility、Cost、Cooldown、Target Count等参数往往固定或低速成长；
4. 高阶成长节点可能改变机制，而不是继续叠倍率；
5. Extended Skill Level必须单独检查，因为它会和角色等级、装备、星级产生乘法叠加。

以上为 `supported-inference`。

## Benchmark Fields

每个外部技能至少记录：

- Character；
- Skill Type；
- Skill Level；
- Damage/Heal/Shield values；
- Buff/Debuff values；
- Base Chance；
- Duration；
- Cooldown；
- Resource Cost/Gain；
- Target Count；
- Hit Count；
- Fixed fields；
- Extended-level source；
- Source Date / Version。

## Normalization

跨技能比较优先：

`NormalizedSkillValue(s)=V(s)/V(max)`

`GrowthRatio=V(max)/V(1)`

`RelativeLevelDelta=V(s)/V(s-1)-1`

再结合：

`RealizedValue = PerUseValue × Frequency × TargetFactor × Reliability`

不要直接跨游戏比较“200% vs 300%”。

