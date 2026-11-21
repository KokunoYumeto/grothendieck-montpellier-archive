# A complete positive formula on the central five-row staircase

## G-023. Seven active polytopes and exact support

For all \(r,d\ge0\), put
\[
n=d+2r,\qquad
\lambda=(d+4r,d+3r,d+2r,d+r,d).
\tag{SF.1}
\]
Every outer label \(\mu\vdash5\) has the positive formula (SF.6),
with at most seven active lattice polytopes of at most eight variables.
At \(r\ge2\) every one of the seven coefficients is positive. At
\(r=1\), the coefficients in the label order
\((5),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1^5)\) are
\((0,1,1,1,1,1,0)\), for every \(d\). At \(r=0\), the unique
nonzero coefficient is one, at \(\mu=(5)\) for even \(d\), and at
\(\mu=(1^5)\) for odd \(d\).

For \(r>0\), these shapes lie strictly inside the remaining region:
\(\lambda_2+\lambda_3=2n+r\) and
\(\lambda_3+\lambda_4=2n-r\). Thus the result evaluates an entire
central family through the actual cycle-trace morphism of G-022.

## 1. Exact trace polytopes and their periods

Take the balanced module \(B_r\) of G-022 at \(m=5\). Its trace
on each conjugacy class is exactly (ST.5)–(ST.6), including the
vanishing condition and the explicit residue-permutation sign. For a
class with cycle lengths \(\ell_1,\ldots,\ell_c\), the count in
(ST.6) is the integer-point count in \(rP_g\), with one variable
per parallel edge and bounds between zero and one in \(P_g\).
Its affine equations are exactly the exponent conditions in (ST.6).
The point with every variable one-half satisfies them, so the dimension
is \(\sum_{i<j}\gcd(\ell_i,\ell_j)-c+1\), with zero for one cycle.

The denominators of the vertices divide
\(L_g=\operatorname{lcm}(\ell_1,\ldots,\ell_c)\). Here is a proof
of the precise denominator bound. At a vertex, remove the edges whose
variables are fixed to zero or one. The remaining edges form a forest:
a cycle would give a nonzero weighted circulation, and both sufficiently
small positive and negative multiples preserve all bounds, contradicting
extremality. Multiply the equation at vertex \(i\) by \(\ell_i\).
Every edge then has ordinary incidence coefficient
\(\operatorname{lcm}(\ell_i,\ell_j)\). The right-hand side is an
integer, because \(\ell_i(5-\ell_i)\) is even; the fixed bound
edges contribute integers as well. Cutting one free forest edge and
summing the equations on a component shows that its value is an integer
divided by that edge's least common multiple. This proves the claimed
common denominator. At the identity all vertices are integral and the
dimension is six.

The cited lattice-count theorem is Beck–Robins, *Computing the Continuous
Discretely*, second edition, **Theorem3.8, p.68**, and **Theorem3.23,
p.80**, in the [author's corrected text of18February2023](https://matthbeck.github.io/papers/ccdnew.pdf).
These give a degree-six polynomial at the identity and, on each other
class, a quasipolynomial of degree at most three, two, one, zero, zero,
zero, respectively, with period dividing \(L_g\). The sign and
vanishing conditions in G-022 have the same periods. Hence finitely
many explicitly counted values determine each trace from \(r=0\).

## 2. The complete seven trace formulas

Write \(I(r)=\operatorname{tr}(1\mid B_r)\). The edge-count recursion
in `staircase_five_trace.py` enumerates the free incident edges of the
first vertex, updates the remaining exact balance demands, and repeats.
Every integer assignment appears once, because its first-vertex edge
values determine the next demands. The final one-vertex demand must be
zero. Parallel-edge values are combined using the coefficients of
\((1+z+\cdots+z^r)^g\), which count their ordered assignments exactly.
This proves the finite enumeration algorithm used below.

The initial identity counts, at \(r=0,\ldots,6\), are
\[
(1,24,219,1136,4175,12216,30429).
\]
Their successive first forward differences give
\[
\boxed{I(r)=1+23\binom r1+172\binom r2+550\binom r3
 +850\binom r4+630\binom r5+180\binom r6.}
\tag{SF.2}
\]
The degree-six theorem just proved makes this equality valid for every
\(r\ge0\). The complete other traces are

| cycle type | exact trace on \(B_r\) |
|---|---|
| \(2\,1^3\) | zero for odd \(r\); at \(r=2h\), \((h+1)^3+h^3\) |
| \(2^2\,1\) | zero for odd \(r\); at \(r=2h\), \(3h^2+3h+1\) |
| \(3\,1^2\) | at \(r=3h,3h+1,3h+2\), respectively \(h+1,-h,0\) |
| \(3\,2\) | periodic list \((1,0,0,0,-1,0)\) modulo six |
| \(4\,1\) | periodic list \((1,0,-1,0)\) modulo four |
| \(5\) | periodic list \((1,-1,-1,1,0)\) modulo five |

For a complete finite verification, the transposition's four required
even values are \(1,9,35,91\); the double transposition's three are
\(1,7,19\). The three-cycle values on residues zero and one are
\((1,2)\) and \((0,-1)\), respectively, at their first two terms;
the remaining residue vanishes by (ST.5). The last three rows are the
initial values of their fixed periods, computed by the same bounded
edge equations. These are all the samples required by the respective
degree and period bounds, so this is a proof by exact finite
interpolation. The certificate additionally checks the identity through
\(r=9\) and every other row through \(r=15\).

## 3. Every fixed positive constant

Use the class sizes \(1,10,15,20,20,30,24\) and the complete
irreducible character table in G-019. Let \(T_g(r)\) be the seven
explicit functions just proved, and set
\[
b_\nu(r)=\frac1{120}\sum_g|g^{S_5}|\chi_\nu(g)T_g(r).
\tag{SF.3}
\]
This is the actual multiplicity \([\nu:B_r]\), by the projector
of T-003. For \(0\le s<60\) and \(0\le j\le6\), define the
fixed integers
\[
C_{\nu,s,j}=\frac1{120}\sum_g|g^{S_5}|\chi_\nu(g)
\sum_{i=0}^j(-1)^{j-i}\binom ji T_g(s+60i).
\tag{SF.4}
\]
Only arguments at most419 occur. The delivered exact certificate
computes all2,940 constants from these elementary functions, checks
divisibility by120, and verifies
\[
C_{\nu,s,j}\ge0,\qquad C_{\nu,s,j}>0\quad(j\ge1).
\tag{SF.5}
\]
The minimum over every positive-order constant is107,377,819. All
entries, minima by order, and exact zero constants are in
`STAIRCASE_FIVE_CERTIFICATE.json`; the complete reproducing computation
is `staircase_five_certificate.py`. No representation computation at
an input-dependent size enters (SF.4).

For \(r=s+60q\), the proven residue degree bound and Newton's
identity give the positive formula
\[
\boxed{p_{\mu,(n)}^\lambda
=\sum_{j=0}^6 C_{\nu,s,j}\binom qj,
\quad
\nu=\mu\ (d\text{ even}),\quad\nu=\mu'\ (d\text{ odd}).}
\tag{SF.6}
\]
The determinant map establishing this sign is the last paragraph of
G-022 §4. Every input parameter and every sign therefore has an actual
representation comparison.

For each residue and order, the polytope has integer variables
\(q,y,z_1,\ldots,z_j\) and constraints
\[
60q=r-s,\quad q\ge0,\quad 0\le y<C_{\nu,s,j},\quad
0\le z_1<\cdots<z_j<q.
\tag{SF.7}
\]
An empty chain is omitted. Every strict inequality becomes an integer
difference at most minus one. Choosing \(y\) and the increasing
\(j\)-subset is an explicit bijection with its lattice points,
whose count is the summand of (SF.6). There are seven active tags,
420 tags before selecting the residue, and at most eight variables.
Evaluation takes a fixed number of arithmetic operations of polynomial
bit cost in \(\log(r+d+2)\).

The exact zeros in the initial residue interval are: \(r=1\) for
\(\nu=(5)\); \(r=0\) for each of the five intermediate labels;
and \(r=0,1\) for \(\nu=(1^5)\). All other initial values are
positive. For \(r\ge60\), the strictly positive first-difference
term in (SF.6) is already nonzero. This proves the entire support and
all endpoint assertions in the statement.

## 4. Geometric transport

The finite normalizer projector is transported from the compact oscillator
representation by T-001–T-003. The determinant character, cycle eigenvalue
map and lattice coefficient extraction in G-022 are explicit maps on
that representation. Formula (SF.6) computes its Schur multiplicity
and hence the composition operation of cote133/024–029 in the exact
representation group of SGA6 VI3.3. Its associated Schur sheaf and
frame-torsor maps are SGA3 I4.5,4.7.2–4.7.3. The underlying torus
weight decomposition and coefficient extraction commute with the
specified base changes after the characteristic-zero projectors are
formed. The count gives an exact rank of this actual projector.
