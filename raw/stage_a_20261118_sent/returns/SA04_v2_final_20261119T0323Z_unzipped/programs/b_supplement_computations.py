"""Exact checks for source-specific supplement; mathematical proofs are in the memo."""
import json, math
from pathlib import Path
import sympy as s

# Every pair over these fields is enumerated, and the projective point at infinity is added.
points={}
for p in (3,5):
    pts=[(x,y) for x in range(p) for y in range(p) if (y*y-x*x*x+2*x)%p==0]
    points[str(p)]={"affine_points":pts,"projective_count":len(pts)+1}
assert points["3"]["projective_count"]==4
assert points["5"]["projective_count"]==10
xP,yP=s.Rational(2),s.Rational(2)
slope=(3*xP*xP-2)/(2*yP)
double_x=slope*slope-2*xP
double_y=slope*(xP-double_x)-yP
assert (double_x,double_y)==(s.Rational(9,4),-s.Rational(21,8))
disc=-16*(4*(-2)**3)
assert disc==512
# In F_2[epsilon]/epsilon^2[x]/(x^2), nabla=d/dx+epsilon*x.
eps=s.symbols("epsilon")
N=s.Matrix([[0,1],[eps,0]])
assert N*N==eps*s.eye(2)
# (e1+e2) tensor squared minus the two pure squares has the two nonzero mixed entries.
v=s.Matrix([1,1]);e1=s.Matrix([1,0]);e2=s.Matrix([0,1])
tensor_defect=s.kronecker_product(v,v)-s.kronecker_product(e1,e1)-s.kronecker_product(e2,e2)
assert list(tensor_defect)==[0,1,1,0]
# Checks of the p-power extraction coefficient; the proof for all d is in prose.
hasse=[]
for p in (2,3,5,7):
    for d in range(1,40):
        q=1;m=d
        while m%p==0:
            m//=p;q*=p
        residue=math.comb(d,q)%p
        assert residue==m%p and residue!=0
        hasse.append({"p":p,"d":d,"q":q,"coefficient_mod_p":residue})
result={
 "elliptic_counterexample":{"equation":"y^2=x^3-2x","section":[2,2],"discriminant":disc,
  "base":"Spec Z[1/30]","points":points,"twice_section":[str(double_x),str(double_y)],
  "torsion_bound_from_reductions":math.gcd(4,10),
  "all_primes_argument":"For p>=7, rational 2-torsion makes Np even; Hasse gives 0<Np<2p, hence gcd(p,Np)=1. This is a written proof, not extrapolation from point counts."},
 "nilpotent_p_curvature":{"base":"F2[epsilon]/epsilon^2","connection":"d+epsilon*x*dx",
  "matrix_on_1_x":str(N),"square":str(N*N),"conclusion":"nonzero p-curvature epsilon, nilpotent square zero"},
 "tensor_power_nonadditivity":{"p":2,"rank":2,"basis_order":["11","12","21","22"],"defect":[int(a) for a in tensor_defect]},
 "hasse_coefficient_finite_checks":{"count":len(hasse),"rows":hasse},
 "scope":"Exact computations only. General proofs, source interpretations, and hypotheses are separately written; no automated verdicts."
}
path=Path("/workspace/scratch/594d1dc856a9/SA04_work/outputs/b_supplement_computations.json")
path.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({k:v for k,v in result.items() if k!="hasse_coefficient_finite_checks"},indent=2))

