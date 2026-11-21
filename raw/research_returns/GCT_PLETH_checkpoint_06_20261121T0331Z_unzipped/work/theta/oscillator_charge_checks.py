"""Exact T052 Weyl identities and finite harmonic-kernel comparisons.

The proposed representation is constructed as a literal rational nullspace
of the lowering and compact raising matrices. Actual plethysms on the
comparison side use the independent rectangular agent's cycle-index/MN code.
"""
from pathlib import Path
from functools import lru_cache
from itertools import product
from fractions import Fraction
from math import factorial, comb
import hashlib
import json
import sys
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'rectangular'))
from verify_rectangular import partitions, character, z
from verify_outer4_chambers import actual


def add(*ops):
    ans = {}
    for op in ops:
        for term, c in op.items():
            ans[term] = ans.get(term, 0) + c
    return {a: c for a, c in ans.items() if c}


def scale(c, op):
    return {a: c*b for a, b in op.items() if c*b}


def multiply(left, right):
    ans = {}
    for (a, b), ca in left.items():
        for (c, d), cb in right.items():
            for nu in product(*(range(min(x, y)+1) for x, y in zip(b, c))):
                coefficient = ca*cb
                for bi, ci, ni in zip(b, c, nu):
                    coefficient *= comb(bi, ni)*factorial(ci)//factorial(ci-ni)
                key = (tuple(ai+ci-ni for ai, ci, ni in zip(a, c, nu)),
                       tuple(bi+di-ni for bi, di, ni in zip(b, d, nu)))
                ans[key] = ans.get(key, 0)+coefficient
    return {a: c for a, c in ans.items() if c}


def comm(left, right):
    return add(multiply(left, right), scale(-1, multiply(right, left)))


def adjoint(op):
    return {(b, a): c for (a, b), c in op.items()}


def weyl_checks(m, r):
    nv = (r+1)*m
    zero = (0,)*nv
    identity = {(zero, zero): Fraction(1)}
    def term(xs=(), ds=()):
        a, b = [0]*nv, [0]*nv
        for i in xs: a[i] += 1
        for i in ds: b[i] += 1
        return {(tuple(a), tuple(b)): Fraction(1)}
    X = lambda a, i: a*m+i
    Y = lambda i: r*m+i
    R = [add(*(term((X(a,i),Y(i))) for i in range(m))) for a in range(r)]
    C = [add(*(term(ds=(X(a,i),Y(i))) for i in range(m))) for a in range(r)]
    A = {}
    for a in range(r):
        for b in range(r):
            A[a,b] = add(*(term((X(a,i),),(X(b,i),)) for i in range(m)),
                         scale(Fraction(m,2)*(a==b), identity))
        A[a,r] = scale(-1,R[a]); A[r,a] = C[a]
    A[r,r] = add(*(scale(-1,term((Y(i),),(Y(i),))) for i in range(m)),
                 scale(-Fraction(m,2),identity))
    B = {}
    for i in range(m):
        for j in range(m):
            B[i,j] = add(*(term((X(a,i),),(X(a,j),)) for a in range(r)),
                         scale(-1,term((Y(j),),(Y(i),))),
                         scale(Fraction(r-1,2)*(i==j),identity))
    cases = 0
    for (a,b), left in A.items():
        for (c,d), right in A.items():
            expected=add(scale(int(b==c),A[a,d]),scale(-int(a==d),A[c,b]))
            assert comm(left,right)==expected,(m,r,'A',a,b,c,d)
            cases += 1
    for (i,j), left in B.items():
        for (p,q), right in B.items():
            expected=add(scale(int(j==p),B[i,q]),scale(-int(i==q),B[p,j]))
            assert comm(left,right)==expected,(m,r,'B',i,j,p,q)
            cases += 1
    for a,left in A.items():
        for b,right in B.items():
            assert not comm(left,right),(m,r,'mixed',a,b)
            cases += 1
    for a in range(r):
        assert adjoint(R[a])==C[a]
        assert adjoint(A[a,r])==scale(-1,A[r,a])
    for a in range(r+1):
        for b in range(r+1):
            expected = scale(-1,A[b,a]) if ((a==r) != (b==r)) else A[b,a]
            assert adjoint(A[a,b])==expected
    for i in range(m):
        for j in range(m): assert adjoint(B[i,j])==B[j,i]
    assert add(*(A[a,a] for a in range(r+1)))==add(*(B[i,i] for i in range(m)))
    return cases


@lru_cache(None)
def compositions(n,m):
    if n<0: return ()
    if m==1: return ((n,),)
    return tuple((a,)+tail for a in range(n+1)
                 for tail in compositions(n-a,m-1))


@lru_cache(None)
def basis(alpha,m,k):
    if min(alpha,default=0)<0: return ()
    ans=[]
    for rows in product(*(compositions(a,m) for a in alpha)):
        v=sum(rows,())
        if all(sum(v[a*m+i] for a in range(len(alpha)))>=k for i in range(m)):
            ans.append(v)
    return tuple(ans)


def lowering(alpha,m,k,a):
    source=basis(alpha,m,k)
    beta=list(alpha); beta[a]-=1
    target=basis(tuple(beta),m,k); index={v:i for i,v in enumerate(target)}
    out=sp.zeros(len(target),len(source))
    for j,v in enumerate(source):
        for i in range(m):
            d=sum(v[row*m+i] for row in range(len(alpha)))
            # Literal Fock differentiation: d-k is the Y_i exponent.
            coefficient=v[a*m+i]*(d-k)
            if coefficient:
                w=list(v); w[a*m+i]-=1
                out[index[tuple(w)],j]+=coefficient
    return out


def raising(alpha,m,k,a,b):
    source=basis(alpha,m,k)
    beta=list(alpha); beta[a]+=1; beta[b]-=1
    target=basis(tuple(beta),m,k); index={v:i for i,v in enumerate(target)}
    out=sp.zeros(len(target),len(source))
    for j,v in enumerate(source):
        for i in range(m):
            if v[b*m+i]:
                w=list(v); w[b*m+i]-=1; w[a*m+i]+=1
                out[index[tuple(w)],j]+=v[b*m+i]
    return out


def permutation(cyc):
    p=[]; start=0
    for length in cyc:
        p.extend(start+(i+1)%length for i in range(length)); start+=length
    return tuple(p)


def permute_monomial(v,p,r,m):
    w=[0]*len(v)
    for a in range(r):
        for i in range(m): w[a*m+p[i]]=v[a*m+i]
    return tuple(w)


def kernel_traces(alpha,m,k,projection=False):
    r=len(alpha); source=basis(alpha,m,k); dim=len(source)
    lowers=[lowering(alpha,m,k,a) for a in range(r)]
    ops=lowers+[raising(alpha,m,k,a,b) for a in range(r) for b in range(a+1,r)]
    equations=sp.Matrix.vstack(*ops) if ops else sp.zeros(0,dim)
    vectors=equations.nullspace()
    K=sp.Matrix.hstack(*vectors) if vectors else sp.zeros(dim,0)
    classes=tuple(partitions(m))
    if K.cols:
        rows=K.T.rref()[1]
        inverse=K[list(rows),:].inv()
        index={v:i for i,v in enumerate(source)}
        traces=[]
        for cyc in classes:
            p=permutation(cyc); pinv=tuple(p.index(i) for i in range(m))
            preimages=[index[permute_monomial(source[i],pinv,r,m)] for i in rows]
            action=inverse*K[preimages,:]
            assert all(a.q==1 for a in [sp.trace(action)])
            traces.append(int(sp.trace(action)))
    else:
        traces=[0]*len(classes)
    if projection and dim:
        T=sp.zeros(dim,dim)
        for a,C in enumerate(lowers):
            beta=list(alpha); beta[a]-=1
            small=basis(tuple(beta),m,k)
            index={v:i for i,v in enumerate(source)}
            R=sp.zeros(dim,len(small))
            for j,v in enumerate(small):
                for i in range(m):
                    w=list(v);w[a*m+i]+=1
                    R[index[tuple(w)],j]+=1
            T+=R*C
        t=sp.Symbol('t'); q=T.charpoly(t).as_poly()
        while q.eval(0)==0: q=q.exquo(sp.Poly(t,t))
        P=sp.zeros(dim,dim)
        for coeff in q.all_coeffs(): P=P*T+coeff*sp.eye(dim)
        P/=q.eval(0)
        assert P*P==P
        assert all(C*P==sp.zeros(C.rows,dim) for C in lowers)
        Cstack=sp.Matrix.vstack(*lowers)
        assert sp.trace(P)==dim-Cstack.rank()
    return classes,tuple(traces),dim,K.cols


def main():
    weyl=sum(weyl_checks(m,m-2) for m in (3,4,5))
    requests=[]
    for m,Nmax in ((3,6),(4,5),(5,3)):
        r=m-2
        for N in range(Nmax+1):
            for alpha in partitions(N):
                if len(alpha)>r: continue
                alpha=alpha+(0,)*(r-len(alpha))
                for k in range(N//m+1): requests.append((m,k,alpha))
    requests += [(5,1,alpha+(0,)*(3-len(alpha)))
                 for alpha in partitions(5) if len(alpha)<=3]
    rows=[]; class_checks=0; projection_checks=0; max_dimension=0
    for m,k,alpha in requests:
        b=sum(alpha)-m*k; t=alpha[0]
        use_projection=(m,k,alpha) in {(3,1,(3,)),(3,1,(4,)),(3,1,(5,)),
                                     (4,0,(2,1)),(4,1,(3,2)),(5,1,(3,1,1))}
        classes,traces,dimension,kernel_dimension=kernel_traces(alpha,m,k,use_projection)
        projection_checks+=use_projection;max_dimension=max(max_dimension,dimension)
        for determinant in (0,1):
            for extension in ((0,1) if k==0 else (0,)):
                n=t-k+determinant+extension
                if n>6: continue
                lam=(t+b+determinant+m*extension,t+determinant)+tuple(
                    t-a+determinant for a in reversed(alpha))
                assert sum(lam)==m*n and all(lam[i]>=lam[i+1] for i in range(m-1))
                expected_values=[]
                for mu in partitions(m):
                    numerator=sum((factorial(m)//z(cyc))*character(mu,cyc)
                                  *((-1)**(m-len(cyc)))**(t+determinant)*trace
                                  for cyc,trace in zip(classes,traces))
                    assert numerator%factorial(m)==0
                    expected=numerator//factorial(m)
                    value=actual(mu,n,lam)
                    assert expected==value,(m,k,alpha,mu,lam,expected,value)
                    rows.append((m,k,alpha,mu,n,lam,value))
                    expected_values.append((mu,value))
                reconstructed=tuple(sum(character(mu,cyc)*v for mu,v in expected_values)
                                    for cyc in classes)
                assert reconstructed==tuple(((-1)**(m-len(cyc)))**(t+determinant)*tr
                                             for cyc,tr in zip(classes,traces))
                class_checks+=len(classes)
        print('checked',m,k,alpha,'ambient',dimension,'highest harmonic',kernel_dimension,flush=True)
    receipt={'statement':'T-052','status':'PASS','exact_Weyl_commutators':weyl,
             'kernel_cases':len(requests),'literal_plethysm_comparisons':len(rows),
             'class_trace_comparisons':class_checks,'rational_projection_checks':projection_checks,
             'maximum_kernel_domain_dimension':max_dimension,
             'method':'normal-ordered exact Weyl algebra; literal rational simultaneous lowering/raising nullspaces; actual cycle-index/Murnaghan-Nakayama comparison',
             'sha256':hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()}
    (HERE/'OSCILLATOR_CHARGE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))


if __name__=='__main__': main()
