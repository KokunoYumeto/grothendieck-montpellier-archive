#!/usr/bin/env python3
"""Finite coefficient and CM-table audits of the computations copied in cote 63.

Exact integer recurrences, independently checked packed series, and explicitly
labelled high-precision (not interval-certified) complex evaluations. Finite
congruence checks are never substituted for an all-index literature theorem.
"""
from pathlib import Path
import json,math,time,random
import sympy as s
import mpmath as mp
from qseries import conv,inv,power,euler,eisenstein,j_coefficients
tic=time.monotonic(); out={}
def naive(a,b,N,M):
 c=[0]*min(N,len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):
   if i+j<len(c):c[i+j]=(c[i+j]+x*y)%M
 return c
rng=random.Random(63)
for M in [17,13**8,2**64,10**90+7]:
 a=[rng.randrange(-M,M) for _ in range(57)];b=[rng.randrange(-M,M) for _ in range(39)]
 assert conv(a,b,74,M)==naive(a,b,74,M)
 a[0]=1;g=inv(a,74,M)
 assert naive(a,g,74,M)==[1]+[0]*73
out['packed_series_independent_checks']={'moduli':[17,13**8,2**64,str(10**90+7)],'random_seed':63,'naive_products_and_inverse_residuals':'all pass'}

# Exact Euler recurrence, independent of Newton inversion and integer packing.
N=3000;parts=[0]*(N+1);parts[0]=1;operations=0
pent=[]
for k in range(1,100):
 for g in[k*(3*k-1)//2,k*(3*k+1)//2]:
  if g<=N:pent.append((g,1 if k%2 else -1))
pent.sort()
for n in range(1,N+1):
 for g,sign in pent:
  if g>n:break
  parts[n]+=sign*parts[n-g];operations+=1
for M in [17,13,169]:
 assert inv(euler(N+1,M),N+1,M)==[x%M for x in parts]
def valuation(n,p):
 if n==0:return 'infinite'
 v=0
 while n%p==0:n//=p;v+=1
 return v
out['partition_exact']={'p243':str(parts[243]),'24n_minus1':24*243-1,'factorization':{str(k):v for k,v in s.factorint(24*243-1).items()},'v7_p243':valuation(parts[243],7),'p2623':str(parts[2623]),'p2623_mod17':parts[2623]%17,'recurrence_max_n':N,'recurrence_additions':operations,'independent_series_comparisons':'all 3001 coefficients modulo17,13,169 match'}
N17=206839*2+2623+1
p17=inv(euler(N17,17),N17,17)
out['partition_progression_mod17']=[{'n':n,'argument':206839*n+2623,'residue':p17[206839*n+2623]} for n in range(3)]
assert all(r['residue']==0 for r in out['partition_progression_mod17'])

# j and Delta: independent small integer recurrence avoids modular ambiguity.
N=2601;M=2**80*3**40*5**30*7**20*11**10*13**8
j=j_coefficients(N,M)
f=euler(N+2,M);delta=[0]+power(f,24,N+1,M)
known=[196884,21493760,864299970,20245856256,333202640600,4252023300096]
assert[j[n] for n in range(1,7)]==known
out['j_initial_coefficients']={str(n):str(j[n]) for n in range(-1,7)}
bounds={2:lambda a:3*a+8,3:lambda a:2*a+3,5:lambda a:a+1,7:lambda a:a,11:lambda a:a}
lehner=[]
for p,bd in bounds.items():
 tested=0;bad=[]
 for n in range(1,N+1):
  a=valuation(n,p)
  if a:
   tested+=1
   if j[n]%(p**bd(a)):bad.append(n)
 lehner.append({'prime':p,'n_through':N,'tested_multiples':tested,'failures':bad})
assert all(not x['failures'] for x in lehner)
out['Lehner_finite_checks']=lehner
assert all((-j[13*n]-delta[n])%13==0 for n in range(1,201))
assert all((j[169*n]-8*j[13*n])%13==0 for n in range(1,16))
out['Newman_mod13']={'minus_Uj_equals_Delta_n_through':200,'U_squared_equals8U_n_through':15,'all_pass':True}
hecke=[]
for ell in [2,3,5,7,11,13]:
 bad=[];count=0
 for n in range(1,N//ell+1):
  count+=1;rhs=delta[ell]*delta[n]-(ell**11*delta[n//ell] if n%ell==0 else 0)
  if (delta[ell*n]-rhs)%M:bad.append(n)
 hecke.append({'ell':ell,'count':count,'failures':bad})
assert all(not x['failures'] for x in hecke)
out['tau_Hecke_finite_checks_mod_large_composite']=hecke

# Weight24 exact coefficients are safely recovered under this large modulus.
L=10;M24=10**80
d=[0]+power(euler(L,M24),24,L-1,M24)
f24=conv(d,power(eisenstein(4,L,M24),3,L,M24),L,M24)
g24=conv(d,d,L,M24)
def signed(x):return x if x<M24//2 else x-M24
f24=list(map(signed,f24));g24=list(map(signed,g24))
cols=[]
for v in[f24,g24]:
 a=v[2];b=v[4]+2**23*v[1]-a*f24[2];cols.append([a,b])
mat=s.Matrix.hstack(*[s.Matrix(c) for c in cols]);char=mat.charpoly().as_expr();disc=s.discriminant(char)
assert s.simplify(disc/(24**2))==144169
out['weight24']={'basis':'Delta*E4^3, Delta^2','T2_matrix':mat.tolist(),'characteristic_polynomial':str(char),'discriminant':str(disc),'squarefree_factor':144169,'eigenvalues':[str(v) for v in mat.eigenvals()]}

# Finite small-prime normalized congruences; the modulus is the displayed one.
small=[]
for p,rate in [(2,3),(3,2),(5,3),(7,1),(11,1)]:
 for a in range(1,4):
  step=p**a
  if step*8>N:continue
  base=j[step];v=valuation(base,p)
  if not isinstance(v,int):continue
  modulus=p**(rate*a);precision_needed=p**(v+rate*a)
  if M%precision_needed:continue
  denom=(base//(p**v))%modulus
  if math.gcd(denom,modulus)!=1:continue
  vals={n:(j[step*n]//(p**v))*pow(denom,-1,modulus)%modulus for n in range(1,N//step+1) if j[step*n]%(p**v)==0}
  pairs=[];bad=[]
  for ell in [2,3,5,7]:
   if ell==p:continue
   for n in range(1,min(20,N//(step*ell))+1):
    if n*ell not in vals or ell not in vals or n not in vals:continue
    rhs=vals[n]*vals[ell]-(pow(ell,-1,modulus)*vals.get(n//ell,0) if n%ell==0 else 0)
    pairs.append([ell,n])
    if (vals[n*ell]-rhs)%modulus:bad.append([ell,n])
  small.append({'prime':p,'alpha':a,'valuation_denominator':v,'modulus':modulus,'pairs':len(pairs),'failures':bad})
out['small_prime_exploratory_finite_checks']=small

# The exact half-integral-weight 13-adic relation in Garvan-Shomanov, Conj1.2.
partition_hecke=[]
for a in[1,2]:
 modulus=13**a;Ns=[n for n in range(1,150) if (13**a*n+1)%24==0]
 for ell in[5,7]:
  maxarg=(ell**2*13**a*max(Ns)+1)//24
  pp=inv(euler(maxarg+1,modulus),maxarg+1,modulus)
  def P(v):
   if not isinstance(v,int) or v<0 or(v+1)%24:return 0
   return pp[(v+1)//24]
  def symbol(v):
   r=pow(v%ell,(ell-1)//2,ell)
   return -1 if r==ell-1 else r
  def rest(n):
   v=13**a*n
   return(P(ell**2*v)+symbol(-3*v)*pow(ell,-2,modulus)*P(v)+(pow(ell,-3,modulus)*P(v//ell**2) if v%ell**2==0 else 0))%modulus
  unitn=next(n for n in Ns if math.gcd(P(13**a*n),modulus)==1)
  kval=rest(unitn)*pow(P(13**a*unitn),-1,modulus)%modulus
  bad=[n for n in Ns if(rest(n)-kval*P(13**a*n))%modulus]
  partition_hecke.append({'alpha':a,'ell':ell,'k':kval,'N_values':Ns,'partition_max_index':maxarg,'failures':bad})
assert all(not x['failures'] for x in partition_hecke)
out['partition_13_Hecke_finite_checks']=partition_hecke

# Class-number-one tables. Enumeration proves each listed order has h=1,
# not that there are no further discriminants. Numerical j values are independent.
Ds=[-3,-4,-7,-8,-11,-12,-16,-19,-27,-28,-43,-67,-163]
js=[0,1728,-3375,8000,-32768,54000,287496,-884736,-12288000,16581375,-884736000,-147197952000,-262537412640768000]
mp.mp.dps=130;cm=[]
for D,target in zip(Ds,js):
 forms=[]
 for a in range(1,math.isqrt(abs(D)//3)+2):
  for b in range(-a,a+1):
   if(b*b-D)%(4*a):continue
   c=(b*b-D)//(4*a)
   if a>c or(math.gcd(a,math.gcd(abs(b),c))!=1):continue
   if(abs(b)==a or a==c) and b<0:continue
   forms.append([a,b,c])
 assert len(forms)==1,(D,forms)
 a,b,c=forms[0];tau=(-b+1j*mp.sqrt(-D))/(2*a);q=mp.exp(2j*mp.pi*tau);r=abs(q);terms=80
 E={}
 err={}
 for weight,factor in[(4,240),(6,-504)]:
  total=mp.mpc(1)
  for n in range(1,terms+1):
   sig=sum(d**(weight-1) for d in range(1,n+1) if n%d==0)
   total+=factor*sig*q**n
  E[weight]=total
  # sigma_(weight-1)(n)<=n^weight; successive tail bounds geometric.
  err[weight]=abs(factor)*(terms+1)**weight*r**(terms+1)/(1-r*((terms+2)/(terms+1))**weight)
 A=E[4]**3;den=A-E[6]**2;numj=1728*A/den
 ea=3*(abs(E[4])+err[4])**2*err[4];ed=ea+2*abs(E[6])*err[6]+err[6]**2
 tail=1728*(ea/(abs(den)-ed)+abs(A)*ed/(abs(den)*(abs(den)-ed)))
 residual=abs(numj-target)
 assert residual<mp.mpf('1e-95'),(D,residual)
 cm.append({'D':D,'reduced_primitive_forms':forms,'j_exact_table_integer':str(target),'q_abs':mp.nstr(r,12),'numerical_residual':mp.nstr(residual,8),'analytic_qseries_tail_bound':mp.nstr(tail,8)})
out['CM_table']={'working_decimal_digits':130,'terms':80,'rounding':'ordinary high-precision arithmetic; analytic tail bounded, floating rounding not interval-certified','rows':cm}

# Arithmetic operation counts, not Atlas timing claims.
counts=[]
for nmax in[1000,4000,10000,40000]:
 gs=[];k=1
 while k*(3*k-1)//2<=nmax:
  gs.extend(g for g in[k*(3*k-1)//2,k*(3*k+1)//2] if g<=nmax);k+=1
 adds=sum(nmax-g+1 for g in gs)
 counts.append({'N':nmax,'pentagonal_additions':adds,'ratio_to_N_power1_5':adds/nmax**1.5,'dense_product_terms':nmax*(nmax+1)//2})
out['operation_counts']=counts
out['elapsed_seconds']=time.monotonic()-tic
path=Path(__file__).resolve().parents[1]/'outputs/c63_numerics.json';path.write_text(json.dumps(out,ensure_ascii=False,indent=2,default=str)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2,default=str))
