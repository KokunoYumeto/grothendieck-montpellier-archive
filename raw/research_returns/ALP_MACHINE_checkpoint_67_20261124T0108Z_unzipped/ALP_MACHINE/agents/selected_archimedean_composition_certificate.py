"""Exact normalization diagnostics for ALP-LIFT-25.

The compact examples test Schur averaging on actual irreducible finite
unitary representations.  They do not prove the compact Howe theorem.
"""
from fractions import Fraction as F
from itertools import permutations, product
from math import factorial
from pathlib import Path
import json


def mm(A, B):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*B)]
            for row in A]


def mv(A, v):
    return [sum(x*y for x, y in zip(row, v)) for row in A]


def standard(p):
    """Permutation action on the basis e_i-e_last."""
    n = len(p)
    return [[int(p[j] == i)-int(p[n-1] == i)
             for j in range(n-1)] for i in range(n-1)]


def compact_checks():
    checks = 0
    norms = []
    for n in (3, 4):
        d = n-1
        mats = []
        for p in permutations(range(n)):
            ip = [0]*n
            for i, j in enumerate(p):
                ip[j] = i
            R = standard(p)
            Rd = [list(x) for x in zip(*standard(ip))]
            mats.append((R, Rd))
        vecs = list(product((-1, 0, 1), repeat=d))
        for ell, w in product(vecs, repeat=2):
            out = [[0]*d for _ in range(d)]
            for R, Rd in mats:
                le, rw = mv(Rd, ell), mv(R, w)
                for i in range(d):
                    for j in range(d):
                        out[i][j] += le[i]*rw[j]
            tr = sum(x*y for x, y in zip(ell, w))
            expected = [[F(tr, d) if i == j else F(0)
                         for j in range(d)] for i in range(d)]
            assert [[F(x, len(mats)) for x in row] for row in out] == expected
            checks += 1
        # This nonorthonormal model has Gram I+J and inverse I-J/n.
        G = [[1+int(i == j) for j in range(d)] for i in range(d)]
        Gi = [[F(int(i == j))-F(1, n) for j in range(d)] for i in range(d)]
        assert mm(G, Gi) == [[int(i == j) for j in range(d)] for i in range(d)]
        omega_norm2 = sum(Gi[i][j]*G[i][j] for i in range(d) for j in range(d))
        assert omega_norm2 == d
        # Unit-normalized h yields squared averaged norm exactly 1/d.
        h = [1]+[0]*(d-1)
        ell = mv(G, h)
        trace = sum(x*y for x, y in zip(ell, h))
        assert trace == 2
        projected_norm2 = F(trace*trace, d*d)*omega_norm2
        assert projected_norm2/F(trace*trace) == F(1, d)
        norms.append({"dimension":d, "diagonal_norm_squared":d,
                      "unit_highest_projection_norm_squared":str(F(1, d))})
    return checks, norms


def mul(A, B):
    out = {}
    for ea, ca in A.items():
        for eb, cb in B.items():
            e = tuple(x+y for x, y in zip(ea, eb))
            out[e] = out.get(e, 0)+ca*cb
    return {e:c for e, c in out.items() if c}


def det_poly(n, r):
    out = {}
    for p in permutations(range(r)):
        e = [0]*(n*n)
        for i, j in enumerate(p):
            e[i*n+j] += 1
        inv = sum(p[i] > p[j] for i in range(r) for j in range(i+1, r))
        out[tuple(e)] = (-1)**inv
    return out


def power(P, m, n):
    out = {(0,)*(n*n):1}
    for _ in range(m):
        out = mul(out, P)
    return out


def highest(lam):
    n = len(lam)
    out = {(0,)*(n*n):1}
    for r in range(1, n+1):
        gap = lam[r-1]-(lam[r] if r < n else 0)
        if gap:
            out = mul(out, power(det_poly(n, r), gap, n))
    diagonal = tuple(lam[i] if i == j else 0 for i in range(n) for j in range(n))
    assert out[diagonal] == 1
    return out


def fischer(P):
    return sum(c*c*__import__('functools').reduce(
        lambda x, e:x*factorial(e), mon, 1) for mon, c in P.items())


def hook(lam):
    out = 1
    for i, row in enumerate(lam):
        for j in range(row):
            out *= row-j+sum(x > j for x in lam[i+1:])
    return out


def polynomial_checks():
    cases = [(1,1), (2,1), (3,1), (3,2), (2,1,1), (3,2,1),
             (3,3,2,2), (4,3,2,2)]
    counts = []
    for lam in cases:
        P = highest(lam)
        assert fischer(P) == hook(lam)
        counts.append({"partition":lam,"monomials":len(P),"fischer_norm_squared":hook(lam)})
    for eta, q in [((1,1,0,0),2), ((2,1,0,0),2), ((2,1,0),1)]:
        nu = tuple(x+q for x in eta)
        n = len(eta)
        actual = mul(highest(eta), power(det_poly(n,n),q,n))
        assert actual == highest(nu)
        ratio = 1
        for i, x in enumerate(eta):
            for k in range(1,q+1):
                ratio *= x+n-i-1+k
        assert F(fischer(actual),fischer(highest(eta))) == ratio
    return counts


def vp(n, p=11):
    assert n > 0
    z = 0
    while n%p == 0:
        n//=p
        z+=1
    return z


def vfac(n, p=11):
    z = 0
    while n:
        n//=p
        z+=n
    return z


def hookvp(lam):
    n = len(lam)
    return sum(vfac(x+n-i-1) for i,x in enumerate(lam))-sum(
        vp(lam[i]-lam[j]+j-i) for i in range(n) for j in range(i+1,n))


def dimvp(lam):
    return sum(vp(lam[i]-lam[j]+j-i)-vp(j-i)
               for i in range(len(lam)) for j in range(i+1,len(lam)))


def actual_weight_checks():
    out=[]
    for a,d,C,f in [(42,1760,45156049293,42),(168,1634,40530339687,168)]:
        b=a+d
        nu0=[(2*(a-i)+1)*C+i-(a+b-2)//2 for i in range(a)]
        eta0=[x-nu0[-1] for x in nu0]
        assert eta0 == [(a-1-i)*(2*C-1) for i in range(a)]
        eta1=nu0+[0]*d
        delta=4*C-d
        nu1=[x+delta for x in eta1]
        dim0=a*(a-1)//2*vp(2*C)
        dim1=dim0+sum(vfac(nu0[i]+b-i-1)-vfac(nu0[i]+a-i-1)
                     +vfac(a-i-1)-vfac(b-i-1) for i in range(a))
        assert dimvp(eta0)==dim0
        assert dimvp(eta1)==dim1
        h0=hookvp(nu0)
        h1=h0+sum(vfac(x+delta+b-i-1)-vfac(x+b-i-1)
                  for i,x in enumerate(eta1))
        assert hookvp(eta1)==h0
        assert hookvp(nu1)==h1
        expected=(0,43,8344837905338,40893317909328) if a==42 else (
            0,86,115754650130062,144968918676189)
        assert (dim0,dim1,h0,h1)==expected
        out.append({"a":a,"d":d,"f":f,"nu0_last":nu0[-1],"delta":delta,
                    "v11_dim0_one_place":dim0,"v11_dim1_one_place":dim1,
                    "v11_literal_two_haar_denominators":f*(dim0+dim1),
                    "v11_hook0_one_place":h0,"v11_hook1_one_place":h1,
                    "v11_hook_product_all_places":f*(h0+h1)})
    return out


def main():
    checks,norms=compact_checks()
    out={"finding":"ALP-LIFT-25","status":"PASS",
         "scope":"Exact finite compact Haar projections, Fischer/hook and actual rank valuations; not a proof of global theta nonvanishing.",
         "compact_projection_checks":checks,"compact_norms":norms,
         "highest_polynomials":polynomial_checks(),
         "actual_weights":actual_weight_checks()}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
