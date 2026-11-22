#!/usr/bin/env python3
"""Build exact ternary-jet bracket polynomials, then select bases modulo 101.

Exploration/build tool using NumPy. Each polynomial contracts eight epsilon
tensors against symmetric tensors whose orders are the profile (2,...,8).
Coefficients are integral; selected graph and coefficient data are saved.
The eventual proof verifier will use only the standard library.
"""
import argparse
from collections import defaultdict
from itertools import permutations,product
import json
import os
from pathlib import Path
import random
import tempfile
import time

import numpy as np

PERMS = np.array(list(permutations(range(3))), dtype=np.uint8)
PSIGNS = np.array([(-1)**sum(p[i]>p[j] for i in range(3)
                            for j in range(i+1,3)) for p in PERMS], dtype=np.int32)
N = 6**7
DIGITS = np.empty((N,8),dtype=np.uint8)
DIGITS[:,0] = 0
for i in range(7): DIGITS[:,i+1] = np.arange(N,dtype=np.int32)//6**i%6
COLORS = PERMS[DIGITS]
SIGNS = np.prod(PSIGNS[DIGITS],axis=1,dtype=np.int32)
TRIPLES = {j:np.array([(a,b,j-a-b) for a in range(j+1)
                       for b in range(j-a+1)],dtype=np.uint8) for j in range(2,9)}
MAPS = {}
for j, triples in TRIPLES.items():
    maps=[]
    for perm in PERMS:
        t=triples[:,perm].astype(np.int16)
        maps.append((t[:,0]*(2*j+3-t[:,0])//2+t[:,1]).astype(np.uint8))
    MAPS[j]=maps


def initial_graph(degrees,edge_count=8):
    edges=[[] for _ in range(edge_count)]
    for vertex,degree in sorted(enumerate(degrees),key=lambda x:-x[1]):
        chosen=sorted(range(edge_count),key=lambda e:(len(edges[e]),e))[:degree]
        for edge in chosen:edges[edge].append(vertex)
    assert all(len(e)==3 and len(set(e))==3 for e in edges)
    return edges


def walk(graph,rng,steps=128):
    edges=[list(e) for e in graph]
    for _ in range(steps):
        a,b=rng.sample(range(len(graph)),2);i=rng.randrange(3);j=rng.randrange(3)
        x,y=edges[a][i],edges[b][j]
        if x!=y and x not in edges[b] and y not in edges[a]:
            edges[a][i],edges[b][j]=y,x
    return sorted([sorted(e) for e in edges])


def decompositions(profile):
    """Possible degree profiles of a proper disconnected component."""
    out=[]
    for left in product(*(range(k+1) for k in profile)):
        weight=sum(j*k for j,k in enumerate(left,2))
        if weight%3 or not 6<=weight<=12:continue
        c=weight//3
        if any(k and j>c for j,k in enumerate(left,2)):continue
        if any(k-l and j>8-c for j,(k,l) in enumerate(zip(profile,left),2)):continue
        out.append(left)
    return out


def disconnected_graph(degrees,left,rng):
    groups=[[],[]]
    counts=list(left)
    for vertex,j in enumerate(degrees):
        side=0 if counts[j-2] else 1
        groups[side].append(vertex)
        if side==0:counts[j-2]-=1
    edges=[]
    for vertices in groups:
        ds=[degrees[v] for v in vertices];c=sum(ds)//3
        graph=walk(initial_graph(ds,c),rng)
        edges.extend([[vertices[v] for v in edge] for edge in graph])
    return sorted([sorted(edge) for edge in edges])


def biased_graph(degrees,rng):
    """A completion-safe sampler that frequently creates repeated edges."""
    remaining=list(degrees);edges=[]
    for slots in range(8,0,-1):
        mandatory=[i for i,d in enumerate(remaining) if d==slots]
        choices=[i for i,d in enumerate(remaining) if d and i not in mandatory]
        previous=edges[-1] if edges else []
        if previous and rng.random()<.55 and all(remaining[i] for i in previous) and all(i in previous for i in mandatory):
            edge=previous[:]
        else:edge=mandatory+rng.sample(choices,3-len(mandatory))
        for i in edge:remaining[i]-=1
        edges.append(sorted(edge))
        assert min(remaining)>=0 and max(remaining)<=slots-1
    assert not any(remaining)
    return sorted(edges)


def pack(rows):
    """Two uint64 big-endian words, lexicographic order of up to 12 bytes."""
    out=np.zeros((len(rows),16),dtype=np.uint8);out[:,:rows.shape[1]]=rows
    return out.view('>u8').reshape(-1,2).astype(np.uint64)


def expand(graph,degrees):
    """Return canonical S3 monomial keys and reduced-orientation coefficients.

    The full coefficient at each monomial in orbit O is 6/|O| times the
    returned integer. This restores all six orientations of the first
    epsilon. Eight is even, so no extra global-permutation sign occurs.
    """
    slots=defaultdict(list)
    for e,vertices in enumerate(graph):
        for slot,v in enumerate(vertices):slots[v].append((e,slot))
    terms=np.empty((N,len(degrees)),dtype=np.uint8)
    for vertex,j in enumerate(degrees):
        a=np.zeros(N,dtype=np.int16);b=np.zeros(N,dtype=np.int16)
        for e,slot in slots[vertex]:
            col=COLORS[:,e,slot];a+=col==0;b+=col==1
        terms[:,vertex]=a*(2*j+3-a)//2+b
    best=None
    for pi in range(6):
        mapped=np.empty_like(terms)
        for j in range(2,9):
            positions=[i for i,d in enumerate(degrees) if d==j]
            if positions:
                values=MAPS[j][pi][terms[:,positions]]
                mapped[:,positions]=np.sort(values,axis=1)
        packed=pack(mapped)
        if best is None:best=packed
        else:
            smaller=(packed[:,0]<best[:,0])|((packed[:,0]==best[:,0])&(packed[:,1]<best[:,1]))
            best[smaller]=packed[smaller]
    structured=best.view([('a','u8'),('b','u8')]).reshape(-1)
    unique,inverse=np.unique(structured,return_inverse=True)
    coeff=np.bincount(inverse,weights=SIGNS).astype(np.int64)
    nonzero=coeff!=0
    keys=unique[nonzero].view(np.uint64).reshape(-1,2)
    return keys,coeff[nonzero]


def unpack(keys,k):
    return keys.astype('>u8').view(np.uint8).reshape(-1,16)[:,:k]


def atomic_json(path,value):
    """Publish metadata last, with no partially written JSON visible."""
    with tempfile.NamedTemporaryFile(mode='w',dir=path.parent,
                                     prefix=path.name+'.',suffix='.tmp',delete=False) as handle:
        json.dump(value,handle,indent=2)
        handle.write('\n')
        temporary=handle.name
    os.replace(temporary,path)


class Basis:
    def __init__(self,p=101):
        self.p=p;self.index={};self.rows=[];self.pivots=[];self.graphs=[];self.polys=[]
    def insert(self,keys,coeff,graph):
        oldlen=len(self.index)
        columns=[]
        for key in map(tuple,keys.tolist()):
            if key not in self.index:self.index[key]=len(self.index)
            columns.append(self.index[key])
        added=len(self.index)-oldlen
        if added:self.rows=[np.pad(row,(0,added)) for row in self.rows]
        row=np.zeros(len(self.index),dtype=np.int32);row[columns]=coeff%self.p
        for pivot,other in zip(self.pivots,self.rows):
            value=int(row[pivot])
            if value:row=(row-value*other)%self.p
        nonzero=np.flatnonzero(row)
        if len(nonzero)==0:return False
        pivot=int(nonzero[0]);row=row*pow(int(row[pivot]),-1,self.p)%self.p
        self.pivots.append(pivot);self.rows.append(row);self.graphs.append(graph)
        self.polys.append((keys,coeff))
        return True
    def save(self,directory,profile,dimension,attempts,elapsed):
        directory.mkdir(parents=True,exist_ok=True)
        tag='_'.join(map(str,profile))
        arrays={}
        for i,(keys,coeff) in enumerate(self.polys):
            arrays['keys'+str(i)]=keys;arrays['coeff'+str(i)]=coeff
        with tempfile.NamedTemporaryFile(dir=directory,prefix=tag+'.',
                                         suffix='.npz.tmp',delete=False) as handle:
            np.savez_compressed(handle,**arrays)
            temporary=handle.name
        os.replace(temporary,directory/(tag+'.npz'))
        inverse={i:key for key,i in self.index.items()}
        meta=dict(profile=profile,dimension=dimension,rank=len(self.rows),prime=self.p,
                  attempts=attempts,graphs=self.graphs,
                  pivot_monomials=[inverse[i] for i in self.pivots],
                  total_terms=sum(len(c) for _,c in self.polys),elapsed_seconds=elapsed)
        atomic_json(directory/(tag+'.json'),meta)
        return meta


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile',type=int,nargs=7)
    parser.add_argument('--max-attempts',type=int,default=1000)
    parser.add_argument('--output-dir',type=Path,default=Path('work/support_lmr/results/bracket_basis'))
    parser.add_argument('--reverse',action='store_true')
    parser.add_argument('--disconnected',action='store_true',help='frequently sample product invariants')
    parser.add_argument('--diverse',action='store_true',help='also bias toward repeated epsilon edges')
    parser.add_argument('--resume-dir',type=Path,help='keep independent polynomials from this prior data directory')
    args=parser.parse_args()
    profiles=json.loads(Path('work/support_lmr/results/invariant_profiles.json').read_text())['profiles']
    if args.profile is not None:profiles=[x for x in profiles if x['profile']==args.profile]
    if args.reverse:profiles=list(reversed(profiles))
    overall=time.monotonic()
    for pi,entry in enumerate(profiles):
        profile=entry['profile'];target=entry['invariant_dimension']
        tag='_'.join(map(str,profile));done=args.output_dir/(tag+'.json')
        if done.exists() and json.loads(done.read_text())['rank']==target:
            continue
        start=time.monotonic();degrees=[j for j,k in enumerate(profile,2) for _ in range(k)]
        graph=initial_graph(degrees);rng=random.Random(20261122+sum((j+2)*13**j*k for j,k in enumerate(profile)))
        cuts=decompositions(profile) if args.disconnected else []
        basis=Basis();seen=set()
        if args.resume_dir:
            source=args.resume_dir/(tag+'.json')
            if source.exists():
                prior=json.loads(source.read_text())
                with np.load(args.resume_dir/(tag+'.npz')) as arrays:
                    for i,oldgraph in enumerate(prior['graphs']):
                        assert basis.insert(arrays['keys'+str(i)],arrays['coeff'+str(i)],oldgraph)
                print(json.dumps(dict(profile=profile,resumed_rank=len(basis.rows))),flush=True)
        for attempt in range(1,args.max_attempts+1):
            if args.diverse and attempt%3==1:graph=biased_graph(degrees,rng)
            elif cuts and attempt%3==0:graph=disconnected_graph(degrees,rng.choice(cuts),rng)
            else:graph=walk(graph,rng)
            key=tuple(tuple(e) for e in graph)
            if key in seen:continue
            seen.add(key)
            keys,coeff=expand(graph,degrees)
            if basis.insert(keys,coeff,graph):
                print(json.dumps(dict(profile=profile,rank=len(basis.rows),target=target,
                       attempt=attempt,terms=len(coeff),seconds=round(time.monotonic()-start,3))),flush=True)
                if len(basis.rows)==target:break
        meta=basis.save(args.output_dir,profile,target,attempt,time.monotonic()-start)
        print(json.dumps(dict(profile_done=profile,rank=meta['rank'],target=target,attempts=attempt,
                   total_terms=meta['total_terms'],seconds=round(meta['elapsed_seconds'],3),
                   overall_seconds=round(time.monotonic()-overall,3))),flush=True)


if __name__=='__main__':main()
