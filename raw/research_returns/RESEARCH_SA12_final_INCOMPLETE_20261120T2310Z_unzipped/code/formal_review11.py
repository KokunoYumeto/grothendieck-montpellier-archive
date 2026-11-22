"""Perform the actual scheduled review11; refuses early or duplicate use."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
root=Path(__file__).resolve().parents[1]
due=datetime(2026,11,20,13,10,tzinfo=timezone.utc);now=datetime.now(timezone.utc)
assert now>=due,'Review11 is not due.'
out=root/'code/output/formal_review11.json';assert not out.exists(),'Review11 already recorded.'
prior=json.loads((root/'code/output/formal_review10.json').read_text())
packet=json.loads((root/'code/output/integrate_post16_all.json').read_text())
assert len(packet['labels'])==17 and packet['main_reduction_count']==1
for info in packet['files']:
 assert hashlib.sha256((root/info['path']).read_bytes()).hexdigest()==info['sha256'],info['path']
for name in ['integration_manifest_Brauer_zero_D.json','integration_manifest_local_Brauer_zero_D.json']:
 manifest=json.loads((root/'parts/D/post16_research'/name).read_text())
 assert set(manifest['audit_scope'])=={'root','B','C','D'}
receipt=json.loads((root/'code/output/checkpoint17_saved_receipt.json').read_text());assert receipt['status']=='succeeded'
bounded=json.loads((root/'parts/D/post17_research/integration_manifest_bounded_Brauer_period_D.json').read_text())
assert set(bounded['audit_scope'])=={'root','B','C','D'}
assert hashlib.sha256((root/bounded['path']).read_bytes()).hexdigest()==bounded['sha256']
qa=json.loads((root/'qa/pdf_verified.json').read_text())
gates=[
 'Alternating simple-quotient multiplicities and the remaining simple families outside the proved linear/order and bounded-scalar/order criteria.',
 'Unbounded geometric Brauer period in defining-characteristic projective representations on the residual global and complete-local surfaces; each fixed period bound is now covered, with a constant allowed to depend on that bound.',
 'Uncovered cross-characteristic Lie families with order divisible by the ground characteristic.',
 'General monolithic nonabelian crowns with permutation, field or semilinear actions; selected simple-product bounds alone do not suffice.',
 'Full finite generation for the residual nonprojective normal proper surface punctures and original-boundary tame quotients.',
 'Higher-dimensional boundary reductions outside finite omitted loci, controlled exceptional centres and the proved projective-model full-generation criteria; nonnormal D2 scope retained.',
 'Dependent residual L8.'
]
reduction='The former unbounded-scalar projective gate is now restricted to unbounded geometric Brauer period in the proved surface scopes. Uniform q^(C r^2) counts are proved with arbitrary scalar order for Brauer-zero projective representations on normal proper surfaces with original-divisorial tameness and on complete normal equicharacteristic local surfaces without an algebraization hypothesis. A fixed-cover closure handles every fixed bound B on geometric Brauer period, with the constant allowed to depend on B. Fixed detecting surfaces, finite normalization, selected simple-product quotients and the all-dimension local detecting-surface transfer are closures of this one reduction.'
aux=[
 'Integral anti-nef cycles and fixed-multiple cohomology avoid denominator losses but do not give formal determination or a hereditary object atlas.',
 'RDP Hom vanishing, exact two-end framing, the internal-branch counterfamily, finite transverse A-chain jets and actual-full-bundle Artinian rigidity remain auxiliary.',
 'Sparse two-generator DVR charts, including imperfect primitive residue extensions and exact all-ring unpointed Isom witnesses, leave global coefficient poles and the constrained surface-extension locus open.',
 'The rank-r+1 determinant presentation, asymmetric finite-jet gluing and nonzero-Brauer residue/block routes remain research unless separately completed; no advance is inferred from a proposed construction.',
 'Recognition, scope closure, repeated source or proof audits, finite certificates and document work are not additional movement.'
]
review={'review_number':11,'scheduled_utc':due.isoformat(),'actual_utc':now.isoformat(),'preceding_review_actual_utc':prior['actual_utc'],'requested_status_changes':[],'requested_open':prior['requested_open'],'movement':True,'consecutive_no_movement_reviews':0,'strict_main_gate_reductions':[reduction],'remaining_strongest_gates':gates,'auxiliary_not_movement':aux,'checked_post16_files':packet['files'],'latest_successful_checkpoint':17,'latest_completed_visual_verification':{'build':qa['build'],'pages':qa['pages'],'sha256':qa['sha256']},'next_review_utc':'2026-11-20T14:10:00+00:00','next_scheduled_checkpoint_utc':'2026-11-20T13:40:00+00:00','note':'One completed strict reduction since review10, counted once with its scope/transfer consequences. No requested row closes. The historical review10 counter remains unchanged in its own record. Stopping condition is not met.'}
review['checked_bounded_period_closure']={'path':bounded['path'],'sha256':bounded['sha256'],'labels':bounded['labels'],'additional_movement':False}
out.write_text(json.dumps(review,indent=2)+'\n')
with (root/'PROGRESS_LEDGER.md').open('a') as f:
 f.write('\n\n## Formal review11:20 November2026,13:10UTC\n\nINCOMPLETE. Actual review:'+now.isoformat()+'. General D.1, general D.2(ii), and residual L8 remain open; all A/B/C requested rows remain decided. No requested row changed.\n\n'+reduction+'\n\n')
 f.write('The integral-cycle, RDP framing, finite-jet and sparse-DVR estimates remain auxiliary. The proposed core-generation, thickened-branch gluing and nonzero-Brauer graded-block constructions do not yet yield a new quantitative atlas. They do not count as movement. Alternating and uncovered cross-characteristic multiplicities, general crowns and the remaining global geometric reductions are still open.\n\n')
 f.write('Movement:YES, one strict main-gate reduction. Consecutive no-movement reviews:0. The stopping condition is not met. Next formal review12 is14:10UTC; next scheduled checkpoint18 is13:40UTC. Checkpoint17 is the latest saved archive.\n')
p=root/'code/assemble.py';lines=p.read_text().splitlines(keepends=True)
summary='Formal review11 was completed during the scheduled13:10UTC period. All A/B/C requested rows remain decided; general D.1, D.2(ii), and residual L8 remain open. The Brauer-zero projective count removes the scalar-order bound in the proved global and complete-local scopes. Its fixed-cover closure handles every fixed geometric Brauer-period bound, with a constant depending on that bound, leaving unbounded geometric period. This is one strict main reduction; its detecting-surface, normalization and selected-product consequences are grouped with it. The integral-cycle, framing, finite-jet and sparse-DVR statements remain auxiliary. Consecutive no-movement reviews:0. Exact comparison is in code/output/formal_review11.json. Next formal review12 is14:10UTC; next checkpoint18 is13:40UTC. Checkpoint17 remains the latest saved archive; no stopping condition is met.'
for i,line in enumerate(lines):
 if line.startswith("'Formal review10 was completed"):
  lines[i]=repr(summary)+',\n';break
else:raise AssertionError('Review10 summary missing.')
p.write_text(''.join(lines))
print(json.dumps({'review':11,'actual_utc':now.isoformat(),'movement':True,'strict_reductions':1,'consecutive_no_movement_reviews':0}))
