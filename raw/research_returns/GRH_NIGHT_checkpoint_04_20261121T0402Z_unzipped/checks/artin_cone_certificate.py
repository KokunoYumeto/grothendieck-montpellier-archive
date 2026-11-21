"""Exact finite certificate for MT-ART04; no floating point arithmetic."""
from itertools import permutations
import json

def mul(a, b):
    return tuple(a[b[i]] for i in range(5))

def inv(a):
    b = [0] * 5
    for i, j in enumerate(a):
        b[j] = i
    return tuple(b)

def even(a):
    return sum(a[i] > a[j] for i in range(5) for j in range(i + 1, 5)) % 2 == 0

G = [a for a in permutations(range(5)) if even(a)]
def chi(a):
    return sum(a[i] == i for i in range(5)) - 1

X = [[chi(mul(g, inv(h))) for h in G] for g in G]
K = [[60 * (i == j) - 5 * X[i][j] for j in range(60)] for i in range(60)]
assert all(sum(X[i][k] * X[k][j] for k in range(60)) == 15 * X[i][j]
           for i in range(60) for j in range(60))
v = [chi(g) for g in G]
quad = sum(v[i] * K[i][j] * v[j] for i in range(60) for j in range(60))
assert sum(v) == 0 and sum(t * t for t in v) == 60 and quad == -900
classes = {frozenset(mul(mul(h, g), inv(h)) for h in G) for g in G}
class_sizes = sorted(map(len, classes))
assert class_sizes == [1, 12, 12, 15, 20]
print(json.dumps({
    "statement": "MT-ART04", "group_order": len(G),
    "conjugacy_class_sizes": class_sizes,
    "character_sum": sum(v), "character_norm_squared_times_order": sum(t*t for t in v),
    "matrix_identity": "X^2=15X (checked entrywise)",
    "negative_quadratic_form": quad,
    "scope": "Exact finite calculation; not a formal proof assistant certificate and not an actual Artin L-order realization."
}, indent=2))
