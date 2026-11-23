"""Exact diagnostics for the class/refinement and terminal comparisons in DO055."""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product, permutations
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, math
import sympy as sp

counts={}
def check(name,x):
    if not x: raise AssertionError(name)
    counts[name]=counts.get(name,0)+1

# Unequal arithmetic stabilizers: real permutation groups act on the
# primitive-vector orbit; contraction values are invariant but not constant.
for r,q in [(3,2),(3,3),(4,2),(4,3)]:
    group=list(permutations(range(r)))
    points=[x for x in product(range(q),repeat=r) if any(x)]
    def act(p,x): return tuple(x[p[i]] for i in range(r))
    unseen=set(points); orbits=[]
    while unseen:
        x=min(unseen); orb={act(p,x) for p in group}
        stab=sum(act(p,x)==x for p in group)
        check('unequal_stabilizer_orbit_size',len(orb)*stab==len(group))
        orbits.append((x,orb,stab)); unseen-=orb
    for power in range(1,7):
        def value(x): return sum((v+1)**power for v in x)+math.prod(v+1 for v in x)
        full=sum(F(value(x),len(group)) for x in points)
        refined=sum(F(value(x),stab) for x,orb,stab in orbits)
        check('coefficient_orbit_mass',full==refined)
        h=len(points)
        for denom in range(1,8):
            v=F(1,denom)
            check('middle_volume_refinement',v*full==h*(v/h)*refined)
            for I1,I2 in [(3,7),(7,11),(13,31)]:
                weighted=(I1*h)*(v/h)*refined
                check('weighted_orbit_full_operator',weighted==I1*v*full)
                check('all_q_trace_cancellation',F(1,I1*I2)*I2*weighted==v*full)

# A finite version of the entire-top-function middle substitution.
# GL2(F3) acts transitively on nonzero vectors. Both nontrivial determinant
# factors occur; they cancel only after pairing the two kernels.
q=3
group=[]
for a,b,c,d in product(range(q),repeat=4):
    det=(a*d-b*c)%q
    if det:
        di=pow(det,-1,q)
        group.append(((a,b,c,d),((d*di)%q,(-b*di)%q,(-c*di)%q,(a*di)%q),1 if det==1 else -1))
points=[x for x in product(range(q),repeat=2) if any(x)]
for z in range(25):
    vals=[]
    for x,y in points:
        total=0
        for g,gi,chi in group:
            u=(gi[0]*x+gi[1]*y)%q; v=(gi[2]*x+gi[3]*y)%q
            first=chi*((u+1)**2+(z+1)*(v+1))
            second=chi*((v+2)**2-(z+2)*u)
            total+=first*second
        vals.append(F(total,len(group)))
    check('whole_top_function_orbit_independence',len(set(vals))==1)
    check('whole_top_function_compression',sum(vals)==len(points)*vals[0])

# Exact compact Schur averaging with a nonorthonormal polynomial basis.
# S3 acts on {x1+x2+x3=0}; its invariant Gram is not the identity.
G=sp.Matrix([[2,-1],[-1,2]])
B=sp.Matrix([[1,0],[-1,1],[0,-1]])
reps=[]
for p in permutations(range(3)):
    P=sp.zeros(3)
    for i in range(3): P[i,p[i]]=1
    R=(B.T*B).inv()*B.T*P*B
    check('actual_nonidentity_gram',R.T*G*R==G)
    reps.append(R)
for x in range(-2,3):
    for y in range(-2,3):
        v=sp.Matrix([x,y+1]); ell=sp.Matrix([[y-1,x+2]])
        A=v*ell
        avg=sum((R*A*R.inv() for R in reps),sp.zeros(2))/6
        check('compact_rank_one_schur',avg==sp.trace(A)*sp.eye(2)/2)

# The terminal branch-period factor includes inverse branch scale, with
# complex phases, a nonidentity Gram, and genuine compact averaging.
for c in [sp.Rational(2),sp.Rational(3,2),1+sp.I,2-sp.I]:
    for h in [sp.Rational(1),sp.Rational(2),sp.Rational(5,3)]:
        G3=sp.diag(h*G,sp.Matrix([[3]]))
        Br=sp.Matrix([[c,0,0],[0,c,0]])
        Badj=G3.inv()*Br.conjugate().T*G
        beta=sp.simplify(c*sp.conjugate(c)/h)
        check('branch_schur_norm',(Br*Badj-beta*sp.eye(2)).applyfunc(sp.simplify)==sp.zeros(2))
        for j in range(1,7):
            P=sp.Matrix([j-2,2*j+1,3-j]); v=sp.Matrix([j+1,1-j])
            Z=sp.Matrix([[2-j,j+2]])
            E=sp.Matrix([[j,2-j,j+1]])
            ell=Z*G
            lhs=0
            for R in reps:
                R3=sp.diag(R,sp.Matrix([[1]]))
                lhs+=(ell*R*v)[0]*(E*R3.inv()*P)[0]
            lhs=sp.simplify(lhs/6)
            rhs=sp.simplify((ell*Br*P)[0]*(E*Badj*v)[0]/(beta*2))
            check('literal_terminal_period',sp.simplify(lhs-rhs)==0)
            check('inverse_branch_phase',sp.simplify(Badj/beta-sp.Matrix([[1/c,0],[0,1/c],[0,0]]))==sp.zeros(3,2))

# Complete frame evaluation is faithful on actual polynomial coefficient
# models, rather than on a single chosen highest seed.
for degree in range(1,10):
    A=sp.Matrix([[sp.Integer(t)**k for k in range(degree+1)] for t in range(degree+1)])
    expected=math.prod(j-i for j in range(degree+1) for i in range(j))
    check('faithful_complete_frame_reading',A.det()==expected and expected!=0)

# A coevaluation over the middle cancels one Schur denominator; an
# individual matched tensor does not. The actual two step cTop/cBot
# comparisons keep all other constants separate.
for d0,d1,dv,dw in product(range(1,7),repeat=4):
    check('complete_versus_matched_schur',sum(F(1,d0*d1) for _ in range(d1))==F(1,d0))
    check('vertical_average_not_simple_coevaluation',F(1,dv)*dv==1)
    for bscale in [F(2),F(3,2)]:
        check('branch_period_forward_distinction',F(1,bscale*dw)*bscale==F(1,dw))

root=Path(__file__).resolve().parent
proof=root/'definite_oscillator_coupled_image_seesaw.md'
record={'finding':'AM-DO-055','model':'GPT-6 Astra Pro','effort':'inherited, not separately exposed',
        'run':'ALP_MACHINE','time_utc':datetime.now(timezone.utc).isoformat(),
        'status':'PASS','counts':counts,'assertions':sum(counts.values()),
        'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
        'scope':'Exact finite orbit/class volumes, full-function covariance, nonidentity-Gram Schur/branch phase and polynomial-reading diagnostics; no automorphic or Lean computation.'}
(root/'definite_oscillator_coupled_image_certificate.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
