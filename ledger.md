# ledger.md — updated 2026-07-25, end of Session 23
# This file is the complete Skycak artifact: STATE (Part A) + GRAPH (Part B) + HARDWARE (Part C).
# Supersedes the 2026-07-23 print. Covers Sessions 22 (Jul 24) and 23 (Jul 25).
# Node IDs (N1…) are file-internal shorthand only — full names in conversation.

═══════════════════════════════════════════════
# PART A — STATE
═══════════════════════════════════════════════

## ★ PROGRAM STRUCTURE
**CS (Python + Linux) = single-track steady state. Mathematics holds the primary daily slot.**
- One solid CS block per day. ~38 days to summer break's end.
- Block selection rule: **the queue picks the block.** Due reviews/defenses first; frontier or production when nothing is due.
- **DAY COUNT, not streak (renamed 2026-07-25, his call).** The number = calendar days since June 26, zero days included. **Jul 25 = day 30.** Zero days on record: Jul 9, Jul 11, Jul 22 — counted honestly. The word "streak" was never accurate: item3.py computes `gap.days + 1`, a date subtraction that never checked whether a day was worked. Name now matches math.
- Optional cleanup, filed not assigned: `19th,July/item3.py` still names its variable `streak` and prints "The streak is now"; file still named streak_log.txt. Two-minute edit whenever he wants the tool to speak the new dialect.
- Doubling trial: SUPERSEDED Jul 23 (ran day 0–4; data archived).

## Fluent (legacy — spot-check occasionally, don't drill)
N1 variables · N2 f-strings · N3 string methods · N6 lists · N7 for loops · N8 unpacking ·
N12 if/elif/else · N13 branch ordering · N15 while · N9–N11 dict cluster · N19 functions ·
N22 try/except · N5 Git · N30 with-frame

## Fluent (recent promotions)
| Node | Evidence | Next review |
|---|---|---|
| **N40 composition** | Jul 16 13:28 → Jul 19 defended 9:47/15:00 | **~Jul 26 — TOMORROW** (2nd defense, fresh domain, ≤15:00) |
| **N41 integrative ladder** | Jul 16 fail → Jul 17 +1:00 → Jul 19 FLUENT 5:40/12:00 | **~Jul 26 — TOMORROW** (2nd defense, fresh domain, ≤12:00) |
| N36 record-keeper | S14 2:59; Jul 21 paid; **Jul 24 ⊇-ridden** (min-tracker variant, review.py) | expanding |
| N35 count accumulator | S13; Jul 21 paid early | expanding |
| N37 split-then-index-convert | S13; Jul 21 paid early; Jul 24 ridden | expanding |

## produced-once
| Node | Evidence | Next |
|---|---|---|
| N24 except-as · N25 ladders · N26 .get() fallback | Jul 17 cold, Jul 19 ridden | ride N41 defense Jul 26 |
| N29 datetime pipeline | Jul 19 hack3 | rides item3.py reruns |
| N30w-"a" append | Jul 19 hack3 | rides composite builds |
| N34 gate pattern | S13–S16 + Jul 19 solo design | rides composite builds |
| N59 list comprehensions | Jul 19 → Jul 20 composition-proven | expanding |
| N60 generators | Jul 21 both forms cold; **Jul 24 rep PAID** (birth-rate data, generator expression feeding min-tracker loop) | 1→3d, **next ~Jul 27** |
| N44 navigation trio · N47 cat+paths | Jul 17 cold; **both live on Bandit Jul 25** | ride Bandit |
| N51 file operations | Jul 20 cold rep | expanding |
| N54 flash+headless | Jul 18 (guided) | one-time skill |
| **N55 SSH** | Jul 18 guided → **Jul 24 solo reconnect to boogiewoogie · Jul 25 SSH to a STRANGER'S machine (bandit) with non-default port** | **ENGINE RESTARTED** — Bandit sessions now ⊇ the navigation cluster daily |
| **N50 permissions** | **Jul 24 taught + guided production run on boogiewoogie**: rwx×3-audience model, ls -l tag reading, chmod u±r, self-lockout as owner. 3/3 predictions on mechanism incl. the no-x directory trap | needs one cold rep — **Bandit will supply it free** |

## taught / needs evidence
- **N49 find/grep** — taught Jul 23, guided evidence strong. Cold rep pending; **can ride any Bandit level that hides a file**
- Pair-yielding generator recipe (N60 sub-pattern) — taught Jul 21 reconciliation only
- N27 error taxonomy — 17 species. **Jul 24 refinement: `int("6.4")` raises ValueError but `int(6.4)` works** — int() from a *string* demands integer-shaped text; float() accepts both. Chain for display: `int(float("6.4"))`. Conversion-as-discard also re-met (bare `float(pair[1])` on its own line — return value on the floor; same species as bare `.get()`)

## PYTHON TIER STATUS: all nodes production-evidenced · zero contracted debt · all clocks expanding
- Frontier (walking pace): **Bandit levels** (now the main vehicle) · Telegram hack N52/N53 (filing his call) · pair-yielding generator rep · generators' siblings

## Linux nodes (Tier L)
| Node | State |
|---|---|
| N42/N43/N45/N46/N48 | taught; ridden by every Bandit session |
| N44 · N47 · N51 | produced-once |
| N49 find/grep | taught + guided; cold rep pending |
| **N50 permissions** | **taught + guided Jul 24** |
- N46 soft spots: leading-slash absolute-vs-relative (Jul 20 ×2) · fresh-shell-starts-at-home (Jul 23, lived)

## Tier C — CYBER (OPENED Jul 25)
| Item | State |
|---|---|
| **Bandit gate** | **OPEN.** All prerequisite nodes taught; production side cleared |
| **Bandit level 0** | **CLEARED Jul 25** — SSH to bandit.labs.overthewire.org, port 2220, fingerprint + blind password |
| **Bandit 0→1** | **CLEARED Jul 25** — ls + cat in home directory; password retrieved, logged in as bandit1 |
| Bandit 1→2 | next; same read-a-file shape with a filename twist |
- **New concept taught Jul 25: PORT.** One machine, many numbered doors; SSH default 22 (used silently on every prior connect); Bandit runs 2220, named explicitly via `-p`. Flag grammar consistent with `rm -r`, `ls -l`
- **Banner intelligence noted as real intel, not decoration:** `/etc/bandit_pass/` holds every level's password, readable only by its own user — the permissions tag system IS the game's spine, announced in the welcome text. Home dirs are read-only; /tmp is sanctioned scratch
- Spoiler discipline: passwords stay his; Claude verifies by report only

## Tier H — hardware/Pi: PAUSED (Jul 20, his call; resumes on his word only)
- **Jul 24: Eleparts pickup COMPLETE** — RPi Camera (D) 5MP OV5647 + 16cm FFC, HC-SR501 ×2, DC-40P F/F jumpers, 방열케이스 all in hand. Inventory-in only, no hardware work
- N54/N55 produced · N52/N53/N56/N57/N58 untaught

## Gates
- Linux acquisition: OPEN · **Bandit: OPEN and ENTERED** · Pi deployment: informally gated on Bandit-level shell fluency

## ★ EXTERNAL SCHEDULE (new, Jul 25)
**2026-2학기: 프로그래밍언어 (AAK10076-40), IT경영전공 교필 — JAVA.** 이충석 · 월 11:30–13:20 · 화 09:30–11:20 · D동401호 · 3학점.
- **Weeks 4–10 = 객체지향** (클래스, 필드/메소드, 오버로딩, 생성자, 상속, 접근제한자, 오버라이딩, 추상클래스, 인터페이스, 다형성). **This IS the filed OOP block — now externally scheduled with a vehicle and a deadline.** ~40h estimate stands; the Java dialect forces the object model rather than allowing avoidance, which suits acquisition
- Weeks 1–3 (변수/연산자/제어문) = his fluent tier in Java clothes · Weeks 11–12 (파일과 스트림, 예외 처리) = owned concepts, new grammar
- Grading is build-shaped: 발표 25% · 실습 (팀 10% + 팀프로젝트 25%) · 3인 1팀 · **출석 1/5 이상 결석 시 F** (hard rule)
- Decision deferred: pre-study vs walk in cold in September

## Conduct rules (standing)
Timer to zero · mid-rep question voids · spec questions before clock free · no psychological commentary on motives/enthusiasm · predictions-first on shell runs (**5th skip instance Jul 25, Bandit login — logged, no sermon; rule stands**) · his self-report is the diagnosis · when memory holds no evidence, structural prediction IS the honest prediction · design authority over his own tools is his · traced-correct output disagreeing with spec gets flagged aloud (binds both sides)

## Repo hygiene & reconciliations
- hack3 = `19th,July/item3.py` on disk (reconciled Jul 23). item3c.py = corrective-block sibling; item4.py unrelated
- streak_log.txt honest as of Jul 19; runs since unconfirmed. Rename cleanup filed (see ★ structure)
- review.py (Jul 21) committed with the two-generator exhaustion bug — his file, his call

## Session 22 record (Jul 24 — COMPLETE)
1. **N60 generator rep PAID.** Birth-rate dataset, generator expression + downstream min-tracker. **ValueError on `int("6.4")`** met; three repairs attempted, all pointed at the wrong spot (type() check against a string that only looks like a float · bare float() with return discarded · bare round(), same discard). Fix supplied at reconciliation: `float()` accepts both shapes. **Unprompted win: while fleeing the conversion bug he rebuilt max-tracker-named-`lowest` into a genuine min-tracker** (`<` with seed 1000, seed correctly chosen to lose first comparison) — fixed a lying-name design bug nobody flagged
2. **N50 permissions acquisition + guided run.** Three verbs × three audiences × file-vs-directory meanings; ls -l ten-character tag; ownership line locates you; **first-match-wins identity resolution = the elif ladder, permissions edition**; chmod who/what/verb grammar. **Predictions 3/3**, including the drw-rw-rw- trap (no x anywhere = a furnished room nobody can enter). Run on boogiewoogie: birth tag `-rw-rw-r--` (no x by default; social not private — umask named), empty-cat silence, `chmod u-r` surgical (one switch, seven untouched), **owner locked out of own file** — tag outranks ownership; owner's power is to change the tag, never to bypass it
3. **Live ssh grammar lesson at zero cost:** `ssh boogiewoogie` defaulted to the *local* username (주현준), which doesn't exist on the Pi — three correct passwords refused. Diagnosed from the prompt line naming who was asking. `user@machine`'s left half = whose triple you're claiming
4. Eleparts pickup completed (see Tier H)

## Session 23 record (Jul 25 — COMPLETE, day 30)
1. **Day-count rename** (see ★ structure) — his catch, his call, permanent
2. **Java syllabus filed** (see ★ external schedule) — OOP block now externally scheduled
3. **BANDIT ENTERED.** Level 0 cleared (port concept taught, `-p 2220`, fingerprint + blind password, known_hosts cosmetic error as expected). Level 0→1 cleared (ls + cat, structural prediction given where memory held no evidence). Logged in as bandit1
- Flags: predictions skipped before the login run (5th instance, logged)

## Next (queue-picked, one block/day)
1. **Jul 26 (TOMORROW): N40 + N41 second defenses** — fresh domains, ≤15:00 and ≤12:00, cold, timer to zero. Baselines 9:47 and 5:40. **First live test of the effort-metric commitment if either misses**
2. **~Jul 27: N60 generator rep** (minutes, folds into anything)
3. Then: Bandit 1→2 onward — block-sized, self-reviewing, and the vehicle for N49's cold rep and N50's cold rep
4. Filed: Telegram hack (N52/N53) if filed Python · pair-yielding generator promotion · item3.py rename cleanup
5. Hardware: resumes on his word only

═══════════════════════════════════════════════
# PART B — THE KNOWLEDGE GRAPH (structure)
═══════════════════════════════════════════════
`←` = prerequisite. `⊇` = encompasses, weight {1.0 full … 0.3 partial}.

**Tier 0 — substrate**
- N1 variables · N2 f-strings ← N1 · N3 string methods ← N2 · N4 int()/float() ← N1 (**Jul 24: string-conversion asymmetry — int() demands integer-shaped text, float() accepts both**) · N5 Git

**Tier 1 — containers & iteration**
- N6 lists ← N1 · N7 for loops ← N6 · N8 enumerate/unpacking ← N7,N6 · N9 dict access ← N1,N2 · N10 read-modify-write ← N9 · N11 create-vs-read asymmetry ← N9

**Tier 1 — control flow**
- N12 if/elif/else ← N1 · N13 branch ordering ← N12 · N14 boundaries ← N12 · N15 while ← N12 · N16 count-up ← N15,N7 · N17 while+if ← N15,N12 · N18 loop var outlives ← N7,N15

**Tier 2 — functions**
- N19 def/return ← N1 · N20 round() ← N19,N4 · N21 substitution model ← N19

**Tier 2 — errors & robustness**
- N22 try/except ← N12 · N23 specific nets ← N22 · N24 except-as ← N23 · N25 ladders ← N23,N13 · N26 .get()/None ← N9,N11 · N27 taxonomy (17 species) ← N22,N4

**Tier 3 — library & I/O**
- N28 import ← N1 · N29 datetime ← N28 · N30 file I/O ← N28,N2 (all modes produced)

**Tier 3 — composite patterns**
- N31 .split() ← N2,N6 · N32 .append() ← N6 · N33 empty-tail ← N31,N14 · N34 gate ← N7,N12 · N35 count accumulator ← N7,N1 · N36 record-keeper ← N7,N12,N1 (**min-tracker variant produced Jul 24**) · N37 split-index-convert ← N31,N6,N4 · N38 if-guarded overwrite ← N12,N10,N36 · N39 seed-then-feed ← N35,N36,N7
- N40 integrative composition ← N30,N31,N33,N34,N35,N36,N37 — FLUENT
- N41 integrative ladder ← N10,N35,N36,N25,N34,N26 — FLUENT
- N59 comprehensions ← N7,N6,N34 — produced + composition-proven
- N60 generators ← N59,N7,N19 — produced-once, rep paid Jul 24

**Tier L — Linux/shell**
- N42 shell/OS model (wildcard expansion happens before the program launches) · N43 cwd ← N42 · N44 nav trio ← N42,N43 — produced · N45 home/~ ← N44 · N46 paths ← N43 · N47 cat ← N44,N46 — produced · N48 prompt anatomy ← N42 · N49 find/grep ← N44,N46,N42 — taught+guided · **N50 permissions ← N44 — taught+guided Jul 24** · N51 file ops ← N44,N46 — produced

**Tier H — hardware/Pi (paused)**
- N52 pip ← N28 · N53 HTTP/requests ← N52,N19 · N54 flash+headless ← N42 — produced · N55 SSH ← N44,N54 — produced (**+port/-p flag Jul 25**) · N56 GPIO/PIR ← N52,N34 · N57 camera ← N52,N28 · N58 THE MACHINE ← N56,N57,N53,N30w,N29

**Tier C — cyber (NEW, opened Jul 25)**
- **N61 Bandit ← N44,N46,N47,N49,N50,N55** — levels 0 and 0→1 cleared. The track's own review engine

**External block:** OOP ← N19,N21 — **scheduled 2026-2학기 via Java (weeks 4–10)**

**Encompassing edges:**
- N40 ⊇ N30{1.0}, N31{1.0}, N33{1.0}, N34{1.0}, N35{1.0}, N36{0.8}, N37{1.0}, N4{0.7}, N7{1.0}, N12{0.8}
- N41 ⊇ N9{1.0}, N10{1.0}, N7{1.0}, N35{0.8}, N36{0.7}, N12/N13{0.7}, N25{1.0}, N24{0.8}, N26{0.6}, N34{0.6}
- **N61 Bandit ⊇ N55{1.0}, N44{1.0}, N46{0.9}, N47{1.0}, N48{0.8}, N49{0.8 when a level hides a file}, N50{0.9}, N42{0.7} — the shell tier's live review engine, replacing the idle boogiewoogie loop**
- N49 ⊇ N44{0.6}, N46{0.9}, N43{0.7}, N42{0.6} · N50 ⊇ N44{0.4}, N48{0.6}, N13{0.5 first-match-wins}
- N60 ⊇ N59{0.7}, N7{1.0}, N19{0.6} · N59 ⊇ N7{1.0}, N6{0.8}, N34{0.8}, N32{0.6}, N37{0.8}
- item3.py ⊇ N29{1.0}, N30w-a{1.0}, N31{0.8}, N37{0.8}, N34{0.8}, N14{0.7}, N28{0.6}
- N39 ⊇ N35{1.0}, N36{0.6}, N7{1.0}, N1{0.7} · N38 ⊇ N12{1.0}, N36{0.8}, N10{0.6} · N37 ⊇ N31{1.0}, N6{1.0}, N4{0.4} · N36 ⊇ N7{1.0}, N12{0.8}, N1{0.6} · N35 ⊇ N7{1.0}, N1{0.7} · N33 ⊇ N31{0.8}, N14{0.5} · N30 ⊇ N28{0.5}, N2{0.4} · N29 ⊇ N28{0.5}, N4{0.3} · N25 ⊇ N23{1.0}, N13{0.8}, N24{0.8} · N17 ⊇ N15{1.0}, N12{1.0} · N16 ⊇ N15{1.0}, N7{0.7} · N8 ⊇ N7{1.0}, N6{0.8}
- N47 ⊇ N44{0.6}, N46{0.8}, N43{0.7} · N44 ⊇ N43{1.0}, N42{0.5} · N46 ⊇ N43{0.8} · N51 ⊇ N44{0.5}, N46{0.6}
- N55 ⊇ N44{1.0}, N42{0.7}, N48{0.8} — **live again as of Jul 24**
- N58 ⊇ N56{1.0}, N57{1.0}, N53{1.0}, N30w{0.8}, N34{0.8}, N29{0.7}

**Graph-reading notes (Jul 25, end of S23):**
- **Tier C is open and entered.** Bandit now carries the shell tier's review load — every level silently exercises navigation, paths, cat, and increasingly find/grep and permissions. N49 and N50's cold reps will arrive as by-products rather than assignments.
- Python review is quiet except tomorrow's two defenses; the frontier is deliberately parked while Bandit runs.
- OOP is no longer a floating ~40h estimate — it has a date, a vehicle, and an attendance rule.

═══════════════════════════════════════════════
# PART C — HARDWARE LOG
═══════════════════════════════════════════════

## The declared machine
**Pi-based home security camera.** V1: motion (PIR) → photo → Telegram alert → event log. TRACK PAUSED Jul 20, his call; resumes on his word.

## Live systems
| Machine | State |
|---|---|
| **boogiewoogie** (Pi 4B 4GB, Argon ONE M.2) | ALIVE. RPi OS Lite 64 (trixie). USB-boot (Toshiba stick), Wi-Fi jini 2.4GHz, **192.168.0.9**, `ssh snakeyboy777@192.168.0.9` (**bare `ssh boogiewoogie` defaults to the Windows username and fails — always name the user**). Used Jul 24 for the permissions run. known_hosts Korean-path issue: cosmetic, permanent-until-fixed |

## Inventory
| Item | Status |
|---|---|
| Pi 4 4GB + Argon ONE M.2 + USB bridge | running (bridge+SSD disconnected until wipe) |
| Transcend 128GB M.2 SSD | seller's OS aboard, untrusted; wipe deferred |
| Toshiba 28.9GB USB | boot drive |
| Samsung 16GB microSD | idle, untested |
| Keerda 5V/3A | bench power, testing only |
| **RPi Camera (D) 5MP OV5647 + 16cm FFC · HC-SR501 ×2 · DC-40P F/F jumpers · 방열케이스** | **IN HAND — picked up Jul 24, Eleparts 가산** |
| ElectroCookie 27W · SanDisk 32GB | delivery status unlogged since pause |
| micro SD reader | broke Jul 18; replace cheaply |

## Case & setup facts
SD slot external · jumper 2-3 = always-on (set at deployment) · M.2 data path = USB bridge only · ribbon routing = weak point (fallback: Argon desk, 방열케이스 wall) · Pi Connect declined · LED grammar: red steady = power, green flicker = disk.

## Deferred / v2
60cm cable · IR-CUT camera · High Endurance SD · mmWave sensor · Pi AI Camera · known_hosts fix.

## Long-horizon (filed)
Manafish ROV (9–15mo) · rybtronics thermal drone (3–5yr).