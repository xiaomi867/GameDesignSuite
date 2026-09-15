# Cross-Game Skill Scaling Patterns

本参考从崩坏：星穹铁道、原神、鸣潮公开角色与技能页提炼技能等级数值成长模式。只用于 Benchmark 与验证思路，不直接迁移倍率。

## Source Boundary

首批来源：

- `https://sr.appfeng.com/character`
- `https://ys.appfeng.com/character`
- `https://mc.appfeng.com/avatar`
- 公开Wiki的 Ability/Talent/Forte Scaling 页面用于交叉验证技能等级表。

任何精确倍率必须记录角色、技能、技能等级、来源日期和版本。

## HSR Pattern

公开技能数据可观察到：

- Basic ATK 常有独立较短等级区间；
- Skill / Ultimate / Talent 常有更长等级区间；
- Eidolon/Trace可提供额外技能等级，使Extended Level超过常规上限；
- 同一技能中，Damage、Base Chance、Action Delay、Buff等字段可以采用不同成长速度；
- 有些Utility字段保持固定。

示例性公开曲线：

- 多个Basic ATK可见 50% -> 100%（常规等级）并有更高Extended值；
- 飞霄Skill公开数据可见 100% 在常规高等级增长至约200%，Extended继续到更高值；
- Welt Skill同时存在Damage成长与Base Chance缓慢成长，说明“同一技能不同字段不同曲线”是可行模式。

这些只是具体角色事实，不是项目标准。

## Genshin Pattern

公开 Talent Level Scaling 数据显示存在多个Scaling Family：

- Normal/Physical Attack类；
- Elemental Percentage类；
- Flat Heal/Shield/Effect类；
- 少量特殊曲线。

同一技能里百分比值和Flat值可以使用不同Level Multiplier；某些机制的数值并非纯粹按通用曲线放大。

可迁移模式：

- 先按Parameter Type选择成长族；
- Throughput与Utility分离；
- 普攻与元素技能未必共享曲线；
- 特殊技能允许例外，但需要明确原因与回归测试。

不可直接迁移：具体1~15级Multiplier表、Talent上限、资源成本。

## Wuthering Waves Pattern

公开Forte/Skill页面常给出 Lv1~10 的完整Attribute Scaling表。

可观察到：

- 多个Damage字段从Lv1到Lv10接近约2倍量级，但每一级并非简单固定百分比；
- 不同Damage段可以保持相同曲线形状；
- Concerto Regen、Energy Cost、Cooldown等Utility/Economy字段经常保持固定；
- 多段技能、重击、共鸣技能、Forte等会共享或区分伤害分类；
- Sequence/共鸣链再叠加独立的倍率、触发、资源或规则升级。

公开例子中，Roccia Forte与其他技能页面可看到完整1~10数值表，同时Concerto Regen保持固定，说明“只成长Throughput、不成长所有字段”是一种常见结构。

## Cross-Game Shared Pattern

三个项目共同提示：

1. 技能等级不是“所有数字一起乘系数”；
2. Throughput参数最常持续成长；
3. Utility、Cost、Cooldown、Target Count等参数往往固定或低速成长；
4. 高阶成长节点可能改变机制，而不是继续叠倍率；
5. Extended Skill Level必须单独检查，因为它会和角色等级、装备、星级产生乘法叠加。

以上为 `supported-inference`。

## Benchmark Fields

每个外部技能至少记录：

- Character；
- Skill Type；
- Skill Level；
- Damage/Heal/Shield values；
- Buff/Debuff values；
- Base Chance；
- Duration；
- Cooldown；
- Resource Cost/Gain；
- Target Count；
- Hit Count；
- Fixed fields；
- Extended-level source；
- Source Date / Version。

## Normalization

跨技能比较优先：

`NormalizedSkillValue(s)=V(s)/V(max)`

`GrowthRatio=V(max)/V(1)`

`RelativeLevelDelta=V(s)/V(s-1)-1`

再结合：

`RealizedValue = PerUseValue × Frequency × TargetFactor × Reliability`

不要直接跨游戏比较“200% vs 300%”。
