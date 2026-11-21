# F48 second supplement: mixed weights still cannot retain the full collision centralizer

Author: /root/gct_statements, GPT-6 Astra Pro; inherited effort not exposed. Date: 21 November 2026 UTC. Parent independently proposed the largest-cyclic-summand proof of the center lemma below and requested this extension. All new deductions are proved here. Independent review is requested.

The preceding single-weight obstruction can be strengthened if a rational spectral-retuning family is also required to retain the actual full centralizer at v=1. Under that additional requirement, allowing mixed weights does not suffice.

## C1. Rational power traces under spectral retuning

Fix b>1 real. Let F(v) be an invertible N-by-N matrix over C(v), regular and invertible at b and at all sufficiently large b^n. Suppose
\[
\operatorname{Spec}F(b^n)
 =\operatorname{Spec}(F(b)^n)
\tag{C1}
\]
as multisets for every sufficiently large integer n. No purity hypothesis is made.

**Lemma C2.** Every eigenvalue of F(b) is b^m for an integer m. If r_m is its positive integer multiplicity, then
\[
\operatorname{Tr}F(v)=\sum_m r_m v^m,\qquad
\det(TI-F(v))=\prod_m(T-v^m)^{r_m}.
\tag{C2}
\]
Only finitely many r_m are nonzero.

**Proof.** Put f(v)=Tr F(v). By (C1),
\[
f(b^n)=\sum_\alpha m_\alpha\alpha^n,
\]
where alpha ranges over distinct nonzero eigenvalues of F(b), and m_alpha is its positive integer multiplicity.

Here is the complete rational argument used in F26, specialized to this trace. The finite power sum satisfies a constant-coefficient recurrence
\[
\sum_{j=0}^{s} c_j f(b^{n+j})=0,\qquad c_0\ne0,
\]
because its characteristic roots alpha are nonzero. The rational function
\[
G(v)=\sum_{j=0}^{s}c_j f(b^jv)
\]
has infinitely many zeros v=b^n and hence is identically zero. Suppose f had a pole at a nonzero finite complex point rho of maximal modulus among its nonzero finite poles. For j at least one, a pole of f(b^jv) has the form sigma/b^j, with modulus strictly less than |rho|. Therefore only the nonzero term c_0 f(v) has a pole at rho, contradicting G=0. Thus f has poles only at zero and infinity and is a Laurent polynomial.

Write f(v)=sum_m a_m v^m. Its evaluations give
\[
\sum_m a_m(b^m)^n=\sum_\alpha m_\alpha\alpha^n
\]
for all sufficiently large n. Finite power sums with distinct nonzero roots are linearly independent: evaluating any claimed zero relation at s consecutive sufficiently large integers produces an invertible Vandermonde matrix, multiplied by a nonzero diagonal matrix of root powers. Consequently every alpha is b^m, and a_m is exactly the positive integer multiplicity of that root; all other coefficients vanish. This proves the trace identity.

At v=b^n, (C1) now gives the characteristic polynomial
\[
\prod_m(T-b^{mn})^{r_m}.
\]
Each coefficient agrees at infinitely many v=b^n with the corresponding coefficient of the rational polynomial in (C2), so those coefficients agree identically. QED.

The first equality is a positive Laurent trace because these are actual eigenvalue multiplicities. A virtual alternating trace may cancel roots and does not by itself support the same conclusion about all hidden eigenvalues.

## C3. The center of one-eigenvalue centralizers

Let k be a field and N_0 a nilpotent endomorphism of a nonzero finite-dimensional k-vector space V. Let s be its nilpotency index.

**Lemma C4.**
\[
Z\bigl(\operatorname{End}_{N_0}(V)\bigr)
       =k[N_0]\simeq k[t]/(t^s).
\tag{C3}
\]
In particular this center is local and has no nontrivial idempotents.

**Proof.** Regard V as a k[t]-module with t acting by N_0. Its nilpotent Jordan decomposition has the form
\[
V=\bigoplus_i M_{r_i},\qquad
M_r=k[t]/(t^r),\qquad \max_i r_i=s.
\]
Take a central element z of End_{k[t]}(V). Commuting with the projection onto each displayed cyclic summand forces z to be block diagonal. On M_{r_i} every k[t]-linear endomorphism is multiplication by some polynomial f_i modulo t^{r_i}.

Choose a largest summand M_s and let f modulo t^s be the restriction of z to it. For every other summand M_r, the quotient map M_s to M_r sending 1 to 1 is a k[t]-linear map. Insert it as an off-diagonal endomorphism of V. Commuting with this map forces f_i=f modulo t^r. This also handles multiple largest summands. Thus z is exactly the same polynomial f(N_0) on every block. Conversely every polynomial in N_0 commutes with its full centralizer. The largest summand ensures the kernel of k[t] to k[N_0] is exactly (t^s), proving (C3). QED.

This proof needs neither algebraic closure nor a semisimplicity assumption. Nilpotent Jordan blocks exist over every field.

## C5. The actual collision obstruction, with arbitrary mixed weights

Assume in addition to (C1) that F(v) is regular at v=1. Lemma C2 gives
\[
\det(TI-F(1))=(T-1)^N.
\tag{C4}
\]
In particular F(1) is automatically invertible and F(1)-I is nilpotent. Its full centralizer has local center by Lemma C4.

The actual rank-three collision algebra in F19 is
\[
A_1=k\times k\times M_2(k[\epsilon]/(\epsilon^2)).
\tag{C5}
\]
Its center is
\[
Z(A_1)=k\times k\times k[\epsilon]/(\epsilon^2),
\tag{C6}
\]
which has three nonzero primitive central idempotents and is not local. Therefore
\[
\operatorname{End}_{F(1)}(k^N)\not\simeq A_1
\tag{C7}
\]
for every auxiliary rank N.

This proves the following exact statement: no finite rational matrix family, regular at the collision parameter, can satisfy all-extension spectral retuning at one fixed b>1 and recover the actual full collision algebra as its full Frobenius centralizer. Mixed weights, eigenvalue permutations, arbitrary Jordan blocks and a different auxiliary rank do not remove this obstruction.

The proof only needs the spectral rule, not a fixed-basis equality F(b^n)=F(b)^n. A rational change of basis that gives another regular matrix model at v=1 does not alter the characteristic-polynomial identity or the local-center conclusion. The theorem does require a finite fixed-rank regular matrix model; it does not cover a nonflat coherent object with a different special-fiber rank, a rational family with no regular finite extension at v=1, or recovery of A_1 merely as a specified subalgebra of a larger centralizer.

For the inverse convention v=Q^{-n/2}, apply the same proof to F(v^{-1}) with b=Q^{1/2}; inversion fixes the collision point v=1. No claim concerning an unlabeled multivalued algebraic parameter family is made.

## C8. Relation to the earlier constructions

This does not contradict F46. Its Cayley family is rational and retains the full algebra through collision, but it fails spectral retuning, as already explicitly proved there. It does not contradict F48's identity or finite-order tensor Frobenii: those retain the actual actions as specified subalgebras and are not full-centralizer identifications. It does not contradict a mixed-weight coefficient object attached separately to each word; the hypotheses concern one rational matrix family and its complete spectrum across extensions.

The single-weight obstruction in the first supplement acts already at a regular generic parameter because the actual algebra there is nonsimple and semisimple. The present obstruction instead uses the full collision algebra, requires regularity there, and needs no purity assumption. These are distinct conditional comparisons, each with an explicit scope.

## Verification record

The author directly reconstructed the rational recurrence/pole argument, finite Vandermonde uniqueness, characteristic-polynomial identity, center-of-centralizer lemma and actual special-center comparison. No formal proof-kernel certificate, symbolic computation or new source theorem is claimed. F19 is the previously certified exact algebra input; the rational scalar lemma is reproved here to avoid relying on a search hit or a statement without context.
