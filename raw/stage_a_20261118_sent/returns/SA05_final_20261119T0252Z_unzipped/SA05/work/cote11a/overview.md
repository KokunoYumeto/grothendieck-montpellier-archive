# Cote11a completed scope report

**Status date: 19 November 2026.** This report covers all 82 indexed entries of `MPL_11_002-042`, Codex K11-01/K11-02 as comparison witnesses and leads, and the assigned reused EGA and English cycle-class pages in Codex B12-01. It is a scope contribution to the parent SA05 dossier, with its own reproducible records and calculations. It is not a claim to have read every other package or every paper cited in full.

## Coverage and outputs

| Measure | Count |
|---|---:|
| Indexed entries, each with a read verdict | 82 |
| Consolidated items | 59 |
| Claims, including explicitly attributed earlier-run comparisons and published refinements | 90 |
| Problems | 24 |
| Scan alarms, none decided on ink | 46 |
| Links | 76 |
| Ranked directions | 11 |
| Bibliographic records | 34 |
| Search-ledger rows | 32 |
| Recorded check events | 249 |

Entry verdicts: 38 kept, 24 merged, 20 corrected. Claim classes: A9, B42, C28, D2, E5, F4. Page-status labels: 40 proof sketched, 27 stated without proof, 11 open on the pages, 8 proved there, 3 false as stated, 1 corrected by himself later. Two questions receive negative answers in the current checks while retaining “open on the pages” as their historical page status. Links divide into 35 folder links, 21 published-work links and 20 separate earlier-project leads.

All 82 entry IDs match the index exactly once. Items may cite the same entry when it contains several substantive claims, while eight additional B12 items have no fabricated index IDs. Every claim maps to actual executed searches and opened-reference extents. All item, claim, problem, reference and event identifiers resolve within this contribution. Every scan-alarm line range was programmatically checked against the supplied file and its current scan marker. The program `run_all.py` rebuilds the manually authored data, executes the exact calculations and runs structural validation; its actual output is saved in `build_output.txt`.

## What these pages contain, in their own order

The handwritten cote 11 thread begins with a bivariant algebra-valued functor on a category with products. Its pullbacks, pushforwards, projection formula and selected exchange squares produce a category whose arrows from X to Y are elements of A(X×Y). The following pages work through convolution, units, graph maps, action on A(X), transpose, coefficient operations and trace adjointness. This is the starting structure. Later additive enlargements, projectors and Tate twists are legitimate comparisons with motive categories, but they are additional constructions.

The next section organizes stable subfamilies and the operations generating them. Its literal set of single classes f_*1 is not generally a subring; at a point, such values do not include−1. Taking an additive span repairs this particular problem, and characteristic-zero resolution supplies the familiar generation statement. The source’s range of objects and maps remains essential: no fixed-variety result replaces a statement quantified over all objects or all powers.

The Poincaré-algebra section introduces trace adjoints, weakens perfectness to an image criterion, examines tensor products and tests an exchange condition. It visibly rejects a naive tensor-pushforward formula and later restricts to even shifts. The projection-formula margin correctly detects the factor (−1)^(δj) relating left and right conventions. A bivariant algebra isomorphism need not be a “good” one: the element f_*1 records the gauge change. In the wider commutative gauged category the tensor of two Poincaré targets still has the product universal property, even for a degenerate source, because its pullback has a uniquely determined adjoint into the perfect target.

Finite-set systems and cohomology of powers follow. Special Künneth isomorphisms, compatible gauges and the empty-set convention must be kept visible. No condition A^0=k is written in the final setup: the text identifies a coefficient object k in degree 0. The final diagonal-class and full-faithfulness questions therefore cannot be simplified by an invented connectedness assumption.

Interleaved with this handwriting are19 retained reused GIT sheets. Their mathematical text and internal numbering match Mumford’s Geometric Invariant Theory, including numerical functions, the spherical-building viewpoint, a Tits-centre hope, proper actions, descent and ordered point configurations. They are not Grothendieck’s newly stated motif theorems. Their archive order differs from their typescript order, and their exact physical date/version is not established by the later book match. Both supplied cross-package continuations were read: the determinant-cone and greedy-flag proof continues on scans58 and 56, while the quotient-ampleness goal reaches the corollary and theorem on scans54 and 52. The absent typed3.16 criterion remains a specific local gap.

The extra B12 scope contains cancelled EGA drafting material on separating families, generic freeness, local properties under flat maps, integrality, associated primes and schematic dominance. Its published comparisons belong to EGAIV2/IV3 and SGA3, with attribution to the Grothendieck–Dieudonné drafting context rather than to the live motives argument. Page100 is an English cycle-class typescript whose author is not securely identified. It constructs classes by trace duality and then asserts rational-equivalence and product compatibility; those assertions require more than uniqueness of the trace-dual class.

## Main mathematical corrections

**Cartesian squares of gauged Poincaré objects need not satisfy exchange.** Four degree-zero copies of Q with trace weights2,1,1,1 give a commutative square of isomorphisms, hence a Cartesian square, satisfying the proposed dimension relation. Its exchange composites are multiplication by 1 and 2. All hypotheses were checked. The valid tensor-square theorem or an explicitly imposed exchange axiom must be kept separate (SA05-C1023,C1024; MP-SA05-1002).

**Unrestricted singleton evaluation of finite-set systems is not an equivalence.** The partition system has a one-dimensional singleton value and a two-dimensional two-point value, with unital pullbacks, adjoint pushes, projection formula and natural maps all verified. Its special Künneth map fails. The general argument is in `proof_checks.md`;56 maps and 1618 composition/naturality cases for cardinalities≤3 supplement that proof. Hua’s November2026 paper proves a restricted commutative ungraded special-system theorem with multiplicative gauges. Its prose proof was read, its v1/v2 variance discrepancy recorded, and its reported Lean compilation was not run (SA05-C1031–C1035).

**The nilpotent-density draft omits an essential hypothesis for its ordinary assertion.** Let S=Spec Q[x,ε]/(ε²,xε), let S₀=Spec Q[x], and take X=S, Z=D(x). Both X and Z are flat over S. The reduction Z₀→X₀ is schematically dominant, whereas Z→X kills nonzero ε. The published SGA3II IX4.2 and EGAIV3 11.9.15 require the successive ideal layers to be locally free on S₀; here J/J²≅Q[x]/(x) is not. The relative-universal assertion has a stronger premise and is not refuted by this example (SA05-C1077,C1089).

**Two different EGA integrality issues must be separated.** Under the modern definition, geometric unibranchness allows nilpotents: the identity on Q[ε]/ε² refutes a literal unreduced version of the draft’s total-domain question. The draft also suggests reducing to normal A. Murayama2022 Corollary 4.1 gives geometric punctual integrality of all fibers under quasi-excellence, while Remark 4.2 warns against a general domain-ascent inference. The exact bridge to the intended normal-base total-space question was not established from the opened references. This is a precise limitation of the literature identification, not a claim that the question remains open worldwide (SA05-C1062,C1090).

**An old schematic-dominance question has an exact later answer.** EGAIV3 Proposition 11.10.6 proves preservation under every base change over a field, answering the B12/85 “nous ignorons” question without the draft’s locally Noetherian restriction. The exact theorem, its module counterpart11.9.13 and the universal-relative definition were opened (SA05-C1074–C1076).

**The GIT claims have distinct successors and distinct hypotheses.** Kempf’s optimal cocharacter/parabolic theorem concerns an unstable vector and a chosen invariant norm; its rational version has perfect-field and rational-norm conditions. The convex-subcomplex centre theorem and the Bate–Martin–Röhrle finite-type polyhedral quasi-state criterion do not justify an undefined universal centre assertion. The latter paper explicitly distinguishes GIT instability sets from subcomplexes. These distinctions prevent a broad “Tits conjecture solved” label from overstating the reused sheet (SA05-C1042).

## Scan and provenance priorities

The highest-impact handwriting alarms are the graph-action terminal value on 11/15, φ_A versus φ_B on 11/36, the two ambient targets that should plausibly be A_m and A_(n+m) on 11/40, the degree interval on 11/42, and the Pro/Codex centrality question on 11/17. The tensor retraction and subsequent sign trials require a scan-aware edition. In the EGA fragment, B_h free over A_h is ill-typed with h chosen in B, and the proof points toward B′_h over B_h. The same passage carries scan 66 in B12-01 but scan 72 in Pro/K12-05. K12-05 additionally reads11.9.5 where the other witnesses read11.9.6. None of these discrepancies was silently corrected.

The large inherited network of cote 16/47/44/54 links was retained only as explicitly unavailable leads. This includes the standard-conjecture lettering dictionary, chosen Lefschetz/projector image, Cartier/de Rham links and derived-kernel comparison. The earlier note does supply an explicit K-class pull–multiply–push formula; it should not be replaced by an unrelated vague realization-injectivity question. A modern proper-flat perfect-kernel model was opened and checked, while the actual missing cote 47 hypotheses remain unverified. Oda’s exact Corollaries5.11–5.12 were opened for the degree-one comparison, distinguishing the p-kernel from a full p-divisible group and retaining the k-point hypothesis in the smooth proper case.

## Reference and computation limits

`reference_checks.tsv` distinguishes theorem/proof passages, abstract-only verification, metadata and blocked targets. A bibliographic `note={verified}` means the stated URL was opened to the extent recorded, not that every theorem in the work was audited. The original Hironaka paper, zbMATH Oda review and pinned Hua repository targets remain marked unverified. The SGA5 desired cycle-class section was not retrieved; Milne’s opened Theorem 23.4 states the compatibility but expressly omits its long proof. The final EGAIV2 §7.5/§7.9 text was outside the accessible indexed range. These limits are also in the claim fates and search ledger.

The computations use exact symbolic or rational arithmetic. They check kernel matrices/convolution, diagonal and Frobenius identities, parity, degree transport, scalar gauges, partition-system finite cases, block corners, inverse operators, lowering coefficients, selected weight inequalities and the two algebraic counterexample relations. Finite tests are labelled as such and do not replace general proofs. No Lean certificate was compiled, and no scan image was available.

## Parent merge recommendations

The principal cross-scope joins are the correspondence/action/completion material with cote 11b SA05-2002/2007, the Poincaré and tautological material with SA05-2003/2010/2011/2014/2018, and the GIT continuation. The dual-number model already shows Δ=y₁+y₂ for P¹, so the later universal “basis” language cannot mean independence for every X; no earlier hypothesis in this scope excludes P¹.

For the duplicated EGA fragment, root SA05-77 should merge into SA05-1052 with its indexed source retained, and root SA05-C95 should merge specifically into SA05-C1061. The appropriate primary comparison is EGAIV3 11.9.7–11.9.10, with received1964-11-15/publication1966 metadata and undated draft provenance; the unrelated Cisinski–Déglise reference/date must not survive. SA05-C1060 concerns the adjacent generic-freeness induction, not a second duplicate of the displayed lemma. The exact original lemma still has missing hypotheses and malformed notation, so no verbatim final-EGA identity is asserted.
