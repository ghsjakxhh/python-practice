# ledger.md — updated 2026-08-08, end of Session 32 (day 44)
# Complete Skycak artifact: STATE (Part A) + GRAPH (Part B) + HARDWARE (Part C).
# Supersedes the 2026-08-01 evening print.
# Covers Aug 3 (S30), Aug 4 (S31), Aug 8 (S32) — days 39, 40, 44.
# ★ SESSION NUMBERING CONVENTION (Aug 1, his design):
#   ONE session number per calendar day; multiple sits fold into it.
#   Historical Jul 31 = S27+S28 stands as an artifact of the old convention —
#   committed history is not renumbered.
# ★ RECORD CORRECTION (Aug 8): the ~Aug 9 N40/N41 clocks were labeled
#   "second-defense" in the queue while the evidence rows already showed
#   Jul 26 as the 2nd defense. Aug 8 was therefore the THIRD defense for both.
#   Mislabel had been copied forward three prints. Corrected at source.
# Node IDs (N1…) are file-internal shorthand only — full names in conversation.

═══════════════════════════════════════════════
# PART A — STATE
═══════════════════════════════════════════════

## ★ PROGRAM STRUCTURE
**CS (Python + Linux) = single-track steady state. Mathematics holds the primary daily slot.**
- One solid CS block per day — a floor and a steady-state, not a ceiling.
- Block selection rule: **the queue picks the block.** Due reviews/defenses first; frontier or production when nothing is due.
- **One session number per calendar day.** Extra sits by appetite fold into the day's session.
- **BURST MODE** (installed 2026-07-25, his design): a burst = one completed atom · indivisible work stays block-shaped · zero decision cost via the standing BURST MENU · atoms accumulate toward the day's block.
- **PARTIAL BLOCK is a real ledger category** (established Aug 3): a non-zero day carrying one atom is logged as a partial block, not a full session. One atom ≠ one block, by burst mode's own definition.
- **DAY COUNT, not streak.** Calendar days since June 26, zero days included. **Aug 8 = day 44.**
  Zero days on record (8): Jul 9 · Jul 11 · Jul 22 · Jul 29 · **Aug 2 · Aug 5 · Aug 6 · Aug 7**.
- **Prioritization rule (named Aug 8):** when a debt and a clocked item compete, the clocked item wins.
  Debts have no expiry and can improve with age; spacing clocks overrun into re-establishment.
  Convenience arguments ("setup's already written," "milestone value") do not outrank an expiry date.
- Optional cleanup, filed not assigned: `19th,July/item3.py` still says `streak`; file still streak_log.txt.

## ★ BURST MENU (current)
1. **N49 find/grep cold retry** — spec written Aug 4, setup aborted on a paste fault, never run. Closes Tier L's last debt. Atom-sized (12:00 cap)
2. **Container cold rep** — from blank, no notes: run any image with one published port + one mounted folder, verify in browser, destroy, recreate
3. **Bandit 3→4** — next level
4. **hack3 run** — day-count log (runs since Jul 19 unconfirmed)
(Pair-yielding consumed Jul 31 · REP 2 permissions consumed Aug 1 · **tally consumed Aug 3 — promoted** · **Bandit 2→3 consumed Aug 4 — cleared**.)

## Fluent (legacy — spot-check occasionally, don't drill)
N1 variables · N2 f-strings · N3 string methods · N6 lists · N7 for loops · N8 unpacking ·
N12 if/elif/else · N13 branch ordering · N15 while · N9–N11 dict cluster · N19 functions ·
N22 try/except · N5 Git · N30 with-frame

## Fluent (recent promotions)
| Node | Evidence | Next review |
|---|---|---|
| **N40 composition** | Jul 16 13:28 → Jul 19 9:47 → Jul 26 2nd def 8:00/15:00 → **Aug 8 3rd def 12:27/15:00 PASS** | 14→21d, **~Aug 29** |
| **N41 integrative ladder** | Jul 16 fail → Jul 17 +1:00 → Jul 19 5:40 → Jul 26 2nd def 5:56/12:00 → **Aug 8 3rd def 5:44/12:00 PASS — PERSONAL BEST** | 14→21d, **~Aug 29** |
| N36 record-keeper | S14 2:59; Jul 21/24/27 ⊇-ridden; Aug 1 ×2 incl. dict-walking variant; Aug 8 ×2 (both defenses) | expanding |
| N35 count accumulator | S13; Jul 21; Aug 1; Aug 8 ×2 | expanding |
| N37 split-then-index-convert | S13; Jul 21; Jul 27 ⊇-ridden; Aug 1; Aug 8 | expanding |

- **★ Recurring minor flag — double lookup / repeated computation. FIFTH SIGHTING Aug 8** (S24 · Jul 27 · Jul 31 double-split · Aug 1 triple-int · **Aug 8: `line.split(" ")` computed five times per line plus one discarded bare call**). Now the most consistent pattern in his code. Efficiency only. Watch, don't drill — but if a sixth lands, offer the micro-drill.

## produced-once
| Node | Evidence | Next |
|---|---|---|
| N24 except-as · N25 ladders · N26 .get() fallback | Jul 17 cold, Jul 19, Jul 26 ⊇-ridden; N23/N24 paid Aug 1; N26 paid Aug 1 (per-key seed) + Aug 3 (tally cold) + Aug 8 (quiet lookup, honest fallback) | expanding |
| N29 datetime pipeline | Jul 19 hack3 | rides item3.py reruns |
| N30 w-"a" append | Jul 19 hack3 | rides composite builds |
| N34 gate pattern | S13–S16 + Jul 19 solo; Aug 1 at the boundary; Aug 8 (trail gate) | rides composite builds |
| N59 list comprehensions | Jul 19 → Jul 20 composition-proven; Aug 1 paid — load-bearing, filtered, chain-in-recipe | expanding |
| N60 generators | Jul 21 both forms cold; Jul 24 + Jul 27; Jul 31 PAID EARLY — pair-yielding cold rep | 14d, **~Aug 14 — APPROACHING** |
| Pair-yielding sub-pattern | PROMOTED Jul 31 | rides N60 clock |
| **N72 tally-dict** | **PROMOTED Aug 3 (S30)** — cold rep, fresh data (bird sightings). Build loop + report loop both solo. `tally.get(animal, 0) + 1` produced with no scaffold; counts exact | expanding |
| **N50 permissions** | PROMOTED Aug 1 — full both-directions cycle on boogiewoogie | expanding |
| N44 navigation trio | Jul 17 cold; Bandit Jul 25; Jul 30; Aug 1; **Bandit Aug 4** | rides Bandit |
| N47 cat + paths | Jul 17 cold; Bandit Jul 25; Jul 30 full ride; **Bandit Aug 4 — the level was a cat-argument problem end to end** | rides Bandit |
| N51 file operations | Jul 20 cold rep | expanding |
| N54 flash+headless | Jul 18 (guided) | one-time skill |
| N55 SSH | Jul 18 → Jul 24 → Jul 25 → Jul 28/30 solo → Jul 31 by hostname → Aug 1 flaky, ridden solo → **Aug 4 clean login to Bandit** | rides Bandit + Pi work |

## taught / needs evidence
- **N49 find/grep** — taught Jul 23; Aug 1 cold attempt CONVERTED TO GUIDED. **Cold rep re-spec'd Aug 4; setup aborted on a paste fault, rep never ran. Cold debt stands — STILL THE ONLY OPEN DEBT IN TIER L**
- **Bare `--` as end-of-flags marker** — met Aug 4 via cat's own hint line (`to pass '--spaces' as a value, use '-- --spaces'`). Read, understood, **not produced** — the solve used `./` + quotes instead. Filed
- **Narrow-net + `continue`** — taught Aug 1, not owed
- **N73 dict/set comprehensions** — set form met-in-the-wild Aug 1; dict form untaught, filed
- **N71 standard input** — taught Jul 30, met in the wild. Pipes/redirection downstream, untaught
- N27 error taxonomy — 17 species + Aug 1 order-swap variant. **Aug 8: `int()` on `"8.2"` → ValueError, met and repaired inside the timer (float), no new species**
- **Boundary discipline (candidate principle, not yet a node):** filter/convert ONCE at the edge. Three sightings Aug 1. Aug 8's five-splits-per-line is the same family in efficiency clothes. Promote if it keeps earning
- **★ "The shell rewrites before the program sees anything" (candidate principle, not yet a node):** THREE sightings — glob expansion (Aug 1) · quoted `-name` pattern (Aug 1) · **argument splitting on spaces (Aug 4)**. Same mechanism, three costumes. Promote if it keeps earning

## ★ TIER D — CONTAINERS (opened Jul 31)
| Node | State |
|---|---|
| N62 client/daemon/socket model | taught. Socket is a file → the permissions tag is the law there too. **Group `docker` = root-equivalent** |
| N63 images vs containers | produced (guided). Template/instance = OOP arriving early |
| N64 port mapping | PRODUCED, verified externally (`-p 8080:80`) |
| N65 volume mapping | PRODUCED, verified live. **The mount is a live window, not a snapshot** |
| N66 container disposability | PRODUCED, controlled experiment |
| N67 docker exec | produced (guided). Prompt-reading three machines deep |
| N68 compose | UNTAUGHT, deliberately gated on a second container |
| N69 shell scripting | taught only. Shebang · if/fi · case/esac · $() · set -e · set -x · `curl \| sh` hazard |
| N70 disks/partitions/mounting | taught, no production. `lsblk` unrun; SSD unwiped |

## PYTHON TIER STATUS: all core nodes production-evidenced · clocks pushed out
- **N40/N41 next defenses ~Aug 29** — three weeks of Python review slack
- **N60 ~Aug 14** — the only Python clock in the near field
- Frontier: dict comprehensions (filed) · nested comprehensions (filed) · Telegram hack N52/N53

## Linux nodes (Tier L)
| Node | State |
|---|---|
| N42/N43/N45/N48 | taught; ridden by every Bandit + Pi session |
| N44 · N47 · N51 · N50 | produced-once |
| N46 paths | taught. **Leading-slash soft spot ×4** (Jul 20 ×2 · Jul 23 adjacent · Aug 1 forgotten outright). Fifth sighting → micro-drill offered, his call |
| N49 find/grep | taught + guided. **Cold rep pending — Tier L's sole open debt** |
| N71 standard input | taught, met in the wild |

**N46/N49 knowledge (Aug 1, unchanged):**
- **Glob needs raw material:** unmatched globs pass through as literal characters
- **Quoted `-name "*.py"` mechanism owned** — quotes stop the shell's rewrite
- **find echoes the road it was handed**
- **grep's three seats: grep · pattern · papers.** No starting-point slot
- **grep output anatomy:** `filename:` prefix with multiple files; silence from a searched file IS the "no"
- **grep matches characters, not words**; `-w` filed
- Trailing slash in a typed address = grammar with no word after — ignored
- **★ Per-component globbing — HIS DISCOVERY:** `/c/CS/*,July/*.py`

**N47/N61 knowledge added Aug 4 (Bandit 2→3):**
- **★ A leading `--` marks a FLAG, and flags are read before filenames.** cat rejected `--spaces` and exited before `in`, `this`, `filename--` were ever considered — which is why the four "no such file" errors he predicted never appeared. Falsified cleanly by the machine
- **`./` and quoting solve two DIFFERENT problems** — dashes vs spaces. Neither substitutes for the other. `./--spaces` fixes the flag read and leaves the split untouched
- **`--` bare = end-of-flags marker** (from cat's hint line). Taught, unproduced
- **The shell splits on spaces before the program sees anything** — one filename became four arguments; none of them was the file

**N50 knowledge (Aug 1, unchanged):**
- **Regular file's type character is `-`, not `f`**
- **First-match-wins:** owner match fires first and FINAL
- **The verbs are independent switches:** `-w-` = legal write into a file you cannot read
- **ls -l columns:** link count after the tag; **size in bytes** after ownership
- **Silence taxonomy #2:** cat of an empty file = no output + prompt returned, vs Jul 30's `cat -` hang (no prompt). **The prompt is the tell**

## Tier C — CYBER
| Item | State |
|---|---|
| Bandit gate | OPEN; production side cleared |
| Bandit level 0 · 0→1 | CLEARED Jul 25 |
| Bandit 1→2 | CLEARED Jul 30 |
| **Bandit 2→3** | **CLEARED Aug 4 (guided).** Login as bandit2 confirmed |
| **Bandit 3→4** | next |

- **Assist accounting, 2→3:** Claude supplied the flags-before-filenames fact and pointed at quoting; the four-argument split diagnosis and the final composition (`cat ./"--spaces in this filename--"`) were his. Rides as production evidence, not a cold clear
- **The level did NOT collect the N49 debt** — the file was hidden in plain sight, no `find` required. Future file-hiding levels remain a legal collector
- Port concept taught Jul 25; banner intel: `/etc/bandit_pass/`, per-user readability
- **Spoiler discipline:** passwords stay his; Claude verifies by report only. Passwords NOT in this file
- `bandit0`/`bandit0` is public

## Gates
- Linux acquisition: OPEN · Bandit: OPEN and ENTERED, 4 levels cleared · Containers: OPEN, three core ideas produced · Compose: gated on a second container

## Tier H — hardware/Pi
- **Camera project: still PAUSED** (Jul 20, his call). All V1 parts in hand
- N54/N55 produced · N52/N53/N56/N57/N58 untaught
- Filed ideas: Pi-hole · WireGuard · Jellyfin · Flask status dashboard

## ★ MEDIA SERVER PROJECT (opened Jul 31)
- Goal: movie library on boogiewoogie. Jellyfin = library + streaming; transcoding is the Pi 4's ceiling
- **Blocked on storage, not skill:** SSD carries seller's untrusted OS — not wiped, not formatted, not mounted. Boot-order trap live: connect bridge while Pi runs; wipe promptly
- **Declined, on record:** the dev-smurf stack (ruling about the artifact, not the person; also a poor teacher)
- Filed as its good part: the Flask dashboard shape (opens N52/N53)

## ★ EXTERNAL SCHEDULE
**2026-2학기: 프로그래밍언어 (AAK10076-40), IT경영전공 교필 — JAVA.** 이충석 · 월 11:30–13:20 · 화 09:30–11:20 · D동401호 · 3학점.
- Weeks 4–10 = 객체지향 (the filed OOP block) · Weeks 1–3 = fluent tier in Java clothes · Weeks 11–12 = owned concepts, new grammar
- 발표 25% · 실습 (팀 10% + 팀프로젝트 25%) · 3인 1팀 · 출석 1/5 이상 결석 시 F
- Decision deferred: pre-study vs walk in cold

## Conduct rules (standing)
Timer to zero · mid-rep question voids · spec questions before clock free · no psychological commentary on motives/enthusiasm · predictions-first on shell runs (**commands are not calls**) · his self-report is the diagnosis · when memory holds no evidence, structural prediction IS the honest prediction · design authority over his own tools is his · traced-correct output disagreeing with spec gets flagged aloud (**binds both sides**) · a burst = one completed atom · defenses and new-idea acquisition never split · "I don't remember that session" changes nothing ·
**a prediction Claude has already spoiled is void — struck, not scored. THREE instances: Jul 30 ls-count · Jul 31 curl · Aug 1 read-fail call** ·
**the level page is the spec** — superset, not recipe; walkthroughs never ·
**a forgotten fact gets retaught plainly, not dangled — rep converts cold→guided, honestly logged** ·
**one session number per calendar day; sits fold in** ·
**★ a deliberate design choice, stated as such, is logged as intentional and not second-guessed** (Aug 8: the `>=` tie rule) ·
**★ look-don't-recall binds Claude — dates, node states, and clock arithmetic come from reading the file** (fired Aug 8: caught the second/third-defense mislabel by reading)

## Repo hygiene & reconciliations
- hack3 = `19th,July/item3.py`. streak_log.txt honest as of Jul 19; runs since unconfirmed
- review.py (Jul 21) and practice1.py (Jul 27) retain his chosen imperfections
- `1st,August/` holds review1.py + review2.py — committed Aug 1
- **`3rd,August/` holds review1.py** (tally cold rep) · **`8th,August/` holds defense.py + defense2.py**
- CRLF/LF warnings on git add: ruled COSMETIC; `core.autocrlf` filed
- **Tooling fact (Aug 4):** Git Bash paste = right-click or Shift+Insert; Ctrl+V does not work. A paste carrying an invisible character (`$'\302\226'`) killed the first command and cascaded every dependent line — read the FIRST error, not the last
- RECORD CORRECTION (Aug 1): perms_test.txt was never locked and is 0 bytes. Machine won
- boogiewoogie home: `get-docker.sh` · `site/` · `perms_test.txt` (unlocked, empty)
- Bandit passwords: outside the committed repo

---

## Session record — Aug 3 (day 39, S30, PARTIAL BLOCK)
**One atom: N72 tally-dict cold rep, fresh data (bird sightings).**
- Build loop `tally[animal] = tally.get(animal, 0) + 1` produced cold, no scaffold. Counts exact (`magpie 4, cat 2, pigeon 2, heron 1`), verified against a hand trace
- Two distinct loops as specified. Report loop's first version printed bare values; **caught against the spec and repaired solo** — cold debugging, not a violation
- `print(tally)` checkpoint before writing the report loop — look-don't-recall applied to his own program state, third sighting of that instinct
- **Spec deviation flagged aloud:** spec said `magpie: 4`, output was `magpie:4`. Verdict gate didn't include format → ungated, Claude's to have specced tighter
- **Timer irregularity, logged honestly:** clock started after the build loop existed; only the report portion (2:52) measured. Cold criterion met throughout; cap 10:00 never in danger
- **RULING: N72 → produced-once.** ⊇ credit now LIVE for N26, N10, N9, N11, N39
- **Ruled a partial block, not a full session** — his standard, applied against a generous reading. Bandit 2→3 offered as a second atom, declined

---

## Session record — Aug 4 (day 40, S31, PARTIAL BLOCK)
**One atom: Bandit 2→3, CLEARED (guided).**
- `ls` prediction HIT — file renders as `--spaces in this filename--`
- First cat attempt: predicted four "no such file" errors. **Machine gave one flag-rejection and an early exit.** Clean falsification, absorbed without argument. Claude prompted the missing fourth-argument call before the run; the amendment was his
- `./` recalled cold from level 1→2, unprompted, no lookup. Right tool, half the problem
- Under one prompt he produced the four-argument split himself and stated that none of them names the file — **that's the diagnosis, and he made it**
- Claude named quoting by pointing at his own find work; the composition `cat ./"--spaces in this filename--"` was his. Password extracted
- **N48 minor:** called the PuTTY session "Git Bash" mid-level. First sighting, noted only
- **N49 cold retry spec'd as the second atom.** Setup block pasted → invisible character killed `mkdir`, whole tree failed to build. Hand-typed retry issued; **rep never ran.** Day closed here
- **Bandit avoidance counter closed:** three times queued, one run

---

## Session record — Aug 8 (day 44, S32, FULL BLOCK)
**Mode: review. Both integrative defenses, third time, cold.**

### Pre-session ruling — prioritization
Debt (N49) vs clocked items (N40/N41, due ~Aug 9) competed. Claude's first recommendation put the debt first; **reversed on his question.** Reasoning that survived: a debt cannot decay and had already improved with age; a spacing clock that overruns costs a real measurement. The counterargument (13 days vs 14 under-tests the interval) was named and ruled noise. Convenience arguments were named as the weak part of the original call.

### Defense 1 — N40 composition, THIRD defense: **PASS, 12:27/15:00**
Fresh domain (trail-running log). Output `4 / 39.5 / 2026-03-09`, verified against a hand trace.
- File written from Python (`"w"`), read back in a separate frame — the mode-is-a-contract model held cold
- `int("8.2")` → ValueError met and repaired to `float()` inside the timer, solo
- Date printed as `2026-03-04:` — **trailing colon caught and chained off solo** (`.split(":")[0]`), unprompted
- **Tie at 12.6 handled deliberately:** `>` → `>=`, keeping the most recent record. Stated reason: "it just makes more sense to me." Logged as intentional design, not second-guessed
- **N33 empty-tail unexercised** — his write string carried no trailing newline, so `lines` had no empty final element. Spec artifact, not a fault; ⊇ credit adjusted accordingly
- **Double-lookup, fifth sighting:** `line.split(" ")` computed five times per line, plus a bare discarded call on line 15

### Defense 2 — N41 integrative ladder, THIRD defense: **PASS, 5:44/12:00 — PERSONAL BEST**
Fresh domain (shipping costs by city). Output: culprit line naming `'jeju'`, total `14700`, honest fallback line.
1. **Loud net via the caught object** — `except KeyError as A:` with `{A}` printing `'jeju'` quotes-on. This was Jul 16's exact gap; third clean showing
2. **Ladder** — KeyError first, `except Exception as B` last, silent on the healthy run
3. **Total structurally correct** — accumulator inside the try, after the lookup. Jul 16's failure inverted: the try's jump makes a missing key structurally incapable of contaminating the sum. Built unprompted
4. **Quiet lookup** — `.get()` with a non-impersonating fallback, return wrapped in print
- Line 8's bare `shipping[request]` flagged as either a deliberate explicit-trigger or a vestigial line; **left open for his ruling**

### Rulings
- **N40 → third defense PASSED, 14→21d, next ~Aug 29**
- **N41 → third defense PASSED, 14→21d, next ~Aug 29**
- ⊇ paid: N30, N31, N34, N35, N36, N37, N4, N7, N12 (via N40) · N9, N10, N35, N36, N12/N13, N25, N34 (via N41)
- **Ledger correction issued** (second → third defense mislabel), caught by reading rather than recalling
- N49 offered as a third atom, declined. Session closed at two defenses

**By the day-metric:** first full block since Aug 1. Both defenses cold, both under cap, one a personal best, every repair inside the timer made solo.

---

## Next (queue-picked)
1. **N60 generators ~Aug 14** — the only clock in the near field
2. **N49 find/grep cold retry** — spec written, setup pending; closes Tier L's last debt
3. **Bandit 3→4**
4. **N40/N41 fourth defenses ~Aug 29**
5. **SSD: wipe → format → mount** — the media-server blocker; boot-order trap live
6. Second container → compose (N68) · dict comprehensions · Telegram hack / Flask dashboard (filed) · camera resumes on his word only

═══════════════════════════════════════════════
# PART B — THE KNOWLEDGE GRAPH (structure)
═══════════════════════════════════════════════
`←` = prerequisite. `⊇` = encompasses, weight {1.0 full … 0.3 partial}.

**Tier 0 — substrate**
- N1 variables · N2 f-strings ← N1 · N3 string methods ← N2 · N4 int()/float() ← N1 · N5 Git

**Tier 1 — containers & iteration**
- N6 lists ← N1 · N7 for loops ← N6 · N8 enumerate/unpacking ← N7,N6 · N9 dict access ← N1,N2 · N10 read-modify-write ← N9 · N11 create-vs-read asymmetry ← N9

**Tier 1 — control flow**
- N12 if/elif/else ← N1 · N13 branch ordering ← N12 · N14 boundaries ← N12 · N15 while ← N12 · N16 count-up ← N15,N7 · N17 while+if ← N15,N12 · N18 loop var outlives ← N7,N15

**Tier 2 — functions**
- N19 def/return ← N1 · N20 round() ← N19,N4 · N21 substitution model ← N19

**Tier 2 — errors & robustness**
- N22 try/except ← N12 · N23 specific nets ← N22 · N24 except-as ← N23 · N25 ladders ← N23,N13 · N26 .get()/None ← N9,N11 · N27 taxonomy (17 species + order-swap variant) ← N22,N4

**Tier 3 — library & I/O**
- N28 import ← N1 · N29 datetime ← N28 · N30 file I/O ← N28,N2

**Tier 3 — composite patterns**
- N31 .split() · N32 .append() · N33 empty-tail · N34 gate · N35 count accumulator · N36 record-keeper (incl. dict-walking variant) · N37 split-index-convert · N38 if-guarded overwrite · N39 seed-then-feed
- N40 integrative composition — FLUENT, **three times defended**
- N41 integrative ladder — FLUENT, **three times defended**
- N59 comprehensions ← N7,N6,N34 · N60 generators ← N59,N7,N19 (pair-yielding sub-pattern PRODUCED Jul 31)
- **N72 tally-dict (per-key seed-then-feed) ← N9,N10,N11,N26,N39 — PRODUCED-ONCE Aug 3**
- N73 dict/set comprehensions ← N59,N9 — set form met-in-the-wild Aug 1; dict form untaught, filed

**Tier L — Linux/shell**
- N42 shell/OS model · N43 cwd · N44 nav trio — produced · N45 home/~ · N46 paths (two jobs; leading-slash soft spot ×4) · N47 cat — produced, **argument-parsing knowledge added Aug 4** · N48 prompt anatomy · N49 find/grep — taught+guided, **sole Tier L debt** · N50 permissions — PRODUCED · N51 file ops — produced
- N71 standard input ← N42 — taught, met in the wild. Downstream untaught: pipes and redirection
- N69 shell scripting ← N42,N44 — taught · N70 disks/partitions/mounting ← N43,N46 — taught, no production

**Tier D — containers**
- N62 client/daemon/socket ← N42,N50 — taught
- N63 images vs containers ← N62 — produced (guided)
- N64 port mapping ← N63, port concept — PRODUCED
- N65 volume mapping ← N63,N46,N70 — PRODUCED
- N66 disposability/persistence ← N63,N65 — PRODUCED
- N67 docker exec ← N63,N48 — produced (guided)
- N68 compose ← N64,N65,N66 + YAML — UNTAUGHT, gated on a second container
- Downstream: container networking · PUID/PGID ← N50 · secrets/.env · reverse proxy + TLS ← N64

**Tier H — hardware/Pi**
- N52 pip · N53 HTTP/requests · N54 flash — produced · N55 SSH — produced · N56 GPIO/PIR · N57 camera · N58 THE MACHINE
- Jellyfin ← N64,N65,N70 — storage is the only real blocker

**Tier C — cyber**
- N61 Bandit ← N44,N46,N47,N49,N50,N55,N71 — **levels 0, 0→1, 1→2, 2→3 cleared**; the shell tier's review engine

**External block:** OOP ← N19,N21 — 2026-2학기 via Java (weeks 4–10). N63's template/instance is an early sighting

**Encompassing edges:**
- N40 ⊇ N30{0.8}, N31{1.0}, N33{1.0 *only when the data carries a trailing newline*}, N34{1.0}, N35{1.0}, N36{0.8}, N37{1.0}, N4{0.7}, N7{1.0}, N12{0.8}
- N41 ⊇ N9{1.0}, N10{1.0}, N7{1.0}, N35{0.8}, N36{0.7}, N12/N13{0.7}, N25{0.5}, N34{0.6} — best task for the error-handling cluster
- N61 Bandit ⊇ N55{1.0}, N44{1.0}, N46{0.9}, N47{1.0}, N48{0.8}, N49{0.8 *only when a level hides a file*}, N50{0.9}, N42{0.7}, N71{0.8 when a level touches stdin}
- **N72 ⊇ N26{1.0}, N10{1.0}, N9{0.9}, N11{0.8}, N39{0.8}, N34{0.6 when gated at build} — LIVE CREDIT since Aug 3**
- N50 ⊇ N48{0.4}, N42{0.5} — live credit
- N71 ⊇ N42{0.6} · N46 ⊇ N43{0.8}
- N64 ⊇ port{1.0}, N48{0.4} · N65 ⊇ N46{0.9}, N70{0.7}, N44{0.5} · N66 ⊇ N65{0.8}, N63{1.0}
- N67 ⊇ N48{0.9}, N44{0.6}, N42{0.7} · N62 ⊇ N50{0.9}, N42{0.6} · N69 ⊇ N42{0.8}, N12/N13{0.6}, N19{0.5}
- N39 ⊇ N35{1.0}, N36{0.6}, N7{1.0}, N1{0.7} · N38 ⊇ N12{1.0}, N36{0.8}, N10{0.6} · N37 ⊇ N31{1.0}, N6{1.0}, N4{0.4} · N36 ⊇ N7{1.0}, N12{0.8}, N1{0.6} · N35 ⊇ N7{1.0}, N1{0.7} · N33 ⊇ N31{0.8}, N14{0.5} · N30 ⊇ N28{0.5}, N2{0.4} · N29 ⊇ N28{0.5}, N4{0.3} · N25 ⊇ N23{1.0}, N13{0.8} · N17 ⊇ N15{1.0}, N12{1.0} · N16 ⊇ N15{1.0}, N7{0.7} · N8 ⊇ N7{1.0}, N6{0.8}

**Graph-reading notes (Aug 8 evening):**
- **The dict cluster is fully production-evidenced.** N72's promotion lit N26/N10/N9/N11/N39 in one rep — the cluster's best day since S8–9 finally paid off
- **Tier L's debt column is still one item long: N49.** Bandit 2→3 rode N44/N46/N47/N48/N55 at full weight but did NOT collect N49 — no file-hiding. Two collectors remain: a later Bandit level, or the direct cold retry already spec'd
- **Python review pressure is at its lowest of the program.** Both integrative defenses pushed to ~Aug 29; only N60 (~Aug 14) sits in the near field. The frontier and the shell tier have a clear three-week runway
- **The leading slash holds at four sightings** — no fifth. Micro-drill still unoffered by rule
- **Two candidate principles are now competing for promotion:** boundary discipline (3 sightings) and shell-rewrites-first (3 sightings). Neither is a node yet. The double-lookup flag at five sightings may be the same animal as the first one wearing efficiency clothes — worth watching whether they converge
- **N33's edge got a condition attached** — a composition only exercises empty-tail handling if the data actually has one. Weight was overclaiming before

═══════════════════════════════════════════════
# PART C — HARDWARE LOG
═══════════════════════════════════════════════

## The declared machine
**Pi-based home security camera.** V1: motion (PIR) → photo → Telegram alert → event log. TRACK PAUSED Jul 20, his call; resumes on his word.

## Second project (Jul 31)
**Jellyfin media server on boogiewoogie.** Blocked only on storage. Container skills in place.

## Live systems
| Machine | State |
|---|---|
| **boogiewoogie** (Pi 4B 4GB, Argon ONE M.2) | ALIVE. RPi OS Lite 64 (trixie), kernel 6.18.34. USB-boot (Toshiba 28.9GB), Wi-Fi jini, **192.168.0.9** — also `boogiewoogie` (IPv6 link-local; resolution flaky Aug 1; IP is the reliable fallback). `ssh snakeyboy777@…`. Docker Engine 29.7.0 + compose v5.3.1, daemon enabled at boot. Images: hello-world, nginx. Home: get-docker.sh · site/ · perms_test.txt (unlocked, empty). **No sessions since Aug 1** |

## Inventory
| Item | Status |
|---|---|
| Pi 4 4GB + Argon ONE M.2 + USB bridge | running (bridge + SSD still disconnected) |
| Transcend 128GB M.2 SSD | seller's OS aboard, untrusted; **wipe deferred — the media-server blocker** |
| Toshiba 28.9GB USB | boot drive (`/dev/sda`: sda1→/boot/firmware, sda2→/) |
| Samsung 16GB microSD | idle, untested |
| Keerda 5V/3A | bench power, testing only |
| RPi Camera (D) 5MP OV5647 + FFC · HC-SR501 ×2 · DC-40P jumpers · 방열케이스 | IN HAND |
| ElectroCookie 27W · SanDisk 32GB | delivery status unlogged since pause |
| micro SD reader | broke Jul 18; replace cheaply |

## Case & setup facts
SD slot external · jumper 2-3 = always-on · M.2 data path = USB bridge only · ribbon routing = weak point · Pi Connect declined · LED grammar: red steady = power, green flicker = disk.
**Boot-order trap (open):** SSD and boot stick are both bootable USB devices. Connect the bridge while the Pi is running; wipe promptly.

## Deferred / v2
60cm cable · IR-CUT camera · High Endurance SD · mmWave sensor · Pi AI Camera · known_hosts Korean-path fix · docker group membership (declined — `sudo` per command).

## Filed ideas
Pi-hole · WireGuard VPN endpoint · Jellyfin · Flask status dashboard. All whisper-class.

## Long-horizon (filed)
Manafish ROV (9–15mo) · rybtronics thermal drone (3–5yr).