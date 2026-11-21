"""Finite exact tests for the prime-cocharacter construction and its failure mode."""
from itertools import product
from pathlib import Path
import json
import sympy as sp


def prime_family(n, delta):
    h = 2 * delta * (n - 1)
    bound = 16 * (h + 2 * n + 2) ** 2
    primes = []
    x = h
    for _ in range(2 * n):
        x = int(sp.nextprime(x))
        primes.append(x)
    assert primes[-1] <= bound
    base, alternates = primes[:n], primes[n:]
    weights = [tuple(base)]
    for j in range(n):
        row = base.copy()
        row[j] = alternates[j]
        weights.append(tuple(row))
    return weights, bound


def monic_product_image(roots, weights, characteristic):
    polynomial = [1]
    for root, weight in zip(roots, weights):
        if root is None:
            continue
        new = [0] * (len(polynomial) + weight)
        for j, coefficient in enumerate(polynomial):
            new[j + weight] = (new[j + weight] + coefficient) % characteristic
            new[j] = (new[j] - root * coefficient) % characteristic
        polynomial = new
    return tuple(polynomial)


exhaustive = []
for characteristic in [2, 7]:
    n, delta = 4, 1
    weights, bound = prime_family(n, delta)
    images = {}
    base_images = {}
    count = 0
    base_collisions = 0
    for roots in product([None] + list(range(characteristic)), repeat=n):
        signature = tuple(monic_product_image(roots, row, characteristic)
                          for row in weights)
        assert signature not in images
        images[signature] = roots
        if signature[0] in base_images:
            base_collisions += 1
        base_images[signature[0]] = roots
        count += 1
    exhaustive.append(dict(characteristic=characteristic, n=n, delta=delta,
                           normalized_products=count,
                           all_product_pairs_separated=True,
                           base_curve_collision_count=base_collisions,
                           characteristic_weight_present=
                           any(characteristic in row for row in weights)))


def subset_collision(weights):
    states = {0: 0}
    for i, weight in enumerate(weights):
        extension = {}
        for total, mask in list(states.items()):
            target = total + weight
            candidate = mask | (1 << i)
            previous = states.get(target, extension.get(target))
            if previous is not None and previous != candidate:
                positive = candidate & ~previous
                negative = previous & ~candidate
                vector = [int(bool(positive & (1 << j)))
                          - int(bool(negative & (1 << j)))
                          for j in range(len(weights))]
                assert any(vector)
                assert sum(a * b for a, b in zip(vector, weights)) == 0
                return vector
            extension[target] = candidate
        states.update(extension)
    raise AssertionError("Pigeonhole collision was not found")


weights, bound = prime_family(64, 1)
a = subset_collision(weights[0][:32]) + [0] * 32
b = [0] * 32 + subset_collision(weights[0][32:])
assert 2 ** 32 > 32 * bound + 1
for row in weights:
    assert (sum(x * y for x, y in zip(a, row)) == 0
            or sum(x * y for x, y in zip(b, row)) == 0)

x = sp.symbols("x0:64")
u, v = sp.Matrix([[1, -1]]), sp.Matrix([1, 1])


def binomial_and_matrix(exponents):
    matrix = sp.eye(2)
    for i, exponent in enumerate(exponents):
        matrix *= sp.diag(x[i] ** max(exponent, 0),
                          x[i] ** max(-exponent, 0))
    return (u * matrix * v)[0], matrix


fa, ma = binomial_and_matrix(a)
fb, mb = binomial_and_matrix(b)
output = sp.expand((u * ma * (v * u) * mb * v)[0])
assert sp.expand(output - fa * fb) == 0
poly = sp.Poly(output, *x)
assert not poly.is_zero
assert all(max(exponent) <= 1 for exponent in poly.monoms())

result = dict(exhaustive_product_tests=exhaustive,
              raw_family_counterexample=dict(
                  n=64, delta=1, curves=len(weights), weight_bound=bound,
                  base_max_weight=max(weights[0]),
                  first_relation=[(i, a[i]) for i in range(64) if a[i]],
                  second_relation=[(i, b[i]) for i in range(64) if b[i]],
                  all_raw_curves_kill_product=True,
                  nonzero_multilinear_width2_bridge_identity=True),
              scope="Exact finite corroboration, not a general formal certificate.")
Path(__file__).with_name("I33_computation_checks.json").write_text(
    json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
