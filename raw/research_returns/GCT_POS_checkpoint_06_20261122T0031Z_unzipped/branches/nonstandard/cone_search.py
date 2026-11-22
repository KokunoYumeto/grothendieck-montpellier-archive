"""Exact Laurent-coordinate cone search; modular independence gives a rigorous lower bound.
Source arithmetic inherited from INT-NSRH-4 h4cone.py; dual action independently derived.
"""
import sys,pathlib,itertools,json,time
root=pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent/'dependencies'))
import e4lib as L
from collections import defaultdict
OUT=pathlib.Path(__file__).resolve().parent
P=1000003; V=2
G=L.G; keyind={(a,b):i for i,(a,b) in enumerate(itertools.product(G,repeat=2))}
D={-2:1,0:2,2:1}; delta={-1:1,1:1}
# C_w C_s = sign-conjugate of C'_w C'_s.
CM={}
for w in G:
 for si,s in enumerate(L.S):
  xp=L.toCp(L.mulCp(L.Cp[w],s))
  CM[w,si]={z:{e:(-1)**((L.length(z)-L.length(w)-1)%2)*c for e,c in p.items()} for z,p in xp.items()}
def acc(R,k,p,m=1):
 if not p:return
 q=L.padd(R.get(k,{}),p,m)
 if q:R[k]=q
 elif k in R:del R[k]
def step(X,si):
 out={}
 for (a,b),p in X.items():
  acc(out,(a,b),L.pmul(p,D))
  for c,co in CM[a,si].items():acc(out,(c,b),L.pmul(L.pmul(p,co),delta))
  for d,co in CM[b,si].items():acc(out,(a,d),L.pmul(L.pmul(p,co),delta))
  for c,co in CM[a,si].items():
   for d,do in CM[b,si].items():acc(out,(c,d),L.pmul(p,L.pmul(co,do)),2)
 return out
def ev(p):return sum(c*pow(V,e,P) for e,c in p.items())%P
def vec(X):return {keyind[k]:ev(p) for k,p in X.items() if ev(p)}
def add_rank(X,piv):
 x=vec(X)
 for col,r in piv:
  if col not in x:continue
  m=x[col]
  for k,a in r.items():
   t=(x.get(k,0)-m*a)%P
   if t:x[k]=t
   elif k in x:del x[k]
 if not x:return False
 col=min(x);iv=pow(x[col],-1,P);x={k:a*iv%P for k,a in x.items()}
 piv.append((col,x));return True
def positive(X):return all(c>=0 for p in X.values() for c in p.values())
def checks():
 for w in [(),(1,),(1,2),(1,2,1),(2,3,2,3,2,3,1,2,1,2,1)]:
  X=L.ONE_T
  for i in w:X=step(X,i-1)
  assert X==L.dualcoords(L.word_elt(w)),w
checks()
start=time.time();piv=[];pospiv=[];basis=[];posbasis=[]
X=L.ONE_T
add_rank(X,piv);add_rank(X,pospiv);basis.append(());posbasis.append(())
frontier={():X};stats=[];bad=[]
maxlen=int(sys.argv[1]) if len(sys.argv)>1 else 10
for depth in range(1,maxlen+1):
 nf={};npos=0;nbad=0
 for w,X in frontier.items():
  for i in (1,2,3):
   if w and (w[-1]==i or w[-1]==3 and i==1):continue
   nw=w+(i,);Y=step(X,i-1);nf[nw]=Y
   if add_rank(Y,piv):basis.append(nw)
   pos=positive(Y)
   if pos:
    npos+=1
    if add_rank(Y,pospiv):posbasis.append(nw)
   else:
    nbad+=1
    if len(bad)<20:
     neg=[{'a':a,'b':b,'p':p} for (a,b),p in Y.items() if any(c<0 for c in p.values())]
     bad.append({'word':nw,'negative_coordinates':neg})
 frontier=nf
 row=dict(length=depth,words=len(nf),positive=npos,negative=nbad,rank=len(piv),positive_rank=len(pospiv),seconds=time.time()-start)
 stats.append(row);print(row,flush=True)
 (OUT/'cone_search_progress.json').write_text(json.dumps({'stats':stats,'basis':basis,'positive_basis':posbasis,'first_negative':bad,'prime':P,'v':V},indent=2))
 if len(pospiv)==114:break
