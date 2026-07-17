# ledger.md — updated 2026-07-17, mid-Session 16 (evening items pending)
# This file is the complete Skycak artifact: STATE (Part A) + GRAPH (Part B) + HARDWARE (Part C).
# Supersedes the 2026-07-15 ledger. Node IDs (N1…) are file-internal shorthand only — full names in conversation.
# S16 evening items (cold shell run, file-ops acquisition) NOT yet run — their rows say PENDING.

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
| **N40 composition: file-read→parse→report incl. write-then-read** | **S15 attempt 3 (Jul 16): PASS.** ~13:28/15:00, fully cold, zero assists, output 2/135/day4 clean. Both prior killers dead in first draft (inline colon fix; file written from Python). Self-repaired io.UnsupportedOperation (read on "w" handle → second with-block "r") inside the timer | **~Jul 19** (3d — first fluency check, fresh data, ≤15:00) |
| N36 record-keeper / max tracker | S14 retry 2:59, mid-timer self-repair of last-one-wins bug | **~Jul 21** (7d) |
| N35 count accumulator | S13 pass; Jul 16 review ridden via N40 attempt 3 at full weight | ~Jul 23 (7d) |
| N37 split-then-index-convert | S13 pass; Jul 16 review ridden via N40 attempt 3 at full weight | ~Jul 23 (7d) |

## produced-once
| Node | Evidence | Next |
|---|---|---|
| **N24 except-as naming** | Jul 16: written cold but caught object unused (culprit via loop variable); {A} added post-critique, quotes-on lesson re-derived from own output. **Jul 17 (S16 retry): cold, unprompted, functioning** — failure line named culprit via caught object | rides N41 fluency retry |
| **N25 exception ladders + honest backstop** | Jul 16: built post-critique only. **Jul 17: cold, correct order (specific first, Exception-as last), backstop correctly silent on healthy run.** Confession wording (culprit-not-species) flagged; his veto, closed | rides N41 fluency retry |
| **N41 integrative ladder build** | **Jul 17 (S16): first complete cold evidence.** All 4 spec items met unassisted: loud loop via {A}, full ladder, found-games accumulator INSIDE the try, honest quiet fallback. Over time ~+1:00. Mid-timer solo repair: for-loop pointed at dict instead of report list + loop-var shadowing — diagnosed from output (4 lines, no failure line) | **fluency attempt: next timed round, ≤12:00, fresh domain. NO interval contraction** (clean cold build 1 min over = expanding evidence) |
| N26 .get() with honest fallback | Jul 16: cold, non-impersonating fallback ("Game Not Found"); self-caught discarded-return slip. Jul 17: repeated clean | rides N41-shaped builds |
| N30w file writing ("w", \n, write-then-read) | First cold rep inside N40 attempt 3 (Jul 16). assisted → produced-once | rides composite builds; "a" mode still unproduced (streak-appender hack) |
| N30 with-frame | Cold in S13–S16 builds repeatedly incl. two with-blocks in one file | fold into fluent-legacy at next clean appearance |
| N34 gate pattern / gated count | A2, D1, S13–S16 compositions | rides composite builds |

## taught / needs evidence
- N29 datetime pipeline — **still zero production evidence.** Streak-appender hack remains the vehicle; pairs with N30w "a" mode + real stale-data repair.
- N27 error taxonomy — grew Jul 16: **io.UnsupportedOperation** (mode-as-contract: "w" handle is write-only; reading needs its own opening). Now 15 named species, all met and repaired at least once.

## Linux nodes (Tier L)
| Node | State | Evidence / next |
|---|---|---|
| N42 shell/OS model · N43 cwd · N45 home/~ · N46 paths · N48 prompt anatomy | taught | guided evidence Jul 14–15. N48 got live use Jul 17: read a seller's terminal screenshot (prompt, cat, free -h, df -h) to vet used hardware — comprehension evidence, not production |
| **N44 navigation trio** | taught → **cold attempt PENDING tonight** | S16 evening: typed, unassisted, predictions-first navigate run |
| **N47 cat + shell errors** | taught → **cold attempt PENDING tonight** | same run: cat from wrong cwd forces relative-.. or absolute path decision |
| **N51 file operations (mkdir/touch/rm/mv/cp)** | **NOT YET TAUGHT — acquisition PENDING tonight** | one idea: nav trio reads the filesystem, these five write it; incl. rm-has-no-undo (the "w"-wipe's bigger sibling) |
| N49 file search (find/grep) | not taught — **Bandit gate** | |
| N50 permissions | not taught — **Bandit gate** | also a Pi-track prerequisite (sudo, script execution) |

## Gates
- Linux acquisition: OPEN (acquisition-mode binding).
- **Bandit: CLOSED.** Requires N44, N49, N50 at produced-once (cold, typed, unassisted). N44's first cold attempt is tonight.
- **Pi first-boot: OPENS Jul 21 with hardware arrival** — no skill gate (headless flash + SSH is guided-acceptable as first contact); Pi *deployment* (wall-mounted camera) informally gated on the same shell fluency as Bandit.

## Conduct rules
- The attempt runs until the timer ends (Jul 15, standing).
- Mid-rep question = attempt void (S13, standing). **Spec questions before the clock = free (S15 precedent, standing).**
- No psychological commentary on his motives/enthusiasm; answer the asked question (Jul 16, his explicit request; reinforces the over-mechanizing rule).

## Repo hygiene
- **streak_log.txt still STALE** (last entry Jul 10 / streak 14; real ~21). Appender hack filed, not assigned.
- test.py scratch file (Jul 16) shadowed built-in `dict` — flagged once, throwaway.

## Session 15 record (Jul 16)
- N31 corrective micro-block: 5/5 reasoned cold; AttributeError name attached to pattern; **corrective flag REMOVED** (joint absent in both subsequent timed builds).
- **N40 → FLUENT** (attempt 3, details above). N30w → produced-once. N35/N37 reviews ridden.
- N41-shaped ladder build: SLOW/incomplete — dead-net first draft self-diagnosed from output mid-timer; backstop absent, accumulator on wrong container, except-as unused; all three fixed post-critique (corrected reps). 12-day starvation confirmed as the decay mechanism for this cluster.

## Session 16 record (Jul 17 — in progress)
- **N41 retry: cold clean sweep, +1:00 over** → N24, N25, N41 promoted to produced-once (details above).
- Python-coverage question answered (graph vs language vs load-bearing-20% framing; 15-species catalogue as the transferable asset). His conclusion: bottleneck is the shell → chose shell work.
- **PENDING tonight: N44/N47 cold run + N51 acquisition.**
- Hardware track opened and fully procured same day (Part C).

## Next
1. **Tonight**: N44/N47 cold shell run (predictions first, no timer, zero assists) + N51 acquisition. Then reprint ledger.
2. **Jul 19 (Sun)**: N40 first fluency review — fresh-data composition, cold, ≤15:00.
3. **Jul 21 (Tue)**: N36 review due. Hardware arrives (adapter + SD); Eleparts pickup likely; **first boot: flash SD (Imager, headless SSH+Wi-Fi preconfig), boot own OS, SSH in via Git Bash** — N44 skills on a real second machine.
4. **Jul 23**: N35 + N37 reviews.
5. When slots exist: N41 fluency retry · Telegram alert hack (opens N52/N53) · streak-appender hack (N29 + N30w-"a") · N49/N50 teaching toward Bandit.

═══════════════════════════════════════════════
# PART B — THE KNOWLEDGE GRAPH (structure)
═══════════════════════════════════════════════
`←` = prerequisite. `⊇` = encompasses (producing this implicitly reviews that), weight {1.0 full … 0.3 partial}. Warm-up selection = the one small build whose ⊇ edges cover the most due nodes.

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
- N24 except-as naming ← N23 — **produced-once Jul 17**
- N25 exception ladders (specific before broad) ← N23, N13 — **produced-once Jul 17**
- N26 .get() with fallback / None ← N9, N11 — **produced-once Jul 16**
- N27 error taxonomy (15 species incl. io.UnsupportedOperation, mode-as-contract) ← N22, N4

**Tier 3 — library & I/O**
- N28 import ← N1
- N29 datetime pipeline ← N28 — zero production evidence
- N30 file I/O ← N28, N2 — N30r+with ≈ fluent-track; **N30w produced-once Jul 16** ("a" mode unproduced)

**Tier 3 — processing & composite patterns**
- N31 .split() ← N2, N6 — **corrective flag REMOVED Jul 16**
- N32 .append() ← N6
- N33 empty-tail / empty-string handling ← N31, N14
- N34 gate pattern ← N7, N12
- N35 count accumulator ← N7, N1
- N36 record-keeper / max tracker ← N7, N12, N1
- N37 split-then-index-then-convert ← N31, N6, N4
- N38 if-guarded overwrite ← N12, N10, N36
- N39 seed-then-feed ← N35, N36, N7
- N40 integrative composition (incl. N30w write-then-read) ← N30, N31, N33, N34, N35, N36, N37 — **FLUENT Jul 16**
- N41 integrative ladder build ← N10, N35, N36, N25, N34, N26 — **produced-once Jul 17**; failure species logged Jul 16: accumulator outside the try totals the wrong container (correct-code-wrong-data)

**Tier L — Linux/shell**
- N42 shell/terminal/OS model + REPL (independent spine)
- N43 cwd, shell-side ← N42
- N44 navigation trio ← N42, N43 — cold attempt tonight
- N45 home directory & ~ ← N44
- N46 paths ← N43
- N47 cat + shell-error anatomy ← N44, N46 — cold attempt tonight
- N48 prompt anatomy ← N42 — live comprehension use Jul 17 (hardware vetting)
- N49 file search (find/grep) ← N44, N46 — not taught; **Bandit gate**
- N50 permissions ← N44 — not taught; **Bandit gate + Pi deployment**
- **N51 file operations: mkdir/touch/rm/mv/cp ← N44, N46 — acquisition tonight**

**Tier H — hardware/Pi (opened Jul 17 by procurement; nothing taught yet; block activates Jul 21)**
- N52 pip / third-party libraries ← N28 — first vehicle: Telegram hack
- N53 HTTP requests / API call (requests lib, webhook alert) ← N52, N19
- N54 flash + headless setup (Imager, SSH/Wi-Fi preconfig) ← N42 — guided-acceptable (first contact)
- N55 SSH into remote machine ← N44, N54 — the Bandit-shape skill on owned hardware
- N56 GPIO digital read (PIR via gpiozero) ← N52, N34 — "the gate pattern wearing a wire"
- N57 camera capture from Python ← N52, N28
- N58 integrative: motion → capture → log → alert (THE MACHINE) ← N56, N57, N53, N30w, N29

**Encompassing edges (review-compression map):**
- N40 ⊇ N30{1.0 incl. N30w}, N31{1.0}, N33{1.0}, N34{1.0}, N35{1.0}, N36{0.8}, N37{1.0}, N4{0.7}, N7{1.0}, N12{0.8}
- N41 ⊇ N9{1.0}, N10{1.0}, N7{1.0}, N35{0.8}, N36{0.7}, N12/N13{0.7}, N25{1.0}, N24{0.8}, N26{0.6}, N34{0.6} — full error-cluster review in one build
- N39 ⊇ N35{1.0}, N36{0.6}, N7{1.0}, N1{0.7}
- N38 ⊇ N12{1.0}, N36{0.8}, N10{0.6}
- N37 ⊇ N31{1.0}, N6{1.0}, N4{0.4}
- N36 ⊇ N7{1.0}, N12{0.8}, N1{0.6}
- N35 ⊇ N7{1.0}, N1{0.7}
- N33 ⊇ N31{0.8}, N14{0.5}
- N30 ⊇ N28{0.5}, N2{0.4}
- N29 ⊇ N28{0.5}, N4{0.3}
- N25 ⊇ N23{1.0}, N13{0.8}, N24{0.8}
- N17 ⊇ N15{1.0}, N12{1.0}; N16 ⊇ N15{1.0}, N7{0.7}; N8 ⊇ N7{1.0}, N6{0.8}
- N47 ⊇ N44{0.6}, N46{0.8}, N43{0.7} — best Linux review task; tonight's run
- N44 ⊇ N43{1.0}, N42{0.5}
- N46 ⊇ N43{0.8}
- N55 ⊇ N44{1.0}, N42{0.7}, N48{0.8} — once live, SSH sessions become free review of the whole navigation cluster
- N58 ⊇ N56{1.0}, N57{1.0}, N53{1.0}, N30w{0.8}, N34{0.8}, N29{0.7} — the machine IS the review engine once built

**Graph-reading notes (as of Jul 17 evening):**
- **The error cluster is repaired**: N24/N25/N26/N41 all carry cold production within 48h of being the most starved region. N41's fluency pass would move the whole cluster onto expanding intervals.
- **Tonight's shell run is the highest-leverage 10 minutes on the sheet**: first Tier-L production evidence, and N47 ⊇ covers N44/N46/N43 in one task.
- **Tier H exists but is dormant until Jul 21.** Its design intent: N55 and N58 are review-compression machines — once the Pi runs, daily SSH + the camera build silently review the entire Linux tier and half of Tier 3. The declared machine doubles as the spaced-repetition engine.
- **N29 remains the only zero-evidence Python node** — and N58 has a ⊇ edge to it (timestamps), so it gets production evidence the moment the camera logs its first event, if not earlier via the streak-appender.
- Due next: Jul 19 N40 · Jul 21 N36 · Jul 23 N35, N37.

═══════════════════════════════════════════════
# PART C — HARDWARE LOG (opened 2026-07-17)
═══════════════════════════════════════════════

## The declared machine
**Pi-based home security camera** replacing the broken one at home. V1: motion (PIR) → photo → Telegram alert → event log. Real problem, hack-series DNA, sits on existing skill graph.

## Inventory
| Item | Source | Cost | Status |
|---|---|---|---|
| Raspberry Pi 4 Model B **4GB** Rev 1.2 + Argon ONE V2 case + ~500GB SSD (SSD-boot configured, hostname devRasPi) | Danggeun, 여의도동, vetted via seller's live terminal screenshot (cat /proc/device-tree/model · free -h 3.7Gi · df -h sda2 469G) | ₩100,000 | **IN HAND (Jul 17, ~5 PM)** |
| RPi Camera (D) 5MP OV5647 66° + 16cm FFC · HC-SR501 ×2 · 점퍼 DC-40P 20cm F/F | Eleparts #2026071714203717563, 방문수령 가산 (대성디폴리스 A동 510호, 8:00–16:30, lunch 11:30–12:30) | ₩27,555 | PAID; pickup date pending KakaoTalk reply (quoted 발송예정일 7/21) |
| 방열 케이스 (ElectroCookie, camera holes + GPIO access + wall-mount holes) | Eleparts (earlier order line) | ₩12,100 | with above — likely redundant given Argon; keep as wall-duty case if Argon ribbon-routing fails |
| ElectroCookie 27W 5V/5A USB-C adapter | Coupang | ₩15,100 | arrives Tue 7/21 |
| SanDisk Ultra 32GB microSD (SDSQUNR) | Coupang | ₩18,560 | arrives Tue 7/21 |
| **Total** | | **~₩173,000** | |

## Known issues / deferred
- Argon ONE V2 camera-ribbon routing is awkward → fallback: Argon on desk, 방열케이스 (or cheap open case) on wall.
- 60cm camera cable (2,180원) — order at mounting time.
- Seller's OS on SSD = untrusted for a 24/7 networked camera → fresh flash to SD is the day-one move; SSD wipes/demotes to storage later.
- Filed v2 ideas: IR-CUT night camera (45,310원) · SanDisk High Endurance card (continuous video) · mmWave presence sensor (XenD101H, 6,300원) · Pi AI Camera (onboard detection).

## Long-horizon references (filed, not assigned)
- Manafish ROV (plans in bio) — robotics-track capstone, 9–15 mo horizon.
- rybtronics thermal drone — 3–5 yr horizon; custom PCB/SMD is its own craft.
- Both share the micro:bit→Arduino→ESP32 spine of roadmap months 3–6.