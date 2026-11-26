"""Universal odd-prime Heisenberg Pfaffian certificates, CC0 1.0.

Written directly from the statement formula before any original program read.
The implementation uses memoized symbolic Pfaffian recurrence, not sampled
coefficients. Monomials are sets with parity cancellation in characteristic two.
"""
from pathlib import Path
from functools import lru_cache
import argparse, datetime, hashlib, json, math, time


def certificate(ell):
    m = (ell - 1) // 2
    shift = 4 * ell
    inv2 = (ell + 1) // 2
    edge = {}
    for i in range(1, ell):
        for j in range(i + 1, ell):
            delta = (i - j) % ell
            cindex = min(delta, ell - delta) - 1
            yindex = ((i + j) * inv2) % ell
            edge[i, j] = (1 << (4 * yindex)) + (1 << (shift + 4 * cindex))

    @lru_cache(None)
    def pfaff(mask):
        if mask == 0:
            return frozenset([0])
        ibit = mask & -mask
        i = ibit.bit_length() - 1
        rest = mask ^ ibit
        candidates = rest
        result = set()
        while candidates:
            jbit = candidates & -candidates
            j = jbit.bit_length() - 1
            candidates ^= jbit
            factor = edge[i, j]
            for term in pfaff(rest ^ jbit):
                product = term + factor
                if product in result:
                    result.remove(product)
                else:
                    result.add(product)
        return frozenset(result)

    polynomial = pfaff(((1 << ell) - 1) ^ 1)
    lowmask = (1 << shift) - 1
    coefficients = {}
    for term in polynomial:
        y, c = term & lowmask, term >> shift
        coefficients.setdefault(y, []).append(c)

    def exponents(word, n):
        return [(word >> (4 * i)) & 15 for i in range(n)]

    def support(c):
        return sum(1 << i for i in range(m) if ((c >> (4 * i)) & 15))

    uncovered = set(range(1, 1 << m))
    witnesses = {}
    for y, terms in sorted(coefficients.items(), key=lambda item: (len(item[1]), item[0])):
        decorated = [(c, support(c)) for c in terms]
        for supp in list(uncovered):
            survivors = [c for c, t in decorated if t & ~supp == 0]
            if len(survivors) == 1:
                witnesses[str(supp)] = {
                    'nonzero_coefficient_indices': [i + 1 for i in range(m) if supp >> i & 1],
                    'y_monomial_exponents': exponents(y, ell),
                    'surviving_c_monomial_exponents': exponents(survivors[0], m),
                    'full_coefficient_monomials': [exponents(c, m) for c in sorted(terms)],
                }
                uncovered.remove(supp)
        if not uncovered:
            break
    result = {
        'ell': ell,
        'pfaffian_removed_row_and_column': 0,
        'degree': m,
        'formal_matching_count': math.prod(range(1, ell - 1, 2)),
        'cached_subproblems': pfaff.cache_info().currsize,
        'nonzero_full_monomials': len(polynomial),
        'y_coefficients': len(coefficients),
        'supports_required': (1 << m) - 1,
        'supports_certified': len(witnesses),
        'uncovered_supports': sorted(uncovered),
        'witnesses': witnesses,
    }
    assert not uncovered, result
    pfaff.cache_clear()
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='pfaffian_support_certificate.json')
    parser.add_argument('--primes', type=int, nargs='+', default=[3, 5, 7, 11, 13, 17])
    args = parser.parse_args()
    start = time.perf_counter()
    results = []
    for ell in args.primes:
        result = certificate(ell)
        results.append(result)
        print(json.dumps({k: v for k, v in result.items() if k != 'witnesses'}), flush=True)
    out = {
        'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'method': 'Memoized symbolic Pfaffian recurrence over F2[c,y], parity cancellation of monomial sets; support-wise universal nonzero coefficients. No original program imported and no finite-field sampling.',
        'scope': 'Each listed support has a y-coefficient reducing to one nonzero c-monomial; therefore the maximal Pfaffian is nonzero for every nonzero c over every characteristic-two field. Only the explicitly listed primes are certified.',
        'elapsed_seconds': time.perf_counter() - start,
        'program_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'passed': True,
        'results': results,
    }
    Path(args.output).write_text(json.dumps(out, indent=2) + '\n')


if __name__ == '__main__':
    main()
