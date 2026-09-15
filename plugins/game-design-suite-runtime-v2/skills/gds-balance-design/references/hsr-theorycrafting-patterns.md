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