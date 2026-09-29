# Game Design Suite Chat Edition — Commercial Game Benchmark Library

> Purpose: retain user-provided commercial-game references as thinking material for game design, numerical design, itemization, hero progression, formulas, systems, and level/pacing analysis.
> These sources are references, not standards for the user's project.

## Evidence policy

External commercial-game sources use:
- `official-data`: directly visible official game data or official pages.
- `community-theorycraft`: community-derived formulas / testing.
- `community-wiki`: structured community database/wiki.
- `pattern-only`: use architecture/pattern, not constants.
- `version-sensitive`: may change by patch/version.

Never upgrade an external benchmark into the user's project `verified-config`, `verified-code`, or `verified-runtime`.

When extracting a precise value, record:
`Game + Version/Date + Character/Item/System + Level/Rank/State + Source URL`.

Interactive pages with level/skill sliders require recording the selected state. Do not copy the default max-level screen as Lv1.

## Honkai: Star Rail / 崩坏：星穹铁道

### Character / progression / skill data
- https://sr.appfeng.com/character
- https://sr.appfeng.com/character/1504
- https://wiki.biligame.com/sr/%E8%A7%92%E8%89%B2%E5%9B%BE%E9%89%B4
- Example cross-check page previously used: https://wiki.biligame.com/sr/%E6%99%AF%E5%85%83

Use for:
- HP / ATK / DEF growth;
- fixed identity stats such as SPD, Energy Max, Taunt;
- ascension/breakpoint structure;
- skill rank topology;
- trace/stat bonus structure;
- eidolon/star-node style mechanic upgrades;
- growth-material cadence.

A detail page can expose max-level base stats, skill rank ranges, ascension-material states and other character data. Treat level selection as stateful and capture it explicitly.

### Relics / itemization
- https://sr.appfeng.com/relic

Use for:
- slot architecture;
- fixed-main-stat vs variable-main-stat slots;
- functional stat taxonomy;
- set-effect taxonomy;
- strengthening event cadence;
- affix/roll structure.

### Formula / theorycrafting
- https://www.hoyolab.com/article/36700608
- https://www.hoyolab.com/article/18126946
- https://hsr.keqingmains.com/misc/speed-guide/
- https://www.hoyolab.com/article/19460061
- https://www.hoyolab.com/article/18981104
- https://hsr.keqingmains.com/fu-xuan/

Use for:
- damage multiplier decomposition;
- DEF / RES / vulnerability / mitigation;
- speed, action value, advance/delay;
- effect hit / effect resistance;
- toughness / break;
- incoming damage and mitigation analysis.

All are reference/community models unless independently verified.

## Genshin Impact / 原神

- https://ys.appfeng.com/character
- https://ys.appfeng.com/weapon
- https://ys.appfeng.com/reliquary

Use for:
- character level/ascension growth;
- bonus-stat unlock cadence;
- weapon base-stat / secondary-stat budget families;
- weapon refinement as duplicate value;
- artifact fixed/variable slot structure;
- main/substat randomization;
- 2-piece/4-piece set architecture;
- strengthening event density;
- long-term replacement/graduation cost.

Do not assume Genshin's level caps or exact multipliers are timeless. Record source date/version.

## Wuthering Waves / 鸣潮

- https://mc.appfeng.com/avatar
- https://mc.appfeng.com/weapon
- https://mc.appfeng.com/echo

Use for:
- avatar base-stat and skill-level curves;
- weapon base/substat families and rank progression;
- Echo / Sonata set architecture;
- cost-slot structure;
- build diversity and equipment-role coupling;
- resonance resource/efficiency related attributes.

Wuthering Waves is a cross-game benchmark, not a miHoYo title.

## Zenless Zone Zero / 绝区零

### User-provided MiHoYo-community links
- https://www.miyoushe.com/zzz/article/57192241
- https://www.miyoushe.com/zzz/article/55734399
- https://www.miyoushe.com/zzz/article/56637226
- https://www.miyoushe.com/zzz/article/55366836
- https://www.miyoushe.com/zzz/article/72454789

These were provided as design/numerical/system-analysis thinking material. Dynamic page content may not be reliably readable in every environment. When正文 cannot be fetched:
- retain URL as a source lead;
- do not claim exact contents were read;
- search/verify the same topic through a stable source before using exact formulas or constants.

### Stable cross-check formula sources
- https://www.hoyolab.com/article/28987778
- https://www.hoyolab.com/article/37522351
- https://www.hoyolab.com/article/35508795
- https://www.hoyolab.com/article/41060247
- https://www.prydwen.gg/zenless/guides/anomalies-and-disorders
- https://www.prydwen.gg/zenless/guides/agents-attributes
- https://github-wiki-see.page/m/Night-Sky-Studio/interknot-calculator/wiki/ZZZ-Formulas

Use for:
- direct-damage buckets;
- DEF shred / DEF ignore / PEN;
- RES;
- Daze/Stun windows;
- anomaly / disorder;
- energy and agent attributes;
- conditional vs unconditional stat layers.

## Benchmark extraction protocol

Do not “look at a game” and jump to a recommendation.

For every benchmark:
1. **Observed fact** — what the source actually shows.
2. **System job** — why that rule likely exists.
3. **Dependency** — which formulas/content/economy make it work.
4. **Player consequence** — what decision/behavior it creates.
5. **Transferable pattern** — the abstract design pattern.
6. **Non-transferable constants** — what must NOT be copied.
7. **Current-project fit** — what evidence would be needed to adopt it.

### Example
Observed:
- fixed main-stat slots + variable main-stat slots.

Pattern:
- stabilize part of the loot search space while reserving some slots for build expression.

Do NOT conclude:
- every RPG should use the same number of slots, the same stat pool, or the same +15/+20 enhancement cap.

## Cross-game comparison matrix

When comparing systems, normalize by role rather than raw number.

Useful columns:
- progression horizon;
- item slots;
- fixed vs random main stat;
- number of affixes;
- roll events;
- set/unique power budget;
- duplicate value;
- average usable-drop probability;
- expected replacement cadence;
- build lock-in;
- resource recovery/salvage;
- endgame graduation target;
- failure/tail behavior.

The purpose is to expand solution space and improve reasoning, not to clone a commercial game.


# 2026-09-30 Coverage Audit & Source Expansion

## A. What is already preserved

The Chat Edition currently preserves the user's known public benchmark families for:

- Honkai: Star Rail character/stat/skill/progression;
- HSR relic/itemization;
- HSR formula/theorycraft topics including SPD/action value, DEF/RES, effect hit/resistance, break/toughness and mitigation;
- Genshin character/weapon/reliquary structure;
- Wuthering Waves avatar/weapon/echo structure;
- Zenless Zone Zero formula/system-analysis leads, including the five user-provided MiHoYo-community URLs already listed above.

These sources support thinking about:
- character stat curves;
- skill level curves;
- ascension/breakpoints;
- combat formula decomposition;
- action economy;
- energy/resource loops;
- itemization;
- build structure;
- role/roster patterns.

They remain reference-data.

## B. Current public source availability

When this audit was performed, the following public index families were accessible and suitable as source leads:

- `https://sr.appfeng.com/character`
- `https://sr.appfeng.com/relic`
- `https://ys.appfeng.com/character`
- `https://mc.appfeng.com/avatar`
- `https://mc.appfeng.com/weapon`
- `https://mc.appfeng.com/echo`

Individual pages can expose stateful level/skill/progression information. Re-check exact page state when extracting a value.

Some dynamic pages may fail in a particular browser/tool session. Failure to fetch is not evidence that the source or data does not exist.

## C. System / Level / Production References

Commercial-game numerical pages alone are not enough to improve level/system reasoning. Also use stable design/production references such as:

### HoYoverse / related
- GDC Vault: `Honkai: Star Rail — Reimagining RPGs for Mass Audiences and Broad Appeal`
  - https://gdcvault.com/play/1035480/-Honkai-Star-Rail-Reimagining
  - use for design principles, accessibility/depth framing, universe/content expansion.
- GDC 2021: `Genshin Impact: Building a Scalable AI System`
  - https://media.gdcvault.com/GDC%2B2021/20210528_%2BGDC21_shuo_presentation%2B_Final.pdf
  - use for AI/system/level-scripted behavior and production architecture context.

### Level design
- GDC: `Ten Principles for Good Level Design`
  - https://www.gdcvault.com/play/1019023/Ten-Principles-for-Good-Level
- GDC: `Level Design Fundamentals & Techniques`
  - https://www.gdcvault.com/play/1022453/Level-Design-Fundamentals
- GDC: `Level Design in a Day — Decisions That Matter`
  - https://www.gdcvault.com/play/1021073/Level-Design-in-a-Day
- GDC: `A Narrative Approach to Level Design`
  - https://gdcvault.com/play/1024302/
- GDC: `An Approach to Holistic Level Design`
  - https://www.gdcvault.com/play/1024301/Level-Design-Workshop-An-Approach

Use these for process/pattern extraction, not as proof that a current project level is correct.

### Character / Hero
- GDC: `Character Design Across Multiple Game Genres`
  - https://www.gdcvault.com/play/1020595/Character-Design-Across-Multiple-Game
- GDC: `Characterization, Purpose and Action: Creating Strong Video Game Characters`
  - https://www.gdcvault.com/play/1020440/Characterization-Purpose-and-Action-Creating
- GDC: `Creating Compelling Characters`
  - https://gdcvault.com/play/1024290/Creating-Compelling-Characters-Insights-from
- GDC: `Fundamental Multiplayer RPG Math`
  - https://gdcvault.com/play/1015037/Fundamental-Multiplayer-RPG

Use these to enrich character purpose, genre fit, gameplay action, and data-driven RPG stat frameworks.

## D. Benchmark Retrieval Contract V2

For any precise external comparison record:

`Game + Version/Date + Object + State(Level/Rank/Skill/Equipment) + Source + Observed Fact`

Then derive separately:

`System Job -> Dependency -> Player Consequence -> Pattern -> Transfer Risk -> Candidate Use -> Local Validation`

If exact version/state is unknown, do not quote exact values as stable truth.

## E. Historical-source honesty

The current repository proves preservation only for sources actually listed in current files.

If an older conversation contained additional URLs that are not present in the repository or current context, do not claim they were preserved. Recover them when available, then add them to this registry.

The goal is a durable source map, not the appearance of complete memory.
