# Review of GCT_NSRH.tex: F01–F15 and applications

Reviewer: `/root/rectangular_and_theta`, GPT-6 Astra Pro, inherited effort not exposed. Date: 2026-11-21 Europe/Berlin (review around 00:24; UTC 2026-11-20 23:24). Scope: complete proof texts F01–F15, their immediate applicability paragraphs, the existing source/positivity/KL sections, and the IP/BIP section through the present end of the draft. Later Grothendieck/final parts were still being written by root and are not included in this review. The snapshot checked near the end had 590 lines and SHA-256 `6763d272a7bfb987193a288bb99240b88791bee6846c81a6a454efda7bbb7742`; the working file can legitimately change afterward.

## Verdict

**No mathematical blocker found in F01–F15 after the F06 grading clarification and F03 exponent typo correction made during review.** Theorems remain conditional where appropriate; none is used to claim general nonstandard positivity, PH1, or a complexity separation. The rank-one cone obstruction is correctly limited to the fixed inclusion and ambient cone. The counterexamples do not purport to refute the specific signed/normalized GCT conjectures.

Two small precision edits remain recommended at this snapshot:

1. **F04:** explicitly say that the error estimate is required for each conjugate trace system in the all-embedding conclusion. Constants and the sublinear η-sequence may depend on σ. The intended interpretation of “same all-embedding duality hypotheses” is correct, but a literal reader should not have to infer that the newly introduced error bound is included.
2. **F12:** put “in an orthonormal basis” in the statement's principal-minor assertion, as already present in the proof. Also the exact stable-dimension condition is `dim V≥ℓ(λ)`, which is preferable to “stable dimension range.”

A copy-edit, not a proof issue: the abstract calls F01 “vector-valued.” Its variables lie in a vector space, but t is scalar-valued. “Multidimensional path-sum estimate” would avoid implying a vector-valued trace function.

## Corrections requested and checked during this review

### F06 grading clarification: resolved

The earlier sentence “one-dimensional Tate piece in grades 0 and 2 with the usual matching Tate weights” was ambiguous: the ordinary cohomological degree sequence (1,0,1) of P¹ does satisfy the usual degree-two Hard Lefschetz theorem. Root has now made the intended normalized grading explicit:

- M_0=Q_l, M_1=0, M_2=Q_l(−2);
- grade j carries weight 2j;
- the perfect pairing M_0⊗M_2→Q_l(−2) gives the graded duality;
- any operator of grade +1 has square zero and cannot satisfy the D=2 isomorphism of F07.

The corrected example is valid. It is an abstract graded Weil object, not claimed to arise from smooth projective cohomology with its Lefschetz operator.

### F03 exponent typo: resolved

The displayed estimate had `Q^{,k(a+d)/2+d/2+1}`. The stray comma has been removed. The exponent itself is correct, as checked below.

## Full proof-by-proof check

### F01 — PASS

Read the complete proof. Orthogonality gives QN=M^k+R for all complex t. With a nondegenerate bilinear form, K_h K_h*=Q^d I for h≠0; symmetry of the bilinear form is not required. The path matrix coefficient has exactly k−1 Fourier kernels and k−2 diagonal multipliers. The row functional t^T has norm ||t||_2 because its Hermitian-dual vector is bar(t). The product bound is therefore

`(Q−1)Q^{d(k−1)/2}||t||_2²||t||_∞^{k−2}`.

The k=2 convention is handled. No scalar sign/nonnegativity hypothesis was smuggled into the proof. The distinction between an open-chain coefficient and a trace of a power is accurate.

For the geometric interpretation later, the pairing should be defined over F_q if one wants all H_k to be fibres of fixed F_q schemes; this is implicit in that interpretation, while the abstract theorem legitimately does not require it.

### F02 — PASS

Read the complete generating-function proof. Distinct nonzero α_j with nonzero grouped coefficients yield actual simple poles at 1/α_j. The nearest-pole radius and Cauchy–Hadamard give the limsup exactly. Coincident roots must be grouped first; the text says so. No simultaneous phase-alignment claim or semisimplicity assumption is used. Finite power traces of Jordan matrices have the asserted eigenvalue form.

### F03 — PASS

Recomputed the exponent:

`d(k−1)/2 +(a+d)+a(k−2)/2 +1 = k(a+d)/2+d/2+1`.

The pointwise rank/weight bound supplies B^k. For each fixed k the n-th-root estimate removes that constant. From (S1) and (S2), `−ε^k R` is the sum of the B_k spectrum and the k-fold product spectrum of A, with positive integer grouped multiplicities. The diagonal k-tuple ensures that α^k survives even if it coincides with another root. F02 then gives the required k-th-root bound, and taking unbounded k removes the overhead.

The order of limits is explicit and correct. The dualizing scalar q^(a+d) is rational because a+d is integral, hence unchanged under all complex embeddings. The all-conjugate hypothesis is stated separately; purity is not deduced merely from one chosen complex embedding. Empty spectral multisets cause no contradiction: the conclusion is vacuous.

### F04 — PASS with recommended clarification above

The rearranged positive spectral sum equals ε^k(E−R), with the sign correct. Its fixed-k exponential rate is bounded by the maximum of the two rates. Since η_k/k→0 and the Parseval overhead is constant in k, taking k-th roots yields the same limiting bound. For the all-conjugate purity statement, apply this same argument after every embedding, including the corresponding error bound. The statement is sufficient, not asserted necessary, and the text preserves that limitation.

### F05 — PASS

Read each example with the claim it refutes:

- constant t on A¹ shows the analytic identity and Parseval alone do not force the claimed middle weight;
- Q_l(−1)⊕Q_l(−1)[−1] has identical eigenvalues in degrees 0 and 1, so all alternating traces vanish;
- eigenvalue 1 distinguishes an upper weight bound from equality;
- {R,−R} defeats an arbitrary odd-degree subsequence;
- the normalized F_3 matrix is non-Hermitian, and the F_2 matrix has a negative eigenvalue;
- the unipotent rank-two Q_l representation is continuous through Z_l and punctually pure but arithmetically nonsemisimple.

The arithmetic/geometric semisimplicity distinction is accurately retained, and no example is presented as a counterexample to the fully stated F03.

### F06 — PASS after explicit grading fix

The rank-one Frobenius −1 example is pure weight zero and has the stated alternating trace. The polynomial v²−1+v^−2 is ≥1 for every nonzero real v and bar invariant, yet not coefficientwise positive. Evaluating at v=1 indeed forces exponent a=0 and the positive overall sign in any hypothesized `±(v−v^−1)^a f`, so the stated signed-factor form also fails for this h. The now-explicit graded Weil example proves that purity plus graded duality alone need not supply the degree-one Lefschetz injections. This example is fully separated from actual smooth-projective Hard Lefschetz geometry.

### F07 — PASS

Read both full arguments. The first is an exact conditional split-K0 argument: an actual finite direct-sum decomposition, together with a basis-preserving graded ring isomorphism, gives nonnegative integral coefficients. The text does not infer that the needed category/isomorphism exists.

For Lefschetz, symmetry follows from the displayed isomorphisms. If j<D/2, the integer D−2j is at least 1. Thus Lx=0 implies L^(D−2j)x=0, and injectivity of the latter map implies x=0. Therefore dimensions increase up to the middle. Symmetry then gives decrease after the middle, including the odd-D equal middle pair. This is a sufficient formal theorem and requires no additional hidden geometric assumption. The finite-dimensionality of the normalized multiplicity pieces is understood in “multiplicity space”; it could be stated explicitly if preferred.

The paragraph after the proof correctly retains rational denominators, signs, vanishing factors, and the correct grading variable before using this for VIII. No efficiency consequence is claimed.

### F08 — PASS

The two-point scheme is finite étale, smooth and projective. K0 is Z² with componentwise product; Frobenius on H⁰ is the identity. The basis determinant is 1, both classes are actual bundles, Gram minors are 2,5,1, and `(1,4)=3(1,2)−2(1,1)` is exact. Componentwise λ-operations are correct. The scope caveat prevents this from being mislabeled as a refutation of a specified GCT basis.

This proof originated partly in this reviewer's earlier notes, so this event is a targeted recheck of the root's presentation, not an independent re-proof by a new author.

### F09 — PASS

Checked the full ring computation and the exact source normalization. Writing b=c−δ gives cb=0 and b²=−δb; hence P²=δ²P. The displayed ambient expansion gives linear independence of 1,P over the Laurent domain. If 2b is coefficientwise nonnegative then b is; multiplying a nonzero such b by δ gives a nonzero nonnegative polynomial, incompatible with the simultaneous coefficientwise nonnegativity of −δb. Thus the cone intersection is exactly the scalar cone.

The categorical consequence follows for the fixed split-K0 character map and the actual-object cone assumed. It is not extended to arbitrary derived realizations or other hearts. Internal multiplication remains positive, and the text correctly says this is not a counterexample to VIII's signed normalized assertions. The §3.1 convention and §11.1 printed slip are recorded transparently.

This is again a targeted recheck of a proof contributed by this reviewer earlier, not a new independent re-proof.

### F10 — PASS

Read all three parts. The exclusive positive monomial coordinate argument works because the subalgebra structure constants already lie in R and division by a positive monomial preserves R_+.

For the disjoint-support counterexample, B=R×R[t]/(t²−c) is free with basis 1=(1,1), x=(0,t), y=(0,1). Its positive multiplication table is correct. The submodule with basis 1,x,z=py is closed under multiplication, because `x²=hz`, `xz=px`, `z²=pz`; it is free since p is nonzero. Its generic algebra equals B after inverting p and is semisimple since t²−c is separable over Q(v). The identity `(v+v^−1)(v²−1+v^−2)=v³+v^−3` is exact. All indicated coefficients are bar invariant.

The final example over Q[v], rather than the Laurent ring, correctly shows that disjoint supports only modulo v do not imply global positive multiplication. Expanding `(x+v)²` using x²=x gives precisely `(1+2v)b1−v(1+v)b0`.

### F11 — PASS in its stated illustrative sense

The virtual λ and γ identities are correct. The example proves that formal λ-operations on a virtual class do not preserve the effective representation cone; it is not used to claim that no extra theorem involving λ-operations could ever prove positivity. In M₂(F_p), A^p=B^p=0 and (A+B)^p is nonzero, so the p-th-power formula fails additivity. The text explicitly leaves separately constructed categorical/quantum Frobenius open.

### F12 — PASS, statement precision edit recommended

Read the projector proof and both representation identifications. Averaging a unitary finite-group representation gives an orthogonal idempotent onto invariants. Gram determinants are nonnegative in an orthonormal basis, exactly as the proof states. The Kronecker triple-invariants formula uses self-duality of Specht modules correctly. For plethysm, the subgroup `(S_n)^d⋊S_d` acts on d blocks of size n, and Schur–Weyl gives `aλ(d[n])=dim[λ]^H` when `dim V≥ℓ(λ)`.

The source applicability is precise: BIP Proposition 3.3 and equation (4.1) give these constructions; Proposition 4.5 gives a spanning family, not an independent basis; Theorem 4.7 includes signed evaluations. The subsequent Gram-minor identity characterizes rank and does not assert a polynomial-time algorithm or an inherent hardness theorem.

This descends from the reviewer's earlier T-PROJ contribution and is a targeted recheck.

### F13 — PASS

Read the full additive-functor induction. Finite direct sums at each of finitely many stages ensure a finite path sum. Split semisimplicity identifies the final simple multiplicity. The lattice-point assertion additionally includes boundedness, so a polytope rather than merely an unbounded polyhedron is obtained. No polynomial bound on its description or witness size is inferred; those requirements are explicitly retained later.

The S4 explanatory decomposition is correct. The permutation action on three pairings factors through S3 and splits into the trivial plus the two-dimensional Specht representation. The listed character values and their squares give exactly trivial+sign+[(2,2)]. This does not purport to rule out a correctly identified different theta chain.

This descends from the reviewer's T-PATH and is a targeted recheck.

### F14 — PASS

The characteristic-polynomial factorization for a stable subspace and quotient proves the first assertion in every embedding. Eigenvalues of the induced endomorphism action are all α/β even in the presence of Jordan blocks, so weight zero follows. No semisimplicity is needed. The following paragraph correctly notes that Frobenius stability, grading and the actual target identification are additional inputs.

This descends from the reviewer's A-SUB and is a targeted recheck.

### F15 — PASS

Read the full scheme-theoretic construction. The orbit map gives a homomorphism of finitely generated Z-algebras. Its kernel defines a finite-type quotient. The image is a subring of Z[GL_N], hence torsion-free as a Z-module; over the PID Z this is flat, including for a module not finitely generated over Z. Flatness of C preserves the kernel, and the resulting image is a subring of C[GL_N], a reduced domain. Thus the complex fibre is the reduced scheme-theoretic orbit closure.

The explicit refusal to identify every mod-p fibre with the orbit closure of the reduced tensor is necessary and correct. The projective follow-up is qualified as homogeneous. The P¹ line-bundle and G_m-linearized-point examples prove exactly the loss of polarization/linearization data asserted. The coherent-section saturation/degree caveat prevents a false all-degrees identification between a graded coordinate ring and H⁰ of Proj. No Riemann–Roch contradiction is alleged.

This descends from the reviewer's A-ORBIT/A-HILB and is a targeted recheck; root added the torsion-free/flat observation, which was checked here independently.

## Exact IP Theorem 1.10 verification

Re-read the complete attached statement at source lines 409–421, label `thm:secondmain`, and previously matched it to arXiv 1512.03798v2, Theorem 1.10.

The statement begins with d,n∈N and λ⊢dn. Its part (a) is genuinely universal under those hypotheses:

`bar λ∈{(1),(1,1),(1^4),(1^6),(2,1),(3,1)} ⇒ aλ(d[n])=0`.

No m-bound, long-first-row condition, or large-d/n hypothesis belongs to part (a). They occur exclusively in part (b): there exists m≥3 such that length≤m², tail size≤md, d>3m³, n>3m⁴, and the tail is outside the exceptional set. The paper's current transcription is correct.

The adjoining IP statements are numbered correctly for the attached version: strategy Theorem 1.4, no-zero obstruction Theorem 1.6, shape constraint Theorem 1.8. BIP's main theorem is correctly numbered 1.4 in the attached v3, and its multiplicity comparison is correctly attributed to §1(c). The distinction among orbit-closure multiplicities K_n, symmetric rectangular orbit multiplicities sk_n, and ordinary g_n is retained.

## Source applicability and efficiency audit

The paper consistently avoids these invalid upgrades:

- a complex-analytic RH theorem ⇒ a finite-field nonstandard realization;
- pointwise spectral purity ⇒ Tate stalks or coefficientwise positivity;
- scalar positivity or Gram positivity ⇒ a specified canonical basis;
- an abstract path count ⇒ #P membership with polynomial witnesses;
- an abstract positive basis ⇒ PH1's particular Ehrhart/separation-oracle package;
- existence of a positivity algorithm ⇒ existence of permanent/determinant multiplicity obstructions;
- an algebraic complexity obstruction ⇒ Boolean P≠NP.

The source audit's detailed VIII signs and normalizations matter to these conclusions and are used appropriately. The paper does not assert that the proposed nonstandard RH has been formally stated by the four supplied papers.

## Check-event semantics

This review is an independent reading of the root's current paper, but some proofs originated in this reviewer's earlier contribution. Therefore record these events as **targeted proof check** or **used and rechecked in this run**, not indiscriminately as “independent re-proof.” No Lean/kernel verification or external formal certificate was performed. The complete proof texts, not only statements/headings, were read.

## Final-text review addendum: F12/F13, F16/F17, Section 9, Parts III/IV

**Snapshot and scope.** Fresh review on 2026-11-21 Europe/Berlin, approximately 00:30–00:39 (UTC 2026-11-20 23:30–23:39), of the completed draft. The first completed snapshot read had 774 lines, SHA-256 `efbc46e346b8e448607c48ad2d75c3e27095b302cd972f0632e0bd912b1e1238`. Corrections made during review were then re-read; the resulting snapshot had 778 lines, SHA-256 `0dc0fec4deaf39a4761997d7bd168b86f247f897cd5705eb81c3d6a4159686bb`. The root is continuing to add findings afterward; these hashes are historical scope anchors, not a claim that the working file is frozen.

Read the complete final proof texts of F12, F13, F16 and F17, the full rectangular section, and the complete mathematical discussion in Parts III and IV. Also re-read F03/F04 and F09 where needed to check the new dependent arguments. Part III was checked for mathematical applicability and distinctions; this reviewer did not newly inspect the archival manuscript images or independently prove SGA/BBD background results. The full revised-IV §18 two-row formula and its immediate proofs were inspected in the attached source and matched to numbered statements in the primary PDF.

### Verdict and resolved clarifications

**No mathematical blocker found in this final-text scope.** The prior F04 all-embedding clarification, F12 orthonormal-basis statement and exact dimension hypothesis, and abstract “multidimensional” wording are present and correct. F16 now correctly distinguishes its Tate-degree sequence `(1,2,1)` from coefficients in consecutive powers of v, `(1,0,2,0,1)`. It makes no unsupported transfer of this normalization to VIII's unimodality claim.

A small integral-model clarification was requested for Part III and applied: the projector's model over Z[1/|H|] is stated for the integral Specht/tensor representations used in the GCT instances. An arbitrary complex representation in F12's opening statement need not descend to Q. The standard integral Specht lattices do, so averaging after inverting the group order gives exactly the finite locally free direct summand asserted in the application.

### F12: projectors and Gram ranks — PASS

The averaging calculation proves Hermitian idempotence for a unitary representation. In an orthonormal basis, the principal submatrix has entries `(P e_i,P e_j)` because P is self-adjoint and idempotent, so the principal minors are Gram determinants. The rank equals the invariant dimension. For triple Specht tensors the self-dual character identification gives g; for plethysm, the actual subgroup `(S_n)^d ⋊ S_d` acting on blocks is the correct one, and Schur–Weyl comparison is valid once `dim V ≥ length λ`.

The subsequent sum of Gram minors detects rank at least r because an r-fold wedge is nonzero exactly for an independent r-tuple. This proves a rank-detection identity, not a method to select a basis efficiently, not a specified canonical basis, and not a stretching/saturation property. The paper states all of these limits accurately.

### F13: exact branching framework — PASS, with the existence gate essential

Finite direct-sum decompositions can be propagated through the exact additive functors. Products of 0/1 entries count paths, and semisimplicity identifies the coefficient with a multiplicity. The polytope assertion applies when the path labels are the integral arrays specified in the statement; boundedness makes the feasible region a polytope. No identification of these functors or endpoints with the actual theta/GCT data is proved or claimed.

An exact count by a polytope for each fixed input does not alone give an Ehrhart family under stretching: one must additionally prove a uniform coordinate/lattice identification and the required homogeneous dependence on the input. Nor does a rational polytope imply the support property `h(Nu)>0 ⇒ h(u)>0` on the original label lattice; this is distinct from VI Definition 1.2.4's residue-wise terminology. The paper's gate P retains the dimension, bitlength, separation, Ehrhart and index obligations, so it does not make either upgrade.

There is a stronger limited deduction, developed separately in `agent_theta_saturation.md`: homogeneous **integral difference/order constraints with no extra conditions** force saturated support by coordinatewise flooring. The explicit pair `g((1,1)^3)=0`, `g((2,2)^3)=1` therefore excludes that particular model even for two-row rectangles. This is not an objection to F13 or to general GGP chains. The two-row positive crystal formula in revised IV in fact includes parity and invariant-removal data outside this model.

### F16: a different positive rank-one inclusion — PASS

The abstract-algebra argument is exact: both algebras are free of rank two with presentation `R[z]/(z²−δ²z)`, and the map sending P to E is an isomorphism. The Tate cohomology dimensions of P¹×P¹ give `v⁻²(1+2v²+v⁴)=δ²`. At v=1, `P=2(1+s⊗s)` and `E=(1+s)⊗(1+s)` act by 4 and 0 respectively on sign⊗sign. Hence the map does not preserve that ambient representation under the specified generator comparison.

The conclusion is properly limited to a changed algebra inclusion. It is not a categorification of all VIII coefficients, and it does not prove that the ungraded cohomology is pure of a single weight. The updated grading warning closes the possible ambiguity about ordinary coefficientwise unimodality.

### F17: full multiples and separate dual spectra — PASS (fresh proof check)

Fix k and substitute n=e_k r. The spectral sequence in r contains `(α^k)^{e_k}` with a positive multiplicity. Different roots may merge after powering, but their coefficients add positively, so the roots relevant to the bound cannot cancel. The bound has exponential base `(q^{e_k})^{k(a+d)/2+c_k}` with `c_k=d/2+1` or the F04 maximum. Taking the `(e_k k)`th root removes e_k exactly; the k-limit is unchanged. A prefactor polynomial in e_k r remains subexponential in r for fixed k. The requirement of all full positive multiples, rather than an arbitrary infinite subsequence, is correctly retained.

For the dual-spectrum assertion, the upper bounds `|α|≤q^{(a+d)/2}` and `|q^d/α|≤q^{(d−a)/2}` give equal opposite bounds. Frobenius invertibility and multiplicity matching are explicit, and rationality of q^d makes the argument valid under every embedding. The geometric paragraph correctly retains the compact-support/ordinary-cohomology comparison needed to construct the asserted pairing. No such pairing is inferred merely from dimension.

### Rectangular Section 9 — PASS

Freshly re-read the attached IP statements and BIP's theorem/comparison context. IP Theorem 1.10(a) has **only** d,n∈N, λ⊢dn and the listed exceptional tail as its hypotheses. Its universality in the paper is correct. The part-(b) bounds, and Theorems 1.4, 1.6 and 1.8, are transcribed correctly. BIP's attached version is Theorem 1.4, with n≥m²⁵, and its coordinate-ring quotient argument gives the stated strict-multiplicity obstruction while excluding occurrence obstructions in that range. The orbit/closure distinction `K≤sk≤g` is retained.

Revised IV's two-row result is correctly restricted to the two factors of length at most two, with the ambient GL₄ label of length at most four. The full formula in Theorem 18.2 and equation (172) provides a useful further check: its rectangle-ray specialization is `g((d,d)^3)=1` for even d and zero for odd d. This is an existing positive-formula consequence, not a new theta result. It has the exact rational Ehrhart model `P={1/2}`; its arithmetic denominator explains why an exact rational model and failure of support saturation are compatible. In VI Definition 1.2.4 (printed p.14), this parity quasipolynomial actually has saturation index zero, since its nonzero residue polynomial is the constant 1. It is not a counterexample to VI's residue-wise notion of strict saturation. This model covers that ray only and supplies no general-height rectangle or closure-multiplicity formula.

### Parts III/IV — PASS within the stated framework scope

The representation-K0 dictionary uses effective irreducible classes only in characteristic zero and keeps integral/modular failures of semisimplicity separate. Its λ-ring discussion correctly distinguishes virtual and actual classes, K0 from G0 on singular schemes, and Euler pushforwards from section modules. The trace determinant is the alternating one; its logarithm has the stated trace signs. The distinction between a pure complex and exact singular-stalk Tate weights is correct.

The motives paragraph does not assign an unjustified Chow motive to an arbitrary singular orbit closure or a quantum algebra. F15's ordinary IC purity remains separate from coherent section multiplicities. The archival table is carefully labeled a reading of selected leaves, not a fresh proof of complete manuscript theorems; verification of those scans belongs to the dedicated archival audit.

The gates R/S/E/L/C/P/O remain sufficient research conditions, not assertions of existence or necessary-and-sufficient characterizations of every possible route. In particular F04's spectral error budget is not identified with VIII's coefficient-vector correction bound; revised-IV Kronecker duality is not left conjectural; PH1 is not equated with #P membership; and efficient formulas do not by themselves yield an asymptotic multiplicity obstruction. The final INCOMPLETE status therefore matches the actual mathematical scope.

**Event labels:** fresh whole-proof checks for root-added F16/F17; targeted rechecks for F12/F13 and prior contributed lemmas; source-statement/application checks for IP/BIP and revised IV; mathematical framework review, not archival-image re-verification, for Part III. The separate new difference-polytope proof is author-checked pending another reviewer.

## Subsequent complete-text checks: F18–F20 and F21/F22/F25

The F18–F20 snapshot reviewed in full had 955 lines and SHA-256
fa7a864670d6afcb6d791da0557d9ce8661de42c953baf8931f7fc4f0fcc0296.
All three findings, their complete proofs, and their following scope paragraphs were read and re-read after the earlier clarification cycle. Verdict: PASS.

For F18 the flooring proof retains integral endpoints, homogeneous dependence, a fixed constraint list and the exclusion of additional equations/congruences. The exact S2/S4 character argument, whole parity ray, rational-point model, VI residue-wise saturation distinction, IP-region limitation and representation-K0 restatement are correct. This is a targeted check of this reviewer's contribution, with a separate independent review recorded in REVIEW_THETA_SATURATION_GCT.md.

For F19 the two-idempotent central parameter, central Chinese remainder decomposition, four matrix generators, unit conditions and root collision proof agree with the independently reviewed rank-three report. The specialization argument correctly identifies the radical as the kernel of the actual ambient map. The coherent End model explicitly uses trivial bundles, while the constant-sheaf replacement is described as a chosen replacement. The obstruction to full End of a semisimple object is correctly distinguished from an action by a nonsemisimple subalgebra.

For F20 the perverse purity and primitive Schur-idempotent image use the actual symmetric Satake category. The canonical isotypic evaluation map, with Frobenius on the Hom factor, is the correct descent mechanism; restriction on the support's own smooth open gives the stated weight difference. This does not require arithmetic semisimplicity. The product-group application gives the Kronecker dimension and weight in the stated dimension bounds. The two-step GL2 fiber is P1, its H2 supplies the determinant multiplicity, and intermediate-extension strictness removes a competing degree-zero boundary contribution from the open IC. The modified symmetry acts as the tensor swap and therefore negates this line. The claim rules out an unsigned permutation basis, while the later F23 provides the stronger signed-basis example.

The subsequent 290-line insertion finding_F21_F22_F25.tex was reviewed in full at SHA-256
0f7f028df041b91e0fa7e0a00eec10412e4b63795b386c94971574353d2a6f1b.
The containing main-paper snapshot had 1380 lines and hash
168675a390886383f73f88c4b65d17d97e24c349d444c8a50de395bd2424feb8.
These events cover that insertion, not every other newly added section in that larger snapshot. Verdict: PASS, with detailed exact scope, report hashes, matrix checks, Ext calculations, étale comparison and trace-normalization review in REVIEW_R3_TENSOR_THETA.md. No mathematical blocker was found.

## F23 final-text match

The entire finding_F23.tex fragment was read and compared with the complete note agent_satake_projector_gate.md, which had independently passed the Grothendieck agent's full mathematical review. The corrected fragment has 144 lines and SHA-256
663c18798b6348336533988585837c86127f7c7c20d8d0c41a77c7d62ee58600.
The containing paper snapshot at this check had 1574 lines and SHA-256
ca83a1cdde354ddd82bc7ec1ae42dac5a58d8d7ca8acc64d0512cb83af466690.

Verdict: PASS after one restored encoding hypothesis. The fragment now expressly requires a polynomial-time procedure computing Young block sizes and trivial/sign types from the orbit label; their short descriptions alone would not suffice for the proposed verifier. All signed-induction and primitive-idempotent arguments, the degree-three GL2 flag geometry, the precise signed-versus-general-monomial caveat, the classical Hermite/Clebsch–Gordan application and the VI residue-wise saturation qualification match the checked report. This is a targeted final-text check of a prior contribution, not a new independent proof of its entirety.

## F26 final-text match

The complete 112-line finding_F26.tex fragment was read at SHA-256
a4f8b3b8d61b8b7be218a5245704b6cc63e45440cc54c3d73e4f85d7c94d8bf7.
The containing main snapshot has hash
3734a73ffdc824560d0c34d37ce31bd1b9d71be9feb091230d15f42f5b2c8a7f,
with exact text containment confirmed. Verdict: PASS. The global convention that q is a prime power supplies q>1. The actual trace, recurrence/maximal-pole argument, fixed finite-cohomology contradiction and deliberately limited normalized-word dictionary agree with the independently reviewed report. Complete check details and the independent algebraic reconstruction appear in REVIEW_R3_TRACE_THETA.md. This event does not certify all other intervening additions to the main paper.

## Final-text checks of F28 and F32

The main-paper snapshot at this check had SHA-256
807a3a251dff4f177bfb61171aec5181a67e86161f52b4d0b8dea4bb4efd8996
and 2804 lines. The following complete fragments each occur exactly once as identical text in that snapshot. This is a scoped check of those fragments, not a review of every other addition to the larger paper.

### F28 — PASS after two boundary qualifications

The complete 132-line finding_F28.tex fragment was read and compared with the independently checked generalized rectangular report and Manivel application. Final fragment SHA-256:
9813ba2b376659885cf2eb873f8a09e834ab6d6e877cf7e61fbe362c42510834.

Its isolated-hook proof, arbitrary scalar-phase character reduction on Young stabilizers, effective decomposition argument, every nontrivial rectangle via the IP hook product, size-four edge case, actual Schur–Weyl multiplicity identification, non-Young signed model, and known Manivel polynomial algebra/exponent rule are all correct. The final text now restricts the adjacent-two-hook identity to \(1\le j\le a-1\) and the concluding exclusion in the height-two application to \(d\ge2\). These two qualifications avoid boundary overstatements; the theorem itself was already correctly restricted to nontrivial rectangles. The singleton convention is explicit. The denominator-two point model and its limited scope agree with the source. This is a targeted final-text match of this reviewer's contribution, whose full independent review is in REVIEW_RECTANGULAR_HOOK_GCT.md.

### F32 — PASS

The complete 160-line finding_F32.tex fragment was read and compared with the fully independently checked countable-spectrum report. Fragment SHA-256:
44165a8b32ba3d9d9ebb2492abe89354530fe3fd06cac92b0ea5d4fd8ed50c6f.

The full normal-convergence/pole proof, moment convention, uniqueness, finite tensor grouping, real signed even-power argument, fixed-k-before-unbounded-k order of limits, powered-root visibility, separate all-embedding assumptions, bounded reciprocal-support finiteness, integer-coefficient refinement and explicit F26 completion are preserved correctly. The statement about tensor products follows by the same displayed finite-tuple bound and product moment estimate for factors with a common maximum radius and common moment. The completion does not purport to construct the required pointwise/path identities. Neither regularized nor non-atomic traces are excluded. The separate fresh full report review and independent outer-circle/Cesàro proof are in REVIEW_COUNTABLE_SPECTRUM_THETA.md.

