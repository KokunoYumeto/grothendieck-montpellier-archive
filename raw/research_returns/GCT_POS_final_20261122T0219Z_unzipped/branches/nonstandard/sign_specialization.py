"""Exact rank and restricted trace form of the P-generated image at v=i.
Integer coordinate normalization absorbs the common i parity in each tensor row.
"""
import pathlib,sys,itertools,json,time
from fractions import Fraction
base=pathlib.Path(__file__).resolve().parent/'dependencies';sys.path.insert(0,str(base))
import e4lib as L
out=pathlib.Path(__file__).resolve().parent
keys=list(itertools.product(L.G,repeat=2));ind={k:i for i,k in enumerate(keys)}
parity=[(L.length(a)+L.length(b))%2 for a,b in keys]
# i-exponent decomposition; return pair real,imag ints.
def ev(p):
 a=b=0
 for e,c in p.items():
  t=e%4
  if t==0:a+=c
  elif t==1:b+=c
  elif t==2:a-=c
  else:b-=c
 return a,b
def mult_i(z,k):
 a,b=z
 return [(a,b),(-b,a),(-a,-b),(b,-a)][k%4]
ops=[]
for si,s in enumerate(L.S):
 O=[]
 for j,k in enumerate(keys):
  Z=L.tmulP({k:{0:1}},s);vec={}
  for l,p in Z.items():
   h=ind[l];a,b=mult_i(ev(p),parity[j]-parity[h]);assert b==0
   if a:vec[h]=a
  O.append(vec)
 ops.append(O)
def step(X,si):
 Y={}
 for j,c in X.items():
  for k,a in ops[si][j].items():Y[k]=Y.get(k,0)+c*a
 return {k:a for k,a in Y.items() if a}
# Exact rational row reduction. Pivot rows kept normalized.
piv=[]
def add_rank(X):
 x={k:Fraction(a) for k,a in X.items()}
 for j,r in piv:
  if j not in x:continue
  c=x[j]
  for k,a in r.items():
   z=x.get(k,0)-c*a
   if z:x[k]=z
   elif k in x:del x[k]
 if not x:return False
 j=min(x);c=x[j];x={k:a/c for k,a in x.items()};piv.append((j,x));return True
I={ind[(L.e,L.e)]:1};basis=[I];words=[()];add_rank(I);front=[0];start=time.time()
while front:
 nf=[]
 for j in front:
  for si in range(len(L.S)):
   Y=step(basis[j],si)
   if add_rank(Y):
    nf.append(len(basis));basis.append(Y);words.append(words[j]+(si+1,))
 front=nf
 print('rank',len(basis),'new',len(nf),'seconds',time.time()-start,flush=True)
# tau(T_aT_c) = 1 if c=a^-1, else 0.
def inv(w):return tuple(w.index(i) for i in range(len(w)))
invrows=[ind[(inv(a),inv(b))] for a,b in keys]
gram=[]
for X in basis:
 row=[]
 for Y in basis:
  row.append(sum(a*Y.get(invrows[j],0)*(-1 if parity[j] else 1) for j,a in X.items()))
 gram.append(row)
oldp=piv;piv=[]
for row in gram:add_rank({j:a for j,a in enumerate(row) if a})
res={'dimension_image':len(basis),'trace_gram_rank':len(piv),'words':words,'basis_integer_vectors':basis,'gram':gram,'seconds':time.time()-start,'scope':'Image subalgebra in the specialized ambient tensor Hecke algebra; not abstract order fiber and not E(4).'}
(out/('sign_specialization_rank%d_certificate.json'%L.n)).write_text(json.dumps(res,indent=2))
print('RESULT dimension',len(basis),'trace rank',len(piv),'seconds',time.time()-start,flush=True)
