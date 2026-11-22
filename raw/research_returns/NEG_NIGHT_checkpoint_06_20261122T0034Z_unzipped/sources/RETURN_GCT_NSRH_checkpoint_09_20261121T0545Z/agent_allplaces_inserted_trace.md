# F55 supplement: all-places regularity tests the zeroth inserted trace

Author: /root/rectangular_and_theta. Date: 21 November 2026 UTC.

This is a separate strengthening of F55 Part2. It does not alter the reviewed fractional construction or its one-place exception. The new argument removes the need for right-action commutation at the base of the all-places obstruction. It also applies to finite virtual traces when their zeroth trace is nonzero. It imposes the same strong all-places regularity condition, which is not automatic from a coefficient scheme.

## 1. Backward propagation of polynomial trace identities

**Lemma A1.** Let W be a finite-dimensional complex vector space, F an invertible endomorphism, X any endomorphism, and b a nonzero complex number. Put

\[
 S_n=\operatorname{Tr}(XF^n)\qquad(n\ge0).
\]

For a polynomial Q(v,Y) in C[v,Y], if Q(b^n,S_n)=0 for every sufficiently large integer n, then

\[
 Q(1,\operatorname{Tr}X)=0.
 \tag{A1}
\]

No commutation of X with F, diagonalizability, algebraicity of their eigenvalues, effectivity, or weight hypothesis is required.

**Proof.** Write Q(v,Y)=sum q_ij v^i Y^j over its finite support. Use the convention W^(tensor0)=C and X^(tensor0)=F^(tensor0)=1. On the finite direct sum

\[
 W_Q=\bigoplus_{q_{ij}\ne0}W^{\otimes j}
\]

define

\[
 T_Q=\bigoplus_{q_{ij}\ne0}b^iF^{\otimes j},
 \qquad
 U_Q=\bigoplus_{q_{ij}\ne0}q_{ij}X^{\otimes j}.
\]

The operator T_Q is invertible. Tensor-product trace gives

\[
 z_n:=\operatorname{Tr}(U_QT_Q^n)
     =Q(b^n,S_n)
 \quad(n\ge0).
 \tag{A2}
\]

This identity does not use X F = F X: the product on each block is q_ij b^(in) (XF^n)^(tensor j).

If d=dim W_Q, write the characteristic polynomial of T_Q as
T^d+c_(d-1)T^(d-1)+...+c_0, with c_0 nonzero. Cayley--Hamilton and trace give

\[
 z_{n+d}+c_{d-1}z_{n+d-1}+\cdots+c_0z_n=0
 \qquad(n\ge0).
\]

Since z_n vanishes for all sufficiently large n and c_0 is nonzero, this recurrence propagates the vanishing backwards one index at a time, down to z_0. Equation (A2) at zero is exactly (A1). The zero polynomial is immediate; otherwise W_Q is nonzero unless W=0 with only positive j, in which case S_n=0 and the assertion follows directly from the polynomial in b^n. QED.

For the intended applications W has positive dimension, so no zero-dimensional convention is needed. The lemma includes all arithmetic Jordan blocks automatically. It also includes finite alternating traces by replacing W with a direct sum and putting the signs into X.

## 2. A polynomial with a prescribed all-places reduction

Let L/C(v) be a finite field extension and set

\[
 O=\mathbb C[v]_{(v-1)}.
\]

Let B be the integral closure of O in L. In characteristic zero, B is finite over O by Stacks Lemma10.161.8, tag032L. It is torsion-free and hence finite free over this DVR by Stacks Lemma15.22.11(3), tag0AUW. Its rank is [L:C(v)]. Its localizations at maximal ideals are the places over v=1; they are DVRs by the finite-normalization, lying-over, and dimension-one-normal-local facts already cited in F55.

**Lemma A3.** Suppose f in L is regular at every place over v=1 and has the same residue c in C at every such place. Then there is a polynomial Q(v,Y) in C[v,Y] satisfying

\[
 Q(v,f)=0,\qquad
 Q(1,Y)=a(1)(Y-c)^d
 \tag{A3}
\]

for some d>0 and some polynomial a with a(1) nonzero.

**Proof.** Regularity at every maximal localization implies f in B. Explicitly, for a fraction f define the denominator ideal I={a in B: af in B}. If f were not in B, I would be proper and contained in a maximal ideal m. Membership f in B_m would give an element a not in m with af in B, contradicting I contained in m.

The finite C-algebra B/(v-1)B has residue f=c at every maximal ideal. Multiplication by f-c cannot have a nonzero eigenvalue lambda: otherwise multiplication by f-c-lambda would be singular, so f-c-lambda would be a nonunit and would lie in a maximal ideal. Its residue there is -lambda, a contradiction. Here a multiplication operator is invertible exactly when its multiplying element is a unit; if the operator is bijective, its preimage of 1 is the inverse element. All residue fields equal C because they are finite extensions of the algebraically closed field C. Thus every eigenvalue of multiplication by f-c is zero, and this operator is nilpotent.

Choose an O-basis of B and let H(v,Y) in O[Y] be the monic characteristic polynomial of multiplication by f. Its degree is d=[L:C(v)] and its specialization is

\[
 H(1,Y)=(Y-c)^d.
\]

Cayley--Hamilton for this multiplication operator, applied to 1 in B, gives H(v,f)=0. Clear its finitely many rational coefficient denominators by a common polynomial a(v) with a(1) nonzero, which is possible since every coefficient belongs to O. Then Q=a H has exactly (A3). QED.

The commutative-algebra inputs here are standard statements, not new findings. Exact primary references personally opened/read on 21 November 2026:

- [Stacks Lemma10.161.8, tag032L](https://stacks.math.columbia.edu/tag/032L): finite normalization over a Noetherian normal domain in a finite separable extension.
- [Stacks Lemma15.22.11(3), tag0AUW](https://stacks.math.columbia.edu/tag/0AUW): finite torsion-free modules over a PID are free.
- [Stacks Lemma10.36.17, tag00GQ](https://stacks.math.columbia.edu/tag/00GQ): lying over.
- [Stacks Lemma10.119.7, tag00PD](https://stacks.math.columbia.edu/tag/00PD): the DVR criterion.

The proof supplies their specific application, including why the scalar function is integral and why the multiplication operator has the required reduction. It does not assert that a particular analytic branch is selected by normalization.

## 3. The all-places inserted-trace principle

**Theorem A4.** Let L/C(v) be a finite coefficient field, b>1, f in L, W a finite-dimensional complex vector space, F_0 an invertible endomorphism of W, and X_0 any endomorphism. Suppose selected regular evaluations of this same algebraic element satisfy

\[
 f_{b^n}=\operatorname{Tr}(X_0F_0^n)
\]

for every sufficiently large integer n. If f is regular at every place of L over v=1 and has the common residue c there, then

\[
 c=\operatorname{Tr}X_0.
 \tag{A4}
\]

**Proof.** Choose Q by Lemma A3. At the selected points, Q(b^n,Tr(X_0F_0^n))=0 for every sufficiently large n. Lemma A1 gives Q(1,Tr X_0)=0. By (A3), this equals a(1)(Tr X_0-c)^d. Its nonzero leading scalar forces (A4). QED.

No positivity, common radius, integral weight, or commutation assumption appears. Unlike F54's genuine-spectrum classification, this theorem uses the strong all-places regularity hypothesis directly.

## 4. Application to the actual marked element

Let F(v) be an algebraic matrix family on the actual rank-64 module, with invertible base F_b and selected regular evaluations. Let X(v) be the actual marked central operator from F54, and suppose

\[
 \operatorname{Tr}(X_{b^n}F_{b^n})
      =\operatorname{Tr}(X_bF_b^n)
\]

for all sufficiently large n. Assume F is regular on the actual pulled-back lattice at every coefficient-field place over v=1. The actual matrix identity X(1)=0 makes

\[
 f(v)=\operatorname{Tr}(X(v)F(v))
\]

regular with residue zero at every such place. Theorem A4 therefore forces Tr X_b=0. But the actual marked sector has rank eight and X_b acts there by Delta(b), so

\[
 \operatorname{Tr}X_b=8\Delta(b)\ne0
 \qquad(b>1).
\]

This is a contradiction.

**Strengthened conclusion.** The all-places marked trace law is impossible even if the matrix family is not assumed to commute with the actual right action, even at the base. Invertibility is required only for F_b in this argument; one still needs the stated regular evaluations and all-places regularity to formulate the comparison. No full-centralizer identification or global-basis assertion is used.

The original positive one-place construction remains an exception to this stronger theorem's regularity hypothesis: its operator has poles at t=+1. The proof does not affect its actual right-action compatibility, which is a separately verified positive property of that construction.

For a nilpotent rather than zero specialization of X, one must still check that Tr(XF) specializes to zero; commutation would be one sufficient condition. The new argument does not silently drop that requirement.

## 5. Finite virtual traces and exact scope

If the prescribed sequence is a finite alternating trace

\[
 S_n=\sum_j(-1)^j\operatorname{Tr}(X_jF_j^n)
\]

with all F_j invertible, put F_0=direct sum F_j and X_0=direct sum (-1)^j X_j. Theorem A4 gives the common residue

\[
 c=\sum_j(-1)^j\operatorname{Tr}X_j.
\]

Thus zero residue at every place excludes any such virtual comparison with nonzero zeroth inserted trace. If that zeroth trace is zero, this particular obstruction says nothing. It does not convert a virtual trace into a genuine positive spectrum.

Invertibility of the base operator matters: F_0=0 and X_0=I on a nonzero space give S_n=0 for all n>=1 but S_0=dim W. The regular function f=0 would then be an immediate exception. Actual finite Weil spaces have invertible Frobenius, so the intended arithmetic application has the needed hypothesis.

## 6. Separate Grothendieck dictionary

The normalization B is a finite locally free O-algebra, and multiplication by f is an actual O-linear endomorphism. Its characteristic polynomial records its nilpotent or scalar reduction on the special fiber. This is ordinary affine/coherent-module language within the EGA dictionary already cited in F55, with the exact finite-normalization and DVR module statements cited above.

The polynomial trace construction uses finite direct sums and tensor powers of the specified base endomorphisms. It is not a positivity theorem for an effective or gamma cone. The finite virtual extension uses the ordinary alternating trace of a bounded coefficient complex; it tests the zeroth inserted Euler trace without asserting that its sign or spectrum is effective.

All-places regularity remains an extra comparison between the algebraic coefficient family and the actual lattice. A continuous real branch is a separate condition, addressed by the parent's F55 Part3. No matrix-kernel, perverse category, or coefficient scheme alone is said to provide either condition.

## 7. Author check record

The finite tensor/direct-sum realization (A2), the backward recurrence, the localization/normalization step, the nilpotent multiplication reduction, the characteristic-polynomial specialization, and the actual rank-eight marked application were reconstructed directly. No numerical test is needed for these finite-dimensional algebra arguments.

This supplement awaits a fresh full independent review before integration. It does not modify any previously reviewed report or final fragment.

