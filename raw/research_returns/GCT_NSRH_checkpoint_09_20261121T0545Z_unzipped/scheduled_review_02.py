"""Run the second scheduled progress review at or after 03:00 UTC only."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json

r = Path(__file__).resolve().parent
now = datetime.now(timezone.utc)
due = datetime(2026, 11, 21, 3, 0, tzinfo=timezone.utc)
if now < due:
    raise SystemExit('The second scheduled review is not yet due.')
out = r / 'PROGRESS_REVIEW_02.md'
if out.exists():
    raise SystemExit('Refusing to overwrite a completed scheduled review.')
prior_state = json.loads((r / 'REVIEW_STATE.json').read_text())
if prior_state['last_review_number'] != 1:
    raise SystemExit('Expected review01 as the immediately preceding scheduled review.')
with (r / 'QUESTIONS_at_review_01.tsv').open(newline='') as f:
    baseline = list(csv.DictReader(f, delimiter='\t'))
with (r / 'QUESTIONS.tsv').open(newline='') as f:
    current = list(csv.DictReader(f, delimiter='\t'))
old = {row['id']: row for row in baseline}

def cell(s):
    return s.replace('|', '/').replace('\n', ' ')

head = f'''# Scheduled progress review 02

Actual review time: {now.isoformat()}. Scheduled time: 2026-11-21 03:00 UTC /04:00 CET.

Reviewer: /root, GPT-6 Astra Pro; effort not exposed; run GCT_NSRH_20261121.

## Decision: movement; continue

This review compares the exact frozen QUESTIONS_at_review_01.tsv and PROGRESS_REVIEW_01.md with the current questions and dated ledger. It does not count proof-record maintenance, fresh checks, citation/scope wording, PDF work, packaging or newly added side questions by themselves as movement.

The existing main gates Q2, Q3 and Q3-GCT have strictly narrowed in the following specified senses:

1. At review01, the actual coefficient realizations still lacked an opposite-sign path realization and compatible geometric tensor operations. F50 now supplies an explicit fully faithful perverse realization for every effective finite coefficient representation, retaining the actual End/Hom and specified actions, and proves actual compact-cohomology concentration with an effective negative output for an unbounded set of good even path lengths. F53 supplies a coherent geometric convolution carrying the actual all-degree tensor maps. These are complete constructions with full proof reviews. Their remaining bounds are identified exactly: for the Gaussian construction the pointwise and reciprocal inequalities are equivalent to the target coefficient purity. No independent weight estimate or designated simple/global basis is claimed.

2. The literal fixed-operator arithmetic comparison in the main GCT gate has now been ruled out with a finite test: F54 shows that the two actual words P1 and P1^2 alone contradict the changing quadratic coefficient under parameter retuning. This needs no purity, algebraicity or full-centralizer assumptions. Thus that comparison cannot be left as an unexplored possible route; a graded coefficient object, word-dependent object, or materially different comparison is required. This is narrower than the earlier normalized-word obstruction and applies to unnormalized actual operators with composition.

3. F51/F52/F54 settle the specified algebraic full-centralizer and trace-only alternatives that were unresolved at review01. Full spectral retuning cannot preserve the actual whole relative order as its full regular centralizer. Genuine identity traces alone can preserve it, as the explicit two-trace model proves. A marked insertion sharply separates the two situations, and the actual both-actions corollary removes the weight hypothesis when the named ordinary left maps commute with the base Frobenius. These results close stated comparison routes, while leaving the explicitly identified alternatives open.

F49 also closes the particular global-form inclusion test for an actual commutant projector; it does not refute VIII's canonical-basis conjectures. Its contribution is scoped separately and is not treated as a proof of the main positivity target.

The global nonstandard-RH/canonical-positivity target remains open and is not supplied with invented finite-field data. Current F55/F56 memoranda, if present, are not needed to establish movement at this review; their precise check/integration state is recorded in their own files and current questions.

Consecutive scheduled reviews without movement: **0**. Next scheduled review: **2026-11-21 04:00 UTC /05:00 CET**. Continue under the user's two-consecutive-no-movement stop rule. The next checkpoint remains **03:30 UTC /04:30 CET**, not a new review-triggered checkpoint.

## Changes to existing rows since review01

| ID | Previous gate | Current gate |
|---|---|---|
'''
changes = []
for row in current:
    before = old.get(row['id'])
    if before and (before['state'] != row['state'] or before['current_gate'] != row['current_gate']):
        changes.append('| ' + cell(row['id']) + ' | ' + cell(before['current_gate']) + ' | ' + cell(row['current_gate']) + ' |')
all_table = '\n'.join('| ' + cell(row['id']) + ' | ' + cell(row['state']) + ' | ' + cell(row['current_gate']) + ' |' for row in current)
out.write_text(head + '\n'.join(changes) + '\n\n## Every current question and gate\n\nThe complete table includes every open row and the closed rows for context. Newly introduced rows are not counted as movement merely by being new.\n\n| ID | State | Current gate or proved boundary |\n|---|---|---|\n' + all_table + '\n')
(r / 'QUESTIONS_at_review_02.tsv').write_bytes((r / 'QUESTIONS.tsv').read_bytes())
state = {
    'last_review_number': 2,
    'last_review_utc': now.isoformat(),
    'movement': True,
    'consecutive_no_movement': 0,
    'next_review_utc': '2026-11-21T04:00:00+00:00',
    'decision': 'continue',
    'record': out.name,
    'questions_sha256': hashlib.sha256((r / 'QUESTIONS.tsv').read_bytes()).hexdigest(),
}
(r / 'REVIEW_STATE.json').write_text(json.dumps(state, indent=2) + '\n')
with (r / 'LEDGER.md').open('a') as f:
    f.write('\n## ' + now.isoformat() + ' — scheduled progress review02\n\nMovement: yes. Consecutive no-movement count0. Exact comparison with review01 is in PROGRESS_REVIEW_02.md and QUESTIONS_at_review_02.tsv. Counted changes: actual Gaussian negative path cohomology, coherent all-degree geometric tensor maps, the finite two-word arithmetic-composition obstruction, and resolved full-spectrum/identity/marked comparison alternatives. The independent weight and designated basis gates remain. Packaging, citation repair and new side rows are not movement. Next review04:00UTC; next checkpoint03:30UTC.\n\n' + all_table + '\n')
with (r / 'RUN_METADATA.md').open('a') as f:
    f.write('\nScheduled review02 completed ' + now.isoformat() + '; movement yes, no-movement count0. Next review04:00UTC, checkpoint06 at03:30UTC.\n')
with (r / 'CHECK_EVENTS.tsv').open('a', newline='') as f:
    csv.writer(f, delimiter='\t').writerow(['REVIEW02-GATE-COMPARISON', now.isoformat(), '/root', 'GPT-6 Astra Pro', 'not exposed', 'GCT_NSRH_20261121', 'used and rechecked in this run', 'Compared exact review01 snapshot to current states and checked finding scopes; movement decision is a research-gate review, not a new mathematical proof or computation certificate.', 'PROGRESS_REVIEW_02.md; QUESTIONS_at_review_01.tsv; QUESTIONS_at_review_02.tsv'])
print(json.dumps(state))
