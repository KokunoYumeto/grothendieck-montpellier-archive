"""Complete signed-permutation harmonic kernel over the residual ring."""
from pathlib import Path
from itertools import permutations, product
from collections import defaultdict
import argparse
import json
import random
import time
from math import gcd, factorial

HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--k',type=int,required=True)
parser.add_argument('--modulus',type=int,required=True)
args=parser.parse_args()
k=args.k
Q=args.modulus
assert Q>1 and gcd(Q, 336*factorial(2*k+1))==1
DEST=HERE/f'e{k+1}_m{Q}'
DEST.mkdir(exist_ok=True)
start=time.monotonic()


def orbits(k):
    exps=[(a,b,k-a-b) for a in range(k+1) for b in range(k-a+1)]
    return sorted({tuple(sorted(zip(a,b))) for a in exps for b in exps
                   if all((x-y)%2==0 for x,y in zip(a,b))})


def difference(orbit):
    return tuple(sorted(a-b for a,b in orbit))


def rref(a):
    a=[[x%Q for x in row] for row in a]
    pivots=[]
    for j in range(len(a[0])):
        r=len(pivots)
        pivot=next((i for i in range(r,len(a)) if gcd(a[i][j],Q)==1),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        inverse=pow(a[r][j],-1,Q)
        a[r]=[x*inverse%Q for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][j]:
                t=a[i][j]
                a[i]=[(x-t*y)%Q for x,y in zip(a[i],a[r])]
        pivots.append(j)
        if len(pivots)==len(a):break
    return a,pivots


source,target=orbits(k),orbits(k-1)
si={o:i for i,o in enumerate(source)}
ti={o:i for i,o in enumerate(target)}
sg,tg=defaultdict(list),defaultdict(list)
for i,o in enumerate(source):sg[difference(o)].append(i)
for i,o in enumerate(target):tg[difference(o)].append(i)
columns=[]
for o in source:
    polynomial=defaultdict(int)
    for monomial in set(permutations(o)):
        for i,(a,b) in enumerate(monomial):
            if a and b:
                out=list(monomial);out[i]=(a-1,b-1)
                polynomial[tuple(out)]+=a*b
    columns.append({ti[o]:polynomial[o] for o in target if polynomial[o]})
basis=[]
blocks=[]
for diff,indices in sorted(sg.items()):
    targets=tg[diff]
    if targets:
        a=[[columns[j].get(i,0) for j in indices] for i in targets]
        red,piv=rref(a)
        assert len(piv)==len(targets)
    else:red,piv=[],[]
    free=[j for j in range(len(indices)) if j not in set(piv)]
    for j in free:
        column={indices[j]:1}
        for r,p in enumerate(piv):
            if red[r][j]:column[indices[p]]=(-red[r][j])%Q
        # Direct check against the entire contraction, not the row reduction.
        sums=defaultdict(int)
        for i,c in column.items():
            for row,v in columns[i].items():sums[row]=(sums[row]+c*v)%Q
        assert not any(sums.values())
        basis.append(sorted(column.items()))
    blocks.append({'difference':diff,'source_count':len(indices),
                   'target_count':len(targets),'pivot_columns':[indices[j] for j in piv],
                   'free_columns':[indices[j] for j in free]})
d=len(basis)
assert d==len(source)-len(target)
random_source=random.Random(20261121+k)
points=[[[random_source.randrange(1,Q) for _ in range(3)] for _ in range(2)]
        for _ in range(d+2)]
frames=json.loads((HERE.parent/'neighbor_frames.json').read_text())
out={'status':'EXPLORATORY complete harmonic basis over Z/M',
     'q':Q,'k':k,'e':k+1,'source_orbits':source,'target_orbits':target,
     'harmonic_basis_sparse_columns':basis,'blocks':blocks,
     'identifying_and_extra_points':points,'dimension':d,
     'source_dimension':len(source),'target_dimension':len(target),
     'preparation_seconds':time.monotonic()-start}
(DEST/'model.json').write_text(json.dumps(out,indent=2)+'\n')
with (DEST/'model.txt').open('w') as f:
    f.write(f'{Q} {k} {len(source)} {d}\n')
    for o in source:f.write(' '.join(str(x) for pair in o for x in pair)+'\n')
    for b in basis:
        f.write(str(len(b))+' '+' '.join(f'{i} {c}' for i,c in b)+'\n')
    f.write(str(len(points))+'\n')
    for point in points:f.write(' '.join(str(v) for row in point for v in row)+'\n')
    for norm in (2,4):
        fs=frames[str(norm)]['selected_frames']
        f.write(str(len(fs))+'\n')
        for frame in fs:f.write(' '.join(str(t) for column in frame for x in column for t in x)+'\n')
print(json.dumps({key:out[key] for key in ('q','k','dimension','source_dimension',
                                          'target_dimension','preparation_seconds')}),flush=True)
