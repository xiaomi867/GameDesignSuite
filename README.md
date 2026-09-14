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

## 核心结构

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

## 导入方式

本仓库采用通用 `skills/<skill-name>/SKILL.md` 结构。

- 如果你的 GPT/Agent 支持 Git 仓库作为 Skill 来源：把整个 `GameDesignSuite` 推到 GitHub，再添加仓库。
- 如果支持上传单个 Skill：上传对应 `skills/<name>` 目录，或使用本包内生成的单 Skill ZIP。
- 不同宿主对 marketplace manifest 的要求可能不同；本仓库不伪造某一宿主专属 manifest。若宿主报缺少 manifest，应按该宿主当前规范补充。

## 设计原则

1. 已有项目先读现状，再设计。
2. 用户明确要求“不改机制”时，Fixed Rules 视为不可变约束。
3. 事实、推断、提案、候选值、验证结果分开表达。
4. 理论计算不能冒充 Playtest。
5. 数值修改必须考虑横向强度和上下游系统。
6. 配置问题必须落到表、行/Key、字段、值、引用、验证。
