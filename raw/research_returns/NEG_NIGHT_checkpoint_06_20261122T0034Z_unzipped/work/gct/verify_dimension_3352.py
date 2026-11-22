"""Independent Laurent-polynomial verification of the new 3,352-pair lift.
Does not import supplied dimension-ring builders. Exact integer dictionaries.
Author: /root/gct, GPT-6 Astra Pro (inherited); effort not exposed.
"""
from pathlib import Path
from itertools import product
from collections import defaultdict
import json
import sympy as sp

def add(a,b):
 o=dict(a)
 for k,v in b.items():
  o[k]=o.get(k,0)+v
  if o[k]==0:del o[k]
 return o

def scale(a,z):return {k:z*v for k,v in a.items() if z*v}
def mul(a,b):
 o={}
 for i,x in a.items():
  for j,y in b.items():o[i+j]=o.get(i+j,0)+x*y
 return {k:v for k,v in o.items() if v}
def power(a,n):
 o={0:1}
 for _ in range(n):o=mul(o,a)
 return o
D={-1:1,0:2,1:1}
def poly(co):
 o={}
 for n,c in enumerate(co):o=add(o,scale(power(D,n),c))
 return o
W=poly([0,3]);U={1:poly([0,3]),2:poly([0,1])}
V={1:poly([0,15]),2:poly([-4,1,2])}
h=poly([1,-3,1]);B=poly([10,-17,5])
delta={1:add(scale(h,6),scale(B,-1)),2:add(B,scale(h,-2))}
# Actual beta=1 products; auxiliary Lambda_i=A_i/delta_i are rational functions.
G={1:scale(mul(D,h),6),2:mul(D,B)}
S=scale(mul(mul(D,h),B),2)
A={1:add(scale(mul(power(D,2),h),6),scale(mul(B,D),-5)),
   2:add(mul(power(D,2),B),scale(mul(h,V[2]),-2))}
words=('1','12','2','21')
names=['mu','Sigma']+[f'g{i}_{x}' for i in (1,2) for x in words]
# All local reductions: remove doubled junction, then each alternating length3 contributes Lambda.
def red(word):
 compressed=[];alpha=0
 for ch in word:
  if compressed and compressed[-1]==ch:alpha+=1
  else:compressed.append(ch)
 beta=(len(compressed)-1)//2
 z=compressed[0] if len(compressed)%2 else compressed[0]+compressed[-1]
 return z,alpha,beta

tab={}
for b in names:tab['mu',b,b]={0:1};tab[b,'mu',b]={0:1}
tab['Sigma','Sigma','Sigma']=S
for i in (1,2):
 for x in words:
  a=f'g{i}_{x}';g=mul(power(D,len(x)-1),G[i])
  tab['Sigma',a,'Sigma']=g;tab[a,'Sigma','Sigma']=g
for i,j,x,y in product((1,2),(1,2),words,words):
 a,b=f'g{i}_{x}',f'g{j}_{y}'
 if i!=j:tab[a,b,'Sigma']=mul(power(D,len(x)+len(y)-2),W)
 else:
  z,al,be=red(x+y)
  tab[a,b,f'g{i}_{z}']=mul(delta[i] if be==0 else A[i],power(D,al))
  if be==0:
   tab[a,b,'Sigma']=mul(power(D,len(z)+al-2),U[i])
  else:
   tab[a,b,'Sigma']=mul(power(D,len(z)+al-1),V[i])
# Symbolic input conversion only; no source multiplication code is used.
v=sp.Symbol('v');true={}
for row in json.loads(Path('sources/OURS_E4_scripts/e3_constants.json').read_text()):
 ex=sp.Poly(sp.expand(sp.sympify(row['c'],locals={'v':v})*v**40),v)
 out={}
 for (e,),c in ex.terms():
  assert (e-40)%2==0
  out[(e-40)//2]=int(c)
 true[row['b'],row['bp'],row['bpp']]=out
fail={'nonnegative':[],'domination':[],'parity':[],'associativity':[]}
total=bottom=0
for key in set(tab)|set(true):
 a,b=tab.get(key,{}),true.get(key,{})
 for e in set(a)|set(b):
  x,y=a.get(e,0),b.get(e,0)
  if x<0:fail['nonnegative'].append([key,e,x])
  if x<abs(y):fail['domination'].append([key,e,x,y])
  if (x-y)%2:fail['parity'].append([key,e,x,y])
  h=(x-abs(y))//2;total+=h
  if key[2]=='Sigma':bottom+=h

def multiply(u,w):
 out={}
 for a,ca in u.items():
  for b,cb in w.items():
   cab=mul(ca,cb)
   for z in names:
    if (a,b,z) in tab:out[z]=add(out.get(z,{}),mul(cab,tab[a,b,z]))
 return {k:v for k,v in out.items() if v}
for a,b,c in product(names,repeat=3):
 left=multiply(multiply({a:{0:1}},{b:{0:1}}),{c:{0:1}})
 right=multiply({a:{0:1}},multiply({b:{0:1}},{c:{0:1}}))
 if left!=right:fail['associativity'].append([a,b,c])
result={'total_cancelling_pairs':total,'bottom_cancelling_pairs':bottom,'nonzero_constants':len(tab),'triples_checked':len(names)**3,'failures':{k:len(v) for k,v in fail.items()},'failure_details':fail,'parameters_D':{'W':[0,3],'U1':[0,3],'U2':[0,1],'H':[1,-3,1],'J':[10,-17,5],'delta1':[-4,-1,1],'delta2':[8,-11,3],'G1':[0,6,-18,6],'G2':[0,10,-17,5],'S':[0,20,-94,132,-64,10],'V1':[0,15],'V2':[-4,1,2],'A1':[0,-50,91,-43,6],'A2':[8,-26,20,-7,1],'Lambda_note':'Lambda_i=A_i/delta_i,rational functions'},'constants':[{'key':k,'dimension_q':a,'trace_q':true.get(k,{})} for k,a in sorted(tab.items())]}
Path('work/gct/dimension_certificate_3352.json').write_text(json.dumps(result,indent=2))
print(json.dumps({k:v for k,v in result.items() if k not in ['constants','failure_details']},indent=2))
assert total==3352 and bottom==2752 and not any(fail.values())
