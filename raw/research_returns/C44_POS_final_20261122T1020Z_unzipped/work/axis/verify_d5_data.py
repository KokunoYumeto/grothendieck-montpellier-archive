"""Exact D5 algebra and moment arithmetic; not a geometric proof check."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json, math
G=list(product(range(5),range(2)))
def mul(x,y):return ((x[0]+(-1)**x[1]*y[0])%5,(x[1]+y[1])%2)
def inv(x):return ((-(-1)**x[1]*x[0])%5,x[1])
def add(a,b):return {g:a.get(g,0)+b.get(g,0) for g in G if a.get(g,0)+b.get(g,0)}
def scale(a,c):return {g:v*c for g,v in a.items() if v*c}
def prod(a,b):
 c={}
 for g,v in a.items():
  for h,w in b.items():
   k=mul(g,h);c[k]=c.get(k,0)+v*w
 return {g:v for g,v in c.items() if v}
def star(a):return {inv(g):v for g,v in a.items()}
one={(0,0):Q(1)};s={(0,1):Q(1)}
e1={g:Q(1,10) for g in G};es={g:Q((-1)**g[1],10) for g in G}
eu=add(add(one,scale(e1,-1)),scale(es,-1))
ep=scale(prod(eu,add(one,s)),Q(1,2));em=scale(prod(eu,add(one,scale(s,-1))),Q(1,2))
blocks=[e1,es,ep,em]
assert add(add(e1,es),add(ep,em))==one
for i,e in enumerate(blocks):
 assert prod(e,e)==e and star(e)==e
 for j,f in enumerate(blocks):
  if i!=j:assert prod(e,f)=={}
c={(1,0):Q(1),(4,0):Q(1)}
assert star(c)==c
for g in G:assert prod(c,{g:Q(1)})==prod({g:Q(1)},c)
assert prod(add(add(prod(c,c),c),scale(one,-1)),eu)=={}
# F=Q[tau]/(tau²+tau−1), encoded by a+b*tau.
def fa(x,y):return (x[0]+y[0],x[1]+y[1])
def fs(x,q):return (x[0]*q,x[1]*q)
def fm(x,y):return (x[0]*y[0]+x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def fp(x,n):
 y=(Q(1),Q(0))
 for _ in range(n):y=fm(y,x)
 return y
Z=(Q(0),Q(0));I=(Q(1),Q(0));tau=(Q(0),Q(1));tau2=(Q(-1),Q(-1))
weights=[fs(I,2),Z,tau,tau2]
character_norm=fs(fa(fs(I,4),fa(fs(fp(tau,2),2),fs(fp(tau2,2),2))),Q(1,10))
assert character_norm==I
moments=[]
for v in [Q(1,4),Q(1,9),Q(1,25)]:
 exact=Z
 for bits in product([0,1],repeat=len(weights)):
  val=Z
  for b,w in zip(bits,weights):val=fa(val,fs(w,Q(b)-v))
  pr=v**sum(bits)*(1-v)**(len(bits)-sum(bits))
  exact=fa(exact,fs(fp(val,4),pr))
 S2=Z;S4=Z
 for w in weights:S2=fa(S2,fp(w,2));S4=fa(S4,fp(w,4))
 mu4=v*(1-v)**4+(1-v)*v**4
 formula=fa(fs(fa(fp(S2,2),fs(S4,-1)),3*v*v*(1-v)**2),fs(S4,mu4))
 assert exact==formula
 moments.append({'v':str(v),'fourth_moment_F':[str(x) for x in exact]})
def coeff_pm(a,b,k):return sum(math.comb(a,j)*math.comb(b,k-j)*(-1)**(k-j) for j in range(k+1) if j<=a and k-j<=b)
h4=[math.comb(12,4),coeff_pm(4,8,4),0,0]
low=[sum((-1)**i*math.comb(12,i) for i in range(4)),sum((-1)**i*coeff_pm(4,8,i) for i in range(4)),0,0]
assert h4==[495,-17,0,0] and low==[-165,-5,0,0]
def mult_zero_rotation(ch):return [(ch[0]+5*ch[1])//10,(ch[0]-5*ch[1])//10,ch[0]//5,ch[0]//5]
assert mult_zero_rotation(h4)==[41,58,99,99]
assert mult_zero_rotation(low)==[-19,-14,-33,-33]
result={'scope':'Exact arithmetic only, no geometry or monodromy proof.','group_order':10,'four_self_adjoint_orthogonal_idempotents':True,'central_field_polynomial':'tau²+tau−1','central_polynomial_on_standard_part':True,'character_norm_squared':1,'H4_character':h4,'H4_absolute_multiplicities':mult_zero_rotation(h4),'lower_alternating_character':low,'lower_alternating_multiplicities':mult_zero_rotation(low),'moments':moments}
Path('work/axis/d5_arithmetic_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
