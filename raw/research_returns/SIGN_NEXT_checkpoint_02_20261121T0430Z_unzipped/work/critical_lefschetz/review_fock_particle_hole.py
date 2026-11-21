"""Independent signed-exterior check of IF-04's particle-hole construction.

No code is imported from the integral_fock agent.  Original coordinates are
in the usual column order, so an interior simple root tests the required
root-first reordering signs rather than assuming them away.
"""
from collections import defaultdict
import json


def elementary(mask, coordinate, create):
    occupied = bool(mask & (1 << coordinate))
    if occupied == create:
        return None
    sign = -1 if (mask & ((1 << coordinate) - 1)).bit_count() % 2 else 1
    return mask ^ (1 << coordinate), sign


def compose_elementary(mask, operations):
    coefficient = 1
    for coordinate, create in operations:
        result = elementary(mask, coordinate, create)
        if result is None:
            return None
        mask, sign = result
        coefficient *= sign
    return mask, coefficient


def row_operator(mask, r, q, root, lower):
    result = defaultdict(int)
    a, b = (root + 1, root) if lower else (root, root + 1)
    for column in range(q):
        term = compose_elementary(mask, [(column * r + b, False), (column * r + a, True)])
        if term:
            result[term[0]] += term[1]
    return {m: c for m, c in result.items() if c}


def particle_hole(mask, r, q, root):
    new_mask, sign = 0, 1
    spectators = [a for a in range(r) if a not in (root, root + 1)]
    ordered = [root, root + 1] + spectators
    new_rank = {a: rank for rank, a in enumerate(ordered)}
    for column in range(q):
        original = [a for a in range(r) if mask & (1 << (column * r + a))]
        inversions = sum(new_rank[a] > new_rank[b] for j, a in enumerate(original) for b in original[j + 1:])
        sign *= (-1) ** inversions
        pair_offset = column * (r - 1)
        root_state = int(root in original) + 2 * int(root + 1 in original)
        new_root_state = {0: 1, 1: 0, 2: 3, 3: 2}[root_state]
        new_mask |= new_root_state << (2 * pair_offset)
        for index, spectator in enumerate(spectators, start=1):
            singleton = 2 if spectator in original else 1
            new_mask |= singleton << (2 * (pair_offset + index))
    return new_mask, sign


def exterior_lefschetz(mask, pairs, raise_degree):
    result = defaultdict(int)
    for pair in range(pairs):
        e, f = 2 * pair, 2 * pair + 1
        operations = [(f, True), (e, True)] if raise_degree else [(e, False), (f, False)]
        term = compose_elementary(mask, operations)
        if term:
            result[term[0]] += term[1]
    return {m: c for m, c in result.items() if c}


def run():
    records = []
    for r in range(2, 5):
        for q in range(1, 4):
            for root in range(r - 1):
                images = set()
                for mask in range(1 << (r * q)):
                    target_mask, sign = particle_hole(mask, r, q, root)
                    assert target_mask not in images
                    images.add(target_mask)
                    for lower in (True, False):
                        left = defaultdict(int)
                        for domain_mask, coefficient in row_operator(mask, r, q, root, lower).items():
                            image_mask, image_sign = particle_hole(domain_mask, r, q, root)
                            left[image_mask] += coefficient * image_sign
                        left = {m: c for m, c in left.items() if c}
                        right = {m: sign * c for m, c in exterior_lefschetz(target_mask, (r - 1) * q, lower).items()}
                        assert left == right, (r, q, root, mask, lower, left, right)
                records.append({"r": r, "q": q, "simple_root_one_based": root + 1,
                                "basis_vectors_checked": 1 << (r * q), "status": "passed"})
    print(json.dumps({"independent_signed_exterior_check": records,
                      "basis_vectors_total": sum(x["basis_vectors_checked"] for x in records),
                      "intertwining_identities_total": 2 * sum(x["basis_vectors_checked"] for x in records)}, indent=2))


if __name__ == "__main__":
    run()
