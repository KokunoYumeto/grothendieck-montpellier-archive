# Pro cote 43, scans 94–142: completed workstream synthesis

## Scope and completion

This workstream audits all 89 entries of `MPL_43_094-142`, their doubts table, and every passage in the accompanying transcription: 46 faces, scans 94–142 excluding 99, 111 and 127, aggregate lines 1–1871. There is no second-pass package for this range. No scan image was supplied, so no reading was changed. The 57 entries in `readings.tsv` are mathematical alarms for a later image-based decision.

The worker inventory before cross-package merging is **80 items, 111 claim records and 39 problems**. Every source entry has one verdict: **76 kept, 9 merged, and 4 withdrawn with the manuscript's cancellation or narrowing retained**. “Withdrawn” records an assertion's source status, not deletion of its historical evidence. The final rereading confirmed that the arithmetic examples, DVR example, Atiyah attribution and context register were already carefully labelled in the earlier notes; they are kept rather than described as errors invented by this audit.

The claim classes are **A: 10; B: 21; C: 36; D: 0; E: 35; F: 9**. No class D was assigned merely because a search failed. The full distribution of the deliberately qualified source-status strings is in `outputs/audit_counts.json`; that file also records the integrity checks. One claim, CL-SA19-056, is explicitly an earlier-run test model rather than a theorem written on the pages. Six claims, CL-SA19-084–089, belong to reused Atiyah material. These origins should remain visible in the final dossier's counts.

The links ledger contains **71 rows**: 48 archive/published-source comparisons and **23 separately marked external-project target rows**. `external_pointer_index.tsv` preserves all **160 entry/target pairs from 85 citing entries**, with the original context and an explicit unavailable-target qualification. It is a mechanical pointer index, not a source of verdicts. The audit records 87 fully read faces, including the 46 assigned faces and selected cross-reference endpoints. The remaining parts of the topic are owned by the other workstreams; no completion claim about those pages is made here.

All 111 claims have a row in `research_log.tsv`. The 337 check events distinguish documentary comparison, independent proof, finite calculation, primary-source use and literal refutation. `computations.md` gives 24 proof/check sections; the actual finite calculations and their output are retained. The programs format hand-authored decisions and test referential integrity; they do not infer a verdict from a heading or keyword.

## The manuscript's line of work, in its own order

### 1. Weil sheaves and a Néron realization: scans 94–98

The opening faces ask how to turn geometric groups into a cohomological category. They define a finite-cover/quasi-scheme setting, introduce \(H\) and internal/global Ext, and propose a valuation-ring realization called Néron. The questions are foundational: comparison with quasi-algebraic groups, Galois descent, filtered continuity, preservation of injectives or acyclic objects, and two different relative-Hom spectral sequences. These are not consequences of writing a Leray-shaped display.

The immediately preceding Codex faces 92–93, read for the cross-link, explicitly worry that a choice of reduced/smooth test objects could lose infinitesimal groups. That warning matters throughout the later finite-group tables. On scans 96–97 the author withdraws a blanket filtered-colimit assertion. The infinite-Witt model in `computations.md` §2 explains the obstruction: infinitely many coordinates need not lie in one finite stage, even though every finite Witt truncation commutes with filtered unions.

The modern comparison is Suzuki's rational/ind-rational theory, especially the precise Ext theorem and the coefficient-dependent realization/acyclicity results (Suzuki, 2022, Theorem 2.1.5, first circulated 2013; Suzuki, 2020, §§2.4 and 3.4, first circulated 2014). These sources develop the programme into rigorous statements. They do not establish that every uncertain handwritten object is equivalent to the modern site. The site dictionary remains the highest-priority commentary task.

### 2. Local class field theory and geometric duality: scans 100–120

The next sequence uses Cartier, Serre and Pontryagin duality, local Rosenlicht theory, Lang descent and finite coefficient calculations. The manuscript alternates between a geometric object over the residue field and ordinary cohomology of the fraction field. Its degree-one and degree-two dualities can therefore be legitimate at different stages, while still requiring an actual descent map to connect them.

The local tables correctly point toward three separate characteristic-p sequences: flat Kummer for \(\mu_p\), Artin–Schreier for \(\mathbf Z/p\), and Frobenius on \(\mathbf G_a\) for \(\alpha_p\). Their quotients are respectively multiplicative \(K^\times/K^{\times p}\), additive \(K/(F-1)K\), and additive \(K/K^p\). A perfect residue field does not make the fraction field perfect, and replacing the latter by its perfection can kill the displayed flat cohomology. The formal \(\mathbf G_m\)/\(\mathbf Z\) comparison and finite character limits additionally require continuous Hom and the declared group category.

The Néron-component pairing on scan 117 has a particularly clear later fate. Suzuki proves the perfectness of Grothendieck's pairing over a complete discretely valued field with **perfect residue field**, together with the derived local-duality theorem (Suzuki, 2020, Theorem A; preprint October 12, 2014). Its bidual notation is mathematically substantive. It does not yield a canonical splitting of the page's extensions or justify an unqualified product decomposition. The rank \(2a+t\) is likewise the prime-to-characteristic Tate rank of a semiabelian variety; the étale p-rank is a different invariant.

The abelian Ext tables on scans 119–120 need more care than a blanket appeal to Barsotti–Weil. Ribeiro and Rosengarten's recent arbitrary-base theorem gives internal fppf \(\underline{\operatorname{Ext}}^2(A,\mathbf G_m)=0\) (first circulated June 20, 2025; revised July 28, 2026). Combined with Kummer, it verifies
\[
\underline{\operatorname{Hom}}(A,\mu_n)=0,\quad
\underline{\operatorname{Ext}}^1(A,\mu_n)=A^\vee[n],\quad
\underline{\operatorname{Ext}}^2(A,\mu_n)=0.
\]
It does not verify every higher zero, and the paper explicitly notes higher-Ext nonvanishing. Nor does a finite-level calculation automatically commute with the passage to \(\mu_\infty\). This is a substantive limit on the manuscript table, not an unresolved bibliography label.

The geometric divisibility statement on scan 120 is about a component of realized \(H^1(K,A)\). It is supported by the finite-flat geometric \(H^2\)-vanishing and Kummer sequence in Suzuki's theory. It says nothing about arithmetic units. The earlier notes already emphasize that distinction; their explicit \(\mathbf Q^\times\) and \(\mathbf Z[1/6]^\times\) models are valid independent examples and are re-proved here.

### 3. Local support duality and completion: scans 123–125

These leaves ask how support Ext, duality and thickening limits fit together. An exact later match is SGA2 VI, Theorem 2.3: the support-Ext colimit requires a coherent first argument, a quasi-coherent second argument, and the appropriate locally noetherian/noetherian distinction. Root's Codex scans 161–162 state the same theorem with those hypotheses more visibly; they are duplicate occurrences, not two independent results.

SGA2 V, Theorem 2.1 supplies the regular-local duality formula with its dimension shift and injective dualizing object. The final formal-completion arrow on scan 125 is less definite. Formal functions and local duality give exact versions under finite-generation, derived-limit and Mittag–Leffler hypotheses, but the unfinished manuscript target cannot be identified without further reconstruction.

The earlier run's DVR computation is fully verified: \(\operatorname{Ext}^1_R(R/t^n,R)=R/t^n\), the transition is multiplication by \(t\), the colimit is \(K/R\), and its endomorphism ring is \(R\) for complete \(R=k[[t]]\). Matlis (1958, Theorem 3.7, pp. 522–523) is an exact primary comparison. Root's complementary nonfinite-first-argument example explains the finiteness gate: every \(\operatorname{Hom}_R(K,t^{-n}R/R)\) is zero, while the quotient \(K\to K/R\) is nonzero.

### 4. Curves, trace and finite cohomology: scans 128–140

The curve programme begins with a complete nonsingular curve, a category of C-groups, and a proposed relative cohomological bound. It then constructs a duality map by evaluation and a trace that is still to be supplied. The Kummer/Picard table and its idèle/adèle annotations identify genuine computational ingredients. They do not establish the entire derived duality by themselves.

Finite-flat curve duality has a precise primary endpoint in Artin and Milne (1976, Corollary 4.9, p. 124), over a perfect field and on their perfect test-site; Suzuki's 2020 curve paper, first circulated March 25, 2018, supplies the open-curve and localization-compatible formulation. The Artin–Milne PDF was read directly by rendering/OCR, with the theorem page visually checked. Its printed shift is kept in its own convention and is not silently imposed on the manuscript.

The finite prime-to-p curve rows follow from Kummer and the full Picard sheaf, including its degree component. The Picard–Brauer five-term sequence also distinguishes actual line bundles from rational points of the relative Picard scheme. An obstruction term cannot be discarded without a reason, such as a rational point. For characteristic p, the \(F-1\) map on finite-dimensional semilinear cohomology is surjective over an algebraically closed field, while \(F\) itself need not be. That is why the \(\mathbf Z/p\) and \(\alpha_p\) rows differ.

The full relative \(\mu_p,J[p],\mathbf Z/p\) row is treated more cautiously than the field-valued row. Flat Kummer gives its formal low-degree structure, but the higher relative vanishing depends on the realization. Modern perfect test-sites lose infinitesimal structure. They cannot be cited as an automatic verification of an unchanged full big-fppf group-scheme row for arbitrary test bases.

The literal line identifying an étale fundamental-group quotient with **full** \(J[p]\) is false. A smooth supersingular elliptic curve in characteristic 3 has trivial geometric étale 3-quotient but a finite flat 3-torsion group of rank 9. The explicit curve \(y^2=x^3-x\) is checked in `computations.md` §14, including geometric smoothness and vanishing Cartier operator. The valid étale comparison is in SGA1 IX, Remark 5.8, final paragraph (recomposed p. 194; original pp. 252–253), using symmetric powers and the Jacobian. Whether a realization or dual marker was lost in transcription is left for the scan.

Oda's 1969 paper supplies exact finite duality and semilinear conventions: isogeny-kernel duality, the F/V dual operators, Frobenius twists and the de Rham–Dieudonné identification of \(A[p]\) over a perfect field. Corollary 5.2 itself states degeneration of the curve Hodge-to-de Rham spectral sequence; its proof uses the Abel–Jacobi \(H^1(\mathcal O)\) isomorphism. It must not be paraphrased as though the corollary stated every possible full de Rham pullback comparison. The general Corollary 5.12 is an injection with a specified image, while the abelian Corollary 5.11 is an isomorphism.

Finally, the localization pages leave genuine questions about point-supported Ext, henselization, extension by zero and dual triangles. Modern sources prove the finite-flat/smooth comparisons under exact hypotheses and also exhibit failure for arbitrary fppf sheaves. The boxed unshifted support/open comparison fails in ordinary degree zero on \(\mathbf P^1\supset\mathbf A^1\). Its valid nearby replacement is a **conditional shifted** localization isomorphism. The boundary term is generally a cokernel of valuation-ring cohomology, not simply all field cohomology.

## Reused pages and their exact fates

The physical range mixes 27 mathematical faces, 11 reused typescript faces, four cancelled drafts and four covers. A modern commentary must not turn this archival adjacency into a single chronological argument.

**Atiyah:** scans 103 → 101, followed by the bibliography on 105, reproduce the end of *Thom Complexes* (1961, pp. 308–310; received March 15, 1960). The connectivity inequality is correct and is independently recomputed. The real Stiefel theorem retains its explicit stable range. Adams–Walker and Sigrist–Suter later settle relevant numerical cross-section criteria; the accessible Adams–Walker theorem statement is verified from the primary publisher extract, not from an unread full proof. Those results do not settle the distinct intrinsic-join/diagonal map comparison that Atiyah still poses on p. 309. Its ultimate exact fate was not located, which is not a claim that it remains open in 2026.

**EGA:** the proper coherent direct-image proof on scan 115 is an exact match to EGA III1, Theorem 3.2.1, pp. 116–117. The Euler and Hilbert–Euler material on scan 121 matches OIII 11.10.2 and III 2.5.2–2.5.3: the Euler polynomial is valid for all integer twists, whereas its agreement with the length of global sections requires sufficiently large twists. The zero sheaf blocks an unconditional strict-positive leading coefficient.

The cancelled connected-component draft has a precise nearby fate in EGA IV3 15.5.4–15.5.8, pp. 233–236, including the role of properness and geometric reducedness. The multiplicity question on scan 110 is more consequential. EGA IV3 12.2.1(xi), 12.2.1.4 and 12.2.2(iii), pp. 179–181, prove the flat case; Remark 12.2.3(vi), pp. 182–183, explicitly preserves the universal-openness/full-support extension and associated-prime question. This audit found that exact printed question but not a later exact resolution.

The simple \(R\oplus k\) counterexample refutes the different sentence “inequality implies flatness”: all the reconstructed properness, openness, full-support and S₁-fibre hypotheses hold, the lengths are \(2\ge1\), and the module is not flat. It does not refute the proposed semicontinuity theorem. Similarly, assuming that \(t\) avoids **all associated primes** makes the local depth argument easy; EGA's question only avoids **minimal primes**. These are materially different hypotheses, and the ink is still needed to choose the manuscript reading.

**Sheaf and flatness typescripts:** the fine-sheaf tensor embedding, its primitive-element lemma, extension by zero, soft-ring partition argument and faithful-flat criteria are checked with explicit hypotheses. Cartan's 1951 seminar provides exact theorem matches for the fine construction. It does not, by itself, identify the anonymous numbered typescript 239 or establish its authorship. The typed pages 87 → 88 occur in reverse scan order 141 → 139. The polynomial dimension/depth fragment is valid with its noetherian, flat-local and regular-fibre hypotheses; the final blank property list cannot be filled from a familiar theorem family.

## What the earlier notes contribute and what this audit changes

The Pro notes are unusually careful about separating manuscript text, earlier-run ideas and unavailable project contexts. They correctly preserve the cancelled continuity claim, the distinction between arithmetic units and geometric divisibility, the lack of a second Fourier witness, and the difference between the curve endpoint and the higher-cycle programme. They also supply useful independently checkable DVR, unit-group, support and flatness countermodels.

The audit's main changes are **precision and later-fate verification**, rather than manufacturing errors in those qualifications. It resolves exact primary locators; separates low Ext degrees from unjustified higher zeros; distinguishes field points, full finite flat groups and perfected realizations; preserves twists in F/V annihilators; and identifies the exact EGA question without declaring it still open from a failed search. The source errors or dangerous literal readings are recorded as claims about the transcription, not misattributed to the notes that already warned about them.

The companion cycle programme is related through ordinary Jacobian duality and finite group schemes, but Pro43 contains no proof of a uniform higher-cycle Betti bound, a cycle-family kernel characterization, a height/intersection formula, or positivity of the descended correspondence. Saito's primary paper supplies a precise later Picard/incidence construction and a Betti bound, with complementary duality up to isogeny (Saito, 1979, Proposition 3.4, Theorem 3.6, Proposition 4.4, pp. 109–113). This is a closer comparison than replacing the whole programme by universality for all regular homomorphisms. The companion worker handles its full theorem audit.

For the Fourier notes, Oda's equality of two named finite/p-divisible pairings is a completed compatibility theorem. It is not the same map as the Fourier unit-fibre \(\theta\) questioned on cote 47. The verified cross-links retain that distinction.

## Remaining limits and handoff to consolidation

The nine class-F claims are genuinely unidentified at theorem level: the exact manuscript site, some degree bounds and contradictory displays, an ambiguous Witt quotient, unfinished subquotients, the undefined θ-range, missing referenced hypotheses and a blank property list. Class-C records say precisely which subcase is established or which reading is refuted. None means “unsearched.” Every problem has a state-of-the-art entry anchored in an opened primary source, even when the conclusion is that a nearby theorem does not resolve the exact question.

External project targets remain separately unverified because their files are absent. The 23 named-target rows preserve every citing entry, including the original distinction between unchecked hunches, return claims and source-range pointers. No outside theorem is accepted merely because an earlier register called it proved.

Recommended cross-package consolidations are documented for the parent: Pro63 with the companion A[p] reconstruction item; Pro54 with the cycle-bound item; Pro57 with the height item; Pro50/51 with Fourier inversion. Pro61 can merge into the finite F/V annihilator item, while Pro60's general isogeny-kernel/bidual-sign statement and Pro62's semilinear dual realization should remain identifiable. Root CL-SA19-647 is the second occurrence of CL-SA19-054. The earlier constructible étale support-duality problem on 43/89–90 should remain distinct from the local-field-versus-geometric coefficient-range problem, with explicit links to the localization task.

The ranked `directions.md` contains eleven bounded follow-up tasks, each with item, claim and problem origins, a known endpoint, an intended result and the first concrete step. Their purpose is to produce the next manuscript commentary and precise map comparisons. No new research direction is presented as solved by this consolidation.
