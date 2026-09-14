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

1. 优先读取 `plugins/game-design-suite/skills/game-design/SKILL.md`；若宿主直接命中专业 Skill，也允许 Direct Specialist Entry，但不得绕过 Header 规则。
2. 由 `game-design` 选择最小充分 Skill 集；Direct Specialist Entry 时只加载完成任务真正需要的其他 Skill。
3. 完整读取被选 Skill 的 `plugins/game-design-suite/skills/<skill-name>/SKILL.md`。
4. 只按 Skill 路由读取会改变当前判断的 reference；不要为了显得全面加载全部资料。
5. **在任何正式结论之前输出 Professional Context Header。** 若 `game-design` 已输出则不重复；若宿主直接进入专业 Skill，该 Skill 必须自行输出，只列实际已读取/使用的专业。
6. 对已有项目，优先检查现有规则、文件、配置、数据与必要代码，不把项目当白纸。
7. 缺关键资料时执行 Missing Evidence Guard：标记证据边界，列出最小缺失材料，同时继续所有独立可做工作。
8. 配置表任务执行 Field Attribution Guard：先锁定 `Table/Sheet + RowKey/ID + FieldName + RawValue`，再解释数值；不得跨列串位。
9. 继续执行任务并交付实际结果。
10. 最终回复应是设计、结论、配置修改、验证结果或待确认 Human Gate，不是 Skill 名称列表。

## Professional Context Header

这是路由可观察性要求，不是角色扮演。

- 专业身份必须来自本次实际 Skill 路由；
- 简单任务保持一行；复杂生产任务最多 3~4 行；
- `game-design` 通常不作为主责职业显示；
- 不得列出未实际读取/使用的 Skill；
- 不得为了显得全面把全部 Skill 都列出来；
- 不得只写“我是资深 XX 策划”代替实际路由；
- Header 必须出现在正式答案前部，不能回答完再补；
- Header 后必须继续完成任务，不能只汇报路由；
- 如果宿主跳过 Router 直接调用专业 Skill，该专业 Skill 必须自行补 Header；同一轮已有 Header 时不重复。

推荐格式：

```text
专业视角：关卡策划（level-design）｜协同：战斗策划（combat-design）
```

复杂任务：

```text
【本次专业视角】
主责：技能策划（skill-design）
协同：数值策划（balance-design） / 配置审计（config-audit） / 代码验证（code-verification）
证据边界：当前仅有真实配置，可验证到 verified-config；代码语义仍为 unverified
```

统一规则见：

`plugins/game-design-suite/skills/game-design/references/professional-context-header.md`

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
- Professional Context Header 必须与实际路由一致；若后续证据使主责专业发生实质变化，可在正文中说明路由调整，不必反复重发完整 Header。
- Direct Specialist Entry 不得虚构尚未加载的协同 Skill。

## 配置读取硬规则

涉及 Excel/CSV/JSON/配置表时：

1. 先确认 Sheet/表名、Header Row 与准确列名；
2. 关键事实绑定 `Table/Sheet + RowKey/ID + FieldName + RawValue`；工具可提供时同时保留 CellAddress；
3. 关键修改项在输出前重新检查一次字段归属；
4. 不得把 `CoverCheckType = 2` 读成 `UniqueId = 2`，也不得把 A 列的值分布转写成 B 列的分布；
5. 不得根据截图视觉邻近、上一轮讨论字段或“数字看起来像某枚举”推断字段归属；
6. 用户指出“看错字段/看错列”时，撤销所有依赖该错误归属的结论并从表头重新读取；
7. 代码解释必须等待字段身份锁定后再做枚举 / Parser / Runtime 追踪。

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
