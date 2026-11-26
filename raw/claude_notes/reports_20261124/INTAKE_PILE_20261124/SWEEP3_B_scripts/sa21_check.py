# Independent check of SA21-A27 (finite L: Sigma(M(L)) orthomodular iff conditional lattice),
# SA21-A06 Boolean part (Boolean iff nonisolated points form a chain), SA21-A14a (atom criterion).
# Written from the definitions in supports.tex (Def SA21-A05); none of the run's code used.
import sys, itertools, time
def posets(n):
    # naturally labelled posets: element k added with a down-closed set of {0..k-1} as its strict downset
    def rec(k, down):
        if k==n:
            yield [frozenset(d) for d in down]; return
        # choose a downset D of current poset (down-closed set)
        elems=list(range(k))
        for mask in range(1<<k):
            S={i for i in elems if mask>>i&1}
            if all(down[i]<=S for i in S):
                yield from rec(k+1, down+[S])
    yield from rec(0, [])
def le(down,a,b): return a==b or a in down[b]
def lt(down,a,b): return a in down[b]
def M(down):
    n=len(down)
    syms=[(a,) for a in range(n)]+[(a,b) for a in range(n) for b in range(n) if lt(down,a,b)]
    m=len(syms)
    def plt(U,V):
        return U!=V and all(le(down,u,v) for u in U for v in V)
    N=[0]*m
    for i,U in enumerate(syms):
        for j,V in enumerate(syms):
            if plt(U,V) or plt(V,U): N[i]|=1<<j
    return syms,N
def closed_sets(N,m):
    full=(1<<m)-1
    fam={full}
    gens=set(N)
    frontier=[full]
    # closure under intersection with generators
    while frontier:
        new=[]
        for A in frontier:
            for g in gens:
                B=A&g
                if B not in fam:
                    fam.add(B); new.append(B)
        frontier=new
    return fam
def polar(A,N,m):
    r=(1<<m)-1
    i=0
    while A:
        if A&1: r&=N[i]
        A>>=1; i+=1
    return r
def is_oml(fam,N,m):
    fl=sorted(fam,key=lambda x:bin(x).count('1'))
    pol={A:polar(A,N,m) for A in fl}
    for A in fl:
        pa=pol[A]
        for B in fl:
            if A!=B and A&B==A and (B&pa)==0: return False
    return True
def is_boolean(fam,N,m):
    # Boolean iff OML and (zero meet => orthogonal) ; use A04-free direct check: distributive
    pol={A:polar(A,N,m) for A in fam}
    def join(A,B): return polar(pol[A]&pol[B],N,m)
    L=list(fam)
    if len(L)>400: L=L  # still fine
    for A in L:
        for B in L:
            if A&B==0 and (B & pol[A])!=B: return False  # disjoint not orthogonal
    return is_oml(fam,N,m)
def conditional(down,n):
    for x in range(n):
        for y in range(n):
            ub=[z for z in range(n) if le(down,x,z) and le(down,y,z)]
            if ub:
                if not any(all(le(down,z,w) for w in ub) for z in ub): return False
            lb=[z for z in range(n) if le(down,z,x) and le(down,z,y)]
            if lb:
                if not any(all(le(down,w,z) for w in lb) for z in lb): return False
    return True
def boolean_crit(down,n):
    non=[x for x in range(n) if any(lt(down,x,y) or lt(down,y,x) for y in range(n))]
    return all(le(down,a,b) or le(down,b,a) for a in non for b in non)
def atom_crit(down,n):
    iso=[x for x in range(n) if not any(lt(down,x,y) or lt(down,y,x) for y in range(n))]
    anti=all(not lt(down,a,b) for a in range(n) for b in range(n))
    return anti or not iso
def atoms_ok(fam,syms,N,m):
    nz=[A for A in fam if A]
    atoms={A for A in nz if not any(B!=A and B&A==B for B in nz)}
    for i,s in enumerate(syms):
        if len(s)==1:
            c=polar(N[i],N,m)  # cl{P_x} = N(N({x}))
            if c not in atoms: return False
    return True
maxn=int(sys.argv[1])
for n in range(0,maxn+1):
    t=time.time(); cnt=0; bad=[0,0,0]; stats=[0,0,0]
    for down in posets(n):
        cnt+=1
        syms,N=M(down); m=len(syms)
        fam=closed_sets(N,m)
        oml=is_oml(fam,N,m); cond=conditional(down,n)
        if oml!=cond: bad[0]+=1; print('A27 mismatch',down)
        boo=is_boolean(fam,N,m) if oml else False
        if boo!=boolean_crit(down,n): bad[1]+=1; print('A06 mismatch',down)
        if atoms_ok(fam,syms,N,m)!=atom_crit(down,n): bad[2]+=1; print('A14a mismatch',down)
        stats[0]+=oml; stats[1]+=boo; stats[2]+=len(fam)
    print(f'n={n} labelled posets={cnt} OML={stats[0]} Boolean={stats[1]} mismatches(A27,A06,A14a)={bad} time={time.time()-t:.1f}s',flush=True)
