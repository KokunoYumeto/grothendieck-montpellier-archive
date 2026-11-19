# Independent check of the singular-base genus-one torsor

**Verdict:** the proposed construction works, with the conclusion restricted
to failure of an automatic positive-degree relative divisor class. It does
not assert that the Brauer group is infinite. This check was performed by
the Part D agent independently of Part B's construction on November 19,
2026.

Let E be a smooth plane elliptic cubic over F_q with its rational origin,
T=P^2, and S=T_1 amalgamated with T_2 along E by the identity. The explicit
equation t(t-f_E)=0 in the total space of O_T(3) realizes this pushout as a
finite flat rank-two scheme over T. Locally its ring is the fibre product
of two copies of O_T over O_E. Set A=E times S.

The sheaf sequence

    0 -> A_S -> i_1* A_T + i_2* A_T -> i_E* A_E -> 0

on the small etale site is exact. The kernel statement is the universal
property of the closed pushout, which remains valid after etale base
change. Surjectivity can be checked at strict-henselian local rings: their
quotients by the component ideals are henselian, and a section of the
smooth group E over the intersection lifts across the associated closed
henselian pair.

Every morphism P^2 -> E is constant, so A(T)=E(F_q), whereas a morphism
E -> E is uniquely a translation followed by an origin-preserving
endomorphism. Thus A(E)/E(F_q)=End_{F_q}(E). The long exact sequence
injects this quotient into H^1_et(S,A). In particular alpha=delta(id_E)
has infinite order, since n times the identity endomorphism is nonzero
for every nonzero integer n, including integers divisible by the
characteristic.

For representability, glue X_i=E times T_i along E times E using
(x,t) -> (x+t,t). Both arrows from the gluing locus to the respective
components are closed immersions. Consequently **Stacks Lemma 37.67.8,
tag 0B7M**, gives a scheme pushout directly; no extra affine-neighborhood
hypothesis is needed in this two-closed-immersion case. **Lemma
37.67.9(4), tag 0CYY**, gives smoothness of the resulting X -> S from
smoothness of the component projections. Both full proofs were opened,
together with Proposition 37.67.3 (0E25) and its setup (0ECI).

Etale locally on S, smooth lifting supplies component translations whose
difference is the gluing cocycle, identifying X with E times S. The
pushout is compatible with this flat base change, either by the local
fibre-product exact sequence or by Stacks Lemma 37.67.7. Thus X -> S is
the A-torsor represented by alpha (possibly its negative according to
the boundary convention), and is a proper smooth genus-one scheme.
Properness can also be descended from its finite surjective proper
component cover after the separatedness statement in Lemma 37.67.4.

The relative Picard sheaf Pic^1 of a genus-one torsor has the same torsor
class, up to the conventional sign under E=E^vee. Its degree-d component
has class plus or minus d alpha. Any global line bundle of relative
degree d gives a section of that component and therefore kills d alpha.
Since alpha is of infinite order, d=0. The relative degree is one
constant integer because S is connected and X -> S is smooth proper.

Primary source URLs opened:

- https://stacks.math.columbia.edu/tag/0E25 (Proposition 37.67.3;
  Ferrand Theorem 7.1(iii) identified in the source).
- https://stacks.math.columbia.edu/tag/0ECI (Situation 37.67.1).
- https://stacks.math.columbia.edu/tag/0B7M (Lemma 37.67.8).
- https://stacks.math.columbia.edu/tag/0CYY (Lemma 37.67.9).
- https://stacks.math.columbia.edu/tag/0ECH (full section, including
  Lemmas 37.67.4 and 37.67.7).

Web retrieval references: turn690598149view0, turn521936493view0,
turn521936493view1, turn894865856view0, turn894865856view1.
