#!/usr/bin/env python3
"""Finite exact supplement for B71, including the scalar point-field case."""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import datetime,hashlib,json,time


def roots(points):
    h=[]
    for x,y in sorted(points):
        x,y=int(x),F(y)
        while len(h)>1:
            x0,y0=h[-2]
            x1,y1=h[-1]
            if (y1-y0)*(x-x1)<(y-y1)*(x1-x0):
                break
            h.pop()
        h.append((x,y))
    ans=Counter()
    for (x0,y0),(x1,y1) in zip(h,h[1:]):
        z=(y0-y1)/(x1-x0)
        if z>0:
            ans[z]+=x1-x0
    return dict(ans)


def orbit(p,c):
    N=p*p-1
    return tuple(sorted((c%N,p*c%N)))


def run():
    start=time.perf_counter()
    primes=[5,7,11,13,17,19]
    counts=Counter()
    sectors=[]
    scalar_samples=[]
    next_patterns=[]
    for p in primes:
        q=p*p
        N=q-1
        for t in range(2,2*p+2):
            if t%p==0:
                continue
            e=t*(p-1)
            s=e*(p+1)
            a=e*N
            assert e%p and e<=2*q-p-1<2*q<p**3
            assert e>p and s%N==0
            sectors.append({"p":p,"t":t,"e":e})
            counts["sectors"]+=1

            # The first-level exact break recovers every prime parameter.
            seen=set()
            for B in range(1,p*e):
                if B%p==0:
                    continue
                alpha=s-B
                r=p*alpha-B
                assert r==p*s-(p+1)*B and r>0
                assert r not in seen
                seen.add(r)
                counts["prime_parameter_first_level_breaks"]+=1

            # Actual small high quotient has a marked stable low line,
            # and its ratio can be scalar: both possibilities are retained.
            for B in range(1,e):
                D=p*B
                A=s-D
                assert A>B>0
                assert roots([(1,a),(p,(p-1)*D),(q,0)])=={F(A):p-1,F(B):q-p}
                for c in range(B%(p+1),N,p+1):
                    high=(p*c-D)%N
                    low=(c+D)%N
                    assert high%(p+1)==0 and low%(p+1)==0
                    assert (low-high)%N==((p+1)*B)%N
                    assert (high==low)==(B%(p-1)==0)
                    counts["marked_low_line_weights"]+=1
                counts["marked_quotient_newton_records"]+=1

            small=list(range(1,(e-1)//p+1))
            assert all(1<=b<=2*p-2 for b in small)
            for b1 in small:
                for b2 in small:
                    if b1>=b2:
                        continue
                    counts["small_unequal_pairs"]+=1
                    if q*b1>e:
                        D1=q*b1
                        D2=q*b2
                        A1=s-D1
                        A2=s-D2
                        C2=F(D2,p)
                        assert D1>e and D2>e
                        assert A1%p and A2%p
                        inv1=roots([(0,A1),(1,a),(p,(p-1)*D1),(q,0)])
                        inv2=roots([(0,C2),(1,a),(p,(p-1)*D2),(q,0)])
                        assert inv1=={F(A1,q):q}
                        assert inv2=={F(C2,q):q}
                        assert F(A1,q).denominator==q
                        exact_break=N*A1
                        assert q*A1==A1+exact_break
                        # The second model would require the reverse inequality.
                        assert q*C2<C2+exact_break
                        gap=A1-C2
                        assert gap==s-p*(p+1)*b2+q*(b2-b1)
                        assert gap>q*(b2-b1)>0
                        # When the high lines correspond, the actual p-level
                        # second quotient has unequal prime-parameter breaks.
                        r1=p*s-(p+1)*A1
                        r2=p*s-(p+1)*A2
                        assert r1==(p+1)*(D1-e)>0
                        assert r2==(p+1)*(D2-e)>0
                        assert r1!=r2
                        counts["separated_high_point_field_records"]+=1
                        if b1%(p-1)==0 and b2%(p-1)==0:
                            counts["scalar_quotient_point_field_records"]+=1
                            scalar_samples.append({
                              "p":p,"e":e,"b":[b1,b2],
                              "point_valuations_L":[str(F(A1,q)),str(F(C2,q))],
                              "point_valuations_E":[str(A1),str(C2)],
                              "actual_break":exact_break,
                              "second_displacement":str(q*C2),
                              "required_lower_bound":str(C2+exact_break)})
                    if (b2-b1)%(p-1)==0:
                        if b1>=2:
                            assert q*b1>=2*q>e
                            counts["nontrivial_common_norm_pairs_excluded"]+=1
                        else:
                            assert b1==1 and b2==p
                            for c1 in range(p%(p+1),N,p+1):
                                c2=(c1+p*(p-1))%N
                                assert c2==p*c1%N
                                assert orbit(p,c1)==orbit(p,c2)
                                counts["surviving_frobenius_orbit_pairs"]+=1

            # Large/mixed-side common-high parameters.
            for B in range(p,p*e,p):
                assert B!=e
                new=p*B if B<e else s-B
                assert (new%p==0)==(B<e)
                counts["divisible_high_quotient_branches"]+=1

            prime_b=[b for b in range(1,e) if b%p]
            div_b=list(range(p,e,p))
            for b in prime_b:
                alpha=s-p*b
                assert alpha>=e+p
                assert F(b,q).denominator==q
                for b2 in div_b:
                    lhs=q*(alpha-b2)
                    rhs=b-b2
                    assert lhs>p**3 and rhs<e<p**3
                    assert lhs>rhs
                    counts["tame_mixed_point_field_inequalities"]+=1
            for b1 in div_b:
                for b2 in div_b:
                    B1=p*b1
                    B2=p*b2
                    assert B1!=e and B2!=e
                    if B1>e or B2>e:
                        large=B1 if B1>e else B2
                        other=B2 if B1>e else B1
                        assert (s-large)%p and (other//p)%p==0
                        counts["tame_high_low_divisibility_exclusions"]+=1
                    else:
                        assert B1==B2==q
                        assert (2*q)%(p-1)==2
                        counts["tame_equal_q_exchanged_line_exclusions"]+=1
            counts["full_monodromy_lower_upper_thresholds"]+=1

        # First arithmetic pattern beyond the current theorem's endpoint.
        e=2*N
        b1,b2=1,2*p-1
        B1,B2=p*b1,p*b2
        c1=p
        c2=(p+2*p*(p-1))%N
        assert B1<e and B2<e and q*b1<e
        assert (c1-B1)%(p+1)==0 and (c2-B2)%(p+1)==0
        assert (c1-c2)%(p-1)==0
        assert (c1-B1-c2+B2)%N==0
        assert orbit(p,c1)!=orbit(p,c2)
        next_patterns.append({
            "p":p,"e":e,"b":[b1,b2],"c":[c1,c2],
            "special_orbits":[orbit(p,c1),orbit(p,c2)],
            "scope":"Unexcluded by the present stated theorem; not a construction or nonexistence conclusion."
        })
    result={
        "status":"PASS",
        "scope":"Finite exact Newton and point-field normalization/inequality supplement. Universal geometric, Galois and quotient statements are proved separately; no existence is inferred from numerical patterns.",
        "primes":primes,"sectors":sectors,
        "counts":dict(sorted(counts.items())),
        "scalar_samples":scalar_samples,
        "next_arithmetic_patterns":next_patterns,
        "elapsed_seconds":time.perf_counter()-start,
        "actual_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "program_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    Path(__file__).with_suffix(".output.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
    return result


if __name__=="__main__":
    run()
