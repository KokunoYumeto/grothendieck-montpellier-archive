"""Independently evaluate the public six-AND construction in senegrom's PR 1350."""

from itertools import combinations
from pathlib import Path
import json


edges=[(0,4),(0,7),(0,8),(0,9),(1,5),(1,8),(1,10),(2,6),(2,9),(2,10),
       (3,7),(3,10),(4,10),(5,8),(6,9),(7,9)]
rows=[
    ([4],[],[0,10],[]),([5],[0],[1,8],[]),([8,10],[],[0,1],[1]),
    ([9],[2],[2,7],[1]),([7,10],[2,3],[3],[3]),([6],[2,4],[2,9],[4]),
]


def candidate(x):
    gates=[]
    for lv,lg,rv,rg in rows:
        a=any((x>>i)&1 for i in lv) or any(gates[i] for i in lg)
        b=any((x>>i)&1 for i in rv) or any(gates[i] for i in rg)
        gates.append(a and b)
    return any(gates[i] for i in [0,1,4,5])


def edge(x):
    return any((x>>a)&(x>>b)&1 for a,b in edges)


def main():
    vertices=range(11)
    all_inputs=range(1<<11)
    maximal=[x for x in all_inputs if not edge(x)
             and all((x>>i)&1 or edge(x|(1<<i)) for i in vertices)]
    covered=[(x,i) for x in maximal for i in vertices if not ((x>>i)&1)]
    assert all(not candidate(x) for x in maximal)
    assert all(candidate(x|(1<<i)) for x,i in covered)
    tau=11-max(x.bit_count() for x in maximal)
    neighbors=[{b if a==i else a for a,b in edges if i in (a,b)} for i in vertices]
    assert all(len(neighbors[i]&neighbors[j])<2 for i,j in combinations(vertices,2))
    bad=sorted((x for x in all_inputs if bool(candidate(x))!=edge(x)),key=lambda x:(x.bit_count(),x))
    assert tau==7 and len(maximal)==24 and len(covered)==170
    witness=[i for i in vertices if (bad[0]>>i)&1]
    result={"source":"https://github.com/brilliant-hq/pequalnp-proofs/pull/1350",
            "vertices":11,"edges":16,"triangle":[0,7,9],"cover_number":tau,"and_gates":len(rows),
            "maximal_independent_sets":len(maximal),"pointed_extensions":len(covered),
            "full_table_inputs":2048,"wrong_inputs":len(bad),"first_wrong_support":witness,
            "expected":edge(bad[0]),"actual":bool(candidate(bad[0]))}
    Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2),encoding="utf8")
    print(result)


if __name__=="__main__":
    main()
