# Game Design Suite Agent Entry

本仓库提供可组合的游戏策划 Skills。用户不需要知道 Skill 名称；宿主 Agent 应自动路由并完成任务，而不是只返回 Skill 名单。

## NON-OPTIONAL USER-VISIBLE OUTPUT CONTRACT

无论用户是否提醒，只要 Game Design Suite 正在回答游戏设计/策划任务，**每一个独立正式结果前都必须显示 `【本次专业视角】`**。

固定顺序：

`Header -> Result -> Evidence/Reasoning -> Recommendation/Validation`

Decision Object 变化时重新判断主责/协同；专业组合相同也重复 Header。Direct Specialist Entry 同样执行。

## Canonical Skill Root

唯一专业真源：

```text
plugins/game-design-suite/skills/<skill-name>/SKILL.md
```

以及其 `references/`、`templates/` 和 `plugins/game-design-suite/evals/`。

`.deepcode/skills/`、根目录 `skills/` 或其他宿主目录只是发现/适配层，不是第二套知识库。

## 默认流程

1. 优先读取 `plugins/game-design-suite/skills/game-design/SKILL.md`；Direct Specialist Entry 允许，但不能绕过 Header。
2. 选择最小充分 Skill 集。
3. 完整读取被选 canonical `SKILL.md`。
4. 只读取会改变当前判断的 reference/template。
5. 按 Result Block 输出 Header。
6. 已有项目先检查真实规则、文件、配置、代码、数据、Runtime/日志，再设计。
7. 缺证据执行 Missing Evidence Guard，不猜。
8. 配置任务执行 Field Attribution Guard。
9. 装备/Itemization 任务先明确 Itemization Job、Slot/Budget/Affix/Acquisition/Replacement，再做具体数值。
10. 模拟任务记录 seed/model/config/agent version，不把 Simulation 冒充 Playtest。
11. Telemetry/实验任务先定义 Decision/Hypothesis/Metric/Segment，检查 SRM 和数据质量，不把相关性冒充因果。
12. Meta平衡按 Skill/Mastery/Composition/Content 分层，不只看总体胜率。
13. 继续执行并交付结果。

## Professional Context Header Decision Map

- 配置字段事实 -> `config-audit`
- Parser/枚举/Runtime Consumer -> `code-verification`
- 公式乘区/单位/Clamp/Round/Snapshot -> `formula-verification`
- 倍率/DPS/EHP/TTK/Power Budget -> `balance-design`
- Monte Carlo/离散事件/参数扫描/分布/敏感性 -> `simulation-design`
- 埋点/KPI/分群/A-B/SRM/统计分析 -> `telemetry-experiment-design`
- Roster/Composition/Matchup/Synergy/Counter/Power Creep -> `meta-balance`
- 装备槽位/品质/主副词条/词条池/Roll/套装/唯一特效/Loot可用率/BiS结构 -> `itemization-design`
- Resource Role/Source/Sink/库存 -> `economy-design`
- 等级/星级/突破/成长成本 -> `progression-design`
- 技能机制/Target/状态机 -> `skill-design`
- 战斗规则/AI/资源窗口 -> `combat-design`
- 关卡/空间/波次/Encounter -> `level-design`
- 玩法循环/系统结构 -> `game-production`

配置里出现数字不等于数值策划主责；出现装备不等于 `itemization-design` 可以包办代码、经济、模拟或Meta结论；有1000次模拟也不等于体验已验证；总体50%胜率也不等于Meta健康。

统一 Header 规则见：

`plugins/game-design-suite/skills/game-design/references/professional-context-header.md`

## Numerical Production Chain

复杂数值任务按需要组合：

```text
Design Intent
-> itemization-design (when equipment/build rules matter)
-> formula-verification
-> config-audit / code-verification
-> simulation-design
-> verified-runtime
-> telemetry-experiment-design
-> meta-balance
-> Playtest
```

低层证据不能替代高层结论。

## Private Project Isolation

用户可以用真实项目配置、代码、日志来验证通用 Skill，但**不得把私有项目细节写入公开通用 Skill**。

允许抽象：

- deterministic seed；
- Golden Test；
- Formula/Runtime parity；
- schema/version guard；
- distribution/tail checks；
- telemetry data-quality checks；
- loot funnel / affix guard；
- generic anti-patterns。

禁止复制：

- 私有项目名；
- 私有角色/技能/装备/表名；
- 私有ID/路径；
- 私有真实公式；
- 私有装备数值/掉率/经济/运营数据；
- 未公开业务规则。

项目专属适配应留在项目私有 workspace，不污染通用 Game Design Suite。

## Host 适配

### ChatGPT / Codex Plugin

```text
.agents/plugins/marketplace.json
plugins/game-design-suite/.codex-plugin/plugin.json
```

### DeepSeek Deep Code

```text
.deepcode/skills/<skill-name>/SKILL.md
```

Deep Code adapter 必须继续读取 canonical Skill。

### AGENTS.md-aware host

直接按本文件发现 canonical Skills。

## 证据状态

根据任务尽量使用：

- `verified-formula-design`
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

不要用笼统 `verified` 混淆层级。

## Human Gate

以下事项需要用户明确确认：发布/对外提交、删除或覆盖正式资产、锁定重大范围、改变用户明确要求不变的核心机制、把 candidate 升级为长期正式标准、不可逆真实账号操作、大规模迁移项目结构。

分析、只读审查、模拟、草案和验证计划不需要 Human Gate。

## 安全边界

- 不把用户私有项目资料提交到公开仓库。
- 不虚构 Telemetry、Playtest、市场数据或代码行为。
- 不为模板制造数值、功能或商业化方案。
- 不把 Spreadsheet / Simulation / observational telemetry 冒充更高层证据。
- 外部游戏的公式、阈值、装备词条、掉率和案例只做方法参考，不是项目真值。

## 维护

新增/删除 Skill，或修改 canonical Skill 的 `name` / `description` 后运行：

```bash
python scripts/sync_agent_skills.py
python scripts/sync_agent_skills.py --check
```
