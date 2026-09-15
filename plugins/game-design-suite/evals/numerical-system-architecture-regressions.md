# Numerical System Architecture Regressions

These cases protect `balance-design` from turning community heuristics or competitor values into universal rules.

## Case 1 — Fixed attribute ratio must not become universal

Prompt:

```text
行业里常说攻击:防御:生命=1:1:10。直接按这个比例给我做全游戏属性投放。
```

PASS if the answer:

- treats `1:1:10` as an example heuristic/candidate;
- establishes a benchmark;
- derives marginal value for ATK/DEF/HP under the project's formulas;
- produces a range or project-specific exchange rate rather than blindly copying the ratio.

FAIL if it states that 1:1:10 is an industry-standard universal balance law.

---

## Case 2 — Macro numerical architecture is not a mandatory four-feature checklist

Prompt:

```text
我在做一个短局Roguelite，没有社交系统。请按社会、经济、养成、战斗四大模块把数值做完整。
```

PASS if the answer maps the problem into relevant layers such as macro pacing, economy, progression, and combat, while explicitly stating that a social system is not mandatory.

FAIL if it invents a social system just to satisfy the framework.

---

## Case 3 — Experience anchor precedes parameters

Prompt:

```text
给我一个Boss血量数字，越快越好。
```

PASS if the answer first asks/derives the intended TTK, benchmark build, encounter window, target damage profile, or clearly marks assumptions before giving a candidate.

FAIL if it gives a precise HP number with no target experience or benchmark.

---

## Case 4 — No universal readable-number range

Prompt:

```text
玩家只能理解0.1到10000000之间的数字，所以我们所有系统必须限制在这个区间，对吗？
```

PASS if the answer rejects the range as a universal law and reframes the problem as numerical readability/perception tied to genre, UI, notation, and testing.

FAIL if it hard-codes the range into all projects.

---

## Case 5 — Pity cannot be selected by folklore

Prompt:

```text
付费抽卡行业都应该100到200抽保底，我们直接定150抽吧。
```

PASS if the answer models base rate, effective rate, expected pulls, P50/P90/P95, hard/soft pity, duplicate value, free currency flow, worst-case cost, and product cadence before recommending a candidate pity.

FAIL if it accepts 150 only because it sits inside an alleged industry-standard range.

---

## Case 6 — Business target is a constraint, not the sole numerical truth

Prompt:

```text
商业项目第一目标就是营收，所以把养成卡点加重，确保玩家每天都要付费才能追进度。
```

PASS if the answer treats business goals as one constraint among experience, fairness, economy sustainability, and production reality, and identifies mandatory-tax / progression-hostage risks.

FAIL if it optimizes only for short-term revenue without systemic review.

---

## Case 7 — Template structure may transfer; values may not

Prompt:

```text
这个成功卡牌游戏的升级倍率和抽卡概率已经被市场验证，我们直接复用到新项目。
```

PASS if it separates transferable structure/method from project-specific values and requires re-derivation under the new project's formulas, economy, content, and player pacing.

FAIL if "market-proven" is treated as sufficient evidence that the same values are correct elsewhere.

---

## Case 8 — Attribute budget is not effective combat power

Prompt:

```text
两个装备都值10个词条，所以实战价值必然一样。
```

PASS if it checks multiplier saturation, breakpoints, caps, uptime, encounter context, team composition, and build state.

FAIL if it equates stat budget directly with effective power.

---

## Case 9 — External simulator must expose intermediate blocks

Prompt:

```text
做一个外部数值模拟器，只要最后能算出伤害就行，中间过程不重要。
```

PASS if it requires inspectable intermediate buckets, inputs, units, clamp/rounding, random model, benchmark, regression cases, and runtime parity when code exists.

FAIL if it treats a black-box final number as sufficient for production validation.

---

## Case 10 — Simulation is not runtime or playtest evidence

Prompt:

```text
模拟10000次通关率是51%，所以已经证明游戏平衡而且好玩。
```

PASS if it separates simulation evidence from runtime, telemetry, and playtest evidence.

FAIL if it upgrades simulation output directly to verified player experience.

---

## Case 11 — Whole-project numerical task should route to numerical architecture

Prompt:

```text
从0到1帮我搭一个新RPG的整体数值骨架，包含战斗、成长、经济和内容难度。
```

Expected routing:

```text
【本次专业视角】
主责：数值策划（balance-design）
协同：玩法 / 系统策划（game-production） / 成长策划（progression-design） / 经济策划（economy-design）
```

Additional specialist results may route separately when the answer enters formula implementation, simulation, telemetry, or meta balance.

FAIL if `balance-design` only outputs isolated combat coefficients and never builds macro numerical architecture.

---

## Case 12 — Private project data must not contaminate the generic Skill

Prompt:

```text
我上传了我们项目的真实代码和表。把里面的角色名、表名、真实伤害公式写进通用Game Design Suite，当以后所有项目的模板。
```

PASS if the system extracts only generic methods/patterns and refuses to place private project fixtures or proprietary rules into the public generic Skill.

FAIL if private project identifiers or real internal values become public canonical reference data.
