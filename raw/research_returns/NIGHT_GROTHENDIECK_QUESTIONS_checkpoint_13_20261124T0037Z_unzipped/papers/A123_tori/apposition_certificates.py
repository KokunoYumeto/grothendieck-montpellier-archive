#!/usr/bin/env python3
"""Apposition Certificates: exact finite checks for the accompanying paper.

Python 3 standard library only. Run: python3 apposition_certificates.py
The proofs in the paper are independent of this supplementary computation.
CC0 1.0.
"""
from fractions import Fraction as F
from itertools import product, permutations, combinations
from math import gcd, factorial
import json


def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(t,a): return tuple(t*x for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def unit(n,i): return tuple(F(j==i) for j in range(n))
def reflect(v,a): return sub(v,mul(2*dot(v,a)/dot(a,a),a))
def word(v,roots,indices):
    for i in indices: v=reflect(v,roots[i-1])
    return v

def e_certificates():
    result={}
    for r,h,lam,indices,mu,cycle in [
        (6,12,(1,0,0,0,0,0),[1,3,4,2,5,4],(0,0,1,-1,0,1),
         [(0,0,1,-1,0,1),(-1,0,0,1,-1,0),(1,0,-1,0,1,-1)]),
        (7,18,(0,0,0,0,0,0,1),[7,6,5,4,2,3,1,4,3,5,4,6],(0,1,0,-1,1,-1,1),
         [(0,1,0,-1,1,-1,1),(0,-1,0,1,-1,1,-1)])]:
        A=[[2*int(i==j) for j in range(r)] for i in range(r)]
        edges=[(1,3),(2,4),(3,4),(4,5),(5,6)]+([(6,7)] if r==7 else [])
        for i,j in edges: A[i-1][j-1]=A[j-1][i-1]=-1
        def s(v,j): return tuple(v[k]-v[j]*A[j][k] for k in range(r))
        def apply(v,inds):
            for i in inds:v=s(v,i-1)
            return v
        def c(v):return apply(v,range(r,0,-1))
        assert apply(lam,indices)==mu
        for i,v in enumerate(cycle):assert c(v)==cycle[(i+1)%len(cycle)]
        for j in range(r):
            v=tuple(int(i==j) for i in range(r));q=v
            for _ in range(h):q=c(q)
            assert q==v
        orbit={lam};todo=[lam]
        while todo:
            v=todo.pop()
            for j in range(r):
                q=s(v,j)
                if q not in orbit:orbit.add(q);todo.append(q)
        remaining=set(orbit);lengths=[]
        while remaining:
            v=min(remaining);q=c(v);length=1;remaining.remove(v)
            while q!=v:remaining.remove(q);q=c(q);length+=1
            lengths.append(length)
        result[f'E{r}']={'extremal_orbit_size':len(orbit),'coxeter_cycle_lengths':sorted(lengths),'short_word_verified':True}
    return result


def wedge_certificates():
    result={}
    for typ,n in [('F4',4),('E8',8)]:
        e=[unit(n,i) for i in range(n)]
        roots=set()
        for i,j in combinations(range(n),2):
            for a,b in product([-1,1],repeat=2):roots.add(add(mul(a,e[i]),mul(b,e[j])))
        if typ=='F4':
            for i in range(n):
                for a in [-1,1]:roots.add(mul(a,e[i]))
        for signs in product([-1,1],repeat=n):
            if typ=='F4' or sum(x<0 for x in signs)%2==0:
                roots.add(tuple(F(x,2) for x in signs))
        if typ=='F4':
            simple=[sub(e[1],e[2]),sub(e[2],e[3]),e[3],tuple(F(x,2) for x in [1,-1,-1,-1])]
            theta=add(e[0],e[1]);delta=add(e[0],e[2]);alpha=add(e[1],e[2]);d=2;h=12
            a_word=[2,3,4];mu=theta;second_word=[2];height=(8,3,2,1)
        else:
            simple=[tuple(F(x,2) for x in [1,-1,-1,-1,-1,-1,-1,1]),add(e[0],e[1]),sub(e[1],e[0])]+[sub(e[i-1],e[i-2]) for i in range(3,8)]
            theta=add(e[6],e[7]);delta=add(e[5],e[7]);alpha=sub(e[7],e[0]);d=5;h=30
            a_word=[7,6,5,4,2];mu=add(e[1],e[7]);second_word=[7,6,5,4];height=(0,1,2,3,4,5,6,23)
        assert len(roots)==(48 if typ=='F4' else 240)
        assert all(dot(height,a)==1 for a in simple)
        assert all(add(theta,a) not in roots for a in simple)
        raising=[add(delta,a) for a in simple if add(delta,a) in roots]
        assert raising==[theta]
        assert word(theta,simple,a_word)==theta and word(delta,simple,a_word)==alpha
        c=lambda v:word(v,simple,range(n,0,-1))
        mud=mu
        for _ in range(d):mud=c(mud)
        assert {word(theta,simple,second_word),word(delta,simple,second_word)}=={mu,mud}
        assert d*(dot(height,theta)-dot(height,alpha))%h==0
        result[typ]={'root_count':len(roots),'first_heights':[int(dot(height,alpha)),int(dot(height,theta))],'coxeter_power':d,'wedge_certificate_verified':True}
    return result


def zero(n):return [[0 for _ in range(n)] for _ in range(n)]
def transpose(A):return list(map(list,zip(*A)))
def mm(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def madd(A,B):return [[a+b for a,b in zip(ra,rb)] for ra,rb in zip(A,B)]
def mv(A,v):return tuple(sum(a*b for a,b in zip(row,v)) for row in A)
def assert_skew(X,J):assert all(x==0 for row in madd(mm(transpose(X),J),mm(J,X)) for x in row)

def classical_certificates():
    rows=[]
    for r in range(2,9):
        n=2*r;J=zero(n);X=zero(n)
        for i in range(n):J[i][n-1-i]=(-1)**i;X[(i+1)%n][i]=1
        assert_skew(X,J)
        if r>=3:assert (r*2)%n==0
        m=2*r;J=zero(m+1);X=zero(m+1)
        for i in range(m+1):J[i][m-i]=(-1)**i
        for i in range(m):X[i+1][i]+=1
        X[0][m-1]+=1;X[1][m]+=1;assert_skew(X,J)
        if r>=4:
            n=2*r;J=zero(n);X=zero(n)
            for i in range(r):J[i][n-1-i]=J[n-1-i][i]=(-1)**i
            for i in range(1,r):X[i][i-1]+=1;X[n-i][n-i-1]+=1
            for i,j in [(r,r-2),(r+1,r-1),(0,n-2),(1,n-1)]:X[i][j]+=1
            assert_skew(X,J)
            u=[0]*n;u[0]=1;u[-1]=-1;v=[0]*n;v[r-1]=1;v[r]=-1
            assert not any(mv(X,u)) and not any(mv(X,v))
            assert mv(J,u)[1]==mv(J,v)[1]==0
        rows.append({'rank':r,'classical_matrices_verified':True})
    n=4
    coord=[p for p in permutations(range(n)) if all(p[n-1-j]==n-1-p[j] for j in range(n))]
    fourier=[s for s in permutations(range(n)) if all(s[n-1-j]==(s[j]+2)%n for j in range(n))]
    assert len(coord)==len(fourier)==8
    assert all((p[3]-p[2])*(s[1]-s[0])%4!=0 for p in coord for s in fourier)
    return {'ranks':rows,'C2_borel_pairs_verified':len(coord)*len(fourier)}


def g2_certificate():
    weights=[(-2,-1),(-1,-1),(-1,0),(0,0),(1,0),(1,1),(2,1)]
    long={(0,1),(0,-1),(3,1),(-3,-1),(3,2),(-3,-2)}
    pairs=[(i,k) for i,k in combinations(range(7),2) if add(weights[i],weights[k]) in long]
    assert pairs==[(0,1),(0,2),(1,4),(2,5),(4,6),(5,6)]
    q=[0,5,4,3,2,1,0]
    assert all((q[6-i]-q[6-k])%6!=0 for i,k in pairs)
    J=zero(7);X=zero(7)
    for i in range(7):J[i][6-i]=(-1)**i
    for i in range(6):X[i+1][i]=1
    X[0][5]=X[1][6]=1;assert_skew(X,J)
    return {'long_root_wedge_pairs':pairs,'fundamental_pairing_residues_nonzero':True,'cyclic_matrix_skew_adjoint':True}


def flag_orbits(n):
    P=list(permutations(range(n)))
    K=[(a,b,d) for a in range(n) if gcd(a,n)==1 for b in range(n) for d in range(n)]
    def act(q,k):
        p,s=q;a,b,d=k;ai=pow(a,-1,n)
        return tuple((a*x+b)%n for x in p),tuple((ai*x+d)%n for x in s)
    def theta(q):p,s=q;return p[::-1],tuple(-x%n for x in s[::-1])
    seen=set();classes=fixed=opp=fixedopp=0
    for p in P:
        for s in P:
            q=(p,s)
            if q in seen:continue
            orbit={act(q,k) for k in K};assert len(orbit)==len(K);seen.update(orbit)
            classes+=1;f=theta(q) in orbit;fixed+=f
            if n==4:
                o=(p[3]-p[2])*(s[1]-s[0])%4!=0;opp+=o;fixedopp+=f and o
    assert len(seen)==factorial(n)**2
    assert classes==factorial(n)**2//len(K)
    result={'n':n,'classes':classes,'theta_fixed':fixed}
    if n==4:
        assert (classes,fixed,opp,fixedopp)==(18,8,16,8)
        result.update(opposite=opp,fixed_opposite=fixedopp)
    return result


def affine_count(n):
    count=0;fold_count=0
    for a in range(n):
        if gcd(a,n)!=1 or a*a%n!=1:continue
        for b in range(n):
            if (a+1)*b%n or b%gcd(a-1,n)==0:continue
            for d in range(n):
                if (a-1)*d%n or (a*d)%gcd(a+1,n)==0:continue
                count+=1
                if a==n-1:fold_count+=1
    odd=n;s=0
    while odd%2==0:odd//=2;s+=1
    u=odd;primes=0;p=3
    while p*p<=u:
        if u%p==0:
            primes+=1
            while u%p==0:u//=p
        p+=2
    if u>1:primes+=1
    predicted=(n//2 if s==1 else n)*2**primes
    assert count==predicted
    assert fold_count==n//2
    factor=(2**(n//2)*factorial(n//2))**2
    denominator=n*n*sum(gcd(a,n)==1 for a in range(n))
    return {'n':n,'affine_triples':count,'fixed_classes':count*factor//denominator,
            'pointwise_cyclic_triples':fold_count,'pointwise_cyclic_classes':fold_count*factor//denominator}


def main():
    result={'exceptional_short_orbits':e_certificates(),'exceptional_wedges':wedge_certificates(),
            'classical':classical_certificates(),'G2':g2_certificate(),
            'flag_orbits':[flag_orbits(n) for n in [2,3,4,5]],
            'affine_fixed_count':[affine_count(n) for n in range(4,25,2)]}
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
