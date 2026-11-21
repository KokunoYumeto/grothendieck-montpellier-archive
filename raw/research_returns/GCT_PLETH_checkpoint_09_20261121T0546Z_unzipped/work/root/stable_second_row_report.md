# Stable tails with second part two in every outer degree

## G-038. Positive free and Koszul formulas for all stable tails \((a,2)\)

Let \(m\ge3\), \(a\ge2\), \(t\ge0\), \(n\ge a+t\), and
\(\mu\vdash m\). Define
\[
\begin{gathered}
\lambda=(mn-a-2-(m-1)t,a+t,t+2,t^{m-3}),\qquad D=a+2,\\
\nu=\mu\quad(t\text{ even}),\qquad
\nu=\mu'\quad(t\text{ odd}),\qquad N=\binom m2.
\end{gathered}
\tag{SR2.1}
\]
The displayed tuple is a partition: its first gap is at least
\(a-2\), and its second gap is \(a-2\). The coefficient
\(p_{\mu,(n)}^\lambda\) has a positive description by at most
\(N+4\) explicitly constructed bounded polytopes, each with at
most \(3m-3\) variables. Their matrices and an exact coefficient
and support evaluator have bit complexity polynomial in \(m\)
and the binary parameter lengths. At \(t\ge1\), the ordinary
binary-part output lists \(m\) positive parts. At \(t=0\), the
bound is stated in \(m\) and the binary parameters; no bound
polynomial in the compressed \(\log m\) encoding is asserted.

Here is the full formula. Put \(W=\mathfrak h_m\),
\(P=\operatorname{Sym}W\), and
\(I=P^{S_m}=\mathbb Q[e_2,\ldots,e_m]\), with
\(\deg e_i=i\). Let \(f_\alpha(q)\) be the actual graded
coinvariant multiplicity polynomial of \([\alpha]\), as in
G037/HK8–11. For a representation \(T\), write
\(f_T=\sum_\alpha[T:[\alpha]]f_\alpha\). Define
\[
A_\nu(q)=q^2f_{[\nu]\otimes\operatorname{Sym}^2W}(q),
\qquad B_\nu(q)=qf_{[\nu]\otimes W}(q).
\tag{SR2.2}
\]
There are two specified exceptional labels:
\[
\begin{array}{c|c}
\nu&d_\nu\\\hline
(m-1,1)&1\\
(m-2,1,1)&2
\end{array}
\]
They are distinct for every \(m\ge3\). Let \(\epsilon_\nu=1\)
on these two labels and zero on all others; terms containing
\(d_\nu\) below occur only for these two labels. Set
\[
F_\nu(q)=A_\nu(q)-B_\nu(q)
+\epsilon_\nu q^{d_\nu}
 \left(1-\sum_{i=2}^m q^i\right)
=\sum_{j=0}^{N+2}c_{\nu,j}q^j.
\tag{SR2.3}
\]
Every \(c_{\nu,j}\) is a nonnegative integer. The exact positive
coefficient is
\[
\boxed{\begin{aligned}
p_{\mu,(n)}^\lambda
={}&\sum_{j=0}^{N+2}c_{\nu,j}
 \#\{(b_2,\ldots,b_m)\ge0:\ \sum_{i=2}^m ib_i=D-j\}\\
&+\epsilon_\nu [q^{D-d_\nu}]
 \sum_{2\le i<k\le m}
 \frac{q^{i+k}}{\prod_{l=i}^m(1-q^l)}.
\end{aligned}}
\tag{SR2.4}
\]
All counts with a negative right side are zero. Sections3–5 give
the actual module decomposition proving positivity of (SR2.3),
and sections6–7 give a polynomial algorithm for its coefficients
and every polytope matrix.

## 1. Exact transport to the stable Schur module

Use the stable flag coordinate map T032/C4–8, or the balanced
highest-space model G015 with ideal order zero. Removing the
displayed determinant line by its perfect exterior-column pairing
gives the actual \(S_m\)-module isomorphism
\[
(S_\lambda\mathbb Q^m)_{(n^m)}
\simeq\operatorname{sgn}^t\otimes S_{(a,2)}W.
\tag{SR2.5}
\]
The condition \(\lambda_2\le n\) is precisely \(a+t\le n\).
The same coordinate map multiplies the stable first-row generator
when \(n\) increases, and its inverse divides on the specified
stable chart; polynomial extension was proved in T032. Thus
(SR2.5) identifies the original coefficient with
\([S_{(a,2)}W:[\nu]]\), including the sign twist. All subsequent
maps are on this actual Schur module.

## 2. Quadratic polarization, its kernel and its whole cokernel

Give the two free \(P\)-modules
\[
\mathcal A=P\otimes\operatorname{Sym}^2W,
\qquad \mathcal B=P\otimes W
\]
the total grading in which their tensor factors have degrees two
and one. The \(P\)-linear, \(GL(W)\)-equivariant morphism is
\[
\phi(f\otimes uv)=fu\otimes v+fv\otimes u.
\tag{SR2.6}
\]
Put \(K=\ker\phi\). In total degree \(D\ge4\), Pieri gives
\[
\begin{aligned}
\mathcal A_D&=S_{(D)}W\oplus S_{(D-1,1)}W
                         \oplus S_{(D-2,2)}W,\\
\mathcal B_D&=S_{(D)}W\oplus S_{(D-1,1)}W.
\end{aligned}
\tag{SR2.7}
\]
The Young inclusions are the rational tensor symmetrizers; use
Macdonald I§5(5.16), p73, for the Pieri decomposition. The map
on the first summand is nonzero, since
\(x^{D-2}\otimes x^2\) maps to
\(2x^{D-1}\otimes x\). On the second summand its highest vector
\[
x^{D-2}\otimes xy-x^{D-3}y\otimes x^2
\]
maps to
\(x^{D-1}\otimes y-x^{D-2}y\otimes x\), which is nonzero.
Both vectors are killed by the raising operator sending \(y\)
to \(x\), so this specifies the asserted highest summands.
The highest vector
\[
x^{D-2}\otimes y^2-2x^{D-3}y\otimes xy
                       +x^{D-4}y^2\otimes x^2
\]
is killed by \(\phi\) and by that raising operator. Its weight is
\((D-2,2)\). The rational Young inclusion and complete
reducibility now give the exact kernel
\[
K_D=S_{(D-2,2)}W\quad(D\ge4).
\tag{SR2.8}
\]
These calculations remain valid in dimension two; unavailable
Schur summands vanish by their column antisymmetrizers.

The small degrees determine the entire cokernel. At degree one,
\(\mathcal A_1=0\) and \(\mathcal B_1=W\). At degree two,
the map is the nonzero symmetric inclusion
\(\operatorname{Sym}^2W\to W\otimes W\), whose cokernel
is \(\Lambda^2W\). At degree three the two summands displayed
for \(\mathcal B_D\) occur once in \(\mathcal A_D\), and the
same two nonzero vectors prove surjectivity. All degrees at least
four were already covered. Consequently
\[
\operatorname{coker}\phi=W\text{ in degree1}
                 \ \oplus\ \Lambda^2W\text{ in degree2}.
\tag{SR2.9}
\]
Every positive-degree element of \(I\) kills this cokernel,
because its degree is at least two and all cokernel degrees at
least three are zero. The exterior hook Young map identifies
\(W=[m-1,1]\) and \(\Lambda^2W=[m-2,1,1]\).
This proves the two exact exceptional labels, with multiplicity
one and their specified degrees.

## 3. Actual free modules away from those two labels

Apply \(\operatorname{Hom}_{S_m}([\nu],-)\) to (SR2.6).
Rational averaging makes this functor exact. The homogeneous
coinvariant section, averaged over \(S_m\), gives the actual
graded multiplication isomorphism \(I\otimes H\simeq P\)
used in A088§1, with \(H=P/(I_+)\). Thus
\(\mathcal A_\nu\) and \(\mathcal B_\nu\) are finite graded
free over \(I\); their basis polynomials are exactly
\(A_\nu(q)\) and \(B_\nu(q)\). The rational invariant perfect
forms identify dual Specht modules and justify the tensor
multiplicity notation in (SR2.2).

For every label outside the two in (SR2.9), the actual map
\(\mathcal A_\nu\to\mathcal B_\nu\) is surjective. Lift each
chosen homogeneous free basis vector of the target and extend
\(I\)-linearly. This is a graded section of the displayed map,
so its kernel is finite graded projective. Choose homogeneous
lifts of a basis modulo \(I_+\). Graded Nakayama gives a
surjective map from the associated graded free module. Its
kernel is a graded direct summand, because the target is
projective. Reducing modulo \(I_+\) leaves zero kernel, and a
second graded Nakayama application gives zero kernel itself.
This proves a free isomorphism. Its basis degrees have
polynomial \(A_\nu-B_\nu=F_\nu\), establishing positivity
for every such label through an actual module decomposition.

## 4. The two exceptional modules and the exact Koszul summand

Fix either of the two listed labels and write \(d=d_\nu\).
The cokernel is one copy of \(I/I_+\) in degree \(d\).
Choose a homogeneous free basis of \(\mathcal B_\nu\)
adapted to its quotient: one basis vector \(e_0\) of degree
\(d\) maps to1, and every other basis vector maps to0.
Such a basis is obtained by rational row reduction among the
degree-\(d\) basis vectors; all other degrees already map to0.
It follows exactly that
\[
\operatorname{im}\phi_\nu=I_+e_0\oplus\mathcal B',
\tag{SR2.10}
\]
where \(\mathcal B'\) is the free span of the remaining vectors.

Lift the basis of \(\mathcal B'\) through the actual map.
Projection to \(\mathcal B'\) gives a split surjection, and
its kernel \(\mathcal A_0\) is graded free by the same
projective/Nakayama proof. The remaining map is the actual
surjection
\(\mathcal A_0\to I_+e_0\).
For each \(i=2,\ldots,m\), choose a homogeneous lift \(x_i\)
of \(e_ie_0\), in degree \(d+i\).
Their residues in \(\mathcal A_0/I_+\mathcal A_0\) are
linearly independent: a relation would map to a relation among
the independent minimal generators \(e_i\) in
\(I_+/I_+^2\). Choose a homogeneous complementary residue
basis in the kernel of this residue map and lift it to vectors
\(y_j\). The \(x_i,y_j\) form a homogeneous free basis;
the graded Nakayama argument just given proves this directly.

Every image of \(y_j\) is in \(I_+^2e_0\). Express it as
\(\sum_i g_{ji}e_ie_0\), where each \(g_{ji}\in I_+\)
is homogeneous, and replace \(y_j\) by
\(y_j-\sum_i g_{ji}x_i\). This is an invertible triangular
basis change and makes every such image zero. We have proved
the actual graded decomposition
\[
\begin{gathered}
K_\nu\simeq\mathcal F_\nu\oplus Z_1(I)[d],\\
Z_1(I)=\ker\left(\bigoplus_{i=2}^m I\xi_i
 \longrightarrow I\right),\quad
\deg\xi_i=i,\quad\xi_i\longmapsto e_i.
\end{gathered}
\tag{SR2.11}
\]
Here \([d]\) denotes addition of \(d\) to the degrees, and
\(\mathcal F_\nu\) is the free span of the adjusted \(y_j\).
Every map and basis choice can be implemented by rational
homogeneous row reduction in the indicated finite degrees.

The basis polynomial of \(\mathcal A_0\) is
\(A_\nu-B_\nu+q^d\). Removing the displayed free basis
vectors \(x_i\) subtracts \(q^d\sum_{i=2}^m q^i\).
The remaining free polynomial is exactly (SR2.3). Its
coefficients are therefore nonnegative integers for both
exceptional labels as well. Since the coinvariant degrees
are at most \(N\), every free generator degree is at most
\(N+2\). The same bound covers the correction terms because
\(m\le N\) for \(m\ge3\).

## 5. A polynomial basis for the weighted Koszul cycle

For a monomial \(e^\beta\), let
\(J=\{i:\beta_i>0\}\) and \(i=\min J\).
For each \(k\in J\setminus\{i\}\), the polynomial vector
\[
e^\beta\left(\frac{\xi_k}{e_k}
                         -\frac{\xi_i}{e_i}\right)
\tag{SR2.12}
\]
is in \(Z_1(I)\). The notation has no poles: both denominators
divide the displayed monomial. In this multidegree the map to
\(I\) sends every basis vector \(e^\beta\xi_j/e_j\)
to \(e^\beta\). Its kernel has precisely the differences
in (SR2.12) as a basis. This is a complete direct proof over
every multidegree, and agrees with G037/HK13–14 and A088§2.

The index \(i\) is the first positive exponent; choosing
\(k>i\) forces both exponents to be positive. Other exponents
with index at least \(i\) are arbitrary. Consequently the
Hilbert series of this actual basis is
\[
\operatorname{Hilb}Z_1(I)
=\sum_{2\le i<k\le m}
  \frac{q^{i+k}}{\prod_{l=i}^m(1-q^l)}.
\tag{SR2.13}
\]
Combining (SR2.8), the free decompositions and (SR2.13) gives
(SR2.4) in every parameter of (SR2.1).

## 6. Computing the free numerator in polynomial time

No enumeration of all partitions of \(m\) is needed. Write
\(\alpha\nearrow\beta\) for addition of one corner box.
The permutation module \(E=\mathbb Q^m\) has \(E=\mathbf1\oplus W\).
The actual coset tensor map and restriction/induction give
\[
[\nu]\otimes E\simeq
 \operatorname{Ind}_{S_{m-1}}^{S_m}
 \operatorname{Res}_{S_{m-1}}^{S_m}[\nu].
\]
For definiteness, the coset tensor isomorphism sends
\(v\otimes gH\) to \(g\otimes g^{-1}v\), with inverse
\(g\otimes w\mapsto gw\otimes gH\).
Therefore the multiplicity of \([\alpha]\) in
\([\nu]\otimes W\) is the number of two-step paths
\(\nu\searrow\beta\nearrow\alpha\), minus
\(\mathbf1_{\alpha=\nu}\). This yields at most \(O(m^2)\)
candidate labels by literal corner operations.

There is also an actual isomorphism
\[
\mathbb Q\{\{i,j\}:i<j\}
 \longrightarrow\operatorname{Sym}^2W,
\qquad \{i,j\}\longmapsto(P_me_i)(P_me_j).
\tag{SR2.14}
\]
To prove injectivity, pair with the hyperplane \(\sum x_i=0\).
A kernel element gives a quadratic polynomial
\(\sum_{i<j}a_{ij}x_ix_j\) vanishing on that hyperplane.
It is divisible by \(\sum x_i\), and hence equals
\((\sum x_i)(\sum b_ix_i)\). Its square coefficients are
zero, forcing every \(b_i=0\), and then every \(a_{ij}=0\).
Both spaces have dimension \(\binom m2\), proving the stated
equivariant isomorphism, with a rational inverse.

The left side of (SR2.14) is the coset module for
\(S_{m-2}\times S_2\). The same tensor-coset map identifies
\([\nu]\otimes\operatorname{Sym}^2W\) with induction of
its restriction to that subgroup. One removes a two-box
horizontal strip or a two-box vertical strip from \(\nu\)
and adds a strip of the same kind. Each branch has multiplicity
one by the two Pieri identities, and different branches are
counted separately. Thus
\[
\begin{aligned}
M_{\nu,\alpha}={}&
 \#\{\beta:\nu/\beta,\alpha/\beta
                         \text{ horizontal strips of size2}\}\\
&+\#\{\beta:\nu/\beta,\alpha/\beta
                         \text{ vertical strips of size2}\}.
\end{aligned}
\tag{SR2.15}
\]
This formula follows from Frobenius reciprocity and the actual
rational Young branching maps; use Macdonald I§7(7.1)–(7.3),
pp112–113, and I§5(5.16) and its conjugate, p73. Two corner
removals followed by two additions give \(O(m^4)\) candidate
paths. The strip tests are the displayed interlacing inequalities
for horizontal strips and row differences at most one for
vertical strips. No unspecified tensor-product coefficient is
left in (SR2.2).

For each encountered \(\alpha\), use the proved fake-degree
formula from G037/HK8–11:
\[
f_\alpha(q)=q^{b(\alpha)}
 \frac{\prod_{i=1}^m(1-q^i)}
      {\prod_{c\in\alpha}(1-q^{h(c)})}.
\tag{SR2.16}
\]
Truncate the formal product division at degree \(N\); this
recovers the whole polynomial, whose degree is at most \(N\).
The coefficients count standard tableaux with the proved comajor
statistic and have size at most \(m!\). The path multiplicities
are polynomial in \(m\), so every computed coefficient has
\(O(m\log m)\) bits. Equations (SR2.2)–(SR2.3) now compute
all \(c_{\nu,j}\) in polynomial bit complexity. Positivity
was proved by the exact free decomposition and is also checked
as an executable assertion.

## 7. Literal polytopes, support and binary-degree evaluation

For each \(j\) with \(c_{\nu,j}>0\) and \(j\le D\), take
the following bounded polytope in \(m\) variables:
\[
\begin{gathered}
0\le u\le c_{\nu,j}-1,\qquad
0\le b_i\le\left\lfloor\frac{D-j}{i}\right\rfloor
\quad(2\le i\le m),\\
\sum_{i=2}^m ib_i=D-j.
\end{gathered}
\tag{SR2.17}
\]
The integer coordinate \(u\) indexes the homogeneous free
basis vectors in degree \(j\); \(b\) indexes their invariant
monomial multiples. Fixing a basis by the homogeneous rational
row reductions above gives an actual bijection. The matrices
are computed from (SR2.3) and need no construction of the full
possibly large basis.

On an exceptional label, append the single polytope
G037/HK19 with \(r=1\), trivial label, and total degree
\(D-d_\nu\). It uses the \(3(m-1)\) variables recording
least support, one chosen further support index, and exponents.
Its already proved inverse is exactly (SR2.12). Here the hook
parameter passed to G037 is \(D-d_\nu-1\ge1\), so every
declared input lies in its domain. There are at most \(N+3\)
free-degree polytopes and one cycle polytope, giving the bound
\(N+4\) and maximum dimension \(3m-3\).

The support test is explicit. A free-degree term contributes
precisely when \(c_{\nu,j}>0\) and
\(D-j\in\{0,2,3,4,\ldots\}\), because the available
coin sizes contain2 and3 and have no1. The cycle term uses
G037's proved trivial-hook support: for \(m\ge4\), every
degree at least5 occurs; for \(m=3\), degrees at least5
occur except6. Applying this to \(D-d_\nu\), and taking
the union with the free-degree test, decides every zero.

For exact coefficient evaluation, apply G037/HK18's proved
Bostan–Mori parity extraction to
\(F_\nu(q)/\prod_{i=2}^m(1-q^i)\), and append the same
G037 trivial-hook evaluator at the shifted degree. Numerator
and denominator degrees are \(O(m^2)\); the denominator
roots are roots of unity, and the bit bound proved there
applies verbatim to these exact polynomials. This supplies
polynomial bit complexity in \(m\) and \(\log(D+1)\).
The executable `stable_second_row_positive.py` contains the
corner and strip paths, every finite polynomial, support test,
literal matrix and coefficient procedure.

## 8. Geometric dictionary and check scope

Equation (SR2.5) is the actual balanced frame/flag comparison
of G015 and T032, with its determinant line. Equations
(SR2.6), (SR2.10) and (SR2.11) define morphisms and coherent
kernel sheaves over \(\operatorname{Spec}I\). The free
summands and weighted Koszul cycle are actual sheaves with
the exhibited presentations and basis morphisms. The
coset/Young maps in (SR2.14)–(SR2.15) transport the invariant
character calculation to this same kernel. These comparisons
use SGA3 I4.5/4.7.2–4.7.3 for frames and associated bundles,
EGA II2.4.1–2.4.2 and2.5.2/2.5.4 for the projective and
coherent constructions, SGA6 VI3.3 and V4.2,4.4,4.8–4.9
for the exact Schur and K0 operations. Archive cote133/028
is carried by A012's actual tensor-word, torus-weight and
Young maps. All maps are rational and spread after their
displayed finite denominators are inverted; the coefficient
theorem concerns the characteristic-zero fiber.

Whole-proof readings and independent computations are recorded
as separate dated events. The finite checks exercise the
proved maps and formulas; their numerical ranges do not replace
the unbounded module argument in sections2–5.
