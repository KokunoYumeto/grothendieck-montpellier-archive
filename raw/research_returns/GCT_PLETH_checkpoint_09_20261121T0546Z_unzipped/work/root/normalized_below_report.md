# The complete normalized region below the ideal order

## G-035. Every normalized coefficient with c<k

Let \(x,b,k,c,d\) be nonnegative integers satisfying
\[
c<k,\qquad b+c\ge2k,\qquad2b+x+3c\ge5k.
\tag{NB.1}
\]
Set
\[
\begin{aligned}
n&=d+b+x+c-k,\\
\lambda&=(d+3b+2x+4c-5k,d+b+x+c,d+b+x,d+x,d).
\end{aligned}
\tag{NB.2}
\]
For every \(\mu\vdash5\), \(p_{\mu,(n)}^\lambda\) has a
fixed positive formula with at most152 selected bounded integer
polytopes, each with at most eleven variables. The complete disjoint
routing is in §5. It treats every point of (NB.1), including small
orders and every boundary. Its formulas require only fixed rational
polynomial data, residue selection and bounded-order binomial
evaluation; no input-sized representation computation occurs.

The new ingredients are two four-variable cones, three adjacent
three-variable strips and six low-order boundary pieces. Their actual
restriction maps, all phase formulas and all positivity certificates
are specified below. G033 and G034 supply the completed \(c=0,1\)
routes, while T058 supplies the four-variable upper cone.

## 1. Exact parameters and the full restricted character

Put
\[
C=c,\qquad R=k-c\ge1,\qquad b_0=b-c.
\]
Then (NB.1) is exactly
\[
b_0\ge2R,\qquad2b_0+x\ge5R.
\tag{NB.3}
\]
These equalities follow by the displayed integral substitution and
its inverse \((c,k,b)=(C,C+R,C+b_0)\). They do not change the
original module. With \(a=b+x\), \(F=\mathbb Q^3\), and
\(J_k=\bigcap_i(\ell_i\otimes F)^k\), its exact form is
\[
\begin{aligned}
M&=\operatorname{Hom}_{GL(F)}
 \bigl(S_{(a+c,b+c,c)}F,(J_k)_{2b+x+3c}\bigr),\\
(S_\lambda\mathbb Q^5)_{(n^5)}
&\simeq\operatorname{sgn}^{d+b+x+c}\otimes M.
\end{aligned}
\tag{NB.4}
\]
The maps are G027/T049's normal substitution, rational Young
projection and balanced inverse \(u^{-k}F(v(X))\), with its proved
polynomial extension. The oriented restriction complex has literal
quotient maps. Terms of size at least four vanish by degree
\(4(k-1)<2b+x+3c\).

Let \(P_g^\circ\) denote its ambient, singleton and pair trace.
The singleton is exactly T058/GU5 and T057's proved \(c<k\)
formula. The pair is T058/GU6–9, including the explicit exterior
minor maps, rational highest-space isomorphism and selected-slot
permutations. Their proofs require only \(c<k\) and
\(b+c\ge2k\), not the upper-cone inequality.

For a stable selected triple, let \(\eta\vdash3\) be its cycle
type and \(\epsilon=\pm1\) its complementary-line eigenvalue.
Define \(A_{\eta,\epsilon}\) and \(h_\eta\) by G034/OW4,
with zero coefficients at negative indices. Set
\(\tau=3R-3-b_0\). G034's complete rank-three telescope gives
the exact full trace
\[
\begin{aligned}
P_g={}&P_g^\circ+
\sum_{\substack{|A|=3\\gA=A}}
(-1)^{\#\operatorname{cyc}(g|A)}
\epsilon_A^{x+R-1}h_{\eta_A}(C)\\
&\hspace{16mm}\cdot
\left(A_{\eta_A,\epsilon_A}(\tau)
      -A_{\eta_A,\epsilon_A}(\tau-x-1)\right).
\end{aligned}
\tag{NB.5}
\]
Indeed its two deficits become
\(3k-3-b-2c=\tau\) and \(\tau-x-1\), and its phase
\(\epsilon^{x+c+k-1}=\epsilon^{x+R-1}\).
The factor \(h_\eta(C)\) is \(C+1\) for \(\eta=111\),
the even-degree indicator for \(\eta=21\), and the periodic
sequence \(1,-1,0\) for \(\eta=3\). These follow directly
from its printed rational generating function.

Every term in (NB.5) is therefore the trace of the specified
normal Young and complementary-line Pieri maps, with its actual
orientation. The only remaining steps are exact rational
polynomial evaluation and positive finite differences.

## 2. The two arbitrary-twist lower cones

All coordinates in the following table are nonnegative:
\[
\begin{array}{c|c|c|c|c}
&R&x&b_0&\tau\\\hline
A&T+6+K&T+X&2T+15+3K&T\\
B&X+2S+8+K&X&2X+5S+20+3K&X+S+1.
\end{array}
\tag{NB.6}
\]
In both rows \(c=C\), \(k=C+R\), \(b=C+b_0\).
The partition gaps are respectively \(X+K\) and \(K\).
Also \(b_0-2R\) is \(K+3\) on A and \(S+K+4\) on B.
Thus every point gives the actual module (NB.4).
The second tail term in (NB.5) is zero on A and has argument
\(S\) on B.

T058's input coordinates are \((X_o,B_o,K_o,C_o)\), with
\(R=K_o+4\) and \(b_0=3R-2+B_o\). For the two new cones
the exact substitutions are
\[
\begin{array}{c|cccc}
&X_o&B_o&K_o&C_o\\\hline
A&T+X&-T-1&T+K+2&C\\
B&X&-X-S-2&X+2S+K+4&C.
\end{array}
\tag{NB.7}
\]
The character calculation of §1 proves these substitutions for
\(P_g^\circ\) before the triple term is added. Phases are selected
using the physical \((a,b,k,c)\) and then transformed. The output
phase keys are explicitly the residues of the new cone coordinates.

The immutable source is `GENERIC_TWIST_UPPER_INPUT.json`.
The exact script `generic_twist_lower_cones.py` expands (NB.7)
and adds (NB.5). It saves all2291 phases per cone in
`GENERIC_TWIST_LOWER_A_CHECK.json` and its B counterpart.
The seven class degrees are \((6,3,2,1,0,0,0)\).
Separate-degree bounds are \((3,3,4,4)\) and \((3,2,4,4)\).
All monomial coefficients of the identity phase are nonnegative.

For each nonzero step60 order, subtract from the identity
difference the class-size-weighted coefficientwise maximum of
the absolute nonidentity difference coefficients over all phases.
The complete exact certificates give:

| Cone | Positive active orders | Least constant margin | Total-degree bound |
|---|---:|---:|---:|
| A | 151 | 131670 | 6 |
| B | 108 | 8700 | 6 |

Every coefficient of every margin is nonnegative and each constant
is positive. The order sets are the downward closures of all
monomial supports; all omitted differences vanish. Every complete
margin, rational coefficient and phase key is in the saved data.
No coefficient sign is inferred from an unproved interpolation.
The underlying quasipolynomial identity is (NB.5), with T058's
exact finite summation and G034's proper root-of-unity tail series.

At \(C=0\) these characters are exactly G033's two cones.
The zero-third-coordinate torus subspace, with its inclusion and
projection, identifies the rank-three Young extraction with the
rank-two extraction there. At \(C=1\) they are G034's two
cones. Thus those comparisons also retain their actual module maps.

## 3. Three boundary strips and six small-R pieces

The strips have a fixed \(D\in\{0,1,2\}\) and free
\(Y,T,H\ge0\). Define
\[
\begin{gathered}
C=H+2,\quad R=T+D+3,\quad b_0=2T+3D+6,\\
x=T+3-D+Y.
\end{gathered}
\tag{NB.8}
\]
Here \(b_0-2R=D\), \(\tau=T\), and the partition gap
is \(Y\). They are exact substitutions into cone A's character:
\[
(X,T,K,C)=(Y+3-D,T,D-3,H+2).
\tag{NB.9}
\]
Their triple formula remains valid by (NB.1), and the second
tail argument is negative. The singleton and pair bounds remain
those proved in §1. Thus the negative constant value of \(K\)
in (NB.9) is justified by the actual maps and their trace formula.

The remaining small-\(R\) upper pieces have \(R=1,2,3\)
and \(C=H+2\). Their free variables and physical parameters are:

| Name | Free coordinates | R | b0 | x | Partition gap |
|---|---|---:|---|---|---|
| R1a | (Y,H) | 1 | 2 | Y+1 | Y |
| R1b | (X,B,H) | 1 | B+3 | X | 2B+X+1 |
| R2a | (Y,H) | 2 | 4 | Y+2 | Y |
| R2b | (X,B,H) | 2 | B+5 | X | 2B+X |
| R3a | (Y,H) | 3 | 7 | Y+1 | Y |
| R3b | (X,B,H) | 3 | B+8 | X | 2B+X+1 |

In each case \(b_0\ge3R-2\), so \(\tau<0\) and every
triple trace is zero. Substitute the table into T058's coordinates
\[
(X_o,B_o,K_o,C_o)=(x,b_0-3R+2,R-4,H+2).
\tag{NB.10}
\]
The exact initial summation range must be checked at these negative
values of \(K_o\). The singleton triangle has order
\(r=k-l\ge R\ge1\). For complementary period \(L\),
its two residue indices \(s,t\in\{0,\ldots,L-1\}\) give
\[
M=\left\lfloor\frac{r-1-s-t}{L}\right\rfloor\ge-2.
\]
At \(M=-2,-1\), the triangle is empty and its finite-sum
formula \(\binom{M+2}{i+j+2}\) is zero, because its upper
argument is zero or one and its lower argument is at least two.
At \(M\ge0\), the proved T054 summation applies directly.
Every other complete-function argument is in its proved range:
\(b\ge k+1\) bounds the shifted second row, \(C\ge2\)
makes the ambient third row nonnegative, and the pair orders
\(k-l\), \(k-C+l\) are at least \(R\ge1\).
The outer residue sums have upper bounds at least minus one,
with the exact empty-binomial convention of T058. This proves
the polynomial extension on every small-\(R\) piece.

`generic_twist_boundaries.py` performs exactly (NB.9) and
(NB.10), keeping the physical phase selection explicit. Each
output is `GENERIC_TWIST_BOUNDARY_<name>.json`. The full finite
certificates give:

| Piece | Free dimension | Positive active orders | Least constant margin |
|---|---:|---:|---:|
| D0 | 3 | 56 | 805020 |
| D1 | 3 | 56 | 829590 |
| D2 | 3 | 56 | 852540 |
| R1a | 2 | 18 | 2362800 |
| R1b | 3 | 60 | 3016760 |
| R2a | 2 | 18 | 4215300 |
| R2b | 3 | 60 | 1557680 |
| R3a | 2 | 18 | 3371790 |
| R3b | 3 | 60 | 3473785 |

Every identity coefficient and every margin coefficient is
nonnegative; every listed constant margin is positive. The
downward closure of the full monomial support is the checked
order set. Each total degree is at most six. This is an exact
rational certificate on the whole nonnegative orthant.

## 4. Positive constants, bounded polytopes and support on the cones

For any new piece with free coordinate vector \(Z\) of length
\(r\), put \(Z=s+60q\), \(0\le s_i<60\). Let \(\nu\)
be \(\mu\) or \(\mu'\) according as \(d+b+x+c\) is even
or odd, and let \(f_\nu\) be the class inner product of its
exact trace. The fixed constants are
\[
D_{\nu,s,\delta}=
\sum_{0\le h\le\delta}(-1)^{|\delta|-|h|}
\binom\delta h f_\nu(s+60h).
\]
For nonzero active orders they are strictly positive: use
\(|\chi_\nu(g)|\le\chi_\nu(1)\) in the class inner product
and the complete coefficientwise margins in §§2–3.
For order zero they are nonnegative because the trace is that
of the actual module (NB.4). Their integrality follows from
the integer multiplicities and finite differences. This proves
all signs without requiring a full \(60^4\) base-cube replay.

Every coordinate used to define a fixed constant is at most419,
since the residue is at most59 and the total order is at most6.
The exact polynomial Newton identity gives
\[
\boxed{p_{\mu,(n)}^\lambda=
\sum_\delta D_{\nu,s,\delta}
\prod_{i=1}^r\binom{q_i}{\delta_i}.}
\tag{NB.11}
\]
For each positive constant, its literal bounded polytope is
\[
\begin{gathered}
60q_i=Z_i-s_i,\quad q_i\ge0,\quad0\le y<D_{\nu,s,\delta},\\
0\le u_{i1}<\cdots<u_{i,\delta_i}<q_i.
\end{gathered}
\tag{NB.12}
\]
Integer gaps of one replace the strict inequalities. The selector
and increasing subsets give the exact lattice-point bijection.
There are \(r+1+|\delta|\le11\) variables. The largest number
of tags is152 on cone A. Every coefficient and bound has bit
length polynomial in the input bit length, with all fixed constants
independent of the input. The implementations export the actual
integer matrices and lazy witnesses.

The complete support on the four-variable cones follows from an
additional explicit map. Increasing \(C\) by two adds
\((4,4,2,0,0)\) to \(\lambda\) and two to \(n\).
Multiply in the flag-polynomial domain by T058/GU14's invariant
sum of squares of the minors with columns \((1,3,5),(2,4)\).
Its nonzero Vandermonde value proves injectivity. The determinant
parity is unchanged. On A the only \(C=0\) zeros are G033's
five entries, at \((X,T,K)=(0,0,0),(0,1,0),(0,2,0)\);
the only \(C=1\) zeros are G034's two origin entries. At the
three affected \(C=2\) points, the effective vectors are
\[
\begin{array}{c|c}
(X,T,K)&(5,41,32,311,221,2111,11111)\\\hline
(0,0,0)&(1,9,9,16,9,8,1)\\
(0,1,0)&(6,23,27,32,26,20,5)\\
(0,2,0)&(9,41,48,62,46,37,7).
\end{array}
\]
At the \(C=3\) origin it is \((3,17,19,28,18,16,2)\).
All entries were separately checked by actual balanced characters.
Thus every \(C\ge2\) coefficient on A is positive.

On B the \(C=1\) slice is entirely positive. The four affected
\(C=2\) points above the six \(C=0\) zeros have vectors
\[
\begin{array}{c|c}
(X,S,K)&\text{effective vector}\\\hline
(0,0,1)&(10,43,51,65,51,41,9)\\
(0,1,0)&(3,19,22,33,21,18,2)\\
(0,3,0)&(6,34,39,56,38,32,5)\\
(0,5,0)&(10,53,61,85,60,50,9).
\end{array}
\]
They too were checked by actual balanced characters. The same
invariant multiplication proves positivity for every \(C\ge1\)
on B. These support arguments retain every original \(C=0,1\)
exception and use no extrapolation from sampled values. On the
other pieces the fixed formula (NB.11) gives the coefficient
directly; the previously proved G031 catalog independently
decides every outer-five zero.

## 5. Exhaustive routing on the normalized lower region

For \(c=0\) use G033, and for \(c=1\) use G034. Now take
\(C=c\ge2\), and compute \(R,b_0,\tau\) as in §1.

At \(\tau<0\) one has \(b_0\ge3R-2\). For \(R\ge4\)
this is exactly T058. For \(R=1\), (NB.3) gives \(b_0\ge2\):
\(b_0=2\) requires \(x\ge1\) and is R1a; \(b_0\ge3\)
is R1b. For \(R=2\), \(b_0=4\) requires \(x\ge2\)
and is R2a; \(b_0\ge5\) is R2b. For \(R=3\), this branch
has \(b_0\ge7\): \(b_0=7\) requires \(x\ge1\) and is
R3a; \(b_0\ge8\) is R3b. These statements give exactly the
inverse coordinates in the table in §3.

At \(\tau\ge0\), first take \(x<\tau\). The inverse
cone-B coordinates are
\[
(X,S,K,C)=(x,\tau-x-1,2b_0+x-5R,c).
\tag{NB.13}
\]
All are nonnegative by the integer inequality and (NB.3).
Substitution into (NB.6) recovers the original \(R,b_0,x\).

For \(x\ge\tau\), put \(D=b_0-2R\ge0\).
At \(D\ge3\), the inverse cone-A coordinates are
\[
(X,T,K,C)=(x-\tau,\tau,D-3,c).
\tag{NB.14}
\]
At \(D=0,1,2\), use the corresponding strip with
\[
(Y,T,H)=(2b_0+x-5R,\tau,c-2).
\tag{NB.15}
\]
The partition gap makes \(Y\ge0\); the other coordinates
are nonnegative by the branch definitions. Its equations recover
\(R=\tau+D+3\), \(b_0=2\tau+3D+6\), and
\(x=\tau+3-D+Y\). These cases exhaust the integer domain.

Every provider used for \(c=0,1\) has at most122 selected tags
and at most eleven variables: G021 gives122; T045/T050/T051
give at most55, with their at most18 coin tags and small-order
branches; G026/G030/G032 give at most17; T054/T055/T056 and
G033/G034 use at most47. The upper T058 provider has144.
The new lower and boundary counts in §§2–3 therefore give the
uniform bound152 asserted at the start.

`normalized_below_positive.py` implements these decisions,
calls `generic_twist_lower_positive.py` on A/B, and exports
every boundary constraint matrix. Its physical entry point is
\((x,b,k,c,d,\mu)\), with every inequality in (NB.1) checked.

## 6. Exact geometric transport and verification scopes

The Schur-operation class is that of the actual module (NB.4).
The normal Young projector, oriented quotient maps and the
complementary-line Pieri arrows give its exact coherent class;
(NB.5) computes this same class by finite alternant reindexing.
T058's exterior maps and rational highest-space isomorphism
specify the pair comparison. The affine parameter changes in
(NB.6)–(NB.10) merely give integral coordinates on these stated
modules, with their inverse substitutions printed. No object is
identified solely from a matching dimension.

The coordinate and sheaf arrows are EGA II2.4.1–2.4.2 and
2.5.2/2.5.4; the frame/comodule functor is SGA3
I4.5/4.7.2–4.7.3; its representation-to-sheaf class is SGA6
VI3.3. Schur and λ operations use SGA6 V4.2,4.4,4.8–4.9.
Cote133/028 is carried by A012's exact tensor-word, torus-weight
and Young maps. The additional support arrows are the literal
flag-polynomial multiplications of G024/T058, so they carry
nonzero balanced sections through the same associated-bundle
and representation-K0 maps.

Each four-variable lower cone passed224 full restriction traces,
112 actual balanced coefficients and112 continuation/parity
checks; the literal witness counts are291 and321. All eight
support seed vectors were separately checked. The nine boundary
pieces passed1323 full restriction traces,840 actual balanced
coefficients,714 continuation/parity cases and3859 literal
matrix witnesses. The receipts are
`GENERIC_TWIST_LOWER_RECEIPT.json` and
`GENERIC_TWIST_BOUNDARIES_RECEIPT.json`.
These are executed comparisons and supplement the exact proofs
and complete rational certificates above. No \(60^4\) residue
enumeration is claimed. Independent whole-proof reviews and
reconstructions have their separately dated check events.
