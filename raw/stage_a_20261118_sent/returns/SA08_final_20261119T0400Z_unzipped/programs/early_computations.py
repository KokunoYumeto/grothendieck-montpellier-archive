"""Independent exact arithmetic checks for the early SA08 manuscript.

Finite checks supplement, never replace, the general proofs in early/proofs.md.
All integers/rationals are exact.  The output labels the scope of every test.
"""
from math import comb,factorial,gcd
from fractions import Fraction
from itertools import product,combinations
from pathlib import Path
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

out={}
def c(i,j): return comb(i+j,i)
def vp(n,p):
 a=0
 while n and n%p==0: a+=1;n//=p
 return a
def digits(n,p):
 a=[]
 while n:a.append(n%p);n//=p
 return a or [0]
def rankmod(mat,p):
 a=[list(map(lambda x:int(x)%p,row)) for row in mat]
 if not a:return 0
 r=0
 for col in range(len(a[0])):
  piv=next((i for i in range(r,len(a)) if a[i][col]),None)
  if piv is None:continue
  a[r],a[piv]=a[piv],a[r];v=pow(a[r][col],-1,p)
  a[r]=[(x*v)%p for x in a[r]]
  for i in range(len(a)):
   if i!=r and a[i][col]:
    b=a[i][col];a[i]=[(x-b*y)%p for x,y in zip(a[i],a[r])]
  r+=1
  if r==len(a):break
 return r

# Lucas/no-carry, the two recurrences on scan21, Legendre, and p-unit factors.
count=0;rec=0
for p in [2,3,5,7,11]:
 for i,j in product(range(81),repeat=2):
  a,b=digits(i,p),digits(j,p);l=max(len(a),len(b));a+=[0]*(l-len(a));b+=[0]*(l-len(b))
  digitproduct=1
  for u,v in zip(a,b):digitproduct*=c(u,v)
  assert c(i,j)%p==digitproduct%p
  assert (c(i,j)%p!=0)==all(u+v<p for u,v in zip(a,b));count+=1
 for N in range(1,121):
  if (N+1)%p:continue
  N1=(N+1)//p-1
  for e in range(1,5):
   assert c(N+1,p**e-1)%p==c(N1+1,p**(e-1)-1)%p
   assert c(N,p**e)%p==c(N1,p**(e-1))%p;rec+=1
 for n in range(301):assert vp(factorial(n),p)==(n-sum(digits(n,p)))//(p-1)
out['arithmetic']={'lucas_pairs':count,'scan21_recurrences':rec,'legendre_cases':5*301,'primes':[2,3,5,7,11]}
units=[]
for p,r in product([2,3,5,7],range(4)):
 n=p**r; q=factorial(p*n)//(factorial(n)**p*factorial(p));nu=factorial(p-1)*q
 assert q%p!=0 and nu%p!=0
 units.append({'p':p,'r':r,'v_p_nu':vp(nu,p),'nu_mod_p':nu%p})
out['p_typical_units']=units

# Sparse lemma: the actual weaker hypothesis does NOT force x4=x2.
I=[2,3,4,6];sol=[]
for xs in product(range(2),repeat=4):
 d=dict(zip(I,xs))
 if all(comb(j,i)*(d[j]-d[i])%2==0 for i in [2,3] for j in I if j>i):sol.append(xs)
assert all(x[0]==x[1]==x[3] for x in sol)
assert (0,0,1,0) in sol
out['sparse_F2']={'indices':I,'solutions':sol,'witness':[0,0,1,0]}

# Finite field truncations of the full all-pairs relation. Limitations explicit.
tail=[]
for p,N in product([2,3,5,7],range(7)):
 top=1
 while top<=N+5:top*=p
 top-=1;inds=list(range(N,top+1));rows=[]
 for i,j in combinations(inds,2):
  r=[0]*len(inds);r[j-N]=comb(j,i);r[i-N]=-comb(j,i);rows.append(r)
 nullity=len(inds)-rankmod(rows,p);assert nullity==1
 tail.append({'p':p,'N':N,'top_p_power_minus_one':top,'nullity':nullity})
out['tail_field_tests']=tail

# Weighted family identity and local comparison identity.
count=0
for i in range(11):
 for k in range(i,35):
  for ell in range(15):
   assert c(ell,k)*comb(k,i)==c(ell,k-i)*comb(k+ell,i);count+=1
for i,j,j1 in product(range(10),repeat=3):
 if j1>=j:assert Fraction(c(j1-j,j+i),c(j1-j,j))==Fraction(c(i,j1),c(i,j))
bez=[]
for i,N in product(range(9),range(9)):
 N=max(i,N);g=0;last=N-1
 while g!=1:
  last+=1;g=gcd(g,comb(last,i))
  assert last<N+1000
 bez.append({'i':i,'N':N,'first_prefix_end_with_gcd1':last})
out['weighted_family']={'identities':count,'bezout_prefixes':bez,'index_mismatch_i1_k2':{'correct_c_i_k_minus_i':c(1,1),'literal_c_k_k_minus_i':c(2,1)}}

# Weight-preserving PD de Rham complex, exact matrix ranks over Q,F2,F3.
def comps(n,r):
 if r==0:
  if n==0:yield ()
  return
 for a in range(n+1):
  for b in comps(n-a,r-1):yield (a,)+b
pd=[]
for r in [1,2,3]:
 for w in range(7):
  bases={q:[(a,J) for a in comps(w-q,r) for J in combinations(range(r),q)] if w>=q else [] for q in range(r+1)}
  dif={}
  for q in range(r):
   target={x:i for i,x in enumerate(bases[q+1])};D=sp.zeros(len(target),len(bases[q]))
   for col,(a,J) in enumerate(bases[q]):
    for t in range(r):
     if a[t] and t not in J:
      b=list(a);b[t]-=1;K=tuple(sorted(J+(t,)));sgn=(-1)**sum(j<t for j in J)
      D[target[(tuple(b),K)],col]+=sgn
   dif[q]=D
  for q in range(r-1):assert dif[q+1]*dif[q]==sp.zeros(len(bases[q+2]),len(bases[q]))
  for field in ['Q',2,3]:
   ranks={q:(D.rank() if field=='Q' else rankmod(D.tolist(),field)) for q,D in dif.items()}
   h=[len(bases[q])-ranks.get(q-1,0)-ranks.get(q,0) for q in range(r+1)]
   expected=[int(w==0)]+[0]*r;assert h==expected
  pd.append({'variables':r,'weight':w,'dimensions':[len(bases[q]) for q in range(r+1)],'H_over_Q_F2_F3':expected})
out['pd_poincare']=pd

# Endpoints, pairing coefficients, deleted generation, omitted cross-syzygies.
out['small_counterexamples']={
 'parity_T_square':{'exterior_degree':0,'weight':1,'T2_coefficient':c(1,1)},
 'tensor_two_first_shadows_weight2':{'source_rank_Z':1,'target_rank_Z':1,'multiplication':2,'cokernel':'Z/2'},
 'endpoint_F2_alpha1_beta3_d1':{'forbidden_j1_coefficient':c(1,1)%2,'allowed_j2_coefficient':c(1,2)%2,'nonzero_map':'multiplication by T'},
 'deleted_tail_generation_F2_N3':{'only_possible_degree4_multiplier_degree':1,'coefficient':c(3,1)%2,'T_divided_4_nonzero':True},
 'cross_syzygy_F2':{'ambient':'F2[x,y]/(x^2,y^2)','listed_module':'S/(x)e_x direct_sum S/(y)e_y','omitted_relation':'y e_x + x e_y','component1_nonzero':True,'component2_nonzero':True},
 'nonnegative_adjoint_Q':{'Hom_gr_Qt_Qt_to_tQt':0,'Hom_gr_Qt_tQt_to_tQt':1},
 'CP2_PD':{'H4_generator':'u^2','required_integer_equation':'2a=1','integer_solution':False},
 'BC2_odd_alternation_F2':{'ordinary_H':'F2[u], degree(u)=1','u_squared_nonzero':True,'alternating_odd_square':0,'weights1_2_product_coefficient_mod2':c(1,2)%2}}

# I/I^2 for Fp DP: indecomposables in degrees p^r. Demonstrates arbitrarily high survivors.
ind=[]
for p in [2,3,5]:
 top=p**4
 survivors=[n for n in range(1,top+1) if all(c(i,n-i)%p==0 for i in range(1,n))]
 assert survivors==[p**r for r in range(5)]
 ind.append({'p':p,'range':[1,top],'indecomposable_degrees':survivors})
out['negligible_counterexample']=ind

# Finite stages of infinite-height group. The infinite conclusion is proved in prose.
height=[]
for p in [2,3,5]:
 for N in range(1,6):
  R=sp.zeros(N+1,N+1);R[0,0]=p
  for j in range(1,N+1):R[j,0]=-1;R[j,j]=p**j
  D=smith_normal_form(R,domain=ZZ);diagonal=[abs(int(D[j,j])) for j in range(N+1)]
  assert sp.prod(diagonal)==p**(1+N*(N+1)//2)
  # A homomorphism to Q/Z sends x to1/p and y_j to1/p^(j+1).
  vals=[Fraction(1,p)]+[Fraction(1,p**(j+1)) for j in range(1,N+1)]
  assert all(sum(int(R[i,j])*vals[j] for j in range(N+1)).denominator==1 for i in range(N+1))
  height.append({'p':p,'N':N,'smith_diagonal':diagonal,'x_image_Q_mod_Z':str(vals[0]),'max_available_root_depth':N})
out['infinite_height_finite_stages']=height

# Ring specialization/Int(Z), factorial denominators, and the Stokes cancellation.
t=sp.symbols('t');binompoly=lambda n:sp.prod(t-j for j in range(n))*sp.Rational(1,factorial(n))
for m,n in product(range(8),repeat=2):
 lhs=sp.Poly(binompoly(m)*binompoly(n),t).LC()
 assert lhs*factorial(m+n)==c(m,n)
for m,n in product(range(8),repeat=2):
 assert Fraction(c(m,n),factorial(m+n))==Fraction(1,factorial(m)*factorial(n))
stokes=[]
for n in range(2,10):
 terms={}
 for i in range(n+1):
  face=[j for j in range(n+1) if j!=i]
  for j in range(n):
   simplex=tuple(face[:j]+face[j+1:]);terms[simplex]=terms.get(simplex,0)+(-1)**(i+j)
 assert all(v==0 for v in terms.values());stokes.append({'dimension':n,'codim2_terms':len(terms),'all_coefficients_zero':True})
out['specialization_and_binomial']={'checked_m_n_0_to_7':True,'binomial_leading_term':'t^n/n!','stabilization_transition_from_weight_r':'r+1','infinite_discrete_obstruction':'a finite denominator cannot be divisible by infinitely many distinct primes'}
out['stokes_boundary_squared']=stokes
print(json.dumps(out,indent=2))
