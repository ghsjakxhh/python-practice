# Week 1 — Python Foundations (June 26 – July 3, 2026)

Seven sessions in eight days, one per day, every one committed and pushed to GitHub (`python-practice` repo). Method: the daily loop — **predict → run → investigate → modify → make** — where every session ends with rebuilding the concept from a blank file.

---

## The sessions

### Session 1 — Variables, strings, f-strings
**Concepts.** Assigning values to variables. Strings vs integers. F-strings: the `f` switches a string into fill-in-the-blank mode, and `{ }` marks live code whose *result* gets dropped into the text — without the `f`, everything in quotes is dead literal text. `.upper()` uppercases a string. `len()` counts every character in a string — including spaces and punctuation.

**Mistakes / lessons.**
- Predicted `len("Resident Evil")` = 12. It's 13 — the space counts. First taste of "the machine's counting isn't your eye's counting."
- In the Make (`make.py`): typed `sice` instead of `since`. Ran fine — Python never reads inside the quotes. Errors catch broken code, never broken English.
- Hardcoded `2026` in the age math — correct only this year, silently wrong next year.

**Also this session:** first `git init`, first commit, first push. Learned Git = save points (commits) on your machine; GitHub = the cloud copy (push). The three-step pipeline: `git add .` (stage) → `git commit -m "..."` (snapshot + label) → `git push` (upload). Commit messages describe the *change*; code comments (`#`) describe the *code*.

### Session 2 — Lists, for loops, enumerate
**Concepts.** Lists store items by position, counted from **0**. A `for` loop walks every item. `enumerate(list)` tags each item with a counter; `for number, task in enumerate(...)` fills the two variables **by position** — the first always catches the counter, names are irrelevant to Python. `enumerate(list, 1)` sets the start of the count (default 0); the counter then steps +1 on its own, because that's what counting is. `len()` on a list counts items — same idea as on strings, new container.

**Mistakes / lessons.**
- Deliberately swapped variable names (`for task, counter in ...`) to probe how unpacking works. Confirmed: Python fills by position, names are for humans. Corollary: names that lie (`task` holding a number) are landmines in real code.
- Initial confusion between the two `+1`s: the hand-written `{index + 1}` display fix vs. the counter's automatic stepping. They're unrelated — the stepping is built in.
- Confusion about why `print("len(backlog) games...")` wouldn't work — resolved via the `sice` lesson: inside plain quotes everything is literal; only `f"...{ }"` evaluates.

### Session 3 — Functions, return, round()
**Concepts.** `def` packages logic into a reusable machine: define once, call many times with different arguments. The function **returns** a bare value; `print` assembles the sentence around it. Return ≠ print. `round()` rounds to the nearest integer.

**Mistakes / lessons.**
- Deleted the comma in `print(days_to_finish(70, 2), "days...")` → `SyntaxError`. The comma is the argument separator; without it Python can't parse the line at all. New rule: **inside quotes = text zone (never parsed); outside quotes = code zone (strict grammar, every symbol load-bearing).** Bonus: the comma also inserts the space between printed arguments.
- Flagged for later: Python's `round()` uses banker's rounding — a perfect .5 rounds to the nearest *even* number (`round(2.5)` → 2).

**Bug species so far:** (1) SyntaxError — won't run at all. (2) String typo — runs, output is wrong English.

### Session 4 — Conditionals: if / elif / else
**Concepts.** Branches are checked **top to bottom; the first True one wins** and everything below is skipped. Therefore: **specific conditions before broad ones**, or the broad branch swallows everything. Boundaries are exact: `<= 3` includes 3; `<` doesn't.

**Mistakes / lessons.**
- Ran the reorder trap: putting `<= 7` above `<= 3` made the URGENT branch **unreachable** — dead code, no error, wrong answers.
- Phrasing slip: said the function "prints" a string when it **returns** it.

**Make:** `rest_day(fatigue)` — a sprint-training rest-day checker. First Make pointed at real life instead of games.

### Session 5 — While loops
**Concepts.** A `while` loop repeats until its condition flips False, re-checking every lap. The decrement inside the body is the engine of escape. The last lap runs at the last True value; exit happens at the *check*. `>` vs `>=` moves the finish line by exactly one — the classic **off-by-one** error. Loop variables **outlive the loop** and keep their final value.

**Mistakes / lessons.**
- Triggered the infinite loop on purpose (deleted the decrement), watched it spam, killed it with **Ctrl + C**. Bug species #3: runs *forever*, no error.
- Boundary probe: `>= 0` adds one extra lap and leaves the variable at −1 after exit.

**Make:** `make5.py` — three-phase summer-break countdown (60 days, escalating dread), three `while` loops passing one variable as a baton. Invented, not assigned.

### Session 6 — while + if/elif combined
**Concepts.** One loop with the decision *inside* it: sixty laps, each re-asking "which phase am I in?" Structure went from three sequential tunnels to one tunnel with a switchman. Scales better: a new mood = one `elif`, not a new loop. Pattern: **decide (assign `mood` in the branches), then act (one shared print)**.

**Mistakes / lessons.**
- Reorder trap at scale: broad-first ordering corrupted 30 of 60 lines — silently. Named it correctly: **dead code**. Confidently-wrong output is the dangerous kind; nothing crashes, nothing warns.
- Retention rewrite of session 1 surfaced bug species #5: **correct code, wrong data**. `released = 1990` (placeholder; real answer 2001) — flawless logic, false output. The original file had the same disease (`1996` left over from Resident Evil). Twin rules: Python won't fact-check your numbers, won't proofread your strings ("That make" — `sice`'s cousin), and won't remember which values you never meant. Professionals mark placeholders (`# TODO`, absurd values like 9999).

**Make:** `make6.py` — code-level status meter, 0 → 100. First count-up loop. Correct `<=` ladder (narrowest tier first). Caught the sneaky count: 0 through 100 inclusive = **101 iterations**.

### Session 7 — Dictionaries
**Concepts.** A dictionary stores **by name, not position**: keys point to values, `hours["RE4"]` asks for RE4's number directly. Reading: `d[key]`. Updating: `d[key] = d[key] - 15` (read–modify–write, same shape as the loop decrement). **One write syntax for update *and* create** — `d[key] = value` overwrites if the key exists, creates the pair if it doesn't. The asymmetry: **writing to a missing key creates it; reading a missing key crashes** (`KeyError`). `len()` counts pairs — third container, same idea. Bonus pointer: `sum(d.values())` totals the values.

**Mistakes / lessons.**
- Trace error: assumed "Silent Hill 2" was already a key (it wasn't — memory merged the diagram with the code). Logic was flawless *from a wrong premise*. Rule earned: **look, don't recall** — re-read the source before tracing; never trust memory of something on screen.
- Bug species #6: the **runtime crash**. Perfect grammar, runs fine, prints four lines, *then* dies mid-flight on the missing key. A crash + traceback is not "printing an error" — output is on purpose; a traceback is a crash report.
- In the Make, forgot the create syntax and tried `PC_Build["Headphone": 50]`. Two lessons: (a) **braces build, brackets access** — `key: value` colons live only inside `{ }` literals; all later writes use `=`; (b) the baffling error (`unhashable type: 'slice'`) happened because the wrong syntax accidentally spelled a *different valid thing* (a slice). **Error messages describe what Python thought you meant, not what you meant.**

**Make:** `make7.py` — PC build budget (GPU/CPU/Monitor/RAM), read + update + create demonstrated.

---

## The bug species collection (six so far)

1. **SyntaxError** — grammar violation outside the quotes; never runs. (missing comma)
2. **Silent string typo** — runs fine, prints broken English; quotes are never proofread. (`sice`)
3. **Infinite loop** — runs forever, no error; kill with Ctrl + C. (deleted decrement)
4. **Wrong branch order** — runs, silently picks wrong answers; dead code. (broad before specific)
5. **Correct code, wrong data** — flawless logic launders bad input into confident lies. (1990/1996)
6. **Runtime crash** — valid code dies mid-run asking for something that isn't there. (`KeyError`)

## Conventions ignored (and the fix)

- **`PC_Build` → `pc_build`.** PEP 8, Python's style guide: `lowercase_with_underscores` for variables and functions, `CapitalizedWords` for classes, `ALL_CAPS` for constants. Casing tells a reader what kind of thing a name is. (Everywhere else — `days_left`, `reps_left`, `code_level` — the convention was already followed by instinct.)

## Recurring principles

- The machine is **literal and exact**: spaces count, counting starts at 0, `<=` vs `<` moves the line by one, boundaries are where sloppy sentences become bugs.
- **Names are for people, not the machine** — position and syntax are all Python sees.
- **Look, don't recall** — verify the source before reasoning from it.
- Predicting code and producing code are different skills; the Make step exists because traced-and-understood isn't the same as in-your-fingers.
- Every session ends in a commit: green squares = visible proof of showing up.

---

## The roadmap

### Big picture (12 months, ~1–2 hrs/day)

| Phase | Months | Domains |
|---|---|---|
| Block | 1–3 | Python (tiny scripts → small apps) + Cyber prep in parallel |
| Interleave | 3–6 | + Robotics (micro:bit → Arduino → ESP32), + Web (HTML/CSS → JS → small app) |
| Full interleave | 6–12 | All four running together |

Cyber path: Bandit → TryHackMe → PicoCTF → Hack The Box. Python and cyber block together first because they're the same muscle (Python + Linux); robotics and web phase in once mixing helps instead of overwhelming. ROS 2 deferred until much later.

### Session-level spine

| Sessions | Topic | Status |
|---|---|---|
| S1–3 | Variables, lists, loops, functions | ✅ done |
| S4–6 | Logic: if/elif/else, while, both combined | ✅ done |
| S7–9 | Dictionaries + error handling (try/except) | S7 ✅ — S8 next |
| S10–12 | Files, imports, libraries (datetime) | — |
| S13–15 | **Cyber begins:** Linux + OverTheWire Bandit | — |
| S16–18 | TryHackMe path + Python projects | — |
| S19+ | Branch out: robotics, then web | — |

The spine is a direction, not a contract — compress if a block is easy, slow down if one fights back.

**Next up: Session 8 — `try/except`.** The KeyError stops being fatal.
