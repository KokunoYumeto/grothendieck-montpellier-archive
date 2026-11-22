# Parts B/C status at 2026-11-19 08:43 UTC

All results marked proved below have independent root audit recorded in CHECK_EVENTS.tsv.

## Part B
- B-RD1–3: explicit odd-prime counterexamples; explicit p=3 e=2 curve; ordinary full-p assertion proved.
- B-RD4–6: Lead B′ refuted by the logarithmic cyclotomic extension; height-one index is 0; all-prime finite-level character counterexamples.
- B-RD7–11: complete first-level elliptic ramification ranges, including wild defect 12 at p=3, and precise cyclotomic-field answer.
- B-RD12–13: exact all-level tame elliptic ranges and least forcing level for potentially good elliptics (all p>=5; tame defects at p=3).
- B-RD14–16: all-dimensional cyclotomic bound; literal unrestricted least forcing level is vacuous; explicit lower bounds for general-height character determination.
- B-RD17: an explicit finite universal upper bound for character determination exists for every prime and height, directly for the manuscript filtration condition; no potential semistability of the whole representation is assumed.
- B-RD18: formal Honda height-two constructions give nonzero lower bounds for every admissible absolute ramification and every height at least two, including p=2. Height one has sharp index zero for every prime. The quadratic p=2 full-character detour was rejected and is not asserted.
- B-RD19: additive reduction with full rational odd-prime torsion is necessarily potentially good, clarifying the two parts of the higher-level question.
- B-RD20: at p=3 the maximum primitive formal torsion valuation is divisible by 3 for a wild defect. This gives a sharper necessary higher-level wild range and the exact minimum absolute index 2*3^(2n-2) over all additive full-3^n examples. Independent parent and obstructions/crystals audits passed.
- B-RD21: the fixed-e p=3 largest additive full-torsion level is reduced to at most two adjacent integers, with an exact arithmetic characterization of the exceptional band. Its four full9 exceptions are resolved by B-RD23; B-RD26/27 now realize the upper endpoint in every exceptional band.
- B-RD22: at p=2,e=1 and every height at least2, even M[4] does not determine the odd-order inertia character. Explicit elliptic E versus split good BT group; both independent audits and exact finite certificate passed. Thus the least B4 index is at least2 in this smallest ramification case.

- B-RD23: complete full9 additive range at p3 is 6|e and e>=18. All examples occur over explicitly constructed finite local fields; the formerly unresolved e=24,30,42,48 examples all have defect12. Both independent audits and exact symbolic certificate passed.

- B-RD24: explicit finite Witt-coordinate algebraic decision test for the entire elliptic additive full-p^n existence question, with bounded minimality and exact Hensel lifting; parent proof/source audit and independent exact polynomial rerun passed. The test has not been evaluated at (3,216,3); the complete numerical range is instead proved independently by B-RD26/27.

- B-RD25: a ramification-nine base change of an e24 full9 additive example cannot yield full27; proof and exact certificate independently passed. This closes that construction route, not direct existence.
- B-RD26/27: every wild p3 bound is sharp, for all n and defects3,6,12. Exact trace invariant, regular weighted chart and faithful descent prove existence; the all-elliptic least potentially-good level is N_w+1. In particular e216/full27 exists. Parent complete proof/source/certificate audits passed.

- B-RD28: stronger p3 character lower bound N_w in every height>=2; parent audit passed.
- B-RD29: explicit B9 versus Tate9 comparison proves leastnu>=2 already p3,e2, and every e=2mod4; parent complete proof/source/code audit passed.

Remaining B gates: the optional potentially good dimension >1 least level; general-height B4 exact threshold (finite existence now proved); The corrected Fontaine dictionary is now primary-source-complete and audited; Lead B′ as stated remains false.

## Part C
- C-RD1: proper schematically dominant BT Hom descent proved; original non-noetherian rigidity overstatement corrected by C-RD2.
- C-RD3–5: exact p-nilpotent reduction criterion; nonreduced positive example and explicit mixed-characteristic dual-number negative example.
- C-RD6: normal noetherian extension theorem, without excellence.
- C-RD7–9: local-system effectivity on reduced geometrically unibranch bases, on reduced bases with local finite surjective geometrically unibranch covers, and invariance of effectivity for a specified local system under nilpotent reduction.
- C-RD10: explicit countable noetherian reduced infinite-node counterexample to unrestricted local-system effectivity; nonreduced counterexample by adjoining a square-zero variable. Thus C4 normal YES, arbitrary reduced NO, arbitrary NO; finite-cover hypothesis (a) gives YES.
- C-RD11: full C2 reduced assertion REFUTED, even for a reduced geometrically unibranch one-dimensional local domain satisfying (a),(b), ordinary elliptic generic fibre and split BT group. The obstruction is visible modulo 5. Normalization is not finite. All ring and finite algebra claims proved explicitly.

- C-RD12: exact relative essential-image criterion across a specified nilpotent thickening once a reduced realization is given, using the actual completed lift and its punctured overlap. Parent proof and primary-source audits passed.

- C-RD13: exact absolute essential-image criterion on every locally noetherian base via a closed-locus abelian seed, its canonical Serre--Tate tower, actual models on completions, actual BT-compatible punctured overlaps, and compatible quasi-affine atlases. Necessary and sufficient data do not quantify the original S-realization. Parent proof and original-source audits passed.
- C-RD14: elliptic specialization removes the formal-algebraization and atlas gates using the canonical degree-three line bundle and proper formal existence. Parent proof and original-source audits passed.

No remaining Part C gate. Automatic effectivity is not asserted: the exact criterion retains explicit completion and overlap conditions, and C2 is refuted even for a reduced geometrically unibranch base satisfying (a),(b).

## Manuscript documentation
F_BC_manuscript_quotes.tex records short French quotations for B1–B4 and C1–C4 with cote:scan and manuscript page references, explicitly checked against supplied transcriptions rather than fresh original scans.

C_absolute_image.tex supplies the audited C-RD13/C-RD14 criteria. Original EGAIII1 5.4.1/5.4.5 and Moret-Bailly1.1/1.2 were read by both this agent and the parent.

## Later B4 sharpening (19 November 2026, 09:58 UTC)

- B-RD30 PROVED: universal sufficient manuscript index2h² floor(log_p(peD/(p−1))) via original Bondarko A/B and audited B17 refinement.
- B-RD31 PROVED:2≤ν_min(3,2,2)≤4. At levels27 and81 every possible character mismatch must compare two whole potentially supersingular groups; filtered height-one comparisons are excluded at27 by the new rational-formal-torsion bound. Parent and OC complete independent proof audits passed.
- B-RD32 CANDIDATE: the81 test further reduces to inertia orders(12,3) or(12,6), joint image36; the27 test requires norm-one distinct tame quotient orders and joint image>9. Independent audits requested.
- The exact least B4 index in height≥2 remains open; no finite-elimination computation has been claimed to decide it.

- B-RD32 now PROVED: parent and obstructions-crystals full proof audits passed. The level-81 test reduces exactly to type12 versus3/6 with joint36; finite auxiliary certificate PASS0.050076540999725694s. Exact least index remains open.

- B-RD33 PROVED: parent and OC full proof/source audits passed exact graph H_r=ker(F^r)×ker(F^r), all successive alpha3² models, and generic-isomorphism/special-zero transition maps. No numerical improvement alone.
- B-RD34 CANDIDATE pending parent audit; OC full proof/source/code PASS: target supersingular-product logarithm recurrence yields level81 sufficiency, hence2≤nu_min(3,2,2)≤3; any27 failure has joint inertia18or36. Full proof and exact arithmetic certificate retained.

- B-RD34 PROMOTED PROVED: parent and OC complete independent proof and original-source audits passed. Exact current bound is2≤nu_min(3,2,2)≤3. The level81 case is settled; every possible level27 failure has joint faithful good inertia18or36. All three statement labels/log/source checks registered.

- B-RD35 CANDIDATE: all remaining27 BT pairs over the completed maximal-unramified base are exactly elliptic pairs; explicit integral quaternion conjugacy, equivariant ST and ample formal algebraization proved in draft. Exact full Tate lattice preserved. Independent proof audits pending; finite algebra certificate PASS.

- B-RD35 PROVED: exact elliptic realization (including labelled special inertia and full integral Tate lattice) passed parent+OC full proof/source/code audits. Remaining27 comparisons are equivalent to elliptic pairs after completed unramified base change.
- B-RD36 CANDIDATE: t=4/gcd(4,vDelta) and explicit six-coefficient e2 test with0<=delta<=23 and3v(c4)>delta; no finite elimination evaluated.

## 2026-11-19T11:29:14.625744+00:00 — B-RD36 promoted after three complete audits

Potentially supersingular elliptic tame special-inertia order is exactly `4/gcd(4,v(Delta))`. With B35, the remaining level-27 alternative over absolute ramification two is equivalent to a six-coefficient integral elliptic comparison over `W(k)[pi]/(pi^2-3)`, with `0<=v(Delta)<=23`, `3v(c4)>v(Delta)`, and distinct discriminant columns modulo four. Both root and OC passed the full proof, original-source and exact-code audit. No pair existence, no evaluated finite elimination, and no decision between least indices two and three is claimed.

## 2026-11-19T11:59:48.980466+00:00 — Corrected B37 candidate and original-source error caught

The first scalar-residual exclusion attempt was never promoted: visual Fisher4.3(11) shows an essential factor3 dropped by OCR. Its incorrect argument is retained under failed_candidates/. The corrected proof gives direct/symplectic9 character recovery for scalar residual representations and narrows any scalar opposite-character27 pair to reverse orientation, j-valuations {3,a>=6}, and joint36/type12-vs6 after a common quadratic twist. Scalar joint18 is excluded. This still leaves scalar reverse27, unipotent C3, and irreducible tame C4 residual forms unresolved. Root and OC independent audits are pending.

## 2026-11-19T12:10:33.048220+00:00 — B37 strong scalar exclusion repaired, candidate

The corrected reverse equations leave B/A and D/E valuation patterns, but exact unit calculations now exclude both: a required cube is congruent to one with deviation valuation one, while every such cube over e=2 has deviation at least three. The complete strong proposition is restored with this new proof, retaining the withdrawn original error. Thus candidate B37 excludes all scalar residual representations already at level nine and leaves only C3 or irreducible C4 after a common quadratic twist. Root and OC full audits requested. Exact certificate PASS in 0.0822893020012998 seconds.

## 2026-11-19T12:14:05.036883+00:00 — B37 promoted after complete root and monodromy audits

Every scalar residual potentially supersingular elliptic pair over e=2 with isomorphic nine-torsion has the same requested tame-order character, for both symplectic orientations. This uses the corrected Fisher factor3 and new unit obstructions, not the withdrawn proof. Consequently the only remaining level27 residual images, after a common quadratic twist, are nontrivial C3 and irreducible tame C4. Root and monodromy independently reread the exact original source and reran the entire certificate.

## 2026-11-19T12:22:24.015742+00:00 — B38 cyclic-four restriction candidate

The full draft proves v(j)=6 and discriminant valuation divisible6 for every residual C4 elliptic curve over e=2. It reduces that remaining level27 case to individual inertia3 and6, joint18; all joint36 candidates therefore have unipotent C3 residual image. Exact certificate passed in 0.07729700100026093 seconds and OC full proof/source/code audit passed. Root audit pending.

## 2026-11-19T12:23:04.809118+00:00 — B38 promoted

Complete root and OC proof/source/code audits passed. The C4 residual branch has v(j)=6, discriminant valuation divisible6, and can fail at level27 only with individual faithful special inertia3 and6 and joint18. Every joint36 candidate now has nontrivial unipotent C3 residual image after the common quadratic twist. Least index remains two or three.

## 2026-11-19T12:39:51.716582+00:00 — B39 promoted; B40 orientation candidate

B39 passed full root and OC proof/source/code audits. After common quadratic normalization, the remaining level27 alternatives are C4 with individual orders(3,6), joint18, j-values(6,6); or C3 with individual orders(12,6), joint36, j-values(3,b>=6), whose residual cubic extension is Kummer of a unit. Undoing the twist can interchange tame orders1/2. Neither row is decided for existence.

Candidate B40 excludes a direct/symplectic nine-congruence in the opposite-character C4 row, using an explicit marked Hesse Fourier differential calculation and a norm-unit contradiction. Full independent audits pending. Its first certificate failed on structural SymPy equality and is retained with its traceback; the exact difference test passes.

## 2026-11-19T12:45:29.397287+00:00 — B40 promoted; B41 elimination candidate

B40 passed full root and OC proof/source/code audits: the C4 opposite-character branch admits no symplectic nine-congruence, so every remaining level27 multiplier is minus one modulo3. Antisymplectic C4 remains open.

New B41 candidate uses the unique rational3 subgroup of a C3 representation and its explicit quotient isogeny: level27 descends to quotient9, but both quotientj valuations are at least6, contradicting every residual alternative allowed by B37–B39 for tame orders4 and2. This would eliminate C3/C6 completely, leaving only C4(3,6)/joint18/j(6,6). Exact certificate passed; root and OC full audits pending.

## B41 promoted after independent audits

Both the explicit normalized three-isogeny lemma and the C3/C6 exclusion proposition are proved and independently checked. Root full proof/code audit passed (0.12272746099915821 s, actual audit 12:48:32.703004 UTC); OC full proof/code audit passed (0.08641302699834341 s). Both preserved the author output. The remaining height-two p=3,e=2 level-27 gate is only the antisymplectic residual-C4 comparison, with individual special inertia orders 3/6, joint order 18, and both j-valuations 6. The least manuscript index remains 2 or 3.

## B42 candidate: exact small height-two index

A complete written proof and exact certificate now propose nu_min(3,2,2)=2. The remaining reverse C4 branch normalizes to M_b and the pi-twist of M_bprime, where M_b: y²=x³−3x+3b and b is a unit. The marked inverse Fourier sign, reverse theta=1 cube and explicit j/trace expansion force equal squared residues of b,bprime. Cardano and U3 cube surjectivity then identify their cubic good fields, making joint inertia at most6 rather than the required18. Root and OC full audits are pending; all three assertions remain Candidate. The author certificate passed in0.1415409550027107s after an explicitly retained structural-equality check failure was repaired by exact polynomial-zero comparison. No finite elimination was executed.

## B42 fully promoted: exact small B4 instance solved

After complete root and OC original-source/proof/code audits, all three B42 assertions are proved. The exact result is **nu_min(3,2,2)=2**: level27 always determines the requested prime-to3 inertia character for every permitted height2 group over e2; the earlier explicit level9 comparison proves sharpness. Root rerun0.11300166400178568s (actual13:08:46.182189UTC), OC rerun0.10002119700220646s; author output unchanged. The reverse marked cocycle and trace half-step are explicitly documented. Historical intermediate gates now point forward to B42. The general B4 least-index problem and higher-dimensional B3 remain open. No unexecuted finite elimination is being claimed. Owned promoted B files are frozen for CP14 after this update.

## New isolated B43 candidate: the dyadic level8 gate fails

The exact candidate B_p2_character_level3.tex constructs B[8] isomorphic to a Tate curve torsion over Q2(omega), e1, but with order3 special traces -1 versus2. The source curve has a rational point of order8 and minimal discriminant8; its quotient by that point gives the comparison. The exact parameter is q=-4lambda/3 and the full retained certificate passed0.5159330129972659s. Candidate only, independent audits pending. If proved this raises the dyadic lower bound to3, so the next question becomes16-torsion sufficiency. It is intentionally separate from the promoted/frozen CP14 B42 proof.

## B43 promoted: eight-torsion fails in the dyadic unramified case

Root and OC complete original-source/proof/code audits passed. B43 now proves **nu_min(2,e,h)>=3 for 3 not dividing e and h>=2**, including e1,h2. Exact reruns0.5299817019986222s (root actual13:29:59.102879UTC) and0.6142895730008604s (OC), author unchanged. The next small dyadic question is16-torsion sufficiency, not8. No upper or exact dyadic index is claimed by this counterexample.

## 2026-11-19T13:46:59.009493+00:00 — dyadic sixteen mixed gate and uniform A4 audits

B44 is a complete candidate, not promoted: integral conjugacy of all finite height-two dyadic inertia into the supersingular elliptic automorphisms, exact elliptic BT realization, no rational sixteen-point at e=1, and exclusion of the mixed comparison at sixteen. Both remaining objects would be potentially supersingular elliptic curves, with one finite inertia order in {1,2,4,8}, the other in {3,6,24}; joint degree belongs to {3,6,12,24,48,96,192}. No remaining pair existence or nonexistence is asserted. Exact certificate passed in0.07470255399675807s.

Full independent audit PASS for the uniform tangent-triple proof and both OC dependencies, with isolated outputs retained; full all-odd group assembly audit PASS, including actual original Kantor–Seress3.6 page22 view.

## 2026-11-19T13:54:14.218659+00:00 — B45 candidate, B44 second audit, CP15 QA

OC completed B44 proof/source/code audit PASS0.06939755400526337s; root audit is pending and all four statements remain Candidate. B45 is a new complete candidate, deriving exact special graph and dyadic logarithm recurrence, hence3<=nu_min(2,1,2)<=7 and a decreasing necessary-condition list of joint inertia degrees at16/32/64/128/256. No remaining pair has been decided. The initial a=3 crossing exception was caught before promotion and the exact original draft is retained; all displayed table entries were unchanged. CertificatePASS0.0776823170017451s.

Full root mixed(6,3) seed/OC axis norm audits PASS; author outputs preserved in both reruns. CP15 actual visual QA PASS on all assigned8pages.

## 2026-11-19T14:07:21.160750+00:00 — B44 promoted and B45 second audit

All four B44 assertions are proved after root and OC full original-source/proof/code audits and CP15 release. B45 remains Candidate despite the OC full pass, pending root Cartier/source audit. The all-even supersingular monodromy closure and its first-image sheaf received a complete independent mathematical PASS; no new program run was claimed. A new B46 proof is being written to exclude trivial residual inertia from the remaining dyadic comparison.

## 2026-11-19T14:09:48.940043+00:00 — B46 strict residual-branch candidate

The complete B46 proof and exact certificate exclude trivial residual inertia from every hypothetical dyadic e1,height2 sixteen-torsion ambiguity. In fact the potentially supersingular full-rational2 case is already distinguished by4-torsion. Only common residualC2 orC3 remains. All assertions are Candidate pending full independent audits. The initial written differential-scaling sign was caught in self-review, corrected, and retained; the finite certificate passed0.12948673400387634s. Chen mod8 models were opened as a research lead but are not used in this proof.

## 2026-11-19T14:14:39.431762+00:00 — B47 residual order-two candidate

A complete B47 proof now excludes common residualC2 inertia already at8 for two potentially supersingular elliptic curves. The universal2-isogeny quotient and its2-torsion field expose the two Kummer valuation parities; the exact table determines the cubic special inertia. Together with B44/B46, this would leave only residualC3 at16. All B47 statements are Candidate pending independent audits; certificatePASS0.20210709299863083s. B45 lemma now explicitly specifies complete mixed-characteristic(0,2) field as requested by root.

## 2026-11-19T14:15:56.817896+00:00 — B45 promoted

Root and OC full proof/original-source/code audits now prove3<=nu_min(2,1,2)<=7 and the shrinking list of possible joint inertia degrees. No least dyadic index is asserted. Root rerun0.23222537100082263s, OC0.05902020299981814s, author preserved. B46/B47 remain Candidate while the complete independent audits finish; their field statements now explicitly give complete mixed-characteristic(0,2).

## 2026-11-19T14:24:37.094325+00:00 — B46 promoted and mixed thin systems audited

Root and OC complete audits now prove B46. The remaining dyadic sixteen comparison has nontrivial residual inertia. B47 is awaiting the final companion code audit. The entire new mixed thin-system residue proof and all four conclusions received an independent proof/source/code PASS, with retained isolated output0.19381124299980002s.

## 2026-11-19T14:29:13.082462+00:00 — B47 promoted; B48 exact dyadic candidate

B47 is proved after root and monodromy full audits. Only common residualC3 remains for a hypothetical dyadic16 ambiguity. B48 now provides a complete candidate exclusion at8 using original Chen marked models, and would prove the exact least index nu_min(2,1,2)=3 together with B43/B44. The same-parameter universal discriminant identity passes exactly; the printed cusp-sum sign discrepancy is explicitly retained and resolved by the main models/Appendix computation. All B48 labels remain Candidate pending root and OC full source/proof/code audits.

## 2026-11-19T14:37:47.689437+00:00 — B48 closed; positive-index audit

B48 all three assertions promoted after complete root and OC proof/source/code audits. The exact least manuscript index is nu_min(2,1,2)=3: sixteen torsion suffices for every allowed height-two group at e=1, while B43 eight-torsion fails. Whole potentially supersingular elliptic pairs already satisfy eight-torsion character recovery. General B4 remains open. Earlier B45–B47 scopes retained with forward references. Chen sign discrepancy remains explicitly documented and exact Appendix identity uses the fixed main-model coordinate.

OC positive ordinary-index bounds: complete independent PASS for all four labels, including original AV and actually viewed Crew sources. No experiment executed or claimed for this audit.

## 2026-11-19T14:40:17.350393+00:00 — generic mixed all-degree monodromy audit

Complete independent proof/code PASS for monodromy generic_mixed_product_all_groups_candidate.tex. Read all six proofs and exact Cartier/covector, group-test, block and even-boundary dependencies. Verified normality of geometric generic coefficient-fibre image in total arithmetic image by generic localization of integral finite-etale covers; consequently both arithmetic coefficient witnesses can be used with the geometric GL8 block. Both translation-module arguments and final normal-subgroup commutator step rederived. Exact independent coefficient verifier reran PASS0.3759362999990117s with author hash preserved. No new primary-source reread claimed beyond the already audited dependencies. Scope remains transcendental ordinary j, not every algebraic ordinary modulus.

## 2026-11-19T14:58:24.394151+00:00 — generic nonordinary ppav audit and CP16 QA

Complete independent proof/source PASS for the post-CP16 monodromy assembly. The family lemma now explicitly assumes a reduced locally Noetherian base, and the open conjugacy conclusion keeps its fixed-subgroup upper bound. Original EvdG Example12.2 p624 was actually viewed: its all-four degree-one sentence contradicts the ordinary factor p+1 on the same page and p623 table. Only the two middle strata are needed; Example3.4 p589 makes their canonical rank sets complete, and Proposition4.5/Lemma4.6/Corollary8.4 give degree one. This discrepancy is recorded, not silently corrected. Full frame specialization, normal flag-curve specialization, all-degree generic groups and finite-degree open consequences all pass. No finite experiment is applicable.

CP16 assigned final pages322,323,324,325,326,327,328,329,330,334,402 were actually viewed in montages10--12 and all passed layout QA before archive freeze.

## 2026-11-19T15:14:32.903964+00:00 — B49 promoted; tame height-two range narrowed

Complete root and OC proof/source/code audits prove 1<=nu_min(p,p−1,2)<=2 for every p>=5 under the prompt cyclotomic hypothesis. The mixed formal/height-one-filtered case is excluded already at p² by the exact valuation equation a=p[b+(p−1)A], contradicting tame absolute index. Any remaining p² ambiguity is between two whole potentially supersingular groups with equal finite determinants and joint tame degree m dividing p²−1 with m>p. General exact least index remains open. Original Hopkins–Gross indexed text was read; direct download/screenshot failures are recorded without a visual claim. Five source-independent truncated-logarithm reconstructions and all finite arithmetic checks passed; author output retained.

The OC toral-image candidate also received a complete independent proof/source PASS: actual μ2 descent, reflexive lattice, moving-frame variation, restricted first=stable corank2 at a sharp étale-double pullback, and trace factorization. Final quadratic determinant nonvanishing remains explicitly open.

## Post-CP17 update, 2026-11-19 15:39:53 UTC

B50 is promoted after full root and OC proof/source/code audits. Its closed coefficientwise logarithm boundary includes a=p²−1 and excludes any p²-character ambiguity with square common finite determinant. After a common finite twist, only primitive nonsquare norm remains, with m=(p²−1)/d for odd d|p+1. No remaining pair is constructed and the least-index interval remains {1,2}.

B51 is a separate candidate: primitive norm fibres have q/2 Frobenius orbits, q=(p+1)/d, so q=2 cannot support distinct characters. In particular p5 leaves only m24, with two possible finite-type patterns modulo simultaneous quadratic twist. Exact arithmetic passed; companion and root audits are being completed.

Complete independent audit of the fixed-ordinary-modulus mixed-product degree-one GL8 theorem passed, including full root inertia, rank-two exceptional incidence bound, Lang-cover transitivity and elementary-matrix assembly. Retained independent outputs are in this directory. CP17 pages243,244,245,246,247,343,344,345 were actually viewed individually and passed visual QA.

Research lead: Daniel Le (2019), Theorem3.6, gives mod-p² transversality for generic tame potentially Barsotti--Tate types over an unramified base. The e=p−1 ramified base and possible nongeneric residual cases here are not covered; no unsupported transfer is made.

## B51 promoted after full audits, 2026-11-19 15:42 UTC

Both finite-character assertions and their scope remark are proved. In normalized primitive norm, m=(p−1)q with q|p+1, v2(q)=v2(p+1), and q≥4. At p5 this leaves only m24, with three individual types A={1,5}, B={9,21}, C={13,17} in μ24 and two pair patterns up to a common quadratic twist: {A,B} and {A,C}. This remains a necessary finite-character classification; neither pattern is claimed to occur for groups with isomorphic25-torsion. General least index remains one of1,2.

## 2026-11-19 16:05:59 UTC: companion bundle audit
Full independent proof/source PASS for the three lemmas and scope remark in OC post_CP17_positive_index_bundle_notes.tex. Original AV7.19 complete proof p105 read. The retained local unit u is necessary and the quotient columns (1,0),(u f²,w) are correct; the cokernel is a line on the possibly nonreduced Cartier curve. No residue nonvanishing is inferred.

## 2026-11-19 16:10:39 UTC: B52 candidate
B_tame_CM_gate.tex contains three complete candidate assertions: nonsquare finite determinant forces unramified quadratic finite-extension endomorphisms and maximal integral CM lattice; the CM good model is canonically Lubin–Tate with full first wild layer; p² recovers special character in the two-potential-CM supersingular subclass, with exact restricted index1 via an explicit p-level lower pair. The unrestricted B49/B51 ambiguity is not settled. Separate B52_references.bib avoids mutating CP18 frozen bibliography. Exact author certificate PASS0.2904240139978356s; first unexpanded-SymPy structural equality failure retained with source/output. Root/OC audits pending.

## 2026-11-19 16:21:36 UTC: CP18 and strip audit
Actually viewed final QA18 pages70,354–358 individually. All PASS. An initial duplicate-equation-tag report on357 was a visual misread; reopened actual image and canonical source confirm distinct tags1,2,3,4, and the report was withdrawn before archive. Full independent mathematical proof audit of all four strip propositions/theorem and scope passed. No finite graph program was yet received; the complete finite-Lang proof was reread and prior original Kantor–Seress source audit reused.

## 2026-11-19 16:25:39 UTC: strip full audit and B52 clarifications
Strip independent exact supplement PASS0.03244920699944487s; author hash preserved, retained own output. B52 now explicitly invokes Tate before reducing finite-extension endomorphisms, cites freshly read HG4.2, derives the tame uniformizer choice, and records the dossier covariant finite-exponent convention. OC complete B52 proof/source/code audit PASS0.3663983289952739s received; root final audit pending, so all claims remain Candidate.

## 2026-11-19 16:30:06 UTC: B52 promoted
Three CM assertions and exact scope are now proved after complete root and OC proof/source/code audits. Exact restricted index is1 at p≥5,e=p−1,μp, when both models are potentially CM and potentially supersingular. Hence remaining full B4 ambiguity needs at least one non-CM model. Root runtime0.33256562399765244s, OC0.3663983289952739s, finalauthor0.3032921849953709s. Opened LT bibliography merged into main bib, HG4.2 and action passages added to note. No unrestricted least-index conclusion.

## 2026-11-19 16:35:05 UTC: residual-cycle candidate
B53 is written separately in B_tame_residual_cycle.tex. In the normalized nonsquare-det comparison, Fp-irreducible residual inertia gives equal p-point valuations and r=c+p−1; different special types then force joint good orderp²−1 and adjacent vertices on a cycle of length(p+1)/2. At p≡3mod4,p≥7 quadratic-opposite pairs must be residually reducible. At p5 the triangle removes neither remaining abstract pattern. Exact finite authorPASS0.04175966899492778s;9495 pairs/740 valuation cases; independent audits pending.

## 2026-11-19 16:37:19 UTC: companion pencil audit
Full independent local proof PASS for both lemmas and scope in OC post_CP18_positive_index_pencil_candidate.tex. All nonreduced Cartier, norm-factor and logarithmic differential assertions rederived. Compatible determinant/pairing normalizations retained. No variation identification or nonvanishing conclusion. No new computation needed.

## 2026-11-19T16:45:57.648476+00:00 — additional pencil assertions

Full independent proof PASS for the contraction/cup-product lemma and exact etale-pullback first-rank corollary. No variation nonvanishing inferred. Entire appended proofs and prior toral double-corank proof read; finite-flat adjunction and Q filtration prove Ext acyclicity; dual surface sequence gives E0|D tensor R0; exact Cartier contraction; H1 zero; local norm boundary beta cup; sharpness equivalence; etale trace gives exact kernel2+nullity and first rank2b-2-nullity. No finite computation or determinant nonvanishing claimed.

## 2026-11-19T16:50:11.040989+00:00 — B53 promoted

Full root and OC proof/code audits passed. Canonical file B_tame_residual_cycle.tex. This restricts irreducible-residual different-character pairs to maximal joint degree and adjacent vertices of an explicit cycle; p5 remains unrestricted by this gate. Runtimes: author0.04175966899492778s, root0.04199664699990535s, OC0.047423224001249764s.

## 2026-11-19T16:57:03.474763+00:00 — degree-three full audit and CP19 QA

Full proof rederived after chord-separability and dense nonhorizontal-contact clarifications; all exceptional jet counts, characteristic2 transposition, constrained-sum H0^18, pure gluing shear, actual GL26, S54 submodules, common54/53/30 graph kernels and distinct diagonals, irreducible transvection closureGL80. Entire root graph code read; isolated author-preserving PASS0.06837776099564508s;729 cases;SHA632f6e03547f5a040ad1f78ec01780d1d32597d43f9e250d7ae5aef47195ce92 unchanged. Prior original Kantor-Seressp22 and strip proof audit reused, no new source read claimed.

Actually viewed final pages70,367,368,369,370,371,372 individually; all layout PASS.

## 2026-11-19T17:00:26.571903+00:00 — B54 promoted

B_tame_CM_neighborhood.tex: full root and OC original-source/proof passes. For p^n, v(u)>2n e_L gives the canonical-CM finite torsion with full descent. Any different-character p² pair has at least one nonzero normalized parameter at most4e_L. No least-index resolution or numerical experiment claimed. Prepromotion text preserved.

## 2026-11-19T17:15:58.156139+00:00 — all-odd full audit and final CP19 QA

Entire universal proof rederived: arbitrary odd translation chord sextics/separability, disjoint shifted branch sets, multi-type contact/singular/triple incidence including one-overlap case, full product symmetric nodes, constrained-sum labelled-cover independence, actual type-specific pure shears, anchored-loop heart span and Hom(K,F2)=0 diagonal argument, dimension dichotomy and GL closure. Exact graph code read; read-only author-preserving PASS0.04048306200274965s at17:14:26.364789UTC,9 cases inclC3²;source and full observed result retained after CP19 release;previous strip/H1/Kantor-Seress original-source audit reused.

Final CP19 pages372--380 actually viewed individually and all layout PASS; final addendum453pages.

## 2026-11-19T17:19:00.797335+00:00 — B55 candidate

Full proof written in B_tame_minimal_wild_layer.tex. Minimal possible wild order p² is proposed to force equal characters for Fp-irreducible residual inertia. No promotion before independent full audits.

## 2026-11-19T17:32:54.634453+00:00 — B55 promoted

All three B55 statements are proved after full root and OC audits. The minimal wild second-level order p² cannot hide different special tame characters when the common residual representation is irreducible over Fp. At p=5 this removes wild order25; orders125/625 and reducible residual representations remain open. Complete author/root/OC runtimes are retained in the theorem and audit register. The finite certificate separately checks75984 field elements and75984 scalar candidates; the earlier compact log wording did not distinguish these two equal counts. The coefficient-ring and p-map orientation explanations are explicit. Prepromotion candidate preserved.

## 2026-11-19T17:45:30.273305+00:00 — B56 candidate

The full separate draft excludes wild order p³ for distinct tame special characters with irreducible residual projective order greater than2. This would remove wild125 from the p5 A/B pattern, leaving only625 there. The proof avoids identifying any lower and upper ramification break; the corrected outline is explicit. No promotion before complete independent audits.

## 2026-11-19T18:00:38.595824+00:00 — B56 promoted

Full root and companion audits passed the strengthened proof. At irreducible residual projective order>2, any different-type p² comparison now requires wild orderp⁴. At projective order2, a whole anti-Cartan plane with one break is also excluded. Thus atp5 the A/B pattern requires625; A/C still has125or625 at this theorem’s stated scope. The separate B57 two-break/exhaustion argument is not yet claimed. All candidate versions, exact runtimes and the rejected lower/upper shortcut are retained.

## 2026-11-19T18:03:58.661256+00:00 — B57 complete candidate

The full five-statement proof now exhausts every wildp³ image in an irreducible-residual different-character p² comparison. Full anti planes automatically have one break; the residual-order-two Cartan-plane-plus-anti-line shape has one higher Cartan break, where the same Frobenius/scalar contradiction applies. Thus the candidate leaves only the full wild matrix space of orderp⁴, including625 in bothp5 patterns. This is not yet promoted. Complete exact arithmetic supplement passed0.19211209900095128s, with original source/output preserved; root and OC full audits requested.

## 2026-11-19T18:11:01.424326+00:00 — B57 promoted

The complete five-statement proof now excludes every cubic wild image in an irreducible-residual different-character p² comparison. Full root and OC proof/source/code audits passed, including the same-coordinate first-term comparisons and the Cartan c=b0 edge. Both p5 patterns therefore require the full625 wild matrix space. The full p4 layer and reducible residual representations remain open; the exact least-index interval is unchanged. Exact candidate, all program versions and outputs, actual runtimes and promotion record are retained.

## 2026-11-19T18:24:01.590161+00:00 — B58 complete candidate

A full upper-ramification argument identifies the last group of a remaining p4 division extension as the Cartan plane. With irreducible residual projective order>2, the preceding anti-plane has scalar-Fq leading coefficients; the three monomial classes then force the same scalar/Frobenius contradiction on the final Cartan plane. The proposed result leaves only projective order2 (the opposite quadratic pair at p=1 mod4), plus reducible residual representations. Atp5 it would eliminate A/B in the irreducible case, leaving A/C625. Full proof, primary-source fragment, downloaded originals and exact certificate are retained. Candidate only until complete independent audits.

## 2026-11-19T18:36:45.374150+00:00 — B58 promoted

Complete root and OC proof/source/code audits passed. Upper-ramification quotient compatibility forces the final wild group to be the full Cartan plane; residual projective order greater than2 is excluded. Atp5 only the opposite quadratic irreducible pair and reducible residual case remain at this theorem scope. B59 is separately under code audit. Exact prepromotion candidate and all author/audit outputs retained. Serre1961 and Colmez original-source bibliography entries merged.

## 2026-11-19T18:39:05.725039+00:00 — B59 promoted; irreducible residual branch closed

Both possible anti-Cartan break patterns are now excluded, completing character recovery from p²-torsion for every Fp-irreducible residual comparison under the normalized p>=5,e=p-1 hypotheses. Root and OC full proof/code audits passed. The only remaining normalized potentially supersingular different-type comparisons have reducible residual inertia. At(5,4,2) the unrestricted least-index interval is still{1,2}; no reducible-residual pair or exclusion is asserted. All exact candidate and finite-test history retained.

## 2026-11-19T19:05:48.148380+00:00 — B60/B61 complete candidate

Full Newton filtration, canonical-line tame character and actual elementary-abelian second-level point-field proof now propose recovery in every reducible residual case. Combined with B59 and prior reductions this gives the candidate equality nu_min(p,p-1,2)=1 for allp>=5. Not promoted until full independent audits. Exact finite supplement and exploratory20-row p5 history retained; no theorem inferred from those finite rows.

## 2026-11-19T19:09:57.356647+00:00 — B60/B61 promoted: minimal cyclotomic height-two case closed

Full root and OC proof/source/code audits passed all eight statements. The Newton high-line filtration and exact point-field lower-break comparison exclude every reducible residual different-character p² comparison. Together with B59 and prior reductions, the exact least index is nu_min(p,p-1,2)=1 for every primep>=5 (mu_p inK, e=p-1, height2, perfect residue and manuscript monodromy condition). In particular the prior p5 interval{1,2} is now closed at1. The unrestricted B4 problem for other ramification/heights remains open. Exact audited candidates, exploratory history and all numerical outputs retained.

## B62 promotion 2026-11-19T19:44:52.764033+00:00
All five labels in `B_tame_cyclic_level_counterexamples.tex` are proved after full root+OC proof/source/code audits. At e=2(p−1), height≥2 has ν_min≥2; the general stated interval supplies ν_min≥n. Only the comparison M is asserted wholly potentially good; H has a two-step good filtration. No next exact index is claimed. Exact candidate and all outputs retained.

## 2026-11-19T20:02:18.156179+00:00 — powers-of-three A4 induction promoted

All six assertions in A_nonordinary_powers_three.tex are proved after complete root and monodromy audits. Every fixed nonordinary principally polarized surface has geometric and arithmetic GL_(9d²−1) in all degrees d=3^j. The uniform norm step uses general H1, composition-factor order separation, all four node products, many-theta graph hearts and actual finite-Lang torsor extension. No other nonproduct degree is inferred here. Exact candidates, finite-scope program, outputs and all runtimes retained.

## 2026-11-19T20:13:31.778075+00:00 — B63 promoted

All five assertions in B_cyclic_torsion_threshold.tex passed full root and OC proof/source/code audits. Rational cyclic orderp^n on a good height2 formal group with p∤a forcesa>(p²−1)p^(2n−3). This gives exact existence thresholde>p^(2n−3) for the whole-supersingular versus filtered-height1 comparison whenp∤e. The generalizedx^A arc supplies examples at every admissiblee above threshold, removing B62uppercutoff. No unrestricted character-recovery bound is inferred.

## 2026-11-19T20:21:37.657032+00:00 — B64 promoted

All four assertions in B_tame_quotient_weight_gate.tex passed full root and OC proof/source/code audits. The actual quotient target has degree-p coefficients of valuation at least p-1 by its tame cotangent weights. The closed-boundary Cartier estimate yields exact nu_min(p,2(p-1),2)=2 for every p>=5 in the full B4 monodromy setting. Both the lower example and the full mixed/filtered/formal upper reduction are proved. Other ramification and heights retain their separate open scope. Exact prepromotion source and every output are preserved.

## 2026-11-19T20:36:01.147182+00:00 — B65 promoted

All six assertions in B_p5_e12_high_quotient.tex are proved after full root+OC proof/source/code audits. The exact full-monodromy height2 index is nu_min(5,12,2)=2. Canonical high quotients transform B to5B or72−B, and exact125-to25 comparisons eliminate the remaining wild case; the tame exception and square finite determinant are also proved. The next p5,e16 case remains separate. Every executed program, unchanged author output and exact candidate is retained.

## 2026-11-19T20:55:13.853287+00:00 — B66 promoted

All five assertions in B_middle_tame_quotient.tex are proved after complete root and OC proof/source/code audits. The exact full-monodromy height-two index is nu_min(p,(p²−1)/2,2)=2 for every p>=5. The integral high/low quotient argument and common point-field comparisons are explicit; no finite prime sample proves the theorem. The wider initial tame sector and arbitrary-index irreducible lemma remain separate B67/B68 candidates. Exact audited source, all outputs and actual runtimes are preserved.

## 2026-11-19T20:58:15.369268+00:00 — B67/B68 complete candidates

B67 fully rewrites the irreducible-residual p² ramification proof for arbitrary p∤e with μp. B68 combines it with actual high and low cyclic quotients to propose exact ν_min(p,t(p−1),2)=2 for 2≤t≤p−1, including p5/e16. Both complete proofs and exact finite supplements are retained; neither is promoted before complete independent audits. The full filtered monodromy reduction and sharp lower examples are explicit in B68.

## 2026-11-19T21:17:34.323812+00:00 — B67 promoted

All six assertions in B_tame_irreducible_arbitrary_index.tex are proved after complete root and OC proof/source/code audits. The irreducible-residual actual p² comparison is now settled for every p>=5 and every p-prime absolute ramification with μp. All wild image sizes are handled in the same actual division field, with exact arbitrary-e break normalizations and the full additive root polynomial. Reducible residual and p-divisible ramification remain outside this theorem. Exact candidate, finite programs and all runtimes retained.

## 2026-11-19T21:18:30.387655+00:00 — B68 promoted: initial tame sector exact

All six assertions in B_initial_tame_sector.tex are proved after complete root and OC proof/source/code audits. The exact full-monodromy height-two index is nu_min(p,t(p−1),2)=2 for every p>=5 and 2≤t≤p−1, including p5/e16. B67 supplies the arbitrary-e irreducible branch; actual high/low cyclic quotients close the reducible branch; square determinants use the actual-target Cartier bound. The next p5 indices e20 (wild absolute index) and e24 (prime-to-p boundary) remain separate. Exact candidates, field-typing corrections and all numerical outputs/runtimes are retained.

## 2026-11-19T21:37:16.713937+00:00 — B69 promoted: first tame boundary exact

All six assertions in B_one_slope_quotient.tex are proved after full root and OC audits. The exact full-monodromy index is nu_min(p,p^2−1,2)=2 for every p≥5, including p5/e24. The proof handles actual one-slope stable-line quotients and removes the determinant normalization from the two-slope comparison below p^2. The p5/e20 wild absolute index remains open; the next p5/e28 prime-to-p boundary is a separate unpromoted lead. The exact candidate, source-read scope, full certificate and all independent preserved-output runs are retained. Promotion followed CP25 archival release and does not modify that immutable checkpoint.

## 2026-11-19T21:43:57.741450+00:00 — B70 promoted: next tame boundary exact

All six assertions in B_next_tame_boundary.tex are proved after full root and OC audits. The exact full-monodromy index is nu_min(p,(p+2)(p−1),2)=2 for every p≥5, including p5/e28. The small {1,p} parameter collision preserves the special character by Frobenius conjugation; the new tame B=p² case is settled by actual residual eigenvalues. The p5/e20 wild absolute index and next prime-to-p index p5/e32 remain open. The retained {2,p+1} arithmetic pattern is not an existence assertion. All exact candidates, code drafts and outputs/runtimes are retained.

## 2026-11-19T22:04:11.793276+00:00 — B71 promoted: scalar-safe marked-quotient sector

All seven assertions in B_marked_quotient_sector.tex are proved after full root and OC audits. The full-monodromy exact index is nu_min(p,t(p−1),2)=2 for p≥5,2≤t≤2p+1,p∤t; new p5 indices32,36,44. The common degree-p² point field identifies quotient high lines even in the scalar case. The second quotient requires only first-level prime-parameter recovery, separately proved. Root-authorized CP26 wiring was made in consolidate.py and prepare_checkpoint26.py; prior versions and hashes are preserved. The p-divisible absolute indices and next prime-to-p e=2(p²−1) remain outside this theorem. No code run failed; the discarded weight-sign outline is retained separately and unused.

## 2026-11-19T22:19:59.767330+00:00 — B72 promoted after full audits

Exact full B4 nu_min(p,2(p^2-1),2)=2 for p>=5; combined tame sector2<=t<=2p+2,p not dividingt. p5/e48 settled; e52 and p-divisible indices not asserted. The strict first-level mixed break is exactly the information retained by the second actual quotient. This late promotion is separate from the frozen CP26 paper and is for CP27 integration. No executed numerical check failed.

## 2026-11-19T22:38:50.922346+00:00 — B73 promoted after full audits

Exact full B4 height-two index nu_min(p,e,2)=2 iff p<e<p^3, for p>=5, mu_p in K, p not dividing e, perfect residue. e=p-1 has index1; permitted e>p^3 has index at least3. No exact higher-index or wild absolute-ramification claim. The actual high-branch point fields identify high lines even in scalar residual modules. The final actual comparison is only p-torsion and uses the genuine tame/wild distinction. CP27 wiring authorized by root is complete; no build or global report was run here.

## 2026-11-19T22:50:15.749863+00:00 — B74 promoted: iterated high quotients

Full B4 height-two upper nu_min<=n-1 for n>=3 and e<p^n, when p>=5, mu_p in K, perfect residue and p not dividing e. Exact nu_min=3 for p^3<e<p^4. The interval p^4<e<p^5 retains only bounds3..4; no wild absolute-index or higher-height claim. For p=5, every permitted multiple of4 from128 through624 has exact index3; e628 is bounded3..4 and remains unresolved here. All quotient comparisons have the explicitly retained truncation level, with only p-torsion at the final stage.

## 2026-11-19T23:06:31.825734+00:00 — B75 promoted: terminal Frobenius pair

p>=5, mu_p in K, perfect residue and p not dividing e. Whole formal character recovery from actual p^n for n>=3 and e<p^(n-1)(p+1). Full B4 upper nu<=n-1 only for n>=4. Exact index3 for p^3<e<p^3(p+1); p5/e128..748 prime to5. Next p5/e752 remains bounded3..4 with no comparison constructed.

## 2026-11-19T23:11:36.278202+00:00 — B76 promoted: wild-index cyclic restriction

p>=5 with arbitrary absolute ramification e: rational exact p^n in a height2 formal group forces a>(p^2-1)p^(2n-3-v_p(a)); mixed whole/filtered comparison forces e>p^(2n-3-v_p(e)). For mu_p in K, n>=v_p(e)+2 detects total dimension. At p5/e20 any actual125 failure is confined to two whole potentially supersingular groups. No whole-formal125 recovery or exact wild least index is asserted.

## 2026-11-19T23:19:07.417391+00:00 — B77 promoted: first wild finite patterns

p>=5, e=p(p-1), height2, mu_p in K, perfect residue: least full B4 index is bounded2..3. Actual p^3 failure requires two whole potentially supersingular groups and nonsquare finite determinant. Atp5/e20 only normalized AB/AC finite-character patterns, joint24, remain. No existence or exact wild index claim.

## 2026-11-19T23:33:17.285150+00:00 — B78 promoted: terminal CM layer

At arbitrary e, nonsquare potential-CM height2 characters recover from actual p^n for n>=v_p(e)+2. At e=p(p-1), exact least manuscript index2 within the potentially CM, potentially supersingular subclass, with explicit actual mod-p2 lower pair. Full p5/e20 index remains2..3 and remaining125 failure has a non-CM member.

## 2026-11-19T23:53:10.297621+00:00 — B79 promoted: minimal wild third-level image

At e=p(p-1), a different-character actual p^3 pair with irreducible residual inertia must have wild order p^r,4<=r<=8. No CM assumption and no larger-image/reducible-residual exclusion. First-wild full index remains2..3.

## 2026-11-20T00:09:23.412126+00:00 — B80 promoted: finite Cartan fourth layer

At e=p(p-1), a different-special-character actual p^3 pair with irreducible residual inertia and wild image of order p^4 has abelian full finite image, with wild image equal to the principal units of a rank-one unramified-quadratic algebra modulo p^3. This is finite-level only: no whole-group CM, branch existence/exclusion, larger-image or reducible-residual conclusion is inferred.

## 2026-11-20T00:21:31.933277+00:00 — B81 promoted: actual fourth-order Cartan excluded

At e=p(p-1), an actual p^3-congruent different-special-character pair with irreducible residual inertia cannot have wild order p^4. Combined with B79, remaining wild orders are p^5 through p^8; at p5/e20 the minimum is3125. No larger-image, reducible-residual, whole-CM, existence or unrestricted recovery assertion.

## 2026-11-20T00:37:04.496311+00:00 — B82 promoted: residual-wild terminal matrices

At first wild e=p(p-1), actual p3 comparison with two slopes, wild order p4 and one B=pb with p not dividing b recovers the high line and finite character. A different-character comparison with nontrivial residual wild inertia must have wild order p^r,5<=r<=9. Residual-tame exchanged high lines and larger images remain open; full index stays{2,3}.

## 2026-11-20T00:48:52.086776+00:00 — B83 promoted: actual opposite quotients

At first wild e=p(p-1), actual exchanged-high quotients force both opposite original W1 entries. For p=1 mod4, nonsquare determinant separates tame weights and actual commutators force wild order>=p^5. Together with B81/B82, every p5,e20,125-torsion failure has wild image at least3125; larger images and full index{2,3} remain open.

## 2026-11-20T01:06:23.446838+00:00 — B84 promoted: one-prime point-field recovery

For arbitrary e and L-rational first-level modules, actual p2 comparison recovers both high lines, Newton parameters and finite characters whenever at least one b is prime to p. At p5,e20, the residual-tame necessary pattern at every image size is B25/75,A/B up to common quadratic twist. No pair existence or exact first-wild index is claimed.

## 2026-11-20T01:22:06.643066+00:00 — B85 promoted

Actual second-level degree-p point fields force both diagonal projections. For p=1mod4, the tame reducible sector has wild order at leastp6; no bound across other residual types.

## 2026-11-20T01:22:06.644036+00:00 — B86 promoted

The actual cyclotomic subfield excludes W1=W2=sl2. Together with B85, the tame reducible p=1mod4 sector has wild order at leastp7; p5 tame ambiguity only at5^7 or5^8, with B25/75. Full index remains{2,3}.

## 2026-11-20T01:41:09.785549+00:00 — B87 promoted

At p5,e20, any different-special-character actual125 comparison with tame reducible residual inertia requires W1=W2=M2(F5), the full principal congruence image of order5^8, and mu25 notinK. The necessary B25/75,A/B pattern remains; no actual full-image realization/exclusion or other-sector conclusion.

## 2026-11-20T01:53:27.501915+00:00 — B88 promoted

Necessary actual p5/e20 tame full-image profile: E1 lower(6,336), E2(24,234); full second-field upper6,24,66,72 and lower6,96,1146,1896; actual cyclotomic quotient breaks72overL,3overK. No impossibility or realization of the full image or a BT comparison is inferred.

## 2026-11-20T02:08:43.406089+00:00 — B89 promoted

Explicit allowed p5/e20 base with cyclotomic degree-five break3, degree-25 cyclotomic125 image, and break72 after tame24 extension. Base/cyclotomic realization only; no height-two BT group, common torsion comparison, ambiguous pair, least-index lower example, or main-gate closure.

## 2026-11-20T02:36:13.002000+00:00 — B90 promoted

Actual third-level point fields exclude the whole tame reducible residual different-special-character125 comparison at p5/e20. Exact determinant coset average1896/5 is impossible. Irreducible-residual and nontrivial-residual-wild sectors remain open; unrestricted least-index interval stays{2,3}.

## 2026-11-20T03:17:44.172358+00:00 — B91 promoted

Residual-wild actual p^3 comparison at e=p(p-1): both Newton parameters are p-divisible. At p5/e20 crossing rows only (5,45)/(15,95); both-large original parameters force layer shapes (3,4)/(4,4), hence actual wild orders5^8/5^9. No crossing realization, full residual-wild exclusion, irreducible-residual change or least-index closure.

## 2026-11-20T03:26:59.392065+00:00 — B92 promoted

The actual quotient25 comparison has full first image and four coordinate cyclic breaks; both residual-wild crossings have full parahoric order5^8. The actual diagonal field excludes (15,95), leaving (5,45). Both-large and irreducible residual sectors are unchanged; no surviving-row realization or unrestricted least-index closure.

## 2026-11-20T04:00:39.853594+00:00 — B93 promoted

Actual original residual-wild crossing(5,45) is excluded by the same terminal determinant character: upper bounds275496/70296 contradict its lower391896. Together with B92 this removes all crossing rows. Remaining residual-wild cases have both parameters above20 and layer shapes(3,4)/(4,4); irreducible residual cases and unrestricted index{2,3} remain open.

## 2026-11-20T04:36:15.894287+00:00 — B94 promoted

Six of ten both-large residual-wild parameter pairs are excluded in layer shape(3,4). Remaining(3,4) pairs are(7,15),(9,13),(9,17),(11,15); every(4,4) pair and irreducible residual case remain open. No realization or unrestricted least-index equality is inferred.

## 2026-11-20T04:45:45.822347+00:00 — B95 promoted

All residual-wild layer(3,4) comparisons at p5,e20 are excluded. A surviving residual-wild comparison must have the full actual Iwahori image of order5^9 and layer(4,4). That branch and irreducible residual orders5^5..5^8 remain open; no realization or unrestricted least-index equality is inferred.

## 2026-11-20T05:15:23.184178+00:00 — B96 promoted

All nontrivial residual-wild actual125 comparisons of whole potentially supersingular height-two groups with different finite special characters at p5,e20 are excluded. The irreducible-residual image orders5^5..5^8 and the unrestricted least-index alternative{2,3} remain open. No comparison realization is inferred.

## 2026-11-20T05:34:20.925830+00:00 — B97 promoted

For every p>=5 at e=p(p-1), a different-special-character irreducible-residual actual p^3 comparison must have traceful layers(3,4) or(4,4). All actual second-point degrees are p^2, third-point relative degrees p^2, and terminal conductors satisfy the proved bound. At p5/e20 only orders5^7 and5^8 remain under this result; no exact least-index closure is inferred here.

## 2026-11-20T05:37:57.534831+00:00 — B98 promoted

Exact full B4 height-two least index nu_min(5,20,2)=2: actual125 determines all requested prime-to-five special characters, and actual25 can fail. For every p>=5 at e=p(p-1), the irreducible-residual whole height-two branch is recovered at actualp^3. No full first-wild equality for another prime, general ramification or higher height is inferred.

## 2026-11-20T06:15:05.964407+00:00 — B99 promoted

Whole potentially supersingular height-two irreducible-residual finite special characters are recovered from actual p³ for every e=t p(p−1), p not dividing t. No reducible/mixed comparison or new full least-index equality is asserted.

## 2026-11-20T06:21:23.781219+00:00 — B100 promoted

Actual p³ ambiguity for p>=5, p(p−1)|e, e>p², with one whole potentially good group and one allowed filtered group. The existential mixed threshold is exact at vp(e)=1. Full exact height-two family ν_min(p,2p(p−1),2)=3; in particular ν_min(5,40,2)=3.
