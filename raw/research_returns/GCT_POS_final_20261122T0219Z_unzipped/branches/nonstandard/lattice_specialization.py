"""Necessary integral-closure test at v=2.
A=Z[v±] maps into Z[1/2]. Odd denominators in unique coordinates refute lattice equality.
"""
import pathlib,sys,json,time
from fractions import Fraction as F
base=pathlib.Path(__file__).resolve().parent/'dependencies';sys.path.insert(0,str(base))
import e4lib as L
out=pathlib.Path(__file__).resolve().parent
cert=json.loads((out/'mixed_cone_certificate.json').read_text());words=[tuple(r['word']) for r in cert['records']]
def ev(p):return sum(F(c)*F(2)**e for e,c in p.items())
def vec(X):return {k:a for k,p in X.items() if (a:=ev(p))}
def add(x,y,m):
 for k,a in y.items():
  z=x.get(k,F(0))+m*a
  if z:x[k]=z
  elif k in x:del x[k]
piv=[];elts=[];start=time.time()
for j,w in enumerate(words):
 X=L.word_elt(w);elts.append(X);x=vec(X);comb={j:F(1)}
 for pc,r,rep in piv:
  if pc not in x:continue
  a=x[pc];add(x,r,-a);add(comb,rep,-a)
 assert x
 pc=min(x);a=x[pc];r={k:c/a for k,c in x.items()};rep={k:c/a for k,c in comb.items()};piv.append((pc,r,rep))
 if j%20==0:print('basis',j+1,'seconds',time.time()-start,flush=True)
fail=None;count=0
for j,w in enumerate(words):
 for si,s in enumerate(L.S):
  Y=L.tmulP(elts[j],s);x=vec(Y);coeff={}
  for pc,r,rep in piv:
   if pc not in x:continue
   a=x[pc];add(x,r,-a);add(coeff,rep,a)
  assert not x,(w,si)
  count+=1
  bad={k:c for k,c in coeff.items() if c.denominator & (c.denominator-1)}
  if bad:
   fail={'source_word':w,'right_generator':si+1,'bad_coefficients':{str(k):str(c) for k,c in bad.items()},'all_coefficients':{str(k):str(c) for k,c in coeff.items()},'basis_words':words}
   print('ODD DENOMINATOR',w,si+1,list(bad.items())[:5],flush=True);break
 if fail:break
res={'tested_products':count,'failure':fail,'seconds':time.time()-start,'scope':'Unique coordinates in uncorrected basis; corrected basis differs by integral unipotent matrix.'}
(out/'lattice_specialization_certificate.json').write_text(json.dumps(res,indent=2))
print('RESULT','proper lattice' if fail else 'no necessary-test failure',time.time()-start,flush=True)
