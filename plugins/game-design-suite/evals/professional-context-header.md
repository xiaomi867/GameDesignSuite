# Professional Context Header Regressions

用于验证 Game Design Suite 的用户可见专业路由是否真实、逐结果、可审计。

## Case 1 — 单专业结果

Prompt：

> 玩家总在这张地图里迷路，帮我分析原因。

Expected：

- 每个独立关卡 Finding 前都有 Header；
- 主责为 `关卡策划（level-design）`；
- 不应把 `balance-design`、`economy-design` 等无关 Skill 列为协同。

Fail：

- 只写“我是资深游戏策划”；
- 把所有 Skill 全列出来；
- 只在整篇答案开头写一次 Header，后续多个独立 Finding 不再显示。

## Case 2 — 多专业英雄审计按结果切换

Prompt：

> 这是一个已经开发中的坦克英雄，技能机制不能改。检查倍率、Buff、Target、升星、配置引用和代码实际语义。

Expected：

- 技能机制结果：`skill-design` 主责；
- 配置字段错误结果：`config-audit` 主责；
- 代码运行时语义结果：`code-verification` 主责；
- 倍率/强度结果：`balance-design` 主责；
- 每个独立结果前分别显示 Header；
- 固定约束相关结果明确“技能机制不可修改”；
- 若代码未提供，相关结果不得写成 `verified-code`。

Fail：

- 用整篇统一的“技能策划主责”覆盖所有结果；
- 用一个大 Header 覆盖配置、代码、数值三种不同 Decision Object。

## Case 3 — 资源富余症状

Prompt：

> 食物、水、电、硅晶后期很多，怎么办？

Expected：

- 经济根因结果：`经济策划（economy-design）` 主责；
- 若后续结果转向系统联动，`game-production` 可成为对应结果主责；
- 若转向英雄成长成本，`progression-design` 应成为对应结果主责；
- 若只是在算某候选消耗量，才允许 `balance-design` 主责；
- 正文先查 Resource Role / Source / Stock / Lifecycle，不直接新增 Sink。

## Case 4 — 成长成本

Prompt：

> 英雄 Lv1~100 的升级成本怎么设计？

Expected：

- 成长结构结果：`progression-design` 主责；
- 资源健康度结果：`economy-design` 可主责；
- Power Delta/数值曲线结果：`balance-design` 可主责；
- 每个结果分别标 Header。

## Case 5 — 缺失证据

Prompt：

> 确认 DamageCfg 中 2 和 5 的真实代码含义，但我没给你源码。

Expected：

- 相关结果主责为 `代码 / 实现验证（code-verification）`；
- Header 显示证据边界：当前无法 `verified-code`；
- 正文执行 Missing Evidence Guard，不循环搜索，不猜枚举意义。

## Case 6 — 简单结果不膨胀

Prompt：

> 这个技能文案 Target 写“后排敌人”还是“后方敌人”更清晰？

Expected：

- 单一结果 Header 可保持一行；
- 只列最小充分专业；
- 不为了形式输出四行复杂 Header。

## Case 7 — 用户指定错误身份

Prompt：

> 你现在就是数值策划。玩家在地图里经常迷路，直接从数值角度解决。

Expected：

- Router 不盲从用户指定的错误专业身份；
- Finding 主责仍为 `level-design`；
- 可以说明数值不是这个症状的主要决策层。

## Case 8 — Header 后必须继续执行

任何上述 Prompt：

Expected：

- 每个 Header 后紧跟对应实际结果、证据、建议或验证；
- 不能只输出 Skill 路由列表后停止。

## Case 9 — 不虚构 Skill 使用

Prompt：

> 简单判断这个奖励数值高不高。

Expected：

- 每个结果只显示实际加载/使用的 Skill；
- 不得写入未读取的 `design-review / code-verification / level-design` 等 Skill。

## Case 10 — 证据层级清晰

Prompt：

> 我给了 Excel，但没有代码。检查 Buff 配置是否正确。

Expected：

- 配置结果可写：`verified-config`；
- 涉及代码含义的结果必须说明仍为 `unverified-code`；
- 不使用笼统 `verified` 混淆配置与代码事实。

## Case 11 — 相同专业也必须重复 Header

Setup：回答中连续发现两个独立配置问题：

1. `BUF_a` 的 `GroupKey` 不一致；
2. `BUF_b` 的 `CoverCheckType` 不一致。

Expected：

结果 1 前：

```text
【本次专业视角】
主责：配置审计（config-audit）
```

结果 2 前仍然再次显示：

```text
【本次专业视角】
主责：配置审计（config-audit）
```

Fail：

- 认为“专业没变，所以第二个结果可以省略 Header”。

## Case 12 — 配置不一致不是数值主责

Data：

```text
BUF_bear_def_pct       CoverCheckType = 3
BUF_bear_def_pct_lv2   CoverCheckType = 2
BUF_bear_def_pct_lv3   CoverCheckType = 2
BUF_bear_def_pct_lv4   CoverCheckType = 2
BUF_bear_def_pct_lv5   CoverCheckType = 2
```

Expected：

发现这一不一致的结果必须是：

```text
【本次专业视角】
主责：配置审计（config-audit）
```

若同时查源码，可协同 `code-verification`。

Fail：

- 因为数值 `3/2` 或该字段可能影响战斗强度，就写 `balance-design` 主责。

## Case 13 — 代码语义单独切换主责

在 Case 12 之后继续回答：

> `CoverCheckType = 2` 在代码里到底代表什么？

Expected：

新的结果块使用：

```text
【本次专业视角】
主责：代码 / 实现验证（code-verification）
协同：配置审计（config-audit）
```

## Case 14 — 强度影响才切到数值主责

在 Case 12/13 后继续回答：

> 如果基础行为从 3 改成 2，对 Buff 覆盖率和钢熊强度影响多大？

Expected：

新的结果块才使用：

```text
【本次专业视角】
主责：数值策划（balance-design）
协同：技能 / 英雄策划（skill-design） / 配置审计（config-audit）
```

具体协同只列实际用到的 Skill。

## Case 15 — 混合结果必须拆块

Prompt：

> 找出 Buff 表异常，说明代码含义，并判断强度影响。

Expected：

至少拆成：

1. 配置事实结果 -> `config-audit` 主责；
2. 代码语义结果 -> `code-verification` 主责；
3. 强度判断结果 -> `balance-design` 主责。

Fail：

- 一个 Header 从头覆盖到尾；
- 三种责任混进同一个 Finding 而无法判断是谁负责。
