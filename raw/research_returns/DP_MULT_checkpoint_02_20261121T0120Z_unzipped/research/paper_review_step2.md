# Independent paper review: local proofs and étale framework

Reviewer: `/root/step2_higher`; model: GPT-6 Astra Pro. Runtime effort setting: not exposed. Date: 2026-11-21 UTC. This is an actual review record, not a proposed checking plan.

## 1. Scope and outcome of the proof review

I read the complete statements and proofs of DP1, DP1r, DP2, DP3, DP4, DP5 and DP6 in the working `DP_MULT.tex`, including their conventions and the step-2 normalization discussion. A second full reading of the same proof span ended at approximately 00:08 UTC according to the clock tool. The author's paper was being extended elsewhere during this reading; the comments below identify the exact mathematical claims reviewed rather than certify future edits. The complete file fingerprint sampled after the second reading was SHA-256 `82d3fbe0eb6859cc11d40d08114b4f10e11caa72d6a62d7e372a6d5dd09cd8bf` (61,938 bytes).

**Outcome: the local arguments pass this independent mathematical reading.** The one minor normalization ambiguity found on the first pass, allowing the scalar `u=0` while writing `n v_p(u)` at order zero, has already been repaired in the text by requiring `u∈K^×` and discussing the zero derivation separately. I found no remaining substantive error in the reviewed span. This is a human-style mathematical proof review by an LLM, not Lean kernel verification.

### DP1: uniform affine estimate

The logarithm construction and coefficient recurrence are valid over `K=Frac(W(k))`. For `m<q`, every coefficient of `[p](t)` appearing in the recurrence lies in `pR`; for `m=q`, every factor in a product with at least two factors uses degrees below `q`. These observations justify precisely the asserted integrality below degree `q` and valuation at least `−1` at degree `q`.

The truncated logarithm is a strict integral coordinate, and its integral inverse makes the coordinate-invariance assertion legitimate. The translation identity gives exactly `Δ_q=D^q/q!+bD`, with no additional degree-`q` terms. The resulting operator identity

`D^q=p^B u_0D+p^(B+1)T`

has integral `T` and `u_0`. Multiplication on the right by `D^(n−q)` is important: no commutation assertion is needed to propagate coefficientwise ideals. The base-digit minimum is exactly `1−h`; the second recursive term exceeds the desired real exponent by `1−c_h≥0`. Taking ceilings is justified because valuations in `K` are integral. The test `n=q−1, f=t^(q−1)` establishes optimality of the affine intercept for every fixed normalized group satisfying the height-at-least hypothesis. This optimality claim does not require exact height.

### DP1r: recursive integer refinement

The base case and the two terms of the operator recurrence give the asserted bound directly. The paper appropriately avoids claiming that this recurrence computes the exact minimum at every order.

### DP2: contraction and exact exponential coefficients

The finite Eisenstein extension is complete, and the scaling of the group law has integral coefficients. Every scaled `p`-series coefficient is divisible by `p`. Coefficient induction therefore proves integrality of the scaled logarithm and its inverse without invoking a Lubin–Tate normal form.

For the reduction argument, `g_π/p` reduces to `t+ā_q t^q`. In the logarithm recurrence, the terms `g_π^i/p` for `i≥2` vanish modulo `π`; hence the scaled logarithm has exactly that reduction. Its additive-polynomial inverse has a nonzero coefficient at each `q^r`, so the corresponding exponential valuation is an equality. No cancellation in those coefficients was overlooked. The trivial extension when `q−1=1` is correctly separated.

### DP3: floor-sum estimate and sharpness

The exponential coefficient estimate yields the preliminary evaluation bound because only finitely many coefficients contribute at a fixed degree. The passage from rational to integral valuations permits exactly the displayed floor. The use of formal translation to recover a coefficientwise estimate is valid in `R[[t,u]]`.

For `j=hr+s`, the reduction of `E_π(z)^(p^s)` uses characteristic-`p` Frobenius and has nonzero coefficient at degree `p^j`. Scaling back gives valuation `−(p^j−p^s)/(q−1)`, equal to the indicated floor. Thus the stated witnesses work for each fixed formal group of exact height `h`, not just a chosen Honda or Lubin–Tate model.

The base-`p` digit composition is legitimate because all operator estimates hold coefficientwise. Both digit-sum rearrangements are correct. The resulting integer exponent is the sum over `j≥1` not divisible by `h`. The witnesses prove equality at the stated `p`-power orders and optimality of the asymptotic slope. The text correctly refrains from pointwise optimality claims at all other orders.

### DP4: endpoints and normalization

At height infinity, all coefficients of `[p]` are divisible by `p`, so the same induction works in `R` without extension. The inverse logarithm is integral, and the factorial estimate and its witness follow. The multiplicative height-one example is correct. The corrected scalar condition `u∈K^×` and denominator correction `n v_p(u)−M` are precise.

### DP5: distributions and divided powers

The convolution multiplication has the claimed leading binomial coefficient: all higher-degree terms of `F` contribute only lower filtration degree in distributions. This proves the associated-graded divided-power algebra, rather than asserting a false identification of the filtered convolution algebra with it. At exact finite height, `e_q` has valuation `−1`, so `D^q/q!` fails to preserve the original integral ring. The separate PD-ideal obstruction follows from `p!γ_p(t)=t^p`. The integral additive coordinate after contraction indeed transports integral divided derivative operators back to the scaled group.

The later comments correctly distinguish the restricted `p`-operation on invariant vector fields from the `p`-curvature of a connection. I did not newly re-prove all the cited EGA/SGA3/crystalline background statements during this proof reading; those must retain their source/background status in the event table.

### DP6 and the step-2 passage

The height-two specialization gives exactly `c_2=p/(p²−1)`, and the integer floor sum is the sum of the odd reciprocal-power floors. The coefficientwise bound at order `p` proves restricted nilpotence for height at least two; the height-one witness proves its failure there. Height infinity is covered separately. The proof uses the standard elliptic height dichotomy as background.

The step-2 discussion accurately separates this universal local result from the additional identification of an analytically normalized theta jet with an integral local function and the normalized invariant derivation. Changing a frame or period is not silently treated as preserving all jets. The paper does not claim that the local result alone proves a shorter theta-lift chain.

## 2. Actual proof-check events

These events are whole-proof readings; they are not source audits, finite computations, formal verification, or a claim of reviewing unrelated later proofs. The first independent derivations of parts of DP1 were separately recorded in `step2_higher_agent.md`.

| Event ID | Finding | Check performed | Outcome | Date UTC | Model / effort |
|---|---|---|---|---|---|
| SPR-P-001 | DP1 | Read the complete current statement and proof; independently checked coefficient recurrence, strict coordinate, translation operator, digit minimum, induction, and optimal-intercept witness | Passed | 2026-11-21 | GPT-6 Astra Pro / not exposed |
| SPR-P-002 | DP1r | Read complete statement and proof and checked dependence on the integral operator identity | Passed; lower-bound scope retained | 2026-11-21 | GPT-6 Astra Pro / not exposed |
| SPR-P-003 | DP2 | Read complete statement and proof; checked scaled `p`-series, integral logarithm, reduction and inverse-polynomial recurrence | Passed | 2026-11-21 | GPT-6 Astra Pro / not exposed |
| SPR-P-004 | DP3 | Read complete statement and proof; checked evaluation-to-coefficientwise passage, every `p`-power witness, digit composition and optimal-slope argument | Passed | 2026-11-21 | GPT-6 Astra Pro / not exposed |
| SPR-P-005 | DP4 | Read complete statement and proof, including endpoints and scalar correction | Passed after minor `u≠0` wording fix, observed in second reading | 2026-11-21 | GPT-6 Astra Pro / not exposed |
| SPR-P-006 | DP5 | Read complete statement and proof; checked convolution filtration, factorial obstruction and transport after contraction | Passed; external crystalline/EGA background not independently re-proved here | 2026-11-21 | GPT-6 Astra Pro / not exposed |
| SPR-P-007 | DP6 | Read complete statement and proof and surrounding step-2 normalization discussion | Passed; elliptic height dichotomy carried as cited background | 2026-11-21 | GPT-6 Astra Pro / not exposed |

## 3. Precisely relevant étale-cohomological framework

Let `a:A→S` be an abelian scheme, with `S` locally noetherian and a prime `ℓ` invertible on `S`. Smooth proper base change for the constant sheaves `Z/ℓ^rZ` gives locally constant finite cohomology sheaves and their geometric-fibre identifications. Passing to the `ℓ`-adic system gives the lisse sheaf `R^1 a_* Q_ℓ`, whose stalk at a geometric point `s̄` is `H^1_et(A_s̄,Q_ℓ)`. For an abelian scheme of relative dimension `g`, its rank is `2g`.

If `S` is of finite type over `F_q`, the closed fibres are smooth projective. Deligne's Weil I theorem then makes their `H^1` pure of weight one: for a closed point with residue field of cardinality `q_s`, the geometric Frobenius eigenvalues have every complex absolute value `q_s^(1/2)`.

This is a legitimate placement of the abelian-family objects in the SGA/Weil framework. These theorems do not supply an integral formal parameter, a theta trivialization, a `p`-adic period comparison, the coefficientwise derivative valuation, or the bridge to automorphic multiplicity. Complex weights and the local integral `p`-adic lattice are different data. In particular the weight-one assertion applies to both ordinary and supersingular elliptic fibres, whereas their normalized invariant differential operators have the different behaviour proved in DP6.

### Exact verified primary locators

1. **SGA 4, Exposé XII, Théorème 5.1 and Corollaire 5.2:** proper base change and its geometric-fibre form. The latter is explicitly identified as the fibre assertion used by XVI, Théorème 2.1. Primary-text re-edition: <https://www.normalesup.org/~forgogozo/SGA4/12/12.pdf>.
2. **SGA 4, Exposé XV, Théorème 2.1:** smooth morphisms are universally locally acyclic for coefficients whose torsion primes are invertible on the base. Together with XVI, Théorème 2.1, this gives the lissity assertion for locally constant constructible coefficients. Primary-text re-edition: <https://www.normalesup.org/~forgogozo/SGA4/15/15.pdf>.
3. **SGA 4, Exposé XVI, Théorème 2.1 and Corollaire 2.2**, original pagination pp.213–214, re-edition PDF pp.4–5: proper locally acyclic morphisms, and in particular smooth proper morphisms, preserve local constancy of the appropriate cohomology sheaves and identify their stalks with fibre cohomology. The coefficient sheaf must be locally constant and constructible. Theorem 2.1 states that hypothesis. The printed Corollary 2.2 omits the words “locally constant”; use the correct hypothesis explicitly, or cite Theorem 2.1 together with XV 2.1. Our application to constant `Z/ℓ^rZ` satisfies it. Primary text: <https://www.normalesup.org/~forgogozo/SGA4/16/16.pdf>.
4. **Deligne, La conjecture de Weil I, Théorème (1.6), p.276**, Publications Mathématiques de l'IHÉS 43 (1974), 273–307. This is the smooth projective theorem and therefore directly applies to abelian fibres. The Frobenius convention is discussed in §1.15, p.279. The theorem was checked visually in the primary PDF, not merely inferred from a secondary reference: <https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf>.

The Orgogozo SGA4 files are re-editions of the primary text and include editorial annotations. The original pagination is preserved in their margins; it should be distinguished from PDF page numbers. No unread original handwritten manuscript is involved in these source checks.

### Source-check events, distinct from proof checks

| Event ID | Source checked | Actual check | Status |
|---|---|---|---|
| SPR-S-001 | SGA4 XVI 2.1–2.2 | Read the exact statement and immediate dependency discussion in the primary-text re-edition, including the locally constant hypothesis and fibre formula | Statement and applicability rechecked; full published proof not re-proved |
| SPR-S-002 | SGA4 XII 5.1–5.2; XV 2.1 | Checked the exact locators through the primary text and XVI's explicit cross-references | Source/dependency check; not a new proof of base change |
| SPR-S-003 | Deligne, Weil I (1.6), p.276 | Downloaded the Numdam primary PDF, extracted its text, rendered PDF page 5 and read the theorem visually, confirming the exponent `i/2` | Statement and abelian-fibre applicability rechecked; Deligne's theorem is cited, not re-proved |

### Weil II verification added after the proof review

Deligne, **La conjecture de Weil II, Corollaire (3.3.9), p.207**, Publications Mathématiques de l'IHÉS 52 (1980), 137–252, states the smooth **proper** version: the degree-`i` Frobenius eigenvalues have all complex absolute values `q^(i/2)`; the characteristic polynomial is integral and independent of `ℓ≠p`. This strengthens the smooth projective scope of Weil I (1.6). It gives the same weight-one conclusion for abelian fibres and does not prove the local derivative estimate.

Primary URLs: <https://www.numdam.org/item/PMIHES_1980__52__137_0.pdf> and the author's publication copy <https://publications.ias.edu/sites/default/files/Number40.pdf>. I read the theorem in the author-hosted parsed primary text, then rendered and visually read printed p.207 of the Numdam PDF (its PDF page 72). The visual check confirmed the exponent `i/2` and the distinction between proper and projective.

Source event **SPR-S-004**, 2026-11-21 UTC, GPT-6 Astra Pro / effort not exposed: Weil II (3.3.9), statement and applicability rechecked visually; full published proof cited, not re-proved.

SGA5 is not required to prove this special case once the preceding SGA4 and Weil references are given. Its role, if cited, is the `ℓ`-adic coefficient formalism. A precise source check of that formalism is separate from the derivative proofs. No statement here derives local `p`-divisibility from purity.


### SGA5 coefficient formalism: exact primary scans checked

**SGA5, Exposé VI (J.-P. Jouanolou), §1.4.2, Definition 1.4.3, pp.265–266** defines constructible `Q_ℓ` sheaves as the quotient of constructible `Z_ℓ` systems by torsion, describes morphisms by tensoring Hom with `Q_ℓ`, and describes the lisse category through continuous finite-dimensional `π_1` representations when the base is connected. The subsection heading is numbered 1.4.2; the actual definition is 1.4.3. This is consistent with the reference in Weil II §1.1.1 to SGA5 VI (1.4.2). Earlier exact locators are Definition 1.1.1, p.251 (constructible adic systems), Definition 1.2.1, p.254 (lisse integral systems), and Proposition 1.2.5, p.259 (continuous integral representations).

I downloaded and visually read the original page scans, rather than relying on an automated transcription. Stable archive: <https://wstein.org/sga/sga/5/>. Individual scans for pp.265–266: <https://wstein.org/sga/sga/5/SGA5-page-277.png> and <https://wstein.org/sga/sga/5/SGA5-page-278.png>. This is coefficient formalism, not an additional local derivative-divisibility theorem.

Source event **SPR-S-005**, 2026-11-21 UTC, GPT-6 Astra Pro / effort not exposed: SGA5 VI definition/description statements and their exact pagination checked visually; no claim of independently re-proving the entirety of ℓ-adic sheaf theory.

## 4. Supplementary complete reading of DP7–DP9

After the initial review, I read the complete current DP7, DP8 and DP9 statements and proofs. DP7's homomorphism identity and mixed coefficientwise bounds are correct; an integral homomorphism suffices, and a rational isogeny factor alone does not. DP8's product-of-multiplicative-formal-groups counterexample is valid, and its full integral CM counts and conjugation argument agree with the Tate source reviewed in the earlier memo. DP9's ratio formula is correct, and the unit/scalar examples refute precisely the claimed inference to positive generic-fibre vanishing. The paper expressly avoids declaring the existence of a shorter specially constructed theta chain impossible. A minor display typo was reported: `\widehat\Gm^{,r}` has a stray comma.

Events **SPR-P-008** (DP7), **SPR-P-009** (DP8), and **SPR-P-010** (DP9), 2026-11-21 UTC, GPT-6 Astra Pro / effort not exposed: complete proof readings, all passed; the standard CM decomposition is cited background with its source separately checked, not a new proof of Tate's theorem.

## 5. Actual integrated-paper review of DP17–DP24

### Version and scope

At the root's request I read the complete integrated statements and proofs of DP17 and DP18, challenged their normalization against the recovered source, and read the complete DP19 and DP20 proofs against `ramified_cm_scope.md`. DP22 was then added to the paper; I read its complete actual statement and proof, not merely the preceding agent memo. The newly integrated DP21, DP23 and DP24 statements and proofs were also read in full. I subsequently reread all eight theorem/proof blocks together, after computing their individual hashes and checking that none had changed between extraction and that reading.

The first paper hash, while DP17–DP20 were being read, was `eafedfe8d2234efad9271b2782a0a37f47cc9e27e24e1d92dd1a738b5b7382ec`. The integrated paper sampled at the later check was **SHA-256 `a46cfaf802a0502124908ba5acbb5ff80b1d2cfda6300b4324fbd71e5d7e6b1a`**, 86,415 bytes. The clock tool returned **2026-11-21 00:33:18 UTC** at that hash-recording step. Individual statement-plus-proof hashes and source line spans are preserved in `paper_review_new_theorems_metadata.json`. The second full reading checked those exact block hashes, so later edits elsewhere in the paper do not alter which mathematical text was reviewed.

**Outcome: all eight reviewed proofs pass with their stated scope.** No substantive mathematical correction was requested. I suggested one source-normalization clarification for DP18: the displayed budget is the inner bracket in `SizeWindows`, which also multiplies it by `x^(C epsilon)`. The root added the clarification, and I observed it in the paper. Since that factor is at least one under the source hypotheses, the lower-bound argument is unchanged.

This is an independent mathematical reading by `/root/step2_higher`, GPT-6 Astra Pro, effort setting not exposed. It is not Lean kernel execution, a reproof of the published background theorems, or a renewed review of DP1–DP16.

### DP17: ramp certificate

The symmetric difference of the indices was checked explicitly. Compared with odd indices, the added terms are even indices not divisible by `h`; the removed terms are odd multiples of `h`. The added sum is bounded by `A/(p²−1)`. When `h` is odd, the removed sum is bounded by `Ap^h/(p^(2h)−1)≤A/(p²−1)`; when `h` is even it is zero. Taking the difference of two quantities in that interval gives the claimed absolute bound, without the unnecessary factor two that a crude triangle inequality could introduce.

Each local sum converges by geometric comparison. The prime sum of the *differences* converges absolutely with the displayed `C`; this does not require the two separate infinite prime sums to converge in the zero-weight case. A common finite cutoff only removes nonnegative terms from the two bounding sums. For `w_i≥1`, the finite cutoff agrees with the infinite form once `p^i>A`. The zero-weight identity `R_h=Ac_h` follows from subtracting the multiples-of-`h` geometric series.

I also checked the source normalization, separately from this elementary proof. `DataParams₂.lean:205–206` defines `sz=2*lwP*ramIdx*y`; its `FactEtaMean:265–267` sums `lwP*ramIdx` over all places above `p` to `log p`. This gives exactly the stated factor `2C` when other inputs are fixed. The positivity of these finite-place weights permits restriction to the relevant subsets. `GlobalTheoremInputs.LinkG_at:132–135` places the ramp expression on the lower side of the gain comparison. Therefore the paper correctly calls it a lower-bound certificate and does not turn the summable change into an upper bound on a new construction's actual gain. Its express caveats concerning one fewer lift and cancellation of leading terms are necessary and correct.

### DP18: unchanged error allowance

Dividing each of the three terms of `B` by `S`, with `d_i=N_i/n`, gives exactly

`2A/(mbd_2)*(1+m²/k) + 4m*x^epsilon/(d_1*d_2) + 2k*x^(2epsilon)/(d_1*n²)`.

All denominators are positive. The assumptions `A≥xb`, `d_i≤1` and `x^epsilon≥1` yield `2x/m+4m` by discarding only nonnegative terms. The stated bound for `m≤x^(1/2−delta)` follows directly. If the signal is multiplied by a positive factor uniformly bounded above by `M`, the lower bound is merely divided by `M`, so its power of `x` cannot improve.

The actual source `GrowthBoundGivesRiemannHypothesis.lean:109–122` contains the same inner bracket, the outer factor `x^(C epsilon)`, and the same signal. Its generic `SizeWindows` predicate alone does **not** give `A≥xb`. The paper explicitly supplies that additional condition; `DataParams₂.Scale.a:31` is `x*b`, and `ErrorFormsWeakWindowsFalse.ErrWindows0:28–30` includes the lower-scale inequality. Thus the proof is not accidentally applied to the weaker generic window. A lower bound on an upper-bound allowance is not a lower bound on the actual error, and the integrated discussion preserves that distinction.

### DP19: full integral unramified CM action on a ramified base

The Teichmüller average is integral because `q−1` is a unit; its linear coefficient is one, so it is an integral invertible coordinate preserving the primitive tangent vector. Reindexing the action gives the asserted exact equivariance. For any forbidden exponent a root of unity has `zeta^(n−1)−1` a unit, so the support restrictions on `[p]`, `L` and `E` follow. The height condition makes the first allowed nonlinear `p`-series coefficient a unit.

The contraction places every `p`-series coefficient in `pA'`; the logarithm coefficient induction remains valid in a ramified valuation ring because `(p−p^n)/p` is a unit. Crucially, the support restriction makes `n−m` a multiple of `q−1`. The exponential coefficient lower bound is therefore an integer before any rounding is attempted. This supplies the factorial-minus-floor estimate even though the original value group can contain nonintegers. Translation and the already established finite base-`p` composition argument then give `E_h(n)` coefficientwise.

For the affine estimate the integral operator identity has the same two integer powers of `p`. The paper uses the integer ideal-containment recurrence from DP1r, rather than rounding the valuation of an arbitrary coefficient of `A`. That distinction is essential and correctly implemented. The cases `h=1` and `q=2` are explicitly addressed. No discrepancy with the agent memo was found. The full action is on the integral lifted group; an action present only after reduction is not silently substituted.

### DP20: genuine ramified counterexample

The proof uses the cited Lubin–Tate deformation theorem to provide an actual integral formal group, rather than treating an arbitrary chosen polynomial as a `p`-series. I checked the application and the resulting calculations against `ramified_cm_scope.md`; this review does not independently reprove Lubin–Tate Proposition 1.1. The complete ring specialization is legitimate because `varpi` is topologically nilpotent.

The degree-`p` cocycle gives the invariant coefficient `varpi*t^(p−1)`, hence `D^p t(0)=(p−1)!*varpi`. The sum of the cocycle in the repeated formal sum telescopes to `(p^(p−1)−1)*varpi`, which is a unit times `varpi`, including when `p=2`. The condition `e>p` is exactly what makes `r=(1−1/e)/(p−1)>1/p`. After contraction and division by `p`, every coefficient of degree at least `p+1` then has strictly positive valuation, while the coefficient of degree `p` is a unit.

The scaled logarithm is integral and reduces to `x+c*x^p`: after dividing its functional equation by `p`, every term involving the second or a higher power of the scaled `p`-series vanishes modulo the maximal ideal. The inverse additive-polynomial recurrence has nonzero coefficients at all `p^s`. Scaling back and Legendre's exact value `v_p((p^s)!)=(p^s−1)/(p−1)` give the displayed equality. Since `1/(e(p−1))<c_h`, the deficit is linear along this subsequence, so an `O(log n)` error cannot repair it. Finally `E_h(p)=1` for `h≥2`, making the claimed failure of an integral lift of the full unramified action a direct consequence of DP19.

### DP21: the fixed logarithm

The actual integrated proof matches the independently derived source obstruction in `step2_recovered_sources.md`, §8. The coefficient of degree `p²` in `oneLog` is exactly `+1/p`. The lower logarithm coefficients for a height-at-least-three group over `W(k)` are integral; composition with an integral invertible coordinate and a unit scalar preserves their integrality in that degree. The independent `p`-series calculation has coefficient `1−p^(p²−1)` and therefore exact height two. The final sentence correctly limits the claim to the actual scalar logarithm and retains the possibility of another representation of a particular theta function.

### DP22: the concrete CM Jacobian

The two affine charts glue as asserted because `y²/x^8=x^(−1)−x^(−8)`. They are finite over the two standard affine charts of `P¹`, hence give a proper double cover. The partial derivatives prove smoothness at `11`, including infinity. The eight simple branch points give genus three. The cited standard relative-Jacobian construction applies because the curve is smooth proper with a section.

The chosen unramified cubic ring contains the seventh roots of unity. The automorphism extends across infinity, and its covariant action on Jacobian divisor classes is compatible with the Abel–Jacobi pullback. At infinity `ord(x)=−2`, `ord(y)=−7`, and `ord(dx)=−3`, so the displayed differentials have orders `4,2,0`; their eigenvalues are `zeta_7,zeta_7²,zeta_7³`. A characteristic-zero homomorphism of abelian varieties with zero differential has trivial connected image, so the cyclotomic polynomial kills the endomorphism. Irreducibility gives the claimed maximal-order action of degree six. The characteristic-zero identity extends to the integral abelian scheme, so this supplies the integral action used in the local decomposition.

Multiplication by `11≡4 mod 7` gives precisely the two orbits in the proof. Their type counts are two and one, and the unramified local factors have degree/height three. The integral completed-order idempotents give an actual direct-factor decomposition, not merely an isogeny decomposition. Tate's cited CM formula gives the slopes `2/3` and `1/3`. The dimension-one factor has connected closed fibre; the standard connected formal-group correspondence over the complete local base therefore yields the claimed integral formal factor and split tangent lattice. Those general correspondence and CM theorems are cited background, not re-proved in this event. The arithmetic `66/665`, `11/120` and `144/133` is exact. The following paragraph correctly leaves global theta costs uncomputed.

### DP23 and DP24: limited obstructions

DP23's slopes are `1/h` and `(h−1)/h`; a rank-one alternating CM orbit has half its embeddings selected and thus slope `1/2`. For `h>2` neither original slope is `1/2`. Isogeny invariance, products of slope multisets and the product-of-conjugates description of finite unramified restriction of scalars prove the stated obstruction. The adjoining paragraph explicitly restricts it to the rank-one alternating inputs and does not assert that all higher-rank source objects have that Newton polygon.

DP24 uses a constant integral function. Every positive-order invariant differential monomial kills it, and so does every positive-degree homogeneous determinant differential operator. The universal lower bounds allow zero; a finite controlled-nonvanishing inequality does not. The text expressly retains the actual Cartier theorem's exponential main term and unit-minor assumptions, so the example refutes inference of those assumptions, not the theorem.

### New whole-proof check events

All events in this table occurred on 2026-11-21 UTC, by `/root/step2_higher`, GPT-6 Astra Pro / effort not exposed. Each concerns the entire integrated statement and proof, with the block hash in `paper_review_new_theorems_metadata.json`.

| Event ID | Finding | Actual challenge | Outcome |
|---|---|---|---|
| SPR-P-011 | DP17 | Full proof read twice; checked both parity cases, absolute difference, convergence, cutoffs, zero-weight slope and certificate-only scope | Passed |
| SPR-P-012 | DP18 | Full proof read twice; independently divided all three terms and checked positivity, lower-scale hypothesis, bounded factor and allowance-only conclusion | Passed; harmless outer-factor clarification observed |
| SPR-P-013 | DP19 | Full proof read twice; checked the averaging coordinate, support, ramified integer exponents, coefficientwise transfer and integer affine recurrence | Passed relative to previously reviewed DP1r/DP2/DP3 |
| SPR-P-014 | DP20 | Full proof read twice and compared with the source memo; checked specialization, derivative and cocycle coefficients, strict contraction, inverse recurrence and linear deficit | Passed; published deformation existence used as cited input |
| SPR-P-015 | DP21 | Full integrated proof read twice; checked both the integral-coefficient contradiction and direct `p`-series calculation | Passed |
| SPR-P-016 | DP22 | Full integrated proof read twice; checked both curve charts, CM action/type, integral factor construction, slope/connectedness application and exact constants | Passed with the cited standard Jacobian/CM/formal-group theorems |
| SPR-P-017 | DP23 | Full integrated proof read twice; checked slope multisets, isogeny invariance and unramified restriction, and the rank-one-only limitation | Passed |
| SPR-P-018 | DP24 | Full integrated proof read twice; checked annihilation by all positive-degree operators and distinction from the actual Cartier hypotheses | Passed |

Separate source-interface events **SPR-S-006** and **SPR-S-007** record the actual reinspection of the source for DP17 (`DataParams₂`, `FactEtaMean`, `LinkG_at`) and DP18 (`SizeWindows`, `Scale.a`, `ErrWindows0`), respectively. These are source-normalization checks, not Lean execution or a new proof of the source's final global theorem.

**Observed later DP22 revision.** After this review the root expanded the projective-relative-Jacobian and connected-formal-group citations. I read the entire revised DP22 statement and proof again. The finite morphism to `P¹` is projective, smoothness gives flatness, the hyperelliptic fibres are geometrically integral, and `H²(O)=0` for those fibres, so the added hypotheses fit the cited Picard construction. The positive slopes give the connectedness needed for the stated formal-group equivalence. The mathematical application still passes; exact checking of the newly supplied FGA/Tate-1967 locators belongs to the root/archive agent's separate source events. This follow-up is **SPR-P-016r**, and its revised paper/block hashes are in the `later_rechecks` array of the metadata file. The sampled whole-paper hash for this revision is `5fd942a90c4807c7ca19e964f6bbe22bff5ac9064b3aa38fe31b6ff5c2407a54`.

**Observed explicit Čech revision of DP22.** I subsequently read the entire revised proof replacing the Riemann–Hurwitz sentence by an explicit genus computation. The relation `v=x^(-4)y` gives the summand with transition `x^(-4)`, hence `pi_*O_C=O⊕O(-4)`. On the two affine charts the second Čech quotient is the displayed Laurent-polynomial quotient; the exponents not covered by `k[x]` and `x^(-4)k[x^(-1)]` are exactly `−1,−2,−3`. The first summand has zero first cohomology. The two affine preimages and their affine intersection give the stated vanishing in degree two; the nonsquare branch polynomial gives geometric integrality. I reread all the remaining CM-action, factor and normalization steps as well. **SPR-P-016s**, 2026-11-21 UTC, GPT-6 Astra Pro / effort not exposed: whole revised DP22 proof passed. Paper hash `3ecf680f5d003bf431f17ad15e9b424cb44474ea73dc903a6f2ed14198d405b1`; DP22 block hash `f075a530804b757f7eb2ffd9b515abb71e90f3f702ea1ab92c19df21e931e57c`.

## 6. Actual integrated dual theorems: DP30 and DP32

These are new whole-proof reads on **2026-11-21 UTC**, by `/root/step2_higher`, **GPT-6 Astra Pro**, runtime effort not exposed. The actual paper and block hashes, observation time and exact snapshots are saved in `paper_review_actual_dual_metadata.json`. They are integrated-text checks, distinct from the source checks and independent-agent reports in the research memos. No Lean execution is claimed.

### SPR-P-019: complete integrated DP30

Read the entire statement, proof and following limitation paragraph. The strict Teichmüller coordinate makes the law additive below degree `q`. The restricted Verschiebung has rank-p image equal to the Frobenius kernel, so exact finite Cartier duality gives the stated quotient. The explicit coordinate inclusion is faithfully flat of rank p; equality of the `[p]` and iterated Frobenius kernels follows from the height ideal, without equating Verschiebung to an iterated Frobenius as maps. The inequality `2p^(h−1)−2<p^h` kills every nonlinear term, including at p=2. The primitive-basis and restricted-p computation, equality of Lie algebras, and primitive integral lift all agree with the complete memo proof. The paper explicitly avoids requiring all of the dual to be connected. The conclusion concerns an integral coordinate; the following paragraph does not identify it with an actual theta entry. **Passed without mathematical correction.**

The Tate locators used in this integrated proof have also been independently text-read and visually checked by this agent: §1.2–1.3 printed pp. 159–160; §2.2 Proposition 1 and diagram (3), pp. 162–164; §2.3 Proposition 3, p. 166. Those are primary-source facts, not an independent reconstruction of Tate's general theorems.

### SPR-P-020: complete integrated DP32

Read the entire newly integrated statement and proof and the following equal-direction comparison. The monomial cycle has total exponent h and finite degree p^h; its matrix functional equation matches Hazewinkel's hypotheses, including the d=1 case. The explicit lifted monomial-basis argument proves finite freeness over the entire formal function ring. Duality and cancellation occur over F_p, so the proof does not hide a Frobenius twist. The resulting identity `F^h=[p]` proves connectedness and puts the integral one-dimensional p-series directly in the known Lubin–Tate class. Hazewinkel §5 p. 77 gives precisely the uniqueness and integral strict-isomorphism result used here.

For each cyclic arrow the weight equation is `p^e r_j−r_i=1`. Iterating it gives the displayed coefficient valuation `1+p^(e_1)+…+p^(e_1+…+e_(n−1))−n`, strictly positive for n≥2. The residue logarithm is `id+M`; M is additive in characteristic p, so its formal inverse is the stated alternating composition series. In coordinate i, only full cycles return to that same input coordinate, giving a unique nonzero q-power coefficient with the asserted sign. The scaling and Legendre calculation therefore prove the exact derivative sequence, not only a lower bound.

For a general integral f, substitution into the integral scaled inverse gives the weighted coefficient estimate. Treating the untranslated variables as coefficient variables in the integral group translation supplies the coefficientwise version. The sum of slopes equals c_h, and the mean comparison uses the already proved strict ratio bound; it is expressly limited to equally weighted coordinate directions. I checked p=2 and h=2 edge cases and found no missing hypothesis. **Passed without mathematical correction.**

The scaling derivation was challenged before integration and the actual integrated proof was then read in full. The two actions are not counted as two independent reviewers.
