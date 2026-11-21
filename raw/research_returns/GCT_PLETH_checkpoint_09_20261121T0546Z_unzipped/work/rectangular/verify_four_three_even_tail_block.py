"""R043 literal two-by-two mixed-moment canonical matrix."""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
from math import factorial,comb
from collections import defaultdict
import csv,random
import sympy as sp
from verify_rectangular import sign
from verify_outer4_chambers import actual
from verify_second_row_two_rank_law import product_form

HERE=Path(__file__).resolve().parent

def generators(vectors):
    n=len(vectors);m=len(vectors[0])-1
    w=[tuple(F(v,r[0]) for v in r[1:]) for r in vectors]
    mean=[sum(r[j] for r in w)/n for j in range(m)]
    z=[tuple(r[j]-mean[j] for j in range(m)) for r in w]
    S=sp.Matrix(m,m,lambda i,j:sum(r[i]*r[j] for r in z))
    C1=sp.Matrix(m,m,lambda i,j:sum(r[0]*r[i]*r[j] for r in z))
    C2=sp.Matrix(m,m,lambda i,j:sum(r[1]*r[i]*r[j] for r in z))
    D11=sp.Matrix(m,m,lambda i,j:sum(r[0]**2*r[i]*r[j] for r in z))
    D12=sp.Matrix(m,m,lambda i,j:sum(r[0]*r[1]*r[i]*r[j] for r in z))
    adj=S.adjugate()
    phi1=S[0,0]*sp.trace(adj*C2)-S[0,1]*sp.trace(adj*C1)
    u,v=sp.symbols('u v')
    def mixed(A,B):
        return sp.Poly((S+u*A+v*B).det(),u,v).coeff_monomial(u*v)
    phi2=mixed(D11,C2)-mixed(D12,C1)
    return tuple(F(int(t.p),int(t.q)) for t in (phi1,phi2))

def determinant_patterns(m):
    ans=defaultdict(int);k=m+1
    for tau in permutations(range(k)):
        rows=[]
        for i in range(k):
            e=[0]*m
            if i:e[i-1]+=1
            if tau[i]:e[tau[i]-1]+=1
            rows.append(tuple(e))
        ans[tuple(sorted(rows))]+=sign(tau)*factorial(k)
    return {key:c for key,c in ans.items() if c}

def literal(a,n,m,vectors,extension=0):
    pair={}
    for beta,value in product_form(vectors).items():
        norm=F(value,factorial(n))
        for e in beta:norm*=factorial(e)
        pair[beta]=norm
    def moment(e):
        d=sum(e)
        if d==5:return F(extension*(1+sum((i+2)**v for i,v in enumerate(e))))
        assert d<=4
        return pair.get((n-d,)+tuple(e),0)
    k=m+1
    e1=(1,)+(0,)*(m-1);e2=(0,1)+(0,)*(m-2)
    e11=(2,)+(0,)*(m-1);e12=(1,1)+(0,)*(m-2)
    # scope0: inside the fixed minor; scope1: all a rows.
    terms=[
        ((e11,1),(e2,0)),((e12,1),(e1,0)),
        ((e11,1),(e2,1)),((e12,1),(e1,1)),
        ((e1,1),(e1,1),(e2,0)),((e1,1),(e2,1),(e1,0)),
        ((e11,0),(e2,0)),((e12,0),(e1,0)),
        ((e2,1),(e11,0)),((e1,1),(e12,0)),
        ((e1,1),(e1,0),(e2,0)),((e2,1),(e1,0),(e1,0))]
    totals=[F(0)]*len(terms)
    for inside,coefficient in determinant_patterns(m).items():
        blocks=list(inside)+[(0,)*m]*(a-k)
        for index,factors in enumerate(terms):
            d=len(factors);full=(1<<d)-1
            increments=[]
            for mask in range(1<<d):
                increments.append(tuple(sum(factors[j][0][i] for j in range(d) if mask>>j&1)
                                        for i in range(m)))
            dp={0:F(1)}
            for row,e in enumerate(blocks):
                allowed=full if row<k else sum(1<<j for j in range(d) if factors[j][1])
                coeff={}
                sub=allowed
                while True:
                    coeff[sub]=moment(tuple(e[i]+increments[sub][i] for i in range(m)))
                    if sub==0:break
                    sub=(sub-1)&allowed
                nxt=defaultdict(F)
                for mask,value in dp.items():
                    for add,c in coeff.items():
                        if not(mask&add) and c:nxt[mask|add]+=value*c
                dp=nxt
            totals[index]+=coefficient*dp.get(full,0)
    X=totals[0]-totals[1];Y=totals[2]-totals[3];Z=totals[4]-totals[5]
    J=totals[6]-totals[7];H=totals[8]-totals[9];N=totals[10]-totals[11]
    phi1=F(a*X-k*Y-Z,a*a)
    B=J-F(k,a)*H-N/a
    phi2=(B-phi1)/a
    return tuple(comb(a,k)*t for t in (phi1,phi2))

def matrix(a,n,m):
    k=m+1;l=a-k
    C=[[F(l*l,a*a),F(l,a*a)],[F(k*l,a**3),F((a-1)*l,a**3)]]
    u=F(n*(n-1),(n-2)*(n-3))
    D=[[1,0],[(m+1)*u,-6*u]]
    scalar=F(2*(-1)**m*factorial(a),factorial(a-m-1)*n**(m+1)*(n-1)**(m+1)*(n-2))
    return [[scalar*sum(C[i][q]*D[q][j] for q in range(2)) for j in range(2)] for i in range(2)]

def write(name,rows):
    with (HERE/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)

def main():
    rng=random.Random(43043);rows=[]
    configs=[(m,n) for m in (2,3) for n in (4,5,6)]
    configs +=[(4,5),(4,6),(4,7)]
    for m,n in configs:
        rank=min(2,max(0,n-m-1));old=[]
        for tag in range(max(1,rank)):
            for trial in range(100):
                lower=[[rng.randrange(-3,5) for p in range(m)] for i in range(n)]
                vectors=[(i+2,)+tuple((i+2)*v for v in r) for i,r in enumerate(lower)]
                phi=generators(vectors)
                if rank==0 or sp.Matrix(old+[phi]).rank()==len(old)+1:break
            else:raise AssertionError(('no independent sample',m,n,tag))
            old.append(phi);scale=1
            for r in vectors:scale*=r[0]
            for a in range(m+2,min(m+4,8)+1):
                lhs=literal(a,n,m,vectors)
                mat=matrix(a,n,m)
                rhs=tuple(scale**a*sum(mat[i][j]*phi[j] for j in range(2)) for i in range(2))
                assert lhs==rhs,(a,n,m,tag,lhs,rhs)
                if m==2 and n==4 and a==4:
                    assert literal(a,n,m,vectors,7)==lhs
                for j in (0,1):
                    rows.append(dict(a=a,n=n,m=m,sample=tag,generator=j+1,
                        literal_pairing=str(lhs[j]),matrix_value=str(rhs[j]),status='PASS'))
        print('completed literal mixed block m,n',m,n,'rows',len(rows),flush=True)
    write('FOUR_THREE_EVEN_TAIL_CANONICAL_CHECK.tsv',rows)
    print('PASS literal mixed block pairings',len(rows),flush=True)
    rows=[]
    for a in range(4,9):
        for n in (3,4,5):
            for m in range(2,a):
                lam=(a*n-2*m-3,4,3)+(2,)*(m-2)
                if lam[0]<4:continue
                target=actual((a,),n,lam);source=actual((n,),a,lam)
                want=int(a>=m+3) if n==3 else min(2,max(0,a-m-1))
                source_want=0 if n==3 else min(2,max(0,n-m-1))
                assert target==want and source==source_want,(a,n,m,target,source,want,source_want)
                rows.append(dict(a=a,n=n,m=m,output=','.join(map(str,lam)),
                    target_actual_MN=target,source_actual_MN=source,status='PASS'))
        print('completed mixed family MN a',a,'cases',len(rows),flush=True)
    write('FOUR_THREE_EVEN_TAIL_MN_CHECK.tsv',rows)
    print('PASS mixed family target/source pairs',len(rows),flush=True)

if __name__=='__main__':main()

