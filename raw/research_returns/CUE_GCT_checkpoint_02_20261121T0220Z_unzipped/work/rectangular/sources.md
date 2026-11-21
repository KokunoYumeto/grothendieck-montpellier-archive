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
