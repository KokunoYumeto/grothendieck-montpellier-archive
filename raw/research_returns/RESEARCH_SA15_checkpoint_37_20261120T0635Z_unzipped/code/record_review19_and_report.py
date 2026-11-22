"""Record actual review19 only after its due time; packaging is not movement."""
from pathlib import Path
import datetime,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
due=datetime.datetime.fromisoformat('2026-11-19T23:50:40+00:00')
assert datetime.datetime.now(datetime.timezone.utc)>=due
for rel in ['agents/reduction_descent/B_terminal_frobenius_pair.tex',
            'agents/reduction_descent/B_wild_cyclic_point.tex',
            'agents/reduction_descent/B_first_wild_finite_patterns.tex']:
    assert '\\status{Candidate' not in (w/rel).read_text(),rel
movement=[
 'B.4: against review18 the full height-two prime-to-p exact index3 interval strictly grows fromp³<e<p⁴ to p³<e<p³(p+1), by the terminal Frobenius-pair proof B75. Atp5 the previously open prime-to5 multiples of4 from628 through748 are now settled. Actual high quotient levels and the Frobenius-equivalent unequal terminal pair are proved; the abstract next pair is not treated as a counterexample.',
 'B.4: the new B76 rational-point theorem at arbitrary v_p(e) excludes the actualp³ mixed whole-formal/height1-filtered branch at every first wilde=p(p-1). B77 further excludes square finite determinants in the remaining whole-formal branch and proves the full least-index interval{2,3}. Atp5,e20 the actual125-torsion gate is now precisely the two normalized nonsquare whole-formal patternsAB/AC with joint tame degree24. Both are still unresolved. This is a strict reduction of a main gate, not a finite enumeration substituted for existence.'
]
def promoted(rel):
    p=w/rel
    return p.exists() and '\\status{Candidate' not in p.read_text() and '\\textup{[Candidate' not in p.read_text()
if promoted('agents/monodromy/nonordinary_uniform_eleven_theta_geometry.tex'):
    movement.append('A.4: against review18, the fixed-f0 odd degree11 gate is closed by a complete all-modulus nodal norm-eleven self-isogeny and universal algebraic certificate. The good-theta and cubic-component transfer now prove every odd multiple11 on each fixed f0 principally polarized surface in the complete systems|3dTheta|. The proved family is all even degrees, degree1 and odd multiples of3,5,7or11; the first remaining odd degree is13. Both complete independent proof audits and a full independent resultant recomputation passed. Fixedf1degree5/even8 and generalX remain open.')
if promoted('agents/reduction_descent/B_wild_CM_layer.tex'):
    movement.append('B.4: B78 proves exact first-wild least index2 in the potentially CM potentially supersingular subclass, with an actualLT fixed field and actualCMp²-congruent lower pair. Its general nonsquareCM recovery thresholdn>=v_p(e)+2 excludes two-CM members from the remaining first-wild actualp³ comparison. In particular either remainingp5/e20 AB/AC125 failure must contain a non-CM model. The unrestricted index remains in{2,3}.')
assessment={
 'due_utc':due.isoformat(),
 'next_checkpoint_due_utc':'2026-11-20T00:35:40+00:00',
 'movement':movement,
 'unresolved_refinements':[
  'General A.3/A.4 remain open. The primitive mixed-polarization mapdim imPsi_s>=2 is not proved by the connection or boundary-kernel calculations alone.',
  'Only a canonically promoted full norm-eleven proof is counted above; the actual universal certificate and all geometric exceptional cases are required. Later norm-thirteen or other candidate calculations are not promoted by this review.',
  'Higher-dimensional B.3, the remaining wild whole-formal actual125 comparisons, larger tame exact-index intervals and higher heights remain open.',
  'The single-class transvection route, marked-normalization triple-collision obstruction, rational/residual countermodel, literature work and checkpoint production do not shrink a main gate and are not counted as movement.'
 ]}
p=w/'notes/review19_assessment.json'
assert not p.exists()
p.write_text(json.dumps(assessment,indent=2)+'\n')
subprocess.run([sys.executable,str(w/'code/update_current28.py')],cwd=w,check=True)
subprocess.run([sys.executable,str(w/'code/record_review.py'),'19',str(p)],cwd=w,check=True)
r=json.loads((w/'notes/progress_review_19.json').read_text())
assert r['no_movement_streak']==0 and r['movement']
text=('\n### Actual hourly review19\n\n'
 f"Actual review19 was recorded at {r['actual_utc']} against review18 at {r['baseline_actual_utc']}. "
 'The full prime-to-p height-two exact third-index interval is strictly larger, '
 'and the first-wild actualp³ comparison has been reduced to nonsquare whole-formal '
 'pairs, specificallyAB/AC atp5,e20. Any additional promoted main-gate movement '
 'is enumerated explicitly in the immutable review record. The no-movement '
 'streak is zero; disposition:Continue. Searches, packaging and auxiliary '
 'route limitations are excluded from the movement count. Checkpoint28 is '
 'due23:50:40UTC, checkpoint29 at00:35:40UTC and actual review20 at00:50:40UTC '
 'on20November2026.\n')
for rel in ['notes/checkpoint28_changes.md','RESEARCH_SA15_report.md']:
    with (w/rel).open('a') as f:f.write(text)
print(text)
