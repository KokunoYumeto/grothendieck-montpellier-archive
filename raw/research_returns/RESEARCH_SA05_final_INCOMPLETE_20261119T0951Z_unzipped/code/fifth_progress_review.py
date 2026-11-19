"""Execute the scheduled fifth review; preparation is not a review event.

The script cannot run before09:50UTC. Its no-movement decision is to be
used only after the root's actual interval review and agent reports agree.
"""
from pathlib import Path
from datetime import datetime, timezone
from copy import deepcopy
import csv
import json
import time

root=Path(__file__).resolve().parents[1]
start=time.perf_counter()
due=datetime(2026,11,19,9,50,tzinfo=timezone.utc)
now=datetime.now(timezone.utc).replace(microsecond=0)
if now<due:raise SystemExit('Review05 is not due until09:50UTC; no review was written.')
target=root/'progress/review_05.json'
if target.exists():raise SystemExit('Review05 already exists and will not be overwritten.')
previous=json.loads((root/'progress/review_04.json').read_text())
with (root/'ITEM_STATUS.tsv').open(newline='') as f:
    items=list(csv.DictReader(f,delimiter='\t'))
by={r['item']:r for r in items}
rows=deepcopy(previous['open_mathematical_rows'])
for item in rows:rows[item]['recorded_status']=by[item]['status']
attempts={
 'B.1':('The explicit two-boundary comparison has cokernel im(G) intersect ker(cl) on threefold components; it proves neither vanishing nor survival under shrinking. The ordinary Milnor regulator kernel and residue-divisibility lemma now hold in every degree, and the separated quotient is countably free. Their diagonal twist has negative unramified weights, whereas the required degree-three/twist-two residue interval includes zero. The explicit free permutation-submodule completion example blocks an inference from freeness without saturation. The moving lemma permits whole-variety support, and current torsion/divisibility or integral-surjectivity results do not kill the rational Chow kernel.'),
 'B.3':('The previously proved equivalent simply-connected, irregularity-zero, very-ample-canonical surface test class remains the current strict reduction. No algebraic representative has been produced for every fixed divisor class in that class. Later torsion and integral-cycle results either assume surface Tate or cover specified families; they do not prove the retained surface gate.'),
 'B.5':('The exact all-Chow-heart finite-field coefficient-duality dependency remains Beilinson plus Parshin, distinguished from homogeneous pure coefficients and from arithmetic f-admissibility. No general pure-coefficient global regulator comparison, finite Sha assertion or actual rational compact-support duality has been proved. The inspected current logarithm/comparison results retain the relevant global hypotheses.'),
 'C.1(c)':('The finite all-power Chow criterion, without an extra C+ assumption, remains proved. Its actual general vanishings, including the K3 transcendental exterior projector, are not established. Current special-family papers, field-extension injectivity and withdrawn preprints give no general Chow rational equivalence. Field extension does not turn a homological determinant relation into a rational-equivalence relation.'),
 'C.4':('The finite exterior-power test proves universal middle-degree trait endpoint iff weight–monodromy, with r<=j+1 and explicit product/alteration transfers. This is an equivalent universal gate, not a strictly smaller one. The simple-spectrum target theorem replaces target positivity in a sufficient subcase, retaining mixed numerical=homological equivalence and globally squarefree primitive spectrum over a fixed field. No transfer supplies these assumptions universally. The first unrestricted threefold primitive-image pairing remains unproved. The Zhang source corrections are bounded audits, not failures of geometric weight–monodromy.'),
 'C.6':('The finite-field rank-conjecture implication and finite-prime local/global transfer remain sufficient and exact in their stated scopes, but no converse pure-local cycle encoding has been constructed. Blowup/cut cancellation and purity/local-constancy diagnostics exclude the attempted gadgets only. Current conductor formulas yield scalar derived-inertia traces that ignore nilpotent rank even after a homogeneous projector; ordinary Weil traces and reconstruction theorems still do not supply the missing invariant dimension. No general proof or named-conjecture equivalence has emerged.'),
 'Lead B1':('The finite-field degree-extension factor, ordinary/continuous distinctions, explicit limit counterexamples and additional Milnor structure are proved. They leave the same universal Chow comparison and separately stated arithmetic comparison gates unresolved.'),
 'Lead C1':('The precise modified-diagonal identification and the stated finite-power reductions remain proved; the actual general K3 Chow determinant vanishing is still missing. None of the later scope checks supplies it.')
}
next_attempts={
 'B.1':'Control the weight-zero unramified part of degree-three/twist-two residues, or prove a geometric saturation/uniform-support result strong enough to kill the critical projective-space invariant class.',
 'B.3':'Construct the required divisor representatives on the retained simply-connected canonical surfaces, using the precise finite-field Tate formulation rather than an assumed integral-cycle consequence.',
 'B.5':'Establish the actual pure-coefficient f-admissibility and compact-support regulator pairing; retain Beilinson–Parshin where the larger Chow-heart scope is used.',
 'C.1(c)':'Produce a genuine Chow rational equivalence for the general transcendental exterior projector; numerical or cohomological vanishing alone is insufficient.',
 'C.4':'Prove nondegeneracy for the actual primitive restriction image without the retained product or simple-spectrum hypotheses, or supply a universal transfer to a proved class.',
 'C.6':'Construct a pure local realization detecting an arbitrary finite-field cycle, or prove a degreewise ordinary inertia-invariant comparison compatible with the required projectors.',
 'Lead B1':'Attack the same universal Chow and arithmetic comparison gates, keeping ordinary, continuous and completed cohomology distinct.',
 'Lead C1':'Attack the actual general-K3 Chow determinant relation underlying the proved finite criterion.'
}
attempts['B.1'] += (' The ordinary separated quotient is now common to all primes different from p, but the formal common integral module has a completed eigenline only at3. After taking inverse Frobenius and the formal F4 twist, that example matches a weight-zero invariant. The actual elliptic Milnor example separately demonstrates non-root-of-unity eigenvalues in a geometric completion; it is not a prime-dependent geometric counterexample.')
attempts['C.4'] += (' The final transfer check proves that finite constants, smooth projective surface alterations and nonzero Artin-factor twists retain existing primitive spectral multiplicity, so those operations do not supply the sufficient squarefree hypothesis.')
attempts['C.6'] += (' The current geometric conductor and mixed-characteristic singular-support statements retain the missing special-stalk/inertia-invariant and cross-prime comparisons; the BGV Clemens–Schmid exactness statement is conditional on weight–monodromy.')
for item in rows:
    rows[item]['attempts_and_limits']=attempts[item]
    rows[item]['next_attempt']=next_attempts[item]
excluded=[
 'The universal trait endpoint iff weight–monodromy theorem is an equivalent universal formulation, not a strictly smaller gate.',
 'The all-degree ordinary Milnor theorem, free quotient and completion countermodels do not control the actual twist-two weight-zero residue or the invariant colimit.',
 'The simple-spectrum pairing theorem is a sufficient subcase with retained unproved mixed-product and spectrum conditions.',
 'Conductor trace diagnostics and corrected source passages neither close an original open row nor establish the missing pure-local converse.',
 'Independent proof checks, current-source searches, typesetting, indexing and checkpoint packaging are not movement.'
]
count=previous['consecutive_reviews_without_movement']+1
assert len(items)==44 and len(rows)==8 and count==2
record=dict(review=5,scheduled_at=due.isoformat(),reviewed_at=now.isoformat(),
    movement=False,consecutive_reviews_without_movement=count,comparison_review=4,
    movement_evidence=[],not_counted_as_movement=excluded,all_item_rows=items,
    open_mathematical_rows=rows,main_A_status=previous['main_A_status'],
    main_D_status=previous['main_D_status'],B2_scope_note=previous['B2_scope_note'],
    editorial_rows={k:by[k] for k in ['E.1','E.2']},
    next_formal_review=None,next_checkpoint=None,stop_rule=previous['stop_rule'],
    stop_rule_triggered=True,final_status='INCOMPLETE',
    final_preparation_in_progress=True)
lines=[f'\n## Formal hourly review05 — {now:%Y-%m-%d %H:%M:%S} UTC\n',
    'No qualifying mathematical movement occurred after review04. Consecutive formal reviews without movement: **2**. The required stopping rule is now triggered. The research programme is **INCOMPLETE**; remaining work is final verification and packaging, not further mathematical research.\n',
    'All44 item rows are snapshotted in `progress/review_05.json`. Every mathematically open row, the exact failed step and a prospective next attempt are retained below.\n',
    '| Open row | Current gate | Attempts and limit | Prospective next attempt |',
    '|---|---|---|---|']
for item,r in rows.items():
    cells=[item,r['current_gate'],r['attempts_and_limits'],r['next_attempt']]
    lines.append('| '+' | '.join(x.replace('|','\\|') for x in cells)+' |')
lines+=['\nWork excluded from the movement count:\n']+['- '+x for x in excluded]
lines+=['\nReview04 and review05 are the two consecutive no-movement reviews. The stopping instruction takes precedence over the existence of further conceivable approaches; no completion of the open mathematics is claimed.\n']
target.write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
p=root/'PROGRESS_LEDGER.md';p.write_text(p.read_text()+'\n'.join(lines))
p=root/'RESEARCH_SA05_report.md';s=p.read_text()
assert s.startswith('INCOMPLETE')
s+=f'''\n## Final stopping decision\n\nFormal review05 took place at {now:%H:%M:%S} UTC (10:50Europe/Berlin). It found no qualifying movement since review04. These are two consecutive formal reviews without an open-row closure or a strictly smaller proved universal gate, so the user's stopping rule now requires this work to stop. The final status is **INCOMPLETE**. All44 item rows and all8 mathematically open rows remain explicitly recorded, with the strongest proved reductions, exact limitations and prospective next attempts.\n\nThe final package preserves the complete current deliverables and every new or changed work file since the last successful checkpoint. Its file list identifies earlier successful checkpoints holding unchanged supplementary outputs. No earlier ZIP is embedded. The supplied original archive, raw third-party sources and ordinary render images are excluded as required.\n'''
p.write_text(s)
p=root/'RESEARCH_SA05_paper.tex';s=p.read_text()
old='This document is an unfinished research record until every item in the accompanying ledger is discharged.'
new='\\textbf{INCOMPLETE.} The programme stopped under the required two-review rule; the accompanying ledger identifies every unresolved item.'
assert old in s
p.write_text(s.replace(old,new,1))
out=dict(review=5,reviewed_at=now.isoformat(),all_items=len(items),
    open_mathematical_rows=len(rows),movement=False,
    consecutive_without_movement=count,stop_rule_triggered=True,
    seconds=round(time.perf_counter()-start,6))
(root/'code/fifth_progress_review_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
