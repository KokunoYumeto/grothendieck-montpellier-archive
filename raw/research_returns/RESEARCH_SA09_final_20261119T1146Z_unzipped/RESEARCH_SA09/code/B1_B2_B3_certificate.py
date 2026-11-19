"""Exact certificates for B.1--B.3; Python 3 + SymPy only.

Permutations are zero-based tuples; composition a*b means a after b.
Scopes: all 5400 ordered pairs of the specified S6 cycle types; all 24
permutations for the torus counterexample; standard opposite-paired bouquets
of genera 1 through 8. General statements are proved in the paper.
"""
from itertools import permutations
from time import perf_counter
import json
import sympy as s

started = perf_counter()

def compose(a,b): return tuple(a[b[i]] for i in range(len(a)))
def inv(a):
    q = [0]*len(a)
    for i,j in enumerate(a): q[j]=i
    return tuple(q)
def cycles(a):
    left=set(range(len(a))); out=[]
    while left:
        x=min(left); cc=[]
        while x in left:
            left.remove(x); cc.append(x); x=a[x]
        out.append(tuple(cc))
    return out
def ctype(a): return tuple(sorted((len(c) for c in cycles(a)),reverse=True))
def conjugate(a,q): return compose(compose(q,a),inv(q))
def centralizer(*ps):
    return [q for q in permutations(range(len(ps[0])))
            if all(compose(q,p)==compose(p,q) for p in ps)]
def fixes_cycles(q,p):
    return all({q[x] for x in cc}==set(cc) for cc in cycles(p))
def notation(p):
    return ''.join('('+','.join(str(i+1) for i in cc)+')' for cc in cycles(p))

# B.1: the one-vertex, two-edge, one-face torus map.
rho=(1,2,3,0); alpha=(2,3,0,1); face=compose(inv(rho),alpha)
aut=centralizer(rho,alpha)
kernel=[q for q in aut if all(fixes_cycles(q,p) for p in [rho,alpha,face])]
assert len(aut)==4 and len(kernel)==2
assert ctype(rho)==(4,) and ctype(alpha)==(2,2) and ctype(face)==(4,)
print('B1 torus: rho=',notation(rho),'alpha=',notation(alpha),'face=',notation(face))
print('B1 torus: automorphisms=',[notation(x) for x in aut])
print('B1 torus: pinned kernel=',[notation(x) for x in kernel])
print('B1 torus: Gamma size=2; image size=2; actual pinned classes=1; naive count=2')
matchings4=[p for p in permutations(range(4)) if ctype(p)==(2,2)]
assert sum(ctype(compose(inv(rho),p))==(4,) for p in matchings4)==1
# The rigid one-loop sphere still has a nontrivial image on face labels.
rr=(1,0); aa2=(1,0); ff=compose(inv(rr),aa2)
ac=centralizer(rr,aa2)
kk=[q for q in ac if all(fixes_cycles(q,t) for t in [rr,aa2,ff])]
assert len(ac)==2 and len(kk)==1
print('B1 one-loop sphere: Aut size=2; pinned kernel=1; Gamma size=2; pinned classes=1')

# B.2: complete ordered-pair enumeration and conjugacy quotient.
S6=list(permutations(range(6)))
rs=[p for p in S6 if ctype(p)==(3,2,1)]
ss=[p for p in S6 if ctype(p)==(2,2,1,1)]
valid=[(r,a) for r in rs for a in ss if ctype(compose(inv(r),a))==(6,)]
assert len(rs)==120 and len(ss)==45 and len(valid)==2160
r=(1,2,0,4,3,5)
cr=centralizer(r)
aa=[a for a in ss if ctype(compose(inv(r),a))==(6,)]
unseen=set(aa); orbits=[]
while unseen:
    a=min(unseen); orbit={conjugate(a,q) for q in cr}
    assert len(orbit)==6
    orbits.append(orbit); unseen-=orbit
assert len(aa)==18 and len(orbits)==3
reps=[(3,1,5,0,4,2), (3,1,2,0,5,4), (3,5,2,0,4,1)]
assert len({next(i for i,o in enumerate(orbits) if a in o) for a in reps})==3
for j,a in enumerate(reps,1):
    aut=centralizer(r,a)
    assert len(aut)==1
    print('B2 representative',j,notation(r),notation(a),notation(compose(inv(r),a)),
          'automorphisms=',len(aut),'S6 orbit=',720)
mirror=(0,2,1,3,4,5)
assert conjugate(inv(r),mirror)==r
assert conjugate(reps[0],mirror)==reps[2]
assert conjugate(reps[1],mirror)==reps[1]
print('B2 enumeration: rho count=120; involution count=45; pairs tested=5400; admissible=2160; orbits=3')

# Exact polynomial computations in Q[c,z].
c,z,rvar=s.symbols('c z r')
h=z**3*(z-1)**2*(z-c)
G=z*z-(5*c+4)*z/6+c/2
delta=25*c*c-32*c+16
p=25*c**3-12*c*c-24*c-16
P=-delta*p/7776
Q=c*(5*c-8)*(25*c**3-6*c*c+8)/2592
H=z*z+(2*c-2)*z/3+(5*c*c-4*c-4)/12
remainder=s.rem(h,G,z)
assert s.expand(remainder-P*z-Q)==0
assert s.expand(s.diff(h,z)-z*z*(z-1)*6*G)==0
identity=s.expand(h-Q-G**2*H)
assert all(s.rem(v,p,c)==0 for v in s.Poly(identity,z).all_coeffs())
qred=(32-52*c-c*c)/1500
assert s.rem(Q-qred,p,c)==0
assert s.gcd(p,c*(c-1)*delta*Q)==1
assert s.gcd(p,s.discriminant(H,z))==1
assert s.gcd(p,s.resultant(G,H,z))==1
mod7=[int(p.subs(c,i))%7 for i in range(7)]
assert all(mod7)
assert s.discriminant(p,c)==-2**8*3**9
crad=(4+18*rvar+6*rvar*rvar)/25
assert s.rem(s.expand(p.subs(c,crad)),rvar**3-2,rvar)==0
assert s.solve(delta,c)==[s.Rational(16,25)-s.Rational(12,25)*s.I,
                         s.Rational(16,25)+s.Rational(12,25)*s.I]
alpha_expr=(5*c+4)/6; beta_expr=-c/2
A=(alpha_expr-2)*(alpha_expr-c)+beta_expr+1
B=(alpha_expr-2)*beta_expr-(beta_expr+1)*c
assert s.expand(A+(5*c*c-10*c-4)/36)==0
assert s.expand(A*(alpha_expr**3+2*alpha_expr*beta_expr)
                +(alpha_expr**2+beta_expr)*B-P)==0
assert s.expand(beta_expr*(alpha_expr**2+beta_expr)*A
                +alpha_expr*beta_expr*B-Q)==0
assert s.expand(alpha_expr*(alpha_expr**2+2*beta_expr)
                -(5*c+4)*(25*c*c+4*c+16)/216)==0
print('B2 raw P=',s.factor(P))
print('B2 Q=',s.factor(Q))
print('B2 effective cubic=',p)
print('B2 Q modulo p=',qred)
print('B2 H=',H)
print('B2 exact identity remainder=',s.factor(identity))
print('B2 cubic discriminant=',s.discriminant(p,c),'factorization=',s.factorint(5038848))
print('B2 values p mod 7=',mod7,'(no zero, hence irreducible)')
print('B2 roots of delta=',s.solve(delta,c))
print('B2 approximate roots of p=',[str(x) for x in s.nroots(p,n=20)])
print('B2 c=(4+18*r+6*r^2)/25, r^3=2: exact substitution remainder=0')
print('B2 gcds excluding degeneracies: all 1')

# B.3: clean orange rational maps, checked for every n from 1 to 8.
for n in range(1,9):
    bn=-4*z**n/(z**n-1)**2
    assert s.cancel(bn-1+(z**n+1)**2/(z**n-1)**2)==0
    assert s.cancel(s.diff(bn,z)-4*n*z**(n-1)*(z**n+1)/(z**n-1)**3)==0
print('B3 oranges n=1..8: white divisor and derivative identities verified exactly')

# B.3: exact finite combinatorial models of all claimed exceptional genera.
for genus in range(1,9):
    n=4*genus
    rho=tuple((i+1)%n for i in range(n))
    alpha=tuple((i+2*genus)%n for i in range(n))
    phi=compose(inv(rho),alpha)
    assert ctype(rho)==(n,) and ctype(phi)==(n,)
    assert ctype(alpha)==(2,)*(2*genus)
    # Centralizer of a full n-cycle is precisely its n powers.
    powers=[tuple((i+k)%n for i in range(n)) for k in range(n)]
    kernel=[q for q in powers if all(fixes_cycles(q,t) for t in [rho,alpha,phi])]
    assert kernel==[tuple(range(n)),alpha]
    print('B3 genus',genus,'darts',n,'V,E,F=',1,2*genus,1,'kernel size=',len(kernel))

print('All assertions passed.')
print('Elapsed seconds:',round(perf_counter()-started,6))
