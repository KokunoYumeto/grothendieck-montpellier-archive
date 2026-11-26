#!/usr/bin/env python3
"""Independent concrete checks in the exact charged-gate semantics. No dependencies."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path

N = 12
EDGES = ((0,1),(0,2),(2,3),(3,4),(4,5),(5,6),(6,1),
         (0,7),(7,8),(8,9),(9,10),(10,11),(11,1))
WITNESS = [
    ["OR",1,2],["OR",12,7],["AND",0,13],
    ["OR",6,11],["AND",1,15],["OR",2,4],
    ["AND",3,17],["OR",4,6],["AND",5,19],
    ["OR",7,9],["AND",8,21],["OR",9,11],
    ["AND",10,23],["OR",14,16],["OR",18,20],
    ["OR",22,24],["OR",25,26],["OR",28,27]]
MATCHING = ((0,2),(3,4),(5,6),(7,8),(9,10),(11,1))

def edge_value(mask, edges=EDGES):
    return any((mask & (1 << u)) and (mask & (1 << v)) for u,v in edges)

def circuit_value(gates, output, mask, n=N):
    """Future/out-of-range reads are false AT THE TIME of gate evaluation."""
    wires = [bool(mask & (1 << i)) for i in range(n)]
    for row in gates:
        op, *args = row
        assert op in ("AND","OR","NOT") and len(args) <= 2
        assert all(isinstance(i,int) and i >= 0 for i in args)
        bits = [wires[i] if i < len(wires) else False for i in args]
        if op == "AND": value = all(bits)
        elif op == "OR": value = any(bits)
        else: value = not (bits[0] if bits else False)
        wires.append(value)
    return wires[output] if 0 <= output < len(wires) else False

def bitparallel_value(gates, output, n=N):
    """Independent evaluator: whole truth tables as integer bit vectors."""
    all_rows = (1 << (1 << n)) - 1
    tables = [sum(1 << s for s in range(1 << n) if (s >> i) & 1) for i in range(n)]
    for op,*operands in gates:
        values = [tables[i] if i < len(tables) else 0 for i in operands]
        if op == "NOT": z = all_rows ^ (values[0] if values else 0)
        elif op == "AND":
            z = all_rows
            for v in values: z &= v
        else:
            z = 0
            for v in values: z |= v
        tables.append(z)
    return tables[output] if output < len(tables) else 0

def compact_hash(rows):
    return hashlib.sha256(json.dumps(rows,separators=(",",":")).encode("ascii")).hexdigest()

def verify():
    target = [bool(edge_value(s)) for s in range(1 << N)]
    evaluated = [circuit_value(WITNESS,29,s) for s in range(1 << N)]
    assert evaluated == target
    expected_bits = sum(1 << s for s,t in enumerate(target) if t)
    assert bitparallel_value(WITNESS,29) == expected_bits
    bad = [r[:] for r in WITNESS]
    bad[0][0] = "AND"
    mismatches = [s for s,t in enumerate(target) if circuit_value(bad,29,s) != t]
    assert mismatches
    assert compact_hash(WITNESS) == "6ba6850d53d9ab84cbdc7422e055314cf4464e57d08ea1ff5aa80ec0b09e0cf7"
    independent = [s for s,t in enumerate(target) if not t]
    maximal = [s for s in independent if all(target[s | (1 << v)] for v in range(N) if not (s >> v)&1)]
    covers = [(1 << N)-1-s for s in independent]
    tau = min(s.bit_count() for s in covers)
    minimum_covers = [s for s in covers if s.bit_count()==tau]
    assert tau==6 and minimum_covers==[1323]
    assert len(set(itertools.chain.from_iterable(MATCHING)))==12
    assert all(frozenset(e) in {frozenset(e) for e in EDGES} for e in MATCHING)
    # Semantics whose omission would change the project's circuit model.
    assert circuit_value([["AND"]],0,0,0)
    assert not circuit_value([["OR"]],0,0,0)
    assert circuit_value([["NOT"]],0,0,0)
    assert circuit_value([["NOT",2],["AND"]],0,0,0)
    assert not circuit_value([["OR",1],["AND"]],0,0,0)
    assert circuit_value([["NOT",0,1]],2,2,2)
    assert not circuit_value([],999,0,2)
    assert circuit_value([["OR",0,0]],2,1,2)
    assert (sum(target),len(independent),len(maximal)) == (3799,297,27)
    return dict(status="PASS",assignments=4096,true_rows=sum(target),false_rows=len(independent),
                maximal_independent_masks=maximal,minimum_cover_masks=minimum_covers,
                vertex_cover_number=tau,matching=[list(e) for e in MATCHING],
                witness_gates=18,witness_output=29,witness_sha256=compact_hash(WITNESS),
                negative_control=dict(change="gate 12 OR changed to AND",mismatches=len(mismatches),
                                      smallest_failing_mask=min(mismatches)),
                independent_evaluators=["scalar exact semantics","integer truth-table operations"],
                nonstandard_semantics_checks=8)

if __name__ == "__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--json",type=Path)
    args=ap.parse_args()
    result=verify()
    rendered=json.dumps(result,indent=2)+"\n"
    if args.json: args.json.write_text(rendered)
    print(rendered,end="")
