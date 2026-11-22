# Part B working notes

AI-produced by GPT-6 Astra (OpenAI), run /root/part_b, begun 2026-11-20 00:11 UTC.

## Current checked state after closure of the weak gate

All requested Part B assertions and the separately tracked weak replacement are decided. B.1 and all margin variants are proved, including the infinitesimal part. B.2 uniform h1 boundedness holds over every field. The stronger claim of one constant domination-cofinal Picard diagram is false over imperfect fields by the explicit threefold B.2q. The distinct weak assertion, a stable upper cone above every initial permitted model, is proved over every field in B.2u. B.3 has the requested proof without fundamental-group theory and the corrected ell-not-equal-p rank formula. L6c proves R1 normal-to-regular birational vanishing in every dimension. Complete proofs, exact primary locators, finite example certificates and independently scoped audit events are saved. No priority or original-discovery claim is made.

The chronological working entries below preserve earlier failures and gates; they are historical and are superseded by this current state.

## Historical checkpoint at 2026-11-20 00:48 UTC

The complete checked proofs are now in `paper_B.tex`, and the genuinely unresolved full-group stabilization assertion is isolated in `unresolved_B.tex`. The earlier working paragraphs below record the route as it developed and are superseded by this state:

- B.1 is proved, including all margin variants, by finite-flat torsor purity, Raynaud duality, and finite subgroup detection.
- B.2 uniform h1 boundedness is proved, including geometrically normal models over arbitrary fields and dimensions zero and one. The geometric generic curve argument was independently audited by the root agent; this event is recorded as a targeted proof check, not a second discovery.
- B.2 full Pic^tau essential constancy remains unresolved in general. Tangent-space constancy and the smooth-proper-model case are proved. A stronger finite Galois quotient case is under audit; regular Galois alterations then reduce the remaining issue to purely inseparable descent.
- B.3 is proved without fundamental-group theory and without properness of Pic^tau. The manuscript's n(K/k) is existential (Pro line1133), and scan077 explicitly permits a generic-curve genus, as our proof supplies. The restriction ell not equal p is necessary and explicitly checked.
- L6's deformation criterion and smooth/surface vanishing cases are proved or verified with exact primary sources. Its suggested counterexample search is vacuous under B.1's hypotheses.
- `results_B.csv` has exactly the requested seven columns; `CHECK_EVENTS_B.tsv` records checks; `corrections_B.tsv` gives exact input file and line locators.

## Verified sources and manuscript corrections

- Read supplied Pro transcription cote 29 scans 71--77, source lines 916--1188; checked against study c29a lines 338--389.
- Manuscript 29/071 displays Pic(X)≃Pic(U); the intended Pic(Y)≃Pic(U) is forced by the next commutative diagram and factoriality of Y.
- 29/072 tangent-space argument has a genuine gap: α_p↪α_{p²} is a proper bijective closed immersion inducing a Lie isomorphism. It does not refute the Picard assertion.
- Moret-Bailly purity: current publication downloaded and read: Marrama (2026), Proposition 3, p.432, and Theorem 6, pp.433--434. Only this verified publication is cited in the paper.
- Raynaud (1970), Spécialisation du foncteur de Picard, Proposition 6.2.1, opened; exact statements being extracted.
- Search-index metadata associated Marrama with arXiv:2512.00235; opening that PDF found a wholly unrelated set-theory paper. This arXiv identifier is NOT used. Published PDF verified by actual title and contents.

## B.1 complete route, being formalized

Proper birational f:X→Y, normal X regular Y: inverse is defined and isomorphism on open U⊂Y with codimension≥2 complement. For any finite flat Y-group G, restriction of an f*G-torsor on X to U extends over Y by Moret-Bailly purity. The resulting pullback and initial torsor are generically isomorphic; normality of X extends this isomorphism because their Isom scheme is finite over X. Hence Tors(Y,G)→Tors(X,f*G) is an equivalence.

For finite commutative k-group H, Cartier duality converts this to Hom(H,Pic_Y)≃Hom(H,Pic_X). Each map from finite H lands in Pic^τ. Pullback Pic^τ_Y→Pic^τ_X is a closed immersion via universal f*O_X=O_Y and properness. A closed subgroup of a proper commutative k-group containing every finite subgroup is the whole group: prime-to-p torsion is dense in the reduced identity abelian variety; every component has a torsion point; a sufficiently high Frobenius kills all nilpotents, and its finite kernel plus the reduction fppf-generates the group. Thus B.1 true, all margin variants automatic over algebraically closed k except projectivity, which is not needed.

## B.2 new route, targeted checking in progress

Fix projective normal M with function field K, U=M_reg, and coherent reflexive Ω_M^[1]=j*Ω_U. Its global section space V is finite-dimensional. Choose m so Ω_M^[1] embeds in O_M(m)^r, with locally split inclusion on U. Choose n>m and generic complete intersection curve C of d−1 degree-n hypersurfaces; C is smooth, proper, lies in U. The restriction V⊗F→H⁰(C,Ω_C) is injective: restriction of H⁰(O_M(m)) to C is injective by successive integral hypersurface sections (negative twists have no sections); conormal O_C(−n)^{d−1} has no sections.

For every model X, normalized graph W→M and W→X, C generically avoids the exceptional image (codim≥2) and lifts to W. Kernel of H¹(W,O)→H¹(C,O) Frobenius-stable. Any nilpotent part has nonzero ker F, represented by global exact differential on W; its rational differential extends to U and is in V, hence cannot die on C. Bijective part corresponds to étale Z/p covers; finite cover of W extends over U by purity and then normalization of M; inverse image of C is connected by ample connectedness. Hence uniform h¹(X)≤g(C).

Remaining checks: precise connectedness/Bertini source locators; base extension to arbitrary k (geometrically normal models); and separate eventual Pic^τ constancy. Bounded tangent dimension alone does not formally imply constancy (α_{p^n} chain), and the manuscript actually lists dimension, torsion, and tangent bounds together.

## B.3

Direct route via rational Albanese/Weil Picard variety or generic-curve restriction of reduced Picard variety. Need avoid fundamental-group theory and (per manuscript margin) properness of Pic^τ as a premise. The h¹ curve bound would imply dim Pic≤h¹≤g(C) without π₁, but its current stable-F step uses finite covers; a direct restriction-of-algebraic-families proof is preferable.

## L6

H¹ isomorphism + H² injectivity ⇒ formal Picard isomorphism by small-extension obstruction theory is valid; will write complete induction. Smooth-source higher-direct-image vanishing follows Chatzistamatiou--Rülling (2011) after exact source check. No counterexample to B.1 can exist once purity proof verified; therefore the proposed dimension≥3 counterexample locus is vacuous.

## Update 2026-11-20 01:53 UTC

Full Pic^tau stabilization is now proved for every perfect k in B.2h, following B.2d (one Jacobian embeds all modification Pic^tau schemes), B.2e (regular finite-Galois quotient), B.2f (purely inseparable function-field descent) and B.2g (de Jong). B.1e also proves the regular-target statement over arbitrary fields for geometrically normal geometrically integral source, using finite separable rational-point extension and finite k-group detection; this avoids an unjustified purely inseparable base change in torsor purity.

B.2i gives a complete explicit failure of filteredness over imperfect k. It does NOT refute constancy of the actual Picard diagram: the example is rational. The remaining gate now distinguishes weak stabilization over the upper cone of one geometrically normal model from a constant cofinal diagram for the nonfiltered category. We are investigating the abelian-target graph lemma and descent from the perfect closure. A general proper smooth target does not satisfy that graph lemma; the B.2i example uses P1 coordinates.

Source checks added: Milne Algebraic Groups 2022 author PDF, Theorems5.14/5.28, Proposition5.25, Theorems5.34/5.39 (pp102--108); Stacks0CCJ effective descent along finite locally free maps for quasi-projective schemes; Stacks0BXT normalization after finite purely inseparable base extension. Schröer2024 Th6.1 and Prop6.2 read in full: they control Albanese comparison, not geometric normality of compactifications.

Independent root-A arithmetic audit: opened Milne ADT II2.3a, II3.1/3.2, I2 local duality; root arithmetic-test proof passes targeted audit, including all primes, arbitrary torsion extension and b+1 closed-point H2 witness. Event appended to CHECK_EVENTS_B.tsv.

Programs added/run: promote_algebraically_closed_B.py (output: promoted B.2d-g, corrected B.2c scope, synchronized data); integrate_post02_B.py (output: integrated B.1e, B.2h, B.2i); imperfect_graph_certificate_B.py, 24 symbolic assertions at p=2,3,5, all passed, elapsed0.050912s; fetch_sources_B.py rerun with timestamped provenance logs. These maintenance scripts are not additional mathematical certificates.

## Update 2026-11-20 02:08 UTC

New candidate B.1f proves finite-group detection for every finite-type commutative group scheme over an arbitrary characteristic-p field. Relative Frobenius kernels force equality on the identity component by Krull intersection; geometric torsion representatives can be captured by finite k-group schemes after Frobenius and Galois descent. B.1g then extends normal-to-regular birational Picard invariance to geometrically integral proper schemes without requiring geometric normality. Source locators checked: MilneAG2022 Theorems8.27 (pp154--155),16.13 (pp328--329),5.34; Kleiman2005 Proposition6.12 and Remarks6.14/6.19 (pp57--60). The candidate is in B1_finite_detection_extension.tex pending root audit. Agent C independently obtained the special case where the target Picard group is proper via the same Frobenius/Krull argument.

Agent C is pursuing the uniform-bound route through an alteration over a finite purely inseparable ground extension. Agent D did a focused primary-source search for the abelian-target graph lemma: proper geometrically reduced graph Albanese base-change is known, but does not itself give geometric normality of the graph. We continue without assuming that lemma.

## Update 2026-11-20 02:08 UTC

Root independent audit passed the complete B.1f/B.1g candidate; both statements are now integrated into paper_B.tex and results_B.csv, and the precise audit is logged. No further input of B1_finite_detection_extension.tex is needed. This strengthens the arbitrary-field alteration comparison; full imperfect B.2 stabilization remains under active attack.

## Checkpoint03 freeze at 2026-11-20 02:20 UTC

Checked paper/results/bib are frozen for root assembly. B.1f/g are included; root independently audited B.2h/i, events appended. C's fixed-alteration kernel lemma was read and independently checked by B: normal Stein factor, finite flatness outside codimension two, norm and universal Hartogs control all nonreduced test schemes; B.1g fixes the altered Picard target and J[d] bounds the kernel rank. It is not yet integrated pending the checkpoint freeze; only the image gate remains.

Further failed construction tests: merely composing the rational P1 graph counterexample with a map into an abelian variety gives nothing, since such maps are constant. A regular geometrically nonnormal exceptional elliptic curve can be engineered in a blowup of a geometrically normal hypersurface by higher-order deformations, but those deformations destroy the map to a fixed elliptic target; this is not a counterexample to the abelian-target graph lemma. The Poincare/reflexive-algebra route still lacks graph identification or finite generation.

## Post-checkpoint03 state at 2026-11-20 02:47 UTC

B.2j--k are checked and integrated: C supplied the generic-degree Picard-kernel argument, and B independently checked every norm and universal Hartogs step against Stacks02KH/0EBJ/0BCY/0BD2. The full fppf kernel, including nonreduced parameter schemes, is killed by d; the fixed Jacobian bounds its rank by d^(2g). This leaves the image bound over imperfect k, not a kernel issue.

B.2l is checked and integrated: for geometrically integral K/k, one finite purely inseparable extension of constants suffices to obtain a geometrically normal projective model with stable Picard groups on its upper cone. We descend the stable k^perf-model, its projective equations and its birational marking, then descend the Picard isomorphism for any geometrically normal dominator. This is a finite-field-of-definition reduction, not descent to the original field or a cofinality assertion.

Cotner--Zavyalov2024 Lemmas3.4.1--3.4.3 were opened in PDF and TeX and are now cited as related finite-group detection/isomorphism criteria. No claim of a new finite-group principle is made. The exact role of the independent argument remains arbitrary finite k-subgroup detection in B.1f and the birational application in B.1g.

Additional unsuccessful image routes: Ravindra--Srinivas2005/2006 §5 recalls a Weil-Picard abelian variety over arbitrary fields for geometrically integral projective schemes smooth in codimension one, but its proved hyperplane theorem is over an algebraically closed field. Boissiere--Gabber--Serman2019 Proposition3.2 represents algebraically trivial Weil classes on normal parameter schemes, but the whole paper assumes k algebraically closed. Neither supplies a geometrically normal Cartierizing modification over imperfect k. The normalized Rees algebra of a divisorial ideal must not be identified with its symbolic/reflexive algebra: for R=k[x,y,z]/(xy-z^2), I=(x,z), one has overline(I^2)=x(x,y,z) while (I^2)^{**}=(x). This is a warning against that proof route, not a counterexample to geometric Cartierization.

We continue to distinguish the weak upper-cone problem and a specified cofinal-constant diagram. A hypothetical chain E[F^r] in a fixed ambient elliptic curve demonstrates only an abstract missing image bound. It is not claimed to arise from proper geometrically normal models. The two smooth rational threefolds in B.2i demonstrate nonfilteredness and have trivial Picard torsion parts, so they likewise are not a counterexample to Picard constancy.

## B.2m integrated at 2026-11-20 02:56 UTC

The fixed-alteration kernel bound is now unconditional on the constant field of an alteration: choose Y smooth geometrically integral over finite l/k by descent from kbar, compare through Res_{l/k}Pic^tau(Y/l), and use B.1g on normal main graphs over l. C simplified the proof to a kernel-only comparison, avoiding any tau/Weil-restriction equality. Root and C independently audited the complete written proof, including the correction from a potentially unjustified purely inseparable l/k to a general finite l/k. The remaining B.2-U gate is a uniform bound or realization of images in this fixed comparison object.

## Surface reduction before checkpoint04

B.2n--o establish the weak upper-cone Picard stabilization over arbitrary fields in dimension at most2. A fixed regular surface resolution gives a finite-length R1 sheaf; maximal length among permitted models forces R1=0 along the chosen upper cone. Lipman1969 Theorem12.1(i) provides geometric-point descent, and L6a plus the closed immersion retains the formal structure. C independently checked the source and proof. The proof uses regular-target vanishing from Lipman1969 Proposition1.2(2), not an unjustified application of the smooth CR2011 theorem over an imperfect field. The high-dimensional image bound and stronger cofinal formulation remain open.

## 2026-11-20 after checkpoint04: all-dimensional R1 vanishing

L6c is proved and independently audited by root and C. The proof uses only the already checked torsor equivalence B.1b, applied to alpha_p and constant Z/p after strict henselization at a minimal support prime. A hypothetical R1 becomes finite length; injective Frobenius forces the maximal ideal to kill it. The necessary semilinear fixed-vector lemma is proved over separably closed imperfect residue fields by stabilizing the spans of F^n M before using an invertible matrix. This rules out the proposed nonzero-R1 route to a B.1 counterexample in every dimension and makes the formal criterion L6a automatic. It does not by itself improve the remaining dimension-at-least3 singular-target image gate in B.2.

## 2026-11-20 03:26: explicit abelian-graph obstruction

B.2p refutes the special abelian-target graph lemma. The counterexample is the characteristic3 complete intersection over F3(a) given explicitly in the checked paper. It has seven geometric singular points and is geometrically normal; its normal incidence graph is regular along an exceptional E_{k(a^(1/3))}, whose generic local ring becomes the cusp s^3=t^2q after extending constants. Any normal resolving modification must retain that divisorial valuation, which is incompatible with geometric normality. Root, C and D independently audited the construction; root also audited the actual written file. The exact19-assertion certificate passed. Two initial certificate-harness errors were corrected: coefficient reduction before a univariate Poly, and the exponent t^4 in the cleared-denominator identity s^6=t^4q^2. The proposed stronger threefold nonconstant-Picard-branch construction is being independently attacked by C and remains provisional.

## 2026-11-20 03:43: literal B.2 pair decided; additional weak gate retained

B.2q gives a fully checked threefold counterexample to constant domination-cofinal Picard diagrams over an imperfect field. The generic triple cover of the cone over E1 times E2 has two geometrically normal partial graphs. All allowed models dominating the first retain E1 as geometric reduced Picard identity, and those dominating the second retain E2; the curves are not geometrically isogenous. The complete proof supplied by C was read by B and root; exact elliptic and A2 certificates each passed11 assertions. The literal h1 question is true, whereas the asserted equivalent cofinal constancy is false. A stable upper cone without cofinality is a separate weaker replacement that we continue to investigate for imperfect fields in dimension at least3. No failure of that weak replacement is inferred from the two branches. Equation tags in the copied fragment were made unique; the previously duplicate fixed-Jacobian tag was corrected to B.2.J.

## 2026-11-20 04:05 — weak stabilization under a regular model

B.2r and B.2s are checked and integrated. The weak upper-cone claim holds over arbitrary fields whenever a proper regular birational model exists, hence for all dimensions at most3 by the primary Cossart–Piltant2019 Theorem1.1. The key finite induction is on the dimension of the largest abelian subgroup of a fixed ambient Picard group: an excessive subgroup has a geometrically bad divisor in its rational Albanese graph; maximizing that valuation's allowed centre gives one fixed generic-fibre restriction annihilating all future Picard images but not that subgroup. No filteredness or fixed list of all bad divisors is assumed. At the end the ambient quotient has bounded exponent; the fixed Jacobian bounds finite orders. The all-dimensional extension via an equivariant alteration with semilinear constants is under actual-file audit.

## Final weak-gate closure: all-dimensional semilinear alteration proof

The fixed comparison group is R=Res_l/k Picτ(Y/l), with Γ acting semilinearly on the finite alteration constants. Every invariant abelian subgroup is realized up to [n]V^e by a rational abelian-torsor map over K: the construction keeps separable constants, kills translations for Γ0, descends through the finite Galois constant extension, and uses the q-power field homomorphism for the remaining purely inseparable extension. Its normal graph is either allowed and realizes the subgroup, or has a bad divisorial K-valuation. Maximizing that valuation's allowed centre and restricting on a fixed divisor above it in L imposes a closed subgroup condition that strictly cuts the excessive abelian part. The finite induction ends with ambient quotient of bounded exponent N. The comparison kernel is killed by d=[L:K], so the source Picard quotient by its maximal abelian variety is killed by dN; a fixed Jacobian bounds its order. A maximal-order model is stable under every later permitted domination. No filteredness or geometrically normal common refinement is used. The previously tracked gate B.2-U is closed; strong cofinality remains refuted, not silently weakened.

## 2026-11-20T04:23:24.243414+00:00 — independent full arithmetic-tower audit

Parent reassigned us from the unresolved general-model topology question to C's quadratic arithmetic construction. We read the entire actual file and independently checked its group, local, class-field, noetherian-limit, Brauer and Picard steps. The proof passes; detailed scope and exact reopened primary locators are in `A2_tower_independent_audit.md`. This supplies a full counterexample to general A.2 if promoted by the parent, independent of the cyclotomic Iwasawa gate. We do not claim that the paused higher-dimensional strictly-local-model question itself was settled.

## B normality convention, checked 2026-11-20T04:24:39.942443+00:00

The prompt explicitly interprets normal over k as geometrically normal. B.2 and B.3 use that convention throughout. In B.1 the ground field is algebraically closed, so ordinary normality and geometric normality agree, and regularity is smoothness; all margin variants are covered. B.1g independently establishes the ordinary-normal source/regular-target version over arbitrary fields under geometric integrality, and L6c only requires ordinary normality and regularity of integral Noetherian schemes. Parent was notified that proof-local paragraph formatting changes do not affect these statements.

## 2026-11-20T04:33:58.294482+00:00 — evidence inventory refinement and D audits

Under the parent's explicit narrow freeze exception, results_B.csv now separately inventories the three numbered B.2t lemmas and the numbered dimension-at-most-three corollary after B.2s. Statements B.2j--u and L6c now point to their actual theorem labels. There are 40 result rows, all with seven fields and distinct ids. No checked paper or bibliography was changed. We also recorded actual-file audits of A's sharp arithmetic-curve consequence, D's elliptic ramification/application theorem and D's finite-exceptional-wild-image criterion.
