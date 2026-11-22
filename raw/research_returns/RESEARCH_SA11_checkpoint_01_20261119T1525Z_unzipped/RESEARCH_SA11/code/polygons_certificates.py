#!/usr/bin/env python3
"""Exact finite certificates for SA11 polygon claims (integer signs only).

Run from the package root: python code/polygons_certificates.py
No third-party package is required.  The program checks the full signed
basis-exchange chirotope axiom, not only the uniform three-term relations.
"""
from itertools import combinations, permutations
from functools import cmp_to_key
import json
import time


def sign(x):
    return (x > 0) - (x < 0)


def det(a, b, c):
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def alternating(table):
    def value(*t):
        if len(set(t)) != len(t):
            return 0
        inversions = sum(t[i] > t[j]
                         for i in range(len(t)) for j in range(i + 1, len(t)))
        return (-1 if inversions % 2 else 1) * table[tuple(sorted(t))]
    return value


def vector_chi(vectors):
    return alternating({t: sign(det(*(vectors[i] for i in t)))
                        for t in combinations(range(len(vectors)), 3)})


def combined_chi(old_chi, q, n):
    table = {t: old_chi(*t) for t in combinations(range(n), 3)}
    table.update({(i, j, n): q(i, j) for i, j in combinations(range(n), 2)})
    return alternating(table)


def basis_exchange(chi, ground):
    """Axiom B2 for every pair of ordered nonzero triples.

    For nonzero chi(x)*chi(y), one i must give that same product from
    chi(y_i,x_2,x_3)*chi(y_1,...,y_{i-1},x_1,y_{i+1},...,y_3).
    """
    ordered = [t for t in permutations(ground, 3) if chi(*t)]
    checked = 0
    for x in ordered:
        for y in ordered:
            checked += 1
            target = chi(*x) * chi(*y)
            terms = []
            for i in range(3):
                z = list(y)
                z[i] = x[0]
                terms.append(chi(y[i], x[1], x[2]) * chi(*z))
            if target not in terms:
                return {"valid": False, "checked_pairs": checked,
                        "x": x, "y": y, "target": target, "terms": terms}
    return {"valid": True, "checked_pairs": checked}


def q_from_word(word):
    """Boundary word -> contraction: signed pair alternation, or zero."""
    pos = {label: i for i, label in enumerate(word)}
    n2 = len(word)

    def q(i, j):
        if i == j:
            return 0
        i, j = i + 1, j + 1
        length = (pos[-i] - pos[i]) % n2
        plus_inside = 0 < (pos[j] - pos[i]) % n2 < length
        minus_inside = 0 < (pos[-j] - pos[i]) % n2 < length
        if plus_inside == minus_inside:
            return 0
        return 1 if plus_inside else -1
    return q


def boundary_word(chi, q, n):
    """Canonical expanded word from deletion chi and loopless rank-two q.

    The first half-circle starts at positive ray 1.  Each parallel packet
    is ordered using -eta*chi(i,j,k)*q(i,k), k outside the packet.
    Opposite packets have reversed orders.  Labels are signed 1,...,n.
    """
    k0 = next(k for k in range(1, n) if q(0, k))
    labels = []
    for i in range(n):
        if i == 0:
            eps = 1
        elif q(0, i):
            eps = q(0, i)
        else:
            eps = q(0, k0) * q(i, k0)
        labels.append(eps * (i + 1))

    def compare(a, b):
        i, j = abs(a) - 1, abs(b) - 1
        eps, eta = sign(a), sign(b)
        if q(i, j):
            return -eps * eta * q(i, j)
        k = next(k for k in range(n) if q(i, k))
        # Positive value means a precedes b in the packet.
        before = -eta * chi(i, j, k) * q(i, k)
        assert before in (-1, 1), (a, b, k, before)
        return -before

    labels.sort(key=cmp_to_key(compare))
    packets = []
    for a in labels:
        if not packets or q(abs(packets[-1][0]) - 1, abs(a) - 1):
            packets.append([a])
        else:
            packets[-1].append(a)
    return tuple(labels + [-a for packet in packets for a in reversed(packet)])


def cyclic_equal(a, b):
    return len(a) == len(b) and any(tuple(a) == tuple(b[i:] + b[:i])
                                  for i in range(len(b)))


def run():
    started = time.perf_counter()
    result = {}

    # R3: x=0, x=z, y=0; D: z=0.  Sigma is nontrivial, since det=1.
    a = [(1, 0, 0), (1, 0, -1), (0, 1, 0)]
    d = (0, 0, 1)
    chi = vector_chi(a)
    q = lambda i, j: sign(det(a[i], a[j], d))
    w = boundary_word(chi, q, 3)
    expected = (2, 1, 3, -1, -2, -3)
    assert cyclic_equal(w, expected)
    assert all(q_from_word(w)(i, j) == q(i, j)
               for i, j in combinations(range(3), 2))
    assert not all(w[(i + 3) % 6] == -w[i] for i in range(6))
    result["P3_cluster_reversal"] = {
        "old_normals": a, "new_normal": d, "old_basis_sign": chi(0, 1, 2),
        "boundary_word": w, "half_turn_is_label_negation": False,
        "full_chirotope_check": basis_exchange(vector_chi(a + [d]), range(4))}

    # Exploratory incompatibility example.  This does NOT meet the final
    # fixed-base three-triangle test and is not our L3 counterexample.
    old = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)]
    old_chi = vector_chi(old)
    qtab = {pair: 1 for pair in combinations(range(4), 2)}
    qp = alternating(qtab)
    candidate = combined_chi(old_chi, qp, 4)
    b2 = basis_exchange(candidate, range(5))
    assert not b2["valid"]
    terms = [candidate(2, 0, 1) * candidate(2, 3, 4),
             -candidate(2, 0, 3) * candidate(2, 1, 4),
             candidate(2, 0, 4) * candidate(2, 1, 3)]
    assert terms == [1, 1, 1]
    restricted = []
    for keep in combinations(range(4), 3):
        cert = basis_exchange(candidate, keep + (4,))
        assert cert["valid"]
        restricted.append({"old_indices": [i + 1 for i in keep], **cert})

    # The same word is genuine for four tangent-parabola lines; exactly three
    # immediate stable-to-substable specializations for this DIFFERENT base.
    # Borrowing them does not establish the fixed-base L3 hypotheses.
    other = [(1, t, t * t) for t in range(4)]
    other_chi = vector_chi(other)
    true_ext = vector_chi(other + [d])
    assert all(true_ext(i, j, 4) == 1 for i, j in combinations(range(4), 2))
    assert basis_exchange(true_ext, range(5))["valid"]
    specializations = []
    for pair in combinations(range(4), 2):
        qq = dict(qtab)
        qq[pair] = 0
        ext = combined_chi(other_chi, alternating(qq), 4)
        if basis_exchange(ext, range(5))["valid"]:
            specializations.append(tuple(i + 1 for i in pair))
    assert specializations == [(1, 2), (1, 4), (3, 4)]
    result["exploratory_n4_not_the_fixed_M_L3_counterexample"] = {
        "base_normals": old,
        "base_chi_in_123_124_134_234_order":
            [old_chi(*t) for t in combinations(range(4), 3)],
        "candidate_word": [1, 2, 3, 4, -1, -2, -3, -4],
        "contraction_signs": [1] * 6,
        "grassmann_pluecker_witness_1based":
            {"lambda": 3, "a": 1, "b": 2, "c": 4, "d": 5, "terms": terms},
        "full_chirotope_failure": b2,
        "all_three_old_line_restrictions": restricted,
        "other_base_realizing_same_word": other,
        "other_base_check": basis_exchange(true_ext, range(5)),
        "three_specialization_pairs": specializations,
        "specialization_arcs_in_candidate_word": [[1, 2], [4, -1], [-3, -4]],
        "arrow_weights": [1, 1, 1], "corner_weights": [2, 2, 1],
        "weight_sum": 8,
        "scope": "Exploratory incompatibility certificate only. The three triangles belong to the other base, so this is not a counterexample to the fixed-M L3 test. The valid L3 counterexample is certified in polygons_l3_verify.py."}

    # R1 one-class edge case: three small disjoint chords cutting off three caps.
    cap_word = [1, -1, 2, -2, 3, -3]
    # Each cyclic block of length 3 must contain each label exactly once if the
    # endpoints form two packets as required for a single vertex on D.
    packet_possible = any(len({abs(cap_word[(i + j) % 6]) for j in range(3)}) == 3
                          for i in range(6))
    assert not packet_possible
    assert all(q_from_word(cap_word)(i, j) == 0
               for i, j in combinations(range(3), 2))
    result["P1_one_class_packet_condition"] = {
        "boundary_word": cap_word, "all_chords_disjoint": True,
        "disjointness_is_equivalence": True,
        "two_packets_exist": packet_possible,
        "scope": "One-class degenerate case only; nontrivial rank-three arrangements avoid this obstruction."}

    result["runtime_seconds"] = round(time.perf_counter() - started, 6)
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
