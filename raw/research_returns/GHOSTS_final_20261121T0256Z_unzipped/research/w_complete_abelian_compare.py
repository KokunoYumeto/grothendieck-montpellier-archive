"""Complete finite comparison after the separately proved abelian-cycle reduction.

Uses exact additive base-1001 encodings with a checked coefficient bound.
Any found equality is reconstructed and verified in all 70 exterior coordinates.
"""
from pathlib import Path
from collections import defaultdict
import pickle
root=Path(__file__).resolve().parent
exec((root/'t0_search.py').read_text().split('extra={}')[0])
with open(root/'w_full_abelian_search.catalog','rb') as ff:zeros,dp,weights=pickle.load(ff)
def encode(v):return sum(a*w for a,w in zip(v,weights))
def bar(z):return z[0]-z[1],-z[1]
def dij(a,i,j):
 u,v=cmforms(a,i)
 return add(wedge(add(form(2*j),scale(-1,u)),add(form(2*j+1),scale(-1,v))),
            scale(-1,wedge(form(2*i),form(2*i+1))),scale(-1,wedge(form(2*j),form(2*j+1))))
P,Q=dij((1,0),0,2),dij((0,1),0,2)
U,V=dij((1,0),1,3),dij((0,1),1,3)
qdict=add(wedge(P,U),scale(-1,wedge(P,V)),scale(-1,wedge(Q,U)),scale(-2,wedge(Q,V)))
q=tuple(qdict.get(k,0) for k in basis);qc=encode(q)
plusz={(2,0),(1,-1),(2,1)}
minusz={(a-3,b) for a,b in plusz}
perm=[4,5,6,7,0,1,2,3]
trans=[]
for b in basis:
 bb=tuple(perm[i] for i in b)
 trans.append((basis.index(tuple(sorted(bb))),(-1)**sum(bb[i]>bb[j] for i in range(4) for j in range(i+1,4))))
def transpose(v):
 out=[0]*70
 for c,(j,s) in zip(v,trans):out[j]=s*c
 return tuple(out)
entries=[z for z in product(range(-3,4),repeat=2) if norm(z)<=9]
G=[];seen=set()
def insert(D,z,v,name,d):
 if v in seen:return
 seen.add(v);G.append((D,z,encode(v),v,name,d))
for h in product(entries,repeat=4):
 T=sum(map(norm,h))
 if T>9:continue
 dd=det(h);d=norm(dd)
 if d not in (1,3,4) or T+d>10:continue
 D=2*(1+d+T);zz=bar(dd)
 if d==1:
  if D>14 and zz!=(-1,0):continue
 else:
  if zz not in plusz|minusz and bar(zz) not in plusz|minusz:continue
 vv=graph(h)
 insert(D,zz,vv,('graph',h),d)
 if d>1:insert(D,bar(zz),transpose(vv),('transpose_graph',h),d)
print('W graph counts:',Counter((g[0],g[5]) for g in G),flush=True)
maxcoeff=max(abs(x) for g in G for x in g[3])
zmax=max(abs(x) for v in zeros for x in v)
assert 2*11*max(maxcoeff,zmax)+max(abs(x) for x in q)<1000
print('Exact encoding coefficient bound:',2*11*max(maxcoeff,zmax)+max(abs(x) for x in q),'<1000',flush=True)
A=[i for i,g in enumerate(G) if g[5]==1 and g[0]<=14]
pairs=defaultdict(list)
for ai,i in enumerate(A):
 for j in A[ai:]:
  D=G[i][0]+G[j][0]
  if D>22:continue
  z=ka(G[i][1],G[j][1])
  kind='plus' if z in plusz else 'minus' if z in minusz else None
  if kind:pairs[D,kind].append((G[i][2]+G[j][2],i,j))
singleplus=[i for i,g in enumerate(G) if g[5]>1 and g[1] in plusz]
singleminus=[i for i,g in enumerate(G) if g[1] in minusz]
print('Pair groups:',{k:len(v) for k,v in pairs.items()},flush=True)
print('Single plus/minus:',len(singleplus),len(singleminus),flush=True)
zgens=[(D//2,encode(v),name,v) for v,(D,name) in zeros.items()]
def reconstruct_extra(code,n):
 out=[]
 while n:
  for d,c,name,v in zgens:
   if d<=n and code-c in dp[n-d]:
    out.append((d*2,name,v));code-=c;n-=d;break
  else:raise AssertionError('zero-cycle reconstruction failed')
 assert code==0
 return out
def make_vector(main,extras):
 v=(0,)*70
 for i in main:v=va(v,G[i][3])
 for _,_,w in extras:v=va(v,w)
 return v
def find_positive(code,degree):
 for (D,kind),pp in pairs.items():
  if kind!='plus' or D>degree:continue
  n=(degree-D)//2
  if n>7:continue
  for pc,i,j in pp:
   if code-pc in dp[n]:return [i,j],reconstruct_extra(code-pc,n)
 for i in singleplus:
  g=G[i]
  if g[0]<=degree and code-g[2] in dp[(degree-g[0])//2]:return [i],reconstruct_extra(code-g[2],(degree-g[0])//2)
 raise AssertionError('positive reconstruction failed')
def success(pc,degree,minus_main,minus_extra):
 plus_main,plus_extra=find_positive(pc,degree)
 pv=make_vector(plus_main,plus_extra);mv=make_vector(minus_main,minus_extra)
 assert vs(pv,mv)==q
 print('FOUND EXACT DEGREE',degree,flush=True)
 print('PLUS:',[G[i][4] for i in plus_main],[(d,n) for d,n,_ in plus_extra],flush=True)
 print('MINUS:',[G[i][4] for i in minus_main],[(d,n) for d,n,_ in minus_extra],flush=True)
 print('All 70 coordinates verified.',flush=True)
 raise SystemExit
for degree in (16,18,20,22):
 positive=set()
 for (D,kind),pp in pairs.items():
  if kind!='plus' or D>degree:continue
  n=(degree-D)//2
  for pc,i,j in pp:positive.update(pc+e for e in dp[n])
 for i in singleplus:
  g=G[i]
  if g[0]<=degree:positive.update(g[2]+e for e in dp[(degree-g[0])//2])
 print('Degree',degree,'positive classes',len(positive),flush=True)
 checked=0
 for (D,kind),pp in pairs.items():
  if kind!='minus' or D>degree:continue
  n=(degree-D)//2
  for pc,i,j in pp:
   for e in dp[n]:
    checked+=1
    if pc+e+qc in positive:success(pc+e+qc,degree,[i,j],reconstruct_extra(e,n))
 for i in singleminus:
  g=G[i]
  if g[0]>degree:continue
  n=(degree-g[0])//2
  for e in dp[n]:
   checked+=1
   if g[2]+e+qc in positive:success(g[2]+e+qc,degree,[i],reconstruct_extra(e,n))
 print('No abelian-cycle equality at degree',degree,'negative candidates checked',checked,flush=True)
