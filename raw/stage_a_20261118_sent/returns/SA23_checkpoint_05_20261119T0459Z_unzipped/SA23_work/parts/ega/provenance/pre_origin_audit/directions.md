# Ranked directions from cotes22,23 and26

These are separate future tasks. Numeric ratings are manual judgments from1(low) to5(high). Progress concerns a bounded single run, with missing scans taken into account. Additional Codex subjects SA23-1301–1320 have no indexed Stage1 entries; the69 indexed subjects and82 entry verdicts are unchanged. Exact machine-readable provenance is in directions.json.

| Rank | Direction | Interest (1–5) | One-run progress (1–5) | Exact source IDs |
|---|---|---|---|---|
|1|The non-Cohen–Macaulay construction|5|3|SA23-1301; C-SA23-ega-077; MP-SA23-ega-41|
|2|Broad Cohen lifting|5|3|SA23-128; SA23-129; SA23-130; SA23-131; SA23-132; SA23-133; SA23-134; C-SA23-ega-018; C-SA23-ega-019; C-SA23-ega-020; C-SA23-ega-055; C-SA23-ega-056; C-SA23-ega-057; C-SA23-ega-058; C-SA23-ega-059; C-SA23-ega-060; MP-SA23-ega-05; MP-SA23-ega-27; MP-SA23-ega-28; MP-SA23-ega-29; MP-SA23-ega-30|
|3|Finite-order natural functors|5|3|SA23-1302; C-SA23-ega-039; C-SA23-ega-040; C-SA23-ega-041; C-SA23-ega-044; C-SA23-ega-045; MP-SA23-ega-16; MP-SA23-ega-17|
|4|The withdrawn compactness proposition|5|3|SA23-1303; C-SA23-ega-053; MP-SA23-ega-26|
|5|Infinite differential directions|4|5|SA23-140; SA23-141; SA23-142; C-SA23-ega-021; C-SA23-ega-022; C-SA23-ega-023; MP-SA23-ega-06; MP-SA23-ega-09|
|6|Meromorphic denominators under restriction|4|4|SA23-1304; C-SA23-ega-046; MP-SA23-ega-20|
|7|A scan-based errata concordance|4|3|SA23-1303; SA23-1305; SA23-1306; SA23-1307; SA23-1308; SA23-1309; C-SA23-ega-049; C-SA23-ega-050; C-SA23-ega-051; C-SA23-ega-052; C-SA23-ega-053; C-SA23-ega-058; C-SA23-ega-061; C-SA23-ega-070; C-SA23-ega-097; MP-SA23-ega-23; MP-SA23-ega-24; MP-SA23-ega-25; MP-SA23-ega-26; MP-SA23-ega-31; MP-SA23-ega-37|
|8|Lang’s alleged gap|3|3|SA23-111; C-SA23-ega-006; MP-SA23-ega-03|
|9|Reused trace and integrability pages|3|2|SA23-118; SA23-119; SA23-120; SA23-121; SA23-152; SA23-165; C-SA23-ega-027; C-SA23-ega-031; MP-SA23-ega-11|
|10|One quotient or bundle problem from cote26|5|3|SA23-1311; SA23-1312; SA23-1313; SA23-1314; SA23-1315; SA23-1316; SA23-1317; SA23-1318; SA23-1319; SA23-1320; C-SA23-ega-086; C-SA23-ega-087; C-SA23-ega-088; C-SA23-ega-089; C-SA23-ega-090; C-SA23-ega-091; C-SA23-ega-092; C-SA23-ega-093; C-SA23-ega-094; C-SA23-ega-095; C-SA23-ega-096; MP-SA23-ega-48; MP-SA23-ega-49; MP-SA23-ega-50; MP-SA23-ega-51; MP-SA23-ega-52; MP-SA23-ega-53; MP-SA23-ega-54; MP-SA23-ega-55; MP-SA23-ega-56; MP-SA23-ega-57; MP-SA23-ega-58|
|11|The graded-algebra sequence|3|4|SA23-1310; C-SA23-ega-078; C-SA23-ega-079; C-SA23-ega-080; C-SA23-ega-081; C-SA23-ega-082; MP-SA23-ega-42; MP-SA23-ega-43; MP-SA23-ega-44|
|12|Differential-field and discriminant collation|3|4|SA23-143; SA23-144; SA23-149; SA23-150; SA23-151; C-SA23-ega-026; C-SA23-ega-030; MP-SA23-ega-10; MP-SA23-ega-12|

## 1. The non-Cohen–Macaulay construction

**What it would establish.** A precise example with the intended unusual change in the non-Cohen–Macaulay locus, including every geometric existence choice and local depth calculation.

**Known.** The fibre-product exact sequence and its extra Tor term are checked in this run. The gap is earlier: normality and failure of Cohen–Macaulayness do not alone isolate the bad locus sufficiently for the intended hypersurface choice. Stacks00RD gives the standard finite-type openness context, but does not supply the missing projective input.

**First step.** Specify the desired dimension and isolated bad locus on the projective scheme, then find one explicit normal projective example whose local cohomology is computable. A useful first run can finish that example or demonstrate that the proposed dimension pattern is incompatible with the chosen geometry. [C-SA23-ega-077; MP-SA23-ega-41]

## 2. Broad Cohen lifting

**What it would establish.** The strongest nonlocal lifting statement actually supported by the draft, separated from established complete local Cohen factorization.

**Known.** Stacks07NN/09Q9 supply the local complete flat regular-fibre factorization. The relative pro-Tor comparison is reconstructed in proof_notes.md. These results do not automatically establish the draft’s arbitrary topological algebra version or its global uniqueness claims.

**First step.** Write an exact diagram of rings and topologies from the relevant scan and list which completeness, locality, finiteness and residue-separability hypotheses are used at each lift. Test the weakest missing hypothesis on a product or localization example. [SA23-128–134; MP-SA23-ega-05,27–30]

## 3. Finite-order natural functors

**What it would establish.** A valid scheme-theoretic equivalence between finite-order natural constructions and actions of a finite jet or principal-parts group, under explicit base and locality conditions.

**Known.** The smooth-manifold equivalence in Kolár–Michor–Slovák §§14.6,14.8 is an exact analogue. The manuscript’s scheme category and Greenberg-style extension have not been identified with a theorem of that scope.

**First step.** Restrict to smooth affine schemes of one fixed relative dimension over a characteristic-zero field, make the locality axiom explicit, and compare the representing jet group with the bitorsor already constructed. This isolates a tractable statement before any arbitrary-base extension. [SA23-1302; C-SA23-ega-039–041,044–045; MP-SA23-ega-16–17]

## 4. The withdrawn compactness proposition

**What it would establish.** Either a counterexample satisfying the exact hypotheses of withdrawn EGA0.19.3.12, or a corrected theorem with additional countability or topology assumptions.

**Known.** The original linear-variety proof is invalid and the1967 errata expressly withdraw the proposition. The finite-solvability polynomial example checks that proof mechanism only. Successive countable adic lifting has a different argument.

**First step.** Extract the exact original theorem and define its square-open ideals and topology independently of the defective proof. Compare countable versus uncountable inverse systems before attempting a general algebra-lift example. The task should begin from the withdrawal, not by treating the old assertion as established. [C-SA23-ega-053; MP-SA23-ega-26; EGAIV1; EGAIV4]

## 5. Infinite differential directions

**What it would establish.** A reusable precise note covering nonsplitting and nonprojectivity of differentials of power-series rings, with the adic and discrete categories visibly separated.

**Known.** The finite-support proofs in this run settle the stated cases. The earlier run’s stronger idea is not silently attributed to the manuscript, and the searches do not establish novelty.

**First step.** Check the scans’ precise coefficient-field and finite-base-enlargement clauses, then compare the completed proof with modern accounts of noncontinuous derivations. A few-hour run should produce a polished theorem/proof and a bounded prior-literature search, rather than a novelty announcement. [SA23-140–142; MP-SA23-ega-06,09]

## 6. Meromorphic denominators under restriction

**What it would establish.** An explicit nonnoetherian example explaining exactly which stalk or open-set identification fails in the printed EGA20.1 formulation, and which definition is stable under restriction.

**Known.** Lê’s correction matches the original printed text. Stacks01X1 gives the restriction-stable setup;0EMG restores the familiar identifications for locally noetherian schemes. The separate21.2.9 trivialization issue is already localized.

**First step.** Construct an affine ring and open subset where a section is a nonzerodivisor at the chosen stalk but fails the required neighborhood condition. Check the sheaf and stalk maps explicitly, then use the scans to decide Lê’s intended notation. [C-SA23-ega-046; MP-SA23-ega-20]

## 7. A scan-based errata concordance

**What it would establish.** A reliable critical apparatus linking Deligne’s letters, the original EGA passages, the later correction list and the final SGA redactions.

**Known.** Several exact correspondences are now established: the withdrawal of0.19.3.12; the locality correction; the sign change with its own old/new-label transposition; the16.1 immersion hypothesis; the19.5.5 proof credited to Deligne; and the Artin XII6.3 draft. The III4.3.6 equality is false, but the conclusion survives an injection-based proof.

**First step.** Put each manuscript scan beside the corresponding original printed page and decide only the flagged ink questions. A concordance should preserve authorship, dates, cancellations and the distinction between an erratum, a proof simplification and a changed hypothesis. [MP-SA23-ega-23–26,31,37]

## 8. Lang’s alleged gap

**What it would establish.** The exact missing step alleged in Jouanolou’s1963 offprint and whether Lang’s own argument or later corrections already handle it.

**Known.** Jouanolou points specifically to separability of a completion fraction field. Nagata’s1957 note removes a normic-form assumption in related C_i results, which is not enough to identify this analytic gap. The original Lang proof has not been read in this run.

**First step.** Obtain the original1952 paper, locate the convergent-series/complete-valued-field argument, and trace every use of separability. Report a proof comparison with exact pages, even if the outcome is that Jouanolou’s allegation cannot be confirmed. [SA23-111; C-SA23-ega-006; MP-SA23-ega-03]

## 9. Reused trace and integrability pages

**What it would establish.** Authorship and precise hypotheses for the trace/repartition formulas and the English coordinate-integrability calculation.

**Known.** Determinant norms cover a finite locally free portion of the first topic. The English page’s relation to infinitesimal conjugation is a present comparison, not an archival cross-reference. Exact-phrase and author-bibliography searches have not identified its source.

**First step.** Inspect typeface, page numbers, bibliography fragments and neighboring scans. Search a distinctive complete sentence, preserving its original spelling. Mathematical reconstruction should follow identification rather than supply an assumed author. [SA23-118–121,152,165; MP-SA23-ega-11]

## 10. One quotient or bundle problem from cote26

**What it would establish.** A modern theorem or counterexample for one exact question, such as the quotient of a specified free flat group action or bundles over a fixed relative curve.

**Known.** Modern algebraic-space and stack representability answers many constrained versions. Nonprojective duality and unpolarized abelian deformations are established. Arbitrary varieties, arbitrary affine structural groups and “without fixed points” remain too broad or ambiguous to be one theorem.

**First step.** Choose a single row in MP48–58, fix the moduli functor and topology, and compare its hypotheses with the exact opened theorem. For the relative P1 question, begin with a two-stratum family where splitting type changes, so that the limitation of fibrewise classification is visible. [C-SA23-ega-086–096]

## 11. The graded-algebra sequence

**What it would establish.** A coherent sequence of generation, section-independence, Poincaré-series and flatness statements suitable for an annotated edition.

**Known.** The augmented-composition condition and the missing surjectivity assumption are mathematically necessary. The first flatness implication is false, while the other two have tensor-product proofs.

**First step.** Decide the two missing hypotheses on the scans. Then state each corrected implication with a single grading convention and attach the saved minimal counterexample to the literal alternative. This is an editorial and expository task; no novelty claim is indicated. [MP-SA23-ega-42–44]

## 12. Differential-field and discriminant collation

**What it would establish.** An accurate comparison of the manuscript’s characteristic-two examples with the misprinted EGA field, and of the discriminant exponent with the general homogeneous formula.

**Known.** The field counterexamples and coefficient-degree formula have been checked. Binary forms and quadrics fail to expose the exponent error; a plane cubic does expose it. The correct differential-field example must actually adjoin the extra independent generator.

**First step.** Inspect the exponents and generator lists on the scans, keeping original print and manuscript as separate witnesses. The finished task should provide a short critical note with exact hypotheses and the already saved certificates, not overwrite the diplomatic text. [SA23-143–144,149–151; MP-SA23-ega-10,12]
