
# ledger.md — updated 2026-07-20, end of Session 19
# This file is the complete Skycak artifact: STATE (Part A) + GRAPH (Part B) + HARDWARE (Part C).
# Supersedes the 2026-07-19 print. Node IDs (N1…) are file-internal shorthand only — full names in conversation.

═══════════════════════════════════════════════
# PART A — STATE
═══════════════════════════════════════════════

## Fluent (legacy — spot-check occasionally, don't drill)
N1 variables & assignment · N2 strings & f-strings · N3 string methods ·
N6 lists & indexing · N7 for loops · N8 .items()/enumerate unpacking ·
N12 if/elif/else · N13 branch ordering · N15 while loops ·
N9–N11 dict read/write/KeyError asymmetry · N19 functions ·
N22 try/except mechanics · N30 with-frame (folded in per Jul 19 note) ·
N5 Git add/commit/push (incl. vim exits; -m habit confirmed in the wild Jul 19)

## Fluent (recent promotions)
| Node | Evidence | Next review |
|---|---|---|
| **N40 composition (write→read→parse→report)** | Jul 16 pass 13:28 → Jul 19 defended 9:47/15:00 | **~Jul 26** (2nd defense, fresh domain, ≤15:00) |
| **N41 integrative ladder build** | Jul 16 fail → Jul 17 +1:00 → Jul 19 FLUENT 5:40/12:00 | **~Jul 26** (2nd defense, fresh domain, ≤12:00) |
| N36 record-keeper | S14 2:59; ⊇-ridden Jul 19 (N40) + Jul 20 (build1 record-keeper limb) | spot-check only |
| N35 count accumulator | S13; ⊇-ridden Jul 19–20 (Jul 20: replaced by len(comprehension) mid-build — the compression itself is evidence) | Jul 23 clock pre-paid |
| N37 split-then-index-convert | S13; ⊇-ridden Jul 20 **inside a comprehension recipe** (int(split[i]) as one-line chain) | Jul 23 clock pre-paid |

## produced-once
| Node | Evidence | Next |
|---|---|---|
| **N59 list comprehensions (recipe/loop/gate)** | **Jul 19 acquisition + cold first-draft production** (item6: filter-only + transform+filter, N37 chain in recipe slot, own data). **Jul 20: first appearance inside real composition** (build1: two comprehensions — filter feeding transform feeding downstream loops; len() riding the filtered list). Clock paid full weight 2 days early | expanding; rides any composite build |
| N29 datetime pipeline | Jul 19 first production (hack3, post-corrective-block) | rides hack3 reruns + N58 timestamps |
| N30w-"a" append mode | Jul 19 (hack3, non-idempotence + prefix-\n convention) | rides composite builds |
| N34 gate pattern | S13–S16; Jul 19 solo streak-gate design; Jul 20 gate relocated *inside* a comprehension | rides composite builds |
| N24 except-as · N25 ladders · N26 honest fallback | Jul 17 cold; Jul 19 ridden full weight (N41 fluency) | ride N41-shaped builds |
| N44 navigation trio | Jul 17 cold run | daily SSH = free review (paused with hardware track — see note) |
| N47 cat + paths | Jul 17 cold; Jul 18 live on real Linux | rides shell work |
| **N51 file operations (mkdir/touch/mv/cp/rm/rm -r)** | **Jul 20 cold, unassisted, predictions-first, correct end state.** Four errors met live, four solo resolutions: ls-lists-the-room-you-stand-in (repair: invented `ls <path>` cold) · absolute-vs-relative leading slash ×2 · deleted-the-room-I-stood-in (ghost cwd, `cd ..` walkout) · final rm failure correctly read as confirmation-of-prior-success. rmdir recalled at reconciliation, not during — logged | expanding; rides shell work |
| N54 flash + headless · N55 SSH | Jul 18 produced (guided) | N55 review engine **idle during hardware pause** |

## taught / needs evidence
- (none in Python — tier clean)

## PYTHON TIER STATUS: zero nodes without production evidence · zero contracted debt · all clocks expanding
- **Acquisition frontier (updated Jul 19–20):** last new Python = **list comprehensions, Jul 19** (13-day pause ended). Queued next, cheap-first: generators (N59's sibling) → pip/requests (vehicle: Telegram hack, currently subject to hardware-pause ruling — his call which way it files).
- **Error catalogue: 16 species.** Jul 19 addition: IndexError (KeyError's list-sibling: missing position vs missing key; `~~~^^^` traceback markers noted). Jul 20 build1: five species met, five solo repairs (FileNotFoundError ×2 · printed-machine g.read-no-parens · AttributeError via line/lines one-letter trap · str-poisoned accumulator caught by staged print · TypeError str-vs-int in record-keeper seed comparison).
- **New audit rule (Jul 20, from spec-error incident):** when traced-correct output disagrees with the spec's stated expectation, flag the discrepancy aloud — correct-code-wrong-SPEC is a real species. (The spec's 3/160 was Claude's arithmetic error; his 4/200/day6 was correct and shipped without a flag.)

## Linux nodes (Tier L)
| Node | State |
|---|---|
| N42/N43/N45/N46/N48 | taught; ⊇-ridden by shell work. Jul 20: absolute-vs-relative surfaced as the remaining soft spot in N46 (leading-slash misses ×2) — exactly what Bandit drills |
| N44 · N47 · **N51** | **produced-once** |
| N49 find/grep · N50 permissions | **NOT TAUGHT — the entire remaining Bandit wall.** One teaching session away |

## Tier H — hardware/Pi: **PAUSED Jul 20 by his call** ("I'll tell you when we're back")
| Node | State |
|---|---|
| N54 · N55 | produced (guided); idle |
| N52 pip · N53 requests · N56 GPIO/PIR · N57 camera · N58 THE MACHINE | not taught; unscheduled until resume |
- Jul 21 hardware day CANCELED. Deliveries/pickup/SSD wipe untimed — parts don't decay. boogiewoogie idle at 192.168.0.9.
- Telegram hack filing ambiguity on record: it's hardware-track by purpose, pure-Python by content. His call whether the pause covers it.

## Gates
- Linux acquisition: OPEN. Bandit: **CLOSED** (wall = N49+N50 untaught; N44/N47/N51 now all produced-once — the production side of the gate is nearly cleared).
- Pi deployment: informally gated on Bandit-level shell fluency; moot during pause.
- **Doubling trial: CONFIRMED Jul 19 ("formal go"). Jul 20–26, day 0 = Jul 19 (unplanned, passed).**

## Doubling trial log
| Day | Date | Blocks | Notes |
|---|---|---|---|
| 0 | Jul 19 | 2 (defenses+hack3 / comprehensions acquisition+production) | unplanned proof-of-concept; fried at 4 PM |
| **1** | **Jul 20** | **2 (N51 cold / comprehension-riding build)** | **both blocks done before 1 PM, gas left.** 9 species repaired solo. No degradation signal. Same volume as day 0, better packing |
| 2–7 | Jul 21–26 | — | hardware day canceled; Jul 21 now a normal trial day. Day-7 = defenses + data decision |
- Success criteria: streak intact · cold times not degrading · day-7 decision from data. One-block days count. Misses inside the trial are data, not verdicts.

## Conduct rules (standing)
Timer to zero · mid-rep question voids · spec questions before clock free · predictions-first on shell runs — **including outputs per line, silence called explicitly (enforced Jul 20: command list alone ≠ predictions)** · no psychological commentary on motives/enthusiasm · his self-report is the diagnosis · design authority over his own tools is his · flag spec/output discrepancies aloud (new, Jul 20, binds both sides).

## Repo hygiene
- streak_log.txt honest as of Jul 19 (streak 24); daily run of hack3 is his habit to build. **Jul 20 run not yet confirmed — streak 25 pending his commit.**
- sandbox19 created and fully removed Jul 20 (correct end state, /c/Python clean).
- build1.py flags raised (no sermons): dead seed variables after len() compression · record-keeper loop re-splits what `minutes` already parsed · doubled parens in int((separate[2])).

## Session 19 record (Jul 20 — COMPLETE, trial day 1)
1. **Block 1 — N51 cold rep: PASS → produced-once.** Predictions-first enforced (commands-only draft sent back; outputs called before window opened). Four live errors, four solo resolutions incl. cold invention of `ls <path>` and `rm -r ../` from inside the target. rmdir forgotten during, recalled at reconciliation.
2. **Hardware track paused by his call.** Jul 21 hardware day canceled; Tier H unscheduled.
3. **Block 2 — comprehension-riding build (build1.py): COMPLETE.** Read-and-clean as comprehension per constraint; final file carries two (filter + transform-with-int-recipe). Five species met, five solo repairs. Design fork resolved: gate inside the comprehension → len() replaces count accumulator. Output 4/200/day6 correct; **spec's stated 3/160 was Claude's arithmetic error** — audit rule added. Comprehension clock paid full weight, 2 days early.
4. Both blocks complete before 1 PM.

## Next
1. **Jul 21 (Tue): trial day 2, normal shape.** Block 1 candidates: naked spot-check none needed (clocks pre-paid) → straight to production or the N51-adjacent frontier. Block 2: generators acquisition, or Telegram hack if he rules it Python-filed, or production.
2. Jul 23: N35/N37 clocks (pre-paid; spot-check).
3. **~Jul 26: N40 + N41 second defenses** (fresh domains) · **doubling trial day-7 data decision** (baselines: 9:47 and 5:40).
4. When slots exist: N49/N50 teaching → Bandit gate opens · generators · comprehension review rides any composite build.
5. Hardware track: resumes on his word only.
6. Daily habit his to build: hack3 run (streak self-maintenance).

═══════════════════════════════════════════════
# PART B — THE KNOWLEDGE GRAPH (structure)
═══════════════════════════════════════════════
`←` = prerequisite. `⊇` = encompasses (producing this implicitly reviews that), weight {1.0 full … 0.3 partial}. Warm-up selection = the one small build whose ⊇ edges cover the most due nodes.

**Tier 0 — substrate**
- N1 variables & assignment · N2 strings & f-strings ← N1 · N3 string methods ← N2 · N4 int()/float() ← N1 · N5 Git add/commit/push (independent spine; vim exits Jul 19)

**Tier 1 — containers & iteration**
- N6 lists & indexing ← N1 · N7 for loops ← N6 · N8 enumerate/unpacking ← N7,N6 · N9 dict access ← N1,N2 · N10 read-modify-write ← N9 · N11 create-vs-read asymmetry ← N9

**Tier 1 — control flow**
- N12 if/elif/else ← N1 · N13 branch ordering ← N12 · N14 boundaries/off-by-one ← N12 · N15 while ← N12 · N16 count-up ← N15,N7 · N17 while+if ← N15,N12 · N18 loop var outlives ← N7,N15

**Tier 2 — functions**
- N19 def/return ← N1 · N20 round() ← N19,N4 · N21 substitution model ← N19

**Tier 2 — errors & robustness**
- N22 try/except ← N12 · N23 specific nets ← N22 · N24 except-as ← N23 · N25 ladders ← N23,N13 · N26 .get()/None ← N9,N11 · N27 taxonomy (**16 species**; IndexError added Jul 19) ← N22,N4

**Tier 3 — library & I/O**
- N28 import (two forms) ← N1 · N29 datetime pipeline ← N28 — produced-once Jul 19 · N30 file I/O ← N28,N2 — all three modes produced

**Tier 3 — composite patterns**
- N31 .split() ← N2,N6 · N32 .append() ← N6 · N33 empty-tail ← N31,N14 · N34 gate ← N7,N12 · N35 count accumulator ← N7,N1 · N36 record-keeper ← N7,N12,N1 · N37 split-index-convert ← N31,N6,N4 · N38 if-guarded overwrite ← N12,N10,N36 · N39 seed-then-feed ← N35,N36,N7
- **N59 list comprehensions (recipe + loop + gate) ← N7,N6,N32,N34 — produced-once Jul 19, composition-proven Jul 20**
- N40 integrative composition ← N30,N31,N33,N34,N35,N36,N37 — FLUENT, defended Jul 19
- N41 integrative ladder ← N10,N35,N36,N25,N34,N26 — FLUENT Jul 19

**Tier L — Linux/shell**
- N42 shell/OS model · N43 cwd ← N42 · N44 navigation trio ← N42,N43 — **produced-once** · N45 home/~ ← N44 · N46 paths ← N43 (**soft spot Jul 20: leading-slash absolute-vs-relative**) · N47 cat + error anatomy ← N44,N46 — **produced-once** · N48 prompt anatomy ← N42 · N49 find/grep ← N44,N46 — **Bandit gate, untaught** · N50 permissions ← N44 — **Bandit gate, untaught** · **N51 file ops + flags ← N44,N46 — produced-once Jul 20**

**Tier H — hardware/Pi (PAUSED)**
- N52 pip ← N28 · N53 HTTP/requests ← N52,N19 · N54 flash+headless ← N42 — produced Jul 18 · N55 SSH ← N44,N54 — produced Jul 18 · N56 GPIO/PIR ← N52,N34 · N57 camera capture ← N52,N28 · N58 THE MACHINE ← N56,N57,N53,N30w,N29

**Future block (filed):** OOP ← N19,N21 · ~40h · post-camera · Generators ← N59,N7 (next cheap frontier).

**Encompassing edges:**
- N40 ⊇ N30{1.0}, N31{1.0}, N33{1.0}, N34{1.0}, N35{1.0}, N36{0.8}, N37{1.0}, N4{0.7}, N7{1.0}, N12{0.8}
- N41 ⊇ N9{1.0}, N10{1.0}, N7{1.0}, N35{0.8}, N36{0.7}, N12/N13{0.7}, N25{1.0}, N24{0.8}, N26{0.6}, N34{0.6}
- **N59 ⊇ N7{1.0}, N6{0.8}, N34{0.8 when gated}, N32{0.6 — replaces it}, N37{0.8 when chain-in-recipe}** — build1 proved the full edge set live
- hack3 ⊇ N29{1.0}, N30w-a{1.0}, N31{0.8}, N37{0.8}, N34{0.8}, N14{0.7}, N28{0.6}
- N39 ⊇ N35{1.0}, N36{0.6}, N7{1.0}, N1{0.7} · N38 ⊇ N12{1.0}, N36{0.8}, N10{0.6} · N37 ⊇ N31{1.0}, N6{1.0}, N4{0.4} · N36 ⊇ N7{1.0}, N12{0.8}, N1{0.6} · N35 ⊇ N7{1.0}, N1{0.7} · N33 ⊇ N31{0.8}, N14{0.5} · N30 ⊇ N28{0.5}, N2{0.4} · N29 ⊇ N28{0.5}, N4{0.3} · N25 ⊇ N23{1.0}, N13{0.8}, N24{0.8} · N17 ⊇ N15{1.0}, N12{1.0} · N16 ⊇ N15{1.0}, N7{0.7} · N8 ⊇ N7{1.0}, N6{0.8}
- N47 ⊇ N44{0.6}, N46{0.8}, N43{0.7} · N44 ⊇ N43{1.0}, N42{0.5} · N46 ⊇ N43{0.8} · **N51 ⊇ N44{0.8}, N46{0.9 — the Jul 20 run WAS a paths workout}, N43{0.7}**
- N55 ⊇ N44{1.0}, N42{0.7}, N48{0.8} — idle during pause
- N58 ⊇ N56{1.0}, N57{1.0}, N53{1.0}, N30w{0.8}, N34{0.8}, N29{0.7}

**Graph-reading notes (Jul 20, end of S19):**
- Python tier remains historic-clean and gained a node: N59 went taught → produced-once → composition-proven in ~26 hours.
- Shell production tier: N44/N47/N51 all produced-once. **The Bandit gate's production requirements are met; only the two untaught nodes (N49/N50) stand between here and a Bandit attempt.** N46's leading-slash soft spot is Bandit's home turf — it'll get drilled for free.
- Hardware pause idles the N55 review engine; navigation-cluster review falls back to Git Bash work until resume.
- Due: ~Jul 26 N40/N41 second defenses · Jul 23 spot-checks (pre-paid).

═══════════════════════════════════════════════
# PART C — HARDWARE LOG (track PAUSED Jul 20 — resumes on his word)
═══════════════════════════════════════════════

## The declared machine
Pi-based home security camera. V1: motion (PIR) → photo → Telegram alert → event log. Unchanged; paused, not canceled.

## Live systems
| Machine | State |
|---|---|
| **boogiewoogie** (Pi 4B 4GB, Argon ONE M.2) | ALIVE, idle. RPi OS Lite 64-bit (trixie), updated Jul 18. USB-boot (Toshiba 28.9GB), Wi-Fi jini 2.4GHz, **192.168.0.9**, `ssh snakeyboy777@192.168.0.9`. known_hosts Korean-path issue deferred |

## Inventory
| Item | Status |
|---|---|
| Pi 4 4GB + Argon ONE M.2 case + Argon USB 3.0 bridge | RUNNING (bridge + SSD disconnected until wipe) |
| Transcend 128GB M.2 SATA SSD | seller's OS aboard, untrusted; wipe-from-boogiewoogie pending (untimed); seller pw `qwert12#$5` or unset |
| Toshiba TransMemory 28.9GB USB | boot drive |
| Samsung 16GB microSD | idle, untested |
| Keerda 5V/3A | bench power, testing duty only |
| RPi Camera (D) 5MP + FFC · HC-SR501 ×2 · 점퍼 F/F · 방열케이스 | Eleparts #2026071714203717563 — pickup 가산, timing now his call |
| ElectroCookie 27W · SanDisk Ultra 32GB | arriving Tue Jul 21 (delivery unaffected by pause) |
| micro SD reader | broke Jul 18 — replace cheaply, no urgency |

## Case & setup facts
Micro SD slot external · jumper 2-3 = always-on (set at deployment) · M.2 data path = USB bridge only · camera-ribbon routing = known weak point (fallback: Argon on desk, 방열케이스 on wall) · Pi Connect declined · LED grammar: red steady = power, green flicker = disk.

## Deferred / v2
60cm camera cable · IR-CUT night camera · High Endurance SD · mmWave sensor · Pi AI Camera · known_hosts fix.

## Long-horizon references (filed)
Manafish ROV (9–15 mo) · rybtronics thermal drone (3–5 yr) · micro:bit→Arduino→ESP32 spine, roadmap months 3–6.