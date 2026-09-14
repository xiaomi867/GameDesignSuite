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
