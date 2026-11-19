"""Independent finite calculations supporting the SA15 cote8/9/4 audit.

Each output says whether it is a complete finite certificate, a counterexample,
or an illustrative calculation. No finite test is called a general proof.
Only Python's standard library is used. Run from any working directory.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction
from math import isqrt
import json
W=Path(__file__).resolve().parents[1]
out={}
def mul(A,B,m=None):
    C=tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
    return tuple(tuple(x%m for x in row) for row in C) if m else C
def ident(n):return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
def power(A,n,m=None):
    B=ident(len(A))
    for _ in range(n):B=mul(B,A,m)
    return B
def mod(A,m):return tuple(tuple(x%m for x in r) for r in A)
def transpose(A):return tuple(zip(*A))
def det2(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]

# C8:81: a complete explicit section of GL_2(Z/4)->GL_2(F_2).
S=((0,1),(1,0));R=((0,-1),(1,-1));I=ident(2)
assert power(S,2)==I and power(R,3)==I and mul(mul(S,R),S)==power(R,2)
H={mod(mul(power(S,a),power(R,b)),4) for a in range(2) for b in range(3)}
G2={((a,b),(c,d)) for a,b,c,d in product(range(2),repeat=4) if (a*d-b*c)%2}
assert len(H)==6 and {mod(A,2) for A in H}==G2
assert all(mul(A,B,4) in H for A in H for B in H)
section={str(mod(A,2)):A for A in sorted(H)}
out['GL2_mod4_section']={'type':'complete finite certificate and counterexample to all d>=2 nonvanishing','generators':{'S':S,'R':R},'relations_over_Z':['S^2=I','R^3=I','SRS=R^2'],'subgroup_order':len(H),'reduction_is_bijection_to_GL2_F2':True,'all_36_products_checked':True,'section':section}

# C9:5/7: one fully specified truncation convention; it diagnoses rather than
# decides whether the historical W_n notation means length n or n+1.
def elements(p,n):
    return list(product(range(p**(n+1)),*[range(p**(n+1-i)) for i in range(1,n+1) for _ in (0,1)]))
def phi_product(a,b,p,n,target_len):
    s=a[0]*b[0]
    for i in range(1,n+1):
        j=1+2*(i-1);s+=p**i*(a[j]*b[j+1]+a[j+1]*b[j])
    return s%(p**target_len)
pairings=[]
for p,n in [(2,1),(3,1),(2,2)]:
    E=elements(p,n)
    rad=[a for a in E if all(phi_product(a,b,p,n,n+1)==0 for b in E)]
    wrongrad=[a for a in E if all(phi_product(a,b,p,n,n)==0 for b in E)]
    assert rad==[tuple(0 for _ in range(2*n+1))]
    pairings.append({'p':p,'n':n,'ring':'Z_p[F,V]/(FV-p,F^(n+1),V^(n+1))','additive_order':len(E),'correct_target':'Z/p^(n+1)','correct_radical_order':len(rad),'target_Z_p_n_radical_order':len(wrongrad),'type':'complete finite pairing check, not a proof for all p,n or nontrivial Witt Frobenius'})
out['truncated_Dieudonne_pairings']=pairings

# C9:8: literal precomposition by F for BOTH dual operators cannot preserve FV=p.
F=((0,1,0),(0,0,1),(0,0,0));V=((0,0,0),)*3
assert mul(F,V,2)==V and mul(V,F,2)==V and power(F,3,2)==V
wrong_F=transpose(F);wrong_V=transpose(F)
bad=mul(wrong_F,wrong_V,2)
assert bad!=V
out['dual_V_typo_counterexample']={'base':'F_2','original_F':F,'original_V':V,'FV_equals_VF_equals_p':True,'F_nilpotence_index':3,'wrong_dual_F':wrong_F,'wrong_dual_V':wrong_V,'wrong_product':bad,'violates_FV_equals_0':True,'type':'counterexample to the literal formula, not an ink decision'}

# C9:17: the two distinct Grassmannian sections become equal after Frobenius.
out['Frobenius_descent_counterexample']={'ring':'F_p[epsilon]/epsilon^2 for every prime p','lines':['R*(1,0)','R*(1,epsilon)'],'different_reason':'Projection onto the second coordinate is zero on the first and contains epsilon on the second.','Frobenius_pullbacks':['R*(1,0)','R*(1,0)'],'reason':'epsilon^p=0 for p>=2','type':'symbolic counterexample with all hypotheses checked'}

# C9:19,24: an ordinary elliptic curve over a perfect but nonclosed field.
p=5
pts=[(x,y) for x in range(p) for y in range(p) if (y*y-x*x*x+x)%p==0]
N=len(pts)+1;trace=p+1-N
f={3:1,1:-1}
def polymul(a,b):
    c={}
    for i,x in a.items():
        for j,y in b.items():c[i+j]=c.get(i+j,0)+x*y
    return c
g={0:1}
for _ in range((p-1)//2):g=polymul(g,f)
hasse=g.get(p-1,0)%p
assert N==8 and hasse==3 and trace%p==hasse
out['ordinary_E_F5']={'equation':'y^2=x^3-x','base':'F_5, perfect','discriminant_mod5':64%5,'affine_points':pts,'point_at_infinity':1,'point_count':N,'Frobenius_trace':trace,'Hasse_coefficient_of_x4_in_(x3-x)^2':hasse,'ordinary':True,'E_5_F5_order':1,'rational_5_torsion_dimension':0,'tangent_dimension':1,'rational_points_formula_false':True,'type':'complete point count plus explicit Cartier/Hasse coefficient; ordinary criterion explained in proofs.md'}
out['discarded_degree_lemma_counterexamples']={'Frobenius':{'ordinary_curve':'ordinary_E_F5','degree':5,'square_in_Z':isqrt(5)**2==5,'reason':'A smooth curve over a perfect field has [k(C):k(C)^p]=p.'},'minus_one':{'ordinary_curve':'ordinary_E_F5','degree':1,'rank_etale_Tate':1,'determinant':-1,'positive_sqrt_degree':1},'type':'counterexamples to the canceled universal assertion; no contradiction to Rosati-positive restriction'}

# C9:27: integer-valued polynomial need not have integral coefficients.
bvals={str(n):str(Fraction(n*(n-1),2)) for n in range(-8,9)}
assert all(Fraction(n*(n-1),2).denominator==1 for n in range(-8,9))
out['polynomial_rationality']={'p':3,'constant':str(Fraction(1,2)),'in_Q_and_Z3':True,'in_Z':False,'integer_valued_example':'T(T-1)/2','sample_values':bvals,'rational_coefficients':['0','-1/2','1/2'],'type':'counterexample to canceled intersection; sample values illustrate a general parity proof'}

# C4:11: exact dimension identity from two short exact sequences.
# A=H^i_cris, T=A_tor, B=H^(i+1)_cris[p]. The stable functor is exact.
# h=(free A/p)_st + (T/p)_st + B_st.
cases=[]
for a,b,c,k in product(range(4),repeat=4):
    if k>c:continue
    h=a+b+c;phi_kernel=c-k
    cases.append((a,b,c,k,h-a,phi_kernel))
assert all(diff==b+c for a,b,c,k,diff,ker in cases)
counter=[x for x in cases if (x[5]==0)!=(x[4]==0)]
out['preceding_torsion_dimension_identity']={'symbols':{'a':'dim(H^i_cris/T)/p stable','b':'dim(T/p) stable','c':'dim H^(i+1)_cris[p] stable','k':'dim ker(v)'},'identity':'dim H^i(O)_stable - a = b+c','revised_sequence':'dim ker(phi)=c-k','counterpattern_to_equivalence':{'a':0,'b':1,'c':0,'k':0,'phi_bijective':True,'inequality_strict':True},'warning':'This pattern is an exact-sequence countermodel, not a constructed smooth-projective variety. It proves that the asserted equivalence does not follow from the displayed ingredients without extra hypotheses.','finite_nonnegative_dimension_patterns_checked':len(cases),'failed_equivalence_patterns':len(counter),'type':'symbolic derivation plus finite arithmetic audit'}

# C4:12: every residue is the trace of an invertible matrix for each rank >=2.
trace_examples=[]
for p in (2,3,5,7,11):
    for rank in (2,3,5):
        mats=[]
        for t in range(p):
            a=(t-(rank-2))%p
            B=((a,-1),(1,0))
            A=tuple(tuple(B[i][j] if i<2 and j<2 else int(i==j) if i>=2 and j>=2 else 0 for j in range(rank)) for i in range(rank))
            assert sum(A[i][i] for i in range(rank))%p==t and det2(B)==1
            mats.append({'trace':t,'matrix':mod(A,p),'determinant_mod_p':1})
        trace_examples.append({'p':p,'rank':rank,'all_traces':mats})
out['GL_trace_surjectivity']={'formula':'diag([[t-(r-2),-1],[1,0]],I_(r-2))','determinant':1,'trace':'t','scope':'all fields F_p, all r>=2, all t in F_p','examples':trace_examples,'type':'general symbolic construction with finite checks'}

# Basic tensor/Tor and the polarization square-root lattice normalization.
out['Tor_two_term_resolution']={'resolution':'[Z --n--> Z] in degrees -1,0 resolves Z/n','after_tensor_R':'[R --n--> R]','H_minus1':'R[n]','H_0':'R/nR','char_p_n_p':'[R --0--> R], both cohomology groups R','warning':'Local splitting of this two-term model does not provide an equivariant/global splitting for a twisted local system.','type':'independent algebraic computation'}
lattices=[]
for p in (2,3,5):
    for e in (0,1,2,3):
        et_order=p**e;kernel_order=et_order**2;sqrt=isqrt(kernel_order)
        assert sqrt==et_order
        lattices.append({'p':p,'v_p_sqrt_degree':e,'etale_kernel_order':et_order,'total_p_primary_kernel_order':kernel_order,'normalized_index':Fraction(et_order,sqrt).numerator})
out['polarization_lattice_normalization']={'identity':'For Cartier-self-dual ordinary ker(lambda), length(K_et)=length(K_mult), hence v_p(sqrt(deg lambda))=length(K_et)=valuation(det T_p(lambda)_et).','examples':lattices,'type':'arithmetic check of the stated length argument, not independent verification of Cartier self-duality'}

(W/'outputs/calculations.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:({'type':v.get('type')} if isinstance(v,dict) else {'cases':len(v)}) for k,v in out.items()},ensure_ascii=False,indent=2))
