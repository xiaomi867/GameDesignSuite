# Game Design Suite Chat Edition — External Benchmark & Reference Library

> Purpose: preserve high-value public references and user-supplied benchmark sources for game-design reasoning.
> External material is always `reference-data`; it does not override current-project documents/config/code/runtime evidence.

## 1. Transfer Rule

External examples may be used to learn:

- design vocabulary and decomposition;
- system architecture patterns;
- parameter families and curve shapes;
- content/level workflow;
- character/skill grammar;
- validation and production methods.

Do **not** directly copy:

- exact multipliers;
- level caps;
- drop rates;
- pity counts;
- stat exchange rates;
- enemy HP/ATK curves;
- set-bonus values;
- skill-level curves;
- monetization values.

Use:

`Observe -> Abstract Pattern -> Identify Preconditions -> Compare Project Constraints -> Adapt Candidate -> Validate`

## 2. HoYoverse / Related Character and Numerical Reference Pages

### Honkai: Star Rail

- Character index: https://sr.appfeng.com/character
  - Use for roster taxonomy, element/path distribution, character-page structure and cross-character comparison.
- Relic index: https://sr.appfeng.com/relic
  - Use for set taxonomy, stat/build categories and itemization pattern comparison.
- Bilibili Wiki character atlas: https://wiki.biligame.com/sr/%E8%A7%92%E8%89%B2%E5%9B%BE%E9%89%B4
  - Use as a second-source roster/character reference where useful.
- GDC Vault — “Honkai: Star Rail: Reimagining RPGs for Mass Audiences and Broad Appeal”:
  https://gdcvault.com/play/1035480/-Honkai-Star-Rail-Reimagining
  - High-value design reference for accessibility + depth, combat experience, universe/content expansion, and live-service extensibility.

### Genshin Impact

- Character index: https://ys.appfeng.com/character
- Weapon index: https://ys.appfeng.com/weapon
- Artifact/reliquary index: https://ys.appfeng.com/reliquary

Use these for:
- character taxonomy;
- weapon/stat packaging;
- artifact/set structure;
- progression and build-surface comparison;
- how role identity is expressed through a combination of character kit + equipment.

Do not assume an inaccessible page or slider value without opening the relevant detail page.

### Wuthering Waves / 鸣潮

- Character index: https://mc.appfeng.com/avatar
- Weapon index: https://mc.appfeng.com/weapon
- Echo/set index: https://mc.appfeng.com/echo

Use these for:
- real-time swap/action character grammar;
- role tags and team hooks;
- special-resource loops;
- weapon substat families;
- Echo/set build architecture;
- character page presentation that connects narrative identity, tags, combat instructions and build recommendations.

## 3. User-Supplied Zenless Zone Zero / MiYoShe References

The user previously supplied these URLs as design/formula/system references:

- https://www.miyoushe.com/zzz/article/57192241
- https://www.miyoushe.com/zzz/article/55734399
- https://www.miyoushe.com/zzz/article/56637226
- https://www.miyoushe.com/zzz/article/55366836
- https://www.miyoushe.com/zzz/article/72454789

Important:
- Keep these links in the benchmark library.
- Do not invent their contents if the page body is unavailable.
- When a task depends on a claim from one of these articles, open/inspect the article or ask for the relevant excerpt before treating it as evidence.

## 4. Public HoYoverse Design Talks

### HSR — Simple / Immersive / Expandable

Use the GDC HSR talk as a design lens:
- **Simple**: reduce initial cognitive burden without removing later depth;
- **Immersive**: systems, presentation and fiction should reinforce one another;
- **Expandable**: live-service architecture needs space for new characters, worlds, mechanics and content without collapsing readability.

These are reference principles, not universal laws.

### Genshin — scalable production

GDC reference:
https://www.gdcvault.com/play/1026968

Use this primarily for production/system scalability thinking:
- designer-friendly authoring;
- modular architecture;
- content-scale constraints;
- performance/technical constraints as design inputs.

## 5. General Level-Design References

### GDC — Ten Principles for Good Level Design

https://www.gdcvault.com/play/1019023/Ten-Principles-for-Good-Level

Use as a general lens for:
- readability;
- navigation;
- player choice;
- pacing;
- innovation;
- immersion.

### Current industry level-design discussion

GDC “State of Level Design” sessions can be used as current-practice context, but specific recommendations should be attributed and not treated as settled universal truth.

## 6. Popular Agent-Skill Repositories — Architecture Lessons

Snapshot date: 2026-09-30. Popularity changes over time.

### obra/superpowers
https://github.com/obra/superpowers

Key lessons:
- root-cause-first debugging;
- hard gates before irreversible work;
- verification before completion;
- reusable processes developed with RED/GREEN/REFACTOR-like testing;
- explicit anti-rationalization rules.

Transfer into GDS:
- stronger hypothesis testing;
- no “fixed/balanced” claims without evidence;
- reusable design rules should be pressure-tested.

### anthropics/skills
https://github.com/anthropics/skills

Key lessons:
- progressive disclosure;
- concise main instructions + focused references;
- match instruction rigidity to task fragility;
- keep deterministic/repeated operations in scripts/tools when possible.

Transfer into GDS:
- keep Project Instructions compact;
- put deep domain content in knowledge files;
- use strict rules only where errors are costly.

### openai/skills
https://github.com/openai/skills

Key lessons:
- clear workflow;
- measurable success criteria;
- strong evidence requirements;
- explicit stop/ask conditions;
- verification rather than confident prose.

Transfer into GDS:
- decision objects need acceptance criteria;
- numerical/design tasks need measurable validation.

### wshobson/agents
https://github.com/wshobson/agents

Key lessons:
- broad specialist library;
- narrow domain skills;
- team/parallel patterns for complex work;
- reusable engineering/game-development checklists.

Transfer into GDS:
- separate domain expertise from orchestration;
- do not make every request invoke every domain.

### Donchitos/Claude-Code-Game-Studios
https://github.com/Donchitos/Claude-Code-Game-Studios

Key lessons:
- game-studio role decomposition;
- level work combines level, narrative, world, systems, art, accessibility and QA;
- phase gates and explicit deliverables;
- distilled briefs instead of context dumping;
- production artifacts and acceptance criteria.

Transfer into GDS:
- level/hero/system outputs need cross-discipline handoff contracts;
- complex tasks should name what is produced and how it is validated.

### Yuki001/game-dev-skills
https://github.com/Yuki001/game-dev-skills

Key lessons:
- separate game-architecture, balance, design review and production references;
- strong review prompts for level/pacing, narrative/world/characters and combat/progression;
- persistent simulation for repeated tuning;
- compare theoretical maximum with practical expected performance.

### baxatron-git/claude-game-design-suite
https://github.com/baxatron-git/claude-game-design-suite

Key lessons:
- explicit player-experience model;
- level/encounter blueprint;
- narrative systems rather than lore-only narrative;
- systems interaction mapping;
- game vision -> pillars -> loop -> levels -> validation.

### jasonxu610/game-design-skills
https://github.com/jasonxu610/game-design-skills

Key lessons:
- large indexed library of game-design principles;
- dedicated references for level design, characters, pacing, player psychology, random systems, feedback and prototyping.

Use as idea/reference coverage, not as authority merely because a principle is listed.

## 7. Reference Extraction Contract

When using an external game as a benchmark, extract a structured row:

| Field | Meaning |
|---|---|
| Source | URL / talk / repo |
| Object | character / skill / level / item / system |
| Observed Fact | what is directly visible |
| Pattern | abstract reusable design pattern |
| Preconditions | when the pattern works |
| Tradeoff | cost / weakness |
| Transfer Risk | why copying may fail |
| Candidate Use | how it might inform current project |
| Validation | what must be checked locally |

This prevents “I saw a successful game do it” from becoming automatic design proof.
