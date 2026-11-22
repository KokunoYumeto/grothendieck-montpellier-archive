from mpmath import mp
from collections import Counter
mp.dps=75

def loglocal(w,signs,n,a):
 M=2**(n-1)
 num=Counter()
 for e in range(3):
  for i in w:
   for j in w:
    if i!=j:num[(signs[e]*(i-j))%M]+=1
 den=Counter((signs[0]*i+signs[1]*j+signs[2]*k)%M for i in w for j in w for k in w)
 zero=den.pop(0,0)
 result=mp.mpc(0)
 for k,c in (num-den).items(): pass
 for k in set(num)|set(den):
  c=num[k]-den[k]
  if c:result+=c*mp.log(1-mp.exp(2j*mp.pi*a*k/M))
 return result,zero
for n in range(4,17):
 M=2**(n-1);chain=[(-2)**i%M for i in range(n-1)]+[0];second=[0]+[2**i for i in range(n-1)]
 for a in [1,pow(3,-1,M)]:
  lc,zc=loglocal(chain,[1,1,1],n,a);ls,zs=loglocal(second,[1,-1,-1],n,a)
  ratio=mp.exp(ls-lc)
  print('n',n,'a',a,'zero',zc,zs,'log2_abs_second_over_chain',mp.nstr((ls-lc).real/mp.log(2),18),'phase_pi',mp.nstr(mp.arg(ratio)/mp.pi,10),flush=True)
