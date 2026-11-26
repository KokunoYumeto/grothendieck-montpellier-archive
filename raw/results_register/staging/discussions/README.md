# Staging: index wave 1, the settled discussions (USER_INPUTS.md and RUNBOOK_20261110.md)

Written by abe075dcdd909eea0 (Claude Opus 5.5 at effort max), from 25 Nov 2026, for the main session 329fb1e6 (Claude
Opus 5.5 at effort max), under results_register/PLAN.md. No new mathematics and no rechecking: every row records what
the two sources say was proposed, established, linked or checked, with its locator.

## Files (tab-separated, UTF-8, one header row; columns follow regkit.py of a65dbdc2, plus `secondary`)
- `OBJECTS.tsv`: object_id, kind (RESULT, RUN, INPUT, CONJ, ARCHIVE, CAND, TOPIC), title, aliases, patterns, hexagon,
  new, links, locator, added_utc, added_by, secondary.
- `CHECKS.tsv`: check_id (DISC-C#####), object_id, alias_used, scope (PROOF / USE / STATEMENT / COMPUTATION / FORMAL),
  verdict (holds / gap / refuted), finding, who (agent or person, model and effort as the source gives them), type (the
  seven, as in regkit.py), date, locator, submitted_utc, submitted_by, origin, secondary.
- `RELATIONS.tsv`: relation_id (DISC-R#####), subject, relation (regkit's words), object, mechanism, established_by,
  checks, locator, state (established / checked / open route), routes_tried, hexagon, new, ..., secondary.
- `READINGS.tsv`: reading_id (DISC-D#####), object_id, who, what_read, date, locator, ... (never a check).
- `APPEARANCES.tsv`: object_id, locator, version, context.

## Locators
- `UI:P1234` = USER_INPUTS.md entry P1234 (F:/user/Documents/claude_open_courses_20260926/USER_INPUTS.md); `UI:L5678`
  = its line 5678 where an entry spans many numbers.
- `RB:L1234` = RUNBOOK_20261110.md line 1234 (<local>/Documents/RUNBOOK_20261110.md), as of 25 Nov 2026.

## `secondary`
- `primary`: the user's own words in USER_INPUTS (a proposal, a decision, or a statement of what was settled).
- `SECONDARY`: a summary's report (the RUNBOOK, or Claude's "Directive:" paraphrase in USER_INPUTS) of a result, check
  or link made elsewhere; to be confirmed at the source (PLAN.md section 2).

## Ids
Ids are canonical-looking slugs (`TOPIC:j-1728`, `RESULT:...`, `RUN:...`, `CONJ:...`, `INPUT:...`); duplicates against
other waves are to be merged by the import (PLAN.md, layer 1). Duplicate user entries P9816-P9873 of 25 Nov are counted
once per number.

## Progress
Recorded in `<local>/Documents/agent_notes/abe075dcdd909eea0_NOTES.md` (wave 1 progress log); the row files per
reading chunk are in `<local>/Documents/agent_notes/abe075dc_wave1/rows/`.
