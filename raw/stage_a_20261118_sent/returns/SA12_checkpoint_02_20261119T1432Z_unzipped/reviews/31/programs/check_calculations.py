"""Finite certificates and symbolic identities for the cote31 review.
These are independently reconstructed checks, not formal certification of all theorems.
Only Python's standard library is needed.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction
import json
root=Path('/workspace/scratch/a77a578fa7d4/SA12_work/reviews/31')
R={}
def permute(v,p):return tuple(v[p[i]] for i in range(len(p)))
def plus(v,w):return tuple(x+y for x,y in zip(v,w))
# Faithful ring action: B=Z^6, sigma=(12)(3456), H=<sigma^2>.
p=(1,0,3,4,5,2); b=(1,0,1,0,1,0)
assert permute(permute(b,p),p)==b
assert plus(b,permute(b,p))==(1,)*6
assert any(permute(permute(tuple(int(i==j) for i in range(6)),p),p)!=tuple(int(i==j) for i in range(6)) for j in range(6))
# On M=Z^2, H acts trivially; Hhat0(H,M)=M/2M.
H0=list(product(range(2),repeat=2));stable=[v for v in H0 if v==v[::-1]]
cor=lambda v:(sum(v)%2,)*2
assert len(set(map(cor,stable)))==1 and len(set(map(cor,H0)))==2
R['relative_corestriction']={'B':'Z^6; faithful sigma=(12)(3456)','H':'<sigma^2>','M':'Z^2 via first two coordinates, sigma swaps','trace_one_element':b,'relative_trace':plus(b,permute(b,p)),'Hhat0_H':H0,'stable_elements':stable,'corestriction_on_stable':[(v,cor(v)) for v in stable],'Hhat0_G':'diagonal Z / 2 diagonal Z = F2','conclusion':'stable-corestriction bijection FALSE; unrestricted corestriction is onto; restriction identifies F2 with diagonal F2','relative_projectivity':'phi=diag(1,0); phi+sigma phi sigma^-1=identity'}
# O=F2[e]/e^3: 3 binary coefficients encoded as bits.
def mul(a,b):
 z=0
 for i in range(3):
  for j in range(3-i):z^=(((a>>i)&1)*((b>>j)&1))<<(i+j)
 return z
def sig(a):return a^(((a>>1)&1)<<2)
O=list(range(8));U=[a for a in O if a&1]
assert all(sig(sig(a))==a for a in O) and sig(2)!=2
assert all(sig(mul(a,b))==mul(sig(a),sig(b)) for a in O for b in O)
inv={a:next(b for b in U if mul(a,b)==1) for a in U}
norm={a:mul(a,sig(a)) for a in U};cocycles=[a for a in U if norm[a]==1]
coboundaries=sorted({mul(inv[a],sig(a)) for a in U})
cosets=sorted({tuple(sorted(mul(a,c) for c in coboundaries)) for a in cocycles})
assert len(cosets)==2
R['semilocal_H1']={'ring':'F2[e]/(e^3), local Artin, maximal ideal(e), residue F2','action':'sigma(e)=e+e², faithful order2 automorphism','units_bit_encoding':U,'norms':norm,'cocycles':cocycles,'coboundaries':coboundaries,'H1_cosets':cosets,'inertia':'G=C2, one maximal ideal so transitivity holds','residue_H1':'0 since F2^*=1','conclusion':'natural H1 reduction is not injective; refutes unqualified comparison, also GL_n version at n=1'}
# Group algebra regular representation determinant for elementary abelian groups.
def sign(p):return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1
det_rows=[]
for ell in [2,3,5]:
 for r in range(1,4):
  el=list(product(range(ell),repeat=r));index={x:i for i,x in enumerate(el)}
  a=tuple([1]+[0]*(r-1));perm=[index[tuple((x+y)%ell for x,y in zip(v,a))] for v in el]
  d=sign(perm);formula=(-1)**((ell-1)*ell**(r-1));assert d==formula
  det_rows.append({'ell':ell,'rank':r,'order':ell**r,'determinant':d,'augmented_determinant':d*d})
R['regular_norm']=dict(rows=det_rows,general_formula='(-1)^((ell-1)*ell^(r-1))',exception='ell=2,r=1 only',repair='rho direct_sum det(rho)^(-1), determinant1, dimension |Gamma|+1')
# A=C[[x,y]], E_n over C[[y]] with x e1=0, x ej=-y e(j-1).
module_rows=[]
for n in range(1,9):
 # Apply x n-1 times to y e_n; track (basis-index,y-degree,integer-coefficient).
 j,pow_y,c=n,1,1
 for _ in range(n-1):j-=1;pow_y+=1;c=-c
 assert (j,pow_y,c)==(1,n,(-1)**(n-1))
 module_rows.append({'n':n,'x^(n-1)(y e_n)':f'{c}*y^{pow_y}*e{j}','E_n/xE_n':f'C[[y]] plus {n-1} copies C','ker_x':'C[[y]] e1'})
R['module_chain']={'rows':module_rows,'all_n_argument':'x acts as -y times the left shift, so multiplication has the displayed form for all n by induction; y is regular in C[[y]]. Transition E_n to E_(n+1) is inclusion of first n free basis vectors.','colimit':'M[x]=C[[y]]e1 finite over A/(x); M/xM=direct_sum_(j>=1) C e_j is not finite. Ext^1_A(A/(x),M)=M/xM; Ext^i=0 for i>1.','terminology':'old SGA2 J-cofini only controls Hom and is satisfied; modern Ext-cofinite fails'}
# Formal square root gives unit norm counterexample over C((t)).
coeff=[Fraction(1)]+[Fraction(0)]*7;target=[Fraction(1),Fraction(2),Fraction(3),Fraction(4),Fraction(5),Fraction(6),Fraction(7),Fraction(8)]
for n in range(1,len(coeff)):coeff[n]=(target[n]-sum(coeff[i]*coeff[n-i] for i in range(1,n)))/2
square=[sum(coeff[i]*coeff[n-i] for i in range(n+1)) for n in range(len(coeff))]
assert square==target
R['unit_norm']={'base':'K=C((t))','extension':'L=C((u)), u²=t; finite cyclic degree2, ramificationindex2','arbitrary_unit_argument':'every a(t) in C[[t]]^* has a formal square root b(t) in C[[t]]^*: choose b0²=a0 then solve b_n=(a_n-sum_(0<i<n)b_i b_(n-i))/(2b0). Viewed in L, N(b)=b²=a.','example_target':[str(x) for x in target],'root_coefficients':[str(x) for x in coeff],'square_checked':[str(x) for x in square],'conclusion':'norm units onto does not imply unramified with arbitrary residue field'}
# Frobenius/additive automorphism: polynomial identity, finite table is supplementary.
R['additive_automorphism']={'identity':'(a+b)^p=a^p+b^p in characteristic p; (x,y)->(x+y^p,y), inverse(x,y)->(x-y^p,y)','conclusion':'additive polynomial automorphism is not a GL2-linear map for p>1; does not disprove vector-group classification'}
for p0 in [2,3,5,7]:assert all(pow(a+b,p0,p0)==(pow(a,p0,p0)+pow(b,p0,p0))%p0 for a in range(p0) for b in range(p0))
# Cech spectral sequence: E_r^{p,q}->E_r^{p+r,q-r+1}.
R['spectral_degrees']={'differential_bidegree':'(r,1-r)','incoming_to_Er_n0':[(r,('n-'+str(r),r-1)) for r in range(2,7)],'conclusion':'incoming differentials to bottom row total degree n originate in total degree n-1; n-boundary comparison needs q up to n-1, not automatically n+1','dimension_arithmetic':'if support dimension phi_y(R^q f_*F)<=phi_x(F)-q, then p>phi_x(F)-q iff p+q>phi_x(F); p-q is wrong.'}
# Orbit sum transfer: tested on cyclic permutation of the standard 2-simplex's vertices,
# including oriented edges; general algebraic chain identity recorded separately.
def edges_boundary(c):
 r=[0,0,0]
 for (a,b),v in c.items():r[a]-=v;r[b]+=v
 return tuple(r)
edges={(0,1):1,(1,2):1,(2,0):1};assert edges_boundary(edges)==(0,0,0)
R['orbit_transfer']={'example_C3_triangle_orbit_edge_lift':[[k,v] for k,v in edges.items()],'boundary':edges_boundary(edges),'general_identity':'For an orbit [sigma], define T[sigma]=sum_(g in G) g sigma. It is independent of representative and d_i T=T d_i; hence boundary commutes. Projection p_* T=|G| id on the free simplicial chain group, including stabilizer multiplicities.','conclusion':'|G| H_*(E/G) contained in image H_*(E); finite enumeration is illustrative, general chain identity supplies proof.'}
R['degree1_torsion_cocycle']={'field':'K=C(t), Ksep, G=Gal(Ksep/K)','U':'torsion subgroup of Ksep^*=all roots of unity, G acts trivially','cocycle':'c(g)=g(sqrt(t))/sqrt(t) in {+1,-1}','nonzero_in_H1_U':'the quadratic extension K(sqrt(t))/K is nontrivial since t has odd t-adic valuation; cocycle nonzero, all coboundaries for trivial U action are1','zero_in_H1_Ksep_units':'it is the displayed coboundary of sqrt(t)','exact_correction':'For Q=V/U a Q-vector discrete G-module, H^i(Q)=0 i>0. Long exact sequence gives H^i(U)~=H^i(V) i>=2; H^1(U)->H^1(V) onto with kernel image Q^G.'}
R['strict_cd_bound']={'scheme':'Spec F3, dimension0','quadratic_polynomial':'T²+1 irreducible overF3 because squares={0,1}','squares_mod3':sorted({x*x%3 for x in range(3)}),'result':'nontrivial C2 torsor SpecF9 ->SpecF3 gives H1_et(F3,Z/2)≠0, contradicting cd<2dim+1; correct weak bound≤1.'}
R['closed_restriction']={
 'origin':'Independent reconstruction of K31-01 scans57–59; not a formal proof certificate from finite enumeration.',
 'injective_sheaf':'On X=A²_Q let I=product_(x∈X) i_x*Q. Each factor is injective because stalk is exact and Q injective; products of injectives are injective. I(U) is all Q-valued functions on U, but i^-1I on a closed Y consists of ambient germs, not all functions on Y.',
 'nonflasque_example':'Y=V(xy), p=(0,0). On Y−p the constant ambient germs0 and1 on the two disjoint branches form a section. A germ at p extending it would equal0 and1 on nonempty ambient opens. Those intersect because X is irreducible, a contradiction.',
 'nonacyclic_example':'Y1=V(y), Y2=V(y−x²+1), Y=Y1∪Y2. Their reduced intersection is {a=(-1,0),b=(1,0)}. The closed-cover exact sequence0→I|Y→i1*(I|Y1)⊕i2*(I|Y2)→i12*(I|{a,b})→0 is stalkwise exact.',
 'H1_obstruction':'The pair of ambient constant germs(0 at a,1 at b) is not a difference of global sections on Y1,Y2. Choose representatives f_i,a and f_i,b for a putative section on each irreducible Yi. Compatibility on Yi gives an ambient nonempty open on which f_i,a=f_i,b. The required difference is0 on an ambient open near a and1 on an ambient open near b. All finitely many ambient opens meet in irreducible X, yielding0=1. Hence the cokernel of the H0 difference map, and therefore H1(Y,I|Y), is nonzero. No flasqueness of the restrictions to Yi is needed.',
 'irreducible_surface':'In X=A³_Q take Y=V(z) and X1=V(z−y(y−x²+1)). Both are irreducible affine planes; Z=X1∩Y is the two-curve example. Push the injective all-functions sheaf on X1 forward to X. Closed direct image preserves injectives (its left adjoint inverse image is exact) and is exact. Restriction to Y is the closed pushforward of its restriction to Z, giving the same nonzero H1.'}
# Polynomial identities used in the intersection geometry, checked over Q.
def graph(x,y):return y*(y-x*x+1)
assert all(graph(x,0)==0 and graph(x,x*x-1)==0 for x in range(-4,5))
assert [x for x in range(-4,5) if x*x-1==0]==[-1,1]
R['closed_restriction']['polynomial_check']={'factorization':'y(y−x²+1); quotient by z gives this product exactly','intersection':'y=0 and y=x²−1 imply x²−1=(x−1)(x+1)=0 overQ, two distinct reduced points','sample_values_checked':9,'scope':'Polynomial factorization is the exact argument; the nine evaluations are only a sanity check.'}
R['pointwise_affine_bound']={
 'origin':'New deduction comparing exact published ILO and SGA4 theorems, not a claim of the manuscript.',
 'inputs':'ILO XVIII-B3.2.5: a strictly local regular noetherian R of dimension d≥2 with ℓ invertible and a principal affine U has cd_ℓU=2d−1. ILO XVIII-B4.1.2 gives cd_ℓFracR≤d. SGA4X2.4 gives the reverse, hence equality.',
 'deduction':'For every point y∈U apply SGA4X2.4 to R_y: cd_ℓκ(y)+dimR_y≤cd_ℓFracR=d. Thus the proposed pointwise supremum is≤d<2d−1=cd_ℓU. All ℓ-invertibility hypotheses hold. If ℓ=2, strict henselianity and invertibility of2 give a root of T²+1, hence all residue fields are nonreal; this checks the real exception.',
 'limits':'Depends on the existence theorem and its exact hypotheses, not a newly constructed explicit R; no numerical experiment certifies those inputs.'}
assert all(d<2*d-1 for d in range(2,20))
(root/'outputs'/'calculations.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(R,ensure_ascii=False,indent=2))
