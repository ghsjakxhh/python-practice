# ledger.md — updated 2026-07-19, end of Session 18
# This file is the complete Skycak artifact: STATE (Part A) + GRAPH (Part B) + HARDWARE (Part C).
# Supersedes the mid-S18 (morning) print. Node IDs (N1…) are file-internal shorthand only — full names in conversation.

═══════════════════════════════════════════════
# PART A — STATE
═══════════════════════════════════════════════

## Fluent (legacy — spot-check occasionally, don't drill)
N1 variables & assignment · N2 strings & f-strings · N3 string methods ·
N6 lists & indexing · N7 for loops · N8 .items()/enumerate unpacking ·
N12 if/elif/else · N13 branch ordering · N15 while loops ·
N9–N11 dict read/write/KeyError asymmetry · N19 functions ·
N22 try/except mechanics · N5 Git add/commit/push (extended Jul 19: commit-without--m → vim editor; :q! and i/Esc/:wq exits taught)

## Fluent (recent promotions)
| Node | Evidence | Next review |
|---|---|---|
| **N40 composition (write→read→parse→report)** | Jul 16 pass 13:28 → **Jul 19 DEFENDED 9:47/15:00**, fresh data, cold, zero assists, exact output. Colon fix + fused record-keeper + one-pass loop, first draft | **~Jul 26** (7d, fresh domain, ≤15:00) |
| **N41 integrative ladder build** | Jul 16 could-not-produce → Jul 17 +1:00 → **Jul 19 FLUENT 5:40/12:00**, fresh domain, all 4 items first-draft (loud {A} loop · correct ladder, silent backstop · accumulator inside try · honest quiet fallback) | **~Jul 26** (7d, fresh domain, ≤12:00) |
| N36 record-keeper | S14 2:59; ⊇-ridden Jul 19 at 0.8 (fused updates in N40 defense) | Jul 21 clock pre-paid; spot-check only |
| N35 count accumulator | S13; ⊇-ridden Jul 16 + Jul 19 full weight | Jul 23 clock pre-paid |
| N37 split-then-index-convert | S13; ⊇-ridden Jul 19 (N40 full + solo int() repair in hack3) | Jul 23 clock pre-paid |

## produced-once
| Node | Evidence | Next |
|---|---|---|
| N24 except-as naming | Jul 17 cold; Jul 19 ⊇-ridden full weight | expanding; rides N41 |
| N25 exception ladders | Jul 17 cold; Jul 19 ridden full weight | expanding; rides N41 |
| N26 .get() honest fallback | Jul 16–17; Jul 19 ridden | rides N41-shaped builds |
| **N29 datetime pipeline** | **Jul 19 first production**: decay met head-on (traced Jul 6, "forgot all syntax" Jul 19 = 13-day gap) → corrective micro-block: worked example + 3 blocked reps from blank → live in hack3. import-forms distinction self-raised (import datetime vs from-import = different name-creating lines). Fencepost +1 reasoned to day-24 by hand; off-by-one species attached | rides hack3 reruns + N58 timestamps |
| **N30w-"a" append mode** | **Jul 19 produced in hack3** — incl. live append non-idempotence (double line manufactured; "idempotent" taught) and prefix-\n convention (correct-by-convention, his deliberate choice, comment flag vetoed) | rides composite builds |
| N30 with-frame | 3 with-blocks in hack3 alone; repeatedly cold since S13 | fold into fluent-legacy at next print |
| N34 gate pattern | S13–S16; **Jul 19: reinvented solo as streak-number gate (own design: append only if last-logged streak < computed streak)** | rides composite builds |
| N44 navigation trio | Jul 17 cold run (predictions skipped — logged) | daily SSH = free review (N55 ⊇) |
| N47 cat + paths | Jul 17 cold; Jul 18 live on real Linux (cat /etc/os-release, absolute path from ~) | rides shell work |
| N54 flash + headless setup | **Jul 18 produced (guided-acceptable per protocol first-contact rule)**: Imager, Lite-64 Trixie, user/Wi-Fi/SSH customisation; SD reader broke → USB-boot improvisation on Toshiba stick | one-time skill; re-evidence at next flash |
| N55 SSH into remote machine | **Jul 18 produced (guided)**: .local timeout → router DHCP-list diagnosis → SSH by IP; fingerprint trust; blind password; reconnected independently post-reboot | **LIVE REVIEW ENGINE** — every session ⊇ N44/N42/N48 |

## taught / needs evidence
- N51 file operations (mkdir/touch/mv/cp/rm, rm -r, flags concept) — taught + guided Jul 17; **cold rep pending, predictions-first**
- N27 error taxonomy — 15 species, all repaired. Jul 19 experience additions: TypeError str-vs-int (solo int() fix); machine-not-shelf mirror (g.read no-parens, solo)

## PYTHON TIER STATUS: zero nodes without production evidence · zero contracted debt · all clocks expanding
- **Acquisition frontier note (Jul 19, his catch):** last new Python concept taught = datetime, Jul 6 — a deliberate 13-day consolidation pause, now complete. The acquisition slot is FREE, not forbidden. Queued frontier, cheap-first: comprehensions (compresses owned loops) → generators → pip/requests (vehicle: Telegram hack).

## Linux nodes (Tier L)
| Node | State |
|---|---|
| N42/N43/N45/N46/N48 | taught; ⊇-ridden by every SSH session. Jul 18 additions: /home vs /c/Users dialect · prompt-reading across machines (lived: typed Pi command at Windows prompt post-disconnect, zero cost) |
| N44 · N47 | produced-once |
| N51 | taught + guided; cold rep pending |
| N49 find/grep · N50 permissions | **NOT TAUGHT — the entire remaining Bandit wall.** N50 head start: sudo/root used ~10× in practice Jul 18 |

## Tier H — hardware/Pi (ACTIVE since Jul 18, 3 days early via USB boot)
| Node | State |
|---|---|
| N54 · N55 | produced (guided) — see above |
| N52 pip · N53 HTTP/requests | not taught — vehicle: Telegram hack (hardware-free, boogiewoogie can host) |
| N56 GPIO/PIR · N57 camera capture | not taught — hardware lands ~Jul 21 |
| N58 THE MACHINE | not taught — ⊇ edge to N29 means first logged camera event re-reviews datetime automatically |

## Gates
- Linux acquisition: OPEN.
- **Bandit: CLOSED.** Wall = N49 + N50 (untaught), one teaching session away. SSH mechanics for bandit0@bandit already produced (N55).
- Pi deployment (wall-mounted camera): informally gated on Bandit-level shell fluency.
- **Doubling trial (Jul 20–26): PROPOSED, awaiting his confirmation.** Structure: Block 1 morning (current session shape) + Block 2 evening (production or cross-domain acquisition; NEVER second same-domain acquisition — the 1–2-new-ideas cap is per-domain and hour-invariant). Success criteria: streak intact, cold-rep times not degrading, day-7 data decision. One-block days still count.

## Conduct rules (standing)
Timer to zero · mid-rep question voids · spec questions before clock free · no psychological commentary on motives/enthusiasm · predictions-first on shell runs (S17+) · his self-report is the diagnosis · design authority over his own tools is his (Jul 19 precedent: format/duplicates/convention defended with reasons → conceded, costs named once, flag-and-veto).

## Repo hygiene
- **streak_log.txt HONEST as of Jul 19** (streak 24, computed from real clock). hack3 gate prevents duplicate-day appends. Running it daily is his habit to build; mixed-format history accepted by his explicit choice (future whole-file parsers must handle both shapes).
- hack3 quirk on record: prefix-\n convention (file never ends with newline; last split piece always real). Correct-by-convention; comment flag vetoed.

## Session 18 record (Jul 19 — COMPLETE)
1. **N40 fluency defense: PASS 9:47** (4 min faster than first pass). Interval 3→7d.
2. **N41 fluency: PASS 5:40** (under half target). Error cluster fully expanding; contracted-retry arc complete (3-day showcase: fail → over → half-time).
3. **hack3 COMPLETE**: N29 + N30w-"a" produced. Corrective micro-block run mid-hack per protocol (decay → isolate → 3 blocked reps → recompose). Solo gate design. Solo TypeError repair. Design-authority exchange closed.
4. git-commit/vim encounter resolved.
5. Afternoon: university comparison (straight answer) · Python fluency treemap (~65h owned = load-bearing quarter; ~200h remaining; bands: cheap frontier / OOP mountain ~40h post-camera / skippable internals) · doubling proposal + acquisition-frontier clarification.
- Flags raised (no sermons): `sprint` name colliding with data vocab · "keyboard" vs "headphone" spec-literalism · counting loop vs len() · prefix-\n comment (vetoed).

## Next
1. **Jul 20 (Mon): doubling trial day 1 IF confirmed** — Block 1 candidate: comprehensions acquisition (frontier reopens) · Block 2 candidate: Telegram hack or N51 cold rep.
2. **Jul 21 (Tue): hardware day** — ElectroCookie + SanDisk arrive · Eleparts pickup (camera, PIR ×2, jumpers, 방열케이스) · **SSD wipe from inside boogiewoogie** → demote to storage · first camera/PIR contact (N56/N57 acquisition) · N36 spot-check (pre-paid).
3. Jul 23: N35/N37 clocks (pre-paid; spot-check).
4. **~Jul 26: N40 + N41 second defenses** (fresh domains) · doubling trial day-7 decision.
5. When slots exist: **N49/N50 teaching → Bandit gate opens** · N51 cold rep · Telegram hack (N52/N53) · comprehensions/generators acquisition.
6. Daily freebie: SSH into boogiewoogie (N55 ⊇ navigation cluster).
7. Filed: OOP block (~40h) as post-camera mountain — needed for gpiozero-style object APIs · known_hosts Korean-path fix (cosmetic).

═══════════════════════════════════════════════
# PART B — THE KNOWLEDGE GRAPH (structure)
═══════════════════════════════════════════════
`←` = prerequisite. `⊇` = encompasses (producing this implicitly reviews that), weight {1.0 full … 0.3 partial}. Warm-up selection = the one small build whose ⊇ edges cover the most due nodes.

**Tier 0 — substrate**
- N1 variables & assignment · N2 strings & f-strings ← N1 · N3 string methods ← N2 · N4 int()/float() ← N1 · N5 Git add/commit/push (independent spine; vim exits appended Jul 19)

**Tier 1 — containers & iteration**
- N6 lists & indexing ← N1 · N7 for loops ← N6 · N8 enumerate/unpacking ← N7,N6 · N9 dict access ← N1,N2 · N10 read-modify-write ← N9 · N11 create-vs-read asymmetry ← N9

**Tier 1 — control flow**
- N12 if/elif/else ← N1 · N13 branch ordering ← N12 · N14 boundaries/off-by-one ← N12 (fencepost variant produced Jul 19) · N15 while ← N12 · N16 count-up ← N15,N7 · N17 while+if ← N15,N12 · N18 loop var outlives ← N7,N15

**Tier 2 — functions**
- N19 def/return ← N1 · N20 round() ← N19,N4 · N21 substitution model ← N19

**Tier 2 — errors & robustness**
- N22 try/except ← N12 · N23 specific nets ← N22 · N24 except-as ← N23 · N25 ladders ← N23,N13 · N26 .get()/None ← N9,N11 · N27 taxonomy (15 species) ← N22,N4

**Tier 3 — library & I/O**
- N28 import ← N1 (two forms distinguished Jul 19: import-box vs from-import-tool, different names created)
- N29 datetime pipeline ← N28 — **produced-once Jul 19**
- N30 file I/O ← N28,N2 — **all three modes now produced** (r/with fluent-track · w Jul 16 · a Jul 19)

**Tier 3 — composite patterns**
- N31 .split() ← N2,N6 · N32 .append() ← N6 · N33 empty-tail ← N31,N14 · N34 gate ← N7,N12 · N35 count accumulator ← N7,N1 · N36 record-keeper ← N7,N12,N1 · N37 split-index-convert ← N31,N6,N4 · N38 if-guarded overwrite ← N12,N10,N36 · N39 seed-then-feed ← N35,N36,N7
- N40 integrative composition ← N30,N31,N33,N34,N35,N36,N37 — **FLUENT, defended Jul 19**
- N41 integrative ladder ← N10,N35,N36,N25,N34,N26 — **FLUENT Jul 19**

**Tier L — Linux/shell**
- N42 shell/OS model (spine) · N43 cwd ← N42 · N44 navigation trio ← N42,N43 — **produced-once** · N45 home/~ ← N44 · N46 paths ← N43 · N47 cat + error anatomy ← N44,N46 — **produced-once** · N48 prompt anatomy ← N42 (cross-machine reading lived Jul 18) · N49 find/grep ← N44,N46 — **Bandit gate, untaught** · N50 permissions ← N44 — **Bandit gate, untaught** · N51 file ops + flags ← N44,N46 — taught+guided

**Tier H — hardware/Pi**
- N52 pip ← N28 · N53 HTTP/requests ← N52,N19 · N54 flash+headless ← N42 — **produced Jul 18** · N55 SSH ← N44,N54 — **produced Jul 18, live engine** · N56 GPIO/PIR ← N52,N34 · N57 camera capture ← N52,N28 · N58 THE MACHINE ← N56,N57,N53,N30w,N29

**Future block (filed, not scheduled): OOP** — classes/objects/methods/inheritance ← N19,N21 · ~40h · prerequisite-shaped for gpiozero-style APIs (N56/N57 consume objects) · natural post-camera opening.

**Encompassing edges:**
- N40 ⊇ N30{1.0 all modes}, N31{1.0}, N33{1.0}, N34{1.0}, N35{1.0}, N36{0.8}, N37{1.0}, N4{0.7}, N7{1.0}, N12{0.8}
- N41 ⊇ N9{1.0}, N10{1.0}, N7{1.0}, N35{0.8}, N36{0.7}, N12/N13{0.7}, N25{1.0}, N24{0.8}, N26{0.6}, N34{0.6}
- hack3 ⊇ N29{1.0}, N30w-a{1.0}, N31{0.8}, N37{0.8}, N34{0.8}, N14{0.7}, N28{0.6}
- N39 ⊇ N35{1.0}, N36{0.6}, N7{1.0}, N1{0.7} · N38 ⊇ N12{1.0}, N36{0.8}, N10{0.6} · N37 ⊇ N31{1.0}, N6{1.0}, N4{0.4} · N36 ⊇ N7{1.0}, N12{0.8}, N1{0.6} · N35 ⊇ N7{1.0}, N1{0.7} · N33 ⊇ N31{0.8}, N14{0.5} · N30 ⊇ N28{0.5}, N2{0.4} · N29 ⊇ N28{0.5}, N4{0.3} · N25 ⊇ N23{1.0}, N13{0.8}, N24{0.8} · N17 ⊇ N15{1.0}, N12{1.0} · N16 ⊇ N15{1.0}, N7{0.7} · N8 ⊇ N7{1.0}, N6{0.8}
- N47 ⊇ N44{0.6}, N46{0.8}, N43{0.7} · N44 ⊇ N43{1.0}, N42{0.5} · N46 ⊇ N43{0.8} · N51 ⊇ N44{0.5}, N46{0.6}
- **N55 ⊇ N44{1.0}, N42{0.7}, N48{0.8} — LIVE: every boogiewoogie session silently reviews the navigation cluster**
- N58 ⊇ N56{1.0}, N57{1.0}, N53{1.0}, N30w{0.8}, N34{0.8}, N29{0.7} — the machine IS the review engine once built

**Graph-reading notes (Jul 19, end of S18):**
- **Historic state confirmed and extended: every Python node has production evidence, all intervals expanding, zero debt.** Python is review-quiet until ~Jul 26 AND acquisition-open now — two different facts, both true.
- The bottleneck is the shell, and specifically two untaught nodes: N49, N50. One teaching session from a Bandit attempt.
- Cheapest high-value acquisitions available: comprehensions (rides N7/N6 fluency), pip/requests (rides the Telegram hack, feeds N58).
- Tier H: N56/N57 acquisition unblocks Jul 21 with hardware; N58's ⊇ web makes the finished camera a standing review engine for half the graph.
- Due: ~Jul 26 N40/N41 defenses · Jul 21/23 clocks pre-paid (spot-checks fine).

═══════════════════════════════════════════════
# PART C — HARDWARE LOG
═══════════════════════════════════════════════

## The declared machine
**Pi-based home security camera** replacing the broken one at home. V1: motion (PIR) → photo → Telegram alert → event log. Real problem, hack-series DNA, sits on existing skill graph.

## Live systems
| Machine | State |
|---|---|
| **boogiewoogie** (Pi 4 Model B 4GB Rev 1.2, Argon ONE M.2 case) | **ALIVE since Jul 18.** Raspberry Pi OS Lite 64-bit (Debian 13 trixie), fully updated Jul 18 (58 pkgs incl. python3.13). Boots from Toshiba TransMemory 28.9GB USB stick, blue USB3 port. Wi-Fi 2.4GHz (jini), **192.168.0.9**, SSH by IP (`ssh snakeyboy777@192.168.0.9`; .local resolution unreliable on Windows). User snakeyboy777. Renamed via hostnamectl + /etc/hosts nano edit (address-book lesson). Windows-side known_hosts write fails on Korean-username path — cosmetic, fingerprint re-asked per session, deferred |

## Inventory
| Item | Status |
|---|---|
| Pi 4 4GB + **Argon ONE M.2 case** (corrected from "V2" Jul 17: M.2 SATA expansion board in base, top board 05152021V2.6, M.2 board 12152020V1.6) + Argon USB 3.0 U-turn bridge | RUNNING (bridge + SSD disconnected until wipe) |
| **Transcend 128GB M.2 SATA SSD** (TS128GMTS830S, 02.2021 — corrected from "~500GB" Jul 17: label+listing+seller Kakao agree; df-h 469G reading no longer trusted) | seller's OS aboard, untrusted; seller password `qwert12#$5` or unset (Kakao Jul 18) — **wipe from inside boogiewoogie Jul 21, demote to clean storage** |
| Toshiba TransMemory 28.9GB USB | current boot drive (permanent-enough home; SD migration optional) |
| Samsung 16GB microSD | idle, untested (reader broke) |
| Keerda 5V/3A USB-C (KC-certified, 15W) | bench power — testing duty only, bare-minimum spec for Pi4+fan+SSD |
| RPi Camera (D) 5MP OV5647 + 16cm FFC · HC-SR501 ×2 · 점퍼 DC-40P F/F · 방열케이스 | Eleparts #2026071714203717563 — pickup 가산 ~Jul 21 |
| ElectroCookie 27W 5V/5A · SanDisk Ultra 32GB microSD | arrive Tue Jul 21 |
| micro SD reader | **BROKE Jul 18** — replace cheaply |

## Case & setup facts (Jul 17–18)
- Micro SD slot reachable from outside — no disassembly to flash.
- Jumper 1-2 DEFAULT / 2-3 ALWAYS-ON: set 2-3 at deployment week (blackout auto-recovery for the camera).
- M.2 board's only data path to the Pi = the USB bridge into blue USB3.
- Camera-ribbon routing = known weak point; fallback: Argon on desk, 방열케이스 on wall.
- Raspberry Pi Connect: declined (attack surface / same-network sufficiency / raw-SSH skill-building).
- Boot LED grammar: red steady = power ok · green flicker = disk activity.

## Deferred / v2
60cm camera cable at mounting time · IR-CUT night camera (45,310원) · SanDisk High Endurance (continuous video) · mmWave presence sensor (XenD101H) · Pi AI Camera · known_hosts path fix.

## Long-horizon references (filed, not assigned)
Manafish ROV (9–15 mo, robotics capstone) · rybtronics thermal drone (3–5 yr, custom PCB/SMD craft) · both ride the micro:bit→Arduino→ESP32 spine of roadmap months 3–6.