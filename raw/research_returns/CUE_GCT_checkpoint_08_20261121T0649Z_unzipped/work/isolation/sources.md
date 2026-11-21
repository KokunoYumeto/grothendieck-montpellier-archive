# Isolation sources and exact locators

All source paths below refer to the supplied archive extracted once to `sources/`. Existing results are not claimed as new. The dates in bibliographic entries follow publication/version dates, not regenerated PDF title-page timestamps.

## I-B01 — new graph input

Hoza, W. M. (2026). *NL = UL* (ECCC TR26-323). Supplied file `ECCC_TR26-323_Hoza_NL_equals_UL.pdf`.

- Definition 1.2, printed p. 2: internal-vertex path weights; uniqueness for all reachable vertex pairs.
- Theorem 1.3, printed pp. 2–3: one seed per fixed simple graph; seed length O(log(WN)); logarithmic-space computability; polynomial integer magnitudes.
- Formula (1), printed p. 3: rho_x(a,i)=sum_j 6^(nu_2(i)+ell-j) C(a)_j x_j.
- Theorem 2.4, printed p. 5: failure probability at most 2^(-d) W^4 N^2.
- Used as the supplied theorem. This track did not claim a formal or full independent verification of the theorem.

## I-B02 — basis isolation

Agrawal, M., Gurjar, R., Korwar, A., & Saxena, N. (2014). *Hitting-sets for ROABP and sum of set-multilinear circuits* [Preprint]. arXiv:1406.7535v1. https://arxiv.org/abs/1406.7535

Supplied source: `LIT_AGKS_hitting_sets_ROABP_basis_isolation/deltaDistanceSICOMP.tex`.

- Theorem 1: source label `thm:ROABPhs`; source lines 241–246; PDF p. 2.
- Definition 5: basis isolating weight assignment; source lines 902–919; PDF p. 7.
- Lemma 6: source label `lem:basisIsolation`, lines 927–988; PDF pp. 7–8.
- Observation 7: `obs:smallerWeight`, lines 1005–1028; PDF p. 8.
- Lemma 8: `lem:weightFunction`, lines 1040–1055 and proof thereafter; PDF pp. 9–11.
- Additional I-17 context: Theorem 3 (`thm:invROABPHS`), printed pp. 5 and 19; Lemma 27 (`lem:bSConc`), printed p. 22, source lines 2354–2400, invertible-constant-term matrix concentration. Primary PDF refs `turn317946964view0`, `turn814896166view0`, `turn814896166view1`, `turn814896166view2`.
- Primary PDF inspected: https://arxiv.org/pdf/1406.7535 ; web reference `turn166538694view0`; targeted findings `turn944129952view0`, `turn944129952view1`.

## I-B03 — matrix invariants

Forbes, M. A., & Shpilka, A. (2013). *Explicit Noether normalization for simultaneous conjugation via polynomial identity testing* [Preprint]. arXiv:1303.0084v2. https://arxiv.org/abs/1303.0084

Supplied source: `LIT_Forbes_Shpilka_explicit_Noether_normalization_matrix_invariants/pit-nn.tex`.

- Theorem 1.3 (`generatinginvariants`): trace generators of words of length at most m² in characteristic zero.
- Theorem 1.13 (`thm:integral subring`) and Corollary 1.14: quasipolynomial separating invariants/integral subring.
- Theorem 1.15 (`thm:orbit intersection`): deterministic NC orbit-closure intersection already follows from white-box PIT.
- Construction 3.1 (`roabpinv`), source lines 510–516: M(x), trace-generating polynomial.
- Lemma 3.2 (`diffofinv`), lines 520–526: difference has width 2m².
- Lemma 3.4 (`roabpcoeff`), lines 540–567; Corollary 3.6 (`reducetoroabp`), lines 581–587.
- Construction 3.7 (`const:hittingset`), lines 591–595.
- Theorem 3.8 (`thm:sepinv`), lines 599–613: m²|H| homogeneous separating invariants.
- Theorem 3.9: specialization of Derksen–Kemper Theorem 2.3.12, homogeneous separating invariants give integrality over algebraically closed characteristic zero.
- Corollary 3.10: integral-subring consequence for the same set.
- Primary PDF inspected: https://arxiv.org/pdf/1303.0084 ; web reference `turn166538694view1`; exact-number findings `turn944129952view2`, `turn944129952view4`.

## I-B04 — revised GCT V numbering

Mulmuley, K. D. (2017). Geometric complexity theory V: Efficient algorithms for Noether normalization. *Journal of the American Mathematical Society, 30*, 225–309. https://doi.org/10.1090/jams/864

Supplied source: `LIT_Mulmuley_GCT_V_Noether_normalization/main.tex`, matching arXiv:1209.5993v5 (26 May 2016).

- Theorem 5.14, source label `tequisdit`, lines 3094–3110; PDF pp. 45–46: strengthened general PIT versus strict e.s.o.p. for universal-circuit orbit closures. This is stronger than ordinary ROABP PIT and has an infinitesimal/border requirement.
- Section 7.5 and Lemma 7.9 (`lforbes`): replace symbolic determinant testing by ROABP testing for matrix invariants.
- Theorem 7.1 (`tmatrixstrongform`), Theorem 7.2 (`tintroorbitclosureNew`) and Theorem 7.7 (`tsepderksen`): exact scope of matrix normalization and already-known orbit-closure algorithms.
- Primary PDF inspected: https://arxiv.org/pdf/1209.5993 ; the cited theorem numbering was checked in this version.
- A reference in the 2013 Forbes–Shpilka paper to an earlier GCT V Theorem 1.6 must NOT be copied as the current theorem number. In the supplied revised source Theorem 1.6 is a different theorem about constant-dimensional groups.

## Independent source check for root finding G-07

Leal, M., Lozano Huerta, C., & Vite, M. (2024). The Noether–Lefschetz locus of surfaces in P³ formed by determinantal surfaces. *Mathematische Nachrichten, 297*(12), 4671–4688. https://doi.org/10.1002/mana.202400132

Primary preprint: https://arxiv.org/pdf/2303.09028 , version 3 (1 November 2024), inspected in this independent review.

- Definition 2, PDF p. 2: closed determinantal locus det(a,b).
- Proposition 1.1, PDF p. 4: irreducibility and nonempty smooth locus.
- Theorem 2, PDF pp. 3 and 15: prime divisor F1 degree 320112.
- Table 2, PDF p. 13: F1 has a=(5,5,5,5), b=(6,6,6,6), hence linear entries.
- Section 4.1, PDF p. 15 immediately before Theorem 2: `P_(20,2)=(1/2)D_(23,14)`.
- Primary web reference `turn280289537view0`; exact locators `turn520265669view0`, `turn520265669view2`, `turn520265669view3`.

## I-B05 — arithmetic support and logarithmic-space counting

Allender, E., & Ogihara, M. (1996). Relationships among PL, #L, and the determinant. *RAIRO–Theoretical Informatics and Applications, 30*(1), 1–21. https://doi.org/10.1051/ita/1996300100011

Primary scan inspected: https://www.numdam.org/item/ITA_1996__30_1_1_0.pdf

- Section 2, printed p. 4: halting logarithmic-space machines and their accepting-minus-rejecting gap.
- Theorem 1, printed p. 2: GapL and logarithmic-space functional reductions to integer determinant; following paragraph explicitly passes through iterated multiplication of {0,1,-1} matrices.
- Section 5, Definition 2, printed p. 11: C_=L defined by gap zero.
- Theorem 14, printed p. 12: singular integer matrices are C_=L-complete.
- I-12 proves its particular ROABP formulation directly. It does not assert that coC_=L is different from NL or that arbitrary polynomial-time algebraic support manipulation is impossible.
- Primary web references: `turn392175736view1`, `turn776322203view2`, `turn647216830view0`.

## Independent source check for P-08

Lagarias, J. C., & Odlyzko, A. M. (1977). Effective versions of the Chebotarev density theorem. In A. Fröhlich (Ed.), *Algebraic number fields* (pp. 409–464). Academic Press.

Primary-text TeXromancers transcription inspected: https://aareyanmanzoor.github.io/assets/articles/lagarias-odlyzko.pdf

- Theorem 1.1 and Corollary 1.2, transcription p. 4; equation (1.4): GRH for the Dedekind zeta function of L alone, an effective absolute constant, and an unramified prime ideal for every conjugacy class with norm bounded by c₂(log Δ_L)²(log log Δ_L)⁴.
- The parenthetical immediately following (1.4) handles L=Q by p=(2).
- The source's full Chebotarev proof was not independently checked. P-08's entire reduction proof was independently read and checked; see `independent_review_purity.md`.
- Primary web reference: `turn392175736view0`.


## I-B06 — known rank-one cut and product closure

Agrawal et al. (2014), the same primary supplied source and arXiv:1406.7535v1 as I-B02.

- Section 5.3, Lemma 32, printed p. 25, source label `lem:width2`: rank-one factorization of singular 2×2 factors after multiplication by a nonzero entry.
- Lemma 33, printed p. 26, source label `lem:lagrange`: Lagrange interpolation through a common hitting set preserves each scalar factor and its product. Its degree parameter is total degree, and disjoint variables are not required.
- Theorem 34, printed p. 26, source label `thm:ROABP22HS`: unknown-order width-two sparse-block result; univariate factors have sparsity at most delta+1 and maximum monomial support one, yielding polynomial size with the necessary field-size/extension convention.
- Primary PDF references `turn522083603view0` and `turn522083603view2`. Lemma proofs and theorem specialization were read; the entire AGKS article was not independently certified.

## I-B07 — one hidden order, known order, and every order

Gurjar, R., Korwar, A., & Saxena, N. (2017). Identity testing for constant-width, and any-order, read-once oblivious arithmetic branching programs. *Theory of Computing, 13*(2), 1–21. https://doi.org/10.4086/toc.2017.v013a002

- Primary publisher PDF: https://theoryofcomputing.org/articles/v013a002/v013a002.pdf
- Theorem 3.6 and Corollary 3.7, printed p. 11: constant width gives polynomial size when the variable order is known, in characteristic zero or the stated sufficiently large characteristic.
- Definition in §2.2.2, printed p. 6, and Theorem 4.9: the every-order class requires a width bound in each order, unlike a single hidden order.
- Primary statement/scope locators inspected: `turn482893562view0`, `turn440398949view0`; full article not independently certified.

Guo, Z., & Gurjar, R. (2020). Improved explicit hitting-sets for ROABPs. In *APPROX/RANDOM 2020*, LIPIcs 176, Article 4, 4:1–4:16. https://doi.org/10.4230/LIPIcs.APPROX/RANDOM.2020.4

- Primary PDF: https://drops.dagstuhl.de/storage/00lipics/lipics-vol176-approx-random2020/LIPIcs.APPROX-RANDOM.2020.4/LIPIcs.APPROX-RANDOM.2020.4.pdf
- Theorem 1, printed p. 4:3: unknown-order size polynomial in `d*(nr)^(log n/max(1,log log n-log log r))` in characteristic zero or greater than d; an explicitly weaker all-characteristic bound is also stated.
- Theorem 3, printed p. 4:4, treats the distinct every-order class.
- Primary theorem locators inspected: `turn440398949view1`, `turn440398949view2`; full proofs not independently certified here.

Hu, I., van Melkebeek, D., & Morgan, A. (2024). Polynomial identity testing via evaluation of rational functions. *Theory of Computing, 20*(1), 1–70. https://doi.org/10.4086/toc.2024.v020a001

- Primary PDF: https://theoryofcomputing.org/articles/v020a001/v020a001.pdf
- Theorem 1.9, printed p. 10: the SV-type width assertion includes a nonzero monomial of degree at most l+1. That extra promise must be retained.
- Inspected source/theorem locators: `turn334963068view0`, `turn317946964view1`.

Shpilka, A. (2026, November 9). *Polynomial-size hitting sets for multilinear any-order read-once algebraic branching programs and for set-multilinear depth-3 circuits with constant-size variable sets*. ECCC TR26-314. https://eccc.weizmann.ac.il/report/2026/314/

- Theorem 1.1, printed p. 3: multilinear every-order ROABPs; Remark 1.3 gives the border extension. The theorem permits arbitrary characteristic and a sufficiently large field/extension.
- Primary PDF and exact theorem inspected: `turn482893562view2`, `turn440398949view3`. This is not a one-hidden-order theorem.

Liu, Y. (2026, November 19). *Black-box identity testing for affine orbits of read-once oblivious algebraic branching programs* (Version 1, Hexagon 2611.00634v1) [Unrefereed preprint]. https://hexagonmath.org/2611.00634v1

- Primary PDF read: https://hexagonmath.org/pdf/2611.00634v1
- Section 3.1, Theorem 3.2 and Lemma 3.3, printed pp. 5–6: truncated coefficient spaces and the rank-profile support lemma.
- Section 3.2, Lemma 3.4, printed p. 6, and Lemma 3.6, printed p. 7: lowest homogeneous components and local rank tests.
- Proposition 3.1, printed p. 4, and §3.4, printed pp. 8–10: generator implementation inspected for context. The source's fixed-width polynomial bound is of the form `(nD+1)^(2^{O(w^2)})`, not `(nD+1)*2^{O(w^2)}`.
- I-21 proves a narrower original-coordinate width-three specialization independently in full, with ten interpolation pairs and a common scalar center. It does not rely on the Hasse-jet lemma. I-31 later proves a separate original-coordinate result for arbitrary width with width-dependent exponential pair count; the source's broader affine-orbit and multivariate-layer assertions are not certified.
- Host metadata inspected directly (`turn686172258view3`, lines 4, 8, 16–18): primarily AI-generated text; human understanding no parts; contributed by Yilin Liu; CC BY 4.0; OpenAI models used for formulation, proof development/review, text, and finite checks. This is source provenance, not a mathematical rejection or validation.
- Hexagon has its own identifier namespace. Official https://arxiv.org/abs/2611.00634 is an unrelated robotics article; it must not be cited for this paper.
- Primary proof locators: `turn138845898view0`, `turn412753216view0`. A local direct download failed with HTTP403; the primary PDF text was read via the web tool.

Singh, S., & Singh, V. (2026, February 13). *An algebraic rigidity framework for order-oblivious deterministic black-box PIT of ROABPs* (arXiv:2602.13449v1) [Preprint]. https://arxiv.org/abs/2602.13449

- Official arXiv record and primary PDF https://arxiv.org/pdf/2602.13449 were located (`turn293412751view0`, `turn920509881view1`).
- The full proof-scope audit I-22 refutes two foundational reductions; it does not disprove the headline existence statement. Definition 2.1 (p. 4) and section 3.1 (p. 6) conflate a scalar output with its generated coefficient algebra. Lemma 3.1 (pp. 6–7), Remark 3.1.4 (p. 9), and Lemma 3.2 (p. 10) incorrectly use radical nilpotence to discard nonzero products lying in the radical. Theorem 7.4 (p. 38) relies on these steps. Exact counterexamples and full proofs appear in I-22.
- Primary official locators independently inspected: `turn328741140view0`, `turn328741140view1`, `turn712030574view0`, `turn712030574view1`, `turn712030574view2`, `turn712030574view3`, `turn284504949view0`, `turn284504949view1`, `turn284504949view2`. Root and purity independently read the relevant primary claims and counterexamples.

## I-26 — determinantal SV vanishing ideals

Hu, I., van Melkebeek, D., & Morgan, A. (2024). Polynomial identity testing via evaluation of rational functions. *Theory of Computing, 20*(1), 1–70. https://doi.org/10.4086/toc.2024.v020a001

- Primary PDF: https://theoryofcomputing.org/articles/v020a001/v020a001.pdf
- Theorem 1.3, printed p. 6, and Corollary 1.5, printed p. 7: determinantal multilinear degree-(k+1) annihilators of SV_k on 2k+1 variables. Theorems 1.9–1.10, printed p. 10, retain the stated low-degree-monomial hypothesis for their ROABP assertions. Proposition 2.2, printed p. 16, gives the relation to rational-function evaluation.
- Primary locators read: `turn557879984view0`, `turn557879984view1`, `turn978349895view1`, `turn978349895view2`, `turn580774578view2`, `turn466993286view0`. I-26 proves its centered variant and invertible ROABP representation directly; no historical novelty claim is made.

Fournier, H., & Korwar, A. (2018, March 16). *Limitations of the Shpilka–Volkovich generator* [WACT presentation slides]. https://wact.imj-prg.fr/pdfs/slides-korwar.pdf

- Slides 13–19 state the earlier degree-(k+1) annihilator question. Primary source inspected: `turn978349895view0`, `turn580774578view1`. This is provenance for the problem, not a substitute for the proved I-26 argument.

## I-B08 — known logarithmic SV bound for the every-order class

Forbes, M. A., Saptharishi, R., & Shpilka, A. (2014). Hitting sets for multilinear read-once algebraic branching programs, in any order. In *Proceedings of the 46th Annual ACM Symposium on Theory of Computing* (pp. 867–875). https://doi.org/10.1145/2591796.2591816

- Primary full version: *Pseudorandomness for multilinear read-once algebraic branching programs, in any order*, https://arxiv.org/pdf/1309.5668 . Definition 1.1, printed p. 3, defines its “commutative” class by a width bound in every variable order, not by a single hidden order. Pairwise commuting coefficient matrices imply membership but are a sufficient representation condition, not the definition.
- Theorem 4.1, printed pp. 21–22, and Corollary 4.3, printed p. 22: SV with `1+2 floor(2 log_2 w)` pairs hits individual-degree-less-than-d width-w every-order polynomials, with stated field condition `|F|>nd` and quasipolynomial evaluation size. The proof's local factorization use of the every-order condition and additive SV composition were read. Subsidiary rank-condenser proofs were not all rechecked.
- Primary locators: `turn861149972view0`, `turn528173805view0`, `turn528173805view1`. The later primary exposition Forbes–Shpilka–Volk (2018), https://theoryofcomputing.org/articles/v014a018/v014a018.pdf , was used to locate the original result, not as a replacement for it.
- I-B08 makes explicit that the commuting unipotent I-26 family already has a known logarithmic sufficient pair bound. The open question in I-26 is for the full one-hidden-order rank-test class.

## I-31 — full matrix cone specialization

Liu (2026), the same explicitly unrefereed primary source as I-B07.

- Section 3.3, printed pp. 7–8, reopened and read in full: stable projected-cone deletion for rank-s blocks, composition under disjoint restrictions, and the rank-level recurrence. Primary locators `turn173872731view0`, `turn173872731view1`.
- I-31 gives a direct full proof with the looser count2ws-1, avoiding the source's first-block function-field factorization, and adds rectangular endpoint absorption in the ground GL_w space. It proves the original-coordinate, one-hidden-order result for all widths, with2^{O(w log w)} pairs in general; the field, interpolation and fixed-width versus variable-width distinctions are explicit.
- Root and purity independently checked the complete standalone proof. This does not certify the source's affine-orbit, bounded-overlap, or bivariate refinements.


## I-32 — paired reset construction

This is a deduction authored in the purity track from I-24, with complete independent proof readings by root and isolation. The exact retained-coordinate threshold and all partial-interval ranks are proved in the report. No external priority claim or new source theorem is invoked.

## I-33 — established PIT scope and the explicit prime construction

Bisht, P., Gupta, N., & Volkovich, I. (2023). Towards identity testing for sums of products of read-once and multilinear bounded-read formulae. In *43rd IARCS Annual Conference on Foundations of Software Technology and Theoretical Computer Science (FSTTCS 2023)*, LIPIcs 284, Article 9, 9:1–9:23. https://doi.org/10.4230/LIPIcs.FSTTCS.2023.9

- Primary publisher PDF: https://drops.dagstuhl.de/storage/00lipics/lipics-vol284-fsttcs2023/LIPIcs.FSTTCS.2023.9/LIPIcs.FSTTCS.2023.9.pdf
- Theorem 1, printed p.9:4: polynomial-time blackbox PIT for the sum of two products of read-once formulas. The immediately preceding paragraph states |F|>n*d or access to an adequate extension.
- Section1.3.1, printed pp.9:5–9:7, gives the proof overview; Theorem48, printed p.9:20, gives the generator G_(n,4), followed by the proof of Theorem1. The statements and proof overview were inspected; all subsidiary proofs have not been independently certified.
- Primary retrieval locators from the original reads: turn543797353view0 and turn827549969view0. The publisher PDF was reopened at the recorded I33 integration event. Official ECCC provenance also exists at https://eccc.weizmann.ac.il/report/2023/109/ .
- I-33 proves its specific divisor-orbit prime family directly and claims no historical priority. Polynomial PIT for its width-two subclass is already supplied by I-B06; higher-degree univariate factors also split into linear read-once factors after scalar extension. The scalar product-closure repair is explicitly the AGKS2014 Lemma33 construction, with its source locators in I-B06.

- Additional root primary-source check received at 2026-11-21T02:59:23+00:00: Theorem1 p.9:4 and Theorem48/direct proof p.9:20, refs turn513248768view1 and turn513248768view2; all-characteristic field-size premise and eight-parameter G4 confirmed. This does not certify the full BGV proof.


## I-34 — prime repair under a local nullity promise

The complete proof is a deduction from the I-33 divisor lemma and elementary coefficient elimination. Constant-term-count PIT is background, supplied for example by I-B08; no new general complexity claim is made for that established case. The arbitrary-term-count statement retains its local-nullity promise. The three-product additive identity and the tensor-rank-four example are proved directly and corroborated by check_I34.py. Root and purity each independently read the complete proof. No additional external theorem or historical priority claim is invoked.

## I-35 — contraction tests and exact composition scope

Parthasarathy, K. R. (2004). On the maximal dimension of a completely entangled subspace for finite level quantum systems. *Proceedings of the Indian Academy of Sciences—Mathematical Sciences, 114*(4), 365–374. https://doi.org/10.1007/BF02829441

- Primary full version: https://arxiv.org/pdf/quant-ph/0405077 . Propositions 1.3–1.4 and Theorem 1.5, preprint pp.4–6, were reopened and their complete local proofs read (turn918939176view0).
- The 2r−1-dimensional two-factor Hankel test space and its optimality over the complex numbers are known background, already recorded as P-B16. Its reproof is retained only in I35_known_background_audit.md; it is not presented as a new result. The same Segre argument gives the explicitly stated algebraically closed field formulation.

The Stacks Project Authors. (2026). *The Stacks Project*.

- Lemma 27.13.6, tag01WD (Segre embedding): https://stacks.math.columbia.edu/tag/01WD . Primary statement and displayed proof read (turn779543504view1).
- Lemma 33.34.3, tag0B2R (projective intersection dimension): https://stacks.math.columbia.edu/tag/0B2R . Primary statement and displayed proof read (turn779543504view0).
- I-35 proves the rank-one-annihilator criterion, the generic unipotent bridge realization, extension-field composition with fresh seeds and an explicit polynomial-map degree budget, both synchronization failures, and the rank-one multiplicative-corner obstruction. The generic small-subspace existence argument asserts neither an effective construction nor a field-of-definition bound. Root and purity each independently read the full repaired proof.

## I-36 — pairwise dominance and singular-factor completion

This deduction invokes no new external theorem. The rank-one pivot identity and scalar product closure are the established mechanism recorded in I-B06 (AGKS2014 Lemmas32–33) and the fully proved P-14. The full-width-three rank-one completion is the already audited I-21/I-29/I-30 argument. I-36 proves directly that t+SV1 is dominant on every pair, applies the pivot-cleared identity to rank-one compound words, and thereby supplies one whole maximal-minor preservation stage. All-characteristic scalar extension and finite-grid requirements are stated explicitly. Root and purity independently read and rederived the full proof. No computation certificate or historical priority claim is made.

## I-37 — affine singular width-three words and two centered pairs

This is a fully proved deduction from I-36 and elementary polynomial algebra, with no additional external theorem accepted as an unproved input. The purity agent supplied the first-order pole-extraction idea while studying Hu, van Melkebeek, and Morgan (2024), *Polynomial identity testing via evaluation of rational functions*, whose primary published source and exact RFE/SV locators are already recorded under I-26 and P-B20. I-37 directly proves the arbitrary-nonzero-slope and every-characteristic version required here. It also supplies complete proofs of irreducible multilinear factor inheritance, the multivariate-UFD rank-one factorization, compatible endpoint gauges, the tridiagonal Hessian induction and every boundary case of the final state-path contradiction. These deductions are not attributed as a theorem of the source paper, and no historical priority claim is made.

The rank-one compound/pair-dominance input is exactly the already audited I-36. The result is for representations by affine singular factors, not every polynomial that happens to be multilinear with an unrelated higher-degree singular representation. Root and purity independently read and rederived the entire standalone proof; both passed it without a requested mathematical change. The final polynomial sampler has five parameters and the exact grid count (D+1)((n-1)D+1)^2 binom(D+2,2), with the stated working-field extension convention. No numerical certificate is required or claimed for this algebraic proof.

## I-38 — isolated invertible affine factors

This is a proved extension of I-37, not a new external result being accepted. Every new step is written in full: algebraic triple dominance without a Jacobian, inheritance of the no-adjacent-rank-three promise, exact compound connector scope, rank (rather than all-minor) preservation, endpoint projections, compatible I/P constants with transported endpoint shears, and the two tangent-kernel elimination. Purity independently suggested Hh=Hh² rather than a slope-dependent determinant; the latter can be degenerate in characteristic two. The proof and the five-parameter polynomial sampler hold in every characteristic. Root and purity each read and rederived the entire standalone proof and passed it without requesting a repair. No historical priority claim or numerical verification claim is made.

## I-39 — concrete failures of the next mixed-word repairs

The rational identity and residue forms are the explicit P-16 construction, independently read in full earlier in this run. I-39 rederives every needed identity rather than relying on an unstated RFE theorem. The additional ordinary-node parity scaling, affine matrix corner and variable anchors, absolute irreducibility, all-interval rank assertions, and abstract Hessian identities are proved in full. Purity independently checked the abstract Hessian idea and then read the complete written proof; root also read and rederived the entire proof. Both passed it without repair. The all-characteristic assertions of I-37/I-38 are unchanged; I-39's two obstructions are explicitly over characteristic zero. No historical priority claim is made. The actual symbolic check_I39_matrix_identities.py execution corroborated the finite displayed matrix and rational identities, without being described as a general proof certificate.


## I-B09 — characteristic-free highest-weight lines

Jantzen, J. C. (n.d.). *Representations of algebraic groups and their Lie algebras, Lecture I*. Primary author lecture: https://www.math.uni-bielefeld.de/~baumeist/sommerschule/Jantzen1.pdf . The exact inputs are printed p.2 (Frobenius reciprocity and both adjunction maps) and p.3 (for the lower Borel, induction of character d is Sym^d(V*) for d>=0 and zero for d<0). These statements and their immediate computations were independently read in full by isolation, purity and root in this run. No characteristic-zero simplicity or complete-reducibility result from the later discussion is used. The upper-Borel eigenline convention follows by dualizing and Weyl conjugation; a complete sign check and direct Bruhat audit are in I40_highest_weight_audit.md. This is established background, not a claimed new representation-theoretic theorem.

## I-40 — determinant-character budget and the balanced nine-variable closure

The new deduction is proved in full from I-B09, the already audited split-torus grading G-B02, I-37/I-38, and the stable P-17 theorem. Both Borel support spaces provide nonnegative determinant weights, whose sum is the bond rank times n-2D. The actual minimal-core inclusion yields the exact matrix covariance and the full-rank increment, rather than assuming an equivariant representation. Root and purity independently read and rederived the complete proof and the separate convention audit, passing without repair. The balanced-ideal degree and lowest-component inputs retain their exact Hu–van Melkebeek–Morgan Definition9.5/Theorem9.13/Proposition8.3 locators recorded under P-B20 and in the independent P17 review. The full nine-variable conclusion is distinguished from the ordinary centered-SV result for the weight-zero/one translation-invariant subclass. The denominator-safe finite grid and all extension-field requirements are proved directly. No historical priority or numerical certificate is claimed.


## I-41 — saturated weight-two connectors and the balanced ten-variable closure

This is a fully proved deduction from I-40's determinant budget, I-B09's established characteristic-free group representation input, the I-37/I-38 rank and normalization arguments, and stable P-17. The saturation argument makes only the determinant-weight-zero bounding support spaces SL2-stable. The adjacent standard-module conclusion is proved by integer weight pairing, explicitly excluding Frobenius twists without semisimplicity. The characteristic-two three-plane is the actual submodule Gamma^2(V) inside V tensor V; the proof never identifies it with its dual. The right anchor uses the actual antidiagonal coefficient pairing. Purity independently checked that matrix calculation and the endpoint simplification during development, then root and purity independently read and rederived the entire proof. Both passed with only the same TeX dim typo, repaired before integration. The resulting five-parameter map is balanced rational evaluation with common slope one; no ordinary centered-SV or arbitrary-slope extension is claimed at weight two. No new external theorem, historical priority, or numerical certificate is asserted.


## I-42 — reset-Hessian thresholds and saturated-run subclasses

The reset-Hessian argument and both sharp abstract examples are proved directly by Vandermonde column independence. They invoke no new external theorem. Root and purity independently rederived the complete draft, including the characteristic-two overlap and the characteristic-not-two row(k+1) argument. The saturated-run application uses precisely the established I-B09 input and I40/I41 canonical support-space arguments. Its positive promise is stated for an irreducible homogeneous translation-invariant input and its actual minimal cores; factor inheritance of that additional run-length promise is not assumed. The abstract seven- and eight-node Hessians carry no fixed-polynomial integrability or ROABP-annihilator claim. Root requested explicit transport of endpoint shears through initial/terminal identity strings, which is now included from the already checked I38 proof. No computation certificate or historical priority is claimed.


## I-B10 — lines in a Grassmannian over an arbitrary field

Ghorpade, S. R., Patil, A. R., & Pillai, H. K. (2009). Decomposable subspaces, linear sections of Grassmann varieties, and higher weights of Grassmann codes. *Finite Fields and Their Applications, 15*(1), 54–68. https://doi.org/10.1016/j.ffa.2008.08.001 . Primary author/arXiv version: https://www.math.iitb.ac.in/~srg/preprints/DecomposableSubspaces.pdf ; arXiv0710.5161v1, https://arxiv.org/abs/0710.5161 . The exact input is Lemma3, printedp4, and its full proof: two independent decomposable exterior vectors have decomposable sum precisely when their associated planes intersect in codimension one. Its ambient field is arbitrary (specified in section2, printedp3). Isolation, root, and purity each independently opened this primary PDF and read the complete lemma/proof in this run. The arXiv primary record confirms the journal metadata and DOI.

Internal retrieval record: isolation turn794558131view0 (author PDF, lines159–221), turn794558131view1 (arXiv bibliographic record); root turn612985097view0. These identifiers are audit locators, not manuscript bibliography text.

## I-43 — weight-three connectors and balanced eleven-variable closure

This is a fully proved deduction from the established I-B09/I-B10 inputs and the already independently checked I40–I42 and P19 results. The determinant-weight-one Grassmann orbit line supplies invariant two/four-planes; actual adjacent coefficient support of dimension at most3 excludes larger torus weights by a physical-unipotent calculation valid in every characteristic. That constraint makes the normalized middle compound affine, and a unique internal pole tests its coefficient using independent anchor values. The determinant-weight-zero case needs only one canonical anchor; the opposite affine rows are handled directly, without invariant or self-dual assumptions. Root and purity independently read and rederived the entire exact standalone proof, including shared-parameter pivot/endpoint composition, the reset-Hessian application and the n<=11 degree induction, and passed it without repair. The arbitrary-variable cubic result P19 was independently reread in full by isolation. No numerical certificate, ordinary-SV promotion, or historical priority claim is made.


## I-44 — exact torus-chain anchors and the next balanced windows

This deduction uses no new external theorem. It applies the already proved exact integer-character covariance of I40 to classify every possible three-weight step pattern, then enumerates all minimal singular affine anchors into the unique chain pattern. The coefficient-row and coefficient-column independence are those of the actual minimal tensor representation. Both independent reviewers explicitly re-enumerated the six two-row and four three-row subsets, the excluded multiplicities, the surviving five matrix patterns, and the actual antidiagonal right pairing. The two quadratic pole equations are derived directly and use no division by2. Root and purity each read and rederived the complete exact standalone proof, passing without repair, including the common-parameter rank/endpoints, factor reduction and finite degree windows. I42 supplies only its already audited scalar reset thresholds, so the distinction between all-characteristic rank preservation for five-core runs and the characteristic-not-two scalar conclusion remains explicit. No numerical certificate, new background theorem, ordinary-SV promotion or historical priority claim is made.
