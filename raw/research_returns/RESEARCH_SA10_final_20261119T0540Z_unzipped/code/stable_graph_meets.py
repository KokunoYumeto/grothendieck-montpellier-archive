#!/usr/bin/env python3
"""Enumerate stable graphs by all inverse single-edge contractions.

Vertices carry genera and masks of labelled legs; edges form an unordered
multiset and loops are allowed. Canonicalization checks every vertex
permutation. Output is a complete finite certificate within the listed (g,n).
"""
import itertools as it
import json, sys
from pathlib import Path
from time import perf_counter

def canon(gs,ls,es):
    v=len(gs); es=[tuple(sorted(e)) for e in es]
    best=None
    for p in it.permutations(range(v)):
        inv={old:new for new,old in enumerate(p)}
        key=(tuple(gs[i] for i in p),tuple(ls[i] for i in p),tuple(sorted(tuple(sorted((inv[a],inv[b]))) for a,b in es)))
        if best is None or key<best:best=key
    return best

def stable(G,g,n):
    gs,ls,es=G;v=len(gs)
    deg=[x.bit_count() for x in ls]
    for a,b in es:deg[a]+=1;deg[b]+=1
    if any(2*gs[a]-2+deg[a]<=0 for a in range(v)):return False
    if sum(gs)+len(es)-v+1!=g:return False
    if sum(ls)!=(1<<n)-1 or any(a&b for a,b in it.combinations(ls,2)):return False
    seen={0}
    while True:
        new=seen|{b for a,b in es if a in seen}|{a for a,b in es if b in seen}
        if new==seen:break
        seen=new
    return len(seen)==v

def expands(G):
    gs,ls,es=G;v=len(gs)
    for a in range(v):
        if gs[a]:
            gg=list(gs);gg[a]-=1
            yield canon(gg,ls,list(es)+[(a,a)])
        flags=[('e',k,q) for k,e in enumerate(es) for q,x in enumerate(e) if x==a]
        flags += [('l',k,0) for k in range(ls[a].bit_length()) if ls[a]>>k&1]
        for h in range(gs[a]+1):
            for mask in range(1<<len(flags)):
                deg1=mask.bit_count();deg0=len(flags)-deg1
                if 2*h-2+deg0+1<=0 or 2*(gs[a]-h)-2+deg1+1<=0:continue
                gg=list(gs)+[gs[a]-h];gg[a]=h
                ll=list(ls)+[0];ee=[list(e) for e in es]+[[a,v]]
                for j,f in enumerate(flags):
                    if not(mask>>j&1):continue
                    if f[0]=='e':ee[f[1]][f[2]]=v
                    else:ll[a]-=1<<f[1];ll[v]|=1<<f[1]
                yield canon(gg,ll,ee)

def contracts(G):
    gs,ls,es=G
    for k,(a,b) in enumerate(es):
        ee=es[:k]+es[k+1:]
        if a==b:
            gg=list(gs);gg[a]+=1
            yield canon(gg,ls,ee)
        else:
            gg=list(gs);ll=list(ls);gg[a]+=gg[b];ll[a]|=ll[b]
            del gg[b];del ll[b]
            remap=lambda x:a if x==b else x-1 if x>b else x
            yield canon(gg,ll,[(remap(x),remap(y)) for x,y in ee])

def run(g,n):
    t0=perf_counter();dim=3*g-3+n
    first=canon([g],[(1<<n)-1],[])
    levels=[{first}]
    for e in range(dim):
        nxt=set()
        for G in levels[-1]:nxt.update(expands(G))
        assert all(stable(G,g,n) for G in nxt)
        levels.append(nxt)
    graphs=sorted(set.union(*levels),key=lambda x:(len(x[2]),x))
    idx={G:k for k,G in enumerate(graphs)}
    below=[set() for G in graphs]
    ancestors=[]
    for k,G in enumerate(graphs):
        anc={k}
        for H in contracts(G):
            assert H in idx
            anc|=ancestors[idx[H]]
        ancestors.append(anc)
        for j in anc:below[j].add(k)
    bad=[];comparable=0;with_common=0
    for a,b in it.combinations(range(len(graphs)),2):
        common=below[a]&below[b]
        if not common:continue
        with_common+=1
        # Maximal lower bounds for reverse-contraction order = refinements
        # having no strictly smaller edge contraction still in common.
        maxs=[c for c in common if not ((ancestors[c]-{c})&common)]
        if len(maxs)>1:bad.append((a,b,maxs))
    report={'g':g,'n':n,'level_counts':[len(z) for z in levels], 'graph_count':len(graphs),'pairs_tested':len(graphs)*(len(graphs)-1)//2,'pairs_with_common_refinement':with_common,'failure_count':len(bad),'elapsed_seconds':perf_counter()-t0}
    if bad:
        witness=min(bad,key=lambda t:(max(len(graphs[t[0]][2]),len(graphs[t[1]][2])),sum(len(graphs[c][2]) for c in t[2]),t))
        report['witness']={'G':graphs[witness[0]],'H':graphs[witness[1]],'maximal_common_refinements':[graphs[c] for c in witness[2]]}
    print(json.dumps(report),flush=True)
    dest=Path(__file__).resolve().parent/'stable_graph_data';dest.mkdir(exist_ok=True)
    (dest/f'g{g}_n{n}.json').write_text(json.dumps({'report':report,'graphs':graphs,'contractions':[sorted(a) for a in ancestors],'failures':bad},indent=2))

if __name__=='__main__':
    tasks=[(0,3),(0,4),(0,5),(1,1),(1,2),(1,3),(1,4),(2,0),(2,1),(3,0)]
    if len(sys.argv)>1:tasks=[tuple(map(int,p.split(','))) for p in sys.argv[1:]]
    for g,n in tasks:run(g,n)
