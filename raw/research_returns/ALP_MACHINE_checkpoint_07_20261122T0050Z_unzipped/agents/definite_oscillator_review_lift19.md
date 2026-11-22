# Independent whole-proof review of ALP-LIFT-19

Reviewer: GPT-6 Astra Pro, ALP_MACHINE `/root/definite_oscillator`.
Inherited reasoning effort is not separately exposed. Review completed
21 November 2026 UTC, after the author's whole-proof PASS at 23:49:36.

**Verdict: PASS in the stated local theorem and conditional global scope.**
I read the complete final `ramified_column_type_chain.md`, including its
certificate and scope sections. I separately opened the primary
Casselman Proposition 2.6, Zelevinsky Propositions 8.5–8.6, and
Mínguez Theorem 1(2), and checked the actual source `HX`, `SX`, `lamX`,
and the inverse adelic-type convention. This is a mathematical review,
not a Lean compilation or a check of the full source constructor.

## 1. Representation and character checks

The finite Steinberg copy gives an actual Iwahori-fixed vector: the
sum of its integral `u e` basis is nonzero and is fixed by both the
upper unipotent group and the diagonal torus. Casselman's result
therefore places the initial irreducible representation inside an
unramified principal series. Every segment of its cuspidal support
is consequently on an unramified character line.

The newly inserted one-dimensional `GL_d` factors have support on
the distinct nontrivial residue-character lines of the actual stage
characters. No segment from different factors can be linked.
Zelevinsky Proposition 8.5 applies to irreducible factors, even
when the initial factor is neither tempered nor generic. Thus the
whole displayed normalized induction is irreducible. The conditional
unitarity claim is also correct.

In the Hom model the scalar is
`eta_j(det g)^(-1) eta_j(det h)`. With the literal bilinear input,
the type-II quotient on the source is `Pi_j^vee tensor eta_j`.
Mínguez's contragredient old block becomes `Pi_j tensor eta_j^(-1)`;
restoring the target scalar cancels that twist and gives the old
block plus `eta_j circ det_d`. This is the required sign. The
source's `levTyp = levChr^(-1)` gives the inverse generic character
and the determinant factors `eta_i`, exactly as in (T5).

## 2. Finite Mackey component and support

In the displayed coordinate order, the first `P_j` block consists
of `A,L_0,...,L_(j-1)`. Its intersection with the conjugated `Q`
parabolic has upper blocks of sizes `(k,1,...,1)`. Every `T_i`
diagonal block is unrestricted. Therefore the Levi image in (T12)
is exact and surjective.

The radical intersection acts trivially on the inducing coefficient:
the off-diagonal `Q` blocks are inflated trivially, and the only
within-block additions are upper unipotents inside a determinant
character. Extending functions by zero from `Q w P_j`, then taking
right radical invariants, consequently constructs an actual
submodule, not merely a constituent of a Mackey filtration.

The fully generic vector is obtained on the reversed-block open
unipotent orbit. Its stabilizer is the internal `U_k` and hence
its orbit has size `q^(k j+j(j-1)/2)`. For the omitted-root branch,
the vector is supported on `P_(k,j)` and only the longest flag
cell in its `GL_j` block contributes; its size is
`q^(j(j-1)/2)`. Both character transformation laws agree with
the literal `SX` branch.

I independently checked the radical defect by its actual matrix
positions. A root of the `P_j` radical fails the `Q` condition
exactly when its row is `L_l`, its column is in `T_i`, and `l>i`.
There are `t j(j-1)/2` such entries. Adding this to the preceding
orbit exponents gives precisely (T20). The finite induced-function
norm therefore has the support quotient and the Gaussian
multinomial denominator in (T22), with no extra unipotent factor.

## 3. Primitive lattice and norm checks

The vector `sum_u psi(u) u e` is primitive in the integral Steinberg
basis. Expanding `e` in flags cancels every Weyl cell other than the
longest: a non-longest Weyl element has a simple positive root in
its stabilizer, and the generic character is nontrivial there.
The remaining `|U_k|` flags are distinct, with unit coefficients.
Thus its squared flag norm is exactly `q^(k(k-1)/2)`. This proof
does not make the erroneous assertion that the full `u e` basis
is orthonormal.

All the support extensions use only the actual group action and
roots of unity, so the constructed finite induced vector remains
primitive. The isometric embedding of the finite Steinberg copy
in a unitary p-adic compact model may be chosen, but it does not
identify a global arithmetic lattice; the final text correctly
retains that distinction. The formula for the 11-adic valuation
of the Gaussian multinomial follows directly by collecting the
indices divisible by `ord_11(q)` and applying the elementary
lifting-the-exponent identity.

I reran the author's exact diagnostic after reading the proof.
It passed all 32,404 matrix-line covariance checks over `F_3` and
`F_5`, the 100 root-count configurations, and the 1,344 Gaussian
multinomial valuations. The generic multiplicity is one and the
omitted-root multiplicity is two in the stated small examples;
the proof needs existence only and makes no uniqueness claim.

## 4. Global scope

Section 7 now explicitly retains the rank-gap, selected real-type,
and angular-weight hypotheses of LIFT14. Adding the finitely many
ramified G places to its omitted set leaves the checked partial
Rallis product argument intact. At those split places Mínguez gives
local occurrence; at the other places the previous fixed tests are
unchanged. The compact-character projector argument is valid on
the actual generated previous theta image because finite group
translations are absorbed by Weil equivariance.

This proves availability of the specified nonterminal compact
types, not nonvanishing of the predetermined raw `PhiG`, `PhiGS`
or `Xi` operator. The terminal group, arithmetic image lattice,
later content and growth cost, original source-field wrappers,
and the six comparison identities remain separate. The transfer
to the degree-84 host is conditional on its own characters and
actual first extraction, as stated in the final draft.

## Exact primary and source locators read

- Casselman, W. (1980), *The unramified principal series of p-adic
  groups. I. The spherical function*, Proposition 2.6, printed
  p.396: https://numdam.org/item/CM_1980__40_3_387_0.pdf.
- Zelevinsky, A. V. (1980), *Induced representations of reductive
  p-adic groups. II. On irreducible representations of GL(n)*,
  Proposition 8.5, p.196, and Proposition 8.6, p.197:
  https://www.numdam.org/article/ASENS_1980_4_13_2_165_0.pdf.
- Mínguez, A. (2008), *Correspondance de Howe explicite: paires
  duales de type II*, Theorem 1(2), printed p.718:
  https://www.numdam.org/item/ASENS_2008_4_41_5_717_0.pdf.
- Recovered commit `7cbf7a0c32fca1badf05931879a37c3f8a2b03b4`,
  `Formalism/LocalToGlobal/Columns/RecLevel.lean`, lines 50–52;
  `GenericUnipotentCharacter.lean`, lines 437–452.
- The integral Steinberg and flag-norm inputs were directly read
  in the DO033 author check: Steinberg (1957), Theorems 1–2,
  pp.348–350; Geck (2015), Theorem 2.1 and Corollary 2.3.

