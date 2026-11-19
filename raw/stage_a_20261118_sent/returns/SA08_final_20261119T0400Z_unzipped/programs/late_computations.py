"""Exact finite audits of SA08 late leaves. These are not proofs of infinite assertions.
All arithmetic is integer/rational. Mathematical proofs accompany the certificates.
"""
from math import factorial, comb, gcd
from fractions import Fraction
from itertools import product
import json
from pathlib import Path

def vp(n,p):
    if n == 0: return None
    v=0
    while n%p==0: v+=1; n//=p
    return v
def vf(n,p):
    ans=0
    while n: n//=p; ans+=n
    return ans
def ds(n,p):
    s=0
    while n: s+=n%p;n//=p
    return s
def av(n,p):return n-vf(n,p)
out={}
assert all(vf(n,p)==(n-ds(n,p))//(p-1) for p in (2,3,5,7,11) for n in range(1000))
assert all(av(n+1,p)-av(n,p)==1-vp(n+1,p) for p in (2,3,5,7,11) for n in range(1000))
out['valuation_identities']={'primes':[2,3,5,7,11],'n_range':[0,999],'checked':True,
 'scan241_line229_counterexample':{'p':3,'i':2,'s':1,'a_i':av(2,3),'a_i_plus1':av(3,3), 'conclusion':'weak inequality holds at s=1; strict inequality iff s=0'}}
valrows=[]
for p in (3,5,7):
 for i in range(1,41):
  bound=((p-1)*av(i,p)-1)//(p-2)
  amin=min(av(n,p) for n in range(i,bound+1))
  assert amin==min(av(n,p) for n in range(i,2000))
  if (i+1)%p==0:
   bound2=((p-1)*av(i+1,p)-1)//(p-2)
   assert amin==min(av(n,p) for n in range(i+1,bound2+1))
  valrows.append({'p':p,'i':i,'finite_bound':bound,'ideal_exponent':amin})
out['odd_prime_ideal_table']=valrows
out['p2']={'a_2_to_power_r':[av(2**r,2) for r in range(1,14)],'conclusion':'all values one; positive PD filtration ideals are 2Z_2, by separate digit-sum proof'}
assert all(min(av(n,p) for n in range(p-1,200))==p-1 for p in (3,5,7,11))
out['graded_free_counterexamples']=[{'p':p,'a_p_minus1':p-1,'a_p':p-1,'graded_piece_p_minus1':0} for p in (3,5,7,11)]

assert all(comb(p+q-1,p)+comb(p+q-1,q)==comb(p+q,p) for p in range(1,25) for q in range(1,25))
assert all(Fraction(factorial(a*b),factorial(b)*factorial(a)**b).denominator==1 for a in range(1,10) for b in range(1,10))
out['pd_coefficient_identities']={'Pascal_pairs':576,'iterated_PD_integrality_pairs':81,'odd_extension_residual':'gamma_2(y+yprime) - gamma_2(y)-y*yprime-gamma_2(yprime) = -y*yprime if gamma_2 is forced zero on all odd sums; a square-zero product restriction is needed'}

assert all(comb(j,n)%p!=0 for p in (2,3,5,7) for r in range(1,5) for j in [p**r-1] for n in range(j+1))
assert all(comb(j,n)*comb(j+a,a)==comb(j+a,n+a)*comb(n+a,a) for a in range(12) for j in range(30) for n in range(j+1))
out['binomial_rigidity']={'Lucas_unit_cases':'p=2,3,5,7; r=1,...,4; all 0<=n<=p^r-1','weighted_identity':'C(j,n)C(j+a,a)=C(j+a,n+a)C(n+a,a)','weighted_range':'0<=a<=11;0<=n<=j<=29'}
neg=[]
for d in range(1,16):
 for i in range(d,40):
  for j in range(i,50):
   assert Fraction(comb(j,i),comb(j,d))==Fraction(comb(j-d,i-d),comb(i,d))
 for p in (2,3,5,7):
  for r in range(1,7):
   if p**r>d:
    j=p**r-1+d
    v=vp(comb(j,d),p)
    assert v==r-vp(d,p)
    neg.append({'d':d,'p':p,'r':r,'j':j,'valuation':v})
out['negative_tail_relation']={'rational_relation_checked':True,'local_denominator_valuations':neg,
 'infinite_claim_proof_location':'work/late/proofs.md, negative tail presentation; finite checks alone do not prove R_d=Q'}
for p in (2,3,5):
 for r in range(1,5):
  assert all(comb(p**r,i)%p==0 for i in range(1,p**r))
out['non_serre']={'indecomposable_PD_degrees_checked':'p^r for p=2,3,5;r=1,...,4','reason':'every nontrivial product coefficient C(p^r,i) vanishes in F_p; see proof memo for extension'}
out['product_bezout']={'C4_2':comb(4,2),'C7_3':comb(7,3),'bezout':6*comb(4,2)-comb(7,3),'gcd':gcd(comb(4,2),comb(7,3))}

# Finite PD counterexample B=Z + (Z/2)t + (Z/4)u, t^2=2u,tu=u^2=0.
# Constant coefficients need only be tested modulo 4 for multiplication on J.
def norm(x):return (x[0],x[1]%2,x[2]%4)
def add(x,y):return norm(tuple(a+b for a,b in zip(x,y)))
def mul(x,y):
 a,b,c=x;d,e,f=y
 return norm((a*d,a*e+b*d,a*f+c*d+2*b*e))
def scale(n,x):return norm(tuple(n*a for a in x))
def power(x,n):
 z=(1,0,0)
 for _ in range(n):z=mul(z,x)
 return z
def gamma(n,x):
 assert x[0]==0
 if n==0:return(1,0,0)
 if n==1:return x
 if n==2:return(0,0,(x[1]**2)%4)
 return(0,0,0)
J=[(0,a,b) for a in range(2) for b in range(4)]
R4=[(a,b,c) for a in range(4) for b in range(2) for c in range(4)]
counts={'additivity':0,'scalars':0,'products':0,'iteration':0}
for x,y in product(J,repeat=2):
 for n in range(7):
  rhs=(0,0,0)
  for i in range(n+1):rhs=add(rhs,mul(gamma(i,x),gamma(n-i,y)))
  assert gamma(n,add(x,y))==rhs;counts['additivity']+=1
for a,x in product(R4,J):
 for n in range(1,7):
  assert gamma(n,mul(a,x))==mul(power(a,n),gamma(n,x));counts['scalars']+=1
for x in J:
 for m,n in product(range(1,7),repeat=2):
  assert mul(gamma(m,x),gamma(n,x))==scale(comb(m+n,m),gamma(m+n,x));counts['products']+=1
  coeff=factorial(m*n)//(factorial(n)*factorial(m)**n)
  assert gamma(n,gamma(m,x))==scale(coeff,gamma(m*n,x));counts['iteration']+=1
out['nonflat_convolution_PD']={'PD_axiom_finite_checks':counts,'f_at_one':[0,0,0],'f_at_e':[0,1,0], 'convolution_square_at_e':mul((0,1,0),(0,1,0)),
 'all_possible_additive_gamma2_values_at_e':[x for x in J if scale(2,x)==(0,0,0)],
 'contradiction':'Any additive g:A->B has 2g(e)=0, while f*f(e)=2u!=0. Hence f*f=2gamma_2(f) is impossible.',
 'proof_scope':'The proof memo verifies remaining infinite-index identities and counital cocommutative coalgebra axioms.'}

out['dual_numbers']={'multiplication_eps_matrix':[[0,0],[1,0]],'kernel_equals_image':'both k epsilon','Hom_into_trivial_k_differential':0,'Ext_n_k_k':'k for every n>=0; periodic-resolution proof in memo'}
out['tensor_and_totalization']={'DK_Z1_level_tensor_normalized_degree1_rank':1,'ordinary_tensor_Z1_degree1_rank':0,'unsigned_dh_plus_dv_square':'2 dh dv','signed_total_differential':'D=d_h+(-1)^horizontal_degree d_v','rank2_convolution_pair_source_rank':4,'target_rank':2}
out['elementary_checks']={'Dirichlet_tail_bound_counterexample':{'u':[-1,2,-1,0],'c':[str(Fraction(1,n)) for n in range(1,5)],'max_partial_sum':1,'R_1':str(Fraction(2,2)-Fraction(1,3)),'claimed_Mc2':'1/2','correct_general_bound':'2Mc_(n+1)'},
 'missing_i_scan326':'lambda=i, mu=-i gives b=(i-(-i))/(2i)=1, while printed (lambda-lambda^-1)/2=i',
 'real_projective_component':'diag(-1,1) has negative determinant; scaling changes determinant by a positive square, so no SL2(R) representative'}
def alternate_u(n):return int(n<=1)
for p,q in product(range(1,40),repeat=2):
 assert alternate_u(p*q)==alternate_u(p)*alternate_u(q)**p
 assert comb(p+q,p)*(alternate_u(p)*alternate_u(q)-alternate_u(p+q))%2==0
out['scan324_uniqueness_counterexample']={'base':'F2','coalgebra':'A=F2 with Delta(1)=1 tensor1','canonical':'u_n(1)=T^(n)','alternative':'v_0=1,v_1=T,v_n=0 for n>=2','checks':'composition and binomial product identities for 1<=p,q<=39','scope':'fixed representing object and the two displayed relations only; not a natural additive operation for every module M'}
path=Path('/workspace/scratch/7feb9690b71f/SA08_work/logs/late_computations_output.json')
path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'status':'all exact finite checks passed','output':str(path),'sections':list(out)},indent=2))
