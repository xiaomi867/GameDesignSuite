# GameDesignSuite

一套面向生产项目的游戏策划 Skill Suite，重点覆盖：

- 玩法策划 / 核心循环 / 系统策划
- 战斗策划 / 技能策划
- 数值策划 / 平衡 / 成长曲线
- 经济策划 / 产销闭环
- 关卡与空间设计
- 游戏 UI / UX / Onboarding
- 配置表审查 / ID 与字段关联
- 客户端 / 服务器实现验证
- 设计评审
- GDD / System Spec

## 多 Agent 架构

Game Design Suite 现在采用 **单一专业真源 + 多宿主适配层**：

```text
GameDesignSuite/
├── .agents/
│   └── plugins/
│       └── marketplace.json          # ChatGPT / Codex Marketplace
├── .deepcode/
│   └── skills/                       # DeepSeek Deep Code discovery adapters
│       ├── game-design/
│       ├── balance-design/
│       └── ...
├── plugins/
│   └── game-design-suite/
│       ├── .codex-plugin/
│       │   └── plugin.json
│       ├── skills/                   # 唯一专业真源 / Canonical Skills
│       │   ├── game-design/
│       │   ├── game-production/
│       │   ├── balance-design/
│       │   └── ...
│       └── evals/
├── scripts/
│   └── sync_agent_skills.py          # 同步/检查宿主适配层
├── docs/
│   └── MULTI_AGENT.md
├── AGENTS.md
├── README.md
├── skills-index.json
└── validate_skills.py
```

### 唯一真源

所有专业规则只维护在：

```text
plugins/game-design-suite/skills/<skill-name>/SKILL.md
```

以及这些 Skill 引用的 `references/`、模板和 `plugins/game-design-suite/evals/`。

`.deepcode/skills/` 只负责让 Deep Code 发现 Skill；执行时会继续读取 canonical `SKILL.md`。不要维护第二套专业正文。

更多说明见 `docs/MULTI_AGENT.md`。

---

## ChatGPT / Codex：从 GitHub 安装

在 ChatGPT 的“添加插件市场”中填写：

```text
来源：
https://github.com/xiaomi867/GameDesignSuite.git

Git 引用：
main

稀疏路径：
留空
```

不要填写 `tree/main`，也不要把稀疏路径设为 `skills`，因为 Marketplace manifest 位于仓库根目录下的 `.agents/plugins/marketplace.json`。

其中：

- `.agents/plugins/marketplace.json`：插件市场入口；
- `plugins/game-design-suite/.codex-plugin/plugin.json`：Game Design Suite 插件清单；
- `plugins/game-design-suite/skills/*/SKILL.md`：14 个专业 Skill。

### 本地目录测试

“来源”直接选择或填写包含 `.agents/` 和 `plugins/` 的 **GameDesignSuite 根目录**；Git 引用与稀疏路径留空。

---

## DeepSeek Deep Code：项目级使用

Deep Code 使用项目级 Agent Skills 时，会从：

```text
.deepcode/skills/<skill-name>/SKILL.md
```

发现 Skill。本仓库已经提供 14 个对应适配器。

### 1. 获取仓库

```bash
git clone https://github.com/xiaomi867/GameDesignSuite.git
cd GameDesignSuite
```

已有本地仓库则：

```bash
git pull
```

### 2. 在仓库根目录启动 Deep Code

```bash
deepcode
```

进入后可使用 `/` 查看可发现的 Skills，或直接点名：

```text
/game-design
/balance-design
/skill-design
/level-design
```

也可以直接用自然语言描述任务，让 Agent 根据 Skill description 选择专业能力。

### 3. DeepSeek 网页/App 与 Deep Code 的区别

普通 DeepSeek 网页/App 聊天不是本仓库的项目 Skill 安装入口；要让 DeepSeek 自动发现并读取这套仓库 Skills，优先使用 Deep Code 或其他支持仓库级 Agent Skills / `AGENTS.md` 的宿主。

---

## 核心 Skill

| Skill | 主要职责 |
|---|---|
| `game-design` | 总入口、路由、多 Skill 协调 |
| `game-production` | 玩法、系统、产品、制作约束 |
| `design-frameworks` | MDA、Core Loop、Flow、设计 Pattern |
| `balance-design` | 数值模型、Power Budget、成长、DPS/HPS、概率与参数验证 |
| `economy-design` | Resource Role、Sources/Sinks、流速、价值、通胀、产销 |
| `progression-design` | 等级、星级、技能树、解锁、成长节奏 |
| `combat-design` | 战斗规则、行动/资源经济、状态、Gauge、AI 与遭遇 |
| `skill-design` | Hero Kit、状态机、资源图、Target、Buff/Debuff、升级与构筑 |
| `level-design` | 关卡、地图、波次、Mechanic Lifecycle、Encounter、节奏与 Boss |
| `game-interface-design` | HUD、菜单、引导、反馈、Accessibility |
| `config-audit` | Excel/配置字段、ID、引用、漏配、一致性 |
| `code-verification` | 客户端/服务器代码读取、实际生效链路 |
| `design-review` | 根因、反模式、矛盾、主导策略、比较与压力测试 |
| `game-design-doc` | GDD、System Spec、正式设计文档 |

## Professional Context Header

从 `v1.1.0` 开始，Game Design Suite 在正式回答游戏设计问题前，会先显示本次真实专业路由，让用户能直接判断是否“找对策划”。

简单任务示例：

```text
专业视角：关卡策划（level-design）｜协同：战斗策划（combat-design）
```

复杂生产任务示例：

```text
【本次专业视角】
主责：技能策划（skill-design）
协同：数值策划（balance-design） / 配置审计（config-audit） / 代码验证（code-verification）
证据边界：当前只有真实配置，可验证到 verified-config；代码语义仍为 unverified
```

规则：

- Header 来自实际 Skill Routing，不是角色扮演；
- 只显示最小充分专业集合；
- 简单问题一行，复杂问题最多 3~4 行；
- 不列未实际使用的 Skill；
- 不用“我是资深 XX 策划”替代路由；
- Header 后继续完成实际任务。

详细规范见：

```text
plugins/game-design-suite/skills/game-design/references/professional-context-header.md
```

## 推荐调用示例

### 英雄技能调整

```text
skill-design + balance-design
+ config-audit（已有配置）
+ code-verification（需要确认实现）
+ design-review（定稿前）
```

### 七日奖励 / 日常任务 / 资源循环

```text
game-production + economy-design + progression-design + balance-design
```

### Boss / 关卡

```text
game-production + combat-design + level-design
```

### 完整 GDD

```text
game-production + 必要专业 Skill + design-review + game-design-doc
```

## 建议测试 Prompt

### 自动路由测试

```text
一个卡牌 Roguelite 里，三选一时玩家永远选伤害技能，治疗、防御和功能卡没人拿。
不要让我选择专业方向，你自己分析并给出验证方案。
```

### Professional Context Header 测试

```text
我们游戏食物、水、电、硅晶后期会大量堆积，你判断根因并给出处理方案。
```

预期主责应优先为 `经济策划（economy-design）`，而不是因为涉及资源数值就只显示 `balance-design`。

### 配置 + 代码证据测试

```text
这是一个已经开发中的坦克英雄，技能机制不能改。
检查伤害倍率、护甲 Buff、嘲讽 Target、升星成长和配置引用。
缺少代码或配置时不要猜；真实代码出现后允许推翻旧 candidate。
```

## 证据原则

重要结论尽量区分：

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
2. 用户明确要求“不改机制”时，Fixed Rules 视为不可变约束。
3. 症状不等于方案；先查根因。
4. 事实、推断、候选值和验证结果分开表达。
5. 理论计算 / Spreadsheet / Simulation 不能冒充 Playtest。
6. 配置问题必须落到表、Row/Key/ID、字段、引用和值。
7. 代码验证必须追到 Parser / Runtime Consumer / Target / Result，而不是看到字段名就猜语义。
8. 新证据可以推翻旧 candidate。

## 维护与同步

新增/删除 Skill，或修改 canonical Skill 的 `name` / `description` 后运行：

```bash
python scripts/sync_agent_skills.py
```

检查 Deep Code 适配层：

```bash
python scripts/sync_agent_skills.py --check
```

若需要要求适配层完全由 canonical description 自动生成：

```bash
python scripts/sync_agent_skills.py --check --strict
```

专业正文只改 `plugins/game-design-suite/skills/`，不要人工维护多份。
