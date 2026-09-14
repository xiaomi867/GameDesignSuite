---
name: game-production
description: 负责游戏整体体验、玩法循环、系统规则、奖励框架、教程、产品节奏、制作范围、依赖和验证。适用于玩法策划、系统策划、现有系统诊断和跨系统方案设计；具体数值、经济、技能、关卡、配置或代码问题应与对应专业 Skill 协作。
---

# 游戏玩法与系统策划

把玩家体验目标转化为可执行、可测试、可交付的系统规则。

涉及跨系统绑定、系统参与度、强制依赖或“为了联动而联动”时，优先读取 [System Coupling & Anti-patterns](references/system-coupling-and-antipatterns.md)。

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

## 玩法策划关注点

### Core Loop
检查 `Act -> Feedback -> Reward -> Repeat` 是否闭合，内层输出是否支撑外层循环。

### Choice Quality
选项必须产生真实取舍。关注 Opportunity Cost、信息充分度和后果可读性。

### Failure & Recovery
失败原因可理解，存在恢复路径，避免形成“失败 -> 更弱 -> 更容易继续失败”的负循环。

### Onboarding
推荐 `Introduce -> Practice -> Confirm -> Combine -> Apply Under Pressure`。

### Content Scope
内容数量必须与团队、周期和复用能力相匹配，不用“很多内容”代替预算。

## 常见系统反模式

- **Forced Coupling**：为了联动而强行绑资源或进度；
- **Progression Hostage**：用一个系统卡住另一个系统核心成长；
- **Patch Stacking**：用新功能覆盖旧结构问题；
- **Mandatory Tax**：没有决策价值的固定消费；
- **Feature-as-Fix**：发现问题第一反应是再加一个系统；
- **Reward Bribery**：系统本身无价值，只靠奖励强迫参与；
- **Hollow Loop**：奖励不能反馈到下一层循环；
- **Complexity Over Depth**：规则增加而决策没有增加。

## 平台与性能

性能是设计约束。根据目标平台考虑同屏单位、Projectile、Physics、VFX、动画、UI 更新、后台模拟、网络、Streaming、CPU/GPU/内存等。

不凭直觉宣称“低端可运行”；需要 Profiling 或目标设备证据。

## 可执行交付

用户要求落地时，根据任务包含：

- Intent
- Player Outcome
- Rules
- States / Transitions
- Tunables
- Dependencies
- Coupling Rationale
- Technical Touchpoints
- Exclusions
- Acceptance Scenarios
- Open Decisions

## 验证

- 规则：状态路径 walkthrough / 配置 / 实现检查
- 数值：交给 `balance-design`，再通过模拟/对照/实战数据
- 经济：交给 `economy-design`，同时检查 Resource Role 与 Sink Legitimacy
- 成长：交给 `progression-design`，检查 Cost Semantics 与 Switching Cost
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
