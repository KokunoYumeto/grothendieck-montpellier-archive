"""Search exact common intertwiners explaining a bounded detector cancellation."""
from pathlib import Path
exec(Path('code/C_finish_elementary_tensor_curvature.py').read_text().split('for label,L,R in')[0])
start=perf_counter()
def simultaneous(A,B):
 n=A[0].shape[0]
 if B[0].shape!=(n,n):return {'dimension_match':False}
 if not n:return {'dimension_match':True,'intertwiner_dimension':0,'invertible':True,'matrix':[]}
 units=[]
 for i in range(n):
  for j in range(n):
   E=np.zeros((n,n),dtype=np.int64);E[i,j]=1;units.append(E)
 D=np.column_stack([np.concatenate([(E@a-b@E).ravel() for a,b in zip(A,B)]) for E in units])%3
 H=ker(D,3);dim=H.shape[1];P=None
 pars=product(range(3),repeat=dim) if dim<=7 else np.random.default_rng(1907+n).integers(0,3,size=(3000,dim),dtype=np.int64)
 tested=0
 for c in pars:
  tested+=1;Q=(H@np.array(c,dtype=np.int64)%3).reshape(n,n)
  if rank(Q,3)==n:P=Q;break
 if P is not None:assert all(not np.any((P@a-b@P)%3) for a,b in zip(A,B))
 return {'dimension_match':True,'intertwiner_dimension':dim,'coefficient_combinations_tested':tested,'invertible':P is not None,'matrix':None if P is None else P.tolist()}
runs=[]
for label,L,R in [('full_full',Tf,Tf),('full_plane',Tf,Tq),('plane_plane',Tq,Tq),('full_pair',Tf,pair)]:
 T1=kron(L,ident(len(R)));T2=kron(ident(len(L)),R);n=len(T1)
 H,dimensions=tangent_basis(T1,T2);d=H.shape[1]
 t1,t2=ar(T1),ar(T2);ii=ar(ident(n))
 x1,x2=aa(t1,an(ii)),aa(t2,an(ii))
 v1,v2=aa(aa(ii,t1),am(t1,t1)),aa(aa(ii,t2),am(t2,t2))
 for s in (1,2):
  d0=ab(x1,an(asc(v2,s)),x2,v1);d1=ab(v1,asc(v2,s),an(x2),x1)
  h0,p0=homology(d0[0],d1[0],3);h1,p1=homology(d1[0],d0[0],3)
  gamma0=p1@d0[1]@h0%3;gamma1=p0@d1[1]@h1%3
  AA=[];BB=[]
  for j in range(d):
   u1=(H[:n*n,j].reshape(n,n),np.zeros((n,n),dtype=np.int64));u2=(H[n*n:,j].reshape(n,n),np.zeros((n,n),dtype=np.int64))
   w1=aa(aa(u1,am(t1,u1)),am(u1,t1));w2=aa(aa(u2,am(t2,u2)),am(u2,t2))
   dd0=ab(u1,an(asc(w2,s)),u2,w1);dd1=ab(w1,asc(w2,s),an(u2),u1)
   cur0=aa(am(d1,dd0),am(dd1,d0));cur1=aa(am(d0,dd1),am(dd0,d1))
   assert not np.any(cur0[0]) and not np.any(cur1[0])
   c0=p0@cur0[1]@h0%3;c1=p1@cur1[1]@h1%3
   AA.append(image_map(gamma0,c1));BB.append(image_map(gamma1,c0))
  out=simultaneous(AA,BB)
  runs.append({'baseline':label,'s':s,'tangent_generators':d,'image_dimensions':[AA[0].shape[0],BB[0].shape[0]],**out})
  print(label,s,out,flush=True)
report={'status':'COMMON-INTERTWINER SEARCH COMPLETE','scope':'For each of four specified tensor-product baselines and s1,2, solves the simultaneous linear intertwiner equations for all tangent generators on the two pi-Bockstein images. An invertible solution proves characteristic-polynomial equality for all tangent parameters in that specified space and slope, but does not establish equality of Swan classes.',
        'runs':runs,'runtime_seconds':round(perf_counter()-start,6)}
Path('logs/C_finish_elementary_tensor_intertwiner.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
