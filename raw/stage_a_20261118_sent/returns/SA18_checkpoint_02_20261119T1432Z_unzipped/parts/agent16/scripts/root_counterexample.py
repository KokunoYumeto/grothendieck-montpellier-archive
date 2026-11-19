"""Exact counterexample to c44:5 lines2893–2915; not a transcription change."""
import sympy as s,json
from pathlib import Path
O=Path(__file__).resolve().parents[1]
roots=[s.Matrix(v) for v in [(3,0),(-3,0),(0,3),(0,-3),(1,1),(-1,-1),(1,-1),(-1,1)]]
rootset={tuple(v) for v in roots}
for a in roots:
    reflection=s.eye(2)-2*a*a.T/(a.dot(a))
    assert {tuple(reflection*b) for b in roots}==rootset
    assert reflection*a==-a
assert roots[0]-roots[4]-roots[6]==s.Matrix([1,0])
assert roots[2]-roots[4]+roots[6]==s.Matrix([0,1])
for a in roots:
    assert [tuple(b) for b in roots if s.det(s.Matrix.hstack(a,b))==0]==[tuple(b) for b in roots if b==a or b==-a]
Q=sum((a*a.T for a in roots),s.zeros(2))
coroot=s.Rational(2,3)*s.Matrix([1,0])
out={'roots':[list(a) for a in roots],'lattice':'Z², explicit generators e1=3e1−(e1+e2)−(e1−e2), e2=3e2−(e1+e2)+(e1−e2)','all_reflections_permute_roots':True,'reduced':True,'dual_invariant_form':str(Q),'root':'3e1','coroot':str(coroot),'pairing_with_e1_plus_e2':str(coroot.dot(s.Matrix([1,1]))),'conclusion':'Axioms a–c do not imply primitive roots or integral coroots. The entire source paragraph is cancelled.'}
(O/'outputs/root_counterexample.json').write_text(json.dumps(out,default=str,indent=2)+'\n')
print(json.dumps(out,default=str,indent=2))
