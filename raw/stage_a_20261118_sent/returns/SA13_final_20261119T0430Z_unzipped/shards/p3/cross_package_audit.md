# P3 ↔ P4 semantic consolidation audit

19 November 2026. This is a proposed merge map for the parent assembler. It does not edit either source transcription or p4's shard. The review compared all 110 p3 item statements and 56 problems with all 106 currently saved p4 item statements and 41 problems. The central candidate passages were read in full on both supplied sides: 36:052 and 054–058; 36:004–008 and 073–084; 36:039–040 and 061–065; and the distinct Griffiths reference at 34:097–098. P4's later auxiliary additions outside this saved snapshot are not silently certified by this audit.

## Recommended object-level item consolidation

The following merges consolidate **one continuous object or repeated warning**, while keeping every distinct mathematical claim, hypothesis, counterexample and source verdict. They are not declarations that all claims under the merged item are equivalent. The parent should concatenate source lists and loci, and rewrite the combined statement in the indicated separate clauses.

| Old item | Canonical item | Source entries to preserve | Reason and mandatory distinctions |
|---|---|---|---|
| SA13-405 | SA13-324 | p4 #6; existing p3 #75–76 | Section c at 36:054 explicitly says “comme dans a)” and refers to the group-Hom vanishing of 36:052 a. One Ext-sheaf classification object continues from extensions to biextensions. Retain C-SA13-296, C-SA13-297 and C-SA13-405 separately: the first is the global/internal Ext edge isomorphism, the second is pointed-function rigidity, and the last is Biext=Hom(B,internal Ext¹). |
| SA13-407 | SA13-327 | p4 #8; existing p3 #78–79 | The one-variable forgetful functor at 36:052 continues to the two-variable forgetful functor at 36:054. Use a combined item “Rigidified torsors, extension laws and biextensions.” Preserve the primitive-class condition for extensions, additivity in both variables for biextensions, and the explicitly boxed special-case equivalence on 36:056. C-SA13-299 and C-SA13-407 remain distinct. |
| SA13-409 | SA13-329 | p4 #11–12; existing p3 #80 | At 36:056 the source says “Reprenons les not. … de la fin de b),” referring exactly to the NS defect diagram at 36:052. The same NS/Picard extension is then revisited on 36:058. Keep the formal injection C-SA13-300 and the conditional doubled splitting C-SA13-409 as separate claims. The unfinished final formula remains unfinished. |
| SA13-439 | SA13-322 | p4 #47–48; existing p3 #73–74 | Both occurrences warn that nonzero finite torsion pairings can disappear in the Tate limit. Preserve the p3 abstract bounded-torsion example and the p4 geometric finite-extension example as two different demonstrations of the same information-loss warning. Keep C-SA13-295 and C-SA13-439 separately, including the finite extension depending on the torsion level. |

The quadratic identity SA13-408 stays separate from SA13-329. It is a particular new theorem and a mathematically decisive sign alarm, not a repetition of the NS-defect construction. Likewise transpose/additivity SA13-406 stays separate from the classification item: it is an extra compatibility assertion, precisely the one matched to SGA7 VII2.9.6 in p4. The uncertain A/B letter SA13-330 also stays separate as a reading question.

These object merges imply four item aliases, not four erased mathematical assertions. There are no recommended claim-ID aliases in this p3↔p4 audit.

## Problems: one genuine continuation, several distinct obligations

**MP-SA13-92 → MP-SA13-134.** Consolidate the doubled Picard extension into the existing problem about primitive torsors and the generalized NS quotient. The combined problem must have a separate last clause: after defining the NS quotient and the symmetric birigidified defect, does the displayed diagonal lift split the Picard extension pulled back by 2, with the asserted canonicity over the intended base? Preserve p4's full occurrences on 36:056 and 058, its conditional homomorphic-lift hypothesis and its exact state-of-art limit. The primitive-torsor theorem is proved under rigidity; the unfinished canonical lift is still a distinct unresolved substep. This is a continuation of the same explicitly recalled NS extension, not a claim that proving the first settles the second.

**MP-SA13-133 retains its ID and gains 36:079–080.** P4 has no separate problem ID for its finite-versus-Tate warning. Once SA13-439 is aliased to SA13-322, add those p4 loci to MP-SA13-133 and preserve the K/K′ reading alarm. Its question asks when compatible finite pairings are faithfully recovered by the Tate modules. The finite extension that detects one torsion point need not carry an entire compatible tower.

The following should **not** receive problem aliases:

| Pair | Why both remain |
|---|---|
| MP-SA13-64 and MP-SA13-99 | The first contains the explicit Néron completion question and an editorial doubt about limits in draft2.6(a). The second asks for arithmetic orthogonality over the broad adic base. Add the 36:004 editorial occurrence to the proof-obligation discussion of MP99, but retain MP64's distinct completion/base-change question. The source does not show that the missing draft remark had exactly the later adic hypotheses. |
| MP-SA13-65 and MP-SA13-100 | The first has an unresolved generic/special torsion-kernel subscript and zero-dimensional-kernel question. The second is a concrete finite subgroup closure/lifting and specialization step. The formal identity K[n]=ker(G[n]→H[n]) does not prove the latter. |
| MP-SA13-63 and MP-SA13-103 | The early A.M.-versus-“yours” pairing question has absent formulas and uncertain initials. The later problem precisely compares the curve discriminant pairing with the Néron biextension obstruction and includes residue weights. The later heading makes Artin–Mazur plausible, but does not uniquely identify the early two maps. Link the questions; do not identify them without the missing draft. |
| MP-SA13-78 and MP-SA13-103 | Extension of an entire biextension from its torsion restrictions is a categorical criterion. Identifying a computed curve obstruction pairing is a geometric comparison. One can inform the other without being the same assertion. |
| MP-SA13-82 and MP-SA13-99 | Perfectness of a filtered pairing of dual 1-motives is distinct from vanishing on fixed and toric submodules of Néron Tate modules. Full annihilator equality needs additional rank or geometric information. |
| MP-SA13-84/85 and MP-SA13-93/95/96 | The p3 absolute torsor–Picard/Albanese formulas and singular extension questions do not coincide with p4's relative-trait invariant-cycle exact sequence, vertical divisor kernel, and Brauer inverse limit. |
| MP-SA13-141 and MP-SA13-232 | A36 concerns the Griffiths group and the primitive Leray injection. K34:097–098 attributes the complex-analytic monodromy exponent i+1 to Griffiths. The shared name is not an identity of results or bibliographic source. |
| MP-SA13-149 and MP-SA13-100 | Both use finite étale lifting, but A36 asks about the image of a special semilinear fixed representation at an arbitrary specialization; p4 concerns a torsion subgroup over a henselian pair. The nodal counterexample to A36's arbitrary-point version does not refute the valid henselian finite-part theorem used by p4. |

## Exact evidence at the rigidity boundary

On 36:052, part a assumes internal group-Hom vanishes. Part b separately assumes internal pointed-Hom vanishes; the margin explains that maps need not be additive and must respect unit sections. This distinction survives every base change and is the hypothesis behind the split torsor comparison and the normalized coherence proof.

On 36:054, c explicitly recalls a and uses internal group-Hom vanishing for the Biext–HomExt classification. Its next displayed function-Hom condition is uncertain. The preceding 36:052 b supplies a mathematically coherent **pointed/reduced-function interpretation** of that condition. This is stronger evidence than an isolated conjecture that all unpointed functions vanish, which would generally force the constant coefficient group to vanish. It remains a reading candidate: the scan, not the continuation, decides the written abbreviation. The corrected combined commentary should quote both places, preserve the uncertain fct/ens marks, and state the modern universal pointed-map hypothesis openly.

On 36:056 the box says that birigidified bitorsors on A×A are being assumed to be biextensions. Consequently the equivalence is a hypothesis at this stage, not a consequence of the word “birigidified.” The general primitive-image condition from 36:052 cannot be dropped. The diagonal identity then computes hΔ*j′=2 on the NS quotient. At 36:058 the text claims the resulting doubled extension splits and begins another formula, then stops. Each proof status must remain visible after the object-level merger.

## Exact evidence for finite versus Tate data

P3's 36:050 margin says the projective-system statement cannot be expressed by the Tate modules without stronger divisibility. The example P=Z/ell, Q=G=Qell/Zell has TP=0 and nonzero Biext¹(P,Q;G). It is an abstract algebraic example, with the finite data explicitly computed in p3.

P4's 36:079–080 starts from perfect finite Weil pairings. A nonzero toric torsion point has a dual detecting point over some finite extension K′. This does not provide a single finite extension containing all points in a division tower. The unpropagated final K label is a separate reading alarm. These are two occurrences of the same failure of recovering finite pairing information from a Tate-level vanishing statement, with genuinely different examples and hypotheses.

P4's bounded Brauer transition argument, C-SA13-420 / MP-SA13-96, remains a third **distinct assertion**. Uniform exponent only implies zero inverse limit when the transitions actually multiply by ell; identity transitions give a nonzero limit. P3's exactness of the 1-motive Tate sequence, C-SA13-264 / MP-SA13-80, uses surjective transitions and Mittag–Leffler. Sharing the words “inverse limit” is not grounds to merge these two proofs.

## IX2.6(a), weights and invariant cycles

The explicit reference “Rmq2.6 a)” on 36:004 is strong documentary evidence for linking the editorial doubt to the arithmetic-method comparison in p4 N97. P4's primary audit reports that printed IX2.6(a) distinguishes the arithmetic inclusion from the full orthogonal-complement theorem IX2.4 over a henselian trait. The early sentence asks whether S is a trait and whether Néron models commute with the relevant limit; it does not supply the criticized remark. The editorial concern should therefore be attached as a dependency or proof obligation, with the published comparison and draft scope recorded separately.

The semiabelian strictness/isogeny claim of 36:004 and the dual 1-motive graded pairing of 36:033 differ from the finite-field spectral-separation lemma at 36:075–076. The former concern the exact filtration and perfect pairings; the latter shows that an equivariant map must be zero because source and target Frobenius eigenvalues are separated. They are linked inputs, not duplicate results.

The Picard object is likewise used differently. P3's scans36:039–040 ask about H¹(X,A) and internal Ext into Picard sheaves; p4's36:061–065 concern a regular proper model over a trait, vertical divisors, inertia invariants and Brauer obstructions. The p3 real-field and nodal torsor diagnostics have no direct implication that p4's carefully qualified invariant-cycle sequence is false. P4's kernel R and component cokernel Ψ must also remain distinct from p3's generalized NS quotient of rigidified torsors.

## Other checked nonmerges

The reused Lie exponential/Levi material at p3 36:038 is not the BCH-in-a-restricted-family construction at p4 39:006. The Dirac-mass normalization on p3 36:006 is not the locally compact Haar/subgroup-limit theory reused at p4 36:066–072. P3's Čech comparison and p4's nearby-cycle spectral sequence have different functors and limits. The formal henselian-family questions in cote39 are not the Néron henselian-base questions. No item or problem alias is proposed for those thematic similarities.

## Assembly instructions

Apply only the four item aliases and one problem alias listed as recommendations. Repoint the affected entries without deleting any row. Preserve all 93 p3 source verdict rows and all p4 rows; the merged source rows become `merged` with a reason that names the original assertion and the new combined object. Retain the original stable IDs in an alias table and keep all distinct claim IDs. Add the new occurrences to MP-SA13-133, and add the IX2.6(a) editorial dependency to MP-SA13-99 without deleting MP-SA13-64. The accompanying `cross_package_merge_map.tsv` is the machine-readable proposal; the parent owns its final application.
