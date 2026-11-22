"""Perform actual review25 only after05:50:40, against audited canonical results."""
from pathlib import Path
import datetime,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
due=datetime.datetime.fromisoformat('2026-11-20T05:50:40+00:00')
assert datetime.datetime.now(datetime.timezone.utc)>=due
required=json.loads((w/'notes/checkpoint36_promoted_inputs.json').read_text())
assert len(required)==7
for rel in required:
 p=w/rel;assert p.exists() and '\\status{Candidate' not in p.read_text(),rel
audits=['outputs/root_B96_audit.json','agents/obstructions_crystals/B96_independent_audit.json',
 'outputs/root_B97_audit.json','agents/monodromy/outputs/independent_B97_point_field_layers_audit.json',
 'outputs/root_B98_audit.json','agents/obstructions_crystals/B98_independent_audit.json',
 'outputs/root_odd_Cartier_evaluation_audit.json','agents/monodromy/outputs/independent_odd_Cartier_evaluation_audit.json',
 'outputs/root_prime_Heisenberg_rank_audit.json','agents/obstructions_crystals/prime_Heisenberg_independent_audit.json',
 'outputs/root_primitive_prime_generic_rank_audit.json','agents/obstructions_crystals/primitive_prime_generic_rank_independent_audit.json']
for rel in audits:
 r=json.loads((w/rel).read_text());assert 'PASS' in r.get('status',r.get('result','')),rel
assessment={
 'due_utc':due.isoformat(),'next_checkpoint_due_utc':'2026-11-20T06:35:40+00:00',
 'movement':[
  'B.4 strictly shrinks: the entire first-wild height-two instance(p,e,h)=(5,20,2), previously reduced to the residual-wild full Iwahori5^9 and irreducible-residual orders5^5 through5^8, is now closed with exact least manuscript index2. B96 excludes the former; B97 proves actual point degrees and conductor bounds; B98 uses the two-tower cyclotomic different and the actual terminal character to exclude the latter. Earlier determinant/mixed and tame reducible reductions exhaust the full setting, while the explicit actual25-torsion counterexample proves sharpness. The whole irreducible-residual branch at e=p(p-1) is also excluded for every p>=5. General B.4 remains open in the other stated families.',
  'A.3 strictly shrinks in the primitive polarization gate: for every fixed nonordinary abelian surface in characteristic2 with an ample globally generated type(1,ell) line, ell=3,5,7,11,13,17, the generic smooth curve has genus ell+1 and p-rank f(A)+ell-1. Odd theta descent supplies a smooth member, and the actual Euler criterion combined with the birational Pfaffian map proves generic rank ell-1. These are complete geometric rank results for the stated types, not merely tensor-rank experiments; untested primitive cases and the arbitrary-X question remain open.'
 ],
 'unresolved_refinements':[
  'Every general open row is reviewed in the accompanying current-state table: A.3, exact whole-image/effective all-large A.4, higher-dimensional B.3, and general B.4. Their statuses remain OPEN. A.5 remains fully closed for every X, residue and nonempty open under the explicit proved bound.',
  'The globally generated primitive type(1,3) source case has full GL2(F2) relative image, a reduced Euler cubic, a nonempty smooth-member open and sharp relative stable rank2. This is a precisely stated additional source case and does not close the fixed-principal degree17 whole-image question.',
  'Odd-polarization Cartier surjectivity, generic rank4 evaluation for Euler characteristic prime to6, universal Heisenberg Pfaffian certificates through prime17 and the birational radical map are proved. The separate geometric consequence now proves the stated primitive sharp ranks. Neither it nor the algebraic ingredients establish the common wall, stable loss, Lang connectedness, exceptional module K=0 or a new full-principal degree. Packaging and proof audits are not independently counted as movement.',
  'At the fixed f0 degree17 gate, the previous strongest bound remains dimK<=1728 in rank2600, with quotient dimension>=872; the exact group still requires K=0. The f1 first odd/even gaps remain5 and8. No all-X effective degree threshold for full image is supplied.',
  'The full first-wild conclusion beyond p5, other wild absolute indices, later tame exact intervals including p5/e752 with bounds3<=nu<=4, and higher heights remain open. The p5/e20 patterns are no longer open patterns or claimed realizations: they have all been excluded. No new exact index is inferred from a finite profile alone.'
 ]}
p=w/'notes/review25_assessment.json';assert not p.exists();p.write_text(json.dumps(assessment,indent=2)+'\n')
subprocess.run([sys.executable,str(w/'code/update_current36.py')],cwd=w,check=True)
subprocess.run([sys.executable,str(w/'code/record_review_markdown_safe.py'),'25',str(p)],cwd=w,check=True)
r=json.loads((w/'notes/progress_review_25.json').read_text())
assert r['no_movement_streak']==0 and len(r['movement'])==2
assert {x['item'] for x in r['open_rows']}=={'A.3','A.4','B.3','B.4'}
message=('\n### Actual hourly review25\n\n'
 f"Review25 occurred at {r['actual_utc']}, against actual review24 at {r['baseline_actual_utc']}. "
 'The exact first-wild height-two case nu_min(5,20,2)=2 is now proved, and irreducible-residual first-wild character recovery holds for every p>=5. These remove actual possibilities in the previous B.4 gate. A.3 also advances: the globally generated primitive prime types through17 now have proved smooth opens and sharp relative stable rank ell-1. No full degree17 group conclusion is inferred. General A.3,A.4,B.3,B.4 remain open, and A.5 remains fully closed. Consecutive no-movement count: zero; disposition: Continue. '
 'Checkpoint36 is due05:50:40UTC. Next checkpoint37 is due06:35:40UTC; next actual review26 is due06:50:40UTC on20November2026.\n')
for rel in ['notes/checkpoint36_changes.md','RESEARCH_SA15_report.md']:
 with (w/rel).open('a') as f:f.write(message)
print(message)
