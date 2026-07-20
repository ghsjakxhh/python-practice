# Days 8–9 — Error Handling Block Complete (July 4–5, 2026)

Sessions 8 and 9, plus the launch of the **hack series** (hack1, hack2) — the first unassigned, ungraded builds. Squares 11–14 pushed. This document continues `week1_summary.md`; same loop: **predict → run → investigate → modify → make**.

---

## Day 8 review round (before Session 8)

Five prediction questions covering S1–S7. Score: 3/5, both misses mapping to lessons already owned:

- **Miss 1:** predicted `games[1]` *adds* an item. It **accesses**. Rule reinforced: **brackets access — always, on every container.** (Adding to a list is `.append()`, not yet covered.) Diagnosed as the Session 7 trace error in a new costume: flawless logic from a wrong premise.
- **Miss 2:** misidentified a false `released = 1996` as species #2 (string typo). It's **species #5 (correct code, wrong data)**. The distinction matters because they need different proofreading: #2 is caught by reading output as English; #5 only by checking facts against the world.

**New concept stacked during review: looping over a dictionary.**
```python
for game, time in hours.items():
```
Same two-variable unpacking as `enumerate` — filled **by position**, names irrelevant. Swapped names run fine and lie on every line. `total = total + cost` inside such a loop is the mirror of Session 5's `days = days - 1`: **read–modify–write** as the engine of *accumulation* instead of escape.

---

## Session 8 — try/except: the KeyError stops being fatal

**Concepts.**
- `try:` = attempt this block, stand by. The block runs normally until something fails; at the instant of failure execution **jumps** to `except` — everything below the failing line inside the try is **abandoned**, including lines that would have succeeded. The jump doesn't check.
- If nothing fails, `except` is skipped entirely.
- `except KeyError:` is a **specific net for a named species**. It catches only KeyErrors.
- Precise vocabulary (self-corrected, unprompted): errors are **raised**; an *uncaught* raised error becomes a **crash**. try/except doesn't prevent the error — it catches it mid-air. A caught error is a **planned path, not a fixed bug**.

**Predictions: 5/5** including the 8c trap (a valid lookup below the crashing line inside the try never runs).

**Traps.**
1. **Wrong net:** `except ValueError` does not catch a KeyError — the crash sails through a net shaped for a different species. Raised error + no matching net = crash.
2. **Too-big net:** bare `except:` caught a `huors` typo (a NameError) and printed "Not in the library." — a message written for KeyErrors describing a different disease. **A bare except is species #4's evil twin:** broad-before-specific swallows branches in an elif ladder, swallows *bugs* in an except. **Name your exceptions.** Loud and honest beats quiet and lying.
3. **Territories:** `print("Done!")` moved *inside* the try, below the crash line, dies in the jump. Inside-the-try and after-the-try are different territories.

**Trap 2 detour — species #7 discovered: NameError.** Valid grammar, but a name that was never created. Not a missing key in a real container — the container itself doesn't exist. Family portrait of one wrong letter: `sice` inside quotes = silent lie; `huors` outside quotes = fatal. Inside quotes is never parsed; outside quotes every symbol is load-bearing.

**Make (`make8.py`):** game-hours checker. Three lookups in one try; the missing one (Elden Ring) caught, program survives to "Thank you!". **Deliberate extra:** a *valid* lookup placed below the crashing line — proving the jump abandons even lines that would have succeeded. Demonstrated the catch *and its cost*, beyond the assignment.

**Observation carried into Session 9:** "Certain game not found" — certain *which* game? The catch traded information for survival. The 8a traceback named the culprit; the except message lost it.

---

## Session 9 — Naming the catch, choosing the net, stacking the nets

**Concepts.**
- **`except KeyError as missing:`** catches the error *object* into a variable; `{missing}` in an f-string reports the culprit (prints the key **with quotes on** — the object is a representation, not the bare string).
- **`.get(key)`** never raises. Returns `None` on a miss; `.get(key, fallback)` returns the fallback. A different *philosophy* from try/except: `.get()` **prevents** the error from rising; the net **catches** it mid-air.
- **`None`** = Python's word for absence. Not zero, not empty string — a third thing. Will reappear (e.g., functions without `return`).
- **Multiple excepts** check like an elif ladder: top to bottom, first *matching* net wins, non-matching nets are inert. **Specific nets first, broad net last** — and the broad net must confess: `except Exception as anything:`. The honest catch-all receives only what specific nets declined and names what it caught.
- **Order of evaluation** (reasoned unprompted in 9d): `huors["Sekiro"]` raises NameError, never KeyError — Python resolves the name before the key lookup is ever attempted. The missing key never gets a chance to matter.

**Predictions: 3.5–4/4.** Two surface misses that taught more than the hits: the quotes on the caught key, and `.get()`'s miss printing `None` rather than nothing.

**Traps.**
1. Each species finds its own net; the broad net stays quiet — confirmed.
2. **Reversed ladder:** `except Exception` first makes the KeyError net below **dead code** — Session 4's trap in its third organ. Also: `{anything}` on a caught KeyError prints the *key*, not the word "KeyError" — the honest broad net reports the culprit but not the species. Nets always trade something.
3. `.get()` can't save a NameError — the name resolves before the dictionary can be asked anything. `.get()` handles missing *keys* only.
4. **(Case 3, the deep one) SyntaxError is outside the reach of any net.** Python reads the whole file's grammar *before executing line 1*; a violation means the program never starts, and a net inside a program that never started doesn't exist. **try/except catches errors that happen while running; SyntaxError happens before running.** Species #1 is the only species no error handling can touch. This is a fact about parsing vs. execution — true in every language.

**Make (`make9.py`):** screen-time averages by week — **first Make with real personal data, zero invented numbers.** Took three drafts:
- Draft 1: Session 8 machinery only — plain net, `.get()` without fallback, and the `.get()`-under-a-net collision (net can never fire = dead code).
- Draft 2: named catch + fallback added; net was `Exception` used *alone* (Trap 2 with a confession).
- Final: `.get("...", "Unrecorded data")` for a key that was never real data (quiet), bracket lookup + `except KeyError as missing` for a legitimate missing week (loud), `except Exception as anything` backstop in last position. All three tools, correct order.

---

## The loud/quiet design question (took three passes — worth the space)

When a lookup can fail, pick **one** strategy per lookup:

- **Quiet** (`.get()` with fallback): no error ever rises. The failure's trace is *camouflaged as a value* — a fallback `0` prints identically to a real recorded `0.0`. Nothing distinguishes data from apology.
- **Loud** (brackets + named catch): the failure *announces itself*, unambiguous, named.

Both survive. The question is only: **if this lookup fails, do I want to be told?** Failure normal and harmless → quiet is fine. Failure means something's wrong → loud, or quiet hides a bug.

Key refinements from pushback:
- Quiet failure with a numeric fallback is **how species #5 gets manufactured at runtime** — a fake 0 entering an average is a confident lie no one sees. A quiet fallback that *can't* impersonate data (`"Data not found"`) is far more honest; the danger isn't `.get()`, it's fallbacks that look like values.
- The tools are **competing answers, not stackable safety layers**. `.get()` under a try/except makes the net dead code. More error handling ≠ safer.
- Honest scale judgment (mine, accepted): in a five-line demo testing a key you already know is missing, the choice barely matters. It earns its weight when missing values feed computation or keys come from outside your control. The habit is installed *before* the stakes are real because the file where it matters won't announce itself.

---

## The hack series (new)

**"Tiny hacks" made official** — unassigned, ungraded builds integrating multiple sessions. Named for the original MIT sense: a quick, clever, unpolished build solving a real problem you have. The cyber work from S13 on is the second meaning built out of the first — you can't bend a system you've never built.

### hack1.py — Screen Time Analyzer
One loop over real screen-time data: report line per week, if/elif tag (Light/Medium/Heavy) inside the loop, accumulator → computed average, one deliberate failed lookup (went loud).

**First draft contained three bugs — all repeats from the catalogue:**
1. Bare `except:` **and** `.get()`-with-fallback under it — the philosophy collision again; dead net.
2. Hardcoded `23.1` in the average — species #5 wearing a calculator; correct today, silently wrong the moment a week is added. Fix: accumulator; test by adding a fake week and confirming the average moves by itself.
3. "you're data" — species #2, cited and fixed.

Lesson: **staged development catches loud bugs; the silent species walk through it.** The tool for silent bugs is tracing your own finished file as skeptically as a Predict exercise. The bug catalogue is a *checklist*, not a diary.

### hack2.py — Backlog Advisor
First real function architecture: data at top, two `def`s, logic at bottom, values flowing as arguments and returns. `time_to_finish(backlog, title)` returns bare hours; `verdict(hours)` returns a judgment string from a ladder; the main loop assembles sentences by calling both inside f-strings; total accumulated and fed back into `verdict` — a number the ladder never anticipated, landing safely in the open-ended `else` (the stress test the top branch's unboundedness passes).

**The four-rule function model** (requested as *model, not fix* — then used to find own bugs):
1. **Slot:** the parameter is an empty slot filled at call time; same body, different fuel per call.
2. **Substitution:** the call *becomes* the returned value — `verdict(50)` is replaced by `"Meaty"` wherever it stands, exactly like `len()` always was.
3. **Seal (scope):** variables born inside a def exist only while it runs; only the return escapes.
4. **Eject:** `return` halts the machine instantly — nothing below runs, and a return inside a loop kills the loop mid-lap.

Corollary of Session 3's return-vs-print: functions return **bare values**, callers assemble sentences — that's what lets one `verdict` serve per-game lines and the total alike.

Deliberate design: mixed boundary operators (`<= 30`, `< 80`) so exactly-80 hours gets the "Oof" — a decision, not an accident.

---

## The bug species collection (seven)

1. **SyntaxError** — grammar violation; never runs. **Now proven unique: the only species outside the reach of any try/except** (parsing happens before execution — the net never exists).
2. **Silent string typo** — runs, broken English. (`sice`, "you're data")
3. **Infinite loop** — runs forever; Ctrl + C.
4. **Wrong branch order** — silently wrong answers; dead code. *Third organ discovered:* a broad except above a specific one.
5. **Correct code, wrong data** — confident lies from bad input. *New manufacturing method:* a quiet numeric fallback entering computation; also the hardcoded 23.1.
6. **Runtime crash** — valid code dies mid-run. **Now survivable** via nets; a caught #6 is a planned path.
7. **NameError** — code-zone typo; a name that was never created. Crashes naming the ghost. (`huors`)

---

## Recurring principles (added/updated)

- **Specific before broad** — now in three organs: elif ladders, except ladders, and the Exception backstop's mandatory last position.
- **One strategy per lookup** — `.get()` and try/except are competing answers; stacked, one starves the other.
- **Loud or quiet is a design decision, not syntax** — the question is "if this fails, do I want to be told?"
- **Errors are raised; uncaught raised errors crash** — vocabulary now precise.
- **Trace from line 1** — the interesting neighborhood isn't the whole street; unedited boring lines print just as loudly. (Missed "Checking library..." in a trap prediction.)
- **Predict the file you're running, not the file in your head** — reconcile world and prediction before running.
- **Look, don't infer** — sibling of "look, don't recall," established when Claude wrongly assumed hack1 wasn't built stage-by-stage from a single finished screenshot. Applies to both sides of the table.
- **Comments capture the why; code only shows the what** — same principle as idea-capturing commit messages, at line scale.
- Legal and learned by instinct: line breaks inside an open `{ }` (the multiline dictionary literal).

## Standing conventions (updated)

- **Comment flag-and-veto:** Claude flags where a `#` comment would earn its place (unrecoverable reasoning: multiple failure strategies in one file, boundaries chosen against the obvious default, non-obvious magic numbers). 주현준 holds the per-file veto. One line, no sermon. (hack2: flagged, vetoed, closed.)
- Real personal data in Makes and hacks; invented data gets marked (`# made-up data`).
- Idea-capturing commit messages continue.
- Hacks are a numbered series (`hack1.py`, `hack2.py`, ...) separate from makes.
- One session per day — extra appetite goes to hacks, not tomorrow's session.

---

## Where things stand

| Sessions | Topic | Status |
|---|---|---|
| S1–3 | Variables, lists, loops, functions | ✅ |
| S4–6 | Logic: if/elif/else, while, combined | ✅ |
| S7–9 | Dictionaries + error handling | ✅ **block complete** |
| S10–12 | Files, imports, libraries (datetime) | **S10 next** |
| S13–15 | Cyber begins: Linux + OverTheWire Bandit | — |
| S16–18 | TryHackMe path + Python projects | — |
| S19+ | Robotics, then web | — |

Streak: 9 days, 9 sessions, 14 green squares, zero skipped.

**Carried forward:**
- Open dictionary-loop prediction from Session 7 — resolved during day 8 review (the warm-up).
- The self-audit gap: rereading own finished files with Predict-level suspicion — the specific remaining edge of the execution gap; watch it in hack3.
- `.append()` mentioned but not taught — lists can grow; parked for the files block.
- Garnish filed, not built: `sum(d.values())`, `.get(key, 0)` inside accumulating loops as a species-#5 disguise.

**Next up: Session 10 — files, imports, `datetime`.** Scripts stop living in a bubble and start touching the world outside their own file — reading and writing, which turns "what will future-me need?" from a comment question into a data-format question.
