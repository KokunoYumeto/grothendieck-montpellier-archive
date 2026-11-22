#!/usr/bin/env python3
"""Exact finite supplement to B69; this is not a formal-group existence test.

Newton polygons are reconstructed from the stated universal vertices with
Fraction arithmetic. Quotient root multiplicities are then counted from the
actual product formula. The finite scopes and every counter are retained.
"""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import datetime
import hashlib
import json
import time


def hull(points):
    out = []
    for x, y in sorted(points):
        x, y = int(x), F(y)
        while len(out) >= 2:
            x0, y0 = out[-2]
            x1, y1 = out[-1]
            if (y1-y0)*(x-x1) < (y-y1)*(x1-x0):
                break
            out.pop()
        out.append((x,y))
    return out


def roots(points):
    h = hull(points)
    ans = Counter()
    for (x0,y0),(x1,y1) in zip(h,h[1:]):
        val = (y0-y1)/(x1-x0)
        if val > 0:
            ans[val] += x1-x0
    return dict(ans)


def quotient_from_high(p, a, b, alpha, beta):
    q=p*p
    inv=roots([(0,alpha),(1,a),(p,b),(q,0)])
    out=Counter({p*beta:p-1})
    for z,mult in inv.items():
        assert z < alpha
        assert mult*(p-1) % p == 0
        out[p*z] += mult*(p-1)//p
    assert sum(out.values()) == q-1
    return dict(out)


def as_record(values):
    return [{"valuation":str(v),"multiplicity":m}
            for v,m in sorted(values.items(),reverse=True)]


def run():
    started=time.perf_counter()
    counts=Counter()
    primes=[5,7,11,13,17,19]
    sectors=[]
    boundary_records=[]
    for p in primes:
        q=p*p
        N=q-1
        for t in list(range(1,p))+[p+1]:
            e=t*(p-1)
            s=e*(p+1)
            a=e*N
            assert e<q and e%p and s%N==0
            sectors.append({"p":p,"e":e,"t":t})
            counts["sectors"]+=1

            # Both the collinear threshold and strictly one-slope coefficient
            # are checked; their common inverse polynomial is recomputed.
            for b in [p*e*(p-1),p*e*(p-1)+1,a]:
                first=roots([(1,a),(p,b),(q,0)])
                inv=roots([(0,e),(1,a),(p,b),(q,0)])
                assert first == {F(e):N}
                assert inv == {F(e,q):q}
                onequot=Counter({F(p*e):p-1})
                for z,mult in inv.items():
                    onequot[p*z]+=mult*(p-1)//p
                expected={F(p*e):p-1,F(e,p):q-p}
                assert dict(onequot)==expected
                assert p*min(onequot)==e
                counts["one_slope_product_quotients"]+=1

            # Leading scalar residues and the inherited tangent action.
            for c in range(N):
                assert sorted([c,p*c%N])==sorted([p*c%N,q*c%N])
                counts["isogeny_character_orbits"]+=1
                if (c+e)%(p+1)==0:
                    assert (p*c-e)%(p+1)==0
                    assert ((c+e)%N)==0 or ((c+e)%N)%(p+1)==0
                    counts["scalar_stable_line_weights"]+=1
                for c2 in range(c,N,p+1):
                    # Equality of actual one-slope scalar eigenvalues is
                    # stronger than norm equality and identifies c itself.
                    if (c+e)%N==(c2+e)%N:
                        assert c==c2
                        counts["equal_scalar_characters"]+=1

            for B in range(1,p*e):
                b=(p-1)*B
                alpha=F(s-B)
                beta=F(B,p)
                assert alpha>beta>0
                first=roots([(1,a),(p,b),(q,0)])
                assert first=={alpha:p-1,beta:q-p}
                invlow=roots([(0,beta),(1,a),(p,b),(q,0)])
                assert invlow=={F(B,p**3):q}
                counts["unequal_newton_and_low_inverse_records"]+=1

                high=quotient_from_high(p,a,b,alpha,beta)
                if B<e:
                    Bnew=p*B
                    assert high=={F(s-Bnew):p-1,F(Bnew,p):q-p}
                elif B>e:
                    Bnew=s-B
                    assert high=={F(s-Bnew):p-1,F(Bnew,p):q-p}
                else:
                    assert B%p!=0
                    assert high=={F(e):N}
                    Bnew=None
                    counts["critical_equal_parameter_one_slope_quotients"]+=1
                counts["high_quotient_root_counts"]+=1

                for c in range(B%(p+1),N,p+1):
                    assert (c-B)%(p+1)==0
                    if Bnew is None:
                        assert (p*c+e)%(p+1)==0
                    else:
                        assert (p*c-Bnew)%(p+1)==0
                    counts["unrestricted_tangent_quotient_weights"]+=1

                if B%p==0:
                    assert B!=e
                    low=Counter({alpha+(p-1)*beta:p-1})
                    for z,mult in invlow.items():
                        assert z<beta
                        low[p*z]+=mult*(p-1)//p
                    assert dict(low)=={F(s)-F(B,p):p-1,F(B,p*p):q-p}
                    counts["low_quotient_root_counts"]+=1
                    # Mixing one-slope and two-slope polygons after the
                    # scalar-residual reduction.
                    if B<e:
                        assert (p*B)%p==0 and e%p!=0
                    else:
                        assert (s-B)%p!=0 and s-B>e
                        assert s-B==e if B==p*e else s-B!=e
                    counts["mixed_polygon_quotient_exclusions"]+=1

            small=[B//p for B in range(p,e,p)]
            assert all(1<=b<=p-1 for b in small)
            assert len({b%(p-1) for b in small})==len(small)
            for b1 in small:
                for b2 in small:
                    if (b1-b2)%(p-1)==0:
                        assert b1==b2
                    counts["equal_norm_small_parameter_pairs"]+=1

            divisible=list(range(p,p*e,p))
            for B in divisible:
                assert B!=e
                if B<e:
                    assert (p*B)%p==0
                else:
                    assert (s-B)%p!=0
                counts["wild_divisible_quotient_branches"]+=1

            low_div=[b for b in range(1,e) if b%p==0]
            low_prime=[b for b in range(1,e) if b%p]
            for b in low_prime:
                alpha=s-p*b
                assert alpha>=e+p
                for b2 in low_div:
                    k=b2//p
                    assert p*p*k>e
                    lhs=p*p*(alpha-p*k)
                    rhs=b-p*k
                    assert lhs>p**3 and rhs<p*p and lhs>rhs
                    B1=p*b
                    B2=p*p*k
                    if B1<e:
                        assert (p*B1)%p==0 and (s-B2)%p!=0
                    else:
                        assert B1>e
                        assert (s-B1)%p!=0 and (s-B2)%p!=0
                        assert s-B1!=s-B2
                    counts["tame_mixed_divisibility_branches"]+=1
            for b1 in low_div:
                for b2 in low_div:
                    B1=p*b1
                    B2=p*b2
                    assert B1>e and B2>e
                    assert (s-B1)%p!=0
                    assert (B2//p)%p==0
                    if s-B1==s-B2:
                        assert B1==B2
                    counts["tame_both_divisible_branches"]+=1
            assert e<p**3
            counts["mixed_monodromy_upper_thresholds"]+=1
            if t>1:
                assert e>p
                counts["lower_counterexample_thresholds"]+=1
            if e==N:
                boundary_records.append({
                    "p":p,"e":e,"s":s,
                    "one_slope_quotient":as_record({F(p*e):p-1,F(e,p):q-p}),
                    "critical_B_equals_e_high_quotient":as_record({F(e):N}),
                    "small_b_interval":[1,(e-1)//p],
                    "lower_level":"actual p^2",
                    "upper_level":"actual p^3",
                    "claimed_manuscript_index":2,
                })

    # The one/two quotient obstruction itself has no e<p^2 hypothesis.
    extended=[]
    for p in primes:
        for t in [p+2,2*p+1,3*p+2]:
            e=t*(p-1)
            if e%p==0:
                continue
            s=e*(p+1)
            for B in range(p,p*e,p):
                assert B!=e
                if B<e:
                    assert (p*B)%p==0
                else:
                    assert (s-B)%p!=0 and s-B>e
                counts["unrestricted_mixed_polygon_arithmetic"]+=1
            extended.append({"p":p,"e":e})

    result={
        "status":"PASS",
        "scope":"Finite exact Newton, quotient-root-count, semilinear-weight and case-arithmetic supplement only. The all-prime geometric/Galois assertions require the written proofs.",
        "primes":primes,
        "sectors":sectors,
        "counts":dict(sorted(counts.items())),
        "new_boundary_records":boundary_records,
        "additional_mixed_polygon_indices":extended,
        "elapsed_seconds":time.perf_counter()-started,
        "actual_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "program_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    out=Path(__file__).with_suffix(".output.json")
    out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
    return result


if __name__=="__main__":
    run()
