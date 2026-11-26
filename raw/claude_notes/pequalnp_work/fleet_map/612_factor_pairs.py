"""Exact intersection-of-two-single-level-factors test for the 3-path theta graph."""
import itertools
import json
import time
import argparse
from collections import Counter
from pathlib import Path


def prefix_costs():
    masks = [m for m in range(1,16) if m.bit_count() >= 2]
    code = {m: 1 << i for i,m in enumerate(masks)}
    reachable = {0}
    for state in range(1 << len(masks)):
        if state not in reachable:
            continue
        known = [1,2,4,8] + [m for m in masks if state & code[m]]
        for a,b in itertools.combinations(known,2):
            reachable.add(state | code[a|b])
    best = [min(s.bit_count() for s in reachable if s & goal == goal)
            for goal in range(1 << len(masks))]
    return code,best


def solve_factor_pair(a, b, rects, costs, limit):
    demand = a | (b << 16)
    items = []
    for r,mask,lc,rc in rects:
        cover = (mask if not mask & ~a else 0) | ((mask << 16) if not mask & ~b else 0)
        if cover:
            items.append((r,mask,lc,rc,cover))
    byreq = [[i for i,item in enumerate(items) if item[-1] >> bit & 1] for bit in range(32)]
    best = limit + 1
    leaves = 0
    visited = 0

    def search(remaining, lc, rc, chosen, blocked):
        nonlocal best, leaves, visited
        visited += 1
        d = len(chosen)
        partial = 2*d-1 + costs[lc] + costs[rc]
        if partial >= best or partial > limit:
            return
        if not remaining:
            leaves += 1
            disjoint = False
            for partition in range(1 << d):
                ga = gb = 0
                for j,i in enumerate(chosen):
                    if partition >> j & 1: ga |= items[i][1]
                    else: gb |= items[i][1]
                if ga == a and gb == b:
                    disjoint = True
                    break
            best = min(best, partial + int(not disjoint))
            return
        if partial + 2 >= best or partial + 2 > limit:
            return
        available = None
        todo = remaining
        while todo:
            bit = (todo & -todo).bit_length()-1
            bucket = [i for i in byreq[bit] if not blocked >> i & 1 and
                      2*d+1 + costs[lc|items[i][2]] + costs[rc|items[i][3]] < best]
            if not bucket:
                return
            if available is None or len(bucket) < len(available):
                available = bucket
            todo ^= 1 << bit
        available.sort(key=lambda i: (-(remaining & items[i][-1]).bit_count(), items[i][0]))
        for i in available:
            _,_,li,ri,cover = items[i]
            search(remaining & ~cover, lc|li, rc|ri, chosen+(i,), blocked)
            blocked |= 1 << i
    search(demand,0,0,(),0)
    return best,leaves,visited


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=11)
    args = parser.parse_args()
    limit = args.limit
    start = time.perf_counter()
    left,right = (0,5,6,7),(1,2,3,4)
    theta = {(0,2+i) for i in range(3)} | {(2+i,5+i) for i in range(3)} | {(1,5+i) for i in range(3)}
    target = sum(1 << (4*i+j) for i,x in enumerate(left) for j,y in enumerate(right)
                 if tuple(sorted((x,y))) in theta)
    missing = [bit for bit in range(16) if not target >> bit & 1]
    prefix,costs = prefix_costs()
    rectangles = []
    for rows,cols in itertools.product(range(1,16),repeat=2):
        edges = sum(1 << (4*i+j) for i in range(4) for j in range(4)
                    if rows >> i & 1 and cols >> j & 1)
        rectangles.append(((rows,cols), edges,prefix.get(rows,0),prefix.get(cols,0)))
    vertex_truth = [sum(1 << w for w in range(256) if w >> i & 1) for i in range(8)]
    truths = {}
    for extra in range(1 << len(missing)):
        mask = target | sum(1<<bit for i,bit in enumerate(missing) if extra>>i&1)
        truth = 0
        for i in range(4):
            for j in range(4):
                if mask >> (4*i+j)&1: truth |= vertex_truth[left[i]] & vertex_truth[right[j]]
        truths[mask] = truth
    valid,leaves,visited = 0,0,0
    histogram = Counter()
    for a,b in itertools.combinations((m for m in truths if m!=target),2):
        if a & b != target: continue
        red = [divmod(i,4) for i in range(16) if a&~target & (1<<i)]
        blue = [divmod(i,4) for i in range(16) if b&~target & (1<<i)]
        cross = all(target & ((1<<(4*i+l))|(1<<(4*k+j))) for i,j in red for k,l in blue)
        assert bool(cross) == (truths[a]&truths[b] == truths[target])
        if not cross: continue
        valid += 1
        best, nl, nv = solve_factor_pair(a,b,rectangles,costs,limit)
        leaves += nl
        visited += nv
        histogram[best if best <= limit else f"above_{limit}"] += 1
        if time.perf_counter()-start > 70:
            raise TimeoutError("70-second standalone budget exceeded")
    results = {"vertices":8,"edges":9,"strict_supergraphs":127,"valid_unordered_factor_pairs":valid,
               f"threshold_{limit}_results":dict(histogram),"search_nodes":visited,"completed_relaxed_covers":leaves,
               "checked_input_assignments":256,"elapsed_seconds":round(time.perf_counter()-start,3)}
    print(results)
    output = Path(__file__).with_suffix(".json") if limit == 11 else Path(__file__).with_name(f"612_factor_pairs_at{limit}.json")
    output.write_text(json.dumps(results,indent=2),"utf-8")
