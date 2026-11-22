#!/usr/bin/env python3
"""Research computation of the degree-6 quadratic symbol for quaternary nonics.

Each edge ij in a 13-edge omitted-pair multigraph means the determinant
bracket on the other four symbolic letters. Two free slots are at letters
4,5 (zero based). Symmetrization over six letters makes a degree-6 covariant.
No claim about vanishing on all determinant pencils is made by this script.
"""
from itertools import permutations, combinations
import json
import random
from collections import Counter

P=101
EDGES=list(combinations(range(6),2))
COMPLEMENTS={edge:tuple(i for i in range(6) if i not in edge) for edge in EDGES}
PERMS=list(permutations(range(6)))


def det4(columns):
    a=[[columns[j][i] % P for j in range(4)] for i in range(4)]
    out=1
    for j in range(4):
        i=next((i for i in range(j,4) if a[i][j]),None)
        if i is None:return 0
        if i!=j:a[i],a[j]=a[j],a[i];out=-out % P
        v=a[j][j];out=out*v % P;inv=pow(v,-1,P)
        for i in range(j+1,4):
            c=a[i][j]*inv % P
            for k in range(j+1,4):a[i][k]=(a[i][k]-c*a[j][k]) % P
    return out


def parity(sequence):
    return -1 if sum(sequence[i]>sequence[j] for i in range(len(sequence))
                     for j in range(i+1,len(sequence))) % 2 else 1


def evaluation_table(vectors):
    brackets={inds:det4([vectors[i] for i in inds]) for inds in combinations(range(len(vectors)),4)}
    rows=[]
    for assignment in permutations(range(len(vectors)),6):
        values=[]
        for edge in EDGES:
            inds=[assignment[i] for i in COMPLEMENTS[edge]]
            values.append(parity(inds)*brackets[tuple(sorted(inds))] % P)
        rows.append((assignment,values))
    return rows


def evaluate(graph,vectors,weights=None,component=(0,0),table=None):
    if weights is None:weights=[1]*len(vectors)
    if table is None:table=evaluation_table(vectors)
    out=0
    multiplicity=Counter(graph)
    for assignment,values in table:
        value=1
        for edge,count in multiplicity.items():
            value=value*pow(values[EDGES.index(edge)],count,P) % P
            if not value:break
        if value:
            for i in assignment:value=value*weights[i] % P
            value=value*vectors[assignment[4]][component[0]]*vectors[assignment[5]][component[1]] % P
            out=(out+value) % P
    return out


def random_graph(rng):
    stubs=sum(([i]*(4+(i>=4)) for i in range(6)),[])
    while True:
        rng.shuffle(stubs)
        pairs=[tuple(sorted(stubs[i:i+2])) for i in range(0,len(stubs),2)]
        if all(a!=b for a,b in pairs):return pairs


def main():
    rng=random.Random(1909)
    vectors=[[rng.randrange(P) for _ in range(4)] for _ in range(6)]
    table=evaluation_table(vectors)
    for trial in range(1000):
        graph=random_graph(rng)
        # Repeated assigned letters must meet in some bracket and thus vanish.
        if not all(any(a not in edge and b not in edge for edge in graph)
                   for a,b in EDGES):continue
        value=evaluate(graph,vectors,table=table)
        if value:break
    else:raise RuntimeError('no nonzero symbol found')
    print(json.dumps(dict(graph=graph,ambient_witness=vectors,ambient_value=value,trial=trial)),flush=True)
    # Four pairs with equal restriction to x0=0: their signed sum has a linear factor.
    vectors=[];weights=[]
    for i in range(4):
        a=[0]+[rng.randrange(1,P) for _ in range(3)]
        b=a[:];b[0]=rng.randrange(1,P)
        w=rng.randrange(1,P)
        vectors.extend([b,a]);weights.extend([w,-w % P])
    table=evaluation_table(vectors)
    results={}
    for i,j in combinations(range(4),2):
        results[str((i,j))]=(evaluate(graph,vectors,weights,(i,j),table)
                              +evaluate(graph,vectors,weights,(j,i),table)) % P
    for i in range(4):results[str((i,i))]=evaluate(graph,vectors,weights,(i,i),table)
    print(json.dumps(dict(padded_witness=vectors,weights=weights,quadratic_components=results)),flush=True)


if __name__=='__main__':main()
