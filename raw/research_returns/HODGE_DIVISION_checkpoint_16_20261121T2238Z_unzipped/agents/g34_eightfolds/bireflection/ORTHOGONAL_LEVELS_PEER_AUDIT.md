# Independent whole-proof audit of D-OL-01–03

**Outcome: PASS in the stated scope.** No mathematical repair is requested.

- Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, effort inherited/unexposed, run HODGE_DIVISION.
- Actual record time: **2026-11-21 20:37:49 UTC**.
- Complete reviewed file: `agents/imprimitive/orthogonal_levels/orthogonal_level_section.tex`.
- Frozen SHA-256: `889ddcc6a70b196139c30678ac6d4a72c8a11a4a58f85b33e53bdfe8df6b2ed9`.
- I read the whole proof, its bibliography, and the entire author arithmetic program. I independently reconstructed the displayed arithmetic in `audit_orthogonal_levels.py`; I did not import the author's checker, constants output, or polynomial helpers.

## What is proved, and what remains

The result gives a strict reduction for transitive ordinary orthogonal normal cores. Every factor which descends to the natural orthogonal group has character level below `10^30`. A genuinely spin factor, or a descended factor which does not extend to the special orthogonal group in odd characteristic, must have natural dimension below `2·10^30`. The remaining ordinary low-level natural dimension is **not** bounded here. No theta-constituent irreducibility, exhaustion theorem, full orthogonal extension, or solution of that residual gate is asserted.

The proof separately establishes a mixed-core degree obstruction: if every factor has degree at least `q^(M0 d)`, with `M0=2·10^29`, arbitrary compatible normalizers have projective support at least `3/16` of the full degree. The actual intermediate Hurwitz factorization then contradicts period rank nine. The transition to a bound on one factor uses transitivity and equality of factor degrees, without claiming that level itself is invariant under outer automorphisms.

## Published inputs independently checked

The full **published** Guralnick–Larsen–Tiep article is the 60-page Springer PDF, *Inventiones mathematicae* 235 (2024), 151–210, DOI `10.1007/s00222-023-01221-5`:

https://link.springer.com/content/pdf/10.1007/s00222-023-01221-5.pdf

The retained PDF has SHA-256 `ad6f1d3bf9e0acc60220f9098033513b521f96668967002914da7d5a91ced957`. I freshly read Definition 3.2(ii), Lemmas 3.3–3.4 and their complete proofs on pp.160–161; Theorem 3.7 and its complete proof on pp.165–167; Theorem 1.5(iii), p.154, and its complete proof on p.167; Proposition 6.3 and its complete proof on pp.193–194; and Proposition 7.3 and its complete proof on pp.198–200. The exact formulae and all ordinary-character, parity, dimension and inflation hypotheses match their uses in OL. Source pagination is distinguished from the separately retained 49-page author version.

The Larsen–Tiep input was freshly reopened at:

https://arxiv.org/pdf/2403.09046

This is the accepted author version of the published Annals article, not a claimed retrieval of the journal PDF. I reread the entire Theorem 5.5 proof, author pp.25–26, including the explicit constant `1/(6507·2^21·10^18)>7·10^−29`, and the spin-support convention immediately before Proposition 6.4 on author p.30. Theorem 5.5 explicitly includes both `Omega` and, in odd characteristic, `Spin`. The earlier complete reading of Theorem 4.4 and its constant derivation in the UNW/LNW audit remains a separate recorded check.

HHM Chapter 5, Table 1 and the complete preceding exceptional-cover discussion, p.35, were freshly reread during the immediately adjacent HOS07–10 audit. There are no exceptional orthogonal multipliers at the natural dimensions used by OL. The cover and natural-image arguments in OL are written separately from that classification input. The underlying published classification and Deligne–Lusztig constructions have not been independently reproved in this audit.

## Whole mathematical proof checks

### D-OL-01

The level is exactly the least exponent of the specified natural permutation-character combination. On the groups in question the two characters coincide, as Lemma 3.3 states. The sharper range `ell≤floor(d/2)` therefore applies. The degree upper bound is the actual published constituent-degree bound, and the lower bound is the contrapositive of Theorem 3.7 with `k=ceil(ell/3)`. Its exceptional low-dimensional cases are absent at `d≥50`.

For odd-dimensional spin groups, failure to descend means nontriviality on the full center of order two, which gives the faithfulness required by Proposition 6.3(i). For even-dimensional spin groups, Proposition 6.3(ii) directly assumes noninflation; no unsupported faithfulness on an entire noncyclic center is inserted.

The cyclic quotient `SO/Omega` has order two in the stated odd-characteristic range. An invariant irreducible character extends by rescaling an intertwiner. A character which does not extend consequently induces irreducibly with degree `2a`, so Proposition 7.3 has precisely its required reducible-restriction hypothesis. Dividing its two estimates by two yields the stated weaker common exponent. I checked all four exponent reductions; the gaps are `m/2+1/8`, `0`, `9/8`, and `0`.

### D-OL-02

A noncentral covering-group element has positive natural projective support. In the spin case, a natural scalar image would give scalar commutators in the covering kernel; perfectness forces these commutators to be trivial. Thus that element would itself be central. This justifies using support at least one in the uniform character bound.

The product `sigma0·M0=2` gives character ratio at most `q^−2≤1/4`. The normalizer commutator is an actual core operator; nonidentity scalar commutators have full moving rank and require no noncentral character bound. In the nonscalar case the trace inequality gives moving rank at least `3a/8`, and the commutator-rank inequality then gives normalizer support at least `3a/16`. Perfectness is used only where specified, not as an unproved restriction on the normalizer.

The factorwise eigenvalue convolution and weighted tensor-cycle proof cover every compatible scalar, outer, and factor-permuting operator. A nontrivial cycle has support at least one quarter, which is stronger than the common bound. The finite-order normalization of individual return operators is justified by the finite projective order of the full operator.

The geometric step uses the actual polarized Shapiro variation on the intermediate quotient curve and a finite Hurwitz cover of its pointed moduli. It correctly excludes positive genus and forces at least twelve genuine branch points. Scalar inertias are handled by their full ordinary moving rank. The source inequality is `2e+6≥9e/4`, so `e≤24`, contradicting the factor-degree premise. No dimension inequality is treated as sufficient for dominance.

The final transitive consequence uses equality of all factor degrees and the same orthogonal parameters in the stated large-dimensional range. It does not need a Galois or automorphism invariance assertion for the level.

### D-OL-03

If `ell≥J0`, its range gives `d≥2J0≥50`. The exact chain

`k≥ell/3`, `k≤d/6+2/3`, and `d−2k−2≥3d/5`

implies `a≥q^(d ell/5)≥q^(M0 d)`, contradicting the preceding strict degree bound. No sign reversal occurs because all multiplied quantities are positive.

At `d=2J0+s`, the difference between the spin/extension exponent and `M0 d` is exactly the displayed quadratic. After writing `J0=10+t`, every coefficient is positive, including the constant `3`. Thus both failures force a forbidden factor degree for every claimed dimension. In even characteristic the argument asserts only the already-ordinary covering behavior and does not apply the odd-characteristic extension proposition.

## Independent exact arithmetic

The actual independent run passed in **0.044676667006569915 seconds**. It checks the four source-exponent gaps, the full symbolic barrier polynomial and coefficientwise positivity after a shift, the universal level-inequality algebra, 21,900 finite boundary pairs plus the explicit enormous threshold residues, and all trace/normalizer/period constants. These computations supplement the universal written proof. They do not enumerate finite groups or certify the published classification inputs.

The first auditor run used raw SymPy structural equality to compare an expanded polynomial with an unexpanded equivalent expression. That implementation assertion failed before any mathematical inequality was tested. I replaced it with exact expansion of the difference; the corrected full run passes. This auditor-only failure is retained in `audit_orthogonal_levels_attempts.json`. No author proof or source assertion was changed.

TeX displays and proof environments were checked for balance. No TeX compilation is claimed.
