# Intake of RESEARCH_SA17: representability (cote 131), descent (126-128), Barsotti-Tate and crystals (129), heights (130), λ-operations and groups (133)

- **The run.** GPT-6 Astra (ChatGPT Pro mode), on the prompt `pro_prompt_builds/RESEARCH_SA17/PROMPT.md`.
  - It started at 04:00:25 UTC on 19 Nov 2026 and saved checkpoint 01 at 04:45 and checkpoint 02 at 05:30 UTC.
  - Nothing came after. By the user's rule a run silent for hours ended at its last checkpoint, so checkpoint 02 is
    its final.
  - That is about 1 h 30 min of work. The three-hour progress review was never reached, so `PROGRESS_LEDGER.md` holds
    only two working snapshots.
- **The return**, `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA17_checkpoint_02_20261119T0530Z_unzipped/RESEARCH_SA17/`:
  - a report whose first line is INCOMPLETE. It is an outcome table plus computation logs; its "Corrections" section
    is a stub ("being consolidated").
  - a paper of 63 pages in seven section files, with 0 overfull boxes above 2pt by its own log;
  - a results register of 80 statements;
  - 100 check events, all by the run's own agents. By type: 21 targeted proof checks, 20 used and rechecked,
    7 computations, 3 independent re-proofs, 2 refuted, 5 "own proof" and 2 "own proof plus finite certificate"
    (types the prompt does not allow), 2 "primary source application", and several rows with a locator in the type
    column;
  - 24 programs with their logs.
- **Taken in by** Claude Opus 5.5 at effort max (agent ac8bd2a26d00b4f37, the reader of the Work folders K126-K132),
  19 Nov 2026, 11:46-12:10 UTC, within a bound of about 200k tokens. No sub-agents.
- **What I read.**
  - In full: the prompt; the report and ledger; the results register; `sections/A.tex`; `sections/A45.tex` lines
    1-384 (Lemma 1.3 of 127, Lemma 1 of 128); `notes/ROOT_STATUS.md`, `A_Artin_Rees.md`, `A_research.md`;
    `sections/unresolved.tex`.
  - In part: `B.tex` (conventions, B:NiceV, B:Kummer, B.3), `C.tex` (C.4 formal splitting), `D.tex` (opening), and
    the outlines of `A_gluing.tex` and `C.tex`.
  - One source, opened by me: Murre's Séminaire Bourbaki exposé 294 (Numdam).
  - Against our readings: K126-K132 (mine), `133_002-018_030-054.md` (a598c2df), `STUDY.md` (a34c0444, cotes 129
    and 131), and the cote 131 Pro transcription and notes.
  - **Not read:** the A_gluing proofs; A45 lines 385 onward (the 128 Théorème, A.5); the B.1 DVR derivation and the
    B.4 proofs; most of C.1-C.3; the D proofs; the PDF. The context guard stopped further literature reading at 70 %.
- **Files beside this one:**
  - `INTAKE_RESEARCH_SA17_20261119_CHECK_EVENTS.tsv`;
  - `intake_RESEARCH_SA17_20261119/check_A4_boundaries.py` and `.out`;
  - `intake_RESEARCH_SA17_20261119/check_D_conic_pencil.py` and `.out`.

  The scripts neither import nor run anything from the return.

---

## 1. The main answers

**A.1 (main), his representability theorem of cote 131 scan 14: open.** The run proves parts and states the gate.
- **Settled, checked here:**
  - **Condition 8° as written is not necessary.** Scan 14 puts no finiteness on the test scheme Z. A square-zero
    thickening of k[t] by ⊕_a k[t]/(t−a) gives an h_S whose modular locus is only the generic point. With Z locally of
    finite type, necessity holds.
    - The transcription agrees: scan 14's "fini" is struck, and scan 2's version has "Z ... fini sur S'".
    - This is a defect of wording, not of the theorem he meant.
  - **NR(b) of scan 16 (Corollaire 2) as written is not necessary.** The ink says "irréductible ... premier minimal
    p, I ⊂ p, Ip = 0". Take A = k[[t,ε]]/(ε², tε) with its embedded prime: h_{Spec A/I} satisfies the hypotheses and
    fails the conclusion.
    - The example was first proposed conditionally in the Pro notes of MPL_131 (RN020); the run credits them.
    - The corrected condition, a unique associated prime (A:NR-density), is exactly Murre's (F7). It is also his own
      scan 7 insertion "d'adhérence schématique".
  - **Corollaire 1 (étale) is proved:** an Artinian-test extension lemma (A:artinian-tests, proof read) plus Murre's
    Corollary 2.
- **Conditional, not checked here.** Assume the local schemes exist: F_{S_s} representable over every local base.
  Then 8° on finite-type tests gives an open étale locus (uniform Artin-Rees). That gives an algebraic space, and
  Stacks 0417 makes it a scheme.
- **The gate.** Derive those local representing schemes from 7° as written (actual modularity, not pro-modularity),
  and with them the constructibility of the modularity locus (L1).
  - Also open: Corollaire 2 (unramified), through "8° ⇒ Murre (F8)".
  - "Quasi-modulaire" and the gluing proposition are done only under stated hypotheses (A:formal-gluing,
    A:local-to-global; not checked here).
- **What the literature says, and the run's best find.** Murre, *Representation of unramified functors.
  Applications (according to unpublished results of A. Grothendieck)*, Sém. Bourbaki 17e année 1964/65, n° 294
  (talk of May 1965), is the published form of cote 131. I checked it on the Numdam text:
  - (F7) uses "only one associated prime";
  - Theorem 1 is the unramified theorem with (F1)-(F8), and its Note says "neither (F7) nor (F8) can be omitted";
  - Corollary 2 is the étale case;
  - a further note says the theorem holds "with 'unramified' replaced by 'locally quasi-finite'". That is cote
    131's theorem, stated there without proof;
  - the appendix, §4, Theorem (a)-(d), proves effective descent for separated locally quasi-finite schemes;
  - §3 applies it: "an abelian scheme A over a normal variety is projective" (cote 131 scan 17).

  This dates cote 131's programme to before May 1965. Our study had not found it.

**A.2.**
- **8° is not superfluous over a base of dimension 1.** Proved and checked here: A:ind-thickening, the ind-scheme
  colim Spec k[t,x]/(x², f_E(t)x). It satisfies 1°-7°, is finite over every local base, and fails 8° with Z = S.
  This answers his margin "Donner l'exemple-type (S de dim 1)".
- **L2 (7° from a strengthened 4°): open.** Murre's note that (F7) cannot be omitted concerns the unramified
  theorem; it does not decide L2.

**A.3 / L3: settled, and checked.**
- Descent from Ŝ to S (step 3 of his induction) is Murre §4, Theorem, case (d) (S' locally noetherian); I read it
  in the source.
- **The question of 126 scans 32-35 has the answer no.**
  - Take Hironaka's 3-fold: Y = P³ minus two lines, g the free involution, and V_Y the blow-up of the conics C, D in
    the two orders, glued.
  - Restricted to T' = Y − Q, which keeps one point P of the fibre over s, V_Y gives a projective T'-scheme with a
    descent datum that is not effective, because V_Y/g is not a scheme.
  - This is exactly his deleted-point construction with G = Z/2.
- The positive replacements, SGA 1 VIII 7.7 and 7.8 (finite locally free covers; compatible ample bundles), are
  standard.

**A.4: settled in its two lemmas, and checked here.**
- **127 Lemma 1.3 is true, with weaker hypotheses** (any f, U retrocompact). The flat closure G = im(F → j_*G_U) has
  cokernel Q in sections over a finite affine cover. Q ⊗ B is flat, so Q is flat by Artinian flatness descent
  (Stacks 051E; not opened by me, consistent with my test CE-019 of the K126-K132 reading). Proof read and found
  sound.
- **128 Lemma 1 (G_m against G_a) is false in every characteristic,** not only in characteristic 2.
  - Example: A = F_p[x,y,a,b]/(a^p, b^p, ε²), ε = ya − xb, I = (ε), A' = A_x × A_y (the punctured plane). The
    additive boundary image is {c_{p−1} = 0} and the logarithmic one is {c_{p−1} = c_0}.
  - I recomputed both images for p = 2, 3, 5, 7 and re-derived the reduction to k[t]/(t^p) by hand.
  - The exact always-valid replacement is Prop. A4:boundary: the kernels are H/δ(C_0) and H/{u⁻¹δu}.
- **The 128 Théorème (finite semi-local, GL_m against H¹) survives** by an independent proof (A4:finite-descent-theorem).
  Not checked here; the run marks its all-rank part "under final root audit".

**A.5: known.**
- Abelian schemes over normal locally noetherian bases have a relatively ample bundle. The fixed-P^N subtlety
  over a non-quasi-compact base is a counterexample of definition.
- Murre §3 carries the same application. Not checked further.

**B.1 / L5 (his V, cote 129 scan 115).**
- V holds up to isogeny for every p. Integrally it holds iff p ≥ 3 or 2A = 0.
- R3 is confirmed by a second party (the run): odd p integrally, and the reduction at 2.
- I checked the Kummer counterexample at p = 2: E_{±1} over Z_2 agree mod 2 with equal Hodge lines, and a lift
  forces r² = −1 with r ≡ 1 mod 2A, so 2 = 0.
- The complete-DVR derivation was written but not checked here.

**B.2: "known"** (the nilpotent-display theorem for both alternatives). Not checked here.

**B.3 (his conjecture of scan 114).**
- Positive classes come from the literature: quasisyntomic (Anschütz-Le Bras 4.74), p-basis and reduced
  PD-torsion-free (Lau), excellent lci (de Jong-Messing 4.6). Locators not opened by me.
- **The unrestricted conjecture is refuted** over F_p[x,y]/(x,y)², over two planes meeting at a point, and over its
  polynomial extension. The nonzero p-torsion crystalline scalar τ = γ_p(ac)γ_p(bd) − γ_p(ad)γ_p(bc) gives
  D(μ_{p^∞}) → D(Q_p/Z_p) with no group map behind it.
  - I checked pτ = 0, dτ = 0, φ(τ) = 0, the compatibility pτ = φ(τ), Hom = 0, and that these bases lie outside all
    positive classes.
  - **τ ≠ 0** rests on the run's "finite PD detector" (B:finite-PD), which I did not check. It is the one step to
    verify before the refutation is used.
- "A largest class" is open.

**B.4 / L6.**
- Δ*(G) is constructed (not checked here).
- **L6 as written is refuted, and the refutation is right.** L6 put Δ*(G) into the tensor formula of scan 94. The
  page has the finite Dieudonné module M, as our study says (SA17-6). The misquote is the Lead's.

**C.1 (his question of 133 scan 29, "Est-ce vrai si k est un anneau local ?").**
- Settled:
  - every Q-algebra (polynomial iff K_0(k) = Z);
  - every ring of positive characteristic (no);
  - regular noetherian rings (iff characteristic 0 and K_0 = Z);
  - Z and mixed-characteristic DVRs, Z_p included (yes).
- **Even torsion-free local rings of characteristic 0 can fail.** k = Z_(2)[u]/(u²−1) is local. The rank-one module
  with the transposition acting by u has class (h_2, e_2) on the two rational points, which is not in Z[ρ_1, ρ_2].
  Checked by that reasoning.
- The classification for all rings is open (singular modular fibres).

**C.2 / L7.** The ring of distinguished functors is determined. L7, read as a special-λ claim, is refuted by finite
certificates, and the T^n formula is corrected through partition types. Not checked here.

**C.3 / L8.**
- L8 is proved in characteristic 0. Split WG(BO_m) is determined in characteristic 0.
- Special λ-identities fail in every odd characteristic: ψ^p is not multiplicative on the modular Green ring of
  C_p. Not checked here.
- Positive characteristic for BO_m is open.

**C.4 / L9.**
- **L9 is refuted, and the refutation is right.** Heis(F_3)² and Heis(F_9) both have order 729, centre and derived
  group F_3², and the same crossed-module data. Their commutator pairings have rank distributions 16 + 64 against
  0 + 80, counted by hand here, so they are not isoclinic.
- **The formal splitting.** A Galois-twisted extension of μ_{p^∞} by μ_{p^∞} over F_p (Frobenius acting by a
  unipotent [[1,1],[0,1]] on the dual Tate module) does not split even up to isogeny. This refutes (I) with a
  "smooth" kernel, and (II), **over F_p, the scope our prompt asked for**. The page states no base field.
  - The run's own correction (2) shows the multiplicative case splits up to isogeny over an algebraically closed
    field.
  - Its correction (1) agrees with our reading: a kernel killed by p^N splits after [p^N].

**D.1 / L10 (cote 130), proved under his hypotheses; checked against my readings.**
- The rank ρ(J') = ρ(X) + H² − 2 minus the reducible-fibre excess. It agrees with my decided ink "ρ(X̃) − 2" (CR-018)
  and with "z = number of base points" (CR-019).
- The height formula Q = −(ξ·η) with irreducible fibres, as Shioda's.
- The local corrections v of scans 4-6 as inverse fibre intersection matrices, giving the component pairing.
- The conic-pencil example (three reducible members) shows the irreducibility hypothesis is needed; recomputed.

## 2. Where the run's tables overstate or understate

- **L4** is labelled "Refuted". L4 said 128 Lemma 1 fails in characteristic 2, and the run proves that and more. What
  is refuted is R2's "fine in odd characteristic". The label should read *proved, and strengthened to all p*.
- **A.1** "Literal necessity is refuted" refutes the wording of 8°, not the theorem meant. Scan 2's version has the
  finiteness.
- **B.3** "Refuted: the unrestricted conjecture" rests on τ ≠ 0 (the PD detector), which no second party has
  checked. It should be marked as resting on that lemma.
- **C.4** "Refuted ... (I) and (II) of scan 36" refutes the prompt's perfect-field scope. Over algebraically closed
  fields the multiplicative case holds. The table should say *over F_p*.
- **"Known" rows** (A.5, B.2, B.3 positive classes, C.1 for Z): the report does not show the derivations from the
  cited theorems that the prompt asked for. The register labels them Known all the same.
- **Missing:** the report's corrections section (file and line) is a stub. The 5 "own proof" check events are self
  checks, not second-party checks.
- **Understated:** the Murre 294 identification and the all-primes refutation of 128 Lemma 1 are not flagged as new
  for us in the report.

## 3. His text (claims about the pages, checked against our readings)

| Run's claim | Our record | Verdict |
|---|---|---|
| 131 scan 14: 8° has no finiteness on Z; scan 2's version has "Z fini" | MPL_131 transcription, scan 14 line 304 ("fini" struck) and scan 2 line 61 | agrees |
| 131 scan 16: NR(b) says "irréductible", "premier minimal 𝔭", I ⊂ 𝔭, I𝔭 = 0 | transcription line 335; Pro notes RN019-RN020 | agrees; our study's "domains" was wrong |
| 131 scan 14 margin "Non" does not by itself decide L2 | STUDY SA17-14 | agrees |
| 127 scan 3: the inserted parenthesis is A ↪ Γ(Y', O_{Y'}) | Work transcription K127-01 reads Γ(Y, O_Y), without the prime | **differs**; the mathematics needs Y' (Γ(Y, O_Y) = A trivially). Decided on the image at 600 dpi, 19 Nov 12:12 UTC: the ink has Γ(Y, O_Y), an author's slip (K126-K132-CR-025) |
| 128 scans 20-21: Lemma 1 asserts "un isomorphisme canonique" through 1 + z ↦ z | K128-02 transcription | agrees |
| 126 scans 32-35: the deleted-point construction | my reading SA17-28 | agrees |
| 129 scan 94: M, not Δ*(G), in the tensor formula | STUDY SA17-6 | agrees; the Lead L6 misquoted |
| 129 scan 115: V is stated "up to isogeny" | STUDY SA17-13 | agrees |
| 130 scan 14: the rank formula with its irreducibility hypothesis | my readings CR-018 and CR-019 | agrees; the run uses n = H² base points |
| 133 scan 36: (I) and (II) | a598c2df's reading | agrees on the text; the scope differs (see C.4) |
| 133 scans 6, 7, 26, 28-29 (WG by isometry classes and orthogonal sums; K_s against K; the finite-support reading of the blue marginal formula of scan 26) | not checked here | to verify |

## 4. Ours: where our readings, study or prompt were wrong

1. **R2 and my readings (CR-014, hunch 4):** "128 Lemma 1 is fine in odd characteristic".
   - My record said this held in the model k[s]/(s²). The prompt's R2 dropped "in the model".
   - It is false for every p: the model k[t]/(t^p) is the relevant one. Correction CR-014 must be revised.
2. **STUDY SA17-14:** NR(b) was described on "complete local domains". The ink says "irréductible", and the
   difference is the whole point of the example.
3. **Lead L6:** it put Δ*(G) in scan 94's formula. The page and our study have M.
4. **My hunch 2 (K126-K132):** "for relative dimension ≤ 1 I expect yes" in the deleted-point question. It is
   refuted by Hironaka's example, whose fibres have dimension ≤ 1 over a 3-fold base. Only a 1-dimensional base
   remains plausible.
5. **Prompt C.4:** "over a perfect field" is wider than the page. (I) and (II) fail over F_p for multiplicative
   kernels.
6. **Lead L1** (constructibility by noetherian induction from 8°): the naive induction fails, because modularity
   after a closed base change is not the original locus. L1 is not refuted, but its route is insufficient. The
   run's repair is conditional (Artin-Rees).
7. **Our study's literature for cote 131** missed Murre's exposé 294, the published form of the programme with exact
   locators.
8. **My reading of 127 Lemma 1.3** said "the comparison G ⊗ A' ≅ G' is the open part". The run proves it directly.
   My hunch 3 ("true") is confirmed, but by a different route, not through cote 128.

## 5. New results of the run

**Checked by this intake** (events in the TSV):
- A:ind-thickening;
- A:8-literal;
- A:NR-counterexample and A:NR-density (proof read);
- A:artinian-tests (proof read);
- A:nonfinite-descent (the adaptation of Hironaka's example to his deleted-point setting);
- A4:flatclosure;
- A4:boundary;
- A4:all-primes (computed for p = 2, 3, 5, 7);
- B:Kummer;
- C:local_charzero_counterexample (by reasoning);
- C:isoclinism_counterexample (by hand counts);
- C:formal_Frobenius_counterexample;
- D:rank, D:height and D:local, at the level of the statements against my readings;
- the D conic pencil (recomputed).

**Not checked here** (carried as the run's own):
- the conditional A.1 local-to-global theorem (Artin-Rees, Stacks 086R, 07RY, 03KV, 0417);
- A:formal-gluing and A:local-to-global;
- the 128 Théorème (A4:finite-descent-theorem, A4:derivation-orbits, A4:finite-rank-equivalence, A4:infinite-orbits);
- B:NiceV in full;
- B:DVR-classification;
- B:crystal-counterexamples' τ ≠ 0 (B:finite-PD);
- B:Delta;
- B:coLie-Dieudonne;
- most of C.1-C.3 (C:regular_noetherian, C:normal_domain_counterexample, C:torsion_generic_kernel, C:lambda_failure,
  C:odd_characteristic_failure, C:BO_positive_failure, C:charzero_lambda);
- C:central_twists.

## 6. Ink claims that need a reader on the scans

1. **127 scan 3:** the inserted parenthesis is Γ(Y', O_{Y'}) (run) or Γ(Y, O_Y) (Work transcription). The mathematics
   needs Y'. **Decided** on the image at 600 dpi (19 Nov 2026, 12:12 UTC, same agent): the ink has Γ(Y, O_Y), with
   no prime. The Work transcription stands, and the page has an author's slip (K126-K132-CR-025).
2. **131 scan 16:** "irréductible" against "intègre" in NR(b). The run inspected the image; the transcription agrees.
   This bears on correction 2 of section 4.
3. **131 scan 14:** that the struck "fini" in 8° attaches to S' and not to Z.
4. **133 scan 26:** the blue marginal formula, read by the run with finite supports (the basis of C:distinguished_ring).
5. **133 scans 6-7 and 28-29:** WG defined by isometry classes and orthogonal sums only, and K_s against K.

## 7. Literature locators the main answers rest on

| Locator | Used for | Status |
|---|---|---|
| Murre, Sém. Bourbaki n° 294 (1964/65), "(according to unpublished results of A. Grothendieck)": (F7), Theorem 1, Corollary 2, Note on "locally quasi-finite", appendix §4 Theorem (a)-(d), §3 abelian schemes over normal bases | A.1 étale corollary, NR density, A.3/L3, A.5 | **opened and checked by me** (statements; the in-text page numbers 245-247 not verified) |
| SGA 1 VIII 7.7, 7.8, 7.10; Hironaka's example (Stacks 08KE, 08J1) | A.3 | not opened by me (context bound); standard |
| Stacks 051E (flatness descends along injective maps from Artinian rings) | A.4 Lemma 1.3 | not opened; consistent with my test CE-019 |
| Stacks 0395, 02VI, 0417, 086R, 07RY, 03KV | A.1 conditional, NR density | not opened |
| Anschütz-Le Bras Thm 4.74; Lau (divided Dieudonné crystals) 7.6, 7.9, 9.3, 9.5; de Jong-Messing 1999 Thm 4.6 | B.3 | not opened |
| Messing LNM 264 V.1.6; Lau Remark 2.6 | B.1 | not opened |
| Tate 1967 §1.2-1.4, §2.2 | C.4 | not opened; standard |
| Shioda 1990 (8.11-8.13) | D.1 | not opened; consistent with my readings |

## 8. What the run did not reach, and what a finishing prompt must carry

**Open items, with gates and the approaches tried:**
- **A.1 (main).**
  - Gate: actual local representability over complete local bases from 7°, then constructibility (L1).
  - Tried:
    - Artin algebraization (needs excellence and versality);
    - general algebraic-space descent (not effective by itself);
    - naive noetherian induction (fails at closed base change);
    - formal completion (detects étaleness, not local-ring isomorphism).
  - Then: Corollaire 2 through "8° ⇒ Murre (F8)", and an unconditional "quasi-modulaire". Murre's proof of his
    Theorem 1 (§2) is the model to adapt to the locally quasi-finite case.
- **L2.** Tried: a henselised infinitesimal-group quotient, checked only on complete local tests. Neither fpqc descent
  nor colimits are proved.
- **A.4.** The all-rank part of the 128 Théorème is "under final root audit".
- **B.3.** "Largest class" in the literature. Also an independent check of τ ≠ 0, for instance by machine for p = 2,
  3, which the refutation needs.
- **B.1.** The DVR derivation, if the intake of a successor does not check it.
- **C.1.** Rings with singular modular fibres. The reduction is A:allrings_obstructions.
- **C.3.** WG(BO_m) in positive characteristic and non-semisimple cases.
- **C.4.** The non-commutative unipotent alternative of (I), and realisation without a baseline group. Also restate
  the scope: over algebraically closed fields, against perfect fields.
- **The report:** the corrections section with file and line, never written; the progress reviews.

**Files to restore from** (this checkpoint, nothing earlier is needed):
- `sections/*.tex`;
- `notes/*.md` and `notes/*.tex`, especially ROOT_STATUS, A_Artin_Rees, B_research, C_research, A45_D_research;
- `RESEARCH_SA17_results.csv`, `CHECK_EVENTS.tsv`, `checks_*.tsv`, `RESEARCH_SA17_references.bib`, `PROGRESS_LEDGER.md`;
- `code/` and `logs/`;
- the original three attachments.

**Items the intake settled, which a finishing prompt drops:**
- A.3 and L3;
- the dimension-one half of A.2;
- A.4's two lemmas (127 Lemma 1.3 true; 128 Lemma 1 false for every p);
- B.1's integral and isogeny answer, apart from the DVR derivation;
- L6 (misquote);
- L9;
- C.4's formal splitting over F_p;
- D.1 and L10.

**The A.1 gate rests on two lemmas,** "A:artinian-tests" (read here) and the conditional Artin-Rees theorem (not
read). A successor should carry the second as a statement to check, not as background.
