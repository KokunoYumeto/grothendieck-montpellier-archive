#!/usr/bin/env python3
"""Independent direct multigraph enumeration for A4.5 positive cases.

Unlike the root's inverse-contraction generator, enumerate all multigraphs
with the proven stable vertex/edge bounds, all genera and all labelled-leg
placements. Canonicalize by every vertex permutation, then compute direct
edge contractions and all common-refinement minima.
"""
from itertools import product, permutations, combinations_with_replacement, combinations
from time import perf_counter
import json

def canonical(genera, legs, edges):
    v=len(genera)
    variants=[]
    for order in permutations(range(v)):
        remap={old:new for new,old in enumerate(order)}
        variants.append((tuple(genera[x] for x in order),tuple(legs[x] for x in order),tuple(sorted(tuple(sorted((remap[a],remap[b]))) for a,b in edges))))
    return min(variants)

def connected(v,edges):
    reach={0}
    for _ in range(v):
        for a,b in edges:
            if a in reach: reach.add(b)
            if b in reach: reach.add(a)
    return len(reach)==v

def enumerate_graphs(g,n):
    found=set(); candidates=0
    for v in range(1,2*g-2+n+1):
        slots=list(combinations_with_replacement(range(v),2))
        for e in range(v-1,3*g-3+n+1):
            vertex_genus=g-e+v-1
            if vertex_genus<0: continue
            for edges in combinations_with_replacement(slots,e):
                if not connected(v,edges): continue
                for gs in product(range(vertex_genus+1),repeat=v):
                    if sum(gs)!=vertex_genus: continue
                    for placement in product(range(v),repeat=n):
                        ls=[0]*v
                        for label,vertex in enumerate(placement):ls[vertex] |= 1<<label
                        deg=[x.bit_count() for x in ls]
                        for a,b in edges:deg[a]+=1;deg[b]+=1
                        candidates+=1
                        if all(2*gs[a]-2+deg[a]>0 for a in range(v)):
                            found.add(canonical(gs,ls,edges))
    return found,candidates

def direct_contractions(G):
    gs,ls,es=G;v=len(gs)
    result=set()
    for k,(a,b) in enumerate(es):
        edges=[edge for j,edge in enumerate(es) if j!=k]
        if a==b:
            genera=list(gs);genera[a]+=1
            result.add(canonical(genera,ls,edges))
        else:
            blocks=[{a,b}]+[{x} for x in range(v) if x!=a and x!=b]
            remap={old:new for new,block in enumerate(blocks) for old in block}
            genera=[sum(gs[x] for x in block) for block in blocks]
            legs=[sum(ls[x] for x in block) for block in blocks]
            result.add(canonical(genera,legs,[(remap[x],remap[y]) for x,y in edges]))
    return result

def check(g,n,expected):
    t0=perf_counter();graphs,candidates=enumerate_graphs(g,n)
    assert len(graphs)==expected,(g,n,len(graphs),expected)
    contractions={}
    for G in sorted(graphs,key=lambda z:len(z[2])):
        contractions[G]={G}
        for H in direct_contractions(G):
            assert H in graphs
            contractions[G] |= contractions[H]
    pairs=0;compatible=0;failures=[]
    for G,H in combinations(graphs,2):
        pairs+=1
        common={K for K in graphs if G in contractions[K] and H in contractions[K]}
        if not common:continue
        compatible+=1
        minimal={K for K in common if not ((contractions[K]-{K})&common)}
        if len(minimal)!=1:failures.append((G,H,len(minimal)))
    assert not failures,failures
    output={'g':g,'n':n,'candidates':candidates,'graphs':len(graphs),'pairs':pairs,'compatible_pairs':compatible,'failures':0,'runtime_seconds':round(perf_counter()-t0,6)}
    print(json.dumps(output))

if __name__=='__main__':
    for g,n,count in [(1,1,2),(1,2,5),(1,3,23),(2,0,7)]:check(g,n,count)
