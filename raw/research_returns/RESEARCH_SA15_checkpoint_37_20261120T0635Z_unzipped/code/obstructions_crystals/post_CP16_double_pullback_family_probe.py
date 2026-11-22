#!/usr/bin/env python3
"""Retained finite probes of first ranks at several etale double pullbacks.

This does not prove an assertion for arbitrary nonproduct surfaces.
The first exploratory weight-rank read reported [18,18], [16,17], total32;
this saved run retains that calculation with its code and runtime.
"""
from pathlib import Path
from time import perf_counter
import ast,json,random,itertools
started=perf_counter()
source=Path(__file__).with_name('post_CP16_etale_double_variation_probe.py')
tree=ast.parse(source.read_text());nodes=[]
for node in tree.body:
    if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='out'
                                          for t in node.targets):break
    if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='started'
                                          for t in node.targets):continue
    nodes.append(node)
namespace={'__file__':str(source.resolve())}
exec(compile(ast.Module(body=nodes,type_ignores=[]),str(source),'exec'),namespace)
for key in ['basis','cartier','multiply','rank','apply','stable_rank','padd','pmul',
            'ppow','nullspace','transpose','coordinate_solver','toral','matrix']:
    globals()[key]=namespace[key]
u,v=namespace['u'],namespace['v']
pairs=namespace['pairs'];indices=namespace['indices'];b=len(pairs)
oldsection=namespace['section'];oldC=namespace['C']
ecols=[toral(1<<j) for j in range(b)]
erows=transpose(ecols,b)
W0=nullspace(erows,b)
W1=nullspace([x^(1<<j) for j,x in enumerate(erows)],b)
initial={'weight_dimensions':[len(W0),len(W1)],
         'weight_restriction_ranks':[rank([apply(oldC,x) for x in W]) for W in [W0,W1]],
         'total_rank':rank(oldC)}

smallfirst,smallsecond=basis(6),basis(3)
smallpairs=list(itertools.product(smallfirst,smallsecond))
smallindices={a:i for i,a in enumerate(smallpairs)}
smallm1=[[cartier(multiply(c,x,True),True) for x in smallfirst] for c in smallfirst]
smallm2=[[cartier(multiply(c,x,False),False) for x in smallsecond] for c in smallsecond]
smallcoeff=[]
pullcols=[]
for i,(c,d) in enumerate(smallpairs):
    ci,di=smallfirst.index(c),smallsecond.index(d)
    smallcoeff.append([
      sum(1<<smallindices[(x,y)] for x in smallm1[ci][a] for y in smallm2[di][j])
      for a,j in itertools.product(range(6),range(3))])
    lifted=pmul({(3,0)},pmul(ppow(u,c[0]),ppow(v,c[1])))
    pullcols.append(sum(1<<indices[(t,d)] for t in lifted))

def smallmatrix(s):
    out=[0]*18
    for j in range(18):
        if s>>j&1:out=[a^b for a,b in zip(out,smallcoeff[j])]
    return out

def determinant(cols):
    return ((cols[0]&1)*((cols[1]>>1)&1))^(((cols[0]>>1)&1)*(cols[1]&1))

records=[];rng=random.Random(202611191501)
for trial in range(300):
    s=rng.getrandbits(18)
    Cs=smallmatrix(s);sr,seq=stable_rank(Cs)
    if sr!=16:continue
    S=apply(pullcols,s);C=matrix(S);F=transpose(C,b)
    stable,sequence=stable_rank(C)
    assert stable==32
    I=nullspace([S,toral(S)],b);coords=coordinate_solver(I)
    FI=[coords(apply(F,x)) for x in I]
    ker=nullspace(transpose(FI,len(I)),len(I));left=nullspace(FI,len(I))
    rec={'trial':trial,'source_bits':s,'pullback_bits':S,
         'source_rank_sequence':seq,'pullback_rank_sequence':sequence,
         'I_rank':rank(FI),'I_kernel_dimension':len(ker),
         'weight_ranks':[rank([apply(C,x) for x in W]) for W in [W0,W1]]}
    if len(ker)==len(left)==2:
        fullker=[apply(I,x) for x in ker];variations=[]
        for j in range(b):
            Ft=transpose(namespace['coefficients'][j],b)
            columns=[]
            for k in fullker:
                z=coords(apply(Ft,k))
                columns.append(sum(((lam&z).bit_count()%2)<<i for i,lam in enumerate(left)))
            variations.append(columns)
        monomials=[]
        for i in range(b):
            if determinant(variations[i]):monomials.append([i,i])
            for j in range(i+1,b):
                combo=[a^b for a,b in zip(variations[i],variations[j])]
                if determinant(combo)^determinant(variations[i])^determinant(variations[j]):
                    monomials.append([i,j])
        rec['variation_nonzero_monomials']=monomials
        rec['variation_nonzero']=bool(monomials)
    records.append(rec)
    if len(records)==20:break
out={'scope':'Finite F2 coefficient probes only, not a uniform theorem',
     'initial_weight_probe':initial,'sharp_source_samples':records,
     'elapsed_seconds':perf_counter()-started,'status':'COMPLETED_FINITE_PROBE'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'samples':len(records),'first_ranks':[r['pullback_rank_sequence'][1] for r in records],
                  'I_ranks':[r['I_rank'] for r in records],
                  'variation_nonzero':[r.get('variation_nonzero') for r in records],
                  'elapsed_seconds':out['elapsed_seconds']},indent=2))
