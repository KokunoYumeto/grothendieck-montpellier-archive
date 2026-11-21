#!/usr/bin/env python3
"""Record scheduled review 03 once it is actually due, with current open rows."""
from pathlib import Path
import csv
import datetime
import json
import subprocess
import sys

root = Path(__file__).resolve().parent
now = datetime.datetime.now(datetime.timezone.utc)
due = datetime.datetime.fromisoformat('2026-11-21T04:00:17+00:00')
if now < due:
    raise SystemExit('Review03 is not due yet.')
path = root / 'TIMED_REVIEWS.json'
reviews = json.loads(path.read_text())
if [x['review'] for x in reviews] != [1, 2]:
    raise SystemExit('Review03 requires exactly the two preceding actual reviews.')
subprocess.run([sys.executable, str(root/'build_package.py')], check=True)
questions = list(csv.DictReader((root/'QUESTIONS.tsv').open(), delimiter='\t'))
open_rows = [r for r in questions if not r['state'].lower().startswith(
    ('proved', 'refuted', 'first refuted'))]
gates = {
 'Q1': 'All supplied archive assertions are proved or refuted under explicit interpretations, and all supplied original pages were visually checked. QA030 remains closed. The arbitrary singular-local coefficient-ring classification SA017 remains unclassified; the unused uncertain surname is not authenticated.',
 'Q2': 'Exact positive formulas and nonvanishing for the stated two-row, hook, rectangle and IP families remain proved. General cancellation-free rectangular bases remain open. A034 supplies explicit positive polynomial highest-weight algebras on actual permanent and determinant Hessian rays at every size; O030 extends the all-copy comparison to a three-parameter family.',
 'Q3': 'A034 now identifies the ENTIRE actual determinant Hessian-ray algebra as C[U2,...,Un], in degrees2..n, for every n>=3. Thus K=sk=g=h_n(s) at EVERY stretch, with support{0,2,3,...} in the primitive generated latticeZ. Its normality and positive monomial basis coexist with the genuine relative-saturation hole1. This replaces review02 eventual determinant positivity by exact all-stretch values; general saturation from lambda operations, K-theoretic positivity or purity remains refuted.',
 'Q4': 'A034 proves q_s>=p_n(s)>K_s=sk_s=g_s=h_n(s) for EVERY unpadded n=m>=3 and EVERY s>=1, with both actual multiplicities positive at every s>=2 and gap>=p_n(s-1). O030 gives the corresponding three-parameter exact determinant/positive permanent comparison. A033 strengthens q>=3 at s2, whereK1. F028 has a stronger cubic bound. A035/A036 prove that the full constructed positive algebra survives on EVERY proper partial determinant ray, so it cannot transfer this obstruction to internal padding. A037 refutes exhaustion of the whole proper ray by the binary pair algebra, with exact pair3<ambient=K4. The large-padding comparison remains open under the same proved degree/staircase/support/jet gates, including M019 lambda4>=27 ORlambda2>=239063403. QA033 remains open: the actual permanent endpoint reduces to an explicit residue square map, and O031 proves only one uniform block isomorphism, not arbitrary-size full rank.',
 'Q5': 'New included findings have complete proof readings, separately recorded source-use events and precise geometric dictionaries. Conditional reductions are proved as implications and kept distinct from their unproved nonvanishing gates. Document integration and visual production checks are not counted as mathematical movement.'
}
record = {
 'review': 3, 'date_utc': now.isoformat(), 'scheduled_utc': due.isoformat(),
 'comparison_baseline': 'Actual review02 at03:01:32UTC, using its saved gates and open rows.',
 'movement': True, 'consecutive_no_movement': 0,
 'movement_evidence': [
   'A034 closes the every-size/every-stretch actual-comparison question: the review02 cubic-only all-stretch obstruction and eventual determinant values become uniform exact determinant values and strict actual comparisons for every n>=3 and every stretch.',
   'A034 identifies the full actual determinant ray algebra and its precise primitive relative-saturation hole, replacing an ineffective eventual occurrence statement by an exact all-degree algebra.',
   'A035 and A036 close the proposed basic/constructed-algebra partial-Hessian transfer under internal padding; A037 closes the exhaustion question negatively with an explicit missing ambient copy.'
 ],
 'not_counted_as_movement': 'Packaging, rereading, merely new constants or finite rank examples, and unproved arbitrary-m endpoint claims are not counted. The large-padding main rank-comparison gate has not changed during this interval.',
 'main_gates': gates, 'open_rows': open_rows,
 'decision': 'Continue. Main comparison and saturation questions moved, and the no-movement streak remains zero. Next timed review due2026-11-21T05:00:17Z; next scheduled checkpoint remains04:15:17Z. No checkpoint is made at this review.'
}
reviews.append(record)
path.write_text(json.dumps(reviews, indent=2, ensure_ascii=False)+'\n')
lines = ['# Timed review 03', '', 'Actual review: '+now.isoformat()+'. Scheduled: '+due.isoformat()+'.', '',
         '**Movement: yes. Consecutive reviews without movement: zero. Continue.**', '',
         'The comparison is against the saved review02 gates. The large-padding rank comparison remains open and its numerical gates did not change in this interval.', '',
         '## Main gates', '']
for k,v in gates.items():
    lines += ['### '+k, '', v, '']
lines += ['## Every currently open question row', '', '| ID | State | Current gate |', '|---|---|---|']
for row in open_rows:
    gate = row['finding_ids_or_current_gate'] or row['state']
    lines.append('| '+row['id']+' | '+row['state'].replace('|','/')+' | '+gate.replace('|','/')+' |')
lines += ['', '## Movement evidence', '']+['- '+x for x in record['movement_evidence']]+['', record['not_counted_as_movement'], '', record['decision'], '']
(root/'TIMED_REVIEW_03.md').write_text('\n'.join(lines))
p = root/'LEDGER.md'
s = p.read_text().replace('Two timed reviews have occurred, both with movement; see TIMED_REVIEWS.json. Next scheduled review is 2026-11-21T04:00:17Z. The no-movement streak is zero.', 'Three timed reviews have occurred, all with movement; see TIMED_REVIEWS.json. Next scheduled review is 2026-11-21T05:00:17Z. The no-movement streak is zero.')
s += '\n## Timed review03, '+now.isoformat()+'\n\nMovement: yes; consecutive reviews without movement: zero. Uniform exact all-stretch actual comparisons and the precise normal determinant ray algebra supply main-question movement. Partial-Hessian transfer and pair-algebra exhaustion are now decided in their stated scopes. The large-padding rank comparison and arbitrary-size permanent endpoint remain open. Every open row and each main gate are snapshotted in TIMED_REVIEW_03.md and TIMED_REVIEWS.json. Continue; next review05:00:17UTC.\n'
p.write_text(s)
print(json.dumps({'review':3,'actual_utc':now.isoformat(),'movement':True,'open_rows':[r['id'] for r in open_rows]}))
