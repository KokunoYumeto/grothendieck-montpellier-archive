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
for degree in (16,18,20,22):
 table={}
 for (D,kind),pairs in pairgroups.items():
  if kind!='plus' or degree-D not in E:continue
  ee=E[degree-D]
  for code,i,j in pairs:
   for k,(ex,_,_) in enumerate(ee):table[code+ex]=(i,j,degree-D,k)
 print('Stored degree',degree,'positive classes',len(table),flush=True)
 for (D,kind),pairs in pairgroups.items():
  if kind!='minus' or degree-D not in E:continue
  ee=E[degree-D]
  for code,i,j in pairs:
   for k,(ex,data,vec) in enumerate(ee):
    hit=table.get(code+ex+qcode)
    if hit is not None:
     ii,jj,de,kk=hit
     left=va(va(G[ii][4],G[jj][4]),E[de][kk][2])
     right=va(va(G[i][4],G[j][4]),vec)
     assert vs(left,right)==q
     print('FOUND DEGREE',degree,flush=True)
     print('PLUS GRAPHS',G[ii][3],G[jj][3],'EXTRAS',E[de][kk][1],flush=True)
     print('MINUS GRAPHS',G[i][3],G[j][3],'EXTRAS',data,flush=True)
     raise SystemExit
 print('No two-graph identity degree',degree,flush=True)
