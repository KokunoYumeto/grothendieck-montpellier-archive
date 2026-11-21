# A18: eliminating the elliptic exception with geometric primitive rank zero

Date: 2026-11-21. Author/checker: GPT-6 Astra Pro; effort not exposed;
/root/effective_galois.

Source: A18_GEOMETRIC_PRIMITIVE_BRIDGE.tex.
SHA256: 7572851088b7de775866d879da61ec47ebfff65d40c5524578eaa72232deecd1.

## Outcome

The complete author recheck passes. The sibling agent /root/gt_certificates
reported an independent complete-proof read PASS at the same SHA256, including
the all-genus extension and the genus-two rational-plus-nonordinary refinement.
The parent is independently reviewing the full source.

The result strictly removes the bielliptic qualification from the geometric
primitive-rank-zero criterion in characteristic two. It applies to every genus
at least two. The genus-two theta-orbit criterion thereby applies also to
ordinary bases with a separable elliptic double quotient.

## Proof checks

The projector function has degree 2^omega(n), with simple zeros and poles
on two disjoint odd deck orbits. This part is independent of base genus.
The Castelnuovo–Severi induction and n>(2^omega(n)-1)^2 still exclude
the whole function field because g(D)=n(g(C)-1)+1>=n+1. The intermediate
field has power-of-two residual degree. The faithful/free odd deck action,
small genus bound, reduced fibre and two-orbit support force a degree-two
map to a genus-one curve, exactly as in A15.

The quadratic involution commutes with the cyclic odd deck group. Their
product acts faithfully, so the total function-field extension over the
quotient is Galois of degree 2n. Its two complementary fixed fields have
degrees two and n, trivial intersection over the common base and full
compositum. Thus D is the actual connected smooth fibre product C×_E Z.
The same argument works for every intermediate cyclic degree m dividing n.

The degree-m maps Z_m→E are étale maps of genus-one curves and become
odd isogenies after choosing origins. Their 2-primary Tate modules, hence
their geometric 2-ranks, agree.

Riemann–Hurwitz forces positive different for the separable quadratic map
C→E. If it has r geometric ramification points, r>=1. Its pullback through
an étale degree-m map has exactly mr ramification points. The
Deuring–Shafarevich formula therefore gives
f(D_m)=2f(E)-1+mr. This counts ramification points, not different degree.
In genus two only, different degree two forces r=1.

For V=T2(J_D) tensor Q2, odd pullback/norm identifies the subgroup invariants
with T2(J_Dm) tensor Q2. The cyclic conductor decomposition gives
f(D_m)=sum_{d|m}w_d. The projector A has nonzero eigenvalue exactly at
primitive characters, so f(P_n)=w_n. Möbius inversion gives
f(P_n)=r*phi(n)>0 for n>1, contradicting geometric rank zero.
No dimension-one cohomology eigenspace assumption is used in this all-genus step.

For genus two the entire new factor has rank n-1 and dimension n-1, hence
is ordinary. Thus rational primitive 2-primary group zero together with
nonordinarity of the primitive factor also suffices. Rational vanishing alone
does not produce the contradiction and retains the original qualification.

## Inputs and limits

The exact Castelnuovo–Severi and Deuring–Shafarevich locators are those already
opened and checked in A15_A16_independent_audit.md:
Poonen 2007 Proposition 2.1, Lemma 2.2, Corollary 2.3, author p.3;
Anbar–Beelen–Nguyen Theorem 1, equation (1), author p.3.

The point-section collision-to-lifted-2-primary-class reduction is the same
proved covering formulation used in A11 and A15.
The theta-orbit incidence criterion remains genus-two-specific. A18 does
not assert that every curve has a primitive-rank-zero odd cyclic cover.
No GRH or number-field analytic assumption enters the proof.
