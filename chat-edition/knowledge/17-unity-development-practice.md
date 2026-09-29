# Game Design Suite Chat Edition — Unity Development Practice

> Purpose: strengthen Unity/C# implementation reasoning in ordinary Chat mode.
> This is a project-method reference derived from common patterns in Unity's official agent skills and widely used game-development agent repositories. It does not replace the user's actual Unity project evidence.

## 1. Existing Project First

Before proposing Unity code for an existing project:
- identify Unity version when available;
- identify relevant package/framework;
- inspect the nearest existing implementation;
- preserve project naming, architecture and UI framework;
- do not migrate frameworks or architecture unless explicitly requested.

Project evidence outranks generic Unity best practice.

## 2. Route by Actual Technology

For UI, detect what the project already uses:
- uGUI: Canvas, RectTransform, MonoBehaviour UI scripts;
- UI Toolkit: UXML, USS, UIDocument, CreateGUI;
- IMGUI: OnGUI / OnInspectorGUI, mostly editor tooling.

For an existing screen, match its current framework. Do not rewrite uGUI into UI Toolkit merely because it is newer.

For data/config, identify whether the project uses:
- ScriptableObject;
- generated data tables;
- JSON/bytes;
- server-authoritative data;
- custom loaders/generators.

## 3. Understand Before Editing

For bugs and modifications:
1. locate the exact file/class/method;
2. identify call site and state/input;
3. find nearest working analogue;
4. trace the runtime chain;
5. state one testable root-cause hypothesis;
6. change the smallest necessary code.

Do not rewrite an entire subsystem for a local bug unless evidence shows the subsystem is the root cause.

## 4. Editor vs Runtime Distinction

Always distinguish:
- Editor-only behavior;
- Play Mode behavior;
- Player/runtime behavior;
- client vs server authority;
- generated assets/data vs source files.

An Editor result does not automatically prove Player behavior.
A UI display result does not automatically prove server settlement.
A code path existing does not prove the condition executes.

## 5. Serialized Asset Safety

Scenes, prefabs, ScriptableObjects and serialized assets can carry GUID/reference/state dependencies.

When the user only asks for C# changes:
- do not invent prefab hierarchy;
- do not assume missing node names;
- do not rewrite serialized YAML from memory;
- state the exact node/component assumptions that code depends on.

If screenshots or hierarchy are provided, bind conclusions to the visible object names.

## 6. Small Reviewable Patches

Prefer:
- one bug / one patch;
- local method replacement;
- minimal added fields/events;
- no unrelated cleanup;
- no global formatting;
- no architecture migration.

For repeated changes across files, group only when the same verified pattern applies.

Compile/test between meaningful groups when runtime access exists.

## 7. Code Output Integrity

Existing one-line code stays one physical line unless syntax or the user requires otherwise.

Do not reflow:
- method calls;
- assignments;
- conditions;
- log calls;
- interpolated strings;
- LINQ chains;
- GM commands;
- resource paths;
- Buff/Target config strings.

For a single change, output:
1. file/class/method;
2. original code/block;
3. replacement code/block;
4. why;
5. acceptance check.

## 8. Async / Build / Test State

Starting an operation is not completion.

For build, compile, test, import or asynchronous editor work:
- distinguish trigger from terminal state;
- verify final result;
- read actual error output;
- do not claim success from “started” or “no immediate error”.

When tools are unavailable, state the exact verification the user should perform.

## 9. UI Change Verification

For UI modifications check:
- object exists;
- state transition is correct;
- initial state is correct;
- refresh occurs after data changes;
- locked/received/failure states are mutually consistent;
- click handler points to the correct target;
- text/color/value formatting matches the requirement;
- opening/closing the dialog does not leave stale state.

When a Group/View Switch or similar state controller exists, treat it as the source of state truth rather than manually toggling child objects from unrelated code.

## 10. Performance Claims Need Measurement

Do not call a change “optimized” without evidence.

Relevant evidence may include:
- Unity Profiler;
- Memory Profiler;
- Frame Debugger;
- allocation counts;
- CPU/GPU frame time;
- target-device measurement.

Prefer fixing measured bottlenecks over speculative micro-optimization.

## 11. Version-sensitive APIs

Unity/package APIs change by version.

If a solution depends on version-sensitive behavior:
- identify the Unity/package version;
- use official documentation when external lookup is needed;
- avoid suggesting an API solely from memory when the project version can change correctness.

## 12. Completion Gate

Before saying “fixed”:
- compile succeeds, if compilation can be run;
- original reproduction is re-tested;
- nearest regression path is checked;
- runtime/state result matches the requested behavior.

If these cannot be run here, use:
- code change = provided;
- compile/runtime verification = pending.

Never collapse “code looks correct” into `verified-runtime`.
