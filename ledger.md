# ledger.md — updated 2026-07-15, end of Session 14 (spilled across Jul 14–15)
# This file is the complete Skycak artifact: STATE (Part A) + GRAPH (Part B).
# The graph copy in days10-12_skycak_protocol.md is superseded; this one is living.
# Node IDs (N1…) are file-internal shorthand only — full names in conversation.

═══════════════════════════════════════════════
# PART A — STATE
═══════════════════════════════════════════════

## Fluent (legacy — spot-check occasionally, don't drill)
N1 variables & assignment · N2 strings & f-strings · N3 string methods ·
N6 lists & indexing · N7 for loops · N8 .items()/enumerate unpacking ·
N12 if/elif/else · N13 branch ordering · N15 while loops ·
N9–N11 dict read/write/KeyError asymmetry · N19 functions ·
N22 try/except mechanics · N5 Git add/commit/push

## Fluent (recent promotions)
| Node | Evidence | Next review |
|---|---|---|
| N35 count accumulator | S13 item 1, cold, under 3:00 (Jul 13) | **~Jul 16** (interval 3d) |
| N37 split-then-index-convert | S13 item 3, cold, 1:25 vs 2:00 (Jul 13) | **~Jul 16** (interval 3d) |
| N36 record-keeper / max tracker | S14 retry (Jul 14): 2:59 vs 3:00, cold, fresh data. Mid-timer self-repair of silent bug — dropped `record = b`, gate inert, last-one-wins (`E` printed); diagnosed from output, fixed, passed | ~Jul 21 (3→7d) |

## produced-once
| Node | Evidence | Next timed attempt |
|---|---|---|
| N34 gate pattern | A2, D1, S13 item 4, both S14 compositions | rides composite builds |
| gated count (N34+N35 fusion) | A2 clean (Jul 12); exercised in S13 item 4, S14 compositions | next timed round |
| N40 composition: file-read → parse → report | D1 (Jul 12); S13 attempt voided (unsaved buffer). **S14 attempt 1 (Jul 14): MISS** — `day3:` colon in output; write-from-Python step skipped (file hand-pasted). **S14 attempt 2 (Jul 15): MISS** — cold stall at `.write()`, chair abandoned mid-timer, assist given; output then correct (`2`, `125`, `day3` — colon fix built into first draft) but over time (~9 eff. min + 3:23) and assisted | **S15 attempt 3: fully cold, ≤15:00, timer to zero. Write-from-Python is half the spec.** |

## produced with assist (below produced-once)
| Node | Evidence | Needs |
|---|---|---|
| N30w file *writing* (`"w"`, `\n`, write-then-read) | Jul 15: file genuinely created from Python inside attempt 2, but only after hint. Cold tries: `f.write() = "..."` (SyntaxError: cannot assign to function call), `f.write() == "..."` (TypeError: exactly one argument, 0 given). Model gap: treated `.write()` as shelf, not machine-fed-through-parens (siblings: print, .append) | one cold rep — folded into S15 attempt 3 |

## taught / due for evidence
- **N23–N27 exception ladders + .get() design — STARVED, ~11 days unreviewed.** Highest-value warm-up = N41-shaped build. Deferred Jul 15 by design (no cold review on a tired evening).
- N30 with-frame production — written cold in S13 item 4 + both S14 compositions → effectively produced-once; one isolated cold rep confirms, then promote.
- N29 datetime pipeline — no production evidence.
- editor buffer vs disk (taught Jul 13) — Ctrl+S-before-run held Jul 14–15, zero buffer incidents.

## Linux nodes (block opened Jul 14) — all TAUGHT, guided-run evidence only
| Node | Evidence |
|---|---|
| N42 shell/terminal/OS model + REPL | defined from zero Jul 14 (shell = read-run-print program; terminal = glass; cat/ls are launched programs, cd is the shell moving itself) |
| N43 cwd (shell-side) | Jul 14–15; bridged from N30's "files land where the terminal stands" |
| N44 navigation trio (pwd/ls/cd/cd ..) | guided run clean Jul 15; silence-is-success noticed; prompt-as-live-cwd noticed; used cd ..+pwd unprompted to reposition |
| N45 home directory & ~ | Jul 15; prediction missed (/c/downloads vs /c/Users/주현준) → taught off the miss |
| N46 paths (absolute vs relative, .. in paths, relative-glues-to-cwd) | Jul 15; re-taught from zero after "I don't get it" (bedroom/kitchen notebook model landed); self-test passed with correct reasoning |
| N47 cat + reading shell errors | worked run Jul 15: **3/3 exact predictions** incl. verbatim file contents from memory and pre-written No-such-file failure |
| N48 prompt anatomy (user@machine loc, $ vs #) | Jul 15, on his questions; cut short by his choice |
| N49 file search (find/grep) | **not yet taught** — Bandit gate node |
| N50 permissions | **not yet taught** — Bandit gate node |

## Gates
- **Linux acquisition: OPENED Jul 14.** Note: previous ledger said "opens when record-keeper AND composition both fluent." Opened with composition at produced-once, on the ruling that gates block *Bandit* (cold production in unfamiliar terminal), not acquisition-mode worked examples. As-written gate overridden; recorded, not hidden. Acquisition-mode-only remains binding.
- **Bandit: CLOSED.** Requires N44, N49, N50 at produced-once (cold, typed, unassisted). N44 is guided-only; N49/N50 untaught.

## Conduct rules
- **The attempt runs until the timer ends** (added Jul 15, after mid-timer chair abandonment at the .write stall). A stall surrounded by attempts is evidence; an abandoned chair is not.
- Mid-rep question = attempt void (S13 rule, standing).

## Repo hygiene
- June folders renamed Jul 15: `29th,June.py/`, `30th,June.py/` → `29th,June/`, `30th,June/` (folders wearing file names; names-can-lie demonstrated live). Committed.
- **streak_log.txt is STALE**: last entry 2026-07-10 / streak 14; real streak ~18–19. Known wrong-data in repo. Hack candidate filed (not assigned): append-today script = `"a"` mode + N29 + N30w in one build.
- Convention slip Jul 14: made-up data unmarked in item1.py. Flagged once.

## Session 14 record (Jul 14–15)
- N36 → fluent at 2:59 with mid-timer output-diagnosed self-repair.
- N40 missed twice; attempt 3 speced. N30w zero → assisted.
- Linux first contact complete: full vocabulary stack from zero (calibration note: EVERY term needed definition — never frame new domains as "mostly owned" off mechanics alone), two guided runs, 3/3 cat predictions.
- Corrective trigger: `lines.split(" ")` on the list — twice at same joint (Jul 14, 15).
- Affect signal: three unprompted "this is so cool" statements at the bare terminal — strongest positive affect on record; Linux material currently carries intrinsic motivation.

## Next session (S15)
1. **N31 corrective micro-block**: split-on-a-list, 3–5 reps, 2 min (split acts on a string; a list is split's *output*, never its input).
2. **N40 attempt 3**: write-then-read, ≤15:00, fully cold, timer to zero. Spec: write 4-line log from Python, read back, print python-count / total / max-day clean.
3. **Due Jul 16**: N35 + N37 reviews — fold into one repetition-compression build if possible.
4. If passed + appetite: N41-shaped warm-up for the starved N23–N27 cluster.

═══════════════════════════════════════════════
# PART B — THE KNOWLEDGE GRAPH (structure)
═══════════════════════════════════════════════
`←` = has prerequisite. `⊇` = encompasses (producing this implicitly reviews that), weight {1.0 full … 0.3 partial}. Warm-up selection = the one small build whose ⊇ edges cover the most due nodes.

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
- N30 file I/O ← N28, N2 — **now split for tracking:** N30r read + with-frame (≈produced-once) / N30w write modes `"w"`/`"a"`, `\n` (assisted)

**Tier 3 — processing & composite patterns**
- N31 .split() (incl. empty-piece edges, multi-char separators) ← N2, N6 — **corrective flag: split-on-a-list joint, 2 hits**
- N32 .append() ← N6
- N33 empty-tail / empty-string handling ← N31, N14
- N34 gate pattern (if inside loop) ← N7, N12
- N35 count accumulator ← N7, N1
- N36 record-keeper / max tracker (incl. string-record variant; failure species: dropped record-update → last-one-wins) ← N7, N12, N1
- N37 split-then-index-then-convert ← N31, N6, N4
- N38 if-guarded overwrite ← N12, N10, N36
- N39 seed-then-feed ← N35, N36, N7
- N40 integrative composition: file-read → parse → gate → accumulate → report ← N30, N31, N33, N34, N35, N36, N37 — **now explicitly includes N30w (write-then-read shape) per S14–15 retry spec**
- N41 integrative build: dict-loop + accumulator + if/elif + error handling ← N10, N35, N36, N25, N34

**Tier L — Linux/shell (opened Jul 14; grows toward Bandit)**
- N42 shell/terminal/OS model + REPL (independent spine; conceptual bridge from N28's "REPL" and N21's command-anatomy)
- N43 cwd, shell-side ← N42 (bridges N30's cwd lesson)
- N44 navigation trio: pwd / ls / cd / cd .. ← N42, N43
- N45 home directory & ~ ← N44
- N46 paths: absolute vs relative, .. inside paths ← N43
- N47 cat + shell-error anatomy ← N44, N46
- N48 prompt anatomy: user@machine location, $ vs # ← N42
- N49 file search (find/grep) ← N44, N46 — not yet taught; **Bandit gate**
- N50 permissions ← N44 — not yet taught; **Bandit gate**

**Encompassing edges (review-compression map):**
- N40 ⊇ N30{0.8→now incl. N30w when write-then-read shape used}, N31{1.0}, N33{1.0}, N34{1.0}, N35{1.0}, N36{0.8}, N37{1.0}, N4{0.7}, N7{1.0}, N12{0.8} — **still the best single review task in the graph, and it's already scheduled (S15 attempt 3)**
- N41 ⊇ N9{1.0}, N10{1.0}, N7{1.0}, N35{0.8}, N36{0.7}, N12/N13{0.7}, N25{0.5}, N34{0.6} — best task for the error-handling cluster, which N40 barely touches
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
- N47 ⊇ N44{0.6}, N46{0.8}, N43{0.7} — best current Linux review task (a cat run exercises paths, cwd, and navigation together)
- N44 ⊇ N43{1.0}, N42{0.5}
- N46 ⊇ N43{0.8}

**Graph-reading notes (as of Jul 15):**
- **N40 is doing double duty**: it's both the scheduled retry (S15, ≤15 min, cold) *and* still the widest ⊇ coverage in the graph — passing attempt 3 simultaneously reviews N31/N33/N34/N35/N36/N37 and gives N30w its first cold evidence. Highest-stakes single task currently schedulable.
- **N23–N27 remains the starved cluster** (~11 days), untouched by N40. An N41-shaped build is the correct next warm-up once N40 clears.
- **N29 still has zero production evidence.** The streak-log-appender hack (filed) covers N29 + N30w's `"a"` mode + real-data repair in one build — best value-per-minute task on file once N30w has cold evidence.
- **N31 carries a corrective flag** (split-on-a-list, 2 hits) — micro-block opens S15 *before* N40 attempt 3, since N40 contains the joint.
- **Tier L is all taught/guided.** Nothing in it has production evidence; N47 is the natural first cold-production candidate (a typed, unassisted navigate-and-cat sequence). N49/N50 must be taught before the Bandit gate can even be attempted.
- Due Jul 16: N35, N37 (first 3-day interval check on the S13 promotions).