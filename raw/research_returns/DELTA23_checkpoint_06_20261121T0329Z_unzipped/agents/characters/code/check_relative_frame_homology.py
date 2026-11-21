#!/usr/bin/env python3
"""Rank97 relative homology covers of Q12 and exact torsion centralizers.

The full proof is the fixed-vertex boundary argument in D23.C12.  This code
constructs the quotient graph and independently solves every centralizer
lifting equation at p=2 and p=3.
"""
from collections import deque
import json
from pathlib import Path
import numpy as np


def canon(a):
    a=tuple(x%12 for x in a)
    return min(a,tuple(-x%12 for x in a))


def mm(a,b):
    return canon((a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],
                  a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]))


one=canon((1,0,0,1));s=canon((0,1,-1,0));r=canon((0,-1,1,-1))
group=[one];index={one:0};todo=deque([one])
while todo:
    a=todo.popleft()
    for b in [s,r]:
        c=mm(a,b)
        if c not in index:index[c]=len(group);group.append(c);todo.append(c)
assert len(group)==576
sidx,ridx=index[s],index[r]
r2=mm(r,r)
Scosets=[tuple(sorted([i,index[mm(g,s)]])) for i,g in enumerate(group)]
Rcosets=[tuple(sorted([i,index[mm(g,r)],index[mm(g,r2)]])) for i,g in enumerate(group)]
Sclasses=sorted(set(Scosets));Rclasses=sorted(set(Rcosets))
Si={v:i for i,v in enumerate(Sclasses)};Ri={v:len(Sclasses)+i for i,v in enumerate(Rclasses)}
edgeS=[Si[v] for v in Scosets];edgeR=[Ri[v] for v in Rcosets]
nvertices=len(Sclasses)+len(Rclasses)
assert (len(Sclasses),len(Rclasses),nvertices)==(288,192,480)
adj=[[] for _ in range(nvertices)]
for e,(a,b) in enumerate(zip(edgeS,edgeR)):
    adj[a].append((b,e,1));adj[b].append((a,e,-1))


def paths(root,p):
    parent={root:None};todo=deque([root]);chains={root:np.zeros(576,dtype=np.int16)};tree=set()
    while todo:
        v=todo.popleft()
        for w,e,sign in adj[v]:
            if w in parent:continue
            parent[w]=(v,e);tree.add(e);todo.append(w)
            chain=chains[v].copy();chain[e]=(chain[e]+sign)%p;chains[w]=chain
    assert len(parent)==nvertices
    chords=[e for e in range(576) if e not in tree]
    cycles=[]
    for e in chords:
        c=(chains[edgeS[e]]-chains[edgeR[e]])%p;c[e]=(c[e]+1)%p
        cycles.append(c)
    assert len(cycles)==97
    return chains,chords,cycles


def boundary(v,p):
    out=np.zeros(nvertices,dtype=np.int16)
    for e,a in enumerate(v):
        out[edgeS[e]]-=a;out[edgeR[e]]+=a
    return out%p


def span_basis(vectors,p):
    bs={}
    for raw in vectors:
        v=raw.copy()%p
        for pivot,b in sorted(bs.items()):
            if v[pivot]:v=(v-v[pivot]*b)%p
        nz=np.flatnonzero(v)
        if len(nz):
            pivot=int(nz[0]);v=v*pow(int(v[pivot]),-1,p)%p;bs[pivot]=v
    return bs


def belongs(v,bs,p):
    v=v.copy()%p
    for pivot,b in sorted(bs.items()):
        if v[pivot]:v=(v-v[pivot]*b)%p
    return not np.any(v)


out={"statement":"D23.C12","Q_order":576,"S_vertices":288,"R_vertices":192,
     "edges":576,"cycle_rank":97,"quotient_matrices":group,"checks":[]}
for p,a,base in [(2,s,edgeS[0]),(3,r,edgeR[0])]:
    perm=np.array([index[mm(a,g)] for g in group],dtype=np.int64)
    def act(v):
        ans=np.zeros(576,dtype=np.int16);ans[perm]=v;return ans
    chains,chords,cycles=paths(base,p)
    assert all(not np.any(boundary(c,p)) for c in cycles)
    assert len(span_basis(cycles,p))==97
    image_basis=span_basis([(act(c)-c)%p for c in cycles],p)
    centralizer=[i for i,b in enumerate(group) if mm(a,b)==mm(b,a)]
    allowed=[];checks=[]
    cp={0};cur=one
    for _ in range(1,p):cur=mm(cur,a);cp.add(index[cur])
    for bindex in centralizer:
        vertex=edgeS[bindex] if p==2 else edgeR[bindex]
        v=chains[vertex]
        rhs=(act(v)-v)%p
        liftable=belongs(rhs,image_basis,p)
        assert liftable==(bindex in cp)
        if liftable:allowed.append(bindex)
        checks.append({"q_index":bindex,"matrix":group[bindex],"liftable":liftable,
                       "target_vertex":vertex,"base_vertex":base})
    # Every edge orbit has p elements; invariant chains have boundary zero
    # at every fixed vertex.  Verify this directly on a basis of orbit sums.
    edge_orbits=[];seen=set()
    for e in range(576):
        if e in seen:continue
        orb=[];j=e
        while j not in orb:orb.append(j);seen.add(j);j=int(perm[j])
        assert len(orb)==p
        edge_orbits.append(orb)
    vperm={}
    for e in range(576):
        vperm[edgeS[e]]=edgeS[int(perm[e])];vperm[edgeR[e]]=edgeR[int(perm[e])]
    fixed=[v for v,w in vperm.items() if v==w]
    for orb in edge_orbits:
        c=np.zeros(576,dtype=np.int16);c[orb]=1
        assert not np.any(boundary(c,p)[fixed])
    record={"prime":p,"factor_generator":a,"centralizer_order_in_Q":len(centralizer),
            "centralizer_image_order_in_extension":len(allowed),
            "homology_rank":97,"rank_g_minus_1_on_homology":len(image_basis),
            "fixed_vertices":fixed,"free_edge_orbits":len(edge_orbits),
            "allowed_Q_indices":allowed,"chord_edges":chords,
            "centralizer_lift_checks":checks,"result":"PASS"}
    out["checks"].append(record)
    print(json.dumps({k:record[k] for k in ["prime","centralizer_order_in_Q","centralizer_image_order_in_extension","rank_g_minus_1_on_homology","result"]}),flush=True)


path=Path(__file__).resolve().parents[1]/"records"/"relative_frame_homology.json"
path.write_text(json.dumps(out,indent=2)+"\n")
print('certificate:',path,flush=True)
