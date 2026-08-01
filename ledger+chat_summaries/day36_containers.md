# Day 36 — Containers: Docker installed, three ideas produced (July 31, 2026)

**Primary reader: Claude.** 현준 rarely reads these files. Continues `session25_burst_and_networks.md`. `ledger.md` (2026-07-31 print) is authoritative for state; this is the narrative record.

⚠ **Session number uncertain.** Records jump from Jul 27 (day 32, S25) to Jul 31 (day 36). Whether sessions ran Jul 28–30 is unknown to Claude. Labeled by date and day count throughout; reconcile the session number against the real file.

One chat, split by a long gap: a reading morning (~10:40–11:40) and a production afternoon (~14:20 onward). A new tier opened and produced three nodes in a single day.

---

## PART 1 — THE MORNING: a movie library, and where it went

**His opening:** "Can I make a movie library with my Raspberry Pi 4?" Answered yes — a **media server**, the classic Pi 4 job, same "24/7 always-on server" family as the filed Pi-hole and WireGuard ideas.

Taught from zero, his standard:
- **Media server** = a program holding video files and serving them over the network to client devices.
- **Jellyfin vs Plex** — Jellyfin recommended on his own posture (he declined Pi Connect for having a middleman; Plex is account-based and partly cloud-connected).
- **Transcoding** = the one real ceiling. *Direct play* ships bytes and the client decodes (Pi 4: effortless). *Transcoding* re-encodes in real time when the client can't play the format (Pi 4: roughly one stream, badly at 4K).
- Storage: the Transcend 128GB SSD is the obvious home, once wiped.

**"I want to do this now. I make huge strides in progress whenever I'm motivated like I am right now. Let's do this."** — the pause on the *media-server use* of boogiewoogie lifted on his word. Camera track untouched, still paused.

Four-phase plan given (storage → Jellyfin → files across → clients), boot-order trap flagged (SSD and Toshiba stick are both bootable USB; plug the bridge in while the Pi runs), and step 1 assigned: SSH in, `lsblk`, predictions first.

**Then the block didn't start for four hours.** What happened instead was a chain of questions, each reasonable, none of them a command:

Radarr → what does Jellyfin do then → why can't I use Radarr → explain the indexer/download-client pipeline → a Reddit post → what differs from a pirating setup → what does "acquisition" mean → the dev-smurf GitHub repo → Docker → Docker's system requirements → external storage requirement → how do I install Docker → explain Docker like I'm 5 → what am I looking at on GitHub → how do I install Docker (repeat).

Real vocabulary was acquired. Zero atoms were banked. This is burst-arrival spent on decision cost and adjacent reading — the exact failure mode burst mode was designed to kill — and it was named to him once, plainly, without a story about why.

---

## PART 2 — THE RADARR / REPO RULINGS

### What was explained (freely, as systems knowledge)
- **Radarr** = a movie collection manager and **orchestrator**. It never downloads anything itself; it coordinates an indexer, a download client, and its own import step. Port 7878. Part of the \*arr family (Sonarr/Lidarr/Bazarr/Prowlarr).
- **Release** = one specific packaging of a film (resolution, encode, size, audio), not "a movie." Forty releases per film; the pipeline exists to pick one.
- **Indexer** = the search layer; a catalog answering "does this exist and where," returning metadata plus a *pointer* (magnet link or .nzb), never the file. The DNS-phonebook shape again.
- **Download client** = the dumb competent pipe that speaks the transfer protocol (qBittorrent/Transmission for BitTorrent, SABnzbd/NZBGet for usenet).
- **The glue** = HTTP APIs on ports, wired with API keys. Each service independent, each on its own port, composed by one orchestrator. Named to him as **service-oriented architecture** — the transferable lesson, and why the Bandit port concept keeps paying rent.
- **The folder is the entire interface** between Radarr and Jellyfin. They never talk. Same decoupling as a function returning a bare value and the caller assembling the sentence.

### What was declined, and how
Stated once, then held without re-litigating: **Claude will not wire up the indexer-plus-download-client pipeline**, because in its standard configuration that is automated acquisition of copyrighted films.

The repo he brought (`dev-smurf/Raspberry-Pi-4-Media-Server`) made it unambiguous rather than a judgment call, and the reasoning was given from the artifact:
- **Gluetun** routes all container traffic through a commercial VPN — present so the ISP can't see torrent traffic.
- **FlareSolverr** exists to defeat Cloudflare bot protection on indexer sites.

Neither has a legitimate-library reading. Ruling: no help standing that repo up, including walking its compose file.

**He pushed back twice** — "I'm not going to be pirating movies" and later "No. I am building it. I'm just building it to learn how to use my Raspberry Pi 4." Both taken at face value; the ruling restated as being **about the artifact, not the person**, and then dropped. Not raised again unprompted for the rest of the chat. (Also honored: when he later asked "would these updates help me build the whole media server," the answer explained the generic groundwork and explicitly said the position wouldn't keep being brought up.)

### The separate engineering argument (the one that actually mattered)
Given as advice, not as consolation: **that repo is a bad way to learn the Pi.** `docker compose up -d` on a stranger's file starts nine containers and teaches nothing; when one breaks he'd be debugging an unfamiliar service inside an unfamiliar runtime behind an unfamiliar network layer, with three things lying to him at once. **The July 8 collapse in Docker clothes** — assembly on unproduced components, which his whole protocol exists to prevent.

The counter-path proposed and eventually taken: one container by hand → a second → compose when they need to talk.

**Filed as the genuinely good part of that repo:** its Flask dashboard (`app.py`, `index.html`) — a Python status page for boogiewoogie, his language, opens pip/HTTP (N52/N53), hack-series shaped.

### Vocabulary collision, corrected
He asked what "acquisition" meant. Two senses had collided: **acquisition mode** (his curriculum's word for learning new material) vs plain-English acquisition (getting the files). Named, apologized for once, and the word ceded back to him — "downloading" used thereafter.

---

## PART 3 — READING THINGS: two guided tours

### Docker and Compose, explained twice
First technically, then — on his request — **like he's five**, which is the version that landed:

- **A container is a lunchbox.** Normally a program needs the host kitchen to already have the right flour, eggs, and pan; if two recipes need different flour, one loses. A container packs the whole meal sealed: program, libraries, files, its own slice of filesystem. The computer just heats it.
- **Docker runs one lunchbox.**
- **Compose is the note describing many lunchboxes** — which boxes, which doors, which folders, what order — plus something that follows the note. Not a bigger Docker; written instructions.
- **The one leak, said once so it wouldn't bite later: boxes forget.** Anything written inside a box vanishes when the box is thrown away, which is why compose files map real folders in. This was said hours *before* he proved it himself — worth noting that the pre-taught fact didn't stick and the experiment did.

Also taught: `docker-compose` (hyphen, v1, deprecated) vs `docker compose` (space, v2 plugin) — the README he was reading mixes them incoherently.

### GitHub, the site (his question: "I've been pushing code for a while but never personally used GitHub")
Full surface tour off the dev-smurf page: owner/repo address · public vs private · the commit row (message, short hash, total count = green-squares data in written form) · the file list's hidden third column (each file's last-touching commit) · branches and tags · **the README mechanism** (GitHub renders a top-level file literally named `README.md`) · stars/forks/issues/pull requests/watching/contributors · the languages bar computed by byte count · **MIT license, and that public ≠ free to use** — unlicensed public code is still copyrighted by default.

Two observations he could act on: **his `python-practice` repo has no README**, so it presents as a bare list of dated folders; and the languages bar revealed that the "media server" repo is entirely config plus dashboard — one contributor, none of the nine services is that person's code.

---

## PART 4 — THE BLOCK (afternoon)

Guided acquisition throughout, predictions before commands, reconciliation after.

**1. Catalogue and prerequisites.** `sudo apt update` → 14 upgradable. `sudo apt install -y ca-certificates curl` → both already newest (**predicted correctly**). Read from the output: `Hit:` vs `Get:`, the `archive.raspberrypi.com` feed alongside Debian's, and **`Not Upgrading: 14`** as apt declining to touch what it wasn't asked about. Then `full-upgrade` cleared the backlog.

**2. `df -h`** — first new command. Definition taught from zero on request: disk free, `-h` human-readable, **reports per *filesystem*, not per folder**, six columns ending in the **mount point**. Tied back: the seller's July screenshot (`/dev/sda2 469G` on `/`) was a `df` line, and one line settled a hardware question about a stranger's machine.

- **Prediction:** "Two rows — one the Pi's storage, one the USB stick. About 28GB free."
- **Correction given before running** (it was a factual misconception, not a scoreable guess): **the Pi 4 has no internal storage at all.** No drive, no eMMC. Flashing removable media *is* installing the OS.
- **Actual:** `udev` + seven `tmpfs` + `/dev/sda1` (505M → `/boot/firmware`) + `/dev/sda2` (28G → `/`, 23G free, 15% used).
- **He identified sda2 as the stick and the tmpfs rows as RAM** — correct, and the good half. Two refinements: seven tmpfs not six, and **`sda1` is also the stick**. Taught: **`sda` = the device, the number = the partition.** One disk, two slices, two rows. Flagged forward: the SSD will appear as `sdb`, partitions `sdb1`/`sdb2`, and **getting letter-vs-number backwards is how people wipe the wrong drive.**

**3. `curl -fsSL https://get.docker.com -o get-docker.sh`**

- **Prediction #1 (does it print anything) was VOID — Claude's error.** The answer had been spoiled two messages earlier while explaining that `-s` means silent. Struck from the record, named as Claude's fault, new conduct rule attached.
- **Prediction #2:** "A directory that has the Docker program." **Miss on both halves**, and both useful:
  - It's a **file**, not a directory — no trailing `/`, no color. His own July 18 lesson (markers tell the truth, names don't) applied to his own `ls` output.
  - It's the **script that installs** Docker, not Docker. Recipe vs meal — the same distinction waiting for him in image-vs-container an hour later.
- Also visible in that `ls`: `perms_test.txt`, the file he locked himself out of on July 24, still sitting there unread.

**4. `cat get-docker.sh` — read before running as root.** The habit, deliberately practiced rather than skipped. He then asked what language it was, which produced an unplanned and valuable sub-lesson (Part 5, N69). The file's own closing comment turned out to document the `curl | sh` truncation hazard and the wrap-in-a-function defense — the exact risk that had been flagged when the two-line form was chosen over the pipe.

**5. `sudo sh get-docker.sh`** — Docker Engine **29.7.0**, compose plugin **v5.3.1**, arm64, built the day before. The `+ sh -c` prefixes read as a **`set -x` trace**: the script narrating each command before running it. Read line by line with him: GPG key fetched to `/etc/apt/keyrings/docker.asc` then **`chmod a+r`** (his permissions node, live — the key must be world-readable for apt to verify signatures); repository written to `/etc/apt/sources.list.d/docker.list` tagged `arch=arm64 signed-by=…`; then the install. The script also ran `systemctl enable --now docker` itself, so that step was skipped.

**Client and Server both reported** → the architecture named: `docker` is a client talking to a root daemon. Which is exactly why the installer's closing warning says API access equals root on the host.

**6. `sudo docker run hello-world`** — the pull cycle read in full:
- `Unable to find image … locally` = the local check that precedes any download
- **registry** (Docker Hub), `library/` namespace, **tag** (`latest` is a conventional string, not a guarantee)
- **layer** (`58dee6a49ef1: Pull complete`) — an image is a stack of read-only filesystem diffs; shared layers download once
- **digest** — a content hash, same job as a git commit hash. Tags move; digests never do.
- **`(arm64v8)`** noticed in the container's own message — images are architecture-specific, which is why "does this have an ARM build" is a real question for anything he pulls later.
- **Image vs container** stated plainly: template vs running instance. **One image, many containers — the OOP class/object shape, arriving early via Java in September.**

**7. `docker images` / `docker ps -a`** — his prediction was "100? 7? 5? I don't know" and "I don't know what `ps -a` does. Maybe?" Not scored; instead the derivation was shown (one image pulled tonight = one row) and `ps` defined (process status; `-a` = include stopped). Output read: one image, **22.6kB disk vs 10.3kB content** (layers plus metadata exceed contents), and the corpse — `Exited (0)`, named `zealous_nash`.
- **Exit code taught:** zero = success, nonzero = failure, every Unix program does it, it's how `&&` decides. The container **completed**, it didn't crash.
- **A stopped container isn't gone** — it's an object taking space until removed, which is how people accumulate fifty of them.

**8. The sudo/socket wall — and the teaching failure.** He asked why `sudo` is needed. The full mechanism was given: the daemon is reached through a **Unix socket** at `/var/run/docker.sock`, which is a *file*, so the permissions tag is the law; `srw-rw---- root docker`; identity resolution walks owner→group→others and he lands on others.

**Response: "Shit. This is hard stuff. I don't know what you're talking about."**

The repair that worked was dropping the mechanism entirely:
> There's a door. Behind it is the daemon. The lock's rule: root gets in, and anyone in the group `docker` gets in. You're neither. Two ways past: borrow root's key per command (`sudo`), or get your own key permanently (join the group). **Honest recommendation: just keep typing `sudo`.**

He continued immediately. **The over-explanation was the failure, not the confusion** — the socket/ladder detail was accurate, unasked-for, and load-bearing for nothing he was doing. Also flagged once and left alone: `usermod -aG docker` is **root-equivalent** (mount the host filesystem into a container, read anything, no password) — declined for now, filed as a cyber-relevant thing to recognize from the other side of the table.

**9. Port mapping — first idea, proven externally.**

```
sudo docker run -d -p 8080:80 --name webtest nginx
```

Eight layers pulled (a real image, unlike hello-world's one). `-d` returned a container ID and the prompt immediately. **Prediction hit:** he called that it would pull — and the derivation was his own `docker images` output showing nginx absent.

`docker ps` read: **`Up 2 minutes`** against hello-world's `Exited (0)` — the difference between a program and a service. PORTS column parsed: `0.0.0.0:8080->80/tcp` as "arrives at, forwards to," `0.0.0.0` meaning every address the Pi has (which is why another machine can reach it), plus the `[::]` IPv6 row.

Then **the browser on Windows at `192.168.0.9:8080` loaded the nginx page.** His reaction: *"Cool. Not really but it's something I've never done before."* — correct read, and the boring page is boring by design (proof-of-life, same job as hello-world's paragraph).

**10. Volume mapping — second idea, proven live.**

```
mkdir ~/site
echo "<h1>boogiewoogie</h1>" > ~/site/index.html
sudo docker rm -f webtest
sudo docker run -d -p 8080:80 -v ~/site:/usr/share/nginx/html --name webtest nginx
```

`echo` + `>` taught as the shell's `"w"` mode, overwrite danger included. `rm -f` = remove forcefully, with the ~10s polite-shutdown wait explained when he sat waiting at a hung-looking prompt.

Page showed **boogiewoogie** — his own file, served by a container that has no idea it's reading outside its own box.

- **Prediction #1** (what the page shows): unknown, honestly given. Fine — nothing to reason from yet.
- **Prediction #2 (his, unprompted): "It's going to change. I don't have to rebuild the container."** → `echo "<h1>this is a test</h1>" > ~/site/index.html`, refresh, **page changed. HIT.**
- Lesson named: **the mount is a live window, not a snapshot taken at startup.** Nginx re-reads the real file every request. This is precisely the mechanism that would let Jellyfin see a drive full of movies without copying anything.

**11. `docker exec -it` — inside the box.**

```
sudo docker exec -it webtest bash
```

Prompt flipped to `root@4428ad070f5f2:/#` — **the third machine of the night**, and prompt-reading now three deep (Windows `주현준@DESKTOP-HUSTR16` → Pi green `snakeyboy777@boogiewoogie` → container root). The `#` noticed.

`ls` inside showed a **complete Linux tree that is not the Pi's** — its own `bin boot dev etc home lib …`, same shape, entirely different contents. The lunchbox made literal.

- **Prediction:** `ls /usr/share/nginx/html` returns `<h1>this is a test</h1>`. **Corrected before running** — `ls` lists names, `cat` shows contents; the same distinction he already owns from Git Bash. Actual: `index.html`. Surface miss, right idea underneath.

**12. Persistence — third idea, proven by controlled experiment.**

Inside the container: `echo "scratch" > /tmp/scratch.txt`, confirmed with `cat`, then `exit`. Container destroyed and recreated, re-entered, and both files checked.

- **Prediction (his): "I think it will still be there."**
- **Actual:**
  ```
  cat: /tmp/scratch.txt: No such file or directory
  <h1>this is a test</h1>
  ```
- **MISS — and the one worth having gotten wrong.** Container IDs differed (`4428ad070f5f2` → `0a41eed6b32c`): a different object entirely. **What's inside a container dies with it; only what's mounted from outside survives.**
- **Retroactive payoff:** the folder list he'd read hours earlier in that repo — `qbittorrent/ prowlarr/ radarr/ jellyfin/` — stopped being decoration. Every one is a host folder mapped in, because every setting and database would otherwise evaporate on each container recreation, which happens on every update.

Cleanup: `sudo docker rm -f webtest`, `exit`. Prompt back to Windows.

---

## PART 5 — KNOWLEDGE ADDED (compressed for reuse)

**Containers (Tier D, new):**
- Client/daemon split; the daemon runs as root; the socket is a file and the permissions tag is the law; group `docker` = root-equivalent.
- Registry → tag → layers → digest. Image = read-only template; container = instance + writable layer. Architecture-specific images (`arm64v8`).
- **Port mapping** = one door punched through the box wall; `0.0.0.0` = every address the host has.
- **Volume mapping** = a host folder grafted into the container's filesystem at a path it already reads; **live, not a copy**.
- **Disposability** = the container is the throwaway; mounted folders are the only persistence.
- `docker ps` (running) vs `ps -a` (including corpses); exit codes; auto-generated container names.

**Shell scripting (N69, taught off his own screen):**
- **Shebang** — `#!/bin/sh` tells the kernel which interpreter to feed the file to. Comment syntax is what makes it invisible to the script itself.
- **A `.sh` file is the same language as the prompt, saved instead of typed** — the REPL→`.py` move, shell edition.
- `if/then/fi`, `case/esac` (a first-match-wins ladder = his branch-ordering node in new grammar), `$var`, `$(command)` substitution, functions defined then called.
- `set -e` = stop on first failure; there is **no try/except here**, the default is "keep going after an error."
- `set -x` = echo each command before running it (what produced the `+` prefixes).
- Why `sh` not `bash`: `/bin/sh` exists everywhere; a script that must run on any distro writes to the smaller common language.
- **The `curl | sh` hazard** and the wrap-in-a-function defense, found in the script's own closing comment.

**Disks and mounting (N70, taught, no production):**
- `df -h`, six columns, per-filesystem, mount point in the last column.
- **`sda` = disk, `sda1`/`sda2` = partitions.**
- Linux has **one tree** and mount points; Windows has drive letters. **Mounting** = attaching a drive to an empty directory so paths reach it.
- An unmounted drive is powered, present, and unreachable — **existence without an address**, which is the paths lesson again.
- **The Pi 4 has no internal storage.**

**Networking / SSH addendum:**
- `ssh snakeyboy777@boogiewoogie` works; the name requires a resolution step and **that step is the flaky part** (July 18's `.local` timeout). It resolved to an **IPv6 link-local address** (`fe80::…%11`), not `192.168.0.9` — a second addressing system, self-assigned, valid only on the attached segment, with `%11` naming the sending interface.
- DHCP means the IP can change; the name survives it. Use the name, fall back to the IP.
- `Last login: Fri Jul 24 14:31:25 2026` read as the machine keeping receipts.

**Media servers:** Jellyfin's four jobs (watch folders, fetch metadata, serve on 8096, track state per user); filename parsing is why naming matters; transcoding vs direct play as the Pi 4's only real ceiling.

**Service-oriented architecture:** small single-purpose programs, each on a port, each with an API, composed by an orchestrator. Named as the transferable lesson underneath the whole \*arr explanation.

**GitHub:** repo anatomy, commits/hashes, branches/tags, README rendering, forks/PRs as the open-source mechanism, licenses (public ≠ free to use).

---

## PART 6 — RULINGS & STATE CHANGES

- **Tier D opened. N63 images/containers, N67 `docker exec` → produced (guided). N64 port mapping, N65 volume mapping, N66 disposability → PRODUCED, each verified by observation.** N62 client/daemon/socket → taught. **N68 compose → UNTAUGHT, deliberately gated on a second container.**
- **N69 shell scripting, N70 disks/mounting → taught, no production.**
- **N55 SSH** — another rep, first time by hostname, solo.
- **Camera track still paused.** boogiewoogie is in active use again as a container host; that does not resume Tier H.
- **Media server filed as a second Pi project.** Blocked on storage only: the SSD is still carrying the seller's OS, unwiped, unformatted, unmounted. `lsblk` was assigned four times and never run. Boot-order trap still live.
- **The dev-smurf stack: declined, twice, on the artifact.** Not revisited after the second statement.

### The block ruling, and its reversal
At 11:40 the day was ruled **one atom, no block** — an hour of reading, zero commands, nothing produced. That ruling was correct on the evidence available at 11:40.

After the afternoon he pushed back: *"I think it's kind of insane that all of this doesn't count as a block."*

**Ruling changed to FULL BLOCK**, on precedent rather than on pressure: **Session 17 (flash + SSH) was guided acquisition start to finish in a new domain and counted as a full session.** July 31 is that shape — new domain, worked examples, guided production, predictions before commands, real machine state changed at the end. The morning's reading remains context, not credit; the block is the afternoon.

Worth keeping straight for later reads of the precedent: the 11:40 ruling wasn't overturned as wrong, it was **outgrown**.

**By the day-metric:** the reps that ran, ran honestly — predictions first, no peeking, five misses reconciled without flinching. The honest asterisk is that four hours went to deciding and reading before any of them started.

### Predictions, scored
| # | Prediction | Result |
|---|---|---|
| `apt install` prereqs | (implicit) already installed | HIT |
| `df -h` rows | two: Pi storage + stick | MISS — no internal storage; sda1/sda2 are one stick's partitions |
| `df -h` free space | ~28GB | MISS — 23G (OS occupies ~4G) |
| tmpfs identification | the tmpfs rows are RAM | HIT (miscounted six vs seven) |
| `curl` output | *void — Claude spoiled it* | struck |
| `curl` result | a directory containing Docker | MISS ×2 — file not directory; installer not program |
| nginx pull | it will pull | HIT (derivable from his own output) |
| `ls` inside container | the HTML text | MISS — `ls` lists names |
| volume live-edit | page changes, no rebuild | **HIT — his own call, unprompted** |
| persistence | scratch.txt survives | **MISS — the valuable one** |

### Claude errors, on record
1. **Spoiled a prediction, then asked for it.** Explained that `-s` means silent, then asked what `curl` would print. Void, struck, Claude's fault, **new conduct rule attached: a prediction Claude has already spoiled is void and unscored.**
2. **Over-explained the socket/permissions mechanism** into "I don't know what you're talking about." The correct move was the door-and-key model plus "just keep typing `sudo`" — which is what eventually worked. The detail was accurate and unasked-for.
3. The 11:40 ruling was superseded within hours — noted so the precedent isn't misread later as a reversal on pressure.

---

## PART 7 — WORKING WITH 현준 (additions; binding)

1. **When a ruling gets challenged, answer with precedent or hold.** He challenged the no-block ruling directly. The answer was Session 17, cited by name and shape — not a softening, and not a concession to displeasure. If no precedent had existed, the ruling should have stood.
2. **When he says he doesn't understand, delete the mechanism — don't add to it.** "Shit. This is hard stuff" arrived after an accurate three-layer explanation of Unix sockets. What worked: one physical model (a door, a lock, two keys), the practical instruction (`sudo`), and an explicit offer to skip the topic. Same law as papers-and-folders and bedroom/kitchen: **simpler and more physical, not more thorough.**
3. **"I'm kind of guessing here" is not a reason to stop asking for predictions.** He said it repeatedly and produced two hits anyway, one of them (the live mount) reasoned correctly with no prior exposure. What *is* worth doing: separating guesses from derivations, and pointing out when the answer was already in his own output (`docker images` → nginx must pull).
4. **Declining a build doesn't mean declining the domain.** The whole \*arr architecture, service-oriented design, and every Docker concept were taught freely while the specific wiring stayed declined. Restating the position more than twice would have been the error; it was stated, held, and dropped.
5. **Separate the ruling from the engineering advice.** "I won't help with this" and "this is also a bad way to learn" are different claims, and keeping them apart is what let the second one actually land — he took the one-container path.
6. **Reading is not a block, and saying so once is enough.** It was named plainly at the four-hour mark without a story about why, per standing rule. He responded by going and doing the work.
7. **Cross-machine checks stay cheap and worth repeating.** "So I type this in Git Bash?" — the right answer is the prompt tell, every time, no impatience. Three machines were in play by the end of the night.
8. **He asks for the five-year-old version and it works.** The lunchbox model landed where the technical version hadn't. Offer it before he has to ask next time a new abstraction layer opens.

---

## PART 8 — OPEN THREADS

1. **N60 generators due ~Aug 3** — first item on the Python clock.
2. **Container cold rep** (burst menu #4): from blank, no notes — any image, one published port, one mounted folder, verify in a browser, destroy, recreate.
3. **The SSD: wipe → format → mount.** Required for any real media library, independent of Docker. `lsblk` still unrun after four assignments. Boot-order trap unresolved.
4. **Second container, then compose (N68).** The honest path to reading any stack file line by line.
5. **Jellyfin** — one `docker run` with the two flags he now owns, or one `apt install`, once storage exists.
6. **Flask status dashboard** — filed, hack-series shaped, opens N52/N53.
7. Bandit 1→2 · pair-yielding generator cold rep · Telegram hack.
8. **`perms_test.txt`** still sitting locked in his home directory since July 24.
9. `python-practice` has no README — a two-minute fix, filed not assigned.
10. Camera track resumes on his word only.
