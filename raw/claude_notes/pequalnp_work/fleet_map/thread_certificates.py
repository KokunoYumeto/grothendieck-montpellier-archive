"""Check the fleet's six-degree-two-vertices condition using one forest test."""

from itertools import combinations
import json
from pathlib import Path
import random

import networkx as nx


def thread_certificate(graph, length=6):
    two = graph.subgraph(v for v, degree in graph.degree if degree == 2)
    cuts = []
    for component in nx.connected_components(two):
        if len(component) >= length:
            v = min(component)
            cuts.append((v, min(graph[v])))
    rest = graph.copy()
    rest.remove_edges_from(cuts)
    return cuts, not rest or nx.is_forest(rest)


def by_cycles(graph, length):
    for cycle in nx.simple_cycles(graph):
        if len(cycle) < length:
            return False
        if not any(all(graph.degree[cycle[(i+j) % len(cycle)]] == 2 for j in range(length))
                   for i in range(len(cycle))):
            return False
    return True


def min_cover(graph):
    for size in range(len(graph)+1):
        for vertices in combinations(graph.nodes, size):
            cover = set(vertices)
            if all(u in cover or v in cover for u, v in graph.edges):
                return sorted(cover)


def main():
    fleet_edges = [(0,1),(0,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,1),(0,8),(1,9)]
    graph = nx.Graph(fleet_edges)
    cuts, valid = thread_certificate(graph)
    cover = min_cover(graph)
    matching = [(0,8),(1,9),(2,3),(4,5),(6,7)]
    assert valid and len(cover)==5 and len({v for edge in matching for v in edge})==10
    assert all(graph.has_edge(u,v) for u,v in matching)
    count = 0
    for g in nx.graph_atlas_g():
        for k in (2,4,6):
            assert thread_certificate(g,k)[1] == by_cycles(g,k)
            count += 1
    rng = random.Random(756)
    for _ in range(80):
        core = nx.gnp_random_graph(6, 0.38, seed=rng)
        g = nx.Graph()
        g.add_nodes_from(core)
        for u,v in core.edges:
            fresh = list(range(len(g),len(g)+rng.choice((0,2,5,6,7))))
            nx.add_path(g, [u,*fresh,v])
        assert thread_certificate(g)[1] == by_cycles(g,6)
        count += 1
    report={"criterion_comparisons":count,"L-meta-518":{
        "edges":fleet_edges,"cut_edges":cuts,"cycle_path":[2,3,4,5,6,7],
        "minimum_cover":cover,"disjoint_edges":matching,"gate_lower_bound":len(fleet_edges)+len(cover)-1}}
    dest=Path(__file__).with_name("thread_certificates.json")
    dest.write_text(json.dumps(report,indent=2),encoding="utf8")
    print(json.dumps(report))


if __name__=="__main__":
    main()
