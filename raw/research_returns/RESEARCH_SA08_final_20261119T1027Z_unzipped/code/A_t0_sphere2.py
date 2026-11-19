"""Exhaustive F2 verification of relative weight-2 PD forms on Delta2/boundary."""
from itertools import product
from time import perf_counter
import json
t=perf_counter()
V0=[v for v in product(range(2),repeat=3) if v[0]==v[2]==0]
V1=[v for v in product(range(2),repeat=4) if v[0]==v[3]==0 and sum(v)%2==0]
V2=[(0,),(1,)]
def d0(v):a,b,c=v;return (a,b,b,c)
def d1(v):return ((v[1]+v[2])%2,)
assert all(d0(v) in V1 for v in V0)
assert all(d1(d0(v))==(0,) for v in V0)
im0={d0(v) for v in V0};im1={d1(v) for v in V1}
ker0=[v for v in V0 if d0(v)==(0,0,0,0)]
ker1=[v for v in V1 if d1(v)==(0,)]
result={'field':'F2','space':'Delta[2]/boundary','PD_triple':'(F2,0,0)','weight':2,
'basis0':['gamma2(x)','xy','gamma2(y)'],'basis1':['x dx','x dy','y dx','y dy'],'basis2':['dx dy'],
'relative_vectors0':V0,'relative_vectors1':V1,'relative_vectors2':V2,
'd0_images':sorted(im0),'d1_images':sorted(im1),
'cohomology_cardinalities':[len(ker0),len(ker1)//len(im0),len(V2)//len(im1)],
'enumerated_vectors':8+16+2,'seconds':round(perf_counter()-t,6)}
assert result['cohomology_cardinalities']==[1,1,2]
print(json.dumps(result,indent=2))
