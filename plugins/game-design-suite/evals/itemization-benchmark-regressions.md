# Itemization Benchmark Regression Cases

这些 Case 用于防止外部游戏参考被错误变成当前项目真值。

## Case 1 — 直接复制主属性

Prompt:

> 星铁5星遗器攻击%是43.2%，那我们装备主属性也直接用43.2%吧。

Expected:

- `itemization-benchmark` 识别 43.2% 只属于外部参考事实；
- 不直接迁移；
- 转 `itemization-design + balance-design` 建项目 Benchmark / Exchange Rate；
- 项目候选只能标 `candidate`。

FAIL:

- 直接说43.2%是行业标准；
- 直接给项目定43.2%。

## Case 2 — 只看满级值

Prompt:

> 比较三款游戏装备成长，只看满级属性就够了。

Expected:

- FAIL premise；
- 要求采样等级滑杆、突破前后和关键强化节点；
- 使用 `V(level)/V(max)` 或等价归一化比较曲线。

## Case 3 — +15 / +20 / +25 谁成长更多

Prompt:

> +25一定比+15成长更细，所以鸣潮装备系统更高级。

Expected:

- 不以最大等级数量判断；
- 比较 meaningful upgrade event count / density；
- 可指出 HSR每3级、Genshin每4级、Wuthering Waves每5级都能形成约5次关键副词条事件这一结构 Pattern；
- 不做游戏优劣结论。

## Case 4 — 5星跨游戏等价

Prompt:

> 都是5星，所以三款游戏的5星装备应该用同一Power Budget比较。

Expected:

- 拒绝 Rarity Equivalence；
- 先归一化游戏内预算、战斗公式、装备在总战力中的占比；
- 不能直接比较绝对数值。

## Case 5 — 外部页面打不开

Prompt:

> 这个AppFeng详情页现在打不开，你按记忆把每一级数值补齐。

Expected:

- 标 `externally-blocked`；
- 不从记忆补精确值；
- 可继续做不依赖精确值的结构分析；
- 列出最小缺失数据。

## Case 6 — AppFeng与Wiki冲突

Prompt:

> 两个来源数值不一样，挑一个看起来合理的就行。

Expected:

- 不静默选值；
- 检查版本、等级、突破、显示取整、样本/数据表差异；
- 冲突未解决前保留两个来源。

## Case 7 — 词条事件密度迁移

Prompt:

> 星铁每3级，原神每4级，鸣潮每5级，所以我们的强化也必须5次Roll。

Expected:

- 识别“约5次有意义事件”是参考 Pattern，不是硬标准；
- 结合项目强化长度、Loot频率、认知负担、随机层决定 candidate；
- 不直接定5次。

## Case 8 — 武器只比白值

Prompt:

> 两把武器谁强只看90级基础攻击就行。

Expected:

- 拆 Base Stat / Secondary / Passive / Refinement-or-Resonance / Character Fit / Rotation Reliability；
- 若判断具体强度，切 `balance-design`。

## Case 9 — 套装倍率照抄

Prompt:

> 鸣潮2件套经常是10%属性伤害，我们也统一2件套10%。

Expected:

- 10%仅为外部观察；
- 当前项目套装倍率必须由自身 Power Budget、槽位锁定成本和覆盖率决定；
- 只能作为参考区间输入，不可直接定稿。

## Case 10 — Cost系统照搬

Prompt:

> 鸣潮Cost 4/3/1很好，我们项目也改成Cost系统。

Expected:

- 先回答 Cost-constrained loadout 在原系统解决什么问题；
- 检查当前项目是否已有固定槽位、构筑随机、认知负担；
- 只能作为 candidate；
- 不因参考游戏成熟就判定适用。

## Case 11 — 用户提供当前项目配置

Prompt:

> 我把我们的装备表发你，和星铁/原神/鸣潮对比后告诉我哪些值错了。

Expected:

- `itemization-benchmark` 负责外部对标；
- `config-audit` 负责当前表事实；
- `itemization-design / balance-design` 判断项目结构和强度；
- 外部不同 ≠ 当前项目错误。

## Case 12 — 参考事实冒充项目验证

Prompt:

> 三个商业游戏都这么做，所以这个设计已经verified了。

Expected:

- 明确外部事实最多证明 pattern existence；
- 当前项目仍是 `candidate / supported-inference`，除非有项目内配置/代码/模拟/runtime/playtest/telemetry证据；
- FAIL Reference-to-Verified Leap。
