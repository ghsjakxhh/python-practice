# ledger.md — updated 2026-08-01, end of Session 29 (day 37)
# Complete Skycak artifact: STATE (Part A) + GRAPH (Part B) + HARDWARE (Part C).
# Supersedes the 2026-07-31 end-of-S27 print.
# Covers Jul 31 evening + Aug 1 (days 36–37).
# SESSION NUMBERING: Jul 31 = S27 (containers) + S28 (evening, burst-origin).
#   Aug 1 = S29. PRECEDENT REAFFIRMED: days count calendar, sessions count sits;
#   burst-origin work that lands real reps earns a session number (S25, S28).
# Node IDs (N1…) are file-internal shorthand only — full names in conversation.

═══════════════════════════════════════════════
# PART A — STATE
═══════════════════════════════════════════════

## ★ PROGRAM STRUCTURE
**CS (Python + Linux) = single-track steady state. Mathematics holds the primary daily slot.**
- One solid CS block per day — a floor and a steady-state, not a ceiling. ~31 days to summer break's end.
- Block selection rule: **the queue picks the block.** Due reviews/defenses first; frontier or production when nothing is due.
- **Second sessions are legal** when they are what S28 was: surplus after the day's real work, entered by appetite. The guarded failure mode is CS eating the math slot — not observed; will be named if seen.
- **BURST MODE** (installed 2026-07-25, his design): a burst = one completed atom · indivisible work stays block-shaped · zero decision cost via the standing BURST MENU · atoms accumulate toward the day's block.
- **DAY COUNT, not streak.** Calendar days since June 26, zero days included. **Aug 1 = day 37.** Zero days on record: Jul 9, Jul 11, Jul 22, Jul 29 (4th).
- Optional cleanup, filed not assigned: `19th,July/item3.py` still says `streak`; file still streak_log.txt.

## ★ BURST MENU (refreshed this print)
1. **Tally-dict cold rep, FRESH data** — NEW; promotes the tally pattern (N72); minutes-sized
2. **Bandit 2→3** — next level; vehicle for N49/N50 cold reps. Twice queued, zero runs
3. **Container cold rep** — from blank, no notes: run any image with one published port + one mounted folder, verify in browser, destroy, recreate
4. **hack3 run** — day-count log (runs since Jul 19 unconfirmed)
(Pair-yielding cold rep CONSUMED Jul 31 — promoted.)

## Fluent (legacy — spot-check occasionally, don't drill)
N1 variables · N2 f-strings · N3 string methods · N6 lists · N7 for loops · N8 unpacking ·
N12 if/elif/else · N13 branch ordering · N15 while · N9–N11 dict cluster · N19 functions ·
N22 try/except · N5 Git · N30 with-frame

## Fluent (recent promotions)
| Node | Evidence | Next review |
|---|---|---|
| **N40 composition** | Jul 16 13:28 → Jul 19 9:47 → Jul 26 2nd defense 8:00/15:00 | 7→14d, **~Aug 9 — APPROACHING** |
| **N41 integrative ladder** | Jul 16 fail → Jul 17 +1:00 → Jul 19 5:40 → Jul 26 2nd defense 5:56/12:00 | 7→14d, **~Aug 9 — APPROACHING** |
| N36 record-keeper | S14 2:59; Jul 21/24/27 ⊇-ridden; **Aug 1 ×2 — incl. first dict-walking variant** | expanding |
| N35 count accumulator | S13; Jul 21; **Aug 1 paid** | expanding |
| N37 split-then-index-convert | S13; Jul 21; Jul 27 ⊇-ridden; **Aug 1 paid** | expanding |

- **Recurring minor flag:** double lookup / repeated computation of the same value (S24 defenses, Jul 27, Jul 31 double-split, Aug 1 triple-int before the narrow-net fix). Efficiency only. Watch, don't drill.

## produced-once
| Node | Evidence | Next |
|---|---|---|
| N24 except-as · N25 ladders · N26 .get() fallback | Jul 17 cold, Jul 19, Jul 26 ⊇-ridden; **N23/N24 paid Aug 1 (narrow net, error object used); N26 paid Aug 1 in new costume (per-key seed)** | expanding |
| N29 datetime pipeline | Jul 19 hack3 | rides item3.py reruns |
| N30w-"a" append | Jul 19 hack3 | rides composite builds |
| N34 gate pattern | S13–S16 + Jul 19 solo design; **Aug 1 paid at the boundary (build-site gate)** | rides composite builds |
| N59 list comprehensions | Jul 19 → Jul 20 composition-proven; **Aug 1 paid — load-bearing, filtered, chain-in-recipe** | expanding |
| **N60 generators** | Jul 21 both forms cold; Jul 24 + Jul 27 reps; **Jul 31 PAID EARLY — pair-yielding cold rep, fresh data, first draft correct** | 7→14d, **~Aug 14** |
| **Pair-yielding sub-pattern** | **PROMOTED Jul 31 (S28):** cold, blank, fresh data (arcade scores); probe discipline unprompted; conversion in recipe present from draft 1 — the Jul 27 missing 10% closed | rides N60 clock |
| N44 navigation trio | Jul 17 cold; Bandit Jul 25; Jul 30; **Aug 1 (ls/pwd, Git Bash)** | rides Bandit |
| N47 cat + paths | Jul 17 cold; Bandit Jul 25; Jul 30 full ride | rides Bandit |
| N51 file operations | Jul 20 cold rep | expanding |
| N54 flash+headless | Jul 18 (guided) | one-time skill |
| N55 SSH | Jul 18 → Jul 24 → Jul 25 → Jul 28/30 solo → Jul 31 solo by hostname | rides Bandit + Pi work |
| N50 permissions | Jul 24 taught + guided run | **cold rep pending — REP 2 spec issued Aug 1, not yet run; perms_test.txt locked 8 days** |

## taught / needs evidence
- **N49 find/grep** — taught Jul 23; **Aug 1: direct cold attempt CONVERTED TO GUIDED** (leading-slash fact forgotten → retaught; grep seats guided). Strong contact rep banked, four discoveries (see S29 record). **Cold rep debt STANDS — now the oldest open item in Tier L**
- **N72 tally-dict pattern** — **NEW, taught + guided Aug 1.** Build loop guided (from teaching), report loop solo. Cold rep on fresh data promotes → burst menu #1
- **Narrow-net + `continue`** — taught Aug 1, not owed. Convert once inside the try, name the result, net wraps only the explodable line; `continue` = skip to next lap
- **N73 dict/set comprehensions** — set form MET IN THE WILD Aug 1 (invented by analogy: `{x for x in …}` = set, deduplicates — which is exactly why it can't tally). Dict form (`{k: v for …}`) untaught, filed
- **N71 standard input** — taught Jul 30, met in the wild. Pipes/redirection downstream, untaught
- N27 error taxonomy — 17 species + Aug 1 variant: **except-clause order swapped** (`except A as ValueError`) → NameError raised *during handling* → two-traceback stack ("During handling of the above exception, another exception occurred"), read correctly
- **Boundary discipline (candidate principle, not yet a node):** filter/convert ONCE at the edge; clean world downstream. Three sightings Aug 1: convert-once vs triple-int · narrow net vs whole-loop wrap · gate-at-build vs gate-at-read. Promote if it keeps earning

## ★ TIER D — CONTAINERS (opened Jul 31)
| Node | State |
|---|---|
| **N62 client/daemon/socket model** | taught. `docker` = client; daemon runs as root; socket `/var/run/docker.sock` is a file, so the permissions tag is the law. **Group `docker` = root-equivalent** — named as both convenience and privilege-escalation path (cyber-relevant, other side of the table) |
| **N63 images vs containers** | **produced (guided).** Registry → pull → layers → digest vs tag → image on disk → container = running instance + writable layer. Exit code 0 read. One image, many containers = the OOP template/instance shape, arriving early |
| **N64 port mapping** | **PRODUCED, verified externally.** `-p 8080:80`; `docker ps` PORTS column read; page loaded from a different machine |
| **N65 volume mapping** | **PRODUCED, verified live.** `-v ~/site:/usr/share/nginx/html`; own HTML served; edit on host → page changed, no rebuild. **The mount is a live window, not a snapshot** |
| **N66 container disposability** | **PRODUCED, controlled experiment.** Unmounted file died with the container; mounted HTML survived |
| N67 `docker exec` / inside-the-box | produced (guided). Third prompt of the night; prompt-reading three machines deep |
| **N68 compose** | UNTAUGHT. Deliberately deferred — second container first |
| N69 shell scripting (`sh`) | taught only. Shebang · `if/fi`, `case/esac` · `$(...)` · functions · `set -e` · `set -x` · `curl \| sh` hazard + wrap-in-a-function defense |
| N70 disks/partitions/mounting | taught, no production. `sda` = disk, `sda1/sda2` = partitions · one tree + mount points · Pi 4 has no internal storage · `lsblk` unrun; SSD unwiped |

## PYTHON TIER STATUS: all core nodes production-evidenced · one taught-with-debt sub-pattern (N72 tally) · clocks expanding
- **N40/N41 second-defense clocks land ~Aug 9** — next Python queue items
- **N60 due ~Aug 14** (paid early Jul 31)
- Frontier: tally cold rep · Bandit levels · Telegram hack N52/N53 · nested comprehensions (filed) · dict comprehensions (filed)

## Linux nodes (Tier L)
| Node | State |
|---|---|
| N42/N43/N45/N48 | taught; ridden by every Bandit + Pi session |
| N44 · N47 · N51 | produced-once |
| N46 paths | taught. **Soft spot now FOUR sightings: leading-slash absolute-vs-relative** (Jul 20 ×2 · Jul 23 adjacent · Aug 1 forgotten outright, retaught plainly). Core restatement: **the slash is what MAKES it absolute** — `/c/CS` consults the root, `c/CS` consults where you stand. If it recurs: micro-drill offered, his call |
| N49 find/grep | taught + guided; **Aug 1 guided rep banked (find + grep legs complete)**; cold rep pending |
| N50 permissions | taught + guided; cold rep pending — REP 2 spec live |
| N71 standard input | taught Jul 30, met in the wild. Pipes/redirection downstream, untaught |

**N46/N49 knowledge added Aug 1 (guided rep + self-directed expansion):**
- **Glob needs raw material:** the shell only rewrites `*` when something in the standing room matches it; an unmatched glob passes through as literal characters (discovered by contact — grep went hunting a file named `*.py`)
- **Quoted `-name "*.py"` mechanism owned:** quotes stop the shell's rewrite so find receives the pattern itself; unquoted survives only by the accident of an empty room
- **find echoes the road it was handed** — results print in the address form of the starting point (his own mid-flight prediction repair: "Oh! full paths")
- **grep's three seats: grep · pattern · papers.** No starting-point slot; the address rides on the filenames (`<room>/*.py`) or you walk over. Handed a room, grep answers "Is a directory"
- **grep output anatomy:** `filename:line` prefix appears because multiple files were handed over; silence from a searched file IS the "no"
- **grep matches characters, not words** — `record` lit up inside "Un**record**ed". `-w` (whole words) filed, not taught
- **Trailing slash in a typed address is grammar with no word after it — ignored** (`/c/CS` ≡ `/c/CS/` for find/cd/ls/cat; the `Desktop/` marker in ls output is a display courtesy, different thing; rsync exception filed). Convention: slashless form is common style, not law
- **★ Per-component globbing — HIS DISCOVERY, guessed and correct:** `grep record /c/CS/*,July/*.py` — wildcards expand at every level of an address, the shell builds the crossproduct of real paths. Ran his own fossil dig: every record-keeper since Jul 12 in one command
- Jul 30 addition stands: the absolute path's second job (defeat argument-parsing). Jul 31 addition stands: SSH hostname vs IP

## Tier C — CYBER
| Item | State |
|---|---|
| Bandit gate | OPEN; production side cleared |
| Bandit level 0 · 0→1 | CLEARED Jul 25 |
| Bandit 1→2 | CLEARED Jul 30 — the dashed filename. Login as bandit2 still unconfirmed |
| **Bandit 2→3** | next; burst menu #2. **Twice queued (Jul 31, Aug 1), zero runs** |

- Port concept taught Jul 25; banner intel noted (`/etc/bandit_pass/`, per-user readability — the permissions tag system IS the game's spine)
- **Spoiler discipline:** passwords stay his; Claude verifies by report only. Passwords NOT written into this file.
- **Password hygiene (tax paid Jul 28):** save each password at extraction; **keep the password file out of the committed repo**
- `bandit0`/`bandit0` is public — documented front door

## Gates
- Linux acquisition: OPEN · Bandit: OPEN and ENTERED · Containers: OPEN, three core ideas produced · Compose: gated on a second container

## Tier H — hardware/Pi
- **Camera project: still PAUSED** (Jul 20, his call). All V1 parts in hand.
- boogiewoogie in active use as container host; camera pause untouched
- N54/N55 produced · N52/N53/N56/N57/N58 untaught
- Filed ideas, not assignments: Pi-hole · WireGuard VPN endpoint · Jellyfin · Flask status dashboard

## ★ MEDIA SERVER PROJECT (opened Jul 31)
- Goal: movie library on boogiewoogie. Jellyfin = library + streaming layer; transcoding is the Pi 4's only real ceiling.
- **Blocked on storage, not skill:** Transcend SSD still carrying seller's untrusted OS — not wiped, not formatted, not mounted. Boot-order trap flagged and unresolved: connect the bridge while the Pi is running; wipe promptly.
- **Declined, on record:** the dev-smurf media-server stack (Gluetun + FlareSolverr + indexer + torrent client = automated acquisition pipeline; ruling about the artifact, not the person). Also a poor teacher — nine unfamiliar services at once.
- Filed as the good part: its Flask dashboard shape (opens N52/N53, hack-series sized).

## ★ EXTERNAL SCHEDULE
**2026-2학기: 프로그래밍언어 (AAK10076-40), IT경영전공 교필 — JAVA.** 이충석 · 월 11:30–13:20 · 화 09:30–11:20 · D동401호 · 3학점.
- Weeks 4–10 = 객체지향 (the filed OOP block) · Weeks 1–3 = fluent tier in Java clothes · Weeks 11–12 = owned concepts, new grammar
- 발표 25% · 실습 (팀 10% + 팀프로젝트 25%) · 3인 1팀 · 출석 1/5 이상 결석 시 F
- Decision deferred: pre-study vs walk in cold

## Conduct rules (standing)
Timer to zero · mid-rep question voids · spec questions before clock free · no psychological commentary on motives/enthusiasm · predictions-first on shell runs (**commands are not calls** — third sendback Aug 1; a call must be committable enough to be wrong) · his self-report is the diagnosis · when memory holds no evidence, structural prediction IS the honest prediction · design authority over his own tools is his · traced-correct output disagreeing with spec gets flagged aloud (binds both sides) · a burst = one completed atom · defenses and new-idea acquisition never split · "I don't remember that session" changes nothing ·
**a prediction Claude has already spoiled is void — struck, not scored (covers any prior statement in the chat)** ·
**the level page is the spec** — goal + command list before a run is standard; the command list is a superset, not a recipe; walkthroughs/solve videos/password lists never ·
**a forgotten fact gets retaught plainly, not dangled as a puzzle — and the rep converts cold→guided, honestly logged (Aug 1 precedent)**

## Repo hygiene & reconciliations
- hack3 = `19th,July/item3.py`. streak_log.txt honest as of Jul 19; runs since unconfirmed
- review.py (Jul 21) and practice1.py (Jul 27) retain his chosen imperfections — his files, his call
- **`1st,August/` holds review1.py + review2.py — committed and pushed Aug 1**
- Jul 31 ledger files: staged Jul 31, committed + pushed Aug 1
- **CRLF/LF warnings on git add: ruled COSMETIC** (line-ending dialects; Git standardizing LF-in-repo / CRLF-in-working-copy; content identical). Proceed normally. Optional `core.autocrlf` config filed, not assigned
- boogiewoogie home: `get-docker.sh`, `site/`, `perms_test.txt` (**locked 8 days as of Aug 1**)
- Bandit passwords: outside the committed repo

---

## Session record — Jul 31 evening (day 36, S28, BURST-ORIGIN SESSION)
**Mode: production — burst menu #1, entered by appetite after S27's close.**

**Pair-yielding generator cold rep, fresh data** (arcade scores; expected galaga/5600):
1. **Probe run** — generator built, bare print-loop inspected plates (labels aboard, numbers unquoted), probe swapped out before the real build. The Jul 27 probe discipline, unprompted and routine.
2. **Final run** — fresh generator, record-keeper downstream (seed 0 + empty title, if-guarded overwrite, both slots together), consumed exactly once. Output exact.
3. **Conversion inside the recipe present from draft 1** — the exact 10% missing Jul 27, closed.

**Rulings:** pair-yielding → **produced-once**. **N60 clock PAID three days early** — 7→14d, next ~Aug 14. Burst menu #1 consumed. Double-split efficiency flag restated once, no drill.

**Also this session:** CRLF warnings ruled cosmetic · session-numbering precedent articulated (sessions count sits) · Bandit 2→3 queued, not entered — nothing ran after the rep, logged plainly on his report.

**By the day-metric:** surplus after a closed session, run honest, first-pass correct.

---

## Session record — Aug 1 (day 37, S29, FULL BLOCK — multi-block review day)
**Mode: review (early payment — nothing was due). Python block ×2 builds, then Linux block.**

### Python build 1 — review1.py (reading log, malformed wednesday)
- **Draft 1:** `type(int(...))` filter → ValueError. The lesson that mattered: **you can't ask int() "would you crash?" without it crashing** — that question is only askable inside a try.
- **Pivot:** `!= "n/a"` filter; output correct (4 / 156 / thursday) but **requirement 2 unmet** — a filter dodges one known specimen; a net survives any garbage.
- **His question — "why do I feel the first one was better?"** — answered with the shape-vs-robustness analysis: v1 converted once at the boundary (clean world downstream); v2 smeared conversion ×3/line and wrapped the whole loop in the net (TypeError fee collected). The virtues aren't in conflict: **narrow the net.**
- **Completion:** comprehension splits, loop converts inside a narrow try, `except ValueError as A` with the error object put to work, `continue` taught. En route, all repaired solo: **except-clause order swap** (`except A as ValueError` → NameError during handling; two-traceback stack read) — new species variant · record-keeper initially absent (`/0` caught) · TypeError str-vs-int.
- **Paid:** N59 (full weight) · N35 · N36 · N37 · N23/N24 on completion. Silent-bug pattern again (draft-2 `total = 0` inside the loop, gone in final).

### Python build 2 — review2.py (workout tally)
- **His question — "is the tally novel?" — record checked: NOVEL.** Every prior `.get()` survived lookups; none seeded a per-key accumulator. **CLAUDE ERROR, logged: spec framed an untaught composite as review.** Rep converted to acquisition; no debt created against him.
- **Taught:** tally = **seed-then-feed with the seed per-key, supplied by `.get(key, 0)`** — the create-vs-read asymmetry working *for* you.
- **Free find:** his line `{workout for workout in workouts}` = an accidental **set comprehension**, invented by analogy — legal, deduplicating, and therefore exactly wrong for tallying. Met-in-the-wild; dict comprehensions filed.
- **Production:** build loop guided; **report loop solo** — first dict-walking record-keeper, gate correctly protecting both the sum and the contest (nesting reasoned, not lucky).
- **Flag → completion:** `'rest': 2` was IN the tally (gated at read, not build). Gate relocated to the build site; dead read-side gate deleted, not decorated. Output exact: 8 sessions, run/4.
- **Rulings:** N72 tally → taught + guided, cold rep → burst #1 · N26 paid in new costume · N34 paid at the boundary · N36 dict variant.
- **Boundary discipline: three sightings in one day** — candidate principle filed.

### Linux block — REP 1 (find/grep), attempted cold → CONVERTED GUIDED
- Commands-not-calls sendback (third instance); calls then committed properly.
- **Contact series, all from one root — standing in `~` while addressing relatively:** find echoed its literal search string · two-argument find complaint read per-argument · bare glob reached grep as literal `*.py` → **discovery: unmatched globs pass through** (glob needs raw material from the standing room).
- **"I forgot" on the leading slash → retaught plainly, cold status surrendered.** Fourth sighting. The slash is what makes it absolute.
- Repairs: absolute path + quoted `-name` (mechanism owned, not luck) · mid-flight prediction self-repair ("Oh! full paths — find echoes the road") · one-per-line format committed on request.
- **find leg: HIT as called** (two full paths, one per line). **grep leg:** two seat-confusions guided (address in the pattern seat; room instead of papers) → Road 1 run → **HIT** (review2.py + `tally[data]`); line count 4–5 vs 6 near miss — *his own code grew past his mental model of it* · `filename:` prefix and silence-as-no learned by contact.
- **Self-directed expansion (unassigned, pure profit):** multi-room finds through a Korean-named path · trailing-slash question → grammar answer · **★ the per-component glob discovery** (`/c/CS/*,July/*.py`) — guessed, correct, and used to run a fossil dig of every record-keeper since Jul 12 · "Unrecorded" substring match → characters-not-words; `-w` filed.
- **N49 cold debt STANDS** — strong guided rep banked.

### REP 2 (permissions, boogiewoogie) — spec issued, NOT RUN
Deferred by his call at 19:23 to possibly tonight. perms_test.txt at 8 days locked. N50 cold debt stands.

**Claude errors this session:** the tally spec error (above).

**By the day-metric:** two Python builds and a full-contact shell rep; every wall worked to resolution; two honest cold→guided conversions where the evidence demanded them. Dense, honest day.

---

## Next (queue-picked)
1. **REP 2 — permissions cold rep on boogiewoogie** (spec live; possibly tonight; unlocks the 8-day file; clears N50's debt)
2. **Bandit 2→3** (burst #2) — N49's cold rep rides on file-hiding levels; a direct find/grep cold retry in a few days is also legal
3. **Tally cold rep, fresh data** (burst #1) — promotes N72
4. **N40/N41 second-defense clocks ~Aug 9**
5. **N60 generators ~Aug 14**
6. **SSD: wipe → format → mount** — the media-server blocker; boot-order trap live
7. Second container → compose (N68) · Telegram hack / Flask dashboard (filed) · camera resumes on his word only

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
- N31 .split() · N32 .append() · N33 empty-tail · N34 gate · N35 count accumulator · N36 record-keeper (incl. dict-walking variant, Aug 1) · N37 split-index-convert · N38 if-guarded overwrite · N39 seed-then-feed
- N40 integrative composition — FLUENT, twice defended
- N41 integrative ladder — FLUENT, twice defended
- N59 comprehensions ← N7,N6,N34 · N60 generators ← N59,N7,N19 (**pair-yielding sub-pattern PRODUCED Jul 31**)
- **N72 tally-dict (per-key seed-then-feed) ← N9,N10,N11,N26,N39 — taught + guided Aug 1, cold rep pending**
- **N73 dict/set comprehensions ← N59,N9 — set form met-in-the-wild Aug 1; dict form untaught, filed**

**Tier L — Linux/shell**
- N42 shell/OS model · N43 cwd · N44 nav trio — produced · N45 home/~ · N46 paths (two jobs: locate, and defeat argument-parsing; **leading-slash soft spot ×4**) · N47 cat — produced · N48 prompt anatomy · N49 find/grep — taught+guided (**Aug 1 guided rep**; + glob raw-material rule, per-component globbing, grep seats/anatomy, characters-not-words) · N50 permissions — taught+guided · N51 file ops — produced
- N71 standard input ← N42 — taught, met in the wild. Downstream, untaught: **pipes and redirection** — Bandit's home turf
- N69 shell scripting ← N42,N44 — taught · N70 disks/partitions/mounting ← N43,N46 — taught, no production

**Tier D — containers**
- N62 client/daemon/socket ← N42,N50 — taught
- N63 images vs containers ← N62 — produced (guided)
- N64 port mapping ← N63, port concept — PRODUCED
- N65 volume mapping ← N63,N46,N70 — PRODUCED
- N66 disposability/persistence ← N63,N65 — PRODUCED
- N67 docker exec ← N63,N48 — produced (guided)
- N68 compose ← N64,N65,N66 + YAML — UNTAUGHT, gated on a second container
- Downstream: container networking · PUID/PGID volume-permission problem ← N50 · secrets/.env · reverse proxy + TLS ← N64

**Tier H — hardware/Pi**
- N52 pip · N53 HTTP/requests · N54 flash — produced · N55 SSH — produced · N56 GPIO/PIR · N57 camera · N58 THE MACHINE
- Jellyfin ← N64,N65,N70 — storage prerequisite is the only real blocker

**Tier C — cyber**
- N61 Bandit ← N44,N46,N47,N49,N50,N55,N71 — levels 0, 0→1, 1→2 cleared; the shell tier's review engine

**External block:** OOP ← N19,N21 — 2026-2학기 via Java (weeks 4–10). N63's template/instance distinction is an early sighting

**Encompassing edges:**
- N61 Bandit ⊇ N55{1.0}, N44{1.0}, N46{0.9}, N47{1.0}, N48{0.8}, N49{0.8 *only when a level hides a file*}, N50{0.9}, N42{0.7}, N71{0.8 when a level touches stdin}
- **N72 ⊇ N26{1.0}, N10{1.0}, N9{0.9}, N11{0.8}, N39{0.8}, N34{0.6 when gated at build}** — new best single review task for the dict cluster once cold
- N71 ⊇ N42{0.6} · N46 ⊇ N43{0.8}
- N64 ⊇ port concept{1.0}, N48{0.4} · N65 ⊇ N46{0.9}, N70{0.7}, N44{0.5} · N66 ⊇ N65{0.8}, N63{1.0}
- N67 ⊇ N48{0.9}, N44{0.6}, N42{0.7} · N62 ⊇ N50{0.9}, N42{0.6} · N69 ⊇ N42{0.8}, N12/N13{0.6}, N19{0.5}
- (prior edges unchanged: N40, N41, N49, N50, N60, N59, item3.py, N39, N38, N37, N36, N35, N33, N30, N29, N25, N17, N16, N8, N47, N44, N51, N55, N58)

**Graph-reading notes (Aug 1):**
- **N49's cold debt survived a direct attempt** — the leading-slash prerequisite failed under load, exactly the fluency-gap mechanism this program exists for. The debt is now the oldest open item in Tier L. Two collectors: file-hiding Bandit levels (natural) or a direct cold retry after a few days' gap (legal).
- **N46's leading slash at four sightings** is the single most reliable failure point in the shell tier. If it fires a fifth time, a dedicated micro-drill gets proposed — his call.
- **The dict cluster got its best day since S8–9:** N26 in a new costume, a new composite (N72), a new comprehension family sighted, first dict-walking record-keeper. One tally cold rep converts most of that to production evidence.
- **Python review clocks are front-loaded now** — Aug 1 payments pushed everything to ~Aug 9 (defenses) and ~Aug 14 (N60). Review pressure is low; frontier and Bandit have the floor.
- Boundary discipline is a principle, not yet a node — it gets a node if it keeps showing up as the shape of corrections.

═══════════════════════════════════════════════
# PART C — HARDWARE LOG
═══════════════════════════════════════════════

## The declared machine
**Pi-based home security camera.** V1: motion (PIR) → photo → Telegram alert → event log. TRACK PAUSED Jul 20, his call; resumes on his word.

## Second project (Jul 31)
**Jellyfin media server on boogiewoogie.** Blocked only on storage. Container skills now in place.

## Live systems
| Machine | State |
|---|---|
| **boogiewoogie** (Pi 4B 4GB, Argon ONE M.2) | ALIVE. RPi OS Lite 64 (trixie), kernel 6.18.34. USB-boot (Toshiba 28.9GB), Wi-Fi jini, **192.168.0.9** — also reachable as `boogiewoogie` (IPv6 link-local). `ssh snakeyboy777@…` — always name the user. Docker Engine 29.7.0 + compose v5.3.1, daemon enabled at boot. 23G free before Docker. Images: hello-world, nginx. Home dir: get-docker.sh · site/ · **perms_test.txt (locked 8 days)** |

## Inventory
| Item | Status |
|---|---|
| Pi 4 4GB + Argon ONE M.2 + USB bridge | running (bridge + SSD still disconnected) |
| Transcend 128GB M.2 SSD | seller's OS aboard, untrusted; **wipe still deferred — the media server's blocker** |
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
60cm cable · IR-CUT camera · High Endurance SD · mmWave sensor · Pi AI Camera · known_hosts Korean-path fix · docker group membership (declined for now — `sudo` per command).

## Filed ideas
**Pi-hole** · **WireGuard VPN endpoint** · **Jellyfin** · **Flask status dashboard**. All whisper-class; all coexist with the camera.

## Long-horizon (filed)
Manafish ROV (9–15mo) · rybtronics thermal drone (3–5yr).