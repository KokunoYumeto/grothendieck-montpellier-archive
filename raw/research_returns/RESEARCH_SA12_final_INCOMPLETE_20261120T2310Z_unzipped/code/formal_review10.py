"""Record the actual scheduled review10; refuses early or duplicate execution."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
root=Path(__file__).resolve().parents[1]
scheduled=datetime(2026,11,20,12,10,tzinfo=timezone.utc)
now=datetime.now(timezone.utc)
assert now>=scheduled,'The scheduled review has not begun.'
out=root/'code/output/formal_review10.json'
assert not out.exists(),'An actual review10 record already exists.'
prior=json.loads((root/'code/output/formal_review09.json').read_text())
added=json.loads((root/'code/output/integrate_post15.json').read_text())
assert len(added['labels'])==12
qa=json.loads((root/'qa/pdf_verified.json').read_text())
review=dict(review_number=10,scheduled_utc=scheduled.isoformat(),actual_utc=now.isoformat(),preceding_review_actual_utc=prior['actual_utc'],requested_status_changes=[],requested_open=prior['requested_open'],movement=False,consecutive_no_movement_reviews=1,strict_main_gate_reductions=[],remaining_strongest_gates=prior['remaining_strongest_gates'],auxiliary_not_movement=[
'Uniform first-power canonical defect, relative Noether-different factorization, linear cohomology of fixed exceptional thickenings and weighted genus are auxiliary estimates.',
'Pointed and unpointed linear local Eisenstein charts, bounded branch-data lists and the fixed-full-formal-data curve fibre bound do not control the degree of the additional surface-extension locus.',
'Rank-linear full-sheaf degree on rational-double-point blocks and linear canonical energy do not supply a hereditary presentation with the required coordinate and degree budgets.',
'The exact3r generator example refutes uniformity for arbitrary Azumaya anchors, while leaving a possible better-anchor construction and the desired quadratic projective count open.',
'The earlier complete resolution-size and finite normal descent results were already excluded as auxiliary or closure of the review09 geometric criterion. Subsequent recognition, source searches, arithmetic certificates, proof audits and document work are not movement.',
'Any separate post-freeze integer-cycle or root-gerbe discussion has only its explicitly recorded status and is not an effective object atlas or a completed main reduction.'
],checked_post15_files=added['files'],latest_successful_checkpoint=15,latest_completed_visual_verification=dict(build=qa['build'],pages=qa['pages'],sha256=qa['sha256']),next_review_utc='2026-11-20T13:10:00+00:00',next_scheduled_checkpoint_utc='2026-11-20T12:10:00+00:00',note='Actual comparison with review09 at the scheduled review10 period. All twelve integrated new units are auxiliary under the user definition of movement. No requested status changed, and the strongest main gates are unchanged. One consecutive no-movement review does not meet the stopping rule.')
out.write_text(json.dumps(review,indent=2,ensure_ascii=False)+'\n')
p=root/'PROGRESS_LEDGER.md'
with p.open('a') as f:
 f.write('\n\n## Formal review10:2026-11-20 12:10UTC\n\nINCOMPLETE. Actual review:'+now.isoformat()+'. General D.1, general D.2(ii), and residual L8 remain open; all A/B/C requested rows remain decided. No requested row changed and no strongest main gate strictly shrank relative to review09.\n\n')
 f.write('The twelve new checked units give canonical-defect, local-chart, fixed-fibre, RDP-degree and energy control, together with an exact arbitrary-anchor obstruction. They do not bound the effective surface-extension locus, produce a hereditary object atlas, resolve the unbounded-centre and uncovered simple-family counts, or control general nonabelian crowns. These are auxiliary results and do not count as movement. The separate post-freeze work likewise supplies no completed main reduction.\n\n')
 f.write('Movement:NO. Consecutive no-movement reviews:1. The stopping condition is not met. Next review11 is13:10UTC; checkpoint16 is due now and checkpoint17 is12:55UTC. Checkpoint15 is the latest successfully saved archive at the moment of review.\n')
p=root/'code/assemble.py';s=p.read_text();lines=s.splitlines(keepends=True)
summary='Formal review10 was completed during the scheduled12:10UTC review period. All A/B/C requested rows remain decided; general D.1, D.2(ii), and residual L8 remain open. No requested row changed and the strongest main gates did not strictly shrink relative to review09. The twelve integrated post-checkpoint15 units are auxiliary under the stated movement rule; exact comparison and exclusions are in code/output/formal_review10.json. Consecutive no-movement reviews:1. Next formal review11 is13:10UTC; checkpoint16 is due12:10UTC and checkpoint17 is12:55UTC. Checkpoint15 is the latest saved archive at review time. The stopping condition is not met.'
for i,line in enumerate(lines):
 if line.startswith("'Formal review09 was completed"):
  lines[i]=repr(summary)+',\n';break
else:raise AssertionError('Review09 summary not found')
p.write_text(''.join(lines))
print(json.dumps(dict(review=10,actual_utc=now.isoformat(),movement=False,consecutive_no_movement_reviews=1)))
