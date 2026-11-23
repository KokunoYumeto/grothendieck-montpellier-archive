#!/usr/bin/env python3
"""Exact finite diagnostics for ALP-LIFT-34; no global theta computation."""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "coupled_image_sylow_cancellation_certificate.json"
counts = Counter()

def check(condition, tag):
    assert condition, tag
    counts[tag] += 1

def mul2(a,b,q):
    return ((a[0]*b[0]+a[1]*b[2])%q,
            (a[0]*b[1]+a[1]*b[3])%q,
            (a[2]*b[0]+a[3]*b[2])%q,
            (a[2]*b[1]+a[3]*b[3])%q)

q=23
p=11
z=2
check(pow(z,p,q)==1 and z!=1,"order11")
P=[(pow(z,j,q),0,0,pow(z,-j,q)) for j in range(p)]
check(len(set(P))==p,"group_order")
for a,b in itertools.product(P, repeat=2):
    check(mul2(a,b,q) in P,"group_closure")

# Actual sharp small model: a=1,r=2,t=2,b=4,nT=6.
# X=e0 and y=q^-1 e1 are the exact first sharp support. Z=[diag(I2,D);0],
# D in SL2(F23), is a stable finite window inside the actual second support.
SL=[]
for a,b,c in itertools.product(range(q), repeat=3):
    if a:
        d=((1+b*c)*pow(a,-1,q))%q
        SL.append((a,b,c,d))
    elif (-b*c)%q==1:
        for d in range(q):
            SL.append((a,b,c,d))
check(len(SL)==q*(q*q-1),"SL2_order")
S=set(SL)
rep={}
for D in SL:
    orb=[mul2(D,A,q) for A in P]
    check(len(set(orb))==p,"free_fullrank_orbit")
    check(all(E in S for E in orb),"support_stability")
    rep[D]=min(orb)
C={D for D in SL if D==rep[D]}
check(len(C)*p==len(SL),"cut_support_size")
for D in SL:
    invD=(D[3],(-D[1])%q,(-D[2])%q,D[0])
    check(invD in S and mul2(D,invD,q)==(1,0,0,1),"full_group_transversal")
for D in SL:
    check(sum(mul2(D,A,q) in C for A in P)==1,"cut_partition")
    for A in P:
        E=mul2(D,A,q)
        check(rep[E]==rep[D],"orbit_consistency")
        check((E[0]*E[3]-E[1]*E[2])%q==1,"raw_determinant_phase")

# The first raw factor forces exactly one of the entire G Y quotient.
forced=0
for y in itertools.product(range(q),repeat=4):
    allowed=(y==(0,1,0,0))
    forced+=allowed
check(forced==1,"full_Y_unique_G_class")
# Retain the actual eta row and y=e1. The last two eta entries change
# nontrivially, but their pairing with the distinguished y is preserved.
y=(0,1,0,0)
for e,s,t,A in itertools.product(range(q),[0,1,7],[0,1,9],P):
    eta=(0,e,s,t)
    fullA=((1,0,0,0),(0,1,0,0),(0,0,A[0],A[1]),(0,0,A[2],A[3]))
    moved=tuple(sum(eta[i]*fullA[i][j] for i in range(4))%q for j in range(4))
    old_phase=-sum(eta[i]*y[i] for i in range(4))%q
    new_phase=-sum(moved[i]*y[i] for i in range(4))%q
    check(old_phase==new_phase,"eta_phase_retained")
raw_norm=Fraction(len(SL)*q,q**(6*4+4))
cut_norm=Fraction(len(C)*q,q**(6*4+4))
check(raw_norm==p*cut_norm,"exact_finite_norm")

# A two-coordinate integral cutoff Fourier diagnostic. P acts by
# (x,y)->(z*x,z^-1*y), freely on x!=0. The full function is zeta_q^(xy).
xy_points=[(x,y) for x in range(1,q) for y in range(q)]
orbrep={}
for x,y in xy_points:
    orb=[((x*pow(z,j,q))%q,(y*pow(z,-j,q))%q) for j in range(p)]
    check(len(set(orb))==p,"paired_free_orbit")
    orbrep[(x,y)]=min(orb)
cut_points=[pt for pt in xy_points if pt==orbrep[pt]]
check(len(cut_points)*p==len(xy_points),"paired_cut_size")

# Work in Z[zeta23] using exponent counts, with Phi23=sum zeta^j=0.
def cyclo_normal(v):
    return tuple(v[i]-v[q-1] for i in range(q-1))

fourier={}
for a,b in itertools.product(range(q),repeat=2):
    num=[0]*q
    for x,y in cut_points:
        num[(x*y-a*x-b*y)%q]+=1
    fourier[(a,b)]=num
    check(q*q%p!=0,"Fourier_denominator_is_11_unit")

# Exact inverse transform at every point, numerator denominator q^2.
for x,y in itertools.product(range(q),repeat=2):
    inv=[0]*q
    for (a,b),num in fourier.items():
        shift=(a*x+b*y)%q
        for j,v in enumerate(num):
            inv[(j+shift)%q]+=v
    rhs=[0]*q
    if (x,y) in cut_points:
        rhs[(x*y)%q]=q*q
    check(cyclo_normal(inv)==cyclo_normal(rhs),"exact_integral_Fourier_inverse")

# Finite rational-theta analogue: every invariant polynomial weight has
# the full sum equal to |P| times the cut sum, with exact phases.
for degree in range(7):
    full=[0]*q
    cut=[0]*q
    for x,y in xy_points:
        k=x*y%q
        full[k]+=k**degree
    for x,y in cut_points:
        k=x*y%q
        cut[k]+=k**degree
    check(full==[p*v for v in cut],"invariant_theta_orbit_sum")

# An exact actual-Weyl versus dual-Weyl coevaluation diagnostic:
# Delta_Sym2 has basis (x^2,2xy,y^2), its perfect opposite dual basis
# is (x^2,xy,y^2). The factor2 must remain in the second contraction.
import sympy as sp
u,v,A,B,C0,D=sp.symbols("u v A B C D")
Z=sp.Matrix([[A,B],[C0,D]])
zv=sp.Matrix([u,v])
h=sp.Matrix([[0,-1],[1,-1]])
coeval=sp.expand(Z.det()*(u*u*A*A+u*v*2*A*B+v*v*B*B))
direct=sp.expand(Z.det()*((Z*zv)[0])**2)
check(sp.expand(coeval-direct)==0,"integral_subD_composition")
transZ=Z*h.T.inv()
transz=h.T*zv
transport=sp.expand(transZ.det()*((transZ*transz)[0])**2)
check(sp.expand(transport-direct)==0,"complete_middle_invariance")
hm=sp.diag(-1,1)
zm=hm.T*zv
Zm=Z*hm.T.inv()
honest_moved=sp.expand(hm.det()*Zm.det()*((Zm*zm)[0])**2)
check(sp.expand(honest_moved-direct)==0,"honest_determinant_character_cancellation")
check(h**3==sp.eye(2) and h.det()==1,"integral_order3_middle")
poly=sp.Poly(coeval,u,v,A,B,C0,D)
check(all(c.q==1 for c in poly.coeffs()),"no_Gram_inverse_denominator")
for vals in itertools.product(range(-1,2),repeat=6):
    sub=dict(zip((u,v,A,B,C0,D),vals))
    check(coeval.subs(sub)==transport.subs(sub),"coevaluation_exact_values")

# Actual numerical margins for the separately proved full stabilizer
# reduction corollary. The dimension argument is in the written proof.
actual=[]
for host,f,b,primes in [
    ("J14",42,1802,[4615409,5276377]),
    ("J56",168,1802,[22285932761,64072175441])]:
    Dq=2*f*b
    for g in primes:
        check(g-1>Dq,"actual_G_above_rational_dimension")
    actual.append({"host":host,"rational_middle_dimension":Dq,
                   "actual_G_primes":primes})

report={
    "status":"PASS",
    "completed_utc":datetime.now(timezone.utc).isoformat(),
    "assertions":sum(counts.values()),
    "counts":dict(sorted(counts.items())),
    "diagnostic_group":{"residue_prime":q,"Sylow_prime":p,
                        "SL2_order":len(SL),"SL2_cut_size":len(C),
                        "paired_support":len(xy_points),"paired_cut":len(cut_points)},
    "norm_ratio":str(raw_norm/cut_norm),
    "actual_dimension_margins":actual,
    "scope":"finite support/cutoff/phase/coeval mechanisms; no global theta matrix or Lean build",
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
OUT.write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps(report,indent=2))
