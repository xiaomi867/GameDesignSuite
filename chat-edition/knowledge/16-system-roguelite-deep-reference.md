# Game Design Suite Chat Edition — Systems & Roguelite Deep Reference

> Deep reference bundle for Chat Edition. Use for system coupling, Roguelite build architecture, decision budgets, pacing, and cross-system failure modes.


---

## Canonical source: references/system-coupling-and-antipatterns.md

# System Coupling & Anti-patterns

## 目的

用于判断两个系统应该如何发生关系，以及哪些“联动”其实只是强行绑定。

## 联动价值

跨系统联动应至少产生一种真实价值：

- 新能力；
- 新选择；
- 新策略；
- 效率变化；
- 内容访问；
- 风险/收益权衡；
- 资源转换；
- 信息或反馈变化。

如果唯一结果只是“多扣一种资源”，通常不是好的联动。

## Coupling Ladder

从弱到强通常可分：

1. 信息关联；
2. 解锁关联；
3. 效率关联；
4. 选择关联；
5. 资源转换；
6. 共享成本；
7. 强制依赖。

越往后越需要证明玩家价值和系统必要性。

## 评审问题

任何跨系统绑定至少检查：

- 为什么必须是这两个系统？
- 玩家能不能理解这层关系？
- 是否产生策略，不只是摩擦？
- 是否强迫玩家参与不喜欢的玩法？
- 是否破坏某个系统原本的独立职责？
- 是否提高切换角色/Build/内容的成本？
- 是否有更弱耦合但同样有效的方案？

## 反模式

### Forced Coupling
为了“系统互相有关”而强行共享资源/进度。

### Progression Hostage
用一个系统的资源卡另一个系统的核心成长。

### Reward Bribery
系统本身没有价值，只靠高奖励逼玩家参与。

### Feature-as-Fix
每遇到问题就再加一个系统。

### Patch Stacking
不断加补丁掩盖根因。

### Mandatory Tax
没有选择价值的固定消耗。

## 根因优先

出现“资源多、参与低、成长慢、内容消耗快”时，不先给方案。先判断：

- 是局部参数问题；
- 系统结构问题；
- 生命周期问题；
- 上下游错配；
- UX/信息问题；
- 制作容量问题。

只有根因确认后，才决定是否需要新增规则或系统。



---

## Canonical source: references/roguelite-build-architecture.md

# Roguelite Build Architecture

> 用途：参考《崩坏：星穹铁道》模拟宇宙类玩法中“路线/祝福/共鸣/跨路线补强”的设计经验，抽象成可复用的局内构筑框架。
>
> 边界：只学习构筑结构，不复制具体祝福、共鸣、出现概率或版本数值。

## 1. 构筑不是“同类卡越多越好”

好的 Roguelite 构筑至少包含四层：

1. **Seed / 种子**：告诉玩家本局大概往哪个方向走；
2. **Engine / 引擎**：让核心循环真正开始运转；
3. **Scaler / 放大器**：把已经成立的循环放大；
4. **Stabilizer / 稳定器**：补生存、资源、容错、覆盖率；
5. **Capstone / 成型件**：让 Build 出现质变或明确完成感。

如果只有“不断拿同标签 + 数值越来越大”，构筑会退化成收集同色卡。

---

## 2. 主体系与副体系

推荐用：

`1 主体系 + 1 副体系 + 少量通用生存/资源`

而不是要求玩家单一标签全拿。

### 主体系

决定：

- 主要伤害/控制/资源循环；
- 核心触发；
- Build Identity；
- 成型件。

### 副体系

负责：

- 弥补主体系缺点；
- 提供资源；
- 提高触发频率；
- 提高生存；
- 解决 Boss 特殊要求。

副体系不能比主体系更容易、更泛用，否则会反客为主。

---

## 3. Threshold Reward / 同体系数量阈值

成熟的局内构筑常用“收集若干同体系节点后解锁新能力”强化承诺感。

例如可设计：

- 3 件：解锁基础共鸣；
- 5/6 件：强化核心循环；
- 8/10 件：解锁成型效果；

具体数量由一局平均选择次数决定，不照抄外部游戏。

### 阈值价值

阈值应该提供：

- 新行为；
- 新循环；
- 新触发方式；
- 显著 Build Identity；

而不只是“伤害 +10%”。

---

## 4. Build Completion Probability

构筑体验不能只看单卡强度，还要看“能不能在合理时间成型”。

至少统计：

- P(核心卡在第 N 次选择前出现)；
- P(达到第一阈值)；
- P(达到完整引擎)；
- 平均成型波次；
- 最差 10% 成型波次；
- Dead Pick Rate；
- Forced Off-Build Pick Rate。

如果 Build 很强但只有少数幸运局能成型，不应只用完成态强度评价它。

---

## 5. Dynamic Weighting / 动态权重

随机池不能永远静态。

可根据当前局状态调整：

- 已选体系；
- 已选核心卡；
- 当前缺失组件；
- 玩家生命；
- Boss 距离；
- 资源状态；
- 是否已经连续错过主体系；
- 是否即将进入关键节点。

### 典型保护

- 主体系成型保底；
- 连续多轮未出核心时提高权重；
- 已完成引擎后降低重复低价值卡；
- Boss 前提高生存/修复选项；
- 奶妈存在且低血时提高治疗相关权重。

保底的目标是降低“系统拒绝玩家构筑”的挫败，不是保证每局必定完美。

---

## 6. Choice Quality

三选一不是“三张价值差不多的卡”就算合格。

每次选择至少要产生一个真实问题：

- 立即强度 vs 长期成型；
- 主体系深化 vs 副体系补短；
- 输出 vs 生存；
- 稳定性 vs 高波动；
- 引擎组件 vs 放大器；
- 当前关卡解法 vs 长期 Build。

如果一张卡在绝大多数局面都更优，就形成 Dominant Pick。

---

## 7. Conditional Power

高强度卡可以更强，但要通过条件换取预算。

条件可能是：

- 低生命；
- 高技能点消耗；
- 只对追加攻击；
- 只对 DoT；
- 只在击破/控制状态；
- 只在护盾存在；
- 需要连续叠层；
- 需要特定队伍构成。

数值策划应计算：

`Effective Power = Nominal Power × Expected Uptime × Trigger Reliability × Context Fit`

不要把条件卡按满覆盖价值定价。

---

## 8. Build Conversion / 旧牌不应轻易变废牌

体系升级时，应尽量让前期选择继续有价值。

例如：

- 基础触发 → 高阶触发仍使用同一资源；
- 旧叠层 → 成型后成为新机制燃料；
- 早期防御卡 → 后期可转化成输出；
- 基础标记 → 高阶技能消费标记。

避免出现“第 10 波拿到核心后，前 9 波选择全部作废”。

---

## 9. Negative Synergy / 负协同必须显式检查

常见负协同：

- 一个 Build 需要低血，另一个自动满血；
- 一个体系要求敌人存活叠层，另一个体系秒小怪；
- 一个体系需要消耗资源，另一个体系阻止资源消耗；
- 控制导致反击类机制无法触发；
- 行动提前破坏 Buff 持续窗口；
- 速度提升导致技能点循环转负。

局内池若同时提供互斥组件，应让玩家能识别，而不是形成隐藏陷阱。

---

## 10. Resonance / 共鸣型能力的作用

“共鸣”类系统最有价值的不是再送一个按钮，而是：

- 明确本局身份；
- 让收集同体系的行为有阶段回报；
- 提供可预测的构筑里程碑；
- 在随机环境中给玩家一定确定性；
- 让高层构筑有一个统一输出口。

共鸣必须与体系行为绑定，不能只是独立的大招伤害。

---

## 11. Off-Path Picks / 非主体系卡的价值

非主体系卡要有合理角色：

- 生存补丁；
- 资源补丁；
- 通用增益；
- Boss 对策；
- 临时过渡；
- 与主体系形成跨体系联动。

如果所有非主体系卡都是“垃圾选项”，随机系统会变成找同色卡而不是决策。

---

## 12. 体系测试矩阵

每个体系至少测：

| 维度 | 问题 |
|---|---|
| Seed | 第一张是否能让玩家理解方向 |
| Engine | 几张卡后核心循环成立 |
| Scaling | 中后期如何继续成长 |
| Survival | 输出体系是否必须额外补生存 |
| Resource | 是否会卡怒气/技能点/触发资源 |
| Boss | 对单体、高血、免控、阶段 Boss 是否成立 |
| Variance | 核心卡没来时还能否玩 |
| Cross-build | 有哪些自然副体系 |
| Dead Pick | 哪些卡在大量局面无价值 |
| Ceiling | 极端组合是否无限叠加/失控 |

---

## 13. 局内数值指标

建议记录：

- Pick Rate；
- Win Rate when Picked；
- Win Rate Conditional on Stage；
- Average Pick Position；
- Skip Rate；
- Build Completion Rate；
- Main Path Share；
- Cross-Path Share；
- Dead Pick Rate；
- Damage Contribution；
- Survival Contribution；
- Resource Contribution；
- Time-to-Online；
- Boss Conversion Rate。

不要只看“这张卡选得多不多”。高 Pick 可能只是池子太差，也可能是它无条件主导。

---

## 14. 不照抄参考游戏

值得学习：

- 体系标签；
- 阈值成型；
- 主/副体系；
- 共鸣里程碑；
- 随机构筑中的确定性保护；
- 条件卡与角色机制联动；
- Boss 对构筑的反向检验。

不应该照抄：

- 同体系祝福数量；
- 共鸣解锁数量；
- 祝福稀有度；
- 强化倍率；
- 路线数量；
- 具体随机权重。

所有数量都应根据当前项目“一局能做多少次选择、多久到 Boss、队伍有几个核心机制”重新设计。


---

## Canonical source: references/gameplay-structure-and-pacing.md

# Gameplay Structure & Pacing

> 用途：玩法策划在设计机制、局内循环、事件结构和 Session 时，避免只设计“系统功能”，忽略学习、节奏和决策负荷。

## 1. Gameplay Is a Sequence of Decisions

系统不是因为“功能完整”就成立。要明确玩家在一段体验里反复经历什么：

`Observe -> Interpret -> Decide -> Act -> Feedback -> Update Plan`

玩法价值来自这个循环产生的有意义变化。

## 2. Mechanic Lifecycle

一个新机制通常需要经历：

`Introduce -> Practice -> Test -> Twist -> Combine -> Mastery`

设计系统时同步规划它如何被关卡/波次使用，而不是系统做完后再让关卡“找地方塞”。

## 3. Verb First

先确定玩家动词，再确定内容数量。

例如：

- 选择；
- 攻击；
- 防御；
- 规避；
- 组合；
- 投资；
- 赌风险；
- 探索；
- 转换资源。

新增系统必须说明它是否增加新动词、深化旧动词，还是只增加 UI 和数值层。

## 4. Decision Budget

Session 有决策预算。

不是“选择越多越 Roguelite”。

每个关键决策要记录：

- 影响范围；
- 不可逆性；
- 信息量；
- 与后续 Build 的关系；
- 选择所需时间；
- 是否在高压力状态下出现。

连续高压决策会产生菜单疲劳。

## 5. Rhythm of System Roles

玩法元素应承担不同节奏角色：

- Pressure；
- Choice；
- Reward；
- Recovery；
- Setup；
- Payoff；
- Twist；
- Closure。

如果所有系统都在“给玩家做选择”，会没有节奏；如果所有系统都只给奖励，会没有张力。

## 6. Freeze Vocabulary Before Optimization

当游戏既有“解锁新能力”又有“强化已有能力”时，要明确能力池什么时候稳定。

如果玩家还不知道本局能做什么，就让他连续投资强化，决策可能没有参考基准。

因此先问：

- 能力池何时建立？
- Build Seed 何时出现？
- 强化从何时开始有意义？
- 中途是否允许转型？转型成本多少？

## 7. Intensity ≠ Difficulty

玩法强度可以来自：

- 重规划；
- 信息压力；
- 时间压力；
- 资源危机；
- 目标改变；
- 不确定性；
- 情绪赌注。

不要把节奏问题全部用“敌人加血加攻”解决。

## 8. Rest and Recovery

低强度阶段承担：

- 消化刚学的规则；
- 看奖励；
- 重新规划 Build；
- 恢复资源；
- 建立下一目标。

休止符是玩法结构的一部分，不是空白。

## 9. Random Gameplay Needs Structural Guarantees

随机玩法要区分：

- 内容随机；
- 结构随机；
- 奖励随机；
- Build 随机。

优先保证宏观结构不被随机完全破坏，例如：

- 高压事件最大连续数；
- Boss 前恢复下限；
- 关键 Build 组件保底；
- 新机制首次出现的安全环境；
- 重大决策之间的最小间隔。

## 10. Negative Feedback as Gameplay

负反馈必须产生玩法价值，而不是纯惩罚。

更好的负反馈：

- 玩家主动选择风险；
- 有明确收益交换；
- 改变短期策略；
- 能被后续系统回应；
- 有恢复窗口。

## 11. System-to-Level Contract

每个系统交给关卡前至少说明：

- 首次教学条件；
- 最低安全空间；
- 可调参数；
- 适合的敌人/目标；
- 失败恢复；
- Twist 方向；
- 不允许的组合；
- 需要的 UI/反馈；
- 埋点。

## 12. Anti-patterns

- **System First, Experience Later**：先做功能，再想玩家怎么玩；
- **Choice Spam**：选择过密导致疲劳；
- **Reward Spam**：反馈过密导致无感；
- **Mechanic Dump**：一次塞太多新规则；
- **Difficulty-only Pacing**：节奏只靠战力控制；
- **Random = No Structure**：用随机逃避编排；
- **One-off Mechanic**：开发成本高，只出现一次；
- **Menu Takes Over Play**：局内主要时间花在选菜单而不是实际玩法。

