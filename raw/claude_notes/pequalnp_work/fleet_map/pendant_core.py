"""Test the cover identity underlying the rooted-forest reduction against exhaustive covers."""

from itertools import combinations
import json
from pathlib import Path
import networkx as nx


def cover_cost(graph, root=None, required=None):
    for n in range(len(graph)+1):
        for choice in combinations(graph, n):
            c=set(choice)
            if required is not None and (root in c)!=required:
                continue
            if all(a in c or b in c for a,b in graph.edges):
                return n
    raise AssertionError("No cover meeting the boundary condition")


def marked_core(graph):
    core=nx.k_core(graph,2)
    if not core or not nx.is_connected(graph):
        return None
    exterior=graph.copy()
    exterior.remove_edges_from(core.edges)
    marked=core.copy()
    active=[]
    forest_cost=0
    for vertices in nx.connected_components(exterior):
        roots=set(core).intersection(vertices)
        assert len(roots)==1
        r=roots.pop()
        tree=exterior.subgraph(vertices)
        assert nx.is_tree(tree)
        ca=cover_cost(tree,r,True)
        cb=cover_cost(tree,r,False)
        forest_cost+=min(ca,cb)
        if ca<=cb:
            active.append(r)
            marked.add_edge(r,("fresh",r))
    assert cover_cost(graph)==cover_cost(marked)+forest_cost-len(active)
    return {"n":len(graph),"edges":len(graph.edges),"cover":cover_cost(graph),
            "active_roots":sorted(active),"marked_core_cover":cover_cost(marked),
            "forest_cover":forest_cost,"forest_edges":len(exterior.edges)}


def main():
    count=sum(marked_core(g) is not None for g in nx.graph_atlas_g() if g)
    six=nx.cycle_graph(6)
    six.add_edges_from([(0,6),(2,7),(4,8)])
    case=marked_core(six)
    assert case["cover"]==3 and case["active_roots"]==[0,2,4]
    data={"connected_cyclic_atlas_graphs":count,"three_marked_vertices_on_C6":case}
    Path(__file__).with_suffix(".json").write_text(json.dumps(data,indent=2),encoding="utf8")
    print(data)


if __name__=="__main__":
    main()
