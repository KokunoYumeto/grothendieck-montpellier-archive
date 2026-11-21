"""Third scheduled gate review; immutable record, never before its due time."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json

r = Path(__file__).resolve().parent
now = datetime.now(timezone.utc)
if now < datetime(2026, 11, 21, 4, 0, tzinfo=timezone.utc):
    raise SystemExit('Review03 is not yet due.')
out = r / 'PROGRESS_REVIEW_03.md'
if out.exists():
    raise SystemExit('Refusing to overwrite review03.')
state = json.loads((r / 'REVIEW_STATE.json').read_text())
if state['last_review_number'] != 2:
    raise SystemExit('Expected review02 immediately before this review.')
with (r / 'QUESTIONS_at_review_02.tsv').open(newline='') as f:
    old = {x['id']: x for x in csv.DictReader(f, delimiter='\t')}
with (r / 'QUESTIONS.tsv').open(newline='') as f:
    rows = list(csv.DictReader(f, delimiter='\t'))
def cell(s):
    return s.replace('|', '/').replace('\n', ' ')
changes = '\n'.join('| ' + cell(x['id']) + ' | ' + cell(old[x['id']]['current_gate']) + ' | ' + cell(x['current_gate']) + ' |' for x in rows if x['id'] in old and (x['state'] != old[x['id']]['state'] or x['current_gate'] != old[x['id']]['current_gate']))
table = '\n'.join('| ' + cell(x['id']) + ' | ' + cell(x['state']) + ' | ' + cell(x['current_gate']) + ' |' for x in rows)
head = f'''# Scheduled progress review 03

Actual review time: {now.isoformat()}. Scheduled time: 2026-11-21 04:00 UTC /05:00 CET.

Reviewer: /root, GPT-6 Astra Pro; effort not exposed; run GCT_NSRH_20261121.

## Decision: movement; continue

Compared the frozen QUESTIONS_at_review_02.tsv, PROGRESS_REVIEW_02.md, current questions and dated ledger. Count only closure of an existing open question or a strictly smaller main gate. Packaging, additional checks, source corrections and newly introduced side rows are not movement.

The pre-existing Q2/Q3-GCT gate has strictly narrowed in three exact respects:

1. Review02 required a graded coefficient-object comparison after the fixed-operator retuning route failed. F56 now supplies actual rank-three graded kernels on the original64 states, with explicit quadratic and degree-five relation isomorphisms, ordered coherence, exact split-K0 comparison with the actual word algebra, a perverse arithmetic lift, and a contravariant bar matching the actual localized tensor bar. All proofs and fragments have whole-proof checks. Thus bare rank-three relation maps and formal bar compatibility are no longer missing. All-degree compatibility, designated global forms/simple labels and independent varying-coefficient bounds remain.

2. The same strict effective-kernel route cannot simply be extended simple by simple to the full rank-four algebra. F57 supplies an explicit named-generator word on an actual additional5-dimensional simple whose Laurent trace has negative extreme coefficients. This rules out all strict effective graded matrix models of those named operators on that simple and the stated genuine finite Frobenius-trace comparisons. The simple occurs for ordinary dimensions at least3 and2. It is absent from the two-row quotient, so the scope is explicit.

3. F58 separately closes the strict effective route for the rank-four two-row source-cell comparison. A nonnegative Laurent generator graph cannot change on positive specialization, while the designated generic6-dimensional cell must refine into3+3 at v=1. This applies to any basis retaining that specified cell refinement, not merely the displayed graph or diagonal rescalings. The route therefore requires signed/derived coefficients or different positive operators; arbitrary positive bases without the coordinate-cell comparison remain possible.

F55 additionally resolves the earlier all-places marked-trace alternative without action commutation, effectivity, semisimplicity or weights. The one-place bar-compatible construction shows exactly why its hypotheses matter. This is a further restriction of the arithmetic comparison, not a proof of the global target.

The source-generator and pure-complex refinements, F59 ordinary-Hecke closure, F60 bounded-kernel relation gate and F61 pure rank-three construction are at their respective review/integration stages. They are not needed for, and are not counted in, this review's movement decision. Their complete records remain available; subsequent integration will use their final proof checks.

The global nonstandard-RH/canonical-positivity target remains open. No unspecified finite-field objects, weights, local bounds or canonical labels are supplied by inference.

Consecutive scheduled reviews without movement: **0**. Next scheduled review: **2026-11-21 05:00 UTC /06:00 CET**. Continue under the user's two-consecutive-no-movement rule. Next checkpoint07 remains **04:15 UTC /05:15 CET**; this review creates no checkpoint.

## Changes to existing rows since review02

| ID | Previous gate | Current gate |
|---|---|---|
'''
out.write_text(head + changes + '\n\n## Every current question and gate\n\nEvery open row is listed below, together with the closed rows for context. A newly introduced question does not count as movement merely by being new.\n\n| ID | State | Current gate or proved boundary |\n|---|---|---|\n' + table + '\n')
(r / 'QUESTIONS_at_review_03.tsv').write_bytes((r / 'QUESTIONS.tsv').read_bytes())
state = {'last_review_number': 3, 'last_review_utc': now.isoformat(), 'movement': True, 'consecutive_no_movement': 0, 'next_review_utc': '2026-11-21T05:00:00+00:00', 'decision': 'continue', 'record': out.name, 'questions_sha256': hashlib.sha256((r / 'QUESTIONS.tsv').read_bytes()).hexdigest()}
(r / 'REVIEW_STATE.json').write_text(json.dumps(state, indent=2) + '\n')
with (r / 'LEDGER.md').open('a') as f:
    f.write('\n## ' + now.isoformat() + ' — scheduled progress review03\n\nMovement yes; consecutive no-movement count0. Counted main-gate changes: actual rank-three graded relation maps and matching bar (F56); full rank-four strict simple effectivity obstruction (F57); two-row source-cell-compatible strict effectivity obstruction (F58). F55 further resolves the all-places marked alternative. The designated global/simple and independent weight gates remain. Later unintegrated findings are not used to manufacture movement. Next review05:00UTC, checkpoint07 at04:15UTC. Exact frozen comparison: PROGRESS_REVIEW_03.md and QUESTIONS_at_review_03.tsv.\n\n| ID | State | Current gate or proved boundary |\n|---|---|---|\n' + table + '\n')
with (r / 'RUN_METADATA.md').open('a') as f:
    f.write('\nScheduled review03 completed ' + now.isoformat() + '; movement yes, no-movement count0. Next review05:00UTC; checkpoint07 at04:15UTC.\n')
with (r / 'CHECK_EVENTS.tsv').open('a', newline='') as f:
    csv.writer(f, delimiter='\t').writerow(['REVIEW03-GATE-COMPARISON', now.isoformat(), '/root', 'GPT-6 Astra Pro', 'not exposed', 'GCT_NSRH_20261121', 'used and rechecked in this run', 'Compared frozen review02 gates with current checked findings; movement decision is a research-gate review, not a new mathematical proof or computation certificate.', 'PROGRESS_REVIEW_03.md; QUESTIONS_at_review_02.tsv; QUESTIONS_at_review_03.tsv'])
print(json.dumps(state))
