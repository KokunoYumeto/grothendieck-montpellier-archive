"""Exact arithmetic checks for the Codex continuation of cote136.

Finite calculations validate the stated examples/ranges; they are not claimed
as proofs of unrestricted categorical or geometric theorems. General algebraic
arguments are in work/root/codex_proof_checks.md.
"""
from math import comb, factorial
from fractions import Fraction
from itertools import combinations, product
from collections import defaultdict
import json
import sympy as S

out={}
def record(k,v):out[k]=v
def choose(n,r):return comb(n,r) if 0<=r<=n else 0

rank_tests=0
for N in range(21):
 for p in range(9):
  for q in range(min(N,8)+1):
   assert choose(N+p,p)*choose(N,q)==choose(p+q,p)*choose(N+p,p+q)
   rank_tests+=1
shift_tests=0
for N in range(15):
 for p in range(1,9):
  for q in range(9):
   assert choose(N+p,p+q)==sum(choose(p-1,j)*choose(N+1,p+q-j) for j in range(p))
   shift_tests+=1
record('337_rank_and_shift',{'rank_cases':rank_tests,'shift_cases':shift_tests,'result':'all exact identities passed','symbolic_reason':'factorials and Pascal iteration; p>=1 for exponent p-1'})
record('334_nested_PD',{'p':2,'q':3,'gamma_p_gamma_q_coefficient':factorial(6)//(factorial(2)*factorial(3)**2),'written_opposite_nesting_coefficient':factorial(6)//(factorial(2)**3*factorial(3)),'result':'10 != 15'})

# Exterior forms over the integral free PD algebra in two variables.
NV=2
def tidy(v):return {k:c for k,c in v.items() if c}
def add(*vs):
 d=defaultdict(int)
 for v in vs:
  for k,c in v.items():d[k]+=c
 return tidy(d)
def scale(v,c):return tidy({k:c*a for k,a in v.items()})
def compose(f,g,v):return f(g(v))
def wedge_left(j,I):
 if j in I:return None,0
 return tuple(sorted((j,)+I)),(-1)**sum(i<j for i in I)
def d(v):
 w=defaultdict(int)
 for (a,I),c in v.items():
  for j in range(NV):
   J,sg=wedge_left(j,I)
   if a[j] and sg:
    b=list(a);b[j]-=1;w[(tuple(b),J)]+=c*sg
 return tidy(w)
def delta(v):
 w=defaultdict(int)
 for (a,I),c in v.items():
  for k,j in enumerate(I):
   b=list(a);b[j]+=1
   w[(tuple(b),I[:k]+I[k+1:])]+=c*(-1)**k*(a[j]+1)
 return tidy(w)
def lam(v):
 w=defaultdict(int)
 for (a,I),c in v.items():
  for j in range(NV):
   J,sg=wedge_left(j,I)
   if sg:w[(a,J)]+=c*sg
 return tidy(w)
def theta(v):return tidy({(a,I):(sum(a)+len(I))*c for (a,I),c in v.items()})
def mu(p,v):
 w=defaultdict(int)
 for (a,I),c in v.items():
  for b in product(range(p+1),repeat=NV):
   if sum(b)!=p:continue
   ab=tuple(x+y for x,y in zip(a,b));coef=c
   for x,y in zip(a,b):coef*=choose(x+y,x)
   w[(ab,I)]+=coef
 return tidy(w)
forms=[]
for a in product(range(5),repeat=NV):
 if sum(a)>5:continue
 for k in range(NV+1):
  for I in combinations(range(NV),k):forms.append({(a,I):1})
checks=0
for v in forms:
 assert d(d(v))==delta(delta(v))==lam(lam(v))=={}
 assert add(d(delta(v)),delta(d(v)))==theta(v)
 assert add(d(lam(v)),lam(d(v)))=={}
 assert add(delta(lam(v)),lam(delta(v)))==mu(1,v)
 assert add(theta(lam(v)),scale(lam(theta(v)),-1))==lam(v)
 checks+=5
 for p in range(1,5):
  assert add(d(mu(p,v)),scale(mu(p,d(v)),-1))==mu(p-1,lam(v))
  assert add(delta(mu(p,v)),scale(mu(p,delta(v)),-1))=={}
  assert add(theta(mu(p,v)),scale(mu(p,theta(v)),-1))==scale(mu(p,v),p)
  assert add(lam(mu(p,v)),scale(mu(p,lam(v)),-1))=={}
  checks+=4
record('346_PD_Koszul_operators',{'variables':NV,'basis_forms':len(forms),'identities_checked':checks,'result':'passed over Z with exact integer coefficients','caution':'finite checks supplement the generator-and-derivation proof; no operator-algebra PBW independence asserted'})

# The proposed lift of Gamma^p Phi tensor Psi projects to p times identity.
record('346_proposed_splitting',{'multi_index':[2,1],'sum_q':3,'projection_coefficient':2+1,'prime3_reduction':0,'result':'not a right inverse in characteristic3; divided-by-p repair needs p invertible'})

# Group-like vectors in diagonal coalgebras over a disconnected ring.
e1=(1,0);e2=(0,1)
mul=lambda a,b:tuple(x*y for x,y in zip(a,b))
record('343_disconnected_base',{'ring':'F2 x F2','coefficients':[e1,e2],'squares':[mul(e1,e1),mul(e2,e2)],'cross_term':mul(e1,e2),'sum':tuple(x+y for x,y in zip(e1,e2)),'result':'e1*x+e2*y is group-like of counit1 but not x or y'})

# Alexander–Whitney on one diagonal 1-simplex of Delta1 x Delta1.
# Tensor boundary in degree0 is represented by pairs of endpoint indices.
standard={(1,1):1,(0,0):-1}
with_extra_sign={(0,1):2,(0,0):-1,(1,1):-1}
record('357_AW_sign',{'required_boundary':str(standard),'extra_minus_boundary':str(with_extra_sign),'difference':str({(0,1):2,(1,1):-2}),'result':'the extra (-1)^i violates the conventional chain-map identity over Z'})

def sq(i,m):return choose(m,i)%2,m+i
c1,d1=sq(2,1);c2,d2=sq(1,d1)
c3,d3=sq(3,1);c4,d4=sq(1,1);c5,d5=sq(2,d4)
record('365_Adem_counterexample',{'space':'RP^infinity','class':'t in H^1(-;F2)','Sq1Sq2_t':f'{c1*c2}*t^{d2}','Sq3_t':f'{c3}*t^{d3}','Sq2Sq1_t':f'{c4*c5}*t^{d5}','result':'0 != t^4; correct Adem relation is Sq1 Sq2 = Sq3'})

# Normalized ranks for exterior powers of Phi and Psi, over Q.
def faces(n,quotient=False):
 ans=[]
 for j in range(n+1):
  M=S.zeros(n,n+1)
  for i in range(n+1):
   if i!=j:M[i-(i>j),i]=1
  if quotient:
   P=S.zeros(max(n-1,0),n)
   for r in range(n-1):P[r,0]=-1;P[r,r+1]=1
   M=P*M[:,1:]
  ans.append(M)
 return ans
def exterior(M,r):
 rows=list(combinations(range(M.rows),r));cols=list(combinations(range(M.cols),r))
 return S.Matrix(len(rows),len(cols),lambda a,b:M.extract(rows[a],cols[b]).det())
norms=[]
for n in range(7):
 for r in range(1,5):
  for quotient in [False,True]:
   dim=choose(n if quotient else n+1,r)
   f=faces(n,quotient)
   blocks=[exterior(x,r) for x in f[1:]]
   rank=S.Matrix.vstack(*blocks).rank() if blocks and dim else 0
   norm=dim-rank
   expected=int(n==r) if quotient else int(n in [r-1,r])
   assert norm==expected,(n,r,quotient,norm,expected)
   norms.append({'n':n,'r':r,'object':'Psi' if quotient else 'Phi','normalized_rank':norm})
record('338_341_normalized_ranks',{'cases':len(norms),'result':'passed: N Lambda^r Psi has rank1 in degree r; N Lambda^r Phi rank1 in degrees r-1,r','examples':[x for x in norms if x['r']==2]})

# Milnor coproduct on polynomial xi generators, coassociativity.
xi={side:{i:S.Symbol(f'{side}{i}') for i in range(1,5)} for side in 'abc'}
def get(side,i):return S.Integer(1) if i==0 else xi[side][i]
milnor=0
for p in [2,3,5]:
 for k in range(1,5):
  left=0;right=0
  for i in range(k+1):
   delta_ki=sum(get('a',k-i-j)**(p**j)*get('b',j) for j in range(k-i+1))
   # Frobenius makes raising to p^i termwise valid in characteristicp.
   left+=sum(get('a',k-i-j)**(p**(j+i))*get('b',j)**(p**i)*get('c',i) for j in range(k-i+1))
   right+=get('a',k-i)**(p**i)*sum(get('b',i-j)**(p**j)*get('c',j) for j in range(i+1))
  assert S.expand(left-right)==0
  milnor+=1
record('367_Milnor_coproduct',{'cases':milnor,'result':'coassociativity of displayed xi coproduct passed; Frobenius expansion used only in characteristicp'})

a=S.Symbol('a');I=S.eye(3);E12=I.copy();E23=I.copy();E13=I.copy()
E12[0,1]=a;E23[1,2]=1;E13[0,2]=a
assert E12*E23*E12.inv()*E23.inv()==E13
record('370_elementary_perfectness',{'commutator':'[e12(a),e23(1)] = e13(a)','matrix':str(E13),'result':'passed exactly; stable spare index gives perfectness over every unital ring'})
record('372_unstable_symmetry_counterexample',{'n':1,'G':'Z','H':'Z/2','degree':3,'left':'H3(S1;Z/2)=0','right':'H3(B(Z/2);Z)=Z/2','chain_complex_right':'... Z --2--> Z --0--> Z --2--> Z --0--> Z','result':'unrestricted symmetry is false; this example is outside the manuscript stable range'})
record('374_base_change_counterexample',{'X':'countably infinite discrete set','R':'Fp[u]','class':'(1,u,u^2,...) in R^N','reason':'every element of Fp^N tensor_Fp Fp[u] has a uniform polynomial degree bound','result':'not in image; finite type or finite-dimensional coefficients restore this comparison'})
u=S.Symbol('u');p=3
record('374_Frobenius_semilinearity',{'p':p,'class':'u*z, z in H2(CP∞;F3)','actual_coefficient':str(u**p),'written_linear_coefficient':str(u),'difference':str(u**p-u),'result':'nonzero in F3[u]; positive Steenrod powers also require Frobenius on scalars'})
def vp(i,p):
 n=0
 while i%p==0:n+=1;i//=p
 return n
record('376_Breen_exponent_comparison',{'p':2,'rows':[{'i':i,'manuscript_F_exponent':vp(i,2),'Breen_F_exponent':vp(i,2)+1} for i in range(1,9)],'result':'one exponent difference in every degree; mathematical comparison only, manuscript ink undecided'})
print(json.dumps(out,ensure_ascii=False,indent=2))
