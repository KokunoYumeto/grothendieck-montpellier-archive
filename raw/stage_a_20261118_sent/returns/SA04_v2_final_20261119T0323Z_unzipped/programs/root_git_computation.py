"""Exact verification of the displayed SL2 degeneration, cote100 scans14/16.
The mathematical orbit and stabilizer argument is in root_computation_notes.md.
"""
from pathlib import Path
import sympy as s
import json,datetime
X,Y,l=s.symbols('X Y lambda', nonzero=True)
g=s.Matrix([[0,-1/l],[l,0]])
gi=g.inv()
xp,yp=gi*s.Matrix([X,Y])
linear=s.expand((l*X+Y).subs({X:xp,Y:yp},simultaneous=True))
quartic=s.expand((X**2*Y**2).subs({X:xp,Y:yp},simultaneous=True))
assert linear==-l*X+Y and quartic==X**2*Y**2 and g.det()==1
out={'source':'cote100 scans14/16; left action by inverse substitution',
     'determinant':str(g.det()),'transformed_linear':str(linear),
     'transformed_quartic':str(quartic),'limit_linear_pair':['Y','Y'],
     'phi_on_normal_form':'alpha**2*beta**2',
     'warning':'This is an exact substitution certificate; quotient and stabilizer claims have a separate written proof.'}
p=Path(__file__).resolve().parents[1]/'outputs/root_git_computation.json'
p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
with (p.parents[1]/'progress.log').open('a') as f:f.write(datetime.datetime.now(datetime.timezone.utc).isoformat()+'\troot_git_computation.py\tall assertions passed; outputs/root_git_computation.json\n')
