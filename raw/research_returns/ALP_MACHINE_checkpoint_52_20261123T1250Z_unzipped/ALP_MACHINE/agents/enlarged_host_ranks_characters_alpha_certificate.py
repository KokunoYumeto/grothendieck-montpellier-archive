"""AM-K031: exact finite arithmetic, not a Hecke/analytic/Lean verification."""
from datetime import datetime, timezone
from fractions import Fraction
from math import gcd, isqrt, lcm, prod
from pathlib import Path
import hashlib
import json


def prime_trial(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


def prime_factors(n):
    result = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            result[d] = result.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def parameter_check(k=42, f=42, m=2, t=1759):
    order = f // 2
    r = k + m - 1
    d = t + 1
    S = r + m * t
    C = S ** 3 + k + t + 11
    ranks = [k % 2 == 0, m % 2 == 0, t % 2 == 1, 2 <= m,
             m + 3 <= k, r + 5 <= t, 3 * m < t,
             m <= 2 * order <= k, m * m <= k + m * d]
    assert all(ranks) and r + t >= 1801
    u = [Fraction((2 * (k - i) + 1) * C) + Fraction(1, 2)
         for i in range(k)]
    v = [2 * (k - i) * C for i in range(k - 1)]
    b = [(4 * j - 2) * C for j in range(m)]
    e = [4 * j * C for j in range(m)]
    eta = Fraction(-1, 2)
    H = Fraction(t + 3, 2)
    assert all(u[i + 1] < v[i] < u[i] for i in range(k - 1))
    assert u[-1] > -b[0]
    assert all(e[j] - b[j] >= H for j in range(m))
    assert all(b[j + 1] - e[j] >= H for j in range(m - 1))
    assert all(x.denominator == 2 for x in u)
    assert all((f * ej) % 2 == 0 for ej in e)
    centred = []
    for j in range(m):
        distances = [abs(x + e[j]) for x in u]
        distances += [abs(x + e[j]) for x in v]
        distances += [abs(e[j] - x) for x in b]
        for jj in range(m):
            if jj != j:
                distances += [abs(-e[jj] + Fraction(t - 1, 2) - ell + e[j])
                              for ell in range(t)]
        assert min(distances) >= H
        centred.append({"j": j, "comparisons": len(distances),
                        "minimum": str(min(distances))})
    nc = []
    for j in range(m + 1):
        shift = eta if j % 2 else 0
        entries = [(Fraction(x) + shift, True) for x in v]
        # Source i-j is natural subtraction, not signed subtraction.
        entries += [(Fraction(-b[i]) + shift,
                     i <= j or max(i - j, 0) % 2 == 0) for i in range(m)]
        for i in range(min(j, m)):
            entries += [(Fraction(-e[i]) + Fraction(t - 1, 2) - ell + shift, True)
                        for ell in range(t)]
        positive = {x for x, sign in entries if sign}
        negative = {x for x, sign in entries if not sign}
        distances = [abs(x - y) for x in positive for y in negative]
        if distances:
            assert min(distances) > S ** 3
        nc.append({"j": j, "true_entries": len(positive),
                   "false_entries": len(negative), "unordered_cross_pairs": len(distances),
                   "minimum": str(min(distances)) if distances else None})
    # Source lamTrue_0 = u_i - (k-1)/2 + i; then DO25.5.
    w0 = [u[i] - Fraction(k - 1, 2) + i for i in range(k)]
    nu0 = [x + e[0] - Fraction(k + d, 2) for x in w0]
    assert all(x.denominator == 1 for x in nu0)
    nu0 = [int(x) for x in nu0]
    assert all(nu0[i] >= nu0[i + 1] for i in range(k - 1)) and min(nu0) > 0
    Delta = e[1] - e[0] - d
    w1 = [x - Fraction(d, 2) for x in w0] + [-e[0] + Fraction(k, 2)] * d
    nu1 = [x + e[1] - Fraction(k + 2 * d, 2) for x in w1]
    assert nu1 == [x + Delta for x in nu0] + [Delta] * d
    assert Delta > 0
    return dict(k=k, f=f, m=m, t=t, order=order, r=r, d=d,
                N=[k + j * d for j in range(m + 1)], nV=r+t,
                S=S, S_cubed=S**3, C=C, C_mod7=C%7,
                e=e, e_mod7=[x%7 for x in e], b=b,
                centred=centred, NCGaps=nc, nu0=nu0,
                nu0_min=min(nu0), Delta=Delta, G_lower_threshold=2*f*k)


def main():
    params = parameter_check()
    assert params['S_cubed'] == 45156047481
    assert params['C'] == 45156049293
    assert params['C_mod7'] == 5 and params['e_mod7'] == [0, 6]
    C = params['C']
    assert params['nu0'] == [(85 - 2*i)*C + i - 921 for i in range(42)]
    assert params['nu0_min'] == 3*C - 880
    primes = []
    modulus = 812
    for a, bb, q, generator in [(1, 812, 4615409, 3),
                                (813, 812, 5276377, 5)]:
        assert a*a + 7*bb*bb == q and prime_trial(q)
        assert (a-1) % modulus == 0 and bb % modulus == 0
        assert (q-1) % modulus == 0 and q-1 > params['G_lower_threshold']
        assert gcd(q, 2*a) == 1
        fac = prime_factors(q-1)
        assert prod(p**e for p,e in fac.items()) == q-1
        assert all(prime_trial(p) for p in fac)
        witnesses = {p:pow(generator, (q-1)//p, q) for p in fac}
        assert all(z != 1 for z in witnesses.values())
        assert pow(generator,q-1,q) == 1
        assert 2 % (q-1) != 0 and 4 % (q-1) != 0 and 2 % (q-1) != 4 % (q-1)
        primes.append(dict(a=a,b=bb,q=q,trial_limit=isqrt(q),
                           factors_q_minus_1=fac,primitive_root=generator,
                           primitive_root_witnesses=witnesses))
    L = lcm(28, *(p['q']-1 for p in primes))
    assert L == 14995460592
    subgroup = {pow(3,i,28) for i in range(12)}
    assert subgroup == {1,3,9,27,25,19} and 17 not in subgroup
    generated = {(x*pow(17,j,28))%28 for x in subgroup for j in range(2)}
    assert generated == {a for a in range(28) if gcd(a,28)==1}
    norm_half = [a for a in generated if a%7 in {1,2,4}]
    assert sum(norm_half) == 84 and sum(norm_half)%28 == 0
    assert 1+7*2**2 == 29 and gcd(2,29)==1
    assert 42%8 != 0 and all(((42*h)%8 == 0) == (h%4 == 0) for h in range(1,65))
    result = dict(result='PASS',checked_at=datetime.now(timezone.utc).isoformat(),
        scope='Exact numerical source Ranks/HC/centred/NCGaps and selected recurrence, primality by trial division, norm/congruence and primitive-root witnesses, common-field finite Galois group and alpha arithmetic. No Hecke, theta, class-number or Lean theorem is computationally inferred.',
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        parameters=params,primes=primes,coefficient_root_lcm=L,
        subgroup_generated_by_3=sorted(subgroup),
        subgroup_generated_by_3_and_17=sorted(generated),
        external_quadratic_norm_half=sorted(norm_half),
        alpha_norm=29,minimum_real_extension_for_eight_divisibility=4)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
