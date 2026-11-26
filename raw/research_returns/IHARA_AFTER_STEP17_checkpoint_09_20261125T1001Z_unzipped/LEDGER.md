# Research ledger

Started 2026-11-25 04:16 Europe/Berlin (03:16 UTC). First 45-minute checkpoint due about 05:01 Europe/Berlin; checkpoints are immutable full deliverable ZIPs. First three-hour gate review due about 07:16 Europe/Berlin, then hourly.

## Initial gates

- A1: componentwise quotient: definition depends on lifts; exact c-fixed counterexample proved. Need arithmetic realization and Galois-stable correction.
- A2: componentwise arithmetic: three different indices are being traced; no kernel inclusion claimed.
- A3: relative pole separation: subgroup injectivity alone does not prove quotient detection; explicit retraction counterexample proved.
- B1: CM freeness: newer Ishii source records a relation for most class-number-one fields; explicit derivation certificate under construction.
- B2: CM Iwasawa module: semilinear complex conjugation exchanges variables; exact invariant-module obstruction proved at algebraic level.
- K1: K-theory dependency and finite-to-infinite class group transport being verified.
- I1: integral generation: no assertion yet; rational leading terms alone do not control a lattice index.

## 04:25 Europe/Berlin

First editable paper draft written with full proofs of lift dependence, exact kernel comparison, and dual-character formula. Other results enter only after verification.

## 04:59 Europe/Berlin — mathematical gate review during drafting

- A1 REFUTED as a general Galois assertion: at p=37 every exact c-fixed primitive lift of T32 has H-normal closure not stable under Γ. Proof uses U≅Λ^18 and the nonzero η7/η25 cup. Arbitrary lifts also have a finite UT4 certificate.
- A2 PROVED in the canonical abelian form: the outer kernel has zero image in (U/D)⊕⊕T_e when X_e and X_(2−e) are finite. Independent statement-only reproof found and resolved a finite exceptional-weight issue by quotienting out those target letters. Full proof is in the paper.
- A3 OPEN: ambient saturation has the desired abelianization but the nonabelian kernel containment remains. An exact Γ×Δ-equivariant abstract model proves factor injectivity alone insufficient even after saturation.
- K1 PROVED transport and reflection calculation: K4m(Z)/p identifies the −2m class component, norm coinvariants identify the bottom class group, and reflection supplies the paired component at every prime for m=1..15,21. Other m≤30 have fifteen certified possible exceptional primes, each at one weight. The all-prime −2m input remains explicitly dependent on the posted K-theory theorem.
- I1 REFUTED: specified Soulé elements do not generate degree32 at37, by McCallum–Sharifi Thm9.7 with Brown's now-proved injectivity. The nonzero cyclic cokernel has order37^r with r≥1; r=1 is not proved here.
- B1 REFUTED for w_K=2: the claimed free elliptic Lie algebra has the explicit Pollack relation. Independently re-proved. For Q(i),Q(√−3), freeness remains open.
- B2 OPEN with smaller structural gates: semilinear plus eigenspaces over the full two-variable algebra were computed exactly; class-number and decomposition hypotheses are proved by hand in the two smallest examples. Their Γ≅Zp² extension has nonzero transgression, so commuting lifts require a different argument.
- F.3.32: Nakamura1996 printed115–117 source use now checked; the complete polynomial certificate still needs recreation and verification, and its arithmetic-to-geometric input map remains a separate gate.

This is not the prescribed three-hour stagnation review; first such review remains due07:16 Europe/Berlin.

## 05:26 Europe/Berlin — component and CM gates advance

- A1: the non-Galois result at 37 now covers every primitive lift of the pure even component, not just complex-conjugation-fixed lifts. Independent statement-only reproof passed.
- A2: canonical class-two component quotient detected under the paired hypotheses X[e] and X[2-e] finite. Independent statement-only reproof passed; the paper includes the construction and proof.
- B2: the two explicit CM examples have a repaired pure-locality proof, independently re-proved using a local Hilbert pairing. Their maximal abelian extensions above the full ray tower are detected.
- CM elliptic-unit radicals at every split prime: Ishii's complete primitive-pair moment formula gives a promising unconditional proof; the auxiliary-ideal step is under independent review. No completed claim is recorded yet.
- F.3.32 polynomial identity reconstructed from invariant-tensor definitions: all 36 entries vanish exactly. Full geometric reductions and the arithmetic-to-geometric bridge are separate gates.

The first prescribed three-hour stagnation review remains due at 07:16 Europe/Berlin.

## 05:44 Europe/Berlin — second scheduled checkpoint preparation

- The paper is now 42 pages and compiles from a fresh copy with no overfull boxes or undefined references. The two main theorems are stated in Section 1; the former abelian theorem is now a corollary of the stronger canonical class-two theorem. First two PDF pages visually inspected; complete visual and two-reading review remains pending.
- A-ALL-LIFTS PROVED: intersection of the normal closures over all unrestricted lifts of a finite abelian direct summand is trivial when the retained free rank is at least two. Two different Magnus marker proofs give finite p-group separators. Universal lift-wise containment is exactly equivalent to full outer faithfulness.
- CM-RADICAL PROVED: at every split prime p≥5 in class-number-one CM fields, all elliptic-unit radicals are detected; their Galois quotient equals the quotient separated by all elliptic Soulé characters. Independent statement-only reproof completed.
- CM finite-plus gate advances: an exact Kummer class-group annihilator and a trace argument from finite inverse-limit plus to zero direct-limit plus are being checked. They are not yet claimed in the paper.
- Full higher Magnus separation of the original note has been checked, including repeated roots and inverse-limit substitution. The obstruction for a larger selected quotient remains its explicit Galois-stable kernel and target factorization.

First scheduled three-hour gate review still due at 07:16 Europe/Berlin. Next checkpoint after this one is due at 06:31 Europe/Berlin.

## 06:25 Europe/Berlin — strict reductions before checkpoint 03

- A-CENTRAL-TORSION PROVED and independently reconstructed: for every odd prime the outer action detects Q=(W plus E/Z), where Z is central Lambda-torsion. All odd commutators survive. Paired component finiteness proves Z[e]=0 and full survival of T_e. The new unconditional theorem replaces the selected quotient as the first main theorem.
- CM finite-plus abelian gate CLOSED: exact full-class Kummer sequence, norm/extension capitulation, anticyclotomic invariants vanishing by cyclotomic weak Leopoldt, and the exact finite-index elliptic-unit comparison prove full abelian detection. Independent reconstruction of the cohomology and character-orbit argument passed.
- CM source freeness PROVED under finite X2+. The graded Lie freeness in Ishii's proposed presentation is a separate assertion connected by the filtered outer map; its w=2 Pollack relation remains.
- CM component form PROVED: a c-stable tame character set O with finite fixed class component gives detection of e_(cyclotomic O^-1)A. The Kummer twist is proved explicitly.
- New p37 Gamma-core proof is being independently reconstructed; proof record saved but not yet promoted into the paper. It uses an actual Gamma-stable odd free factor and a Vandermonde identity on adjacent pair matchings.
- Nonabelian CM attempt via exact eigenlifts fails through an explicit module equation: a torsionfree Lambda2 abelianization admits no nonzero eigenvector for the proposed gamma scalar. The Pollack relation gives a deeper outer image; exact cancellation still requires integral filtered strictness.

This is a progress entry, not the prescribed stagnation review. The first scheduled review remains 07:16 Europe/Berlin (06:16 UTC). Checkpoint03 is due06:31 Europe/Berlin (05:31UTC); the next checkpoint is07:16 Europe/Berlin.

06:28 Europe/Berlin: A-GAMMA-CORE37 independently re-proved and promoted into the paper. Thus one literal lift-wise inclusion at37 is equivalent to full faithfulness, through the exact core map.

Checkpoint03 materialized at 2026-11-25T05:31:15.280462+00:00:52-page PDF freshly rebuilt; no overfull boxes or undefined references; first two pages visually inspected. Full final readings remain pending.

## 07:16 Europe/Berlin /06:16 UTC — first scheduled three-hour review

Movement: YES. This is the first scheduled review; no consecutive no-movement review is recorded.

- A single-component arithmetic row CLOSED: Ohta2020II6.2.2 plus Ohta2026density2.3.4 and exact dagger/Tate transport supply Upsilon; cyclicity plus FK handles every multiplicity. Independent reconstruction proves one uniform p-power cup bound. The selected canonical class-two theorem uses X[e]finite alone, and all thirty K-theory characters now apply at every odd prime with the posted dependency.
- A main kernel gate STRICTLY SMALLER: Kouter⊂K3⊊K2 by a source-defined canonical central relation quotient. All completed Lie3(W) survives. Two independent statement-only reconstructions and a separate Jordan-residue proof agree.
- A literal lift construction remains REFUTED as Galois-stable. Every pure lift at37 has trivial Gamma-core, so even one literal containment there is equivalent to full faithfulness. The larger specified ambient quotient remains OPEN beyond the canonical K3 reduction.
- B finite-plus abelian, source freeness and character-orbit rows CLOSED during this review interval. Full nonabelian CM faithfulness remains OPEN at the exact filtered correction map. A/Nell now embeds in the regular two-variable measure module, giving torsion-free source control and an exact obstruction to eigenvector lifts.
- Geometric detector computation CLOSED: six Johnson brackets, determinant-203784 and R-vanishing independently recalculated. Full geometric recognition draft now uses the degree27 UT3(F3) cover of genus10; root has not yet completed the full polynomial-to-geometric proof audit. The arithmetic-centralizer-to-geometric-procyclic map remains OPEN.
- K-theory dependency audit and integral degree32 obstruction remain PROVED at their stated scope. No new Lean kernel run or modified Gaussian archive verification is claimed.

Current active approaches: selected class-three quotient; higher companion residue saturation and degree-four resonances; full geometric normalization audit with the explicit high-genus cover. Next hourly review due08:16 Europe/Berlin /07:16 UTC. Next checkpoint due08:01 Europe/Berlin /07:01 UTC.

## 07:56 Europe/Berlin /06:56 UTC — work before checkpoint05

- Selected Q3 row CLOSED: exact canonical normal closure, abelianization(U/D0)+T_Sigma, all graded modules, two independent reconstructions. The all30 application now uses its strictly larger class-three field.
- Geometric recognition row CLOSED at its precise geometric scope: full profinite detector, genus10 UT3 cover, arithmetic core and rational cusp, Nakamura degree6 quotient, Hain strictness, Johnson detector and all-parameter polynomial identity. The arithmetic centralizer bridge remains OPEN; the paper gives its exact pullback obstruction.
- Degree-three source divisibility CLOSED by two proofs. Positive-weight eigenvalue exclusion CLOSED via finite HS duality and K-theory finiteness.
- CM nontrivial procyclic normalizers now have trivial Gamma image under finite X2+; independent bare-statement root reconstruction passed. The full nonabelian CM kernel remains OPEN.
- Canonical class-four construction is under independent source verification: pair/triple pole injection and bounded-torsion proof have been written; the separate Hall-presentation reconstruction remains pending. It is not yet a main-paper theorem at this entry.

This is not the scheduled hourly stagnation review. Next review remains07:16UTC; next checkpoint07:01UTC.

Checkpoint05: canonical class-four theorem completed and integrated before packaging. Source-defined K4det is strictly smaller than K3, all pure odd Lie4(W) survives, and Q4 is the exact compact image through length four. The integral Hopf/HS proof uses symmetric Koszul parameters, including p=3. Fresh PDF: 80 pages. Main gate has strictly decreased again.

Checkpoint05 saved at2026-11-25T07:04:37UTC:142files,1493259bytes, SHA256 f4b20c5666b9c18f5ee70062863056a40410ebe055928b72c1d3bb5a77f9fa19. Native file libfile_f9dc4eaf17308191ae02bcf2f1c34835. The planned07:01 save was completed after the final class-four insertion and fresh build. Next checkpoint remains the scheduled07:46UTC slot; next stagnation review07:16UTC.

## 08:16 Europe/Berlin /07:16 UTC — second scheduled review, recorded07:23UTC

Movement: YES. Consecutive no-movement reviews: zero. The review was recorded seven minutes after its scheduled time, following the source and selected-class-four independent checks. The hourly schedule remains anchored to the start time; the next review is08:16UTC.

- A main kernel gate is STRICTLY SMALLER: canonical K4det is strictly below K3, with full Lie4(W) injection, a closed explicit torsion annihilator and exact equality with the fourth truncated outer-image kernel. Full independent source reconstructions and a later complete CM-worker audit passed.
- A selected quotient row CLOSED through class four: the omitted even BCH submodules of B4 have an intrinsic Galois-stable normal closure; Ab=(U/D0)+T_Sigma, with exact class4 when-2,-4 belong to Sigma. Two separate statement-only reconstructions passed. The all30 application is correspondingly stronger.
- The complete geometric normalizer recognition row CLOSED during this interval, with exact covering, monodromy and tensor maps. The arithmetic centralizer bridge remains OPEN at its precise extra-input gate.
- CM nontrivial procyclic normalizer exclusion CLOSED, but full CM nonabelian faithfulness remains OPEN at the integral filtered correction map.
- Degree-four and all-degree pair-companion total-product saturation now have independent algebraic proofs. Root integration and the broader multi-companion arithmetic extension are in progress; no all-degree arithmetic kernel theorem is recorded.

Current main approaches: exact fifth-stage source presentation and multi-companion residue saturation; CM arithmetic centralizer and filtered correction maps. Next checkpoint remains07:46UTC.

Checkpoint06 preparation,07:43UTC: selected class-four theorem, all-degree pair-companion divisibility and the exact CM centralizer pullback are integrated. Fresh PDF86pages, no overfull boxes or undefined references. First two pages visually inspected; all first-page credit locators fit. The fifth canonical stage is being checked at its rational adapted-coordinate and bounded-torsion steps; no fifth-stage paper claim yet. Next scheduled hourly review08:16UTC; checkpoint07due08:31UTC.

Checkpoint06 saved2026-11-25T07:46:17UTC:160files,1602331bytes; SHA256133bafab943e2cc39c0b7e42199b3b8f051ab6910e1df0527842db32ffbd7cef; native file libfile_68af4a550d7c8191af9664efd9336d27. Fresh86-page PDF, precise52-statement index, complete new selectedQ4/pair-saturation/CM-pullback proofs, and explicitly unfinished Q5 record included. Next checkpoint08:31UTC; next scheduled review08:16UTC.

After checkpoint06, canonical and selected fifth quotients CLOSED and independently checked. Root audited full fixed-class source correction, preserved the lower bounded torsion, checked the exact d5=max(d4+c4,2b+c) bound and the new cubic total4 residue map. Kouter is contained in K5det strictly below K4det. The paper is being reorganized around the fifth theorem, with earlier canonical stages as body results. The all-stage representation and inverse-limit intersection remain OPEN.


## 09:16 Europe/Berlin /08:16 UTC — third scheduled review

Movement: YES. Consecutive no-movement reviews: zero. The review is anchored to the original hourly schedule; the next review is09:16UTC.

- A main kernel gate is STRICTLY SMALLER: the fifth canonical source kernel K5det is strictly below K4det. The exact class-five quotient detects every pure odd Lie5(W) word, with an explicit closed torsion annihilator. Independent source reconstructions by the CM and K-theory workers and root proof audit passed.
- The selected class-five row CLOSED: the canonical quotient has abelianization (U/D1) plus T_Sigma, maps onto the selected fourth quotient, and has exact class5 when the characters-2 and-4 lie in Sigma. The all30 application now uses this larger detected field.
- All-degree pair-companion saturation is proved and integrated. The all-stage arithmetic extension remains OPEN: the current precise gate is the source reduction for the full complex of coefficient cuts, including crossing internal poles. A local balanced tensor injection has been proved, but it does not settle that gate.
- The canonical recursion limit remains OPEN for the arithmetic source. An independently checked explicit free pro-p model computes a nontrivial limit under the structural freeness and eigenvalue assumptions alone; no arithmetic realization is claimed.
- CM full nonabelian faithfulness remains OPEN. The exact centralizer pullback is integrated. A source-defined CM class-two measure quotient retaining full abelianization is now under independent statement-only verification; it is not yet counted as a closed theorem row at this review.

Current approaches: the full cut-complex principal-part map for arbitrary companion weights; the CM shear operator on the image of elliptic Kummer measures; exact arithmetic control of the canonical limit. Next checkpoint remains08:31UTC.

08:26UTC: CM-MEASURE-CLASS2 CLOSED after a frozen bare-statement integral reconstruction and root source/map check. The exact displacement identity gives a canonical detected torsionfree class-two quotient retaining all of A. Finite integral character operators prove exact class2 for every classnumberone CM field, strengthening the original two-field candidate. The main CM theorem and proof overview now include it. The arithmetic image intersection with kerJ remains OPEN.

Checkpoint07 preparation08:29UTC: fresh96-page PDF,57 indexed statements, no undefined references or overfull boxes. First two pages visually inspected; all first-page credit locators fit. Added the all-K CM class-two theorem, exact source-limit countermodel and odd-torsion/plus-finiteness adjoint comparison. Full final expert/newcomer readings and all-page visual inspection remain pending.

Checkpoint07 saved2026-11-25T08:31:25UTC:182files,1760738bytes; SHA256dec7a6037b13ed82fb7d750c71ffc6c5b03bcb92fc3878b0e49a8f98e8e2b36f; native file libfile_0c6f0bdf8214819189d77714e1383e45. Fresh96-page PDF and57-statement index. Next checkpoint and scheduled hourly review are both09:16UTC.

09:13UTC: All-degree arbitrary weighted companion saturation, all-stage arithmetic source recursion, exact outer-kernel intersection, and integral all-stage selected quotients CLOSED after the frozen independent reconstructions and root full proof comparisons listed in CHECK_EVENTS. The selected Sigma30 application is now strict through class61. Paper reorganized around these results; earlier explicit classes remain in the body. Full final expert/newcomer readings and all-page visual inspection still pending. Checkpoint08 remains due09:16UTC.

## Scheduled review4 —09:16UTC,25November2026

Movement: YES. Consecutive no-movement reviews: zero. The next review is10:16UTC.

- CLOSED the arbitrary-weight all-degree companion source-saturation gate, with two frozen independent proofs and full root paper audit.
- CLOSED the all-stage arithmetic source recursion. Each Q_n is the exact compact outer image through generator length n, torsionfree of exact class n. The original characteristic polynomial defines every closed torsion kernel with a bounded p-power.
- CLOSED the exact outer-intersection identification: intersection F_n=Kouter and union of detected canonical fields=Omega*. Triviality of this intersection remains OPEN; the structural countermodel remains relevant.
- CLOSED the selected all-stage construction using all tame eigen-elements and integral central averaging. The exact abelianization retains every selected T_e; the Sigma30 field tower is strict through class61 on the stated external vanishing inputs.
- CLOSED the CM class-two decomposable-kernel row: every rationally independent abelian pair has a nonzero shear commutator. The general completed wedge intersection with kerJ remains OPEN.

The paper has been reorganized around the stronger theorems. The canonical class-five and earlier explicit stages remain in the body. Fresh three-pass compilation succeeded, with no overfull box or undefined reference. First two pages were visually inspected and all precise credit locators fit on page1. Full final expert/newcomer readings and every-page visual inspection remain pending. Checkpoint08 is the scheduled immutable snapshot; the next checkpoint is10:01UTC.

Checkpoint08 saved2026-11-25T09:16:15UTC:209files,1989455bytes; SHA25604a42d9a2b1959407ae33b57b7a307dab74f625c8f256c8eb10690630149452c; native file libfile_08b4be336c18819192e96e2c5f07ac32. Fresh109-page PDF,65-statement precise index. Next checkpoint10:01UTC; next scheduled review10:16UTC. Prior snapshots remain immutable.

09:53UTC interval update: the exact relation-module and Fp-augmentation inverse-limit obstruction is proved, with its Hopf homology term. The CM geometric measure now has an exact finite-level identification with the dual of the elliptic Euler triangle cokernel, including normalization12/144, Kummer restriction, origin correction, natural transition and integral lattices. The remaining CM class-two gate is this integral inverse system; cokernel-transition injectivity and bounded persistent duals remain open. Root completed the full10210-line newcomer reading; K-worker completed the earlier whole expert reading and is checking all later additions. No final completion claim or early research stop. Next checkpoint10:01UTC; next scheduled review10:16UTC.

Checkpoint09 preparation09:58UTC: new finite elliptic Euler-kernel theorem, continuous Hopf comparison, exact mixed-chart image, CM centralizers/free subgroups, and relation-module Fp obstruction integrated and independently checked. Whole expert/newcomer readings complete for documented snapshots and added proofs; remaining visual and final-delta checks explicitly pending. Fresh118-page build passed without overfull/undefined references; first2pages inspected. Exact source tables repaired and all11 programs documented.
