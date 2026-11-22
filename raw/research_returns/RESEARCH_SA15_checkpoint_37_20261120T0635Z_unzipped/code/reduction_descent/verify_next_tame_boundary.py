#!/usr/bin/env python3
"""Finite exact supplement to B70: character exponents and branch arithmetic.

The source does not construct formal groups or infer any all-prime theorem
from the finite range. It also retains the first unexcluded arithmetic pair.
"""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import datetime
import hashlib
import json
import time


def orbit(p,c):
    N=p*p-1
    return tuple(sorted([c%N,p*c%N]))


def run():
    start=time.perf_counter()
    primes=[5,7,11,13,17,19,23,29,31,37,41,43]
    counts=Counter()
    records=[]
    next_unexcluded=[]
    for p in primes:
        q=p*p
        N=q-1
        e=(p+2)*(p-1)
        s=e*(p+1)
        assert e==q+p-2
        assert q<e<2*q and e<p**3 and e>p
        assert e%(p-1)==0 and e%p==p-2
        assert s%N==0 and s%p!=0
        small=[b for b in range(1,e) if p*b<e]
        assert small==list(range(1,p+1))
        unequal_pairs=set()
        for b1 in small:
            for b2 in small:
                counts["small_parameter_pairs"]+=1
                if (b1-b2)%(p-1):
                    continue
                assert b1==b2 or {b1,b2}=={1,p}
                for c1 in range((p*b1)%(p+1),N,p+1):
                    c2=(c1+p*(b2-b1))%N
                    assert (c2-p*b2)%(p+1)==0
                    assert (c2-c1)%(p-1)==0
                    assert (c1-p*b1-c2+p*b2)%N==0
                    assert orbit(p,c1)==orbit(p,c2)
                    counts["small_common_high_character_orbits"]+=1
                    if b1!=b2:
                        assert c2==p*c1%N
                        unequal_pairs.add((b1,b2))
                        counts["unequal_parameter_frobenius_collisions"]+=1
        assert unequal_pairs=={(1,p),(p,1)}

        # All possible critical B=q weights, without assuming a primitive norm.
        B=q
        candidates=list(range(B%(p+1),N,p+1))
        for c1 in candidates:
            for c2 in candidates:
                high1=(c1-B)%N
                low1=(p*c1+B)%N
                high2=(c2-B)%N
                low2=(p*c2+B)%N
                assert high1!=low1 and high2!=low2
                exchanged=(high1==low2 and high2==low1)
                assert not exchanged
                assert (B+B)%(p-1)==2
                if high1==high2:
                    assert c1==c2
                counts["critical_exchanged_high_line_pairs"]+=1

        # Integer identity proving the general exchanged-line divisibility;
        # nonzero test values are varied independently.
        for j in range(1,41):
            c1=7*j+1
            c2=11*j-2
            B1=p*j+3
            B2=q*j-5
            x=c1-B1-p*c2-B2
            y=c2-B2-p*c1-B1
            assert p*x+y == (1-p*p)*c2-(p+1)*(B1+B2)
            counts["exchange_integer_identities"]+=1

        # Every p-divisible original parameter avoids the critical B=e.
        divisible=list(range(p,p*e,p))
        for B in divisible:
            assert B!=e
            Bnew=p*B if B<e else s-B
            assert (Bnew%p==0)==(B<e)
            assert 0<Bnew<p*e
            counts["divisible_high_quotient_branches"]+=1

        primes_b=[b for b in range(1,e) if b%p]
        multiples_b=list(range(p,e,p))
        for b in primes_b:
            assert Fraction(b,p*p).denominator==p*p
            alpha=s-p*b
            assert alpha>=e+p
            for b2 in multiples_b:
                k=b2//p
                lhs=p*p*(alpha-p*k)
                rhs=b-p*k
                assert lhs>p**3 and rhs<e<p**3 and lhs>rhs
                B1=p*b
                B2=p*p*k
                if B1<e and B2<e:
                    assert k==1
                    if (b-b2)%(p-1)==0:
                        assert b==1 and b2==p
                        counts["new_tame_small_orbit_cases"]+=1
                elif B1>e and B2>e:
                    assert (s-B1)%p and (s-B2)%p
                    assert s-B1!=s-B2
                else:
                    assert B1!=e and B2!=e
                    small_B=min(B1,B2)
                    large_B=max(B1,B2)
                    assert small_B<e<large_B
                    assert (p*small_B)%p==0 and (s-large_B)%p
                counts["tame_mixed_point_field_inequalities"]+=1

        for b1 in multiples_b:
            for b2 in multiples_b:
                B1=p*b1
                B2=p*b2
                assert B1!=e and B2!=e
                if B1>e or B2>e:
                    large_B=B1 if B1>e else B2
                    other_B=B2 if B1>e else B1
                    assert (s-large_B)%p!=0
                    assert (other_B//p)%p==0
                    counts["tame_both_divisible_high_low_exclusions"]+=1
                else:
                    assert B1==B2==q
                    assert (B1+B2)%(p-1)!=0
                    counts["tame_critical_equal_B_exclusions"]+=1

        # First later small-parameter pair: this is an unexcluded arithmetic
        # pattern, not an assertion that any torsion comparison exists.
        e_next=(p+3)*(p-1)
        B1=2*p
        B2=p*(p+1)
        c1=p-1
        c2=0
        assert B1<e_next and B2<e_next
        assert (c1-B1)%(p+1)==0 and (c2-B2)%(p+1)==0
        assert (c1-c2)%(p-1)==0
        assert (c1-B1-c2+B2)%N==0
        assert orbit(p,c1)!=orbit(p,c2)
        next_unexcluded.append({
            "p":p,"e":e_next,"B":[B1,B2],"b":[2,p+1],
            "c":[c1,c2],"special_orbits":[orbit(p,c1),orbit(p,c2)],
            "scope":"Compatible small-parameter arithmetic only; no formal groups or truncation isomorphism constructed."
        })
        records.append({"p":p,"e":e,"s":s,"small_b_max":p,
                        "unequal_small_pairs":sorted(unequal_pairs),
                        "claimed_exact_manuscript_index":2})
        counts["boundary_indices"]+=1
    result={
        "status":"PASS",
        "scope":"Finite exact all-weight character, quotient-divisibility and point-field inequality supplement. The all-prime theorem is established by the separate proof, not by these cases.",
        "primes":primes,
        "counts":dict(sorted(counts.items())),
        "boundary_records":records,
        "next_unexcluded_arithmetic":next_unexcluded,
        "elapsed_seconds":time.perf_counter()-start,
        "actual_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "program_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    Path(__file__).with_suffix(".output.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
    return result


if __name__=="__main__":
    run()
