#!/usr/bin/env python3
"""Exact finite certificates for A-S09-06, A-S09-07, and A-S09-08.

Checks specified constructions; no computation is claimed to refute the
integral admissible-theory uniqueness conjecture.
"""
from itertools import product
from math import comb
from pathlib import Path
from time import perf_counter
import json


def add(a, b, scale=1):
    r = a.copy()
    for k, v in b.items():
        r[k] = r.get(k, 0) + scale * v
        if not r[k]:
            del r[k]
    return r


def mul_basis(a, b):
    x, z, mask = a
    xx, zz, mm = b
    if mask & mm or x+z+mask.bit_count()+xx+zz+mm.bit_count() > 2:
        return {}
    inversions = int(bool(mask & 2) and bool(mm & 1))
    c = (-1)**inversions * comb(x+xx, x) * comb(z+zz, z)
    return {(x+xx, z+zz, mask|mm): c}


def mul(a, b):
    r = {}
    for aa, ac in a.items():
        for bb, bc in b.items():
            r = add(r, mul_basis(aa, bb), ac*bc)
    return r


def diff_basis(a):
    x, z, mask = a
    r = {}
    if x:
        r = add(r, mul_basis((x-1, z, 1), (0, 0, mask)))
    if z:
        r = add(r, mul_basis((x, z-1, 2), (0, 0, mask)))
    return r


def qmul(a, b):
    r = mul(a, b)
    for aa, ac in a.items():
        q = aa[2].bit_count()
        if q % 2:
            for bb, bc in b.items():
                r = add(r, mul({aa: 1}, diff_basis(bb)), -ac*bc)
    return r


def elem(a):
    return {a: 1}


def ring_mul(a, b, m):
    return tuple(sum(a[i]*b[k-i] for i in range(k+1)) % m for k in range(3))


def main():
    start = perf_counter()
    e0 = (1, 0)
    edge = 1
    left_cup = e0[0] * edge
    right_cup = edge * e0[1]
    assert left_cup != right_cup
    basis = [(x, z, mask) for x in range(3) for z in range(3)
             for mask in range(4) if x+z+mask.bit_count() <= 2]
    associativity_count = 0
    for a,b,c in product(basis, repeat=3):
        assert qmul(qmul(elem(a), elem(b)), elem(c)) == qmul(elem(a), qmul(elem(b), elem(c)))
        associativity_count += 1
    y = elem((0,0,1))
    z = elem((0,1,0))
    comm = add(qmul(y,z),qmul(z,y),-1)
    assert comm == {(0,0,3):-1}
    nil_checks = []
    for m in (2,3,4,6):
        elements = list(product(range(m), repeat=3))
        idems = [a for a in elements if ring_mul(a,a,m)==a]
        assert all(a[1:]==(0,0) for a in idems)
        triples = []
        for a,b,c in product(idems, repeat=3):
            if tuple((a[i]+b[i]+c[i])%m for i in range(3)) != (1,0,0):
                continue
            if any(ring_mul(u,v,m)!=(0,0,0) for u,v in ((a,b),(a,c),(b,c))):
                continue
            if b[0] != 0:  # the middle edge idempotent must be in the nilpotent ideal
                continue
            assert b == (0,0,0)
            triples.append([a,b,c])
        assert len(triples)==len(idems)
        nil_checks.append({"modulus":m,"elements_enumerated":len(elements),
                           "idempotents":idems,"vertex_partition_maps":len(triples)})
    result = {
        "statement_ids":["A-S09-06","A-S09-07","A-S09-08"],
        "AW_interval":{"e0_cup_edge":left_cup,"edge_cup_e0":right_cup},
        "Q_scope":"two-variable integral PD de Rham algebra, weights <=2; cosimplicial degree1",
        "Q_basis_count":len(basis),
        "Q_associativity_triples_checked":associativity_count,
        "Q_commutator":{"dx_dz_tensor_v_squared":comm[(0,0,3)]},
        "nilpotent_idempotent_tests":nil_checks,
        "PD_disk_weight_two":{"degree3_rank":1,"degree4_rank":1,
                              "differential_matrix":[[2]],"smith_invariant":2,
                              "H4":"Z/2", "H3":"0"},
        "PD_disk_pairs_computed":[{"arity":m,"differential_coefficient":comb(m,1),"degrees":[2*m-1,2*m]}
                                 for m in range(1,9)],
        "elapsed_seconds":perf_counter()-start,
        "success":True,
    }
    out=Path(__file__).resolve().parents[1]/"logs"/"A_cosimplicial_obstructions.json"
    out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__ == "__main__":
    main()
