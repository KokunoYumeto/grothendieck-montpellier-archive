# SA14 — Ranked directions for subsequent work

**18 concrete tasks, ordered jointly by mathematical interest and useful progress in a focused run of roughly two to four hours.** A high feasibility rating concerns the bounded output specified below. It is not an estimate that an unsettled general theorem can be proved in that time. These are proposals for later work; this document develops none of them.

The selection combines the early Picard, late Picard/Lefschetz and cote 60 directions with the current root claims and problem records. Every item, claim and problem identifier below is canonical under `research/consolidation_aliases.json`. The known starting points and their limits are those recorded in the consolidation as of 19 November 2026. An unmatched manuscript assertion is not thereby declared open in present-day mathematics.

| Joint priority | Direction | Interest | Useful progress in one run |
|---|---|---|---|
| 1 | Make determinant descent and the three-torsor comparison canonical | Very high | High: one convention and one descent cocycle |
| 2 | Compare the two canonical doubled-theta constructions | Very high | High for the Jacobian case; medium for every base |
| 3 | Specify the category in which formal Hom comparison is fully faithful | Very high | Very high: a precise theorem and hypothesis table |
| 4 | Assemble the analytic Picard completion theorem from its separate arguments | Very high | High: a theorem with an explicit dependency diagram |
| 5 | Match the intrinsic local Picard functor to the resolution construction | Very high | High for a functor comparison; medium for the unrestricted letter |
| 6 | Separate Picard sheafification from representability of the numerical quotient | High | High for one positive case and an exact hypothesis matrix |
| 7 | Compute the omitted mixed Poincaré connection class | Very high | High in the abelian-scheme case |
| 8 | Compare arbitrary opens, henselization and the actual completion ideal | High | Very high: a finite diagram and a concrete cone example |
| 9 | Find the exact wild-torsion boundary of Picard flatness propagation | High | High for a targeted theorem search with fixed hypotheses |
| 10 | Compare Kummer transgression with the generalized-Jacobian torsor | Very high | High over a field; medium for arbitrary relative bases |
| 11 | Describe the codimension-two defect in the printed order formulas | High | Very high for a bounded family of explicit orders |
| 12 | Translate the averaged local factors into epsilon-factor conventions | High | High for one fixed curve and two local points |
| 13 | Produce a source-concordant version of the formal-series recurrence | Medium–high | Very high for a finite comparison and one fresh example |
| 14 | Formulate the generic-hyperplane assertion over its original field | High | Medium–high for the differential lemma and an exact statement |
| 15 | Distinguish Néron–Severi rank jumps, p-primary nonsaturation and Picard Mittag–Leffler | High | Medium: one verified family and two carefully separated tests |
| 16 | Isolate a valid projective-flat permanence theorem for formal Lefschetz | High | Medium for a tractable case and the precise bottleneck |
| 17 | Make the motivic determinant-sign hypotheses explicit | High | High for a hypothesis table; source reading may remain gated |
| 18 | Recover boundary type and lower niveau before studying their obstructions | High | High for a concordance; later mathematics depends on source recovery |

## 1. Make determinant descent and the three-torsor comparison canonical

**Canonical items:** SA14-655; SA14-656; SA14-657; SA14-658; SA14-659; SA14-669; SA14-671.

**Claims:** C-SA14-655; C-SA14-656; C-SA14-657; C-SA14-658; C-SA14-659; C-SA14-669; C-SA14-671.

**Problem anchors:** MP-SA14-655; MP-SA14-658; MP-SA14-669; MP-SA14-671.

**What it would establish.** A hypothesis-complete comparison between the determinant maps on Picard components and their contracted torsors, with the normalization that makes the comparison canonical stated explicitly.

**What is already known.** The determinant construction, its base-change requirements and the exponent −χ under change of basepoint are checked. Put Q=Alb¹(X), P=Pic_X^δ and R=Pic_B^{φ(δ)}. With the positive Poincaré kernel and h_M(β)=t_β^*M⊗M⁻¹, tensoring by β gives the Picard-class difference +h_M(β). Thus the normalized map has equivariance (−χ,+h), and its section belongs to R+χQ−h_*P. The manuscript product has the same meaning if its tilde map is −h. Movement of a divisor support by −β supplies no additional minus. Knudsen–Mumford and Mukai provide the published formalism; equality of torsor classes alone does not choose the required isomorphism.

**First concrete step.** Fix these conventions on one pointed smooth proper curve, write the Čech cocycle for two local basepoints, and compare the determinant isomorphisms on triple overlaps. Check the curve theta sign in the same convention.

**Bounded output.** A single signed diagram and an explicit list of the rigidifications needed for canonical descent. The remaining task is coherence of the comparison; the modern tensor/translation sign has already been corrected in the consolidation.

**Opened starting references:** `R_KnudsenMumford1976`; `R_Mukai1981` (full records in `SA14_references.bib`).

## 2. Compare the two canonical doubled-theta constructions

**Canonical items:** SA14-664; SA14-666; SA14-672; SA14-673.

**Claims:** C-SA14-664; C-SA14-666; C-SA14-672; C-SA14-673.

**Problem anchors:** MP-SA14-664; MP-SA14-666; MP-SA14-672.

**What it would establish.** Whether the section obtained by inversion of the canonical theta pair agrees, under a specified identification of torsors, with the normalized Poincaré pullback representing twice the polarization.

**What is already known.** Alexeev gives the principal-polarization theta-pair construction. The pullback (1,λ)^*P represents 2λ with its rigidification. For a Jacobian, the involution L↦K_C⊗L⁻¹ on Pic^{g−1} gives the doubled section K_C. The gcd calculation establishes annihilation of a torsor class; even when this implies existence of a section of the relevant contracted power, it does not identify canonical sections. Arbitrary polarization types have additional issues and are outside this initial task.

**First concrete step.** Use one smooth pointed curve. Identify the two doubled torsors, compare their normalized fibres at the identity, and track the involution under that identification before extending the comparison over a base.

**Bounded output.** A complete Jacobian comparison, or an exact residual normalization discrepancy. An all-base claim should follow only after the descent data are checked.

**Opened starting references:** `R_Alexeev2002`; `R_PoonenStoll1999` (full records in `SA14_references.bib`).

## 3. Specify the category in which formal Hom comparison is fully faithful

**Canonical items:** SA14-302; SA14-304; SA14-341; SA14-342; SA14-305; SA14-308.

**Claims:** C-SA14-300; C-SA14-301; C-SA14-302; C-SA14-303; C-SA14-307.

**Problem anchors:** MP-SA14-248; MP-SA14-249; MP-SA14-250; MP-SA14-251.

**What it would establish.** The exact depth-controlled category supported by the formal-completion argument, together with a clear separation of full faithfulness from its still-incomplete essential-image assertion.

**What is already known.** Raynaud I.1.1–1.5 supplies the comparison framework. The checked application requires a noetherian local ring that is a quotient of a regular ring and is complete for (t), and target depth at least two at points closed in the puncture outside V(t). The unrestricted Serre-quotient fullness claim fails; exactness, faithfulness and conservativity do not repair it. The source labels a, b, c′ and T₁ remain partly undefined.

**First concrete step.** Place the manuscript objects beside Raynaud’s category C. Write the off-divisor condition point by point, then identify precisely which coherent-hull or extension clauses need the missing definitions.

**Bounded output.** A finished comparison statement and a bounded source request for the essential image. A new unrestricted algebraization theorem is not an expected short-run result.

**Opened starting references:** `Raynaud1974Lefschetz` (full records in `SA14_references.bib`).

## 4. Assemble the analytic Picard completion theorem from its separate arguments

**Canonical items:** SA14-46; SA14-55; SA14-49; SA14-47; SA14-80; SA14-60; SA14-79; SA14-78; SA14-53.

**Claims:** C-SA14-070; C-SA14-071; C-SA14-079; C-SA14-080; C-SA14-081; C-SA14-089; C-SA14-140; C-SA14-141.

**Problem anchors:** MP-SA14-028; MP-SA14-029; MP-SA14-032; MP-SA14-035.

**What it would establish.** One precise theorem distinguishing Picard classes on the analytic germ, their images at each finite order, and a compatible formal line bundle; it should state the finite-length criterion and each proper analytic comparison hypothesis.

**What is already known.** The source separates fixed-level stable images from convergent representatives of entire compatible systems. Formal functions gives a completed cohomology module; it does not imply surjectivity onto every finite-order cohomology group. The consolidation supplies a finite-complex countertest to that inference, not a geometric counterexample to the final theorem. Grauert’s direct-image results and the proper analytic-local bridge provide the relevant comparison tools. Uniform stabilization and eventual constancy of the entire Picard tower are stronger assertions.

**First concrete step.** Write the analytic and formal exponential long exact sequences in one diagram. Label every vertical map, assign each use of Mittag–Leffler to its actual image system, and isolate the proper GAGA input.

**Bounded output.** A complete scoped statement with a proof outline and an explicit list of hypotheses imported from published results. The dated letter’s claim about an unwritten exposition remains a separate historical fact.

**Opened starting references:** `PE_Grauert1960`; `PE_Grauert1963`; `PE_AbramovichTemkin2019` (full records in `SA14_references.bib`).

## 5. Match the intrinsic local Picard functor to the resolution construction

**Canonical items:** SA14-601; SA14-602; SA14-603; SA14-604; SA14-605; SA14-676.

**Claims:** C-SA14-601; C-SA14-602; C-SA14-603; C-SA14-604; C-SA14-605; C-SA14-676.

**Problem anchors:** MP-SA14-601; MP-SA14-603; MP-SA14-604; MP-SA14-605; MP-SA14-676.

**What it would establish.** Which exact local Picard functor is represented in the modern geometric setting, and how its quotient description compares with the letter once the coefficient field, test algebras and topology are fixed.

**What is already known.** Boutot and Kollár establish substantial geometric versions; the cited setting includes S₂, pure dimension at least three and essential finite type over a field. The resolution sequence uses exceptional divisors of codimension one. Over a non-separably-closed residue field the exceptional lattice can be twisted, and rational points carry both a lattice-cohomology issue and a Picard-sheaf descent obstruction. Conditional stabilization from an ample conormal is proved. Tangent vanishing alone establishes neither representability nor countability of components.

**First concrete step.** Write the letter’s completed-base-change functor beside the exact functor in Boutot. Compare them first on fields and Artin test algebras, and draw the quotient and obstruction sequence for two models dominated by a common model.

**Bounded output.** A precise comparison in one established setting, with model independence, coefficient-field dependence and the wider countability question kept distinct.

**Opened starting references:** `R_Boutot1978`; `R_Kollar2014`; `R_Lipman1976`; `R_Lipman1975` (full records in `SA14_references.bib`).

## 6. Separate Picard sheafification from representability of the numerical quotient

**Canonical items:** SA14-214; SA14-217; SA14-215; SA14-216; SA14-639; SA14-687.

**Claims:** C-SA14-205; C-SA14-206; C-SA14-207; C-SA14-208; C-SA14-639; C-SA14-687.

**Problem anchors:** MP-SA14-204; MP-SA14-205.

**What it would establish.** When the numerical quotient Pic/Pic^τ is a scheme, when only an algebraic-space quotient is supplied, and which prior representability assumptions the draft’s argument actually uses.

**What is already known.** Numerical equivalence agrees with τ-equivalence in the checked proper-field setting. Closedness of a kernel tests separatedness after a represented faithfully flat quotient is available; it does not produce that quotient. The relative Picard object is a sheaf of relative classes. Under universal f_*O_X=O_S, a section supplies its rigidified line-bundle description; C-SA14-687 gives the stated finite-Stein-factor replacement with universal O_Σ=φ_*O_X. Kleiman’s particular smooth proper relation theorem does not imply arbitrary scheme representability.

**First concrete step.** Define the fppf quotient and its equivalence relation in one of the source’s proper-flat families. Test every hypothesis of a specific quotient theorem, and state exactly where a global line bundle, a rigidified bundle or only a relative class is being used.

**Bounded output.** One complete positive representability statement and a sharply delimited remainder for the attempt to represent the quotient without first representing all of Pic.

**Opened starting references:** `Grothendieck1962FGA236Complement`; `Kleiman2005Picard`; `R_Kleiman2005` (full records in `SA14_references.bib`).

## 7. Compute the omitted mixed Poincaré connection class

**Canonical items:** SA14-12; SA14-14; SA14-13.

**Claims:** C-SA14-003; C-SA14-006; C-SA14-008; C-SA14-009; C-SA14-142.

**Problem anchors:** MP-SA14-001; MP-SA14-002; MP-SA14-003; MP-SA14-054.

**What it would establish.** The mixed component as the duality identity, with its sign fixed by the Poincaré rigidification, the connection convention and the order of the Künneth factors.

**What is already known.** The restrictions to both zero sections kill the pure Künneth components. The manuscript explicitly leaves the mixed calculation unfinished. Mazur–Messing gives the abelian universal-extension comparison with its integrable and group-compatible structures. The initial source sheaf permits arbitrary relative connections, so its identification with that universal extension needs an explicit comparison. The cancelled pullback-torsor proposal has a separate variance ambiguity.

**First concrete step.** Choose a normalized Poincaré bundle on an abelian scheme and its dual. Write a Čech representative of dlog and evaluate the mixed term on tangent vectors from the two factors.

**Bounded output.** A convention-complete abelian calculation and the exact additional conditions needed to relate it to the source’s all-connections sheaf. The cancelled absolute-connection proposal stays outside the established theorem.

**Opened starting references:** `PE_MazurMessing1974` (full records in `SA14_references.bib`).

## 8. Compare arbitrary opens, henselization and the actual completion ideal

**Canonical items:** SA14-65; SA14-67; SA14-624; SA14-625; SA14-626; SA14-212.

**Claims:** C-SA14-090; C-SA14-097; C-SA14-624; C-SA14-625; C-SA14-626.

**Problem anchors:** MP-SA14-036; MP-SA14-040; MP-SA14-043; MP-SA14-624; MP-SA14-626.

**What it would establish.** The exact range of the letter’s arbitrary-open comparison, with the punctured whole cone, punctured local spectrum, henselization and completion treated as distinct spaces.

**What is already known.** Elkik settles Picard comparison for a noetherian henselian pair (A,J), on the complement of V(J), after J-adic completion. This is an isomorphism of Picard groups and does not imply full faithfulness of the groupoid of line bundles. Replacing J-adic completion by maximal-ideal completion while retaining another open requires a separate argument. The smooth plane-quartic cone already has a one-dimensional characteristic-zero formal correction in the checked positive-twist calculation.

**First concrete step.** Draw the four spaces for that cone and the two different ideals appearing in the proposed generalization. Mark which open is the inverse image of which, then place Elkik’s exact corollary on the corresponding arrow.

**Bounded output.** A finished hypothesis and map comparison. Any remaining m-adic assertion for a different open becomes a separately quantified question; the established Elkik theorem needs no new proof.

**Opened starting references:** `PE_Elkik1973`; `R_Elkik1973`; `R_Kollar2014` (full records in `SA14_references.bib`).

## 9. Find the exact wild-torsion boundary of Picard flatness propagation

**Canonical items:** SA14-255; SA14-16.

**Claims:** C-SA14-243; C-SA14-244; C-SA14-251; C-SA14-252; C-SA14-258.

**Problem anchors:** MP-SA14-215; MP-SA14-216; MP-SA14-221.

**What it would establish.** Whether the written implication Pic⁰-flat ⇒ Pic^τ-flat holds under the manuscript’s actual represented-family hypotheses, and precisely which part is already covered by tame torsion.

**What is already known.** FGA236 Proposition 2.10(i) proves propagation to Pic^σ; its σ uses prime-to-characteristic orders. It does not establish the full wild τ assertion. Multiplication by n invertible on the base is étale in the checked setting. The annotated nonflat example refutes an unconditional flatness hope, but it should not be reused as a counterexample to a stronger conditional statement without checking its identity component.

**First concrete step.** Fix the base, proper-flat family, represented Picard object and exact identity-component flatness assumption. Follow citations of FGA 2.10 for the p-primary component and test any candidate example against all four conditions.

**Bounded output.** An exact later theorem match or a verified counterexample; if neither is found, a bounded unmatched statement with the search limits recorded. Historical uncertainty does not by itself establish present-day openness.

**Opened starting references:** `Grothendieck1962FGA236` (full records in `SA14_references.bib`).

## 10. Compare Kummer transgression with the generalized-Jacobian torsor

**Canonical items:** SA14-640; SA14-641.

**Claims:** C-SA14-640; C-SA14-641.

**Problem anchors:** MP-SA14-641.

**What it would establish.** The precise sign and hypotheses in the proposed equality between the compact-support Leray transgression and the Kummer boundary of the degree-one Picard torsor of the pinched curve.

**What is already known.** The generalized-Jacobian and Kummer identifications are checked with a nonempty finite étale puncture and n invertible. The opened field-level and semiabelian extension formulas closely match the source. They do not automatically prove the full relative compact-support equality, and the page itself asks for the comparison.

**First concrete step.** Fix one field and one punctured smooth proper curve. Choose a common Čech convention, write the degree-one torsor cocycle and the compact-support distinguished triangle, and compare the resulting two boundary cocycles.

**Bounded output.** A complete field-case calculation or an explicit normalization discrepancy, followed by a list of the base-change and descent inputs needed for the relative statement.

**Opened starting references:** `R_MVW2006`; `R_HarariSzamuely2009`; `R_PetrovSkorobogatov2026` (full records in `SA14_references.bib`).

## 11. Describe the codimension-two defect in the printed order formulas

**Canonical items:** SA14-462.

**Claims:** C-SA14-467; C-SA14-472; C-SA14-563; C-SA14-564.

**Problem anchors:** MP-SA14-414.

MP-SA14-414 is the source-recovery dependency for the reused algebra sheets. It is not an unresolved version of the local criteria, which are proved in this consolidation.

**What it would establish.** A useful global comparison that records the defect lost by height-one localization, and a precise explanation of which reflexivity hypothesis would make the printed conductor identity valid.

**What is already known.** The global equality C:B=B*:C* fails for C=A+(x,y)√2 inside B=Q(√2)[x,y], with A=Q[x,y], while its height-one version and its reflexive-order version are proved. The local multiplier criterion D:D=C ⇔ ω invertible and the semilocal quotient criterion are also proved under their stated order, Cohen–Macaulay and separable-trace assumptions. These local facts cannot detect a codimension-two discrepancy.

**First concrete step.** Keep the same characteristic-zero quadratic extension and compare two explicitly chosen (x,y)-primary ideals I in orders A+I√2. Compute C**, C:B and B*:C*, then identify the support and length of the conductor defect before proposing a general exact sequence.

**Bounded output.** A small family of fully certified examples and a precise candidate defect statement. Recovering adjacent printed context remains a separate archival step; stationery and print dates do not date the handwriting.

**Opened starting references:** `Stacks0BW0`; `Stacks0BM4`; `Marseglia2019Powers` (full records in `SA14_references.bib`).

## 12. Translate the averaged local factors into epsilon-factor conventions

**Canonical items:** SA14-453; SA14-457; SA14-492; SA14-455; SA14-456; SA14-458.

**Claims:** C-SA14-439; C-SA14-440; C-SA14-441; C-SA14-443; C-SA14-444; C-SA14-445; C-SA14-446.

**Problem anchors:** MP-SA14-407; MP-SA14-408; MP-SA14-409; MP-SA14-410.

**What it would establish.** A sign-sensitive dictionary from the manuscript’s averaged virtual extension and determinant factors to the local constants in the published curve product formula.

**What is already known.** The averaging argument and μ cancellation are checked in the specified quasi-unipotent category. The modified Euler characteristic follows from the degree-weighted Grothendieck–Ogg–Shafarevich formula and the finite-support correction. Deligne and Laumon supply local constants and the global product theorem. The manuscript’s squared determinant identity cannot choose the square-root sign, and similarly named local factors need not have identical normalization.

**First concrete step.** Fix geometric Frobenius, an additive character and a differential. Compute one tame rank-two Jordan-block example at a rational missing point, then repeat at one closed point of degree greater than one, preserving all degree factors.

**Bounded output.** A complete convention table and one checked local-to-global example. Variation of sheaf or curve can be formulated afterward with the auxiliary data held fixed.

**Opened starting references:** `Deligne1973Constants`; `Laumon1987Fourier`; `Raynaud1965Euler` (full records in `SA14_references.bib`).

## 13. Produce a source-concordant version of the formal-series recurrence

**Canonical items:** SA14-489; SA14-487.

**Claims:** C-SA14-498; C-SA14-503; C-SA14-565; C-SA14-567.

**Problem anchors:** MP-SA14-414.

MP-SA14-414 anchors recovery of cut exercise antecedents. The positive-exponent recurrence and the two literal counterexamples are already checked; no present-day open theorem is being asserted.

**What it would establish.** Which exponent range, coefficient normalization and within-block recurrence belong to the complete printed statement, and how that statement relates to the surviving draft exercise.

**What is already known.** The allowance of zero exponents is false under the literal printed hypotheses. A general positive-exponent block proof is saved. For v=xy−z^{i−1}T and v′=Σb_n x^{−n−1}T^n, the exact within-block relation is yb_{n+1}=z^{i−1}b_n; the printed division by x fails even in the checked positive coprime example. Samuel’s opened publications supply exact comparison passages. The 1962 talk date and the surviving text’s later references must remain distinct.

**First concrete step.** Put the exercise beside the exact Samuel passages and compare every symbol in the first two coefficients. Select one further positive triple satisfying the full relevant hypotheses, including any hypotheses needed only for the factoriality application, and prepare an independently inspectable coefficient certificate.

**Bounded output.** A short annotated theorem and a draft-to-publication concordance. Deciding whether the differing letter is a transcription issue or an error in the source requires the scan.

**Opened starting references:** `Samuel1962Derivations`; `Samuel1964TIFR`; `Samuel1964Mechants` (full records in `SA14_references.bib`).

## 14. Formulate the generic-hyperplane assertion over its original field

**Canonical items:** SA14-17; SA14-18; SA14-19; SA14-20; SA14-21; SA14-22.

**Claims:** C-SA14-011; C-SA14-012; C-SA14-013; C-SA14-014; C-SA14-015; C-SA14-016; C-SA14-017; C-SA14-018; C-SA14-019; C-SA14-020; C-SA14-021; C-SA14-022; C-SA14-023; C-SA14-024; C-SA14-025.

**Problem anchors:** MP-SA14-006; MP-SA14-007; MP-SA14-008; MP-SA14-010.

**What it would establish.** A precise surviving Lefschetz question in which the starting classes are defined over the original field, the target is a geometric generic hyperplane, and the group and cohomology topology are fixed.

**What is already known.** The draft restricts classes defined over the original field; replacing them by all classes after scalar extension changes the assertion. Some displayed Picard rows are refuted by the recorded Veronese and Segre examples. Cotner–Zavyalov gives precise finite-commutative comparisons under additional assumptions, and SGA2 supplies conditional integral Picard results. Neither settles an unspecified affine-group filtration or the unwritten characteristic-zero specialization step.

**First concrete step.** Choose the finite-commutative fppf version or another explicitly filtered commutative group class. Write the differential-restriction lemma at scan 100 with its actual normalization and differential sheaf, and test its hypotheses before attempting the larger table.

**Bounded output.** One well-posed theorem or counterexample question, with the original field, dimension and group-scheme versus geometric-point distinctions explicit.

**Opened starting references:** `PE_CotnerZavyalov2024`; `PE_SGA2` (full records in `SA14_references.bib`).

## 15. Distinguish Néron–Severi rank jumps, p-primary nonsaturation and Picard Mittag–Leffler

**Canonical items:** SA14-52; SA14-53; SA14-55; SA14-57; SA14-64; SA14-223; SA14-253; SA14-246.

**Claims:** C-SA14-100; C-SA14-111; C-SA14-112; C-SA14-116; C-SA14-216; C-SA14-217.

**Problem anchors:** MP-SA14-044; MP-SA14-049; MP-SA14-208.

**What it would establish.** A worked example explaining the Mittag–Leffler obstruction in positive residue characteristic, with a separate assessment of the source’s proposed finite-subgroup divisibility mechanism.

**What is already known.** Kresch–Mathur Theorem 1.1 in the opened arXiv v2 states: for X proper smooth over a complete DVR A with positive residue characteristic, the Picard tower is Mittag–Leffler exactly when rk NS(X₀)=rk NS(X_η). The NS groups here are over the actual closed and generic fields as defined in their Definition 4.5; a geometric-field variant needs separate justification. The theorem includes mixed characteristic. Maulik–Poonen supplies verified specialization phenomena by a different construction. A p-primary cokernel between equal-rank lattices does not itself change rank, so the source’s divisibility mechanism gives no Mittag–Leffler conclusion without a separate rank calculation. Its subgroup containments remain conditional and its literal arrows need scan resolution. Eventual constancy of the entire Picard tower is also stronger than Mittag–Leffler.

**First concrete step.** Choose one published rank-jump family and verify properness, smoothness, the complete DVR with positive residue characteristic and its actual-field NS calculation. Identify the failure of stabilization at a fixed level if the theorem applies. In separate rows record the two actual-field ranks, any separately justified geometric ranks, the torsion of a defined specialization map and whether the exact subgroup containments proposed in the manuscript occur.

**Bounded output.** One complete example with rank change, saturation and fixed-level image stabilization distinguished. Any attempt to realize the manuscript’s specific finite-subgroup mechanism then has a precisely stated additional target.

**Opened starting references:** `PE_KreschMathur2025`; `MaulikPoonen2012NS` (full records in `SA14_references.bib`).

## 16. Isolate a valid projective-flat permanence theorem for formal Lefschetz

**Canonical items:** SA14-294; SA14-295; SA14-296; SA14-297; SA14-298; SA14-299; SA14-300.

**Claims:** C-SA14-293; C-SA14-294; C-SA14-295; C-SA14-296; C-SA14-297; C-SA14-298.

**Problem anchors:** MP-SA14-242; MP-SA14-243; MP-SA14-244; MP-SA14-245; MP-SA14-246.

**What it would establish.** A scoped permanence statement separating cohomological comparison, algebraization of coherent sheaves and effectivity of projective schemes.

**What is already known.** The checked conditional route uses bounded perfect derived pushforwards, compatible base change and formal limits. SGA2 and Raynaud provide relevant comparison and existence theorems, but the broad manuscript formulation does not establish every perfectness or effectivity input. Removing quasi-projectivity is a separate strengthening. Shrinking away a closed nonflat locus is valid only after the needed finite-presentation and proper-support conditions are in place.

**First concrete step.** Choose the source’s projective morphism and one relatively flat coherent sheaf with proper support. Write the exact derived pushforward statement required, then test boundedness, perfectness, base change and support independently.

**Bounded output.** A complete positive case and a precise list of the missing inputs for the broader statement. The proposed auxiliary faithfully flat module should be used only after its base and descent role are defined.

**Opened starting references:** `Grothendieck1968SGA2`; `Raynaud1974Lefschetz` (full records in `SA14_references.bib`).

## 17. Make the motivic determinant-sign hypotheses explicit

**Canonical items:** SA14-408; SA14-409; SA14-410; SA14-416; SA14-417; SA14-420; SA14-421; SA14-418; SA14-422.

**Claims:** C-SA14-406; C-SA14-407; C-SA14-408; C-SA14-413; C-SA14-414; C-SA14-415; C-SA14-416.

**Problem anchors:** MP-SA14-401; MP-SA14-402.

**What it would establish.** Which conclusions in the sign argument follow from purity, rationality, a given selfduality, or an alternating polarization, and which of those structures the source actually admits.

**What is already known.** The consolidation includes rank-one scope tests and a symmetric two-dimensional similitude showing why these conditions cannot be conflated. They are not counterexamples to a statement whose standing geometric polarization supplies the missing structure. A given generic isomorphism of lisse sheaves extends on a normal integral scheme; existence of that selfduality is a different assertion. Deligne’s geometric weight results and Jannsen’s numerical semisimplicity have different hypotheses and consequences.

**First concrete step.** Create one row per source object and one column per required structure. Start with the exact “si on admet” passages and mark assumption, proved property and unreadable convention separately; then match each claimed implication to its precise theorem.

**Bounded output.** A corrected explanatory table for the determinant signs and a minimal scan request. A proof of standard conjectures is outside this bounded task.

**Opened starting references:** `Deligne1974WeilI`; `Deligne1980WeilII`; `Jannsen1992Numerical`; `Stacks0BQM` (full records in `SA14_references.bib`).

## 18. Recover boundary type and lower niveau before studying their obstructions

**Canonical items:** SA14-425; SA14-427; SA14-423; SA14-430; SA14-459.

**Claims:** C-SA14-419; C-SA14-421; C-SA14-422; C-SA14-447; C-SA14-448; C-SA14-449; C-SA14-450; C-SA14-451.

**Problem anchors:** MP-SA14-403; MP-SA14-404; MP-SA14-411; MP-SA14-412.

**What it would establish.** Two precise predicates: the source’s boundary “type” and its permitted lower-niveau factors. Only after recovering them can one formulate a weight comparison or a restricted norm-one cocycle problem.

**What is already known.** The cone-duality shift is fixed as −1 in the chosen cohomological convention, and the unrestricted rational involution calculation is complete. Neither identifies the missing type invariant or the allowed subgroup H of factors. Weil II weight inequalities and Wildeshaus’s resolution-dependent boundary result do not define the source’s terms. Ordinary Hilbert 90 would only answer the unrestricted problem that the manuscript explicitly excludes.

**First concrete step.** Concord every occurrence of type, niveau and the indexed factors in the supplied text, then request the exact adjoining definitions and scans 65, 67 and 69. If these determine an involution-stable H, test fixed-point order parity in one explicitly allowed finite-support model.

**Bounded output.** A source-faithful definition dossier and, conditionally, one finite model obstruction calculation. If the definitions remain unavailable, the mathematical target stays explicitly unformulated.

**Opened starting references:** `Deligne1980WeilII`; `Wildeshaus2006Boundary`; `Deligne1973Constants` (full records in `SA14_references.bib`).

## Source gates and quarantined comparisons

The mathematical tasks above start from supplied passages, saved independent checks or opened published sources. No direction assumes a result from an unavailable earlier project. La Longue Marche, Les Dérivateurs, WG2, S6, Hua and the unavailable external cotes remain quarantined comparison leads. Bringing such a source into a later workspace would permit a new comparison; the present links do not certify its contents.

No scans or second-pass files were supplied for this consolidation. Where a direction requires an ink decision, the bounded output can be a precise source request or a conditional commentary. In particular, the printed algebra and editorial sheets have their own attribution: locating their edition or first circulation does not date Grothendieck’s handwriting. The local-order and recurrence tasks use MP-SA14-414 only for the missing-source dependency; editorial planning records MP-SA14-415 and MP-SA14-416 are not repurposed as mathematical conjectures.

Stable published identifications are used as starting points. The list does not recast the exact Elkik Picard comparison, the already-proved local order criteria, the positive-exponent recurrence, the principal theta-pair theorem or the fixed cone shift as new open problems. The work proposed is the explicitly stated comparison, extension within fixed hypotheses, source recovery or concrete example.

## Reproducibility

The authored selection is stored in `research/final_directions_selection.json`. `scripts/build_final_directions.py` renders this document, resolves the explicit alias map, checks every cited item/claim/problem against the consolidated registers and checks each bibliographic key. Its output is `outputs/final_directions_validation.txt`. The three saved inspection programs are `scripts/directions_inventory.py`, `scripts/directions_selected_records.py` and `scripts/directions_core_inventory.py`; their saved inventories and the actual chunks read are listed in `outputs/directions_source_reads.txt`. These programs format and validate authored choices; they do not infer research verdicts.
