from pathlib import Path
from functools import lru_cache
import json
from fixed_twist_arrangement import normal_schur
from first_power_zero_twist import complete_values
@lru_cache(None)
def A(eta,eps,h):
 if h<0:return 0
 v=[1]+[0]*h
 for ell in eta:
  for sign in (1,eps**ell):
   for i in range(ell,h+1):v[i]+=sign*v[i-ell]
 return v[h]
checks=0
for k in range(2,9):
 for eta in ((1,1,1),(2,1),(3,)):
  coeff=normal_schur(eta,k)
  for eps in (1,-1):
   for t in range(k):
    b=3*(k-1)-t
    for c in range(5):
     for x in range(2*k+1):
      alpha=(b+x+c,b+c,c);N=sum(alpha)
      actual=sum(v*eps**(N-sum(rho)) for rho,v in coeff
       if alpha[0]>=rho[0]>=alpha[1]>=rho[1]>=alpha[2]>=rho[2]>=0)
      h=complete_values(eta,c)[c]
      expected=eps**((x+c+k-1)%2)*h*(A(eta,eps,t-2*c)-A(eta,eps,t-x-2*c-1))
      assert actual==expected,(k,eta,eps,t,c,x,actual,expected)
      checks+=1
r={'statement':'rank-three triple identity candidate','checks':checks,'k':'2..8','c':'0..4','t':'0..k-1','x':'0..2k','selected_cycles':['111','21','3'],'epsilon':[1,-1],'outcome':'PASS'}
Path('work/root/RANK3_TRIPLE_IDENTITY_CHECK.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r))
