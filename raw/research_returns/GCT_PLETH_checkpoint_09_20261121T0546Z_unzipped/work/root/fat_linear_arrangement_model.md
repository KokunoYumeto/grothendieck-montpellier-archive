# A fat-linear-arrangement model in every outer degree

## G-027. Exact product-ideal and restriction-complex models

Let \(m\ge3\), \(E=\mathfrak h_m\), and \(F=\mathbf Q^{m-2}\).
Write \(S=\operatorname{Sym}(E\otimes F)\), with its ordinary
polynomial grading, and put
\[
\ell_i=e_i-\tfrac1m\mathbf1,\qquad
I_i=(\ell_i\otimes F)\subset S,\qquad
J_k=\bigcap_{i=1}^m I_i^k,\qquad P_k=\prod_{i=1}^m I_i^k.
\tag{FA.1}
\]
Every ideal here is specified by linear forms; the powers are ordinary
ideal powers. Let \(Q=E/\mathcal O(-1)\) on \(\mathbf P(E)\),
and let \(\mathcal I_Z\) be the ideal of the frame points
\([\ell_i]\).

For every partition \(\alpha\) with at most \(m-2\) rows and
\(N=|\alpha|\), the actual polynomial evaluation maps give
\[
\boxed{H^0(\mathbf P(E),\mathcal I_Z^k\otimes S_\alpha Q)
\simeq\operatorname{Hom}_{GL(F)}(S_\alpha F,(J_k)_N).}
\tag{FA.2}
\]
For every \(k\ge1\) and \(N\ge mk\),
\[
\boxed{(J_k)_N=(P_k)_N.}
\tag{FA.3}
\]
In the same degree range, the signed restriction maps form an exact
\(S_m\times GL(F)\)-equivariant complex
\[
\begin{split}
0\longrightarrow(J_k)_N\longrightarrow S_N
\longrightarrow\bigoplus_{|A|=1}(S/\sum_{i\in A}I_i^k)_N
\longrightarrow\cdots\\
\longrightarrow\bigoplus_{|A|=m-2}
(S/\sum_{i\in A}I_i^k)_N\longrightarrow0.
\end{split}
\tag{FA.4}
\]
The summands carry the orientation of their ordered subset; this
specifies all signs in the group action and differential.

For a partition \(\lambda\vdash mn\) with at most \(m\) rows,
define
\[
\alpha_i=\lambda_2-\lambda_{m+1-i}\quad(1\le i\le m-2),
\qquad k=\max(0,\lambda_2-n),\qquad N=|\alpha|.
\tag{FA.5}
\]
The explicit flag comparison of G-015 gives
\[
\boxed{(S_\lambda\mathbf Q^m)_{(n^m)}
\simeq\operatorname{sgn}^{\lambda_2}\otimes
\operatorname{Hom}_{GL(F)}(S_\alpha F,(J_k)_N).}
\tag{FA.6}
\]
At \(k\ge1\), \(N=\lambda_1-\lambda_2+mk\ge mk\), so
(FA.3)–(FA.4) apply to every such input. At \(k=0\), \(J_0=S\)
and its Schur component is simply \(S_\alpha E\). Thus every
balanced plethysm module has one of these exact descriptions.

The resulting character in §5 is an explicit finite alternating
expression with known terms and actual maps. No unknown cohomology
rank remains in that expression. Its cancellation has not here been
replaced by a uniform small positive formula in every outer degree.
The completed positive specializations are stated separately.

## 1. Global Schur sections and the exact normal-order substitution

The polynomial Cauchy decomposition of \(S\) identifies its
\(S_\alpha F\) multiplicity with \(S_\alpha E\). The natural
quotient \(E\to Q\) gives
\[
S_\alpha E\xrightarrow{\ \sim\ }H^0(S_\alpha Q).
\tag{FA.7}
\]
Here is a verification in the signed tensor convention used throughout
this paper. Apply a primitive Young idempotent to
\([\mathcal O(-1)\to E]^{\otimes N}\), with Koszul signs.
The degree-\(j\) term is a direct sum of
\(\mathcal O(-j)\otimes S_\beta E\), where \(\alpha/\beta\)
is a vertical \(j\)-strip. There are no terms with \(j>m-2\).
The averaged local contraction proves exactness, just as in the
fully written two-row complex. On \(\mathbf P^{m-2}\), every
\(\mathcal O(-j)\), \(1\le j\le m-2\), has zero cohomology
in all degrees. The projective line-bundle calculation therefore
leaves precisely the first term in degree zero and proves (FA.7).
The differential is the same tensor-slot inclusion as in (S.1),
and the exterior-Pieri branching gives its terms; no dimension-only
replacement of the quotient map is being made.

Fix a frame point and choose a basis
\((e_0,e_1,\ldots,e_{m-2})\) of \(E\) with
\(e_0=\ell_i\). On its affine projective chart the moving line is
spanned by \(e_0+\sum_j x_j e_j\). The quotient map sends
\(e_0\) to \(-\sum_jx_je_j\) and fixes the other basis vectors.
In polynomial coordinates on \(E\otimes F\), write \(Y_{0a}\)
for the \(e_0\)-row and \(Y_{ja}\) for the other rows. Evaluation
on the quotient is exactly
\[
Y_{0a}\longmapsto-\sum_{j=1}^{m-2}x_jY_{ja},
\qquad Y_{ja}\longmapsto Y_{ja}\quad(j\ge1).
\tag{FA.8}
\]

This substitution preserves the least normal order. To prove it,
write a nonzero polynomial uniquely as a sum of its homogeneous
degrees in the \(Y_{0a}\), and let \(t\) be the smallest degree
with a nonzero coefficient polynomial in the other rows. Over the
fraction field of those other rows, the square generic matrix
\((Y_{ja})\) has nonzero determinant. The linear substitution from
the \(Y_{0a}\) to the \(x_j\) is therefore invertible over that
field. Its degree-\(t\) image is nonzero and remains homogeneous of
degree \(t\) in \(x\). All later terms have larger \(x\)-degree,
so they cannot cancel it. This proves
\[
\operatorname{ord}_{x=0}f(-xY,Y)
=\min\{t:f\text{ has a nonzero degree-}t
                   \text{ term in }Y_0\}.
\tag{FA.9}
\]
The argument also works for fewer columns by using a nonzero maximal
minor, but the chosen square size suffices here.

The coefficient polynomials in \(Y\) encode the Schur section
faithfully through Cauchy decomposition. Consequently the section
vanishes to order at least \(k\) at \([\ell_i]\) exactly when
its polynomial representative lies in
\((Y_{01},\ldots,Y_{0,m-2})^k=I_i^k\). Intersecting these exact
conditions over every frame point proves (FA.2). All the maps are
induced by the quotient and coefficient substitution, so they commute
with \(GL(F)\) and the literal frame permutation action.

## 2. Product, saturation, and the degree bound

The source used here is Conca–Herzog, *Castelnuovo–Mumford regularity
of products of ideals*, **Theorem3.1, Lemma3.2 and Corollary3.3,
p.6**, with their proofs on **p.7**, in
[arXiv:math/0210065v1](https://arxiv.org/pdf/math/0210065).
They apply to products of nonzero ideals generated by linear forms,
with repetitions allowed. Apply them to the \(mk\) factors formed
by repeating each \(I_i\) exactly \(k\) times. The product
\(P_k\) has regularity \(mk\), and agrees with its saturation in
every degree at least \(mk\).

We now identify that saturation with the stated intersection by an
actual local calculation. The intersection of any \(m-1\) of the
linear spaces defined by the \(I_i\) is the origin: the corresponding
frame vectors span \(E\). Hence a nonzero point belongs to at most
\(m-2\) of those spaces. Their frame vectors are independent.
After a linear coordinate change, their ideals are generated by
disjoint blocks of \(m-2\) variables. For disjoint blocks, a monomial
lies in every \(k\)-th power precisely when its degree in every
block is at least \(k\); this is precisely membership in their
product. The other ideals are units on that local chart. Thus
\(P_k\) and \(J_k\) have the same ideal sheaf on
\(\operatorname{Proj}S\).

Each \(I_i^k\) is saturated: split its variables from a complementary
nonzero block, and multiply by a variable in that complement;
membership in \(I_i^k\) is unchanged. Its intersection is saturated
as well. Therefore \(P_k^{\mathrm{sat}}=J_k\). The cited saturation
degree bound proves (FA.3). Its regularity also gives
\[
H^{q>0}(\operatorname{Proj}S,\widetilde J_k(N))=0
\quad(N\ge mk).
\tag{FA.10}
\]
For the precise algebra-to-sheaf convention, this is the equivalent
regularity formulation in Derksen–Sidman,
*A sharp bound for the Castelnuovo–Mumford regularity of subspace
arrangements*, **Theorem1.2, p.153**, in the
[published primary text](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/05/A.I.a.10.pdf).
The use is the stated regularity implication, not an assertion that
the fat union is reduced.

## 3. The exact signed restriction complex

Consider the closed union with ideal sheaf \(\widetilde J_k\).
The term associated with an ordered subset
\(A=\{i_1<\cdots<i_s\}\) is
\(\widetilde{S/(I_{i_1}^k+\cdots+I_{i_s}^k)}\).
The differential is the alternating sum of restriction maps, adding
one index with sign \((-1)^j\) in its ordered position. A permutation
of the frame carries an ordered subset to its reordered image with
the sign of that reordering. This defines the equivariant complex
and its orientation line explicitly.

The augmented sheaf complex is exact. This is checked on the same
local disjoint-block charts used above. All the ideals there are
monomial block powers. For a monomial, retain precisely those block
indices whose ideals do not contain it. Its component of the
augmented complex is the augmented cochain complex of the full
simplex on those indices. It is exact; contracting along the least
retained index gives an explicit homotopy. A monomial contained in
every ideal has no component. Decomposing by monomials proves
exactness over the coordinate ring, and localization preserves it.
This proves the sheaf statement without an unsupported exactness
assumption for an arbitrary subspace arrangement.

For \(s\le m-2\), the quotient term is a free graded module over
the polynomial ring on the complementary variables, with basis the
normal monomials of degree below \(k\) in each of its \(s\) blocks.
The shifts have total at most \(s(k-1)\). At \(N\ge mk\), every
remaining twist is nonnegative, so all these quotient sheaves have
zero higher cohomology and their zeroth cohomology equals the
indicated graded component. For \(s\ge m-1\), the support is the
origin, so the sheaf is zero. Its degree-\(N\) module component is
also zero: already \(m-1\) independent truncated blocks have
maximum total degree \((m-1)(k-1)<mk\).

Finally (FA.10), the projective cohomology of \(S_N\), and the
ideal sequence show that the union sheaf has zero higher cohomology
in these twists and its global sections are the quotient of \(S_N\)
by \((J_k)_N\). Taking global sections of the exact acyclic
resolution gives precisely (FA.4). This verifies every term and
every endpoint used in that finite complex.

## 4. The complete balanced-flag dictionary

Let \(d=\lambda_m\) and \(a=\lambda_2-d\). In G-015, first
remove the full determinant power \(d\). Over \(\mathbf P(E)\)
the remaining quotient-flag weight on \(Q^*\) is
\((\lambda_3-d,\ldots,\lambda_m-d)\), of length \(m-2\),
and the first-line twist is \(a\). The perfect exterior-column
pairing in the rectangle of width \(a\) gives
\[
S_{(\lambda_3-d,\ldots,0)}Q^*
\simeq(\det Q^*)^a\otimes S_\alpha Q,
\tag{FA.11}
\]
with \(\alpha\) exactly (FA.5). Since
\(\det Q^*=\det E^*\otimes\mathcal O(-1)\), the line twists
cancel and the character is \(\operatorname{sgn}^{d+a}
=\operatorname{sgn}^{\lambda_2}\). The ideal order stays
\(k=\max(0,\lambda_2-n)\). The map back to the original balanced
polynomial is the fixed chart inverse
\(u^{n-\lambda_2}F(v(X))\), with the transverse-order proof of
G-015. Composing that map with (FA.8) and Cauchy extraction proves
(FA.6).

At positive \(k\), the size calculation is
\[
N=(m-2)\lambda_2-\sum_{j=3}^m\lambda_j
=\lambda_1-\lambda_2+m(\lambda_2-n)
=\lambda_1-\lambda_2+mk.
\tag{FA.12}
\]
This verifies the needed degree bound from the partition inequality.
At \(k=0\), (FA.7) and Cauchy decomposition give the plain Schur
module already stated, including \(N=0\). No positive-\(k\)
degree identity is imposed on that separate endpoint.

## 5. Every term as an explicit stabilizer module

For a subset \(A\) of size \(s<m\), there is an invariant direct
sum
\[
E=\operatorname{span}(\ell_i:i\in A)\oplus W_A,
\qquad
W_A=\{(v_j):v_i=0\ (i\in A),\ \sum_{j\notin A}v_j=0\}.
\tag{FA.13}
\]
To verify the intersection is zero, write its first component as
\(\sum_{i\in A}c_i\ell_i\). The zero coordinates on \(A\)
force \(c_i=(\sum c_j)/m\); summing gives
\((1-s/m)\sum c_j=0\), hence every \(c_i=0\).
The dimensions then prove the displayed direct sum. The stabilizer
\(S_s\times S_{m-s}\) permutes the first basis and acts on
\(W_A\) as the standard \(\mathfrak h_{m-s}\).

Put \(T_k(F)=\bigoplus_{t=0}^{k-1}\operatorname{Sym}^tF\).
The quotient term is therefore the actual graded module
\[
S/\sum_{i\in A}I_i^k
\simeq T_k(F)^{\otimes s}\otimes
\operatorname{Sym}(\mathfrak h_{m-s}\otimes F).
\tag{FA.14}
\]
The first symmetric group permutes the \(s\) tensor factors. The
orientation in (FA.4) multiplies that action by \(\operatorname{sgn}_{S_s}\).
Inducing over all subsets gives every term of the complex, with no
unspecified cohomology representation.

Define
\[
C_{s,\alpha,k}=\operatorname{Hom}_{GL(F)}
\left(S_\alpha F,
 [T_k(F)^{\otimes s}\otimes
   \operatorname{Sym}(\mathfrak h_{m-s}\otimes F)]_N\right).
\tag{FA.15}
\]
For \(s=0\), this is \(S_\alpha\mathfrak h_m\).
Exactness proves the representation-ring identity
\[
\boxed{[H^0(\mathcal I_Z^kS_\alpha Q)]
=\sum_{s=0}^{m-2}(-1)^s
\left[\operatorname{Ind}_{S_s\times S_{m-s}}^{S_m}
 (\operatorname{sgn}_{S_s}\otimes C_{s,\alpha,k})\right].}
\tag{FA.16}
\]
All terms in (FA.15) are obtained by tensor products, ordinary Schur
branching and the explicit finite truncation \(t<k\). In particular,
at a permutation with cycle lengths \(c_1,\ldots,c_v\) in the
first subgroup, its polynomial trace factor is exactly
\[
\prod_{j=1}^v\left(\sum_{t=0}^{k-1}h_t(X_1^{c_j},\ldots,
X_{m-2}^{c_j})\right).
\tag{FA.17}
\]
This follows by taking the literal cyclic tensor trace, preserving
the same degree in each factor of a cycle. The remaining symmetric
algebra in (FA.15) has the ordinary Cauchy character with the known
standard representation of the other subgroup. Thus (FA.16) is a
fully specified finite character calculation for every parameter.

## 6. Geometric and computational scope

The constructions are quotient maps of locally free sheaves, powers
of specified coherent ideals, and coefficient extraction from their
Cauchy decomposition. The affine normal-order equality (FA.9),
the projective saturation comparison and the signed restriction
complex prove their exact agreement. They live in the frame/comodule
language of SGA3 I4.5,4.7.2–4.7.3. The exact complex defines its
representation \(K_0\) class. Its geometric map to the bounded-rank
locally free \(K_0\) of SGA6 VI3.3 is this resolution map: choose
finite invariant graded generator spaces for each syzygy over the
regular polynomial ring, take their finite equivariant graded free
resolution, sheafify, and send the bounded complex to the alternating
sum of those locally free terms. Reductivity over \(\mathbf Q\)
supplies the invariant splittings. Choose the lifts minimally from
each syzygy quotient by the homogeneous maximal ideal. After
tensoring with the residue field, all differentials are zero; these
terms compute Tor. The variable Koszul resolution bounds Tor by the
number of variables, so graded Nakayama makes the later minimal
terms zero. This verifies termination for this equivariant form.
For the underlying finite-resolution theorem, the exact primary
locator is Eisenbud, *Lectures on the Geometry of Syzygies*,
MSRI51(2004), Theorems1.2–1.3, p.118,
[author text](https://library.slmath.org/books/Book51/files/04eisenbud.pdf).
This specifies the coherent
comparison used here. The Schur operation is
SGA6 V4.2,4.4,4.8–4.9, transported from cote133/024–029 by A-010.
The ideal sheaves and their graded coordinate maps are the explicit
Proj and coordinate-image constructions of EGA II2.4.1–2.4.2 (p.28) and EGA I9.5.2; graded sheafification and its exactness are EGA II2.5.2 and2.5.4 (p.31).

The new reduction replaces the remaining unspecified flag cohomology
maps by the explicit exact complex (FA.4) and the actual product
ideal (FA.3). Formula(FA.16) retains alternating signs. Its conversion
into small uniformly positive lattice formulas remains a separate
computation; the theorem does not claim that dropping those signs
preserves the representation. G-026 gives one complete positive
specialization, and T-047 computes the independent stable-defect
restriction model with which this complex can be compared.
