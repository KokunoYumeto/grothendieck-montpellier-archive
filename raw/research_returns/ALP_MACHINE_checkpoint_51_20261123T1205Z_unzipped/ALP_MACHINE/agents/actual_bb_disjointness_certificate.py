#!/usr/bin/env python3
"""AM-K045: exact BB disjointness; deterministic elementary arithmetic only."""
from pathlib import Path
from datetime import datetime, timezone
from math import gcd, isqrt, prod
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
CHECKS = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    CHECKS.append(name)


def prime_by_trial(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n)+1, 2))


SMALL_PRIMES = [n for n in range(2, 1000) if prime_by_trial(n)]


def small_factorization(n):
    rest = n
    factors = {}
    for p in SMALL_PRIMES:
        v = 0
        while rest % p == 0:
            rest //= p
            v += 1
        if v:
            factors[p] = v
    assert rest == 1, ('remaining gcd has an unproved factor', n, rest)
    assert prod(p**v for p, v in factors.items()) == n
    return factors


def valuation(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def main():
    configs = [
        ('J14',42,43,4615409,5276377,177,27,61),
        ('J56',168,169,22285932761,64072175441,618,27,991),
    ]
    reports = []
    for name, a, N, g0, g1, remaining_count, gcd_count, maxp in configs:
        check(name+' actual source rank r=k+m-1', N == a+2-1)
        check(name+' distinct exact trial-division primes',
              g0 != g1 and prime_by_trial(g0) and prime_by_trial(g1))
        powers = [[g**d for d in range(1,N+1)] for g in (g0,g1)]
        unscreened = []
        digest = hashlib.sha256()
        largest = 1
        screen_count = 0
        for d, A in enumerate(powers[0],1):
            for e, B in enumerate(powers[1],1):
                C = gcd(A-1,B-1)
                assert (A-1) % C == 0 and (B-1) % C == 0
                screen = C**4 <= min(A,B)
                digest.update(f'{d},{e},{C},{int(screen)}\n'.encode())
                largest = max(largest,C)
                if screen:
                    screen_count += 1
                else:
                    unscreened.append(dict(d=d,e=e,gcd=C))
        check(name+' complete gcd screen pair count',
              screen_count+len(unscreened) == N*N and
              len(unscreened) == remaining_count)
        values = sorted({x['gcd'] for x in unscreened})
        factorizations = {C:small_factorization(C) for C in values}
        candidates = sorted({p for v in factorizations.values() for p in v})
        check(name+' all remaining gcds fully factored by small prime trials',
              len(values) == gcd_count and max(candidates) == maxp and
              all(prime_by_trial(p) for p in candidates))
        exceptions = {}
        one_sided = [[],[]]
        for p in candidates:
            data = []
            for side in (0,1):
                ex = []
                maxv = 0
                for d, A in enumerate(powers[side],1):
                    v = valuation(A-1,p)
                    maxv = max(maxv,v)
                    if A < p**(4*v):
                        ex.append(dict(d=d,valuation=v))
                if ex:
                    one_sided[side].append(p)
                data.append(dict(exceptional_degrees=ex,max_valuation=maxv))
            assert not(data[0]['exceptional_degrees'] and data[1]['exceptional_degrees'])
            exceptions[p] = data
        check(name+' candidate Exc sets are disjoint',
              not set(one_sided[0]).intersection(one_sided[1]))
        # A second check on the actual unscreened pairs, without discarding
        # their exponent indices in favour of the candidate superset.
        comparisons = 0
        for row in unscreened:
            A,B = powers[0][row['d']-1],powers[1][row['e']-1]
            for p in factorizations[row['gcd']]:
                v0,v1 = valuation(A-1,p),valuation(B-1,p)
                assert not(A < p**(4*v0) and B < p**(4*v1))
                comparisons += 1
        check(name+' every unscreened pair checked directly', True)
        cross = []
        for p, side in ((g0,1),(g1,0)):
            ex = []; nonzero = []
            for d, A in enumerate(powers[side],1):
                v=valuation(A-1,p)
                if v:
                    nonzero.append(dict(d=d,valuation=v))
                if A < p**(4*v):
                    ex.append(dict(d=d,valuation=v))
            assert not ex
            cross.append(dict(prime=p,other_prime=(g0,g1)[side],
                nonzero_valuation_degrees=nonzero,exceptional_degrees=ex))
        check(name+' both distinguished cross-prime cases excluded', True)
        reports.append(dict(host=name,k=a,N=N,g0=g0,g1=g1,
            exact_primality_method='Trial division by every odd integer through floor(sqrt(g)); no probable-prime test.',
            primality_trial_limits=[isqrt(g0),isqrt(g1)],
            total_pairs=N*N,screened_pairs=screen_count,unscreened_pairs=unscreened,
            all_pair_digest_sha256=digest.hexdigest(),largest_gcd=largest,
            distinct_remaining_gcds=len(values),remaining_gcd_factorizations=factorizations,
            candidate_primes=candidates,candidate_exception_table=exceptions,
            one_sided_candidate_Exc_sets=one_sided,
            direct_unscreened_prime_comparisons=comparisons,
            cross_prime_cases=cross,BB_intersection=[]))
    source=ROOT/'work/research/alpoge_source/Formalism'
    statement=source/'CyclotomicNorms/StatementI.lean'
    datan=source/'SharpRestriction/LevelLetterCocycles/DataN.lean'
    criterion=source/'CyclotomicNorms/StatementT.lean'
    st=statement.read_text()
    check('literal strict Exc and BB degree range',
          'g ^ d < ℓ ^ (4 * padicValNat ℓ (g ^ d - 1))' in st and
          '{g} ∪ {ℓ | ∃ d, 1 ≤ d ∧ d ≤ N ∧ Exc g d ℓ}' in st)
    check('literal NTypes BB_disj field',
          'BB_disj : Disjoint (Formalism.CyclotomicNorms.BB R.r (H.g 0)) (Formalism.CyclotomicNorms.BB R.r (H.g 1))' in datan.read_text())
    check('literal irreducibility criterion disjointness premise',
          'BB N (g 0) ∩ BB N (g 1) = ∅' in criterion.read_text())
    result=dict(finding='AM-K045',status='PASS',
        time_utc=datetime.now(timezone.utc).isoformat(),
        grouped_checks=len(CHECKS),checks=CHECKS,hosts=reports,
        total_gcd_pairs=sum(h['total_pairs'] for h in reports),
        scope='Complete exact BB intersection for the two specified rank/prime pairs. No factorization of any g^d-1, probable-prime oracle, good-tuple construction, global automorphic pin or Lean build.',
        source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                       for p in (statement,datan,criterion)},
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    target=Path(__file__).with_suffix('.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',time_utc=result['time_utc'],
        checks=len(CHECKS),gcd_pairs=result['total_gcd_pairs'],output=str(target))))


if __name__=='__main__':
    main()
