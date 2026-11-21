# Stable tails with second part three in every outer degree

## G-039. Cubic polarization and an explicit positive formula

Let \(m\ge3\), \(a\ge3\), \(t\ge0\), \(n\ge a+t\), and
\(\mu\vdash m\). Put
\[
\begin{gathered}
\lambda=(mn-a-3-(m-1)t,a+t,t+3,t^{m-3}),\quad D=a+3,\\
\nu=\mu\ (t\text{ even}),\qquad\nu=\mu'\ (t\text{ odd}),
\qquad N=\binom m2.
\end{gathered}
\tag{SR3.1}
\]
The original Schur plethysm coefficient has an explicit positive
formula using at most \(N+7\) bounded polytopes, each with at
most \(3m-1\) variables. Their matrices, the complete support
test and an exact coefficient evaluator are computable in bit
complexity polynomial in \(m\) and the binary parameters.
As in G037–G038, \(t\ge1\) gives \(m\) explicitly listed
positive output parts. At \(t=0\), the bound is in \(m\),
without a claim polynomial in the compressed \(\log m\) input.

For \(m\ge4\), the formula below has three types of positive
terms: an explicitly computed free numerator, ordinary weighted
Koszul cycles, and weighted cycles for the regular sequence
\(e_2^2,e_3,\ldots,e_m\). Its proof computes the actual
cubic polarization cokernel, including the action of \(I\).
The rank-two case \(m=3\) is given by its exact determinant
pairing in §7.

Write \(W=\mathfrak h_m\), \(P=\operatorname{Sym}W\), and
\(I=\mathbb Q[e_2,\ldots,e_m]\), \(\deg e_i=i\).
Use the actual coinvariant multiplicity polynomial \(f_T(q)\)
from G038/SR2.2. Define
\[
A_\nu=q^3f_{[\nu]\otimes\operatorname{Sym}^3W},
\qquad B_\nu=q^2f_{[\nu]\otimes\operatorname{Sym}^2W}.
\tag{SR3.2}
\]
There is a specified equivariant injection
\(\operatorname{Sym}^2W\to S_{(2,2)}W\), proved in §2.
Let \(\mathcal R\) be its Ricci-kernel complement and put
\[
c_2=[\operatorname{Sym}^2W:[\nu]],\quad
c_{21}=[S_{(2,1)}W:[\nu]],\quad c_R=[\mathcal R:[\nu]].
\tag{SR3.3}
\]
These are nonnegative integers. Set
\[
\begin{aligned}
C_0(q)&=c_2q^2+c_{21}q^3+c_Rq^4,\\
C_1(q)&=c_2q^2\left(q^4+\sum_{i=3}^m q^i\right)
             +(c_{21}q^3+c_Rq^4)\sum_{i=2}^m q^i,\\
F_\nu(q)&=A_\nu(q)-B_\nu(q)+C_0(q)-C_1(q)
              =\sum_{j=0}^{N+3}f_{\nu,j}q^j.
\end{aligned}
\tag{SR3.4}
\]
Every \(f_{\nu,j}\) is nonnegative. For an ordered positive
weight list \(\mathbf w=(w_1,\ldots,w_k)\), define the
explicit positive series
\[
Z_{\mathbf w}(q)=\sum_{1\le i<j\le k}
                  \frac{q^{w_i+w_j}}{\prod_{l=i}^k(1-q^{w_l})}.
\tag{SR3.5}
\]
Let \(\mathbf u=(2,3,\ldots,m)\) and
\(\mathbf v=(4,3,4,5,\ldots,m)\). The two entries4 in
\(\mathbf v\) refer respectively to \(e_2^2\) and \(e_4\),
so they label distinct generators. The exact formula is
\[
\boxed{\begin{aligned}
p_{\mu,(n)}^\lambda=[q^D]\Bigg(&
 \frac{F_\nu(q)}{\prod_{i=2}^m(1-q^i)}
 +(c_{21}q^3+c_Rq^4)Z_{\mathbf u}(q)\\
 &+c_2q^2(1+q^2)Z_{\mathbf v}(q)\Bigg).
\end{aligned}}
\tag{SR3.6}
\]
Section6 gives the literal bounded polytopes and all finite
polynomial calculations; no unknown multiplicity remains in
the formula.

## 1. Actual cubic polarization and every cokernel degree

The stable balanced flag map G015 and T032/C4–8 gives
\[
(S_\lambda\mathbb Q^m)_{(n^m)}
 \simeq\operatorname{sgn}^t\otimes S_{(a,3)}W.
\tag{SR3.7}
\]
Its hypotheses hold because \(\lambda_2=a+t\le n\), and
the first two gaps are respectively at least \(a-3\) and
equal to \(a-3\). This is the same actual determinant and
stable-first-row comparison used in G038/SR2.5.

Take the two graded free \(P\)-modules
\[
\mathcal A=P\otimes\operatorname{Sym}^3W,
\qquad\mathcal B=P\otimes\operatorname{Sym}^2W,
\]
with total degrees three and two for their tensor factors.
The \(P\)-linear, \(GL(W)\)-equivariant transfer is
\[
\phi(f\otimes uvw)
=fu\otimes vw+fv\otimes uw+fw\otimes uv.
\tag{SR3.8}
\]
For a completely specified highest-vector check, use variables
\(x,y\) in the first factor and \(X,Y\) in the second.
At first-factor degree \(b\ge0\), the Pieri highest vectors are
\[
H_i=x^{b-i}X^{3-i}(xY-yX)^i,
\qquad0\le i\le\min(b,3).
\]
Their weights are \((b+3-i,i)\). The transfer is
\(x\partial_X+y\partial_Y\), so it sends them to
\[
(3-i)x^{b-i+1}X^{2-i}(xY-yX)^i
\quad(0\le i\le2),
\]
and kills \(H_3\). These are the rational Young/Pieri
inclusions of Macdonald I§5(5.16), p73; the displayed vectors
are annihilated by the simultaneous raising operator.
Thus the map is nonzero on every target summand and its
kernel in total degree \(D=b+3\ge6\) is exactly
\[
K_D=S_{(D-3,3)}W.
\tag{SR3.9}
\]

The same finite summands give the whole cokernel:
\[
\begin{array}{c|c}
\text{total degree}&\operatorname{coker}\phi\\\hline
2&\operatorname{Sym}^2W\\
3&S_{(2,1)}W\\
4&S_{(2,2)}W.
\end{array}
\tag{SR3.10}
\]
At degree five the summands \((5),(4,1),(3,2)\) occur on
both sides and have nonzero scalars3,2,1. All larger degrees
are surjective by the same argument, and smaller omitted
degrees have zero target. Hence (SR3.10) exhausts the
cokernel, with no infinite-degree remainder.

## 2. The exact quadratic invariant action and Ricci splitting

For this section \(m\ge4\), so \(d=\dim W=m-1\ge3\).
Let \(g\) be the rational invariant dot form on the sum-zero
space. Use its inverse to identify tensors and quadratic
forms. Since \(\sum z_i=0\), the elementary invariant is
\(e_2=-\frac12\sum z_i^2\). Every invariant of degree
at least three kills the cokernel in (SR3.10), by its stated
degree support. The only remaining action is multiplication
by \(e_2\) from degree two to degree four.

Here is the actual quotient map identifying that action.
For symmetric tensors \(A,B\), define
\[
\begin{aligned}
\mathcal K(A,B)_{ijkl}={}&A_{ik}B_{jl}+A_{jl}B_{ik}\\
&-A_{il}B_{jk}-A_{jk}B_{il}.
\end{aligned}
\tag{SR3.11}
\]
Its image has the alternating pairs, pair interchange and
first Bianchi identity of the Young summand \(S_{(2,2)}W\).
It is symmetric in \(A,B\), killing the \((3,1)\) summand
of \(\operatorname{Sym}^2W\otimes\operatorname{Sym}^2W\).
Its full four-slot symmetrization is zero, killing \((4)\).
It is nonzero, for example on \(x^2\otimes y^2\).
Pieri has exactly these three summands, each once. Therefore
(SR3.11) induces an isomorphism from the actual degree-four
cokernel to this tensor realization of \(S_{(2,2)}W\).
It is the specified Young quotient, not a comparison of
dimensions alone. Multiplication by \(e_2\) is, in this
realization, the nonzero scalar \(-1/2\) times
\(B\mapsto\mathcal K(g,B)\).

Contract the first and third slots using \(g^{-1}\). Direct
summation in (SR3.11) gives
\[
\operatorname{Ric}\mathcal K(g,B)
  =(d-2)B+(\operatorname{tr}B)g.
\tag{SR3.12}
\]
The trace of this expression is \(2(d-1)\operatorname{tr}B\).
Consequently the inverse on the image is the explicit map
\[
B=\frac1{d-2}\left(
 \operatorname{Ric}R-
 \frac{\operatorname{tr}\operatorname{Ric}R}{2(d-1)}g\right).
\tag{SR3.13}
\]
All denominators are nonzero for every declared \(m\ge4\).
This proves injectivity of the actual \(e_2\) map. The same
formula gives a right inverse to Ricci on all symmetric
tensors. Subtracting \(\mathcal K(g,B)\) with \(B\) from
(SR3.13) defines the equivariant projector onto
\(\mathcal R=\ker\operatorname{Ric}\). Thus the degree-four
module is the actual direct sum of the quadratic image and
\(\mathcal R\). Every map is \(O(W,g)\)-equivariant and
hence \(S_m\)-equivariant.

With degree shifts written explicitly, the entire cokernel
is therefore the following actual graded \(I,S_m\)-module:
\[
\begin{aligned}
C\simeq{}&
\bigl(I/(e_2^2,e_3,\ldots,e_m)\bigr)[2]
                          \otimes\operatorname{Sym}^2W\\
&\oplus (I/I_+)[3]\otimes S_{(2,1)}W
 \oplus (I/I_+)[4]\otimes\mathcal R.
\end{aligned}
\tag{SR3.14}
\]
For the first summand, send its degree-two generator to the
given class and its multiple by \(e_2\) to the actual image
under multiplication. The injection just proved makes this
a chain of length exactly two. All other positive invariant
actions vanish by degree. The other two summands use the
displayed Young and Ricci projectors. This proves (SR3.14)
as a module isomorphism, including all invariant actions.

## 3. Cancelling free covers by explicit homogeneous basis changes

Apply \(\operatorname{Hom}_{S_m}([\nu],-)\). Rational
averaging is exact. The actual invariant/coinvariant
multiplication \(I\otimes H\simeq P\) of A088§1 makes
\(\mathcal A_\nu\) and \(\mathcal B_\nu\) finite graded
free, with basis polynomials \(A_\nu,B_\nu\).
Equation (SR3.14) gives \(c_2,c_{21},c_R\) copies of its
three displayed cyclic modules. Their minimal generator
and relation free modules are \(M_0,M_1\), with basis
polynomials \(C_0,C_1\) in (SR3.4). The relations are
the literal generators \(e_2^2,e_3,\ldots,e_m\) or
\(e_2,\ldots,e_m\), in the indicated component and degree.

We now compare these covers with the actual map. In the
quotient \(\mathcal B_\nu/I_+\mathcal B_\nu\), select
homogeneous vectors mapping to the displayed basis of
\(C_\nu/I_+C_\nu\). Lift them so that their images in
\(C_\nu\) are the specified cyclic generators, subtracting
positive-invariant multiples of already chosen lifts as
needed. Choose a complementary residue basis in the kernel.
Each complementary image is an invariant-polynomial
combination of the specified cyclic generators with zero
constant coefficients. Subtract these same combinations
of their lifts. The complementary images become zero.
These operations preserve the residue basis and hence give
an invertible homogeneous basis change by graded Nakayama.
The quotient map is now the literal direct sum of
\(M_0\to C_\nu\) and a free summand mapping to zero.

The latter free summand lies in the image of \(\phi_\nu\).
Lift its basis through \(\phi_\nu\), extend \(I\)-linearly,
and cancel this actual split summand on both sides. The
remaining domain \(\mathcal A_0\) is graded free: it is
projective, and the two graded Nakayama steps in G038§3
give a free basis. Its map is onto
\(L_1=\ker(M_0\to C_\nu)\).

Lift the specified minimal generators of \(L_1\), namely
the relation basis of \(M_1\), to homogeneous vectors of
\(\mathcal A_0\). Their residues are independent because
their images form a basis of \(L_1/I_+L_1\). Choose a
complement in the kernel of this residue map and lift it.
Its images lie in \(I_+L_1\), so they are combinations of
the minimal relation generators with coefficients in
\(I_+\). Subtracting those combinations of the chosen
lifts makes these images zero. This invertible triangular
basis change proves the actual decomposition
\[
K_\nu\simeq\mathcal F_\nu\oplus
                  \ker(M_1\longrightarrow M_0).
\tag{SR3.15}
\]
The free basis polynomial of \(\mathcal F_\nu\) is exactly
\(A_\nu-B_\nu+C_0-C_1=F_\nu\). This proves all the
nonnegative coefficients asserted in (SR3.4). It also
proves the degree bound \(N+3\): the free domain has
degrees at most \(N+3\), and every correction has degree
at most \(m+4\le N+3\) for \(m\ge4\).
All choices above are fixed by homogeneous rational row
reduction; the claimed kernel is the kernel of the original
map through the displayed invertible changes of bases.

## 4. Positive bases for both types of relation cycles

For a polynomial ring \(J=\mathbb Q[z_1,\ldots,z_k]\)
with positive weights \(w_i\), the kernel of
\(\bigoplus J\xi_i\to J\), \(\xi_i\mapsto z_i\),
has the following complete vector-space basis. For every
nonzero exponent vector \(\beta\), let \(i\) be its first
positive index; for each further positive index \(j>i\), use
\[
z^\beta\left(\frac{\xi_j}{z_j}-\frac{\xi_i}{z_i}\right).
\tag{SR3.16}
\]
The denominators cancel. In that multidegree the differential
sends each available coordinate vector to \(z^\beta\),
so exactly these differences form a basis of its kernel.
This proves (SR3.5) for arbitrary specified positive weights
by a direct coefficientwise bijection.

For the ordinary relation sequence, take
\(J=I\), \(z=(e_2,\ldots,e_m)\) and weights \(\mathbf u\).
For the other sequence take
\[
J=\mathbb Q[e_2^2,e_3,\ldots,e_m],\qquad
z=(e_2^2,e_3,e_4,\ldots,e_m).
\]
These are algebraically independent, and \(I=J\oplus e_2J\)
as an actual graded free \(J\)-module. Tensoring the kernel
map with this free module preserves its kernel. Its basis
is (SR3.16) and \(e_2\) times that same basis. Its Hilbert
series is therefore \((1+q^2)Z_{\mathbf v}\), with the
two degree-four generators still separately indexed.
The decompositions (SR3.14)–(SR3.15) now prove precisely
(SR3.6), after using the exact highest-space map (SR3.7).

## 5. Polynomial computation of every finite numerator and multiplicity

G038/SR2.14–16 already compute the tensor operators
\(T\mapsto T\otimes W\) and
\(T\mapsto T\otimes\operatorname{Sym}^2W\) through corner
and two-strip paths. Here is a finite path formula for the
remaining symmetric cube. The actual monomial orbit
decomposition of \(\operatorname{Sym}^3E\), \(E=\mathbb Q^m\),
has orbits of types3,21,111. They give respectively the
point, ordered-pair and unordered-triple permutation modules.
Since \(E=\mathbf1\oplus W\), the direct symmetric-power
decompositions give in the representation ring
\[
[\operatorname{Sym}^3W]
=[\mathbb Q\{(i,j):i\ne j\}]
+[\mathbb Q\{\{i,j,k\}:i,j,k\text{ distinct}\}]
-[\mathbb Q\{\{i,j\}:i\ne j\}].
\tag{SR3.17}
\]
This follows by subtracting the actual decompositions of
\(\operatorname{Sym}^3E\) and \(\operatorname{Sym}^2E\);
it computes characters of the stated actual symmetric cube.
The final positive numerator was already proved by modules
in §3, independently of this subtraction used in its algorithm.

Tensoring with the ordered-pair module is restriction to
\(S_{m-2}\) followed by induction: remove two boxes in
order, then add two in order, counting every path.
Tensoring with the unordered-triple module is restriction
to \(S_{m-3}\times S_3\) and induction. For each removed
three-box shape \(\beta\subset\nu\), its three restriction
multiplicities are
\[
\begin{aligned}
u_3(\nu/\beta)&=\mathbf1_{\nu/\beta\text{ horizontal}},\\
u_{111}(\nu/\beta)&=\mathbf1_{\nu/\beta\text{ vertical}},\\
u_{21}(\nu/\beta)&=
 \#\{\gamma:\nu/\gamma\text{ one box},
               \gamma/\beta\text{ horizontal two-strip}\}
 -u_3(\nu/\beta).
\end{aligned}
\tag{SR3.18}
\]
Pieri proves the first two identities; the third follows from
the actual induction decomposition \(s_2s_1=s_3+s_{21}\).
Thus the tensor multiplicity of \([\alpha]\) is
\(\sum_\beta\sum_{\tau=3,21,111}
u_\tau(\nu/\beta)u_\tau(\alpha/\beta)\).
These are the rational coset and Young maps already specified
in G038§6. At most three corner removals and three additions
are used, so this has polynomial size \(O(m^6)\).

The other fixed Schur modules in (SR3.3) are computed from
the two displayed Jacobi–Trudi/Pieri identities
\[
\begin{aligned}
[S_{(2,1)}W]&=[\operatorname{Sym}^2W\otimes W]
                                      -[\operatorname{Sym}^3W],\\
[S_{(2,2)}W]&=[\operatorname{Sym}^2W\otimes\operatorname{Sym}^2W]
                                      -[\operatorname{Sym}^3W\otimes W].
\end{aligned}
\tag{SR3.19}
\]
For the second identity, the summands \((4),(3,1)\) cancel
from the two actual Pieri decompositions, leaving precisely
\((2,2)\). Compose the already specified tensor operators;
only a fixed number of corner steps is involved. The
coefficient of the trivial label in \([\nu]\otimes T\)
gives \([T:[\nu]]\), using the actual invariant perfect
Specht pairing. Finally subtract the quadratic image
multiplicity from \([S_{(2,2)}W:[\nu]]\) to obtain \(c_R\),
justified by the Ricci splitting (SR3.12)–(SR3.13).

For every encountered label use the exact fake-degree
polynomial G038/SR2.16, with its finite hook product
division through degree \(N\). The number of corner paths
is polynomial in \(m\), their length is fixed, and every
coefficient has \(O(m\log m)\) bits by the standard-tableau
bound. This computes (SR3.2)–(SR3.4) in polynomial bit
complexity. No partition enumeration or uncomputed tensor
multiplicity is used by the formula executable.

## 6. Literal polytopes, exact support and evaluation

Each nonzero coefficient \(f_{\nu,j}\), \(j\le D\), gives
the free-degree polytope G038/SR2.17 with multiplicity
\(f_{\nu,j}\) and target degree \(D-j\). It has \(m\)
variables. For each of the three possible cycle terms, use
one least-support polytope as follows. For its weight list
\((w_1,\ldots,w_k)\), multiplicity \(c>0\), and shifted
degree \(L\), take integer variables
\(z_i,y_i\in[0,1]\), exponents
\(0\le b_i\le\lfloor L/w_i\rfloor\), and
\(0\le u\le c-1\). Impose
\[
\begin{gathered}
\sum_i z_i=1,\quad\sum_i y_i=1,\quad
y_j\le\sum_{i<j}z_i,\\
b_j\ge z_j+y_j,\qquad
b_j\le L\sum_{i\le j}z_i.
\end{gathered}
\tag{SR3.20}
\]
For the ordinary cycle term impose \(\sum_i w_ib_i=L\).
For the quadratic-sequence term append
\(\eta\in[0,1]\) and impose
\(\sum_i w_ib_i+2\eta=L\).
These are exactly the monomial-cycle labels in (SR3.16),
with \(\eta\) recording the free \(J\)-basis \(1,e_2\).
The bit \(z\) records the first positive exponent and
\(y\) the chosen later positive index; their inverse is
unique. There are \(3(m-1)+1\) ordinary variables and
one additional quadratic remainder bit, giving maximum
\(3m-1\). There are at most \(N+4\) free-degree pieces
and three cycle pieces, giving \(N+7\).

The free terms have the exact support test
\(f_{\nu,j}>0\) and \(D-j\in\{0,2,3,\ldots\}\).
For \(m\ge4\), ordinary cycles have every degree at least5,
as proved in G037/HK17. The quadratic-sequence cycles after
extension to \(I\) have every degree at least7 and no
smaller degree. To verify this last assertion directly,
the three generator weights4,3,4 give basis degrees7 and8,
and multiplication by the remainder basis element \(e_2\)
adds2. The least-support branch with first index1 permits
every further monomial in weights3 and4. Degrees7,8,9,10,
11,12 are all reached, and adding3 reaches every larger
degree. Every basis vector uses two distinct generator
indices of total weight at least7. Hence the complete
support test is the union of the free test and
\[
(c_{21}>0\text{ and }D\ge8)
\quad\text{or}\quad
((c_2+c_R)>0\text{ and }D\ge9).
\tag{SR3.21}
\]

Exact evaluation uses G037's Bostan–Mori parity operation
on each rational series in (SR3.6). There are \(O(m^2)\)
cycle pairs, each with degree \(O(m^2)\) denominator,
all roots of unity. The same explicit polynomial bit
bound proved in G037§6 applies to their specified weights
and the finite numerator from (SR3.4). Summing the terms
remains polynomial in \(m\) and \(\log(D+1)\).
The executable `stable_third_row_positive.py` supplies the
literal path counts, polynomials, support and matrix data.

## 7. The complete \(m=3\) endpoint

Here \(\dim W=2\). Complementary column wedge pairing
gives the actual equivariant isomorphism
\[
S_{(a,3)}W\simeq(\det W)^3\otimes\operatorname{Sym}^{a-3}W.
\tag{SR3.22}
\]
The three two-box columns supply the determinant factor,
and the remaining row is the symmetric power. The
determinant of \(W\) is the sign character, so the
effective label becomes \(\nu'\). The three fake-degree
polynomials for \(S_3\) are respectively
\(1,q+q^2,q^3\) for \((3),(2,1),(1,1,1)\), obtained
from the same hook formula. Thus the coefficient is
\[
[q^{a-3}]\frac{f_{\nu'}(q)}{(1-q^2)(1-q^3)}.
\tag{SR3.23}
\]
Its at-most-two free-degree polytopes have at most three
variables, and include \(a=3\) without a missing endpoint.
Its support is the same finite coin test. These bounds
are within the global \(N+7\), \(3m-1\) bounds.

## 8. Geometric transport and verification scope

The stable flag/frame map (SR3.7), its determinant pairing
and every Young/coset morphism are the literal maps already
identified in G015, T032 and G038. Cubic transfer defines
a coherent kernel over \(\operatorname{Spec}I\). The
Ricci contraction is a rational associated-bundle morphism
on the orthogonal frame reduction, with exact inverse
(SR3.13) on its specified image. The finite cyclic
presentations in (SR3.14) and actual homogeneous changes
of bases in (SR3.15) identify the same kernel sheaf with
its free and Koszul summands. Flat extension from
\(\operatorname{Spec}J\) uses the exhibited two-element
free basis \(1,e_2\). Thus the positive counts are basis
counts for those actual coherent modules.

The locators are SGA3 I4.5 and4.7.2–4.7.3 for frames
and associated bundles; EGA II2.4.1–2.4.2 and2.5.2/2.5.4
for the projective/coherent constructions; SGA6 VI3.3
and V4.2,4.4,4.8–4.9 for the exact Schur and K0 operations.
Archive cote133/028 is transported by A012's tensor-word,
weight and Young maps. The coefficients are in
characteristic zero; the maps spread after their actual
finite denominators, including \(d-2\) and \(2(d-1)\),
are inverted. No unspecified integral rank comparison is
asserted.

Full-proof readings and executed finite checks are separate
dated events. The complete unbounded formula is proved by
the exact cokernel action and module decomposition above.
