"""Check finite witnesses and truth tables for the circuit literature cross-references."""

from itertools import combinations, product
import json
from pathlib import Path

import networkx as nx


def hazard_indicator(op, a, b, x, y):
    if op == min:
        return ((x and y), x, y, (x or y))[2*a+b]
    return ((x or y), y, x, (x and y))[2*a+b]


def read_hazard(circuit, inputs):
    wires = list(inputs)
    for op, i, j in circuit:
        x = wires[i]
        y = wires[j]
        wires.append(2-x if op == 'not' else min(x,y) if op == 'and' else max(x,y))
    return wires[-1]


def theta_reduction():
    k = nx.Graph()
    for path in [[0, 1], [0, 2, 3, 4, 5, 6, 1], [0, 7, 8, 9, 10, 11, 1]]:
        nx.add_path(k, path)
    cover = {0,1,3,5,8,10}
    matching = [(0,2),(3,4),(5,6),(7,8),(9,10),(11,1)]
    assert all(k.has_edge(i,j) for i,j in matching) and len({v for e in matching for v in e}) == 12
    assert all(u in cover or v in cover for u,v in k.edges)
    cycle_lengths = sorted(len(c) for c in nx.simple_cycles(k))
    assert cycle_lengths == [7,7,12]
    edges = list(k.edges) + [(12,3)]
    stars = {c:[] for c in cover}
    for u,v in edges:
        center = u if u in cover else v
        stars[center].append(v if center == u else u)
    assert all(stars.values())
    for word in range(1<<13):
        def bit(v):
            return (word>>v)&1
        assert any(bit(u) and bit(v) for u,v in edges) == any(
            bit(c) and any(bit(v) for v in vs) for c,vs in stars.items())
    return {'edges_added':len(edges),'cover_increment':len(cover),
            'extension_gates':len(edges)+len(cover),'cycle_lengths':cycle_lengths,'assignments':1<<13}


def check():
    for op in [min,max]:
        for a,b,x,y in product(range(2),repeat=4):
            unknown = op(1 if x else 2*a,1 if y else 2*b) == 1
            assert bool(hazard_indicator(op,a,b,x,y)) == unknown
    # f(z,t)=z OR (t AND NOT t) agrees with z on every Boolean input.
    circuit = [('not',1,1),('and',1,2),('or',0,3)]
    for z,t in product([0,2],repeat=2):
        assert read_hazard(circuit,[z,t]) == z
    assert read_hazard(circuit,[0,1]) == 1
    tested = saturated = 0
    for g in nx.graph_atlas_g():
        if g.number_of_nodes() < 2:
            continue
        if any(len(set(g[u])&set(g[v]))>1 for u,v in combinations(g,2)):
            continue
        tested += 1
        stable_triple = any(all(not g.has_edge(u,v) for u,v in combinations(t,2)) for t in combinations(g,3))
        if not stable_triple:
            saturated += 1
            assert len(g) <= 6
    return {'gate_truth_table_cases':32,'Boolean_witness_assignments':4,'verified_hazard_input':['0','unknown'],
            'C4_free_atlas_graphs_order_2_through_7':tested,'among_them_with_no_independent_triple':saturated,
            'theta':theta_reduction(),'mandatory_unstable_lines':{'PG(2,8), B<=291':73-291//8,'PG(2,7), B<=69':57-69//7}}


if __name__ == '__main__':
    result = check()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
