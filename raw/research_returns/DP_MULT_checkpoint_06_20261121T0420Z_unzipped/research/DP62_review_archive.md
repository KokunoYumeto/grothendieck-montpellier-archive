# DP62 independent complete proof review

Checker: `/root/archive_binomial`, GPT-6 Astra Pro; reasoning effort not exposed. Client date 2026-11-21 UTC. The complete nine-section memo was read at observed 04:05:07 and again 04:08:49; the entire intended theorem/proof and final scope paragraph were read during the same source-check sequence. Challenge closed at observed 04:09:40 UTC. **PASS** for the stated scope; no mathematical correction required.

## Exact reviewed versions

- Memo SHA256 `116c98a37c9f72055fe1fc3695cde05ce5c6d5230e959e85c22402e8c5b377a9`.
- Intended fragment SHA256 `9105aca7b772e610a73b729deccbdced3d2669b97047afd65eb42491b20a8262`.
- Complete theorem/proof block hash and actual main inclusion counts are in `late_proof_snapshots/DP62_archive_review_metadata.json`. Entire read snapshots are preserved there as `DP62_complete_archive_checked.md` and `DP62_integrated_archive_checked.tex`.

## Independent mathematical challenge

The odd normalization works over a general test scheme, including nonreduced schemes and residue characteristics dividing the level. The central identities are exact: from `iota(U)=c U^{-1}` and the fact that symmetry fixes scalars, one obtains `c^N=d^2`. For `a=c^{(N-1)/2}/d`, the identities `a^2 c=1` and `a^N d=1` give both required conditions. Replacing a local lift by `uU` replaces `a` by `u^{-1}a`, so the normalized lift is genuinely independent of a torsor trivialization. The construction descends and commutes with base change. Uniqueness uses the integer Bezout identity for 2 and odd N, which is valid for units over arbitrary rings. No root extraction, invertibility of N, or geometric-points-only argument is used. The N=1 edge is harmless. The result is correctly described as a torsor section; a group splitting is asserted only on a subgroup with trivial commutator.

The relative finite-flat argument applies at primes dividing N: fibrewise multiplication is finite flat, relative flatness follows from the stated fibre criterion, and proper finite fibres give finiteness. The noetherian base then supplies local finite presentation and hence finite local freeness. The degree is read on fibres and the kernel is its zero-section base change. A torsion point extends over the Dedekind good base by properness; finite presentation spreads each local extension to a neighborhood and separatedness makes the extensions agree. The normalized theta lift therefore extends over that same base. The fixed multiplication isomorphism and theta action take an integral base section to an integral individual translate. No assertion of primitivity at every good prime is silently added.

The canonical norm computation is also exact. Translation-invariant curvature scales by M squared under multiplication; after comparing the pullback and tensor metrics by the rigidified isomorphism, the logarithmic norm ratio is globally pluriharmonic on a compact connected complex torus and hence constant. Rigidification forces that constant to vanish. For a finite-order theta lift, its metric ratio is a positive constant, whose N-th power is one; it is therefore one. Supremum and Haar probability norms are preserved under the resulting isometry and surjective multiplication. These are canonical section norms, without an assertion about the source's local exponential gauge or differentiated coefficients.

The tuple-field bound uses the actual finite etale characteristic-zero scheme H to the r-th power. Each tuple's residue-field degree is at most its rank `M^(2gr)`. Uniqueness and base-change functoriality of the lift imply descent over exactly that point field. No full torsion splitting field or adjoining roots is required. Degree bounds do not imply discriminant bounds. The fragment correctly restricts the unramified-at-11 assertion to the DP59 family `M=29^e`; arbitrary odd M may be divisible by 11, while the integral normalization still holds.

## Primary source reading and exact locators

I directly opened and read Polishchuk's author version, *Analogue of Weil representation for abelian schemes*, Section 1, pp.4-5: the finite-flat Heisenberg and symmetric extension definitions, Proposition 1.2, and Corollary 1.3. These support the relative theta torsor and the known odd symmetric torsor triviality. The paper proves the explicit normalized formula for its combined integral application rather than claiming that formula was separately printed there. Primary URL: https://arxiv.org/pdf/alg-geom/9712021 .

I visually read the original Moret-Bailly Proposition II.2.1 on printed p.48 (PDF page51), from the saved original-page image. Its statement gives the unique smooth Hermitian metric for a cubical line and its equivalent characterization by compatible rigidification and invariant curvature. This new pixel read is distinguished from ABA-CE83, which had only read the later published de Jong-Shokrieh statement. Original PDF: https://www.numdam.org/item/AST_1985__129__1_0.pdf .

The three finite-flat Stacks statements were directly read in ABA-CE83. In the present review I also opened and read Lemma 29.43.1, Tag0BX5, and Lemma 29.43.5, Tag0BX7. The latter explicitly extends a map across a valuation-ring point of a Noetherian source when the target is proper. It gives an exact known-result locator for the Dedekind extension paragraph; I sent this small citation improvement to root and author. URLs: https://stacks.math.columbia.edu/tag/0BX5 and https://stacks.math.columbia.edu/tag/0BX7 .

The actual numbered source `ThetaPt.lean`36-92 was read, confirming `SymLift`44-51 and `IsActOf`83-84. These are the ranges already used correctly in DP62. A separate correction to the old DP59 citation ranges is recorded separately, preserving the history of that caught error.

## Scope preserved

The theorem establishes integral individual allowed translates, exact canonical section norms and polynomial tuple-field degree bounds. It supplies no discriminant estimate, no bad-prime norm bound, no equality with a source derivative/gauge norm, no full prescribed row sequence, no mixed-type moduli object and no membership in an iterated theta image. It does not establish a net chain-cost improvement. No Lean execution, numerical verification or TeX compilation is represented as part of this review.

## Exact extension-source precision delta

At04:15:37 the complete diffs adding Stacks0BX7/0BX5 and neighborhood gluing had been read twice. PASS; the rest of the proof is unchanged and both exact source statements were directly read inABA-CE85. Updated memoSHA e4cd20d25da75ec9213c13c0ca81a3c7d642b220b77dfa6252440912ab3ad6e6; fragmentSHA b9ab7cd1c005f08be2d0de862ec7204f900543abfe92c374dcbbab5de5f935ee; exact main count 1. This is a targeted delta, not a new whole proof review.
