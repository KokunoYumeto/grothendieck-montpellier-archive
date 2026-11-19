"""Exact formal WD diagnostic, not a geometric weight-monodromy example."""
from itertools import combinations
from pathlib import Path
import json
import sympy as sp
from datetime import datetime, timezone
from time import perf_counter

started_utc = datetime.now(timezone.utc).isoformat()
started_monotonic = perf_counter()

weights = [6, 4, 4, 2]
F = sp.diag(8, 4, 4, 2)
assert all(int(F[i, i]) % 3 for i in range(4))
N = sp.zeros(4)
N[1, 0] = 1
N[3, 2] = 1
Q = sp.zeros(4)
Q[0, 3] = Q[3, 0] = 1
Q[1, 2] = Q[2, 1] = -1
assert Q.det() != 0
assert 2 * F * N == N * F
assert N.T * Q + Q * N == sp.zeros(4)
assert F.T * Q * F == 16 * Q
assert N ** 2 == sp.zeros(4)
assert N.rank() == 2
assert sum(weights) == 4 * 4
kernel_weights = [weights[i] for i in range(4) if N[:, i] == sp.zeros(4, 1)]
assert kernel_weights == [4, 2]

pairs = list(combinations(range(4), 2))
pair_index = {pair: i for i, pair in enumerate(pairs)}
N2 = sp.zeros(len(pairs))
for col, (a, b) in enumerate(pairs):
    for slot in (0, 1):
        original = a if slot == 0 else b
        for dest in range(4):
            coeff = N[dest, original]
            if not coeff:
                continue
            newpair = [dest, b] if slot == 0 else [a, dest]
            if newpair[0] == newpair[1]:
                continue
            sign = 1
            if newpair[0] > newpair[1]:
                newpair.reverse()
                sign = -1
            N2[pair_index[tuple(newpair)], col] += sign * coeff
wedge_weights = [weights[a] + weights[b] for a, b in pairs]
witness = sp.zeros(len(pairs), 1)
witness[pair_index[(0, 1)], 0] = 1
assert N2 * witness == sp.zeros(len(pairs), 1)
assert wedge_weights[pair_index[(0, 1)]] == 10 > 8
assert N2 ** 3 == sp.zeros(len(pairs))
assert N2 ** 2 != sp.zeros(len(pairs))
kernel_weight_multiplicities = {}
for w in sorted(set(wedge_weights)):
    cols = [i for i, value in enumerate(wedge_weights) if value == w]
    dim = len(cols) - N2[:, cols].rank()
    if dim:
        kernel_weight_multiplicities[str(w)] = int(dim)
result = {
    "scope": "Formal Weil-Deligne linear algebra only; no geometric realization.",
    "local_field": "Q_2",
    "coefficient_field": "Q_3",
    "finite_Weil_inertia": "trivial",
    "frobenius_eigenvalues_are_3_adic_units": True,
    "q": 2,
    "candidate_pure_weight": 4,
    "weights": weights,
    "N_rank": int(N.rank()),
    "N_square_zero": True,
    "frobenius_relation": "2 F N = N F",
    "pairing_determinant": int(Q.det()),
    "N_skew_adjoint": True,
    "frobenius_similitude_factor": 16,
    "determinant_weight": sum(weights),
    "string_centres": [5, 3],
    "kernel_weights": kernel_weights,
    "single_endpoint_bound_passes": True,
    "weight_monodromy_purity": False,
    "exterior_square_basis_pairs": pairs,
    "exterior_square_N": [list(map(int, N2.row(i))) for i in range(N2.rows)],
    "exterior_square_kernel_weight_multiplicities": kernel_weight_multiplicities,
    "exterior_square_witness": "u_6 wedge v_4",
    "witness_weight": 10,
    "required_exterior_square_bound": 8,
    "exterior_square_endpoint_fails": True,
}
result["started_utc"] = started_utc
result["recorded_utc"] = datetime.now(timezone.utc).isoformat()
result["runtime_seconds"] = perf_counter() - started_monotonic
result["runtime_scope"] = "Exact symbolic certificate and result construction; excludes imports, JSON serialization, and file I/O."
output = Path(__file__).with_name("check_c4_exterior_witness_output.json")
output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
