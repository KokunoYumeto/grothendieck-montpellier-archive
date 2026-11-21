#!/usr/bin/env python3
"""Exact S3 outer-Nielsen closure of the mixed SU3(3) quotient; DELTA23."""
import json,pathlib,itertools,sys,numpy as np
import krammer_mixed_structure as k
HERE=pathlib.Path(__file__).resolve().parents[1]
data=json.loads((HERE/'records/krammer_mixed_correlation.json').read_text())
a,b=[np.array(x,dtype=np.int64) for x in data['pairs'][1]['unitary_generators']]
c=k.inverse(k.mm(a,b));I=np.eye(3,dtype=np.int64)
def det(g):
 out=0
 for p in itertools.permutations(range(3)):
  sign=2 if sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2 else 1
  v=sign
  for i in range(3):v=k.M[v,g[i,p[i]]]
  out=k.A[out,v]
 return int(out)
def normalize(g):return k.M[det(g),g]
pairs=[[normalize(x),normalize(y)] for x,y in [(a,b),(b,c),(c,a),(b,a),(c,b),(a,c)]]
assert all(det(g)==1 for p in pairs for g in p)
def key(g):return g.astype(np.int8).tobytes()
def red(w):
 out=[]
 for j in w:
  if out and out[-1]==-j:out.pop()
  else:out.append(j)
 return out
def wi(w):return [-j for j in w[::-1]]
def ev(p,w):
 ans=I.copy();gs={1:p[0],2:p[1],-1:k.inverse(p[0]),-2:k.inverse(p[1])}
 for j in w:ans=k.mm(ans,gs[j])
 return ans

def intertwiner(p,q,frob=False):
 pp=[np.vectorize(lambda x:int(k.N[x//3]*3+x%3)%9)(g) if False else g for g in p]
 if frob:pp=[np.array([[int(x%3)+3*(-int(x//3)%3) for x in row] for row in g]) for g in p]
 rows=[]
 for left,right in zip(pp,q):
  for i in range(3):
   for j in range(3):
    row=np.zeros(9,dtype=np.int64)
    for h in range(3):
     row[h*3+j]=k.A[row[h*3+j],left[i,h]]
     row[i*3+h]=k.A[row[i*3+h],k.N[right[h,j]]]
    rows.append(row)
 space=k.nullspace(rows)
 for j in range(space.shape[1]):
  ans=space[:,j].reshape(3,3)
  if k.rank(ans)==3:
   assert all(np.array_equal(k.mm(l,ans),k.mm(ans,r)) for l,r in zip(pp,q))
   return ans
 return None

def distinguish(p,q):
 els=[I.copy()];targets=[I.copy()];words=[[]];index={key(I):0};cursor=0
 while cursor<len(els):
  g=els[cursor];h=targets[cursor];word=words[cursor];cursor+=1
  for j in range(2):
   gg=k.mm(g,p[j]);hh=k.mm(h,q[j]);kk=key(gg)
   if kk not in index:
    index[kk]=len(els);els.append(gg);targets.append(hh);words.append(word+[j+1])
   else:
    m=index[kk]
    if not np.array_equal(hh,targets[m]):
     rel=red(word+[j+1]+wi(words[m]));assert np.array_equal(ev(p,rel),I)
     for gen in [1,2]:
      ww=red(rel+[gen]+wi(rel)+[-gen])
      if not np.array_equal(ev(q,ww),I):
       assert np.array_equal(ev(p,ww),I)
       assert all(sum((j==a)-(j==-a) for j in ww)==0 for a in [1,2])
       return {'word':ww,'target_matrix':ev(q,ww).tolist(),'source_elements_before_witness':len(els)}
     raise AssertionError('nonidentity central element in centerless SU')
 assert len(els)==6048
 return None

relations=[];different=[];equiv=np.eye(6,dtype=int)
for i in range(6):
 for j in range(i+1,6):
  hit=None
  for frob in [False,True]:
   J=intertwiner(pairs[i],pairs[j],frob)
   if J is not None:hit={'i':i,'j':j,'frobenius':frob,'J':J.tolist()};break
  if hit is not None:
   equiv[i,j]=equiv[j,i]=1;relations.append(hit)
  else:
   witness=distinguish(pairs[i],pairs[j]);assert witness is not None
   different.append({'i':i,'j':j,**witness})
classes=[];seen=set()
for i in range(6):
 if i not in seen:
  cl=list(map(int,np.flatnonzero(equiv[i])));classes.append(cl);seen.update(cl)
assert sorted(map(len,classes))==[2,2,2]
# Project all216 exact P7 solutions to the pair45 basis.
sys.path.insert(0,str(HERE.parent/'pentagon'))
from krammer_f9_probe import to3
from krammer_first_pair import mul,inv
raw=lambda v:to3(np.array(v)).astype(np.int16)
Cb=raw(data['C_full']);Ci=inv(Cb);Qb=raw(data['Q_full']);Qi=inv(Qb)
B45=raw(data['pairs'][1]['splitting_basis']);Bi=inv(B45)
solutions=np.load(HERE.parent/'pentagon/krammer_pentagon_solutions.npz');counts={};tested=[]
def from3(g):
 ans=np.empty((3,3),dtype=np.int64)
 for i in range(3):
  for j in range(3):
   aa,bb=int(g[2*i,2*j]),int(g[2*i+1,2*j]);ans[i,j]=aa+3*bb
   assert np.array_equal(g[2*i:2*i+2,2*j:2*j+2],np.array([[aa,-bb%3],[bb,aa]]))
 return ans
for ind,(R,label) in enumerate(zip(solutions['R'],solutions['labels'])):
 R=R.astype(np.int16);r=mul(mul(Ci,R),Cb);ri=inv(r)
 Av=mul(mul(mul(Qi,r),Qb),ri);Bv=mul(mul(Qi,ri),Qb)
 fullvals=[Av,Bv,r,inv(Av),inv(Bv),ri]
 vals=[from3(mul(mul(Bi,g),B45)[6:,6:]) for g in fullvals]
 checks=[]
 for rel in relations:
  g=vals[rel['i']]
  if rel['frobenius']:g=np.array([[int(x%3)+3*(-int(x//3)%3) for x in row] for row in g])
  J=np.array(rel['J']);target=k.mm(k.mm(k.inverse(J),g),J)
  checks.append(np.array_equal(target,vals[rel['j']]))
 ok=all(checks);lab=str(tuple(map(int,label)));counts.setdefault(lab,[0,0]);counts[lab][int(ok)]+=1
 tested.append({'index':ind,'label':list(map(int,label)),'all_kernel_correlations_pass':ok,'checks':list(map(bool,checks))})
result={'statement':'D23.C15','pair_order':['(a,b)','(b,c)','(c,a)','(b,a)','(c,b)','(a,c)'],'c':'(ab)^-1','normalized_SU_generators':[[x.tolist() for x in p] for p in pairs],'kernel_classes':classes,'same_kernel_intertwiners':relations,'different_kernel_commutator_witnesses':different,'P7_counts_fail_pass':counts,'P7_rows':tested,'result':'PASS exact kernel classification; candidate pass status listed explicitly'}
(HERE/'records/krammer_nielsen_perfect.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['kernel_classes','same_kernel_intertwiners','P7_counts_fail_pass']},indent=2))
