from fractions import Fraction
from itertools import combinations
from time import perf_counter
start=perf_counter()
# Exterior algebra of Q^3, indexed by increasing tuples in {0,1,2}.
def wedge_monom(a,b):
    if set(a)&set(b): return (),0
    sign=(-1)**sum(x>y for x in a for y in b)
    return tuple(sorted(a+b)),sign
def add(*polys):
    out={}
    for P in polys:
        for a,c in P.items(): out[a]=out.get(a,Fraction(0))+c
    return {a:c for a,c in out.items() if c}
def scale(P,c):return {a:c*b for a,b in P.items() if c*b}
def wedge(P,Q):
    out={}
    for a,c in P.items():
        for b,d in Q.items():
            m,s=wedge_monom(a,b)
            if s:out[m]=out.get(m,Fraction(0))+s*c*d
    return {a:c for a,c in out.items() if c}
dgenerator=[{(1,2):Fraction(1)},{(0,1):Fraction(1)},{}]
def deriv(P):
    out={}
    for mon,c in P.items():
        for j,g in enumerate(mon):
            term=wedge(wedge({mon[:j]:Fraction(1)},dgenerator[g]),{mon[j+1:]:Fraction(1)})
            out=add(out,scale(term,c*(-1)**j))
    return out
basis=[tuple(s) for n in range(4) for s in combinations(range(3),n)]
checked=0
for a in basis:
    for b in basis:
        A={a:Fraction(1)};B={b:Fraction(1)}
        assert deriv(wedge(A,B))==add(wedge(deriv(A),B),scale(wedge(A,deriv(B)),(-1)**len(a)))
        checked+=1
assert deriv(deriv({():Fraction(1)}))=={}
assert deriv(deriv({(0,):Fraction(1)}))=={(0,1,2):Fraction(1)}
print('L counterexample: exterior algebra basis size',len(basis))
print('Leibniz identity pairs checked:',checked)
print('d^2(1)=',deriv(deriv({():Fraction(1)})))
print('d^2(e0)=',deriv(deriv({(0,):Fraction(1)})))
# Exact arithmetic check of rank-one examples. This supports, not substitutes
# for, the proof over Q_p: sigma=id and an intertwiner c!=0 forces a=b.
def valuation(x,p):
    x=Fraction(x);n=x.numerator;d=x.denominator;v=0
    while n%p==0:n//=p;v+=1
    while d%p==0:d//=p;v-=1
    return v
for p in [2,3,5,7]:
    a,b=Fraction(1),Fraction(1+p)
    assert valuation(a,p)==valuation(b,p)==0 and a!=b
    print('J rank-one parameters:',p,a,b,'slopes',valuation(a,p),valuation(b,p),'difference',b-a)
print('Elapsed seconds:',perf_counter()-start)
