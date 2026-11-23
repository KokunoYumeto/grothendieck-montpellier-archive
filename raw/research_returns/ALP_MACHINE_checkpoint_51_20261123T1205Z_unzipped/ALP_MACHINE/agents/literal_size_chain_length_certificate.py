#!/usr/bin/env python3
"""ALP-LIFT-54: exact necessary size/length diagnostics; no Lean build."""
from __future__ import annotations
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

HERE = Path(__file__).resolve().parent
BASE = HERE.parent / 'research/alpoge_source'
checks = Counter()


def ck(condition, label):
    if not condition:
        raise AssertionError(label)
    checks[label] += 1


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def log_interval(a, terms):
    """Positive atanh series and an exact geometric upper bound for its tail."""
    z = F(a - 1, a + 1)
    ck(0 < z < 1, 'atanh_argument')
    lo = 2 * sum((z ** (2*j+1) / (2*j+1) for j in range(terms)), F(0))
    tail = 2 * z ** (2*terms+1) / ((2*terms+1) * (1-z*z))
    ck(tail > 0, 'positive_tail')
    return lo, lo + tail


def ceil_fraction(x):
    return (x.numerator + x.denominator - 1) // x.denominator


def main():
    intervals = {p: log_interval(p, n) for p, n in [(2,64),(3,64),(5,96),(7,128)]}
    l2,u2 = intervals[2]
    l3,u3 = intervals[3]
    l5,u5 = intervals[5]
    l7,u7 = intervals[7]
    ck(F(69,100) < l2 < u2 < F(7,10), 'coarse_log_two')

    # Natural division/subtraction is exact after the source parity and m>=2.
    for m in range(2, 514, 2):
        ck(F(m//2-1) == F(m,2)-1, 'natural_rS_to_real_identity')
    small = []
    for m in range(2,22,2):
        fac = m
        lo = hi = F(0)
        for p,(lp,up) in intervals.items():
            while fac % p == 0:
                lo += lp
                hi += up
                fac //= p
        ck(fac == 1, 'small_m_factorization')
        rs = m//2-1
        if m < 20:
            ck(lo*lo > rs, 'even_m_below_twenty_excluded')
        else:
            ck(hi*hi < rs, 'twenty_passes_single_log_clause')
        small.append({'m':m,'rS':rs,'excluded_by_log_clause':m<20})

    bounds = [
        ('f42', l2+l3+l7, u2+u3+u7, 13, 14, 30),
        ('f168', 3*l2+l3+l7, 3*u2+u3+u7, 26, 27, 56),
        ('R023_minimum_f', 283*l2+l3+l7, 283*u2+u3+u7,
         39682,39683,79368),
    ]
    rows=[]
    for name,lo,hi,q0,q1,mmin in bounds:
        ck(F(q0) < lo*lo <= hi*hi < F(q1), 'certified_log_square_interval')
        ck(ceil_fraction(lo*lo) == q1 == ceil_fraction(hi*hi), 'exact_ceiling')
        ck(mmin == 2+2*q1 and mmin % 2 == 0, 'even_length_floor')
        ck(F(mmin-2,2)-1 < lo*lo, 'previous_even_length_fails')
        ck(hi*hi <= F(mmin,2)-1, 'length_floor_passes_single_clause')
        rows.append({'case':name,'log_square_interval':[q0,q1],
                     'necessary_even_m':mmin,
                     'certified_log_interval_millionths':[
                         lo.numerator*10**6//lo.denominator,
                         ceil_fraction(hi*10**6)]})

    ck(2**281 < 21**64 < 2**282, 'carried_R023_integer_bracket')
    ck(42*2**282 == 2**283*3*7, 'repaired_f_factorization')

    # Exact simplification of the literal SizeM lower bound.
    ck(F(1,100)+F(1,16) == F(29,400), 'SizeM_exponent_simplification')
    ck(F(1,2)-F(29,400*52) == F(10371,20800), 'uniform_growth_exponent')
    ck(F(9,2)+F(1001,5200) < 5, 'SizeK_upper_exponent_below_five')
    ck(F(1,100)+2 == F(201,100), 'first_SizeKRel_extra_exponent')
    for f,m,xb,klower in [(42,30,5,1020600000),(168,56,10,92522938368)]:
        ck(F(f,2) < xb**2, 'fixed_degree_x_upper')
        ck(m**5*f == klower, 'fixed_degree_k_lower_exact')
        ck(xb**5 < klower, 'fixed_degree_any_scale_contradiction')
        ck(f**3 < 32*m**10, 'general_necessary_size_inequality_fails')
    ck(F(52,2)-F(29,400) == F(10371,400), 'o_tie_length_exponent')
    ck(100*F(10371,400) == F(10371,4), 'odd_divisor_length_exponent')
    repair_lo=F(10371,4)*(l3+l7)/u2
    repair_hi=F(10371,4)*(u3+u7)/l2
    ck(F(11388) < repair_lo < repair_hi < F(11389), 'full_repair_length_bits')

    # The unchanged R022/L343 scale; all comparisons use rational intervals.
    lxlo=960*l2-343
    lxhi=960*u2-343
    ll_lo=3*l7
    ll_hi=3*u7
    ck(0 < lxlo <= lxhi, 'actual_x_exceeds_one')
    ck(ll_hi/lxlo < F(1,52), 'actual_epsilon_window')
    scales=[]
    for name,p,q,lower in [
        ('m',F(1,2),-F(29,400),231),
        ('n',F(2),F(799,100),997),
        ('k',F(9,2),F(999,100),2177),
    ]:
        lo=p*lxlo+q*(ll_lo if q>=0 else ll_hi)
        hi=p*lxhi+q*(ll_hi if q>=0 else ll_lo)
        blo,bhi=lo/u2,hi/l2
        ck(F(lower) < blo < bhi < F(lower+1), 'fixed_scale_log2_interval')
        scales.append({'parameter':name,'lower_bound_log2_interval':[lower,lower+1]})
    ck(2*(2**997)==2**998, 'fixed_scale_f_bound')
    for f in [42,168]:
        ck(f < 2**231 < 2**998, 'fixed_fields_fail_full_size_bounds')

    # Other literal pointwise clauses: exact scope is retained in the report.
    for k in range(6,130,2):
        ck(2**(k-2) == 2*2**(k-3), 'full_binary_code_twice_SizeWords_cap')
    for g in [4615409,5276377,22285932761,64072175441]:
        ck(g < 2**36 < 2**2744, 'fixed_G_primes_fail_SizeG')

    paths=[
        'Formalism/SharpRestriction/ElevenLe.lean',
        'Formalism/SharpRestriction/ParConsts.lean',
        'Formalism/SharpRestriction/FamCore.lean',
        'Formalism/LocalRingCardinality/Params.lean',
        'Formalism/LocalRingCardinality/DataParams₂.lean',
    ]
    sources={p:(BASE/p).read_text() for p in paths}
    needles={
        paths[0]:[
            'Real.log D.R.f ≤ Real.sqrt D.R.rS',
            'SizeN L ∧ SizeM L ∧ SizeK L ∧ SizeKRel L',
            'L.sc.x ^ (-szTh L) * Real.sqrt (L.sc.x * L.sc.delta1) ≤ (D.R.m : ℝ)',
            '2 + 8 * L.sc.eps - szTh L',
            '9 / 2 + 10 * L.sc.eps - szTh L',
            '@Fintype.card D.what₂.Word D.wordFin ≤ 2 ^ (D.R.k - 3)',
            '((D.R.k : ℝ) * L.sc.b) ^ 8 ≤ (D.host.g i : ℝ)',
        ],
        paths[1]:[
            'structure FamP (eps : ℝ) extends FamCore eps where',
            'sizes : ∀ x, x1 < x → ∀ i : Ix x, SizesAt (L x i)',
        ],
        paths[2]:[
            'Win_unb : ∀ y : ℝ, ∃ x ∈ Win, y ≤ x',
            'Ix_win : ∀ x ∈ Win, Nonempty (Ix x)',
            'L_x : ∀ x i, x1 < x → (L x i).sc.x = x',
            'L_eps : ∀ x i, (L x i).sc.eps = eps',
        ],
        paths[3]:[
            'm_even : Even m','two_le_m : 2 ≤ m','m_le_f : m ≤ 2 * ord',
            'def f : ℕ := 2 * R.n','def rS : ℕ := R.m / 2 - 1',
        ],
        paths[4]:[
            'eps_lt : eps < 1 / 52','def L : ℝ := s.x ^ s.eps',
            'def delta1 : ℝ := s.x ^ (-(s.eps / 8))',
            'o_tie : (D.R.o : ℝ) ≤ sc.x ^ (sc.eps / 100)',
        ],
    }
    for p,ns in needles.items():
        for needle in ns:
            ck(needle in sources[p], 'literal_source_fingerprint')
    data={
        'finding':'ALP-LIFT-54','status':'PASS',
        'time_utc':datetime.now(timezone.utc).isoformat(),
        'assertions':sum(checks.values()),'checks':dict(checks),
        'pointwise_length_floors':rows,'small_even_lengths':small,
        'fixed_scale_bounds':scales,
        'retained_host_full_SizeM_log2_lower_interval':[11388,11389],
        'source_sha256':{p:sha(BASE/p) for p in paths},
        'script_sha256':sha(Path(__file__)),
        'scope':'Exact necessary numerical clauses and source fingerprints. No Host, family, theta lift, image, period, DP44 sign, or Lean build.'
    }
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,default=HERE/'literal_size_chain_length_certificate.json')
    out=ap.parse_args().output
    out.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'status':'PASS','assertions':data['assertions'],
                      'output':str(out),'time_utc':data['time_utc']}))


if __name__=='__main__':
    main()
