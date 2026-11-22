# Independent audit of D-HES-01–03

**Result:** the complete mathematical argument and the finite certificates pass, **conditional exactly on the displayed proper-parabolic semisimple estimate (GM)**. This report does not verify that still-unread primary theorem or promote the all-rank conclusion to an unconditional theorem.

- Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, effort inherited/unexposed.
- Run: HODGE_DIVISION.
- Actual review: 2026-11-21, approximately 18:31–18:34 UTC.
- Complete draft read: `agents/imprimitive/lie_small_fields/higher_even_symplectic_draft.tex`.
- Reviewed SHA-256: `eb84630499dd1f4ec84d01735f4fc6b1988a979b037d3c92dff9ece66e7109d7`.
- Also read the complete exporter and arithmetic checker. No author arithmetic or selected-row list was imported by the independent check.

## Whole-proof checks

The degree floor is valid in every rank. Faithfulness of a nontrivial representation of the simple group makes its restriction to the embedded Sp10(2) nontrivial. The elementary abelian subgroup of GL_n(2) supplies all nonzero weights under its GL_(n−1)(2) normalizer, giving the second floor 2^(n−1)−1.

The elliptic semisimple argument is complete. Nonreciprocal primary summands are invariant isotropic subspaces, and a nonzero fixed summand contains an invariant isotropic line. For a self-reciprocal irreducible polynomial, the adjoint involution on E is its order-two Frobenius. The nondegenerate trace pairing defines the stated Hermitian form with the correct sesquilinearity and symmetry, including in characteristic two. Hermitian dimension at least two gives an isotropic E-line by norm surjectivity. Consequently every remaining primary occurs once and the exact symplectic centralizer is the product of norm-one groups. The resulting bound by 3^n and the displayed all-rank comparison with the degree floor are valid.

For odd prime order, every nonidentity power has the same invariant subspaces, so the same parabolic/elliptic alternative applies. The Fourier average bounds the 1-eigenspace by 8a/9; reality pairs every other eigenvalue with its distinct conjugate. Involutions are unipotent and have projective support at least a/8 from the separate 3/4 character estimate. Passing from an arbitrary nonidentity element to a nonidentity prime-order power has the correct inequality direction. The rank-four endpoint gives a/5 without (GM).

The full normalizer argument permits arbitrary factors and scalar actions. Trivial outer groups reduce factor-preserving operators to scalars times tensor products of core elements. The normalized maximum eigenspace does not increase under tensor convolution. A nontrivial factor permutation has the stated weighted-cycle bound of one quarter. The argument does not require transitivity of the factor set.

Reality of all core characters supplies the unique bilinear-form line, hence a similitude character on the whole inducing group. If that character were trivial, finite-order reciprocal eigenvalue pairing would make every trace real, contradicting inclusion of the original imaginary quadratic field in the inducing character field. At genus zero, generation and product one force at least two nontrivial multipliers; their fixed spaces are isotropic and cost half the total degree each.

The actual intermediate-cover factorization is used correctly. Genus at least two is impossible by the Euler formula, while genus one has fewer than nine parameters. At genus zero, an image of dimension nine requires at least twelve effective branch points. The resulting budget gives e≤54, contradicting e≥155 if any rank is at least five. If every factor has rank four, the stronger support bound gives e≤6, contradicting e≥35. No sufficiency claim is drawn from the branch dimension.

## Independent exact check

`audit_higher_even_symplectic.py` and its JSON output reconstruct the used finite arithmetic from the frozen original input, SHA-256 `9117f0b99643c2a44ea135db3435d29b8fa54a643a9aaa9d49071de31a1a45e8`.

- All 279 complete rows and 45,209 nonidentity entries in nontrivial rows checked.
- Sp8(2): minimum degree 35, maximum certified absolute character ratio 3/5, attained by −21 in degree 35.
- Sp10(2): minimum degree 155, maximum certified ratio 17/31, attained by −85 in degree 155.
- Exact character reality was independently checked by polynomial reduction against conjugation. Group orders, class-size sums, degree-square sums and trivial-row uniqueness also checked.
- The universal elliptic induction and all support/Hurwitz fractions were checked symbolically, with their genuine initial cases. This is not finite-to-infinite extrapolation.
- Actual runtime: **0.092672 seconds**, PASS.

The reviewer reused only their own previously written integer polynomial reducer. No sibling code, output scan or row selection was imported. The ATLAS tables themselves are published inputs, not newly derived classifications.

## Primary-source checks and exact remaining boundary

R. Gow, *Products of two involutions in classical groups of characteristic 2*, Journal of Algebra 71 (1981), 583–591: the theorem and its explicit inverse-conjugacy consequence on p. 583 were freshly read, along with the complete §3 proof on pp. 589–591 and the invoked preceding lemma discussion, in the original article text at https://www.academia.edu/115642614/Products_of_two_involutions_in_classical_groups_of_characteristic_2 . This is the even-characteristic source; no odd-characteristic theorem was substituted.

M. Liebeck, *Character ratios for finite groups of Lie type, and applications*: the definitions on author p. 2 and complete Theorem 2.4 on pp. 3–4 were freshly read at https://www.ma.imperial.ac.uk/~mwl/princeton-survey-final.pdf . Its unipotent estimate is 3/4 for q≤4, while its nonunipotent estimate there is 19/20. These are kept distinct. This is the published research restatement actually read; Gluck's original 1995 proof was not newly retrieved in this audit.

D. Gluck and K. Magaard, *Absolute Fourth Moments and Finiteness of Linear Groups*: the complete relevant paragraph on author p. 25 explicitly states trivial outer group and trivial multiplier for Sp_(2n)(2), n≥4. It was freshly read at https://www.academia.edu/29518749/Absolute_Fourth_Moments_and_Finiteness_of_Linear_Groups . The paper's fourth-moment hypotheses are not applied to the inducing representations; only those unconditional group-structure facts are used. The earlier checked HHM multiplier classification remains a separate published input.

**Still unresolved:** Gluck–Magaard 1998, Theorem 3.1(b), must be read in its primary form (or an exact primary research restatement) before (GM) is accepted. A review or bibliographic record is not sufficient. No part of this audit closes that source-verification gap.
