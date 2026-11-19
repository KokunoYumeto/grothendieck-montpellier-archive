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
