# Game Design Suite Chat Edition — Narrative & Worldbuilding

> Purpose: a first-class domain for worldbuilding, factions, character background, story architecture, quests, environmental storytelling, and narrative-system consistency.
> External stories and commercial games are references only. Current-project canon must come from current project evidence or explicit user confirmation.

## 1. Narrative Decision Object

Before writing lore, identify what is actually being decided:

- World rule;
- Faction / institution;
- Character background or relationship;
- Story hook / arc;
- Quest / mission narrative;
- Environmental storytelling;
- Narrative delivery system;
- Narrative-system consistency;
- Continuity / canon issue.

Do not answer a system-design problem with lore, and do not answer a narrative-causality problem with flavor text.

## 2. World Truth Hierarchy

Separate:

1. **Hard World Rules** — physics, technology, metaphysics, social rules that other content must obey;
2. **Historical Facts** — events that actually happened in canon;
3. **Public Beliefs** — what ordinary people think happened;
4. **Faction Narratives** — biased institutional interpretations;
5. **Character Beliefs** — personal knowledge, misunderstanding, prejudice, secrets;
6. **Rumor / Mystery** — intentionally unresolved material.

A contradiction is not automatically bad. An unexplained contradiction between two hard truths is.

For existing projects, lock each important claim to its source before treating it as canon.

## 3. Worldbuilding Workflow

Use:

`Theme / Experience -> World Rule -> Consequence -> Institution -> Daily Life -> Conflict -> Player Contact -> Gameplay Expression`

For every major world rule ask:

- What behavior does this rule make possible?
- Who benefits?
- Who pays the cost?
- What institution forms around it?
- What does an ordinary person do differently because of it?
- What conflict does it create?
- Where does the player experience the rule through action rather than exposition?

Worldbuilding that can be removed without changing player understanding, decisions, emotion, space, enemies, rewards, or relationships is low-impact lore.

## 4. Faction Architecture

For each faction define:

| Field | Requirement |
|---|---|
| Purpose | Why the faction exists |
| Value | What it believes is worth protecting |
| Fear | What it cannot allow |
| Method | How it gets power/resources/influence |
| Internal contradiction | Where ideology and reality diverge |
| External conflict | What other group it opposes and why |
| Player relationship | Ally / employer / rival / threat / ambiguous |
| Visual/material language | Readable identity |
| Mechanical expression | Enemies, rewards, rules, shops, territory, quests |
| Change pressure | What could split, reform or destroy it |

Avoid factions that differ only by color, costume, or exposition.

## 5. Character Background Contract

Character background must connect to gameplay and current story.

`World Rule -> Faction/Social Position -> Past Event -> Want -> Need -> Fear -> Contradiction -> Relationship -> Choice Pressure -> Gameplay/Visual Expression`

Check:

- Why this person exists in this world;
- what they want now;
- what they refuse to lose;
- what false belief or contradiction creates drama;
- what relationship changes their choices;
- what the player can learn by watching behavior;
- what part of the kit, animation, target preference, resource loop, or team hook expresses identity.

For playable heroes, coordinate with `02-hero-skill.md`; narrative does not override kit or numerical evidence.

## 6. Story Hook & Arc

A usable hook contains:

`Disruption -> Personal Stake -> Unanswered Question -> Immediate Action -> Escalation Promise`

An arc should track both:

- **External state** — situation, enemy, faction, objective, world consequence;
- **Internal state** — belief, relationship, fear, identity, commitment.

Do not confuse chronology with an arc. Events can happen in sequence without changing anything meaningful.

## 7. Narrative Delivery Architecture

Choose delivery based on player behavior, not author preference:

- Critical-path scene/dialogue;
- Optional dialogue;
- Environmental storytelling;
- Item/collectible text;
- Companion banter;
- Encounter composition;
- Mission-state changes;
- World-state changes;
- Systemic consequences;
- UI / codex;
- Audio / music / VFX;
- Player-authored emergent events.

For every delivery channel define:

`Information -> Why player needs it -> Delivery moment -> Required/optional -> Gameplay interruption cost -> Recall test`

Do not use a cutscene, codex, or exposition block when the information can be experienced more directly through play.

## 8. Quest / Mission Narrative State

Model quests as states, not prose:

`Discoverable -> Offered -> Accepted -> Active -> Branch/Complication -> Resolution -> Reward -> World Aftermath`

Each state needs:

- entry trigger;
- player-readable motivation;
- objective;
- gameplay verb;
- narrative information;
- branch condition;
- failure/cancel/re-entry rule;
- reward;
- persistent world or relationship change.

Check fake choice, soft-locks, invisible consequences, duplicate completion, and narrative state disagreeing with runtime objective state.

## 9. Player Agency

Classify each choice:

- **Outcome agency** — changes the result;
- **Route agency** — changes how the result is reached;
- **Expression agency** — changes style/identity but not outcome;
- **Information agency** — changes what the player learns;
- **Strategic agency** — changes future resources/options;
- **No agency** — presentation only.

Do not sell expression choice as outcome choice.

For important decisions record:

`Choice -> Information available -> Tradeoff -> Immediate feedback -> Delayed consequence -> Reversibility`

## 10. Environmental Storytelling

Use:

`Past Cause -> Physical Trace -> Player Observation -> Inference -> Optional Confirmation -> Gameplay Consequence`

Useful evidence:

- architecture and route;
- damage/wear;
- props and resource distribution;
- enemy/NPC placement;
- sound and lighting;
- restricted/open spaces;
- changed objective or interaction;
- aftermath after the player's action.

A decorative prop is not environmental storytelling unless it communicates something.

## 11. Character-to-System Consistency

Check the chain:

`Character Claim -> Repeated Player Action -> System Reward -> Team/World Reaction -> Growth`

Examples of failure:

- story says self-sacrificing, gameplay rewards abandoning allies;
- faction condemns a resource, progression requires farming it with no narrative acknowledgement;
- character is framed as precise, kit is random with no compensating reason;
- story calls an event dangerous, level/economy treats it as trivial repeat farming.

Not every tension is a bug; intentional dissonance must have payoff.

## 12. Narrative × Level

For each major area/mission define:

- narrative purpose;
- information before entry;
- environmental question;
- encounter/story relationship;
- discovery beats;
- emotional peak;
- post-event spatial/world change;
- what the player causes rather than watches.

Level pacing and story pacing should be reviewed together when narrative is material.

## 13. Narrative × Economy / Progression

Narrative rewards can include:

- new information;
- relationship change;
- access;
- faction standing;
- location/world change;
- new dialogue/state;
- mechanical unlock.

Do not bribe players through unrelated currency to compensate for weak narrative content.

Progression nodes should not contradict character/faction identity without deliberate narrative explanation.

## 14. Continuity / Canon Audit

For existing content, verify:

`Claim -> Source -> Canon Level -> Time -> Character Knowledge -> Conflicts -> Resolution`

Check:

- timeline;
- geography;
- faction membership;
- identity/names/titles;
- technology/power rules;
- who knows what, and when;
- character motivation continuity;
- dead/alive/available state;
- quest outcome persistence;
- localization terminology.

A contradiction report should distinguish:
- true canon conflict;
- unreliable narrator;
- changed state;
- translation/terminology issue;
- missing evidence.

## 15. Narrative Failure Modes

- Lore Encyclopedia;
- Exposition Before Motivation;
- Cutscene Hostage;
- Narrative Island;
- Fake Agency;
- Consequence Without Feedback;
- Character Biography Without Playable Causality;
- Faction Palette Swap;
- Mystery With No Truth Model;
- World Rule Without Consequence;
- Emotional Beat With No Recovery/landing;
- Story Requirement That Breaks Core Gameplay.

## 16. Validation

Narrative quality is not verified by author confidence.

Use:

- cold-read comprehension;
- blind playtest;
- recall test after play;
- choice/consequence recognition;
- environmental inference test;
- objective motivation test;
- continuity audit;
- dialogue/quest state runtime verification;
- telemetry only where behavior can answer the question.

Example hypotheses:

- first-time players can explain why they are entering the area before the first fight;
- players identify the faction conflict without opening the codex;
- players notice that a choice changed a later state;
- character behavior is predicted consistently from established motives.

## 17. Acceptance Matrix

| Layer | Acceptance question |
|---|---|
| World | Do rules create consequences and conflict? |
| Faction | Do values produce distinct behavior and mechanics? |
| Character | Do want/need/fear/contradiction drive choices? |
| Hook | Is there an immediate stake and actionable question? |
| Delivery | Is information delivered at the right cost and moment? |
| Agency | Can the player tell what kind of choice they are making? |
| Level | Do space and encounters express the story? |
| Systems | Do rewards/progression/combat support the fiction? |
| Continuity | Can claims coexist in one timeline/canon model? |
| Validation | What evidence shows players understood and felt the intended result? |
