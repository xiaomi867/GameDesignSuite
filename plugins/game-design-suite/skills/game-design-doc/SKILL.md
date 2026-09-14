---
name: game-design-doc
description: 生成、整理、重构和维护 Game Design Document（GDD）、System Spec、Concept GDD、Production GDD 或 Pitch Design Document。优先复用已确认项目事实，不为了填满模板而虚构数值、内容量、商业化方案或验收标准。
---

# 游戏设计文档

本 Skill 负责整理、组织、关联、表达和维护；专业设计由对应 Skill 完成。

## Result-Level Professional Context

当文档任务中输出一个新的专业设计结论、系统决策、风险 Finding 或正式规则前，按 `../game-design/references/professional-context-header.md` 输出一次结果级 Header。`game-design-doc` 只有在“文档组织/规格化表达本身”是当前 Decision Object 时才主责；具体经济、技能、数值、关卡等内容必须由对应专业主责，本 Skill 作为协同。相邻结果专业相同也重复显示。

## 文档类型

根据用户目标选择：

- Concept GDD
- Production GDD
- System Spec
- Pitch Design Document

不要把一个小系统需求扩成巨型 GDD。

## 证据状态

文档内容区分：

- `confirmed`
- `candidate`
- `TBD`
- `unknown`

不得为了“完整”把候选值写成事实。

## 禁止 Fog Words

“快、爽、丰富、深度高、强反馈”等词如果能量化，应给指标；若还未验证，标 `candidate`，不要制造虚假精度。

## 推荐章节

根据项目成熟度选择：

1. Elevator Pitch
2. Player Promise / Audience
3. Design Pillars（通常 3~5，不强制）
4. Core Loop Stack
5. System Inventory
6. System Interaction Matrix
7. Feature Backlog
8. Acceptance Criteria
9. Progression
10. Economy
11. Monetization（若存在）
12. Content Budget
13. Risk Register
14. Open Questions
15. Change Log

## System Interaction Matrix

重点发现：

- 循环依赖；
- 隐性依赖；
- 单点故障；
- 系统冲突；
- 上下游遗漏。

关系类型可用 `critical/direct/indirect/none`，不强制固定枚举。

## Feature Backlog

可使用：

| Feature | Priority | Status | Value | Cost | Depends On | Acceptance Criteria | Owner |
|---|---|---|---|---|---|---|---|

真实依赖优先于表格排序，不用“必须引用上一行”这种格式规则掩盖循环依赖。

## Acceptance Criteria

数量根据复杂度决定，不机械要求至少 3 条。避免“体验良好/运行正常”这种不可验证描述。

## Content Budget

未知数量写 `TBD`，不为了填表虚构英雄、敌人、关卡、任务数量。

## Risk Register

根据项目覆盖 Design、Balance、Technical、Production、Content、Business、Market、UX、Performance 等相关风险。

## 与专业 Skill 协作

必要时使用：

- game-production
- level-design
- skill-design
- combat-design
- balance-design
- economy-design
- progression-design
- game-interface-design
- design-review
- config-audit
- code-verification

## Quality Gate

交付前检查：

- 未定义术语；
- Fog Words；
- Candidate 被写成事实；
- 系统依赖遗漏；
- 隐性循环；
- 无用途资源；
- Feature 无玩家价值；
- AC 不可验证；
- 内容数量无来源；
- 重大 Open Question 被偷偷补全；
- 冲突规则；
- 过期旧方案。
