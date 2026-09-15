# Canonical Detailed Guidance

> Preserved from the canonical Game Design Suite specialist. The runtime wrapper is intentionally compact; this file retains the detailed domain rules, workflows, guards, anti-patterns, and done criteria.

# Hero Stat Progression / 英雄等级属性成长

目标不是把 Lv1 和 LvMax 两个数字插值，而是建立**可解释、可复现、能与技能/内容/成长成本联动**的角色属性曲线。

优先读取：

- [Cross-Game Character Stat Growth Patterns](cross-game-character-stat-growth-patterns.md)
- [Hero Stat Curve Audit Template](../templates/hero-stat-curve-audit.md)

## 强制用户可见输出协议（MUST）

每一个独立等级曲线、突破跳变、基础属性模板、成长副属性、阶段Power Delta或成长异常结论前，都先显示：

```text
【本次专业视角】
主责：英雄成长数值（hero-stat-progression）
协同：仅列当前结果真实使用的专业
```

常见协同：

- `hero-concept-design`：确认体质与角色身份一致；
- `hero-kit-design`：确认技能Scaling Source与资源循环；
- `skill-value-design`：检查角色等级成长与技能等级成长是否重复放大；
- `progression-design`：等级上限、突破节点、成本与解锁；
- `balance-design`：阶段强度、横向Power Budget与敌我Benchmark；
- `formula-verification`：属性进入伤害/防御/治疗公式的真实方式；
- `simulation-design`：全等级参数扫描、Breakpoint与极端成长；
- `config-audit` / `code-verification`：真实表与Runtime读取。

Direct Specialist Entry 仍执行共享 First-Visible-Line / Section Gate / Pre-Send Header Lint。

---

## 1. Stat Taxonomy / 先分属性类型

任何成长表先把属性分类：

### Level-Scaled Base Stats
常见：HP、ATK、DEF。

### Fixed/Mostly-Fixed Combat Stats
常见：基础速度、能量上限、基础暴击率、基础暴伤、嘲讽/仇恨权重等。

### Ascension / Breakthrough Bonus Stat
例如暴击、伤害加成、元素/属性伤害、治疗、效果命中、特殊效率等。

### Node-Based Stats
通过行迹/天赋树/技能树节点获得，而不是角色等级自动增长。

### Derived Stats
由公式计算，例如战力、EHP、DPS、实际行动频率。

禁止把所有属性都塞进同一等级插值公式。

---

## 2. Growth Contract

建立曲线前明确：

- Level Cap；
- Breakthrough / Ascension Levels；
- Lv1 Base；
- LvMax Base；
- 每次突破是否直接加属性；
- 突破后是否重置/改变成长斜率；
- Bonus Stat在哪些阶段增加；
- 稀有度/职业是否共享模板；
- 哪些属性固定；
- 目标内容曲线；
- 玩家每个阶段应感知的Power Delta。

必须检查：

`Power Curve <-> Content Curve <-> Cost Curve <-> Time Curve`

---

## 3. Curve Families

允许的曲线族包括：

### Linear
`V(L)=V1 + k*(L-1)`

适合可读、稳定、易预测的成长。

### Piecewise Linear
不同突破区间使用不同斜率。

### Multiplier Table
`V(L)=BaseTemplate * LevelMultiplier(L) + AscensionDelta(Phase)`

适合多个角色共享统一成长形状但拥有不同基础模板。

### Exponential / Power Curve
仅在设计目的明确且有长期数值空间时使用。必须检查后期膨胀。

### Hybrid
基础属性采用Multiplier，突破使用离散Delta，特殊属性通过节点增加。

不能因为某成熟游戏使用某种曲线，就直接复制其Multiplier表。

---

## 4. Normalized Growth

跨角色/跨游戏比较时不要直接比绝对数。

常用：

`Normalized(L) = V(L) / V(Lmax)`

`GrowthFromBase(L) = V(L) / V(1)`

`MarginalGrowth(L) = V(L) - V(L-1)`

`PhaseDelta = V(after ascension) - V(before ascension)`

`PhaseShare = PhaseDelta / V(Lmax)`

这样可以区分：

- 同样LvMax，谁前期更强；
- 哪个系统把Power放在突破；
- 哪些阶段增长过密或过空；
- 是否存在“十级几乎没感觉，突破瞬间暴涨”。

---

## 5. Roster Stat Envelope

建立角色池的属性包络：

- Min / P25 / Median / P75 / Max；
- 同角色职责内分布；
- 同稀有度内分布；
- 同Scaling Source内分布；
- 不同等级阶段的分布。

例如：

- Tank不一定必须全属性最高，但应在其生存核心指标有可解释优势；
- 高速角色的低ATK是否被行动次数补偿；
- HP/DEF双成长是否形成异常EHP；
- Healer的基础体质是否支持其站场/受击预期。

避免“每个新角色都比旧角色基础属性略高一点”的隐性Power Creep。

---

## 6. Scaling-Source Alignment

角色成长必须和 Kit 的Scaling Source交叉验证。

检查：

- 主要伤害吃ATK，ATK成长是否合理；
- Tank以DEF输出，DEF成长是否同时过度提高生存与输出；
- HP治疗+HP生存是否形成Double Scaling；
- 高速角色是否因速度固定而无法体现设定；
- 能量上限与技能循环是否匹配；
- 暴击/命中等Bonus Stat是否恰好补角色需求，还是强行制造专属答案。

如果一个属性同时提高多个主要输出维度，必须交 `balance-design` 做Effective Power检查。

---

## 7. Ascension / Breakthrough Design

突破节点可以承担：

- 等级上限提升；
- Base Stat jump；
- Bonus Stat；
- Major Passive；
- Skill Level Cap；
- 新机制解锁。

检查：

- 是否有可感知收益；
- 是否一次性给太多Power；
- 是否强迫玩家突破才能让角色“能用”；
- 是否和内容门槛形成硬锁；
- 是否出现等级成长+突破+技能解锁同一节点多重爆发。

建议记录每个节点：

`TotalPowerDelta = BaseStatDelta + BonusStatDelta + UnlockValue + SkillCapValue`

这是分析框架，不要求把不同价值机械相加。

---

## 8. Growth Density / 成长密度

把Lv1~LvMax划分阶段，计算：

- 每10级或每阶段属性增长；
- 突破跳变；
- 技能等级上限变化；
- 被动解锁；
- 装备/系统同步开放。

目标不是每一级收益相同，而是避免：

- Dead Levels；
- Power Cliffs；
- 多系统同点爆炸；
- 前期成长过快导致内容失效；
- 后期成长过慢导致升级无感。

---

## 9. Cross-Validation With Skill Levels

角色等级和技能等级往往同时成长，因此必须检查乘法叠加。

概念式：

`Output(L,S) = BaseStat(L) × SkillMultiplier(S) × OtherMultipliers`

若BaseStat从Lv1到满级提升3倍，Skill倍率又提升2倍，则基础输出可出现约6倍放大，还未计算装备/暴击/增伤。

所以不能分别看：

- “属性曲线很平滑”；
- “技能倍率曲线也很平滑”；

然后默认组合后仍然平滑。

必须做二维检查：

`Character Level × Skill Level`。

---

## 10. Fixed Stat Guard

速度、能量、暴击等属性是否随等级成长必须是明确设计决定。

固定属性的好处：

- 循环稳定；
- Build阈值可控；
- 角色身份清晰。

成长属性的风险：

- Breakpoint随等级漂移；
- 低级体验与高级体验不是同一角色；
- 配装目标不断移动。

不要因为HP/ATK/DEF成长，就默认所有属性都应该成长。

---

## 11. External Benchmark Boundary

公开商业游戏角色页可用于研究：

- 等级上限与突破节点；
- 哪些基础属性随等级变化；
- 哪些属性固定；
- 成长副属性如何在突破中投放；
- 技能等级上限如何被突破约束。

但必须记录 Source Date / Version。外部网站可能滞后于当前版本；例如某站点仍显示旧等级上限时，不得把它写成当前项目的“行业标准”。

---

## 12. Statistical / Formula Checks

至少根据任务检查：

- Monotonicity；
- Integer/decimal rounding；
- Level boundary continuity；
- Ascension pre/post values；
- Min/Max outliers；
- Rank-order stability；
- Growth ratio；
- Marginal gain；
- Power Elasticity；
- Breakpoint crossings。

表格计算只能证明数学结果，不能证明体验良好。

---

## 13. Done Criteria

一次英雄等级数值任务至少交付：

- 属性分类；
- Lv1 / 关键突破 / LvMax快照；
- 成长公式或Multiplier表；
- 突破Delta；
- Bonus Stat投放；
- Roster Envelope；
- Scaling Source Alignment；
- Character Level × Skill Level联合检查；
- 异常/Breakpoint；
- Evidence Boundary；
- 需要Simulation/Runtime/Playtest的下一步。

## 14. 反模式

- **Two-Point Interpolation**：只给Lv1/LvMax，中间无验证；
- **All-Stats Growth**：所有属性一起线性涨；
- **Ascension Power Cliff**：突破节点强度断层；
- **Dead Levels**：长区间升级几乎无感；
- **Double-Scaling Blindness**：属性和技能分别合理，组合后爆炸；
- **Role/Stat Mismatch**：角色职责与基础成长方向相反；
- **Cross-Game Copy**：直接复制外部游戏等级Multiplier；
- **Version Blindness**：引用旧Wiki等级上限却当当前事实。
