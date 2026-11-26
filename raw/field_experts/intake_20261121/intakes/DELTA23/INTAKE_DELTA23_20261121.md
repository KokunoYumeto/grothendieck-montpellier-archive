# Intake of DELTA23 (prompt 29, "Δ, 2-3 reciprocity of frames on GT"), checkpoint 06

Intake by Claude Opus 5.5 at effort max (agent ae4ae3dc17acaa440), 21 Nov 2026, 04:20-04:40 UTC, at the request of the
main session (Claude Opus 5.5 at effort max). The run is GPT-6 Astra (ChatGPT Pro mode) with four cooperating workers of
the same model; its RUN_START.txt says the effort setting was not exposed by the runtime. The run started 20 Nov 22:59 UTC
and is still going.

## 0. What I read, and my scope

**The return folder.** `grothendieck_archive_transcription_20261110\research_returns\DELTA23_checkpoint_06_20261121T0329Z_unzipped`.
It was the only DELTA23 folder at 04:21, 04:31 and 04:38 UTC. Checkpoint 07 was due about 04:14 UTC and had not landed.

**The state of the return.**
- The paper is 188 pages, `DELTA23.tex` with 101 proof files.
- There are 141 statement ids: 138 in the part "Findings with a completed whole-proof check", and C32, F29 and F38, which
  appear only in the check events.
- `CHECK_EVENTS.tsv` has 493 rows, all by the run's own workers.
- The prompt's main question, A.84, is open in the run. Its gate is one finite Hurwitz label, (1,0), with 32 complete
  affine tables (H13).

**Read in full, statement and proof (22 findings):**
- item 1: L1-L8;
- the main question: H2, P18, H12, H13, H14;
- descents and characters: F22, P13, C36, C1, C2, C6, C8;
- level six: F18;
- distribution: D1.

I also read the prompt as sent, `QUESTIONS.tsv`, `LEDGER.md`, `IMPLICATIONS.md`, `README.md`, `RUN_START.txt` and the
paper's §1 (conventions and supplied inputs).

**Read at the level of the statement (119 findings):**
- C3, C4, C5, C7, C30, C34, D2, F2, F5, F7 and F9 from their statements in the paper;
- every other id from its row in `QUESTIONS.tsv` and its check events. These are mostly the finite Krammer, Hurwitz and
  orbital computations: P1-P33, F10-F17, F19-F21, F23-F44, C9-C35, H1, H3-H11 and T1-T2.

**Compared with:**
- our register rows (`results_register\REGISTER.tsv`):
  - EXIT_TOWER E.44, E.49;
  - GT_TOWER_CHECK A.1, A.3, A.4, A.5, A.7, B.1, B.1.8, B.2.1, B.2.25;
  - LM8_PUSH C.21, C.23, C.30;
  - LM7_PUSH E.3, E.58, E.65;
  - DELTA_ON_GT A.14, A.24, A.84, A.86, A.103, A.112, B.40;
- the Δ referee report, `results_register\delta_referee_20261118\REFEREE_REPORT.md`, §§1, 4, 5;
- my sweep-1 tower files, `results_register\sweep1_tower\SUMMARY.md` and `CORRECTIONS.md`;
- Fable's suggestion 1, `reports_20261120\alpoge_rh\bridges\FABLE_PROGRAM_SUGGESTIONS_20261120.md`, lines 23-46;
- `reports_20261120\IMPLICATIONS_REPORT_20261121.md`, §5 item 1.

**Not done:**
- I reran none of the run's code.
- My computations are my own scripts, written from the statements. They are listed in §2 and in the check events.

## 1. The finding that governs this intake: the run's main question is decided on our record

**What our record holds.** These rows are all GPT-6 Astra (ChatGPT Pro mode):
- **EXIT_TOWER E.49 (Proved):** "For the continuous character Δ of LM7 E.65, with its specified signed frames, one has
  Δ|GT̂ = 0." The E.58 element is therefore not in GT̂.
  - The proof uses the three-division configuration, the universal-curve and forgetting maps, and E.44.
  - E.44 is the ten-point Klein configuration, giving 𝒥(A) = A on all of GT̂.
- **GT_TOWER_CHECK A.3:** E.49, with its two label comparisons repaired.
- **GT_TOWER_CHECK A.7:** Δ|GT̂ = 0 for every multiplier, and G_Q ⊆ GT̂ ⊊ ker Δ ⊊ GT̂₀.
- **GT_TOWER_CHECK A.5:**
  - d₂ = 0 on the multiplier-one domain, from the first square of the ten-point construction;
  - then e₃ = 0, from the sum Δ = d₂ + e₃ = 0.
- **GT_TOWER_CHECK B.1.8:** D_L|GT̂ = id and D_P(F) = cFc on GT̂.
- **GT_TOWER_CHECK B.2.25:** the characters χ_n = Δ∘Dⁿ are linearly independent even on H; Ξ(H) = F₂^ℕ, Ξ(GT̂) = 0 and
  Ξ∘D = shift∘Ξ.
- **LM8_PUSH C.30:** explicit independent quadratic characters indexed by the primes p ≡ 5 mod 12, vanishing on all of
  GT̂; the quadratic rank is countably infinite.

**How far these are checked.**
- The two gates were refereed by Claude Fable 5.2 at effort max (agent a49aabbf5ed57bb8e, 18 Nov), with the verdict
  Proved:
  - route 1, EXIT_TOWER E.44;
  - route 2, SECTION_GHOSTS E.176-E.181.
- The referee did not read E.37, E.49, GT_TOWER_CHECK A.1, A.3 or A.7 (report §1, event DR18). So the last step from the
  gates to Δ|GT̂ = 0 has no check outside its runs.
- My sweep-1 correction 1 (19 Nov) records E.3 as proved on record and standing on one model.

**What the prompt said.** Prompt 29 gave A.84 and E.3 as open. It attached only:
- DELTA_ON_GT checkpoint 05;
- LM7_PUSH;
- Alpöge's note;
- Fable's suggestions.

None of the rows above was attached or named. The run therefore gave its main effort, about 4.5 hours and most of its
141 statements, to a question decided on our record.
- *Cause:* the prompt took the states of E.3 and A.84 from their own runs' registers, not from the cross-run register or
  sweep-1 correction 1.
- *Fix:* before a prompt calls a question open, its builder reads the question's rows in `REGISTER.tsv` across runs and
  in the sweep corrections.

**Consistency.** Nothing in DELTA23 contradicts those rows.
- D23.H14 (no element of GT̂ ∩ ker λ has Δ = d₂ = 1) follows from A.5 (d₂ = 0) and also from A.7 (Δ = 0).
- D23.C8 with B.2.25 or C.30 gives N ⊄ cl([G,G]G²G_Q). C8 states only the equivalence, so there is no conflict.
- The question left open after F22, whether a₃ = a₃∘𝒟_E on full GT̂, is A.5's e₃ = 0, by F22.3.
- C6 says only 0 and Δ factor through the adelic frame pair. So C.30's characters cannot factor through that pair. This is
  a consistency point for whoever uses C.30 (§6).

**What DELTA23 adds to the decision.**
1. **Why finite tests could not decide it.**
   - Taken together, these show that every test of the following kinds lets a mixed candidate through:
     - pronilpotent level-six tests (F12, which assumes the supplied E.58 lifting input);
     - congruence tests (F18, unconditional);
     - the degree-12 cyclic cover at 2 and 3 (F21, conditional);
     - fixed-target cyclotomic distribution relations (D1-D2);
     - the Hurwitz and Krammer word tests at the levels tried (P7-P14, P32, F41, F43).
   - The proof on record uses different information: the Klein four-group at the ten-point configuration, brought back to
     the discrete group by Boggi-Zalesskii Theorem A or by Smith theory (E.44; SECTION_GHOSTS E.176).
   - This is information about finite subgroups of the profinite group. No finite word test carries it.
   - If E.49 holds, compactness guarantees that some finite level does exclude the mixed state, at an unknown depth: an
     inverse limit of nonempty finite sets is nonempty. The run's levels do not reach it.
2. **A second route to Δ|GT̂ = 0, from the run's identities (my derivation).**
   - On the multiplier-one gentle group, Δ = d₂ + e₃ (DELTA_ON_GT A.103).
   - F22.3 gives e₃ the intrinsic form a₃ + a₃∘𝒟_E.
   - d₂ = 0 on GT̂ ∩ ker λ comes from the ten-point square (A.5's first half). It does not use E.49's three-division step.
   - So an independent proof that e₃ = 0 on GT̂ ∩ ker λ proves Δ|GT̂ = 0 without E.49. The natural candidate is 𝒟_E|GT̂ = id,
     the fixed-point equation D23.F22.4 on all of GT̂ and the equianharmonic counterpart of B.1.8's D_L|GT̂ = id.
   - This is the item for a successor (§7).

**In the project's terms.**
- B = C₂ ∐ C₃ is π₁^orb(M_{1,1}). Its two orbifold points are j = 1728 (CM by Z[i]) and j = 0 (CM by Z[ω]).
- An element of GT̂₀ moves the two local generators by conjugators, the frames β_F and A_F. Δ compares the parities of
  the two frames.
- The decision on record says the hexagon and pentagon force the two parities to agree. In Grothendieck's terms these are
  the relations at levels 1 and 2 of the Lego, M_{0,4} and M_{0,5} (cote 145, scan 6: normalized actions and their
  conjugating elements).
- So GT̂ sees no difference between the harmonic and the equianharmonic frames, while the gentle group GT̂₀ does (E.58).
- The decisive input on record is rigidity of a finite subgroup, the Klein four-group of M_{0,10}. It is not reciprocity.

## 2. Verdicts, finding by finding

The check types are those of the check rubric. "Given" names the inputs supplied by earlier runs that a finding uses.
None of those inputs was re-proved here.

### 2.1 Read in full (22)

| Id | Statement (short) | My check | Verdict |
|---|---|---|---|
| D23.L1 | For a CRT representative n ≡ (−1)^{a₂} mod 4, (−1)^{a₃} mod 3: L₂ = (n,3)₂ = (−1)^{a₂}, L₃ = (n,3)₃ = (−1)^{a₃}, L₂L₃ = (−1)^δ = χ₁₂(u); E.58 gives n = 5, (L₂,L₃) = (1,−1) | targeted proof check; computation (Hilbert symbols, χ₁₂ = χ₋₄χ₋₃ on {1,5,7,11}) | **confirmed.** As the run says, it is an encoding: the definition uses the bits |
| D23.L2 | (n,3) obeys Hilbert reciprocity; full ramification table; E.58's extra place is 5 | computation of (n,3)_v at v = 2, 3, 5, 7, 11, 13, ∞ for n = 1, 5, 7, 11 | **confirmed**; every row has an even number of −1 |
| D23.L3 | b₂ = b₃ ⟺ a class (a,3) supported only at 2, 3 ⟺ an algebra ramified at most at 2, 3; the equal-bit algebras are M₂(Q) and (2,3) ≅ (−1,3) | targeted proof check by hand (i′ = (1+j)i has square 2 and anticommutes with j); computation of the ramification of (−1,3), (2,3) | **confirmed.** Two-place support for all of GT̂ ∩ ker λ is equivalent to A.84 |
| D23.L4 | No function of the relative pro-3 action and the retained frames gives a₃ | targeted proof check | **confirmed, given** E.58.20, E.58.23 (the E.58 lifting input D.50 is not in the attachment) |
| D23.L5 | The product L₂L₃ is choice-independent; the individual symbols are not; neither bit is a Dirichlet character of the multiplier | targeted proof check | **confirmed, given** DELTA_ON_GT A.25 and E.65.5-6 |
| D23.L6 | The splitting-normalized Kubota cocycle of the corrected frames is 1 at 2 and at 3 on the whole gentle multiplier-one group | targeted proof check: AD.2 puts both frames in Γ₁(4,Z₂) at 2 and in SL₂(Z₃) at 3, where the cocycle splits | **confirmed, given** AD.2. The splitting is cited (Hida 2023 §1.3; Gelbart Prop. 2.8); I did not open those sources |
| D23.L7 | (−1,−3) is ramified at {3,∞}, (2,3) at {2,3}; not isomorphic | computation | **confirmed** |
| D23.L8 | With T₃ = aI + bR₀ and W₃ = cI + dS: (a+b,3)₃ = (−1)^{a₃} and (c²−d²,3)₃ = (−1)^{a₂}. Both bits are read at the prime 3 | targeted proof check (mod 3, (a+b)² = 1; c² + d² = 1 has the four solutions (±1,0), (0,±1)) | **confirmed, given** AD.2 and E.65's definitions of the bits |
| D23.H2 | Any h ∈ GT̂ ∩ ker λ times a σ ∈ G_{Q^ab} has ρ ≡ 0 mod 3, a₂ = 0, a₃ = Δ(h) | targeted proof check: k(2^{1/3})/k is cyclic of degree 3 and k(r₀) = k(3^{1/4}) has degree 2, coprime, so the restriction is onto C₃ × C₂ | **confirmed, given** DELTA_ON_GT A.88, A.102, A.12-A.13 and E.65 |
| D23.P18 | Multiplier-one GT̂ permutes Nielsen classes C^n/G compatibly with the Drinfeld action, so it preserves every B_n-orbit whose degree is unique; the degree-1344 and degree-36 orbits are; (P18.2) | targeted proof check: completed Artin sequence, peripheral transport, f(y_n,σ_n²) ∈ N, evaluation on σ₁, σ₂, σ₃ including the commuting-factor step z₃ = σ₁²y₃ | **confirmed.** I did not recompute the orbit-degree lists. The Drinfeld action theorem is cited (Lochak-Schneps 1994 §5 Prop. 10) |
| D23.H12 | For a normalized mixed element with label (1,0), the whole E₀-table lies in two 9-dimensional affine families; ϑ ∈ {0,2} | read in full | **not checked as a computation** (R_E of order 1179648·3⁹⁰, K = F₃⁹⁰, the inconsistency of the odd-ϑ cases with the raw action: not rerun) |
| D23.H13 | 32 existential normal forms for the table | read in full | **not checked as a computation** (the automorphism test (H13.2) and the GT powers (H13.3) are sound as described; the counts were not rerun) |
| D23.H14 | No h ∈ GT̂ ∩ ker λ has (Δ, d₂) = (1,1); hence Δ\|_{H₅} = 0 or d₂\|_{H₅} = 0 | targeted proof check of the deduction from H2, C34, C30, H12, C36 | **confirmed as a deduction**; it rests on the computations of C30, C34 and H12, which I did not rerun. It is **superseded on our record** (implied by GT_TOWER_CHECK A.5 and by A.7) |
| D23.F22 | A canonical endomorphism 𝒟_E of H (cubic descent) with a₃(𝒟_E h) = Ψ₃(h)/2 and ρ(𝒟_E h) = ρ(h); e₃ = a₃ + a₃∘𝒟_E; fixed-point form (F22.4) | targeted proof check of the group theory (E = C₃ ∐ C₃; ψ_f well defined since sgs = g⁻¹; uniqueness of the normalized representative); computation of the SL₂(F₃) identities: q_E(x) = −U², q_E(y) = −L², R = U²L²U⁻², C_E U^{2ρ} = R^ρ with a unique centralizing power | **confirmed, given** the supplied covariance f(U²,L²) = M_ρ, A.88-A.90, A.100 and AD.2 |
| D23.P13 | a₂(𝒟_E h) = a₂(h); Δ∘𝒟_E = d₂ = a₂ + a₂∘D_L = a₂ + a₂∘D_P on H | targeted proof check of (P13.4); computation of the ring identities in (Z/4)[ω]: (1−ω)c = 1 with c = 2+3ω, 2+ω² = 1−ω, the six phases distinct | **confirmed, given** FP.34 and A.107 |
| D23.C36 | f_h(S,R) = S^{ϑ(h)} in SL₂(F₃) with ϑ: H → Z/4 a character and ϑ mod 2 = Ψ₃/2 | targeted proof check by hand: on P¹(F₃) ≅ F₄, R: t ↦ ωt and S: t ↦ t+ω; the preimage of {1, S̄} is ⟨S⟩ ≅ C₄; additivity from f_{hk} = f_h φ_h(f_k) | **confirmed, given** A.89-A.90 |
| D23.F18 | Multiplier-one gentle elements act innerly on the congruence completion of Γ₀(6); every congruence Atkin-Lehner defect is trivial; the congruence version of A.86 is false | targeted proof check; computation: the conjugation formula for W₃ on 2401 integer matrices, W₃² = −3I | **confirmed, given** AD.1 (and E.58 for the refutation clause) |
| D23.D1 | If Y normally generates a finite G, one ordinary commutator word realizes any prescribed q(f) ∈ G′ and all distribution data (c_N, qδ_N(f)) for finitely many N; profinitely for all N | targeted proof check of the construction (q(K_m) = G; δ_N(K_L) = K_{L/N}; corrections in V_N′ in descending order; V₀ for g₀) | **confirmed.** The match of δ_N with Enriquez 2007 eq. (50) was not checked against the source |
| D23.C1 | d = a₂ + a₂∘D_P extends uniquely to G with d\|_{G_Q} = 0 | targeted proof check | **confirmed, given** E.65.16-17 and A.62 |
| D23.C2 | Characters factoring through finitely many descendant parities are spanned by Δ∘D^j, d∘D^j | targeted proof check (the tree argument) | **confirmed, given** B.14 |
| D23.C6 | The adelic frame image of H is N₃(4) × N₄(4); the Galois image is the equal-parity subgroup; frame-factoring relative characters are 0, Δ | targeted proof check of the deduction | **confirmed, given** C4, C5 (statements read, proofs not read), A.12 and the E.58 element |
| D23.C8 | ker Δ = N·G_Q; the relative quadratic characters are 0, Δ ⟺ N ⊆ cl([G,G]G²G_Q) | targeted proof check | **confirmed.** With B.2.25 or C.30 on record, the right-hand side fails |

### 2.2 Read at the level of the statement (119)

No statement read this way conflicts with another or with our record.
- **Item 1.** C7 says neither bit is a function of the 2-adic frames, with an actual inertia-square element whose 2-adic
  data are the identity and whose bits are (1,1).
- **Order five.**
  - T1-T2 and F1-F2 give an actual order-five norm-one frame character C₅ on GT̂ ∩ ker λ. It is built from the six-point
    stabilizer, so no descent to the five-point sphere group is assumed.
  - F3-F4 give the fifth-fibre and scalar characters.
  - F5: a common fifth-fibre bit is impossible.
  - F9: C₅ = (−1)^{κ₅}Ω₅ on G_{Q^ab}.
  - The comparison beyond Galois is open.
- **Level six.**
  - F6-F7 give the marked involution and two exact word equations for A.86.
  - F8 and L7 rule out the literal quaternion identifications.
  - F10 and F12 are pro-two and pronilpotent blindness results, conditional on the E.58 lifting input.
  - F11: the five-strand symplectic sign is 1.
- **Characters.**
  - C3: separation, through the LI.8 element, assumed.
  - C4-C5: the adelic CM images of y² = x³+1 and y² = x³−x over Q^ab, and the signed path comparison.
  - P15-P16: relative-seed and iterate limits.
  - C21-C22: the octahedral phase κ₃₂₄.
- **The finite Hurwitz programme.**
  - P1-P14, P17, P19-P33, F13-F17, F19-F21, F23-F44, C9-C35, H1, H3-H11: necessary conditions on a hypothetical mixed
    element, and finite-scope refutations of particular tests.
  - The run itself keeps these apart from actual lifts.
  - Given E.49, the mixed element does not exist. These conditions stay true and constrain nothing.

### 2.3 Verdict counts

| Verdict | Count |
|---|---|
| targeted proof check, confirmed (5 with a computation of mine) | 16 |
| confirmed, given supplied inputs I did not re-prove (L4, L5, C6) | 3 |
| deduction confirmed, resting on computations not rerun (H14) | 1 |
| read in full, computation not rerun (H12, H13) | 2 |
| read at the level of the statement | 119 |
| gap found | 0 |
| refuted | 0 |

The run's own check events: 140 of the 141 ids have at least one, and 86 have an event its workers call independent.
Their type field is free text (about 150 distinct strings), not the rubric's six types.

## 3. What is new

**Against the literature.**
- L1-L3 and L7 are elementary computations with Hilbert symbols (Voight, *Quaternion algebras*, 12.4.10-12.4.14, 14.2.1).
- C4 is the main theorem of complex multiplication applied to two curves (Milne, MF 1.10, Theorem 12.27).
- F18 is close to classical: GT̂ acts on the congruence completion through inner automorphisms.
- P18's isolated-orbit argument is the familiar rigidity trick for Nielsen classes, here for GT̂. Its form is likely
  folklore. Check before calling it new: Fried-Völklein, Collas 2012, and Schneps on dessins.
- D1 is a small new lemma as far as I know. Distribution relations in one finite target that Y normally generates impose
  nothing on the G′-value.
- The rest (F22, P13, C36, H2-H14, C6, C8) are statements about our objects: the gentle group GT̂₀ of LM7_PUSH, its frames
  and Δ. They are new in the sense that these objects are ours.

**Against tonight's runs.**
- **AN_GRH T01-T07** (cyclotomic-coordinate certificates for the finite levels of GT̂₀): no overlap. DELTA23 works at
  multiplier one and uses no GRH.
- **ALPOGE_BRIDGES F3** (the (2,3,6) orbifold E₀/μ₆ of the hexagonal CM curve): DELTA23's cubic detector E₀ =
  F₃² ⋊ SL₂(F₃), of order 216 (P10), is the affine group of the 3-torsion of the equianharmonic curve. I read it as the
  finite shadow of the quotient Ẑ[ω] ⋊ C₆ that Fable points to. This is my reading, not checked.
- **K17 on the tripod:** compare its Galois statements with C4-C5. Not done here.

**Against our own results.**
- A.84 = E.3: decided on record (§1).
- B.40: partly answered on record. B.2.25 and C.30 give infinitely many relative quadratic characters. C8 reduces "only
  0 and Δ" to N ⊆ cl(...), which therefore fails.
- C6 overlaps LM8_PUSH C.21 ("Δ is the unique nonarithmetic character through the two coordinates"). C6 is the form at
  every adelic level. I have not read C.21's proof.
- The open half of F22 (a₃ = a₃∘𝒟_E on GT̂) is GT_TOWER_CHECK A.5's e₃ = 0, which is derived there from A.7.

**New and of use to us:**
1. 𝒟_E, the cubic descent, as an actual endomorphism with Δ∘𝒟_E = d₂ (F22, P13). It is the equianharmonic counterpart of
   D_L and D_P, and it gives the second route of §1.
2. The 2-3 reading closed (§5).
3. The order-five frame character C₅ (F1-F2, F9).
4. ϑ, a Z/4 lift of the half-Kummer bit (C36).
5. The limits F12, F18, F21 and D1, which say which tests cannot see Δ.

## 4. Scope of the two proofs

- No statement of DELTA23 uses RH or GRH, for Dirichlet or for Hecke L-functions. The README says so, and the proofs I
  read confirm it.
- Masullo is not used.
- Alpöge's steps 3 and 5 (metaplectic reciprocity) are discussed in IMPLICATIONS.md only as analytic background. D23.L6
  refutes the metaplectic (Kubota) reading of the frames that Fable proposed.
- No statement claims more than its input gives. The claims that rest on the E.58 lifting input, LM7_PUSH D.50, which is
  not in the attachment, are marked conditional by the run: L4, F10, F12, F21, the refutation clause of F18, C6 (it uses
  the E.58 element) and C3 (the LI.8 element).

## 5. Fable's suggestion 1, checked

Suggestion 1 is by Claude Fable 5.2 at effort max, 20 Nov. It reads: "Δ is a reciprocity defect at the primes 2 and 3":
Δ(F) = χ₁₂(u(F)), with χ₁₂ = χ₋₄·χ₋₃ and Δ = ε₂ + ε₃ mod 2, so that E.3 becomes "do the hexagon and pentagon force
ε₂ = ε₃?".

| Part of the suggestion | What DELTA23 proves or refutes |
|---|---|
| Δ = χ₁₂ ∘ u | **Proved** in its typed form, (−1)^Δ = χ₁₂(u) (L1). Δ is additive and χ₁₂ multiplicative; I checked the four values |
| ε₂, ε₃ are local symbols at 2 and 3 of the pair of frames | **Proved only as an encoding**: L1 uses the bits to choose n. **Refuted** in every reading with content that was tested: the harmonic bit is no function of the 2-adic frames (C7); the Kubota symbol of the frames is 1 at both places (L6); the relative pro-3 data do not give a₃ (L4); the individual bits change with the Galois correction (L5). What is true: **both bits are 3-adic invariants of the frames** (L8) |
| Evaluate on E.58 | Done: n = 5, (L₂,L₃) = (1,−1) (L1) |
| "An element with unequal bits ... fails the product formula" | **Refuted** (L2): the global class (5,3) obeys Hilbert reciprocity, with its extra −1 at 5 (and (7,3) at 7). Requiring support only at 2 and 3 is **equivalent** to equal bits (L3), so the reciprocity form restates the gate and supplies no mechanism |
| The quaternion algebra (−1,−3) | It is not the discriminant-6 algebra (2,3) (L7). Fable's own values for (−1,−3) at 2, 3, ∞ are right |
| E.3 as "do the hexagon and pentagon force ε₂ = ε₃?" | Yes on our record (E.49, GT_TOWER_CHECK A.3/A.7), by rigidity of the Klein four-group at the ten-point configuration, not by reciprocity. DELTA23 neither proves nor uses this |

**What remains of the suggestion:**
1. The "2" of "2-3 reciprocity" comes from the CRT encoding of DELTA_ON_GT A.6. The frames carry both bits at 3, the prime
   where j = 0 and j = 1728 reduce to the same supersingular point (my reading of L8 with C7). Read this way, Fable's
   supersingular remark is the right picture: Δ compares two CM frames at the one prime where the two CM points meet.
   - Whether the supersingular endomorphism algebra (−1,−3) gives an invariant of the frame pair whose value is (−1)^Δ is
     not tested by the run. It is the one thread of the suggestion still open.
2. Whether the metaplectic or reciprocity material of Alpöge's steps 3 and 5 bears on Δ at all: nothing in DELTA23 says
   it does, and L6 removes the direct reading.

## 6. Integration (entries to make; I made none outside this folder)

1. **LM7_PUSH E.3 and DELTA_ON_GT A.84 rows** (register notes and the programme map): add "DELTA23 (checkpoint 06, 21 Nov)
   leaves it open in the run. The decision on record is EXIT_TOWER E.49 = GT_TOWER_CHECK A.3/A.7. Its gates are refereed
   (Claude Fable 5.2 at effort max, 18 Nov); its last step is not. DELTA23 H14 is implied by A.5 and A.7 and agrees."
2. **DELTA_ON_GT A.5** (the plain product formula does not compare the frames): add "Sharpened by D23.L2-L3: the global
   symbol obeys reciprocity, with a compensating place; support at 2 and 3 only ⟺ equal bits."
3. **DELTA_ON_GT A.103** ("the vanishing assertions remain open"): mark them proved by GT_TOWER_CHECK A.5, and add the
   intrinsic form of D23.F22.3, e₃ = a₃ + a₃∘𝒟_E, with Δ∘𝒟_E = d₂ (P13).
4. **DELTA_ON_GT B.40:** add D23.C6 (frame-factoring relative characters are 0 and Δ) and D23.C8 (the kernel criterion).
   Add that B.2.25 and C.30 make the space infinite, so C8's kernel image is nontrivial.
5. **DELTA_ON_GT A.24:** add D23.T1-T2, F1-F5 and F9 (the actual order-five frame character and its Galois scalar). Open:
   the comparison on GT̂ ∩ ker λ.
6. **DELTA_ON_GT A.86:** add D23.F6-F7 (the exact two-word criterion) and F18 (every congruence test is trivial). The full
   non-congruence comparison stays open, at lower priority now that Δ|GT̂ = 0 is on record.
7. **FABLE_PROGRAM_SUGGESTIONS_20261120.md, suggestion 1, and IMPLICATIONS_REPORT_20261121.md §5 item 1 ("Done"):** add
   the table of §5 above in one paragraph: identity proved; local-symbol readings refuted except the encoding and the
   3-adic formulas; product-formula failure refuted; support version equivalent to the gate; E.3 decided on record by
   another route.
8. **Grothendieck's texts:**
   - DELTA23 inspected cote 145 (*Printemps 81, vieille rédaction*), PDF pages 7, 11, 12, 22 and 28 = scans 6, 10, 11, 21
     and 27, and records PDF page = scan + 1 because of the cover. No reading changes.
   - It keeps DELTA_ON_GT B.24-B.25's caution that the manuscript's numerical β (scans 10-11) is not a modern frame
     coordinate.
   - Cote 143 was downloaded and not used.
   - The Longue Marche §47 locator (cote 140-3, folios 415-420, scans 229-240) is kept as a source-run locator only.
   - Entry for the cote-145 study notes: "the conjugating elements of scan 6 are the frames whose parities Δ compares; on
     GT̂ they agree (E.49/A.7); on the gentle group they need not (E.58)."
9. **`field_experts\HEXAGON_CANDIDATES.md`:** D1 at most, as a minor entry with its gates (§8).
10. **Record of the prompt error** (cause and fix, §1): in the prompt-building notes for the archive-research prompts.

## 7. Prompt updates

**For a successor of DELTA23, or a revision of the LM7_PUSH successor:**
1. **Attach and state the record:**
   - the rows: EXIT_TOWER E.44, E.49; GT_TOWER_CHECK A.1, A.3, A.5, A.7, B.1.8, B.2.1, B.2.25; LM8_PUSH C.21, C.23, C.30;
     SECTION_GHOSTS E.176-E.182;
   - the referee report.
   - Say that Δ|GT̂ = 0 is proved on record and that its last step has not been refereed.
2. **Main item: a second proof of Δ|GT̂ = 0 that does not use E.49's three-division step.** Prove e₃ = a₃ + a₃∘𝒟_E = 0
   on GT̂ ∩ ker λ, best through 𝒟_E|GT̂ = id. That is D23.F22.4 on all of GT̂, the equianharmonic counterpart of
   GT_TOWER_CHECK B.1.8, by the method of E.44 and SECTION_GHOSTS E.176 at an order-three locus. With A.5's d₂ = 0 and
   Δ = d₂ + e₃, it closes. State the result also in Grothendieck's terms, as the fixed-point equation of the
   equianharmonic descent on the Lego.
3. **Order five:** decide whether C₅ = (−1)^{κ₅}Ω₅ (D23.F9) holds on GT̂ ∩ ker λ. Use the Smith-theory method on the
   order-five locus of M_{0,5}. This is the character-level face of Nakamura-Schneps's (III′) question (referee report
   §5, item 3). State how the result bears on (III′).
4. **B.40:** determine the full group of relative quadratic characters of GT̂₀:
   - from B.2.25's χ_n, C.30's β-defects and d∘D^j;
   - prove that C.30's characters do not factor through the adelic frame pair, as C6 requires;
   - compute the image of N in Q (C8).
5. **Drop:**
   - the existence search for a mixed element by finite Hurwitz tests (moot given E.49);
   - the 2-3 reciprocity reading (closed by L2, L3, C7, L6, L7);
   - the pronilpotent and congruence level-six tests (F12, F18).
   - If the user wants an independent finite proof, it must target the depth where the obstruction lives (compactness,
     §1). The run's levels show that depth is beyond E₀ and the degree-1344 orbit.
6. **The one thread of Fable's suggestion still open:** whether (−1,−3), the supersingular algebra at 3, gives an
   invariant of the frame pair with value (−1)^Δ.
7. **Outside Pro:** the referee pass on EXIT_TOWER E.49 and GT_TOWER_CHECK A.3/A.7 is now the only gate of E.3 on our
   record. It is the next item for the Δ referee (results_register/delta_referee_20261118).

**For the running DELTA23:** its next hours go to the finite gate (1,0). That work cannot decide A.84 by itself unless it
reaches the obstruction depth. Whether to let it run to its own stop or stop it in the ChatGPT window is the user's call.
Nothing it does conflicts with the record.

## 8. Hexagon readiness

The five tests are: complete, self-contained (inputs published or formalized), stable, checked, of interest now.

| Finding | Passes | Gate left |
|---|---|---|
| D23.D1 (distribution relations in a finite target normally generated by Y are blind on G′) | complete; self-contained (free groups, finite groups, Enriquez 2007); stable; checked (my targeted proof check) | interest is narrow (a limit of one kind of test for cyclotomic associators); check δ_N against Enriquez's eq. (50) in the source; one paragraph on why it matters for GT̂ against cyclotomic GT. A minor candidate at best |
| D23.P18 (isolated Nielsen orbits are GT̂-stable) | complete; self-contained (Lochak-Schneps 1994); stable; checked (argument) | likely folklore; prior-art search first. Not a post as it stands |
| D23.L1-L3, L7 (the 2-3 reading) | complete; self-contained; checked | of no interest outside our programme; it belongs in the intake and the companion, not on Hexagon |
| D23.H14 | complete | not stable: superseded by GT_TOWER_CHECK A.5 and A.7 on our record |
| D23.F18, C36, F22, P13, C6 | complete; checked in part | not self-contained: they rest on DELTA_ON_GT and LM7_PUSH inputs (AD.1, AD.2, A.88-A.90, A.107, E.65), unpublished and unrefereed |
| Δ\|GT̂ = 0 itself (EXIT_TOWER E.49, GT_TOWER_CHECK A.7) | complete; stable | not DELTA23's; gate: the referee pass on E.49/A.3/A.7. With that pass it would be the strongest Hexagon candidate of this field, together with the refereed gate (relation (IV) on all of GT̂; Λ·G_Q = GT̂) |

No DELTA23 finding is ready for Hexagon.

## 9. Files

- This intake: `field_experts\intake_20261121\intakes\DELTA23\INTAKE_DELTA23_20261121.md`.
- Check events: `field_experts\intake_20261121\intakes\DELTA23\INTAKE_DELTA23_20261121_CHECK_EVENTS.tsv`.
- Work file: `agent_notes\20261121_intake_DELTA23_NOTES.md`.
- My check scripts (scratch, not part of the record):
  - `<local>/AppData\Local\Temp\claude\f2c80a22394db22f\e0d20ada-e036-40ad-83b1-31e9a63b69bc\scratchpad\d23_my_checks.py`;
  - `<local>/AppData\Local\Temp\claude\f2c80a22394db22f\e0d20ada-e036-40ad-83b1-31e9a63b69bc\scratchpad\d23_inventory.py`.
