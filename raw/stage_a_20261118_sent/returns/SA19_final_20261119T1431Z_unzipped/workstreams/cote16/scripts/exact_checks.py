"""Exact checks of computations already present in cote16 or its earlier notes.

This script does not extend the deferred research directions.  Assertions use
integer/rational/symbolic arithmetic, never floating-point tolerance.  The
general arguments, and the limits of finite matrix checks, are documented in
proof_checks.md.  Output is both readable stdout and a machine-readable JSON.
"""
from pathlib import Path
import json, itertools, math
import sympy as S
ROOT=Path(__file__).resolve().parents[1]
out={}

def wedge(a,b):
    ans={}
    for i,x in a.items():
        for j,y in b.items():
            if i&j: continue
            parity=sum((j&((1<<t)-1)).bit_count() for t in range(i.bit_length()) if i>>t&1)
            k=i|j; ans[k]=ans.get(k,0)+(-1)**parity*x*y
    return {k:S.expand(v) for k,v in ans.items() if v}

def contract(v,t):
    ans={}
    for i,x in v.items():
        if i>>t&1:
            k=i^(1<<t);ans[k]=ans.get(k,0)+(-1)**((i&((1<<t)-1)).bit_count())*x
    return ans

def lower(v,n):
    ans={}
    for t in range(n):
        for i,x in contract(contract(v,2*t),2*t+1).items():ans[i]=ans.get(i,0)+x
    return {i:x for i,x in ans.items() if x}

ext=[]
for n in range(1,6):
    xi={(1<<(2*j))|(1<<(2*j+1)):S.Integer(1) for j in range(n)}
    z={0:S.Integer(1)}; powers=[z]
    for j in range(1,n+1): z=wedge(xi,z);powers.append(z)
    fact=z[(1<<(2*n))-1]
    assert fact==math.factorial(n)
    factors=[]
    for j in range(1,n+1):
        got=lower(powers[j],n); f=j*(n-j+1)
        assert got=={i:f*x for i,x in powers[j-1].items()}; factors.append(f)
    ext.append(dict(n=n,top_coefficient=int(fact),contraction_on_L1=int(lower(xi,n)[0]),string_coefficients=factors))
out['exterior_model']=ext

def shift(r):
    L=S.zeros(r+1)
    for a in range(r): L[a+1,a]=1
    return L,L.T

norm=[]
for n in range(0,6):
    lengths=[n-i for i in range(n+1)]
    L=S.diag(*[shift(r)[0] for r in lengths]);D=L.T;I=S.eye(L.rows);e=I-L*D
    offsets=[];p=0
    for r in lengths: offsets.append(p);p+=r+1
    units=0
    for i,r in enumerate(lengths):
        ei=e*D**r*L**r*e-e*D**(r+1)*L**(r+1)*e
        expected=S.zeros(L.rows);expected[offsets[i],offsets[i]]=1
        assert ei==expected
        for b in range(r+1):
            for a in range(r+1):
                u=L**b*ei*D**a; v=S.zeros(L.rows);v[offsets[i]+b,offsets[i]+a]=1
                assert u==v;units+=1
    assert units==(n+1)*(n+2)*(2*n+3)//6
    norm.append(dict(n=n,module_rank=L.rows,algebra_rank=units,integral_matrix_units='all verified'))
out['normalized_strings']=norm

t=S.symbols('t');L,D=shift(1);I=S.eye(2);P0=S.diag(1,0);P2=S.diag(0,1);g=I+t*L
conj=S.expand(g*D*(I-t*L));rhs=D+t*(P2-P0)-t*t*L
assert conj==rhs
out['nonuniqueness']={'gLambda_g_inverse':str(conj),'difference_from_Lambda':str(conj-D),'g_L_g_inverse':str(g*L*(I-t*L))}
wrong=(D*L-I)*P2
assert wrong==-P2
out['scan17_wrong_projector']={'(Lambda L-1) pi_top':str(wrong),'correct_pair':str((D*L-I)*P0)+','+str((L*D-I)*P2)}

a,b,c,v,w=S.symbols('a b c v w');Q=S.Matrix([[a,b],[b,c]]);vec=S.Matrix([v,w]);Qp=(Q-vec*vec.T).row_join(vec).col_join(vec.T.row_join(S.Matrix([[-1]])))
T=S.eye(3);T[2,0]=v;T[2,1]=w
assert S.simplify(T.T*Qp*T-S.diag(Q,S.Matrix([[-1]])))==S.zeros(3)
out['blowup']={'Qprime':str(Qp),'unimodular_change':str(T),'congruence':str(S.simplify(T.T*Qp*T)),'det_change':str(T.det())}

# A basis of the six-dimensional graded algebra in scan 22 is
# 1; L,Lprime; L²,LLprime; L³.  Relations are checked by multiplication matrices.
ML=S.zeros(6);MP=S.zeros(6)
for j,i in [(0,1),(1,3),(2,4),(3,5),(4,5)]:ML[i,j]=1
for j,i in [(0,2),(1,4),(2,4),(3,5),(4,5)]:MP[i,j]=1
assert ML*MP==MP*ML
assert ML**4==S.zeros(6)
assert MP**2==ML*MP and ML**2*MP==ML**3 and ML**3*MP==S.zeros(6)
Lmid=ML.extract([3,4],[1,2]);Pmid=MP.extract([3,4],[1,2])
assert Lmid.det()==1 and Pmid.rank()==1 and MP**3==ML**3!=S.zeros(6)
out['top_nonzero_counterexample']={'basis':['1','L','Lprime','L²','LLprime','L³'],'L':str(ML),'Lprime':str(MP),'L_middle':str(Lmid),'Lprime_middle':str(Pmid),'top_cube':str(ML**3),'relations':'all checked','ranks':[Lmid.rank(),Pmid.rank()]}

hyp=[]
for r in range(1,9):
    X,D=shift(r);Y,E=shift(r-1)
    rho=S.zeros(r,r+1);gam=S.zeros(r+1,r)
    for j in range(r):rho[j,j]=1;gam[j+1,j]=1
    q=gam*E*rho;T=S.eye(r+1)+q
    assert gam*rho==X and rho*gam==Y
    assert E==rho*(D**2)*gam
    assert rho*D*gam==S.eye(r)
    assert X**2*D+2*X*D*X+D*X**2==X*T+T*X
    assert D*X+X*D==T
    for m in range(1,r+3): assert gam*(E**m)*rho==q*(D**(m-1))*q
    for j in range(r-1):
        pY=S.zeros(r);pY[j,j]=1;pX=S.zeros(r+1);pX[j+1,j+1]=1
        assert gam*pY*E*rho==pX
    ptopY=S.zeros(r);ptopY[r-1,r-1]=1
    assert gam*ptopY*E*rho==S.zeros(r+1)
    hyp.append(dict(string_length=r+1,all_compression_identities='verified',projector_transfer='verified for j≤r−2; top boundary gives zero, not top projector'))
out['hyperplane_formulary']=hyp

L2,D2=shift(2);T1=S.diag(0,1,0)
assert L2*T1!=S.zeros(3) and T1*L2*T1==S.zeros(3)
out['scan53_missing_cutoff']={'model':'H*(P²), basis 1,h,h²; n=2,k=1; H¹=H³=0','T1':str(T1),'L_T1':str(L2*T1),'Lambda_L_T1':str(D2*L2*T1),'T1_L_T1':str(T1*L2*T1),'conclusion':'L T1 is nonzero outside H¹; choosing u1=Lambda gives pi2, not pi1=0.'}

# The scan-25 boxed condition, for W=0,V=k², phi(e,f)=1.
J=S.Matrix([[0,1],[-1,0]]);basis=[S.Matrix([1,0]),S.Matrix([0,1])]
def phi(x,y):return (x.T*J*y)[0]
x,y,tv,z=basis[0],basis[1],basis[0],basis[1]
lhs=phi(x,y)*phi(tv,z);rhs=phi(tv,x)*phi(y,z)
assert lhs==1 and rhs==0
out['associativity_independent']={'phi':str(J),'det_phi':str(J.det()),'W_dimension':0,'x,t':'e','y,z':'f','boxed_lhs':str(lhs),'boxed_rhs':str(rhs),'conclusion':'Nondegenerate phi alone does not impose the boxed associativity equation.'}
Qiso=S.diag(1,-1);isov=S.Matrix([1,1]);assert (isov.T*Qiso*isov)[0]==0
out['isotropic_chi_zero']={'Qtilde':str(Qiso),'xi':[1,0],'isotropic_image_generator':[1,1],'norm_xi':1,'norm_image':0,'phi':'any nondegenerate alternating form','chi':'identically zero'}

def pair_Q(C):
    m=C.rows;d=2*m;pairs=list(itertools.combinations(range(d),2));pos={v:i for i,v in enumerate(pairs)}
    def four(a,b,c,d):
        q=[a,b,c,d]
        if len(set(q))<4:return 0
        sign=(-1)**sum(q[i]>q[j] for i in range(4) for j in range(i+1,4));ss=sorted(q)
        if ss[0]%2==0 and ss[1]==ss[0]+1 and ss[2]%2==0 and ss[3]==ss[2]+1:return sign*C[ss[0]//2,ss[2]//2]
        return 0
    Q=S.Matrix([[four(*a,*b) for b in pairs] for a in pairs])
    pindices=[pos[(2*i,2*i+1)] for i in range(m)]
    return Q,pairs,pindices

# Nondegenerate phi does not force its inverse-image xi to have nonzero Q-norm.
Czero=S.Matrix([[0,1,2],[1,0,3],[2,3,0]])
Qzero,pairzero,pzero=pair_Q(Czero)
xzero=S.zeros(len(pairzero),1)
for index,value in zip(pzero,[1,1,-S.Rational(1,5)]):xzero[index]=value
phi_zero=S.zeros(6);q_zero=Qzero*xzero
for a,(i,j) in enumerate(pairzero):phi_zero[i,j]=q_zero[a];phi_zero[j,i]=-q_zero[a]
assert Qzero.det()!=0 and phi_zero.det()!=0 and (xzero.T*Qzero*xzero)[0]==0
out['nonzero_norm_not_automatic']={'C':str(Czero),'Qdet':str(Qzero.det()),'xi_on_pair_plane':[str(xzero[i]) for i in pzero],'phi_on_pair_plane':[str(q_zero[i]) for i in pzero],'phi_determinant':str(phi_zero.det()),'xi_norm':'0','conclusion':'Q and phi are nondegenerate, but xi is isotropic. No nonzero scalar multiple gives norm one, even after extending the field.'}

C=S.Rational(2,3)*S.Matrix([[0,1,2],[1,0,3],[2,3,0]])
Q,pairs,ps=pair_Q(C);xi=S.zeros(len(pairs),1);xi[ps[1]]=xi[ps[2]]=S.Rational(1,2)
Phi=S.zeros(6);qxi=Q*xi
for a,(i,j) in enumerate(pairs):Phi[i,j]=qxi[a];Phi[j,i]=-qxi[a]
assert Phi==S.diag(J,J,J) and (xi.T*Q*xi)[0]==1
# phi-sharp: inverse of x -> phi(x,-), whose coordinate matrix is Phi^T.
sharp=(Phi.T).inv()
L2sharp=S.Matrix([[sharp[i,k]*sharp[j,l]-sharp[i,l]*sharp[j,k] for k,l in pairs] for i,j in pairs])
U=L2sharp*Q
assert U.extract(ps,ps)==C
one=S.ones(3,1);K=S.Matrix.hstack(one,C*one,C**2*one)
assert Q.det()==S.Rational(2097152,59049) and K.det()==-S.Rational(32,27)
assert U*xi==S.Matrix([one[ps.index(i)] if i in ps else 0 for i in range(len(pairs))])
out['six_dimensional_orbit']={'C':str(C),'Qdet':str(Q.det()),'xi_norm':str((xi.T*Q*xi)[0]),'phi':str(Phi),'U_p_block':str(U.extract(ps,ps)),'U_xi_on_p':[str(x) for x in C*xi.extract(ps,[0])],'C1':[str(x) for x in C*one],'C2_1':[str(x) for x in C**2*one],'cyclic_minor':str(K.det()),'minimum_row_sum':str(min(C*one))}

fam=[]
for m in [2,3,4]:
    numpairs=2*m;ds=[1+S.Rational(j+1,m+1) for j in range(m)];eps=S.Rational(1,1000)
    Ce=S.zeros(numpairs)
    for i in range(numpairs):
        for j in range(i+1,numpairs):Ce[i,j]=Ce[j,i]=ds[i//2] if j==i+1 and i%2==0 else eps
    ones=S.ones(numpairs,1);s=(ones.T*Ce.inv()*ones)[0];Cm=s*Ce;xx=Cm.inv()*ones
    assert s>0 and (xx.T*Cm*xx)[0]==1 and Cm*xx==ones
    Kr=S.Matrix.hstack(*[Cm**j*ones for j in range(m)])
    assert Kr.rank()==m and min(Cm*ones)>1
    # determinant of full Q via its orthogonal 4x4 cross-pair blocks.
    dQ=S.factor(Cm.det()*S.prod(Cm[i,j]**4 for i in range(numpairs) for j in range(i+1,numpairs)))
    assert dQ!=0
    fam.append(dict(m=m,V_dimension=4*m,epsilon=str(eps),normalizing_s=str(s),phi='standard symplectic',xi_norm='1',Q_nondegenerate=True,cyclic_columns_rank=Kr.rank(),minimum_row_sum=str(min(Cm*ones)),determinant_formula='det(C)*product_{i<j} Cij^4'))
out['varying_dimensional_family']=fam

F2=[]
for t in itertools.product([0,1],repeat=3):
    values={tuple(pow(t[i],j,2) for i in range(3)) for j in range(3)}
    # degree-3 split algebra discriminant of [1,x,x²] is Vandermonde squared.
    disc=math.prod((t[j]-t[i])**2 for i in range(3) for j in range(i+1,3))%2
    assert disc==0
    F2.append(dict(element=t,distinct_coordinates=len(set(t)),discriminant=disc))
out['finite_field_monogenic_obstruction']=F2

fx,gy,gx=S.symbols('f_x g_y g_x');Jac=S.Matrix([[fx,0],[gx,gy]])
assert Jac.det()==fx*gy
out['different_transitivity_model']={'jacobian':str(Jac),'determinant':str(Jac.det()),'hypotheses':'presentation by f(x),g(x,y); finite flat complete intersection to identify determinant with the different'}

a,b,c,d=S.symbols('a b c d');A=S.Matrix([[a,b],[c,d]]);det=A.det();inv=((a+d)*S.eye(2)-A)/det
assert S.simplify(A*inv)==S.eye(2)
out['cayley_hamilton_inverse']={'matrix':str(A),'inverse_polynomial':str(inv),'denominator':str(det),'condition':'det≠0 and rational characteristic-polynomial coefficients'}

(ROOT/'outputs/exact_checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
for k,v in out.items():
    print('\n###',k)
    print(json.dumps(v,ensure_ascii=False,indent=2))
print('\nALL EXACT ASSERTIONS PASSED. Finite checks are certificates for the specified examples, not proofs of every parameter value.')
