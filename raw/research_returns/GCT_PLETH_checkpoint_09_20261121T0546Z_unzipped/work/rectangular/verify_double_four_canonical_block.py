"""Literal row-assignment pairings for R045, independent of the moment matrix."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from collections import Counter,defaultdict
from math import factorial,comb
import csv,json,random
import sympy as sp
from derive_double_four_moment_matrix import a,inds,W,central,basis
from verify_second_row_two_rank_law import product_form
from verify_outer4_chambers import actual
HERE=Path(__file__).resolve().parent

POLYS=[sp.Poly(sp.expand(f),list(W.values()))
       for f in basis({t:central(*t) for t in inds if sum(t)>=2})]
PATTERNS=sorted({tuple(t for t,e in zip(inds,pows) for _ in range(e))
                for f in POLYS for pows,coef in f.terms()})
MATRIX=json.loads((HERE/'DOUBLE_FOUR_MOMENT_MATRIX.json').read_text())['matrix']
C=sp.Matrix([[sp.sympify(v,locals={'a':a}) for v in row] for row in MATRIX])

def rat(x):return Q(int(x.p),int(x.q)) if hasattr(x,'p') else Q(x)
def qvals(vectors):
    n=len(vectors);w=[(Q(r[1],r[0]),Q(r[2],r[0])) for r in vectors]
    mean=[sum(r[j] for r in w)/n for j in range(2)]
    z=[(r[0]-mean[0],r[1]-mean[1]) for r in w]
    M={(p,q):sum(r[0]**p*r[1]**q for r in z) for p,q in inds if p+q>=2}
    return tuple(map(Q,basis(M)))

def literal_all(vectors,amax,limit=4,extension=0):
    n=len(vectors);scale=1
    for r in vectors:scale*=r[0]
    pair={}
    for beta,c in product_form(vectors).items():
        v=Q(c,factorial(n)*scale)
        for e in beta:v*=factorial(e)
        pair[beta]=v
    def moment(e):
        d=sum(e)
        if d>limit:return Q(extension*(1+2**e[0]+3**e[1]))
        return pair.get((n-d,)+e,Q(0))
    cache={}
    for pattern in PATTERNS:
        counts=Counter(pattern);types=tuple(sorted(counts));r=tuple(counts[t] for t in types)
        states=list(product(*(range(c+1) for c in r)))
        transitions={}
        for old in states:
            out=[]
            for inc in product(*(range(r[j]-old[j]+1) for j in range(len(r)))):
                deg=tuple(sum(inc[j]*types[j][v] for j in range(len(r))) for v in (0,1))
                value=moment(deg)
                if not value:continue
                factor=1
                for j in range(len(r)):factor*=comb(r[j]-old[j],inc[j])
                out.append((tuple(old[j]+inc[j] for j in range(len(r))),value*factor))
            transitions[old]=out
        dp={(0,)*len(r):Q(1)};out={}
        for aa in range(1,amax+1):
            nxt=defaultdict(Q)
            for old,val in dp.items():
                for new,m in transitions[old]:nxt[new]+=val*m
            dp=nxt;out[aa]=dp.get(r,Q(0))
        cache[pattern]=out
    result={}
    for aa in range(3,amax+1):
        vals=[]
        for f in POLYS:
            val=Q(0)
            for powers,coeff in f.terms():
                pattern=tuple(t for t,e in zip(inds,powers) for _ in range(e))
                val+=rat(coeff.subs(a,aa))*cache[pattern][aa]
            vals.append(val*scale**aa)
        result[aa]=tuple(vals)
    return result,scale

def exact_matrix(aa,n):
    u=sp.Rational(n*(n-1),(n-2)*(n-3));v=sp.Rational(n*(n-1),(n-2)**2)
    H=sp.Matrix([[1,0,0,0],[8*u,-6*u,0,0],[0,0,-4*v,0],
                 [24*u*u,-36*u*u,0,36*u*u]])
    scalar=sp.Rational(aa*(aa-1)*(aa-2),(n*(n-1))**4)
    return scalar*C.subs(a,aa)*H

def write(name,rows):
    with (HERE/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        w.writeheader();w.writerows(rows)

def config(rng,n):
    raw=[(rng.randrange(-3,5),rng.randrange(-3,5)) for _ in range(n-1)]
    raw.append(tuple(-sum(r[j] for r in raw) for j in (0,1)))
    return [(i+2,(i+2)*r[0],(i+2)*r[1]) for i,r in enumerate(raw)]

def main():
    rng=random.Random(45045);rows=[]
    for n in (4,5,6):
        old=[]
        for tag in range(min(4,n-2)):
            for _ in range(100):
                vectors=config(rng,n);v=qvals(vectors)
                if sp.Matrix(old+[v]).rank()==len(old)+1:break
            else:raise AssertionError('no independent population')
            old.append(v)
            literal,scale=literal_all(vectors,7)
            if n==4 and tag==0:
                altered,_=literal_all(vectors,7,extension=5)
                assert altered==literal
            for aa in range(3,8):
                M=exact_matrix(aa,n)
                wanted=tuple(scale**aa*sum(rat(M[i,j])*v[j] for j in range(4)) for i in range(4))
                assert literal[aa]==wanted,(aa,n,tag,literal[aa],wanted)
                for j in range(4):
                    rows.append(dict(a=aa,n=n,sample=tag,generator=j,
                      literal_pairing=str(literal[aa][j]),matrix_value=str(wanted[j]),status='PASS'))
            print('completed double-four n,sample',n,tag,'pairings',len(rows),flush=True)
    write('DOUBLE_FOUR_CANONICAL_MATRIX_CHECK.tsv',rows)
    print('PASS full block pairings',len(rows),flush=True)
    rows=[]
    for tag in range(2):
        vectors=config(rng,3);v=qvals(vectors)
        assert v[0]
        literal,scale=literal_all(vectors,8,limit=3,extension=0)
        altered,_=literal_all(vectors,8,limit=3,extension=7)
        for aa in range(4,9):
            for name,coeff in (
              ('J',(2,0,aa,0)),
              ('K',(2*(aa-2)*(aa*aa-3*aa+6),-2*aa*(aa*aa-3*aa+3),0,aa*aa*(aa-1)))):
                lhs=sum(coeff[j]*literal[aa][j] for j in range(4))
                assert lhs==sum(coeff[j]*altered[aa][j] for j in range(4))
                scalar=Q(aa*(aa-1)*(aa-2)*(aa-3),72)
                if name=='K':scalar*=Q(aa**3-9*aa**2+56*aa-108,9)
                rhs=scale**aa*scalar*v[0]
                assert lhs==rhs,(aa,tag,name,lhs,rhs)
                rows.append(dict(a=aa,n=3,sample=tag,generator=name,
                    literal_pairing=str(lhs),scalar_value=str(rhs),status='PASS'))
        print('completed cubic double-four sample',tag,'pairings',len(rows),flush=True)
    write('DOUBLE_FOUR_CUBIC_CANONICAL_CHECK.tsv',rows)
    rows=[]
    for aa,n in [(aa,n) for aa in range(3,9) for n in (3,4,5)]+[(aa,2) for aa in range(6,10)]:
        lam=(aa*n-8,4,4)
        if lam[0]<4:continue
        def mult(A,N):
            if N>=4:return min(4,max(0,A-2))
            if N==3:return int(A>=4)+int(A>=6)
            if N==2:return int(A>=6)
            raise AssertionError((A,N))
        target=actual((aa,),n,lam);source=actual((n,),aa,lam)
        assert target==mult(aa,n) and source==mult(n,aa),(aa,n,lam,target,source)
        rows.append(dict(a=aa,n=n,output=','.join(map(str,lam)),
                         target_actual_MN=target,source_actual_MN=source,status='PASS'))
    write('DOUBLE_FOUR_MN_CHECK.tsv',rows)
    print('PASS double-four source/target pairs',len(rows),flush=True)
if __name__=='__main__':main()

