#!/usr/bin/env python3
"""Exact U13 trace computation, including coefficients with enormous original index.

No iteration through 13^6*n coefficients is needed. Newton sums on X0(13)
compute U13 on powers of z=(eta(13tau)/eta(tau))². Source formula: Maier2009,
Tables 2, 4 and 5; our coordinate is 1/z, the Fricke transform of t13=13*z.
All divisions are checked before reduction. Finite q-expansion verification is
independent of the trace recurrence and is included below.
"""
from pathlib import Path
import sympy as s,json,time
from qseries import conv,inv,power,euler,j_coefficients
tic=time.monotonic();p=13;alpha=8;mod=p**alpha;MAXD=100;precision=p**(MAXD+alpha+1)
T=s.symbols('T')
F=s.Poly((T*T+5*T+13)*(T**4+247*T**3+3380*T*T+15379*T+28561)**3,T)
Q=s.Poly((T*T+5*T+13)*(T**4+7*T**3+20*T*T+19*T+1)**3,T)
fricke=s.factor(T**13*F.as_expr().subs(T,13/T)/13**13-Q.as_expr()/T)
# j(z)=z^-1+746+sum Ai z^i, 1<=i<=13.
J={13-k:int(v) for(k,),v in F.terms()};assert J[-1]==1 and J[0]==746
c1={k:-v for k,v in J.items() if k!=0}
cs={r:int(Q.nth(r))*13**(r-1) for r in range(2,15)}
S={};U={};negative_residuals=[]
for n in range(1,MAXD+1):
 cur={}
 if n==1:
  cur={k:-v%precision for k,v in c1.items()}
 else:
  for k,v in S[n-1].items():
   for j,b in c1.items():cur[k+j]=(cur.get(k+j,0)-v*b)%precision
  for r in range(2,min(n-1,14)+1):
   for k,v in S[n-r].items():cur[k]=(cur.get(k,0)-cs[r]*v)%precision
  if n<=14:cur[0]=(cur.get(0,0)-n*cs[n])%precision
  elif n>14:
   # The loop already included r=14 once n>=15.
   pass
 S[n]={k:v%precision for k,v in cur.items() if v%precision}
 cur=dict(S[n]);cur[-n]=(cur.get(-n,0)-1)%precision
 assert all(v%precision==0 for k,v in cur.items() if k<=0),(n,[(k,v) for k,v in cur.items() if k<=0 and v])
 divisor=13**(n+1);col={}
 for k,v in cur.items():
  if k<=0:continue
  assert v%divisor==0,(n,k,'non-integral trace')
  a=(v//divisor)%mod
  if a:col[k]=a
 U[n]=col
 if n-14 in S:del S[n-14]
# Initial U(j-744): U(z^-1)=-2-z and constant2 cancel.
v={1:mod-1}
for n,a in J.items():
 if n<=0:continue
 for k,b in U[n].items():v[k]=(v.get(k,0)+a*b)%mod
v={k:a for k,a in v.items() if a};iters={1:v.copy()}
for step in range(2,9):
 assert max(v)<=MAXD,(step,max(v))
 new={}
 for n,a in v.items():
  for k,b in U[n].items():new[k]=(new.get(k,0)+a*b)%mod
 v={k:a for k,a in new.items() if a};iters[step]=v.copy()
# Evaluate each polynomial in z(q), only through the largest output index.
N=5300;f=euler(N,mod);fi=inv(f,N,mod);f13=[0]*N
for k in range((N-1)//13+1):f13[13*k]=f[k]
z=[0]+conv(power(f13,2,N-1,mod),power(fi,2,N-1,mod),N-1,mod)
def evaluate(poly,length=N):
 a=[0]
 for k in range(max(poly),-1,-1):
  a=conv(a,z,length,mod);a+=[0]*(length-len(a));a[0]=(a[0]+poly.get(k,0))%mod
 return a
qiters={k:evaluate(v) for k,v in iters.items()}
# Direct E4^3/Delta through13*200 is an independent check of the trace columns.
direct=j_coefficients(13*200,mod)
assert all(qiters[1][n]==direct[13*n] for n in range(1,201))
# Check U^2 against direct coefficients through13²*15.
assert all(qiters[2][n]==direct[169*n] for n in range(1,16))
def vp(n):
 if n==0:return f'>={alpha}'
 v=0
 while n%13==0:n//=13;v+=1
 return v
indices=[7,11,77,154,757,5299]
table=[{'n':n,'c(13^6*n)_mod13^8':qiters[6][n],'valuation':vp(qiters[6][n])} for n in indices]
checks=[]
for a in range(1,9):
 M=13**a;c1q=qiters[a][1];norm=[v*pow(c1q,-1,M)%M for v in qiters[a]]
 bad=[];count=0
 for ell in [2,3,5,7,11,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]:
  for n in range(1,min(1000//ell,(N-1)//ell)+1):
   count+=1;rhs=(norm[n]*norm[ell]-(norm[n//ell]*pow(ell,-1,M) if n%ell==0 else 0))%M
   if norm[n*ell]!=rhs:bad.append([ell,n])
 checks.append({'alpha':a,'unit_denominator_modulus':c1q%M,'pairs':count,'failures':bad})
out={'method':'Newton power sums of scaled roots13*z((tau+k)/13) on X0(13), remove the extra root1/z, divide by13^(n+1); exact modular arithmetic','modulus':mod,'fricke_residual':str(fricke),'basis_max_degree_computed':MAXD,'iteration_polynomial_degrees':{k:max(v) for k,v in iters.items()},'independent_direct_checks':{'U13_n_through':200,'U13_squared_n_through':15,'all_pass':True},'archival_scan46_table':table,'normalized_Hecke_finite_checks':checks,'elapsed_seconds':time.monotonic()-tic}
path=Path(__file__).resolve().parents[1]/'outputs/c63_u13.json';path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
matrixpath=path.with_name('c63_u13_trace_matrix.json');matrixpath.write_text(json.dumps({'modulus':mod,'columns':U,'iterates':iters},indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
