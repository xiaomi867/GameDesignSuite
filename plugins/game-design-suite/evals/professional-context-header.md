# Professional Context Header Regressions

用于验证 Game Design Suite 的用户可见专业路由是否真实、简洁、可审计。

## Case 1 — 单专业问题

Prompt：

> 玩家总在这张地图里迷路，帮我分析原因。

Expected：

- Header 主责为 `关卡策划（level-design）`；
- 不应把 `balance-design`、`economy-design` 等无关 Skill 列为协同；
- Header 一行即可。

Fail：

- 只写“我是资深游戏策划”；
- 把所有 Skill 全列出来。

## Case 2 — 多专业英雄审计

Prompt：

> 这是一个已经开发中的坦克英雄，技能机制不能改。检查倍率、Buff、Target、升星、配置引用和代码实际语义。

Expected：

- 主责：`技能 / 英雄策划（skill-design）`；
- 协同至少包含 `balance-design + config-audit + code-verification`；
- Header 明确“技能机制不可修改”；
- 若代码未提供，证据边界不得写成 `verified-code`。

## Case 3 — 资源富余症状

Prompt：

> 食物、水、电、硅晶后期很多，怎么办？

Expected：

- 主责：`经济策划（economy-design）`；
- 可协同 `game-production / progression-design / balance-design` 中必要项；
- 不应因为问题包含“资源数值”就把 `balance-design` 设为主责；
- 正文必须先查 Resource Role / Source / Stock / Lifecycle，而不是直接新增 Sink。

## Case 4 — 成长成本

Prompt：

> 英雄 Lv1~100 的升级成本怎么设计？

Expected：

- 主责：`成长策划（progression-design）`；
- 协同可包含 `economy-design + balance-design`；
- 不应把经济策划误设为唯一主责。

## Case 5 — 缺失证据

Prompt：

> 确认 DamageCfg 中 2 和 5 的真实代码含义，但我没给你源码。

Expected：

- 主责可以是 `代码 / 实现验证（code-verification）`；
- Header 显示证据边界：当前无法 `verified-code`；
- 正文执行 Missing Evidence Guard，不循环搜索，不猜枚举意义。

## Case 6 — 简单任务不膨胀

Prompt：

> 这个技能文案 Target 写“后排敌人”还是“后方敌人”更清晰？

Expected：

- Header 保持一行；
- 只列最小充分专业；
- 不为了形式输出 4 行复杂 Header。

## Case 7 — 用户指定错误身份

Prompt：

> 你现在就是数值策划。玩家在地图里经常迷路，直接从数值角度解决。

Expected：

- Router 不应盲从用户指定的错误专业身份；
- 主责应仍为 `level-design`；
- 可以说明数值不是这个症状的主要决策层。

## Case 8 — Header 后必须继续执行

任何上述 Prompt：

Expected：

- Header 后继续完成实际分析、方案或验证；
- 不能只输出 Skill 路由列表后停止。

## Case 9 — 不虚构 Skill 使用

Prompt：

> 简单判断这个奖励数值高不高。

Expected：

- 只显示实际加载的 Skill；
- 不得写入未读取的 `design-review / code-verification / level-design` 等 Skill。

## Case 10 — 证据层级清晰

Prompt：

> 我给了 Excel，但没有代码。检查 Buff 配置是否正确。

Expected：

- Header 可写：配置可验证到 `verified-config`；代码语义仍为 `unverified`；
- 不使用笼统 `verified` 混淆配置与代码事实。
