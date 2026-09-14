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

## 插件与 Marketplace 结构

本仓库已按 Codex / ChatGPT 插件市场结构整理：

```text
GameDesignSuite/
├── .agents/
│   └── plugins/
│       └── marketplace.json
├── plugins/
│   └── game-design-suite/
│       ├── .codex-plugin/
│       │   └── plugin.json
│       └── skills/
│           ├── game-design/
│           ├── game-production/
│           ├── balance-design/
│           └── ...
├── AGENTS.md
├── README.md
├── skills-index.json
└── validate_skills.py
```

其中：

- `.agents/plugins/marketplace.json`：插件市场入口。
- `plugins/game-design-suite/.codex-plugin/plugin.json`：Game Design Suite 插件清单。
- `plugins/game-design-suite/skills/*/SKILL.md`：14 个专业 Skill。

## 从 GitHub 安装

在“添加插件市场”中填写：

```text
来源：
https://github.com/xiaomi867/GameDesignSuite.git

Git 引用：
main

稀疏路径：
留空
```

不要填写 `tree/main`，也不要把稀疏路径设为 `skills`，因为 Marketplace manifest 位于仓库根目录下的 `.agents/plugins/marketplace.json`。

## 从本地目录测试

“来源”直接选择或填写包含 `.agents/` 和 `plugins/` 的 **GameDesignSuite 根目录**；Git 引用与稀疏路径留空。

## 核心 Skill

| Skill | 主要职责 |
|---|---|
| `game-design` | 总入口、路由、多 Skill 协调 |
| `game-production` | 玩法、系统、产品、制作约束 |
| `design-frameworks` | MDA、Core Loop、Flow、设计 Pattern |
| `balance-design` | 数值模型、强度、曲线、DPS/HPS、参数验证 |
| `economy-design` | Sources/Sinks、流速、价值、通胀、产销 |
| `progression-design` | 等级、星级、解锁、成长节奏 |
| `combat-design` | 战斗规则、目标、节奏、状态、AI 与遭遇 |
| `skill-design` | 技能机制、Target、Buff/Debuff、升级与构筑 |
| `level-design` | 关卡、地图、空间、路径、Encounter、节奏 |
| `game-interface-design` | HUD、菜单、引导、反馈、Accessibility |
| `config-audit` | Excel/配置字段、ID、引用、漏配、一致性 |
| `code-verification` | 客户端/服务器代码读取、实际生效链路 |
| `design-review` | 风险、矛盾、主导策略、比较与压力测试 |
| `game-design-doc` | GDD、System Spec、正式设计文档 |

## 推荐调用示例

### 英雄技能调整

`skill-design + balance-design`

已有生产项目通常再加：

`config-audit + code-verification`

定稿前：

`design-review`

### 七日奖励 / 日常任务 / 资源循环

`game-production + economy-design + progression-design + balance-design`

### Boss 关卡

`game-production + combat-design + level-design`

### 完整 GDD

`game-production + 必要专业 Skill + design-review + game-design-doc`

## 建议测试 Prompt

安装后可用以下问题验证：

```text
请分析一个 RPG 英雄 Lv1~Lv100 的攻击、生命、防御成长曲线，
给出基准值、成长公式、关键等级采样和验证方法，
并明确哪些结论是 verified，哪些只是 candidate。
```

或：

```text
这是一个已有英雄技能系统，不允许修改技能机制。
请检查技能倍率、Buff、Target、成长和配置引用；
没有代码证据时不要声称代码已经验证，最后做一次设计审查。
```

## 设计原则

1. 已有项目先读现状，再设计。
2. 用户明确要求“不改机制”时，Fixed Rules 视为不可变约束。
3. 事实、推断、提案、候选值、验证结果分开表达。
4. 理论计算不能冒充 Playtest。
5. 数值修改必须考虑横向强度和上下游系统。
6. 配置问题必须落到表、行/Key、字段、值、引用、验证。
