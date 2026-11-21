# Independent direct review of the generated paper, sections 1–9

Reviewer: `/root/gct_statements`, GPT-6 Astra Pro. Reasoning effort inherited/not exposed by the runtime. Review date: 2026-11-21 (Europe/Berlin); clock check during this review returned 2026-11-20 23:24:03 UTC. This is a mathematical/source review, not proof-assistant verification.

## Reviewed artifact and scope

I read the generated `/workspace/scratch/b5024d19aacd/GCT_NSRH_work/GCT_NSRH.tex` directly, including every statement and proof F01–F15, the surrounding source reconstruction, the KL normalization, the theta discussion, the orbit-model arguments, and the rectangular results through the last paragraph of section 9. This was not a review of the earlier agent memos alone.

A snapshot of the reviewed first nine sections is `REVIEW_PAPER_GCT_sections1_9_snapshot.tex`, 574 lines, SHA-256:

`2facb6b557141a33f83c7e930cd75c93c4c99395f0e6d403505925874d5d8532`.

The paper is being extended and corrected concurrently. The check events below apply to this snapshot, with the explicit qualifications listed. A later pass can match the corrected text and record resolution rather than silently describing the original wording as already corrected.

## Outcome and changes requested

**No substantive counterexample to F01–F15's intended mathematical conclusions was found.** The path sign criterion remains conditional on its strong spectral hypotheses. The new algebraic, categorical, projector and orbit-model deductions are valid. Two hypotheses should be made explicit, and a displayed typo should be corrected before recording an unqualified final pass.

| Location | Finding | Required action/status |
|---|---|---|
| F03, `eq:overhead` | The exponent is printed `Q^{,k(a+d)/2+d/2+1}`. | Delete the stray comma. Pure notation typo; the exponent calculation and proof are correct. |
| F04 | The all-conjugate claim inherits “the same all-embedding duality hypotheses,” but the modified identity and the boundary estimate should explicitly hold for each embedding's system. A bound on one embedding's error is not a bound on its conjugates. | State the modified hypothesis and estimate for every embedding, permitting constants to depend on the embedding and requiring the corresponding overhead divided by k to tend to zero. The proof then passes. |
| F12 | “A unitary representation U” does not explicitly say finite dimensional or complex, though its finite trace/rank is used. | State “a finite-dimensional complex unitary representation.” All applications here already satisfy this. |
| F06, final example | “Usual matching Tate weights” leaves the grading convention implicit. | Recommended explicit example: M_0=Q_l, M_1=0, M_2=Q_l(-2), with grade j tracking Tate exponent j and pairing M_0⊗M_2→Q_l(-2). The current intended counterexample is valid. |
| F10, generic semisimplicity | Separability proves that B_K is semisimple; the intended assertion also concerns A_K. | Add the short bridge that p≠0 becomes invertible in K=Q(v), so A_K=B_K. This is a readily supplied step, not a failed conclusion. Prefer “R-free subalgebra” to the ambiguous “free subalgebra.” |
| Section 9, source convention | Both attached IP and BIP use padding X_11^(n−m)per_m, and the length bound m² matches that convention. The paper currently says only “padded permanent.” | Recommended: display that padding and the ambient Sym^n V* convention explicitly. This prevents accidentally importing the extra-independent-variable convention with its different immediate variable count. |
| Section 3, IC notation | The intended expression is unshifted IC. | For readability write `(j_{!*}(Q_l[ell(w)]))[-ell(w)]`; this removes any possible ambiguity about the domain of perverse intermediate extension. The stated formula is otherwise correct. |

These points were sent to the root as they were found. The F04 and F12 clarifications concern formal scope; they do not require replacing either argument.

## F01–F05: final-text match and proof checks

### F01: PASS — complete targeted proof check; earlier independent reconstruction retained

The exact orthogonality identity and the open-chain matrix coefficient were reread in the generated TeX. For a nondegenerate square bilinear pairing, summing over the second variable gives K_hK_h*=Q^d I. No symmetry of the pairing is needed. The row t^T has operator norm ||t||_2 even for complex t. There are k−1 Fourier kernels and k−2 diagonal factors, so the displayed estimate has the right exponents, including k=2. The text correctly distinguishes the open path from a closed trace moment.

### F02: PASS — complete targeted proof check, plus earlier independent Cesàro re-proof

Every pole 1/alpha_j is genuine after distinct roots have been grouped with nonzero total coefficients. The resulting radius and Cauchy–Hadamard formula prove the stated limsup. R>0 is now explicit. The empty spectrum and vanishing regrouped coefficients are handled. Semisimplicity is not required. The earlier audit's Cesàro argument independently confirms this exact statement.

### F03: PASS modulo displayed comma — complete targeted proof check

Combining the pointwise bound with F01 gives

`d(k−1)/2 + (a+d) + a(k−2)/2 + 1 = k(a+d)/2 + d/2 + 1`.

The sign identity makes the B_k roots and all products of A roots occur with positive integer multiplicities. Therefore alpha^k survives regrouping. Taking n→∞ for fixed k removes B^k; then unbounded k removes (d/2+1)/k. The finite root multisets need not be disjoint or have real eigenvalues.

The final TeX retains integer a and prime-power q>1, so q^(a+d) is rational and fixed by every embedding. The compatible per-embedding trace systems now make the all-conjugate proof legitimate. A fixed reciprocal Tate multiset duality supplies the lower bound. The old arbitrary-algebraic-scalar gap is resolved in this theorem.

### F04: PASS with the explicit per-embedding error condition above — complete targeted proof check

For fixed k, polynomial factors in n and constants depending on k disappear from the nth-root growth rate. The positive spectral sum is epsilon^k(E−R), with exponential rate bounded by q^[k(a+d)/2+max(d/2+1,eta_k)]. Division by k removes the excess. The current sentence correctly calls this a sufficient budget, not a necessity theorem.

For the all-conjugate conclusion, this calculation must be repeated for each embedding with a valid error estimate there. This should be stated as a hypothesis, rather than inferred from a bound for the original complex embedding.

### Geometric explanation following F04: PASS — complete targeted reading

Concentration in degree d gives epsilon=(−1)^d; concentration in kd−1 gives the opposite sign −epsilon^k. A twist (−1) multiplies geometric Frobenius by q^n. The passage correctly keeps concentration, comparison of compact-support cohomology with its dual, and boundary terms as hypotheses. Dimension of the hypersurface does not prove the required concentration. No assertion that schemes are the only possible realization is made.

### F05: PASS — all six countermodels checked in full

The constant trace has eigenvalue q instead of the proposed sqrt(q); the alternating pair cancels with the cohomological shift as written; the smaller-weight eigenvalue illustrates lack of a lower bound; odd extension degrees miss {R,−R}; the Fourier matrices are unitary but not positive semidefinite; and the l-adic unipotent representation is continuous, pure in eigenvalue weight, and not arithmetically semisimple. The arithmetic/geometric distinction is preserved.

## F06–F11: positivity, grading and the actual inclusion

### F06: PASS — complete targeted proof check

The pure rank-one sheaf with Frobenius −1 has the indicated alternating numerical traces. The bar-invariant h(v)=v²−1+v^−² is at least 1 at every nonzero real value while its middle coefficient is negative. Since h(1)=1, a nonnegative Laurent f cannot repair it by a positive power of v−v^−1 or an overall minus sign.

The graded sequence (1,0,1) has symmetry and a compatible Tate-valued pairing but fails unimodality. It is correctly identified as an abstract graded Weil object, not the cohomology of a smooth projective variety. The suggested explicit pieces above resolve the only notational ambiguity. The counterexample concerns purity in each grade; it does not claim that the direct sum of different weights is pure of one weight.

### F07: PASS — complete targeted proof check

The premise is strong enough: actual finite direct-sum decompositions in a split semisimple category, grading shift matching v, and an isomorphism carrying the designated classes to the specified algebra basis. These hypotheses force nonnegative integer structure constants. A merely abstract algebra isomorphism without the basis condition would not suffice, and the statement includes the necessary basis condition.

For the Lefschetz part, if j<D/2 then D−2j is a positive integer. Lx=0 implies L^(D−2j)x=0, hence x=0 by the assumed isomorphism. This gives the increasing half; the same isomorphisms give symmetry. The normalizations and grading-step qualification after the proof are essential and correct. Finite-dimensional multiplicity spaces are understood; making this explicit would be harmless.

### F08: PASS — complete targeted proof check

The two rational points are finite, smooth and projective. K0 is Z² with componentwise product. The two effective rank vectors form a unimodular basis, the Gram determinant is 10−9=1, and b_2²=3b_2−2b_1. The componentwise lambda operation is correct. This demonstrates failure for a chosen effective basis; it does not claim that no positive basis exists.

### F09: PASS — independent re-proof matched to final TeX and targeted source check

With b=c−delta, cb=0 and b²=−delta b. Thus P²=delta²P. The coefficient of c⊗c in P is 2, proving independence from 1 over Z[v±1]. For a+bP, positivity of 2b forces coefficientwise b≥0; positivity of −delta b then forces b=0. Therefore A∩C_+=R_+1. The internal basis remains positive.

The categorical consequence is correctly conditional on an actual-object character taking values in this specified ambient positive cone and inclusion. Additive group completion cannot enlarge its image beyond R1 if every actual object has character in R_+1. This does not prohibit virtual/derived objects, a different basis or an abstractly isomorphic positive algebra.

The exact IV convention warning is retained. In the attached source, §3.1 has `(T_s−q)(T_s+q^−1)=0`, C'_s=T_s+q^−1 and C_s=T_s−q. The start of §11.1 reverses the exponents but keeps an incompatible idempotent assertion. Definition 11.1 and equation (93) give the symbolic generator. The generated proof uses the consistent §3.1 convention explicitly, so it does not silently inherit the slip.

### F10: PASS — independent re-proof matched to final TeX

The exclusive positive monomial coordinate proves the positive-pivot criterion by direct coefficient extraction. Pairwise global disjointness is not required.

In the countermodel p h=c, the ambient table is associative because it comes from the product/quotient algebra. The subalgebra is closed with x²=h z, xz=p x, z²=p z. Its designated basis has disjoint positive supports. The negative coefficient cannot have VIII's signed-positive factor form, by F06. Separability makes B_K semisimple, and p invertible makes A_K=B_K. Bar invariance holds because p,h,c are fixed by v↦v^−1 and the named basis vectors are fixed.

The Q[v] example expands exactly as b_1²=(1+2v)b_1−v(1+v)b_0, proving that local disjointness modulo v is weaker still. VIII 2.2's assertion is in L_alpha/qL_alpha, whereas its globalization and external expansion are separate. The paper does not claim those local supports furnish the pivots. This is the right source interpretation.

### F11: PASS — complete targeted proof check

The lambda-series quotient has coefficient lambda²(z−1)=1−z, outside the effective cone. Substitution t/(1−t) gives gamma_t(z−1)=1+(z−1)t. These formal identities preserve no automatically chosen positive cone. For the matrix example, e_12^p=e_21^p=0 and (e_12+e_21)^2=I, so the displayed pth powers prove nonadditivity for every prime p. This only rules out that automatic Frobenius formula; separately constructed quantum/categorical Frobenius is expressly allowed.

## F12–F15: representations and geometry

### F12: PASS after making finite dimension explicit — complete targeted proof check

Averaging over the finite group gives a self-adjoint idempotent with invariant image. The principal submatrices in an orthonormal basis are Gram matrices of P e_i. Thus their determinants are nonnegative, and trace equals rank. Self-duality of Specht modules gives the triple tensor-invariant realization of Kronecker coefficients.

The subgroup is unambiguously defined as (S_n)^d ⋊ S_d, avoiding variations in the notation for the wreath product. Its invariants in V^(⊗dn) are Sym^d(Sym^n V), so Schur–Weyl proves the stated multiplicity formula. A precise sufficient stable range is dim V≥ell(lambda). The attached BIP equation (4.1) uses the same subgroup/projector; its own written wreath-product order follows its local convention, so the explicit semidirect product in the paper is preferable.

The Gram-minor identity after the theorem holds term by term by the exterior-product determinant identity. A positive sum is equivalent to rank at least r. The text correctly does not assert that all such rank problems are hard.

### F13: PASS — complete targeted proof check and independent character calculation

Finite additive decompositions multiply multiplicities along a chain and sum over paths. In the stated 0/1 case this counts paths. Given the stated identification of admissible integer labels with integral interlacing arrays, boundedness makes the defining polyhedron a polytope. The theorem does not assert that an arbitrary theta chain is such a restriction chain.

I checked the S4 example directly: the quotient of the three-pairing permutation module by its invariant line has character (2,0,2,−1,0) on the listed conjugacy classes. Its square (4,0,4,1,0) equals that character plus trivial plus sign. The determinant-character versus rectangular-Specht distinction is correct.

### F14: PASS — complete targeted proof check

Characteristic polynomials factor through stable subspaces and quotients, so subquotient eigenvalues inherit all-conjugate purity. On End(V)=V⊗V*, conjugation eigenvalues are alpha/beta even if Frobenius is not diagonalizable; triangularization suffices. Their absolute values are 1 when V is pure. No additional semisimplicity hypothesis is hidden.

### F15: PASS — independent reconstruction of both arguments

Let R_0=Z[W], B=Z[GL_N] and I=ker(R_0→B). Then R_0/I embeds in the torsion-free Z-module B, so it is torsion-free and hence flat over Z. Flat base change from Z to the complex field preserves the injection and the exact kernel sequence. The resulting coordinate ring is a subring of the domain C[GL_N], hence reduced; its defining kernel cuts out the reduced orbit closure. Finite type follows from the finite polynomial coordinate algebra. No equality of the resulting model's special fiber with the orbit closure of the reduced tensor is implied.

The extra example in the reviewed final text is correct: x↦p t is injective over Z but becomes the zero-coordinate orbit after reducing f=p modulo p. The special fiber of the image model remains A1, while the reduced vector's orbit is a point.

For P1 with O(r), h0(O(rd))=rd+1 for r>0,d≥0, whereas ordinary/intersection cohomology is unchanged. On a point, different G_m linearizations give characters z^(rd) with identical underlying Weil cohomology. These are valid counterexamples to forgetting polarization and linearization, not to Riemann–Roch or to a specified equivariant coherent comparison.

The following paragraph is appropriately restricted to homogeneous orbit closures and suitable finite-field fibers. “Normalized intersection complex” should retain a fixed shift/Tate convention; it need not mean that an ungraded total cohomology representation has weight zero. Proper pushforward of a pure complex gives the usual degree-adjusted weights. The paper does not use the ordinary purity statement to infer any coherent multiplicity.

## Source and convention audit for sections 1–3 and 9

### GCT sources

The generated statements match the prior full-context IV/VI/VII/VIII audit. I re-read the exact positivity and PH passages during this review. The signs and half-powers in VIII 2.7/3.4 are retained; general plethysm is described through normalized minimal-polynomial coefficients and corrections. The minimal-polynomial sign ambiguity is correctly presented as an ambiguity rather than a counterexample to the intended conjecture. The distinction between established Kronecker duality in revised IV and conjectural general reciprocity in VII is maintained.

PH1 in the attached VI explicitly includes A independent of lambda/pi and b homogeneous linear in them, polynomial dimension/entry-size controls, and a membership/separation algorithm. The paper matches this. The fixed-mu stretching discrepancy in VI Theorem 1.6.8 is retained rather than silently repaired.

### KL normalization

I read Haines Theorem 2.0.1, the complete relevant §4 discussion of Weil compatibility, and Theorem 5.0.4 in the local primary text. The unshifted IC formula and P_(x,w)(T)=sum_j dim H^(2j)(IC)_x T^j match his conventions. His theorem asserts the scalar eigenvalues Q^j, not merely their absolute values. The generated paper correctly separates geometric decomposition from arithmetic equivariance and notes that the original KL proof did not require the modern decomposition-theorem template.

This review does not independently prove Deligne's or BBD's long theorems. Their use is a source-backed background input, not a new formal verification. The local BBD text contains the cited purity/semisimplicity/Lefschetz numbering and the pure unipotent discussion; the final source ledger should retain the other agent's exact-source verification scope.

### IP and BIP parameters, actions and padding

I read the actual attached source statements and adjacent definitions, not just the paper's theorem list. The first-variable padding X_11^(n−m)per_m appears in both IP and BIP. This is why ell(lambda)≤m² is the stated restriction. BIP explicitly works with points in Sym^n V*, action `(g f)(v)=f(g^−1 v)`, and coordinate degree d equal to Sym^d(Sym^n V). Thus the paper's covariant S_lambda V labels are consistent. The formula should be made explicit to prevent a reader substituting a different padding convention.

The IP exceptional set, strict inequalities n>3m^4 and d>3m^3, and existence of m≥3 in Theorem 1.10 are copied correctly. BIP's n≥m^25 is weak, not strict, as printed. The support implication concerns determinant-closure multiplicities. The separate bounds K_n≤sk_n≤g_n concern the orbit-versus-closure distinction correctly. The graded equivariant restriction surjection under orbit-closure containment gives q≤K in each degree by reductivity. No support theorem is silently upgraded to a multiplicity inequality.

The revised IV two-row scope is retained; it is not presented as arbitrary-height rectangular positivity.

## Additional root proposal F16: independent message-level check

The root proposed an additional positive rank-one alternative while this review was running. I checked the proposed algebraic statement and sent the result, but it was not yet present in the reviewed 574-line snapshot, so this is not a final-text check of F16.

Let E=c⊗c. Then E²=delta²E, and {1,E} is independent. Therefore P↦E defines an abstract R-algebra isomorphism R1⊕RP→R1⊕RE. The latter basis is ambient-positive. At v=1, c=1+s and

`P=2(1+s⊗s)`, whereas `E=(1+s)⊗(1+s)`.

On sign⊗sign the former acts by 4 and the latter by 0, proving that the new embedding does not preserve the fixed GCT action. Finally delta²=v^−2(1+v²)² is the centered Tate Poincare polynomial of P1×P1 when v records ordinary cohomological degree. It describes pure Tate pieces in separate degrees; the ungraded direct sum is not a single weight-zero pure Weil module. In coarse Tate grading its dimensions are (1,2,1), but in consecutive integer powers of v the full sequence is (1,0,2,0,1), which is not unimodal. Do not silently infer VIII's exact unimodality convention. These grading qualifications must remain if the proposed statement is added.

## Additional root proposal F17: independent message-level check

The proposed extension-degree flexibility and dual-system alternative are valid conditional strengthenings. They were checked as a root message, not as final TeX in the snapshot above.

For each fixed k, suppose the sign identity and bounds hold on every degree n=e_k r, r≥1, where e_k is a positive integer that may depend on k. F02 can be applied to the r-power sums. The tensor roots become `(alpha_1⋯alpha_k)^(e_k)`. Hypersurface eigenvalues can be stated directly as gamma_(k,j) over F_(q^e_k), giving gamma_(k,j)^r; no choice of e_k-th roots is needed. Positive coefficients remain positive when powering merges spectral values, so alpha^(e_k k) cannot cancel. The conclusion is

`|alpha|^(e_k k) ≤ (q^e_k)^[k(a+d)/2+d/2+1]`,

which gives the same bound for |alpha| after taking the e_k k-th root. Thus no uniform bound on e_k is required. Boundary-error estimates, when used, must hold for every r in this extension system with the stated sublinear overhead in k. A random infinite subsequence such as the odd extension degrees is not substituted for this full multiples progression.

For the second proposal, an additional spectrum A^D=q^d/A with upper bound q^[(d−a)/2] forces the lower bound q^[(d+a)/2] for A. This works in every embedding because q^d is rational. A nondegenerate Frobenius-compatible pairing to Q_l(-d) gives the stated reciprocal relation. The dual trace system's upper estimate is a separate hypothesis: from a pointwise upper weight a for F alone one cannot infer upper weight −a for F dual. In geometry, the natural H_c/H pairing and any identification needed to put both sides into the sign criterion remain explicit obligations.

Allowance for an extension depending on k removes a possible field-of-definition restriction. It does not itself show that a Bertini construction has the exact path identity or the required cohomological signs.

## Check-event recommendations

- `PAPER-GCT-READ-1-9`: complete direct read of generated TeX, first nine sections, snapshot hash above.
- `F01-F05-FINAL-MATCH`: targeted full-proof check against the generated statements; F03 has only a displayed typo, F04 needs explicit per-embedding error wording.
- `F06-F08-FULL`: targeted full-proof check; PASS with explicit grading clarification recommended for F06.
- `F09-F10-INDEPENDENT`: independent re-proof matched to final text and source convention; PASS.
- `F11-FULL`: targeted full-proof check; PASS.
- `F12-FULL`: targeted full-proof check; PASS after finite-dimensional complex hypothesis is made explicit.
- `F13-FULL`: targeted full-proof check and independent S4 character calculation; PASS.
- `F14-F15-FULL`: complete targeted proof check; F15 orbit model reconstructed independently; PASS.
- `SOURCE-IP-BIP-CONTEXT`: used and rechecked exact attached definitions and statements; PASS. Long research proofs not independently re-proved.
- `SOURCE-KL-CONTEXT`: used and rechecked Haines exact normalization and Weil-compatibility discussion; PASS. Deligne/BBD are cited background.
- `F16-PROPOSAL`: independent proof check of message-level proposed statement; PASS with the graded-versus-total purity qualification. Final-text match pending.
- `F17-PROPOSAL`: independent proof check of extension-progression and paired-dual-spectrum strengthenings; PASS with the distinct dual estimate and full progression hypotheses. Final-text match pending.

Do not label any of these checks Lean/formal verification or computer algebra verification. None was used for this review. The reviewed snapshot and this memo are audit artifacts; the root paper was not edited.

## Final complete-text pass, 2026-11-21 00:34 Europe/Berlin

The complete generated `GCT_NSRH.tex` was read directly again after Parts III and IV and F16/F17 were added. All statements and all proofs F01–F17 were reread in their final context. The final paragraphs changed during the review were then read separately, including F04's embedding clause, F06's explicit grading, F10's generic-field sentence, F12's finite-dimensional/orthonormal/stable-range clauses, F15's IC normalization, F16's grading caution, F17's independent dual bound, and the integral representation qualifier in Part III.

The resulting complete snapshot is `REVIEW_PAPER_GCT_full_snapshot.tex`, 775 lines, SHA-256:

`40895819254968296f0571a666cc18dad1b7ceec491e8bd3b1ca82e04901534f`.

Clock time at the hash capture was 2026-11-20 23:34:26 UTC. The model and non-exposed effort metadata are unchanged.

**Final outcome for this snapshot: F01–F17 PASS as conditional statements/counterexamples with their displayed hypotheses. No mathematical blocker remains from this review.** This does not mark the nonstandard realization or the overall research task complete.

### Resolution of previous observations

- F03's exponent comma is removed.
- F04 expressly requires the modified identity and appropriate error estimate for every embedding.
- F06 specifies M_0=Q_l, M_1=0, M_2=Q_l(-2), the weights, pairing, and the degree-one Lefschetz failure.
- F10 expressly notes A_K=B_K because p is invertible.
- F12 specifies a finite-dimensional complex unitary representation, orthonormal basis for principal minors, and dim V≥ell(lambda).
- Section 9 explicitly specifies X_11^(n−m)per_m padding.
- F16 explicitly distinguishes Tate-grade dimensions (1,2,1) from consecutive-v dimensions (1,0,2,0,1), and does not infer the source's precise unimodality convention.
- F17 explicitly says the dual upper bound is independent of the original pointwise upper bound. Its extension-degree and dual-pairing proofs were both checked in full in the final text.
- An additional issue found in Part III was repaired: an arbitrary complex finite-group representation need not descend to Z[1/|H|]. The final paragraph now uses the integral Specht/tensor models in the actual applications and permits a more general coefficient ring carrying a representation. The averaging-idempotent argument then applies correctly.

### New full-text checks

F15's precise post-proof normalization is sound: on a reduced equidimensional projective finite-field scheme of dimension e, `(j_!* Q_l[e])[-e]` is a pure complex of weight zero, and its proper hypercohomology IH^i is pure of weight i. This assertion does not say every singular stalk has exact weight equal to its degree; Part III explicitly distinguishes these notions. The harmless optional parenthesization recommendation for IC notation remains stylistic rather than a mathematical blocker.

Part III's K0/G0 distinction, virtual lambda identities, group-completed trace/zeta identities, and restrictions on motive language are consistent with the proved examples. The zeta formula is read for the finite-dimensional Weil complex delivered by RΓ_c (or an equivalent finite Weil complex); it is not a product of determinants of infinite-dimensional spaces. The source/archive locators in Part III were read as statements of the other agent's recorded source audit. I did not independently visually re-read all the archival manuscript leaves during this final proof pass, and this event must not be described that way.

Part IV's seven gates are explicitly additional hypotheses, not asserted constructions. Its short #P observation is correct when the counted labels/witnesses have the specified unique polynomial-length encodings and uniform polynomial-time tests: guessing the triple counts the sum of products. No claimed #P rule or PH1 follows without those hypotheses. The final state appropriately remains INCOMPLETE.

The exact GCT claims in Parts I and IV continue to match the audited versions: no specified finite-field NSRH; signed/normalized VIII targets; separate basis/cell/globalization and effective-label gates; revised-IV Kronecker duality already proved; general VII reciprocity still conjectural in that source; VI fixed-mu stretching convention preserved. No new source mismatch was found.

### Final check-event classification

`PAPER-GCT-FINAL-40895819`: complete direct textual review and targeted full-proof checks of F01–F17, with independent reconstructions retained for F01–F03, F09–F10, F13's character calculation and F15's orbit-model construction; PASS. F16/F17 have now advanced from message-level proposal checks to complete final-text checks. Exact GCT source claims were matched to the prior full-context audit and the direct source checks described earlier. No proof assistant or new numerical test was used for this final pass.

## Added full-text review of F18 and F19, 2026-11-21 00:51 Europe/Berlin

Both generated finding files were read directly in full, including their complete proofs and post-proof limitations. This is a new review of these exact source files, not a reclassification of the earlier whole-paper snapshot.

- `finding_F18.tex`, SHA-256 `7e35414414d1ed9e40057ad3f8fbfc38a6b54ec45896b27f7a6a504c118dd1af`: **PASS**. The coordinatewise-flooring proof has precisely integral homogeneous endpoint hypotheses; finite-sum positivity is justified; the full parity ray is extracted from the constant term of IV equation (172); the rational singleton model and VI Definition 1.2.4 qualification are correct. The proof and source identification are also independently recorded in `REVIEW_THETA_SATURATION_GCT.md`.
- `finding_F19.tex`, SHA-256 `292edc6700c7e26b520a89ad29713bac64bafefc6fdee01dc1ded65db6ec7f19`: **PASS**. The full presentation reduction, coefficient D^5, units, central CRT, matrix spanning and independence, special radical/kernel, order-two collision, and explicitly trivial coherent bundle all match the independent derivation. The proof does not confuse abstract specialization with the ambient image. The finite-field étale observation is about geometric cohomology, and the full-End semisimplicity limitation is correctly narrow.

Clock at hash capture: 2026-11-20 23:51:01 UTC. These were direct textual/full-proof checks; no additional numerical or formal proof verification was used for the generated files. The separately recorded exact symbolic matrix checks in the newly written tensor-action report concern that new report, not the displayed F19 proof.

Editorial continuation only: once the later actual tensor-module result is inserted, F19's final statement that its bundle is not yet the actual tensor module should refer forward to that result. This was accurate for F19 alone and is not a mathematical error in its proof.

## Added final-text checks of F21/F22/F24/F25/F26/F27, 2026-11-21 UTC

I directly read every statement, complete proof and post-proof limitation in these generated additions. The F21/F22/F25/F27 portions were read in the current full paper; F24/F26 were read directly from their complete generated finding files. Exact reviewed excerpts are saved in `audit_snapshots/`, so a later change of the full paper does not blur the check's scope. All six additions **PASS** under their displayed hypotheses. Model: GPT-6 Astra Pro; effort inherited and not exposed. Verification: full textual/proof review and independent algebraic/analytic reasoning; no new formal-kernel or numerical test was used in this pass.

| Addition | Reviewed snapshot SHA-256 |
|---|---|
| F21 | `26ca933ecf409a69f740bc7565b0f91ac0d60380463e05187135c6040e594d07` |
| F22 | `71de6c40fb351dda20e6dc65356cd06f98f9ff2580a7b618d91acd635e996159` |
| F24 | `4079cab04eec46d08b39ecd648cbef0b5543a611515b2f77d2551673f09fafd1` |
| F25 | `aa0f447bbd90395b72cf3ca5509f70735abb5771af0dfb298ad45350f68d5306` |
| F26 | `3fdf296205167a2c890175b425b6bf9094a0971152d43d0c804390173189e569` |
| F27 | `eb006c7b5e7b4672ab7e928ec95c1c040ae1dcb10389bf1584f005fa5f547256` |

### F21: actual module, not just a matching character

The paper has the correct IV §6.1 locator and consistent normalization `c=T+v^(−1)`. Its right row matrices, three displayed basis changes and determinants agree with the earlier exact symbolic certificate `verify_rank3_matrices.py` and with the independently reconstructed module decomposition. This final-text check did not rerun that certificate or reclassify it as a formal proof. The displayed determinants are units over exactly the stated localization; no factor `z_1−z_2` is inverted. The multiplicity calculation is `16+4=20`, `4`, `8+8=16`, `4`, giving dimension 64. The two branch evaluations jointly act faithfully before specialization because the center embeds in the product of its branch rings.

The `Hom(E,F)` formulation has the correct right action by precomposition. On the matrix component it is a row module, so this is compatible with the source convention and the change-of-basis formulas. The sheaf is expressly not locally free across the collision, and its two branch multiplicities are not incorrectly presented as one constant rank. At specialization its radical annihilator is exactly the matrix ideal generated by the central nilpotent, while the quotient acts faithfully. No simultaneous quantum-group/canonical-lattice comparison is claimed.

### F22: exact information lost by constant étale data

The finite universal homeomorphism proof correctly separates the two generic points from the one special point and checks their residue fields. The length and conductor formulas follow from the displayed difference map and multiplication in the normalization. Topological invariance concerns coefficient-sheaf topoi, not structure sheaves. In the nearby-cycle computation the strict henselian local model has two split geometric generic points, so higher cohomology vanishes; the diagonal specialization map has a one-dimensional cokernel in degree zero. Its Frobenius and inertia are trivial. The tensor-power traces `2^r` and `1` are thus exactly independent of the collision order. The actual root difference has order two in every stated good characteristic, so the final coordinate rescaling gives `C_2`. The explicit limitation to these constant coefficient families is essential and present.

### F24: proposal audit now matched to generated text

The finite signed theorem, controlled-error argument, independent embedding and dual requirements, and retained-top-radius finite-extension clause all match `agent_signed_even_tensor_audit.md`. I rechecked the two complete counterexamples in the generated text. The constant sequence `1−(−1)^n` is indeed the alternating trace of the two indicated unramified lines. The complex-coefficient example is an exact split bilinear count in every characteristic; its exponent and error signs are correct. The result bounds only grouped visible roots and correctly excludes erased cohomology. This check advances F24 from the earlier message-level proposal audit to the stated exact final-text snapshot.

### F25: deformation and basis

The central-block/Morita reduction, vanishing crossed Hom, dimensions `688,816,128`, and the actual base-change map are all correct. The displayed alternating free resolution has the correct orientation: applying `Hom(-,L_2)` starts with multiplication by `−Delta`, then zero, yielding `Ext^1=R/(Delta)`; applying `Hom(-,L_1)` starts with zero then multiplication by `Delta`, yielding self `Ext^1=0`. The 128 cross multiplicities and length 256 follow. The affine center coordinate has an invertible linear coefficient, and its square coefficient is exactly `(D−1)(D−4)`. The regular matrix-unit basis has only the stated three possible structure constants. Its scalar's compact-support point-count identity and twist `(2)` are correct; its negative Laurent coefficients and absence of a categorified product are explicitly retained.

### F26: exact finite-spectrum normalization obstruction

The generated version uses the independently checked recurrence proof of the rational-function criterion. Its constant term is nonzero because every exponential root is nonzero. Choosing a pole of maximal modulus excludes cancellation with every later shifted rational function, so only poles at zero/infinity remain. The argument works for eventual sequences and after inversion of the variable. The module trace calculation and both arithmetic substitutions match the actual F21 matrices. The resolvent identity permits arbitrary fixed endomorphisms, hence even arbitrary Jordan-polynomial trace terms cannot evade the obstruction. If the endomorphism commutes with Frobenius, simultaneous upper triangularization gives ordinary power sums. The exact all-extension word-trace dictionary is isolated rather than attributed to GCT without evidence. The grading/Tate-ring paragraph and its limited statement about completed categories are correct.

### F27: parity versus a changed effective cone

The first assertion is about the parity of **terms** in a bounded complex with the specified split-Grothendieck effective basis. The mixed coefficients of every `P^k` prove it directly and do not incorrectly imply a statement about the cohomology of every possible lift. The explicit zero-differential tensor complex has a nonzero term in every degree and no homotopy equivalent complex can remove an extreme: the homotopy-to-identity correction on the zero-differential complex is zero degreewise. The separate exact-fiber-functor argument correctly proves cohomological amplitude growth and persistence **when mixed-parity cohomology is present**, without assuming a general convolution functor is exact.

The rank-one evaluation map is injective, has the stated congruence image, becomes an isomorphism after inverting delta, and sends the actual nonstandard element to equal nonzero values on the two equal-sign characters. Thus it restores the sign-tensor-sign action lost in F16. The even variable and element `b=vc` give the displayed quadratic relation and actual integer-Tate classes. The object on the supported character points has weights `−2,0,0,2`, as stated; it is not claimed pure in one weight. The normalization claim follows from finite integrality over the normal base and the generic product decomposition. The paper does not identify this cone with VIII's designated basis or turn scalar localization into a finite Weil realization.

The explicit rank-one Soergel bimodule relation used in the post-proof example was checked algebraically using the rank-two graded free decomposition over `Q[x^2]`. This pass did not freshly source-match the exact Elias–Williamson printed theorem/page citations; that external attribution remains the separate source check, not an accomplishment silently claimed by this proof review.

Suggested new events: `F21-FINAL-GCT-26ca933e`, `F22-FINAL-GCT-71de6c40`, `F24-FINAL-GCT-4079cab0`, `F25-FINAL-GCT-aa0f447b`, `F26-FINAL-GCT-3fdf2962`, `F27-FINAL-GCT-eb006c7b`; all full direct text/proof checks, PASS, with the source-verification limitation just stated.

## Generated F29/F30/F32/F34 matches, 2026-11-21 UTC

All four current finding files were read directly and completely, including post-proof scope/dictionary paragraphs. The resulting proof checks pass. These are fragment-level checks at the following hashes, not an assertion that every later full-paper integration was automatically checked.

| File | SHA-256 | Result |
|---|---|---|
| `finding_F29.tex` | `5043cef740bfbcd1e85cbe5b2608e99a963c422df3072189279480f9ca8617bc` | PASS |
| `finding_F30.tex` | `cc6176fe6f45563b644677d3a73e118cc6ca6e11935a4a10ff0ba0f20e30dac0` | PASS |
| `finding_F32.tex` | `44165a8b32ba3d9d9ebb2492abe89354530fe3fd06cac92b0ea5d4fd8ed50c6f` | PASS |
| `finding_F34.tex` | `558792e48349835b8d5df66d083c2d4389407c3006785131d9a5763d22e42de7` | PASS |

F29 matches the full earlier sphericity review. The final source locator is now correctly Manivel §3, p.3, Lemma 1 and Corollary 1; the general invariant-theoretic principle is separately in §2. The quotient by the dual Borel, partial-flag dimensions, regular-semisimple stabilizer and all input/rank bounds were rechecked.

F30 matches both the independently reviewed original obstruction and the separate mixing supplement. I reread the entire generated proof after its layout changes and the explicit clarification that `P_1/D` comes from tower rank two. Saturation, all rational compression coefficients, the two class-sum eigenvalues, regular central-block usage, pairwise unit rescaling, the two invertible mixing blocks, and the scalar commutant/base-change argument are unchanged and correct. The coherent dictionary distinguishes a bundle automorphism from an algebra-equivariant one. This is a final text match by the fragment's author, in addition to the separate fresh reviews by the root, theta and Grothendieck agents; it is not mislabeled as a new independent author-disjoint proof review.

F32 matches the countable-spectrum report and retains its nonnegative moment convention, normal convergence, genuine poles, uniqueness, finite grouping, signed top-radius visibility, per-embedding hypotheses and bounded-visible-dual finiteness. The proof's tensor-power argument also proves products of different admissible spectra by the same finite-outside-a-disk estimate and a common moment, with the product of their absolute moments in place of `S_N^k`. The actual normalized trace example has the correct first absolute moment and the exact reciprocal-support limitation.

F34 matches the full fresh review in `REVIEW_PH1_DIMENSION_GCT.md`. The generated version correctly includes `N=0`, the fixed-inner-weight interpretation, the affine-coordinate projection argument, the uniform compact-parameter contradiction, the exact output-size/#P example, and the prior Kahle–Michałek result. Its source encoding citation now says the opening of §3.4, p.53. Neither the result nor its dictionary confuses a pure multiplicity object with a succinct counting model.

Suggested events: `F29-FINAL-GCT-5043cef7`, `F30-FINAL-AUTHOR-cc6176fe`, `F32-FINAL-GCT-44165a8b`, `F34-FINAL-GCT-558792e4`; all full direct final-fragment/proof matches, PASS, with the author-match classification for F30 made explicit.
