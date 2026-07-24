# ledger.md — updated 2026-07-23, end of Session 21
# This file is the complete Skycak artifact: STATE (Part A) + GRAPH (Part B) + HARDWARE (Part C).
# Supersedes the 2026-07-21 print. Node IDs (N1…) are file-internal shorthand only — full names in conversation.

═══════════════════════════════════════════════
# PART A — STATE
═══════════════════════════════════════════════

## ★ PROGRAM STRUCTURE (changed 2026-07-23, his decision)
**CS (Python + Linux) = single-track steady state. Mathematics holds the primary daily slot.**
- One solid CS block per day — not minimized, not doubled. ~40 days to summer break's end.
- **Doubling trial: SUPERSEDED** (not failed). Ran day 0–4 (Jul 19–22, incl. one zero day Jul 22); data archived; day-7 decision moot.
- Block selection rule: **the queue picks the block.** Due reviews/defenses first; frontier acquisition or production when nothing is due. Same graph-decides principle, one block enforcing it.
- Streak continues under this shape (day 28 as of Jul 23 commit).
- Zero days on record: Jul 9, Jul 11, **Jul 22** — counted honestly.

## Fluent (legacy — spot-check occasionally, don't drill)
N1 variables & assignment · N2 strings & f-strings · N3 string methods (strings-iterable appended Jul 21) ·
N6 lists & indexing · N7 for loops · N8 .items()/enumerate unpacking ·
N12 if/elif/else · N13 branch ordering · N15 while loops ·
N9–N11 dict read/write/KeyError asymmetry · N19 functions ·
N22 try/except mechanics · N5 Git add/commit/push · N30 with-frame

## Fluent (recent promotions)
| Node | Evidence | Next review |
|---|---|---|
| **N40 composition** | Jul 16 pass 13:28 → Jul 19 defended 9:47/15:00 | **~Jul 26** (2nd defense, fresh domain, ≤15:00) |
| **N41 integrative ladder** | Jul 16 fail → Jul 17 +1:00 → Jul 19 FLUENT 5:40/12:00 | **~Jul 26** (2nd defense, fresh domain, ≤12:00) |
| N36 record-keeper | S14 2:59; Jul 21 spot-check paid | expanding; rides composite builds |
| N35 count accumulator | S13; Jul 21 paid early | expanding; rides composite builds |
| N37 split-then-index-convert | S13; Jul 21 paid early | expanding; rides composite builds |

## produced-once
| Node | Evidence | Next |
|---|---|---|
| N24 except-as · N25 ladders · N26 .get() fallback | Jul 17 cold, Jul 19 ⊇-ridden | ride N41 defense Jul 26 |
| N29 datetime pipeline | Jul 19 hack3 production | rides hack3 reruns + N58 |
| N30w-"a" append | Jul 19 hack3 | rides composite builds |
| N34 gate pattern | S13–S16 + Jul 19 solo gate design | rides composite builds |
| N59 list comprehensions | Jul 19 → Jul 20 composition-proven | expanding |
| N60 generators | Jul 21 both forms cold; wild exhaustion encounter same day | **1st review due ~Jul 24** — one generator expression inside anything, minutes |
| N44 navigation trio · N47 cat+paths | Jul 17 cold | ride shell work (SSH engine idle) |
| N51 file operations | Jul 20 cold rep, 4 solo repairs | expanding |
| N54 flash+headless · N55 SSH | Jul 18 produced (guided) | idle during hardware pause |

## taught / needs evidence
- **N49 find/grep — TAUGHT Jul 23 (Session 21), guided evidence strong.** Needs one cold production rep to promote. Evidence detail in session record below.
- Pair-yielding generator recipe (N60 sub-pattern) — taught Jul 21 reconciliation only
- N27 error taxonomy — 17 species (generator exhaustion added Jul 21)

## PYTHON TIER STATUS: all nodes production-evidenced · zero contracted debt · all clocks expanding
- Frontier (frozen-but-walking under new structure, cheap-first): permissions (N50, ~1 block, **opens Bandit**) → Bandit levels (block-sized, self-reviewing) → Telegram hack (N52/N53, 2–3 blocks, filing his call) → pair-yielding generator rep → generators' siblings

## Linux nodes (Tier L)
| Node | State |
|---|---|
| N42/N43/N45/N46/N48 | taught; ⊇-ridden by shell work |
| N44 · N47 · N51 | produced-once |
| **N49 find/grep** | **taught + guided Jul 23; cold rep pending, predictions-first** |
| N50 permissions | **untaught — the Bandit wall is now ONE idea thick.** Raw material already met: Permission-denied wall (lived Jul 23), $ vs #, sudo (~10× Jul 18) |
- N46 soft spot: leading-slash absolute-vs-relative (Jul 20 ×2) · **new Jul 23: fresh-shell-starts-at-home bit him live** (find ran from ~ against predictions written for /c/Python — bedroom/kitchen lesson, find edition; self-readable from prompt)

## Tier H — hardware/Pi: PAUSED (Jul 20, his call; resumes on his word only)
- N54/N55 produced · N52/N53/N56/N57/N58 untaught
- Delivery/pickup status unlogged since pause — log receipt if/when mentioned

## Gates
- Linux acquisition: OPEN · **Bandit: CLOSED — wall = N50 only** (production side + find/grep teaching done)
- Pi deployment: informally gated on Bandit-level shell fluency

## Conduct rules (standing)
Timer to zero · mid-rep question voids · spec questions before clock free · no psychological commentary on motives/enthusiasm · predictions-first on shell runs (**4th skip instance Jul 23 — logged, no sermon; rule stands**) · his self-report is the diagnosis (Jul 23 addendum: when memory genuinely holds no evidence, structural prediction IS the honest prediction — commitment standard applies only when evidence exists) · design authority over his own tools is his · traced-correct output disagreeing with spec gets flagged aloud (binds both sides)

## Repo hygiene & reconciliations
- **hack3 = `19th,July/item3.py` on disk** — name reconciled Jul 23 via find/grep archaeology. Ledger name and disk name now cross-referenced. item3c.py = corrective-block sibling rep (writes date.today() direct); item4.py = unrelated build reusing streak vocabulary.
- Naming-drift lesson on record: ledger name / memory name / disk name are three separate records that drift unless reconciled. Bandit-relevant: filenames there are designed to be unhelpful; location-and-property search is the muscle.
- streak_log.txt: honest as of Jul 19; runs since unconfirmed. Daily hack3 (item3.py) run remains his habit to build.
- review.py (Jul 21) final committed state carries the two-generator exhaustion bug; working draft was prior version. His file, his call.

## Session 21 record (Jul 23 — COMPLETE, one block ~9:54–11:30)
**N49 find/grep acquisition — taught via live search problem.**
1. find anatomy (start point, -name, wildcard) + grep (contents, multi-file `filename:line` attribution) + division of labor: find reads labels, grep reads papers
2. **Fresh-shell-at-home miss, live:** first run searched ~ not /c/Python — predictions invalidated by room, not model. Permission-denied wall met (find reports locked doors and keeps walking — Bandit foreshadow, N50 raw material). Discovery function fired (forgotten Desktop/Python_Cram files surfaced)
3. Re-run with explicit start point (`find /c/Python -name ...`) — find-native habit named: starting point is an argument, standing doesn't matter
4. **Real search problem, end to end:** "hack3.py" missing → hypotheses (deleted vs renamed) → wildcard nets (`*hack*`: hack1/hack2/hack2b, all 5th,July · `*streak*`: log only) → full .py census → narrowed to 19th,July → **grep multi-file identified item3.py by contents** (gap.days fencepost, index-7 gate, "a" append — architecture read from matching lines alone)
5. Shell-expansion mechanism taught on his stop-and-ask: shell rewrites the line before the program launches; wildcards free everywhere; rm * corollary filed
6. Grep prediction corrected: prints the whole matching line (context is the evidence), not the word
7. Prediction-discipline refinements: file-explorer check = look-don't-recall (legal); running the search = answer key (illegal) · empty result answers the question asked, never the question meant
8. Permissions offered, banked — his volume call, affirmed
**Afternoon: program restructure declared and encoded (see ★ above).**

## Next (queue-picked, one block/day)
1. **Jul 24: N60 generator rep due** (minutes, folds into anything) + **N50 permissions** as the natural block → **Bandit opens**
2. **~Jul 26: N40 + N41 second defenses** (fresh domains, ≤15:00 / ≤12:00)
3. Then: Bandit level 0→ (block-sized, self-reviewing) · N49 cold rep (can hide inside Bandit) · Telegram hack if filed · pair-yielding generator promotion
4. Hardware: resumes on his word only

═══════════════════════════════════════════════
# PART B — THE KNOWLEDGE GRAPH (structure)
═══════════════════════════════════════════════
`←` = prerequisite. `⊇` = encompasses, weight {1.0 full … 0.3 partial}.

**Tier 0 — substrate**
- N1 variables · N2 f-strings ← N1 · N3 string methods ← N2 · N4 int()/float() ← N1 · N5 Git (independent spine)

**Tier 1 — containers & iteration**
- N6 lists ← N1 · N7 for loops ← N6 · N8 enumerate/unpacking ← N7,N6 · N9 dict access ← N1,N2 · N10 read-modify-write ← N9 · N11 create-vs-read asymmetry ← N9

**Tier 1 — control flow**
- N12 if/elif/else ← N1 · N13 branch ordering ← N12 · N14 boundaries/off-by-one ← N12 · N15 while ← N12 · N16 count-up ← N15,N7 · N17 while+if ← N15,N12 · N18 loop var outlives ← N7,N15

**Tier 2 — functions**
- N19 def/return ← N1 · N20 round() ← N19,N4 · N21 substitution model ← N19

**Tier 2 — errors & robustness**
- N22 try/except ← N12 · N23 specific nets ← N22 · N24 except-as ← N23 · N25 ladders ← N23,N13 · N26 .get()/None ← N9,N11 · N27 taxonomy (17 species) ← N22,N4

**Tier 3 — library & I/O**
- N28 import ← N1 · N29 datetime ← N28 · N30 file I/O ← N28,N2 (all modes produced)

**Tier 3 — composite patterns**
- N31 .split() ← N2,N6 · N32 .append() ← N6 · N33 empty-tail ← N31,N14 · N34 gate ← N7,N12 · N35 count accumulator ← N7,N1 · N36 record-keeper ← N7,N12,N1 · N37 split-index-convert ← N31,N6,N4 · N38 if-guarded overwrite ← N12,N10,N36 · N39 seed-then-feed ← N35,N36,N7
- N40 integrative composition ← N30,N31,N33,N34,N35,N36,N37 — FLUENT
- N41 integrative ladder ← N10,N35,N36,N25,N34,N26 — FLUENT
- N59 list comprehensions ← N7,N6,N34 — produced + composition-proven
- N60 generators ← N59,N7,N19 — produced-once; sub-pattern (pair-yielding recipe) taught-only

**Tier L — Linux/shell**
- N42 shell/OS model (Jul 23 addition: **shell pre-processes the line — wildcard expansion before program launch**) · N43 cwd ← N42 · N44 nav trio ← N42,N43 — produced · N45 home/~ ← N44 (fresh-shell-at-home, lived Jul 23) · N46 paths ← N43 (leading-slash soft spot) · N47 cat ← N44,N46 — produced · N48 prompt anatomy ← N42 · **N49 find/grep ← N44,N46,N42{expansion} — TAUGHT+guided Jul 23** · N50 permissions ← N44 — **untaught, the whole Bandit wall** · N51 file ops ← N44,N46 — produced

**Tier H — hardware/Pi (paused)**
- N52 pip ← N28 · N53 HTTP/requests ← N52,N19 · N54 flash+headless ← N42 — produced · N55 SSH ← N44,N54 — produced · N56 GPIO/PIR ← N52,N34 · N57 camera ← N52,N28 · N58 THE MACHINE ← N56,N57,N53,N30w,N29

**Future block (filed):** OOP ~40h, post-camera.

**Encompassing edges:**
- N40 ⊇ N30{1.0}, N31{1.0}, N33{1.0}, N34{1.0}, N35{1.0}, N36{0.8}, N37{1.0}, N4{0.7}, N7{1.0}, N12{0.8}
- N41 ⊇ N9{1.0}, N10{1.0}, N7{1.0}, N35{0.8}, N36{0.7}, N12/N13{0.7}, N25{1.0}, N24{0.8}, N26{0.6}, N34{0.6}
- **N49 ⊇ N44{0.6}, N46{0.9}, N43{0.7}, N42{0.6}** — Jul 23 session rode the whole navigation cluster (paths in two dialects, cwd, prompt-reading)
- N60 ⊇ N59{0.7}, N7{1.0}, N19{0.6} · N59 ⊇ N7{1.0}, N6{0.8}, N34{0.8}, N32{0.6}, N37{0.8}
- hack3/item3.py ⊇ N29{1.0}, N30w-a{1.0}, N31{0.8}, N37{0.8}, N34{0.8}, N14{0.7}, N28{0.6}
- N39 ⊇ N35{1.0}, N36{0.6}, N7{1.0}, N1{0.7} · N38 ⊇ N12{1.0}, N36{0.8}, N10{0.6} · N37 ⊇ N31{1.0}, N6{1.0}, N4{0.4} · N36 ⊇ N7{1.0}, N12{0.8}, N1{0.6} · N35 ⊇ N7{1.0}, N1{0.7} · N33 ⊇ N31{0.8}, N14{0.5} · N30 ⊇ N28{0.5}, N2{0.4} · N29 ⊇ N28{0.5}, N4{0.3} · N25 ⊇ N23{1.0}, N13{0.8}, N24{0.8} · N17 ⊇ N15{1.0}, N12{1.0} · N16 ⊇ N15{1.0}, N7{0.7} · N8 ⊇ N7{1.0}, N6{0.8}
- N47 ⊇ N44{0.6}, N46{0.8}, N43{0.7} · N44 ⊇ N43{1.0}, N42{0.5} · N46 ⊇ N43{0.8} · N51 ⊇ N44{0.5}, N46{0.6}
- N55 ⊇ N44{1.0}, N42{0.7}, N48{0.8} — idle during pause
- N58 ⊇ N56{1.0}, N57{1.0}, N53{1.0}, N30w{0.8}, N34{0.8}, N29{0.7}
- **Bandit (once open) ⊇ N44, N46, N47, N49, N50, N48 at high weight per level — the shell tier's future review engine**

**Graph-reading notes (Jul 23, end of S21):**
- Single-track math: one block/day, queue-picked. Due next: N60 rep (~Jul 24, trivial) · N50 (opens Bandit) · Jul 26 defenses.
- The Bandit wall is one idea thick. One block from the gate opening.
- Under steady state, Bandit levels are the ideal block unit: self-contained, self-reviewing, appetite-matched.

═══════════════════════════════════════════════
# PART C — HARDWARE LOG
═══════════════════════════════════════════════

## The declared machine
**Pi-based home security camera.** V1: motion (PIR) → photo → Telegram alert → event log. TRACK PAUSED Jul 20, his call; resumes on his word.

## Live systems
| Machine | State |
|---|---|
| **boogiewoogie** (Pi 4B 4GB, Argon ONE M.2) | ALIVE, idle. RPi OS Lite 64 (trixie), updated Jul 18. USB-boot (Toshiba stick), Wi-Fi jini 2.4GHz, **192.168.0.9**, `ssh snakeyboy777@192.168.0.9`. known_hosts Korean-path issue deferred |

## Inventory
| Item | Status |
|---|---|
| Pi 4 4GB + Argon ONE M.2 + USB bridge | running (bridge+SSD disconnected until wipe) |
| Transcend 128GB M.2 SSD | seller's OS aboard, untrusted; wipe deferred (pause) |
| Toshiba 28.9GB USB | boot drive |
| Samsung 16GB microSD | idle, untested |
| Keerda 5V/3A | bench power, testing only |
| Camera OV5647 + FFC · HC-SR501 ×2 · jumpers · 방열케이스 | Eleparts — status unlogged since pause |
| ElectroCookie 27W · SanDisk 32GB | delivery status unlogged since pause |
| micro SD reader | broke Jul 18; replace cheaply |

## Case & setup facts
SD slot external · jumper 2-3 = always-on (set at deployment) · M.2 data path = USB bridge only · ribbon routing = weak point (fallback: Argon desk, 방열케이스 wall) · Pi Connect declined · LED grammar: red steady = power, green flicker = disk.

## Deferred / v2
60cm cable · IR-CUT camera · High Endurance SD · mmWave sensor · Pi AI Camera · known_hosts fix.

## Long-horizon (filed)
Manafish ROV (9–15mo) · rybtronics thermal drone (3–5yr).