"""Independent character construction and exact central-PT optimality certificates.

The character table is reconstructed via Jacobi--Trudi in power sums rather
than the discovery program's Murnaghan--Nakayama recursion. A floating LP
only discovers a dual; integer coefficients are then checked over Q.
The proved optimum concerns central PSD partial-transpose-fixed operators,
not all common-crossing vectors and not the semiring regularization.
"""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction
from collections import Counter
from math import factorial, prod, gcd
from functools import reduce
import argparse, json, hashlib
import numpy as np
import sympy as sp
from scipy.optimize import linprog

ROOT=Path('/workspace/scratch/9f5945cf2012/VPVNP_HINGE_work')

def parts(n,hi=None):
    if n==0:
        yield ();return
    for i in range(min(n,hi or n),0,-1):
        for p in parts(n-i,i):yield(i,)+p

def ztype(p):
    return prod(k**v*factorial(v) for k,v in Counter(p).items())

@lru_cache(None)
def homogeneous(n):
    if n<0:return {}
    return {p:Fraction(1,ztype(p)) for p in parts(n)}

def add_scaled(dest,src,c):
    for p,a in src.items():
        dest[p]=dest.get(p,Fraction())+c*a
        if not dest[p]:del dest[p]

def multiply(A,B):
    C={}
    for p,a in A.items():
        for q,b in B.items():
            t=tuple(sorted(p+q,reverse=True))
            C[t]=C.get(t,Fraction())+a*b
    return {p:a for p,a in C.items() if a}

@lru_cache(None)
def schur_power_sum(shape):
    # Determinant by assigning one column per row, with the inversion sign
    # of the resulting column permutation computed at each insertion.
    m=len(shape);states={0:{():Fraction(1)}}
    for row in range(m):
        nextstates={}
        for mask,poly in states.items():
            for col in range(m):
                if mask>>col&1:continue
                degree=shape[row]-row+col
                if degree<0:continue
                flips=(mask>>(col+1)).bit_count()
                value=multiply(poly,homogeneous(degree))
                add_scaled(nextstates.setdefault(mask|(1<<col),{}),value,(-1)**flips)
        states=nextstates
    return states[(1<<m)-1]

def verify(path):
    raw=path.read_bytes();data=json.loads(raw);n=data['n']
    allparts=[tuple(p) for p in data['all_partitions']]
    assert allparts==list(parts(n))
    chars=[]
    for lam in allparts:
        poly=schur_power_sum(lam)
        row=[poly.get(mu,Fraction())*ztype(mu) for mu in allparts]
        assert all(a.denominator==1 for a in row)
        chars.append(list(map(int,row)))
    assert chars==data['character_table']
    cls=[factorial(n)//ztype(p) for p in allparts]
    assert cls==data['class_sizes']
    la=allparts.index(tuple(data['lambda']));mb=allparts.index(tuple(data['mu']))
    mult=[sum(c*a*b*d for c,a,b,d in zip(cls,chars[la],chars[mb],row))//factorial(n) for row in chars]
    active=[i for i,m in enumerate(mult) if m]
    assert [list(allparts[i]) for i in active]==data['active_partitions']
    T=sp.Matrix([chars[i] for i in active]);dims=[chars[i][-1] for i in active]
    C=sp.Matrix(data['word_counts']);W=sp.diag(*cls)*C
    assert W==W.T
    K=sp.diag(*dims)*T*W*T.T*sp.diag(*dims)/factorial(n)**2
    assert K==sp.Matrix(data['K'])
    ranks=[d*mult[i] for d,i in zip(dims,active)]
    assert ranks==data['ranks']
    D=2*(sp.diag(*ranks)-K);assert D==sp.Matrix(data['D'])
    x=sp.Matrix(data['witness']['coefficients'])
    assert D*x==sp.zeros(len(active),1) and all(a>=0 for a in x)
    assert sum(a*b for a,b in zip(ranks,x))==1
    entropy_products=[prod(a**a for a in allparts[i]) for i in active]
    boundary_product=max(entropy_products[i] for i,a in enumerate(x) if a>0)
    high=[i for i,p in enumerate(entropy_products) if p<boundary_product]
    boundary=[list(allparts[active[i]]) for i,p in enumerate(entropy_products) if p==boundary_product]
    if high:
        F=sp.diag(*[sp.Rational(1,r) for r in ranks])*D
        A=np.array(F[high,:],dtype=float)
        lp=linprog(np.zeros(len(active)),A_ub=-A,b_ub=-np.ones(len(high)),bounds=[(None,None)]*len(active),method='highs')
        assert lp.success,lp.message
        for scale in (10**3,10**6,10**9,10**12):
            ints=[int(round(float(a)*scale)) for a in lp.x]
            common=reduce(gcd,map(abs,ints));ints=[a//common for a in ints]
            y=sp.Matrix(ints);Dy=D*y
            if all(Dy[i]>0 for i in high):break
        else:raise AssertionError('Could not reconstruct exact positive dual')
    else:
        ints=[0]*len(active);Dy=sp.zeros(len(active),1)
    result={
        'status':'PASS exact central PSD PT-fixed support optimum; no full-p0 or regularization upper bound',
        'input':str(path.relative_to(ROOT)),
        'input_sha256':hashlib.sha256(raw).hexdigest(),
        'n':n,'lambda':data['lambda'],'mu':data['mu'],
        'independent_character_method':'Jacobi-Trudi determinant in the power-sum basis',
        'character_entries_checked':len(allparts)**2,
        'active_constituents':len(active),
        'boundary_entropy_product':str(boundary_product),
        'boundary_partitions':boundary,
        'strictly_higher_entropy_indices':high,
        'integer_dual':ints,
        'D_times_dual':[str(a) for a in Dy],
        'dual_min_on_high':str(min((Dy[i] for i in high),default=sp.oo)),
        'finite_optimum_bits':data['witness']['threshold_bits'],
        'scope':'The dual rules out nonzero nonnegative CENTRAL kernel vectors supported strictly above the boundary entropy. It does not rule out noncentral PSD vectors, indefinite common-crossing vectors, or other Schur types.'
    }
    out=ROOT/'outputs'/path.name.replace('.json','_dual_verified.json')
    tmp=out.with_suffix('.json.tmp');tmp.write_text(json.dumps(result,indent=2)+'\n');tmp.replace(out)
    return {k:result[k] for k in ('status','n','lambda','mu','character_entries_checked','active_constituents','boundary_partitions','dual_min_on_high','finite_optimum_bits')}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('inputs',nargs='+');args=parser.parse_args()
    for p in args.inputs:
        print(json.dumps(verify(ROOT/p),indent=2),flush=True)
