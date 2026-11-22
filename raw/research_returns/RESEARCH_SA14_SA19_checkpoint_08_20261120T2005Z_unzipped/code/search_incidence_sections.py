"""Finite exploratory Cox-ring calculation for Frobenius incidence surfaces.

We compute only a graded quotient of the explicitly generated ideal. We
do not assert saturation, smoothness of sampled sections, or equality
with sheaf cohomology. A dimension excess would trigger those checks.
"""
from pathlib import Path
from itertools import combinations
from functools import lru_cache
from math import comb
import numpy as np,json,time
from search_homogeneous_sections import chi_surface_negative
@lru_cache(None)
def monomials(n,d):
    if d<0:return ()
    if n==1:return ((d,),)
    return tuple((a,)+b for a in range(d+1) for b in monomials(n-1,d-a))
def unit(n,i,power=1):
    x=[0]*n;x[i]=power;return tuple(x)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
pairs=list(combinations(range(4),2));pair_index={a:i for i,a in enumerate(pairs)}
def compute(p,seed):
    start=time.monotonic();r,s=2,p
    yy=monomials(4,r);pp=monomials(6,s);cols={(a,b):i for i,(a,b) in enumerate((a,b) for a in yy for b in pp)}
    z4=(0,)*4;z6=(0,)*6;generators=[]
    pl=[]
    for sign,first,second in [(1,(0,1),(2,3)),(-1,(0,2),(1,3)),(1,(0,3),(1,2))]:
        pl.append((sign,z4,add(unit(6,pair_index[first]),unit(6,pair_index[second]))))
    generators.append((0,2,pl))
    for i,j,k in combinations(range(4),3):
        terms=[(1,unit(4,i),unit(6,pair_index[(j,k)],p)),(-1,unit(4,j),unit(6,pair_index[(i,k)],p)),(1,unit(4,k),unit(6,pair_index[(i,j)],p))]
        generators.append((1,p,terms))
    rng=np.random.default_rng(seed)
    hyperplanes=[]
    for _ in range(3):
        cs=rng.integers(0,p,size=(4,6));hyperplanes.append(cs.tolist())
        generators.append((1,1,[(int(cs[i,j]),unit(4,i),unit(6,j)) for i in range(4) for j in range(6) if cs[i,j]]))
    rows=[]
    for dr,ds,terms in generators:
        for a in monomials(4,r-dr):
            for b in monomials(6,s-ds):
                row=np.zeros(len(cols),dtype=np.int16)
                for c,y,z in terms:row[cols[(add(a,y),add(b,z))]]+=c
                rows.append(row%p)
    matrix=np.stack(rows);rank=0
    for col in range(matrix.shape[1]):
        piv=np.flatnonzero(matrix[rank:,col])
        if not len(piv):continue
        j=rank+int(piv[0]);matrix[[rank,j]]=matrix[[j,rank]]
        matrix[rank]=(matrix[rank]*pow(int(matrix[rank,col]),-1,p))%p
        active=np.flatnonzero(matrix[rank+1:,col])+rank+1
        if len(active):matrix[active,col:]=(matrix[active,col:]-matrix[active,col,None]*matrix[rank,col:])%p
        rank+=1
        if rank==len(rows):break
    dimension=len(cols)-rank;chi=chi_surface_negative(4,p,1,1,1,1)
    return dict(p=p,seed=seed,degree=[r,s],columns=len(cols),rows=len(rows),rank=rank,quotient_dimension=dimension,euler_formula=chi,excess=dimension-chi,hyperplanes=hyperplanes,seconds=round(time.monotonic()-start,3))
if __name__=='__main__':
    start=time.monotonic();results=[compute(p,seed) for p in [2,3] for seed in range(4)]
    out=dict(seconds=round(time.monotonic()-start,3),scope=__doc__,results=results)
    Path(__file__).with_name('search_incidence_sections_output.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({**out,'results':[{k:v for k,v in r.items() if k!='hyperplanes'} for r in results]},indent=2))
