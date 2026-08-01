# Sessions 20–23 — Chat Record (July 21–25, 2026)

A plain account of everything that happened across this chat: four sessions, one program restructure, a rename, a store run, a class syllabus, and the opening of the cyber track. Written to be read, not to be a ledger.

---

## Session 20 — July 21 (day 26)

A two-block day under the (now-retired) doubling trial.

### Block 1 — Generators

Acquisition mode, two ideas.

**Idea 1: a generator is a promise.** A comprehension is a factory that runs the whole line immediately and hands you the finished list. A generator is a chef who takes the order and cooks one plate only when asked. The one-character move: swap `[ ]` for `( )` on a comprehension and the same recipe becomes a generator — nothing computed yet, nothing stored, just a promise of values.

Three facts, all the same fact wearing costumes:
- **One-time use.** Loop a generator twice; the second loop prints nothing (silence = empty this time, not success). The word is *exhausted*.
- **No `len()`.** `len(gen)` raises TypeError — a promise has no contents to count, and Python refuses to run the whole thing just to answer.
- **Prints as a machine.** `print(gen)` shows `<generator object ...>`, not values — same family as the `g.read` printed-machine bug.

**Idea 2: `yield`.** The function version. `return` ejects (halts, hands back one value, dies). `yield` pauses (hands back one value and freezes in place, local variables intact, wakes on the next line when asked again). First machine met where locals survive between calls.

**Predictions:** exhaustion trap called correctly; `len()` reasoned to a crash (TypeError chosen by the machine); a countdown generator's output predicted 4/4 including the timing of a trailing `print("Liftoff!")` — it fires during the final "ask," as the chef's dying words, not after the loop.

**Production (cold, from blank):**
- `production.py` — a generator expression over real screen-time data, plus a deliberate two-loop exhaustion demo. Sidestepped the old colon-in-token problem by indexing position 2 instead of splitting on `": "`.
- `production2.py` — a `yield` count-up machine, an original adaptation of the countdown skeleton. First run yielded only two values; **self-audited against the "at least three" spec and fixed it** (bumped the data), without being flagged.

Ruling: **generators → produced-once.** Both forms, cold, first drafts correct.

### Block 2 — Review build (`review.py`)

A repetition-compression build touching the count accumulator, record-keeper, split-then-index-convert, and the day-old generator node all at once. Fake study-log data provided (`monday: 45` … `friday: 60`), expected `5 / 310 / thursday`.

The working draft got it right — **three spot-check clocks paid in one pass.**

Then the refinement arc, which fought back:
- A detour where looping over `log` (a *string*, not the list) printed one character per lap — the wall of `['m'], ['o'], ['n']`. New fact met live: **strings are iterable, character by character.**
- A NameError, repaired solo.
- The generator made genuinely load-bearing (an earlier draft built it and never used it).
- The final draft hit a **wild exhaustion trap**: two generators chained over one source, the second born already exhausted, silent blank output where "thursday" should have been. The exact species from that morning, caught in the wild four hours later.

Underneath it was a real design tension the spec created — "convert in the recipe" and "print the day label" pull against each other, because a generator yielding bare numbers has thrown the label away. The escape (taught, not drilled): make the recipe yield a small list, `[data[0], int(data[1])]`, keeping both.

"I give up" was called — after the work, not instead of it. Logged as a full honest rep: three drafts, solo repairs, a genuine wall, and the dues already banked.

**Afternoon:** math. Ledger printed.

---

## Session 21 — July 23 (day 28)

(July 22 was a zero day — third on record, counted honestly.)

### Block — find & grep

Acquisition mode. The division of labor: **find locates files by name and property (reads the labels); grep searches inside files (reads the papers).**

find anatomy: the program, a starting point (`.` = here), and a condition (`-name "..."`). Wildcards: `*.txt` = any name ending in `.txt`.

What actually happened was a real search problem, not a clean demo:
- First run searched home (`~`), not `/c/Python` — a **fresh shell starts at home**, and the predictions were written for the wrong room. The command searched the entire Windows user profile instead.
- That surfaced the **Permission denied wall** — find reporting locked doors (AppData, Temp) and calmly walking past them. First taste of permissions, arriving early.
- Re-run with an explicit starting point (`find /c/Python -name ...`). The find-native habit: the starting point is just an argument; where you stand doesn't matter.
- The lost file: `hack3.py` wasn't found by exact name. Not because it was deleted — because it was never named that. Hypotheses (deleted vs. renamed), wildcard nets (`*hack*` found hack1/hack2/hack2b in 5th,July; `*streak*` found only the log), a full `*.py` census, narrowed to 19th,July.
- **grep** then identified the file by its *contents* — `grep "streak" 19th,July/*.py` lit up `item3.py`, its architecture (the fencepost `gap.days + 1`, the index-7 gate, the "a" append) readable from the matching lines alone. Archaeology by grep.

Lessons banked:
- **Shell expansion** — the shell rewrites your line (expands `*`) *before* the program launches, so wildcards work with every command for free. Corollary: `rm *` is already an explicit list of every file by the time rm sees it.
- **grep prints the whole matching line**, not just the search word — the surrounding line is the evidence.
- **An empty result answers the question you asked, never the question you meant.**

### Program restructure

Declared: **CS (Python + Linux) moves to a supporting role; mathematics takes the primary daily slot.** Refined to a concrete shape: **one solid CS block per day**, not minimized, day count continues, ~40 days to summer break. The doubling trial was superseded (not failed) — its data archived. The block picks itself by the queue: due reviews first, frontier or production otherwise.

Ledger printed.

---

## Session 22 — July 24 (day 29)

### Block — generator rep + permissions

**Generator rep (paid):** a birth-rate dataset, a generator expression feeding a min-tracker. Hit **`int("6.4")` → ValueError** — the gotcha that `int()` fed a *string* demands integer-shaped text, while `int(6.4)` fed a float works fine, and `float()` accepts both. Three repair attempts each pointed at the wrong spot (a `type()` check against a string that only looks like a float; a bare `float()` whose return value fell on the floor; a bare `round()`, same discard). The real fix was one word: `float()`. **Unprompted win:** while fleeing the conversion bug, the max-tracker mistakenly named `lowest` got rebuilt into a genuine min-tracker (`<`, seed 1000 chosen to lose the first comparison) — a lying-name design bug fixed that nobody had flagged.

**Permissions (taught + guided run):**
- Three verbs (**read / write / execute**) that mean different things for files vs. directories — for a directory, execute means *enter* (a door key, separate from the list-contents light switch).
- Three audiences (**owner / group / others**), nine switches per file.
- Reading `ls -l`'s ten-character tag by position: type, then owner's rwx, group's rwx, others' rwx. A dash means no.
- **Identity resolution is the elif ladder**: owner? then group? then others? — first match wins, even when it loses you the file.
- `chmod` grammar: who (`u/g/o/a`) + what (`+/-`) + which verb (`r/w/x`).

Predictions 3/3 on mechanism, including the trap: `drw-rw-rw-` — every switch says yes to something, but with no `x` anywhere it's a furnished room nobody can enter.

The run on boogiewoogie (which restarted the idle SSH review engine): a fresh file is born `-rw-rw-r--` (no execute by default; social, not private). `chmod u-r` was surgical — one switch changed, seven untouched. Then the heart of it: **the owner, standing in their own home, locked out of their own file.** Ownership isn't power; the tag is the law. What ownership grants is the right to *change* the tag, never to bypass it. (Root is the only actor the checks wave through — the whole meaning of `#` vs `$`.)

Ruling: **permissions → taught with guided evidence.** The Bandit wall dropped to zero ideas thick.

**Live bonus lesson (free):** `ssh boogiewoogie` with no username defaulted to the *local* Windows username (주현준), which doesn't exist on the Pi — three correct passwords refused, the prompt naming exactly who was being turned away. `user@machine`'s left half is whose identity you're claiming.

### Life logistics — the Eleparts pickup

The camera, PIR sensors, jumpers, and 방열케이스 had been paid for since July 17 and were sitting at the 가산디지털단지 pickup counter. Checked the pickup hours (close 16:30), the KakaoTalk confirmation, and the SMS history — a "준비되었으니 16시30분까지 방문해주십시오" text from July 20 confirmed the order was ready. Round trip ~50 minutes with comfortable margin before close. **Went and got the parts.** Logged as inventory-in only; hardware track stays paused.

(Ledger wasn't printed this session — left mid-close for the store run.)

---

## Session 23 — July 25 (day 30)

### The rename: "streak" → "day count"

Caught a real inaccuracy: the number was never a streak. `item3.py` computes `gap.days + 1` — a date subtraction that counts calendar days since June 26 and never checks whether any given day was worked. Three zero days (July 9, 11, 22) all passed through it untouched. So "streak 24" always meant "day 24 of the program." Chose to **rename the count to match the math** — "day N of the program," no asterisk needed. (The variable, the printed string, and the `streak_log.txt` filename are still an optional two-minute cleanup, filed not assigned.)

### The Java syllabus

Reviewed the syllabus for next semester's 프로그래밍언어 (AAK10076-40, IT경영 교필) — and it's **Java, not Python**. The disappointment was fair, but the week-by-week table hides something: **weeks 4–10 are seven weeks of object-oriented programming** (classes, methods, overloading, constructors, inheritance, access modifiers, overriding, abstract classes, interfaces, polymorphism). That's the OOP block already filed as the "post-camera mountain" — now externally scheduled, with a vehicle and a deadline. Weeks 1–3 map onto the existing fluent tier in Java clothes; weeks 11–12 (files, streams, exception handling) are owned concepts in new grammar. The course is build-and-present shaped (발표 25%, team project) with a hard attendance rule (1/5 absences → F). Filed as a scheduling fact; pre-study vs. walk-in-cold is a decision for later.

### Bandit — the cyber track opens

**What Bandit is:** the beginner wargame from OverTheWire — a legal, deliberately-vulnerable practice server. A ladder of numbered levels, each with the same shape: a password is hidden somewhere on the machine, and finding it (with ls, cd, cat, find, grep, and permissions) unlocks the next level's login. It's the exact proving ground the shell tier was built for, and the gate the cyber track sat behind.

**New concept: port.** One machine has many numbered doors so incoming connections reach the right service. SSH's default is door 22 (used silently on every prior connect); Bandit runs its SSH on 2220, named explicitly with `-p 2220` — the same flag grammar as `rm -r` and `ls -l`.

**Level 0 — cleared.** `ssh bandit0@bandit.labs.overthewire.org -p 2220`, fingerprint prompt, blind password entry. Read the banner as real intelligence: `/etc/bandit_pass/` holds every level's password, each readable only by its own user — the permissions tag system *is* the game's spine, announced in the welcome text.

**Level 0 → 1 — cleared.** `ls` showed a file in the home directory; `cat` on it revealed the level 1 password. (Structural prediction given where memory held no evidence — the honest form of prediction.)

**Logged in as bandit1.** The cyber branch is live — a place that's been visited, not a gate.

Two-session ledger printed.

---

## Where things stand at the end of this chat

- **Day 30 of the program.** Single CS block per day, math primary, ~38 days to summer break.
- **Python:** every node has production evidence; all clocks expanding. Generators produced and rep-paid. Only work due soon is tomorrow's two fluency defenses (N40 ≤15:00, N41 ≤12:00, fresh domains) — the first live test of judging days by effort when a defense might miss.
- **Linux/shell:** find/grep and permissions both taught; their cold reps will arrive as by-products of Bandit rather than as assignments.
- **Cyber:** Bandit entered, levels 0 and 0→1 cleared, sitting as bandit1. Bandit is now the shell tier's live review engine.
- **Hardware:** paused by choice; all V1 parts now physically in hand (camera, 2× PIR, jumpers, case). Resumes on the word.
- **On the horizon:** Bandit 1→2 onward · the OOP mountain arriving via Java in September · the Telegram alert hack still unbuilt and hardware-free · the optional `item3.py` / `streak_log.txt` rename cleanup.

The through-line of these four days: the shell tier stopped being something practiced in isolation and became something *used* — on a real lost file, on a real Pi, and finally on a stranger's machine that was actively hiding things. Everything the fluency work was for.
