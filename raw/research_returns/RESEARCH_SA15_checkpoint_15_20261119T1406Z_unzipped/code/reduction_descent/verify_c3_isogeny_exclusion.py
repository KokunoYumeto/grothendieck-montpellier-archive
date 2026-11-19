#!/usr/bin/env python3
"""Universal exact 3-isogeny identities and the 27-to-9 quotient passage."""
from pathlib import Path
import json,time
import sympy as s
started=time.perf_counter()
x,y,a1,a3=s.symbols('x y a1 a3')
X=x+a1*a3/x+a3*a3/x**2
Y=y-a3*(a1*x+2*a3)*y/x**3-a3*(a1*x+a3)**2/x**3
source=y*y+a1*x*y+a3*y-x**3
target=Y*Y+a1*X*Y+a3*Y-X**3+5*a1*a3*X+a3*(a1**3+7*a3)
numerator=s.fraction(s.cancel(target))[0]
remainder=s.rem(s.Poly(numerator,y),s.Poly(source,y)).as_expr()
assert s.expand(remainder)==0
assert s.factor(2*Y+a1*X+a3-(2*y+a1*x+a3)*s.diff(X,x))==0
A4=-5*a1*a3;A6=-a3*(a1**3+7*a3)
b2=a1*a1;b4=2*A4+a1*a3;b6=a3*a3+4*A6
b8=a1*a1*A6-a1*a3*A4-A4*A4
c4=s.expand(b2*b2-24*b4)
disc=s.expand(-b2*b2*b8-8*b4**3-27*b6**2+9*b2*b4*b6)
assert s.factor(c4-a1*(a1**3+216*a3))==0
assert s.factor(disc-a3*(a1**3-27*a3)**3)==0
t,D=s.symbols('t D')
special_c4=s.factor(c4.subs({a1:3*t,a3:t**3-D}))
special_disc=s.factor(disc.subs({a1:3*t,a3:t**3-D}))
special_j=s.factor(special_c4**3/special_disc)
assert s.factor(special_j-27*t**3*(9*t**3-8*D)**3/(D**3*(t**3-D)))==0
valuation_rows=[]
for r in range(-1,1001):
    S=min(3*r,0)
    assert 4+3*r>0
    vj=6+3*r-S
    assert vj>=6
    if r==-1:assert vj==6
    valuation_rows.append({'r':r,'S':S,'v_quotient_j':vj})

# E[27] as (Z/27)^2 and its invariant order-three line C=< (9,0) >.
mod=27
C={(0,0),(9,0),(18,0)}
all_points=[(a,b) for a in range(mod) for b in range(mod)]
T={P for P in all_points if ((9*P[0])%mod,(9*P[1])%mod) in C}
assert len(T)==243
cosets={frozenset(((P[0]+Q[0])%mod,(P[1]+Q[1])%mod) for Q in C) for P in T}
assert len(cosets)==81
def qcoord(P):
    # b is divisible3; x modulo9 and b/3 modulo9 identify T/C with (Z/9)^2.
    assert P[1]%3==0
    return (P[0]%9,(P[1]//3)%9)
assert len({qcoord(P) for P in T})==81
assert all({qcoord(P) for P in Q}=={qcoord(next(iter(Q)))} for Q in cosets)
# Nontrivial unipotent action has exactly one invariant F3-line.
lines=[frozenset((c*a%3,c*b%3) for c in range(3))
       for a,b in [(1,0),(0,1),(1,1),(1,2)]]
stable=[H for H in lines if all(((a+b)%3,b) in H for a,b in H)]
assert stable==[lines[0]]
out={'status':'PASS','universal_isogeny_map':'source equation divides cleared target equation',
     'normalized_differential':'PASS','target_c4':'a1*(a1^3+216*a3)',
     'target_Delta':'a3*(a1^3-27*a3)^3',
     'target_j_Hesse':'27*t^3*(9*t^3-8*D)^3/(D^3*(t^3-D))',
     'valuation_cases':len(valuation_rows),'first_valuation_rows':valuation_rows[:5],
     'module_sizes':{'E27':729,'C':len(C),'preimage_T':len(T),'T_mod_C':len(cosets)},
     'unique_unipotent_invariant_line':sorted(next(iter(stable))),
     'conclusion':'C3/C6 residual level27 opposite-character comparisons excluded',
     'remaining_branch':'C4 with individual special orders3,6 and joint18',
     'elapsed_seconds':time.perf_counter()-started}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
