# Independent check of COUNTING_VARIETIES cp01 core construction (Lemma incidence, normalization, stabilizer h_p identity),
# K3 point counts over F_3, and the unit-clause point count.
import itertools
from collections import defaultdict
def mul(A,B,p):
    C=defaultdict(int)
    for ea,ca in A.items():
        for eb,cb in B.items():
            e=tuple(x+y for x,y in zip(ea,eb)); C[e]=(C[e]+ca*cb)%p
    return {e:c for e,c in C.items() if c}
def add(A,B,p):
    C=defaultdict(int,A)
    for e,c in B.items(): C[e]=(C[e]+c)%p
    return {e:c for e,c in C.items() if c}
def mono(nv,idx_exps,c=1):
    e=[0]*nv
    for i,k in idx_exps: e[i]+=k
    return {tuple(e):c}
def build(cnf,nvars,p):
    # incidences
    inc=[(f,i) for f,cl in enumerate(cnf) for i in sorted(set(abs(l) for l in cl))]
    b=2*len(inc); u=b+p-1
    W=lambda e,a: 2*inc.index(e)+a
    T=lambda j: b+j-1  # t_1..t_{p-1}
    nv=u
    P={tuple([0]*nv):1}
    for f,cl in enumerate(cnf):
        scope=sorted(set(abs(l) for l in cl)); Pf={}
        for a in itertools.product([0,1],repeat=len(scope)):
            asg=dict(zip(scope,a))
            if any((l>0 and asg[l]==1) or (l<0 and asg[-l]==0) for l in cl):
                Pf=add(Pf,mono(nv,[(W((f,i),asg[i]),1) for i in scope]),p)
        P=mul(P,Pf,p)
    for i in range(1,nvars+1):
        fs=[f for f,cl in enumerate(cnf) if i in [abs(l) for l in cl]]
        Qi=add(mono(nv,[(W((f,i),0),1) for f in fs]),mono(nv,[(W((f,i),1),1) for f in fs]),p)
        P=mul(P,Qi,p)
    Z=mono(nv,[(k,1) for k in range(b)])
    G={}
    for e,c in mul(P,mono(nv,[(T(1),p-1)],p-1),p).items(): G=add(G,{e:c},p)  # -t1^{p-1} P
    for j in range(2,p):
        G=add(G,mul(Z,mono(nv,[(T(j),p-1)]),p),p)
    return G,u
def mulc(A,B,p,cap):
    C=defaultdict(int)
    for ea,ca in A.items():
        for eb,cb in B.items():
            e=tuple(x+y for x,y in zip(ea,eb))
            if max(e)>cap: continue
            C[e]=(C[e]+ca*cb)%p
    return {e:c for e,c in C.items() if c}
def hp(F,nv,p):
    F={e:c for e,c in F.items() if max(e)<=p-1}
    Fp=F
    for _ in range(p-2): Fp=mulc(Fp,F,p,p-1)
    return Fp.get(tuple([p-1]*nv),0)
def stab(G,u,p,Q):
    m=Q-1; d=Q+1; nv=d  # x1..xm, y, z
    Y=m; Zc=m+1
    pad=mono(nv,[(i,1) for i in range(u,m)])
    Gl={e+tuple([0]*(nv-u)):c for e,c in G.items()}
    A=add(mul(Gl,pad,p),mono(nv,[(0,m)]),p)
    F=mul(A,mono(nv,[(Y,1),(Zc,1)]),p)
    F=add(F,mono(nv,[(Y,Q+1)]),p)
    for i in range(m): F=add(F,mono(nv,[(i,Q+1)]),p)
    F=add(F,mono(nv,[(0,1),(Zc,Q)],p-1),p)
    return F,nv
def count(cnf,n):
    return sum(all(any((l>0 and a[l-1]) or (l<0 and not a[-l-1]) for l in cl) for cl in cnf) for a in itertools.product([0,1],repeat=n))
tests=[([(1,2),(-1,2)],2),([(1,2,3),(-1,-2),(2,-3)],3),([(1,),(2,-1)],2),([(1,2),(1,-2),(-1,2),(-1,-2)],2),([(1,-2,3),(-1,2)],3)]
for p in (2,3,5):
    for cnf,n in tests:
        S=count(cnf,n)
        G,u=build(cnf,n,p)
        h=hp(G,u,p)
        # least multiple Q of p with Q>=u+2 (stabilization theorem form)
        Q=p*(-(-(u+2)//p))
        F,nv=stab(G,u,p,Q)
        hF=hp(F,nv,p)
        print('p',p,'cnf',cnf,'S',S,'S mod p',S%p,'h_p(G)',h,'h_p(F_G)',hF,'Q',Q,'d',Q+1, 'OK' if h==S%p==hF else 'MISMATCH',flush=True)
# K3 family over F_3: yz(r^2 - a s^2) + y^4 + r^4 + s^4 - r z^3
def proj_count(f,nv,q):
    tot=0
    for v in itertools.product(range(q),repeat=nv):
        if any(v) and f(v)%q==0: tot+=1
    return (tot)//(q-1)
for a in range(3):
    c=proj_count(lambda v: v[2]*v[3]*(v[0]**2-a*v[1]**2)+v[2]**4+v[0]**4+v[1]**4-v[0]*v[3]**3,4,3)
    print('K3 a',a,'#X(F3)',c,'1+a mod 3',(1+a)%3,'count mod 3',c%3)
# unit clause example count: (yA-a)z + y^2 + sum x_i^2 = 0 over F_3 (affine, 10 vars), with A=G x5..x8 + a^8, G=-c^2 b(a+b)+e^2 ab
aff=0
for xs in itertools.product(range(3),repeat=9):
    a_,b_,c_,e_,x5,x6,x7,x8,y=xs
    G=(-c_**2*b_*(a_+b_)+e_**2*a_*b_)
    A=G*x5*x6*x7*x8+a_**8
    coef=(y*A-a_)%3; const=(y**2+sum(t*t for t in (a_,b_,c_,e_,x5,x6,x7,x8)))%3
    aff+= 1 if coef else (3 if const==0 else 0)
print('unit clause affine',aff,'projective',(aff-1)//2)
