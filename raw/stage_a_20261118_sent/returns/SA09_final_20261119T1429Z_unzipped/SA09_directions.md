# SA09 — Ranked directions for subsequent work

**Status date: 19 November 2026.** These twelve directions are task formulations derived from the consolidated dossier. They distinguish questions left on the manuscript pages, established results that can now be used, unresolved source readings, and comparisons proposed by the earlier runs or this consolidation. They do not claim that the proposed follow-on work has been performed.

The two rankings answer different questions. **Interest rank** measures the direction's importance for recovering the mathematical programme and its dependencies. **Few-hours tractability rank** measures the prospect of completing the bounded next deliverable stated below, using the sources currently available; it does not estimate the chance of proving the direction's entire eventual theorem. Rank 1 is highest in each column. Tasks requiring unavailable scans rank lower on present tractability, even when image access would make their editorial resolution quick.

All item, claim and problem identifiers below were checked against the component records. Canonical identifiers follow `SA09_id_aliases.tsv`; in particular, the repeated arithmetic-inertia claim is CL-SA09-138M-027 and its combined item is SA09-239. Detailed evidence, literature limitations and computation outputs remain in the corresponding ledgers and component proof audits. Bibliographic keys in parentheses identify entries in `SA09_references.bib`.

## Ranking at a glance

| Direction | Interest rank | Few-hours tractability rank | Bounded deliverable for the next run |
|---|---:|---:|---|
| D01. Complete the mixed-degree polynomial-category specification | 1 | 7 | A fully typed axiom and dependency table, with one decisive mixed-degree composition test. |
| D02. Prove existence in the multiplicative extension square | 2 | 4 | The required kernel lemma under explicit hypotheses, or a concrete obstruction in the actual tensor model. |
| D03. Specify the manuscript's structured cochain object | 3 | 8 | One operation-preserving comparison specification with a single modern target. |
| D04. Repair cell pinning and its arithmetic moduli functor | 4 | 2 | A consistent finite geometric category and a precisely distinguished rigidified or class-scheme statement. |
| D05. Isolate oriented normality in the exact peripheral kernel | 5 | 12 | A rigorous rank-three reduction or finite obstruction, with ambient-group hypotheses fixed. |
| D06. Determine the relative exact framework on P and Q | 6 | 3 | An admissible-sequence and closure audit, followed by a corrected evaluation statement. |
| D07. Define one finite category of spherical operations | 7 | 5 | Explicit transition arrows, one complete operation model, and separated strict-clean/folded-edge conditions. |
| D08. Reconstruct the eighteen Fermat-fibre transports | 8 | 11 | A source-target and stabilizer table for the proposed arrows, conditional where ink remains unresolved. |
| D09. Recover the finite-weight PD comparison | 9 | 9 | Weight-one through weight-three complexes with correct terminal kernels and truncation. |
| D10. Classify bounded holomorphic exceptions and their markings | 10 | 6 | A finite spherical stabilizer classification in a declared marking convention. |
| D11. Write the exact Kummer coordinate companion | 11 | 1 | A complete dictionary between the manuscript's torsors, affine coordinates and established image formulas. |
| D12. Resolve the consequential manuscript readings | 12 | 10 | With images, a documented decision on six priority sites; without images, retain explicit alternatives. |

## D01. Complete the mixed-degree polynomial-category specification

**Records.** Items: SA09-40, SA09-41, SA09-42, SA09-44, SA09-49. Claims: CL-SA09-137-047, CL-SA09-137-048, CL-SA09-137-049, CL-SA09-137-051. Problems: MP-SA09-26, MP-SA09-27, MP-SA09-29. **Interest: 1; tractability: 7.**

**Known input.** The homogeneous construction using natural maps \(\alpha_{p,q}:\Gamma^{pq}\to\Gamma^p\Gamma^q\), correctly typed associativity, degree-one units and a separate degree-zero condition has been checked. Roby's polynomial-law theory and the SGA4 module model provide concrete examples. The opened contemporary treatment explicitly excludes the full mixed-degree tensor/multigrading equivalence; it therefore does not settle the remaining assertion (Roby, 1963; SGA4 XVII5.5.2; `Roby1963`, `SGA4XVII`; CL-SA09-137-049).

**Exact remaining task.** Specify the objects, morphisms and compatibility conditions on both sides of the announced equivalence, including addition, mixed composition, constants, parameter-stable representation, tensor coherence and Hom-module polynomial laws. Establish which comparison maps are hypotheses and which follow from universal properties.

**First concrete step.** Expand the composition of a map with degree-one and degree-two summands with a degree-two map. Write every resulting homogeneous and mixed term with its source and target. Test the proposed law over coefficient algebras, not solely by integer scalar substitutions. The few-hours output should be a dependency theorem or a minimal insufficiency example. A homogeneous calculation alone should not be presented as the completed equivalence.

## D02. Prove existence in the multiplicative extension square

**Records.** Items: SA09-22, SA09-23, SA09-24, SA09-82. Claims: CL-SA09-137-039, CL-SA09-137-040. Problems: MP-SA09-18, MP-SA09-19, MP-SA09-20. **Interest: 2; tractability: 4.**

**Known input.** The source's monomorphism proves uniqueness of a factorization once it exists. The audit proves a conditional existence statement when \(X*Y\) is the appropriate simultaneous admissible kernel and the coefficient functor preserves it. The initial disk category has no tensor unit, so the unit enlargement is a separate datum. Here \(*\) is the product transported from simplicial degreewise tensor; it has not been identified without qualification with ordinary total tensor (Dold & Puppe, 1961; Richter, 2009; `DoldPuppe1961`, `Richter2009`; CL-SA09-137-039–040).

**Exact remaining task.** Verify the required kernel formula for the actual source category and tensor product, then prove naturality, independence of the chosen presentations and the unit/associativity/symmetry conditions. The first theorem should state precisely which exactness hypotheses it uses.

**First concrete step.** Choose finite cone presentations for \(X\) and \(Y\), and compute the kernel of

\[
I_0*J_0\longrightarrow(I_1*J_0)\oplus(I_0*J_1).
\]

Test the differential-two disk, the degree-zero sphere and a positive-degree sphere before generalizing. A completed kernel lemma, or one explicit counterexample to it under the weak source hypotheses, is a meaningful single-run outcome. Coherence becomes the next finite verification only after factorization exists.

## D03. Specify the manuscript's structured cochain object

**Records.** Items: SA09-25, SA09-50, SA09-65. Claims: CL-SA09-137-024, CL-SA09-137-041, CL-SA09-137-042. Problems: MP-SA09-08, MP-SA09-09, MP-SA09-21. **Interest: 3; tractability: 8.**

**Known input.** Additive evaluation, binary cup products and certain stated homotopies are available. Sullivan's rational models, Mandell's integral structured cochains, Toën's affinization and Horel's binomial models have different coefficient, connectivity, finiteness and mapping conclusions. None can be substituted for the precise manuscript datum without constructing an appropriate comparison. A binary product up to homotopy also does not by itself specify all higher coherence (Sullivan, 1977; Mandell, 2006; Toën, 2020; Horel, 2024; `Sullivan1977`, `Mandell2006`, `Toen2020`, `Horel2024`).

**Exact remaining task.** Define one source category with its constants, units, substitution, divided powers, homotopies, morphisms and weak equivalences. Choose one modern target and identify the operation-preserving comparison that would be needed before invoking its reconstruction theorem. Separate recognition of objects, conservativity, full faithfulness and recovery of mapping spaces.

**First concrete step.** Produce a table matching each required target operation to an exact manuscript formula, a result of D01/D02, or an explicitly missing construction. Use \(K(\mathbb Z,1)\), \(K(\mathbb Z,2)\) and one torsion example as bounded tests of the declared data. The expected deliverable is a comparison specification and its first obstruction, not an integral homotopy-reconstruction equivalence.

## D04. Repair cell pinning and its arithmetic moduli functor

**Records.** Items: SA09-275, SA09-277, SA09-281, SA09-283, SA09-289. Claims: CL-SA09-138L-017, CL-SA09-138L-020, CL-SA09-138L-021. Problems: MP-SA09-73, MP-SA09-74, MP-SA09-75. **Interest: 4; tractability: 2.**

**Known input.** The literal precarte morphism law fails composition. Cell pinning can retain a nontrivial automorphism, and the labelled elliptic twists \(dy^2=x^3-x\), \(f=x^2\), refute étale separation of the raw rational isomorphism-class presheaf. A fixed dart kills automorphisms in a connected transitive permutation map. The finite geometric class set nevertheless gives a finite étale scheme, with its extension away from primes dividing \(\delta!\) supported by the precise tame-specialization hypotheses (SGA1 XIII2.9–2.11; Stacks Project Lemma58.2.2; `SGA1`, `Stacks03QR`).

**Exact remaining task.** Choose a corrected marking and state its geometric and arithmetic meaning. Distinguish a stack of covers with descent data, a genuinely rigidified functor and the finite scheme of geometric classes. A topological flag choice is not automatically a rational marking available on every form.

**First concrete step.** Compare cell labels, a fixed dart, complete flag labels and a specified point in an unramified reference fibre, recording automorphism kernels and descent data in each case. Apply the already certified genus-one twist as a mandatory test. A few hours should suffice for a consistent finite category and a carefully stated result over \(\mathbb Q\). Any integral fine-moduli claim must separately establish effective descent and the existence and behaviour of its chosen marking.

## D05. Isolate oriented normality in the exact peripheral kernel

**Records.** Items: SA09-239, SA09-258, SA09-259, SA09-260. Claims: CL-SA09-138M-027, CL-SA09-138L-004, CL-SA09-138L-005, CL-SA09-138L-006. Problems: MP-SA09-70, MP-SA09-71, MP-SA09-72. **Interest: 5; tractability: 12.**

**Known input.** With named peripheral classes and a common multiplier, the dossier's sextic-orbit argument refutes normality of the full extended geometric closure and equality of the oriented closure with the multiplier-one kernel in every rank \(\nu\ge2\). These are distinct from normality of \(\widehat T_\nu^\circ\) inside \(\Gamma_\nu^\circ\). In rank two the latter subgroup is trivial and therefore normal. The located genus-zero congruence and tower-compatible results do not settle the exact unrestricted higher-rank question (McReynolds, 2012, Theorem1.1; Collas, 2026, §4.2; CL-SA09-138L-005).

**Exact remaining task.** Determine the rank-three case, or prove a rigorous reduction, for precisely the ambient group defined by the source. A result about full GT, a Belyi-compatible tower, a puncture-permuting group or an arithmetic image must not be substituted without a comparison theorem.

**First concrete step.** Write the puncture-forgetting maps in rank three, including the closed normal subgroups they kill, and separate geometric, inner and arithmetic conjugators. Test one carefully specified finite quotient for a normality obstruction. A few-hours run can reasonably deliver a reduction or certified obstruction; failure to find an obstruction proves neither normality nor that the question is globally open.

## D06. Determine the relative exact framework on P and Q

**Records.** Items: SA09-3, SA09-7, SA09-11, SA09-15. Claims: CL-SA09-137-030, CL-SA09-137-032, CL-SA09-137-033, CL-SA09-137-036. Problems: MP-SA09-12, MP-SA09-14, MP-SA09-15, MP-SA09-17. **Interest: 6; tractability: 3.**

**Known input.** Bounded nonnegative finite-free complexes with degreewise exact sequences support the restricted additive evaluation argument. The split-homology subcategory \(Q\) is not extension-closed in \(P\): the differential-two disk is the middle term of a degreewise split sequence with sphere endpoints. The source's weak initial axioms do not automatically supply the pushout, pullback and composition properties of an exact category. The ordinary evaluation theorem also does not establish the proposed derived-evaluation formula (Bühler, opened 2009 preprint, Definition2.1 and §12; `Buhler2009`; CL-SA09-137-030–036).

**Exact remaining task.** Identify the intended object category and admissible sequences, then prove the precise exact-functor/evaluated-resolution statement under those hypotheses. If \(Q\) needs a smaller exact structure, an exact hull or replacement by \(P\), state that change as a reconstruction.

**First concrete step.** Build a closure table for the live axioms at scans49–63. Test pushouts, pullbacks and compositions on scalar disks and the known extension. Specify one small abelian or exact target in which derived evaluation can be defined and its acyclicity checked. The deliverable should isolate the remaining relative hypothesis, rather than repeat an ordinary additive theorem already proved in the dossier.

## D07. Define one finite category of spherical operations

**Records.** Items: SA09-335, SA09-338, SA09-341, SA09-346, SA09-371, SA09-373. Claims: CL-SA09-138L-054, CL-SA09-138L-056, CL-SA09-138L-057, CL-SA09-138L-075, CL-SA09-138L-076. Problems: MP-SA09-79, MP-SA09-80, MP-SA09-81, MP-SA09-83, MP-SA09-92, MP-SA09-93. **Interest: 7; tractability: 5.**

**Known input.** Normal cores make normal finite covers cofinal; compatible sections still require a defined diagram and its variance. The reference-subset quotient is unfinished on the page. Rational Belyi-extending postcomposition supplies a precise arithmetic subclass. The dossier has also proved the local-index criterion for universal strict-clean preservation; the manuscript's folded-edge inequality is a different convention (SGA1 V; Ellenberg, 2000/2002; Wood, 2003/2006; `SGA1`, `Ellenberg2002`, `Wood2006`).

**Exact remaining task.** Declare a finite cover category, its map-preserving isotopies, pullback functor and compatible-section construction. Then specify one class of reference graphs or rational outer maps and the exact marking and automorphism data it preserves. Do not begin by asserting a classification of all natural operations.

**First concrete step.** Write every transition arrow for a small normal-cover system and calculate the powerset compatible families. Within that same category, compare the identity, the cleaning map \(4t(1-t)\), and one already defined rational extending map. Record separately strict cleanness, folded-edge admissibility, preservation of the source complex surface and preservation of its graph automorphism group. The target is one complete finite construction and a bounded implication table; no universal operation-classification claim is required.

## D08. Reconstruct the eighteen Fermat-fibre transports

**Records.** Items: SA09-157, SA09-158, SA09-159, SA09-160, SA09-161, SA09-194. Claims: CL-SA09-138E-039, CL-SA09-138E-043, CL-SA09-138E-044, CL-SA09-138E-045. Problems: MP-SA09-44, MP-SA09-48. **Interest: 8; tractability: 11.**

**Known input.** The Fermat deck module, compatible root systems, centre and midpoint torsors and mod-three orientation line are explicitly controlled. Direct substitution detects the independent half-turn/cubic-root and inverse-root inconsistencies. The source retracts proposed full arithmetic equivariance to the smaller symmetry generated by \(S_3\) and complex conjugation. The assertion that two transports determine eighteen does not itself check stabilizers or composition relations (SGA1 V; *Esquisse*, §§3–4; CL-SA09-138E-043–045).

**Exact remaining task.** Specify the finite action groupoid of branch, centre and midpoint fibres and the intended path/transport maps. Identify two representative arrows, state their stabilizer compatibility and prove the relations that would generate the other sixteen. Keep any proposed coordinate correction distinct from a reading of the ink.

**First concrete step.** List all eighteen source-target pairs and their symmetry orbits before solving for formulas. Use the existing exact residuals to mark the places where the two possible root readings produce different objects. Once original images settle those readings, test the two representative arrows and their stabilizers. Without images, a conditional groupoid specification is still useful; an assertion of the author's completed functor, or full \(G_{\mathbb Q}\)-equivariance, is not justified.

## D09. Recover the finite-weight PD comparison

**Records.** Items: SA09-27, SA09-28, SA09-29. Claims: CL-SA09-137-003, CL-SA09-137-004. Problem: MP-SA09-01. **Interest: 9; tractability: 9.**

**Known input.** The later manuscript occurrence retracts an untruncated formulation. Good truncation preserves the relevant top kernel, whereas brutal truncation can create spurious cohomology. The opening vanishing lemma is false under its literal surviving projectivity-only equality case. Dold–Puppe and SGA4 provide comparison tools, but the exact complete structured theorem is not supplied by the opened sources (Dold & Puppe, 1961; SGA4 XVII5.5; `DoldPuppe1961`, `SGA4XVII`).

**Exact remaining task.** Formulate and construct the weight-\(n\) comparison with its correct terminal kernel, naturality and homotopy class. Product and divided-power compatibility are further requirements and should be tested separately. The source does not support an immediate unbounded integral reconstruction theorem.

**First concrete step.** Resolve the essential scan4 generator and hypothesis readings, or explicitly condition the calculation on each surviving interpretation. Write matrices for weights one, two and three and compute their terminal kernels. Compare each with good \(\tau_{\le n}\) of the evaluated complex. A low-weight calculation can expose the correct induction statement; it does not prove all weights. This direction depends on D06 for its admissibility framework and supplies concrete tests for D03.

## D10. Classify bounded holomorphic exceptions and their markings

**Records.** Items: SA09-356, SA09-359, SA09-363, SA09-366, SA09-370. Claims: CL-SA09-138L-064, CL-SA09-138L-071, CL-SA09-138L-072, CL-SA09-138L-073. Problems: MP-SA09-85, MP-SA09-86, MP-SA09-89, MP-SA09-91. **Interest: 10; tractability: 6.**

**Known input.** Every radial orange model \(F_n(z)=4z^n/(1+z^n)^2\) has positive-dilation freedom when its edge midpoints are unmarked. The proposed short exception list is therefore incomplete. Three distinct fixed face prime ends give a sufficient finite rigidity criterion, while fixing appropriate centres or midpoints removes freedom in the examined examples. Fully coloured-dessin realization theorems retain more marking data. The space of invariant rigidifications in the source has neither a recovered definition nor a specified topology (Guillot; Morvan, 2017; `GuillotDessins`, `Morvan2017`; CL-SA09-138L-064,071–073).

**Exact remaining task.** Classify a bounded finite spherical case under explicit embedding and marking conventions, and identify the minimal extra markings that kill each surviving holomorphic stabilizer. If a space of such choices is introduced, define its objects, topology and group action before asking about contractibility.

**First concrete step.** Enumerate the one-parameter Möbius stabilizers compatible with the actual black vertices, graph and face data, keeping white midpoints unmarked unless the chosen convention includes them. Record the effect of adding one centre or midpoint. A few hours can settle a restricted spherical family or exhibit another obstruction. Higher-genus, infinite-map and undefined invariant-contractibility assertions should remain separate until their hypotheses and spaces are stated.

## D11. Write the exact Kummer coordinate companion

**Records.** Items: SA09-132, SA09-135, SA09-136, SA09-138, SA09-139. Claims: CL-SA09-138E-020, CL-SA09-138E-021, CL-SA09-138E-023, CL-SA09-138E-037. Problems: MP-SA09-41, MP-SA09-42, MP-SA09-43, MP-SA09-49. **Interest: 11; tractability: 1.**

**Known input.** For radicals of two the exact arithmetic image is the index-two subgroup \((-1)^b=(2/a)\). The origin-split ambient affine group and the arithmetic extension are different. Over \(\mathbb Q\), the rank-\(r\) image has exact index \(2^r\) in the intrinsic saturated radical automorphism group. Over a general number field, independent algebraic generators give finite index by the verified uniform Kummer-degree statement and the dossier's bounded-index deduction. These are established inputs, not new open-image conjectures (Lenstra, Moree, & Stevenhagen, 2014; Moree & Stevenhagen, 2014; Perucca & Sgobba, 2019; `LMS2014`, `MoreeStevenhagen2014`, `PeruccaSgobba2019`).

**Exact remaining task.** Translate the manuscript's \(K(2)\), \(K(1/2)\), finite revised groups and chosen origins into one compatible coordinate dictionary. State how inversion, origin changes and coboundaries alter the affine parameter. Identify the intended torus and its splitting field before interpreting the dimension glyph or transporting a rational exact-index formula.

**First concrete step.** Make a table with the object, acting group, chosen origin, linear character, translation cocycle and transition map at each level. Reuse the saved level-eight computation as a check of conventions. The few-hours deliverable is a complete companion exposition and one exact coordinate translation; the ambiguous “split” margin remains an image-reading question unless the source is recovered.

## D12. Resolve the consequential manuscript readings

**Records.** Items: SA09-9, SA09-11, SA09-28, SA09-41, SA09-138, SA09-160, SA09-342. Claims: CL-SA09-137-003, CL-SA09-137-004, CL-SA09-137-033, CL-SA09-137-047, CL-SA09-138E-023, CL-SA09-138E-044, CL-SA09-138L-060. Problems: MP-SA09-01, MP-SA09-15, MP-SA09-26, MP-SA09-44, MP-SA09-49, MP-SA09-82. **Interest: 12; tractability: 10 with current source access.**

**Known input.** The reading register already separates transcribed text, proposed alternatives and mathematical evidence. Counterexamples and type checks identify consequential sites without deciding what was written. No scan was inspected in this consolidation. The apparent negation in the cellularity condition, for example, cannot be settled by proving the corrected facewise theorem.

**Exact remaining task.** Obtain original-resolution images and decide the highest-impact readings with neighboring handwriting and deletion/insertion evidence. Preserve an authorial mathematical error if the ink confirms it. An unavailable image should remain an unresolved reading, not become a normalized formula.

**First concrete step.** Review six groups of sites: cote137 scan4's hypothesis and degree bound; scans60–63's P/Q and homology symbols; scan81's associativity superscript; cote138 scan23's splitting margin; scans38–42's root and inverse-root symbols; and scan125's negation and graph/face notation. Record accepted and rejected alternatives with exact image coordinates and the resulting affected claims. With those images a short run could close several editorial blockers; without them, the legitimate output remains the explicit decision matrix already prepared by the dossier.

## Dependencies and stopping points

D06 supplies the category needed by D02 and D09. D01 and D02 specify operations that D03 would have to preserve. D04 fixes the moduli distinctions that D07 must respect. D08 and D09 depend on particular outcomes of D12; D11 can largely proceed from the present text while preserving its one unresolved margin. D05 is independent of those editorial repairs once the exact peripheral ambient group is fixed, but its higher-rank answer is the least predictable few-hours target.

The completed counterexamples, exact sextic orbit, finite map census, normality obstruction for the extended group and corrected strict-clean criterion should be reused as inputs. Recomputing them is justified only to settle a new convention or dependency. Missing project endpoints remain source-retrieval tasks, and the proof statuses in retrieved research returns remain attributed; none of these directions acquires a theorem merely by matching a project label.
