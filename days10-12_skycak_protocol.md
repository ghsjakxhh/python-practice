# Days 10–12 + The Skycak Protocol (July 6–12, 2026)

This file has two jobs: (1) compress Sessions 10–12 into the knowledge record, (2) permanently install Justin Skycak's mastery-learning method as the operating system for all future sessions. **Primary reader: Claude.** 현준 rarely reads these files. Written as standing protocol, not as history.

---

## PART 1 — THE OPERATING PROTOCOL (standing rules, all future sessions)

Adopted July 11, 2026, replacing the ad-hoc review system. Source: Justin Skycak's Math Academy methodology (knowledge graph + mastery gating + spaced retrieval + FIRe-style encompassing review). 현준 reads Skycak's X posts regularly — **apply the method, don't explain it.**

### 1.1 The ledger

- Every skill is a node with one of three states:
  - **taught** — explained, traced, understood on contact. Prediction evidence only.
  - **produced-once** — built cold (blank file, no reference) at least once, correct.
  - **fluent** — built cold, unassisted, correct, **inside a time target**.
- **Only cold production promotes a node.** Predicting/tracing never promotes — that was never the weak side. "We covered it" counts for nothing.
- Living copy: `ledger.md` in `C:\Python`, committed with each session. **Update workflow: Claude prints the complete updated ledger at session end; 현준 pastes it wholesale over the old file and commits.** Never ask him to hand-edit rows.

### 1.2 Review scheduling

- Each node has a review clock. Pass cold + fast → interval expands: **1 → 3 → 7 → 14 → 30 days.** Slow or failed → interval contracts and state drops one level.
- **Session warm-ups are repetition-compression builds:** one small cold build chosen to touch the most due nodes at once — never isolated flash questions. The five-prediction review round is retired as a daily fixture.
- The **bug-species prediction round survives as a weekly event**: timed "name the error / predict the failure" across the full catalogue.
- Reviews should hide inside real work where possible (a "new" build that happens to exercise due nodes counts as their review).

### 1.3 Two session modes — never blurred

- **Review mode:** cold, timed, unassisted, mixed/unlabeled where possible. Struggle lives here. No help until an attempt is dead (ten-minute rule; "bring me the attempt, not a blank"). Unlabeled prompts test pattern *selection*, which is the real skill.
- **Acquisition mode:** new material. Max 1–2 genuinely new ideas per session. Worked examples first, tight steps, minimal struggle. Map every new thing onto something owned.
- The July 8 failure mode (acquisition scaffolding bleeding into what should have been his own assembly) is what this split prevents.

### 1.4 Spec granularity is a function of node state

- **taught** node → full annotated worked example **on different data**, then study-close-produce cycle: study 2 min out loud (why each line exists), close everything, blank file, own data, write from nothing, compare, log what dropped. Source open and producing never overlap — "glancing mid-production is tracing wearing a rep's costume."
- **produced-once** node → one-line spec, no structure hints. State the *expected output explicitly* (e.g., "the count = one number, printed once" — a vague spec cost a rep on July 12).
- **fluent** node → timed, fresh data shape, no study pass.
- Vary the fuel, keep the pattern: reps on identical data memorize text, not moves.

### 1.5 Gates

- **The graph decides, not the calendar.** New blocks open only when their prerequisite nodes carry production evidence.
- **Cyber block gate (Bandit):** shell navigation, file search, permissions — all at produced-once or better. Until then, Linux material is acquisition-mode only and Bandit does not start. Rationale: Bandit on non-fluent components reproduces the July 8 collapse in an unfamiliar terminal.
- Immediate next gate: **S13 timed round** — count accumulator ≤3 min, record-keeper ≤3 min, split-then-index-convert ≤2 min, composition (make11-shaped, pointed at a NEW file spec Claude provides) ≤15 min. No study passes. Pass → fluent. Miss → node reschedules, no drama.

### 1.6 Failure handling

- A failed or slow rep is *data*, never a setback: log it, contract the interval, move on. The ledger records truth.
- Build stalls twice at the same joint → corrective remediation: isolate the specific upstream node, 3–5 blocked reps, re-attempt. Never lower the bar; never do the assembly for him.
- Silent bugs are the species that survives staged development — the audit tool is tracing one's own finished file with Predict-level suspicion. He caught his first one solo on July 12 (B3); reinforce that habit.

---

## PART 2 — LEDGER SNAPSHOT (2026-07-12, end of Session 12) — seed for `ledger.md`

### Fluent (legacy — 11 sessions of evidence; spot-check occasionally, don't drill)
variables & assignment · strings & f-strings · lists & indexing · for loops & .items() unpacking · if/elif/else & branch ordering · while loops · dict read/write/KeyError asymmetry · functions (def/return/parameters) · try/except mechanics & ladders (production evidence from make9/hack1-2, but see "due" below)

### produced-once (promoted July 12; next review due ~July 15)
| Node | Evidence |
|---|---|
| count accumulator | A1 (Jul 10, dropped `.items()`, self-repaired), B2-adjacent, D1 |
| gated count (gate + counter fused) | A2 clean (Jul 12) |
| record-keeper / max tracker | B1 warm (Jul 10), B2 cold-clean, B3 clean **on 3 data shapes incl. string record** — strongest node evidence in ledger |
| split-then-index-convert | C1 clean, C2 (2 self-repaired errors), C3 clean-fast, D1 |
| gate pattern (if inside loop) | A2, D1 |
| file-read → parse → report composition | **D1: rebuilt make11 from blank, first attempt, after one 3-min study pass — improved the original** (moved count above extraction) |

### taught / due for evidence
- exception ladders + .get() design (make9 era, ~1 week unreviewed) — due for a compression build
- with-frame *production* (understands "closes but doesn't catch" — Q4; never written cold)
- datetime pipeline production (date → timedelta → .days) — traced and probed only
- file *writing* cold (make10 was assisted-era)

### Timed round pending (S13). Targets in §1.5.

---

## PART 2.5 — THE KNOWLEDGE GRAPH (structure; the ledger tracks state, this tracks dependencies)

Node IDs (N1…) are **file-internal shorthand only — never speak them to 현준; use full names in conversation** (same rule that retired numbered bug species). `←` = has prerequisite. `⊇` = encompasses: producing this node implicitly reviews that one, with weight {1.0 full … 0.3 partial}. **Warm-up selection = pick the one small build whose ⊇ edges cover the most due nodes** (repetition compression). New nodes get added here as blocks open (Linux/Bandit nodes arrive with S14+).

**Tier 0 — substrate**
- N1 variables & assignment
- N2 strings & f-strings ← N1
- N3 string methods (.upper, len) ← N2
- N4 int()/float() conversion ← N1
- N5 Git add/commit/push (independent spine)

**Tier 1 — containers & iteration**
- N6 lists & 0-based indexing ← N1
- N7 for loops ← N6
- N8 enumerate / two-variable unpacking ← N7, N6
- N9 dict key access ← N1, N2
- N10 dict read-modify-write ← N9
- N11 dict create-vs-read asymmetry / KeyError ← N9

**Tier 1 — control flow**
- N12 if/elif/else ← N1
- N13 branch ordering (specific before broad) ← N12
- N14 boundary conditions & off-by-one ← N12
- N15 while loops ← N12
- N16 count-up loops ← N15, N7
- N17 while + if/elif combined ← N15, N12
- N18 loop variable outlives the loop ← N7, N15

**Tier 2 — functions**
- N19 def / parameters / return ← N1
- N20 round() ← N19, N4
- N21 substitution model / function architecture ← N19

**Tier 2 — errors & robustness**
- N22 try/except mechanics (the jump) ← N12
- N23 specific nets; bare-except danger ← N22
- N24 except-as naming ← N23
- N25 exception ladders (specific before broad) ← N23, N13
- N26 .get() with fallback / None ← N9, N11
- N27 error taxonomy (NameError, SyntaxError-as-parse-time, ValueError vs TypeError, AttributeError, FileNotFoundError) ← N22, N4

**Tier 3 — library & I/O**
- N28 import ← N1
- N29 datetime pipeline (date → timedelta → .days; attr vs method) ← N28
- N30 file I/O (modes w/a/r, with-blocks, \n, cwd) ← N28, N2

**Tier 3 — processing & composite patterns**
- N31 .split() (incl. empty-piece edges, multi-char separators) ← N2, N6
- N32 .append() ← N6
- N33 empty-tail / empty-string handling ← N31, N14
- N34 gate pattern (if inside loop) ← N7, N12
- N35 count accumulator ← N7, N1
- N36 record-keeper / max tracker (incl. string-record variant) ← N7, N12, N1
- N37 split-then-index-then-convert ← N31, N6, N4
- N38 if-guarded overwrite ← N12, N10, N36
- N39 seed-then-feed (composed accumulator discipline) ← N35, N36, N7
- N40 integrative composition: file-read → parse → gate → accumulate → report ← N30, N31, N33, N34, N35, N36, N37
- N41 integrative build: dict-loop + accumulator + if/elif + error handling (hack1/2 shape) ← N10, N35, N36, N25, N34

**Encompassing edges (review-compression map):**
- N40 ⊇ N30{0.8}, N31{1.0}, N33{1.0}, N34{1.0}, N35{1.0}, N36{0.8}, N37{1.0}, N4{0.7}, N7{1.0}, N12{0.8} — **best single review task currently in the graph** (D1 proved it: one build, seven nodes evidenced)
- N41 ⊇ N9{1.0}, N10{1.0}, N7{1.0}, N35{0.8}, N36{0.7}, N12/N13{0.7}, N25{0.5}, N34{0.6} — best task for reviewing the **error-handling cluster**, which N40 barely touches
- N39 ⊇ N35{1.0}, N36{0.6}, N7{1.0}, N1{0.7}
- N38 ⊇ N12{1.0}, N36{0.8}, N10{0.6}
- N37 ⊇ N31{1.0}, N6{1.0}, N4{0.4}
- N36 ⊇ N7{1.0}, N12{0.8}, N1{0.6}
- N35 ⊇ N7{1.0}, N1{0.7}
- N33 ⊇ N31{0.8}, N14{0.5}
- N30 ⊇ N28{0.5}, N2{0.4}
- N29 ⊇ N28{0.5}, N4{0.3}
- N25 ⊇ N23{1.0}, N13{0.8}
- N17 ⊇ N15{1.0}, N12{1.0}; N16 ⊇ N15{1.0}, N7{0.7}; N8 ⊇ N7{1.0}, N6{0.8}

**Graph-reading notes (as of Jul 12):** N35–N40 all carry produced-once evidence, so their downstream ⊇ credit is now live — Tier 0–2 review mostly rides free on composite builds. The starved cluster is **N22–N27**: nothing recent encompasses it except N41-shaped builds, so an N41 task is the highest-value warm-up currently schedulable. N29 and file-*writing* within N30 have no production evidence at all — a small "compute from real dates and append to a log" build would cover both in one task.

---

## PART 3 — KNOWLEDGE ADDED, SESSIONS 10–12 (compressed)

### Session 10 — import, datetime, files
- `import` is a **name-creating line** (delete it → NameError, same family as deleting an assignment). Libraries bring **new types**: `date`, `timedelta`. The type system is open, not a finished list.
- **Pipeline pattern:** exotic types at the top deliver plain values into owned code. `today - start` → timedelta → `.days` → plain int → everything old works on it. Substitution rule applies unchanged.
- **Attribute vs method:** `.days` is a shelf (no parens — stored value); `.get()` is a machine (parens = trigger). `(today - start).days()` → **TypeError: 'int' object is not callable** — by the time parens arrive, `.days` already became 14; Python was literally asked to run `14()`.
- `today - start.days` → **AttributeError** (dot binds before minus; `date` has no `.days` shelf — that shelf lives on timedelta). AttributeError = KeyError's cousin: missing shelf vs missing key.
- **File modes:** `"w"` = *erase at open, then write* (silent data destruction — he wiped his own log proving it); `"a"` = append; `"r"` = read. Write/append to a missing file **creates** it; read of a missing file **crashes** (FileNotFoundError) — the dict asymmetry at file scale.
- `with open(...) as f:` — territory whose exit **always** closes the file, crash or not. **with is cleanup, try/except is survival — orthogonal.** with does NOT catch anything (his Q4 miss, then owned).
- Why closing matters: buffered writes may not hit disk until close (data that silently never existed); open files are held resources (Windows locks).
- `\n` is **one stored character** (len proves it), rendered as a break by print. Value vs representation, again.
- Files land where the **terminal** stands (cwd), not where the script lives.
- `date.today()` reads the real clock — computed values immune to schedule slips; hardcoded ones become wrong-data lies as time passes (demonstrated on him within 24h).

### Session 11 — the file becomes data
- `.split(sep)`: string → list of pieces; cuts consume separators; **trailing separator leaves `''` at the end** (n cuts → n+1 pieces). Leading separator → leading `''` (C2). Separators can be multi-character (`": "`).
- `''` = a value containing nothing. Not None, not 0. The nothing-family: `0`, `""`, `None` — all distinct.
- **Gate pattern:** `if line != "":` inside the loop protects the lap. Quiet handling correct for failures that are normal-every-run (loud/quiet doctrine extended).
- `.append()` — finally live; brackets access, `.append()` grows.
- `int("15")` converts; `int("day10")` → **ValueError**. **ValueError vs TypeError test: could another value of the same type have worked?** Yes → ValueError; no value of that type ever could → TypeError.
- Record-keeper: seed must **lose the first comparison**; seed safety is a fact about the data (0 works because streaks > 0), not magic. B3 variant: compare `len(title) > len(record)`, store the *string*; seed `""` (len 0 loses to any real title).
- Naming: `line`/`lines` one-letter trap bit him; **shadowing built-ins** (`list = ...`) runs but plants a wrong-thing-with-familiar-name mine; names should say what the thing is *at that line*.
- Staged development (one transformation per line, printable) is correct at this level — compress later, never regret staging.
- New catalogue entries this block: **AttributeError, TypeError, ValueError, FileNotFoundError, wrong-mode silent data destruction, built-in shadowing.** (Numbered species labels retired July 6 — full error names only, permanent.)

### Session 12 — the reps (July 10 morning + July 12)
- Pattern drill day, study-close-produce. All errors self-repaired via traceback: `.items()` drop → ValueError "too many values to unpack" (looping bare dict yields keys only; unpacking tried to split a 6-char string into 2 slots); split-on-a-list → AttributeError; leading-`''` from space cut → indexed around it.
- July 12 all-cold block: B2, A2, B3, C3, D1 — five for five, zero assists, one silent bug self-caught (B3 draft printed 25 — the length wearing the answer's costume; he diagnosed from output alone).

---

## PART 4 — WORKING WITH 현준 (accumulated, binding)

- **Direct feedback, no empty validation.** Praise only what the evidence supports, and name exactly what it supports.
- **Full error names, never numbered species.** (His explicit request.)
- **Look, don't infer / look, don't recall — applies to Claude too**, including dates: on July 12 Claude mis-stated July-10 reps as "yesterday" and was corrected. Verify timeline claims against what he actually said.
- **Resistance pattern (named to him, accepted):** doubt shows up *before* reps and vanishes *during*. The day's first rep is the whole battle. Contract-shrinking works ("just B2, three lines, then decide"). Don't over-diagnose "rut" — but don't argue away real zeros either; count them honestly.
- Zero days happen (July 9, 11). Streak = showing up; sessions may spill across days; the convention is one session *per* day max, extra appetite → hacks.
- Specs for produced-once reps: one line, but **state the expected output shape explicitly.**
- Comment flag-and-veto convention continues (one line, no sermon, his veto).
- Real personal data in builds; invented data marked `# made-up data`.
- When he says "I don't know how to do X," the gap is almost always **two owned pieces that haven't fused** — name the pieces, show the parallel, let him fuse them. Full assembly instructions are the last resort and cost a rebuild.
- Commit messages capture ideas; drills commit too (squares don't care).

## Where things stand
Streak day ~17 of the program. Session 13 = the timed round (§1.5 targets), then Linux acquisition begins if gates pass. The plan beyond that lives in the ledger, not in this file — the graph decides, not the calendar.
