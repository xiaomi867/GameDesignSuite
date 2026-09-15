---
name: skill-value-design
description: 负责技能等级对应的数值成长与参数预算，包括伤害/治疗/护盾倍率、Buff/Debuff数值、概率、持续、资源、冷却、层数、技能等级曲线、不同参数的升级策略与Lv1~上限增长。用于设计或审计技能数值表、技能等级收益和升级性价比；机制结构交给 hero-kit-design，公式语义交给 formula-verification，角色总体强度交给 balance-design。
---

# Skill Value Design / 技能数值设计

目标不是“把Lv1倍率乘到Lv10”，而是让每个技能参数的成长方式与其职责、触发频率、循环位置、资源成本和角色定位一致。

优先读取：

- [Cross-Game Skill Scaling Patterns](references/cross-game-skill-scaling-patterns.md)
- [Skill Value Audit Template](templates/skill-value-audit.md)

## 强制用户可见输出协议（MUST）

每一个独立技能倍率、技能等级曲线、Buff数值、概率/持续成长、资源/冷却参数或技能升级价值结论前，都先显示：

```text
【本次专业视角】
主责：技能数值策划（skill-value-design）
协同：仅列当前结果真实使用的专业
```

常见协同：

- `hero-kit-design`：确认技能职责、触发频率、循环位置；
- `hero-stat-progression`：检查角色等级属性与技能等级的联合放大；
- `hero-concept-design`：确认数值重点是否强化角色身份；
- `balance-design`：角色总体Power Budget、横向强度；
- `formula-verification`：倍率对象、乘区、Clamp、Round、Snapshot；
- `simulation-design`：Rotation、触发频率、Crit/Target随机分布；
- `config-audit` / `code-verification`：技能等级映射与真实实现。

Direct Specialist Entry 仍执行共享 First-Visible-Line / Section Gate / Pre-Send Header Lint。

---

## 1. Parameter Taxonomy / 先分参数类型

任何技能等级表先把字段分类。

### Throughput Parameters
- Damage Multiplier；
- Heal Ratio / Flat Heal；
- Shield Ratio / Flat Shield；
- Additional Damage；
- DoT / Tick Value。

### Amplification Parameters
- DMG Bonus；
- Vulnerability；
- Crit / Crit DMG；
- DEF/RES Shred；
- Speed/Action modifier；
- Healing/Shield Bonus。

### Reliability Parameters
- Base Chance；
- Hit Count；
- Target Count；
- Stack Cap；
- Trigger Interval；
- Duration；
- Threshold。

### Economy Parameters
- Energy/Rage Cost；
- Resource Gain；
- Cooldown；
- Charge Count；
- Shared-resource cost/generation。

### Structural Parameters
- Target Rule；
- Trigger Rule；
- State Change；
- Skill Replacement；
- Extra Action；
- Follow-up/Counter unlock。

结构参数通常不是简单等级数值；如果升级改变结构，应转 `hero-kit-design` 评估。

---

## 2. Skill Value Contract

每个可升级技能至少记录：

- Skill Job；
- Scaling Source；
- Base Level；
- Normal Max Level；
- Extended Max（星魂/命座/加级时）；
- Use Frequency；
- Resource Cost；
- Target Count；
- Trigger Reliability；
- Damage/Heal/Shield Type；
- Crit Eligibility；
- Level-Scaled Fields；
- Fixed Fields；
- Upgrade Cost；
- Expected Power Delta per level。

没有这些上下文，不直接评价“200%高不高”。

---

## 3. Scaling Families

技能参数可以使用不同增长族。

### Standard Percentage Curve
`V(s)=V1 * M(s)`

适合常规伤害/治疗百分比。

### Flat Curve
Flat值可使用独立Multiplier，避免与百分比值完全同步。

### Additive Step
`V(s)=V1 + Δ(s)`

适合概率、减伤、资源等需要严格边界的参数。

### Milestone Growth
只在特定技能等级增加关键参数，其他等级增长主倍率。

### Fixed Utility
CD、持续、资源回复、目标数等保持固定，只让主要Throughput成长。

### Diminishing Utility
功能参数前期增长较快、后期趋缓，防止控制/减伤/概率接近系统上限。

禁止“一张统一倍率表套所有字段”。

---

## 4. Level Delta / 每级价值

至少计算：

`AbsoluteDelta(s)=V(s)-V(s-1)`

`RelativeDelta(s)=V(s)/V(s-1)-1`

对于最终战斗输出还可计算：

`RealizedPowerDelta = ΔOutput / BaselineOutput`

目标不是每级完全等价值，而是明确：

- 哪些等级是普通成长；
- 哪些是关键节点；
- Lv9->10为何更贵；
- +2技能等级是否过度提高角色；
- 技能加级是否让某参数突破上限/Breakpoint。

---

## 5. Throughput Scaling

伤害/治疗/护盾倍率不能只看单次值。

至少结合：

`PerUseValue × UseFrequency × TargetFactor × Reliability × Uptime`

多段技能再考虑：

- Hit distribution；
- 是否所有段都能命中；
- 是否可切目标；
- 单体/群体环境；
- 条件段/追加段；
- 动画时间与行动成本。

一个1000%但每30秒一次的技能，不自动比200%每3秒一次强。

---

## 6. Utility Scaling Guard

概率、减伤、控制时长、易伤、穿透、行动提前等参数比伤害倍率更容易出现非线性。

必须检查：

- Cap / Clamp；
- 100%附近的边际变化；
- 与Effect Hit / Resist的组合；
- Duration是否跨过一次额外行动；
- SPD/Action是否跨Breakpoint；
- DEF/RES是否进入异常高收益区；
- Reduction是否接近免伤；
- Stack Cap是否导致组合爆炸。

Utility值不能默认与Damage值使用同一成长倍率。

---

## 7. Fixed vs Scaled Fields

一个技能描述中并非所有数字都应该随等级成长。

常见固定字段：

- CD；
- Energy Cost；
- Target Count；
- Duration；
- Resource Gain；
- Stack Cap；
- Toughness / Gauge Value；
- Trigger Interval。

常见成长字段：

- Damage/Heal/Shield；
- 部分Buff/Debuff；
- 部分Base Chance；
- 部分Action/Delay参数。

但具体项目必须根据循环验证。

如果所有字段一起成长，角色高技能等级可能同时获得 Throughput + Reliability + Economy 三重放大。

---

## 8. Skill Level Cap / Extended Levels

必须区分：

- Normal Max；
- Temporary/Equipment Bonus；
- Star/Eidolon/Constellation +Level；
- System Hard Cap。

检查Extended Level：

- 是否继续按同一曲线；
- 是否只提高部分字段；
- 是否出现超出UI/配置上限；
- +2技能等级的真实Power Delta；
- 是否让星级节点的价值异常集中。

---

## 9. Character Level × Skill Level

技能等级不能脱离角色基础属性。

联合模型：

`Output(L,S) = ScalingStat(L) × SkillValue(S) × Multipliers`

至少采样：

- 低角色等级 + 低技能等级；
- 中段匹配等级；
- 满角色等级 + 常规技能满级；
- 满角色等级 + Extended Skill Level。

检查：

- 是否前期过弱；
- 中期是否突然跃迁；
- 后期是否乘法膨胀；
- 星级/命座加级是否放大过度。

---

## 10. Rotation-Level Budget

技能数值最终必须回到完整Rotation。

统计：

- 每分钟/每循环施放次数；
- 技能占总输出/治疗/护盾比例；
- Buff覆盖；
- 资源净流；
- 低频高爆发 vs 高频稳定；
- 被动/追击的隐性贡献；
- Team Amplification。

建议输出 Contribution Share：

`SkillContribution = SkillExpectedValue / TotalRotationValue`

一个角色如果核心技能只占5%贡献，可能存在Mechanic/Numeric mismatch。

---

## 11. Upgrade Cost Alignment

如果技能升级需要资源，检查：

`Power Delta per Cost`

不是要求所有技能性价比完全一样，而是避免：

- 某技能升级几乎没有收益；
- 某被动一升就远超其他技能；
- Utility技能因数值不增长变成“永远不升级”；
- 最后一级成本暴涨但Power Delta没有对应价值。

长期材料与资源循环由 `progression-design + economy-design` 协同。

---

## 12. External Reference Boundary

外部商业游戏可用于研究：

- Skill Level Cap；
- 不同字段使用不同Scaling Family；
- 基础攻击与核心技能是否使用不同曲线；
- 固定Utility与成长Throughput如何分工；
- 高阶加级如何延伸曲线。

外部倍率只能作为 `reference-data`；不得把“某游戏Lv10约为Lv1的2倍”写成通用标准。

---

## 13. Cross Validation

### hero-concept-design
数值重点是否强化角色身份？

### hero-kit-design
倍率最高的动作是否真的是核心Payoff？触发频率是否匹配？

### hero-stat-progression
技能成长与角色属性成长组合后是否仍可控？

### formula-verification
倍率到底乘哪个属性、在哪个乘区、如何Round/Clamp？

### balance-design
完整角色而非单技能是否落在目标Power Budget？

---

## 14. Done Criteria

一次技能数值任务至少交付：

- Parameter Taxonomy；
- Skill Value Contract；
- Lv1~Max完整曲线；
- 每级Absolute/Relative Delta；
- Fixed vs Scaled字段；
- Extended Level；
- Character Level × Skill Level联合检查；
- Rotation Contribution；
- Utility边界/Breakpoint；
- 升级成本性价比；
- Evidence Boundary；
- Simulation/Runtime验证项。

## 15. 反模式

- **One Curve Fits All**：所有字段同一倍率表；
- **Single-Hit Bias**：只看单次倍率；
- **Utility Runaway**：控制/减伤/概率和伤害一样高速成长；
- **Invisible Upgrade**：技能升级玩家几乎无感；
- **Level Cliff**：某一级突然暴涨但无设计理由；
- **Triple Growth**：Throughput、Reliability、Economy同时随等级增强；
- **Extended-Level Explosion**：加技能等级导致异常放大；
- **Stat×Skill Blindness**：只看技能曲线，不看角色基础属性联合成长；
- **External-Copy Curve**：直接抄成熟游戏技能等级倍率表。
