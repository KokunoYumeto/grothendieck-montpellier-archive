"""Perform the scheduled review12; refuse early or duplicate use."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
root=Path(__file__).resolve().parents[1]
due=datetime(2026,11,20,14,10,tzinfo=timezone.utc);now=datetime.now(timezone.utc)
assert now>=due,'Review12 is not due.'
out=root/'code/output/formal_review12.json';assert not out.exists(),'Review12 already recorded.'
prior=json.loads((root/'code/output/formal_review11.json').read_text())
qa=json.loads((root/'qa/pdf_verified.json').read_text())
receipt=json.loads((root/'code/output/checkpoint18_saved_receipt.json').read_text())
assert receipt['status']=='succeeded'
checked=[]
for name in ['integrate_post18_canonical_jets.json','integrate_post18_geometric_inputs.json']:
 p=root/'code/output'/name
 v=json.loads(p.read_text())
 checked.append({'path':str(p.relative_to(root)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'content':v})
aux=[
 'The uniform generation and fixed-determinant cycle charts, single-curve Brauer residue cover, and canonical-module two-level jets are prerequisites; none completes a new representation count.',
 'The energy-controlled reduction cycle is proved and the Kahn-Gavran correspondence is recorded with its exact known-theorem scope. Recognition and application do not count as movement.',
 'The single-curve Cartier pencil identifies parameter-ideal thickenings with fixed Cartier thickenings and transfers pointwise module-jet recovery; it supplies no effective all-family object atlas.',
 'The residual twisted spectral category and its Frobenius transport are proved; normal-direction geometry, realization and quantitative equations remain necessary.',
 'The Artinian reduction-cycle realization and recovered quotient base change are proved only under the stated coflatness and split-boundary hypotheses. Effective equations for those strata remain unproved.',
 'Finite Hom complexes, determinant enumeration, mixed-band anchor/minimal-lattice slope bounds and bounded-depth Hom estimates are active constructions; no unbounded-geometric-Brauer-period count is justified.',
 'Source audits, finite certificates, clean compilation, visual inspection and packaging do not count as movement.'
]
review={'review_number':12,'scheduled_utc':due.isoformat(),'actual_utc':now.isoformat(),'preceding_review_actual_utc':prior['actual_utc'],'requested_status_changes':[],'requested_open':prior['requested_open'],'movement':False,'consecutive_no_movement_reviews':prior['consecutive_no_movement_reviews']+1,'strict_main_gate_reductions':[],'remaining_strongest_gates':prior['remaining_strongest_gates'],'auxiliary_not_movement':aux,'checked_integrations':checked,'latest_successful_checkpoint':18,'latest_completed_visual_verification':{'build':qa['build'],'pages':qa['pages'],'sha256':qa['sha256']},'next_review_utc':'2026-11-20T15:10:00+00:00','next_scheduled_checkpoint_utc':'2026-11-20T14:25:00+00:00','note':'No requested-row status change or strict main-gate reduction since review11. Counter is one; the stopping condition is not met. All seven strongest residual gates are copied unchanged from review11.'}
out.write_text(json.dumps(review,indent=2)+'\n')
with (root/'PROGRESS_LEDGER.md').open('a') as f:
 f.write('\n\n## Formal review12: 20 November 2026, 14:10 UTC\n\nINCOMPLETE. Actual review: '+now.isoformat()+'. General D.1, general D.2(ii), and residual L8 remain open; all A/B/C requested rows remain decided. No requested row changed, and no strongest main gate became strictly smaller.\n\n')
 f.write('\n\n'.join(aux)+'\n\n')
 f.write('Movement: NO. Consecutive no-movement reviews: 1. The stopping condition is not met. Next formal review13 is 15:10 UTC; next scheduled checkpoint19 is 14:25 UTC. Checkpoint18 is the latest saved archive.\n')
p=root/'code/assemble.py';lines=p.read_text().splitlines(keepends=True)
summary='Formal review12 was completed during the scheduled14:10UTC period. All A/B/C requested rows remain decided; general D.1, D.2(ii), and residual L8 remain open. No requested status changed and no strongest main gate became strictly smaller since review11. The new reduction-cycle, Cartier-pencil, two-level-jet, residual-category and qualified Artinian-realization statements remain prerequisites for a quantitative atlas. Known-theorem recognition and audits are not movement. All seven residual gates remain unchanged. Consecutive no-movement reviews:1. Exact comparison is in code/output/formal_review12.json. Next formal review13 is15:10UTC; next checkpoint19 is14:25UTC. Checkpoint18 remains the latest saved archive; the stopping condition is not met.'
for i,line in enumerate(lines):
 if line.startswith("'Formal review11 was completed"):
  lines[i]=repr(summary)+',\n';break
else:raise AssertionError('Review11 summary missing.')
p.write_text(''.join(lines))
print(json.dumps({'review':12,'actual_utc':now.isoformat(),'movement':False,'strict_reductions':0,'consecutive_no_movement_reviews':review['consecutive_no_movement_reviews']}))
