#!/usr/bin/env python3
"""Exact finite supplement for B91; no group realization is inferred."""
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path
from itertools import product
import hashlib
import json
import time


def newton_slopes(vertices):
    hull = []
    for point in sorted(vertices):
        while len(hull) >= 2:
            a, b = hull[-2:]
            if (b[1]-a[1])*(point[0]-b[0]) >= (point[1]-b[1])*(b[0]-a[0]):
                hull.pop()
            else:
                break
        hull.append(point)
    return [(b[0]-a[0], F(a[1]-b[1], b[0]-a[0])) for a,b in zip(hull,hull[1:])]


def add_dist(d, v, n):
    d[v] = d.get(v, 0) + n


def matmul(a, b, p):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) % p for i in range(2) for j in range(2))


def conj(g, h, gi, p):
    return matmul(matmul(g,h,p),gi,p)


def main():
    start = time.perf_counter()
    newton_count = 0
    newton_modes = {'below':0, 'equal':0, 'above':0}
    for p in (5,7,11,13,17,19,23,29,31):
        q=p*p; N=q-1; e=p*(p-1); s=(p+1)*e; a=e*N
        for B in range(1,p*e):
            alpha=s-B; beta=F(B,p)
            roots = newton_slopes([(0,alpha),(1,a),(p,(p-1)*B),(q,0)])
            # The old first-level points outside H give p-1 quotient points.
            distribution = {F(B):p-1}
            for count, value in roots:
                assert value < alpha
                # Every kernel point has valuation alpha, so the actual
                # degree-p Weierstrass product multiplies this value by p.
                multiplicity=F(count*(p-1),p)
                assert multiplicity.denominator == 1
                add_dist(distribution,p*value,int(multiplicity))
            assert sum(distribution.values()) == q-1
            if B < e:
                mode='below'; D=p*B
                expected={F(s-D):p-1,F(D,p):q-p}
            elif B > e:
                mode='above'; D=s-B
                expected={F(s-D):p-1,F(D,p):q-p}
            else:
                mode='equal'; expected={F(e):q-1}
            assert distribution == expected
            newton_count += 1
            newton_modes[mode] += 1

    strict_count=0
    strict_modes={'both_below':0,'crossing':0,'equal_boundary':0,'both_above':0}
    for p in (5,7,11,13):
        q=p*p; N=q-1; e=p*(p-1); s=(p+1)*e
        for B1 in range(1,p*e):
            if B1 % p == 0:
                continue
            for B2 in range(p,B1,p):
                assert p*(s-B2)-B2-(p*s-(p+1)*B1) == (p+1)*(B1-B2)
                if B1 < e:
                    strict_modes['both_below'] += 1
                    D1=p*B1; D2=p*B2
                    assert D1//p == B1 and D2//p == B2
                    assert (D1//p) % p != 0 and (D2//p) % p == 0
                    assert s-D1 > e and s-D2 > e
                elif B2 <= e:
                    strict_modes['equal_boundary' if B2 == e else 'crossing'] += 1
                    D1=s-B1
                    assert D1 % p != 0
                    assert F(D1,p).denominator == p
                    assert B2 <= e
                else:
                    strict_modes['both_above'] += 1
                    D1=s-B1; D2=s-B2
                    assert D1 % p != 0 and D2 % p == 0 and D1 < D2
                strict_count += 1

    # Enumerate actual tame eigenvalue equalities, keeping tangent exponents
    # rather than merely the final arithmetic restriction on b.
    def orbit(c): return tuple(sorted({c%24,5*c%24}))
    normalized=[]
    for b1 in range(1,20):
        for b2 in range(b1+1,20):
            for c1,c2 in product(range(1,24,4),repeat=2):
                h1=(c1-5*b1)%24; h2=(c2-5*b2)%24
                if h1%6 or h1!=h2 or orbit(c1)==orbit(c2):
                    continue
                assert b1%2 and b2%2 and (b1-b2)%4==0
                normalized.append((b1,b2,c1,c2,h1))
    assert normalized
    crossings=[]; both_large=[]
    for row in normalized:
        b1,b2,c1,c2,h=row
        assert not (5*b1<20 and 5*b2<20)
        if 5*b1 < 20:
            if (24-b2)%5:
                # B84 recovers this quotient pair; it cannot survive.
                continue
            crossings.append(row)
        else:
            both_large.append(row)
            assert not ((24-b1)%5==0 and (24-b2)%5==0)
    crossing_parameters=sorted({(5*r[0],5*r[1]) for r in crossings})
    assert crossing_parameters==[(5,45),(15,95)]
    for b1,b2,c1,c2,h in crossings:
        assert sorted([25*b1,5*(24-b2)])==[25,75]

    # Independently reconstruct the invariant linear-functional calculation
    # on sl2 and the span forced by the original unipotent conjugation.
    p=5
    e12=(0,1,0,0); e21=(0,0,1,0); diag=(1,0,0,4)
    identity=(1,0,0,1)
    unip=(1,1,0,1); unip_inv=(1,4,0,1)
    sl2=[(a,b,c,(-a)%p) for a,b,c in product(range(p),repeat=3)]
    def coords(a):
        assert (a[0]+a[3])%p==0
        return (a[1],a[2],a[0])
    functionals=0
    nonzero_intertwining_scalars=0
    for ratio in (2,3):
        tame=(ratio,0,0,1); tame_inv=(pow(ratio,-1,p),0,0,1)
        images=[e21,conj(unip,e21,unip_inv,p),conj(unip_inv,e21,unip,p)]
        span={tuple(sum(coef[j]*images[j][i] for j in range(3))%p for i in range(4)) for coef in product(range(p),repeat=3)}
        assert span==set(sl2)
        for scalar in range(1,p):
            assert scalar*ratio%p != scalar*pow(ratio,-1,p)%p
            nonzero_intertwining_scalars += 1
        survivors=[]
        for coefficients in product(range(p),repeat=3):
            def linear(a): return sum(x*y for x,y in zip(coefficients,coords(a)))%p
            invariant=all(linear(conj(tame,a,tame_inv,p))==linear(a) and linear(conj(unip,a,unip_inv,p))==linear(a) for a in (e12,e21,diag))
            if invariant:
                survivors.append(coefficients)
            functionals += 1
        assert survivors==[(0,0,0)]

    bound_rows=0
    for p in (5,7,11,13,17,19,23,29,31):
        N=p*p-1; e=p*(p-1); s=(p+1)*e
        for B in range(e+1,p*e):
            assert p*s-(p+1)*B < N*N
            bound_rows += 1
    shapes=[(r1,r2,1+r1+r2) for r1 in range(3,5) for r2 in range(r1,5) if (r1,r2)!=(3,3)]
    assert shapes==[(3,4,8),(4,4,9)]
    result={
        'status':'PASS',
        'actual_utc':datetime.now(timezone.utc).isoformat(),
        'runtime_seconds':time.perf_counter()-start,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'inverse_newton_quotient_rows':newton_count,
        'inverse_newton_modes':newton_modes,
        'strict_prime_divisible_rows':strict_count,
        'strict_case_counts':strict_modes,
        'normalized_distinct_character_rows':len(normalized),
        'surviving_crossing_rows':[list(r) for r in crossings],
        'crossing_parameters':crossing_parameters,
        'both_large_rows':[list(r) for r in both_large],
        'invariant_functionals_tested':functionals,
        'nonzero_intertwining_scalars_excluded':nonzero_intertwining_scalars,
        'cyclotomic_break_bound_rows':bound_rows,
        'remaining_large_shapes':shapes,
        'scope':'Exact finite checks of actual inverse-Newton quotient multiplicities, strict case arithmetic, normalized character equations and matrix conjugation. No realization or exclusion of the remaining shapes is inferred; the uniform proof is in B91.'
    }
    out=Path(__file__).with_suffix('.output.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
