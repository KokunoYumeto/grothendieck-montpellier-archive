"""Record actual review22 at or after its due time; no candidate or packaging counts as movement."""
from pathlib import Path
import datetime,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
due=datetime.datetime.fromisoformat('2026-11-20T02:50:40+00:00')
assert datetime.datetime.now(datetime.timezone.utc)>=due
def promoted(rel):
 p=w/rel
 return p.exists() and '\\status{Candidate' not in p.read_text() and '\\textup{[Candidate' not in p.read_text()
assert promoted('agents/reduction_descent/B_p5_third_point_ramification.tex')
assert promoted('agents/obstructions_crystals/A4_Moore_Fermat_nondivisibility.tex')
assert promoted('agents/monodromy/ppav_all_odd_full_root_inertia.tex')
for rel in ['outputs/root_B90_audit.json','agents/monodromy/outputs/independent_B90_third_point_ramification_audit.json','outputs/root_Moore_Fermat_full_audit.json','agents/reduction_descent/outputs/independent_Moore_Fermat_full_audit.json','outputs/root_odd_wall_full_audit.json','agents/reduction_descent/outputs/independent_odd_wall_full_audit.json']:
 r=json.loads((w/rel).read_text())
 assert 'PASS' in r.get('status',r.get('result','')),rel
assessment={
 'due_utc':due.isoformat(),
 'next_checkpoint_due_utc':'2026-11-20T03:35:40+00:00',
 'movement':[
  'B.4: B90 excludes the entire p5/e20 tame reducible residual branch for different-special-character actual125-torsion comparisons. Review21 left the full5^8 principal congruence kernel as the necessary possible image. Actual third-point fields now determine its terminal filtration, and the exact actual determinant-coset average would be1896/5, impossible for the integral lower break of a quotient automorphism. This branch is closed, while irreducible-residual and nontrivial-residual-wild sectors remain.',
  'A.4: on the structural route for every fixed nonordinary principal surface and every odd principal-cube degree, the former local wall-nonemptiness condition is proved. The universal Fermat nondivisibility theorem and exact same-coordinate Cartier block comparison produce a point on the maximal common-rank Hasse wall. The full moving-kernel argument then supplies a complete hyperplane radical of order2^(9d^2-2). The local nonemptiness/inertia gate is removed; the unresolved structural gate is global generation or an adequate irreducibility/connectivity theorem. No new exact full-group degree is claimed.'
 ],
 'unresolved_refinements':[
  'General A.3 and A.4 remain open. A.4 still asks for the exact whole image for every X and an effective all-large-degree result. Counterexamples, the finite algorithm and the new local subgroup do not close that row. The previously stated first fixed-image gaps remain f0 odd17 and f1 odd5/even8.',
  'A.5 remains completely closed in the required every-X, every-residue and every-open scope with the explicit bound already proved. No repeated result is counted as movement.',
  'Higher-dimensional B.3 and general B.4 remain open. The first-wild unrestricted least manuscript index remains in{2,3}; the eliminated p5 tame branch is not confused with the remaining irreducible or residual-wild cases.',
  'B89 realizes the cyclotomic break3 on an explicit base but constructs no Barsotti-Tate comparison and contributes no gate movement. The standalone algebra certificate is counted only through the fully audited local-wall consequence. Earlier common-incidence work preceding review21 is not counted again.',
  'Source retrieval, packaging, layout verification, coefficient searches, failed attempts and unpromoted candidates are excluded from movement. The incomplete exterior-covector and global-generation ideas remain leads only.'
 ]}
p=w/'notes/review22_assessment.json';assert not p.exists()
p.write_text(json.dumps(assessment,indent=2)+'\n')
subprocess.run([sys.executable,str(w/'code/update_current32.py')],cwd=w,check=True)
subprocess.run([sys.executable,str(w/'code/record_review_markdown_safe.py'),'22',str(p)],cwd=w,check=True)
r=json.loads((w/'notes/progress_review_22.json').read_text())
assert r['no_movement_streak']==0 and len(r['movement'])==2
text=('\n### Actual hourly review22\n\n'
 f"Actual review22 was recorded at {r['actual_utc']} against review21 at {r['baseline_actual_utc']}. "
 'B90 removes the entire p5/e20 tame reducible residual branch. The same-coordinate Fermat and Cartier argument closes the local wall-nonemptiness/inertia gate for every odd principal-cube system, leaving the global generation question. '
 'General A.3, A.4, higher-dimensional B.3 and general B.4 remain open; A.5 remains fully closed. No new exact full-image degree is claimed. '
 'The consecutive no-movement count is zero; disposition: Continue. Checkpoint32 is due02:50:40UTC; checkpoint33 is due03:35:40UTC and actual review23 is due03:50:40UTC on20November2026.\n')
for rel in ['notes/checkpoint32_changes.md','RESEARCH_SA15_report.md']:
 with (w/rel).open('a') as f:f.write(text)
print(text)
