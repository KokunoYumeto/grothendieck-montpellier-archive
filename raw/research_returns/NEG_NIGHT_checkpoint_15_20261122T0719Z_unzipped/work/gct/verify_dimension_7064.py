"""Independent Laurent-polynomial verification of the new 7,064-pair lift.
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
W=poly([-8,7]);U={1:poly([-16,13]),2:poly([-4,3])}
V={1:poly([2,-17,14]),2:poly([0,1,2])}
delta={1:poly([2,-3,1]),2:poly([2,-3,1])}
La={1:poly([-2,1]),2:poly([0,-10,3])}
G={1:poly([-32,76,-58,14]),2:poly([-16,38,-29,7])}
S=poly([-64,248,-376,278,-100,14])
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
  tab[a,b,f'g{i}_{z}']=mul(mul(delta[i],power(D,al)),power(La[i],be))
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
result={'total_cancelling_pairs':total,'bottom_cancelling_pairs':bottom,'nonzero_constants':len(tab),'triples_checked':len(names)**3,'failures':{k:len(v) for k,v in fail.items()},'failure_details':fail,'parameters_D':{'W':[-8,7],'U1':[-16,13],'U2':[-4,3],'delta':[2,-3,1],'Lambda1':[-2,1],'Lambda2':[0,-10,3],'G1':[-32,76,-58,14],'G2':[-16,38,-29,7],'S':[-64,248,-376,278,-100,14],'V1':[2,-17,14],'V2':[0,1,2]},'constants':[{'key':k,'dimension_q':a,'trace_q':true.get(k,{})} for k,a in sorted(tab.items())]}
Path('work/gct/dimension_certificate_7064.json').write_text(json.dumps(result,indent=2))
print(json.dumps({k:v for k,v in result.items() if k not in ['constants','failure_details']},indent=2))
assert total==7064 and bottom==6652 and not any(fail.values())
