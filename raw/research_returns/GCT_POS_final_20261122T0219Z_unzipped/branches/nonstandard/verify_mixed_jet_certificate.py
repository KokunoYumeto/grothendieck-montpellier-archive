"""Independent jet certificate replay.
Rebuild accepted words as full Laurent standard-T polynomials, then specialize.
Compute cardinalities a second way: iterated unit-pivot elimination and division
by p, giving Smith valuations. Do not import the search/Howell insertion code.
"""
import pathlib,sys,json,gzip,math,collections,time
out=pathlib.Path(__file__).resolve().parent;sys.path.insert(0,str(out/'dependencies'))
import e4lib as H
stem=sys.argv[1] if len(sys.argv)>1 else 'mixed_jet_p2_k10_L8'
cert=json.loads((out/(stem+'.json')).read_text());stored=json.load(gzip.open(out/(stem+'_rows.json.gz'),'rt'))
p=cert['p'];k=cert['k'];L=cert['jet_length'];m=p**k
keys=[(a,b) for a in H.G for b in H.G if a<=b];ix={v:j for j,v in enumerate(keys)};w=len(keys);ambient=w*L
assert w==cert['ambient_symmetric_rank']
def axpy(x,y,c,mod):
 for j,d in y.items():
  z=(x.get(j,0)+c*d)%mod
  if z:x[j]=z
  elif j in x:del x[j]
def normalize(x,mod):return {j:c%mod for j,c in x.items() if c%mod}
def shift(x):return {j+w:c for j,c in x.items() if j+w<ambient}
def multp(x):return normalize({j:p*c for j,c in x.items()},m)
def jets_of_word(word):
 X=H.word_elt(tuple(word));result={}
 for (a,b),f in X.items():
  assert f==X.get((b,a),{})
  if a>b:continue
  for j in range(L):
   value=0
   for exponent,c in f.items():
    if exponent<0:bc=(-1)**j*math.comb(-exponent+j-1,j)
    else:bc=math.comb(exponent,j) if j<=exponent else 0
    value+=c*bc
   if value%m:result[ix[a,b]+j*w]=value%m
 return result
# Membership and cardinality from the stored triangular certificate.
def read_rows(name):
 rows={r['pivot']:{int(j):c for j,c in r['vector'].items()} for r in stored[name]}
 vals={r['pivot']:r['valuation'] for r in stored[name]}
 return rows,vals
def remainder(x,rows,vals):
 x=normalize(x,m)
 while x:
  j=min(x)
  if j not in rows or x[j]%(p**vals[j]):return x
  axpy(x,rows[j],-x[j]//(p**vals[j]),m)
 return x
def check_triangular(rows,vals):
 for j,r in rows.items():
  assert min(r)==j and r[j]==p**vals[j]
  annihilator={t:c*p**(k-vals[j]) for t,c in r.items()}
  assert not remainder(annihilator,rows,vals)
 return sum(k-a for a in vals.values())
MR,MV=read_rows('M');NR,NV=read_rows('mM')
assert check_triangular(MR,MV)==cert['log_p_size_M']
assert check_triangular(NR,NV)==cert['log_p_size_mM']
# Independent elementary-divisor method. Each unit row contributes k-level
# to log_p size; the all-p-divisible residual is divided and processed again.
def smith_log_size(generators):
 pending=[normalize(x,m) for x in generators if normalize(x,m)];count=0;counts=[]
 for level in range(k):
  mod=p**(k-level);units=[];deferred=[]
  for source in pending:
   x=dict(source)
   for j,r in units:
    if j in x:axpy(x,r,-x[j],mod)
   if not x:continue
   odd=[j for j,c in x.items() if c%p]
   if not odd:deferred.append(x);continue
   j=min(odd);iv=pow(x[j],-1,mod);x={t:c*iv%mod for t,c in x.items() if c*iv%mod}
   assert x[j]==1;units.append((j,x))
  nxt=[]
  for x in deferred:
   for j,r in units:
    if j in x:axpy(x,r,-x[j],mod)
   assert all(c%p==0 for c in x.values())
   y={j:c//p for j,c in x.items() if c//p}
   if y:nxt.append(y)
  counts.append(len(units));count+=(k-level)*len(units);pending=nxt
  print('Smith level',level,'unit pivots',len(units),'residual rows',len(pending),flush=True)
 assert not pending
 return count,counts
start=time.time();words=cert['accepted_words'];gens=[jets_of_word(word) for word in words]
MG=[];NG=[]
for x in gens:
 for j in range(L):
  assert not remainder(x,MR,MV)
  MG.append(x)
  y=x if j else multp(x)
  assert not remainder(y,NR,NV)
  NG.append(y);x=shift(x)
sizeM,smithM=smith_log_size(MG);sizeN,smithN=smith_log_size(NG)
assert sizeM==cert['log_p_size_M'] and sizeN==cert['log_p_size_mM']
# Equality of the generated modules follows from inclusion and equal cardinality.
# Closure is checked from actual appended words, using the Laurent path again.
for word in words:
 for si in range(1,H.n):assert not remainder(jets_of_word(word+[si]),MR,MV),(word,si)
for r in MR.values():
 assert not remainder(shift(r),MR,MV)
 assert not remainder(multp(r),NR,NV)
 assert not remainder(shift(r),NR,NV)
mu=sizeM-sizeN
assert mu==cert['minimal_generators_image']
result={'certificate':stem,'reconstructed_words':len(words),'closure_products_checked':len(words)*(H.n-1),'laurent_then_jet_replay':True,'independent_Smith_levels_M':smithM,'independent_Smith_levels_mM':smithN,'log_p_size_M':sizeM,'log_p_size_mM':sizeN,'minimal_generators_image':mu,'seconds':time.time()-start}
(out/(stem+'_independent_verification.json')).write_text(json.dumps(result,indent=2))
print('PASS',json.dumps(result),flush=True)
