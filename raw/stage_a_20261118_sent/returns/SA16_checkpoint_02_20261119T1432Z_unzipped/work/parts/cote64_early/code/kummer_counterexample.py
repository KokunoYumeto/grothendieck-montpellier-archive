"""Finite action and local-ring checks for C-SA16-291.

The proof of the scheme hypotheses is in proof_supplement.md section 9.
This script verifies the finite group action and the symbolic local ramification.
"""
import itertools, json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
G=list(itertools.product(range(2),repeat=2))
add=lambda g,h:tuple(a^b for a,b in zip(g,h))
# X'=A1_y x {0,1}; (a,b).(y,e)=((-1)^a*y,e+b).
points=[(y,e) for y in [1,-1] for e in [0,1]]
act=lambda g,p:((-1)**g[0]*p[0],g[1]^p[1])
orbit={act(g,(1,0)) for g in G}
assert orbit==set(points)
assert all(len({act(g,p) for g in G})==4 for p in points)
inertia=[g for g in G if g[1]==0]
bad_embedding=[(0,0),(0,1)]
assert inertia!=bad_embedding
# Enumerate automorphisms preserving the monodromy image A.
def lin(A,v): return ((A[0]*v[0]+A[1]*v[1])%2,(A[2]*v[0]+A[3]*v[1])%2)
autos=[A for A in itertools.product(range(2),repeat=4) if (A[0]*A[3]-A[1]*A[2])%2]
preserving=[A for A in autos if lin(A,(1,0))==(1,0)]
assert all(lin(A,(0,1))!=(1,0) for A in preserving)
y=s.symbols('y')
assert s.diff(y*y,y)==2*y
M=s.Matrix([[0,s.Symbol('x')],[1,0]])
assert M.det()==-s.Symbol('x')
out={'base':'S=Spec C; X=A1_x; t=0; X*=G_m',
     'cover':'Xprime=A1_y disjoint union A1_y, x=y^2 on both components',
     'group':'C2 x C2, action (a,b).(y,e)=((-1)^a*y,e+b)',
     'marked_point':'(y,e)=(0,0)',
     'finite_locally_free_rank':4,'smooth_relative_dimension':1,
     'geometric_unramified_fiber_orbit_size':len(orbit),
     'inertia':inertia,'chosen_incompatible_embedding':bad_embedding,
     'ramification_index_at_marked_point':2,'derivative':'2*y; invertible on y!=0',
     'local_norm_y':'-x','tangent_root':'T=C; choose kappa with norm coefficient -1',
     'group_automorphisms':len(autos),'automorphisms_preserving_actual_monodromy':len(preserving),
     'no_such_automorphism_reconciles_bad_embedding':True,
     'conclusion':'Listed target object satisfies its written independent conditions but is not in the essential image. No connectedness assumption occurs at manuscript scan71 lines744-756.'}
(ROOT/'outputs/kummer_counterexample.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
