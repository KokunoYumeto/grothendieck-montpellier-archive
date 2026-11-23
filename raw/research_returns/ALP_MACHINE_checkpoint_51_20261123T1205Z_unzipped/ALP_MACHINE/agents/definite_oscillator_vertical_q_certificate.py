"""Exact finite diagnostics for AM-DO-041; no global theta claim."""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from datetime import datetime, timezone
import json
import random

checks = {}

def kappa(n, q):
    z = F(1)
    for i in range(1, n + 1):
        z *= 1 - F(1, q**i)
    return z

def gaussian(n, r, q):
    z = F(1)
    for i in range(r):
        z *= F(q**(n-i)-1, q**(r-i)-1)
    assert z.denominator == 1
    return z.numerator

def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]

def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def inv(a):
    n = len(a)
    x = [[F(v) for v in a[i]] + eye(n)[i] for i in range(n)]
    for j in range(n):
        p = next(i for i in range(j, n) if x[i][j])
        x[j], x[p] = x[p], x[j]
        c = x[j][j]
        x[j] = [v/c for v in x[j]]
        for i in range(n):
            if i != j:
                c = x[i][j]
                x[i] = [v-c*w for v, w in zip(x[i], x[j])]
    return [row[n:] for row in x]

def det(a):
    n = len(a)
    x = [[F(v) for v in row] for row in a]
    d = F(1)
    for j in range(n):
        p = next((i for i in range(j, n) if x[i][j]), None)
        if p is None:
            return F(0)
        if p != j:
            x[j], x[p] = x[p], x[j]
            d = -d
        c = x[j][j]
        d *= c
        for i in range(j+1, n):
            t = x[i][j]/c
            for k in range(j+1, n):
                x[i][k] -= t*x[j][k]
    return d

def modf(x, q):
    x = F(x)
    assert x.denominator % q
    return x.numerator * pow(x.denominator, -1, q) % q

def integral(x, q):
    return F(x).denominator % q != 0

def raw_support(x, r, q):
    if not all(integral(v, q) for row in x for v in row):
        return False
    if any(modf(x[i][j], q) for i in range(r, len(x)) for j in range(r)):
        return False
    return modf(det([row[:r] for row in x[:r]]), q) != 0

def detmod(a, q):
    return modf(det(a), q)

def invmod(a, q):
    return [[modf(v, q) for v in row] for row in inv(a)]

def all_gl(n, q):
    out = []
    for entries in product(range(q), repeat=n*n):
        a = [list(entries[i*n:(i+1)*n]) for i in range(n)]
        if detmod(a, q):
            out.append(a)
    return out

# Gaussian indices and the precise Haar coefficient.
nchecks = 0
for q, r, t in product((2, 3, 5, 7), range(1, 6), range(1, 6)):
    b = r+t
    g = gaussian(b, r, q)
    assert F(q**(r*t))*kappa(b, q)/(kappa(r, q)*kappa(t, q)) == g
    assert F(1, q**(r*t))*kappa(r,q)*kappa(t,q)/kappa(b,q) == F(1,g)
    nchecks += 1
checks["exact_gaussian_haar_identities"] = nchecks

# Independent finite-ring determinant valuation distributions:
# coefficient of Z^j in kappa_t * product_i (1-Z*q^-i)^-1.
distribution_cases = []
for q, depth, t in ((2,3,2), (3,2,2), (2,5,1), (3,3,1)):
    modulus = q**depth
    count = [0]*(depth+1)
    for entries in product(range(modulus), repeat=t*t):
        if t == 1:
            d = entries[0]
        else:
            d = entries[0]*entries[3]-entries[1]*entries[2]
        j = 0
        while j < depth and d % (q**(j+1)) == 0:
            j += 1
        count[j] += 1
    coeff = [F(1)] + [F(0)]*(depth-1)
    for i in range(1,t+1):
        coeff = [sum(coeff[j-k]*F(1,q**(i*k)) for k in range(j+1))
                 for j in range(depth)]
    coeff = [kappa(t,q)*x for x in coeff]
    total = modulus**(t*t)
    for j in range(depth):
        assert F(count[j],total) == coeff[j]
    assert F(count[-1],total) == 1-sum(coeff)
    distribution_cases.append({"q":q,"depth":depth,"rank":t,
                               "matrices":total,"valuation_counts":count})
checks["determinant_recursion_finite_ring_cases"] = distribution_cases

# Rational Schur-complement identities, including nonunit S and failed
# reverse-support cases.  Determinants of U,g are units at q.
rng = random.Random(410041)
block_checks = 0
for q,r,t in product((3,5), (1,2), (1,2)):
    for trial in range(12):
        U = eye(r)
        g = eye(r)
        for i in range(r):
            for j in range(i+1,r):
                U[i][j] = F(rng.randrange(-3,4))
                g[i][j] = F(rng.randrange(-3,4))
        V = [[F(rng.randrange(-2,3)) for _ in range(t)] for _ in range(r)]
        C = [[F(rng.randrange(-2,3)) for _ in range(r)] for _ in range(t)]
        S = eye(t)
        for i in range(t):
            S[i][i] = F(q**((trial+i)%3))
        W = mm(mm(S,C),U)
        SCV = mm(mm(S,C),V)
        D = [[S[i][j]+q*SCV[i][j] for j in range(t)] for i in range(t)]
        h = [U[i]+V[i] for i in range(r)]
        h += [[q*v for v in W[i]]+D[i] for i in range(t)]
        Xg = g + [[F(0)]*r for _ in range(t)]
        Y = mm(inv(h),Xg)
        assert raw_support(h,r,q) and raw_support(Y,r,q)
        cg = mm(C,g)
        top0 = mm(inv(U),g)
        top1 = mm(mm(inv(U),V),cg)
        predicted = [[top0[i][j]+q*top1[i][j] for j in range(r)]
                     for i in range(r)] + [[-q*v for v in row] for row in cg]
        assert Y == predicted
        assert det(h) == det(U)*det(S)
        # A nonunit initial g cannot meet the simultaneous support.
        gbad = [row[:] for row in g]
        for i in range(r):
            gbad[i][0] *= q
        assert not raw_support(mm(inv(h),gbad+[[F(0)]*r for _ in range(t)]),r,q)
        # A nonintegral C forces failure even when the top block is integral.
        Cbad = [row[:] for row in C]
        Cbad[0][0] += F(1,q)
        Wbad = mm(mm(S,Cbad),U)
        sbcv = mm(mm(S,Cbad),V)
        Dbad = [[S[i][j]+q*sbcv[i][j] for j in range(t)] for i in range(t)]
        hbad = [U[i]+V[i] for i in range(r)]
        hbad += [[q*v for v in Wbad[i]]+Dbad[i] for i in range(t)]
        assert not raw_support(mm(inv(hbad),Xg),r,q)
        block_checks += 1
checks["exact_rational_block_support_checks"] = block_checks

# Tame determinant phase cancellation for every GL2(F3) pair.
gl2 = all_gl(2,3)
phase_count = 0
for U,g in product(gl2,repeat=2):
    du,dg = detmod(U,3),detmod(g,3)
    dui_g = du*dg % 3  # du^-1=du in F3^times
    chi = lambda x: 1 if x % 3 == 1 else -1
    assert chi(du)*chi(dui_g)*chi(dg) == 1
    phase_count += 1
checks["tame_character_pair_cancellations"] = phase_count

# Full finite compact nested section at r=t=1.  This is the exact
# unit-Schur-complement slice, with scalar 1/[GL2:P11].
compact_cases = []
for q in (2,3):
    g2 = all_gl(2,q)
    g3 = all_gl(3,q)
    chi = (lambda x: 1) if q == 2 else (lambda x: 1 if x % 3 == 1 else -1)
    weights = []
    for h in g2:
        hi = invmod(h,q)
        w = F(0)
        for g in range(1,q):
            y = [[hi[0][0]*g % q],[hi[1][0]*g % q]]
            if raw_support(y,1,q):
                w += chi(y[0][0])*chi(g)
        w /= q-1
        weights.append((h,w))
    support_count = 0
    for k in g3:
        ki = invmod(k,q)
        total = F(0)
        for h,w in weights:
            if not w:
                continue
            # First column of k^-1 X_b h.
            c = [(ki[i][0]*h[0][0]+ki[i][1]*h[1][0])%q for i in range(3)]
            if c[0] and c[1] == 0 and c[2] == 0:
                total += w*chi(c[0])
        total *= F(chi(detmod(k,q)),len(g2))
        is_par = k[0][0] != 0 and k[1][0] == 0 and k[2][0] == 0
        if is_par:
            lower_det = (k[1][1]*k[2][2]-k[1][2]*k[2][1])%q
            expected = F(chi(lower_det),gaussian(2,1,q))
            support_count += 1
        else:
            expected = F(0)
        assert total == expected
    assert F(len(g3),support_count) == gaussian(3,1,q)
    compact_cases.append({"q":q,"all_target_matrices":len(g3),
                          "support_matrices":support_count,
                          "scalar_unit_slice":str(F(1,gaussian(2,1,q)))})
checks["nested_compact_section_exhaustive"] = compact_cases

# Count the two unchanged raw Schwartz supports.
raw_counts = []
for q,r,t in ((3,1,1),(2,2,1)):
    b,N = r+t,r+2*t
    for rows,cols in ((b,r),(N,b)):
        count=0
        for entries in product(range(q),repeat=rows*cols):
            x=[list(entries[i*cols:(i+1)*cols]) for i in range(rows)]
            if raw_support(x,r,q):
                count += 1
        norm = F(count,q**(rows*cols))
        assert norm == kappa(r,q)*F(1,q**((rows-r)*r))
        raw_counts.append({"q":q,"rows":rows,"columns":cols,"count":count,
                           "norm_squared":str(norm)})
checks["raw_support_norm_counts"] = raw_counts

actual=[]
for name,a,d in (("J14",42,1760),("J56",168,1634)):
    r,t=a+1,d-1
    b,N=r+t,r+2*t
    z=F(t+1,2)
    margin=z-F(r-1,2)
    assert b==1802 and margin>0
    assert margin == (859 if name=="J14" else 733)
    actual.append({"host":name,"a":a,"r":r,"t":t,"b":b,"N":N,
                   "z_star":str(z),"holomorphy_margin":str(margin),
                   "rt":r*t})
checks["actual_rank_arithmetic"] = actual

out={"status":"PASS","finding":"AM-DO-041",
     "checked_at_utc":datetime.now(timezone.utc).isoformat(),
     "scope":"Exact finite/block/measure diagnostics; no global theta or terminal-value claim.",
     "checks":checks}
path=Path(__file__).with_suffix(".json")
path.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
