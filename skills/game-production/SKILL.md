---
name: game-production
description: 负责游戏整体体验、玩法循环、系统规则、奖励框架、教程、产品节奏、制作范围、依赖和验证。适用于玩法策划、系统策划、现有系统诊断和跨系统方案设计；具体数值、经济、技能、关卡、配置或代码问题应与对应专业 Skill 协作。
---

# 游戏玩法与系统策划

把玩家体验目标转化为可执行、可测试、可交付的系统规则。

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

局部系统不能当孤岛。

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
- Technical Touchpoints
- Exclusions
- Acceptance Scenarios
- Open Decisions

## 验证

- 规则：状态路径 walkthrough / 配置 / 实现检查
- 数值：交给 `balance-design`，再通过模拟/对照/实战数据
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
