"""A102: literal rational raising-kernel traces for the T067 normal modules.

The independent side constructs monomial spaces, simple raising matrices,
rational highest kernels and the actual block-permutation action.
Only the final comparison calls the author's Weyl/cycle formula.
"""
from pathlib import Path
from functools import lru_cache
from itertools import product
import hashlib
import importlib.util
import json
import sys
import sympy as sp

HERE = Path(__file__).resolve().parent
THEIR = HERE.parent / "theta" / "unstable_hook" / "all_fixed_order_hook_positive.py"


def partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    if maximum is None:
        maximum = n
    for first in range(min(n, maximum), 0, -1):
        for tail in partitions(n-first, first):
            yield (first,) + tail


@lru_cache(None)
def weak_compositions(n, q):
    if q == 0:
        return ((),) if n == 0 else ()
    return tuple((v,) + tail for v in range(n+1)
                 for tail in weak_compositions(n-v, q-1))


@lru_cache(None)
def weight_basis(q, k, weight):
    """q rows, q columns, row sums < k, prescribed column sums."""
    if any(v < 0 for v in weight):
        return ()
    rows = tuple(v for n in range(k) for v in weak_compositions(n, q))
    answer = []

    def extend(prefix, left, remaining):
        if remaining == 0:
            if not any(left):
                answer.append(tuple(prefix))
            return
        for row in rows:
            if all(row[j] <= left[j] for j in range(q)):
                new = tuple(left[j]-row[j] for j in range(q))
                if sum(new) <= (remaining-1)*(k-1):
                    extend(prefix + list(row), new, remaining-1)

    extend([], tuple(weight), q)
    return tuple(answer)


def cycle_permutation(cycles):
    p = list(range(sum(cycles)))
    start = 0
    for length in cycles:
        for j in range(length):
            p[start+j] = start+(j+1) % length
        start += length
    return tuple(p)


def literal_case(q, k, shape):
    weight = shape + (0,)*(q-len(shape))
    basis = weight_basis(q, k, weight)
    column_index = {v:i for i,v in enumerate(basis)}
    targets = []
    for j in range(q-1):
        w = list(weight)
        w[j] += 1
        w[j+1] -= 1
        targets.append(weight_basis(q, k, tuple(w)))
    offsets = []
    total_rows = 0
    for target in targets:
        offsets.append(total_rows)
        total_rows += len(target)
    raising = sp.zeros(total_rows, len(basis))
    for j, target in enumerate(targets):
        row_index = {v:i for i,v in enumerate(target)}
        for col, exponent in enumerate(basis):
            for row in range(q):
                pos = row*q+j+1
                coefficient = exponent[pos]
                if coefficient:
                    changed = list(exponent)
                    changed[pos] -= 1
                    changed[pos-1] += 1
                    raising[offsets[j]+row_index[tuple(changed)], col] += coefficient
    null = raising.nullspace()
    highest = sp.Matrix.hstack(*null) if null else sp.zeros(len(basis), 0)
    assert raising*highest == sp.zeros(total_rows, highest.cols)
    if highest.cols:
        pivot_rows = highest.T.rref()[1]
        small = highest.extract(pivot_rows, range(highest.cols))
        inverse = small.inv()
    else:
        pivot_rows, inverse = (), sp.zeros(0, 0)
    traces = {}
    for cycles in partitions(q):
        perm = cycle_permutation(cycles)
        moved = sp.zeros(*highest.shape)
        for old, exponent in enumerate(basis):
            new = [0]*(q*q)
            for row in range(q):
                new[perm[row]*q:(perm[row]+1)*q] = exponent[row*q:(row+1)*q]
            new_index = column_index[tuple(new)]
            for j in range(highest.cols):
                moved[new_index, j] = highest[old, j]
        action = inverse*moved.extract(pivot_rows, range(highest.cols))
        assert highest*action == moved
        tr = sp.trace(action)
        assert tr.q == 1
        traces[",".join(map(str,cycles))] = int(tr)
    checksum = hashlib.sha256(
        repr((raising.tolist(), highest.tolist(), traces)).encode()
    ).hexdigest()
    return {
        "q":q, "k":k, "rho":list(shape), "weight_dimension":len(basis),
        "raising_rows":total_rows, "highest_dimension":highest.cols,
        "traces":traces, "matrix_and_kernel_sha256":checksum
    }


def main():
    spec = importlib.util.spec_from_file_location("their_hook_normal", THEIR)
    their = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(their)
    cases = []
    trace_count = 0
    for q in range(1,4):
        for k in range(1,5):
            local_count = 0
            for degree in range(q*(k-1)+1):
                for rho in partitions(degree):
                    if len(rho) > q:
                        continue
                    record = literal_case(q,k,rho)
                    for cycles in partitions(q):
                        got = record["traces"][",".join(map(str,cycles))]
                        expected = their.normal_trace(q,k,rho,cycles)
                        assert got == expected, (q,k,rho,cycles,got,expected)
                        trace_count += 1
                    cases.append(record)
                    local_count += 1
            print("literal normal highest kernels",q,k,local_count,"PASS",flush=True)
    receipt = {
        "statement":"A-102 / T-067",
        "outcome":"PASS",
        "independent_method":"Exact rational kernels of simple raising matrices; actual tensor-block permutation matrices restricted to those kernels. No Weyl formula, character average or author's polynomial states on the independent side.",
        "cases":len(cases), "cycle_traces":trace_count,
        "total_weight_dimension":sum(c["weight_dimension"] for c in cases),
        "total_highest_dimension":sum(c["highest_dimension"] for c in cases),
        "largest_weight_space":max(c["weight_dimension"] for c in cases),
        "details":cases
    }
    (HERE/"HOOK_NORMAL_HIGHEST_SPACE_RECEIPT.json").write_text(
        json.dumps(receipt,indent=2)+"\n"
    )
    print(json.dumps({k:v for k,v in receipt.items() if k!="details"},indent=2))


if __name__ == "__main__":
    main()
