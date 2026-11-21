"""Exact small instances of the sharp two-rank profile construction."""
from pathlib import Path
import json
import sympy as sp


def elementary(w, i, j):
    e = sp.zeros(w)
    e[i, j] = 1
    return e


checks = []
for w in range(2, 8):
    for r in range(1, w):
        c = w - r
        h = r * c + w - 1
        variables = sp.symbols(f"x0:{h}")
        passive = list(range(r, w))
        projection = sp.diag(*([1] * r + [0] * c))
        layers = []
        index = 0

        def chain(i, j):
            global index
            x = variables[index]
            index += 1
            layers.append((sp.eye(w), elementary(w, i, j), x, w))

        for i, j in zip(passive, passive[1:]):
            chain(i, j)
        for a in range(r):
            x = variables[index]
            index += 1
            layers.append((projection, elementary(w, passive[-1], a), x, r))
            chain(a, passive[0])
            for i, j in zip(passive, passive[1:]):
                chain(i, j)
        assert index == h

        row = sp.zeros(1, w)
        row[0, passive[0]] = 1
        for constant, linear, x, rank in layers:
            assert (constant + x * linear).rank() == rank
            row = (row * (constant + x * linear)).applyfunc(sp.expand)
        assert sp.expand(row[0, passive[-1]] - sp.prod(variables)) == 0

        for start in range(h):
            constant_product = sp.eye(w)
            has_reset = False
            for end in range(start, h):
                constant_product *= layers[end][0]
                has_reset |= layers[end][3] == r
                assert constant_product.rank() == (r if has_reset else w)

        coefficients = {}
        for j in range(w):
            for exponents, coefficient in sp.Poly(row[0, j], *variables).terms():
                coefficients.setdefault(exponents, [0] * w)[j] = coefficient
        all_rows = list(coefficients.values())
        lower_rows = [v for a, v in coefficients.items()
                      if sum(bool(d) for d in a) < h]
        assert sp.Matrix(all_rows).rank() == w
        assert sp.Matrix(lower_rows).rank() == w - 1
        checks.append(dict(w=w, r=r, c=c, h=h,
                           final_scalar_is_full_monomial=True,
                           all_local_ranks_and_constant_interval_ranks=True,
                           full_coefficient_rank=w,
                           smaller_support_coefficient_rank=w - 1))

result = dict(instances=checks,
              scope="Exact finite checks; interval generic-rank equality follows "
                    "from the proved factor-rank upper bound and constant minor.")
Path(__file__).with_name("I29_computation_checks.json").write_text(
    json.dumps(result, indent=2) + "\n")
print(json.dumps(dict(count=len(checks), max_width=7,
                     max_support=max(x['h'] for x in checks),
                     passed=True), indent=2))
