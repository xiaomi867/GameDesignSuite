# GameDesignSuite

一套面向生产项目的通用游戏策划 Skill Suite，覆盖：玩法/系统、战斗/技能、数值/公式、装备/Itemization、Simulation、Telemetry/A-B实验、Meta/版本平衡、经济/成长、关卡、UI/UX、配置审计、代码验证、设计评审和 GDD。

## 多 Agent 架构

Game Design Suite 采用 **单一专业真源 + 多宿主适配层**：

```text
GameDesignSuite/
├── .agents/plugins/marketplace.json
├── .deepcode/skills/                  # DeepSeek Deep Code adapters
├── plugins/game-design-suite/
│   ├── .codex-plugin/plugin.json
│   ├── skills/                        # Canonical Skills
│   └── evals/
├── scripts/sync_agent_skills.py
├── AGENTS.md
├── skills-index.json
└── validate_skills.py
```

唯一专业真源：

```text
plugins/game-design-suite/skills/<skill-name>/SKILL.md
```

`.deepcode/skills/` 只负责发现，执行时继续读取 canonical Skill。

## ChatGPT / Codex：从 GitHub 安装

在“添加插件市场”中填写：

```text
来源：https://github.com/xiaomi867/GameDesignSuite.git
Git 引用：main
稀疏路径：留空
```

Marketplace manifest 位于仓库根目录的 `.agents/plugins/marketplace.json`。

当前插件版本：**1.5.0**。

当前 canonical Skills：**19 个**。

## DeepSeek Deep Code

```bash
git clone https://github.com/xiaomi867/GameDesignSuite.git
cd GameDesignSuite
deepcode
```

进入后可用 `/` 查看 Skill，或直接用自然语言让 Agent 自动路由。

普通 DeepSeek 网页/App 不是本仓库的项目 Skill 安装入口；优先使用 Deep Code 或支持仓库级 Agent Skills / `AGENTS.md` 的宿主。

## Skill 清单

| Skill | 主要职责 |
|---|---|
| `game-design` | 总入口、结果级路由、多 Skill 协调 |
| `game-production` | 玩法、系统、产品、跨系统与制作约束 |
| `design-frameworks` | MDA、Core Loop、Flow、Pattern |
| `balance-design` | Power Budget、DPS/HPS/EHP、成长、参数平衡 |
| `formula-verification` | 公式还原、乘区、单位、Clamp/Round、概率、边界、代码交叉验证 |
| `simulation-design` | Monte Carlo、离散事件、参数扫描、策略代理、分布与敏感性 |
| `telemetry-experiment-design` | 埋点、指标、分群、A/B、SRM、显著性、因果边界 |
| `meta-balance` | Roster/Composition/Matchup/Synergy/Counter、Mastery、Power Creep、版本生态 |
| `itemization-design` | 装备槽位、品质、主/副词条、词条池、Roll、强化、套装、唯一特效、掉落、替换、分解与BiS/Build生态 |
| `economy-design` | Resource Role、Sources/Sinks、流速、库存、价值与产销 |
| `progression-design` | 等级、星级、技能树、突破、解锁、成长节奏 |
| `combat-design` | 战斗规则、行动/资源经济、状态、Gauge、AI、遭遇 |
| `skill-design` | Hero Kit、状态机、Target、Buff/Debuff、升级与构筑 |
| `level-design` | 关卡、地图、波次、Encounter、节奏、Boss |
| `game-interface-design` | HUD、菜单、引导、反馈、Accessibility |
| `config-audit` | Excel/配置字段、ID、引用、漏配、一致性 |
| `code-verification` | 客户端/服务器读取与实际生效链 |
| `design-review` | 根因、反模式、矛盾、主导策略、验证实验 |
| `game-design-doc` | GDD、System Spec、正式设计文档 |

## 数值与Itemization生产链

复杂任务按需要组合：

```text
Design Intent
-> itemization-design (装备/物品化任务)
-> formula-verification
-> config-audit / code-verification
-> simulation-design
-> verified-runtime
-> telemetry-experiment-design
-> meta-balance
-> Playtest
```

其中：

- `itemization-design`：装备结构、Slot、品质、词条、Roll、套装、Loot、替换与Build目标；
- `formula-verification`：公式数学结构是否正确；
- `config-audit / code-verification`：项目实际输入和实现是什么；
- `simulation-design`：上线前看分布、尾部、敏感性、毕业时间和极端组合；
- `telemetry-experiment-design`：上线后看真实玩家数据并做受控实验；
- `meta-balance`：判断角色/Build/装备/队伍/内容生态是否健康；
- Playtest：验证理解、挫败、节奏与乐趣。

低层证据不能冒充高层证据。

## `itemization-design`

用于武器、防具、饰品、遗物、符文、芯片、神器等装备/物品化系统。

核心能力：

- Itemization Job / 装备系统职责；
- Slot Architecture；
- Item Power Budget；
- Base/Main/Substat；
- Affix Pool / Weight / Exclusion；
- Roll Range / Affix Tier；
- 品质/稀有度梯度；
- 强化与继承；
- Set Bonus / Unique Effect；
- 专武 / Signature Tax；
- Loot可用率与真实Upgrade Rate；
- Replacement Curve；
- P50/P90/P95毕业周期；
- Salvage / Duplicate / Crafting；
- Character × Item / Build × Item矩阵；
- Best-in-Slot集中与Power Creep。

核心原则：

```text
更多词条 != 更多Build
更高橙装掉率 != 更高实际升级率
固定属性比例 != 跨项目真理
平均毕业时间 != 坏运气体验健康
高品质 != 所有维度都必须同时膨胀
```

## Professional Context Header

每一个独立正式结果前都必须显示实际专业路由，用户不需要额外提醒。

例如装备任务可能依次切换：

```text
装备 / Itemization 策划
-> 数值策划
-> 配置审计 / 代码验证
-> 数值模拟 / 仿真
-> 经济策划
-> Meta / 版本平衡
```

不能用一个 Header 覆盖不同 Decision Object。

详细规则：

```text
plugins/game-design-suite/skills/game-design/references/professional-context-header.md
```

## Simulation / Telemetry / Meta

### `simulation-design`

支持：

- 100 / 1000 / 10000 次战斗或概率模拟；
- Mean/Median/P90/P95/失败率等分布；
- deterministic seed；
- Monte Carlo；
- Discrete Event Simulation；
- Rotation/Timeline；
- 参数扫描与Sensitivity；
- Bot/Policy Persona；
- 长周期经济、成长、装备掉落与毕业模拟。

Simulation 不能冒充真实玩家体验。

### `telemetry-experiment-design`

支持：

- Event Schema；
- KPI/漏斗/留存/行为指标；
- 玩家Skill/Mastery分群；
- A/B与多变量实验；
- Sample Ratio Mismatch；
- Effect Size / Confidence Interval；
- Guardrail；
- 相关性与因果边界。

### `meta-balance`

支持：

- Roster Matrix；
- Matchup / Synergy / Counter Matrix；
- Character × Item / Build × Item生态；
- Composition；
- Pick/Win/Presence；
- Mastery Curve；
- Diversity / Concentration；
- Pair Lock；
- Best-in-Slot Lock；
- Power Creep；
- 版本改动的二阶影响。

## 外部参考使用原则

崩铁、绝区零、Riot、Ubisoft、GDC、学术论文及其他公开资料只用于：

- 公式/模型结构参考；
- Itemization方法；
- 专业方法论；
- 反模式与验证方法；
- 测试场景与边界启发。

禁止把其他游戏的公式、53%胜率线、速度阈值、词条数量、掉率、套装倍率、强化曲线等直接复制为通用标准。

## 私有项目隔离

真实项目配置、源码和日志可以用来**验证通用 Skill 是否覆盖生产问题**，但不会写入公开通用 Skill。

允许抽象：deterministic seed、Golden Test、Formula/Runtime parity、Schema/version guard、Tail distribution、Loot funnel、Dead-affix guard、Telemetry quality checks。

禁止公开：私有项目名、角色/技能/装备/表名、ID、代码路径、真实公式、装备数值、掉率、经济数据、业务规则。

## 推荐测试 Prompt

### Itemization

```text
给我设计一套装备系统：先定义Slot和每个槽位职责，再建立属性预算、品质、主副词条、词条权重、强化、套装、掉落、分解和毕业周期。不要套固定ATK:DEF:HP比例，并检查Best-in-Slot和Dead Affix风险。
```

### Loot Simulation

```text
模拟目标装备的获取：正确槽位、正确套装、正确主属性、至少3条有效副词条，并在强化中至少3次命中有效词条。报告P50/P90/P95毕业时间，不要只给平均值。
```

### Meta

```text
单件装备看起来都合理，但85%的输出角色使用同一饰品。检查Character×Item、Build×Item、BiS集中、替代品和Power Creep。
```

## 证据原则

常用状态：

- `verified-formula-design`
- `verified-config`
- `verified-code`
- `verified-runtime`
- `verified-data`
- `confirmed`
- `supported-inference`
- `candidate`
- `unverified`
- `not-yet-playtested`
- `externally-blocked`

核心规则：

1. 已有项目先读现状，再设计。
2. 症状不等于方案，先查根因。
3. 配置存在不等于代码读取，代码读取不等于Runtime触发。
4. Itemization必须区分结构、数值、经济、随机分布和Meta责任。
5. Simulation 必须可复现并报告分布，不只报告均值。
6. Telemetry 观察相关性不等于因果。
7. Meta平衡不能只看一个总体胜率或单件装备理论值。
8. Spreadsheet / Simulation / Telemetry 都不能冒充 Playtest。
9. 新证据可以推翻旧 candidate。

## 维护与同步

新增/删除 Skill，或修改 canonical Skill 的 `name` / `description` 后运行：

```bash
python scripts/sync_agent_skills.py
python scripts/sync_agent_skills.py --check
```

专业正文只改 `plugins/game-design-suite/skills/`，不要人工维护多份。
