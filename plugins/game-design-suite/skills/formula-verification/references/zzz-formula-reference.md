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
