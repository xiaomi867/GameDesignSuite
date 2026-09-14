# Game Design Suite Agent Entry

本仓库提供一组可组合的游戏策划 Skills。用户不需要知道 Skill 名称；宿主 Agent 应根据任务自动路由并继续完成工作，而不是只返回“建议使用某个 Skill”。

## 默认流程

当用户提出游戏设计、系统、玩法、数值、经济、成长、战斗、技能、关卡、UI、配置、代码验证、评审或 GDD 需求时：

1. 先读取 `skills/game-design/SKILL.md`。
2. 由 `game-design` 选择最小充分 Skill 集。
3. 读取被选 Skill 的 `SKILL.md`。
4. 对已有项目，优先检查现有规则、文件、配置、数据与必要代码，不把项目当白纸。
5. 继续执行任务并交付实际结果。
6. 最终回复应是设计、结论、配置修改、验证结果或待确认 Human Gate，不是 Skill 名称列表。

## 长期项目

默认不创建长期状态。只有用户明确要求长期推进、统一规则、持续维护项目知识或建立工作流时，才维护：

- Project Context
- Confirmed Rules
- Candidate Rules
- Decisions
- Assumptions
- Open Questions
- Experiments
- Evidence
- Risks
- Change Log

一次实验、一次模拟或单次 Playtest 不得直接升级成长期规则；先保持 `candidate`。

## Human Gate

以下事项需要用户明确确认：

- 发布或对外提交；
- 删除、覆盖正式资产；
- 锁定重大项目范围；
- 改变用户明确要求保持不变的核心机制；
- 将 candidate 规则升级为长期正式标准；
- 使用真实账号执行不可逆外部操作；
- 大规模迁移现有项目结构。

分析、建议、模拟、草案和只读审查不需要 Human Gate。

## 证据状态

重要结论尽量区分：

- `verified`
- `confirmed`
- `supported-inference`
- `candidate`
- `assumed`
- `unknown`
- `not-yet-playtested`
- `externally-blocked`

## 安全边界

- 不把用户私有项目资料提交到公开仓库。
- 不虚构 Telemetry、Playtest、市场数据或代码行为。
- 不为满足模板而制造数值、功能、内容量或商业化方案。
- 不为了“完整”而加载全部 Skill。
