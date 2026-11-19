"""Exact modular power series via carry-free integer packing (standard-library only)."""
def conv(a,b,N,mod):
 if not a or not b or N<=0:return[]
 a=[int(x)%mod for x in a[:N]];b=[int(x)%mod for x in b[:N]]
 size=min(N,len(a)+len(b)-1)
 width=(2*mod.bit_length()+min(len(a),len(b)).bit_length()+7)//8
 A=int.from_bytes(b''.join(x.to_bytes(width,'little') for x in a),'little')
 B=int.from_bytes(b''.join(x.to_bytes(width,'little') for x in b),'little')
 raw=(A*B).to_bytes(width*(len(a)+len(b)),'little')
 return[int.from_bytes(raw[width*i:width*(i+1)],'little')%mod for i in range(size)]
def inv(a,N,mod):
 g=[pow(int(a[0]),-1,mod)]
 while len(g)<N:
  n=min(2*len(g),N);fg=conv(a[:n],g,n,mod);fg+= [0]*(n-len(fg))
  h=[(-v)%mod for v in fg];h[0]=(h[0]+2)%mod
  g=conv(g,h,n,mod)
 return g[:N]
def power(a,k,N,mod):
 out=[1];b=a[:N]
 while k:
  if k&1:out=conv(out,b,N,mod)
  k//=2
  if k:b=conv(b,b,N,mod)
 return out
def euler(N,mod):
 a=[0]*N;a[0]=1;k=1
 while k*(3*k-1)//2<N:
  for j in[k*(3*k-1)//2,k*(3*k+1)//2]:
   if j<N:a[j]=(1 if k%2==0 else-1)%mod
  k+=1
 return a
def eisenstein(k,N,mod):
 factor={2:-24,4:240,6:-504}[k];a=[0]*N;a[0]=1
 for d in range(1,N):
  v=factor*pow(d,k-1,mod)
  for n in range(d,N,d):a[n]=(a[n]+v)%mod
 return a
def j_coefficients(N,mod):
 # Return c(n), -1<=n<=N, including c(0)=744.
 length=N+2;f=euler(length,mod);Delta_over_q=power(f,24,length,mod)
 E4=eisenstein(4,length,mod)
 a=conv(power(E4,3,length,mod),inv(Delta_over_q,length,mod),length,mod)
 return{n:a[n+1] for n in range(-1,N+1)}
