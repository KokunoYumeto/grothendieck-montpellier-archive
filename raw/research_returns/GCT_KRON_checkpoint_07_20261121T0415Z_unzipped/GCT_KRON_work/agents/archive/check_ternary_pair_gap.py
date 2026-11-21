"""Exact first deficit between a ternary-cubic ray and its binary-Hessian pair.

Two independent finite enumerations are used: generating-function weight DP,
and direct enumeration of weak compositions into the ten cubic monomials.
No floating-point arithmetic or numerical rank decision occurs.
"""
from collections import Counter
from itertools import permutations, product
from pathlib import Path
import hashlib
import json


def weight_dp(degree, second, third):
    dp = [[[0] * (third + 1) for _ in range(second + 1)]
          for _ in range(degree + 1)]
    dp[0][0][0] = 1
    for b in range(4):
        for c in range(4 - b):
            for d in range(1, degree + 1):
                for j in range(b, second + 1):
                    for k in range(c, third + 1):
                        dp[d][j][k] += dp[d - 1][j - b][k - c]
    return dp


def composition_weights(degree):
    weights = [(a, b, 3-a-b) for a in range(4) for b in range(4-a)]
    counts = Counter()
    visits = 0

    def visit(i, left, total):
        nonlocal visits
        if i == len(weights) - 1:
            w = weights[i]
            counts[tuple(total[j] + left*w[j] for j in range(3))] += 1
            visits += 1
            return
        w = weights[i]
        for exponent in range(left + 1):
            visit(i+1, left-exponent,
                  tuple(total[j] + exponent*w[j] for j in range(3)))
    visit(0, degree, (0, 0, 0))
    return counts, visits


def pair_upper(s):
    # (1-z)/prod_{i=1}^3(1-z^i)^2
    coefficients = [1] + [0]*s
    for degree in (1, 2, 2, 3, 3):
        for k in range(degree, s+1):
            coefficients[k] += coefficients[k-degree]
    return coefficients[s]


def tetrahedral_hesse_contraction():
    # Four epsilon tensors, with each cubic tensor entering three of them.
    ps = [(p, (-1)**sum(p[i] > p[j] for i in range(3)
                       for j in range(i+1, 3)))
          for p in permutations(range(3))]
    coefficients = Counter()
    for (p, sp), (q, sq), (r, sr), (s, ss) in product(ps, repeat=4):
        indices = [(p[0], q[0], r[0]), (p[1], q[1], s[0]),
                   (p[2], r[1], s[1]), (q[2], r[2], s[2])]
        monomial = [0]*4  # a,b,c,j for ax^3+by^3+cz^3+6jxyz
        for v in indices:
            if v[0] == v[1] == v[2]:
                monomial[v[0]] += 1
            elif len(set(v)) == 3:
                monomial[3] += 1
            else:
                break
        else:
            coefficients[tuple(monomial)] += sp*sq*sr*ss
    return {str(k): v for k, v in coefficients.items() if v}


def main():
    rho = (2, 1, 0)
    rows = []
    for s in (1, 2):
        degree = 4*s
        dp = weight_dp(degree, 3*s+1, 2*s)
        direct, visits = composition_weights(degree)
        signed_terms = []
        value = 0
        for permutation in permutations(range(3)):
            sign = (-1)**sum(permutation[i] > permutation[j]
                            for i in range(3) for j in range(i+1, 3))
            mu = tuple((7*s, 3*s, 2*s)[i] + rho[i] - rho[permutation[i]]
                       for i in range(3))
            count = dp[degree][mu[1]][mu[2]]
            assert count == direct[mu]
            signed_terms.append({"weight": mu, "sign": sign,
                                 "dp_count": count, "direct_count": direct[mu]})
            value += sign*count
        rows.append({"s": s, "outer_degree": degree,
                     "highest_weight": [7*s, 3*s, 2*s],
                     "ambient_multiplicity": value,
                     "free_pair_upper": pair_upper(s),
                     "signed_terms": signed_terms,
                     "weak_compositions_visited": visits})
    assert [row["ambient_multiplicity"] for row in rows] == [1, 4]
    assert [row["free_pair_upper"] for row in rows] == [1, 3]
    contraction = tetrahedral_hesse_contraction()
    assert contraction == {"(1, 1, 1, 1)": -24, "(0, 0, 0, 4)": 24}
    source = Path(__file__).resolve().parents[3] / "external_sources/Isaev_associated_form.pdf"
    result = {
        "method": "exact integer weight DP plus independent weak-composition enumeration",
        "rows": rows,
        "tetrahedral_hesse_contraction": contraction,
        "Aronhold_normalization": "S=-(tetrahedral contraction)/24; S(ax^3+by^3+cz^3+6jxyz)=abcj-j^4",
        "missing_vector_family": {
            "F_c": "2*x^3+6*x*y^2+6*(x^2-y^2)*z+c*z^3",
            "F0": 2, "I2": 4,
            "S": "16*(c-1)", "S_times_F0_squared_I2": "256*(c-1)",
            "binary_pair": "independent of c"
        },
        "primary_source": {
            "author": "Alexander Isaev",
            "title": "On the image of the associated form morphism",
            "journal": "Saitama Math. J. 31 (2017), 89-101",
            "locator": "printed p.98, equation (4.1)",
            "url": "https://www.rimath.saitama-u.ac.jp/research/pdf/smj31-5.pdf",
            "sha256": hashlib.sha256(source.read_bytes()).hexdigest() if source.exists() else None
        }
    }
    target = Path(__file__).with_name("TERNARY_PAIR_GAP_CERTIFICATE.json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
