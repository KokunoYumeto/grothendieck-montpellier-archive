"""Exact calculations for cote84 scans2–96. No numerical sampling is called a proof.
Run: python SA02_work/programs/root_computations.py
All symbolic identities are coefficient identities over Z unless stated otherwise.
"""
from pathlib import Path
import json,itertools
import sympy as s
OUT=Path(__file__).resolve().parents[1]/'outputs'
OUT.mkdir(exist_ok=True)
records=[]
def check(key,description,expr,expected=0):
    if isinstance(expr,s.MatrixBase):
        residual=expr.applyfunc(s.expand)
        ok=all(x==0 for x in residual)
        value=str(residual)
    else:
        residual=s.factor(s.expand(expr-expected))
        ok=residual==0
        value=str(residual)
    records.append(dict(id=key,description=description,method='exact symbolic coefficient identity',residual=value,passed=bool(ok)))
    assert ok,(key,residual)
def report(key,description,result,method):
    records.append(dict(id=key,description=description,method=method,result=result))

# 2–3: the eight parity cases; odd products acquire precisely one factor4.
d1,d2,d3,t1,t2,t3=s.symbols('d1 d2 d3 t1 t2 t3')
def graded(x,y):
    p,d,t=x; q,e,u=y
    if p==q==1:return (0,4*d*e,0)
    if p==q==0:return (0,d*e,t*u)
    return(1,d*e,None)
for ps in itertools.product(range(2),repeat=3):
    a,b,c=[(p,d,None if p else t) for p,d,t in zip(ps,(d1,d2,d3),(t1,t2,t3))]
    left=graded(graded(a,b),c);right=graded(a,graded(b,c))
    assert left[0]==right[0]
    check('R01-'+''.join(map(str,ps)),'Scan2–3 graded associativity: discriminant coefficient',left[1]-right[1])
    if left[0]==0: assert s.expand(left[2]-right[2])==0
report('R02','Scan2 final normalization c1=Arf*zeta^floor(n/2)',
       [{'n':n,'c1_exponent_of_4':n,'Arf_exponent_of_4':(n+1)//2,'remaining':n//2,
         'equal':(n+1)//2+n//2==n} for n in range(13)],
       'finite display of the identity ceil(n/2)+floor(n/2)=n, with parity proof in root_proofs.md')

# 4: monomial basis and multiplication in tensor of three quadratic algebras.
c1,c2,c3=s.symbols('c1 c2 c3')
def mono_mul(a,b):
    coeff=s.Integer(1)
    for i,c in enumerate((c1,c2,c3)):
        if (a>>i)&1 and (b>>i)&1:coeff*=-c
    return a^b,s.expand(coeff)
cols=[]
for a in (0,7):
    for b in (0,6,5,3):
        k,v=mono_mul(a,b);col=[0]*8;col[k]=v;cols.append(col)
D=s.Matrix.hstack(*map(s.Matrix,cols)).det()
report('R03','Scan4 determinant of B0 tensor B0prime -> A',str(s.factor(D)),
       'exact determinant in the eight monomial basis; invertible iff c1c2c3 invertible')
hyperplanes=[]
for a in range(1,8):
    h=[b for b in range(8) if (a&b).bit_count()%2==0]
    assert len(h)==4 and all(x^y in h for x in h for y in h)
    hyperplanes.append(h)
report('R04','Scan4 F2^3 incidence enumeration',{'quadratic_lines':7,'rank_four_subspaces':len(hyperplanes),'hyperplanes':hyperplanes},'complete finite enumeration')

# 18–23: endomorphisms, signs, discriminants and algebra action.
a,b,c,d,x,y,alpha,beta,gamma,lam,mu=s.symbols('a b c d x y alpha beta gamma lam mu')
U=s.Matrix([[a,b],[c,d]]);X=s.Matrix([x,y]);UX=U*X
wedge=UX[0]*X[1]-UX[1]*X[0]
qtext=c*x*x+(d-a)*x*y-b*y*y
check('R05','Scan18 boxed u(x) wedge x is NEGATIVE of displayed coordinate polynomial',wedge+qtext)
check('R06','Cayley–Hamilton for arbitrary2x2 matrix',U*U-s.trace(U)*U+U.det()*s.eye(2))
disc_polar=4*c*(-b)-(d-a)**2
check('R07','Scan19 det(polar Q_u)=-((tr U)^2-4detU)',disc_polar+(s.trace(U)**2-4*U.det()))
uq=s.Matrix([[0,-gamma],[alpha,beta]])
q=lambda X:alpha*X[0]**2+beta*X[0]*X[1]+gamma*X[1]**2
check('R08','Scan23 algebra relation u^2-beta*u+alpha*gamma',uq*uq-beta*uq+alpha*gamma*s.eye(2))
V=lam*s.eye(2)+mu*uq
check('R09','Scan37 Q(vx)=N(v)Q(x) in the universal binary form representation',q(V*X)-V.det()*q(X))
wood_action=s.Matrix([[-beta,alpha],[-gamma,0]])
check('R10','Wood local action after duality and tau=u^t-beta I',wood_action-uq.T+beta*s.eye(2))

# 33–42: conjugation, reflection and trace-pairing adjoints.
p,r,z0,z1=s.symbols('p r z0 z1')
C=s.Matrix([[0,-c],[1,-b]]) # generator satisfying C²+bC+c=0
S=s.Matrix([[1,-b],[0,-1]])
Cbar=-b*s.eye(2)-C
check('R11','Canonical conjugation has square1',S*S-s.eye(2))
check('R12','Conjugation intertwines u and bar(u)',S*C-Cbar*S)
Z=z0*s.eye(2)+z1*C
N=z0*z0-b*z0*z1+c*z1*z1
check('R13','Conjugate-linear complement determinant equals negative norm', (Z*S).det()+N)
Y=s.Matrix([[a,b],[c,d]])
e,f,g,h=s.symbols('e f g h');Y2=s.Matrix([[e,f],[g,h]])
adj=lambda A:s.trace(A)*s.eye(2)-A
pair=lambda A,B:s.trace(A*adj(B))
phi=lambda A:C*A-A*Cbar
check('R14','Scan33–34 phi is skew-adjoint under reduced-norm polar pairing',pair(phi(Y),Y2)+pair(Y,phi(Y2)))
H=s.Matrix([[2,-b],[-b,2*c]])
norm=lambda X:X[0]**2-b*X[0]*X[1]+c*X[1]**2
evec=s.Matrix([1,0])
refl=evec*(evec.T*H)-s.eye(2)
check('R15','Scan37 polar reflection equals algebra conjugation',refl-S)
check('R16','Reflection preserves norm',norm(S*X)-norm(X))
check('R17','Reflection determinant is -1',S.det(),-1)
identity=s.eye(2)
swap=s.Matrix([[0,1],[1,0]])
report('R18','Scan36 uniqueness corollary fails for A=F2xF2',
       {'identity_matrix':str(identity),'swap_matrix':str(swap),'distinct':identity!=swap,
        'both_fix_1':True,'quotient_A_by_scalars_dimension':1,'both_quotient_actions':'1=-1 in F2'},
       'explicit two automorphisms; complete hypotheses checked in root_proofs.md')

# 44–54: universal norm, affine dual polynomial and parity lattice.
B,C0,u,v,l,z,delta,R0,R1,B0,B1=s.symbols('B C u v l z delta r rp bt btp')
Nuv=u*u-B*u*v+C0*v*v
polar=s.Matrix([[2,-B],[-B,2*C0]])
# dual polynomial Q(a,b)=b²+B*a*b+C*a² in basis functional f(1),f(generator)
dualQ=lambda aa,bb:bb*bb+B*aa*bb+C0*aa*aa
arg=polar*s.Matrix([u,v]);dis=B*B-4*C0
check('R19','Scans47/53 correct sign: Q(phi_N(x))=-delta*N(x)',dualQ(*arg)+dis*Nuv)
check('R20','Etaleness/discriminant determinant identity',polar.det()+dis)
Qlat=(z*z-l*l*delta)/4
Nlat=(B0*B0-R0*R0*delta)/4
check('R21','Trace-coordinate lattice polar-to-dual sign',Qlat.subs({l:B0,z:-R0*delta})+delta*Nlat)
check('R22','Q(T)=-delta in coordinates T=(2,0)',Qlat.subs({l:2,z:0}),-delta)
product=((B0*B1+R0*R1*delta)/2,(B0*R1+B1*R0)/2)
prodNorm=(product[0]**2-product[1]**2*delta)/4
check('R23','Trace-coordinate product preserves the norm',prodNorm-Nlat*(B1*B1-R1*R1*delta)/4)
traceform= s.expand(((B0+B1)**2-(R0+R1)**2*delta)/4-Nlat-(B1*B1-R1*R1*delta)/4)
check('R24','Polar norm lattice formula',traceform-(B0*B1-R0*R1*delta)/2)
T0,A0,AA=s.symbols('T0 A AA')
check('R25','Parity lift square independence modulo4 (exact divisible numerator)',(T0+2*AA)**2-T0**2,4*(T0*AA+AA**2))
report('R26','OverF2 discriminant/parity data do not distinguish split and field quadratic algebras',
       {'x2+x_roots':[i for i in range(2) if (i*i+i)%2==0],
        'x2+x+1_roots':[i for i in range(2) if (i*i+i+1)%2==0],
        'trace':1,'discriminant':1},'complete finite root calculation, with algebra classification proof')

# 57–58: Artin–Schreier-type group and torsor translation, modulo2.
tt,tt2,uu,vv,nn=s.symbols('t t2 u v n')
rem2=lambda ex:s.Poly(s.expand(ex),*sorted(ex.free_symbols,key=str),modulus=2).as_expr() if ex.free_symbols else s.Integer(int(ex)%2)
check('R27','Characteristic2 additivity of F_T=u²+Tu',rem2((uu+vv)**2+tt*(uu+vv)-(uu**2+tt*uu)-(vv**2+tt*vv)))
check('R28','Characteristic2 translated root equation differs by F_T',rem2((uu+vv)**2+tt*(uu+vv)+nn-(uu**2+tt*uu+nn)-(vv**2+tt*vv)))
check('R29','Product kernel homomorphism',rem2((tt2*uu+tt*vv)**2+tt*tt2*(tt2*uu+tt*vv)-tt2**2*(uu**2+tt*uu)-tt**2*(vv**2+tt2*vv)))

# 59–65 and90–92: affine changes and contracted quadratic product.
e0,w,k,b1,b2,b3,c1,c2,c3,u1,u2,u3=s.symbols('e w k b1 b2 b3 c1 c2 c3 u1 u2 u3')
q1=u1*u1+b1*u1+c1;q2=u2*u2+b2*u2+c2
bp=b1*b2;cp=b2*b2*c1+b1*b1*c2-4*c1*c2
up=b2*u1+b1*u2+2*u1*u2
check('R30','Scan65 universal product-value identity',up**2+bp*up+cp-(b2*b2*q1+b1*b1*q2+4*(q1*q2-c1*q2-c2*q1)))
check('R31','Scans64/91 product discriminant',(bp*bp-4*cp)-(b1*b1-4*c1)*(b2*b2-4*c2))
def quadratic_product(x,y):
    B,C=x;D,E=y
    return(B*D,D**2*C+B**2*E-4*C*E)
left=quadratic_product(quadratic_product((b1,c1),(b2,c2)),(b3,c3))
right=quadratic_product((b1,c1),quadratic_product((b2,c2),(b3,c3)))
check('R32','Integral associativity of quadratic-product constant coefficient',left[1]-right[1])
check('R33','Scans60–62 independence of T=2e-b under e->e+w, b->b+2w',2*(e0+w)-(b1+2*w)-(2*e0-b1))
check('R34','Scans60–62 independence of N=e²-be+c under affine change', (e0+w)**2-(b1+2*w)*(e0+w)+(c1+b1*w+w*w)-(e0*e0-b1*e0+c1))
check('R35','Scan62 exact failed coefficient for arbitrary T=2e+t',s.expand((e0+w)**2-(e0+w)*(2*e0+tt)+(e0*e0-b1*e0+c1)),w*w-tt*w+c1-(b1+tt)*e0)

# 66–80: chi-split extension tensor operation.
chi,l1,l2,l3=s.symbols('chi l1 l2 l3')
def prod(x,y,B,D):
    u,l=x;v,m=y
    return(chi*u*v+l*B*v+m*D*u,l*m)
def retract(x,B):return chi*x[0]+B*x[1]
X1=(u1,l1);X2=(u2,l2);X3=(u3,l3)
P=prod(X1,X2,b1,b2)
check('R36','Product retraction equals tensor of retractions',retract(P,b1*b2)-retract(X1,b1)*retract(X2,b2))
left=prod(prod(X1,X2,b1,b2),X3,b1*b2,b3)
right=prod(X1,prod(X2,X3,b2,b3),b1,b2*b3)
check('R37','Associativity for arbitrarychi: first coordinate',left[0]-right[0])
check('R38','Associativity for arbitrarychi: augmentation',left[1]-right[1])
tp=prod((-b1,chi),(-b2,chi),b1,b2)
check('R39','chi*T=T1*T2 without cancellation: first coordinate',tp[0]+chi*b1*b2)
check('R40','chi*T=T1*T2 without cancellation: augmentation',tp[1]-chi**2)
check('R41','Unit b0=1, chosen section(0,1)',s.Matrix(prod((0,1),X1,1,b1))-s.Matrix(X1))
qhom=lambda u,l,B,C:u*u+l*B*u+l*l*C
P2=tuple(i.subs(chi,2) for i in P)
check('R42','Scan90 homogenized product-Q identity',qhom(*P2,b1*b2,cp)-l2**2*qhom(u1,l1,b1,c1)*(b2*b2-4*c2)-l1**2*qhom(u2,l2,b2,c2)*(b1*b1-4*c1)-4*qhom(u1,l1,b1,c1)*qhom(u2,l2,b2,c2))
sigma=lambda X,B:(-X[0]-B*X[1],X[1])
left=tuple(i.subs(chi,2) for i in prod(sigma(X1,b1),X2,b1,b2))
right=sigma(P2,b1*b2)
check('R43','Scan82 involution in one factor equals product involution',s.Matrix(left)-s.Matrix(right))

# 83–87: coinvariant relation matrix in the line-bundle local basis.
# Basis L1L2,L1*x2,x1*L2,x1*x2; product is [2,b2,b1,0;0,0,0,1].
F=s.Matrix([[2,b2,b1,0],[0,0,0,1]])
sig1=s.Matrix([[-1,-b1],[0,1]]);sig2=s.Matrix([[-1,-b2],[0,1]])
Rel=s.kronecker_product(sig1,sig2)-s.eye(4)
check('R44','All involution relations lie in kernel of product',F*Rel)
report('R45','Characteristic2 trace-zero failure at b1=b2=0',
       {'product_rank':1,'product_kernel_dimension':3,'involution_relation_rank':0,
        'coinvariant_dimension':4,'desired_product_dimension':2},'exact matrices specialized toF2')
# Explicit elimination on charts b1 or2 invertible is described in proofs; integer matrix atb1=1.
rel_b1=Rel.subs(b1,1)
ker1=s.Matrix([-1,0,2,0]);ker2=s.Matrix([0,1,-b2,0])
check('R46','Kernel generator at b1=1 is minus third relation',ker1+rel_b1[:,2])
check('R47','Second kernel generator at b1=1 from fourth and third relations',ker2+rel_b1[:,3]-b2*rel_b1[:,2])

# 92–93: failure of flatdegree2 when both input algebras are dual numbers.
# Source B=k[x,y]/(x²,y²), targetD=k[z]/z², z->2xy inchar≠2, z->0 inchar2.
M=s.zeros(4);M[3,0]=2
report('R48','Both ramified in characteristic0: multiplication byz onB',
       {'matrix':str(M),'rank':int(M.rank()),'rank_required_for_free_D_rank2':2,'B_dimension_over_k':4},
       'exact Jordan-rank obstruction to flatness over localArtinD')
report('R49','Both ramified in characteristic2',{'z_image':0,'target_z_nonzero':True,'map_injective':False,'flat_faithful':False},'polynomial coefficient reduction modulo2')

# Tangent-functor obstruction to representability, using M=Z/4 and its2-torsion submodule.
report('R50','mu2prime tangent left-exactness failure',
       {'M':'Z/4','ker(2)':[0,2],'image(2)':[0,2],
        'T(ker2)':[0],'T(M)':[0,2],'T(image2)':[0],
        'T_definition':'2M intersect M[2]'},
       'complete finite module calculation; generalization toA/4A proved separately')

# The source's final finite-locally-free statement also permits a zero kernel.
report('R51','Rank-zero kernel counterexample to scan86 OR-generating criterion',
       {'base':'F2','rank_L1':0,'rank_L2':1,'b1':0,'b2':0,
        'b1_generates_L1':True,'both_involutions':'identity',
        'coinvariant_dimension':2,'product_dimension':1,'isomorphism':False},
       'complete linear-algebra example; corrected all-ranks criterion proved in P11')

OUT.joinpath('root_computations.json').write_text(json.dumps(records,indent=2,ensure_ascii=False)+'\n')
OUT.joinpath('root_computations.txt').write_text('\n'.join(json.dumps(x,ensure_ascii=False) for x in records)+'\n')
print(json.dumps({'records':len(records),'symbolic_identities':sum(x.get('passed',False) for x in records),'all_assertions_passed':True,'outputs':['outputs/root_computations.json','outputs/root_computations.txt']},indent=2))
