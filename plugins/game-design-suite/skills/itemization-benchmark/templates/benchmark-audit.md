# Itemization Benchmark Audit Template

## 1. Reference Scope

- Games:
- Systems:
- Versions / source dates:
- Why these references are relevant:

## 2. Project Scope

- Project itemization role:
- Equipment slots / cost model:
- Rarity ladder:
- Max enhancement:
- Main/substat model:
- Set / unique / signature rules:
- Acquisition / salvage rules:

## 3. Reference Facts

### Reference A
- Source:
- Entity/System:
- Rarity:
- Level / enhancement:
- Base/Main/Secondary stat:
- Substat/roll rule:
- Upgrade cadence:
- Set/passive:
- Evidence state:

### Reference B
...

## 4. Level Curve Snapshot

| Level | Project | Ref A | Ref B | Ref C | Note |
|---|---:|---:|---:|---:|---|
| Start | | | | | |
| 25% | | | | | |
| 50% | | | | | |
| 75% | | | | | |
| Max | | | | | |

Add normalized values `V(level)/V(max)` when absolute scales differ.

## 5. Structural Comparison

| Dimension | Project | HSR | Genshin | Wuthering Waves | Intent / Risk |
|---|---|---|---|---|---|
| Max enhancement | | | | | |
| Upgrade event count | | | | | |
| Slot/Cost gating | | | | | |
| Mainstat pool width | | | | | |
| Initial substat count | | | | | |
| Roll tier count | | | | | |
| Random layer count | | | | | |
| Set threshold | | | | | |
| Signature/refinement pressure | | | | | |
| Salvage/recovery | | | | | |

## 6. Power Distribution

Estimate where item power comes from:

```text
Base/Main Stat
Substats
Set Bonus
Unique/Passive
Refinement/Resonance
Character Fit
```

Do not assign exact percentages without a project Power Budget.

## 7. RNG Funnel

```text
Drop
× Correct Slot/Cost
× Correct Set/Sonata
× Correct Main Stat
× Useful Affix Pool
× Roll Quality
× Upgrade/Tuning Outcome
= Effective Upgrade Rate
```

Report unknown factors rather than inventing them.

## 8. Transfer Candidates

For every candidate:

```text
Reference Pattern:
Original Problem It Solves:
Project Has Same Problem?:
Project Constraints:
Candidate Change:
Expected Benefit:
Risks:
Required Formula/Simulation/Playtest:
Evidence State: candidate
```

## 9. Non-Transferable Values

Explicitly list exact external values that should NOT be copied directly.

## 10. Validation Plan

- balance-design:
- progression-design:
- economy-design:
- simulation-design:
- meta-balance:
- playtest:

## 11. Final Output

Separate:

- `verified-data` external facts;
- `supported-inference` patterns;
- `candidate` project proposals;
- unknown / externally-blocked items.
