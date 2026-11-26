# Intake of GCT_NSRH (prompt 24), checkpoint 01: Mulmuley's nonstandard RH against the sign-only purity of Alpöge's step 5

By Claude Opus 5.5 at effort high, launched by the main session (Claude Opus 5.5 at effort max), 21 Nov 2026.
The run: GPT-6 Astra (ChatGPT Pro mode), root and sub-agents; the run records its effort as "not exposed". It is still going.
Work file: `<local>/Documents\agent_notes\a8d753525905811ab_NOTES.md` (a copy of the first part is also in
`agent_notes\20261121_intake_GCT_NSRH_NOTES.md`).

## 0. What I read, and my scope

**Return folder:** `grothendieck_archive_transcription_20261110\research_returns\GCT_NSRH_checkpoint_01_20261120T2345Z_unzipped\`.
This was the only GCT_NSRH folder present when I started. It is the checkpoint of 00:40 CET (`STATUS_TIME.txt`). The README
marks it INCOMPLETE. This is a mid-run state: the run has not yet had its first three-hour review.

**What I read in full:**
- `GCT_NSRH.tex`, lines 1–770: the whole paper, with A01, F01–F17, Parts III–IV and the bibliography;
- `QUESTIONS.tsv`, `LEDGER.md`, `IMPLICATIONS.md`, `README.md` and `RUN_METADATA.md`;
- `RESEARCH_SATAKE_DRAFT.md`;
- the proposition and proof of `agent_theta_saturation.md` (the proposed F18), and the head of its review;
- the column structure and types of `CHECK_EVENTS.tsv`.

**Read at the level of the statement:**
- `agent_rank3_specialization.md` (claim R3-A; the first 5 kB);
- the other agent memoranda (not opened beyond their titles in the paper).

**Sources I opened to check the run:**
- Alpöge's note, p. 3, footnote 3 (in the return's `ALPOGE_remark.txt`, lines 95–160);
- GCT IV (arXiv cs/0703110v4 TeX, from the prompt ZIP): Definition 11.1, equation (93), and Remark 11.19;
- GCT VIII (arXiv 0709.0751v2 TeX): Conjectures 2.7 and 3.4;
- our cote 16 transcriptions `ARCHIVE_16_scan034`–`040`, `049` and `050` (from the prompt-32 ZIP);
- the QUESTIONS of the ALPOGE_GCT checkpoint 01 (prompt 23).

**My own computations:** exact sympy computations, in
`<local>/AppData\Local\Temp\claude\f2c80a22394db22f\e0d20ada-e036-40ad-83b1-31e9a63b69bc\scratchpad\scripts\hecke_cones.py`,
`...\hecke_cones2.py` and `...\hecke_cones3.py`. They cover the nonstandard Hecke algebras for r = 2 and r = 3 (section 2).

**The three mid-run reports, in short:**

| Report | Verdict |
|---|---|
| Iterated Parseval with tensor powers gives purity under opposite parity along long paths (F03, F04, F17) | **Confirmed**, as a conditional theorem |
| GCT VIII allows signed normalizations | **Confirmed** against the source (VIII Conjectures 2.7 and 3.4) |
| The rank-one nonstandard Hecke inclusion does not inherit the ambient positive cone (F09) | **Confirmed as stated** (for the cone of the KL basis C′⊗C′). Its framing is **corrected**: in the cone of the dual KL basis C⊗C, the original inclusion is positive for r = 2 and r = 3. That is BMS's own positivity, GCT IV Remark 11.19. A sign identity proved here shows that the two facts are the same (section 2) |

## 1. Verdicts, finding by finding

The check types follow the rubric. The run's own events (see `CHECK_EVENTS.tsv`) are internal readings by its sub-agents,
GPT-6 Astra (ChatGPT Pro mode), effort not exposed. The verdicts below are my own.

### The main question (Q3)

- **F01: path identity and Parseval bound.** Targeted proof check, **confirmed**. I re-derived K_hK_h^* = Q^d·I from
  nondegeneracy. The inner sum is the bilinear form t^T K_h D K_h ⋯ K_h t, with k − 1 kernels and k − 2 diagonal factors.
  The bound (Q − 1)Q^{d(k−1)/2}‖t‖₂²‖t‖_∞^{k−2} holds.
- **F02: finite spectral no-cancellation.** Targeted proof check, **confirmed**. The generating function has a genuine
  pole at each 1/α_j; Cauchy–Hadamard finishes the proof.
- **F03: the tensor-path purity criterion.** Targeted proof check, **confirmed**. This is the main result.
  - I recomputed the overhead: |R_{k,n}| ≤ B^k Q^{k(a+d)/2 + d/2 + 1}.
  - I recomputed the sign algebra: −ε^k R = Σβ^n + Σ_{tuples}(α₁⋯α_k)^n, and every multiplicity is positive.
  - The diagonal tuple gives α^k, and it cannot cancel.
  - Fixed k first, then k → ∞: this order of limits is correct.
  - The duality uses the rational scalar q^{a+d}, so it holds under every embedding.
  - The hypotheses are exactly the content of footnote 3 on p. 3 of Alpöge's note: "Bertini gives a definite sign from
    middle cohomology, one off the one on M^k ... iterating Parseval k times, opposite signs meaning no cancellation of
    inverse roots".
- **F04: errors of size o(k) in the exponent.** Targeted proof check, **confirmed**.
- **F17: an extension degree e_k that may depend on k, and a separate dual system.** Targeted proof check, **confirmed**.
  The grouped powered roots α^{e_k k} keep positive multiplicities. The dual half is immediate from the hypotheses.
- **F05 (a)–(f): countermodels to shortened forms of the argument.** Targeted check, **confirmed**. I recomputed every
  example: the constant trace; Q_ℓ(−1) ⊕ Q_ℓ(−1)[−1]; the spectrum {R, −R}; the F₃ Fourier diagonal entry e^{2πi/3}/√3;
  the unipotent block.

### Positivity (Q2–Q5)

- **F06.** Confirmed: h = v² − 1 + v⁻² ≥ 1 on the real line but is not of the form ±(v − v⁻¹)^a f. The (1, 0, 1)
  grading is also checked.
- **F07: the effective-categorification criterion.** Confirmed. It agrees with the ALPOGE_GCT run's P-F6.
- **F08.** Confirmed: b₂² = (1, 4) = 3b₂ − 2b₁, and the Gram determinant is 1.
- **F09: the rank-one cone.** Confirmed as stated.
  - Recomputed: b² = −δb, cb = 0, P² = δ²P, and P = δ² − δ(c⊗1 + 1⊗c) + 2c⊗c.
  - The element is the actual one: GCT IV Definition 11.1, equation (93), P_s := C′_s⊗C′_s + C_s⊗C_s.
  - The result is robust: it survives rescaling P to P/[2], and it holds for BMS's Q_s = [2]² − P_s.
  - **Scope.** The cone is the one of the KL basis C′⊗C′. The run concludes that "the fixed inherited ambient cone is
    ruled out" (paper section 15, gate E). That holds only for this cone. Section 2 shows that the C⊗C cone is
    inherited.
- **F10: monomial pivots, and its counterexamples.** Confirmed: c = p·h, x² = hz, and b₁² = (1 + 2v)b₁ − v(1 + v).
- **F11.** Confirmed: λ²(z − 1) = 1 − z; γ_t(z − 1) = 1 + (z − 1)t; for e₁₂ and e₂₁, the p-th power map is not additive.
- **F12: Reynolds projectors.** Confirmed. This is a known reformulation (the projector of BIP, equation (4.1)), not a new
  result. The run says so itself.
- **F13: path counts.** Confirmed. I checked the character identity [2,2]⊗[2,2] = [4] ⊕ [2,2] ⊕ [1⁴].
- **F14 and F15.** Confirmed: the orbit-closure scheme over Z, the f = p example, and h⁰(P¹, O(rd)) = rd + 1.
- **F16.** Confirmed: on sign⊗sign, P acts by 4 and E by 0. Section 2 makes the action mismatch of F16 unnecessary.
- **F18 (proposed; under fresh review in the run): saturation of homogeneous integral difference-constraint models.**
  Targeted proof check, **confirmed**. Flooring preserves x_i − x_j ≤ b for integral b. The Kronecker example
  g((1,1)³) = 0, g((2,2)³) = 1 is classical; it is the same example as ALPOGE_GCT PL-07.
- **A01: no stated finite-field nonstandard RH in IV, VI, VII or VIII.**
  - What I checked: VIII Conjectures 2.7 and 3.4 (the signed forms ±(q − q⁻¹)^a f and ±(q^{1/2} − q^{−1/2})^a f) and the
    IV definition.
  - What I did not read: the rest of the source audit. That part is carried as background, without fault found.
- **Satake draft (QNEW-SATAKE).** Read at the level of the statement.
  - It realizes the classical plethysm and Kronecker multiplicity spaces as Hom(IC_λ, image of the Young idempotent e_ν on
    IC_μ^{*d}), pure of weight dD_μ − D_λ.
  - This is known geometric-Satake material (Mirković–Vilonen; Richarz, Galois descent), not a new theorem.
  - It is correctly labelled a draft. Its use in the run is right: purity is not the missing ingredient for classical
    multiplicity spaces.
- **R3-A (QNEW-H3): A ≅ R × R × M₂(C).** Read at the level of the statement, plus spot checks:
  - the rank is 1 + 1 + 8 = 10;
  - z₁ − z₂ = (D − 1)(D − 4)/D², and D − 4 = (v − v⁻¹)² vanishes to second order at v = 1;
  - this matches the run's "branches collide to second order".

  I did not read the full proof.

**Counts.**

| Check | Findings |
|---|---|
| Targeted proof check, confirmed | 18: F01–F18, with the F05 sub-items counted as one |
| A gap | 0 |
| Refuted | 0 |
| Corrected in scope | 1: the framing of F09 in gate E and in the categorical-consequence paragraph |
| Read at the level of the statement | 3: Satake, R3-A, A01 beyond the VIII and IV locators |

## 2. A new statement from this intake: the sign identity, and positivity in the dual cone

**INT-NSRH-1 (proved here, modulo the classical identity θ(C′_w) = (−1)^{l(w)} C_w).**
- Let θ be the algebra involution of the Hecke algebra H_r given by T_s ↦ −T_s⁻¹.
- Then θ(C′_s) = −C_s and θ(C_s) = −C′_s. Both are checked directly from (T − v)(T + v⁻¹) = 0.
- So θ⊗θ fixes each P_s = C′_s⊗C′_s + C_s⊗C_s, and hence fixes the whole nonstandard Hecke algebra Ȟ_r.
- With θ(C′_w) = (−1)^{l(w)} C_w (Kazhdan–Lusztig 1979; the locator is from memory and must be verified; the identity is
  checked by computation for S₃):

  **for every a ∈ Ȟ_r, its C′⊗C′ coordinates are (−1)^{l(x)+l(y)} times its C⊗C coordinates.**

  The proof is one line: a = (θ⊗θ)(a).
- Consequences:
  - F09's negative entries −δ at (e, s) and (s, e) are this sign pattern.
  - An element positive in both cones is supported on the pairs (x, y) with l(x) + l(y) even.

**INT-NSRH-2 (computation certificate, exact).** For r = 3, with x = P₁ and y = P₂, take the ten alternating words
1, x, y, xy, yx, xyx, yxy, xyxy, yxyx, xyxyx.
- Every coordinate of every one of them in C⊗C lies in N[v, v⁻¹].
- Every one of them except 1 has negative coordinates in C′⊗C′.
- They have rank 10 (checked at v = 3/2).
- They span Ȟ₃ over Z[v, v⁻¹]: use x² = Dx and y² = Dy, and the relation (R3) of IV, Theorem 11.16, which rewrites
  yxyxy and the words of length 6.
- Ten spanning elements of a free module of rank 10 form a basis.

So **Ȟ₃ has a Z[v, v⁻¹]-basis of elements that are positive in the ambient tensor dual-KL cone, through the original
inclusion.** For r = 2 the basis {1, P} is positive in that cone: P = δ²·1⊗1 + δ(1⊗C_s + C_s⊗1) + 2C_s⊗C_s.

**Against the literature.**
- GCT IV Remark 11.19 (rev. v4, TeX lines 4177–4180) states that the older version proved a basis B of Ȟ₃ with
  nonnegative expansions in {C_v⊗C_w}. So the positivity for r = 3 is **known**, for a different basis.
- BMS write that they are "uncertain" whether this holds for Ȟ₄.
- New here: the sign identity, which explains F09 and the C′-signs at once and holds for every r; and the positive basis
  of alternating words.
- The run cites Remark 11.19 in its rank-three memorandum, but the paper's F09 and gate E do not mention it. They should.

**How this bears on the open problems.** The route that F09 appeared to close is open in the dual cone. The obstacle is now
located exactly:
- **Combinatorial obstacle:** positivity of Ȟ_r in C⊗C for r ≥ 4, which BMS left open. The next attack is the same exact
  computation for r = 4 (S₄ has 24 elements, so H⊗H has rank 576): the dimension of Ȟ₄ from IV, and whether a word basis
  stays positive.
- **Categorical obstacle:** the dual KL basis is the basis of classes of simple objects in graded category O₀. The tilting
  and projective objects give C′; this is Koszul duality, Beilinson–Ginzburg–Soergel and Soergel 1997 (from memory, to
  verify). So the heart that F09 says is needed is the Koszul-dual heart: the abelian category O₀^Z(gl_r) ⊠ O₀^Z(gl_r),
  or equivalently the perverse t-structure on the Hecke category.
- **The next attack, stated exactly:** find objects of O₀^Z ⊠ O₀^Z whose classes are the basis of INT-NSRH-2, and an exact
  monoidal-type operation realizing the product of Ȟ₃. That operation is the obstruction, because the C-basis structure
  constants of H are signed, (−1)^{l(x)+l(y)+l(z)}. What has to be explained is that on θ⊗θ-fixed elements the signs
  square away, as in (C_s⊗C_s)² = δ²·C_s⊗C_s.

That is gate E of the paper with a named heart, in place of "a different category or heart".

## 3. What is new

**Against the literature.**
- **F03, F04 and F17** are a clean, correct, conditional form of Alpöge's footnote-3 mechanism. The skeleton is Deligne's
  tensor-power step of Weil I, in which positivity comes from the reality of the coefficients and the k-th powers. Here
  the positivity comes instead from the parity of one-degree concentration. The square-root bound comes from Parseval,
  not from Weil II. That substitution, and the precise hypotheses (S1), (S2) and the duality, are new as a written theorem,
  as far as I can see. They are elementary. (The Weil I locator, §3, is from memory and must be checked before it is
  cited.)
- **F05–F11 and F13–F16** are elementary lemmas and counterexamples, correctly labelled as deductions, not results.
- **F09** is new as stated, but section 2 shows it is the other face of the known positivity in IV Remark 11.19.
- **F12** is known (BIP).
- **F18's example** is classical; its general flooring form is the standard integrality of difference-constraint systems.
  As an obstruction to theta and interlacing models it is a useful precise statement.

**Against tonight's other runs.**
- ALPOGE_GCT (prompt 23), checkpoint 01: P-F6 is the same criterion as F07. PL-07 is the same Kronecker example as F18.
  Q-ALPOGE-METHOD has the same gate as Q3-GCT.
- GCT_PLETH: G-004 (purity and the invariant projector on a finite étale example) is close to F12 and F14. I did not read
  the other runs further.
- No run tonight has the sign identity of section 2.

**Against our own results.**
- The Hodge sketch (`reports_20261120\hodge_bridge\HODGE_BRIDGE_SKETCH_20261121.md`, 3.6) already corrected Fable's
  suggestion 4: the sign of step 5 is the parity of concentration, "the Fourier-transform line ..., not the Hodge index".
  F03 is the theorem behind that sentence. The two agree.
- The sketch's first test of Route 3 (the path form on E^k: the adjacency matrix of a path, nondegenerate exactly for even
  k) fits F17: the criterion needs only an unbounded set of k, so one may take only even k, where the path quadric is
  nondegenerate and unimodular over Z.

## 4. Scope of the two proofs

- No finding uses RH or GRH, from Alpöge or from Masullo, as an input.
- Alpöge's note is used only as the source of the method (footnote 3, p. 3, and steps 3–8).
- No Masullo statement is used. The run says so (paper section 1).
- Nothing claims more than its input gives. The run states explicitly that no nonstandard RH, no canonical-basis
  positivity and no P ≠ NP follows.
- One wording to fix in the successor: "stipulated premises" is right for the scope of this prompt. Our house form is
  "Alpöge's theorem, cited".

## 5. Integration

**Open rows of earlier runs.**
- **ALPOGE_GCT Q-ALPOGE-METHOD (prompt 23):** F03, F04 and F17 give the abstract theorem it asks for. The row's gate
  stays: identify the object.
- **Bridges run (prompt 22), Q05 (the standard conjectures):** unchanged.
- **Fable suggestions:**
  - 3: F01 proves its norm part; F05(e) refutes its literal positive Fourier operator.
  - 4: refuted at the level of the mechanism, as the Hodge sketch 3.6 says. The sign is a parity, not an index.
  - 8: made exact by F13. F18 shows that a homogeneous integral interlacing model cannot count Kronecker coefficients
    (saturation fails), so a theta chain needs congruence or lattice data. That is the run's own next gate, and I agree
    with it.
- **ALPOGE_GCT PL-07 and F18:** record them as the same example (a cross-reference).

**Grothendieck's texts.**
1. **Cote 16, scan numbering.** The run's cote 16 scan numbers are one less than those of our transcription files. In
   ours:
   - `ARCHIVE_16_scan035`, `037` and `039` are typescripts (Karoubi's *Cohomologie des catégories de Banach*; injective
     hulls);
   - `034`, `036`, `038` and `040` are handwritten (the Prop. on P^i(X) → P^i(Y); the decomposition
     H*(Y) = ⊕ L_X^j P^i(X) ⊕ E^{n−1}; Λ_Y);
   - `049` holds the C(X)/semisimplicity passage, and `050` holds "the deduction of the Weil conjectures from the
     conjectures C and A".

   So the run's "corrections" of the Fable locators (its section 13: "semisimplicity is scan 48, not 50"; "34 is a
   reused back") are a numbering offset, not corrections [read: folio numbering (folio = our scan − 1), since the run
  cites the printed folios and our text of record numbers by PDF page (`\scanpage`), recording the folio as `\mspage`
  (HECKE_DIV, `work\grothendieck_locators.md`, checked on the official cote 16 PDF). (corrected 21 Nov 2026 after the
  intake of HECKE_DIV, Claude Opus 5.5 at effort high)]. The Hodge sketch's locators, 3.2 (scan 49 and 50) and 5,
   are right in our numbering. **Edit:** in the run's successor and in any use of its archive table, add 1 to every cote
   16 scan number, and ask the run to state its convention for every cote. I did not check the other cotes (90, 97, 133)
   for the same offset; they should be checked.
2. **Cote 16, our scan 036, the evanescent part.** The "definite sign from middle cohomology" of step 5 is, in
   Grothendieck's hyperplane induction, the fact that the new cohomology of the section Y, namely E^{n−1}(Y), sits in the
   one degree n − 1. Its trace-formula sign (−1)^{n−1} is "one off" from the ambient. This is the bridge to cote 16 for
   prompt 32: the bridge is through the degree of E^{n−1}, not through the sign of the intersection form on it. The index
   form enters only for semisimplicity and positivity (our scan 049).

**Study and companion notes (edits listed, not made):**
- `reports_20261120\hodge_bridge\HODGE_BRIDGE_SKETCH_20261121.md`, 3.6: add "proved as GCT_NSRH F03/F04/F17 (checked in
  this intake)" after "That is the Fourier-transform line".
- Same file, Route 3, first test: add "by GCT_NSRH F17 only an unbounded set of k is needed: take k even".
- Same file, section 5, cote 16 row: add the numbering note of item 1 above.

**The successor prompts it feeds.**
- **Prompt 32 (HODGE_SIGN), item 1.** The abstract sign-only theorem is F03, F04 and F17 here. Its successor should cite
  it (GCT_NSRH, F03) and spend its time on item 2.
- **Prompt 32, item 2, the concrete question.** For which Y (smooth hypersurface sections, quadrics, powers of CM curves)
  do Grothendieck's induction of scans 034–040 (ours) and SGA 7 XI give (S2) for the path hypersurfaces of all even k,
  without weights? [Answered: for every smooth affine U and lisse F, the generic member of f + Σg_i + c on U^k gives
  (S2) (HODGE_SIGN SG-08, SG-09, confirmed); the "take k even" is needed only for the E^k path-bundle test. (corrected
  21 Nov 2026 after the intake of HODGE_SIGN, Claude Opus 5.5 at effort high)]
- **Prompt 33 (TRACE_DET).** F02 and F05(b) state exactly when alternating traces lose eigenvalues. They are the right
  tools for det(1 − wB) against the Fredholm determinants of cote 1.
- **Prompt 35 (ZETA_TWO).** F03 is a purity criterion for any zeta function that has a trace system with the parity
  hypothesis. It should be offered as the route for the conditional purity statements there.
- **Prompt 36 (CUE).** No change.
- **The successor of this run.** See section 6.

**The language of algebraic geometry.** The run's Part III translates every finding (SGA 3 I 4.2 and 4.7; SGA 6 V §§2–3;
SGA 4 XVII–XVIII; SGA 5 III 4.7; Weil II 3.3.1; EGA I §9.5; FGA 221). That is adequate. What is missing:
- the cote 16 offset of item 1;
- the translation of the path hypersurface's parity as the degree of E^{n−1} (item 2);
- for section 2: θ is the Koszul/Ringel duality that exchanges the KL and dual-KL categorifications. In the geometric
  realization, the Hecke category on G/B with its simple perverse sheaves gives C′. That is an SGA 4 framework, but no
  cote is known for it.

## 6. Prompt updates for the successor of GCT_NSRH

1. **Correct the framing of F09 and gate E.**
   - The obstruction holds for the C′⊗C′ cone only.
   - Add the sign identity (INT-NSRH-1), and cite IV Remark 11.19: the older GCT IV proves positivity of a basis of Ȟ₃ in
     the C⊗C cone.
   - State gate E as positivity in the dual cone, not as "some other heart".
2. **Main attack for the next run.**
   - Decide positivity of Ȟ₄ in C⊗C by exact computation: the dimension of Ȟ₄, a word basis, and its C⊗C coordinates.
   - Prove the r = 3 basis positivity of INT-NSRH-2 by hand, or explain it structurally. A candidate explanation: why
     the signs (−1)^{l(x)+l(y)+l(z)} cancel on θ⊗θ-fixed products.
3. **Categorification attack.**
   - Realize the dual-cone basis by objects of O₀^Z(gl_r) ⊠ O₀^Z(gl_r), or by the perverse heart of the Hecke category.
   - Identify the operation that realizes the product of Ȟ_r.
   - Then apply F07 in its abelian (not split) form, and state what F07 needs in that form.
4. **Purity side.** Purity is not the missing ingredient for classical multiplicities (the Satake draft). Ask instead
   whether a trace system for Ȟ_r, a finite-field model of the heart in item 3, satisfies (S1) and (S2) of F03.
5. **Archive.** State the scan convention for each cote. Shift the cote 16 numbers by +1 to our convention. Recheck cotes
   90, 97, 133 and 1.
6. **Effort record.** "Not exposed" is the run's own statement. Our records give the run as GPT-6 Astra (ChatGPT Pro mode),
   as our rules require.
7. **The push rules stand.** The run already has the ledger and the three-hour review in place.

## 7. Check events

See `INTAKE_GCT_NSRH_20261121_CHECK_EVENTS.tsv` in this folder.
