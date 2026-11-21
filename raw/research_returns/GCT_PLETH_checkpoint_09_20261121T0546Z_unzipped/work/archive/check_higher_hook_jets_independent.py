"""T062--63: exact frame-quadric jets and bounded-excess enumeration."""
from pathlib import Path
from fractions import Fraction
from itertools import combinations
from functools import lru_cache
from collections import Counter
import sys,json

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/"theta"/"unstable_hook"))
import second_unstable_hook_positive as target


def compositions(n,d):
    if d==1:
        yield (n,)
        return
    for a in range(n+1):
        for tail in compositions(n-a,d-1):
            yield (a,)+tail


def inverse(A):
    n=len(A);M=[[Fraction(v) for v in row]+[Fraction(i==j) for j in range(n)]
                for i,row in enumerate(A)]
    for i in range(n):
        p=next(j for j in range(i,n) if M[j][i])
        M[i],M[p]=M[p],M[i]
        v=M[i][i];M[i]=[x/v for x in M[i]]
        for j in range(n):
            if j==i or not M[j][i]:continue
            v=M[j][i];M[j]=[x-v*y for x,y in zip(M[j],M[i])]
    return [row[n:] for row in M]


def independent_columns(A):
    rows=[list(map(Fraction,row)) for row in A]
    pivots=[];r=0
    for c in range(len(rows[0])):
        p=next((j for j in range(r,len(rows)) if rows[j][c]),None)
        if p is None:continue
        rows[r],rows[p]=rows[p],rows[r]
        q=rows[r][c];rows[r]=[v/q for v in rows[r]]
        for j in range(len(rows)):
            if j!=r and rows[j][c]:
                q=rows[j][c];rows[j]=[v-q*w for v,w in zip(rows[j],rows[r])]
        pivots.append(c);r+=1
        if r==len(rows):break
    return pivots


def multiply(P,Q,k):
    out={}
    for p,c in P.items():
        for q,d in Q.items():
            exponent=tuple(a+b for a,b in zip(p,q))
            if sum(exponent)<k:
                out[exponent]=out.get(exponent,Fraction())+c*d
    return {p:c for p,c in out.items() if c}


def restrict_quadratic(Q,base,directions,k):
    r=len(directions);zero=(0,)*r
    linear=[]
    for j,v in enumerate(base):
        P={zero:Fraction(v)} if v else {}
        for h,w in enumerate(directions):
            if w[j]:
                exponent=tuple(int(i==h) for i in range(r))
                P[exponent]=Fraction(w[j])
        linear.append(P)
    out={}
    for (i,j),c in Q.items():
        for p,v in multiply(linear[i],linear[j],k).items():
            out[p]=out.get(p,Fraction())+c*v
    return {p:c for p,c in out.items() if c}


def jet_check(m,k):
    d=m-1;r=d-1
    pairs=list(combinations(range(d),2))
    generators=[{pair:Fraction(1),(0,1):Fraction(-1)}
                for pair in pairs if pair!=(0,1)]
    directions=[tuple(int(j==h)-int(j==d-1) for j in range(d)) for h in range(r)]
    derivative=[[sum(c*(-w[i]-w[j]) for (i,j),c in Q.items())
                 for Q in generators] for w in directions]
    pivots=independent_columns(derivative)
    assert len(pivots)==r
    inv=inverse([[row[p] for p in pivots] for row in derivative])
    fs=[]
    for h in range(r):
        Q={}
        for u,p in enumerate(pivots):
            for pair,c in generators[p].items():
                Q[pair]=Q.get(pair,Fraction())+inv[u][h]*c
        fs.append({pair:c for pair,c in Q.items() if c})
    separator={pair:Fraction(2,d*(d-1)) for pair in pairs}
    monomials=[beta for e in range(k) for beta in compositions(e,r)]
    zero=(0,)*r
    matrix=[]
    outside=0
    for point in range(m):
        if point==d:
            base=(-1,)*d;dirs=directions
        else:
            base=tuple(int(j==point) for j in range(d))
            dirs=[tuple(int(j==h) for j in range(d)) for h in range(d) if h!=point]
        p=restrict_quadratic(separator,base,dirs,k)
        f=[restrict_quadratic(Q,base,dirs,k) for Q in fs]
        columns=[]
        for beta in monomials:
            P={zero:Fraction(1)}
            for _ in range(k-sum(beta)):P=multiply(P,p,k)
            for h,exponent in enumerate(beta):
                for _ in range(exponent):P=multiply(P,f[h],k)
            if point!=d:
                assert P=={},(m,k,point,beta,P)
                outside+=1
            else:
                for alpha in monomials:
                    if sum(alpha)<sum(beta):assert not P.get(alpha,0)
                    if sum(alpha)==sum(beta):assert P.get(alpha,0)==int(alpha==beta)
                columns.append(P)
        if point==d:
            matrix=[[P.get(alpha,Fraction()) for P in columns] for alpha in monomials]
    inverse_matrix=inverse(matrix)
    size=len(matrix)
    for i in range(size):
        for j in range(size):
            assert sum(matrix[i][h]*inverse_matrix[h][j] for h in range(size))==int(i==j)
    return size,outside


@lru_cache(None)
def tableaux(shape):
    if not shape:return ((),)
    result=[]
    for i,width in enumerate(shape):
        if i+1<len(shape) and shape[i+1]==width:continue
        smaller=list(shape);smaller[i]-=1
        while smaller and smaller[-1]==0:smaller.pop()
        result.extend(T+((i+1,width),) for T in tableaux(tuple(smaller)))
    return tuple(result)


def main():
    counts=Counter();jets=[]
    for m in (4,5,7):
        for k in range(1,5):
            size,outside=jet_check(m,k)
            counts["jet_coordinate_inverses"]+=1
            counts["jet_basis_polynomials"]+=size
            counts["other_point_zero_jets"]+=outside
            jets.append(dict(m=m,ideal_order=k,jet_dimension=size))
    checked=set()
    for m in range(4,9):
        for r in range(m-1):
            for shape,d in target.target_multiplicities(m,r).items():
                if shape==(m,):continue
                cells=tuple((i+1,j+1) for i,width in enumerate(shape) for j in range(width))
                retained=tuple(c for c in cells if c not in ((1,1),(2,1)))
                b=sum(i*width for i,width in enumerate(shape))
                for budget in range(6):
                    if (shape,budget) not in checked:
                        expect=set()
                        for T in tableaux(shape):
                            comaj=sum(m-j for j in range(1,m) if T[j][0]>T[j-1][0])
                            if comaj-b<=budget:
                                labels={cell:j for j,cell in enumerate(T,1)}
                                expect.add(tuple(labels[c] for c in cells))
                        assert set(target.low_comajor_tableaux(shape,budget))==expect
                        checked.add((shape,budget))
                        counts["complete_low_comajor_sets"]+=1
                    minimum=sum(sorted(j-i+1 for i,j in retained)[:r])
                    expect={frozenset(S) for S in combinations(retained,r)
                            if sum(j-i+1 for i,j in S)-minimum<=budget}
                    got={frozenset(S) for S in target.low_subsets(retained,r,budget)}
                    assert got==expect,(m,r,shape,budget)
                    counts["complete_low_subset_sets"]+=1
                for a in (5,6):
                    points=target.removed_points(m,a,r,shape)
                    assert len(points)==d
                    counts["base_point_sets"]+=1
    receipt={
        "statement":"T062--63 independent jets and bounded-excess audit",
        "status":"PASS",
        "methods":[
            "literal frame cross-quadrics and exact derivative right inverse",
            "truncated rational polynomial products at every frame point",
            "exact inverse of each own-point jet basis matrix",
            "all removable-corner tableaux versus low-excess SSYT output",
            "all retained-cell subsets versus the bounded diagonal window"
        ],
        **dict(counts),
        "jet_cases":jets,
        "original_plethysm_sweep":"not repeated"
    }
    (HERE/"HIGHER_HOOK_JETS_INDEPENDENT_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print(json.dumps({k:v for k,v in receipt.items() if k!="jet_cases"},indent=2))


if __name__=="__main__":main()
