#!/usr/bin/env python3
"""Finite higher-index probes; no uniform theorem is inferred."""
from pathlib import Path
from time import perf_counter
import ast,itertools,json,random
started=perf_counter()
source=Path(__file__).with_name('post_CP16_etale_double_variation_probe.py')
nodes=[]
for n in ast.parse(source.read_text()).body:
    if isinstance(n,ast.FunctionDef):nodes.append(n)
small=Path(__file__).with_name('A3_mixed_product_probe.py')
exec(compile(ast.Module(body=[n for n in ast.parse(small.read_text()).body
                              if isinstance(n,ast.FunctionDef)],type_ignores=[]),
             str(small),'exec'))
exec(compile(ast.Module(body=nodes,type_ignores=[]),str(source),'exec'))
u={(1,0),(-1,0)}
v={(0,1),(-2,1),(0,0),(-1,0),(-2,0)}

def data(m):
    first,second=basis(m),basis(3)
    pairs=list(itertools.product(first,second))
    inds={x:i for i,x in enumerate(pairs)}
    C1=[[cartier(multiply(x,y,True),True) for y in first] for x in first]
    C2=[[cartier(multiply(x,y,False),False) for y in second] for x in second]
    coeff=[]
    for a,z in itertools.product(range(m),range(3)):
        coeff.append([
            sum(1<<inds[(x,y)] for x in C1[a][i] for y in C2[z][j])
            for i,j in itertools.product(range(m),range(3))])
    def matrix(s):
        cols=[0]*(3*m)
        for j in range(3*m):
            if s>>j&1:cols=[x^y for x,y in zip(cols,coeff[j])]
        return cols
    def toral(s):
        ans=0
        for j,((i,h),z) in enumerate(pairs):
            if s>>j&1:
                if (i+h)%2:ans^=1<<j
                if h:ans^=1<<inds[((i+2,0),z)]
        return ans
    return pairs,inds,coeff,matrix,toral

records=[]
for m in [6,12,24,48]:
    case_started=perf_counter()
    spairs,sinds,scoeff,smat,se=data(m)
    tpairs,tinds,tcoeff,tmat,te=data(2*m)
    rng=random.Random(202611191515+m)
    rejected=[]
    for attempt in range(1000):
        s=rng.getrandbits(3*m)
        sr,sseq=stable_rank(smat(s))
        if sr==3*m-2:break
        rejected.append({'section_bits':s,'stable_rank':sr})
    else:raise AssertionError('no source witness')
    pullcols=[]
    for (i,j),z in spairs:
        poly=pmul({(m//2,0)},pmul(ppow(u,i),ppow(v,j)))
        pullcols.append(sum(1<<tinds[(a,z)] for a in poly))
    S=apply(pullcols,s)
    C=tmat(S);F=transpose(C,6*m)
    sr,seq=stable_rank(C)
    assert sr==6*m-4
    I=nullspace([S,te(S)],6*m);coords=coordinate_solver(I)
    FI=[coords(apply(F,x)) for x in I]
    ker=nullspace(transpose(FI,len(I)),len(I));left=nullspace(FI,len(I))
    assert len(ker)==len(left)==2 and rank(FI)==6*m-4
    fullker=[apply(I,x) for x in ker];variations=[]
    for j in range(6*m):
        Ft=transpose(tcoeff[j],6*m)
        columns=[]
        for x in fullker:
            z=coords(apply(Ft,x))
            columns.append(sum(((lam&z).bit_count()%2)<<i for i,lam in enumerate(left)))
        variations.append(columns)
    def det(x):
        return ((x[0]&1)*((x[1]>>1)&1))^(((x[0]>>1)&1)*(x[1]&1))
    nonzero=[]
    for i in range(6*m):
        if det(variations[i]):nonzero.append([i,i])
        for j in range(i+1,6*m):
            combo=[x^y for x,y in zip(variations[i],variations[j])]
            if det(combo)^det(variations[i])^det(variations[j]):nonzero.append([i,j])
    records.append({'source_pole_degree':m,'target_pole_degree':2*m,
                    'source_bits':s,'rejected_sources':rejected,
                    'target_bits':S,'source_rank_sequence':sseq,
                    'target_rank_sequence':seq,'I_rank':rank(FI),
                    'variation_matrices':variations,
                    'variation_nonzero_monomials':nonzero,
                    'quadratic_nonzero':bool(nonzero),
                    'elapsed_seconds':perf_counter()-case_started})
out={'status':'COMPLETED_FINITE_PROBE',
     'scope':'Four exact product examples at increasing ordinary indices; no fixed-nonproduct or uniform assertion',
     'records':records,'elapsed_seconds':perf_counter()-started}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'scope':out['scope'],'cases':[
  {k:r[k] for k in ['source_pole_degree','target_rank_sequence','I_rank','quadratic_nonzero','elapsed_seconds']}
  for r in records],'elapsed_seconds':out['elapsed_seconds']},indent=2))
