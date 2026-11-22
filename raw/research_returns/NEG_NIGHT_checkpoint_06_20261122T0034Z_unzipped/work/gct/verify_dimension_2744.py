"""Independent Laurent-polynomial verification of the new 2,744-pair lift.
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
W=poly([4,-7,2]);U={1:D,2:W}
V={1:poly([0,-3,2]),2:scale(W,3)}
C=poly([-1,1]);H=poly([0,-4,2])
delta={1:poly([0,-3,1]),2:poly([-4,15,-11,2])}
G={1:mul(D,H),2:mul(mul(D,W),C)}
S=mul(mul(power(D,2),C),H)
A={1:poly([0,0,-3,1]),2:poly([0,0,8,5,-9,2])}
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
result={'total_cancelling_pairs':total,'bottom_cancelling_pairs':bottom,'nonzero_constants':len(tab),'triples_checked':len(names)**3,'failures':{k:len(v) for k,v in fail.items()},'failure_details':fail,'parameters_D':{'W': [4, -7, 2], 'U1': [0, 1], 'U2': [4, -7, 2], 'C': [-1, 1], 'H': [0, -4, 2], 'delta1': [0, -3, 1], 'delta2': [-4, 15, -11, 2], 'G1': [0, 0, -4, 2], 'G2': [0, -4, 11, -9, 2], 'S': [0, 0, 0, 4, -6, 2], 'V1': [0, -3, 2], 'V2': [12, -21, 6], 'A1': [0, 0, -3, 1], 'A2': [0, 0, 8, 5, -9, 2], 'Lambda_note': 'Lambda_i=A_i/delta_i,rational functions'},'constants':[{'key':k,'dimension_q':a,'trace_q':true.get(k,{})} for k,a in sorted(tab.items())]}
trace_mass=sum(abs(v) for p in true.values() for v in p.values())
dimension_mass=sum(v for p in tab.values() for v in p.values())
anchors={1}|{e for p in true.values() for e in p if e>0}
n=dimension_mass//2+len(anchors);K=max(anchors);bound=n*(K+1)*4**(n-1)
assert (trace_mass,dimension_mass,n,K)==(4443,9931,4970,5)
assert bound<2**9953
result['improved_degree_cutoff']={'trace_mass':trace_mass,'dimension_mass':dimension_mass,
    'n':n,'anchors':sorted(anchors),'bound_expression':'29820 * 4^4969',
    'strict_power_two_bound':9953,'scope':'NN-G029 equal-score compression bound,not a bound on every realization.'}
Path('work/gct/dimension_certificate_2744.json').write_text(json.dumps(result,indent=2))
print(json.dumps({k:v for k,v in result.items() if k not in ['constants','failure_details']},indent=2))
assert total==2744 and bottom==1296 and not any(fail.values())
