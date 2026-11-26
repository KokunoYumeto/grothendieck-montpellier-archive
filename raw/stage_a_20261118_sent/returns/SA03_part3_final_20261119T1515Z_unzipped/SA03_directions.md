# Ranked research directions

These are tasks cut from the consolidation. They have **not** been developed
here beyond the source, proof and computation checks required for the dossier.
Interest and reach in one run are separate scores from 1 (low) to 5 (high).
The overall rank balances mathematical value, evidential readiness and a useful
deliverable after a few hours; it is not a promise to solve a general conjecture.
Where a scan or an absent source is needed, that is the first input to obtain.

The ranking consolidates 20 cross-folder tasks and 16 further tasks from the
complete Codex-only blocks. The two numeric scores use one scale throughout:
5 is high interest or high reach, 1 is low. They are editorial assessments,
not estimates of a conjecture's probability. The local direction files preserve
their original rankings; `DIRECTION_CONCORDANCE.tsv` maps them to this list.


## 1. Compatible infinitesimal lifts and the geometric obstruction square

**Interest 5; one-run reach 4.** Anchors: SA03-3, SA03-8, SA03-60;
CL-SA03-002, CL-SA03-003, CL-SA03-004, CL-SA03-005; MP-SA03-01, MP-SA03-03.

The combined module presentation is already repaired, while the geometric Ext
comparison remains distinct from existence of a lift. A focused run should put
the actual graph-ideal maps into that presentation and compare the two
obstruction classes naturally in the coefficient module. The intended result is
one precise naturality lemma or an exact remaining obstruction, with existence,
compatibility and torsor transitivity kept separate.

## 2. Historical finite-group objects versus filtered perfect complexes

**Interest 5; one-run reach 4.** Anchors: SA03-656, SA03-658, SA03-664;
CL-SA03-654, CL-SA03-655, CL-SA03-659; MP-SA03-100, MP-SA03-101, MP-SA03-103.

Lau gives the perfect-ring finite category, Faltings gives the nilpotent-PD
deformation theorem, and the 2025 F-gauge paper gives a newer classification.
First make a dictionary of variance, Tor degrees, scalar-flatness, F/V and
filtration for one finite group. The deliverable would identify exactly which
historical request each modern theorem answers, especially at level one where
finite p-groups and BT₁ differ. It should not invent the author's unnamed
candidate.

## 3. Determine the precise nonlinear cokernel criterion

**Interest 5; one-run reach 4.** Origins: SA03-1064–1065; CL-SA03-1064–1065; MP-SA03-177. Source: K93-06, scan217, lines327–370.

The manuscript gives explicit cohomological flatness and kernel-flatness conditions and concludes that the additive p-curvature obstruction cokernel is a vector bundle. The map γ is not O-linear, so linear constant-rank reasoning does not settle the assertion. The existing checks prove the smooth proper curve case has zero fppf cokernel; they neither prove nor refute the full criterion. Mazur–Messing and Bost–Künnemann give related representability statements, with different explicitly stated hypotheses.

**What the task would establish:** an exact theorem or counterexample to the written conditions(a)–(c), with the topology of the cokernel and the distinction between sheaf image and image of rational points fixed. **First concrete step:** transcribe those three conditions from the scan, formulate γ as a homomorphism of additive fppf sheaves between the specified vector bundles, and analyze whether its Frobenius-leading term yields a quotient vector group after an appropriate local decomposition. Do not assume étaleness: even the curve map can have inseparable fibres.

## 4. Wild elliptic deformation quotients

**Interest 5; one-run reach 3.** Anchors: SA03-615, SA03-616, SA03-619;
CL-SA03-623, CL-SA03-624, CL-SA03-625, CL-SA03-626; MP-SA03-93.

The full geometric automorphism groups and equal-characteristic valuation
constraints are checked; the effective wild action on a universal deformation
is not. Fix an algebraically closed characteristic-2 base and one explicit
versal coordinate, then derive the effective action before computing invariants.
The result would separate the actual coarse local ring from a group-order
heuristic and from a tame quotient valid only away from small primes.

## 5. Recover the characteristic-two replacement for the projective-connection dictionary

**Interest 5; one-run reach 4.** Sources: SA03-1240, SA03-1246, SA03-1247, SA03-1249; CL-SA03-1297, CL-SA03-1306–1311, CL-SA03-1315–1316; MP-SA03-203 and MP-SA03-207.

The pages explicitly warn about characteristic two, and the calculation explains why. The Lie algebra `pgl₂` has a six-dimensional derivation algebra in characteristic two, compared with its three-dimensional inner derivations. The two filtration symbols are `−2a₀` and `a₀`; the first loses information when two vanishes. In addition, group Borels still make sense while the usual maximal-solvable-subalgebra definition does not recover the same flag variety from the now-solvable Lie algebra. These are distinct obstructions, not one missing sign.

The known comparator is the odd-characteristic Schwarz-structure theory in Mochizuki, Chapter I, Theorems 1.7, 1.9 and 1.11. SGA 3, Exposé XXIV, Proposition 4.2.1 supplies the integral group-theoretic descent of Borel/Cartan varieties. Neither settles the page's characteristic-two question by a change of notation.

**First concrete step:** specify connections on the `PGL₂`-torsor itself and compute their induced Lie connections over `F₂[ε]/ε²`. Compare the image with all bracket-compatible Lie connections, recording exactly which of the three outer-derivation parameters occur. A successful short run would produce a precise replacement statement or a small obstruction example, with the group and Lie categories kept separate.

## 6. Ordinary crystals, admissibility and canonical filtration

**Interest 5; one-run reach 3.** Anchors: SA03-653, SA03-654, SA03-665,
SA03-668, SA03-669; CL-SA03-652, CL-SA03-653, CL-SA03-660, CL-SA03-661;
MP-SA03-98, MP-SA03-99, MP-SA03-104, MP-SA03-105.

Modern full-faithfulness and image results are base-sensitive, and ordinary
Frobenius diagnostics do not settle the crystalline formulation. First write the
historical site, its Frobenius pullback and admissibility condition in one set
of conventions, then compare them with Lau's exact lemmas. A few hours can
produce a justified hypothesis chart and isolate one remaining implication;
they cannot justify an unrestricted equivalence by analogy.

## 7. Identify a meaningful strengthened version of question e

**Interest 5; one-run reach 4.** Origins: SA03-1035–1040; CL-SA03-1035–1040; MP-SA03-166–169. Source: K93-05, scans196–198, lines58–108.

The literal every-closed-point Verschiebung lifting condition is refuted by the explicit elliptic example. The adjacent universal-vector-extension condition is stronger and is settled by the rank-one p-curvature theorem. Between them lie choices about a fixed connection, compatibility of lifts, rational versus scheme-theoretic images, and a uniform exponent. These should be expressed as different statements before searching for a bridge between them.

**What the task would establish:** an exact implication diagram identifying the weakest additional compatibility that recovers the rank-one theorem, and the status of the broader subgroup questiond. **First concrete step:** write questionc and questione as functors of sections over one arithmetic model, project the canonical zero-p-curvature subgroup, and record the obstruction to choosing a compatible lift in the universal extension. Test every proposed strengthening against the already checked elliptic example. The counterexample itself is complete; re-enumerating more primes adds nothing.

## 8. Classify the low-order integral Schwarzian cocycles under the exact axioms

**Interest 5; one-run reach 3.** Sources: SA03-1221–1222, SA03-640, SA03-1224–1226; CL-SA03-1257–1269; MP-SA03-195–197.

The integral operation

\[
Q(f)=\left(\frac{D^{(2)}f}{D^{(1)}f}\right)^2-
\frac{D^{(3)}f}{D^{(1)}f}
\]

has a verified Hasse-derivative cocycle identity and is nonzero as an operation in characteristics two and three. Its existence is therefore secure. The harder assertion is uniqueness under the manuscript's variable-base, naturality, differential-order and nondegeneracy conditions. The uncertain “faux?!” annotation on scan 74 is material. Frobenius perturbations disprove a naive transfer of the complex kernel theorem, but they do not settle the weaker fixed-characteristic uniqueness claim.

**First concrete step:** transcribe the exact axiom list into a universal jet-ring problem, first with order at most three. Compute the linear constraints on candidate rational jet expressions after clearing powers of the first derivative, separately over `Z`, `F₂`, `F₃` and a symbolic prime greater than three. The useful deliverable would be a finite classification at the chosen order and a precise statement of which unbounded-order part remains open.

## 9. Cartier's target: a critical edition of one decisive construction

**Interest 5; one-run reach 5.** Anchors: SA03-823, SA03-824, SA03-825;
CL-SA03-837, CL-SA03-838, CL-SA03-839, CL-SA03-841; MP-SA03-140.

The cycle-valued formula is refuted and the cohomology-valued inverse Cartier
map is established. First compare the image of the notation on scans 170–171
with the published definition, preserving a separate layer for a p-basis
splitting. A short companion proof can then show exactly where additivity first
requires quotienting by exact forms. No new theorem is needed to make this
historically and mathematically useful.

## 10. Produce an exact November2026 results map for p-curvature

**Interest 5; one-run reach 4.** Origins: SA03-1028–1035; CL-SA03-1028–1035; MP-SA03-163–166. Source: K93-05, scans194–197.

The general conjecture, rank-one/solvable cases, rank2 on generic curves, whole Gauss–Manin systems, privileged systems, and selected subquotients must occupy separate rows. In particular, Lam–Litt’s nonabelian isomonodromy statements do not turn every connection into a solved case, and Esnault–Groechenig explicitly leaves arbitrary Gauss–Manin subquotients open while proving a distinguished-boundary case.

**What the task would establish:** a reusable theorem matrix with hypotheses, arithmetic quantifiers, finite-algebraic-monodromy conclusions, first circulation and publication dates. **First concrete step:** place Katz1972 Introduction, André Corollaries4.3.5–4.3.6, PSW Theorem1.1, Lam–Litt Theorem1.1.1/Conjecture1.1.2 and Esnault–Groechenig Theorems3.1/8.2 side by side. Keep all-closed-point vanishing and special whole-Gauss–Manin infinitely-many-prime results distinct. This is an exposition/history task, not a proposed proof of the general conjecture.

## 11. Normally-flat finite probes and essential positivity

**Interest 5; one-run reach 3.** Anchors: SA03-10, SA03-11, SA03-13, SA03-15;
CL-SA03-008, CL-SA03-011, CL-SA03-012, CL-SA03-013, CL-SA03-014;
MP-SA03-04, MP-SA03-05, MP-SA03-07, MP-SA03-08.

The correspondence certifies early circulation and modern algebraic-space
results supply important inputs. The stronger scheme, quasi-affine and
essential-ampleness quantifiers still need an exact match. Start from the 1963
and 1967 letters and Murre's cited route, keeping separation and the dependence
of jet order on a quasi-compact Hom family explicit. The bounded outcome is an
exact theorem identification or a sharply delimited proof gap.

## 12. Finite constructible maps versus absolutely flat envelopes

**Interest 5; one-run reach 4.** Anchors: SA03-249, SA03-250, SA03-252,
SA03-415, SA03-416, SA03-419; CL-SA03-237, CL-SA03-238, CL-SA03-425,
CL-SA03-426, CL-SA03-429; MP-SA03-38, MP-SA03-61, MP-SA03-62.

The common-partition obstruction is already established. The affine partition
ring A^cons in CL-SA03-426 is also already identified with Olivier's universal
absolutely flat A-algebra; that identification is not a remaining conjecture.
The outstanding comparison concerns the global immersive Ind category and
restricted full faithfulness in CL-SA03-425, together with the uniform
finite-partition condition in CL-SA03-237–238 and CL-SA03-429. First write those
objects and Hom sets with both index sets visible. The goal is an exact
comparison under stated finite-presentation or boundedness hypotheses, or a
diagram that isolates the categorical difference. No unproved exchange of
inverse limit and partition colimit should be built into the definition.

## 13. The stratification and Picard–Fuchs quotient

**Interest 5; one-run reach 4.** Anchors: SA03-811, SA03-812, SA03-813,
SA03-814, SA03-815, SA03-816; CL-SA03-820, CL-SA03-822, CL-SA03-823,
CL-SA03-824, CL-SA03-825, CL-SA03-826; MP-SA03-130, MP-SA03-131,
MP-SA03-132, MP-SA03-133, MP-SA03-134.

Formalization and the smooth characteristic-zero comparison are known. The
horizontal quotient, the weaker flat-differentials hypothesis and the operator
factorization require careful distinctions. Begin with a smooth affine chart
and a finite locally free coefficient module, writing the first two Spencer or
principal-parts maps. The deliverable should identify the exact comparison
that is valid before attempting to extend it to the source's weaker wording.

## 14. A derived formulation of Gauss–Manin

**Interest 5; one-run reach 3.** Anchors: SA03-818, SA03-819, SA03-820,
SA03-821, SA03-822; CL-SA03-827, CL-SA03-828, CL-SA03-829, CL-SA03-830,
CL-SA03-831, CL-SA03-832, CL-SA03-833; MP-SA03-135, MP-SA03-136,
MP-SA03-137, MP-SA03-138, MP-SA03-139.

The filtered de Rham construction and its ordinary cohomology connection have
exact sources. The first step is to choose the base-linear derived category
and the differential-operator or stratification structure that expresses
Leibniz. A short run can make the projection formula, coefficient-flatness
assumptions and secondary torsor class compatible in one diagram. It should
not call an ordinary O-linear map a connection.

## 15. Give the Euler programme a precise finite-core category

**Interest 4; one-run reach 4.** Sources: SA03-1212–1217; CL-SA03-1240–1255 and CL-SA03-1314; MP-SA03-190–194.

The formulas work on finite CW pairs and suitable compact cores with collared ends. West's Corollary 5.3 supplies finite polyhedral homotopy type for compact ANRs, which is weaker than triangulation and already sufficient for many Euler questions. The unqualified singular-cohomology closed-cover assertions, the recursively unstable `C/E` notation and the compact-support switches are the real obstacles to stating the whole programme cleanly.

**First concrete step:** define a category of locally compact metrizable spaces admitting a compact ANR core and a collared finite-type end link. Prove the ordinary and compact-support Euler formulas, including the local-coefficient rank formula and fibration multiplicativity, with an explicit excision hypothesis. Then ask whether the original conical category embeds in it. One run could deliver the core theorem and a list of precisely unresolved category-membership cases, without undertaking a triangulation programme.

## 16. Repair the global Picard obstruction diagram

**Interest 4; one-run reach 5.** Origins: SA03-1046–1050,1057–1065; CL-SA03-1046–1050,1057–1065; MP-SA03-172,175–177, with canonical MP-SA03-142–143. Sources: K93-05 scan206 and K93-06 scans207–217.

The Čech obstruction in H¹Ω¹, flat obstruction in H²(Ω≥1), p-curvature class in the additive cokernel ofγ, and nilpotent formal locus are compatible layers, but the written displays contain distinct issues: the full-H² low-degree row is overbroad, sequence(4.1) has the wrong kernel, and mixed p-nilpotent bases need PD/crystalline language. The checked abelian/universal-extension comparisons give a controlled setting for the repaired picture.

**What the task would establish:** a diagram of fppf sheaves and obstruction classes with exactness at precisely stated terms, plus a separate mixed-base formulation. **First concrete step:** construct the diagram in characteristicp for an abelian scheme using the cited Mazur–Messing propositions, and carry the dual-number nonzero-nilpotent example through it. Do not infer surjectivity where the manuscript displays no terminal zero.

## 17. Test the questioned Azumaya/principal-parts identification equivariantly

**Interest 4; one-run reach 5.** Sources: SA03-1241–1243; CL-SA03-1298–1303; MP-SA03-204–205.

The scan 86 equation `M ≃ f_*P¹(T_{P/X})` carries a question mark and an uncertain adverb. EGA IV, §16.7 and Proposition 16.8.4 verify what principal parts represent, but do not establish that particular pushforward identification. Rank agreement is insufficient. Scan 87 has a separate, definite rank discrepancy: the first neighborhood uses `I²`, not `I`.

**First concrete step:** compute `H⁰(P¹,P¹(T_{P¹}))` as a `PGL₂` or `SL₂` module over `Z`, tracking its extension class and comparison with `End(Z²)`. Reduce modulo two before making an equivariant-isomorphism assertion. A few hours should suffice to identify the correct additive/filtered statement or exhibit the precise obstruction. This task remains distinct from the already resolved normalized `P¹(ω)` identification at scans 91 and 135.

## 18. Resolve the arbitrary-base crystalline-site comparison

**Interest 4; one-run reach 2.** Sources: SA03-682; CL-SA03-1201 and CL-SA03-667; MP-SA03-107. Related, but distinct: MP-SA03-108.

The inherited programme uses an absolute nilpotent crystalline site without selecting a prime. The exact positive results checked in Messing impose `p` locally nilpotent and locally nilpotent divided powers. The vector-subgroup step and abelian filtration equivalence are not missing there: they are Messing III Proposition 2.7.7 and V Theorem 1.10. The remaining task is the literal comparison of sites and hypotheses, not reproving the p-nilpotent theorem or treating it as an unresolved historical conjecture.

**First concrete step:** write a two-column comparison of objects, morphisms and evaluations in the absolute site of the programme and Messing's site. Test the proposed equivalence on a base with mixed prime behavior and on a characteristic-zero nilpotent thickening. A short run should establish the largest verified common scope and identify the exact extra descent argument needed for the broader wording. Keep the universal-extension cocycle problem as a prerequisite link, not a duplicate of filtration effectivity.

## 19. Determine the exact statement behind generic restriction for bare crystals

**Interest 4; one-run reach 3.** Sources: SA03-1207; CL-SA03-1216–1218; MP-SA03-188–189.

The positive-characteristic extension theorem for BT homomorphisms has an identified later solution in de Jong. His F-crystal theorem is also a precise comparator for the suggested DVR reduction. The manuscript deliberately asks first about locally free crystals and then says “or at least” F-crystals. The two categories must remain separate. Lau's locally-p-basis equivalence for Dieudonné crystals does not answer the unstructured-crystal question by itself.

**First concrete step:** fix the exact crystalline site over `k[[t]]`, and express morphisms of locally free crystals as horizontal matrices over the appropriate PD envelope. Search for a horizontal morphism defined after inverting `t` that fails to extend, or prove a pole-removal lemma under a clear quasi-nilpotence hypothesis. A bounded run can produce either a decisive example or a precise reduction that explains why Frobenius is needed.

## 20. Recover the thickness diagram

**Interest 5; one-run reach 3.** Anchors: SA03-421;
CL-SA03-432, CL-SA03-433, CL-SA03-434, CL-SA03-435, CL-SA03-436,
CL-SA03-437, CL-SA03-438; MP-SA03-67, MP-SA03-68, MP-SA03-69.

Some genericity and noetherian implications are checked, but the missing system
and the ambient/intrinsic constructibility distinction affect the remaining
arrows. Inspect scans 126 and 128 first, then write every quantifier and the
actual Mittag–Leffler hypothesis. A recovered exact statement is a successful
outcome; proof of every recovered arrow is a subsequent task.

## 21. Bounded Greenberg data and finite-index maps

**Interest 5; one-run reach 3.** Anchors: SA03-423, SA03-424;
CL-SA03-441, CL-SA03-442, CL-SA03-443, CL-SA03-444, CL-SA03-445,
CL-SA03-446; MP-SA03-70, MP-SA03-71.

Greenberg approximation, the corrected modern point theorem and Sebag's
cylinder results supply specific comparators. Recover the definitions of
“simple”, “finite index” and the bounded invariant, then build a
hypothesis-by-hypothesis table. The goal is an exact identification or a precise
new statement, with residue fields, perfections, properness and separability
kept visible.

## 22. Reconstruct the relative duality and Picard-V scope ledger

**Interest 4; one-run reach 4.** Origins: SA03-1001–1007,1054–1056; CL-SA03-1001–1007,1054–1056; canonical MP-SA03-145 and MP-SA03-151–153,174. Sources: K93-03 scan178; K93-04 scans179–182; K93-06 scans210–211.

The text repeatedly reserves base change and asks for the widest Picard-V generality. Finite adjunction, the smooth top-form Cartier trace, the abelian Picard identification and the perfect-field vector hull are established. The exact transition to arbitrary relative dualizing modules, individual higher-direct-image bundles and all V-killed affine groups remains partly specified.

**What the task would establish:** a single theorem ledger stating which conclusions require smoothness, finite Frobenius, Cohen–Macaulay dualizing sheaves, perfect complexes, cohomology base change, abelian Picard representability or a perfect field. **First concrete step:** align the finite-duality unit/counit square with the relevant Mazur–Messing propositions, then give the relative Picard forgetful map directly before asking when it is Verschiebung. Preserve the completed178–179 residue hypotheses and the distinct finite-flat zero-locus theorem.

## 23. Relative components and the internal-Hom universal property

**Interest 4; one-run reach 5.** Anchors: SA03-45, SA03-49, SA03-50;
CL-SA03-043, CL-SA03-046, CL-SA03-047, CL-SA03-201, CL-SA03-202;
MP-SA03-23, MP-SA03-25.

The finite homogeneous criterion is checked, and the scan-59 continuation
fixes important assumptions. Write one relative component theorem, with the
correct finite étale test category and étale-local compatibility, then trace
the historical terminology. This would replace the false general finite-G-set
premise with a usable geometric statement.

## 24. Orientation axioms and the dimension-four deduction

**Interest 4; one-run reach 4.** Anchors: SA03-630, SA03-634, SA03-635;
CL-SA03-630, CL-SA03-631, CL-SA03-632, CL-SA03-633, CL-SA03-634,
CL-SA03-635, CL-SA03-636; MP-SA03-95.

The local boundary sign and later annulus input are known. Obtain Wanderley's
thesis or reconstruct the precise implication used by the offprint's theorem,
then compare its axioms with the six handwritten ones. The desired result is
a justified removal, or a precise remaining limitation, of the old cutoff
exception. Quinn's theorem alone is not the full categorical proof.

## 25. Universal-extension comparison and all-nil rigidity

**Interest 4; one-run reach 3.** Anchors: SA03-678, SA03-679, SA03-680,
SA03-681, SA03-682; CL-SA03-668, CL-SA03-669, CL-SA03-670;
MP-SA03-108, MP-SA03-109, MP-SA03-110.

Messing supplies the nilpotent-PD comparison and cocycle in its p-local scope;
the characteristic-zero D-group comparison is also available. First match the
historical absolute site to those statements and isolate the passage from
nilpotent to arbitrary nil thickenings. Recovering the old Tate letter would
settle provenance; a first-order vanishing calculation alone would not settle
the full assertion.

## 26. Turn the curve pairing into a corrected companion proposition

**Interest 4; one-run reach 5.** Origins: SA03-1008–1017; CL-SA03-1008–1017; MP-SA03-154–157. Source: K93-04, scans182–186.

Raynaud’s exact pairing supplies the published comparison. The consolidation has checked the nonzero index i+j=p, the determinant Δ=(−1)^((p+1)/2), the characteristic2 theta characteristic, and the distinction between the canonical Pfaffian and the basis-normalized isomorphism. The universal imperfect-field margin is false. A complete companion exposition can now be short, accurate and independent of the cancelled coordinate proof.

**What the task would establish:** a polished proposition and textual apparatus giving both source formulas and the mathematical refinements, followed by a carefully delimited higher-dimensional question. **First concrete step:** inspect scans183–185 for the index, determinant reversal sign and normalization word, then compare the two square-root maps explicitly. A higher-dimensional research task should begin only after deciding whether its object is an exact-form quotient, a determinant of a Cartier complex, or another construction; the manuscript does not select one uniquely.

## 27. A precise functor of nilpotent coordinate changes

**Interest 4; one-run reach 5.** Anchors: SA03-429, SA03-430, SA03-431,
SA03-432, SA03-433; CL-SA03-454, CL-SA03-455, CL-SA03-456, CL-SA03-457,
CL-SA03-458, CL-SA03-459, CL-SA03-460; MP-SA03-74.

The expansions, unit-Jacobian test and translation obstruction are checked.
Choose the test algebras and augmentation condition before writing the degree-2
group law. The result should distinguish evaluation bijections on a nilpotent
ideal from automorphisms of a quotient algebra and from torsors of lifts. This
finite-level definition and its law are realistic in one run.

## 28. Condition R, essential freeness and formal torsors

**Interest 4; one-run reach 3.** Anchors: SA03-55, SA03-56, SA03-57, SA03-58;
CL-SA03-049, CL-SA03-050, CL-SA03-052, CL-SA03-053, CL-SA03-056;
MP-SA03-26, MP-SA03-27, MP-SA03-28.

Murre and SGA 3 provide close but differently worded conditions. First compare
their exact quantifiers and determine whether group flatness was assumed before
the principal-action corollary. A hypothesis chart and one proved implication
would be useful; the broad nonnoetherian extension should remain a separate
task until both directions have been established.

## 29. Coherent envelopes and noncomplete bases

**Interest 4; one-run reach 3.** Anchors: SA03-25;
CL-SA03-022, CL-SA03-023; MP-SA03-12.

The complete-local module argument and the distinction from raw sheaf
intersection are understood. First decide the disputed completeness/coherence
wording on the image, then attempt faithful-flat completion descent with the
actual submodule condition. The intended outcome is either the exact descent
lemma or a counterexample with all hypotheses checked.

## 30. The proper Nagata example and Hom component finiteness

**Interest 4; one-run reach 3.** Anchors: SA03-12, SA03-18;
CL-SA03-018; MP-SA03-06, MP-SA03-10.

The affine-orbit obstruction is established and a modern Hom-component example
is located as a proof sketch. Identify the actual proper target and orbit in
the manuscript, then verify the special gluing in full. A nonseparated
doubled-line example does not answer the proper-target problem.

## 31. The quasi-compact-only pro-Hom wording

**Interest 4; one-run reach 4.** Anchors: SA03-253, SA03-428;
CL-SA03-453; MP-SA03-73.

The qcqs theorem is precisely known. Check the surrounding category's
conventions and the ink on scan 136 before constructing non-quasi-separated
examples. A source-convention verdict may settle the issue quickly; if a
counterexample is needed, every finiteness and transition hypothesis must be
verified.

## 32. Write one normalization chart for all analytic quotient constructions

**Interest 4; one-run reach 5.** Sources: SA03-640; SA03-1227–1237; CL-SA03-1262, CL-SA03-1270–1294; MP-SA03-198–201.

The calculations already determine the corrections: `G=−2S`, `G₀=G/12`; the exponential correction has coefficient one in the `G` scale; the logarithmic derivative ratio uses `f/g`; a horizontal frame has coefficient `−dlog f`; the Riccati map then matches the stated `c_n`. Some diagram arrows and dimension fragments remain undefined, so a corrected chart should include only the objects actually recovered.

**First concrete step:** build a single typed diagram of sheaves of local complex-analytic coordinates, nonzero forms, affine connections and projective connections, with every arrow's domain and torsor action written beside it. Include the scan 36 exponential calculation as a normalization anchor. This is an exposition and source-reconciliation task; it should not claim to settle the unnamed real-analytic arrows on scan 81 or the canonical transcendental construction at scan 135.

## 33. Recover the cancelled site drafts against their published counterpart

**Interest 4; one-run reach 4.** Origins: SA03-1018,1066–1067; CL-SA03-1018,1066–1067; MP-SA03-158. Sources: K93-04 scan187; K93-06 scans216,218.

Grothendieck’s1968 §5.1, pp335–336, supplies a unusually close counterpart: no final object, an identity-pair sheaf covering the final sheaf, and higher products ind-represented by infinitesimal diagonals. That comparison identifies the core construction without settling every uncertain category subscript or the cancelled torsor strengthening.

**What the task would establish:** a side-by-side correspondence between the drafts and the published categories, with only ink-supported identifications. **First concrete step:** inspect the three scans, mark global versus local cancellations, and transcribe the category symbols and arrow directions. The November–December1966 talks and1968 publication give comparison dates; they do not by themselves date the undated leaves.

## 34. Resolve the representation-category and finiteness conventions

**Interest 4; one-run reach 4.** Origins: SA03-1019–1027; CL-SA03-1019–1027; MP-SA03-159–162. Source: K93-04 scans189–192 and K93-05 scan193.

The pages distinguish, sometimes only implicitly, quasi-coherent Cartier descent, locally free bundles, algebraically locally trivial connections, stratifications and representations of enlarged or relative groups. The quasi-coherent counterexample and the Kummer criterion show that these are not interchangeable. Bhatt–Scholze’s Noohi group, its prodiscrete completion and the étale quotient offer useful comparisons, provided coefficient topology and rank are fixed.

**What the task would establish:** the exact largest category in which the source’s proposed field/relative representation equivalences hold, or a precise counterexample under its weak family hypotheses. **First concrete step:** write separate definitions for finite-rank discrete local systems, arbitrary-rank locally constant modules and arbitrary flat/stratified quasi-coherent modules; then compare the relative claim with SGA1X1.3–1.4 at its actual properness and separability hypotheses.

## 35. Turn the Zariski-openness and loop-space counterexamples into reusable companion lemmas

**Interest 3; one-run reach 5.** Sources: SA03-1205–1206 and SA03-1238; CL-SA03-1211 and CL-SA03-1284; MP-SA03-185 and MP-SA03-202.

Two small examples prevent broad misreadings. The slope-one-half graph-filtration family has weakly admissible parameters precisely outside `Q_p`, disproving the proposed Zariski openness in its stated setting. Separately, the reduced quadratic-module example gives a connected single loop space with nonzero first Postnikov invariant, while Baues–Conduché Theorem 5.8 gives the double-loop vanishing statement. These are already checked answers to the pages' questions; neither is a new research conjecture.

**First concrete step:** prepare a short proof appendix with every hypothesis, the historical comparator and the finite computation printed in one place. For the first, explain the difference between Zariski and analytic openness and the exact Breuil realization hypotheses. For the second, distinguish a vanishing invariant from a natural splitting. This would make the dossier usable without encouraging a later run to repeat either false inference.

## 36. The English analysis fragment's missing theorem

**Interest 3; one-run reach 4.** Anchors: SA03-636, SA03-637, SA03-638,
SA03-639; CL-SA03-637, CL-SA03-638, CL-SA03-639; MP-SA03-96.

The visible estimate is checked and Huff's title is a bibliographical candidate.
Obtain the full chapter or another exact textual match and compare its printed
pages 5–6, semigroup lemma and Proposition 1. The outcome is recovery of the
missing quantifiers, not an extension of an unidentified theorem.

## Prerequisites for external-project comparisons

The LM, Dérivateurs, S6, Hua, FLAGGED and other register leads are retained in
`SA03_project_leads.tsv`. They are not ranked as ready mathematical projects:
their destination texts and exact objects must first be obtained. Shared
vocabulary or a previously reported result status is insufficient evidence for
transporting a theorem from this dossier.
