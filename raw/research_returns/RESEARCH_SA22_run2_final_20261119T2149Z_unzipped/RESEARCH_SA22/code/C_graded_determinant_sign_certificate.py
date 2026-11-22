"""Exact finite certificate for the graded-determinant sign correction.

The scope is all four parity pairs, all eight parity triples, and block ranks
0 through 4. It checks the two explicit Spec(Q) counterexamples to the printed
sum exponent. General coherence, arbitrary-rank exterior signs, and the
Knudsen--Mumford source qualifications are established in the written proof;
this finite computation does not certify them by extrapolation.
"""
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
from time import perf_counter


def main():
    started_at = datetime.now(timezone.utc).isoformat()
    started = perf_counter()
    checks = 0

    def verify(condition, description):
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(description)

    def sign(exponent):
        return -1 if exponent % 2 else 1

    parity_pairs = []
    for a, b in product(range(2), repeat=2):
        koszul = sign(a * b)
        printed = sign(a + b)
        verify(koszul * sign(b * a) == 1, "Koszul involutivity")
        verify(printed * sign(b + a) == 1, "printed family is also involutive")
        verify((koszul != printed) == ((a, b) != (0, 0)), "exact parity comparison")
        parity_pairs.append({"a": a, "b": b, "koszul": koszul,
                             "printed_sum": printed,
                             "agree": koszul == printed})

    parity_triples = []
    for a, b, c in product(range(2), repeat=3):
        verify(sign(a * (b + c)) == sign(a * b) * sign(a * c), "first hexagon")
        verify(sign((a + b) * c) == sign(a * c) * sign(b * c), "second hexagon")
        parity_triples.append({"a": a, "b": b, "c": c,
                               "first_hexagon": True, "second_hexagon": True})

    for a in range(5):
        verify(sign(a * 0) == 1, "right unit")
        verify(sign(0 * a) == 1, "left unit")

    block_pairs = []
    for r, s in product(range(5), repeat=2):
        # Move the second block before the first. Count actual inversions,
        # independently of the product formula being checked.
        permutation = tuple(range(r, r + s)) + tuple(range(r))
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(len(permutation))
                         for j in range(i + 1, len(permutation)))
        verify(inversions == r * s, "block inversion count")
        verify(sign(inversions) == sign(r * s), "block exterior sign")
        block_pairs.append({"r": r, "s": s, "permutation": permutation,
                            "inversions": inversions,
                            "exterior_sign": sign(inversions)})

    # Exact rational scalars make the characteristic assumption explicit.
    verify(Fraction(sign(1 + 0)) == -1 and Fraction(sign(1 * 0)) == 1,
           "Spec(Q), degrees(1,0): printed sum contradicts the unit")
    verify(Fraction(sign(1 + 1)) == 1 and Fraction(sign(1 * 1)) == -1,
           "Spec(Q), degrees(1,1): printed sum contradicts the wedge swap")

    source = Path(__file__).resolve()
    result = {
        "status": "PASS",
        "execution_mode": "standalone exact finite certificate; one actual run",
        "source_program": "code/" + source.name,
        "source_sha256": sha256(source.read_bytes()).hexdigest(),
        "started_at_utc": started_at,
        "finished_at_utc": datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds": perf_counter() - started,
        "checks_count": checks,
        "parity_pairs_count": len(parity_pairs),
        "parity_triples_count": len(parity_triples),
        "block_rank_pairs_count": len(block_pairs),
        "scope": "Finite signs only. The general result is proved separately; no base-change or trace-splitting computation is claimed.",
        "parity_pairs": parity_pairs,
        "parity_triples": parity_triples,
        "block_rank_pairs": block_pairs,
        "counterexamples_over_Q": [
            {"degrees": [1, 0], "printed_scalar": -1, "required_unit_scalar": 1},
            {"degrees": [1, 1], "printed_scalar": 1, "required_wedge_scalar": -1},
        ],
    }
    output = source.parents[1] / "logs" / "C_graded_determinant_sign_certificate.json"
    if output.exists():
        raise FileExistsError("Preserve the existing certificate; no optional rerun is intended")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in (
        "status", "started_at_utc", "finished_at_utc", "elapsed_seconds",
        "checks_count", "parity_pairs_count", "parity_triples_count",
        "block_rank_pairs_count", "source_sha256")}, indent=2))


if __name__ == "__main__":
    main()
