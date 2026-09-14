---
name: design-review
description: 对已有游戏概念、GDD、机制、技能、战斗、经济、成长、关卡、UI、原型、配置方案或 Playtest 结果进行评审、比较和压力测试。识别弱点、矛盾、主导策略、False Choice、失衡和证据缺口，并给出最小有效修改与下一步验证实验。
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

## 3. Review Modes

### Focused
一个技能、一段规则、一个小系统。

### Comprehensive
完整 GDD、复杂系统、多表/多模块，需要跨域矛盾检查。

### Exploratory
方向未确定：提出 2~3 个候选方向和能区分它们的小实验。

### Comparative
比较 A/B/多方案，必须使用相同证据和标准。

## 4. Finding 质量

每个重要 Finding 包含：

- Observation
- Mechanism
- Evidence Status
- Impact
- Recommendation
- Validation

推荐最小改动，不默认新增功能。

## 5. 常见风险

按相关性选择，不机械全查：

- Dominant Strategy
- False Choice
- No Opportunity Cost
- Hollow Loop
- Power Creep / Treadmill
- Complexity Over Depth
- Exploit
- Cross-System Conflict
- Recovery Failure
- Unclear Telegraph
- Hidden Dependency
- Content/Production Overreach

## 6. Tradeoff

重要修改说明：

- 改善什么；
- 牺牲什么；
- 影响谁；
- 影响哪些系统；
- 制作成本；
- 新风险。

## 7. Severity

需要排优先级时使用：

- `critical`
- `major`
- `minor`

严重度必须由最终评审统一判断，不能原样继承其他 Skill 的标签。

## 8. 正式报告格式

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
- Evidence status:
- Impact:
- Recommendation:
- Validation:

## Tradeoffs
...

## Next experiment
...
```

## 9. 下一步实验

尽量提出最快减少不确定性的测试，例如：

- Spreadsheet Simulation
- Combat Simulation
- Greybox
- Prototype
- Playtest
- Telemetry Check
- A/B
- Config Verification
- Code Path Verification

测试只能支持它能证明的结论。
