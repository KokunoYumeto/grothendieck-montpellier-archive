"""Exact, finite certificates for specified source computations.
The symbolic calculations do not purport to prove every geometric premise.
Those premises are checked in outputs/proof_notes.md.
"""
from pathlib import Path
from itertools import permutations, product, combinations
from math import gcd, comb
from functools import reduce
import json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form

OUT=Path(__file__).resolve().parents[1]/'outputs'
OUT.mkdir(exist_ok=True)
results={}

def add(a,b):
    c=a.copy()
    for k,v in b.items():c[k]=c.get(k,0)+v
    return {k:v for k,v in c.items() if v}
def scale(a,n):return {k:n*v for k,v in a.items() if n*v}
def mul(a,b):
    c={}
    for x,u in a.items():
        for y,v in b.items():
            if x&y:continue
            c[x|y]=c.get(x|y,0)+u*v
    return {k:v for k,v in c.items() if v}
def prod(ps):
    a={0:1}
    for p in ps:a=mul(a,p)
    return a
def h(i):return {1<<i:1}
def delta(indices):
    full=sum(1<<i for i in indices)
    return {full^(1<<i):1 for i in indices}
def show(a):return {('1' if k==0 else '*'.join('h'+str(i+1) for i in range(8) if k>>i&1)):v for k,v in sorted(a.items())}
def assert_eq(a,b):assert a==b,(a,b)

tests=[]
for n in (2,3):
    hs=[h(i) for i in range(n)]
    for x in hs:assert_eq(mul(x,x),{});tests.append('h_i^2=0')
    for i in range(n):
        for j in range(i+1,n):
            d=delta([i,j]);ij=mul(hs[i],hs[j])
            assert_eq(mul(d,d),scale(ij,2));assert_eq(mul(d,hs[i]),ij);assert_eq(mul(d,hs[j]),ij)
            tests.append(f'P1^{n}: diagonal square and top-class products {i+1}{j+1}')
ds=delta([0,1,2]);top=prod([h(0),h(1),h(2)])
for p,q in [([0,1],[1,2]),([0,1],[0,2]),([1,2],[0,2])]:assert_eq(mul(delta(p),delta(q)),ds)
for i in range(3):assert_eq(mul(ds,h(i)),top)
assert_eq(mul(ds,ds),{})
for p in [[0,1],[0,2],[1,2]]:assert_eq(mul(delta(p),ds),scale(top,2))
assert_eq(add(delta([0,1]),scale(add(h(0),h(1)),-1)),{})
four=prod([delta([0,1]),delta([2,3]),delta([0,2]),delta([1,3])])
assert_eq(four,{15:2})
results['P1_tables']={'passed':tests,'three_factor_relations':'all displayed identities verified with chi=2','basis_counterexample':'Delta12-h1-h2=0','four_factor_excess':show(four),'hypotheses':'X=P1(C), integral cohomology, h point class, deg h=2'}

M=S.Matrix([[1,1],[1,-1]])
snf=smith_normal_form(M,domain=S.ZZ)
assert M.det()==-2 and sorted(abs(snf[i,i]) for i in range(2))==[1,2]
results['middle_lattice']={'matrix':M.tolist(),'determinant':int(M.det()),'smith_invariants':[1,2],'inverse':str(M.inv()),'cokernel':'Z/2','image':'pairs (a,b) with a=b mod2','lambda_mod_diagonal':'(1,-1) maps to 2 times generator of Z^2/<(1,1)>','hypotheses':'ruling basis alpha,beta, h^nu=alpha+beta, lambda=alpha-beta'}
hh=add(h(0),h(1));lam=add(h(0),scale(h(1),-1))
assert_eq(mul(hh,lam),{});assert_eq(mul(lam,lam),{3:-2})
results['quadric_surface']={'lambda_square':show(mul(lam,lam)),'h_square':show(mul(hh,hh)),'h_lambda':show(mul(hh,lam)),'hypotheses':'Q2=P1xP1, alpha=h1,beta=h2, lambda=alpha-beta'}

def ranks(D):return [2 if D%2==0 and i==D//2 else 1 for i in range(D+1)]
def L(D,i):
    rr=ranks(D)
    if i<0:return S.zeros(rr[0],0)
    if i==D:return S.zeros(0,rr[D])
    if D%2 and i==D//2:return S.Matrix([[2]])
    if D%2==0 and i==D//2-1:return S.Matrix([[1],[1]])
    if D%2==0 and i==D//2:return S.Matrix([[1,1]])
    return S.Matrix([[1]])
def coker(A):
    rank=A.rank();free=A.rows-rank;tors=[]
    if A.rows and A.cols:
        sn=smith_normal_form(A,domain=S.ZZ)
        tors=[int(abs(sn[i,i])) for i in range(min(A.rows,A.cols)) if abs(sn[i,i])>1]
    return free,tors
quadrics={}
for D in range(1,9):
    H={}
    for j in range(D+1):
        free,tors=coker(L(D,j-1))
        if free or tors:H[str(2*j)]={'free_rank':free,'torsion_orders':tors}
        kernel=L(D,j).cols-L(D,j).rank()
        if kernel:H[str(2*j+1)]={'free_rank':int(kernel),'torsion_orders':[]}
    expected=[0,D+1,2*D+1] if D%2 else [0,D,D+1,2*D+1]
    assert sorted(map(int,H))==expected
    quadrics[str(D)]={'L_matrices':[L(D,j).tolist() for j in range(D)],'H_punctured_cone':H}
results['integral_quadric_Gysin']=quadrics
results['finite_coefficients_qualification']='Over Z/2^r, multiplication by2 has both a kernel and cokernel: the odd-dimensional-base punctured cone has an additional adjacent group from Tor. Integral/Z_2 tables cannot be copied unmodified to finite coefficients.'

def wedge(a,b):
    c={}
    for x,u in a.items():
        for y,v in b.items():
            if x&y:continue
            inv=sum(1 for i in range(4) for j in range(4) if (x>>i&1) and (y>>j&1) and i>j)
            c[x|y]=c.get(x|y,0)+u*v*((-1)**inv)
    return {k:v for k,v in c.items() if v}
xi={3:1,12:1};xisq=wedge(xi,xi);assert xisq=={15:2}
results['exterior_model']={'xi_squared':xisq,'ordered_basis':['e1','f1','e2','f2'],'middle_rank_one_map':[2]}

x,y,z=S.symbols('x y z');law=lambda a,b:a+b+3*a*b
assert S.expand(law(law(x,y),z)-law(x,law(y,z)))==0
assert S.cancel(law(x,-x/(1+3*x)))==0
assert S.expand(1+3*law(x,y)-(1+3*x)*(1+3*y))==0
results['Gm_Ga_model']={'associator':0,'inverse_composition':0,'generic_coordinate':'u=1+3x','special_law':'x+y in characteristic3','coordinate_ring':'Z_(3)[x,(1+3x)^-1]','smoothness':'open subscheme of A1_R; no Jacobian condition omitted'}

v=S.Matrix([3,1,-1,-3]);a=S.Matrix([1,2,-7,4]);ones=S.ones(4,1)
assert sum(v)==sum(a)==0 and a.dot(v)==0
assert reduce(gcd,[abs(int(t)) for t in v])==1
assert reduce(gcd,[abs(int(a[i]-a[3])) for i in range(3)])==1
for i in range(4):
    for j in range(i):
        e=S.zeros(4,1);e[i]=1;e[j]=-1
        assert S.Matrix.hstack(a,ones,e).rank()==3
WR=[];WT=[]
for p in permutations(range(4)):
    vp=S.Matrix([v[i] for i in p]);ap=S.Matrix([a[i] for i in p])
    if S.Matrix.hstack(v,vp).rank()==1:WR.append(p)
    if S.Matrix.hstack(a,ones,ap).rank()==2:WT.append(p)
assert len(WR)==2 and len(WT)==1
results['SL4_Weyl_counterexample']={'v':list(map(int,v)),'a':list(map(int,a)),'a_dot_v':0,'character_primitive_in_XstarD':True,'R_primitive_cocharacter':True,'restrictions_four_weights_distinct_on_T':True,'WR_permutations':WR,'WT_permutations':WT,'orders':[2,1],'geometric_hypotheses':'C algebraically closed, G=SL4 smooth connected reductive, D diagonal, R connected1-torus and T connected2-torus, R subset T. Distinct weights force both centralizers=D; normalizers reduce to the enumerated S4 permutations.'}

cones={}
for m in range(1,9):
    ls=S.symbols('l0:'+str(m))
    weights=S.Matrix([*ls,-sum(ls)])
    vs=[S.Matrix([-(m-b)]*(b+1)+[b+1]*(m-b)) for b in range(m)]
    out=S.zeros(m+1,1)
    for b in range(m):out+=(weights[b+1]-weights[b])/S.Integer(m+1)*vs[b]
    assert all(S.simplify(t)==0 for t in out-weights)
    cones[str(m)]='symbolic identity verified under sum(lambda)=0'
results['ordered_weight_cone']={'checks':cones,'formula':'lambda=sum_beta (lambda_(beta+1)-lambda_beta)/(m+1)*v_beta','nonnegative_coefficients':'equivalent to ordered weights','missing_nonzero_counterexample':'K=R^2_{>=0}, x=(1,1) in interior, ell=0 satisfies all weak inequalities and ell(x)=0'}

def f2add(a,b):
    c=a.copy()
    for k,v in b.items():c[k]=(c.get(k,0)+v)%2
    return {k:v for k,v in c.items() if v}
def f2mul(a,b):
    c={}
    for x,u in a.items():
        for y,v in b.items():
            k=tuple(i+j for i,j in zip(x,y))
            if sum(k)<=2:c[k]=(c.get(k,0)+u*v)%2
    return {k:v for k,v in c.items() if v}
unit={(0,0,0):1};us=[{tuple(int(i==j) for i in range(3)):1} for j in range(3)]
def linear(ids):
    p=unit.copy()
    for i in ids:p=f2add(p,us[i])
    return p
def invlinear(ids):
    p=f2add(linear(ids),unit)
    return f2add(f2add(unit,p),f2mul(p,p))
def f2prod(ps):
    p=unit
    for q in ps:p=f2mul(p,q)
    return p
double=f2prod([linear([0,1]),invlinear([0]),invlinear([1])])
triple=f2prod([linear([0,1,2]),linear([0]),linear([1]),linear([2]),invlinear([0,1]),invlinear([0,2]),invlinear([1,2])])
assert double=={(0,0,0):1,(1,1,0):1} and triple==unit
results['Delzant_symbol']={'w_dadb_up_to_degree2':{str(k):v for k,v in double.items()},'w_dadbdc_up_to_degree2':{str(k):v for k,v in triple.items()},'coefficients':'F2; variables u=(a),v=(b),w=(c) formal degree1','interpretation':'w1(dadb)=0,w2(dadb)=u*v; J^3 invisible in degrees1,2'}
for n in range(65):
    for j in range(7):assert comb(n,2**j)%2==((n>>j)&1) if 2**j<=n else ((n>>j)&1)==0
results['real_signature_bits']={'n_checked':'0..64','formula':'binom(n,2^j) mod2 = jth binary digit of n','qualification':'For virtual forms with negative signature count, use generalized binomial series or add a common positive form before comparing.'}

# The normal-basis Gram matrix of A3 has m13=2, whereas its inverse is the
# Gram matrix of the dual basis. Squared cosine avoids algebraic approximations.
G=S.Matrix([[1,S.Rational(-1,2),0],[S.Rational(-1,2),1,S.Rational(-1,2)],[0,S.Rational(-1,2),1]])
Gi=G.inv();cos13sq=S.cancel(Gi[0,2]**2/(Gi[0,0]*Gi[2,2]))
assert cos13sq==S.Rational(1,9)
assert all(t>=0 for t in Gi)
results['reflection_dual_angle_alarm']={'A3_Gram':str(G),'dual_Gram':str(Gi),'m13':2,'cos_pi_m13':0,'dual_cos13':'1/3','dual_cos13_squared':str(cos13sq),'valid_corollary':'All entries of dual Gram are nonnegative; chamber inner products remain nonnegative.'}

t=S.symbols('t');X=S.symbols('x0:4')
q=sum(x*x for x in X[:3])-t*t*X[3]**2
assert S.expand(q.subs(X[3],S.Symbol('u')/t)-(sum(x*x for x in X[:3])-S.Symbol('u')**2))==0
results['ramified_quadric_smoothing_counterexample']={'family':str(q),'base':'Spec C[[t]], strictly henselian DVR','projective_flat':'primitive degree2 Cartier equation in P3_R; constant Hilbert polynomial; R-torsion-free homogeneous quotient','generic_fibre':'constant split smooth Q2 after u=t*x3, already over C((t))','special_fibre':'rank3 cone over smooth conic, unique singular point[0:0:0:1]','total_space':'singular at that vertex over t=0','inertia_on_H2':'trivial, because generic fibre is already constant','violated_literal_conclusion':'nontrivial inertia on the rank1 vanishing quotient','refinement':'require a regular ordinary quadratic smoothing; even ramified pullback cannot be allowed'}

# P1 correspondence matrices: alpha=sum c_ij h_target^i h_source^j
# acts by integration over source. Integration selects the h_source term.
def op(c):return S.Matrix([[c.get(2,0),c.get(0,0)],[c.get(3,0),c.get(1,0)]])
basis=[{i:1} for i in range(4)];identity=delta([0,1]);assert op(identity)==S.eye(2)
def compose(c,b):
    # target x=0, middle y=1, source z=2; c(x,y),b(y,z)
    cc={((k&1)|((k&2))):v for k,v in c.items()}
    bb={((k&1)<<1)|((k&2)<<1):v for k,v in b.items()}
    p=mul(cc,bb);out={}
    for k,vv in p.items():
        if k&2:
            kk=(k&1)|((k&4)>>1);out[kk]=out.get(kk,0)+vv
    return {k:v for k,v in out.items() if v}
for c,b in product(basis,repeat=2):assert op(compose(c,b))==op(c)*op(b)
for a,b,c in product(basis,repeat=3):assert compose(compose(a,b),c)==compose(a,compose(b,c))
results['P1_correspondence_composition']={'basis_pair_checks':16,'basis_triple_associativity_checks':64,'identity':'h_target+h_source','operator_identification':'2x2 integer matrices','scope':'finite P1 model; general proof separately uses projection/base change'}

# The five-point P2 chart displayed on11/043. The structural proof in the
# companion is general; this exact rational example checks all chart conditions.
frame=S.Matrix([[1,2,0],[0,1,3],[1,0,1]])
u=S.Matrix([2,3,5]);v0=S.Matrix([7,11,13])
assert frame.det()!=0 and all(z!=0 for z in [u[0],u[1],v0[1],v0[2]])
diag=S.diag(u[1]/u[0],1,v0[1]/v0[2]);normalizer=diag*frame.inv()
normalized_frame=normalizer*frame
assert normalized_frame.is_diagonal() and normalized_frame.det()!=0
p3=normalizer*(frame*u);p3=S.simplify(p3/p3[1])
p4=normalizer*(frame*v0);p4=S.simplify(p4/p4[1])
assert p3[0]==p3[1]==1 and p4[1]==p4[2]==1
results['GIT_five_point_chart']={'frame':str(frame),'frame_determinant':str(frame.det()),'u':str(u),'v':str(v0),'nonzero_conditions':'u0,u1,v1,v2 all nonzero','normalizing_matrix':str(normalizer),'P3_normalized':str(p3),'P4_normalized':str(p4),'scope':'Exact permitted P2 example; uniqueness follows from the two diagonal-scaling ratios. Does not certify absent general R-chart pages.'}

# Greedy minimum-weight independent basis, checked against every basis in
# three concrete rational configurations with ties and negative weights.
columns=[S.Matrix(c) for c in [(1,0,0),(0,1,0),(0,0,1),(1,1,0),(0,1,1),(1,0,1)]]
greedy_checks=[]
for weights in [(-3,-1,0,2,5,8),(0,0,0,0,0,0),(5,-2,3,-2,4,0)]:
 chosen=[]
 for j in sorted(range(6),key=lambda j:(weights[j],j)):
  if S.Matrix.hstack(*(columns[i] for i in chosen+[j])).rank()>len(chosen):chosen.append(j)
  if len(chosen)==3:break
 bases=[b for b in combinations(range(6),3) if S.Matrix.hstack(*(columns[i] for i in b)).det()!=0]
 best=min(sum(weights[i] for i in b) for b in bases)
 assert sum(weights[i] for i in chosen)==best
 greedy_checks.append(dict(weights=weights,chosen=chosen,minimum_weight=best,bases_checked=len(bases)))
results['GIT_greedy_basis']={'checks':greedy_checks,'scope':'Exact finite examples; the prefix-rank proof in proof_notes.md §3 establishes the general assertion.'}

(OUT/'checks.json').write_text(json.dumps(results,indent=2,ensure_ascii=False,default=lambda x:int(x) if isinstance(x,S.Integer) else str(x))+'\n')
print(json.dumps({'status':'all exact assertions passed','families':list(results),'output':str(OUT/'checks.json')},indent=2))
