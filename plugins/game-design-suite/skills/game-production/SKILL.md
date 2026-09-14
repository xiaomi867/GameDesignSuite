---
name: game-production
description: 负责游戏整体体验、玩法循环、系统规则、奖励框架、教程、产品节奏、制作范围、依赖和验证。适用于玩法策划、系统策划、现有系统诊断和跨系统方案设计；具体数值、经济、技能、关卡、配置或代码问题应与对应专业 Skill 协作。
---

# 游戏玩法与系统策划

把玩家体验目标转化为可执行、可测试、可交付的系统规则。

涉及跨系统绑定、系统参与度、强制依赖或“为了联动而联动”时，优先读取 [System Coupling & Anti-patterns](references/system-coupling-and-antipatterns.md)。

涉及 Roguelite、三选一、祝福/卡牌池、Build、体系成型、随机权重、保底、主/副体系或局内共鸣时，优先读取 [Roguelite Build Architecture](references/roguelite-build-architecture.md)。

涉及机制教学、局内节奏、玩法 Beat、决策密度、系统如何交给关卡承载时，优先读取 [Gameplay Structure & Pacing](references/gameplay-structure-and-pacing.md)。

## 先定义设计问题

明确：

- Player Promise / 玩家幻想；
- 重复动作与决策；
- 目标情绪与行为；
- 成功、失败、压力与恢复；
- Session 长度；
- 目标玩家与平台；
- 内容、制作和性能约束；
- 当前问题最小可验证切片。

只有不同答案会显著改变设计时才追问；否则声明假设并继续。

## 症状不等于方案

用户或项目暴露出来的“资源多、选择少、成长没感觉、参与度低、内容消耗快”等首先是症状。

禁止直接做以下跳跃：

- 资源多 -> 新增 Sink；
- 系统参与度低 -> 强制绑定奖励/成长；
- 卡没人选 -> 只加数值；
- 内容不够 -> 只加重复玩法；
- 成长慢 -> 直接提高所有产出。

先判断根因属于：局部参数、系统结构、内容生命周期、上下游耦合、信息/UX、制作约束或玩家目标错配。

## 已有项目优先读取现状

不得默认重做已有项目。根据任务需要检查：

- 当前规则和文档；
- 配置与数据；
- Telemetry / Playtest；
- 内容与地图；
- 必要代码；
- 当前制作边界。

用户要求“不改机制”时，机制属于 Fixed Rule，只能调整允许变化的 Tunables。

## 系统设计模板

对每个系统明确：

1. 玩家输入或决策；
2. 系统状态；
3. 触发与规则；
4. 系统响应；
5. 玩家反馈；
6. 结果与后果；
7. 与其他系统依赖；
8. Fixed Rules；
9. Tunable Parameters；
10. 正常、边界、失败、恢复和 Exploit 路径；
11. 最小原型/模拟；
12. 观察指标和决策规则。

## Gameplay Structure

系统不能只描述“有什么功能”，还必须描述玩家如何在时间中体验它。

优先建立：

`Observe -> Interpret -> Decide -> Act -> Feedback -> Update Plan`

并检查：

- 这一系统新增了什么玩家动词；
- 是深化已有动词，还是只增加数值/UI；
- 机制第一次如何被教会；
- 什么时候进入真正测试；
- 后续如何 Twist/Combine；
- 什么时候允许玩家休息、领奖和重规划；
- Session 内有多少高压力决策；
- 是否出现“菜单时间 > 实际玩法时间”。

### Mechanic Lifecycle

新机制应同时规划内容生命周期：

`Introduce -> Practice -> Test -> Twist -> Combine -> Mastery`

系统策划必须向关卡策划提供首次教学条件、安全网、可调参数、失败恢复、Twist 方向和不允许的组合，而不是把系统做完后让关卡“自己想办法塞进去”。

### Decision Budget

选择不是免费的。每个关键决策都有时间和认知成本。

至少检查：

- 影响范围；
- 不可逆性；
- 信息量；
- 后续持续时间；
- 与 Build/队伍的耦合；
- 是否连续出现高压力选择；
- 是否发生在本就高压的战斗阶段。

“更多三选一”不自动等于“更有 Roguelite 深度”。

### Gameplay Rhythm

玩法元素应承担不同节奏角色：

- Pressure；
- Choice；
- Reward；
- Recovery；
- Setup；
- Payoff；
- Twist；
- Closure。

如果所有系统都在制造选择，玩家会菜单疲劳；如果所有系统都只给奖励，体验会失去张力。

### Intensity != Difficulty

玩法强度可以来自：

- 重新规划；
- 信息压力；
- 时间压力；
- 资源危机；
- 场地/目标变化；
- 不确定性；
- 情绪赌注。

不要把节奏问题全部交给敌人加血加攻。

## System Coupling Legitimacy

跨系统联动必须回答：两个系统为什么要发生关系，这个关系给玩家增加了什么决策或能力。

优先级通常是：

`能力/解锁联动 > 效率联动 > 选择联动 > 内容联动 > 资源转换 > 直接收费绑定`

直接让系统 A 的资源成为系统 B 的强制成本，是最强耦合之一，必须谨慎。

任何跨系统强绑定至少检查：

- 玩家认知是否自然；
- 是否增加真实决策；
- 是否破坏原系统职责；
- 是否制造 Mandatory Tax；
- 是否使玩家被迫玩不喜欢的系统；
- 是否增加新角色/新内容切换成本；
- 是否可以用解锁、效率、制造、可选加速等更自然方式实现。

**跨系统联动 ≠ 跨系统互相收费。**

## 跨系统检查

任何修改都检查：

- 上游输入；
- 下游影响；
- 战斗；
- 成长；
- 经济；
- 任务；
- 活动；
- 商店；
- 关卡；
- 养成；
- 留存；
- UX；
- 教程；
- 商业化（若存在）。

局部系统不能当孤岛，但也不能为了“看起来有联动”强行增加耦合。

## Roguelite 构筑规则

局内 Build 不应退化为“同标签卡越多越好”。至少检查：

- Seed：玩家何时知道本局方向；
- Engine：几张卡后核心循环真正成立；
- Scaler：成型后如何继续成长；
- Stabilizer：生存/资源/容错怎么补；
- Capstone：何时出现质变和完成感；
- 主体系 + 副体系关系；
- Off-build 卡是否仍有合理用途；
- 核心组件在关键波次前的出现概率；
- Dead Pick Rate；
- 成型保底；
- Boss 是否能反向检验构筑。

### 三选一不是静态卡牌比较

每次选择的价值取决于：

- 当前 Build；
- 已有核心卡；
- 当前血量/资源；
- 距离 Boss 的阶段；
- 队伍构成；
- 后续成型概率；
- 当前选项的机会成本。

禁止只按“卡牌品质/裸倍率”排序。

### 构筑阈值

可通过同体系数量阈值、共鸣、成型件提供阶段性回报，但阈值数量必须由本项目一局选择次数推导，不照抄外部参考游戏。

### 动态随机

允许根据局内状态动态调整权重，例如：

- 已选体系；
- 连续未出主体系；
- Build 缺失组件；
- Boss 前生存不足；
- 奶妈存在且队伍低血；
- 已经完成引擎后降低重复低价值组件。

动态权重用于降低“随机系统拒绝玩家构筑”的挫败，不应保证每局完美成型。

### 随机玩法仍需结构保证

随机只意味着具体内容可变，不代表宏观节奏无需设计。

需要定义：

- 连续高压事件上限；
- 关键决策最小间隔；
- Boss 前恢复下限；
- 新机制首次出现的安全环境；
- Build 核心组件的最低可达性；
- P50/P90 Session 时长。

## 玩法策划关注点

### Core Loop
检查 `Act -> Feedback -> Reward -> Repeat` 是否闭合，内层输出是否支撑外层循环。

### Choice Quality
选项必须产生真实取舍。关注 Opportunity Cost、信息充分度和后果可读性。

### Failure & Recovery
失败原因可理解，存在恢复路径，避免形成“失败 -> 更弱 -> 更容易继续失败”的负循环。

### Onboarding
优先通过真实玩法教学。可参考：

`Introduce -> Practice -> Confirm -> Combine -> Apply Under Pressure`

不要一次引入多个新规则，也不要把弹窗当机制教学的默认替代品。

### Content Scope
内容数量必须与团队、周期和复用能力相匹配，不用“很多内容”代替预算。

同一机制能否通过环境、目标、敌人、时间和组合产生变奏，比单纯增加新机制数量更重要。

## 常见系统反模式

- **Forced Coupling**：为了联动而强行绑资源或进度；
- **Progression Hostage**：用一个系统卡住另一个系统核心成长；
- **Patch Stacking**：用新功能覆盖旧结构问题；
- **Mandatory Tax**：没有决策价值的固定消费；
- **Feature-as-Fix**：发现问题第一反应是再加一个系统；
- **Reward Bribery**：系统本身无价值，只靠奖励强迫参与；
- **Hollow Loop**：奖励不能反馈到下一层循环；
- **Complexity Over Depth**：规则增加而决策没有增加；
- **Same-color Drafting**：Roguelite 只剩同体系卡越拿越多；
- **Core-or-Brick**：没抽到单张核心卡整局直接报废；
- **Fake Choice Pool**：大量不属于当前 Build 的死选项；
- **Completed-build Lottery**：只平衡最终成型强度，不管成型概率；
- **Choice Spam**：选择密度高到吞掉实际玩法；
- **Difficulty-only Pacing**：用战力曲线替代节奏设计；
- **Mechanic Dump**：一次性把多个新系统扔给玩家；
- **Random = No Structure**：把“随机”当成“不需要编排”。

## 平台与性能

性能是设计约束。根据目标平台考虑同屏单位、Projectile、Physics、VFX、动画、UI 更新、后台模拟、网络、Streaming、CPU/GPU/内存等。

不凭直觉宣称“低端可运行”；需要 Profiling 或目标设备证据。

## 可执行交付

用户要求落地时，根据任务包含：

- Intent
- Player Outcome
- Rules
- States / Transitions
- Player Verbs
- Mechanic Lifecycle
- Decision Budget
- Rhythm Roles
- Tunables
- Dependencies
- Coupling Rationale
- Level Handoff
- Technical Touchpoints
- Exclusions
- Acceptance Scenarios
- Open Decisions

Roguelite 还应根据需要包含：

- Build Inventory；
- Core/Support/Capstone 标签；
- Pool / Weight；
- Completion Threshold；
- Pity / Guarantee；
- Build Completion Rate；
- Dead Pick 指标；
- Boss Check。

## 验证

- 规则：状态路径 walkthrough / 配置 / 实现检查
- 数值：交给 `balance-design`，再通过模拟/对照/实战数据
- 经济：交给 `economy-design`，同时检查 Resource Role 与 Sink Legitimacy
- 成长：交给 `progression-design`，检查 Cost Semantics 与 Switching Cost
- Roguelite：同时检查构筑成型概率、Dead Pick、Choice Quality、极端 Build、Boss Conversion
- 玩法节奏：与 `level-design` 联合检查 Beat、Decision Budget、休止符、峰值和真实时长
- 可用性：代表性用户测试
- 好玩：Playtest，不可由文档证明
- 性能：Profiling

## 专业分工

优先下沉：

- 关卡 -> `level-design`
- 技能 -> `skill-design`
- 战斗 -> `combat-design`
- 数值 -> `balance-design`
- 经济 -> `economy-design`
- 成长 -> `progression-design`
- UI/UX -> `game-interface-design`
- 配置 -> `config-audit`
- 代码 -> `code-verification`
