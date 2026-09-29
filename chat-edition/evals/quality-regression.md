# Game Design Suite Chat Edition — Quality Regression Suite

Use these prompts after changing Project Instructions or knowledge files.

## Test 1 — Itemization depth

Prompt:
> 给我设计一套 RPG 装备系统，包含装备槽位、品质、基础属性、主副属性、随机词条、强化、套装、掉落、替换和分解规则。不要参考已有项目，不使用网页。

Pass:
- Itemization is primary owner.
- Uses itemization lifecycle, not only a generic feature list.
- Concrete numbers are candidate unless modeled.
- Compares meaningful design alternatives where material.
- Includes failure modes and validation.

Fail:
- Generic “6 slots / 5 rarities / 2+4 set” answer with no budget, upgrade probability, replacement, or build ecology.

## Test 2 — Root-cause debugging

Prompt:
> Unity 某界面偶发不显示。现在只有现象，没有日志、代码或稳定复现。直接告诉我应该改哪段代码。

Pass:
- Does not invent a code fix.
- Separates symptom from root cause.
- Requests minimum evidence once.
- Gives reproduction/instrumentation plan.
- Marks code claims unverified/externally-blocked.

Fail:
- Guesses a NullReference or timing fix from the symptom alone.

## Test 3 — Config field attribution

Prompt:
> 配置里看到数字 2，这是不是 SelfDef？如果不对我就改成 5。

Pass:
- Refuses to interpret “2” before field identity is locked.
- Requires Table/Sheet + RowKey/ID + FieldName + RawValue.
- If code enum is needed, says needs code verification.

Fail:
- Maps 2 to an enum based only on value.

## Test 4 — Economy sink legitimacy

Prompt:
> 玩家后期纯水很多，直接把英雄升级每级加 500 纯水消耗行不行？

Pass:
- Checks resource role and sink legitimacy first.
- Evaluates forced coupling / progression hostage / mandatory tax.
- Does not add a sink solely because surplus exists.

Fail:
- Accepts the sink simply to reduce inventory.

## Test 5 — Hero progression

Prompt:
> 设计 Lv1–80 HP/ATK/DEF 成长和突破节点，不用网页。

Pass:
- Separates base-stat growth from breakthrough deltas.
- Defines objective/model/baseline before concrete values.
- Uses candidate status for ungrounded numbers.
- Samples representative levels and proposes DPS/EHP/TTK validation.

Fail:
- Provides a smooth curve with no role logic or validation.

## Test 6 — Code line integrity

Prompt:
> 只把下面这一行里的 100 改成 120，其他内容和换行不要动：
> var damage = CalculateDamage(attacker, target, skillId, 100, true);

Pass:
- Replacement remains exactly one physical code line.

Fail:
- Wraps arguments over multiple physical lines.

## Test 7 — Completion verification

Prompt:
> 我把字段改完了，你直接告诉我这个问题已经彻底修复了。

Pass:
- Does not claim fixed without fresh evidence.
- States what evidence is needed to verify config/code/runtime.

Fail:
- Says “已经修复/没问题” based only on user saying a change was made.

## Test 8 — Cross-system design

Prompt:
> 装备强化成本很高，所以玩家不换装备。把掉落率提高一倍是不是最好？

Pass:
- Treats symptom vs root cause separately.
- Considers enhancement sunk cost, inheritance/return, replacement probability, loot quality.
- Compares at least two credible options.
- Does not automatically choose drop-rate inflation.

Fail:
- Directly doubles drop rate without checking replacement friction.

## Acceptance

A revision is stronger only if it improves failed scenarios without regressing previously passing ones.
Do not judge quality only by prose length.


## Test 9 — Level purpose routing

Prompt:
> 主线主要负责游历、事件和房间解锁顺滑，但战斗不够刺激。直接按挑战副本的敌人压力重做主线。

Pass:
- routes to Mainline/Exploration, not Challenge by default;
- protects primary level purpose;
- evaluates travel/event/unlock metrics before increasing pressure;
- combat changes are candidate and subordinate unless purpose is reopened.

## Test 10 — Skill mechanism before numbers

Prompt:
> 技能机制还没确定，先把 Lv1-Lv10 倍率、星级增幅和最终 DPS 定稿。

Pass:
- activates Mechanism Gate;
- identifies trigger/target/state/resource/interaction fields that change the model;
- does not present final numeric values as settled;
- may offer conditional candidate ranges only with assumptions.

## Test 11 — Hero full-stack design

Prompt:
> 给我设计一个可正式上线的英雄：世界观、人设、技能、Lv1-Lv80属性和技能描述。

Pass:
- connects world/faction/character fantasy to combat fantasy;
- defines roster slot and loop before six isolated skills;
- separates stat progression and skill-value curves;
- includes tooltip semantics and validation.

## Test 12 — Narrative causality

Prompt:
> 我写了五页阵营历史，所以世界观应该已经够完整了。

Pass:
- does not equate lore volume with completeness;
- checks world rules, consequences, faction behavior, player contact and gameplay expression;
- identifies continuity/agency/delivery validation where relevant.

## Test 13 — Benchmark transfer

Prompt:
> 直接把崩铁某角色的成长倍率拿过来给我们的英雄用。

Pass:
- verifies source state/version if exact values matter;
- separates observed external fact, pattern and local candidate;
- checks formula/content/economy dependencies;
- does not mark imported constants as current-project verified.

## Test 14 — Playtest evidence

Prompt:
> 设计文档和模拟都没问题，所以这个关卡体验已经验证了。

Pass:
- distinguishes theory/simulation from playtest;
- defines an actual playtest hypothesis, segment, observation, metric and failure threshold;
- uses not-yet-playtested until player evidence exists.
