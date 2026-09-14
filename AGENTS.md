# Game Design Suite Agent Entry

本仓库提供一组可组合的游戏策划 Skills。用户不需要知道 Skill 名称；宿主 Agent 应根据任务自动路由并继续完成工作，而不是只返回“建议使用某个 Skill”。

## 唯一真源 / Canonical Skill Root

所有专业规则只维护在：

```text
plugins/game-design-suite/skills/<skill-name>/SKILL.md
```

以及这些 Skill 直接引用的 `references/`、模板与仓库内 `plugins/game-design-suite/evals/`。

`.deepcode/skills/`、根目录 `skills/` 或其他宿主目录都不是第二套专业知识库。宿主适配层只能负责 Skill discovery / routing；真正执行前必须读取 canonical `SKILL.md`。

如果适配文件与 canonical Skill 冲突，以 canonical Skill 为准。

## 默认流程

当用户提出游戏设计、系统、玩法、数值、经济、成长、战斗、技能、关卡、UI、配置、代码验证、评审或 GDD 需求时：

1. 先读取 `plugins/game-design-suite/skills/game-design/SKILL.md`。
2. 由 `game-design` 选择最小充分 Skill 集。
3. 完整读取被选 Skill 的 `plugins/game-design-suite/skills/<skill-name>/SKILL.md`。
4. 只按 Skill 路由读取会改变当前判断的 reference；不要为了显得全面加载全部资料。
5. 对已有项目，优先检查现有规则、文件、配置、数据与必要代码，不把项目当白纸。
6. 缺关键资料时执行 Missing Evidence Guard：标记证据边界，列出最小缺失材料，同时继续所有独立可做工作。
7. 继续执行任务并交付实际结果。
8. 最终回复应是设计、结论、配置修改、验证结果或待确认 Human Gate，不是 Skill 名称列表。

## Host 适配

### ChatGPT / Codex Plugin

通过：

```text
.agents/plugins/marketplace.json
plugins/game-design-suite/.codex-plugin/plugin.json
```

加载 canonical Skills。

### DeepSeek Deep Code

Deep Code 通过：

```text
.deepcode/skills/<skill-name>/SKILL.md
```

发现 Skills。这些文件是薄 adapter；读取 adapter 后必须继续读取其中指向的 canonical Skill，再执行任务。

### AGENTS.md-aware host

若宿主支持 `AGENTS.md`，直接按本文件读取 canonical Skill，无需复制一套专业正文。

更多说明见 `docs/MULTI_AGENT.md`。

## 多 Skill 协作

- 选择最小充分 Skill 集，不机械全开。
- 多 Skill 输出必须合并成统一判断，不把多个报告简单拼接。
- 配置事实、代码事实、数值候选、设计判断和 Playtest 证据分层处理。
- 新证据可以推翻旧 candidate；不要为了维护历史回答一致而忽略更高质量证据。

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

根据任务尽量使用更具体的状态：

- `verified-config`
- `verified-code`
- `verified-runtime`
- `verified-data`
- `confirmed`
- `supported-inference`
- `candidate`
- `assumed`
- `unknown`
- `unverified`
- `not-yet-playtested`
- `externally-blocked`

不要用笼统 `verified` 混淆配置、代码和运行时证据。

## 安全边界

- 不把用户私有项目资料提交到公开仓库。
- 不虚构 Telemetry、Playtest、市场数据或代码行为。
- 不为满足模板而制造数值、功能、内容量或商业化方案。
- 不为了“完整”而加载全部 Skill。
- 不把 Spreadsheet / Simulation / 文档推演冒充玩家体验证据。

## 维护

canonical Skill 的专业内容变更后，一般不需要改 Deep Code adapter；若 `name` / `description` 改动或新增/删除 Skill，运行：

```bash
python scripts/sync_agent_skills.py
python scripts/sync_agent_skills.py --check
```
