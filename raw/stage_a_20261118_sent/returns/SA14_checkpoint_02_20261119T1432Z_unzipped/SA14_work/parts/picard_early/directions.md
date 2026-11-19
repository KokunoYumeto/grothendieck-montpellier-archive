# Ranked research directions from the early Picard packages

These are proposed future tasks. The consolidation records the existing arguments and checks their stated dependencies; it does not launch any of the projects below. “A few hours” is an estimate of a useful first task, not a claim that an unresolved theorem is easy.

| Rank | Direction | Interest | Useful progress in one short run |
|---|---|---|---|
| 1 | A precise analytic Picard completion theorem | High: a substantial theorem is dispersed across a dated letter and several proofs | High: write one hypothesis-complete statement and dependency diagram |
| 2 | The Poincaré mixed class with fixed conventions | High: a single explicit omitted calculation controls the proposed universal extension | High for the abelian case; lower for unrestricted families |
| 3 | The geometric generic hyperplane claim over its original field | High: the source-field issue materially changes the assertion | Medium: fix topology and group class, then isolate the differential lemma |
| 4 | Henselian algebraization on an arbitrary open | High: Elkik settles an important precise version, leaving a different quantifier to examine | Medium: compare completion ideals before attempting examples |
| 5 | Relative Seshadri construction and the induced relation | Medium–high: this separates a published theorem from stronger draft hypotheses | High for a theorem-by-theorem hypothesis matrix |
| 6 | Projectivity from a tower of ample classes | Medium–high: formal, algebraic and analytic versions have different existence inputs | High for a complete algebraic-model proof; medium for the abstract formal case |
| 7 | Characteristic-p failure and repair of Picard ML | High: the manuscript explicitly marks the characteristic boundary | Medium: reproduce a published rank-jump example with every base hypothesis |
| 8 | Recover the missing theta and Zariski-sheet contexts | Documentary interest: likely removes false mathematical identifications | High if adjacent scans or the original printed edition are supplied |

## 1. Assemble the analytic Picard completion theorem

**Origin:** SA14-46–51, SA14-55, SA14-60, SA14-63, SA14-79; C-SA14-070–089 and C-SA14-140–141; MP-SA14-028–035. The manuscript identifies the source as the Picard group of the analytic germ, expressed by a direct limit over neighborhoods, and separates finite-level universal images from a single convergent representative of a complete compatible system.

The target deliverable would be a theorem for a proper morphism of complex analytic spaces near a fixed base point, with all finite-dimensionality, cohomological comparison and neighborhood conditions stated. It should prove precisely when the germ-to-formal Picard map is injective or surjective, and identify the finite-length condition on the coherent H¹ stalk. Grauert’s direct-image/formal-comparison results, the integral-cohomology input, and the elementary analytic-module completion criterion are available; the proper analytic-local algebraic bridge has a modern source in Abramovich–Temkin 2019, §6.3.4 and Appendix C. The manuscript’s claim of an unwritten exposition in July 1962 must remain separate from a modern proof.

**First step:** rewrite the two exponential long exact sequences as one commutative diagram, with each vertical map labelled and every use of ML assigned to an image system. Include an explicit warning that a bounded coherent complex need not surject onto cohomology at every finite order: C-SA14-081 supplies the tested logical obstruction, not a geometric counterexample to the final theorem.

## 2. Compute the mixed Poincaré class

**Origin:** SA14-12–15; C-SA14-001–010, C-SA14-142; MP-SA14-001–005 and MP-SA14-054. The source proves the pure Künneth components vanish and then explicitly leaves the mixed component uncomputed.

The target is an explicit identification of that component with the duality identity, including the sign determined by the chosen Poincaré rigidification, connection convention and Künneth ordering. Mazur–Messing I.2.6.7 and §3 supply the abelian universal-extension comparison, but their integrable, group-compatible interpretation must be related carefully to the manuscript’s initial sheaf of **all** relative connections. The general-family local-freeness inference at scan83 is not a consequence of merely saying “universal extension.”

**First step:** fix the abelian-scheme setting and write the Čech representative of dlog of the normalized Poincaré bundle. Calculate its mixed evaluation on tangent vectors on the two factors. Leave the cancelled absolute-connection proposal and the unclear scan88 pushout as separate questions until their ink and variance are resolved.

## 3. Test the exact generic-hyperplane statement

**Origin:** SA14-17–22; C-SA14-011–025; MP-SA14-006–010. The manuscript starts with classes defined over the original algebraically closed field and restricts them to a geometric generic hyperplane. It does not automatically start with all classes on the source after extending the ground field.

A modern formulation should specify whether G is finite commutative, smooth connected affine, or another explicitly filtered class; it must specify the fppf or étale topology. Cotner–Zavyalov 2024 gives exact finite-commutative and Picard comparison theorems with additional hypotheses. SGA2 gives conditional integral Picard results. Neither reference validates every row of the informal table or the unspecified characteristic-zero specialization step.

**First step:** formulate and prove, or find a precise counterexample to, the differential-restriction lemma at scan100 using the actual normalization/differential sheaf intended. Keep the verified Veronese cubic counterexample to the dimension-two Pic⁰ row distinct from this surviving group-cohomology question. The cancelled full Picard injection also has its own Segre counterexample.

## 4. Compare different opens and different completions

**Origin:** SA14-65–70; C-SA14-090–099; MP-SA14-036–043. Elkik III.1, Theorem3 and the Picard corollary on pp573–574 settle the comparison for a noetherian henselian pair (A,J), on the complement of V(J), after J-adic completion.

The letter’s wording about an arbitrary open with a specified local completion is broader. Changing from J-adic to maximal-ideal completion while keeping a different open is a mathematical change, not a notational one. The target task is a precise map of the valid comparison results, including whether one needs regularity outside the closed set, excellence, a finite étale neighborhood, or a different completion ideal.

**First step:** place the exact Elkik corollary beside each sentence of the letter and construct the three relevant schemes and their opens. Check which restriction/completion squares are cartesian and which maps are not the maps in Elkik’s theorem. The unidentified Mumford formal example should not be used until its exact source is located.

## 5. Audit the relative divisor and quotient construction

**Origin:** SA14-25–29, SA14-33–37; C-SA14-028–041 and C-SA14-047–054; MP-SA14-011–018 and MP-SA14-021–024. The final EGA IV₄ §21.14.3 theorem is available with its actual smoothness and normality hypotheses; §21.14.4(iv) supplies a separate product case with geometrically normal fibres.

The target is a diagram of implications that distinguishes the support of a divisor, the parameter morphism, the induced equivalence relation and its quotient. Several draft steps need more than density or universal openness. The checks here identify denominator clearing, valuation coefficients, Hartogs descent and the coupled gluing equalizer; they do not establish the broad incidence assertion or every relative LCI variant.

**First step:** compare each handwritten hypothesis with the exact EGA theorem and Seshadri’s published 1963 article. Isolate one proposed strengthening and ask whether the existing proof survives. Do not treat the EGA bibliography’s 1962 date as the article’s verified publication date.

## 6. Make the ample-class selection argument complete

**Origin:** SA14-60–64 and SA14-79; C-SA14-083–089, C-SA14-116; MP-SA14-032–035 and MP-SA14-050. If an inverse system of Picard groups is ML and every thickening has an ample bundle, stabilization at the closed fibre permits selection of an ample class that lifts through the whole tower. This is a limit argument, not eventual equality of every Picard group.

The target should give separate statements for a proper algebraic scheme over a complete base, an abstract proper formal scheme, and a proper analytic germ. Kresch–Mathur Theorem11.11 provides characteristic-zero ML for actual algebraic Picard groups. Coherent formal existence for a proper algebraic model is in Grothendieck exposé182 and Stacks088E. A general formal scheme requires the algebraization theorem appropriate to a formal ample line bundle. Proper analytic-local GAGA is a third input.

**First step:** prove a precise inverse-limit selection lemma and state exactly what compatible line bundle or compatible isomorphisms it produces. Then invoke only the existence theorem whose hypotheses the chosen setting satisfies. The cancelled claim that entire Picard groups eventually stabilize must remain excluded.

## 7. Reproduce a characteristic-p ML obstruction

**Origin:** SA14-53–59; C-SA14-100–116; MP-SA14-044–049. The source’s characteristic-zero argument uses algebraic group images and integral component groups, and flags positive characteristic as difficult.

Kresch–Mathur Theorems1.1 and9.3 give a precise proper smooth complete-DVR criterion in characteristic p: Picard ML is tied to constancy of Néron–Severi rank. This is a strong modern answer in its own setting, not a universal theorem for every formal scheme mentioned in the draft.

**First step:** choose one rank-jump example from the opened paper, verify properness, smoothness, the complete DVR and the NS computations, then identify a fixed level whose restriction images fail to stabilize. This would produce a reusable explanation of the characteristic boundary without claiming a broader counterexample than the construction proves.

## 8. Recover source context for the reused sheets

**Origin:** SA14-40, SA14-81–90, SA14-93; C-SA14-067–069 and C-SA14-118–139; MP-SA14-051–053. The theta sketch lacks the coordinates and normalizations needed to identify its cone/blowup assertion. The Zariski-main-theorem extract includes a truncated lemma and unspecified conductor hypotheses. The printed linear-system material uses historical terminology such as “simple” for nonsingular.

The target is documentary identification followed by a finite mathematical comparison. The normalized elliptic quotient/conic calculation in computations§23 demonstrates a possible standard geometry; it does not identify the unlabelled sketch. Similarly, the complete going-down lemma can be checked without pretending the neighboring truncated lemma has been recovered.

**First step:** obtain the adjacent source pages or the exact n°227/n°293 edition and compare a small set of distinctive sentences. Record the ink decisions separately from all present reconstructions. The congressional schedule, reused letters and printed page numbers must not be used as dates for the handwriting without independent evidence.
