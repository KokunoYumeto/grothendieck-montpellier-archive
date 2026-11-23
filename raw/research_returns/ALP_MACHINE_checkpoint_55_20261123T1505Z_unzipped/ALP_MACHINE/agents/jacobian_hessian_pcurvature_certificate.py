#!/usr/bin/env python3
"""Exact finite constants and failed next-divisibility checks for AM-K017.

The global normality argument is a proof in the companion Markdown file.
This script supplies only the exact finite algebraic computations used there.
"""
from datetime import datetime, timezone
from math import factorial
from pathlib import Path
import hashlib
import json
import sympy as sp
import jacobian_theta_direction_jets as recurrence

BASE = Path(__file__).resolve().parent
z = sp.Symbol('z')
phi = sum(z**i for i in range(7))
OriginalCyc = recurrence.Cyc
Expr, const = recurrence.Expr, recurrence.const


class CycWithCompositeModulus(OriginalCyc):
    """Invert via Q[Z]/Phi7, then reduce; never treat Z/121 as a field."""
    def inv(self, a):
        if self.p is None:
            return super().inv(a)
        polynomial = sum(int(v)*z**i for i, v in enumerate(a))
        inverse = sp.Poly(sp.invert(polynomial, phi, z), z)
        result = tuple((int(inverse.nth(i).p) *
                        pow(int(inverse.nth(i).q), -1, self.p)) % self.p
                       for i in range(6))
        assert self.mul(a, result) == self.one
        return result


def selected_flow(direction, order, modulus=11):
    R = CycWithCompositeModulus(modulus)
    x = [Expr(R, 'var', initial=R.zeta(j)) for j in (1,3,5)]
    y = [Expr(R, 'var', initial=R.zero) for _ in range(3)]
    inverses = {(j,k):Expr(R, 'var', initial=R.inv(R.sub(x[j].data[0],x[k].data[0])))
                for j,k in ((0,1),(0,2),(1,2))}
    def inverse_difference(j,k):
        return inverses[j,k] if j<k else -inverses[k,j]
    q = []
    for j in range(3):
        m,n = [k for k in range(3) if k!=j]
        c = inverse_difference(j,m)*inverse_difference(j,n)
        if direction == 1:
            c = c*x[m]*x[n]
        if direction == 2:
            c = -c*(x[m]+x[n])
        q.append(c)
    dx = [y[j]*q[j] for j in range(3)]
    dy = [const(R,R.scalar(7,2))*x[j]**6*q[j] for j in range(3)]
    dinverses = {jk:-v*v*(dx[jk[0]]-dx[jk[1]]) for jk,v in inverses.items()}
    W13 = x[0]*x[1]*x[2]*const(R,R.scalar(1,4))
    W23 = -(x[0]*x[1]+x[0]*x[2]+x[1]*x[2])*const(R,R.scalar(1,4))
    for n in range(order):
        new = [a.coeff(n) for a in dx+dy] + [a.coeff(n) for a in dinverses.values()]
        for a,v in zip(x+y+list(inverses.values()),new):
            a.data.append(v)
    return R,x,y,W13,W23


R,x1,y1,W13,_ = selected_flow(1,11)
c13 = R.neg(W13.coeff(10))
assert c13 == R.scalar(4)
R,x3,y3,_,W23 = selected_flow(3,11)
c32 = R.neg(W23.coeff(10))
assert c32 == R.scalar(-1)
R,x2,y2,_,_ = selected_flow(2,11)
assert all(R.add(y2[j].coeff(11),y1[j].coeff(1)) == R.zero for j in range(3))
assert all(x2[j].coeff(11) == R.zero for j in range(3))
assert R.mul(y1[0].coeff(1),R.inv(y1[0].coeff(1))) == R.one

# The module's arithmetic operations support any positive modulus; its
# original inverse routine is replaced only for this composite-modulus run.
recurrence.Cyc = CycWithCompositeModulus
bottlenecks = []
for i,q in ((1,11),(2,121),(3,11)):
    R,h,S = recurrence.jets(i,2*q,121)
    assert all(int(v)%11 == 0 for v in h[2*q])
    quotient = tuple((int(v)//11)%11 for v in h[2*q])
    assert sp.degree(sp.gcd(sum(v*z**j for j,v in enumerate(quotient)),phi,modulus=11)) == 0
    bottlenecks.append({
        'direction':i,'q':q,'log_derivative_order':2*q,
        'log_derivative_mod121':h[2*q],
        'log_derivative_divided_by11_mod11':quotient,
        'valuation_at_both_primes_above11':1,
        'q_plus_one_log_derivative_mod121':h[q+1],
    })
exceptional=[]
for p,i,q,value in ((3,1,27,2),(5,2,125,1)):
    R,h,S = recurrence.jets(i,q+1,p)
    assert h[q+1] == R.scalar(value)
    exceptional.append({'prime':p,'direction':i,'q':q,
                        'q_plus_one_log_derivative_mod_p':h[q+1]})
recurrence.Cyc = OriginalCyc
mixed_12_0_2 = (4 * factorial(2)) % 11
mixed_100_0_10 = (pow(4,9,11) * factorial(10)) % 11
mixed_110_2_10 = (-2 * pow(4,10,11) * factorial(10)) % 11
assert (mixed_12_0_2,mixed_100_0_10,mixed_110_2_10) == (8,8,2)

result={
    'checked_utc':datetime.now(timezone.utc).isoformat(),
    'method':'Exact Hurwitz algebraic ODE K12.7 over cyclotomic residue rings; composite modulus inverses obtained over Q and checked multiplicatively.',
    'c13_mod11':c13,'c32_mod11':c32,
    'restricted_D2_power_scalar_mod11':10,
    'restricted_scalar_witness_D1_y1':y1[0].coeff(1),
    'restricted_scalar_witness_difference_D2_11_y1_plus_D1_y1':R.zero,
    'source_sigma_mixed_derivative_12_0_2_mod11':mixed_12_0_2,
    'source_sigma_mixed_derivative_100_0_10_mod11':mixed_100_0_10,
    'source_sigma_mixed_derivative_110_2_10_mod11':mixed_110_2_10,
    'bottleneck_next_divisibility_fails':bottlenecks,
    'q_equal_minus_one_exceptions_can_be_nonzero':exceptional,
    'scope':'Finite constants and exact counterchecks. Global formal identities and sigma unit families require the companion AM-K017 proof.',
    'recurrence_sha256':hashlib.sha256((BASE/'jacobian_theta_direction_jets.py').read_bytes()).hexdigest(),
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'status':'PASS',
}
(BASE/'jacobian_hessian_pcurvature_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
