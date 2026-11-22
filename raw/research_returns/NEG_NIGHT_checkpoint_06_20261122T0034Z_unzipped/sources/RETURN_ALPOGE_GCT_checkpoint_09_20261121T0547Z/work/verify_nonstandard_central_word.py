"""Exact finite checks for P-F52; source: GCT VII Figure 1, printed p.30.

This verifies the transcribed projection and its product Gram form. It does
not use the inconsistent two-by-two matrices printed on p.20.
"""
import sympy as s

q = s.symbols("q", positive=True)
f = (q**4+1)*(q**4-q**2+1)*(q**2+1)/q**5
a = q**6-1
b = (q**2-1)**2*(q**4+q**2+1)
c = (q**2+1)**2*(q**2-1)
h = (q**2+1)*(q**8-q**6+q**4-q**2+1)/q**5
e = (q**2+1)/q
k = (q**4+1)/q**2
j = -(q**8-q**6-2*q**4-q**2+1)/q**4
rows = [
    {1:f},
    {2:q*(q**4+1),5:k},
    {3:h,6:a/q**4,9:e},
    {4:(q**8-q**6+q**4+1)/q**3,7:b/q**6,10:a/q**5,13:k},
    {2:k,5:(q**4+1)/q**5},
    {3:c/q**2,6:2*e,9:-c/q**2},
    {4:b/q**2,7:(2*q**8+q**6-2*q**2+1)/q**5,10:j,13:-a/q},
    {8:h,11:c/q**4,14:e},
    {3:e,6:-a/q**4,9:h},
    {4:a/q,7:j,10:(q**8-2*q**6+q**2+2)/q**3,13:b/q**2},
    {8:a/q**2,11:2*e,14:-a/q**2},
    {12:q*(q**4+1),15:k},
    {4:k,7:-a/q**5,10:b/q**6,13:(q**8+q**4-q**2+1)/q**5},
    {8:e,11:-c/q**4,14:h},
    {12:k,15:(q**4+1)/q**5},
    {16:f},
]
P = s.zeros(16)
for i, entries in enumerate(rows):
    for col, val in entries.items():
        P[i,col-1] = val

two = q+q**-1
three = q**2+1+q**-2
d = [s.Integer(1),q**-1*three,three*two**2,q**3*three**2*two**2]
gram = s.diag(*(d[i]*d[j] for i in range(4) for j in range(4)))

def zero_matrix(M):
    return all(s.cancel(v) == 0 for v in M)

assert zero_matrix(gram*P-P.T*gram)
assert zero_matrix(P*P-f*P)
Q = f*s.eye(16)-P
assert zero_matrix(gram*Q-Q.T*gram)
assert zero_matrix(Q*Q-f*Q)

S = (q**10+q**-10+3*(q**8+q**-8)+(q**6+q**-6)
     +5*(q**4+q**-4)-2*(q**2+q**-2)+16)
v = q**2+q**-2-2
R = 3*v**4+23*v**3+57*v**2+48*v+16
assert s.cancel(S-f**2-R) == 0

# Basis-normalization identity for the descended two-dimensional space.
x, pp = s.symbols("x pp")
change = s.Matrix([[1,x],[1,-x]])
diag = s.diag((pp+x)/(2*q**20),(pp-x)/(2*q**20))
M = change.inv()*diag*change
assert zero_matrix(M-s.Matrix([[pp,x**2],[1,pp]])/(2*q**20))

print("PASS: 16x16 source projection, product Gram self-adjointness, complement,")
print("positive scalar identity, and exact descended 2x2 normalization.")

# All coefficients, not only the leading terms, of VII Figures 2 and 7.
# The lists below transcribe the actual source polynomials in ascending
# even powers; the factorizations are checked independently afterward.
def evenpoly(vals, start=0):
    return sum(s.Integer(val)*q**(start+2*i) for i,val in enumerate(vals))

R = -3*q**28-4*q**24+2*q**22-10*q**20+2*q**18-4*q**16-3*q**12
D = (q**8+1)**2*q**24*(5*q**16+8*q**12-4*q**10+18*q**8
                        -4*q**6+8*q**4+5)
g1 = (-R-x)/(2*q**20)
g2 = (-R+x)/(2*q**20)
g3 = q**4+2+q**-4
g4 = q**6+2+q**-6
g5 = q**10+2+q**-10
E1 = g3+g4+g5
E2 = g3*g4+g3*g5+g4*g5
E3 = g3*g4*g5
L = -R/q**20
NN = (q**4-q**2+1)**2*(q**12+q**10+2*q**8+2*q**4+q**2+1)**2/q**16
assert s.cancel((R**2-D)/(4*q**40)-NN) == 0
assert s.cancel(L+E1-S) == 0

source_a = [
    -(q**12+q**10+2*q**8+2*q**4+q**2+1)**2
      *(q**8-q**6+q**4-q**2+1)**2*(q**2+1)**4
      *(q**4-q**2+1)**4*(q**4+1)**2/q**36,
    evenpoly([1,1,7,5,18,21,20,73,-14,187,-107,328,-197,402,
              -197,328,-107,187,-14,73,20,21,18,5,7,1,1])
      *(q**2+1)**2*(q**4-q**2+1)**2/q**32,
    -evenpoly([1,3,8,4,33,12,76,27,115,113,80,253,-9,360,
               -9,253,80,113,115,27,76,12,33,4,8,3,1])/q**26,
    evenpoly([3,2,8,5,17,30,11,61,-15,108,-15,61,11,30,17,5,8,2,3])/q**18,
    -S,
    s.Integer(1),
]
factored_a = [-NN*E3,NN*E2+L*E3,-NN*E1-L*E2-E3,
              NN+L*E1+E2,-L-E1,s.Integer(1)]
for j,(left,right) in enumerate(zip(source_a,factored_a)):
    assert s.cancel(left-right) == 0, ("relation coefficient",j)

Pscalar = q**20*(22-2*(q**2+q**-2)+6*(q**4+q**-4)
                         +2*(q**6+q**-6)+3*(q**8+q**-8)+2*(q**10+q**-10))
b1constant = evenpoly([3,-3,9,2,-1,47,-84,210,-295,462,-516,604,
                       -516,462,-295,210,-84,47,-1,2,9,-3,3],12)
b1x = evenpoly([1,-1,1,4,-9,19,-24,30,-24,19,-9,4,1,-1,1])
b2constant = evenpoly([3,2,9,1,24,18,22,45,-2,92,-2,45,22,18,24,1,9,2,3],12)
b2x = 1+q**4+q**6+6*q**10+q**14+q**16+q**20
source_b = [
    (q**4-q**2+1)**2*(q**8-q**6+q**4-q**2+1)**2*(q**4+1)**2
       *(q**2+1)**4*(-R+x)/(2*q**40),
    -(q**2+1)**2*(b1constant+x*b1x)/(2*q**36),
    (b2constant+x*b2x)/(2*q**30),
    -(Pscalar+x)/(2*q**20),
    s.Integer(1),
]
factored_b = [g2*E3,-E3-g2*E2,E2+g2*E1,-E1-g2,s.Integer(1)]
for j,(left,right) in enumerate(zip(source_b,factored_b)):
    assert s.cancel(left-right) == 0, ("cell coefficient",j)

def quadratic_zero(expr):
    num,den = s.fraction(s.cancel(expr))
    rem = s.rem(num,x*x-D,x)
    return s.cancel(rem) == 0

# (t-g1)*p1(t)=r(t), compared in all six coefficients modulo x²=D.
for j in range(6):
    coeff = (source_b[j-1] if j else 0) - (g1*source_b[j] if j<5 else 0)
    assert quadratic_zero(coeff-source_a[j]), ("full eigenidentity",j)
print("PASS: all six relation coefficients and all five cell coefficients;")
print("complete (t-g1)*p1(t)=r(t) identity modulo x^2=D, independently of blocks.")

# Alternative normalization: actual positive action and both positive
# Lefschetz coefficient lists do not characterize the source factor F.
H = (q+1+q**-1)**4
T = Pscalar/q**20
N = s.cancel((Pscalar**2-D)/(4*q**40))
alphaH = [390,336,242,160,139,132,128,112,103,88,70,44,23,8,2]
betaH = [169556,164696,152852,139200,127656,118312,109695,
         100480,90558,79776,68121,55832,44025,33832,25905,20000,
         15558,12016,9093,6632,4587,2936,1699,864,377,136,39,8,1]
def symmetric_polynomial(vals):
    return vals[0]+sum(v*(q**j+q**-j) for j,v in enumerate(vals[1:],1))
assert s.cancel(H*T-symmetric_polynomial(alphaH)) == 0
assert s.cancel(H**2*N-symmetric_polynomial(betaH)) == 0
for vals in [alphaH,betaH]:
    assert min(vals)>0
    assert all(a>=b for a,b in zip(vals,vals[1:]))
assert alphaH[0]+2*sum(alphaH[1:]) == 3564
assert betaH[0]+2*sum(betaH[1:]) == 2939328
print("PASS: alternative H normalization, full positive nonincreasing trace/norm")
print("coefficient certificates and both values at one.")

# Actual source interpolation denominator and the prescribed normalization.
r = s.symbols("r", positive=True)
eigen = [r**9,-r**-3,r**-11,-r**-15]  # q=r² clears half powers
fp_product = s.prod(eigen[i]-eigen[j] for i in [0,2] for j in range(4) if j!=i)
fp_formula = -q**-33*(q**10-1)**2*(q**6+1)*(q**12+1)*(q**4+1)*(q**2+1)
assert s.cancel(fp_product-fp_formula.subs(q,r**2)) == 0
Ffactor = q**-16*sum(q**j for j in range(10))**2*(1+q**2)*(1+q**12)
assert s.cancel(q**11*(-q*fp_formula/((q-1)**2*f))-Ffactor) == 0
sourceF = [16,16,16,16,17,18,18,18,16,14,12,10,8,6,4,2,1]
assert s.cancel(Ffactor-symmetric_polynomial(sourceF)) == 0
assert Ffactor.subs(q,1) == 400
print("PASS: actual four-eigenvalue interpolation product, all normalization")
print("cancellations, and the full33-term source F coefficient list.")

# Positive R0-order in the actual restricted central endomorphism algebra.
tpos = s.expand(Ffactor*T)
npos = s.expand(Ffactor**2*N)
epos = sum(q**j+q**-j for j in [4,8,12,24])
apos = s.expand((tpos-epos)/2)
dpos = s.expand((tpos+epos)/2)
bpos = s.expand(apos*dpos-npos)
alpha_pos = [354,354,347,340,336,333,321,309,282,256,232,208,182,
             157,131,105,85,65,53,41,31,21,15,9,5,2,1]
beta_pos = [173758,173280,171874,169576,166431,162488,157785,
            152364,146308,139703,132653,125265,117614,109779,101839,
            93877,85986,78264,70768,63560,56676,50156,44035,38352,
            33124,28369,24074,20227,16813,13819,11223,9005,7131,5569,
            4281,3231,2390,1731,1225,845,567,367,228,133,72,35,15,5,1]
delta_pos = list(alpha_pos)
for j in [4,8,12,24]:
    delta_pos[j] += 1
assert s.expand(apos-symmetric_polynomial(alpha_pos)) == 0
assert s.expand(dpos-symmetric_polynomial(delta_pos)) == 0
assert s.expand(bpos-symmetric_polynomial(beta_pos)) == 0
for vals in [alpha_pos,delta_pos,beta_pos]:
    assert all(isinstance(v,int) and v>0 for v in vals)
    assert all(a>=b for a,b in zip(vals,vals[1:]))
assert s.cancel(tpos**2-4*npos-epos**2-4*bpos) == 0
assert epos.subs(q,1) == 8
assert bpos.subs(q,1) == 5759984
assert apos.subs(q,1) == 8796 and dpos.subs(q,1) == 8804

Mscaled = Ffactor*s.Matrix([[Pscalar,D],[1,Pscalar]])/(2*q**20)
change_positive = s.Matrix([[1,epos/2],[0,Ffactor/(2*q**20)]])
Wpositive = s.Matrix([[apos,bpos],[1,dpos]])
assert zero_matrix(Mscaled*change_positive-change_positive*Wpositive)
Upositive = Wpositive-apos*s.eye(2)
assert zero_matrix(Upositive**2-epos*Upositive-bpos*s.eye(2))
assert s.cancel(Wpositive.det()-npos) == 0
assert s.cancel(s.trace(Wpositive)-tpos) == 0
print("PASS: all positive-order coefficient vectors, integer positivity and")
print("symmetric unimodality; exact source similarity, quadratic multiplication,")
print("trace/norm and q=1 simple-basis obstruction values.")

# The actual word form and its internal reciprocal bar.
for coeff in [f,L,E1,E2,E3,NN,*source_a,Ffactor,apos]:
    assert s.cancel(coeff.subs(q,1/q)-coeff) == 0
assert s.cancel(D.subs(q,1/q)-q**-80*D) == 0
assert s.cancel(R.subs(q,1/q)-q**-40*R) == 0
def internal_bar(expr):
    return expr.subs({q:1/q,x:q**-40*x}, simultaneous=True)
for coeff in [g1,g2,*source_b]:
    assert s.cancel(internal_bar(coeff)-coeff) == 0

def reduce_quadratic(expr):
    num,den=s.fraction(s.cancel(expr))
    return s.cancel(s.rem(num,x*x-D,x)/den)
def integer_laurent(expr):
    terms=s.expand(expr).as_ordered_terms()
    for term in terms:
        coeff,expo=term.as_coeff_exponent(q)
        if not (coeff.is_Integer and expo.is_Integer):
            return False
    return True

cell_conjugate=[coeff.subs(x,-x) for coeff in source_b]
v0_coeff=[s.cancel(c+cc) for c,cc in zip(source_b,cell_conjugate)]
v1_coeff=[reduce_quadratic(x*(c-cc)) for c,cc in zip(source_b,cell_conjugate)]
w_coeff=[s.cancel(epos*c0/2+Ffactor*c1/(2*q**20))
         for c0,c1 in zip(v0_coeff,v1_coeff)]
for coeff in v0_coeff+w_coeff:
    assert integer_laurent(coeff)
    assert s.cancel(internal_bar(coeff)-coeff) == 0
for coeff in v1_coeff:
    assert s.cancel(internal_bar(coeff)-q**-40*coeff) == 0
assert s.cancel(fp_formula/f+q**-12*(q-1)**2*Ffactor) == 0
assert s.cancel(Ffactor**2*D/(4*q**40)-epos**2/4-bpos) == 0
print("PASS: reciprocal source relations, splitting-field bar, every source")
print("cell coefficient, integral/bar-fixed v0 and w, rescaling factor, and")
print("exact identity forcing the negative displayed-basis coefficient.")

# Complete actual rank-four module for both rescaled Q generators.
hpos = s.expand((Ffactor*L-epos)/2)
hvector = [164,164,160,156,152,149,143,137,125,114,104,94,83,
           73,62,51,41,31,25,19,14,9,6,3,1]
assert s.expand(hpos-symmetric_polynomial(hvector)) == 0
assert s.expand(hpos-(Ffactor*S-dpos)) == 0
assert all(isinstance(v,int) and v>0 for v in hvector)
assert all(a>=b for a,b in zip(hvector,hvector[1:]))
assert hpos.subs(q,1) == 3996
assert s.cancel(2*hpos+epos-Ffactor*L) == 0
assert s.cancel(hpos*hpos+epos*hpos-bpos-Ffactor**2*NN) == 0

# First verify the block calculation with formal parameters; then the
# exact source identity above supplies their Laurent values.
ff,FF,hh,ee,bb = s.symbols('ff FF hh ee bb')
smallU=s.Matrix([[0,bb],[1,ee]])
smallI=s.eye(2)
blockA=s.BlockMatrix([[FF*ff*smallI,hh*smallI+smallU],
                     [s.zeros(2),s.zeros(2)]]).as_explicit()
blockB=s.BlockMatrix([[s.zeros(2),s.zeros(2)],
                     [FF*smallI,FF*ff*smallI]]).as_explicit()
assert zero_matrix(blockA**2-FF*ff*blockA)
assert zero_matrix(blockB**2-FF*ff*blockB)
actualG=ff**2*s.eye(4)-(blockA-blockB)**2/FF**2
expectedG=s.diag((hh*smallI+smallU)/FF,(hh*smallI+smallU)/FF)
assert zero_matrix(actualG-expectedG)
assert zero_matrix(smallU**2-ee*smallU-bb*smallI)
assert not zero_matrix(blockA*blockB-blockB*blockA)
print("PASS: full h coefficient certificate and source normalization;")
print("both rank4 rescaled-generator matrices, quadratic identities,")
print("central G action and generic noncommutation, without source p20 matrices.")

# Numerical graded-adjoint compatibility with an actual positive Gram.
trace_form=s.Matrix([[2,ee],[ee,ee**2+2*bb]])
mixed_form=trace_form*(hh*smallI+smallU)
four_gram=s.BlockMatrix([[FF*ff*trace_form,mixed_form],
                        [mixed_form,ff*mixed_form]]).as_explicit()
assert zero_matrix(trace_form*smallU-smallU.T*trace_form)
assert zero_matrix(four_gram-four_gram.T)
assert zero_matrix(four_gram*blockA-blockA.T*four_gram)
assert zero_matrix(four_gram*blockB-blockB.T*four_gram)
assert not zero_matrix(blockA-blockA.T)
assert not zero_matrix(blockB-blockB.T)
ut=q**2+q**-2-2
assert s.cancel(L-(3*ut**4+24*ut**3+64*ut**2+62*ut+20)) == 0
assert s.cancel(2*f**2-L-(2*ut**5+17*ut**4+50*ut**3
                         +64*ut**2+42*ut+12)) == 0
complement_product=(q**2-1)**4*(q**4+q**2+1)*(q**4-q**2+1)**2/q**20
complement_product*=sum(q**(2*j) for j in range(5))
complement_product*=sum(q**(2*j) for j in range(7))
assert s.cancel(f**4-L*f**2+NN-complement_product) == 0
assert L.subs(q,1) == 20 and NN.subs(q,1) == 64
assert f.subs(q,1)**2 == 16
gram_at_one=four_gram.subs({FF:400,ff:4,hh:3996,ee:8,bb:5759984})
assert gram_at_one.rank() == 3
print("PASS: both exact Gram adjoint identities, ordinary-adjoint mismatch,")
print("source root/complement positivity certificates, and rank3 at q=1.")

# Exact primitive-twelfth-root anchor for the semisimple-adjoint no-go.
# All operations are in Q[q]/Phi_12, not numerical approximations.
phi12=q**4-q**2+1
def at_primitive_twelve(expr):
    num,den=s.fraction(s.cancel(expr))
    return s.rem(s.rem(num,phi12,q)*s.invert(den,phi12,q),phi12,q)
assert at_primitive_twelve(f) == 0
assert at_primitive_twelve(L) == 1
assert at_primitive_twelve(NN) == 0
f12=at_primitive_twelve(Ffactor)
assert f12 != 0
assert s.gcd(f12,phi12) == 1
assert s.rem(f12**2+12*f12-12,phi12,q) == 0
print("PASS: exact primitive12 anchor f=0,L=1,N0=0,F nonzero;")
print("F satisfies X²+12X−12 there, checked in the cyclotomic quotient.")
