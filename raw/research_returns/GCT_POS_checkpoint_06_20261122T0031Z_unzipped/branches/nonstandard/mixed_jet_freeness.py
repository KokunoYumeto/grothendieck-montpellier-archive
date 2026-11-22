"""Exact finite mixed-characteristic image of the full nonstandard Hecke order.
R=(Z/p^k)[e]/e^L, v=1+e. The ambient symmetric T-tensor space has rank300.
BFS closes the R-span of accepted P-words under every generator. Additive
Howell-style elimination over Z/p^k computes log_p cardinalities exactly.
mu(image)=log_p|M|-log_p|pM+eM|>114 would refute freeness of the full A-order.
An image value <=114 does NOT prove freeness.
"""
import pathlib,sys,argparse,itertools,math,json,time,collections,random,gzip
out=pathlib.Path(__file__).resolve().parent
sys.path.insert(0,str(out/'dependencies'))
import e4lib as H
ap=argparse.ArgumentParser();ap.add_argument('--p',type=int,default=3);ap.add_argument('--k',type=int,default=2);ap.add_argument('--length',type=int,default=8);ap.add_argument('--maxwords',type=int,default=3000)
a=ap.parse_args();prime=a.p;power=a.k;jetlen=a.length;modulus=prime**power
class Howell:
 def __init__(self,p,k):self.p=p;self.k=k;self.mod=p**k;self.rows={};self.valuations={};self.logsize=0
 def val(self,n):
  v=0
  while n%self.p==0:n//=self.p;v+=1
  return v
 def clean(self,x):return {j:c%self.mod for j,c in x.items() if c%self.mod}
 def axpy(self,x,r,c):
  for j,d in r.items():
   z=(x.get(j,0)+c*d)%self.mod
   if z:x[j]=z
   elif j in x:del x[j]
 def contains(self,x):
  x=self.clean(x)
  while x:
   j=min(x)
   if j not in self.rows:return False
   d=self.p**self.valuations[j]
   if x[j]%d:return False
   self.axpy(x,self.rows[j],-(x[j]//d))
  return True
 def add(self,x):
  queue=collections.deque([self.clean(x)]);oldsize=self.logsize
  while queue:
   x=queue.popleft()
   while x:
    j=min(x);b=self.val(x[j])
    if j in self.rows and b>=self.valuations[j]:
     self.axpy(x,self.rows[j],-(x[j]//self.p**self.valuations[j]));continue
    d=self.p**b;iv=pow(x[j]//d,-1,self.mod)
    x={t:c*iv%self.mod for t,c in x.items() if c*iv%self.mod}
    assert x[j]==d
    if j in self.rows:
     self.logsize+=self.valuations[j]-b;queue.append(self.rows[j])
    else:self.logsize+=self.k-b
    self.rows[j]=x;self.valuations[j]=b
    if b:
     f=self.p**(self.k-b)
     ann={t:c*f%self.mod for t,c in x.items() if c*f%self.mod}
     if ann:queue.append(ann)
    break
  return self.logsize>oldsize
 def verify(self):
  assert self.logsize==sum(self.k-v for v in self.valuations.values())
  for j,r in self.rows.items():
   assert min(r)==j and r[j]==self.p**self.valuations[j]
   assert self.contains({t:c*self.p**(self.k-self.valuations[j]) for t,c in r.items()})
 def serial(self):return [{'pivot':j,'valuation':self.valuations[j],'vector':r} for j,r in sorted(self.rows.items())]
def selftest():
 rng=random.Random(7161)
 for p,k,dim in [(2,2,3),(3,2,2),(2,3,2)]:
  m=p**k
  for trial in range(16):
   gs=[tuple(rng.randrange(m) for _ in range(dim)) for _ in range(3)];h=Howell(p,k)
   for g in gs:h.add(dict(enumerate(g)))
   span={tuple(sum(cc*gg[j] for cc,gg in zip(cs,gs))%m for j in range(dim)) for cs in itertools.product(range(m),repeat=3)}
   assert len(span)==p**h.logsize
   for x in itertools.product(range(m),repeat=dim):assert h.contains(dict(enumerate(x)))==(x in span)
   h.verify()
selftest();print('Howell brute-force self-check PASS',flush=True)
assert H.n in (2,3,4)
known_rank={2:2,3:10,4:114}[H.n]
keys=[(x,y) for x in H.G for y in H.G if x<=y];keyidx={x:j for j,x in enumerate(keys)};width=len(keys);dim=width*jetlen
assert width==math.factorial(H.n)*(math.factorial(H.n)+1)//2
# Generalized binomial coefficients expand v^exponent=(1+e)^exponent.
def jet(poly):
 z=[]
 for j in range(jetlen):
  val=0
  for exponent,c in poly.items():
   choose=math.comb(exponent,j) if exponent>=0 and j<=exponent else (0 if exponent>=0 else (-1)**j*math.comb(-exponent+j-1,j))
   val+=c*choose
  z.append(val%modulus)
 return z
ops=[]
for si,s in enumerate(H.S):
 base=[]
 for x,y in keys:
  X={(x,y):{0:1}}
  if x!=y:X[y,x]={0:1}
  Y=H.tmulP(X,s)
  for (u,w),c in Y.items():assert c==Y.get((w,u),{})
  base.append([(keyidx[u,w],j,c) for (u,w),pol in Y.items() if u<=w for j,c in enumerate(jet(pol)) if c])
 O=[]
 for e in range(jetlen):
  for j in range(width):O.append([(target+(e+h)*width,c) for target,h,c in base[j] if e+h<jetlen])
 ops.append(O)
def step(X,si):
 Y={}
 for j,c in X.items():
  for t,b in ops[si][j]:Y[t]=(Y.get(t,0)+c*b)%modulus
 return {t:c for t,c in Y.items() if c}
def shift(X):return {j+width:c for j,c in X.items() if j+width<dim}
def shifts(X):
 for _ in range(jetlen):
  yield X;X=shift(X)
M=Howell(prime,power);one={keyidx[H.e,H.e]:1};words=[()];vectors=[one]
for X in shifts(one):M.add(X)
idx=0;start=time.time();stats=[];complete=True
while idx<len(words):
 for si in range(H.n-1):
  X=step(vectors[idx],si)
  if M.contains(X):continue
  words.append(words[idx]+(si+1,));vectors.append(X)
  for Y in shifts(X):M.add(Y)
  if len(words)%20==0:
   st={'accepted_words':len(words),'processed':idx,'max_length':max(map(len,words)),'log_size':M.logsize,'pivots':len(M.rows),'seconds':time.time()-start};stats.append(st);print(st,flush=True)
  if len(words)>=a.maxwords:complete=False;break
 if not complete:break
 idx+=1
M.verify()
if complete:
 for X in vectors:
  assert M.contains(shift(X))
  for si in range(H.n-1):assert M.contains(step(X,si))
 N=Howell(prime,power)
 for X in vectors:
  for j,Y in enumerate(shifts(X)):
   if j:N.add(Y)
   else:N.add({t:c*prime for t,c in Y.items()})
 N.verify()
 for r in M.rows.values():
  assert N.contains({t:c*prime for t,c in r.items()})
  assert N.contains(shift(r))
 mu=M.logsize-N.logsize
else:N=None;mu=None
record={'strand_rank':H.n,'known_generic_rank':known_rank,'p':prime,'k':power,'jet_length':jetlen,'modulus':modulus,'ambient_symmetric_rank':width,'closure_complete':complete,'accepted_words':words,'log_p_size_M':M.logsize,'log_p_size_mM':None if N is None else N.logsize,'minimal_generators_image':mu,'max_word_length':max(map(len,words)),'seconds':time.time()-start,'stats':stats,'interpretation':'mu>114 proves full integral order nonfree; mu<=114 is inconclusive.'}
stem=('mixed_jet_' if H.n==4 else 'mixed_jet_r%d_'%H.n)+'p%d_k%d_L%d'%(prime,power,jetlen)
(out/(stem+'.json')).write_text(json.dumps(record,indent=2))
with gzip.open(out/(stem+'_rows.json.gz'),'wt') as f:json.dump({'M':M.serial(),'mM':None if N is None else N.serial()},f)
print('RESULT',json.dumps({k:v for k,v in record.items() if k not in ('accepted_words','stats')}),flush=True)
