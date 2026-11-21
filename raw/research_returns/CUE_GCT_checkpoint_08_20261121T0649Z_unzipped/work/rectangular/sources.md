# Rectangular bridge: sources and exact locators

All new R statements are deductions made and checked in this run; no claim
of priority over the literature is made. The older numerical formulas
are explicitly credited. Attached LaTeX was read directly, not inferred
from the prompt summary.

## R-B01 — Bump–Gamburd rectangular product identity

Bump, D., & Gamburd, A. (2006). On the averages of characteristic
polynomials from classical groups. *Communications in Mathematical
Physics, 265*, 227–274. https://doi.org/10.1007/s00220-006-1503-1

Exact locator: §3.1, Proposition 4, equation source label `e:produ`;
theorem label `cpaverage`. Attached source
`LIT_Bump_Gamburd_averages_of_characteristic_polynomials/acp20.tex`,
lines 994–1039. General parameters are `N,L,K`; the polynomial is
`s_(N^L)` in `K+L` variables. This supports R-01.

## R-B02 — Bump–Gamburd swaps and ratios

Same work. Exact locators: §2.3, Lemma 1 (`lem:min1`), §3.1,
Proposition 4 (`cpaverage`), and §4 (`comf`) for rectangular Weyl
coset/Laplace sums. §3.3, Theorem 3 (`t:1`), equation `unitaryratio`
for inverse characteristic-polynomial ratios, with `N≥Q,R` and
the denominator parameters of modulus less than one. The specialization
`K=L=0,Q=R=n²` used in R-09 is within those hypotheses when `N≥n²`.
Attached source lines 1539–1563 and 1650–1735.

## R-B03 — Finite CUE moments, hook content, Schur orthogonality

Same work. §3.1, Corollary 1 (`ratioskeatingsnaith`), equation
`ksformula`; §2.2, equations `ratiosschurorthog` and `e_hhl`.
Finite moment equals the rectangular representation dimension;
the leading asymptotic coefficient need not be an integer.

## R-B04 — Arithmetic CFKRS status and swap formula

Conrey, J. B., Farmer, D. W., Keating, J. P., Rubinstein, M. O., &
Snaith, N. C. (2005). Integral moments of L-functions. *Proceedings
of the London Mathematical Society, 91*(1), 33–104.
https://doi.org/10.1112/S0024611504015175

Version matching attachment: arXiv:math/0206018v3 (2005),
https://arxiv.org/pdf/math/0206018 . Exact locators: Conjecture 1.5.1
(`thm:zeta2kconjecture`), Theorem 1.5.2 (`thm:UN2k`), §2.1 recipe,
§2.2 equation `conj:M`, Lemma 2.5.1 (`thm:concisesumunitary`).
The author's older PDF at Waterloo is v1 and uses different section
numbers; do not cite its §3.2 as if it matched the attached §2.5.
The statements are checked as conjecture versus theorem, not assumed
proved from RH.

## R-B05 — Schur–Weyl and exact projectors

Collins, B., & Śniady, P. (2006). Integration with respect to the
Haar measure on unitary, orthogonal and symplectic group.
*Communications in Mathematical Physics, 264*(3), 773–795.
https://doi.org/10.1007/s00220-006-1554-3

Primary source: https://arxiv.org/pdf/math-ph/0402073 . Exact locators:
Theorem 2.1 (Schur–Weyl duality), equation (3) and the central
idempotents preceding equation (4), Proposition 2.2 (Haar conditional
expectation as orthogonal projection).

## R-B06 — Weingarten calculus with small-dimension correction

Same work: Proposition 2.3, equation (9), includes the necessary
`ell(lambda)≤dimension` cutoff; Corollary 2.4, equation (11), is the
entry integration formula. The example after Proposition 2.5 gives
the negative transposition value `−1/[N(N²−1)]`. No unrestricted
stable Weingarten inverse is substituted at singular small dimensions.

## R-B07 — Rains theorem

Rains, E. M. (2003). Images of eigenvalue distributions under power
maps. *Probability Theory and Related Fields, 125*(4), 522–538.
https://doi.org/10.1007/s00440-002-0250-2

Primary source: https://arxiv.org/pdf/math/0008079 . Exact locators:
Theorem 1.3, equation (8), and Corollary 1.4. They describe one
power's eigenvalue law. They do not assert independence of different
powers of the same matrix.

## R-B08 — GCT multiplicity criterion and rectangular obstruction limit

Ikenmeyer, C., & Panova, G. (2017). Rectangular Kronecker coefficients
and plethysms in geometric complexity theory. *Advances in Mathematics,
319*, 40–66. https://doi.org/10.1016/j.aim.2017.08.024

Primary source: https://arxiv.org/pdf/1512.03798 (v2); exact locators:
Theorem 1.4 (`thm:strategy`), equations (1.3) and (1.5),
Theorem 1.6 (`thm:together`), and Theorem 2.1 (`thm:manivel_rect`).
Theorem 1.6 requires `n>3m^4`. Source hard-coded cross-references
occasionally refer to earlier numbering, so numerical locators were
confirmed against the rendered primary PDF.

## R-B09 — Orbit versus closure and no occurrence obstructions

Bürgisser, P., Ikenmeyer, C., & Panova, G. (2019). No occurrence
obstructions in geometric complexity theory. *Journal of the American
Mathematical Society, 32*(1), 163–193.
https://doi.org/10.1090/jams/908

Primary source matching attachment: https://arxiv.org/pdf/1604.06431v3 .
Exact locators: Theorem 1.4 (`th:main`), `n≥m^25`; §1(b), paragraphs
defining the GCT coefficients and bounding them by the symmetric
rectangular Kronecker coefficient of the orbit, then by the ordinary
rectangular coefficient. The old v1 theorem number 1.5 must not be
silently used for the supplied v3 source.

## R-B10 — Known stable numerical positivity

Manivel, L. (2011). On rectangular Kronecker coefficients. *Journal
of Algebraic Combinatorics, 33*, 153–162.
https://arxiv.org/abs/0907.3351

Primary PDF: https://arxiv.org/pdf/0907.3351 . Exact locators:
Theorem 1(2); §3.3, Corollary 2(1), which explicitly states that for
`d≥q`, `g((nd−q,q),(d^n),(d^n))` is the number of partitions of `q`
into parts between 2 and n. §3.4 gives a birational flag-quotient
interpretation. R-07 credits this numerical identity and proves
explicit centered-polynomial witnesses and their orbit-closure
survival, rather than claiming a new count.

## R-B11 — GCT IV: proved two-row rule, its exact rectangular specialization, and limits

Blasiak, J., Mulmuley, K. D., & Sohoni, M. (2015). *Geometric complexity theory IV: Nonstandard quantum group for the Kronecker problem*. Memoirs of the American Mathematical Society, 235(1109). https://doi.org/10.1090/memo/1109

The supplied file is the later three-author `Apr13KroneckerGCT4.tex`, not the original two-author March 2007 version cited by the older GCT VII/VIII manuscripts. Matching author PDF: https://websites.umich.edu/~jblasiak/Apr13KroneckerGCT4.pdf . Page and theorem numbers below are for that Apr13 manuscript.

- Exact attached file: `sources/LIT_Mulmuley_GCT_IV_nonstandard_quantum_group_Kronecker/Apr13KroneckerGCT4.tex`.
- §12.1, theorem source label `t nonstandard schur-weyl duality`, source lines 4236–4290: nonstandard Schur–Weyl duality proved for general dimensions. This established structural theorem should be distinguished from the later two-row limitation on explicit canonical bases.
- Theorem 15.21, especially (vii)–(viii), manuscript p.102, label `t main canonical basis`, source lines 5963–5978: highest-weight counting rule for two-row Kronecker coefficients and its symmetric/exterior refinement. The two-row restriction means both *inner* GL partitions have length at most two; the outer partition may have four rows.
- Theorem 18.2, manuscript pp.124–125, label `t consequence for Kronecker`; equation (163), label `e g = invariant-free g`: constructive positive two-row rule from five types of invariant-free components, each zero or one.
- Corollary 18.4, manuscript p.127, label `c kronecker generating function sym ext`, source lines 7736 onward; introduction equivalent equation `e intro Kronecker generating function`, lines 1435–1455: symmetric/exterior generating functions. Taking the constant coefficient gives the all-even/four-odd-part formula recorded as R-10. The numerical formula is known; our work specializes and compares it with the closure ring.
- Example 17.8, manuscript p.122, label `ex not positive`, source lines 7326–7351: a divided-power matrix coefficient has mixed Laurent signs, namely `q^10-q^4-q^-4+q^-10`. The source first states that no global sign readjustment makes every specified Chevalley matrix coefficient nonnegative. The displayed algebraic identity was separately recomputed in `check_n2_formulas.py`.
- Conjecture 19.1, §19.1, label `cj canonical basis X^r`, lines 7920–7967: proposed compatible basis for the full tensor power. §19.2, source lines 8191–8209: naive extension can have too small a dimension; it has not supplied the general positive rule. Intro §1.1, source lines 893–903, explicitly describes the unresolved cases.
- R-10 gives a direct principal-minor highest-weight proof of the classical identity `Sym^d(Sym^2 C^s)=direct_sum S_(2mu) C^s`, so no unverified book exercise number is used for that identity.

## R-B12 — GCT VII: proved structure versus conjectural plethysm reciprocity

Mulmuley, K. D. (2008a). *Geometric complexity theory VII: Nonstandard quantum group for the plethysm problem* (revised extended abstract; arXiv:0709.0749v2; original Technical Report TR-2007-14, 2007). https://arxiv.org/abs/0709.0749v2

- Exact attached file: `sources/LIT_Mulmuley_GCT_VII_nonstandard_quantum_group_plethysm/main.tex`.
- Introduction, source lines 212–229, Theorem 1.2, label `tnonstd`: existence of the nonstandard quantization, complete reducibility, and quantum Peter–Weyl theorem.
- Introduction, lines 257–285, Conjecture 1.3, label `cduality`: nonstandard duality. Lines 290–305, Conjecture 1.4, label `creciprocity`: nonstandard reciprocity. §6, Conjecture 6.1, label `crecirefined`: refined specialization statement.
- Introduction, lines 309–335: conditional positive decomposition into `m_lambda^alpha n_pi^alpha` and the two subproblems P1/P2. Lines 336–366 explicitly state that algorithm correctness and the required canonical-basis properties are not proved in this source.
- Abstract and introduction distinguish this proposed positive plethysm formula from already established existence and complete reducibility. Latest attached arXiv version is v2, September 1, 2008; the first version is September 5, 2007.

## R-B13 — GCT VIII: precise conjectural positivity and finite-field RH language

Mulmuley, K. D. (2008b). *Geometric complexity theory VIII: On canonical bases for the nonstandard quantum groups* (revised extended abstract; arXiv:0709.0751v2; original Technical Report TR-2007-15, 2007). https://arxiv.org/abs/0709.0751v2

- Exact attached file: `sources/LIT_Mulmuley_GCT_VIII_canonical_bases_nonstandard_quantum_groups/main.tex`. Primary HTML for this version: https://arxiv.org/html/0709.0751v2 .
- Abstract, lines 144–159, and Introduction, lines 195–218: algorithms are explicitly called conjecturally correct; required properties are also conjectural.
- §2.2, Conjecture 2.2, label `clocalcrystalb`, lines 634–655: local crystal basis existence.
- §2.3, Conjecture 2.5, label `cuniquemindegleft`, lines 947–952: unique minimum degree complexity required for globalization.
- §2.4.1, Conjecture 2.6, label `ccelldecompleft`, lines 1041–1046: cellular decomposition compatible with the restricted standard quantum group.
- §2.4.2, Conjecture 2.7, label `cposkroneckerleft`, lines 1073–1090: Kronecker positivity, with the precisely stated sign and `(q-q^-1)^a` factors allowed for structure constants. The following paragraph defines positive coefficients to mean nonnegative **rational** coefficients.
- §2.4.3, Conjectures 2.8–2.9, labels `cnonstdposleft0` and `cnonstdposleft1`, lines 1151–1214: weaker general saturation and nonstandard almost-positivity claims; not an established nonnegative integer tableau count.
- §3.3, Conjectures 3.1–3.2, labels `cunimindegright`, `cunimindegright2`; §3.4.1, Conjecture 3.3, label `ccelldecompright`; §3.5, Conjecture 3.4, label `cposkroneckerright`; §3.5.1, Conjectures 3.5–3.6, labels `cnonstdposright`, `cnonstdposright1`; §3.5.2, Conjecture 3.7, label `coppquasicell`.
- §6, label `scomplexity`, lines 2810–2854: efficient combinatorial labels and crystal operations needed for a #P rule are additional proposed properties, with details deferred to a full version.
- Introduction, lines 238–247, and §2.4.2, lines 1118–1126: perverse-sheaf theory and the finite-field Riemann-hypothesis machinery are invoked as a prospective extension needed for nonflat, noncommutative varieties. These passages supply no implication from the classical analytic RH or Dirichlet GRH to the stated algebraic conjectures.
- Exact theorem/conjecture numbers were checked against the shared TeX theorem counter; principal positivity and complexity locators were also matched to the primary HTML. No full independent proof of these background quantum-group constructions is claimed.

## R-B14 — Cubic surfaces and the small-degree four-row exclusion

Beauville, A. (2000). Determinantal hypersurfaces. *Michigan Mathematical Journal, 48*, 39–64. https://math.univ-cotedazur.fr/u/beauvill/pubs/det.pdf

- Corollary 6.4, printed pp.52–53 (PDF pages 14–15): over an **algebraically closed** field, every **smooth cubic surface** admits a `3×3` linear determinantal equation. Its additional count of 72 representations is not needed for R-11.
- Corollary 6.5, printed p.53, states the extra twisted-cubic/birationality/six-lines conditions over a field that need not be algebraically closed. R-11 works over C and does not assert the unrestricted statement over other fields.
- §1.9, printed p.42, cross-references the plane-curve and cubic-surface statements and explains the dimensional boundary for generic hypersurfaces.
- R-11 uses Corollary 6.4 only for smooth quaternary cubics, then proves density, block-diagonal padding, linear-substitution closure, and highest-weight ideal containment. It does not claim that every singular cubic itself is a linear determinant; membership in the closure is sufficient.

## R-B15 — Dual Jacobi–Trudi identity used in the simultaneous Fourier proof

Sawin, W. (2020). A representation theory approach to integral moments of L-functions over function fields. *Algebra & Number Theory, 14*(4), 867–906. https://doi.org/10.2140/ant.2020.14.867

- Exact attached file: `sources/LIT_representation_theory_approach_to_moments_function_fields/main.tex`.
- Lemma 2.3, source label `representation-generating-identity`; equation source label `Jacobi-Trudi`, lines343–345. In arXiv:1810.01303v2 this is equation(2.4), printed p.12. The proof explicitly identifies the determinant of exterior powers with the conjugate-partition Schur character, citing Fulton–Harris Formula A6.
- R-16 uses only this unconditional classical identity, with three equal column lengths j, to identify the 3x3 Toeplitz determinant with `s_(3^j)`. The new nonvanishing specialization is then proved directly from the Weyl alternant and the distinct exponents in0..k<m.
- No cohomology-vanishing hypothesis or number-field/function-field transfer is invoked by R-16. The arithmetic parts of Sawin's paper are audited separately by the root/purity agents.
- Matching primary preprint: https://arxiv.org/pdf/1810.01303v2 . Published metadata also checked against the journal's primary PDF endpoint and author metadata.

## Web retrieval references retained for root citation verification

The root must reopen a subagent's web source before using a web citation.
The source URLs above are sufficient; retrieval ids are recorded only
for internal provenance.

- Rains PDF: `turn671720168view0`.
- Collins–Śniady PDF: `turn671720168view1`, targeted formula view
  `turn506510132view0`.
- Ikenmeyer–Panova PDF: `turn629217195view0`, stability passage
  `turn124126028view0`.
- Bürgisser–Ikenmeyer–Panova PDF: `turn629217195view1`.
- Manivel PDF: `turn407184572view0`, Corollary 2 passage
  `turn209001524view1`.
- CFKRS v3 PDF: `turn209001524view0`.

All cited mathematical assertions are either in the supplied sources
or these primary papers. Search snippets from secondary sites were
used only to locate the primary sources.

Additional primary retrieval locators used for R-10 onward:

- GCT IV matching Apr13 author PDF: `turn152986189view2`; Theorem15.21 `turn355908034view2`; Theorem18.2 `turn355908034view3`; Corollary18.4 `turn355908034view5`; Example17.8 `turn404862738view3`; Conjecture19.1 `turn404862738view4`.
- GCT VII v2 metadata: `turn152986189view0`; exact source TeX used for statements.
- GCT VIII v2 metadata `turn152986189view1`, primary HTML `turn404862738view1`; positivity `turn883730071view0`, complexity `turn883730071view2`, RH narrative `turn883730071view3`.
- Beauville Corollary6.4 author PDF: `turn998204997view0`.
- Sawin arXiv1810.01303v2: `turn745220849view2`; Lemma2.3/equation2.4 targeted view `turn887286787view0`.

## Cross-reference used in R-21: G-B10

Alpöge, L. (2026, November20). *Remark* [Supplied note and stipulated analytic input], printedp4, step13. Local PDF: `sources/ALPOGE_remark.pdf`; extraction `work/root/ALPOGE_remark.txt`, line192. The step reads “Bost slope inequality”; the R21 scope audit concerns this step, without re-auditing stipulated RH/Dirichlet-GRH. The complete bibliographic source is registered by root as G-B10, not duplicated under a new R-B identifier.

## R-22 source and derivation map

R-22 is a proved in-run deduction, with no priority claim. Its new local identities, finite parameter-grid selection, and uniform rank estimate are proved completely in r22_fragment.tex.

- R-15/R-17 provide the cyclic base differential dimension 2m^2+2; R-16 gives its exact two-column character quotient. These internal dependencies are stated explicitly in R22 paragraph3.
- R-B15 (Sawin2020, Lemma2.3, equation2.4/source label Jacobi-Trudi) is used only for the unconditional dual Jacobi–Trudi identity in R22 equation R22:schur. Nonvanishing of the geometric specialization is proved directly by the Weyl alternant, rather than imported from an arithmetic theorem.
- R-13 supplies the row–column torus upper bound 4m^2-2m+2; R-14 supplies the padding dimension c_m+3; R-17 gives exact determinant dimension 2n^2+2.
- G-10, G-11/G-12, and G-17 supply the stated effective degree, rectangular boundary, and stretched-label consequences after R22 proves their dimension hypothesis.
- The primitive root is fixed before the parameter grid is selected. The motif may depend on m and q. No statement about a universal coefficient choice or a polynomial-time construction is taken from a source or inferred from finite tests.

## R-B16 — ELSW: the actual linear strand of subpermanents

Efremenko, K., Landsberg, J. M., Schenck, H., & Weyman, J. (2018). On minimal free resolutions of sub-permanents and other ideals arising in complexity theory. Journal of Algebra, 503, 8–20. https://doi.org/10.1016/j.jalgebra.2018.01.021

- Primary author PDF: https://people.tamu.edu/~jml/ELSWmfr2-29.pdf . This is the17-page author version; theorem/page locators below refer to it.
- Theorem1.1, printedp2, gives the complete linear-strand dimensions. Section4.1, Example4.1, printedp11, gives the first linear syzygy dimension 2κ binom(n,κ+1)^2 and the explicit row/column Laplace-difference basis.
- Section4.1, Theorem4.3 and Lemma4.4, printedpp11–13, state and prove the full linear-strand description. For R23 only the first-syzygy case κ=m−1 is used; The standalone audit r23_syzygy_audit.tex checks that special case by monomial comparison; the manuscript cites the known result rather than reproving it.
- The group description at the start of section4, printedp11, also identifies the permanent stabilizer, but R23 does not need to assume it.
- Publication metadata verified against the first author's institutional research record: https://cris.bgu.ac.il/en/publications/on-minimal-free-resolutions-of-sub-permanents-and-other-ideals-ar-2/ .
- Retrievals: author PDF turn322065815view0; precise Example4.1 and Theorem4.3 turn170549272view0; institutional metadata turn124457132view0. Root must reopen sources before web citation.

## R-B17 — BCMV: a codimension bound that blocks the regular-sequence shortcut

Boralevi, A., Carlini, E., Michałek, M., & Ventura, E. (2024). On the codimension of permanental varieties (arXiv:2402.17839v2). arXiv. https://arxiv.org/pdf/2402.17839v2

- Matching primary PDF retrieved at https://arxiv.org/pdf/2402.17839 ; first page identifies v2,4December2024.
- Theorem4.14, printedp14, records von zur Gathen's lower bound5 for the codimension of the permanent singular locus for every m>=3, with upper bound2m.
- Theorem4.23, printedp17, proves the improved lower bound6 for m>=6. R23 only needs the lower bound5 to show depth(R/J_m)<m^2−4.
- The first derivative ideal defines this singular locus; its height is the codimension of the underlying variety even if the ideal is not radical. Neither cited codimension result asserts preservation of linear syzygies under a generic four-variable restriction.
- Retrievals: primary PDF turn322065815view2; Theorem4.14 turn171023286view3; Theorem4.23 turn171023286view4. Root independently opened both relevant primary papers in this run.


## R-24: exact finite certificate at size17

This is an in-run finite computation and deduction, with no external priority claim. The complete pencil, points, selected indices, and raw matrix are in `permanent_maximal/permanent_range_n17.json` and `.u8`; the compact omission list is also stated in the manuscript. `check_permanent_maximal.cpp` uses the R13 subset evaluator, while the separately executed Gray-code Ryser evaluator checked every entry. Root independently verified the selected minor by modular Bareiss and the 32-dimensional scaling kernel in `work/root/check_r24_certificate.py`; this is distinct from the author all-entry recomputation. The only theoretical dependencies are the already recorded R13 upper bound, R23 defect identity, and R14/G17/G18 consequences.

## R-25: exact bordered induction and size18 certificate

An in-run conditional reduction and finite corollary, without a priority claim. The permanent block identity, its parameter derivatives, and irreducible-open intersection are proved in full. The ternary size17 data, evaluation matrix, and selected minor are in `border_ternary/border_dense_m17.json` and `.u16`; `check_border_ternary.cpp` constructs the truncated subset recurrence. `check_border_ryser.cpp` separately checks all entries by Gray-code Ryser and prefix/suffix products. Root checks the specified minor by fraction-free Bareiss in `work/root/check_border_m17.py`. No statement about untested m follows from these finite calculations.

## R-26: uniform Jacobi-continuant induction

This is an in-run deduction, with no external priority claim. Dependencies are the already proved R25 exact border cancellation, R23 Tor identity, R25 base size18, and R14/G17/G18 consequences. The manuscript supplies the exact cofactor and Hessian forms, the normalized pair matrix, all17 core row lists/residues, and both insertion proofs. `check_jacobi_cores.py` and `border_ternary/jacobi_uniform_cores.json` supply full finite matrices; author integer Bareiss checks were performed separately. Root reconstructed the cores by enumerating path matchings, not by the continuant recurrence, and checked their determinants by modular fraction-free Bareiss in `work/root/check_r26_cores.py`. The theorem is not a numerical extrapolation and does not assert exact Tor vanishing.


## R-27: uniform endpoint repair and exact four-variable dimension

This is a proved in-run deduction, with no external priority claim. R26 supplies the continuant/path formulas and exact generic monomial-base ranks; R25 supplies the single-family border induction; R24 supplies the first maximal-size base; R13 supplies the dominant sizes and torus upper bound; R23 identifies the degree-specific Tor defect. The manuscript proves the general-endpoint K11 identity, the three first-order lifts, the finite-order rank lemma, complete-character support, and the whole-epsilon insertion in full. The finite certificate is fully specified by integer alpha/delta vectors, endpoint forms, row/column ordering, recurrence, and deterministic pivot rule in `r27_fragment.tex`, so its proof is not a JSON-only assertion.

The author builders are `check_jacobi_repair.py`, `check_jacobi_boundary_repair.py`, and `check_boundary_toeplitz.py`; all three finite arrays and selected minors are preserved under `border_ternary`. Root independently reconstructed every finite coefficient by direct path-matching enumeration and epsilon-polynomial multiplication in `work/root/check_r27_boundary_jets.py`, obtaining the same33852 entries and ranks84/172/262. The separate author `check_r27_one_insertion.py` verifies only the single m17-to18 row embedding; uniformity rests on the written interval/weight argument, not on this bounded computation. Root's complete proof reading and the author whole-proof reread both passed; other received reviews are recorded by their exact scope.


## R-28: higher-variable dimensions and common scalar-period elimination

This is an in-run deduction, without a priority claim. R17/R23 provide the four-variable determinant rank and cyclic cofactor independence, G21 the permanent dimension, G22 the stable Fourier-frame product point, and G18 the elementary numerical-semigroup bound. The new rank-r determinant extension, irreducible finite-stabilizer cyclic witness, common-open intersection, generic padding-line freeness including exponent1, and center calculation are proved in `r28_fragment.tex`.

The cited external background is already G-B15 rather than a duplicate R-B identifier: Mukai, S. (2003). *An introduction to invariants and moduli* (W. M. Oxbury, Trans.; Cambridge Studies in Advanced Mathematics, Vol.81). Cambridge University Press. Theorem5.3 with Corollary5.4, printedpp161–162, supplies closed-orbit separation; Proposition5.15, printedp166, supplies openness of stability. Primary book: https://www.math.ens.psl.eu/~benoist/refs/Mukai.pdf . Reopened here as `turn445725127view0`, targeted statements `turn860983737view0`/`turn860983737view1`. The statements/hypotheses were read; no independent whole-book verification is claimed.

The common-free-point part holds for3<=r<=m. Its determinant and padded-image dimension formulas retain their separately stated r>=4 hypotheses. No boundary assertion at nu1=(n−m)s is imported from the four-row theorem.


## R-29: prescribed moments and two-block common witnesses

This is an in-run deduction, without a priority claim. The full prescribed-product-moment lemma, two-block Lie-stabilizer calculation, padding weight identity, and enlarged-family intersection are proved in `r29_fragment.tex`. G22 supplies the previously checked Fourier-frame and Hilbert–Mumford framework; R28 supplies the central no-scaling and numerical-semigroup conclusion. The exact rank-r coordinate-ring extraction is the same Cartan calculation in G22 and does not rely on the old r<=m witness range.

The external background is G-B14, not a duplicate R-B identifier: Losev, I. V. (2006). *The Kempf–Ness theorem and invariant theory* [Preprint]. arXiv:math/0605756. https://arxiv.org/pdf/math/0605756 . Theorem4, printedp1, states both directions of closed orbit iff intersection with the moment-zero set; its proof is on printedp2. The primary PDF was reopened as `turn254909748view0` specifically to check the reverse direction needed to normalize the polynomial product. The original Kempf–Ness1979 source is cited by Losev but was not independently opened here. Mukai's Hilbert–Mumford, stability-openness and separation inputs retain the exact G-B15 locators already recorded for G22/R28.

The change of coordinates is an existence consequence of a closed orbit, not a claimed polynomial-time normalization. The proof carefully distinguishes the additive moment on ordered tensor factors from the directly calculated moment of a sum in orthogonal polynomial blocks. It never uses moment additivity for multiplication of forms.


## R-30: endpoint products, compact stabilizers, and tilted padding

An in-run algebraic deduction with no priority claim. R29 supplies the tensor-induced metric convention and reverse Kempf–Ness normalization. The new proper-interval circulant argument, rational eigenvalue tilt, finite padded-form witnesses, and auxiliary-flag elimination are proved in `r30_fragment.tex`. The product in exactly m variables retains a complex torus stabilizer; only its unitary projective stabilizer is made finite.

The external stabilizer input is already G-B14: Losev (2006), *The Kempf–Ness theorem and invariant theory*, proof of Theorem1, printedp2, equations(3)–(4) and the sentence immediately following. At a moment-zero vector, that passage explicitly concludes that the compact stabilizer Lie algebra is a real form of the complex stabilizer Lie algebra. Primary PDF https://arxiv.org/pdf/math/0605756 was reopened as `turn477725151view0`; the statement is applied only to the FULL balanced ordered padded tensor. No assumption that an unbalanced factor has a reductive stabilizer in the fixed unitary position is made.

The checked alternative finite-symmetrization route is preserved in `r30_finite_symmetrization_audit.md`; it is not needed for the manuscript proof and does not on its own give finite stabilizers. Root, purity and isolation each completed a whole-proof review; exact hashes and the later scope-only clarification are recorded in the check events and `r30_author_checks.md`.


## R-31: a proved scalar-period obstruction for the next-row route

This is an in-run deduction without a priority claim. Its only matrix calculation is written explicitly in `r31_fragment.tex`: a compensated transposition fixes the padded two-product form and generic auxiliary covector, has determinant minus one, and after SL normalization acts on the enhanced tensor by(-1)^b. The exact invariant extraction is the previously proved G22 Cartan calculation and requires no stability hypothesis.

The external input is already G-B15: Mukai (2003), Theorem5.3 with Corollary5.4, printedpp161–162, closed-orbit separation. Since every odd homogeneous invariant vanishes on the common subcone, separation places any nonzero closed orbit and its negative in the same orbit. The result concerns only the actual two-product subcone, not either full permanent/determinant orbit closure. The separate rank-deficient-moment failure and unproved richer-pencil routes are recorded in `r31_next_row_attempts.md`. No finite computation or unseen source theorem is used.


## R-32: stable unpadded comparison algebras

This is an in-run deduction without a priority claim. It applies the already proved R29 prescribed-moment and two-block argument with no padding, and therefore has no first-row padding inequality. The known external input remains G-B14 (Losev2006 Theorem4) for moment-zero closedness; R30 supplies the faithful nontrivial partial-flag action argument and R28 supplies closed-orbit separation plus the semigroup bound. The exact Cartan extraction and stable quotient dimension are G22. All new hypothesis checks and the rectangular/nonrectangular distinction are proved in `r32_fragment.tex`. Rectangular directions receive a stable algebra of the claimed dimension but are not asserted to have invariant-degree gcd one.


## R-33: exact tangent kernels control generic projective stabilizers

This is an in-run deduction without a priority claim. G21 supplies the already proved generic coefficient-map rank; the new proof identifies its entire kernel with the visibly independent row-column diagonal gauge on a dense open, then uses every-nonzero Pluecker coordinate to rule out projective variable Lie symmetries. The final quotient inequality uses the exact generic-fiber equality in the Stacks Project, Lemma33.20.4(2), tag0B2L (R-B18 below). Dictionary entry D-S3's EGA/SGA3 statements concern fiber-dimension upper semicontinuity and stabilizer openness; they are not used as a substitute for that equality. No new full EGA proof reading is claimed. The proof avoids any rational-invariant-field identification and never treats generic finite stabilizer as stability. Exact reviewed and final source-only hashes are recorded in `r33_author_checks.md`.


## R-B18 — Exact generic fiber dimension

The Stacks Project Authors. (2026). *The Stacks Project*, Lemma33.20.4(2), tag0B2L. Retrieved November21,2026, from https://stacks.math.columbia.edu/tag/0B2L

- Exact statement: for irreducible X and Z=closure f(X), the fiber dimension equals dimX-dimZ on a dense open. The displayed proof computes the generic fiber dimension as the difference of transcendence degrees.
- The complete short statement and proof were opened and read directly in this run as `turn154614368view0`; root independently opened the same primary source as `turn393219519view0`. This is the precise external input for R33's final quotient upper bound.
- The earlier D-S3/EGA/SGA source attribution was corrected before final compilation; the mathematical proof is unchanged.
