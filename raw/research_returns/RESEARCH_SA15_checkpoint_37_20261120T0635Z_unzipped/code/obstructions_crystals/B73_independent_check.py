#!/usr/bin/env python3
"""Exact finite supplement for B73. No existence or universal-proof inference."""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import datetime
import hashlib
import json
import time


def roots(points):
    polygon = []
    for x, y in sorted(points):
        x, y = int(x), F(y)
        while len(polygon) > 1:
            x0, y0 = polygon[-2]
            x1, y1 = polygon[-1]
            if (y1-y0)*(x-x1) < (y-y1)*(x1-x0):
                break
            polygon.pop()
        polygon.append((x, y))
    answer = Counter()
    for (x0, y0), (x1, y1) in zip(polygon, polygon[1:]):
        v = (y0-y1)/(x1-x0)
        if v > 0:
            answer[v] += x1-x0
    return dict(answer)


def high_quotient(p, e, B):
    q = p*p
    a, s = e*(q-1), e*(p+1)
    alpha, beta = F(s-B), F(B, p)
    inverse = roots([(0, alpha), (1, a), (p, (p-1)*B), (q, 0)])
    quotient = Counter({p*beta: p-1})
    for value, multiplicity in inverse.items():
        assert value < alpha
        assert multiplicity*(p-1) % p == 0
        quotient[p*value] += multiplicity*(p-1)//p
    assert sum(quotient.values()) == q-1
    return dict(quotient)


def encoded(values):
    return [{"valuation":str(v), "multiplicity":m}
            for v,m in sorted(values.items(),reverse=True)]


def run():
    began = time.perf_counter()
    primes = [5, 7, 11, 13]
    counts = Counter()
    sectors = []
    samples = []
    extended = []
    for p in primes:
        q = p*p
        N = q-1
        permitted_t = [t for t in range(2, q+p+2) if t % p]
        assert permitted_t[-1] == q+p+1
        for t in permitted_t:
            e, s = t*(p-1), t*N
            a = e*N
            assert p < e < p**3 and e % p and s == e*(p+1)
            counts['exact_index_two_sectors'] += 1
            sectors.append({'p':p,'t':t,'e':e})
            pbranch_parameters = []
            qbranch_parameters = []

            # Every L-rational first-level candidate has p|D. Reconstruct
            # the actual first and high-target inverse Newton polygons.
            for D in range(p, p*e, p):
                alpha, beta = F(s-D), F(D,p)
                assert alpha > e > beta > 0 and D != e
                first = roots([(1,a),(p,(p-1)*D),(q,0)])
                assert first == {alpha:p-1,beta:q-p}
                inverse = roots([(0,alpha),(1,a),(p,(p-1)*D),(q,0)])
                counts['rational_first_level_polygons'] += 1
                if D < e:
                    C = s-p*D
                    assert C % p and C > D
                    assert inverse == {F(C,p):p,F(D,p):q-p}
                    assert F(C,p).denominator == p
                    assert alpha > F(C,p) > beta
                    assert p*alpha-C == a
                    pbranch_parameters.append(D)
                    counts['degree_p_high_inverse_branches'] += 1
                else:
                    A = s-D
                    assert A % p
                    assert inverse == {F(A,q):q}
                    assert F(A,q).denominator == q
                    assert q*A-A == N*A
                    assert A > e > e-1
                    qbranch_parameters.append(D)
                    counts['degree_q_high_inverse_branches'] += 1

                # Any possible low image in a degree-p point field has
                # normalized valuation D/q. Nonintegrality already excludes
                # it; otherwise the actual lower-bound gap is strictly positive.
                image_v = F(D,q)
                if image_v.denominator != 1:
                    counts['degree_p_low_image_denominator_exclusions'] += 1
                else:
                    gap = image_v+a-D
                    assert gap == N*(e-F(D,q)) > 0
                    assert D < p*e < q*e
                    counts['degree_p_low_image_break_exclusions'] += 1

                # In the degree-q branch, every low-image valuation is
                # less than e, whereas every high first valuation exceeds e.
                assert beta <= e-1
                assert (s-D)-beta > 0
                counts['degree_q_cross_valuation_exclusions'] += 1

            assert len(pbranch_parameters)+len(qbranch_parameters) == e-1
            assert pbranch_parameters and qbranch_parameters

            # Reconstruct both actual quotient root multisets, not just
            # the asserted parameter transformation.
            small_b = list(range(1,(e-1)//p+1))
            both_small_possible = []
            large_second_breaks = set()
            for b in small_b:
                B, D = p*b, q*b
                first_quotient = high_quotient(p,e,B)
                assert first_quotient == {F(s-D):p-1,F(D,p):q-p}
                assert s-D > B
                counts['marked_first_high_quotients'] += 1
                second_quotient = high_quotient(p,e,D)
                C = p*D if D < e else s-D
                assert second_quotient == {F(s-C):p-1,F(C,p):q-p}
                counts['actual_second_high_quotients'] += 1
                if D < e:
                    assert C % p == 0 and s-C > D
                    assert 1 <= b <= p-1
                    both_small_possible.append(b)
                    counts['second_intrinsic_stable_low_records'] += 1
                else:
                    assert D > e and C % p
                    r = p*s-(p+1)*C
                    assert r > 0 and r not in large_second_breaks
                    large_second_breaks.add(r)
                    counts['second_prime_wild_break_records'] += 1
                # Character of the first marked line remains explicit;
                # scalar cases are included and never removed.
                for c in range(B % (p+1),N,p+1):
                    h, low = (p*c-D)%N,(c+D)%N
                    assert h % (p+1) == 0 and low % (p+1) == 0
                    assert (low-h)%N == (p+1)*B%N
                    counts['marked_character_records'] += 1
                    if h == low:
                        assert b % (p-1) == 0
                        counts['scalar_marked_character_records'] += 1

            assert len({b % (p-1) for b in both_small_possible}) == len(both_small_possible)
            for b1 in both_small_possible:
                for b2 in both_small_possible:
                    if (b1-b2) % (p-1) == 0:
                        assert b1 == b2
                    counts['final_small_norm_pairs'] += 1
            # The mixed case is excluded geometrically by tame versus wild;
            # the finite arithmetic only checks which actual quotient branch
            # carries the intrinsic low line and which has a prime parameter.
            mixed_count = len(both_small_possible)*len(large_second_breaks)
            counts['mixed_tame_wild_second_quotient_pairs'] += mixed_count

            # Complete larger-side original common-high division cases.
            for B in range(p,p*e,p):
                assert B != e
                C = p*B if B < e else s-B
                assert (C % p == 0) == (B < e)
                counts['original_common_high_divisibility_branches'] += 1
            counts['full_monodromy_threshold_checks'] += 1

            if p == 5 and e in [48,52,56,64,96,104,124]:
                choices=[D for D in [p,q,(p-1)*q] if 0<D<e]
                for D in choices:
                    C=s-p*D
                    inv=roots([(0,s-D),(1,a),(p,(p-1)*D),(q,0)])
                    samples.append({
                        'p':p,'e':e,'D':D,
                        'inverse_roots':encoded(inv),
                        'high_root_valuation_L':str(F(C,p)),
                        'coordinate_valuation_E':C,
                        'actual_lower_break':a,
                        'forbidden_low_image_condition':'D_image >= q*e',
                        'allowed_parameter_condition':'D_image < p*e',
                        'q_times_e':q*e,'p_times_e':p*e})

        assert (q+p+1)*(p-1) == p**3-1
        next_e=(q+p+2)*(p-1)
        assert next_e == p**3+p-2 > p**3 and next_e % p
        counts['next_index_at_least_three_thresholds'] += 1

        # The high-line proposition has no upper ramification bound.
        # Check additional sectors beyond p^3 with representative parameters
        # on both sides of e, keeping this scope separate from the theorem.
        for t in [q+p+2,2*q+1,3*q+p+1]:
            if t % p == 0:
                continue
            e,s=t*(p-1),t*N
            a=e*N
            choices=sorted({p,p*((e-1)//p),p*(e//p+1),p*(e-1)})
            for D in choices:
                assert 0 < D < p*e and D % p == 0 and D != e
                A=s-D
                inverse=roots([(0,A),(1,a),(p,(p-1)*D),(q,0)])
                if D < e:
                    C=s-p*D
                    assert inverse == {F(C,p):p,F(D,p):q-p}
                    assert C % p and p*A-C == a
                else:
                    assert inverse == {F(A,q):q} and A % p
                assert A > e > F(D,p)
                counts['beyond_threshold_alignment_only_records'] += 1
                extended.append({'p':p,'e':e,'D':D,'inverse_roots':encoded(inverse)})

    result={
        'status':'PASS',
        'scope':'Finite exact Newton multiplicities, actual quotient root counts, denominator/ramification inequalities and complete stated finite parameter branches. No formal-group existence or universal theorem is inferred from these tests.',
        'primes':primes,'sectors':sectors,'counts':dict(sorted(counts.items())),
        'degree_p_branch_samples':samples,
        'beyond_threshold_alignment_only':extended,
        'elapsed_seconds':time.perf_counter()-began,
        'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    }
    Path(__file__).with_suffix('.output.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    return result


if __name__ == '__main__':
    run()
