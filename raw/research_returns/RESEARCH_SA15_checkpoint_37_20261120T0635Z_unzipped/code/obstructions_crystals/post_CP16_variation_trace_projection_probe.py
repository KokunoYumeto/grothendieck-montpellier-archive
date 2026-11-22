#!/usr/bin/env python3
"""Does the finite variation factor through source Cartier cokernel?
This is a probe at one F2 coefficient point, with exact retained output.
"""
from pathlib import Path
from time import perf_counter
import ast,json,itertools
started=perf_counter()
source=Path(__file__).with_name('post_CP16_etale_double_variation_probe.py')
nodes=[]
for node in ast.parse(source.read_text()).body:
    if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='out'
                                          for t in node.targets):break
    nodes.append(node)
ns={'__file__':str(source.resolve())}
exec(compile(ast.Module(body=nodes,type_ignores=[]),str(source),'exec'),ns)
for name in ['basis','cartier','multiply','rank','apply','padd','pmul','ppow',
             'nullspace','transpose','coordinate_solver']:
    globals()[name]=ns[name]
pairs,indices,b=ns['pairs'],ns['indices'],ns['b']
smallpairs=list(itertools.product(basis(6),basis(3)))
smallidx={p:i for i,p in enumerate(smallpairs)}
u,v=ns['u'],ns['v']
pull=[]
for (i,j),z in smallpairs:
    a=pmul({(3,0)},pmul(ppow(u,i),ppow(v,j)))
    pull.append(sum(1<<indices[(x,z)] for x in a))
solvepull=coordinate_solver(pull)
tx={(-1,0)}
ty={(-2,1),(0,0),(-1,0),(-2,0)}
assert not padd(pmul(ty,ty),pmul(tx,ty),ppow(tx,3),{(0,0)})
tau=[]
for (i,j),z in pairs:
    a=pmul({(6,0)},pmul(ppow(tx,i),ppow(ty,j)))
    tau.append(sum(1<<indices[(x,z)] for x in a))
assert all(apply(tau,apply(tau,1<<j))==1<<j for j in range(b))
assert apply(tau,ns['section'])==ns['section']
trace=[solvepull((1<<j)^tau[j]) for j in range(b)]
assert rank(trace)==18
source_section=solvepull(ns['section'])
smallC=[]
for a,z in smallpairs:
    col=0
    for j,(c,d) in enumerate(smallpairs):
        if source_section>>j&1:
            for aa in cartier(multiply(a,c,True),True):
                for zz in cartier(multiply(z,d,False),False):
                    col^=1<<smallidx[(aa,zz)]
    smallC.append(col)
assert rank(smallC)==16
K=nullspace(smallC,18) # annihilator of Cartier image
projection_rows=[sum(((x&t).bit_count()%2)<<i for i,t in enumerate(trace)) for x in K]
Drows=[]
for a in range(2):
    for q in range(2):
        Drows.append(sum(((cols[a]>>q)&1)<<i for i,cols in enumerate(ns['variation'])))
out={'status':'COMPLETED_FINITE_PROBE',
     'scope':'Exact one-point trace/projection comparison only',
     'source_section_bits':source_section,
     'source_cartier_columns':smallC,'etale_trace_columns':trace,
     'variation_rows':Drows,'Cartier_cokernel_projection_rows':projection_rows,
     'rank_variation':rank(Drows),'rank_nil_projection':rank(projection_rows),
     'rank_combined':rank(Drows+projection_rows),
     'factors_through_Cartier_cokernel':rank(Drows+projection_rows)==rank(projection_rows),
     'elapsed_seconds':perf_counter()-started}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if not k.endswith('rows') and not k.endswith('columns')},indent=2))
