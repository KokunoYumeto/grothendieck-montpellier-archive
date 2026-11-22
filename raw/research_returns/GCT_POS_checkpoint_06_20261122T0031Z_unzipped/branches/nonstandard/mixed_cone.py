"""Unimodular triangular cone repair of 114 independent P-words.
This is a basis of its explicitly generated A-lattice, not yet of the full A-algebra.
"""
import pathlib,sys,json,time
# Reuse definitions only (not the search).
p=pathlib.Path(__file__).resolve().parent
src=(p/'cone_search.py').read_text().split('checks()\nstart=')[0]
exec(compile(src,str(p/'cone_search.py'),'exec'))
data=json.loads((p/'cone_search_progress.json').read_text())
candidate_words=[tuple(w) for w in data['positive_basis']]+[tuple(w) for w in data['basis']]
words=[]; pv=[]
for w in candidate_words:
 X=L.ONE_T
 for i in w:X=step(X,i-1)
 if add_rank(X,pv): words.append(w)
S={};records=[];failure=[];start=time.time()
def scale(X,p):return {k:L.pmul(q,p) for k,q in X.items()}
def add(X,Y,m=1):
 Z={k:dict(p) for k,p in X.items()}
 for k,p in Y.items():acc(Z,k,p,m)
 return Z
def dpow(n):
 p={0:1}
 for _ in range(n):p=L.pmul(p,D)
 return p
# Cap coefficient growth: choose donor separately per bad coordinate.
corrected=[]
for j,w in enumerate(words):
 X=L.ONE_T
 for i in w:X=step(X,i-1)
 Y={k:dict(p) for k,p in X.items()};corr=[]
 neg=[(key,e,-c) for key,p0 in X.items() for e,c in p0.items() if c<0]
 for key,e,mag in neg:
  if Y.get(key,{}).get(e,0)>=0:continue
  donors=[]
  for i,B in enumerate(corrected):
   if key not in B:continue
   for k in range(10):
    co=L.pmul(B[key],dpow(k)).get(e,0)
    if co>0:
     donors.append((k,sum(abs(c) for p0 in B.values() for c in p0.values()),i,co));break
  if not donors:
   failure.append({'index':j,'word':w,'coordinate':key,'exp':e});continue
  k,_,i,co=min(donors)
  a=(-Y[key][e]+co-1)//co
  Y=add(Y,scale(corrected[i],dpow(k)),a)
  corr.append({'donor_index':i,'D_power':k,'multiple':a})
 if not positive(Y):
  failure.append({'index':j,'word':w,'uncorrected':True})
  print('FAIL',j,w,flush=True);break
 corrected.append(Y);records.append({'index':j,'word':w,'corrections':corr,'coordinates':len(Y),'max_abs_coeff':max(abs(c) for p0 in Y.values() for c in p0.values())})
 print('basis',j+1,'word',''.join(map(str,w)),'corrections',len(corr),flush=True)
result={'count':len(corrected),'records':records,'failures':failure,'seconds':time.time()-start,'scope':'Unipotent triangular transformation of the stated A-lattice; no full-algebra lattice claim.'}
(p/'mixed_cone_certificate.json').write_text(json.dumps(result,indent=2))
print('RESULT',len(corrected),'failures',len(failure),'seconds',time.time()-start)
