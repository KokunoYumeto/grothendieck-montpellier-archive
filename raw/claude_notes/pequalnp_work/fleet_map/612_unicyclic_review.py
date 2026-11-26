"""Census of rooted-tree decorations of even cycles on at most twelve vertices."""
from functools import lru_cache
from pathlib import Path
import json
import time


@lru_cache(None)
def rooted_trees(n):
    if n == 1:
        return ("()",)
    universe = sorted(tree for i in range(1, n) for tree in rooted_trees(i))
    ans = []

    def assemble(start, remaining, parts):
        if remaining == 0:
            ans.append("(" + "".join(parts) + ")")
        for j in range(start, len(universe)):
            tree = universe[j]
            size = len(tree) // 2
            if size <= remaining:
                assemble(j, remaining - size, parts + [tree])
    assemble(0, n - 1, [])
    return tuple(ans)


def decorations(cycle, extra):
    nontrivial = [(len(t)//2 - 1, t) for i in range(2, extra + 2) for t in rooted_trees(i)]
    canonical = set()

    def fill(path, remaining):
        if len(path) == cycle:
            if remaining:
                return
            reverse = path[::-1]
            key = min(t[i:] + t[:i] for t in (path, reverse) for i in range(cycle))
            canonical.add(key)
            return
        fill(path + ("()",), remaining)
        for cost, tree in nontrivial:
            if cost <= remaining:
                fill(path + (tree,), remaining - cost)
    fill((), extra)
    return sorted(canonical)


def graph_of(parts):
    cycle = len(parts)
    edges = [(i, (i + 1) % cycle) for i in range(cycle)]
    next_vertex = cycle
    for root, code in enumerate(parts):
        stack = [root]
        for token in code[1:-1]:
            if token == "(":
                edges.append((stack[-1], next_vertex))
                stack.append(next_vertex)
                next_vertex += 1
            else:
                stack.pop()
        assert stack == [root]
    return next_vertex, tuple(sorted(tuple(sorted(e)) for e in edges))


@lru_cache(None)
def cover(edges):
    if not edges:
        return 0
    # A cover must contain an endpoint of the first edge.
    return 1 + min(cover(tuple(e for e in edges if v not in e)) for v in edges[0])


def review(cycle, n, edges):
    core = set(range(cycle))
    start = cover(edges)
    m = len(edges)
    steps = charges = 0
    while edges:
        adj = {i:set() for i in range(n)}
        for a,b in edges:
            adj[a].add(b)
            adj[b].add(a)
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        if not leaves:
            assert len(edges) == cycle and cover(edges) == cycle//2
            assert m + start - 1 == charges + cycle + cycle//2 - 1
            return "cycle"
        if core:
            distances = {i:0 for i in core}
            wave = list(core)
            for v in wave:
                for u in adj[v]:
                    if u not in distances:
                        distances[u] = distances[v]+1
                        wave.append(u)
            u = max(leaves, key=distances.get)
        else:
            u = leaves[0]
        v, = adj[u]
        if v in core:
            core.clear()
        if core:
            children = {w for w in adj[v] if distances[w] > distances[v]}
            assert all(len(adj[w]) == 1 for w in children)
            assert len(adj[v]) == len(children)+1
            charges += len(children)+2
        remaining = tuple(e for e in edges if v not in e and u not in e)
        assert cover(edges) == 1 + cover(remaining)
        steps += 1
        edges = remaining
    assert start == steps
    return "forest"


if __name__ == "__main__":
    begin = time.perf_counter()
    census = {}
    for n in range(6,13):
        for cycle in range(6,n+1,2):
            row = {"cycle":0,"forest":0}
            for parts in decorations(cycle, n-cycle):
                size, edges = graph_of(parts)
                assert size == n
                row[review(cycle,n,edges)] += 1
            census[f"{n}/{cycle}"] = row
    totals = {regime:sum(row[regime] for row in census.values()) for regime in ["cycle","forest"]}
    result = {"total":sum(totals.values()),"by_regime":totals,"by_n_and_cycle":census,
              "seconds":round(time.perf_counter()-begin,3)}
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2), "utf-8")
    print(result)
