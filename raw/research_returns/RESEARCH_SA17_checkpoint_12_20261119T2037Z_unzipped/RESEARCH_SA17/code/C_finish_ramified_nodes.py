"""Bounded exact certificate for C:ramified_exponent_two_node.

The symbolic assertions verify the displayed formulas over the generic
domain. Finite rings model Z_2[pi]/(pi^e-2,4), e=2,...,8. They check
the matrix and square-zero-evaluation identities, not the general DVR
normality theorem or the arbitrary-rank additivity of the Tate invariant.
"""
from pathlib import Path
import json
import time
import sympy as sp

started = time.perf_counter()
pi, u, x, eps = sp.symbols('pi u x eps')
h = 1 + 2/pi
a = 1 + pi
y = pi**2*u/x
T = sp.Matrix([[a,x],[-h*y/u,-a]])
P = sp.Matrix([[x,x],[1-a,-1-a]])
I = sp.eye(2)
T0 = sp.Matrix([[a,pi],[-h*pi,-a]])
U = sp.Matrix([[0,1],[h,0]])
wp = sp.Matrix([1,-1])
wm = sp.Matrix([1,-h])

def zero(M):
    assert all(sp.cancel(z) == 0 for z in M)

zero(T*T-I)
zero(T*P-P*sp.diag(1,-1))
assert sp.cancel(P.det()+2*x) == 0
zero(T0*T0-I)
zero(T0*U+U*T0)
zero(U*U-h*I)
zero(T0-I-pi*wm*sp.Matrix([[1,1]]))
zero(T0+I-pi*wp*sp.Matrix([[h,1]]))
zero(U*wp+wm)
zero(U*wm+h*wp)
target = sp.Matrix([[a,pi+eps],[-h*(pi*u-u*eps)/u,-a]])
zero(target-T0-eps*U)
assert sp.expand((pi+eps)*(pi*u-u*eps)-pi**2*u) == -u*eps**2
symbolic_checks = 12

finite_runs = []
for e in range(2,9):
    z = (0,)*e
    one = (1,)+(0,)*(e-1)
    pp = (0,1)+(0,)*(e-2)
    def add(b,c): return tuple((s+t)%4 for s,t in zip(b,c))
    def neg(b): return tuple((-s)%4 for s in b)
    def mul(b,c):
        d=[0]*(2*e-1)
        for i,s in enumerate(b):
            for j,t in enumerate(c): d[i+j] += s*t
        for j in range(2*e-2,e-1,-1): d[j-e] += 2*d[j]
        return tuple(d[i]%4 for i in range(e))
    def power(b,n):
        out=one
        for _ in range(n): out=mul(out,b)
        return out
    def inv(b):
        assert b[0]%2
        # b=1+v or -1+v; normalize the constant residue to 1.
        c=b[0]
        base=tuple((c*s)%4 for s in b)
        v=add(base,neg(one))
        out=z
        term=one
        for _ in range(2*e+1):
            out=add(out,term)
            term=mul(term,neg(v))
        out=tuple((c*s)%4 for s in out)
        assert mul(out,b)==one
        return out
    def qadd(b,c): return (add(b[0],c[0]),add(b[1],c[1]))
    def qneg(b): return (neg(b[0]),neg(b[1]))
    def qmul(b,c):
        return (mul(b[0],c[0]),add(mul(b[0],c[1]),mul(b[1],c[0])))
    def mm(B,C):
        return [[qadd(qmul(B[i][0],C[0][j]),qmul(B[i][1],C[1][j]))
                 for j in range(2)] for i in range(2)]
    qone=(one,z)
    qzero=(z,z)
    qI=[[qone,qzero],[qzero,qone]]
    hh=add(one,power(pp,e-1))
    aa=add(one,pp)
    units={one,neg(one)}
    units.update(add(one,power(pp,r)) for r in range(1,e))
    cases=0
    for uu in sorted(units):
        ui=inv(uu)
        xx=(pp,one)
        yy=(mul(pp,uu),neg(uu))
        assert qmul(xx,yy)==(mul(power(pp,2),uu),z)
        TT=[[(aa,z),xx],
            [qneg(qmul((mul(hh,ui),z),yy)),(neg(aa),z)]]
        assert mm(TT,TT)==qI
        expected=[[(aa,z),(pp,one)],
                  [(neg(mul(hh,pp)),hh),(neg(aa),z)]]
        assert TT==expected
        # The true DVR Tate calculations are proved by the symbolic
        # rank-one factorizations above; their scalar h has residue 1.
        assert hh[0]%2 == 1
        cases += 1
    finite_runs.append({'ramification_index':e,'unit_cases':cases})

out={
    'statement_id':'C:ramified_exponent_two_node',
    'symbolic_exact_identity_groups':symbolic_checks,
    'finite_models':'Z_2[pi]/(pi^e-2,4), e=2,...,8, followed by epsilon^2=0',
    'finite_runs':finite_runs,
    'finite_square_zero_specializations':sum(r['unit_cases'] for r in finite_runs),
    'result':'PASS',
    'scope':'Exact generic/specialized matrix identities and residue h=1. The full normality, formal convergence, Tate-cycle identifications and arbitrary-rank additivity are established in the written proof, not by this bounded computation.',
    'runtime_seconds':time.perf_counter()-started,
}
dest=Path(__file__).resolve().parents[1]/'logs/C_finish_ramified_nodes.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
