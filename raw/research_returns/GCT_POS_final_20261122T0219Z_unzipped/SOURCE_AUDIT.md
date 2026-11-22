# Source, attribution and scope audit

Date: 21–22 November 2026. Run: GCT_POS. Reviewers are identified in `CHECK_EVENTS.tsv`; model GPT-6 Astra Pro, effort not exposed. This is a record of the passages actually inspected. It is not a claim to have independently proved every published theorem or to have searched every inaccessible or unpublished work.

## 1. Conventions that control every comparison

The question expressly fixes **GCT VI = arXiv:0704.0229v4**, with Definitions1.2.2 and1.2.4, printed pp.13–14, and Hypotheses1.6.4–1.6.7, pp.24–25. The general-form hypotheses are3.3.1–3.3.4, pp.50–57. The source's height parameter and constituentwise indices are retained. In particular, eventual positivity at degrees belonging to a constituent's own residue class is weaker than positivity of that polynomial at all positive integer arguments. A theorem about semigroup saturation, eventual support or a different stretching parameter is not silently substituted.

The three supplied runs are prior work, cited by **ALPOGE_GCT P-F…**, **GCT_PLETH G-/T-/R-/A-…**, and **GCT_NSRH F…**. Their mathematical conclusions are not claimed as discoveries of this continuation. Inputs reported only at statement level were re-read when invoked; individual check receipts say which complete proofs were read. A computation is called independent only where the recorded arithmetic or verification was actually reconstructed independently. No Lean certificate or original archive-scan inspection is claimed.

## 2. Finding-by-finding attribution

| Finding | Attribution and extent of the present result | Boundary of the claim |
|---|---|---|
| K-001 | Classical invariant ring, attributed by Bremner–Hu to Vinberg; direct constituent/index calibration in this run. | No claim of a new ternary-trilinear invariant ring. |
| K-002–K-008 | Exact finite n=4 classification, lift coverage, full stabilizers and combined residue proved and certified here, using rechecked ALPOGE_GCT P-F23/P-F60/P-F65. No matching complete calculation found in the inspected literature. | A finite-dimensional pole does not settle variable-n PH3. |
| K-009 | Incidence-lattice/Gram estimate proved here using elementary integer linear algebra. | It is an exponential cutoff, not the conjectured sharp dyadic bound. |
| K-010–K-014 | Exact n=5 fixed-space and lift classification, repeated-block geometry, full stabilizers and combined residue; independent certificate and proof checks. | It does not classify arbitrary dimensions. |
| K-015–K-016 | Lie extension and full-stabilizer arguments for a second all-dimensional family, extending the supplied seed. | One family is not the whole fixed locus. |
| K-017 | Explicit unstable free-support countermodel and finite valuation diagnostics. | It is superseded for the semistable-bound question by K-018, but records why the first route failed. |
| K-018 | Explicit positive boundary gadget and all-dimensional polystable character orders exceeding2^(n−1). Whole-proof and independent arithmetic checks passed. Transportation-polytope priority search is recorded separately. | No priority claim; no global pole or index conclusion follows from this construction alone. |
| K-019–K-021 | Full stabilizers of the amplified family, smooth density-one curves, and exact higher-dimensional fixed-locus counts. Whole-proof checks and exact replays passed. | The global component sum remains open; the local dimension theorem is not a pole theorem. |
| K-022 | Explicit smooth two-curve cancellation on a weighted Gr(2,5) cone; exact Pfaffian numerator and local Euler calculations. The weighted Grassmannian Hilbert numerator is known (Corti–Reid). | No claim that this is the first cancellation example; the grading differs from the uniform tensor grading. |
| K-023 | Specialized cyclic trace identity, derived directly from the known Scharf higher Lie-character/root-number identity. | The general character identity is known; no priority claim for it. |
| K-024 and R-NEW-004 | Full hook-chain stabilizer, unique maximal dyadic fixed curve, unit residue and exclusion of higher colliding poles, proved and whole-proof checked here. | Characteristic-zero geometry is separate from reduction of Hilbert series; no modular smoothness assertion. |
| K-025 | Explicit critical dimension-three frame and block sum with K-020 produce a polystable order3·2^25 character in dimension26. | This refutes blanket exclusion of odd lifts, not exact dyadic poles. |
| K-026–K-028 | Cyclic symmetry classifies the fixed irreducible loci with generic finite effective stabilizer of order prime to3; integral coherent localization reduces cancellation to the stated exceptional support. Luna's slice theorem and coherent localization are classical inputs with new primary checks. | The exceptional class is not determined. No all-n exact dyadic pole or prior-art exclusion is claimed. |
| K-029 | Critical direct sums and a fixed-vector quotient-image argument show that the actual high-dimensional amplified components meet the higher3M-fixed locus. | This realizes the collision exception geometrically; it does not calculate its residue or show that cancellation occurs. No priority claim is made. |
| K-030–K-031 | Finite character-coset and algebraic-group component arguments remove every stabilizer exception. Borel–Serre/Lucchini Arteche and Luna inputs are classical and directly checked at the stated locators. | Only the collision-supported coherent class remains; its Laurent value is unknown. |
| K-032 | Finite normalization and exact graded coefficient formula for the k=8l amplified collision family. General finite restriction is classical (Luna; Bate–Geranios–Martin); the specialized proof and formula are given here. | No density, simple Laurent coefficient, all-component classification or exact-M pole conclusion is claimed. |
| R-NEW-001 | Two independent standard-character implementations and the complete finite outer-six table. | These are exact verification data, not a new character identity or all-degree positive formula. |
| R-NEW-002 | Consequence of published canonical-map rank and propagation theorems; critical annihilators identified as zero in the question's notation. | The full a=4,5 rank laws are credited to their sources. |
| R-NEW-003 | Finite exact rational expression for H4 obtained from an explicit denominator and finite character sums. | The degree3196 numerator has not been fully expanded or minimized; no new fast Hilbert-series algorithm is claimed. |
| PNEW-001 | Assembly and complete rechecking of the supplied cubic refutation chain. | Original refutations belong to ALPOGE_GCT and GCT_PLETH, not this continuation. |
| PNEW-002–PNEW-007 | Explicit threshold79000 and exact finite witnesses/Veronese refinements, proved and checked here. | The threshold is sufficient, not proved optimal; small-rank witness minimality is stated only within its exact proved scope. |
| PNEW-008 | Determinant-twist counterexample to an intrinsic/effective stabilizer-growth converse. | A reading that counts artificial raw general-linear central kernels is not refuted by that example. |
| PNEW-009 | Exact binary-shell density theorem for each fixed proper inner embedding, using the published branching quasipolynomial theorem. | Constants depend on the fixed embedding; the full varying-embedding narrow SH(b) remains open. |
| PNEW-010 | Exponential minimal-cover rank in the literal G-040 family and exact module reduction. | It rules out that dense-cover implementation being polynomial uniformly in b; it does not rule out a compressed positive #P formula. |
| PNEW-011 | Exact equivariant Cox grading and scalar balanced-module dictionary. The Grassmannian Cox-ring identification is known (Castravet–Tevelev). | Scalar fat points give two-row output. General flag tails are a further problem. |
| PNEW-012 | Compiled PPS scalar formula: at most45 fixed polytopes, at most11 variables, and a binary-time evaluator; full proof and exact replay checked. | All general flag tails remain open; the underlying two-row positivity theorem is credited to PPS. |
| PNEW-013 | Elementary modular cyclotomic transfer and its application to the checked hook trace; proves numerical PH3 false for triple rectangles. Bounded targeted searches found no matching application. | Absence from search is not proof of novelty; exact dyadic order and strict index bounds remain open. |
| PNEW-014 | Explicit formal rational-character countermodel to strict-index transfer from the positive trace decomposition and listed numerical constraints; complete proof and independent replays. | These are not invariant algebras, and G is not the actual B_n. No conclusion on the actual tensor strict indices. |
| N-001 | Whole-table obstruction for the specified weighted cyclic identity of rank-three structure coefficients, checked against the actual product relation. | It is not presented as an algebra-automorphism classification. |
| N-002 | First negative P-word in the searched word-length ordering, with exhaustive shorter-word checks. | Word-basis failure alone would not rule out another integral basis; N-009 supplies the stronger obstruction. |
| N-003–N-004 | Explicit generic positive basis/proper lattice and a freeness-to-positive-basis reduction. | The coefficient ring is essential; rational results do not imply freeness over Z[v,v^−1]. |
| N-005 | Explicit associative dimension rings improving earlier finite-window scores; the supplied counting-consult Theorem5 supplies their abstract additive monoidal realizations. | No global minimum, canonical selection, or identification with the geometric Hecke category is proved. |
| N-006 | Explicit fixed-q lisse realization with the actual rank-three coefficient objects and P-actions, built from the supplied F46 model. | It is not asserted to come from constant-coefficient smooth projective cohomology or to implement extension-wise parameter retuning. |
| N-007 | Rational-D versus Laurent-Tate distinction, by an exact scalar example. | Membership in Q(D) alone does not imply a finite Laurent polynomial in q. |
| N-008 | Exact rank-four ambient-image and trace ranks at the sign specialization. | These are not the dimension or radical of the abstract order's fiber. |
| N-009 | All-degree nonfreeness of the full integral P-generated order, with a126-generator residue obstruction against generic rank114. Targeted primary-source search found no earlier theorem of this form. | No claim about localization at2 or [2], the saturated order, or the nonstandard Temperley–Lieb quotient. |
| N-010 | Explicit rational-D models, exact splitting certificate and GT path lines. Generic dimensions/simple-module types were already known in GCT IV. | This does not identify VIII's canonical normalizations. |
| N-011 | Exact formula for extreme Laurent coefficients and its application to the supplied negative examples. | It explains those coefficients; it does not imply all rank-four structure constants are positive or negative. |
| N-012 | Refutation of the external minimization rule literally printed in VIII §3.3, including a rank-one counterexample. | The explicitly bar-fixed rule in §4 and other repairs are distinct. |
| N-013 | Conditional descent of a unique minimum in an explicitly bar-fixed repair to the actual Q[D] word order. | Existence/uniqueness is not supplied by descent alone. |
| N-014 | Exact multiplicity-space obstruction to the literal single-highest-weight label order, also exposing equal-weight antisymmetry failure. | Antichain orders or specified total refinements are alternative definitions, not ruled out. |
| N-015 | Exact114-element basis of the actual unsaturated Q[D] word order, with membership and all-degree closure certificates. | Rational polynomial freeness does not contradict integral mixed-characteristic nonfreeness. |
| N-016 | Terminating finite global-minimization and full-domain uniqueness tests for the explicit bar-fixed repair, with a direct linear implementation. | The attempted repairs fail as recorded in N-017/N-018; no polynomial complexity or identification with the defective printed rule is claimed. |
| N-017 | Complete actual four-element repaired block, all64 multiplication constants and exact source-comparator checks. | The total refinement fails and the successful product block has a forced nonunimodal ambient residual; no printed canonical E4 is identified. |
| N-018 | Exact all-degree fifth-stage failure in the other minimal block; invariant under rational rescaling of the fixed GT lines. | It refutes this product-path repair, not every possible replacement definition. |
| N-019 | Explicit maximal-scaling rule, balanced triple, actual114-element rational-order basis and full12996-product table. Polynomial Hermite reduction is standard and credited below. | This basis is not VIII E4 and fails signed positivity; the bounded search does not prove priority for its particular application. |
| N-020 | Actual rank-four sign fibre, radical, quotient and corrected parabolic section computed with complete multiplication certificates. The rank-three presentation and base-change distinction are known and credited. | No identification with the defective printed E4 or general categorical realization. |
| N-021 | Monomial-matching exponent compression gives an explicit all-degree finite reduction for integral Laurent dimension tables. Determinant/small-integer-witness methods are standard and credited to the inspected primary comparator. | No global optimum, uniqueness, canonical category, binary-budget NP claim or automatic application to rational N-019 coefficients. |

Later findings, if any, are added to this audit and the check ledger before finalization. Absence from the inspected sources is not proof of absolute novelty.

## 3. The requested GCT and complexity sources

### S01. The fixed GCT VI source

Mulmuley, K. D. (2009). *Geometric complexity theory VI: The flip via positivity* (arXiv:0704.0229v4). [Primary version](https://arxiv.org/abs/0704.0229v4).

Inspected against the supplied author LaTeX and primary pagination: Definitions1.2.2/1.2.4, pp.13–14; Theorem1.6.1(d), pp.20–21; Hypotheses1.6.4–1.6.7, pp.24–25; general-form definitions/hypotheses3.3.1–3.3.4, pp.50–57. The exact erratum and implication checks are reproduced in the plethysm companion, citing ALPOGE_GCT P-F11/P-F12/P-F14/P-F15. The version, not an automatically generated title-page date, fixes the claims under examination.

### S02. Later formulations and an access limitation

Mulmuley, K. D. (2011). On P vs. NP and geometric complexity theory. *Journal of the ACM, 58*(2), Article5, 1–26. [DOI](https://doi.org/10.1145/1944345.1944346). [Author manuscript](https://ramakrishnadas.cs.uchicago.edu/gctexplicit.pdf).

The search-indexed primary author text was inspected for Lemma4.9 and Hypotheses4.10–4.11 (author manuscript p.29). These concern asymptotic stretching multiplicities F_(λ,n,m), G_(λ,m) attached to permanent/determinant constructions and parametrized, potentially nonhomogeneous polytopes. They are not automatically the broad plethysm hypotheses of the fixed2009 version. Direct PDF retrieval repeatedly returned502, so no whole-manuscript reading is claimed.

A distinct January31,2011 revision of *GCT VI* is cited in later primary literature at `gct.cs.uchicago.edu/gct6.pdf`. Both that author URL and the corresponding `ramakrishnadas` URL returned502; alternative university aliases were inaccessible. A secondary text transcription suggests changed numbering and definitions, but is **not used as a primary theorem source**. Its exact differences remain an access-limited source-audit item. Likewise, the university catalogue's marking of the old technical report as “obsolete” is metadata, not a mathematical withdrawal theorem. This paper's conclusions expressly target arXivv4 as requested.

### S03. GCT VII

Mulmuley, K. D. (2008). *Geometric complexity theory VII: Nonstandard quantum group for the plethysm problem* (arXiv:0709.0749v2). [Primary PDF](https://arxiv.org/pdf/0709.0749v2).

Problem1.1, printed p.2, is the general positive #P-formula problem; Conjecture1.3 is the proposed nonstandard duality. The actual rank-four restriction table in §7.2.2, pp.48–49, and its floating-point qualification were read in full for N-014. This source does not establish a general positive basis or the integral freeness disproved in N-009.

### S04. GCT VIII

Mulmuley, K. D. (2008). *Geometric complexity theory VIII: On canonical bases for the nonstandard quantum groups* (arXiv:0709.0751v2). [Primary PDF](https://arxiv.org/pdf/0709.0751v2).

Inspected passages: §2.3, printed p.11, single-highest-weight order; §3.1, pp.19–20, GT construction and multiplicity-free condition C1'; §3.3, pp.20–22, external degree complexity, equation(13), Conjectures3.1/3.2; §4, beginning p.26, the different internal definition with an explicit bar-invariance restriction; §5.2, the distinguished rank-four computation. N-012 and N-014 address literal statements in these passages. N-013 labels its repaired rule explicitly. A field-level GT construction is not a proof of the conjectural canonical globalization.

### S05. Kahle–Michałek's obstruction

Kahle, T., & Michałek, M. (2018). Obstructions to combinatorial formulas for plethysm. *The Electronic Journal of Combinatorics, 25*(1), P1.41. [Author version](https://arxiv.org/abs/1507.07131).

Theorem5 and Remark6, printed p.4, are the known homogeneous-Ehrhart obstruction on p_((4s),(3))^((7s,5s)). The supplied author source and the full relevant proof were checked by the plethysm branch; the intake's finite recomputation is retained. This known ray is the input P-K1. It is not the new all-rank PH2/SH(a) mechanism, and a shifted polytope or nonhomogeneous parameterized description must be distinguished from homogeneous PH1.

### S06. Briand–Orellana–Rosas

Briand, E., Orellana, R., & Rosas, M. (2009). *Reduced Kronecker coefficients and counter-examples to Mulmuley's strong saturation conjecture* (arXiv:0810.3163v3). [Primary PDF](https://arxiv.org/pdf/0810.3163).

Theorem2.4, equation(2.5), printed p.7, gives the two-two-row counterfamily with k>2i+j and i>j>0; §2.4, p.8, gives the strong-positivity counterexample. §2.5 and Remark4.10 distinguish relaxed indices (at most1 in that range). The appended Mulmuley text, printed pp.18–20, states relaxed SH(a)/(b), PH2 and PH3 and the conditional relaxed-decision result. These passages were inspected in the supplied source/primary PDF. They refute earlier strong saturation, not the variable-height polynomial-index assertions for triple rectangles asked here.

### S07. Kronecker complexity

Ikenmeyer, C., Mulmuley, K. D., & Walter, M. (2017). *On vanishing of Kronecker coefficients* (arXiv:1507.02955v2). [Primary PDF](https://arxiv.org/pdf/1507.02955).

Theorem1.3, printed p.7, establishes NP-hardness of positivity with unary input. Theorem1.5 concerns a #P subclass; Theorem1.7 and §1.6 give many holes and their construction. The introduction and these statements/definitions were inspected. The theorem is not a hardness theorem for the one-parameter triple-rectangular sequence, and the explicit nonrectangular restrictions in the hole theorem cannot be dropped.

### S08. Plethysm complexity

Fischer, N., & Ikenmeyer, C. (2020). The computational complexity of plethysm coefficients. *Computational Complexity, 29*, Article8. [DOI](https://doi.org/10.1007/s00037-020-00198-4). [Primary preprint](https://arxiv.org/pdf/2002.00788).

Theorems3.1 and3.2, printed p.5, establish positivity NP-hardness and counting #P-hardness for fixed inner degree at least3. Proposition3.3, p.5, gives polynomial time at fixed outer degree; footnote3 distinguishes the encoding scope. Theorem3.4, p.6, states GapP-completeness. The full supplied results section and primary statements were read. These results neither rule out the fixed-outer formulas nor identify a uniform positive rule for the restricted stable-tail families. A #P-hardness statement does not itself show nonmembership in #P.

### S09. Pak–Panova–Swanson

Pak, I., Panova, G., & Swanson, J. P. (2026). *A combinatorial interpretation for certain plethysm and Kronecker coefficients* (arXiv:2511.02312v3, July27). [Primary PDF](https://arxiv.org/pdf/2511.02312).

Theorems1.1–1.2, printed pp.1–2, count marked KOH/GOS trees for two-row **output** partitions. Lemma2.1 reduces the inner shape in that output range. §2.2, p.5, discusses FP/#P via degree-sized dynamic programming. The KOH/GOS identities and marked-tree proofs are §§3–5, specifically Theorems3.1/3.6, Proposition3.9, Lemmas4.1/4.2 and Theorem5.2. The plethysm branch read the full invoked proofs; root inspected the statements, scope, complexity discussion and coefficient-extraction reduction. The scalar outer-six implementation credits this theorem. Two-row output must not be confused with a two-row tail below an additional first row.

### S10. Sarkar

Sarkar, S. (2026). *Stability of plethysm coefficients and modified polynomial induction* (arXiv:2610.07929v2, October14). [Version record](https://arxiv.org/abs/2610.07929v2).

The supplied author LaTeX is the primary text available in this run. TheoremD gives the stable coefficient formula under m≥λ1 and n≥floor((|λ|+λ1)/2), subject to λ[mn] being a partition; TheoremE gives explicit positive formulas through width4. The complete main-theorem section was read; the prior GCT_PLETH proof checks and exact B5/B6 tables support T-012/T-013. Those width5/6 consequences are not attributed to Sarkar's TheoremE. Direct retrieval of the current PDF was disabled; no mirror is substituted for a proof reading.

## 4. Positive formulas, Cox rings and canonical maps

### S11. Fixed outer degree, including h4[hn] and h5[hn]

Kahle, T., & Michałek, M. (2016). Plethysm and lattice point counting. *Foundations of Computational Mathematics, 16*, 1241–1261. [DOI](https://doi.org/10.1007/s10208-015-9275-7). [Primary author version](https://arxiv.org/pdf/1408.5708).

Theorem1.1, printed p.2, supplies piecewise quasipolynomial formulas for fixed outer shape and explicitly computed outer degrees3,4,5. Proposition2.8, Proposition3.4, Definition3.6 (p.10) and §3.4 locate the character/vector-partition method. The theorem and relevant construction passages were read. These are already published formulas for h4[hn] and h5[hn]; the claim that such formulas were first produced in GCT_PLETH would be false. A signed formula is distinguished from that run's positive-polytope routing. Theorem4.2 and Conjecture4.3 concern leading asymptotics, not an effective basis for arbitrary stable tails.

Howe, R. (1987). (GLn, GLm)-duality and symmetric plethysm. *Proceedings of the Indian Academy of Sciences—Mathematical Sciences, 97*, 85–109. [Primary publisher record](https://doi.org/10.1007/BF02837817).

The primary abstract explicitly reports outer degrees2,3,4; the full official PDF returned403/failed access. Thus Howe's detailed formulas are credited through the primary record and corroborating sources, with no claim that their complete original proofs were read in this run. Foulkes's1954 source, *Plethysm of S-functions*, *Philosophical Transactions of the Royal Society A, 246*, 555–591, DOI10.1098/rsta.1954.0008, is a further historical source cited by the inspected papers; its full Royal Society PDF was also inaccessible. The precise modern fixed-outer theorem above is the directly inspected source used here.

### S12. Hook and near-hook formulas

Langley, T. M., & Remmel, J. B. (2004). The plethysm s_λ[s_μ] at hook and near-hook shapes. *The Electronic Journal of Combinatorics, 11*(1), R11. [DOI](https://doi.org/10.37236/1764). [Primary PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v11i1r11/pdf/).

Inspected: introduction pp.1–3; Theorem3.1 p.6; Theorems4.2/4.3 pp.10–11; full Lemma4.4 proof pp.11–12; Theorem4.5 pp.12–13, Corollary4.6 p.14 and Theorem4.8 pp.24–25. The complete long proof of Theorem4.5 was not independently read. The shape and inner-partition restrictions are retained; these statements are not a uniform positive formula for all three-row stable tails.

Paget, R., & Wildon, M. (2021). *Plethysms of symmetric functions and representations of SL2*. *Algebraic Combinatorics, 4*(1), 27–68. [DOI](https://doi.org/10.5802/alco.150). [Author copy](https://kar.kent.ac.uk/87806/11/ALCO_2021__4_1_27_0.pdf).

Theorem10.1, printed p.59, and Table1 classify specified SL2 plethystic equivalences involving two-row, two-column and hook shapes. The statement and opening reduction were read; the complete case-by-case proof is not claimed checked. An equivalence classification is not a general positive coefficient formula. The related de Boeck–Paget–Wildon article, *Transactions of the AMS, 374* (2021), 8013–8043, DOI10.1090/tran/8481, was located as a further source; no uninspected theorem from it is invoked.

### S13. Cox ring

Castravet, A.-M., & Tevelev, J. (2006). Hilbert's14th problem and Cox rings. *Compositio Mathematica, 142*, 1479–1498. [Primary author version](https://arxiv.org/pdf/math/0505337).

Remark3.9, author-version printed p.9 (published p.1487), identifies the relevant blow-ups' total coordinate rings with Grassmannian Plücker rings. PNEW-011 specializes this known statement and proves the exact degree and S_m-action dictionary used here. Gr(2,7), not a larger unrelated Grassmannian, is the six-frame scalar case. The existence of a standard monomial basis does not make it an S6-permutation basis or solve all isotypic multiplicities.

### S14. Canonical-map rank sources

Cheung, M., Ikenmeyer, C., & Mkrtchyan, S. (2015). *Symmetrizing tableaux and the5th case of the Foulkes conjecture* (arXiv:1509.03944). [Primary PDF](https://arxiv.org/pdf/1509.03944).

Theorem6(a),(b), printed p.3, supplies the h_(5,5) kernel and h_(6,5) injectivity. The exact eight kernel labels are retained in R-NEW-002. The source statement and proof/certificate description were inspected; the largest published matrices were not recomputed here.

Ikenmeyer, C. (2015). *On McKay's propagation theorem for the Foulkes conjecture* (arXiv:1509.04957). [Primary PDF](https://arxiv.org/pdf/1509.04957).

Theorem1.3, printed p.2, is the propagation result used in the full rank laws. The source statement/proof was checked in conjunction with the companion sources.

Jacob, J. (2004). *Representation theory of association schemes* (doctoral dissertation, RWTH Aachen). [Primary repository PDF](https://publications.rwth-aachen.de/record/51990/files/Jacob_Juby.pdf).

Definition4.1.1, printed p.92, fixes the canonical map convention; printed p.99 gives the43-by43 determinant2^223·3^67 needed for the a=4 square case. That determinant computation was independently replayed exactly/modularly. The Müller–Neunhöffer primary note, §4, final paragraph on author-version printed p.4, was also inspected for propagation and conventions.

Müller, J., & Neunhöffer, M. (2005). Some computations regarding Foulkes' conjecture. *Experimental Mathematics, 14*(3), 277–283. https://doi.org/10.1080/10586458.2005.10128928. [Primary author PDF](https://www.math.rwth-aachen.de/homes/Max.Neunhoeffer/Publications/pdf/foulkes.pdf). During final bibliography verification, the author publication record confirmed the journal metadata, and the eight-page author PDF's §4, Proposition4.1 and final paragraph, printed p.4, reconfirmed the exact locator and Jacob attribution. This is not a new full-paper proof reading.

Sra, S. (2026). *The q-Foulkes problem III: On Foulkes' conjecture with a graded inner factor* (hexagon:2610.00724v1). [Author-hosted PDF](https://hexagonmath.org/pdf/2610.00724v1). [Author release page](https://suvrit.github.io/papers/qfoulkes3/).

Theorem1.3, printed p.2, and the entire Lemma2.1/proof, pp.3–5, were read by root and a second reviewer. R-NEW-002 keeps the map direction and the window n≥9 (a=4), n≥16 (a=5) explicit. The a=5 square kernel lies outside those windows. The source's exact title is retained in the rank-law proof; no unpublished propagation is substituted.

### S15. Further asymptotics and errata leads

Kuppel, T. (2025). *Asymptotics of plethysm* (arXiv:2509.06424v1). [Primary PDF](https://arxiv.org/pdf/2509.06424).

The introduction's Theorem5 and Proposition7/Thm4 discussion, pp.2–3, were inspected after following Kahle–Michałek's leading-term references. They concern fixed outer degree and stretching the inner degree/output, with explicit exceptions. They are not a solution to the varying-outer-tail positive-basis gate. No theorem from this paper is needed for the current proofs.

Briand, E. J. (2025). *Database of piecewise quasipolynomial functions* (Version0.3.0) [Data set]. Zenodo. [DOI](https://doi.org/10.5281/zenodo.15591322). [Primary README](https://zenodo.org/records/15591322/files/README.md?download=1).

The README's source list flags an error in Macdonald I.8, Example9 for s_(1,1,1)[h_n], corrected using Chen–Garsia–Remmel (1984), Theorem4.1, DOI10.1090/conm/034/777698. It also identifies Manivel–Michałek (2015), TheoremA.2, for s3[e_n]. The linked `errors.pdf` could not be fetched (Unicode400). This lead does not establish an error in Kahle–Michałek's general theorem. The present exterior-duality witnesses use the involution/Cauchy identity, with exact independent coefficient checks, rather than the flagged closed formula.

## 5. Kronecker invariants, geometry and the no-occurrence boundary

### S16. The classical n=3 ring

Bremner, M. R., & Hu, J. (2012). *Fundamental invariants for the action of SL3(C)^3 on3×3×3 arrays* (arXiv:1112.2949v2). [Primary PDF](https://arxiv.org/pdf/1112.2949v2).

Theorem2.4, printed p.5, and the introduction credit Vinberg's polynomial invariant ring of ordinary degrees6,9,12. Root and branch inspected the theorem. The branch also checked Vinberg, E. B. (1976), *The Weyl group of a graded Lie algebra*, *Mathematics of the USSR-Izvestiya, 10*(3), 463–495, DOI10.1070/IM1976v010n03ABEH001711, §9.1, table item2, English printed p.491, in the primary author-hosted scan. Regrading by degree/3 gives H3 as used in K-001.

Stembridge, J. R. (2014). *Appendix to Generalized Stability of Kronecker Coefficients*. [Author PDF](https://websites.umich.edu/~jrs/papers/kron-app.pdf). TableC.1/RemarkC.1, printed p.3, and equation(C.1), p.4, supply known low-degree n=4 coefficients and complementary-rectangle information. Those values are calibrations, not a complete H4 rational numerator.

### S17. Quasipolynomiality and the density theorem

Baldoni, V., & Vergne, M. (2015). *Multiplicity of compact group representations and applications to Kronecker coefficients* (arXiv:1506.02472v1). [Primary PDF](https://arxiv.org/pdf/1506.02472).

Theorem29, p.21, and Proposition31, p.23, give the closed-cone/all-nonnegative-integer quasipolynomial statement used for the finite H4 expression; the properness discussion is p.20. §5.1, pp.51–53, Proposition60, Lemma61, Theorem63 and Propositions65–67 supply the fixed-embedding full-cone branching statement used in PNEW-009. The exact hypotheses and relevant proofs were read during that theorem's review. The n=3 calibration also appears pp.5,70–71. No uniform bounds in a varying embedding follow merely from a theorem with that embedding fixed.

### S18. Universal versus actual denominator

Derksen, H. (2005). Universal denominators of Hilbert series. *Journal of Algebra, 285*(2),586–607. [DOI](https://doi.org/10.1016/j.jalgebra.2004.10.029). [Primary author version](https://arxiv.org/pdf/math/0305111).

Theorem1.10, journal pp.589–590, describes the universal denominator through fixed loci; its full proof was read. Example1.4 illustrates cancellation for the actual Hilbert series in a nonreduced example. Those passages were read expressly to test the possible shortcut from a single high-order stabilizer to an actual pole. They do not justify that shortcut. K-018 strengthens a canonical-normalization obstruction but cannot substitute for a global residue calculation.

### S19. Tensor/K3 geometry

Bhargava, M., Ho, W., & Kumar, A. (2016). Orbit parametrizations for K3 surfaces. *Forum of Mathematics, Sigma, 4*, Article e18, 1–86. https://doi.org/10.1017/fms.2016.12. [Primary journal PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EC421308C92022B8833CBEF1E7CDF567/S2050509416000128a.pdf/orbit_parametrizations_for_k3_surfaces.pdf). The primary journal text's Theorem4.7 (printed p.22) and Corollary4.4 (p.21) were inspected for the4×4×4 tensor geometry and generic stabilizer. They are not an explicit Hilbert-series formula for H4. The proof here uses its own exact stabilizer certificates for the special fixed loci.

### S20. Ordinary positivity is weaker than the strict indices

Amanov, A., & Yeliussizov, D. (2023). *Fundamental invariants of tensors, Latin hypercubes, and rectangular Kronecker coefficients* (arXiv:2202.11059v2). [Primary PDF](https://arxiv.org/pdf/2202.11059v2). Theorem8.12, printed p.31, gives the even-degree positivity range s≥2(n+1)^2 discussed in K-017. The Kronecker branch inspected the exact statement. This is not a bound for the off-residue evaluations in the requested strict saturation index.

### S21. No-occurrence and multiplicity obstructions

Bürgisser, P., Ikenmeyer, C., & Panova, G. (2018). *No occurrence obstructions in geometric complexity theory* (arXiv:1604.06431v3). [Primary PDF](https://arxiv.org/pdf/1604.06431).

Theorem1.4, printed p.3, shows the stated occurrence inclusion in the n≥m^25 range. The introduction and definitions were read. The paper explicitly distinguishes this from the multiplicity-obstruction strategy. It concerns coordinate rings of the actual orbit closures, not every larger ambient representation.

Ikenmeyer, C., & Panova, G. (2017). Rectangular Kronecker coefficients and plethysms in geometric complexity theory. *Advances in Mathematics, 319*, 40–66. [DOI](https://doi.org/10.1016/j.aim.2017.08.024). [Primary author version](https://arxiv.org/pdf/1512.03798).

Theorem1.6, printed p.3, is the rectangular-vanishing obstruction in the n>3m^4 range; Theorem1.8/Corollary1.9/Theorem1.10, p.4, specify the positive regimes and exceptions. The introductory multiplicity comparison and these source statements were inspected. The determinant-orbit/closure multiplicities, symmetric rectangular coefficients and ordinary rectangular coefficients have distinct roles; a triple rectangle is not automatically an actual determinant-closure multiplicity. The present results do not remove multiplicity obstructions.

### S22. Transportation-polytope literature

Brualdi, R. A., & Csima, J. (1977). Fibonacci sequence and extremal stochastic matrices. *The Fibonacci Quarterly, 15*(4), 333–336. [Primary scan](https://www.fq.math.ca/Scanned/15-4/brualdi.pdf). The whole four-page paper was read for its Fibonacci-denominator construction. Kravtsov, V. M. (2006), *Description of the types of maximum noninteger vertices of the polyhedron in the three-index axial assignment problem*, Russian printed pp.1908–1912, was read in full; the English translation is46(10),1821–1825, DOI10.1134/S0965542506100174. “Maximum” there concerns support size3n−2, not a proof of the determinant-order upper bound proposed in the prompt.

Kravtsov (2010), *On a characterization of noninteger vertices of the relaxational polyhedron in the multi-index axial assignment problem*, English50(9),1615–1626, DOI10.1134/S0965542510090125, was read through the first four primary pages during the initial route; the whole paper is not thereby claimed read. Kravtsov, M. K., & Lukshin, E. V. (2008), *Polyhedral combinatorics of multi-index axial transportation problems*, *European Journal of Operational Research, 189*(3),920–938, primary publisher record S0377221707006674, was located as an exponential-denominator lead; no inaccessible theorem from it is invoked.

Franks–Reichenbach, arXiv:2102.06652v3, equation(2.5)/Lemma2.5, printed pp.14–15, was inspected for critical free-support tensors and exponential stabilizer constructions. Line-stochastic three-dimensional arrays in the2026 Linial–Luria–Trakhtman lead are a different polytope from the axial one-coordinate-margin polytope used here. The K-018 search audit continues from these sources without presuming priority.

The follow-up primary audit is `reviews/axial_denominator_primary_scope_audit.md`. It corrects the2008 DOI to10.1016/j.ejor.2007.02.059, confirms M. K. Kravtsov/E. V. Lukshin for2008 and V. M. Kravtsov for2007/2010, and reads all of the2010 Section3. Its Theorems4,5,6 (Russian printed pp.1703–1704) give the precise dyadic constructions compared there. Franks–Reichenbach, *Barriers for recent methods in geodesic optimization*, CCC2021 Article13, DOI10.4230/LIPIcs.CCC.2021.13, Lemma2.5 is on printed p.13:15; it credits Kravtsov2007 Theorem1(k=0) and Kravtsov–Lukshin2005 Theorem9. The2008 Section4 remains unread, so no priority claim for the larger K-018 rate is made.

## 6. Nonstandard algebra sources

### S23. The actual integral order

Blasiak, J., Mulmuley, K. D., & Sohoni, M. (2013). *Geometric complexity theory IV: Nonstandard quantum group for the Kronecker problem* (arXiv:cs/0703110v4). [Primary PDF](https://arxiv.org/pdf/cs/0703110).

Exact locators: §2.1 p.16 (A=Z[v,v^−1]); equation(22) p.20 (Hecke relation); §3.1 p.21 (C',C conventions); Definition11.1/equation(93) p.59 (the unsaturated P-generated subalgebra); Remark11.9 p.61 (abstract specialization versus ambient image); Theorem11.16 pp.65–66 (rank-three freeness); §11.8/Remark11.19 p.67 (rank-four dimension114 and positivity uncertainty). These passages were inspected directly. A conflicting introductory q-power typo is documented, with a direct consistency check, in `branches/nonstandard/N009_definition_literature_audit.md`.

### S24. Blasiak's later nonstandard papers

Blasiak, J. (2015). Nonstandard braid relations and Chebyshev polynomials. *Journal of Algebra, 423*, 375–404. [DOI](https://doi.org/10.1016/j.jalgebra.2014.09.035). [Author version](https://arxiv.org/pdf/1010.0421).

Definition2.2 and §§2.1–2.3, pp.3–4, independently confirm the P-generated order and C'/C convention. Theorem3.7/Corollary3.8, pp.13–14, concern the generalized rank-three/dihedral family. They do not establish full rank-four A-freeness.

Blasiak, J. (2012). *Representation theory of the nonstandard Hecke algebra* (arXiv:1201.2209v2). [Primary PDF](https://arxiv.org/pdf/1201.2209). Theorem5.1, §6 and Corollary7.1 concern the nonstandard Temperley–Lieb quotient; rank-four dimension89 is not the full dimension114 order of N-009. The exact distinction was checked.

The bounded nonfreeness-priority search, search phrases, localization boundary and source convention audit are retained in the separate N009 audit. It found no published126-generator obstruction; this is recorded as a search outcome, not proof of uniqueness of discovery.

## 7. Historical and geometric sources

The complete finding dictionary is `branches/root/grothendieck_dictionary.tex`. Its exact locators are also tabulated there. The inherited GCT_PLETH source audit was read in full and is cited as **verified background**, not represented as a new visual reading of its absent local PDFs. The current run additionally inspected the editor-maintained SGA3 ExposéVIII and the SGA6 VII §2 transcription, and re-read the Stacks Fitting statements and proofs.

- Demazure, M., & Grothendieck, A. (Eds.). (1970). *Schémas en groupes (SGA3)*. ExposéI §4.5, Definitions4.6.1/4.6.3, Propositions4.7.2/4.7.3; ExposéVIII Definition1.1, Theorem1.2, Corollaries1.3/1.4 and Proposition2.1. [Editor-maintained VIII PDF](https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp8-8nov09.pdf), especially PDFpp.3,8. This is a typeset primary edition with original marginal pagination, not manuscript-scan inspection.
- Berthelot, P., Grothendieck, A., & Illusie, L. (Eds.). (1971). *Théorie des intersections et théorème de Riemann–Roch (SGA6)*. LNM225. ExposéV Definition2.1, Lemma2.2.1,2.4.1,3.2–3.4,3.10, Proposition4.2/Definition4.4, Proposition4.8/Corollary4.9; ExposéVI Theorem3.3; ExposéVII Propositions2.5/2.7 and Corollary2.8. The whole VII §2 transcription was read. The regular-immersion/self-intersection formula is not mislabelled as a complete equivariant localization theorem.
- Grothendieck, A., & Dieudonné, J. (1960). *Éléments de géométrie algébrique I*. *Publications Mathématiques de l'IHÉS, 4*,5–228. §§1.3.7–1.4.1, pp.86–92; §§9.5.1–9.5.4, pp.176–177, and9.5.8–9.5.9,p.178. [Primary scan](https://www.numdam.org/item/PMIHES_1960__4__5_0.pdf). Carried from the supplied complete source audit.
- Grothendieck, A., & Dieudonné, J. (1961). *Éléments de géométrie algébrique II*. *Publications Mathématiques de l'IHÉS, 8*. §§2.4.1–2.4.2,p.28;2.5.2/2.5.4,p.31;2.5.7–2.5.9,p.32. [Primary scan](https://www.numdam.org/item/PMIHES_1961__8__5_0.pdf). Carried verified background.
- Grothendieck, A. (1961). *Techniques de construction et théorèmes d'existence en géométrie algébrique IV: Les schémas de Hilbert*. Séminaire Bourbaki, Exposé221. Theorems3.1/3.2,pp.259–260; paragraph after Proposition3.8,p.265; Remarks3.9,p.266. [Primary scan](https://www.numdam.org/item/SB_1960-1961__6__249_0.pdf). The hypotheses of the Quot/Hilbert theorem are retained; no automatic flatness of a closure is asserted.
- Deligne, P. (1980). La conjecture de Weil II. *Publications Mathématiques de l'IHÉS, 52*,137–252. §§1.1.7,pp.150–151; Definitions1.2.1/1.2.2,p.153;1.2.3–1.2.5,p.154. DOI10.1007/BF02684780. These exact purity/Frobenius conventions are inherited audited background; N-006 checks its eigenvalues directly.
- SGA4 ExposéXV, Proposition1.6/Definition1.7 and Corollary2.2, supplies the affine-space cohomology convention in the inherited audit. Original scans were not newly inspected.
- The Stacks Project. (2026). §15.8, tag[07Z6](https://stacks.math.columbia.edu/tag/07Z6), especially Lemmas15.8.2,15.8.4(3),15.8.7,15.8.8; Lemma31.9.6, tag[05P8](https://stacks.math.columbia.edu/tag/05P8). Statements and relevant proofs re-read in this run. An unverified EGA Fitting locator is not invented.
- Macdonald, I. G. (1995). *Symmetric functions and Hall polynomials* (2nd ed.). Oxford University Press. I(4.2),p.62;(4.3),p.63;(7.3),pp.113–114;(7.5)–(7.6),p.114; AppendixA(5.3)–(5.4),p.155;(5.6),p.156;(7.2)/(7.4),p.160. Exact source audit carried from GCT_PLETH; the known exterior-cube closed-form erratum is separately noted in S15.
- Akin, K., Buchsbaum, D. A., & Weyman, J. (1982). Schur functors and Schur complexes. *Advances in Mathematics, 44*,207–278. DOI10.1016/0001-8708(82)90039-1. TheoremsII.2.16,p.232, andIII.1.4,pp.245–246. Their `L_(a)=Λ^a` convention is translated explicitly. Integral Cauchy means a filtration, not an unqualified direct sum.
- Zibrowius, M. (2015). Symmetric representation rings are λ-rings. *New York Journal of Mathematics, 21*,1055–1092. Main theoremp.1056, Definition1.2p.1060, §3.1pp.1068–1069. The metabolic Grothendieck–Witt quotient must be distinguished from naive split quadratic/Witt constructions. The γ-filtration paper arXiv:1411.3198v2, Proposition3.3,pp.19–20, supplies the audited broader Z[1/2] splitting statement.

Archive corrections are identified by the exact supplied cote/scan and GCT_PLETH A-identifiers in the dictionary. Alpöge's GRH theorem is not an input to any new result here; no numerical prime estimate or Lean locator is borrowed without its supplied certificate. Masullo's draft is not used. Thus no hidden conditional consequence of either is included.

## 8. Unfinished source checks are not mathematical assumptions

The access gaps for full Howe/Foulkes texts, the later2011 GCTVI revision, and a few transportation references are explicitly retained. No theorem whose exact hypotheses remain inaccessible is used as a new proof input. The current proofs instead use the precisely identified accessible statements and their direct calculations. The final package must retain these limitations rather than declare the literature search exhaustive.

## 9. Further primary sources for the modular Kronecker route

### S25. Weighted Grassmannian cancellation

Corti, A., & Reid, M. (2002). *Weighted Grassmannians* (arXiv:math/0206011v1). [Primary author version](https://arxiv.org/pdf/math/0206011). Section2, items(iii)–(v), printed p.4; Proposition2.1 and equation(2.4), pp.5–6; Pfaffian numerator p.8 and charts pp.7–8. Root read the complete proposition and proof and the indicated charts; the specialist review independently checked them. The ring and general weighted Pfaffian resolution are known. K-022 proves its particular all-dyadic weight specialization, exact opposite local residues and cancellation, without a historical-priority claim.

### S26. The known root-number character identity

Adin, R. M., Hegedüs, P., & Roichman, Y. (2025). Higher Lie characters and root enumeration in classical Weyl groups. *Journal of Algebra, 664*(Part B),26–72. [DOI](https://doi.org/10.1016/j.jalgebra.2024.10.013). [Primary arXiv version2312.08904v2](https://arxiv.org/pdf/2312.08904v2). Definition2.1 and Theorem2.2, printed p.5, were read in full. They state the symmetric-group root-number identity as a sum of higher Lie characters and attribute it to Scharf. For cubic roots the only allowed cycle lengths are1 and3, and Lie_3 is the Schur module(2,1). K-023 gives the explicit cycle-index specialization needed for the rectangular invariant multiplicities, with coordinate duality and grading checked. The general identity is not new.

Scharf, T. (1991). Die Wurzelanzahlfunktion in symmetrischen Gruppen. *Journal of Algebra, 139*(2),446–457. This original article is credited through the inspected primary modern theorem; its original full proof was not obtained. Schocker, M. (2003), *On the root symmetry of higher Lie characters*, *Archiv der Mathematik, 80*,337–346, DOI10.1007/s00013-003-0790-4, independently credits Scharf in its primary abstract. Only that abstract was inspected, not the full paper.

### S27. Scope of the targeted novelty search

Searches on21November2026 included Kronecker/PH3, rectangular Kronecker Hilbert denominators and exponential periods, cyclic tensor traces, higher Frobenius–Schur indicators, free Lie-module symmetric algebras, and vector-plus-(2,1)-Schur-module invariant rings. The searches located the known higher-indicator/root-character framework and Derksen's denominator distinction. They did not locate the particular hook-chain modular transfer to an exponential actual tensor denominator. This is a bounded search record, not a claim to have excluded all prior literature. No unrelated search result is used as a mathematical source.

## 10. Parameter-notation correction,21November2026 23:08UTC

The complete source definition was re-read in the supplied GCTVI author LaTeX, the introductory relaxation paragraph and §3.4 subgroup-restriction specification (printed p.52), together with ALPOGE_GCT P-F60r–u. The value n²+5n is the unified rank(x), obtained from the ranks of H=GL_n×GL_n and G′=GL_(n²), plus the two weight heights. It is not the introductory h, which uses dim G′ and is n⁴+O(n) for this realization. Both are polynomial in n, so the exponential denominator obstruction refutes both polynomial-bound readings. Earlier checkpoint04 prose called n²+5n h; that notation is corrected in the current paper and registers. No pole or index theorem changes.

## 11. Primary sources for the later reductions and rational-order construction

### S28. Polynomial Hermite forms

Labahn, G., Neiger, V., & Zhou, W. (2017). Fast, deterministic computation of the Hermite normal form and determinant of a polynomial matrix. *Journal of Complexity, 42*,44–71. [DOI](https://doi.org/10.1016/j.jco.2017.03.003). [Primary author version](https://arxiv.org/pdf/1607.04176), version2 dated29March2017. Root and the nonstandard branch inspected §1, printed p.1, for monic pivots, remainder inequalities and row/column conventions, and §3, printed p.8, for diagonal uniqueness up to constants and monic normalization. The author's publication list independently confirms the final journal citation. Polynomial Hermite reduction is credited as a standard method; N-019 proves the particular maximal-scaling equivalence and balanced triple directly.

The exact source comparison and bounded dual-engine search are in `branches/nonstandard/N019_literature_scope.md`. No matching114-element table was located in those searches; this does not establish novelty or priority.

### S29. Slice neighborhoods and coherent localization

Luna, D. (1973). Slices étales. *Mémoires de la Société Mathématique de France, 33*,81–105. [DOI and primary scan](https://www.numdam.org/item/10.24033/msmf.110.pdf). Root and the Kronecker branch read the complete SectionIII.1 slice theorem and proof, the preceding lemma and Remarks1–4, printed pp.96–98. Remark4, p.98, states the subgroup-neighborhood consequence used to prove openness of the finite prime-to3 stabilizer locus. The closed-orbit hypothesis is retained. The finite stratification in III.2, Corollaries3–4, p.100, was also inspected; the specific coset counts in K-028 are justified directly by quasi-finite incidence and constructibility.

Quillen, D. (1973). Higher algebraic K-theory: I. In H. Bass (Ed.), *Algebraic K-theory I: Higher K-theories* (Lecture Notes in Mathematics, Vol.341, pp.85–147). Springer. [Primary paper scan](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Quillen-Higher-I.pdf). Root read Section7.3, Proposition3.2 and its complete short proof, PDFpp.43–44, for localization of coherent-sheaf K-prime groups. This is not a claim to have reread the whole higher localization theorem. K-027 gives the elementary graded degree-zero argument it needs; K-028 supplies the finite-group-equivariant extension and dimension induction. Coherent G0 on a singular quotient is not silently identified with vector-bundle K0 or its lambda operations.

The later targeted searches included cyclic symmetry and Kronecker Hilbert fixed loci, coherent localization with grading, and balanced triples with Hermite forms. They did not locate the exact K-026–K-028 or PNEW-014 constructions. That limited search outcome is not a proof that no earlier form exists; all classical structural inputs above are expressly credited.

## 12. S30: finite subgroups carrying all components

Borel, A., & Serre, J.-P. (1964). Théorèmes de finitude en cohomologie galoisienne. *Commentarii Mathematici Helvetici, 39*, 111–164. Lemma5.11, printed p.152, original PDF page42. [Primary author-hosted scan](https://www.college-de-france.fr/media/jean-pierre-serre/UPL6720771035987925133_Borel_Serre_Theoremes_de_finitude.pdf). Root read the statement and complete displayed proof; only its complex linear-group case is used.

Lucchini Arteche, G. (2017). Extensions of algebraic groups with finite quotient and nonabelian 2-cohomology. *Journal of Algebra, 492*, 102–129. https://doi.org/10.1016/j.jalgebra.2017.08.026. Theorem3.2, arXiv:1503.06582v3 printed p.18; proof Steps1–4, pp.19–23, and preceding Lemma3.3 fully read by root. This modern primary statement supplies the same existence result in greater generality. Neither theorem is a new result of this work.

K-030 proves a finite-group conjugacy-class lemma and removes all finite stabilizer exceptions. K-031 combines it with the classical finite-subgroup theorem and Luna strata to remove all stabilizer exceptions. The remaining exact-pole gate is solely the collision-supported coherent class; K-029 proves the support can occur. No exact all-dimensional dyadic pole is claimed.

## 13. N-020 and the known rank-three presentation

N-020's precise abstract D=0 fibre, trace identity, radical dimensions and corrected explicit section are proved from the certified actual rank-four table. The abstract-specialization/ambient-image distinction was already stated at the ordinary specialization in GCT IV, Proposition11.8 and Remark11.9, printed p.61; it is not a new general phenomenon. See the bounded source audit `branches/nonstandard/N020_literature_scope.md`.

Blasiak, J. (2015). Nonstandard braid relations and Chebyshev polynomials. *Journal of Algebra, 423*, 375–404. https://doi.org/10.1016/j.jalgebra.2014.09.035. Root opened arXiv:1010.0421v2 and read the complete Theorem3.7 proof and Corollary3.8 on printed pp.13–14, plus Remark3.6. The ten-word rank-three presentation is known. N-020 checks its injection into the actual rank-four sign fibre; it does not claim a new abstract rank-three presentation. The nil-ideal and Jacobson-radical criteria are standard. No absence-of-prior-art inference is drawn from the targeted searches.

## 14. S32: rectangular exterior symmetry and its precise scope

Briand, E., Orellana, R., & Rosas, M. (2015). Rectangular symmetries for coefficients of symmetric functions. *The Electronic Journal of Combinatorics, 22*(3), P3.15. https://doi.org/10.37236/4808. Corollary8 and Remark9, printed p.10, give the relevant complement identity and exterior interpretation; the preceding proof is Theorem6, pp.8–9. Root read these journal-PDF passages, the complete branch proof note and its checker, then replayed all checks. Only the correct multiplicity identity and necessary divisibility are used: the sufficiency wording in Remark9 is false at dimension3, exterior degree6, where the exact S6 sum gives g((3,3),(3,3),(3,3))=0. The complement theorem is unaffected. The full source/proof scope and Stembridge credit appear in `branches/plethysm/explorations/tensor_exterior_constraints.md`.

The known bound k_n(s)≤binom(s³,ns), vanishing for n>s², square-boundary value1 and complement symmetry distinguish actual coefficients from PNEW014's formal model. They do not yet control strict off-residue constituent values. This is a concrete attempted route and source-scope correction, not a claim of a new rectangular-symmetry theorem or a resolved strict-index gate.

## 15. Finite restriction and the amplified normalization

Bate, M., Geranios, H., & Martin, B. (2019). Orbit closures and invariants. *Mathematische Zeitschrift, 293*(3–4),1121–1159. https://doi.org/10.1007/s00209-019-02228-6. Theorem1.1, p.1 of arXiv:1604.00924v2 (5December2018), states the finite fixed-quotient restriction criterion and attributes its characteristic-zero form to Luna (1975), *Adhérences d’orbite et invariants*, *Inventiones Mathematicae,29*,231–238. Root read that statement, its attribution, and §2.1's disconnected-group convention; the publisher confirms the final metadata. The original Luna publisher record confirms DOI10.1007/BF01389851; both the article and direct-PDF request expose a subscription preview rather than the proof. Root has not read Luna's original1975 proof or the complete general positive-characteristic proof. K-032 provides its own complete nullcone/finite-module proof for the specific group and grading, then proves the family-specific birationality and graded formula. No priority claim follows from this source search.

## 16. Small integer witnesses and dimension-table exponents

Papadimitriou, C. H. (1981). On the complexity of integer programming. *Journal of the ACM, 28*(4),765–768. https://doi.org/10.1145/322276.322287. Root opened the primary four-page journal scan at https://ii.uni.wroc.pl/~aje/WordEq2015/papers/Papadimitriou.pdf and read Lemma1, p.766, and the main theorem/proof, p.767. The standard determinant and bounded-witness method is credited; N-021 proves its particular positive-associativity matching reduction directly. Its finite bound does not evaluate the optimum. See `branches/nonstandard/N021_literature_scope.md` for the bounded search and the exact integral-input restriction.

## 17. S35: the classical quotient underlying the cyclic diagnostic

Heusener, M., & Porti, J. (2004). The variety of characters in PSL2(C). *Boletín de la Sociedad Matemática Mexicana*, third series, *10*, special issue,221–237. Primary author version: https://arxiv.org/pdf/math/0302075, version2 dated1August2008. Root read Proposition4.2 and its complete proof, printed p14, and Example4.4, equation(8), with its complete computation and Remark4.5, printed p15. The even-sign-change quotient with equation W²=XYZ is explicitly known.

Tillmann, S., & Yao, Y. (2022). *On the topology of character varieties of once-punctured torus bundles*. arXiv:2206.14954. https://arxiv.org/pdf/2206.14954. Root read the complete Section2.4, equations(2.11)–(2.12), printed p7, giving the same square/product map and referring to Heusener–Porti. The checked locator is this author version; no original journal-page reading is claimed.

R-DIAG-001 applies a chosen grading and cyclic permutation to this familiar quotient and proves its exact local coefficients directly. It blocks a proposed symmetry-to-integrality shortcut. It is not a tensor-ring counterexample, does not satisfy the auxiliary-pole premise of PNEW-013, and leaves the main cancellation gate unchanged.

## 18. S36: binary-trilinear covariants and K-033

Holweck, F., Luque, J.-G., & Thibon, J.-Y. (2012). Geometric descriptions of entangled states by auxiliary varieties. *Journal of Mathematical Physics,53*,102203. https://doi.org/10.1063/1.4753989. Root read the complete Sections5.1–5.2, printed pp15–17 of https://arxiv.org/pdf/1204.6375 (version2,8May2012). Section5.2's displayed rational covariant series is exactly K-033g after cancelling the cubic factor. Its classical attribution to Le Paige1881 is retained; no reading of the original Le Paige proof is claimed. The full rational Weyl identity is independently verified in the retained code.

K-033 specializes this known series to an actual n10 fixed-component normalization and evaluates its density and principal part. The precise specialization and finite geometry are proved and checked here; no claim of priority follows from the source search. The computed normalization series alone does not exclude odd inertia on the original component or determine its conductor contribution.

## 19. S37: proper Hilbert series for the actual hook ring

Kurano, K., Sato, E.-i., Singh, A. K., & Watanabe, K.-i. (2009). Multigraded rings, diagonal subalgebras, and rational singularities. *Journal of Algebra,322*,3248–3267. https://doi.org/10.1016/j.jalgebra.2008.11.014. Root read Theorem5.6 and its complete proof, printed p3262, plus Theorem5.1, Remark5.3 and Lemma5.4 with proof, pp3260–3261, at https://www.math.utah.edu/~singh/publications/kurano_sato_singh_watanabe.pdf. Its N-grading is not restricted to standard degree-one generators. Rational singularities imply the Cohen–Macaulay property and negative a-invariant; these yield the proper Hilbert rational form used in PNEW-015.

Boutot, J.-F. (1987). Singularités rationnelles et quotients par les groupes réductifs. *Inventiones Mathematicae,88*,65–68. https://doi.org/10.1007/BF01405091. The principal theorem, p65, is the standard reductive-quotient input. The publisher record confirms the metadata but exposes a subscription preview; root has not read the original proof. The manuscript source note separately states that access limit rather than implying a complete primary proof check.

PNEW-015's residue identity and actual tensor coefficient dichotomy are proved directly using the checked cubic estimates and K-023/K-024. The needed bound on the positive coefficient mass of the actual cyclic covariant remains unproved. K-034 uses the elementary3×3binary determinant bound, Cramer's rule and the previously checked coherent normalization/localization methods; it makes no claim that these classical tools are new.

## 20. Separate-scale dimension tables and source-definition scope

N-022 uses the supplied counting consult, Theorem2 (the132 exact trace constants) and Theorem5 (the dimension-ring criterion and abstract regular-matrix monoidal realization). The branch reread those complete supplied proofs; root read the entire new construction and direct-source certificate implementation. The numerical upper bounds4196 and4194 are explicit constructions, not global minima. The retained bounded two-engine search and exact definition comparison are in `branches/nonstandard/N022_source_scope.md`; no priority claim follows from failure to locate the same table.

A metadata discrepancy in that branch note was caught during root review. The primary publisher page https://www.sciencedirect.com/science/article/pii/S0021869314005572 and Blasiak's author homepage both give Journal of Algebra423(2015),375–404 for *Nonstandard braid relations and Chebyshev polynomials*, DOI10.1016/j.jalgebra.2014.09.035. This agrees with central sourceS31; the conflicting425,126–148 entry was requested corrected. No mathematical theorem is altered.

## 21. S38: finite-order automorphisms and invariant maximal tori

Serre, J.-P. (2006). *Bounds for the orders of the finite subgroups of G(k)* [Author manuscript, April2006]. Section3.3, Proposition3(a)–(c), printed pp13–14. Primary author-hosted version: https://www.college-de-france.fr/media/jean-pierre-serre/UPL3821667391778701726_6___Bounds_for_the_orders.pdf. Root read the entire proposition and its complete published proof sketch. For a finite-order automorphism in characteristic zero, the fixed identity component is reductive, a non-torus has positive-dimensional fixed subgroup, and an invariant Borel–maximal-torus pair exists. The proof refers to Steinberg1968, Corollary9.4, and Springer–Steinberg1968, I.2.9, for the first and third assertions; those original proofs were not newly read. The displayed coroot-cocharacter argument for the second assertion was read completely. This is a known structural input for the current antipodal-spectrum centralizer argument, not a new invariant-torus theorem.

## 22. S39: the ordinary Hecke positive cone and N-023

Elias, B., & Williamson, G. (2014). The Hodge theory of Soergel bimodules. *Annals of Mathematics,180*(3),1089–1136. https://doi.org/10.4007/annals.2014.180.3.6. Root read Theorem1.1 and its complete local setup, printed p1093, and the full Section3.5, pp1107–1109, including Theorem3.5 and its attribution to Soergel2007, Theorem1.10, in the publisher PDF https://annals.math.princeton.edu/wp-content/uploads/annals-v180-n3-p06-p.pdf. This is a reading of the categorical definitions and theorem statements, not a new reading of the whole Hodge-theoretic proof or of Soergel’s original proof.

Root also reread the supplied GCTVIII §5.1 equation(17) and surrounding definition. Its first-cell coefficient b1 gives exactly the two classes used by N-023; the known second-cell printing/sign issue is not used. The complete branch note `branches/nonstandard/N023_source_scope.md` distinguishes the supplied F59 ordinary-Euler quadratic obstruction from this new explicit coefficientwise comparison argument. The algebraic N-023 proof and its arbitrary-correction modulo2 argument were fully read and replayed by root. Its categorical conclusion is confined to the ordinary effective positive cone; no arbitrary derived or Koszul-dual exclusion follows.

## 23. S40: support margins, Gram determinants and PNEW-016

Bürgisser, P., & Ikenmeyer, C. (2017). Fundamental invariants of orbit closures. *Journal of Algebra,477*,390–434. https://doi.org/10.1016/j.jalgebra.2016.12.035. Root read Section4.1, equations(4.1)–(4.2) and Definition4.1, printed pp18–19, and the complete support-margin setup, Proposition4.8 and proof in Section4.2, pp21–22, of the author PDF https://arxiv.org/pdf/1511.02927. The author-version page locators identify the checked passages; the journal citation identifies the published work. These are sources for the inspected determinant-character and support framework, not for the compressed fixed-locus dimension bound proved in PNEW-016.

The proof uses a direct necessary-margin argument: a nonzero invariant has a nonzero supported monomial, and each invariant monomial has equal special-linear torus margins. It does not use Proposition4.8's sufficient-polystability assertion or printed averaging argument. In that passage a nonnegative probability distribution need not be positive on every supported edge; zero weighted average does not force every supported edge weight to vanish. This observation limits the dependency claimed here; it is not a refutation of the proposition's conclusion.

Hadamard, J. (1893). Résolution d'une question relative aux déterminants. *Bulletin des Sciences Mathématiques,17*,240–246 (2nd series). Root read complete Sections2–4 and their displayed derivation, printed pp240–242, in the university-hosted English translation https://maths.nuigalway.ie/~padraig/Docs/HadamardTranslation.pdf. The original French scan was not newly read. The classical Gram determinant inequality is credited; the incidence-lattice application is proved explicitly. Franks–Reichenbach2021, Lemma2.5 and proof, p13:15, retain the earlier whole-proof reading and attribution limits already recorded in this audit.

The entire corrected PNEW-016 proof, checker and primary-source comparison were read by root. The general theorem is proved in writing; its45,360 support/multiplicity cases and10,575 root-filter cases are finite exact calibrations, not exhaustive all-dimensional classifications. The remaining positive coefficient mass of the oscillatory covariant difference is unbounded here. No priority claim follows from the bounded literature comparison.

## 24. S41: a checked degree-bound route that remains insufficient

Doğan, M. L., Maar, J., Oliveira, R., & Qiao, Y. (2026). Fixed-parameter degree bounds and complexity of the orbit closure intersection problem for tensors. In D. Moshkovitz (Ed.), *41st Computational Complexity Conference* (LIPIcs, Vol.383, Article32, pp.32:1–32:21). Schloss Dagstuhl. https://doi.org/10.4230/LIPIcs.CCC.2026.32. Root read the complete Section3 setup, Lemma20 and proof, Theorem21 and proof, and Remark22, pp.32:12–32:14, in the publisher HTML, with PDF locator verification. Theorem16's stated left-right bound was also read, p.32:10. The polynomial regime fixes the third dimension. Substituting m=n directly into Theorem21 with beta_H≤mn⁴ gives beta_G≤(3/8)n^(10n²+5); this supplies no bound on PNEW-016's oscillatory constituent coefficients.

Bürgisser, P., Garg, A., Oliveira, R., Walter, M., & Wigderson, A. (2017). *Alternating minimization, scaling algorithms, and the null-cone problem from invariant theory* (arXiv:1711.08039v1). https://arxiv.org/abs/1711.08039v1. Root read Theorem7.10 and its complete proof, and Lemma7.11 with its complete parameter-substitution proof, printed p.33, in the IAS author PDF https://www.math.ias.edu/~avi/PUBLICATIONS/BurgisserGaOlWaWi_Nov2017.pdf. Lemma7.11 bounds null-cone defining degrees, not by itself generator degrees. Theorem7.10 bounds coefficients of invariant polynomials, not coefficients of Hilbert quasipolynomial constituents. Derksen's original proof was not newly read. These distinctions leave the needed tensor wave estimate unproved.

## 25. Exact specified-family minima and N-024

The complete `branches/nonstandard/N024_source_scope.md` was read by root. It compares the user definition with the supplied counting consult, Section1 Theorem2 and Section3 Theorem5, whose earlier checked scope is retained. Negativity in an auxiliary matrix parameter is allowed; the actual dimension constants satisfy all coefficientwise conditions. The all-degree minima are only for equations N151–153's two-parameter family. Earlier Blasiak presentation locators remain known background, with no fresh complete-paper reading claimed. The branch's bounded two-engine search located no matching minima; no historical priority follows. Root and peer complete-proof reviews and exact full-table replays are recorded separately.

The later N168–170 extension also allows an arbitrary common Laurent cell scale while retaining the other displayed relationships. Its complete proof and extended checker were read and replayed by root and peer; it does not assert an all-table optimum. K-036 and K-037 use the previously read finite-restriction, invariant-torus and character-lattice inputs. Their new geometric and exact-character calculations are proved directly and whole-proof checked; no new reading of an original Luna or Steinberg proof, or historical priority claim, is implied.

## 26. S42: the known coefficient-grade versus support mechanism

Bruns, W., & Ichim, B. (2007). On the coefficients of Hilbert quasipolynomials. *Proceedings of the American Mathematical Society,135*(5),1305–1308. Primary author-hosted published PDF: https://www.home.uni-osnabrueck.de/wbruns/brunsw/pdf-article/Quasipol.published.pdf. Root and the plethysm reviewer read all four pages, including Theorem2, p1306, and its complete proof with Lemmas3–4, pp1306–1307. It bounds the coefficient grade through a quotient by elements whose degrees are coprime to the period. This is credited background for the general support/grade mechanism. It neither proves the compressed tensor fixed-locus estimate of PNEW-016 nor bounds the sizes of the surviving coefficients. No coefficient-size consequence is inferred from it.

## 27. Final attribution entries and freeze scope

**K-035.** The all-point no-odd-inertia statement for the actual n10 component, including its conductor, is proved directly using its full stabilizer, the finite balance certificate, and the stable-maximal-torus argument. Its known structural input is Serre2006, Section3.3 Proposition3(a)–(c), pp13–14, with the original-source reading limits stated at S38. The finite-restriction and coherent-support inputs are those already credited at S29 and Section15. The result determines this component's incidence with the indexed collision support; it does not classify every component or prove global dyadic noncancellation. Whole-proof root and peer readings and exact replay are recorded. No historical priority is asserted.

**K-038.** The displayed tensor's full stabilizer, normalized odd-root component and moving character are proved by the explicit unitary contraction, connected intertwiner-unit group, finite fixed-space quotient and tangent character. The finite-restriction and smooth quotient methods use the already credited K032/K035 dependencies and their exact primary locators. The index-three equations, eighteen distinct rational covariant eigenvalues and moving multiplicities are retained as exact data. This work does not claim a new general covariant construction, connected-unit-group theorem or localization formula, and does not infer priority from a failed search. Its local leading contribution does not decide the sum over components or the target-dyadic moving class.

The final attribution audit covers K001–038, N001–024, PNEW001–016, R-NEW001–004 and R-DIAG001, interpreting equation numbers separately from finding identifiers. Some entries are grouped or located in the later thematic sections rather than the initial table. The secondary report `reviews/final_attribution_coverage_audit.md` records the actual coverage check. Known results are credited; unlocated priority is left undetermined. The phrase “finding of this run” denotes a statement proved or computed in this continuation, not a claim of first publication.

New research stopped at the scheduled02:01UTC review on22November2026. The later finalization edits did not add new mathematical or priority research. Final bibliography verification reopened two already used primary source records to supply missing publication metadata and reconfirm their locators. The observation retained in `reviews/UNCHECKED_BI48_observation_at_freeze.md` is explicitly unverified, is not a source erratum, and does not alter S40 or enter any proof. Q10 remains incomplete as an exhaustive search request; this bounded source record is final.
