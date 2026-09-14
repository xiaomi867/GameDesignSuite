---
name: design-review
description: 对已有游戏概念、GDD、机制、技能、英雄、战斗、经济、成长、关卡、UI、原型、配置方案或 Playtest 结果进行评审、比较和压力测试。识别弱点、矛盾、主导策略、False Choice、失衡和证据缺口，并给出最小有效修改与下一步验证实验。
---

# 游戏设计评审

评审是决策辅助，不是万能清单，也不能替代 Playtest。

## 1. 定义评审对象与决策

先明确：

- Review Object
- Decision at Stake

若没有明确决策，找最重要的未解决假设。

## 2. Evidence Baseline

整理：

- `confirmed`
- `assumed`
- `unknown`

必要时使用专业 Skill 获取配置、代码、数值等证据。

历史方案、用户建议和 AI 先前结论都不是自动成立的事实，必须接受同样的证据审查。

## 3. Review Modes

### Focused
一个技能、一段规则、一个小系统。

### Comprehensive
完整 GDD、复杂系统、多表/多模块，需要跨域矛盾检查。

### Exploratory
方向未确定：提出 2~3 个候选方向和能区分它们的小实验。

### Comparative
比较 A/B/多方案，必须使用相同证据和标准。

## 4. Root Cause Pass

每个重大问题先区分：

1. **Symptom**：玩家/数据/配置表面发生了什么；
2. **Mechanism**：什么规则导致它；
3. **Root Cause**：问题真正来自局部参数、系统结构、内容生命周期、信息/UX、上下游依赖还是制作约束；
4. **Patch Risk**：当前建议是不是只在症状上打补丁。

如果建议只是“新增 Sink、增加奖励、再加一个功能、强制绑定另一个系统、直接加倍率”，默认进入反模式检查。

## 5. Finding 质量

每个重要 Finding 包含：

- Observation
- Mechanism
- Evidence Status
- Root Cause
- Impact
- Recommendation
- Tradeoff
- Validation

推荐最小改动，不默认新增功能。

## 6. 常见风险与反模式

按相关性选择，不机械全查：

### 选择与玩法
- Dominant Strategy
- False Choice
- No Opportunity Cost
- Hollow Loop
- Complexity Over Depth
- Unclear Telegraph
- Recovery Failure

### 英雄与技能
- Button Zoo
- Passive Soup
- Multiplier-only Design
- Role by Label
- Resource Orphan
- Trigger Lottery / Trigger Starvation
- Pair Lock / Team Tax
- Stat Split Tax
- Overloaded Skill
- Dead Slot / Dead Rank
- Window Spill
- Identity Locked Late
- Problem-Sell-Solution
- Direct Replacement / Roster Power Creep

### 战斗与 Encounter
- All-phase Carry
- Gauge as Extra HP
- Shared Resource Blindness
- Reaction Monopoly
- Permanent Burst
- System Invalidation
- Boss Immunity Soup
- DPS Dummy Level
- Window Theft

### 数值与成长
- Power Creep / Treadmill
- Math-washing
- Average-only Balance
- Progression Hostage
- Tax Ladder
- Switching Punishment

### 经济
- Sink for Sink's Sake
- Mandatory Tax
- Resource Everywhere
- Currency Soup
- Production Inflation Patch
- Late-game Dead Currency
- Reward Bribery

### 系统结构
- Forced Coupling
- Patch Stacking
- Feature-as-Fix
- Hidden Dependency
- Cross-System Conflict
- Content/Production Overreach

### 实现与证据
- Config Exists != Runtime Works
- Code Reads != Path Triggers
- Spreadsheet != Playtest
- Historical Conclusion != Verified Fact

发现这些模式时，优先解释“为什么它会发生”，而不是直接给一个更复杂的新系统。

## 7. Hero/Kit Review

评审英雄或技能时，不只看技能文本和倍率。至少检查：

- Core Loop 是否一句话能说清；
- State Machine 是否明确；
- Resource Graph 是否闭环；
- Generator / Setup / Payoff / Recovery 是否都有意义；
- Phase Ownership；
- Field/Action Time；
- Team Hook 与 Pair Lock 风险；
- Trigger Reliability；
- Failure Case；
- Skill Tree 是否有里程碑，而不是全加数；
- 高阶节点是否只是修基础缺陷；
- 升级的 Paper Value 是否能在真实窗口兑现；
- Encounter 是否允许核心机制发生。

如果角色只能在木桩环境成立，或必须依赖唯一队友/特定 Boss 行为，不能只用高倍率解释为“定位特色”。

## 8. Sink / Cost Legitimacy Review

任何新增资源消耗或成长成本都检查：

- Resource Role 是否匹配；
- Fantasy/System Fit 是否成立；
- 是否产生真实决策；
- 是否只是为了消库存；
- 是否是 Source 过高或生命周期断层；
- 是否把一个系统的人为问题转嫁给另一个系统；
- 是否存在更自然的能力/效率/解锁联动。

不能因为“经济闭环”看起来更完整，就通过不合理 Sink。

## 9. Tradeoff

重要修改说明：

- 改善什么；
- 牺牲什么；
- 影响谁；
- 影响哪些系统；
- 制作成本；
- 新风险。

## 10. Severity

需要排优先级时使用：

- `critical`
- `major`
- `minor`

严重度必须由最终评审统一判断，不能原样继承其他 Skill 的标签。

## 11. 正式报告格式

```markdown
# Design Review: [对象]

## Decision at stake
...

## Evidence baseline
- Confirmed:
- Assumed:
- Unknown:

## Priority findings
### [Severity] [Finding]
- Observation:
- Mechanism:
- Root cause:
- Evidence status:
- Impact:
- Recommendation:
- Tradeoff:
- Validation:

## Next experiment
...
```

## 12. 下一步实验

尽量提出最快减少不确定性的测试，例如：

- Spreadsheet Simulation
- Combat Simulation
- Rotation Test
- Trigger Reliability Test
- Encounter Matrix Test
- Greybox
- Prototype
- Playtest
- Telemetry Check
- A/B
- Config Verification
- Code Path Verification

测试只能支持它能证明的结论。
