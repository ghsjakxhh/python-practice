# ledger.md — updated 2026-08-01 (evening), end of Session 29 (day 37)
# Complete Skycak artifact: STATE (Part A) + GRAPH (Part B) + HARDWARE (Part C).
# Supersedes the 2026-08-01 afternoon print AND the 2026-07-31 print.
# Covers Jul 31 evening + Aug 1 full day (days 36–37).
# ★ SESSION NUMBERING CONVENTION AMENDED (Aug 1, his design):
#   ONE session number per calendar day; multiple sits fold into it.
#   Aug 1 = S29 (Python review block + Linux block, three sits).
#   Historical Jul 31 = S27+S28 stands as an artifact of the old convention —
#   committed history is not renumbered. Rule applies Aug 1 forward.
# Node IDs (N1…) are file-internal shorthand only — full names in conversation.

═══════════════════════════════════════════════
# PART A — STATE
═══════════════════════════════════════════════

## ★ PROGRAM STRUCTURE
**CS (Python + Linux) = single-track steady state. Mathematics holds the primary daily slot.**
- One solid CS block per day — a floor and a steady-state, not a ceiling. ~31 days to summer break's end.
- Block selection rule: **the queue picks the block.** Due reviews/defenses first; frontier or production when nothing is due.
- **One session number per calendar day** (amended Aug 1). Extra sits by appetite fold into the day's session. The guarded failure mode remains CS eating the math slot — not observed; will be named if seen.
- **BURST MODE** (installed 2026-07-25, his design): a burst = one completed atom · indivisible work stays block-shaped · zero decision cost via the standing BURST MENU · atoms accumulate toward the day's block.
- **DAY COUNT, not streak.** Calendar days since June 26, zero days included. **Aug 1 = day 37.** Zero days on record: Jul 9, Jul 11, Jul 22, Jul 29 (4th).
- Optional cleanup, filed not assigned: `19th,July/item3.py` still says `streak`; file still streak_log.txt.

## ★ BURST MENU (current)
1. **Tally-dict cold rep, FRESH data** — promotes N72; minutes-sized
2. **Bandit 2→3** — next level; the remaining N49 cold rep rides on file-hiding levels. Twice queued, zero runs
3. **Container cold rep** — from blank, no notes: run any image with one published port + one mounted folder, verify in browser, destroy, recreate
4. **hack3 run** — day-count log (runs since Jul 19 unconfirmed)
(Pair-yielding consumed Jul 31. REP 2 permissions consumed Aug 1 — promoted.)

## Fluent (legacy — spot-check occasionally, don't drill)
N1 variables · N2 f-strings · N3 string methods · N6 lists · N7 for loops · N8 unpacking ·
N12 if/elif/else · N13 branch ordering · N15 while · N9–N11 dict cluster · N19 functions ·
N22 try/except · N5 Git · N30 with-frame

## Fluent (recent promotions)
| Node | Evidence | Next review |
|---|---|---|
| **N40 composition** | Jul 16 13:28 → Jul 19 9:47 → Jul 26 2nd defense 8:00/15:00 | 7→14d, **~Aug 9 — APPROACHING** |
| **N41 integrative ladder** | Jul 16 fail → Jul 17 +1:00 → Jul 19 5:40 → Jul 26 2nd defense 5:56/12:00 | 7→14d, **~Aug 9 — APPROACHING** |
| N36 record-keeper | S14 2:59; Jul 21/24/27 ⊇-ridden; Aug 1 ×2 — incl. first dict-walking variant | expanding |
| N35 count accumulator | S13; Jul 21; Aug 1 paid | expanding |
| N37 split-then-index-convert | S13; Jul 21; Jul 27 ⊇-ridden; Aug 1 paid | expanding |

- **Recurring minor flag:** double lookup / repeated computation (S24, Jul 27, Jul 31 double-split, Aug 1 triple-int pre-fix). Efficiency only. Watch, don't drill.

## produced-once
| Node | Evidence | Next |
|---|---|---|
| N24 except-as · N25 ladders · N26 .get() fallback | Jul 17 cold, Jul 19, Jul 26 ⊇-ridden; N23/N24 paid Aug 1 (narrow net, error object used); N26 paid Aug 1 in new costume (per-key seed) | expanding |
| N29 datetime pipeline | Jul 19 hack3 | rides item3.py reruns |
| N30w-"a" append | Jul 19 hack3 | rides composite builds |
| N34 gate pattern | S13–S16 + Jul 19 solo design; Aug 1 paid at the boundary (build-site gate) | rides composite builds |
| N59 list comprehensions | Jul 19 → Jul 20 composition-proven; Aug 1 paid — load-bearing, filtered, chain-in-recipe | expanding |
| N60 generators | Jul 21 both forms cold; Jul 24 + Jul 27; **Jul 31 PAID EARLY — pair-yielding cold rep** | 7→14d, **~Aug 14** |
| Pair-yielding sub-pattern | PROMOTED Jul 31: cold, blank, fresh data; probe discipline unprompted; conversion-in-recipe from draft 1 | rides N60 clock |
| **N50 permissions** | **PROMOTED Aug 1 — full both-directions cycle on boogiewoogie** (see S29 record). Lock step guided, unlock cold, one exact ten-character tag prediction HIT, first-match-wins absorbed by machine falsification | expanding |
| N44 navigation trio | Jul 17 cold; Bandit Jul 25; Jul 30; Aug 1 | rides Bandit |
| N47 cat + paths | Jul 17 cold; Bandit Jul 25; Jul 30 full ride | rides Bandit |
| N51 file operations | Jul 20 cold rep | expanding |
| N54 flash+headless | Jul 18 (guided) | one-time skill |
| N55 SSH | Jul 18 → Jul 24 → Jul 25 → Jul 28/30 solo → Jul 31 by hostname → **Aug 1: resolution flaked twice + one mid-session drop, ridden solo** | rides Bandit + Pi work |

## taught / needs evidence
- **N49 find/grep** — taught Jul 23; Aug 1 direct cold attempt CONVERTED TO GUIDED (leading-slash forgotten → retaught; grep seats guided). Strong contact rep banked. **Cold rep debt stands — NOW THE ONLY OPEN DEBT IN TIER L**
- **N72 tally-dict pattern** — taught + guided Aug 1. Build loop guided, report loop solo. Cold rep on fresh data promotes → burst #1
- **Narrow-net + `continue`** — taught Aug 1, not owed
- **N73 dict/set comprehensions** — set form met-in-the-wild Aug 1 (invented by analogy); dict form untaught, filed
- **N71 standard input** — taught Jul 30, met in the wild. Pipes/redirection downstream, untaught
- N27 error taxonomy — 17 species + Aug 1 order-swap variant (`except A as ValueError` → NameError during handling; two-traceback stack read)
- **Boundary discipline (candidate principle, not yet a node):** filter/convert ONCE at the edge. Three sightings Aug 1. Promote if it keeps earning

## ★ TIER D — CONTAINERS (opened Jul 31)
| Node | State |
|---|---|
| N62 client/daemon/socket model | taught. Socket is a file → the permissions tag is the law there too. **Group `docker` = root-equivalent** (convenience AND privilege-escalation path) |
| N63 images vs containers | produced (guided). One image, many containers = template/instance, OOP arriving early |
| N64 port mapping | PRODUCED, verified externally (`-p 8080:80`, page loaded from another machine) |
| N65 volume mapping | PRODUCED, verified live. **The mount is a live window, not a snapshot** |
| N66 container disposability | PRODUCED, controlled experiment (unmounted file died; mounted HTML survived) |
| N67 docker exec | produced (guided). Prompt-reading three machines deep |
| N68 compose | UNTAUGHT, deliberately gated on a second container |
| N69 shell scripting | taught only. Shebang · if/fi · case/esac · $() · set -e · set -x · `curl \| sh` hazard |
| N70 disks/partitions/mounting | taught, no production. One tree + mount points · sda/sda1 · Pi has no internal storage · `lsblk` unrun; SSD unwiped |

## PYTHON TIER STATUS: all core nodes production-evidenced · one taught-with-debt sub-pattern (N72 tally) · clocks expanding
- **N40/N41 second-defense clocks ~Aug 9** — next Python queue items
- **N60 ~Aug 14** (paid early Jul 31)
- Frontier: tally cold rep · Bandit levels · Telegram hack N52/N53 · nested comprehensions (filed) · dict comprehensions (filed)

## Linux nodes (Tier L)
| Node | State |
|---|---|
| N42/N43/N45/N48 | taught; ridden by every Bandit + Pi session |
| N44 · N47 · N51 · **N50** | **produced-once** |
| N46 paths | taught. **Leading-slash soft spot ×4** (Jul 20 ×2 · Jul 23 adjacent · Aug 1 forgotten outright, retaught). The slash is what MAKES it absolute. Fifth sighting → micro-drill offered, his call |
| N49 find/grep | taught + guided (Aug 1 guided rep banked). **Cold rep pending — Tier L's sole open debt** |
| N71 standard input | taught, met in the wild. Pipes/redirection downstream, untaught |

**N46/N49 knowledge added Aug 1 (guided rep + self-directed expansion):**
- **Glob needs raw material:** the shell only rewrites `*` when the standing room has a match; unmatched globs pass through as literal characters (discovered by contact)
- **Quoted `-name "*.py"` mechanism owned** — quotes stop the shell's rewrite so find receives the pattern
- **find echoes the road it was handed** (his own mid-flight repair: "Oh! full paths")
- **grep's three seats: grep · pattern · papers.** No starting-point slot; handed a room it answers "Is a directory"
- **grep output anatomy:** `filename:` prefix with multiple files; silence from a searched file IS the "no"
- **grep matches characters, not words** (`record` inside "Un**record**ed"); `-w` filed
- **Trailing slash in a typed address = grammar with no word after — ignored** (find/cd/ls/cat; rsync exception filed; slashless form is style, not law)
- **★ Per-component globbing — HIS DISCOVERY:** `/c/CS/*,July/*.py` — wildcards expand at every level; shell builds the crossproduct. Used for a fossil dig of every record-keeper since Jul 12
- Jul 30 addition stands (path's second job). Jul 31 addition stands (hostname vs IP)

**N50 knowledge added Aug 1 (REP 2 cycle):**
- **Regular file's type character is `-`, not `f`** — the convention marks special cases (d, l); the default goes unmarked
- **First-match-wins, absorbed by falsification:** owner match fires first and FINAL; group `rw-` two characters away is never consulted for the owner. Predicted against, machine enforced
- **The verbs are independent switches:** `-w-` = legal write into a file you cannot read
- **ls -l columns:** the number after the tag = link count (directory entries pointing at the file; ~always 1; says nothing about contents) · the number after ownership = **size in bytes**
- **Silence taxonomy, entry #2:** cat of an empty file = no output + prompt returned immediately (program finished, truthfully reporting emptiness) vs Jul 30's `cat -` hang (no output, NO prompt — waiting on you). **The prompt is the tell**

## Tier C — CYBER
| Item | State |
|---|---|
| Bandit gate | OPEN; production side cleared — **N50 now produced-once strengthens it** |
| Bandit level 0 · 0→1 | CLEARED Jul 25 |
| Bandit 1→2 | CLEARED Jul 30. Login as bandit2 still unconfirmed |
| **Bandit 2→3** | next; burst #2. Twice queued, zero runs |

- Port concept taught Jul 25; banner intel: `/etc/bandit_pass/`, per-user readability — the permissions tag system IS the game's spine, **and N50 is now produced against exactly that system**
- **Spoiler discipline:** passwords stay his; Claude verifies by report only. Passwords NOT in this file.
- **Password hygiene:** save at extraction; password file stays OUT of the committed repo
- `bandit0`/`bandit0` is public

## Gates
- Linux acquisition: OPEN · Bandit: OPEN and ENTERED · Containers: OPEN, three core ideas produced · Compose: gated on a second container

## Tier H — hardware/Pi
- **Camera project: still PAUSED** (Jul 20, his call). All V1 parts in hand.
- boogiewoogie in active use (container host + tonight's permissions lab); camera pause untouched
- N54/N55 produced · N52/N53/N56/N57/N58 untaught
- Filed ideas: Pi-hole · WireGuard · Jellyfin · Flask status dashboard

## ★ MEDIA SERVER PROJECT (opened Jul 31)
- Goal: movie library on boogiewoogie. Jellyfin = library + streaming; transcoding is the Pi 4's ceiling.
- **Blocked on storage, not skill:** SSD carries seller's untrusted OS — not wiped, not formatted, not mounted. Boot-order trap live: connect bridge while Pi runs; wipe promptly.
- **Declined, on record:** the dev-smurf stack (automated acquisition pipeline; ruling about the artifact, not the person; also a poor teacher — nine services at once).
- Filed as its good part: the Flask dashboard shape (opens N52/N53).

## ★ EXTERNAL SCHEDULE
**2026-2학기: 프로그래밍언어 (AAK10076-40), IT경영전공 교필 — JAVA.** 이충석 · 월 11:30–13:20 · 화 09:30–11:20 · D동401호 · 3학점.
- Weeks 4–10 = 객체지향 (the filed OOP block) · Weeks 1–3 = fluent tier in Java clothes · Weeks 11–12 = owned concepts, new grammar
- 발표 25% · 실습 (팀 10% + 팀프로젝트 25%) · 3인 1팀 · 출석 1/5 이상 결석 시 F
- Decision deferred: pre-study vs walk in cold

## Conduct rules (standing)
Timer to zero · mid-rep question voids · spec questions before clock free · no psychological commentary on motives/enthusiasm · predictions-first on shell runs (**commands are not calls** — a call must be committable enough to be wrong) · his self-report is the diagnosis · when memory holds no evidence, structural prediction IS the honest prediction · design authority over his own tools is his · traced-correct output disagreeing with spec gets flagged aloud (**binds both sides — fired Aug 1: ledger said locked, machine said default tag, machine won, rep re-specced on the evidence**) · a burst = one completed atom · defenses and new-idea acquisition never split · "I don't remember that session" changes nothing ·
**a prediction Claude has already spoiled is void — struck, not scored (covers any prior statement in the chat). THREE instances now: Jul 30 ls-count · Jul 31 curl · Aug 1 read-fail call** ·
**the level page is the spec** — superset, not recipe; walkthroughs never ·
**a forgotten fact gets retaught plainly, not dangled — rep converts cold→guided, honestly logged** ·
**★ one session number per calendar day; sits fold in (Aug 1, his design)**

## Repo hygiene & reconciliations
- hack3 = `19th,July/item3.py`. streak_log.txt honest as of Jul 19; runs since unconfirmed
- review.py (Jul 21) and practice1.py (Jul 27) retain his chosen imperfections
- `1st,August/` holds review1.py + review2.py — committed and pushed Aug 1
- CRLF/LF warnings on git add: ruled COSMETIC; proceed normally; `core.autocrlf` filed
- **RECORD CORRECTION (Aug 1): perms_test.txt was NOT locked.** Ledger carried "locked since Jul 24, unread"; `ls -l` showed the default `-rw-rw-r--`. Machine wins; no story invented about how. **Also: the file is 0 bytes — empty since creation.** Current state: unlocked, empty, mystery resolved (there was never anything inside)
- boogiewoogie home: `get-docker.sh` · `site/` · `perms_test.txt` (unlocked, empty)
- Bandit passwords: outside the committed repo

---

## Session record — Jul 31 evening (day 36, S28 under the old convention, BURST-ORIGIN)
**Mode: production — burst #1 by appetite after S27's close.**
Pair-yielding generator cold rep, fresh data (arcade scores): probe run (separate, swapped out before the build) → final run (seed-0 + empty-title record-keeper, if-guarded overwrite, fresh generator consumed once) → `galaga/5600` exact, first draft correct, conversion-in-recipe present from the start (the Jul 27 missing 10%, closed).
**Rulings:** pair-yielding → produced-once · N60 PAID three days early, 7→14d ~Aug 14 · double-split flag restated · CRLF ruled cosmetic · Bandit 2→3 queued, not entered (his report, logged plainly).
**By the day-metric:** surplus after a closed session, run honest.

---

## Session record — Aug 1 (day 37, S29, FULL BLOCK — one session, three sits)
**Mode: review (early payment — nothing due). Python ×2 builds · Linux REP 1 · Linux REP 2 (evening).**

### Python build 1 — review1.py (reading log, malformed wednesday)
- Draft 1: `type(int(...))` filter → ValueError. **You can't ask int() "would you crash?" without it crashing** — only askable inside a try.
- Pivot to `!= "n/a"`: output correct (4/156/thursday), requirement 2 unmet — a filter dodges one known specimen; a net survives any garbage.
- His question ("why did v1 feel better?") → shape-vs-robustness: v1 converted once at the boundary; v2 smeared conversion ×3 + whole-loop net (TypeError fee). **The virtues aren't in conflict: narrow the net.**
- Completion: comprehension splits · narrow try · `except ValueError as A` with the object used · `continue` taught. En route, solo: except-clause order swap (new species variant, two-traceback stack read) · `/0` caught · TypeError str-vs-int.
- Paid: N59 full weight · N35 · N36 · N37 · N23/N24 on completion. Silent-bug pattern again (draft-2 `total = 0` in the loop).

### Python build 2 — review2.py (workout tally)
- **His question — "is the tally novel?" — record checked: NOVEL. CLAUDE ERROR, logged:** spec framed an untaught composite as review. Converted to acquisition, no debt against him.
- Taught: **tally = seed-then-feed, seed per-key via `.get(key, 0)`** — the asymmetry working for you.
- Free find: accidental **set comprehension**, invented by analogy — deduplicating, hence exactly wrong for tallying. Met-in-the-wild; dict comprehensions filed.
- Production: build loop guided; **report loop solo** — first dict-walking record-keeper, gate correctly protecting both sum and contest.
- Flag → completion: `'rest'` was IN the tally (gated at read) → gate relocated to the build site, dead code deleted. Output exact: 8 sessions, run/4.
- Rulings: N72 → taught+guided, cold → burst #1 · N26 new costume · N34 at the boundary · N36 dict variant. **Boundary discipline: three sightings in one day — candidate filed.**

### Linux sit 1 — REP 1 (find/grep), attempted cold → CONVERTED GUIDED
- Commands-not-calls sendback (third instance); calls then committed.
- Contact series from one root — standing in `~`, addressing relatively: find echoed its literal string · per-argument complaints read · bare glob reached grep literally → **discovery: unmatched globs pass through**.
- "I forgot" on the leading slash → retaught plainly, cold surrendered. **Fourth sighting.**
- Repairs: absolute path + quoted `-name` (mechanism owned) · mid-flight self-repair ("full paths — find echoes the road") · one-per-line committed.
- find leg HIT as called. grep leg: two seat-confusions guided → Road 1 → HIT (review2.py + `tally[data]`); 4–5 vs 6 near miss (*his code grew past his mental model*); `filename:` prefix and silence-as-no by contact.
- Self-directed expansion: multi-room finds through a Korean-named path · trailing-slash grammar · **★ per-component glob discovery + fossil dig** · "Unrecorded" substring → characters-not-words; `-w` filed.
- **N49 cold debt stands.**

### Linux sit 2 (evening) — REP 2 (permissions, boogiewoogie) → **N50 PROMOTED**
- SSH: hostname resolution failed twice, one mid-session drop — ridden to a working session solo (N55 evidence).
- Opening tag call from memory: `f -wx r-x r-x` + ownership. Type MISS (**regular file = `-`, not `f`** — the convention marks special cases), owner/group MISS, others partial, ownership HIT.
- **Evidence-contradicts-record flag FIRED:** actual tag `-rw-rw-r--` — the default; the file was NOT locked, contra the ledger. Machine wins; record corrected; **rep re-specced to the full both-directions cycle** (a stronger N50 rep than the original spec).
- **Lock (guided):** `chmod r o-r` repaired via pointers — welded who·what·verb word; `o`=others; target required. His answer for the owner letter: `u`. Final `chmod u-r perms_test.txt`.
- **Tag call `--w-rw-r--` — EXACT TEN-CHARACTER HIT** (link count and size carried too).
- **Read attempt:** his call — success via group membership, mechanism stated. **Machine falsified it: Permission denied.** First-match-wins absorbed by contact: owner match fires first and FINAL; group never consulted. Shape call near-hit (anatomy right, words wrong). **STRIKE #3 ON CLAUDE:** the mechanism was stated before the call was requested → call void under the spoiled-prediction rule, struck, not scored. What survives the strike: he predicted against a stated mechanism and the machine itself settled it.
- `-w-` noted live: write-without-read is legal — the verbs are independent switches.
- **Unlock (cold, correct):** `chmod u+r`. Tag call `-rw-rw-r--` consistent — HIT by evidence.
- **Contents call:** "one line — the `1` is the giveaway" (flagged as assumption). **MISS, the season finale: the `0` was the giveaway — size in bytes. The file is EMPTY, and was since Jul 24.** cat performed a perfectly successful read of nothing. The `1` = link count (filed). **Silence taxonomy entry #2:** prompt-returned emptiness vs Jul 30's promptless stdin hang — the prompt is the tell.
- **Ruling: N50 → produced-once.** Lock guided, unlock cold, three tag reads, one exact prediction HIT, mechanism absorbed by falsification. **Tier L debt: N49 alone.**

**Convention amendment (his design, evening):** one session number per calendar day; sits fold in. S30 does not exist; this all is S29. Cost named once (Jul 31's S27+S28 stands as old-convention artifact); conceded.

**Claude errors this session:** tally spec error · spoiled-prediction strike #3.

**By the day-metric:** two Python builds, two shell reps, three sits; every wall worked to resolution; two honest cold→guided conversions and two promotions across two tracks. Dense, honest day.

---

## Next (queue-picked)
1. **Bandit 2→3** (burst #2) — N49's cold rep rides on file-hiding levels; a direct find/grep cold retry after a few days' gap is also legal
2. **Tally cold rep, fresh data** (burst #1) — promotes N72
3. **N40/N41 second-defense clocks ~Aug 9**
4. **N60 generators ~Aug 14**
5. **SSD: wipe → format → mount** — the media-server blocker; boot-order trap live
6. Second container → compose (N68) · Telegram hack / Flask dashboard (filed) · camera resumes on his word only

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
- N22 try/except ← N12 · N23 specific nets ← N22 · N24 except-as ← N23 · N25 ladders ← N23,N13 · N26 .get()/None ← N9,N11 · N27 taxonomy (17 species + Aug 1 order-swap variant) ← N22,N4

**Tier 3 — library & I/O**
- N28 import ← N1 · N29 datetime ← N28 · N30 file I/O ← N28,N2

**Tier 3 — composite patterns**
- N31 .split() · N32 .append() · N33 empty-tail · N34 gate · N35 count accumulator · N36 record-keeper (incl. dict-walking variant) · N37 split-index-convert · N38 if-guarded overwrite · N39 seed-then-feed
- N40 integrative composition — FLUENT, twice defended
- N41 integrative ladder — FLUENT, twice defended
- N59 comprehensions ← N7,N6,N34 · N60 generators ← N59,N7,N19 (pair-yielding sub-pattern PRODUCED Jul 31)
- N72 tally-dict (per-key seed-then-feed) ← N9,N10,N11,N26,N39 — taught + guided Aug 1, cold rep pending
- N73 dict/set comprehensions ← N59,N9 — set form met-in-the-wild Aug 1; dict form untaught, filed

**Tier L — Linux/shell**
- N42 shell/OS model · N43 cwd · N44 nav trio — produced · N45 home/~ · N46 paths (two jobs; leading-slash soft spot ×4) · N47 cat — produced · N48 prompt anatomy · N49 find/grep — taught+guided, **sole Tier L debt** · **N50 permissions — PRODUCED Aug 1 (both directions)** · N51 file ops — produced
- N71 standard input ← N42 — taught, met in the wild. Downstream untaught: pipes and redirection — Bandit's home turf
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
- N61 Bandit ← N44,N46,N47,N49,N50,N55,N71 — levels 0, 0→1, 1→2 cleared; the shell tier's review engine

**External block:** OOP ← N19,N21 — 2026-2학기 via Java (weeks 4–10). N63's template/instance is an early sighting

**Encompassing edges:**
- N61 Bandit ⊇ N55{1.0}, N44{1.0}, N46{0.9}, N47{1.0}, N48{0.8}, N49{0.8 *only when a level hides a file*}, N50{0.9}, N42{0.7}, N71{0.8 when a level touches stdin}
- N72 ⊇ N26{1.0}, N10{1.0}, N9{0.9}, N11{0.8}, N39{0.8}, N34{0.6 when gated at build} — best single dict-cluster review task once cold
- N50 ⊇ N48{0.4}, N42{0.5} — **now live credit** (production evidence exists)
- N71 ⊇ N42{0.6} · N46 ⊇ N43{0.8}
- N64 ⊇ port{1.0}, N48{0.4} · N65 ⊇ N46{0.9}, N70{0.7}, N44{0.5} · N66 ⊇ N65{0.8}, N63{1.0}
- N67 ⊇ N48{0.9}, N44{0.6}, N42{0.7} · N62 ⊇ N50{0.9}, N42{0.6} · N69 ⊇ N42{0.8}, N12/N13{0.6}, N19{0.5}
- (prior edges unchanged: N40, N41, N49, N60, N59, item3.py, N39, N38, N37, N36, N35, N33, N30, N29, N25, N17, N16, N8, N47, N44, N51, N55, N58)

**Graph-reading notes (Aug 1 evening):**
- **Tier L's debt column is one item long: N49.** Two collectors — file-hiding Bandit levels, or a direct cold retry after a few days' gap. When it clears, the entire shell tier is production-evidenced.
- **N50's promotion strengthens the Bandit position specifically:** the game's spine (`/etc/bandit_pass/` per-user readability) is now a produced skill, not a taught one.
- **The leading slash at four sightings** remains the tier's most reliable failure point. Fifth firing → micro-drill proposed, his call.
- **The dict cluster had its best day since S8–9.** One tally cold rep converts most of it to production evidence.
- **Python review pressure is low** — everything pushed to ~Aug 9 (defenses) and ~Aug 14 (N60). Frontier and Bandit have the floor.
- Boundary discipline stays a principle; it gets a node if it keeps being the shape of corrections.

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
| **boogiewoogie** (Pi 4B 4GB, Argon ONE M.2) | ALIVE. RPi OS Lite 64 (trixie), kernel 6.18.34. USB-boot (Toshiba 28.9GB), Wi-Fi jini, **192.168.0.9** — also `boogiewoogie` (IPv6 link-local; **resolution flaky Aug 1 — name failed twice, then worked; IP is the reliable fallback**). `ssh snakeyboy777@…`. Docker Engine 29.7.0 + compose v5.3.1, daemon enabled at boot. Images: hello-world, nginx. Home: get-docker.sh · site/ · perms_test.txt (**unlocked, empty — Aug 1 resolution**) |

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
SD slot external · jumper 2-3 = always-on (set at deployment) · M.2 data path = USB bridge only · ribbon routing = weak point · Pi Connect declined · LED grammar: red steady = power, green flicker = disk.
**Boot-order trap (open):** SSD and boot stick are both bootable USB devices. Connect the bridge while the Pi is running; wipe promptly.

## Deferred / v2
60cm cable · IR-CUT camera · High Endurance SD · mmWave sensor · Pi AI Camera · known_hosts Korean-path fix · docker group membership (declined — `sudo` per command).

## Filed ideas
Pi-hole · WireGuard VPN endpoint · Jellyfin · Flask status dashboard. All whisper-class.

## Long-horizon (filed)
Manafish ROV (9–15mo) · rybtronics thermal drone (3–5yr).