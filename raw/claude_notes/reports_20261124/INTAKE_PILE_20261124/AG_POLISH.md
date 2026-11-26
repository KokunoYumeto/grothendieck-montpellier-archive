# Cluster AG_POLISH: algebraic geometry, crystals, topology and periods, Grothendieck's own questions, counting

The cluster reader is Claude Opus 5.5 at effort high. The main session 329fb1e6 (Claude Opus 5.5 at effort max) launched
it on 24 Nov 2026, from about 21:10 UTC. It wrote this for the conference (Claude Fable 5.2).

Unless a run says otherwise, every run here is GPT-6 Astra (ChatGPT Pro mode). The runs do not expose their effort
setting.

**Abbreviation.** RR means `<local>/Documents/grothendieck_archive_transcription_20261110/research_returns/`.

**Files written.**
- This file, and `AG_POLISH_ITEMS.tsv` (39 rows).
- One check-event file per run: `INTAKE_<RUN>_20261124_CHECK_EVENTS.tsv`, 10 files with 18 events in all.
- Running notes: `agent_notes/20261124T2111Z_Intake_pile_AG_and_crystals_cluster_NOTES.md`.
- My program: the scratchpad file `agpolish/cv_check.py`.

**Coverage.**
- Most of these runs already had intakes, by field experts of 21-24 Nov in
  `field_experts/intake_20261121/intakes/<RUN>/`.
- Four sets of returns had none:
  - the POLISH_CRISTAUX merge run (cp33);
  - COUNTING_VARIETIES cp01;
  - the second SPLIT_ZERO_AFTER_FGJM run (cp08, 19:40 UTC);
  - the POLISH_ALGEBRAIC_GEOMETRY cp35 intake, which existed but is not in the ledger.
- For each run I say what is new since its last intake. I added my own spot checks on each run's main theorem.

---

## The cluster's most interesting items, ranked by usefulness

1. **K_{4k}(ℤ) = 0 for every k ≤ 20 (KTOWER).**
   - **What it is.** The vanishing of K_{4k}(ℤ) is the Vandiver-type statement for the Soulé characters. Through the
     Longue Marche tower it gives faithfulness of the pro-p action at the primes where it holds. Published unconditional
     vanishing reaches only small degrees (K_8(ℤ) = 0). Pintar's hexagon:2611.00829 reaches k ≤ 26, but under stronger
     simultaneous hypotheses, and our main session found ours not superseded by it.
   - **How each degree is killed.** The gcd of two U(3)/GL_2 comparison values, at p = 7 and p = 13, isolates the
     possible large primes. A unitary determinant over ℚ(√−7) and a cubic determinant on S_{2e+1}(Γ_1(7)) then kill
     each of them.
   - **Check status.** The deductions and every classical finite input were checked and recomputed by ad855737 (Claude
     Opus 5.5 at effort high, 22 Nov). Carried:
     - the U(3) computations;
     - the archive's Lean term `OneCharU_s` (its source trace confirmed, not compiled, no `#print axioms`);
     - the Kaletha–Mínguez–Shin–White inputs, whose stabilization prerequisites are not yet confirmed in print.
   - **Where.** RR/KTOWER_checkpoint_11_20261122T0001Z_unzipped/KTOWER.tex, lines 2674–4059; Hexagon row H18.
   - It ranks first because, if it stands, it is the result outside readers would most want. It also has the most
     carried inputs.

2. **A quantitative bound on Picard kernels (POLISH_ALGEBRAIC_GEOMETRY, Paper 2, thm:positive-excess-picard).**
   - **Statement.** On any normal projective surface in characteristic p, let M ≠ O have order p and be trivial on a
     smooth curve Y with Y² = d > 0. Then δ = 2g(Y) − 2 − md ≥ 0. Whenever [M] ∈ p^r NS(X), which includes every
     algebraically trivial M, (Q_r − 1)δ ≥ md. For r = 1 this reads δ ≥ pd/(2(p−1)).
   - **Why it matters.** It is the first quantitative obstruction for Grothendieck's question of whether Pic(X) → Pic(Y)
     is injective on points, which is also Kweon's Q7.7(i). It needs no ampleness.
   - **Check status.** The proof now has a different-model check end to end:
     - the induction and the NS lift by a018e2d2 (Claude Opus 5.5 at effort high, 24 Nov);
     - the three lemmas (resolution loss, root genus, resolved transfer) by me, here, every step. See section 1.
   - **Where.** RR/POLISH_ALGEBRAIC_GEOMETRY_checkpoint_35_20261124T0416Z_unzipped/workbench/papers/paper_02/main.tex
     l.151; the proofs are in `positive_square_picard_strictness.tex`.
   - It is board row P90e, and the best candidate for a short Hexagon note in the cluster.

3. **The special-inertia-character index on two complete wild bands, and a prescribed-field classification
   (POLISH_CRISTAUX, merge run cp33, Paper 2).**
   - **The bands.** For p ≥ 5, p ∤ k, ν_min(p, (p−1)p^v k, 2) is:
     - v + 1 at k = 1;
     - v + 2 for 2 ≤ k ≤ p² + p + 1;
     - v + 3 for p² + p + 2 ≤ k ≤ p³ + p² + p + 1.
   - **The prescribed field.** Over a prescribed complete DVR, exact-defect-two level-p² existence is classified:
     - it holds for every e ≥ p(p²−1)/2;
     - it fails below that for e prime to p;
     - for e = p(p−1)k it is a p-th-power condition on −p/π^e modulo π^{(p−1)β}, where β runs through the allowed lower
       breaks.

     Explicit fields of the same index on both sides show that the index alone does not decide existence.
   - **Why it matters.** It is Grothendieck's question on cotes 5–9 (SA15), answered on whole bands and for the first
     time over a fixed field.
   - **Check status.** The run made same-model separate reconstructions and comparisons. A512cf71 checked the reduction
     step behind the k ≤ p² band at thread-B cp22. I checked here the consistency of the band endpoints with thread A's
     mixed-ambiguity theorem, and the explicit prescribed fields against their own criterion. No other model has checked
     the recovery halves.
   - **Where.** RR/POLISH_CRISTAUX_checkpoint_33_20261124T2056Z_unzipped/POLISH_CRISTAUX_checkpoint_33/workbench/papers/
     paper2/paper.tex l.126, 6786, 6926, 7746, 7934. Note the extra folder level.

4. **Grothendieck's lattice question on cote 133, classified in the curvilinear case (NIGHT_GROTHENDIECK_QUESTIONS,
   Thm 26.1 and Cor. 27.3).**
   - **Statement.** Let A be finite free and local over a mixed-characteristic DVR, with edim(A/pA) ≤ 1. Then the
     symmetric-group lattice ring is polynomial on the trivial classes iff A is regular. Otherwise the generic kernel
     contains a split ⊕_ℕ ℤ/N, with N = min(n, pr).
   - **Check status.** Thm 26.1 (lines 1–600) and Cor. 26.3–26.4 were checked by a0805369 (Claude Opus 5.5 at effort
     high, 24 Nov), with a computation. Thm 27.1 and Cor. 27.3 are at statement level.
   - **Where.** RR/NIGHT_GROTHENDIECK_QUESTIONS_checkpoint_13_20261124T0037Z_unzipped/papers/A133_lattices/.

5. **#SAT inside one coherent Frobenius entry of a smooth Calabi–Yau hypersurface (COUNTING_VARIETIES cp01, new
   today).**
   - **Statement.** At each fixed p, a Boolean formula with S solutions gives a circuit-presented, smooth, geometrically
     integral hypersurface X ⊂ P^{d−1}_{F_p} with ω_X ≅ O_X and H^{d−2}(X, O) a line. Frobenius acts on that line by
     S mod p, and #X(F_p) ≡ 1 + S.
   - **Complexity.** Evaluating the scalar is #_pP-complete. Deciding that it is nonzero, which is equivalent to
     Frobenius splitting, is Mod_pP-complete.
   - **The run's own results.**
     - Stabilization over the whole coefficient space, for any multiple Q ≥ u + 2 of p, with an explicit smooth quartic
       K3 family over F_3 whose Hasse section is a.
     - A map of where sparse presentations become easy: a bounded number of equations, bounded support, bounded
       saturation cofactors.
   - **Check status.** I read the core proofs and checked them with my own program, in 15 of 15 cases. The K3 and
     worked-example counts match.
   - The main theorem was supplied by the prompt from our earlier construction (NEG_NIGHT C023 and C030–C032 lineage).
     It is the cleanest statement of "purity fixes the sizes, the count sits in a multiplicity".

6. **Monodromy of Frobenius on hypersurface sections of ordinary abelian surfaces (POLISH_CRISTAUX cp33, Paper 21).**
   - **Statement.** The relative geometric image is generated by transvections for every ample system. Nontrivial
     inertia holds on every Hasse component for L^n with n ≥ 4, for 3dΘ with d ≥ 2, and for every product cubic. The
     representation is absolutely indecomposable.
   - **Check status.** The run only. Not checked by another model.

7. **Grothendieck's weak-formal cohomology in degree one (POLISH_CRISTAUX, Paper 9).**
   - **Statement.**
     - Rationally it is rigid cohomology, for every smooth separated X (thread B, cp22).
     - Integrally, H¹ of a smooth proper X injects into H¹_cris. It is finite free of rank at most the rigid rank, with no
       lift needed (new at cp33).
     - It is not finitely generated in degree two on A¹.
   - **Check status.** Only the degree-two deduction was checked by another model (a512cf71).

8. **Int(R) is free for one-dimensional analytically irreducible local domains, refuting three conjectures of Elliott;
   concordance computations in dimensions 3–6 (POLISH_TOPOLOGY_PERIODS, Paper 2).**
   - The first result is already posted as hexagon:2611.00937 v1; v2 is pending.
   - The concordance results include a surjective Casson–Sullivan homomorphism for 3-manifolds with finite π_1. Our
     intake turned them into e-mails, ready on the user's word, correcting Galvin (Compositio 2026) and
     Orson–Powell–Randal-Williams (Crelle, accepted).

9. **Cote 136: Grothendieck's divided-power de Rham conjecture (ARCH_ALG).**
   - **Statement.** It is false strictly over every ring. In the homotopy reading it holds over every ring with finitely
     many non-unit primes.
   - **Check status.** The chain was checked by a0805369. The question over ℤ is open.

10. **Further rows.**
    - **JAC1964.** Cote 44 Th. 4 with the primitive part, conditional on OpenAI 032; and the corrected Th. 5 height
      formula. These are H11 and H04.
    - **SPLIT_ZERO_AFTER_FGJM, second run.** The exact circuit bound |E| + vc − 1 when at most two edges lack quadratic
      witnesses: progress on the pequalnp nodes L-meta-608 and 612.
    - **POLISH_ALGEBRAIC_GEOMETRY.** P90a, the very ample counterexample to Kodaira vanishing. It is posted, and v2
      awaits the user.
    - **NEG_NIGHT.** The catalogue of negative results.

---

## 1. POLISH_ALGEBRAIC_GEOMETRY (prompt 90): newest return cp35, 24 Nov 04:16 UTC

**Read.**
- The PRIMER (a018e2d2, updated to cp35) and the cp35 intake `INTAKE_POLISH_ALGEBRAIC_GEOMETRY_20261124_cp35.md`.
  The ledger does not record that intake; it is by a018e2d2 (Claude Opus 5.5 at effort high), 24 Nov ~11–12 UTC.
- `positive_square_picard_strictness.tex`, lines 1–450, in full.
- main.tex, lines 140–215.

**Useful or not: useful.** Paper 1 answers Grothendieck's cohomological-dimension conjectures of cote 31 negatively,
with sharp examples. Paper 2 holds P90a (posted) and the first quantitative Picard-kernel bound. Papers 3–5 are marginal.

**What it proved.** Statements are as in the PRIMER, section by section. The main ones:
- **P1 Thm 1.1.** An excellent Dedekind domain R of characteristic 0 with cd₂K = 1, while cd₂U = 2 for every nonempty
  open U. Confirmed by a018e2d2.
- **P1 Thm 1.2.** For A = W(F̄₂)[[t]], cd₂ Spec A[1/t] = 3. Confirmed at reading level.
- **P1 Thm 1.4.** Q(X, Y) is topologically finitely generated. Confirmed at reading level.
- **P2 Thm 1.6 = P90a.** A smooth surface in characteristic 2 with L very ample, h⁰(L) = 562 and h¹(L⁻¹) = 1. Confirmed;
  hexagon:2611.00936.
- **P2 thm:positive-excess-picard.** As in item 2 above. The induction was checked by a018e2d2; the lemmas by me (see
  below).
- **P2 thm:conductor-equality-structure and the exclusion of a = 6.** Confirmed by a018e2d2, with Gu–Sun–Zhou,
  Shepherd-Barron and Furukawa unread.
- **P2 G1.** Confirmed.
- **E4, the local-group theorems 1.7–1.9, the endpoint sections.** Statement level.
- **P3 Thm 1.2.** Confirmed, except Prop. integral-descent.
- **P4 Thm 1.1–1.2.** Confirmed for the algebra part.
- **P5 Thm 1.1.** Confirmed.

**New since the last intake.** No new return: cp35 is the newest. New here are my checks of the three lemmas behind
positive excess, which a018e2d2 had left at statement level:
- **Resolution loss.** I checked:
  - the Leray χ argument for p_a(f₀*D) = p_a(D);
  - 2(Δ_D − Δ₀) = λ₀ + K·E, with K·E ≥ 0 after the (−1)-contractions;
  - the blow-up loss μ² ≤ 2μ(μ−1).
- **Root genus.** I checked:
  - the conductor h^{a(p−1)}, from the two bases;
  - ω_D = H ⊗ J|_D;
  - deg H = pG − m(p−1)d, which gives (p−1)δ = ℓ + 2Δ_D.
- **Resolved transfer.** d_T ≥ pd − 2(p−1)δ, and δ_T ≤ (1 + 2(p−1)a)δ.

All three hold. With a018e2d2's check of the induction, the theorem has a complete different-model check. Only the odd-p
strictness clause and the characteristic-2 endpoint sections remain at statement level.

**Open.**
- Existence or exclusion of a nontrivial geometric Picard kernel with positive excess below the bound, for classes
  outside p^r NS. The run concentrates on the characteristic-2 smallest endpoint: d = 4χ, 2d < K² < 3d, very ample needs
  d ≥ 12.
- Merely ample residual branches.
- Kweon's Q7.7(i).
- The uniform wild bounds for local groups (F13).

**Relations.**
- POLISH_CRISTAUX Paper 1 uses the same Raynaud–Mukai/Tango surfaces, with y² + y = x¹⁵ and h⁰(L⁹) = 556.
- Literature: Esnault (2006), Langer, Ekedahl I.2.4, Kweon arXiv 2008.01908v2 p.19, Popescu 2022 §5, Suzuki 2024.
- Grothendieck: cotes 31 (cd), 131 (Murre's representability), 14 (Albanese equivalence), and SGA 2 XIII Conj. 3.1 for
  the metabelian quotient.

**Candidates.**
- Post P90a v2: `reports_20261123/p90a_note`. It fixes the dimension-0 gap of v1's Theorem 2.
- A short note P90e on positive excess. Its remaining gate is a literature pass (Langer; Esnault 2006).
- The e-mails to Zheng, Mukai and Esnault, in `EMAIL_DRAFTS_POLISH_ALGEBRAIC_GEOMETRY.md`. Esnault's Remark 2.3(2) was
  added and checked by a018e2d2.
- Next prompt: none while the run lives. Afterwards, split Paper 2 (152 pp., four topics).

**Problems.**
- hexagon:2611.00936 v1, Theorem 2, is false for X = Spec k. It is fixed in v2, which is not posted.
- No paper has the "Proof overview" box.
- Paper 2 is not postable as one paper: the run's current-PDF readings stand at 0 of 152 pages.

## 2. POLISH_CRISTAUX (prompts 92, 92b, 92c): three threads

**Read.**
- The PRIMER (a512cf71, Claude Opus 5.5 at effort max) for thread A's final and thread B's cp22, and the thread-B cp22
  intake.
- For the merge run cp33 (no intake before this one):
  - README, REVIEW_STATUS.md, CONTINUATION_CURRENT.md and PAPER_NUMBERING.tsv;
  - NEW_RESULTS.tsv: all 58 rows, with the full statements of the main ones;
  - the QUESTIONS.tsv gates A.3, A.4, B.3, B.4 and E.10;
  - the CORRECTIONS_FOR_AUTHORS section list.

**Useful or not: useful.** The run is the strongest in the cluster by volume. Its useful papers are:
- Paper 1: integral crystalline weak Lefschetz fails;
- Paper 2: the inertia-character index;
- Paper 9: weak-formal cohomology;
- Paper 21: monodromy.

Many of the other 21 papers are marginal or near-known (Papers 3, 8, and the E.x "known" rows).

**The threads.**
- **Thread A's final** (23 Nov 18:48 UTC; 18 papers). Intake a512cf71 (final). Its first-boundary package at
  k = (p²+1)/2 is vacuous given thread B: A's normal form is the hypothesis of B's exchanged case, which forces
  p² | k + (p−1)/2.
- **Thread B's cp22** (23 Nov 21:45 UTC; 21 papers). Intake a512cf71. It added:
  - the complete band 2 ≤ k ≤ p² (ν = v + 2);
  - Paper 9 thm:nolift (rational = rigid), the integral injection, and the H² torsion;
  - Paper 21 Hasse reducedness and the natural GL_8 blocks.
- **The merge run 92c, cp33** (24 Nov 20:56 UTC; started 12:41 UTC; 21 papers, 643 pages, 557 formal statements, 58 new
  merge results). **New since every earlier intake:**
  - **Paper 2.**
    - thm:extended-wild-band: ν = v + 2 up to k = p² + p + 1.
    - thm:cubic-wild-band and thm:geometric-endpoint-band: ν = v + 3 on p² + p + 2 ≤ k ≤ p³ + p² + p + 1, recovery by
      p^{v+4}-torsion over every permitted field.
    - The elliptic index: v + 1 for k ≤ (p−1)/2. And cor:elliptic-lower-obstruction: at e = 2(p−1)p^v the sharp
      full-class lower comparison is not realized by elliptic curves.
    - thm:fixed-wild-exact-criterion, thm:fixed-wild-field-obstruction and thm:prescribed-level-two: the prescribed-field
      classification of item 3.
    - prop:half-square-exclusion: no comparison at e = (p−1)p^r(p²+1)/2, which closes thread A's boundary directly.
  - **Paper 9.** thm:proper-finiteness: H¹(C_X, O) ↪ H¹_cris, finite free, no lift.
  - **Paper 21.** Nine new statements: transvection generation, local Artin–Schreier inertia, every-component inertia
    under quadric cut-out (hence for L^n, n ≥ 4), every product cubic, stable corank one on every determinant component,
    and absolute indecomposability.
  - **Paper 18.** The complete list of elementary divisors of the Lubin–Tate comparison, for every prime including 2.
  - **Paper 19 (B's old Paper 18).** In even degree the invariant covectors have geometric dimension exactly 3.
  - **Paper 12.** A universal two-support theorem for every odd prime; prime 19 settled for all 511 supports. Gate:
    supports of size ≥ 3 at primes ≥ 23.
  - **Paper 11.** Four odd thin-system results.
  - **Paper 10.** A quantitative specialization bound, e ≥ 2 + 2^{v₂(D)+f+1}.
  - **Paper 6.** Generic ordinarity for every ample complete system with nonempty smooth locus.
  - **Renumbering.** Paper 18 = A:18 + B:19 (Lubin–Tate); Paper 19 = B:18; Paper 9 = B:9.

**What it proved: the run's own check status.** The run marks every statement "CURRENT_CHECK_SCOPE_RECORDED": separate
same-model reconstructions frozen before the proofs were exposed, then full comparisons. Its review06 (20:42 UTC)
recorded movement, and the run was still going at cp33. Checks by others:
- **a512cf71** (Claude Opus 5.5 at effort max):
  - cp12: Paper 1 every step; Papers 3 and 4 targeted;
  - cp18: the Paper 8 transvection lemma, and the Lubin–Tate mechanism;
  - final: the MW half of Paper 9, the α₂-theta descent, and computations for Paper 8;
  - cp22: the single-exception reduction, given three carried inputs (rc-lem:newton, pg-lem:primitives,
    prop:wild-two-slope-patterns), and the H² deduction.
- **My checks of cp33.** Both are computations, and neither proves the theorems.
  - The prescribed-field fields satisfy their own criterion: δ_{k,j} = (p−1)β_{k,j}, δ < e, p ∤ δ, and the threshold
    case gives δ = 0.
  - The band endpoints agree with thread A's thm:mixed-all-indices. A mixed ambiguity at level p^{v+3} exists iff
    k ≥ p² + p + 2, exactly where v + 3 starts.

**Open (the merge run's gates).**
- Paper 2: higher fixed-wild levels; multipliers beyond p³ + p² + p + 1; a fresh reconstruction of the old foundation.
  Wild invariant-DVR existence and the attainment at e = 162 have no fresh reconstruction.
- Paper 9: rational higher degrees, and finite generation of nonproper integral H¹.
- Paper 21: the full eventual image, Hasse and representation irreducibility, non-product every-component inertia, and
  an effective R.
- Paper 10: global determinant nonvanishing.
- Paper 12: supports of size ≥ 3 at primes ≥ 23.
- Papers 15, 17 and 20: a current-session main reconstruction.
- QUESTIONS rows B.2, B.4, D.1, E.7 and E.10 are still "MERGE_RECONCILIATION_PENDING".

**Relations.**
- POLISH_ALGEBRAIC_GEOMETRY: shared Raynaud surfaces.
- Literature: Hattori, Bondarko, Ozeki–Yoshida, Liedtke–Matsumoto Ex. 5.10, Lau (Breuil windows), Ogus, Katz–Messing,
  Bergh–Rydh, Caucci, Forsberg.
- Grothendieck: cotes 5–9 and 100 (crystals). Paper 9 is his weak-formal site; Papers 2 and 18 are p-divisible groups
  and Dieudonné lattices.

**Candidates.**
- Board rows:
  - "The complete wild bands and the prescribed-field level-p² classification" replaces a512cf71's cp22 row;
  - weak-formal H¹ with proper finiteness;
  - Hasse inertia and transvection generation.

  None is ready: there is no different-model check of the recovery halves or of Paper 21.
- Wait for 92c's final before any next prompt.
- Corrections:
  - **Grammatica, Remark 4.6:** draft ready, worth sending.
  - Rains–Sam, Dimca–Greuel, Bhatt: typos.
  - **New in cp33, not checked by us:**
    - Peel (1971), the proof of Thm 2: Im η should be ker η;
    - Stacks Tag 07P2: z^p − x should be z^p − x^p;
    - Stacks Tags 079Z and 0EVY: proof notation;
    - Achter–Pries (2008): two local discrepancies.

**Problems.**
- The two threads use "k₀" for different numbers: A's (p²+1)/2, B's p² − (p−1)/2. Rename one at the merge.
- cp33's NEW_RESULTS.tsv has an empty `check_events` column for all 58 rows. The check scopes are only in REVIEW_STATUS
  prose and the audit folder.
- REVIEW_STATUS says the "1595-row overlap artifact … has not been located". That number is our intake's computation
  (a512cf71's check of 1,595 cases), not a run file, so the run cannot find it. Say so in the next message to the run, if
  there is one.
- Paper 2 is 221 pages; it is not a posting unit.

## 3. POLISH_TOPOLOGY_PERIODS (prompts 91, 91b): newest return cp26, 24 Nov 00:34 UTC

**Read.**
- The PRIMER and the cp26 intake, both by a9e9559d (Claude Opus 5.5 at effort high).
- Paper 2 main.tex: the result-3 statement (l.208) and its proof (l.1462–1530).

**Useful or not: useful.**
- S20 settles Elliott's published conjectures.
- The concordance results are timely against two 2026 papers.
- Papers 3–5 are marginal but exact. Papers 6–7 are known in substance.

**What it proved.**
- **S20.** Int(R) is free (Paper 2, `analytic_freeness.tex`). The finite-conductor case was checked; it is posted as
  hexagon:2611.00937.
- **The non-flat forest plethory.** Checked.
- **PL components in dimension ≥ 6.** The S³ PL/TOP discrepancy (π₂ = ℤ/2), dimension-5 surjectivity, Casson–Sullivan
  surjectivity, T³, ℝP³. Statement level.
- **The torus, π₀P((S¹)^d) = F₂[ℤ^d]/F₂ (d ≥ 6).** I checked the Wh₃(ℤ^d) = 0 and Wh₂ = 0 computation: the Laurent
  decomposition of K₃(ℤ[ℤ^d]), and the framed assembly hitting every nonconstant summand. Igusa 1984, Thm 8.a.2, is
  carried.
- **Paper 1 tubes and stones; Paper 3 dimension table and the counterexample y² = x³ − x + 1; Paper 4 single cap and
  eigenmodules; Paper 5 crosscaps.** Checked as in the PRIMER.

**New since the last intake.** No new return. The run was active at its last capture: its review 14 found movement.

**Open.**
- A124: injectivity in dimension 5.
- A401/A402 and A701–A704.
- The seven-axiom comparison and King 1985.
- 564 original rows: 106 in Paper 2, 292 in Paper 4.

**Relations.**
- Literature: Hatcher–Wagoner, Igusa (LNM 1046), Galvin 2026, Orson–Powell–Randal-Williams 2026, Elliott (MathOverflow
  75202, 2013).
- The algebra half of Paper 2 (integer-valued polynomials, plethories) touches λ-rings and Grothendieck's binomial rings.

**Candidates.**
- S20 v2, which credits Elliott.
- The e-mails, ready on the user's word: EMAIL_READY_Galvin, _Orson, _Elliott and _Boyle.
- Board rows P91i (Casson–Sullivan) and P91j (embedded smooth partitions).
- Split Paper 2 into four in the successor prompt.

**Problems.**
- The PRIMER says π₀P_CAT((S¹)^d) = F₂[t^{±1}]/F₂·1. The paper has the d-variable Laurent ring
  F₂[t₁^{±1}, …, t_d^{±1}]/F₂, which is correct; the PRIMER is imprecise.
- No paper has the proof-overview box.

## 4. ARCH_ALG (prompt 50): final, 22 Nov 06:22 UTC

**Read.**
- Intake `INTAKE_ARCH_ALG_20261122_final.md` (a0805369, Claude Opus 5.5 at effort high) and its primer.
- `research/cote15/cote15_honda_check.tex`, l.1–80.

**Useful or not: useful** for cote 136; marginal for cotes 134-8, 15 and 123.

**What it proved.**
- **AQ-136-SEMILOCAL, FRACTIONS, ARITH-BOUND.** Confirmed by a0805369.
- **ARCH-134-01..03.** Confirmed given F-SM-34.
- **ARCH-15-HONDA-CHECK.** Confirmed. I recomputed (η) = 𝔭³, γ = 12 − 4s, the invariants 1/3 and 2/3, index 3 and
  dimension 3: a third recomputation.
- **ARCH-123-COUNT.** Confirmed by a0805369's computation for n ≤ 9.

**New since the last intake.** Nothing: the run is final.

**Open.**
- Cote 136 over ℤ. The gate is one weight cutoff for all primes.
- The bare Thm(?) of cote 134-8.
- A unique distinguished class for cote 123.

Parts B and C of NIGHT_GROTHENDIECK_QUESTIONS were meant to continue these, and never ran (section 9).

**Relations.**
- SEED_ARCH_ALG and ALPOGE_BRIDGES.
- Literature: Cartan, Miller, Cenkl–Porter (not yet compared), Honda–Tate (Tate, Bourbaki 352).

**Candidates.**
- The Thakur e-mail, `EMAIL_READY_Thakur_20261124.md`, in the NIGHT_GQ intake folder.
- A cote 136 paper, after a literature pass.

**Problems.**
- The register row ARCH-136-NONCYCLIC-ZEROFORM-QUOTIENT-OPEN is named OPEN although its first clause is refuted.
- About twenty cote-136 modules sit under `research/cote15/136/`.

## 5. KTOWER (prompt 47): newest return cp11, 22 Nov 00:01 UTC

**Read.** The PRIMER and the cp11 intake, both by ad855737 (Claude Opus 5.5 at effort high).

**Useful or not: useful.** This is item 1 above.

**What it proved.**
- K_{4k}(ℤ) = 0 for k ≤ 20.
- Vandiver for the components of order ≤ 4 and of order 6. The order-5 components have total length ≤ 1.
- e⁴/4: statement level.
- The pole theorem K17-POLE-GENERAL: every step confirmed.
- NC01–NC04, the effective class-number and height bounds (H15): confirmed given the cited theorems.

All of these were checked by ad855737 as listed in the PRIMER.

**New since the last intake.** No new return; cp11 is the run's last.

My one check here re-proves the Soulé counterexample independently: ζ₇ acting on ℤ[ζ₇] gives an element of order 7 in
GL₃(O_{ℚ(√−7)}). The refined bound p ≤ 1 + rN is consistent with it.

**Open.**
- Vandiver at order 5 (one class) and at order ≥ 7. The gate is arithmetic: an Euler-system or Stickelberger
  annihilator. Size bounds stop here even under GRH.
- Ihara beyond Greenberg: triple non-vanishing.
- Route 2 of cote 149.

**Relations.**
- The Longue Marche tower (LM6 A.44–45, Esquisse §2); cote 149.
- Literature: Soulé, Rognes–Weibel, Hart–Harvey–Ong, KMSW, Berger–Klosin Lemma 6.8 (not judged), and Pintar
  hexagon:2611.00829.

**Candidates.**
- An H18 note. Gates:
  - compile the archive term and run `#print axioms`;
  - an independent U(3) computation at e = 40 over both fields;
  - name the KMSW conditional inputs;
  - a literature search.
- A successor prompt as in the cp11 intake, section 5.

**Problems.**
- 19 rows of the run's CHECK_EVENTS.tsv carry the date in the statement-id column.
- Several of our earlier statements were superseded; they are listed in the cp11 intake, section 6. One of them: "K_{4k}
  = 0 follows from RH" is false wording.

## 6. JAC1964 (prompt 40): final cp06, 21 Nov 05:21 UTC

**Read.** The PRIMER and both intakes, by a8d75352 (Claude Opus 5.5 at effort high).

**Useful or not: useful.** It gives cote 44 Th. 4 in its margin's primitive form, and Th. 5 corrected. The successor run
is C44_POS, which is not in this cluster.

**What it proved.**
- JAC-T4.1 to T4.5: Th. 4, conditional on OpenAI 032 Cor. 8.4 (van Hoften–Sempliner; Milne's report, unrefereed).
- JAC-P03: without the primitive part, Th. 4 is false.
- H9-C1 counterexample, the H9-T1 corrected formula, H9-T2, H9-T7 (the height-group isometry), H9-T17.

All have targeted checks by a8d75352. I re-proved H9-C1's intersection numbers: (−1)^m(Λ − Λ′)² = 2 in both parities,
and Z|_Y = 0.

**New since the last intake.** Nothing.

**Open.**
- QH9-axis: the fixed-axis sign in characteristic p, m > 2. This went to C44_POS and to NIGHT_GQ Part C, which never
  ran.
- Q35-full: ker AJ₅ = 0 over ℚ.
- The Bost comparison.

**Relations.**
- SIGN_NEXT SN-44-01..05, HODGE_SIGN AR-01, C44_POS.
- Literature: Kahn's refined height pairing (arXiv 2009.00533v7), S.-W. Zhang, Saito (Nagoya 75), SGA 7 XVIII.

**Candidates.** H11 and H04, as on the board.

**Problems.** Th. 4 depends on unrefereed inputs. Say so wherever it is cited.

## 7. NEG_NIGHT (prompt 54): newest return cp15, 22 Nov 07:19 UTC

**Read.** The PRIMER (a8d75352) and the intakes by a17221e5 and a8d75352 (all Claude Opus 5.5 at effort high).

**Useful or not: marginal overall.** The useful part is NN-C005 and C023–C028: counting and parity carried by Frobenius
scalars and motives. COUNTING_VARIETIES grew from it. NN-A001 corrects our own consult.

**What it proved.** 164 findings: A001, A017, C005, S001–S003 and G-series checked, as in the PRIMER. I re-proved C005
here: N mod 2 is the top coefficient of the multilinearized ∏(1 + f_i).

**New since the last intake.** Nothing.

**Open.** The gate table of PRIMER §5: odd-mode cancellation, PIT and isolation, and the 932 enumeration.

**Relations.**
- COUNTING_VARIETIES (C023 → CV-THM-MAIN).
- SPLIT_ZERO_AFTER_FGJM (A001's criterion reappears as P2-zero-motion-half-share).
- GCT VIII.

**Candidates.** The Hexagon NEG row, when its whole-proof checks and literature are done. Not now.

**Problems.** None new.

## 8. NIGHT_GROTHENDIECK_QUESTIONS (prompt 76): newest return cp13, 24 Nov 00:37 UTC

**Read.** The cp13 Part A intake (a0805369) and the primers for Parts A (a0805369), B (a9e9559d) and C (aaf69461).

**Useful or not: useful** for Part A on cote 133. Part A's cote 15 and cote 123 papers are unchanged since cp04.

**What it proved.**
- Thm 26.1, Cor. 26.3 and Cor. 26.4: checked by a0805369.
- Thm 27.1 and Cor. 27.3: statement level.
- Thm 13.1 (computation), Thm 18.1 (mesh and surface lemmas), Cor. 18.8, Thm 23.1 (quadratic orders), Thm 24.1, 25.1
  and 30.1.
- The cp04 results: characteristic 0 is necessary; flat dual numbers have a nonzero class; square-zero extensions.
- Cote 15: the central CM formula, Prop. 5.2.

I re-proved Thm 18.1's surface lemma: div(X) = n·(X, t) on O[[X,t]]/(g(X) + tⁿ).

**New since the last intake.** No new return.

**Open.**
- A133: non-curvilinear singular rings (edim ≥ 2); an intrinsic criterion for normal singular rings; exact kernels over
  ramified DVRs.
- A15: the minimum.
- A123: a natural class.
- **Parts B and C never started.**

**Relations.**
- ARCH_ALG: Part B was to continue cotes 136 and 134-8.
- JAC1964 / C44_POS: Part C is axis positivity.
- Literature: Burke–Walker, Blumberg–Gepner–Tabuada, Swan and Gersten (attribution fix).
- Grothendieck: λ-ring generation by the trivial classes, cote 133.

**Candidates.**
- Board rows A133a (replacement text) and A133b (the regularity criterion), from the cp13 intake §5.
- The Thakur e-mail (ready).
- A separate prompt for Parts B and C. As written, the sequential rule means they will not run inside prompt 76.

**Problems.** The prompt's three parts were sequential, and Part A absorbed the whole night. Do not design another
multi-part prompt this way.

## 9. COUNTING_VARIETIES (prompt 63): cp01, 24 Nov 20:15 UTC; no earlier intake

**Read.**
- README, CHECKPOINT_STATUS, LEDGER, STATEMENTS.tsv (52 rows) and main.tex.
- `sections/introduction.tex` and `core.tex` in full.
- The statements of the presentation theorems.
- Prompt 63, lines 1–70.

The return has an extra `COUNTING_VARIETIES/` folder level.

**Useful or not: useful.** The main theorem is a clean, exact link between counting complexity and coherent Frobenius
on smooth Calabi–Yau hypersurfaces. The run's own additions are real refinements: stabilization over the coefficient
space, and the presentation boundaries.

**What it proved.**
- **CV-THM-MAIN.** As in item 5. The prompt supplied it from our earlier construction, and the run re-proved it.
- **CV-THM-STABILIZER.** Any multiple Q ≥ u + 2 of p. With the K3 family yz(r² − as²) + y⁴ + r⁴ + s⁴ − rz³ over
  F₃, #X_a(F₃) = 13, 11, 15.
- **CV-PROP-SPLITTING.** Nonvanishing is equivalent to Frobenius splitting.
- **sp:thm:bounded.** A fixed number of sparse equations is polynomial at fixed p.
- **sp:thm:bounded-cofactors.** Saturated principal ideals with bounded cofactor degrees are polynomial.
- **sp:thm:support and sp:thm:support-strip.** The cost is T^{c(p−1)}p^K, with K = (p−1)Σσ_i − m.
- **sp:thm:odd-linears.** Mod_pP-complete with three-term linear equations and one sparse nonlinear equation.
- **sp:thm:trinomials.** A projective presentation by trinomials.
- The structured, arrangement and fixed-field sections.

**The run's check status.** The core lemmas are marked "proof checking in progress". The structured section has
targeted checks and two independent re-proofs.

**My checks.**
- **Program** (`cv_check.py`). For 5 formulas at p = 2, 3 and 5, h_p(G) = S mod p and h_p(F_G) = h_p(G), in 15 of 15
  cases. The K3 counts 13, 11 and 15 match. The unit-clause decic has 19,907 affine and 9,953 projective points, as
  printed.
- **Targeted proof checks.** I followed every step of the stabilizer (z-exponent forcing, the empty gradient locus) and
  of the coherent-line lemma (connecting map; sign of the point count).
- **Independent re-proof.** The vanishing clause of sp:thm:support.

**New since the last intake.** Everything; this is the first intake.

**Open (the run's ledger).**
- Saturation-only sparse generators in fixed codimension with unbounded cofactor degree.
- Sparse coordinate changes and sparse multiples.
- The odd-prime support boundary.
- Scheme-preserving compression over the input field.
- Recovering hidden split coordinates without a designated quadric span.
- Small total Betti number versus rank-one coherent cohomology.

**Relations.**
- NEG_NIGHT C005, C023–C032 (ancestors).
- Katz, "Algebraic solutions …", Alg. 2.3.7.14 and Special Case 2.3.7.17, pp. 35–36 (credited).
- Wan's sparse counting theorem; Kudo; Valiant; Cheng–Rojas–Wan; SGA 2 XII Cor. 3.7.
- Grothendieck's frame: the Frobenius action on H^{top}(O) as the "Hasse–Witt" piece of the λ/F-structure. Weights do
  not help: purity fixes |eigenvalues|, while the count is a multiplicity.

**Candidates.** None until the final. The run has reviews at 23:30 Berlin and then hourly. After the final, consider a
Hexagon note on stabilization plus the main theorem, citing our earlier construction honestly.

**Problems.**
- QUESTIONS.tsv at cp01 holds only its header.
- 19 of 52 STATEMENTS rows have no title.
- The main theorem's "proof checking in progress" is the run's own wording. It is not a failure.

## 10. SPLIT_ZERO_AFTER_FGJM (prompt 93): first run cp08 (24 Nov 03:28 UTC); second run cp08 (24 Nov 19:40 UTC)

**Read.**
- The PRIMER and intake of the first run's cp08, by a2fedc2a (Claude Fable 5.2 at effort max).
- For the second run: CONTINUE.md, QUESTIONS.tsv (61 rows) and paper 4's Section 1.
- The paper-3 splitting passages of both runs.

**The second run is not a continuation.** It started fresh at 13:40:35 UTC on 24 Nov and numbered its own checkpoints
01–08. So it is an independent same-model replication plus extensions.

**Useful or not.** Useful for:
- Paper 4: circuit lower bounds for the pequalnp fleet;
- Paper 1: the split-zero foundation.

Marginal for Papers 2, 3 and 5.

**What the second run adds over the first run's cp08 (Fable's intake).**
- **Replications.** It independently re-obtains several first-run theorems, which agree:
  - P1-A (V and K₀ of R₀), P1-C modules;
  - P4 thm:onesided (L-meta-647) and the quadratic and read-1 exact counts;
  - P5 non-unimodality and the cell theorem;
  - P2 quotients and the sign-Tate quotient.
- **Paper 4.**
  - thm:twomissing: an exact |E| + vc − 1 for circuits with at most two edges lacking a quadratic witness.
  - thm:threemissing: one residual configuration, five deletions with an optimal quadratic remainder.
  - P4-DET: an exponential lower bound for the formal determinant's support.
  - Induced-matching bounds.
  - L-meta-608 and 612 remain open.
- **Paper 5.**
  - **Refuted:** the unrestricted bottom-zero assertion, by a lift with zero bottom supported-zero weights.
  - **Refuted:** "every associative lift has an effective refinement", by a specialization of Forsberg Prop. 12 and
    Cor. 13.
  - The least strict-unit basis rank for failure is 3.
  - A fixed-finite-diagram obstruction.
  - Weights over arbitrary global fields.
  - A rank-4 localization certificate: a 114×114 word minor.
- **Paper 2.**
  - The rescaled Hurwitz classification a = 1/m. I re-proved it.
  - Five Hurwitz zero paths certified by two independent verifiers.
  - The CLT-based "half-share" inference refuted. Its exact criterion equals NEG_NIGHT A001's.
- **Paper 1.**
  - Finite distributive and finite-group (R₀[Γ]) projective classifications.
  - Pic(R₀) = Pic(R).
  - FGJM Construction 3.5 classified in full.
  - The double-absorber claim refuted.
  - The general (Q, F) projectivity remains open.
- **Paper 3.** An explicit K₁ cokernel presentation.

**Check status of the second run's results.** Same-model only. No other model has checked them; I checked one small
item.

**Open (second run).**
- P1-C-PROJECTIVES.
- P4-608, 612, 606 and BIP.
- P5-minimum, P5-rank4 and P5-zero-bottom-effective.
- P2-hurwitz (all branches) and the half-share.
- SZ3-Q4 (K₁ splitting).

**Relations.**
- FGJM, CFMM Thm 8.5.
- The pequalnp fleet: L-meta-647, 608, 612, 584 (Petersen).
- GCT VIII (Mulmuley); Forsberg; Jukna.
- NEG_NIGHT A001.
- Our H22 note (v4 done).

**Candidates.**
- Merge the two runs' records before anything is posted.
- The Mulmuley e-mail draft (`EMAIL_DRAFT_Mulmuley_20261124.md`, GCT VIII's computer-check sentence).
- A fleet update on thm:twomissing, after a different-model check.

**Problems: one to resolve.** The two runs disagree on paper 3.
- The first run states thm:universal-nonsplitting: the K₁ sequence is nonsplit exactly for |P| ≥ 2. The file is first
  run `papers/paper3/nonsplitting_statement.tex`.
- The second run says, at `workbench/papers/paper3/main.tex` l.795–799, that splitting is open. Its quotient is a sum of
  localized-integer groups, not C_p = ℤ.

The two may concern different algebras: the second run distinguishes "natural versus scalar one-zero algebras". Neither
statement has been checked by anyone outside the runs. Reconcile this before either paper 3 is used.

**Settled on 25 Nov.** The first run is right, and the runs do not contradict each other. See "Follow-up 25 Nov",
section F3.

---

## What I could not read, and why

- **Proofs not opened:**
  - the POLISH_CRISTAUX cp33 proofs, except for the statements and gates;
  - COUNTING_VARIETIES `presentations.tex`, `structured.tex`, `fixed_fields.tex` and `motives.tex`, beyond the theorem
    statements;
  - the SPLIT_ZERO second run's proofs of thm:twomissing and thm:threemissing, and of the Paper 5 refutations.

  The reason was the token budget (about 1.2M): I gave the depth to the returns that had no intake.
- **Runs left to their earlier intakes, apart from one spot check each:** KTOWER, JAC1964, NEG_NIGHT and ARCH_ALG. Their
  newest return equals the one already taken in.
- **Not opened, as the brief directs:** SAT_WITNESS*, SAT_KRONECKER*, prompt-74, GCT_FLIP, GCT_SEPARATIONS,
  BORDER_RANK, SIGNED_COUNTS_AND_WINDING, and the S6 series.

---

## Follow-up 25 Nov: COUNTING_VARIETIES cp02 and cp03; SPLIT_ZERO_AFTER_FGJM second run cp10; the K₁ question

The same reader (Claude Opus 5.5 at effort high) did this follow-up at the main session's request.

**New files.**
- `INTAKE_COUNTING_VARIETIES_20261125_CHECK_EVENTS.tsv` (3 events).
- `INTAKE_SPLIT_ZERO_AFTER_FGJM_20261125_CHECK_EVENTS.tsv` (3 events).
- Seven new rows in AG_POLISH_ITEMS.tsv, now 46 rows. The earlier K₁ row is marked SETTLED.
- My new programs, in the scratchpad `agpolish/`: `cv_onecof.py`, `cv_ci.py`, `mon_search.py`.

### New, ranked by usefulness

1. **SPLIT_ZERO paper 4, thm:threemissing (second run, cp10).**
   - **Statement.** For a four-cycle-free graph G, every circuit computing a polynomial in Sup(G) with at most three edges
     lacking a quadratic witness has at least |E| + vc(G) − 1 gates. The star circuit attains this, so the bound is exact.
     There is no restriction on the degree or multiplicity of the higher witnesses.
   - **Also exact:** every four-cycle-free graph with at most four edges, with no witness restriction.
   - **Partial results at four missing witnesses:** an induced matching of four missing edges forces at least six deleted
     gates; the remaining four-missing cases are listed.
   - **Consequence.** Any counterexample to the fleet's star bound (L-meta-608/612) must lack quadratic witnesses on at
     least four edges.
   - **Check status.** The run made a separate statement-first re-proof with the same model.
   - **My check.** An exhaustive search over monotone AND/OR circuits (`mon_search.py`) gives minimum size |E| + vc − 1 on
     P3, P4, the triangle, K₁,₃, P5, the spider S(1,1,2) and 2K₂. This is consistent with the theorem, including its
     four-edge clause. It is not a test of the open case of four or more missing witnesses.
   - **Where.**
     RR/SPLIT_ZERO_AFTER_FGJM_checkpoint_10_20261124T2110Z_unzipped/workbench/papers/paper4/main.tex l.85. Paper 4 is now
     49 pp.
2. **COUNTING_VARIETIES: two saturation algorithms (cp02–cp03).**
   - **thm:saturation-intro / sp:thm:one-cofactor.** Take a sparse list whose saturation is (g), with g a smooth
     anticanonical hypersurface. If just one listed f_j has degree at most deg g + B, then the cofactor f_j/g, and with
     it the Frobenius scalar, is computable in polynomial time at fixed p and B. The other inputs may have arbitrary
     binary degrees.
   - **thm:saturation-ci-intro** (`saturation_ci.tex`, new). In codimension c, with 0 ≤ c·maxdeg − (N+1) ≤ E fixed, the
     scalar is polynomial-time. No regular sublist needs to be given. The proof uses regular combinations over a finite
     extension, a bounded-degree annihilator, and a norm descent.
   - **My checks.**
     - Targeted proof check of the line-gcd lemma. The saturation promise is equivalent to the cofactors having no common
       zero, so on chart lines the gcd of the restricted f_i is g.
     - `cv_onecof.py`, over F₅. Take g = y²z − x³ − xz² with cofactors of degrees 1, 25 and 40. The gcds with modular
       exponentiation return h₁(z)/h₁(a) correctly at every point off the line through 0 and a. The four exceptions lie on
       that line, which the paper's chart x₀ = 1 excludes. g is recovered exactly, h₅(g) = 2, and #X(F₅) = 4.
     - `cv_ci.py` checks the Koszul coefficient formula the CI theorem rests on. A smooth quadric-intersection curve over
       F₅ has scalar 3 and 8 points, and the scalar is invariant under changes of generators.

     The annihilator and norm-descent step of the CI theorem was not checked.
   - **Run status.** The indexed CI theorem has a statement-only re-proof by the same model. The no-sublist version has
     targeted checks, and an independent attempt was in progress at cp03.
3. **COUNTING_VARIETIES, smaller additions.**
   - **sp:thm:support-hardness.** At fixed odd p the smooth one-nonlinear-equation family stays Mod_pP-hard with
     K ≤ d^η. So the support boundary lies between K = O(log L), where counting is polynomial, and K = d^η, where it is
     hard.
   - **cor:ff-betti-information.** At most (B+1)^{2B−1}·3^B·2^{B²}·q^{(B³−B)/2} zeta functions over F_q have total Betti
     number at most B. So decoding n-bit counts from zeta alone needs B = Ω((n/log q)^{1/3}).
   - **Re-proofs.** Fresh statement-only same-model re-proofs of the main theorem, of the odd-prime complete
     intersection, and of the trinomial presentation.
   - **Totals.** The paper has grown from 52 to 75 registered statements and to 67+ pages. The run's first three-hour
     review was due at 22:30 UTC.
4. **SPLIT_ZERO paper 1 (cp10).**
   - **thm:canonical-ideal.** For every inverse semiring (Q, F), a semimodule is finitely generated projective iff three
     things hold:
     - its support L is projective over Q;
     - its amplitude G is projective over the action category A_L;
     - J_L G = G.
   - **thm:finite-inverse-projectives.** The finite case is classified completely: a finite support test
     k = ⋁_l δ_l(k)·l, and the amplitudes are the sums of the projective covers P_i of simples with I_L S_i ≠ 0.
   - **Limits.** J_L² ≠ J_L in a finite example, and every ordinary ring ideal occurs as a canonical ideal.
   - **My check, by hand.** The support test against Q = 𝔹 (join-semilattices): the 3-chain passes and M₃ fails, as the
     classical description of finite projective semilattices as distributive lattices requires.
5. **SPLIT_ZERO, other.**
   - Paper 2 now credits the quotient-count formula to hexagon:2611.00993v1. That is our own H22 note as posted (v4).
   - **Paper 3 is unchanged since cp08** (20 pp.).

### F3. The K₁ question: which SPLIT_ZERO run is right

**Answer: the first run is right, and the two runs do not contradict each other.** For every finite set P of at least two
primes, the sequence

0 → coker ∂_P → K₁(N_P) → ⊕_p C_p → 0

does not split. For a singleton it splits, since then C_p = ℤ.

The second run never claims a splitting. It asserts no splitting, and at `main.tex` l.795–799 it states, as an open
question, whether its presented class is zero in Ext¹. The first run's theorem answers that question: the class is not
zero.

**The runs agree on everything else.**
- **The algebra.** Both treat the same algebra, N_P = C₀(W_P^{(1)}) ⋊ Γ_P, the crossed product on the locus where at most
  one adelic coordinate vanishes. The second run's "natural versus scalar" distinction concerns other algebras in its
  paper, not this sequence.
- **The quotient.** The first run's C_p ≅ ℤ[1/Q_p]^{d_p} and the second run's (D_p^{rat})^{Ω_p} are the same group.
  D_p^{rat} = ⋃_U (1/d_U)ℤ is abstractly ℤ[1/Q_p], because the order of p modulo q^k is unbounded exactly for
  q ∈ P∖{p}.

**What I checked.** I re-derived the first run's proof inside the second run's own presentation (its thm:presentation,
eq. (K1presentation)). The decisive steps:
1. **The pullback.** Restricted to the summand C_p, K₁ is G_p/B_p, where B_p = Σ_{q≠p} j_q(F_q) is finitely generated:
   each F_q is the finite-rank group of σ_q-invariant functions.
2. **The splitting of G_p.** Take the transversal ℤ_p^× × U, where Y_p = U ⊔ (−U). The relations coming from functions
   supported on U eliminate J = j_p(O_p) with identity coefficient. This gives G_p ≅ L′ ⊕ O_p ⊕ E_p/(1−σ_p)E_p, with
   L′ ⊕ O_p free.
3. **Case −1 ∉ H_p** (this always holds for odd p when 2 ∈ P).
   - Take U σ-invariant. The even part then maps onto the diagonal of C⁺ ⊕ C⁺.
   - The cokernel C⁺ is nonzero and torsion-free, and C_p is q-divisible for q ∈ P∖{p}.
   - lem:finite-kernel-obstruction forbids a section. I checked the lemma: an ℓ-divisible image in (free) ⊕ (finitely
     generated) is torsion, so it dies in the torsion-free C/I.
4. **Case −1 ∈ H_q for every q.**
   - Then 2 ∉ P, so Q_p is odd.
   - Negation acts trivially on C_p, so the even part maps onto 2C_p ≠ C_p.
   - C_p is divisible by an odd prime, so every map from C_p to the free part vanishes. A section would force C_p = 2C_p.

The check event is in `INTAKE_SPLIT_ZERO_AFTER_FGJM_20261125_CHECK_EVENTS.tsv`.

**What follows.**
- When the two runs' records are merged, the second run's paper 3 should take the first run's thm:universal-nonsplitting,
  credited to that run, and drop the open question.
- The first run's further torsion claims were not checked by me: thm:all-torsion (every order m from four primes) and
  thm:odd-torsion (no odd torsion with three primes).

### Changes to TOPICALITY_GCT_AG_DER.md and MAP_COMPLEXITY.md

- **MAP_COMPLEXITY.md §3.7 (L36), out of date.** "thm:threemissing leaves one residual configuration" is superseded at
  cp10: the star bound is exact for at most three missing witnesses. Any remaining counterexample needs four or more
  missing witnesses.
- **MAP_COMPLEXITY.md T5.** Its note "SPLIT_ZERO cp10 is unread" is now discharged by this section. The different-model
  check asked for there is still missing: mine is a small-graph computation, not a proof check.
- **MAP_COMPLEXITY.md T4.** Its note "COUNTING_VARIETIES cp02 and cp03 are unread" is likewise discharged. NK-6, the
  Artin–Mazur height test, is not in the run: cp03's sections never mention formal groups, Artin–Mazur or Stienstra. So
  NK-6 remains our own observation, and its prompt candidate (does a_{p²} encode a further count?) stands.
- **TOPICALITY row "COUNTING_VARIETIES main": PARTLY stands.** The run cites von zur Gathen–Karpinski–Shparlinski 1996,
  Thm 4.7 (refs_fixed.tex), in its fixed-field section. The new saturation theorems were not checked for topicality.
  Cheng–Rojas–Wan and Kudo are the nearest literature, both cited by the run.
- **TOPICALITY row "SPLIT_ZERO twomissing".** It should now read thm:threemissing. The verdict "UNSETTLED: internal to the
  fleet" stands.
- **No other verdict changes.** Nothing in these checkpoints touches the GCT, AG or Dérivateurs verdicts of the other
  clusters.
