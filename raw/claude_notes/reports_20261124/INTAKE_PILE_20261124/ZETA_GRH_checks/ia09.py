import cmath, math
def prim_root(p):
  for g in range(2,p):
    if all(pow(g,(p-1)//q,p)!=1 for q in set(f for f in range(2,p) if (p-1)%f==0 and all(f%k for k in range(2,int(f**.5)+1)))): return g
worst=0
for p in [3,5,7,11,13,101,211,997]:
  g=prim_root(p); ind={pow(g,k,p):k for k in range(p-1)}
  vals=[]
  for j in range(p-1):
    if j%2==1:  # odd character: chi(-1)=(-1)^j... chi(g)=e^{2pi i j/(p-1)}, chi(-1)=e^{pi i j}
      S=sum(a*cmath.exp(-2j*math.pi*j*ind[a]/(p-1)) for a in range(1,p))
      vals.append(math.pi/p**1.5*abs(S))
  mean2=sum(v*v for v in vals)/len(vals)
  print(p, 'min|L(1,chi)|=%.4f'%min(vals),'mean sq=%.6f formula=%.6f'%(mean2, math.pi**2*(p-1)*(p-2)/(6*p*p)),'bound pi/sqrt6=%.4f'%(math.pi/math.sqrt(6)))
