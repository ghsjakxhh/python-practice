# ledger.md — updated 2026-07-17, end of Session 16
# This file is the complete Skycak artifact: STATE (Part A) + GRAPH (Part B) + HARDWARE (Part C).
# Supersedes the mid-S16 ledger. Node IDs (N1…) are file-internal shorthand only — full names in conversation.

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
| **N40 composition: file-read→parse→report incl. write-then-read** | S15 attempt 3 (Jul 16): PASS. ~13:28/15:00, fully cold, zero assists. Self-repaired io.UnsupportedOperation inside the timer | **~Jul 19** (3d — first fluency check, fresh data, ≤15:00) |
| N36 record-keeper / max tracker | S14 retry 2:59, mid-timer self-repair of last-one-wins bug | **~Jul 21** (7d) |
| N35 count accumulator | S13 pass; Jul 16 review ridden via N40 attempt 3 | ~Jul 23 (7d) |
| N37 split-then-index-convert | S13 pass; Jul 16 review ridden via N40 attempt 3 | ~Jul 23 (7d) |

## produced-once
| Node | Evidence | Next |
|---|---|---|
| N24 except-as naming | Jul 17 (S16 retry): cold, unprompted, functioning — failure line named culprit via caught object | rides N41 fluency retry |
| N25 exception ladders + honest backstop | Jul 17: cold, correct order, backstop correctly silent on healthy run. Confession wording flagged; his veto, closed | rides N41 fluency retry |
| N41 integrative ladder build | Jul 17 (S16): first complete cold evidence, all 4 spec items, over time ~+1:00. Mid-timer solo repair (wrong container + loop-var shadowing, diagnosed from output) | **fluency attempt: next timed round, ≤12:00, fresh domain. NO interval contraction** |
| N26 .get() with honest fallback | Jul 16 cold; Jul 17 repeated clean | rides N41-shaped builds |
| N30w file writing ("w", \n, write-then-read) | First cold rep inside N40 attempt 3 (Jul 16) | rides composite builds; "a" mode still unproduced (streak-appender hack) |
| N30 with-frame | Cold in S13–S16 builds repeatedly | fold into fluent-legacy at next clean appearance |
| N34 gate pattern / gated count | A2, D1, S13–S16 compositions | rides composite builds |
| **N44 navigation trio** | **Jul 17 (S16 evening): first cold shell production run. Typed, unassisted; mid-run ordering slip self-repaired via cd .. (prompt-as-cwd-display used unprompted). Prediction layer SKIPPED — second spec-step skip on record (first: Jul 14 file-write); folded into next run, predictions-first is load-bearing from here** | rides future shell runs + SSH (N55) |
| **N47 cat + paths + shell errors** | **Jul 17: cat streak_log.txt from /c/Python, then cat /c/Python/ledger.md from inside 12th,July — absolute-path answer chosen and executed correctly (relative ../ also valid). ⊇ credit to N43/N46 at full weight** | rides future shell runs |

## taught / needs evidence
- N29 datetime pipeline — **still the only zero-evidence Python node.** Streak-appender hack remains the vehicle (streak_log.txt printed its stale July-10 lines on screen during tonight's run — the hack advertises itself).
- N27 error taxonomy — 15 named species, all met and repaired at least once.
- **N51 file operations (mkdir/touch/rm/mv/cp)** — **taught Jul 17 (S16 evening), guided production in sandbox**: full create/copy/rename/delete cycle run. rm-refuses-directories error met and read; **rm -r taught as first flag** (recursive delete, no-undo-no-size-limit danger named). **His own experiment: mv'd a directory to sandbox.txt — proved names don't change nature; trailing-/ marker held.** Guided evidence only; cold rep pending. Sandbox created in 12th,July instead of /c/Python — flagged once.

## Linux nodes (Tier L)
| Node | State | Evidence / next |
|---|---|---|
| N42 shell/OS model · N43 cwd · N45 home/~ · N46 paths · N48 prompt anatomy | taught, ⊇-credited | N43/N46 rode tonight's N44/N47 run at full weight. N48: live comprehension use Jul 17 (hardware vetting) |
| **N44 navigation trio** | **produced-once** (see Part A table) | |
| **N47 cat + paths** | **produced-once** (see Part A table) | |
| **N51 file operations** | **taught + guided** | needs one cold rep (predictions-first) |
| N49 file search (find/grep) | not taught — **Bandit gate** | |
| N50 permissions | not taught — **Bandit gate + Pi deployment** | |

## Gates
- Linux acquisition: OPEN.
- **Bandit: CLOSED, but first pillar placed** — N44 now produced-once. Remaining: N49, N50 (untaught) at produced-once, plus N51 cold rep recommended.
- **Pi first-boot: OPENS Jul 21 with hardware arrival** — headless flash + SSH is guided-acceptable as first contact; Pi *deployment* informally gated on Bandit-level shell fluency.

## Conduct rules
- The attempt runs until the timer ends (Jul 15, standing).
- Mid-rep question = attempt void (S13); **spec questions before the clock = free (S15, standing).**
- No psychological commentary on his motives/enthusiasm; answer the asked question (Jul 16, standing).
- **Predictions-first on shell runs is load-bearing from S17 on** (tonight's skip logged, not voided — first rep in new domain).

## Repo hygiene
- **streak_log.txt still STALE** (July 10 / streak 14; real ~21). Appender hack filed, not assigned.
- sandbox directory in 12th,July — deleted via rm -r at session close (confirm with ls).

## Session 16 record (Jul 17 — COMPLETE)
- N41 retry: cold clean sweep, +1:00 over → N24, N25, N41 produced-once.
- Python-coverage question answered; his conclusion: bottleneck is the shell.
- **Evening: N44/N47 cold shell run → both produced-once** (first Tier-L production evidence). N51 acquisition complete (guided). First flag taught (rm -r).
- Hardware track: procurement closed, board opened and fully identified (Part C).

## Next
1. **Jul 19 (Sun)**: N40 first fluency review — fresh-data composition, cold, ≤15:00.
2. **Jul 21 (Tue)**: N36 review due. Hardware arrives (adapter + SD); Eleparts pickup likely; **first boot: flash SD (Imager, headless SSH+Wi-Fi preconfig), boot own OS, SSH in via Git Bash** — N44 skills on a real second machine.
3. **Jul 23**: N35 + N37 reviews.
4. When slots exist: N41 fluency retry (≤12:00) · N51 cold rep (predictions-first) · Telegram alert hack (opens N52/N53) · streak-appender hack (N29 + N30w-"a") · N49/N50 teaching toward Bandit.

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
- N24 except-as naming ← N23 — produced-once Jul 17
- N25 exception ladders (specific before broad) ← N23, N13 — produced-once Jul 17
- N26 .get() with fallback / None ← N9, N11 — produced-once Jul 16
- N27 error taxonomy (15 species incl. io.UnsupportedOperation, mode-as-contract) ← N22, N4

**Tier 3 — library & I/O**
- N28 import ← N1
- N29 datetime pipeline ← N28 — zero production evidence
- N30 file I/O ← N28, N2 — N30r+with ≈ fluent-track; N30w produced-once Jul 16 ("a" mode unproduced)

**Tier 3 — processing & composite patterns**
- N31 .split() ← N2, N6 — corrective flag removed Jul 16
- N32 .append() ← N6
- N33 empty-tail / empty-string handling ← N31, N14
- N34 gate pattern ← N7, N12
- N35 count accumulator ← N7, N1
- N36 record-keeper / max tracker ← N7, N12, N1
- N37 split-then-index-then-convert ← N31, N6, N4
- N38 if-guarded overwrite ← N12, N10, N36
- N39 seed-then-feed ← N35, N36, N7
- N40 integrative composition (incl. N30w write-then-read) ← N30, N31, N33, N34, N35, N36, N37 — **FLUENT Jul 16**
- N41 integrative ladder build ← N10, N35, N36, N25, N34, N26 — produced-once Jul 17

**Tier L — Linux/shell**
- N42 shell/terminal/OS model + REPL (independent spine)
- N43 cwd, shell-side ← N42
- N44 navigation trio ← N42, N43 — **produced-once Jul 17**
- N45 home directory & ~ ← N44
- N46 paths ← N43
- N47 cat + shell-error anatomy ← N44, N46 — **produced-once Jul 17**
- N48 prompt anatomy ← N42 — live comprehension use Jul 17
- N49 file search (find/grep) ← N44, N46 — not taught; **Bandit gate**
- N50 permissions ← N44 — not taught; **Bandit gate + Pi deployment**
- N51 file operations: mkdir/touch/rm/mv/cp + rm -r + flags concept ← N44, N46 — **taught + guided Jul 17**

**Tier H — hardware/Pi (procured Jul 17; block activates Jul 21)**
- N52 pip / third-party libraries ← N28 — first vehicle: Telegram hack
- N53 HTTP requests / API call ← N52, N19
- N54 flash + headless setup (Imager, SSH/Wi-Fi preconfig) ← N42 — guided-acceptable (first contact)
- N55 SSH into remote machine ← N44, N54 — the Bandit-shape skill on owned hardware
- N56 GPIO digital read (PIR via gpiozero) ← N52, N34 — "the gate pattern wearing a wire"
- N57 camera capture from Python ← N52, N28
- N58 integrative: motion → capture → log → alert (THE MACHINE) ← N56, N57, N53, N30w, N29

**Encompassing edges (review-compression map):**
- N40 ⊇ N30{1.0 incl. N30w}, N31{1.0}, N33{1.0}, N34{1.0}, N35{1.0}, N36{0.8}, N37{1.0}, N4{0.7}, N7{1.0}, N12{0.8}
- N41 ⊇ N9{1.0}, N10{1.0}, N7{1.0}, N35{0.8}, N36{0.7}, N12/N13{0.7}, N25{1.0}, N24{0.8}, N26{0.6}, N34{0.6}
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
- N47 ⊇ N44{0.6}, N46{0.8}, N43{0.7} — ridden Jul 17
- N44 ⊇ N43{1.0}, N42{0.5}
- N46 ⊇ N43{0.8}
- N51 ⊇ N44{0.5}, N46{0.6}
- N55 ⊇ N44{1.0}, N42{0.7}, N48{0.8} — once live, SSH sessions become free review of the whole navigation cluster
- N58 ⊇ N56{1.0}, N57{1.0}, N53{1.0}, N30w{0.8}, N34{0.8}, N29{0.7} — the machine IS the review engine once built

**Graph-reading notes (as of Jul 17, end of S16):**
- **Tier L has its first production evidence**: N44 and N47 produced-once, N51 taught+guided. The Bandit gate's remaining wall is N49/N50 (untaught) — one teaching session away from attemptable.
- The error cluster is repaired; N41's fluency pass moves it onto expanding intervals.
- Tier H activates Jul 21. N55 and N58 are review-compression machines — once the Pi runs, daily SSH + the camera build silently review the entire Linux tier and half of Tier 3.
- N29 remains the only zero-evidence Python node — N58 has a ⊇ edge to it; streak-appender gets it sooner.
- Due next: Jul 19 N40 · Jul 21 N36 · Jul 23 N35, N37.

═══════════════════════════════════════════════
# PART C — HARDWARE LOG (opened 2026-07-17)
═══════════════════════════════════════════════

## The declared machine
**Pi-based home security camera** replacing the broken one at home. V1: motion (PIR) → photo → Telegram alert → event log. Real problem, hack-series DNA, sits on existing skill graph.

## Inventory (CORRECTED Jul 17 evening — case opened, contents physically verified)
| Item | Source | Cost | Status |
|---|---|---|---|
| Raspberry Pi 4 Model B **4GB** Rev 1.2 | Danggeun, 여의도동 | ₩100,000 (bundle) | **IN HAND** |
| **Argon ONE M.2 case** (NOT plain V2 — includes M.2 SATA expansion board in base, top board 05152021V2.6, M.2 board 12152020V1.6) | (bundle) | — | IN HAND, opened & inspected |
| **Transcend 128GB M.2 SATA SSD (TS128GMTS830S, Feb 2021)** — supersedes prior "~500GB" note; physical label + listing + seller Kakao all agree on 128GB. Prior 469G df-h reading no longer trusted as describing this drive | (bundle) | — | IN HAND; carries seller's OS (untrusted, keep until own OS boots) |
| **Argon USB 3.0 U-turn bridge** (M.2 board → Pi USB3; the "mystery block", Argon Forty logo) | (bundle) | — | IN HAND |
| RPi Camera (D) 5MP OV5647 66° + 16cm FFC · HC-SR501 ×2 · 점퍼 DC-40P 20cm F/F | Eleparts #2026071714203717563, 방문수령 가산 | ₩27,555 | PAID; pickup pending KakaoTalk reply (quoted 발송예정일 7/21) |
| 방열 케이스 (ElectroCookie, camera holes + GPIO + wall-mount holes) | Eleparts (earlier line) | ₩12,100 | with above — wall-duty fallback case |
| ElectroCookie 27W 5V/5A USB-C adapter | Coupang | ₩15,100 | arrives Tue 7/21 |
| SanDisk Ultra 32GB microSD (SDSQUNR) | Coupang | ₩18,560 | arrives Tue 7/21 |
| Keerda 5V/3A USB-C adapter (seller-supplied, KC-certified, 15W) | (bundle) | — | IN HAND; testing-only stopgap — bare-minimum spec for Pi4+fan+SSD, not for 24/7 duty |
| **Total** | | **~₩173,000** | |

## Case facts learned Jul 17 (opened with 4 screws)
- Micro SD slot accessible from OUTSIDE the case — Tuesday's flash needs no disassembly.
- Jumper on top board: 1-2 DEFAULT / **2-3 ALWAYS ON** (auto-boot on power restore) — set to 2-3 at deployment for blackout recovery; leave as-is for now.
- M.2 board connects to Pi solely via the USB bridge (no internal data path).
- Camera-ribbon routing still the known awkward spot → fallback unchanged (Argon on desk, 방열케이스 on wall).

## Known issues / deferred
- 60cm camera cable (2,180원) — order at mounting time.
- Seller's OS on SSD = untrusted for a 24/7 networked camera → fresh flash to SD is the day-one move; SSD wipes/demotes to storage later.
- Filed v2 ideas: IR-CUT night camera (45,310원) · SanDisk High Endurance card · mmWave presence sensor (XenD101H, 6,300원) · Pi AI Camera.

## Long-horizon references (filed, not assigned)
- Manafish ROV — robotics-track capstone, 9–15 mo horizon.
- rybtronics thermal drone — 3–5 yr horizon; custom PCB/SMD is its own craft.
- Both share the micro:bit→Arduino→ESP32 spine of roadmap months 3–6.