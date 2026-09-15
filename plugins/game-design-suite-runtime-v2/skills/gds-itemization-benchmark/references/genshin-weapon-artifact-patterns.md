# Genshin Impact Weapon & Artifact Patterns

用途：记录《原神》武器与圣遗物系统中对通用 Itemization 设计有参考价值的公开结构。只用于参考和验证，不把具体数值直接迁移到其他项目。

## 1. 武器结构

公开资料支持以下稳定结构：

- 武器按类型区分单手剑、双手剑、长柄、弓、法器；
- 3★及以上武器通常具有基础攻击、一个副属性和一个被动；
- 武器等级成长至 90 级，并存在突破节点；
- 副属性随武器等级成长；
- 被动通过精炼 Rank 1~5 成长；
- 不同武器会形成不同的“基础攻击 / 副属性”组合，而不只是所有武器共享同一白值曲线；
- 被动可能是常驻增益、条件增益、触发效果、资源效果或角色行为联动。

可迁移模式：

### Base Stat / Secondary Stat Budget Family

同一品质武器可以通过：

- 高基础 / 低副属性；
- 中基础 / 中副属性；
- 低基础 / 高副属性；

形成不同预算家族。

但在其他项目中必须先用自己的伤害公式、基础属性和角色成长验证交换率。

### Refinement as Duplicate Value

重复武器不是简单返还资源，而是可以提高被动参数。

可迁移问题：

- 重复品是否应该提高基础属性、特效，还是转为其他资源；
- Rank 1 是否已经完整可用；
- Rank 5 是否只是纵向强化，还是会改变机制；
- 重复品价值是否导致付费/获取压力过高。

### Ascension Breakpoints

1~90 不是纯线性一条线，突破承担：

- 等级上限；
- 材料门槛；
- 数值成长阶段；
- 长线节奏节点。

对标时应采样突破前后，而不是只看 Lv1 / Lv90。

## 2. 圣遗物结构

公开资料支持：

- 圣遗物有 5 个槽位；
- 花与羽具有固定主属性；
- 沙、杯、冠承担随机主属性选择；
- 5★圣遗物最高 +20；
- 5★圣遗物初始通常有 3~4 条副词条；
- 每 +4 级发生一次副词条新增或强化事件；
- 副词条不能重复，也不能与主属性完全同名；
- 套装常见为 2 件 / 4 件效果；
- 主属性、套装、初始副词条、强化命中共同构成多层随机。

## 3. 可迁移模式

### Fixed + Variable Slot Architecture

固定槽位降低一部分搜装随机，随机槽位承担 Build差异。

### +20 / Every-4-Level Event

+20 对应 5 个关键副词条事件节点。

值得对比 HSR 的 +15 / 每3级节点：

```text
不同最大强化等级
可以拥有相近的有意义升级事件数量
```

可迁移的是“事件密度”的概念，而不是 +20 本身。

### Main Stat Gating

不同槽位主属性池不同，使：

- 某些功能属性只有特定槽位能拿；
- Build选择被压缩到可理解的槽位决策；
- 同时也会提高特定主属性的刷取压力。

### Set Lock vs Off-Piece Flexibility

2/4件套装允许一个非套装槽位承担高质量散件，这是一种“套装压力与单件质量”之间的结构平衡。

是否适合其他项目，要看：

- 总槽位数；
- 套装门槛；
- 单件随机深度；
- 玩家获取频率。

## 4. 设计风险

- **Crit Convergence**：输出Build大量追暴击/暴伤；
- **Elemental Goblet Scarcity**：功能/伤害类型主属性池过宽会放大目标掉落稀缺；
- **Set + Main + Substat Multiplication**：多层随机相乘后，实际升级率远低于名义掉率；
- **Signature Weapon Pressure**：专武被动若同时覆盖基础属性、关键副属性和角色专属机制，可能形成完成度税；
- **Refinement Scaling Pressure**：重复品继续提高被动，需评估付费/获取差距和边际价值。

## 5. Benchmark 使用

武器对标时比较：

```text
Base Attack Curve
Secondary Stat Curve
Ascension Breakpoints
Passive R1~R5 Delta
Signature Fit
Alternative Coverage
```

圣遗物对标时比较：

```text
Slot Main-stat Gating
Initial Substat Count
Upgrade Event Count
Roll Tier Spread
Set Threshold
Off-piece Flexibility
Effective Upgrade Funnel
```

不要只拿某把90级武器或某件+20圣遗物的满级值直接作为项目候选。

## 6. 主要来源

- https://ys.appfeng.com/weapon
- https://ys.appfeng.com/reliquary
- https://genshin-impact.fandom.com/wiki/Weapon
- https://genshin-impact.fandom.com/wiki/Artifact/Stats

AppFeng 适合通过详情页和等级进度条查看 Lv1~90 武器、突破与精炼，以及不同强化等级的圣遗物属性；若详情页当前无法抓取，应标 `externally-blocked`，不要从记忆补值。
