# ledger.md — updated 2026-07-31, end of Session 27 (day 36)
# Complete Skycak artifact: STATE (Part A) + GRAPH (Part B) + HARDWARE (Part C).
# Supersedes the 2026-07-31 partial print AND the 2026-07-27 print.
# Covers Jul 28–31 (days 33–36) — fuses the Bandit chat with the container chat.
# SESSION NUMBERING RESOLVED: Jul 30 = S26 (Bandit 1→2) · Jul 31 = S27 (containers).
#   Jul 28 = partial, not a session. Jul 29 = zero day.
# Node IDs (N1…) are file-internal shorthand only — full names in conversation.

═══════════════════════════════════════════════
# PART A — STATE
═══════════════════════════════════════════════

## ★ PROGRAM STRUCTURE
**CS (Python + Linux) = single-track steady state. Mathematics holds the primary daily slot.**
- One solid CS block per day. ~32 days to summer break's end.
- Block selection rule: **the queue picks the block.** Due reviews/defenses first; frontier or production when nothing is due.
- **BURST MODE** (installed 2026-07-25, his design): a burst = one completed atom · indivisible work stays block-shaped · zero decision cost via the standing BURST MENU · atoms accumulate toward the day's block.
- **DAY COUNT, not streak.** Calendar days since June 26, zero days included. **Jul 31 = day 36.** Zero days on record: Jul 9, Jul 11, Jul 22, **Jul 29 (4th)**.
- Optional cleanup, filed not assigned: `19th,July/item3.py` still says `streak`; file still streak_log.txt.

## ★ BURST MENU (refreshed this print)
1. **Pair-yielding generator cold rep, FRESH data** — promotes the last taught-only Python sub-pattern; minutes-sized
2. **Bandit 2→3** — next level; vehicle for N49/N50 cold reps
3. **Container cold rep** — from blank, no notes: run any image with one published port + one mounted folder, verify in browser, destroy, recreate
4. **hack3 run** — day-count log (runs since Jul 19 unconfirmed)

## Fluent (legacy — spot-check occasionally, don't drill)
N1 variables · N2 f-strings · N3 string methods · N6 lists · N7 for loops · N8 unpacking ·
N12 if/elif/else · N13 branch ordering · N15 while · N9–N11 dict cluster · N19 functions ·
N22 try/except · N5 Git · N30 with-frame

## Fluent (recent promotions)
| Node | Evidence | Next review |
|---|---|---|
| **N40 composition** | Jul 16 13:28 → Jul 19 9:47 → Jul 26 2nd defense 8:00/15:00 | 7→14d, **~Aug 9** |
| **N41 integrative ladder** | Jul 16 fail → Jul 17 +1:00 → Jul 19 5:40 → Jul 26 2nd defense 5:56/12:00 | 7→14d, **~Aug 9** |
| N36 record-keeper | S14 2:59; Jul 21, Jul 24, Jul 27 ⊇-ridden | expanding |
| N35 count accumulator | S13; Jul 21 paid early | expanding |
| N37 split-then-index-convert | S13; Jul 21 paid; Jul 27 ⊇-ridden | expanding |

- **Recurring minor flag:** double lookup of the same value (S24 defenses, Jul 27). Efficiency only. Watch, don't drill.

## produced-once
| Node | Evidence | Next |
|---|---|---|
| N24 except-as · N25 ladders · N26 .get() fallback | Jul 17 cold, Jul 19, Jul 26 ⊇-ridden | expanding |
| N29 datetime pipeline | Jul 19 hack3 | rides item3.py reruns |
| N30w-"a" append | Jul 19 hack3 | rides composite builds |
| N34 gate pattern | S13–S16 + Jul 19 solo design | rides composite builds |
| N59 list comprehensions | Jul 19 → Jul 20 composition-proven | expanding |
| **N60 generators** | Jul 21 both forms cold; Jul 24 + Jul 27 reps paid | 3→7d, **~Aug 3 — DUE SOON** |
| N44 navigation trio | Jul 17 cold; Bandit Jul 25; **Jul 30 (ls + pwd, cd unused)** | rides Bandit |
| **N47 cat + paths** | Jul 17 cold; Bandit Jul 25; **Jul 30 full ride — the dashed-filename level** | rides Bandit |
| N51 file operations | Jul 20 cold rep | expanding |
| N54 flash+headless | Jul 18 (guided) | one-time skill |
| N55 SSH | Jul 18 → Jul 24 → Jul 25 bandit → **Jul 28/30 bandit re-entry, solo** → Jul 31 solo by hostname | rides Bandit + Pi work |
| N50 permissions | Jul 24 taught + guided run | needs one cold rep — Bandit supplies it |

## taught / needs evidence
- **N49 find/grep** — taught Jul 23, guided evidence strong. Cold rep **still pending**: Bandit 1→2 did not hide a file, so no credit fell out of it
- **Pair-yielding generator recipe** — taught Jul 21, guided Jul 27. Cold rep on fresh data promotes → burst menu #1
- **N71 standard input** — NEW, taught Jul 30, met in the wild (see Tier L)
- N27 error taxonomy — 17 species

## ★ TIER D — CONTAINERS (opened Jul 31)
| Node | State |
|---|---|
| **N62 client/daemon/socket model** | taught. `docker` = client; daemon runs as root; socket `/var/run/docker.sock` is a file, so the permissions tag is the law. **Group `docker` = root-equivalent** — named as both convenience and privilege-escalation path (cyber-relevant, other side of the table) |
| **N63 images vs containers** | **produced (guided).** Registry → pull → layers → digest vs tag → image on disk → container = running instance + writable layer. Exit code 0 read. Random-name generation seen. One image, many containers = the OOP template/instance shape, arriving early |
| **N64 port mapping** | **PRODUCED, verified externally.** `-p 8080:80`; `docker ps` PORTS column read (`0.0.0.0:8080->80/tcp`, plus IPv6 row); page loaded from a *different machine* |
| **N65 volume mapping** | **PRODUCED, verified live.** `-v ~/site:/usr/share/nginx/html`; own HTML served; file edited on host → page changed with no rebuild. **The mount is a live window, not a snapshot** |
| **N66 container disposability** | **PRODUCED, verified by controlled experiment.** `/tmp/scratch.txt` written inside → container destroyed + recreated → gone; mounted HTML survived. Retroactively explains the per-service host folders in any compose stack |
| N67 `docker exec` / inside-the-box | produced (guided). Third prompt of the night (`root@<id>:/#`); container's own full Linux tree observed; prompt-reading now three machines deep |
| **N68 compose** | UNTAUGHT. Deliberately deferred — one container by hand first, second container next, compose when they need to talk |
| N69 shell scripting (`sh`) | taught only. Shebang as interpreter selector · `.sh` = commands written down, same language as the prompt · `if/fi`, `case/esac` (first-match-wins ladder), `$(...)`, functions, `set -e` (no default error survival), `set -x` trace · the `curl \| sh` truncation hazard and the wrap-in-a-function defense |
| N70 disks/partitions/mounting | taught, no production. `df -h` read correctly (device/size/mount point) · **`sda` = disk, `sda1/sda2` = partitions** · Linux has one tree + mount points, no drive letters · **Pi 4 has NO internal storage** (misconception corrected) · `lsblk` still unrun; SSD still unwiped, unmounted |

## PYTHON TIER STATUS: all nodes production-evidenced · zero contracted debt · clocks expanding
- **N60 generators due ~Aug 3** — first thing on the Python queue
- Frontier: Bandit levels · pair-yielding cold rep · Telegram hack N52/N53 · nested comprehensions (filed)

## Linux nodes (Tier L)
| Node | State |
|---|---|
| N42/N43/N45/N48 | taught; ridden by every Bandit + Pi session |
| N44 · N47 · N51 | produced-once |
| N46 paths | taught. Soft spots: leading-slash absolute-vs-relative (Jul 20 ×2) · fresh-shell-starts-at-home (Jul 23) |
| N49 find/grep · N50 permissions | taught + guided; cold reps pending |
| **N71 standard input** | **NEW, taught Jul 30, met in the wild.** Every program launches with three channels wired: read-from, write-to, complain-to. Output and errors were already familiar; the read-from channel defaults to the keyboard. `cat` with no argument reads the keyboard forever · **`-` in an argument slot is the written convention for standard input**, so it can be positioned among real files (`cat header.txt - footer.txt`). Escape = Ctrl+C. **Downstream, untaught: pipes (`\|`) and redirection (`>`, `<`)** — the whole reason the convention exists, and Bandit's home turf |

- **Jul 30 addition to N46 (paths):** the absolute path has a *second job*. It doesn't only say which room — it makes an argument **stop looking like grammar**. `cat -` matched cat's own special case; `cat /home/bandit1/-` and `cat ./-` do not. Same fix, two different reasons, and now both are on record.
- **Jul 31 addition:** SSH by hostname vs IP — the name requires a resolution step (the flaky part); resolved to an **IPv6 link-local address** (`fe80::…%11`), not .9. DHCP means the IP can change; the name survives it. Use the name, fall back to the IP.

## Tier C — CYBER
| Item | State |
|---|---|
| Bandit gate | OPEN; production side cleared |
| Bandit level 0 · 0→1 | CLEARED Jul 25 |
| **Bandit 1→2** | **CLEARED Jul 30** — the dashed filename. Password extracted; login as bandit2 unconfirmed at print time |
| **Bandit 2→3** | next; **burst menu #2** |

- Port concept taught Jul 25 (`-p 2220`); banner intel noted (`/etc/bandit_pass/`, each level's password readable only by its own user — the permissions tag system IS the game's spine)
- **Spoiler discipline:** passwords stay his; Claude verifies by report only. Passwords are NOT written into this file.
- **Password hygiene (tax paid once, Jul 28):** the bandit1 password was lost and had to be recovered by re-solving 0→1. Habit attached — save each password at extraction. **Keep the password file out of the git repo** (or gitignored); ledger.md is committed to GitHub, and a credentials file next to it is exactly the mistake this track exists to stop making.
- **`bandit0`/`bandit0` is public** — OverTheWire's documented front door, not a spoiler and not solved for.

## Gates
- Linux acquisition: OPEN · Bandit: OPEN and ENTERED · Containers: OPEN, three core ideas produced · Compose: gated on a second container

## Tier H — hardware/Pi
- **Camera project: still PAUSED** (Jul 20, his call). All V1 parts in hand.
- **boogiewoogie is in active use again** as of Jul 31 — as a container host, not for the camera. Pause on the camera track untouched.
- N54/N55 produced · N52/N53/N56/N57/N58 untaught
- Filed ideas, not assignments: Pi-hole · WireGuard VPN endpoint · **Jellyfin media server** · Flask status dashboard

## ★ MEDIA SERVER PROJECT (opened Jul 31)
- **Goal as stated:** a movie library on boogiewoogie. Jellyfin = the library + streaming layer (scans a folder, fetches posters, serves on 8096, tracks watch state). Transcoding is the Pi 4's only real ceiling; direct play is effortless.
- **Blocked on storage, not skill:** the Transcend 128GB SSD is present, connected via the Argon USB bridge, still carrying the seller's untrusted OS, **not wiped, not formatted, not mounted.** Nothing was run against it Jul 31. Boot-order trap flagged and unresolved: both the SSD and the Toshiba boot stick are USB and bootable — plug the bridge in while the Pi is already running, wipe promptly.
- **Declined, on record:** the `dev-smurf/Raspberry-Pi-4-Media-Server` stack. Reason given twice, plainly: Gluetun (traffic-hiding VPN) + FlareSolverr (Cloudflare bypass) + indexer manager + torrent client is an automated acquisition pipeline. His stated intent accepted at face value; the ruling is about the artifact, not the person. Not revisited after.
- **Engineering position given (separate from the above):** that repo is also a poor teacher — nine unfamiliar services at once, three unfamiliar layers lying simultaneously when one breaks. The July 8 collapse in Docker clothes. One container by hand → two → compose is the path that actually builds the skill.
- **Filed as the good part of that repo:** its Flask dashboard (`app.py`, `index.html`) — Python status page for boogiewoogie, opens N52/N53, hack-series shaped.

## ★ EXTERNAL SCHEDULE
**2026-2학기: 프로그래밍언어 (AAK10076-40), IT경영전공 교필 — JAVA.** 이충석 · 월 11:30–13:20 · 화 09:30–11:20 · D동401호 · 3학점.
- Weeks 4–10 = 객체지향 (the filed OOP block, externally scheduled) · Weeks 1–3 = fluent tier in Java clothes · Weeks 11–12 = owned concepts, new grammar
- 발표 25% · 실습 (팀 10% + 팀프로젝트 25%) · 3인 1팀 · 출석 1/5 이상 결석 시 F
- Decision deferred: pre-study vs walk in cold

## Conduct rules (standing)
Timer to zero · mid-rep question voids · spec questions before clock free · no psychological commentary on motives/enthusiasm · predictions-first on shell runs · his self-report is the diagnosis · when memory holds no evidence, structural prediction IS the honest prediction · design authority over his own tools is his · traced-correct output disagreeing with spec gets flagged aloud (binds both sides) · a burst = one completed atom · defenses and new-idea acquisition never split · "I don't remember that session" changes nothing ·
**a prediction Claude has already spoiled is void — Claude's error, struck, not scored. (Jul 30 clarification: this covers any prior statement in the chat, not just the same message.)** ·
**NEW (Jul 30) — the level page is the spec.** Reading OverTheWire's level page (goal + command list) *before* a run is legitimate and now standard: it converts an evidence-free guess into a real prediction, which is the entire mechanism the predictions-first rule exists for. **Never** read walkthroughs, solve videos, or password lists — the moves are the thing being bought. Caveat: the listed commands are a **superset, not a recipe** (level 1 listed `du` and `file`; neither was needed).

## Repo hygiene & reconciliations
- hack3 = `19th,July/item3.py`. streak_log.txt honest as of Jul 19; runs since unconfirmed
- review.py (Jul 21) and practice1.py (Jul 27) retain his chosen imperfections — his files, his call
- **boogiewoogie home dir now holds `get-docker.sh`, `site/`, and the July 24 `perms_test.txt`** (still locked, still unread)
- **Bandit passwords: keep the file outside the committed repo.** See Tier C

---

## Jul 28 (day 33) — PARTIAL, no atom banked
Block opened (Bandit 1→2). The bandit1 password was found lost; the recovery attempt reached the bandit0 password prompt and stopped there. Connecting and reading bank nothing — logged honestly as partial, not a session, not a zero.
- Cosmetic known_hosts failure on the Korean-username Windows path reappeared and was correctly read as harmless (fingerprint re-asked each session, connection unaffected).

## Jul 29 (day 34) — ZERO DAY. Fourth on record.

---

## Session record — Jul 30 (day 35, S26, FULL BLOCK)
**Mode: production — Bandit 1→2, the dashed filename.**

**Recovery step.** Re-solved 0→1 from bandit0 to re-extract the lost bandit1 password. Tax paid once; habit attached.

**Predictions (structural — no evidence held).** "`ls` prints about three files, no directories" · "contents ~10 lines, password on the last line."

**Reconciliation:**
- **Count — STRUCK, not scored.** Claude had already stated "a file in the home directory" before predictions were requested (Jul 28 and again Jul 30). Claude's error under the spoiled-prediction rule; comes off the board.
- **Kind — HIT.** File, not directory. No trailing slash, marker read correctly.
- **Line count — MISS, uncontaminated, and the valuable one.** One line, 32 mixed-case alphanumeric characters. Real evidence now held for every remaining level, where before there was none.

**The run:**
1. `ls` → `-`. First read as "nothing is in the home directory." Corrected by **look-don't-infer**: an empty `ls` hands back the prompt with nothing between, and he had seen the genuine article on boogiewoogie Jul 18. The dash was output.
2. **`pwd` run unprompted** → `/home/bandit1`. Establishing the room before addressing the file — bedroom/kitchen applied with no pointer given. His own move.
3. `cat -` → **terminal hung.** Not a crash, not a refusal: `cat` matched its own special case for the exact string `-`, opened standard input, and waited on the keyboard. Same species as `f.write() = "..."` — a valid instruction that isn't the intended one.
4. **Ctrl+C** — escape produced correctly. Second career use (first: the Session 5 infinite loop).
5. `cat /home/bandit1/-` → password extracted. **LEVEL CLEARED.** The fix was **guided** — pointer to the room already printed on his own screen plus the Session 16 step-8 precedent — not solo. Logged as such.

**Knowledge banked:** standard input as the third channel (N71) · `cat` with no argument reads the keyboard · `-` as the written convention for stdin in an argument slot, and why it exists (positioning stdin among real files) · a name that collides with grammar gets swallowed before it is ever treated as a name · **the absolute path's second job** — not only locating, but making an argument stop looking like grammar; `./-` is the cheap equivalent.

**Catalogue note (not an error species — nothing was raised):** *silent wait on standard input.* No output, no error, terminal appears frozen. Sibling of the infinite loop by escape hatch (Ctrl+C), unrelated by mechanism — the program is behaving correctly and waiting on you.

**Convention set:** the level page is the spec (see conduct rules).

**Claude errors this session:** partially spoiled the `ls` output on both Jul 28 and Jul 30 ("a file in the home directory… the twist is visible the second you run `ls`"), then requested predictions. Count-miss struck; the spoiled-prediction rule clarified to cover the whole chat, not just the same message.

**By the day-metric:** honest block. He hit a wall that hangs the terminal, escaped it correctly, and walked out with the password.

---

## Session record — Jul 31 (day 36, S27, FULL BLOCK)
**Mode: acquisition, new domain — containers. Guided production throughout.**

*Morning (~10:40–11:40):* reading only — media servers, the \*arr architecture, service-oriented design, Docker/Compose, GitHub's surface (repo anatomy, commits, forks, PRs, licenses, README mechanism). Zero commands. Ruled at the time: **one atom, no block** (the `df -h` prediction set). Ruling stood on the evidence available.

*Afternoon (~14:20 onward):* the block.
1. `apt update` + full-upgrade backlog cleared (14 packages); `ca-certificates`/`curl` already current — predicted correctly
2. `df -h` — prediction "two rows: Pi storage + stick, ~28GB free." **Two misses:** the Pi has no internal storage at all, and `sda1`/`sda2` are two partitions of the one stick. tmpfs rows correctly identified as RAM. Actual: 23G free, 15% used
3. `curl -o get-docker.sh` — prediction "a directory containing the Docker program." **Miss on both halves:** a *file*, not a directory (his own markers-don't-lie lesson, applied to his own output); and the *script that installs* Docker, not Docker — recipe vs meal
4. `cat get-docker.sh` read before running as root — the habit, deliberately practiced. Shell-script language taught off his own screen (N69)
5. `sudo sh get-docker.sh` — Docker Engine 29.7.0 + compose v5.3.1 installed, daemon enabled and started by the script. `set -x` trace read line by line: GPG key fetched, `chmod a+r` (permissions node live), repository written to `sources.list.d`
6. `docker run hello-world` — pull cycle read in full (registry → tag → layer → digest → status), `(arm64v8)` noticed, exit code 0 explained
7. **nginx, port mapping** — `-d -p 8080:80 --name webtest`. `Up 2 minutes` vs `Exited (0)` contrasted. Page loaded from Windows at `192.168.0.9:8080`
8. **Volume mapping** — `~/site` mounted; own HTML served; **prediction HIT** (his own): editing the file changes the page with no rebuild. Mount is live
9. **`docker exec -it`** — inside the box, root prompt, container's own filesystem tree observed
10. **Persistence experiment** — prediction "scratch.txt survives." **MISS**, and the valuable one: container destroyed → `/tmp/scratch.txt` gone, mounted HTML intact. Third idea proven by controlled experiment rather than assertion

**Ruling: FULL BLOCK.** Precedent = Session 17 (flash + SSH), also start-to-finish guided acquisition in a new domain, also counted. Real machine state changed; predictions ran before commands; five honest misses reconciled.

**Claude errors this session:** (a) spoiled the `curl` output prediction while explaining the flags, then asked for it — void, struck, conduct rule attached; (b) the 11:40 partial ruling was correct on its evidence but was superseded within hours — noted so the precedent reads correctly later.

**Affect note:** "Shit. This is hard stuff. I don't know what you're talking about." at the socket/permissions explanation — the fix was dropping the mechanism entirely for a door-and-key model plus "just keep typing sudo." He kept going immediately after. The over-explanation was the failure, not the confusion.

---

## Next (queue-picked, one block/day)
1. **N60 generators due ~Aug 3** — first Python item on the clock
2. **Bandit 2→3** (burst #2) — the shell tier's review engine; N49/N50 cold reps still riding on it
3. **Container cold rep** (burst #3) — the three ideas from blank, no notes
4. **SSD: wipe → format → mount.** Required for a real library, independent of Docker. `lsblk` still unrun; boot-order trap still live
5. **Second container**, then compose (N68) — the honest path to reading any stack
6. Pair-yielding cold rep · Telegram hack · Flask dashboard (filed)
7. Camera track: resumes on his word only

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
- N22 try/except ← N12 · N23 specific nets ← N22 · N24 except-as ← N23 · N25 ladders ← N23,N13 · N26 .get()/None ← N9,N11 · N27 taxonomy (17 species) ← N22,N4

**Tier 3 — library & I/O**
- N28 import ← N1 · N29 datetime ← N28 · N30 file I/O ← N28,N2

**Tier 3 — composite patterns**
- N31 .split() · N32 .append() · N33 empty-tail · N34 gate · N35 count accumulator · N36 record-keeper · N37 split-index-convert · N38 if-guarded overwrite · N39 seed-then-feed
- N40 integrative composition — FLUENT, twice defended
- N41 integrative ladder — FLUENT, twice defended
- N59 comprehensions ← N7,N6,N34 · N60 generators ← N59,N7,N19 (pair-yielding sub-pattern: cold rep pending)

**Tier L — Linux/shell**
- N42 shell/OS model · N43 cwd · N44 nav trio — produced · N45 home/~ · N46 paths (**two jobs: locate, and defeat argument-parsing**) · N47 cat — produced · N48 prompt anatomy · N49 find/grep — taught+guided · N50 permissions — taught+guided · N51 file ops — produced
- **N71 standard input ← N42 — NEW, taught Jul 30, met in the wild.** Downstream, untaught: **pipes and redirection** (`|`, `>`, `<`) — the next real chunk of shell power, and where Bandit spends most of its levels
- N69 shell scripting ← N42,N44 — taught · N70 disks/partitions/mounting ← N43,N46 — taught, no production

**Tier D — containers**
- **N62 client/daemon/socket ← N42,N50** — taught
- **N63 images vs containers ← N62** — produced (guided)
- **N64 port mapping ← N63, port concept (Bandit)** — PRODUCED
- **N65 volume mapping ← N63,N46,N70** — PRODUCED
- **N66 disposability/persistence ← N63,N65** — PRODUCED
- **N67 docker exec ← N63,N48** — produced (guided)
- **N68 compose ← N64,N65,N66 + YAML** — UNTAUGHT, gated on a second container
- Downstream: container networking (service-name resolution) · PUID/PGID volume-permission problem ← N50 · secrets/.env · reverse proxy + TLS ← N64

**Tier H — hardware/Pi**
- N52 pip · N53 HTTP/requests · N54 flash — produced · N55 SSH — produced · N56 GPIO/PIR · N57 camera · N58 THE MACHINE
- **Jellyfin ← N64,N65,N70** — the storage prerequisite is the only real blocker

**Tier C — cyber**
- N61 Bandit ← N44,N46,N47,N49,N50,N55,**N71** — levels 0, 0→1, **1→2** cleared; the shell tier's review engine

**External block:** OOP ← N19,N21 — 2026-2학기 via Java (weeks 4–10). **N63's template/instance distinction is an early sighting**

**Encompassing edges:**
- N61 Bandit ⊇ N55{1.0}, N44{1.0}, N46{0.9}, N47{1.0}, N48{0.8}, N49{0.8 *only when a level hides a file* — did not fire Jul 30}, N50{0.9}, N42{0.7}, **N71{0.8 when a level touches stdin}**
- **N71 ⊇ N42{0.6}** · **N46 ⊇ N43{0.8}** (unchanged weight; second job noted in Part A, not a new edge)
- **N64 ⊇ port concept{1.0}, N48{0.4}** · **N65 ⊇ N46{0.9}, N70{0.7}, N44{0.5}** · **N66 ⊇ N65{0.8}, N63{1.0}**
- **N67 ⊇ N48{0.9}, N44{0.6}, N42{0.7}** · **N62 ⊇ N50{0.9}, N42{0.6}** · **N69 ⊇ N42{0.8}, N12/N13{0.6 case-ladder}, N19{0.5 functions}**
- (prior edges unchanged: N40, N41, N49, N50, N60, N59, item3.py, N39, N38, N37, N36, N35, N33, N30, N29, N25, N17, N16, N8, N47, N44, N51, N55, N58)

**Graph-reading notes (Jul 31):**
- **Bandit is paying, but not the debt that's outstanding.** Level 1→2 rode cat, paths, prompt anatomy and SSH at full weight and opened a new node (N71) — but it hid nothing, so **N49's cold rep is exactly where it was.** Levels that hide files are what clears it; don't expect it to arrive on schedule.
- **N71's real value is downstream.** Standard input is the doorway to pipes and redirection, which is where the shell stops being a file browser. Untaught on purpose — it arrives when a level demands it.
- **A new tier opened and produced three nodes in one session** — unusual pace, explained by heavy prerequisite coverage: ports (Bandit), permissions (Jul 24), paths (Jul 14–20), prompt anatomy (Jul 15). Docker's three ideas each landed on owned ground.
- **N70 is the bottleneck for everything media-server shaped.** Taught, zero production, and the SSD is untouched. Nothing about Jellyfin is hard once a mounted folder exists.
- **N68 compose is deliberately gated.** The whole failure mode being avoided is assembly on unproduced components.
- Python tier quiet until ~Aug 3.

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
| **boogiewoogie** (Pi 4B 4GB, Argon ONE M.2) | ALIVE. RPi OS Lite 64 (trixie), kernel 6.18.34. USB-boot (Toshiba 28.9GB), Wi-Fi jini, **192.168.0.9** — also reachable as `boogiewoogie` (resolves to IPv6 link-local). `ssh snakeyboy777@…` — always name the user. **Docker Engine 29.7.0 + compose v5.3.1 installed Jul 31, daemon enabled at boot.** 23G free before Docker. Images on disk: hello-world, nginx |

## Inventory
| Item | Status |
|---|---|
| Pi 4 4GB + Argon ONE M.2 + USB bridge | running (**bridge + SSD still disconnected**) |
| Transcend 128GB M.2 SSD | seller's OS aboard, untrusted; **wipe still deferred — now the media server's blocker** |
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