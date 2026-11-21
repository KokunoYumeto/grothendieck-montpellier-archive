"""Exact arithmetic checks for SIGN_NEXT SN-12 and SN-14.

These are computation checks, not Lean certificates.  The paper gives
the proofs; this script independently verifies their finite calculations.
"""
from pathlib import Path
import json
import sympy as s

T = s.symbols('T')
f = T**4 - 5*T**2 + T + 1
quadratics = [T**2+1, T**2+T+2, T**2+2*T+2]
remainders = [s.rem(f, q, domain=s.GF(3)) for q in quadratics]
assert all(s.Poly(r, T, modulus=3) != 0 for r in remainders)
assert all(int(f.subs(T, x)) % 3 for x in range(3))
assert s.rem(f-(T+1)*(T**3+T**2+1), 2, domain=s.ZZ) == 0
intervals = [(-3,-2),(-1,0),(0,1),(2,3)]
assert all(f.subs(T,a)*f.subs(T,b)<0 for a,b in intervals)
group, alternating = s.polys.numberfields.galois_group(f,T)
assert group.order() == 24 and not alternating

N=s.Matrix([[0,1,0],[0,0,1],[0,0,0]])
J=s.Matrix([[0,0,1],[0,-1,0],[1,0,0]])
a0,a1,a2,c,z,t=s.symbols('a0 a1 a2 c z t')
a=a0*s.eye(3)+a1*N+a2*N**2
expN=s.eye(3)+N+N**2/2
exp_tN=s.eye(3)+t*N+t**2*N**2/2
assert N**3 == s.zeros(3) and N**2 != s.zeros(3)
assert J.inv()*N.T*J == -N
assert expN.T*J*expN == J
assert s.trace(a*exp_tN) == 3*a0
assert s.expand((s.eye(3)-z*expN).det() - (1-z)**3) == 0
data={
 'SN-12': {'polynomial':str(f),'discriminant':int(s.discriminant(f,T)),
           'mod3_remainders':list(map(str,remainders)),
           'sign_intervals':intervals,'galois_group_order':int(group.order())},
 'SN-14': {'nilpotent_cube_zero':True,'skew_adjoint_for_J':True,
           'expN_preserves_J':True,
           'coefficient_trace':str(s.trace(a*exp_tN)),
           'unipotent_local_polynomial':str((1-z)**3)}
}
out=Path(__file__).with_name('root_example_checks.json')
out.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
