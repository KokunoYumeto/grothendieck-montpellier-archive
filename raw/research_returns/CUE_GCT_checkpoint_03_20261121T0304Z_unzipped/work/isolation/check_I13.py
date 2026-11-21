"""Finite exact checks for I-13; these supplement, not replace, its proof."""
from itertools import product
from pathlib import Path

import sympy as sp


def projector_basis(d):
    vectors = [sp.eye(d)[:, i] for i in range(d)]
    for i in range(d):
        for j in range(i + 1, d):
            vectors.append(sp.eye(d)[:, i] + sp.eye(d)[:, j])
            vectors.append(sp.eye(d)[:, i] + sp.I * sp.eye(d)[:, j])
    return vectors


lines = []
for d, n in [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2)]:
    local = projector_basis(d)
    columns = []
    for vectors in product(local, repeat=n):
        v = vectors[0]
        for next_v in vectors[1:]:
            v = sp.kronecker_product(v, next_v)
        columns.append((v * v.conjugate().T).reshape(d ** (2 * n), 1))
    matrix = sp.Matrix.hstack(*columns)
    actual = matrix.rank()
    expected = d ** (2 * n)
    assert actual == expected, (d, n, actual, expected)
    lines.append(f"PASS product projectors: d={d}, n={n}, exact rank={actual}")

for n in range(1, 6):
    exponents = list(product(range(2), repeat=n))
    nodes = list(product([-1, 1], repeat=n))
    E = sp.Matrix([[sp.prod(x ** a for x, a in zip(node, alpha))
                    for alpha in exponents] for node in nodes])
    assert E.T * E == (2 ** n) * sp.eye(2 ** n)
    lines.append(f"PASS matching roots-of-unity cubature: delta=1, n={n}, nodes={2 ** n}")

result = "\n".join(lines) + "\n"
Path(__file__).with_name("I13_computation_checks.txt").write_text(result)
print(result, end="")
