"""Exact certificates for the manually identified mathematical claims in package p16.
Finite examples are witnesses; general arguments are supplied in computations.md.
Uses rational/integer arithmetic only. No automatic note verdicts.
"""
from itertools import combinations,product
from math import factorial,comb
import sympy as s

def exterior_mul(a,b):
    out={}
    for u,x in a.items():
        for v,y in b.items():
            if u&v: continue
            inversions=sum(1 for i in range(u.bit_length()) if u>>i&1 for j in range(v.bit_length()) if v>>j&1 and i>j)
            w=u|v;out[w]=s.expand(out.get(w,0)+(-1)**inversions*x*y)
    return {u:v for u,v in out.items() if v!=0}
def contract(a,i):
    out={}
    for u,x in a.items():
        if u>>i&1: out[u^(1<<i)]=(-1)**((u&((1<<i)-1)).bit_count())*x
    return out
def adddict(*ds):
    out={}
    for d in ds:
        for k,v in d.items():out[k]=out.get(k,0)+v
    return {k:s.expand(v) for k,v in out.items() if v!=0}
def L(a,n):return exterior_mul({3<<(2*j):s.Integer(1) for j in range(n)},a)
def contraction(a,n):return adddict(*(contract(contract(a,2*j),2*j+1) for j in range(n)))
def iterate(f,x,j):
    for k in range(j):x=f(x)
    return x
print('C01 Ordinary exterior model: top power and contraction on L1')
for n in range(1,5):
    top=iterate(lambda x:L(x,n),{0:1},n)
    lower=contraction(L({0:1},n),n)
    print('n=',n,'L^n(1)=',top,'Lambda_std L(1)=',lower)
    assert top=={(1<<(2*n))-1:factorial(n)} and lower=={0:n}
for n in range(1,5):
    for i in range(n+1):
        p={sum(1<<(2*k) for k in range(i)):1}
        for j in range(1,n-i+1):
            actual=contraction(iterate(lambda x:L(x,n),p,j),n)
            rhs={u:j*(n-i-j+1)*v for u,v in iterate(lambda x:L(x,n),p,j-1).items()}
            assert actual==rhs
print('Weighted primitive-string formula checked exactly for n≤4; general proof uses anticommutators, not this range.')

def string_model(n):
    basis=[(i,a) for i in range(n+1) for a in range(n-i+1)]
    index={x:j for j,x in enumerate(basis)};N=len(basis)
    up=s.zeros(N);down=s.zeros(N)
    for (i,a),j in index.items():
        if a<n-i:up[index[i,a+1],j]=1
        if a>0:down[index[i,a-1],j]=1
    bottom=[s.diag(*[int(x==(i,0)) for x in basis]) for i in range(n+1)]
    top=[s.diag(*[int(x==(i,n-i)) for x in basis]) for i in range(n+1)]
    return basis,up,down,bottom,top
print('\nC02 Normalized strings, endpoint identities and matrix units')
for n in range(1,5):
    b,u,d,bot,top=string_model(n);N=len(b);Id=s.eye(N)
    assert u*d==Id-sum(bot,s.zeros(N))
    assert d*u==Id-sum(top,s.zeros(N))
    E={(i,a,c):u**a*bot[i]*d**c for i in range(n+1) for a in range(n-i+1) for c in range(n-i+1)}
    for i,a,c in E:
        M=E[i,a,c]
        expected=s.zeros(N);expected[b.index((i,a)),b.index((i,c))]=1
        assert M==expected
    print('n=',n,'faithful module rank=',N,'algebra rank=',len(E),'formula=',sum(j*j for j in range(1,n+2)))
print('At n=1 the algebra rank is 5. In the i=0 string, a=n+1 yields zero, so the draft bound 2n−i cannot index nonzero matrix units.')

print('\nC03 Conjugation fixing raising but changing lowering/projectors')
t=s.symbols('t');u=s.Matrix([[0,0],[1,0]]);d=u.T;p0=s.diag(1,0);p2=s.diag(0,1);g=s.eye(2)+t*u
print('g Lambda g^-1 =',s.expand(g*d*(s.eye(2)-t*u)))
assert s.expand(g*d*(s.eye(2)-t*u)-d-t*(p2-p0)+t*t*u)==s.zeros(2)
print('g pi0 g^-1 =',g*p0*(s.eye(2)-t*u))
print('Literal wrong-side inverse condition (Lambda L−1) pi2 =',(d*u-s.eye(2))*p2)
assert (d*u-s.eye(2))*p2==-p2

print('\nC04 Top power does not imply hard Lefschetz: the manuscript six-dimensional algebra')
x,y=s.symbols('x y');G=s.groebner([x**4,y*y-x*y,x*x*y-x**3,x**3*y],y,x,order='lex')
red=lambda z:G.reduce(s.expand(z))[1]
print('Groebner basis:',list(G));print('y^3−x^3=',red(y**3-x**3))
assert red(y**3-x**3)==0 and red(x**3)==x**3
Mx=s.eye(2);My=s.Matrix([[0,0],[1,1]])
print('L=x on H2→H4:',Mx,'det=',Mx.det());print('Lprime=y:',My,'rank=',My.rank())
for z in [1,x,y,x*x,x*y,x**3]:print('basis representative:',z,'normal form:',red(z))

print('\nC05 Discriminant pairing and symbolic blow-up congruence')
a,b,c,v,w=s.symbols('a b c v w');Q=s.Matrix([[a,b],[b,c]]);V=s.Matrix([v,w]);Qnew=(Q-V*V.T).row_join(V).col_join(V.T.row_join(s.Matrix([[-1]])))
S=s.eye(2).row_join(s.zeros(2,1)).col_join(V.T.row_join(s.ones(1,1)))
err=s.simplify(S.T*Qnew*S-s.diag(Q,s.Matrix([[-1]])))
print('S^T Qnew S − diag(Q,−1) =',err,'det S=',S.det());assert err==s.zeros(3)
Q0=s.Matrix([[-2,1],[1,-3]])
print('Example Q=',Q0,'det=',Q0.det(),'inverse=',Q0.inv())

print('\nC06 Finite-field monogenic obstruction')
counts=[]
for z in product(range(2),repeat=3):
    # A polynomial on F2 is determined by its two values; enumerate its image in F2^3.
    image={tuple(values[zi] for zi in z) for values in product(range(2),repeat=2)}
    counts.append(len(image))
print('Sizes of F2[z] for all z in F2^3:',counts,'maximum=',max(counts),'ambient size=',8)
assert max(counts)==4
print('Nonflat finite-algebra witness: A=k[t], B=A×A/(t); t·(0,1)=0, (0,1)≠0. Fibers: k(q) away from t=0 and k×k at t=0. This is a symbolic module argument, not a point-sample test.')

print('\nC07 Chern expansion and elliptic-product witness')
r,z=s.symbols('r z');
for k in range(1,6):
    coefficient=(-1)**k*s.prod(r-j for j in range(k))/(s.factorial(k)*r**k)
    print('k=',k,'correct coefficient=',s.factor(coefficient),'weaker integrality expression / c_k=',(-1)**k*r)
chi=s.Integer(2);Dprime_square=s.Integer(8)
c2=(chi-1)/(2*chi)*Dprime_square
print('BEFORE geometric normalization: chi=2 and Dprime^2=8 would give c2=',c2)
# On E1×E2 with L of degrees (1,2), transform is E1hat⊠E2hat with ranks (1,2), degree (−1,−1).
# ch = 2−2h1−h2+h1h2; hence Dprime=2h1+h2 and Dprime^2=4 h1h2.
Dprime_square=s.Integer(4);c2=(chi-1)/(2*chi)*Dprime_square
literal=chi*c2
print('Correct product geometry: ch=2−2h1−h2+h1h2; Dprime=2h1+h2; Dprime²=4[pt]; correct c2=',c2,'literal erroneous coefficient gives=',literal)
assert c2==1 and literal==2
print('The initially transcribed value Dprime²=8 in the working item record was detected and corrected; no such value is used in the claim.')

print('\nC08 Associativity is an independent constraint')
J=s.Matrix([[0,1],[-1,0]]);e=s.Matrix([1,0]);f=s.Matrix([0,1]);phi=lambda v,w:(v.T*J*w)[0]
lhs=phi(e,f)*phi(e,f);rhs=phi(e,e)*phi(f,f)
print('V=Q²,W=0,x=t=e,y=z=f: left=',lhs,'right=',rhs);assert lhs!=rhs
print('Isotropic extension: Q=diag(1,−1), v=(1,1), Q(v,v)=',(s.Matrix([[1,1]])*s.diag(1,-1)*s.Matrix([1,1]))[0])

def fourform_model(C):
    m=C.rows;dim=2*m;pairs=list(combinations(range(dim),2));pindex={p:j for j,p in enumerate(pairs)}
    q=s.zeros(len(pairs));form={}
    for i in range(m):
        for j in range(i+1,m):form[(2*i,2*i+1,2*j,2*j+1)]=C[i,j]
    def eval4(tup):
        if len(set(tup))<4:return s.Integer(0)
        inv=sum(tup[i]>tup[j] for i in range(4) for j in range(i+1,4))
        return (-1)**inv*form.get(tuple(sorted(tup)),s.Integer(0))
    for a,p in enumerate(pairs):
        for b,r in enumerate(pairs):q[a,b]=eval4(p+r)
    J=s.diag(*([s.Matrix([[0,1],[-1,0]])]*m))
    wedgeJ=s.Matrix(len(pairs),len(pairs),lambda a,b:J.extract(pairs[a],pairs[b]).det())
    return pairs,q,wedgeJ*q
print('\nC09 Dimension-six rational orbit witness')
C=s.Rational(2,3)*s.Matrix([[0,1,2],[1,0,3],[2,3,0]])
pairs,Q,U=fourform_model(C);xi=s.zeros(15,1)
xi[pairs.index((2,3))]=s.Rational(1,2);xi[pairs.index((4,5))]=s.Rational(1,2)
pidx=[pairs.index((2*i,2*i+1)) for i in range(3)];ones=s.ones(3,1)
print('C=',C,'det Q=',Q.det(),'Q(xi,xi)=',(xi.T*Q*xi)[0])
print('Q(xi,−) at diagonal pairs =',(Q*xi).extract(pidx,[0]).T)
print('U|span(p_i)=',U.extract(pidx,pidx),'Uxi=',(U*xi).extract(pidx,[0]).T)
print('C1=',(C*ones).T,'C²1=',(C*C*ones).T,'cyclic determinant=',s.Matrix.hstack(ones,C*ones,C*C*ones).det())
assert Q.det()==s.Rational(2097152,59049)
assert (xi.T*Q*xi)[0]==1 and U.extract(pidx,pidx)==C
assert s.Matrix.hstack(ones,C*ones,C*C*ones).det()==s.Rational(-32,27)
assert min(C*ones)>1
print('All C entries nonnegative and min row sum=2; C^r 1≥2^r 1, proving an infinite orbit (not just distinct first iterates).')

print('\nC10 Unbounded-family nonvanishing certificate')
for m in range(1,5):
    # C0 has m two-by-two off-diagonal blocks with distinct eigenvalues d_j>0.
    ds=[s.Rational(m+j,m) for j in range(1,m+1)]
    C0=s.diag(*[s.Matrix([[0,d],[d,0]]) for d in ds]);one=s.ones(2*m,1)
    Kry=s.Matrix.hstack(*[C0**j*one for j in range(m)])
    sel=list(range(0,2*m,2));minor=Kry.extract(sel,list(range(m))).det()
    vand=s.prod(ds[j]-ds[i] for i in range(m) for j in range(i+1,m))
    normalization=(one.T*C0.inv()*one)[0]
    print('m=',m,'dim V=',4*m,'selected Krylov minor=',minor,'Vandermonde=',vand,'normalizing scalar=',normalization)
    assert minor==vand and minor!=0 and normalization>0
print('General family proof: the displayed minor is the Vandermonde in the distinct d_j. Perturb every off-block entry by one rational ε>0 outside finitely many zeros; then det C, the minor, and 1^T C^-1 1 remain nonzero, all C_ij are nonzero, and det Q=det C · product_(i<j) C_ij^4. Scaling C by 1^T C^-1 1 and xi=C^-1 1 gives Q(xi,xi)=1 and cyclic rank≥m.')

print('\nC11 Hyperplane strings and the boxed lowering identity')
for N in range(1,6):
    # X string x0,...,xN; Y surviving string y0,...,yN-1.
    LX=s.zeros(N+1);DX=s.zeros(N+1);DY=s.zeros(N)
    restr=s.zeros(N,N+1);gysin=s.zeros(N+1,N)
    for j in range(N):LX[j+1,j]=1;DX[j,j+1]=1;restr[j,j]=1;gysin[j+1,j]=1
    for j in range(1,N):DY[j-1,j]=1
    assert restr*DX**2*gysin==DY
    assert gysin*restr==LX
    assert restr*DX*gysin==s.eye(N)
    print('X length=',N+1,'Y length=',N,'i* Lambda_X² i_*=Lambda_Y: exact; i_*i*=L_X: exact')
print('An evanescent middle Y summand maps to zero by i_* and has zero Λ_Y, so the identity also holds there. General proof acts on each primitive string.')

print('\nC12 Derived zero-section Tor and RHom boundedness')
for n in range(1,5):print('relative dimension',n,'zero-section self-Tor ranks=',[comb(n,j) for j in range(n+1)])
print('Let L=M have k in every degree i≥0 and zero differentials. Then Hom^0(L,M)=product_(i≥0) k with zero differential, hence H^0 RHom(L,M) is infinite-dimensional. Ext^i(k,M)=k for every i≥0, so the explicit uniform vanishing hypothesis in the manuscript fails. This tests coherence, not just boundedness of RHom.')
print('\nAll exact assertions passed.')
