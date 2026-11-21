"""Finite exact checks of O024's shaving and positive count."""
from datetime import datetime, timezone
from itertools import combinations_with_replacement, product
from pathlib import Path
import json


def support(caps):
    if not caps:
        return [()]
    return [g for g in product(range(caps[0] + 1), repeat=len(caps))
            if all(sum(g[j:]) <= caps[j] for j in range(len(caps)))]


def count_recurrence(caps):
    values = [1]*(caps[-1] + 1)
    for cap in reversed(caps[:-1]):
        values = [sum(values[:t + 1]) for t in range(cap + 1)]
    return sum(values)


shape_cases = 0
monomial_cases = 0
for length in range(1, 5):
    for ascending in combinations_with_replacement(range(6), length):
        caps = tuple(reversed(ascending))
        gamma_set = support(caps)
        for b in range(6):
            shaved = tuple(max(c - b, 0) for c in caps)
            A = support(shaved)
            assert count_recurrence(shaved) == len(A)
            partitions = [nu for nu in product(range(shaved[0] + 1), repeat=length)
                          if all(nu[j] <= shaved[j] for j in range(length))
                          and all(nu[j] >= nu[j + 1] for j in range(length - 1))]
            assert len(partitions) == len(A)
            for gamma in gamma_set:
                alpha = list(gamma)
                remaining = b
                for j in reversed(range(length)):
                    take = min(remaining, alpha[j])
                    alpha[j] -= take
                    remaining -= take
                assert tuple(alpha) in A
                assert sum(gamma) - sum(alpha) <= b
                for j in range(length):
                    assert sum(alpha[j:]) == max(sum(gamma[j:]) - b, 0)
                monomial_cases += 1
            shape_cases += 1

C_star = 478126755
max_second_row = (C_star + 77)//3
assert max_second_row == 159375610
assert 3*max_second_row - 77 == 478126753 <= C_star
assert 3*(max_second_row + 1) - 77 == 478126756 > C_star
alternative = {(0, 0), (1, 0), (2, 0), (0, 1), (0, 2)}
D2 = support((2, 2))
sumset = {(a[0] + b[0], a[1] + b[1]) for a in alternative for b in D2}
assert set(support((4, 4))) <= sumset
assert len(alternative) == 5 < len(D2) == 6

record = {
    "finding": "O-024", "date_utc": datetime.now(timezone.utc).isoformat(),
    "model": "GPT-6 Astra Pro", "effort": "not exposed", "run": "GCT_KRON_20261120",
    "shape_and_jet_cases": shape_cases, "greedy_monomial_cases": monomial_cases,
    "scope": "All tails of length1..4 with parts0..5 and jet orders0..5; universal proof is in the text.",
    "C_star": C_star, "max_excluded_second_row_with_other_caps": max_second_row,
    "next_required_second_row": max_second_row + 1,
    "canonical_nonminimal_example_sizes": [6, 5], "status": "PASS",
}
destination = Path(__file__).with_name("shaved_profile_certificate.json")
destination.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"status": "PASS", "shape_cases": shape_cases,
                  "monomial_cases": monomial_cases, "certificate": str(destination)}))
