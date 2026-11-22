"""Exact checks accompanying NN-G030; no search or proof replacement."""
from pathlib import Path
import json
j=json.loads(Path('work/gct/dimension_certificate_3352.json').read_text())['parameters_D']
def add(a,b):
 n=max(len(a),len(b));return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)]
def scale(a,k):return [k*x for x in a]
def mul(a,b):
 z=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for k,y in enumerate(b):z[i+k]+=x*y
 return z
D=[0,1];sigma=[0,-1,1]
G1=j['G1'];G2=j['G2'];S=j['S'];delta2=j['delta2'];A2=j['A2']
residues=[add(S,scale(mul(sigma,G1),-1)),add(add(G2,scale(mul(D,delta2),-1)),scale(G1,-1)),add(add(mul(D,G2),scale(A2,-1)),scale(G1,-1))]
assert all(all(c%4==0 for c in r) for r in residues)
assert G1[0]%4==0 and all(c%2==0 for c in G1)
assert all(p[0]%4==0 and p[1]%2==0 for p in [G2,A2])
B=[c//2 for c in G1[1:]]
assert all(c%4==0 for c in add(S,scale(mul([0,0,-2,2],B),-1)))
assert G1[1]%4==2 and S[2]%4==2
x={'w':10,'g1':70,'g2':90,'s':630,'d1':4,'d2':12,'u1':6,'u2':6,'v1':30,'v2':48,'a1':10,'a2':24}
assert x['w']*x['s']==x['g1']*x['g2']
for i in (1,2):
 assert x['u'+str(i)]*x['s']==x['g'+str(i)]*(x['g'+str(i)]-4*x['d'+str(i)])
 assert x['v'+str(i)]*x['s']==x['g'+str(i)]*(4*x['g'+str(i)]-x['a'+str(i)])
assert all(v%2==0 for v in x.values())
T=x['s']+20*(x['g1']+x['g2'])+200*x['w']+20*(x['u1']+x['u2']+x['v1']+x['v2'])+26*(x['d1']+x['d2'])+14*(x['a1']+x['a2'])
assert T==8522 and (T-4424)//2==2049
violations={k:v for k,v in x.items() if k in ['g1','g2','s','a2'] and v%4}
assert violations=={'g1':70,'g2':90,'s':630}
out={'attainer_polynomial_congruences_checked':3,'attainer_ideal_memberships_checked':True,
     'coefficientwise_divisibility_by4_not_claimed':{'G1_D_coefficient':G1[1],'S_D2_coefficient':S[2]},
     'scalar_candidate':x,'scalar_associativity_and_evenness':True,'relaxed_mass':T,
     'relaxed_score':2049,'violated_necessary_mod4_mass_conditions':violations,
     'scope':'Excluded scalar relaxation point only;no actual2049-pair table was constructed.'}
Path('work/gct/mod4_obstruction_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
