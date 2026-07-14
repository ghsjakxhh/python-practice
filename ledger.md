# ledger.md — updated 2026-07-13, end of Session 13 (timed round)

## Fluent (legacy — spot-check occasionally, don't drill)
variables & assignment · strings & f-strings · lists & indexing ·
for loops & .items() unpacking · if/elif/else & branch ordering ·
while loops · dict read/write/KeyError asymmetry ·
functions (def/return/parameters) · try/except mechanics & ladders

## Fluent (promoted 2026-07-13, timed round) — next review ~July 16
| Node | Evidence | Interval |
|---|---|---|
| count accumulator | S13 item 1, cold, correct, under 3:00 | 1 → 3 days |
| split-then-index-convert | S13 item 3, cold, 1:25 vs 2:00 target, staged | 1 → 3 days |

## produced-once
| Node | Evidence | Next timed attempt |
|---|---|---|
| record-keeper / max tracker | S13 item 2: cold-correct but over 3:00 (two output-diagnosed self-repairs: loop-variable-outlives-loop, single-vs-paired tracking); ALSO written correctly inside S13 item 4 | S14 warm-up, ≤3:00, fresh data |
| gated count | A2 clean (Jul 12); exercised inside S13 item 4 | schedule with next timed round |
| gate pattern (if inside loop) | A2, D1, S13 item 4 | rides composite builds |
| file-read → parse → report composition | D1 (Jul 12); S13 item 4: full build, staged, all self-repaired (AttributeError on f.split, method-object print), 3-report spec incl. embedded record-keeper — timed attempt voided at 7 min by mid-rep question (cause: unsaved-buffer-vs-disk, not Python) | S14 or S15, fresh spec, ≤15:00 |

## taught / due for evidence
- exception ladders + .get() design — STARVED, ~10 days unreviewed; highest-value warm-up remains an error-handling-cluster build
- with-frame production — written cold in S13 item 4 line 1 → arguably produced-once now; confirm with one isolated cold rep
- datetime pipeline production — no production evidence yet
- file *writing* cold — no production evidence yet
- NEW (taught 2026-07-13): editor buffer vs disk — open() reads disk; unsaved paste doesn't exist; the tab-dot means unsaved

## Gates
- Linux acquisition: CLOSED. Opens when record-keeper AND composition both reach fluent.
- Bandit: closed (shell navigation, file search, permissions — no nodes yet).

## Session 13 record
- 2 of 4 promoted. Record-keeper + composition rescheduled, no drama.
- Mid-rep question = attempt void: applied once today, working as intended.
- Streak: session 13 done, day ~18, committed.