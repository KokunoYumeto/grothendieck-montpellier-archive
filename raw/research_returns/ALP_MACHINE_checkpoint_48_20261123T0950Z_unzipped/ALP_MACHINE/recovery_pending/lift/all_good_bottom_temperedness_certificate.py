#!/usr/bin/env python3
"""Exact diagnostics for LIFT076; not a representation-theoretic or Lean proof.

Checks the multiplicity distinctions used by the proof, direct-sum cancellation,
the literal divisor-degree obstruction, actual parity and unit-gap cases, and
the hashes/anchors of the source files read by the author.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return tuple(poly)


def mul(f, g, p):
    out = [0] * (len(f) + len(g) - 1)
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            out[i + j] = (out[i + j] + a*b) % p
    return trim(out)


def divmod_poly(f, g, p):
    f = list(trim(f))
    quotient = [0] * max(1, len(f) - len(g) + 1)
    while len(f) >= len(g) and f != [0]:
        shift = len(f) - len(g)
        coefficient = f[-1] * pow(g[-1], -1, p) % p
        quotient[shift] = coefficient
        for j, a in enumerate(g):
            f[shift + j] = (f[shift + j] - coefficient*a) % p
        f = list(trim(f))
    return trim(quotient), trim(f)


def monic_nonzero(p, degree):
    for const in range(1, p):
        for tail in itertools.product(range(p), repeat=degree-1):
            yield (const,) + tail + (1,)


def factor(f, p):
    """Independent trial division, with the first divisor necessarily irreducible."""
    if len(f) == 1:
        return Counter()
    for degree in range(1, (len(f)-1)//2 + 1):
        for g in monic_nonzero(p, degree):
            quotient, remainder = divmod_poly(f, g, p)
            if remainder == (0,):
                return factor(g, p) + factor(quotient, p)
    return Counter({f: 1})


def reciprocal(f, p):
    scale = pow(f[0], -1, p)
    return tuple(scale*a % p for a in reversed(f))


def divisor_degrees(degrees):
    possible = {0}
    for degree in degrees:
        possible |= {x + degree for x in possible}
    return possible


def arthur_string(label, length):
    return Counter((label, Fraction(length-1-2*i, 2)) for i in range(length))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    own = Path(__file__).resolve().parent
    work = next(p for p in own.parents if (p/'research/alpoge_source').is_dir())
    refs = work/'recovery_pending/lift/source_recovery'
    count = 0
    groups = Counter()

    def check(condition, label):
        nonlocal count
        if not condition:
            raise AssertionError((label, count))
        count += 1
        groups[label] += 1

    # A squarefree polynomial has one copy of each irreducible orbit, not just
    # a named underlying set. Compare exact factorization and actual divisors.
    for p in [2, 3, 5]:
        for degree in range(1, 5):
            for f in monic_nonzero(p, degree):
                factors = factor(f, p)
                product = (1,)
                all_degrees = []
                for g, multiplicity in factors.items():
                    for _ in range(multiplicity):
                        product = mul(product, g, p)
                        all_degrees.append(len(g)-1)
                check(product == f, 'finite_factorization')
                check(sum(all_degrees) == degree, 'finite_factor_degree')
                check((len(factors) == sum(factors.values())) ==
                      all(m == 1 for m in factors.values()), 'squarefree_multiset')
                dual_factors = Counter({reciprocal(g, p): m for g, m in factors.items()})
                check(factor(reciprocal(f, p), p) == dual_factors,
                      'reciprocal_preserves_multiplicity')
                predicted = divisor_degrees(all_degrees)
                actual = {0, degree}
                # Complementary divisors account for the upper half of degrees.
                for d in range(1, degree//2 + 1):
                    if any(divmod_poly(f, g, p)[1] == (0,)
                           for g in monic_nonzero(p, d)):
                        actual |= {d, degree-d}
                check(predicted == actual, 'actual_divisor_degrees')

    # Distinct inertial classes force each exponent to equal its own negative.
    # Ranks vary, so a central-character comparison cannot silently drop d_i.
    exponents = [Fraction(j, 2) for j in range(-2, 3)]
    for classes in range(1, 7):
        ranks = [1 + (3*i) % 7 for i in range(classes)]
        for xs in itertools.product(exponents, repeat=classes):
            support = Counter((i, ranks[i], x) for i, x in enumerate(xs))
            hermitian = Counter((i, ranks[i], -x) for i, x in enumerate(xs))
            equal = support == hermitian
            check(equal == all(x == 0 for x in xs), 'distinct_inertial_exponents')
            check(equal == all(ranks[i]*x == -ranks[i]*x for i, x in enumerate(xs)),
                  'central_absolute_character')
            permuted = list(reversed(list(support.elements())))
            check(Counter(permuted) == support, 'ordering_does_not_change_support')
    # The excluded repeated-class case really defeats this exponent argument.
    for numerator in range(1, 10):
        for denominator in range(2, 11):
            x = Fraction(numerator, denominator)
            repeated = Counter([(0, x), (0, -x)])
            check(repeated == Counter((i, -y) for i, y in repeated.elements()),
                  'repeated_class_counterexample')
            check(x != 0 and repeated[(0, x)] != 0,
                  'repeated_class_not_zero_exponents')

    # A nontrivial Arthur SL2 factor repeats an inertial class even if its
    # distinct unramified twists are distinct irreducible Weil summands.
    for blocks in range(1, 6):
        for lengths in itertools.product(range(1, 5), repeat=blocks):
            expanded = Counter()
            for i, length in enumerate(lengths):
                expanded += arthur_string(i, length)
            inertia = Counter()
            for (label, exponent), multiplicity in expanded.items():
                inertia[label] += multiplicity
            check(tuple(inertia[i] for i in range(blocks)) == lengths,
                  'arthur_inertial_multiplicity')
            check(all(m == 1 for m in inertia.values()) == all(e == 1 for e in lengths),
                  'arthur_genericity_obstruction')
            # The auxiliary string may overlap an old summand; cancellation
            # must therefore be performed on multisets, not their supports.
            common = arthur_string(0, 1 + (sum(lengths) % 7))
            check((expanded + common) - common == expanded,
                  'overlapping_theta_string_cancellation')
            alternate = expanded + Counter({(blocks, Fraction(0)): 1})
            check((expanded + common == alternate + common) == (expanded == alternate),
                  'direct_sum_cancellation_injective')
            shifted = Counter((label, exponent + Fraction(3, 2))
                              for (label, exponent) in expanded.elements())
            unshifted = Counter((label, exponent - Fraction(3, 2))
                                for (label, exponent) in shifted.elements())
            check(unshifted == expanded, 'common_character_twist_cancellation')
    # Multiplicity, not just an underlying set, is essential to GT13.
    check(set(Counter({'a': 1})) == set(Counter({'a': 2})), 'set_vs_multiset_warning')
    check(Counter({'a': 1}) != Counter({'a': 2}), 'set_vs_multiset_warning')

    # The literal divisor clause can force a simple global parameter while no
    # individual local polynomial is irreducible. These are degree models of
    # that clause only, not claims that all other IsGood clauses follow.
    for r in range(5, 82, 2):
        patterns = [(1, r-1), (2, r-2)]
        common = set.intersection(*(divisor_degrees(p) for p in patterns))
        check(common == {0, r}, 'no_local_irreducibility_needed')
        for d in range(1, r//2 + 1):
            witness = [p for p in patterns if d not in divisor_degrees(p)]
            check(bool(witness), 'literal_every_degree_witness')
            # A putative block of rank d must yield d in every local divisor set.
            check(not all(d in divisor_degrees(p) for p in patterns),
                  'global_block_contradiction')
    for total in range(2, 101):
        for first in range(1, total):
            blocks = [first, total-first]
            check(1 <= min(blocks) and 2*min(blocks) <= total,
                  'smallest_global_block')
    for r, mixed in [(43, (37, 6)), (169, (163, 6))]:
        check(sum(mixed) == r, 'carried_concrete_degree_models')
        check(divisor_degrees((r,)) & divisor_degrees(mixed) == {0, r},
              'carried_concrete_degree_models')

    # The symbolic all-word parity/dominance formula is checked on unit HC gaps
    # as well as wider gaps. These finite diagnostics are not all possible words.
    # The theorem must not accidentally reuse LIFT070's >1 input.
    for k in range(2, 50, 2):
        for m in range(2, 22, 2):
            r = k+m-1
            check(r % 2 == 1, 'actual_bottom_odd_rank')
            for seed in range(6):
                gaps = [1 + ((i+seed) % 3) for i in range(r-1)]
                h = [17]
                for gap in gaps:
                    h.append(h[-1] - gap)
                weight = [h[i] - ((r-1)//2-i) for i in range(r)]
                check(all(weight[i]-weight[i+1] == gaps[i]-1 for i in range(r-1)),
                      'actual_integral_coefficient_weight')
                check(all(weight[i] >= weight[i+1] for i in range(r-1)),
                      'unit_gap_dominance')
                check(all((weight[i] == weight[i+1]) == (gaps[i] == 1)
                          for i in range(r-1)), 'unit_gap_not_irregular_hc')
                conjugate_h = [-x for x in reversed(h)]
                conjugate_weight = [conjugate_h[i] - ((r-1)//2-i) for i in range(r)]
                check(conjugate_weight == [-x for x in reversed(weight)],
                      'conjugate_coefficient_parity')
                # A dual orientation changes both HC order and signs together.
                check(all(conjugate_h[i] > conjugate_h[i+1] for i in range(r-1)),
                      'dual_strict_hc_order')

    targets = {
      work/'research/alpoge_source/Formalism/CyclotomicNorms/StatementT.lean':
        ['(∀ v, Squarefree (f v))', '1 ≤ a → 2 * a ≤ N', 'q ∣ f v ∧ q.natDegree = a'],
      work/'research/alpoge_source/Formalism/SharpRestriction/LevelLetterCocycles/DataN.lean':
        ['def goodTuple', 'Formalism.CyclotomicNorms.IsGood R.r', 'def e0', '(X.eSer kv.1'],
      work/'research/alpoge_source/Formalism/LocalRingCardinality/Params.lean':
        ['k_even : Even k', 'm_even : Even m', 'def r : ℕ := R.k + R.m - 1'],
      work/'research/alpoge_source/Formalism/LocalRingCardinality/DataTheta.lean':
        ['def Interlace', 'def Dpar', '(P.v τ i, true)', '(-P.b τ i,'],
      work/'research/alpoge_source/Formalism/SharpRestriction/CuspSpanNormBounds/CayleySignature.lean':
        ['def TParity', 'P.v τ i = (n : ℚ)', 'P.b τ j = (n : ℚ)'],
      refs/'nadimpalli_level_zero2019.txt':
        ['Corollary 3.3.', 'Definition 3.1.', 'inertial support of π is s',
         'G-quotient of π', 'Bushnell–Kutzko type'],
      refs/'casselman1995_draft.txt':
        ['Theorem 5.2.1.', 'Corollary 5.2.3.', 'Lemma 5.2.5.'],
      refs/'waldspurger2003_plancherel.txt':
        ['Proposition III.2.2.', 'Lemme III.2.3.', 'f (mug)', 'δP (m)1/2'],
      work/'agents/lift_refs/gow_vinroot2007.txt':
        ['Theorem 3.2.', 'isomorphisms of graded', 'parabolic induction'],
      work/'agents/local_t_branch_refs/scholze2013_local_langlands.txt':
        ['Theorem 1.2.', 'parabolic induction', 'supercuspidal representations'],
      work/'agents/definite_oscillator_ggp_refs/chen_zou2025.txt':
        ['Theorem 2.6.', 'Theorem 3.1.', 'Theorem 3.4.', 'Proposition 4.1.', 'Remark 6.4.'],
    }
    hashes = {}
    for path, needles in targets.items():
        data = path.read_bytes()
        text = data.decode()
        for needle in needles:
            check(needle in text, 'source_primary_anchor')
        hashes[str(path)] = hashlib.sha256(data).hexdigest()
    result = {
      'status': 'PASS', 'assertions': count, 'groups': dict(groups),
      'completed_utc': datetime.now(timezone.utc).isoformat(),
      'scope': 'Exact finite-polynomial, multiset, exponent, degree, parity and source-anchor diagnostics; not a proof of the cited representation theory, global distinction, or a Lean theorem.',
      'source_sha256': hashes,
      'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['status','assertions','groups','completed_utc']}, indent=2))


if __name__ == '__main__':
    main()
