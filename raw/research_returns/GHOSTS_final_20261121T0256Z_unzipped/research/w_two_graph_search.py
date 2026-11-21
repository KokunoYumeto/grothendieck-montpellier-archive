"""Positive-identity search for 3w; no general lower bound is inferred."""
from pathlib import Path
source=Path('work/agents/t0_search.py').read_text().split('for degree in [8,10,12,14]:')[0]
exec(source)
def dij(a,i,j):
 u,v=cmforms(a,i)
 return add(wedge(add(form(2*j),scale(-1,u)),add(form(2*j+1),scale(-1,v))),
            scale(-1,wedge(form(2*i),form(2*i+1))),
            scale(-1,wedge(form(2*j),form(2*j+1))))
P,Q=dij((1,0),0,2),dij((0,1),0,2)
U,V=dij((1,0),1,3),dij((0,1),1,3)
qd=add(wedge(P,U),scale(-1,wedge(P,V)),scale(-1,wedge(Q,U)),scale(-2,wedge(Q,V)))
q=tuple(qd.get(k,0) for k in basis)
weights=[101**i for i in range(70)]
def encode(v):return sum(a*w for a,w in zip(v,weights))
qcode=encode(q)
def bar(z):return z[0]-z[1],-z[1]
G=[(D,encode(v),bar(det(h)),h,v) for h,(D,v) in graphs.items()]
E={D:[(encode(v),data,v) for v,data in values.items()] for D,values in extras.items()}
zs={ka(u,v) for u in units for v in units}
plusz={z for z in zs if (z[0]-3,z[1]) in zs}
print('Positive z values:',sorted(plusz),flush=True)
pairgroups={}
for i,g in enumerate(G):
 for j in range(i,len(G)):
  hh=G[j];D=g[0]+hh[0]
  if D>22:continue
  zz=ka(g[2],hh[2])
  if zz in plusz:kind='plus'
  elif (zz[0]+3,zz[1]) in plusz:kind='minus'
  else:continue
  pairgroups.setdefault((D,kind),[]).append((g[1]+hh[1],i,j))
print('Pair group sizes:',{k:len(v) for k,v in pairgroups.items()},flush=True)
entries2=[q for q in product(range(-3,4),repeat=2) if norm(q)<=7]
singles=[]
for h in product(entries2,repeat=4):
 T=sum(map(norm,h))
 if T>7:continue
 d=norm(det(h))
 if d not in (3,4):continue
 D=2*(1+d+T)
 if D>22:continue
 zz=bar(det(h))
 if zz in plusz:kind='plus'
 elif (zz[0]+3,zz[1]) in plusz:kind='minus'
 else:continue
 vv=graph(h)
 singles.append((D,kind,encode(vv),h,vv))
print('Single isogeny graphs:',Counter((x[0],x[1]) for x in singles),flush=True)
def curve_class(A,B,qq,i,j):
 return add(scale(A,wedge(form(2*i),form(2*i+1))),
            scale(B,wedge(form(2*j),form(2*j+1))),
            scale(qq[0],dij((1,0),i,j)),scale(qq[1],dij((0,1),i,j)))
curves=[]
for degree in range(2,6):
 for A in range(1,degree):
  B=degree-A
  for qq in product(range(-3,4),repeat=2):
   if 0<norm(qq)<=A*B:curves.append((degree,A,B,qq))
seen_single={vv for _,_,_,_,vv in singles}
for pair1,pair2 in [((0,2),(1,3)),((0,3),(1,2))]:
 for ca,cb in product(curves,repeat=2):
  D=2*ca[0]*cb[0]
  if D>22:continue
  zz=bar(km(ca[3],cb[3]))
  if pair1==(0,3):zz=kn(zz)
  if zz in plusz:kind='plus'
  elif (zz[0]+3,zz[1]) in plusz:kind='minus'
  else:continue
  vd=wedge(curve_class(*ca[1:],*pair1),curve_class(*cb[1:],*pair2))
  vv=tuple(vd.get(k,0) for k in basis)
  if vv in seen_single:continue
  seen_single.add(vv)
  singles.append((D,kind,encode(vv),('nefcurveproduct',pair1,ca,pair2,cb),vv))
print('Single including nef products:',Counter((x[0],x[1]) for x in singles),flush=True)
for degree in (16,18,20,22):
 table={}
 for (D,kind),pairs in pairgroups.items():
  if kind!='plus' or degree-D not in E:continue
  ee=E[degree-D]
  for code,i,j in pairs:
   for k,(ex,_,_) in enumerate(ee):table[code+ex]=('pair',i,j,degree-D,k)
 for si,(D,kind,code,h,vv) in enumerate(singles):
  if kind!='plus' or degree-D not in E:continue
  for k,(ex,_,_) in enumerate(E[degree-D]):table[code+ex]=('single',si,None,degree-D,k)
 print('Stored degree',degree,'positive classes',len(table),flush=True)
 for (D,kind),pairs in pairgroups.items():
  if kind!='minus' or degree-D not in E:continue
  ee=E[degree-D]
  for code,i,j in pairs:
   for k,(ex,data,vec) in enumerate(ee):
    hit=table.get(code+ex+qcode)
    if hit is not None:
     mode,ii,jj,de,kk=hit
     left=va(va(G[ii][4],G[jj][4]),E[de][kk][2]) if mode=='pair' else va(singles[ii][4],E[de][kk][2])
     right=va(va(G[i][4],G[j][4]),vec)
     assert vs(left,right)==q
     print('FOUND DEGREE',degree,flush=True)
     print('PLUS GRAPHS',(G[ii][3],G[jj][3]) if mode=='pair' else singles[ii][3],'EXTRAS',E[de][kk][1],flush=True)
     print('MINUS GRAPHS',G[i][3],G[j][3],'EXTRAS',data,flush=True)
     raise SystemExit
 for si,(D,kind,code,h,vv) in enumerate(singles):
  if kind!='minus' or degree-D not in E:continue
  for k,(ex,data,vec) in enumerate(E[degree-D]):
   hit=table.get(code+ex+qcode)
   if hit is not None:
    mode,ii,jj,de,kk=hit
    left=va(va(G[ii][4],G[jj][4]),E[de][kk][2]) if mode=='pair' else va(singles[ii][4],E[de][kk][2])
    right=va(vv,vec)
    assert vs(left,right)==q
    print('FOUND DEGREE',degree,flush=True)
    print('PLUS GRAPHS',(G[ii][3],G[jj][3]) if mode=='pair' else singles[ii][3],'EXTRAS',E[de][kk][1],flush=True)
    print('MINUS GRAPH',h,'EXTRAS',data,flush=True)
    raise SystemExit
 print('No two-graph identity degree',degree,flush=True)
