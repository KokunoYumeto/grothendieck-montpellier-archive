"""Perform actual review24 only after its due time, from canonical audited results."""
from pathlib import Path
import datetime,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
due=datetime.datetime.fromisoformat('2026-11-20T04:50:40+00:00')
assert datetime.datetime.now(datetime.timezone.utc)>=due
canonical=[
 'agents/obstructions_crystals/A4_Lang_wedge_pole_theta_bound.tex',
 'agents/obstructions_crystals/A4_compatible_residual_modules.tex',
 'agents/reduction_descent/B_residual_wild_last_crossing.tex',
 'agents/reduction_descent/B_both_large_tracefree_rows.tex',
 'agents/reduction_descent/B_remaining_tracefree_rows.tex']
for rel in canonical:
 p=w/rel
 assert p.exists() and '\\status{Candidate' not in p.read_text() and '\\textup{[Candidate' not in p.read_text(),rel
audits=[
 'outputs/root_Lang_wedge_pole_theta_bound_audit.json',
 'agents/monodromy/outputs/independent_Lang_wedge_pole_theta_bound_audit.json',
 'outputs/root_compatible_residual_modules_audit.json',
 'agents/monodromy/outputs/independent_compatible_residual_modules_audit.json',
 'outputs/root_B93_audit.json',
 'agents/obstructions_crystals/B93_independent_audit.json',
 'outputs/root_B94_audit.json',
 'agents/obstructions_crystals/B94_independent_audit.json',
 'outputs/root_B95_audit.json',
 'agents/obstructions_crystals/B95_independent_audit.json']
for rel in audits:
 r=json.loads((w/rel).read_text())
 assert 'PASS' in r.get('status',r.get('result','')),rel
assessment={
 'due_utc':due.isoformat(),
 'next_checkpoint_due_utc':'2026-11-20T05:05:40+00:00',
 'movement':[
  'A.4: the fully audited canonical determinant-wedge/theta-degree proof bounds the exceptional module by dim(K_d)<=9d^2-1-max(8,3d). Compatible actual intermediate residual modules sharpen this at an odd prime ell to dim(K_ell)<=(ell+1)f floor((6ell-1)/f), f=ord_ell(2). At the first remaining degree17, rank2600 now has dim(K_17)<=1728 and quotient dimension>=872, strictly improving the preceding bound dim(K_17)<=2592 and quotient>=8. The exact full-image gate is still K_d=0; no new full-image degree or all-X effective bound is claimed.',
  'B.4: fully audited canonical B93 excludes the last residual-wild crossing(5,45). B94 excludes six both-large(3,4) parameter pairs, and B95 excludes the remaining four by a critical coefficient bound and exact actual-field conductor contradictions. Thus a residual-wild actual125 different-character comparison at p5,e20 must have full Iwahori image of order5^9 with both layers M2(F5). This removes both crossing and all tracefree-first-layer alternatives left at review23. The full Iwahori and residual-irreducible wild orders5^5 through5^8 remain undecided; the least manuscript index stays in{2,3}.'
 ],
 'unresolved_refinements':[
  'Every open row is reviewed in the accompanying current-state table: general A.3; exact whole-image/effective all-large-degree A.4; higher-dimensional B.3; general B.4. Their general statuses remain OPEN. A.5 remains fully closed in its every-X, every-residue, every-open scope with the explicit proved bound.',
  'A.3 primitive mixed positive-index ranks and arbitrary-X ranks have not advanced. The first remaining fixed f0 exact-group odd degree is17; the fixed f1 first odd/even gaps remain5 and8. Dimension bounds and the irreducible main component do not determine the exceptional action or components.',
  'The one-axis product determinant cube and the uniform two-axis reduced cross determinant delimit proposed wall arguments, but neither proves the needed Frobenius-cycle wall or a new fixed-surface full image. They are not counted as main-gate movement.',
  'The primitive type(1,3) stability/Cartier route is saved as an explicitly unpromoted research note. Generic separability is not silently substituted for a smooth-family or full-wall witness. No movement is credited to it.',
  'Conditional cyclic-intermediate full-image criteria, source searches, exact finite profiles without realization, audits and checkpoint production are not independently counted as movement. No surviving arithmetic pattern is asserted to occur.'
 ]}
p=w/'notes/review24_assessment.json';assert not p.exists()
p.write_text(json.dumps(assessment,indent=2)+'\n')
subprocess.run([sys.executable,str(w/'code/update_current35.py')],cwd=w,check=True)
subprocess.run([sys.executable,str(w/'code/record_review_markdown_safe.py'),'24',str(p)],cwd=w,check=True)
r=json.loads((w/'notes/progress_review_24.json').read_text())
assert r['no_movement_streak']==0 and len(r['movement'])==2
assert {x['item'] for x in r['open_rows']}=={'A.3','A.4','B.3','B.4'}
message=('\n### Actual hourly review24\n\n'
 f"Review24 occurred at {r['actual_utc']}, against actual review23 at {r['baseline_actual_utc']}. "
 'The wedge/theta and compatible-module theorems strictly reduce the allowed exceptional module; at degree17 its dimension is at most1728 in rank2600, with quotient at least872. B93-B95 exclude both crossings and the entire residual-wild tracefree first layer at p5,e20, leaving the full Iwahori5^9 branch and the unchanged irreducible-residual sector. '
 'General A.3,A.4,B.3,B.4 remain open, and A.5 remains fully closed. The product determinant results and unpromoted primitive-system route are not independently counted as movement. Consecutive no-movement count: zero; disposition: Continue. '
 'Checkpoint35 is due05:05:40UTC. Next actual review25 and checkpoint36 are both due05:50:40UTC on20November2026.\n')
for rel in ['notes/checkpoint35_changes.md','RESEARCH_SA15_report.md']:
 with (w/rel).open('a') as f:f.write(message)
print(message)
