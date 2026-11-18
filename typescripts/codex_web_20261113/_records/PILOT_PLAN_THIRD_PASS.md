# Pilot plan: a third pass by GPT-6.2 Sol on pages that already have two passes

Written by Claude Opus 5.5 at effort high, 17 Nov 2026 (night), for the main session. Nothing has been sent.

## The question

**The situation.** Thousands of archive pages already have:
- a first pass, by GPT-6 Astra (ChatGPT Pro mode) or GPT-6 Astra at reasoning effort max (Codex web);
- a Claude second pass against the scans.

**Why GPT-6.2 Sol.** On CTRL-148, as a sole transcriber, GPT-6.2 Sol at reasoning effort max (ChatGPT Work) is worse
than GPT-6 Astra at reasoning effort max (Codex web). Its errors per 100 words are 1.73 against 1.39, and its unmarked
errors 1.24 against 0.79 (`returns_control/CTRL-148_SOL62/VERDICT_CTRL-148_SOL62_20261117.md`). But its errors are
largely independent of the other two readers', and it is cheap and fast. So it is to be used as a **third pass**.

**The user's goal:** find by a few pilots how to make that third pass "as useful as it can be without being stupidly
expensive".

**How the variants are ranked** (the user, 17 Nov):
1. known errors caught;
2. false alarms;
3. Work meter used.

Wall time is recorded but weighs little: on Work, runs can be parallelised without limit, and the meter is the
constraint.

## The reference: what the third pass must catch

**What the third pass checks.** On the thousands of other pages, no control run has corrected the second pass. The
pilot therefore gives the third pass the second pass **as it stood before the control runs corrected it**:
- 148: addenda A and B reversed;
- 145: rows 43-55 of its changes file reversed.

`tools/build_third_pass_pilot.py` rebuilds that text exactly from the addendum scripts and the changes table, into
`third_pass_pilot/second_pass_before_controls/<ID>/`. Every reversal is checked to apply exactly once.

**The known errors.** The places where that text is wrong, found by the control runs and confirmed on the scans, are
listed per page and line in `third_pass_pilot/keys/<ID>_known_second_pass_errors.tsv`:

| Control | Known second-pass errors | of which wrong first readings | of which only a majority reading (B7-B12, not settled by the ink) |
|---|---:|---:|---:|
| CTRL-148 (cote 148, scans 44-58) | 23 | 20 | 6 |
| CTRL-145 (cote 145, scans 20-34) | 9 | 9 | 0 |

"Wrong first reading" means the first reading changed. The other entries only added an alternative or a mark. The
majority entries are scored apart, as low-confidence truth.

**The bias in this reference.** Every known error was found because an independent full reading (CTRL-148,
CTRL-148_SOL62, CTRL-145) disagreed with the second pass there. The known set therefore favours the full-reading
variants V1 and V2 by construction. Two things follow:
- the experts must also check on the scan every **new** error a variant claims;
- a variant's score is known errors caught **plus** new errors confirmed on the scan.

## The variants

All eight folders are in `drag_split_third/<VAR>-<ID>/`:
- **Split for Chrome:** two parts each, every part under 9 MB, plus `<VAR>-<ID>_PROMPT.zip`.
- **Lint:** every PROMPT.md passes `claude_tools/push_rule_pro_prompts.py --lint`. That includes the hourly
  checkpoint rule, since these are Work runs, not Codex web.
- **Output:** `<VAR>-<ID>_out.zip`.
- **For the sender:** `drag_split_third/README.md`.
- **Build:** the unsplit builds and the keys are in `third_pass_pilot/`.

| Variant | What the model gets | What it does | Model and effort | What it measures |
|---|---|---|---|---|
| **V1** | the scans (whole page and thirds) | a full independent transcription with the second reading. Taken out of the K template: the mathematical notes (18.7 % of Sol's CTRL-148 session) and the notes file. The second reading stays, but its record is cut to times and changes, with no lists of checked words and formulas. | GPT-6.2 Sol at reasoning effort max | the full third pass, without the notes overhead |
| **V2** | the same folder | the same | GPT-6.2 Sol at reasoning effort high | what the effort setting buys |
| **V3** | crops of only the places the second pass marked doubtful or changed: 158 places on 148, 138 on 145 | reads each place blind. Each place is given by scan, likely third and the text around it, with the place withheld; the answer is one line per place, read twice. | GPT-6.2 Sol at reasoning effort max | a targeted check of the hard places, at a fraction of the reading |
| **V4** | the scans and the second pass's text (before the controls) | checks the text line by line against the ink and flags every disagreement, then takes a second look at each flag | GPT-6.2 Sol at reasoning effort max | the cheapest full check, and how readily it agrees |

Notes on the design:
- **Effort for V3 and V4:** they run at max, so that only the method separates them from V1. V2 isolates the effort.
  The winning method is then rerun once at high if V2 shows that high costs little.
- **No witness:** none of the variants sees Hua's transcription or any other witness. V3 sees no reading of its
  places. V4 sees only the text it checks.
- **What V3 can catch at most:** only the known errors inside a place, 7 of the 23 on 148 (6 of 20 wrong first
  readings) and 4 of the 9 on 145. Most errors of the second pass sit where it was confident and recorded no change.
  V3 measures how well Sol settles the hard places. It cannot replace a full check, but it may be a cheap complement.
- **The risk V4 carries:** agreeing too readily. The pilot measures it as the share of known errors left unflagged,
  against V1's catch rate at the same places.

**What the reconciliation already shows.** CTRL-148_SOL62 is in effect a V1 run with notes. Comparing the
second-pass text before the controls with each full reading, using `tools/reconcile_readings.py`:

| Pair | Disagreement regions | Known errors on a line with a disagreement |
|---|---:|---:|
| 148: second pass vs GPT-6.2 Sol at max (SOL62) | 303 on 215 lines | 18 / 23 (15 / 20 wrong first readings) |
| 148: second pass vs GPT-6 Astra at max (Codex web) | 301 on 213 lines | 21 / 23 |
| 145: second pass vs GPT-6 Astra at max (Codex web) | 343 on 168 lines | 8 / 9 |

The match is by line, so it is generous, and it shares the bias above. It still sets the scale of the job. A full
third reading catches most of the known errors, but the scan check then faces about 20 disagreements a page. Most of
them are noise (layout, conventions, the third reader's own errors). That check is the hidden cost of V1 and V2; V4
and V3 trade some catches for far fewer places to look at.

## What is measured per run

| Measure | How | Weight |
|---|---|---|
| **Known errors caught** | per entry of the key: caught if the variant's reading at that place is the corrected one (V1, V2, V3), or a kept flag there gives it (V4). Counted for wrong first readings and alternatives, majority entries apart. | first |
| **New errors confirmed** | a place where the variant differs from the second pass, the key lists nothing, and the expert finds the variant right on the scan | with the first |
| **False alarms** | a place where the variant differs from the second pass (V1, V2, V3) or flags it (V4), and the second pass is right on the scan. Undecided places are counted apart. | second |
| **Scan-check load** | the number of places the expert had to look at: disagreement regions for V1 and V2, places that differ for V3, kept flags for V4 | with the false alarms |
| **Work meter used** | the meter before and after each run, with the run alone on Work (`drag_split_third/README.md`) | third |
| **Wall time** | start and end UTC, from the sender and `progress.log` | recorded, low weight |

**The ranking.**
- **Main figure:** caught (known plus new) per 1 % of the Work meter.
- **Second:** false alarms per real catch, because every false alarm costs a Claude scan check.
- **The third pass is meant to catch errors,** so a variant that catches clearly fewer real errors than V1 does not
  win on price alone. The plan reports both figures side by side, and the main session chooses.

## How the experts grade the returns

**Who grades:**
- CTRL-148: the expert who made its second pass and both verdicts, agent a8ebc443 (Claude Opus 5.5 at effort max);
- CTRL-145: agent ac292d80 (Claude Opus 5.5 at effort max).

The main session resumes each one with that control's four returns, this plan, and the key files. Both have the crops
and the scans already.

**Step 1: put the returns in place.** Unpack each into `returns_control/<VAR>-<ID>/` and add `RUN.md` with the times
and meter readings.

**Step 2, V1 and V2: three-way triage, then scan checks.**

```
python -I -B tools/reconcile_readings.py \
  PRE=third_pass_pilot/second_pass_before_controls/CTRL-148 \
  SOL=returns_control/V1-CTRL-148/out/pages \
  TRUTH=../second_pass/out/MPL_148_029-072 --scans 44-58 --out returns_control/V1-CTRL-148/TRIAGE.tsv
```

(For 145: `CTRL-145`, `MPL_145` and `--scans 20-34`.) The `pattern` column sorts each place:

| Pattern | Meaning | What the expert does |
|---|---|---|
| A≠B=C | Sol agrees with the truth against the second pass | a catch: no scan check needed |
| A=C≠B | Sol differs, and the truth is the second pass | a false alarm, unless the truth there was never checked: then check it on the scan |
| A=B≠C | the truth changed, and Sol kept the second pass | a known error missed |
| A≠B≠C | the three differ | a scan check |

The count of regions where SOL differs from PRE is the scan-check load that V1 or V2 would bring at scale.

**Step 3, V3.** For each line of `out/V3-<ID>_places_read.tsv`, compare `reading` with
`third_pass_pilot/keys/V3-<ID>_places_key.tsv`:
- **The key file:** it gives the withheld second-pass reading and `known_error_at`. The truth at the place is in the
  current second-pass page file at that scan and line.
- **Results:** the same as the second pass means agreement; the corrected reading at a known-error place is a catch;
  otherwise the place gets a scan check (a new error, or a false alarm).
- **Also record:** the places not found (`found` = no) and the readings marked low.

**Step 4, V4.** For each known error, look for a kept flag on that scan within one line whose `ink_reading` gives the
corrected reading:
- **Catches:** a flag that gives it is a catch.
- **Other kept flags:** each gets a scan check (a new error, or a false alarm). Withdrawn flags are counted apart.
- **How readily it agrees:** compare V4's catch rate with V1's on the same known errors, and its kept flags per page
  with V1's disagreements per page.

**Step 5: the result table.** Each expert writes `returns_control/VERDICT_THIRD_PASS_<ID>_<date>.md`. It holds one row
per variant:
- known errors caught (wrong first readings / alternatives / majority);
- new errors confirmed;
- false alarms;
- undecided;
- scan-check load;
- the meter used;
- wall time;
- caught per 1 % of the meter, and false alarms per catch.

The main session then puts the two tables together and chooses.

## What the result decides

The thresholds below are starting points for the main session, not fixed rules.
- **If V2 catches nearly what V1 catches** (within about a tenth), for clearly less of the meter, the third pass runs
  at high.
- **If V4 catches most of what V1 catches** (about two thirds or more), for well under half the meter and with a
  smaller scan-check load, V4 is the third pass at scale, and its flags go to the Claude scan check.
- **Otherwise the third pass is a full reading** (V1 or V2). `reconcile_readings.py` then turns it into a list of
  places, and the Claude scan check looks only at the regions where Sol differs from the second pass. A two-of-three
  rule, as in the SOL62 verdict, clears the places where the first pass and Sol agree against the second pass. The
  scan still checks those, but first.
- **V3 is a candidate add-on:** it settles the places the second pass itself left doubtful. It is kept if it settles
  them reliably at a small meter cost.

**At scale:**
- each third-pass folder is one package of the second pass;
- its return is reconciled against that package's first and second passes;
- the disagreements go to the Claude scan check in order: two-of-three against the second pass first, then the rest.

## Files

- `codex_web_20261113/tools/build_third_pass_pilot.py`: rebuilds the second pass before the controls, the keys and
  the eight folders. The split is made with `tools/split_for_chrome.py --dst drag_split_third third_pass_pilot/build`
  and the IDs.
- `codex_web_20261113/tools/reconcile_readings.py`: the two- or three-way disagreement list (TSV) of readings of the
  same pages.
- `codex_web_20261113/third_pass_pilot/BUILD_REPORT.txt`: the build figures.
- `codex_web_20261113/third_pass_pilot/keys/`: the known errors, and the V3 place keys. **Never send these to a model.**
- `codex_web_20261113/drag_split_third/`: the eight folders and the sender's README.
