# Intake of RESEARCH_SA08: the divided-power de Rham complex of cote 136, its automorphisms and faisceautisation

- **The run.** GPT-6 Astra (ChatGPT Pro mode), on the prompt built in `pro_prompt_builds/RESEARCH_SA08` (uploaded as
  `PROMPT(20261119-052153).md`), which carries aa2156d1's reading of 136/142-376 (R12-R15, L8, B.5-B.8).
  - It worked from 05:21 to 10:27 UTC on 19 Nov 2026, about 5 h 06 min.
  - Its ledger records checkpoints at 06:06, 06:51, 07:36, 09:06 and 09:51 UTC, and formal reviews at 08:21, 09:21 and
    10:21 UTC.
  - The 08:21 review had movement: A.4 and L2 were settled at 07:44. The reviews of 09:21 and 10:21 had none, so the
    run stopped under the prompt's two-review rule and headed its final INCOMPLETE. The stop is the prompt's ledger
    rule, which the prompt lets override the rule about untried approaches; the session itself did not end.
- **The return** is filed at
  `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA08_final_20261119T1027Z_unzipped`. It
  contains:
  - a report of 13,280 words;
  - a paper of 124 pages (`RESEARCH_SA08_paper.tex`, with 45 section files);
  - a results register of 118 statements: 84 proved (20 of them under stated hypotheses or with a qualification),
    25 refuted, 8 known and rechecked or corrected, and 1 not determined (B-14, the dating);
  - 352 check events, all by the run's own agents: 152 independent re-proofs, 85 targeted proof checks, 59 used and
    rechecked, 43 computations or certificates, and 13 refuted and refined;
  - a corrections table of 75 rows (A-C01 to A-C23, B-C01 to B-C15, C-C01 to C-C08, D-C01 to D-C29);
  - `notes/`, `code/` and `logs/`.
- **Taken in by** Claude Opus 5.5 at effort max (agent a34c04448e8299803, which built the prompt), on 19 Nov 2026,
  finished at about 11:50 UTC.
- **What I read.**
  - From the return, in full: the outcome table and the section on gates of the report (l.1-33, 423-453), the
    results register, the corrections table, `notes/A_all_lattice_obstruction.md`, and the ledger entries from 07:36
    to the end.
  - From the return, also in full: `sections/A_all_models_obstruction.tex` (A-026, both proofs and the description of
    the finite certificate).
  - From the return, in part: D.18 of `notes/D_Breen_comparison.md`, and the run's check events (the counts, and the
    rows on A-026).
  - Against these: our STUDY, HUNCHES, RESEARCH_PACKAGES and readings of SA08; aa2156d1's second pass of 136/328-376
    (scans 332-335, 360, 376); the Pro notes of MPL_136_235-281 (N32, N33, N71) and of MPL_136_142-188 (N029-N031);
    and the scan of 136/376.
  - Not read: the proofs of A, B, C and D beyond the rows above, the C.3 constructions C09-C36, the code, the logs and
    the PDF.
  - No literature was opened (see section 7).
- **Files beside this one:**
  - `INTAKE_RESEARCH_SA08_20261119_CHECK_EVENTS.tsv`: 20 check events, INT-SA08-E01 to E20. It is not the topic table:
    `SA08/CHECK_EVENTS.tsv` is left as it was.
  - `intake_scripts/intake_checks_20261119.py`, with its output `intake_checks_20261119_output.txt`: standard-library
    checks of A-026's arithmetic and lattices, D-C15, B-C01, B-C04, the integrality of T + T^[2], the exponents of 376,
    and W_2. They neither import nor run any program of the return.

## 1. The main answers

- **A.1 (main): settled.** The PD de Rham cohomology over k{T} is determined for every simplicial set and every ring,
  with its products and the action of every T^[a] (A-001 to A-009, A-025).
  - L1 holds for graded direct-sum cochains (A-003). Taken literally for every X it is false: the literal answer is
    H^i(X; I_i), weight by weight (A-002), and the tensor form fails for an infinite discrete X (A-004, re-proved here,
    E01).
- **A.2: his main claim of scans 11-12 holds.** The weighted PD cochains recover RΓ(X, Z) with its product, and
  H^*(X, Z) (D006); after enhancement they recover the E∞ cochain algebra (D006E).
  - The Ext corollary of scan 27 holds for every k, M, N and i (D002).
  - His "?" of 273 on the derived unit has a positive answer in the localizing Serre quotient (D003-D005).
  - The mechanism, an exact left adjoint, was already in the Pro notes of MPL_136_235-281 (N32, N33, N71). Our study
    had missed this (E13).
- **A.4: L2 is refuted in the form asked.** There is no natural, exhaustive, filtered numerical cochain algebra over
  Int(Z) with R-bilinear products whose associated graded is the PD cochain algebra compatibly with coefficients,
  derived and E∞ models included (A-026).
  - The coefficient statement gr Int(Z) = Γ_Z(T) stays true (A-015).
  - The intake re-proved part (1) of A-026, which says that every filtered pairing M_1 ⊗ M_1 → M_2 with
    gr M_i = I_i vanishes (E02-E04).
  - The intake also checked part (2), the reduction from all X to the circle and the torus, step by step (E20). That
    part went from "under investigation" at 07:36 UTC to proved at 07:44 UTC, with one check inside the run (E19).
- **B.2: L4 is false.** The automorphism T ↦ T + T^[2] has Δ = 1 and moves the coefficients (B-07, re-proved, E05).
  - The full action is coefficient substitution (B-06).
- **B.3: his "Non" of scan 182 is right.** No Steenrod square arises, in the strict category the run fixes (B-08,
  B-10).
  - The RP3 sphere test of our SA08-RP3 could not decide the question (B-09, re-proved, E06).
- **B.8: the statements of 374-376 are corrected against Breen 1978 (D013-D021).**
  - The ink of 376 has d = v_p(i) (E11). So the off-by-one that the run finds against Breen's v_p(i)+1 is
    Grothendieck's, not the transcriber's.
  - Breen is not checked by this intake.
- **C.3 is open.** The one open mathematical item is his uniqueness conjecture over Z.
  - The strict form, 121(b), fails over every nonzero ring (C07).
  - The groupoid form is proved for rings with finitely many noninvertible primes (C17), and reduced over Z to local
    completions that are not constructed (C30, C32, C34).
- **L7 (the date of 144-212) is undetermined.** This agrees with our study (E18).

## 2. Item by item against the prompt as sent

Where the last column says the run's table is fair, the intake found nothing against it. In most rows that rests on
the run's own checks, not on a check by this intake.

| Item | The run's state | Statements | Checked by the intake | Is the run's table fair? |
|---|---|---|---|---|
| A.1 | proved; L1 refuted as a literal all-X claim, corrected statement proved | A-001 to A-009, A-025 | A-004 re-proved (E01) | fair |
| A.2 | proved | D001-D006E, D006M | only the attribution to N32, N33 and N71 (E13) | fair; it credits the Pro notes |
| A.3 | proved; the scalar shortcut only under stated hypotheses | A-010 to A-013 | no | fair |
| A.4 | L2 refuted; the associated graded and the homotopy comparison proved | A-015 to A-018, A-021 to A-026, D-025, D-026 | A-026 (1) re-proved and computed (E02-E04); A-026 (2) checked (E20) | fair. Part (2) was written in eight minutes and checked once inside the run; it holds on the intake's check |
| A.5 | L3 proved | A-014 | no | fair |
| B.1 | proved | B-01 to B-04, B-15 to B-17 | the failure of the conditions without (M) (E07) | fair |
| B.2 | L4 refuted; the full action proved | B-05 to B-07 | B-07 re-proved (E05) | fair |
| B.3 | proved in the strict shadow category the run fixes | B-08 to B-10 | B-09 re-proved (E06) | fair, read with its category (B-C10) |
| B.4 | proved; the decompositions of 208 refuted | B-12, B-13 | no | fair |
| B.5 | L8 refuted in its unqualified form | B-11 | no | fair, but only the exclusive placement is refuted: the action is the identity, which lies in both algebras |
| B.6 | refuted; replacements proved | B601-B605 | the ink of 360 (E15) | fair |
| B.7 | proved | D007-D012 | no | fair |
| B.8 | checked; statements corrected or refuted | D013-D021 | the ink of 376 (E11), W_2 (E12), D-C17 (E17) | understates: it calls the author of the 376 exponent unknown, but the ink settles it |
| C.1 | L6 proved | C01 | no | fair |
| C.2 | L5 refuted for additive contraction; the weak form proved | C02-C06 | the notion of flasque (E14) | fair |
| C.3 | open; the finite-prime case proved | C07-C36, D022-D032 | no | fair |
| L7 | undetermined | B-14 | consistent with our study (E18) | fair |

The run did not finish early by its own choice. Its one undecided mathematical item, C.3, has its gate and every
approach tried written out (report l.423-453). The cut came from the ledger rule after two reviews without movement.

## 3. His text: what is false, what needs a repair

- **Scans 142-188 (the automorphisms).**
  - The condition (M) is dropped.
    - Scan 184 writes the relation ξ_i ξ_j = c_ij ξ_(i+j).
    - Scan 186 ends with the B_i "sans autre condition !".
    - The dX_0 part of that relation is (M): C(i+j,i) B_(i+j) = A^[i] B_j + A^[j] B_i. The data A = X, B_2 = 1
      over F_2 violate it (B-C01, E07).
    - First found in the Pro notes of MPL_136_142-188 (N029-N031), which cite Michel Hua's project's findings
      register, and in our reading of 136/142-376.
  - The margin "the condition on B disappears when 2 is invertible" is false.
    - Over F_3{T} the map A = 0, B_3 = T^[5] meets the conditions.
    - A regular element in the coefficient ideal, together with 2 invertible, forces B = 0 (B-C04).
  - The arrays of 178 do not give an affine scheme. Ω is ind-affine (B-C05, B-04).
  - The page proves only that an invertible determinant is necessary. The converse holds as well (B-C07, B-03, B-16).
  - Abstract automorphisms need not be continuous (B-15, an ultrafilter automorphism over F_2).
  - "Seules les op. évidentes (se factorisent par Δ)" (180):
    - false for the full action, which is coefficient substitution (B-06, B-07);
    - true for ordinary cohomology, which sees only the identity (B-08).
- **Scans 189-234: the decompositions of scan 208, marked "(??)", are false (B-13).**
  - The coefficient image from G is {Σ f_n T^[n] : f_n ∈ nk}, which omits T + T^[2] over Z.
  - Over Q the endomorphism A = X(T − X), B = 0 does not factor.
  - The split statement holds for the automorphism groups.
  - G ∩ H = 1 + Ann(T), a square-zero group under addition (B-C11, B-C12).
- **Scans 95-141.**
  - Scan 121 equates groupoid uniqueness with the common-source and equalization assertions. Strict equalization fails
    over every nonzero ring, Q included (C-C05, C07).
  - The "Non" of 91 is right (C01).
  - The Prop. of 98 and the argument of 100 hold after the repair for universally flasque structures (C02-C05).
- **Scans 235-281.**
  - The bounded negligible modules form a Serre class that is not localizing. The elementwise-bounded ones are not
    closed under extensions. The localizing Serre closure is the class that works (D-C03, D004, D005).
- **Scans 282-327: the questions of scan 324 are answered (D007-D012).**
  - Existence fails for a finite nonflat coalgebra over Z/4.
  - The two displayed relations do not force uniqueness.
  - The dual question is classified.
  - The nonflat obstruction over Z was first given in the Pro notes of MPL_136_282-327 (N43, credited by the run).
- **Scans 328-342.**
  - Scan 334 gives γ^p(γ^q(x)) the coefficient (pq)!/((p!)^q q!). That is the coefficient of (x^(p))^(q), the order
    used correctly on 332-333. For γ^2(γ^3(x)) the right value is 10, and the page's formula gives 15 (D-C15, E09).
  - Scan 335 writes (λx)^(p) = λ^p x^p where x^(p) is meant (D-C16). Whether the slip is in the ink is open (E10).
- **Scans 343-361.**
  - Scan 352: the exterior product does not extend naturally to a half-algebra (B601).
  - Scan 360: the pointwise Hom complexes are free Σ_n-resolutions only with the inserted "pour X variable" (C-C07,
    E15).
- **Scans 362-376.**
  - H^*(X, R) = H^*(X, F_p) ⊗ R needs a finiteness hypothesis (D-C17, E17).
  - Every P^i, Q^i and Sq^i is Frobenius-semilinear, not only P^0 (D-C18).
  - The odd-primary theorem on H^*(K(O,m), O) needs the Q^i and the boundary-excess case (D-C19, D-C20).
  - The site and coefficient category must be stated (D-C21, D-C23).
  - In the finite-field test, cochain injectivity does not give cohomology injectivity. Detection holds below total
    weight p^h (D-C22).
  - Ext^(2i)(G_a, G_a) = k[F]/(F^d), d = v_p(i), is off by one against Breen (D-C24, D-C25). The ink is confirmed
    (E11); Breen is not checked.
  - H_j(K(G_a, n)) ≅ G_a ⊗ H_j(K(F_p, n)) holds only in the stable range n ≤ j < 2n (D-C27).
  - The final Tor E_2 computation is valid, but it collapses only at p = 2 (D-C28).

The intake checked D-C15, D-C17, B-C01, B-C04 and the inks of 360 and 376. The other items in this section rest on the
run's own checks.

## 4. Ours: where our study, readings or prompt were wrong

Of the run's 75 corrections:
- 18 touch the prompt and 43 touch our study and readings; 11 of them touch both;
- 24 touch only the transcriptions and the Pro notes;
- 1, C-C08, touches the run's own working note.

Many of the 43 are status updates: something open in our study is now proved (PD descent; L3; the questions of 324).
Those are not errors. The errors are these:

| Correction | Our claim | Verdict |
|---|---|---|
| A-C01 to A-C07 | L1 stated without a cochain convention (STUDY, H7, readings 136_142-376 H2 and 136_282-376, prompt L1) | holds (E01): literal cochains give H^i(X; I_i), graded ones the tensor form |
| A-C11 to A-C16, D-C01, D-C02, D-C05 to D-C07 | the general Ext corollary and the derived unit treated as unproved | holds (E13): the Pro notes of MPL_136_235-281 already had N32, N33 and N71; our study missed them |
| A-C17 to A-C20 | L2, the binomial bridge | holds (E02-E04, E20) |
| B-C08 | L4: Ω acts through Δ only | holds (E05) |
| B-C09 | our SA08-RP3 sphere test, used in prompt B.3 | holds (E06) |
| B-C14 | L8: the operations lie in 𝒜 and not in the Steenrod algebra | not checked; it follows from B-08: the action is the identity, which lies in both algebras |
| B-C02 | "torsion-free target ⇒ PD map" (STUDY l.184-186, readings 136_142-376 l.122-130) | holds (E16): the scalar PD ideal must be preserved |
| B-C03 | "over F_p the B are free on B_(p^m)" | not checked; for automorphisms in odd characteristic the annihilator conditions force B = 0 |
| B-C04 | the F_3 witness called reduced (aa2156d1, 136_142-376 l.133-139) | holds (E08): F_3{T} is not reduced |
| C-C01, C-C04 | L5 and H4: "slice acyclic ⇒ contractible" | not checked; true as π_* = 0, false as an additive contraction without projectivity |
| C-C02, C-C03 | our CE036 counterexample to scan 100 | holds (E14): the constant k is not flasque in the manuscript's sense |
| D-C12 | the two universal-element relations and Yoneda taken as the full PD specification (136_282-376 l.235-252) | not checked; the run adds the sum and scalar equations (D-007, D-010) |
| D-C24 | the Ext formula of 376 recorded without a flag (136_282-376 l.390) | the ink is as we read it (E11); the formula is off by one if Breen is as cited |
| D-C26 | "Ext^1 = 0 only modulo F-torsion, since the Witt extension is nonzero" (aa2156d1, 136_282-376 l.394-395) | holds (E12): the Witt class lies in Ext^1_Z, not Ext^1_(F_p) |
| B-C15 | L7: 1982-83 | consistent (E18): it was a lead, and stays undetermined |

The prompt asked B.3 through our SA08-RP3 reduction, which was wrong. The run replaced it with K(k,i) rather than
following it.

## 5. New results

The run claims these as new. The column on the right says what the intake checked. The run's report says that
Cartan's 1976 pages already establish "the endpoint and products", and credits his §7, pp. 269-271. Any novelty in the
A.1 answer has to be judged against Cartan.

| Result | Statements | Checked by the intake |
|---|---|---|
| No filtered numerical lift of the weighted PD cochains (the module obstruction, then the all-X reduction) | A-026 | part (1) re-proved and computed; part (2) checked |
| The literal and the graded answers to A.1, and T = 1 giving Sullivan's polynomial forms | A-002 to A-004, A-025 | A-004 re-proved |
| PD descent with an integral cocycle formula; L3 | A-010 to A-014 | no |
| The ordinary numerical Kähler associated graded, by finite lattices | A-017 | no |
| The weighted PD cochains determine the integral weak homotopy type (nilpotent, finite type; through Mandell 2006) | A-018, D006M | no |
| The shadows: Ext in general, the derived unit in the localizing quotient, E∞ recovery | D001-D006E | the source of the mechanism only |
| Ω: the three-data theorem with (M), ind-affine and not affine, the converse of the determinant criterion, a discontinuous abstract automorphism, the action as coefficient substitution, no Steenrod squares | B-01 to B-17 | B-07, B-09 re-proved; (M) computed |
| Half-algebras: the obstruction, the ambiguity, the classification | B601-B605 | no |
| Natural convolution PD laws: the equation space, flat uniqueness, the Z/4 counterexample, the dual | D007-D012 | no |
| The faisceautisation: L6, the repaired flasqueness, and strict equalization false over every nonzero ring | C01-C08 | the notion of flasque only |
| C.3, partly: the finite-prime case, conditional reductions over Z, and counterexamples to proposed shortcuts | C09-C36, D022-D032 | no |
| A refutation of Caradot-Lin, arXiv 2511.22614v4, Prop. 3.10 (unrestricted termwise-free chain-map lifting) | D-031 | no. It bears on other authors' published work. Check it before any use and before writing to the authors |

## 6. Ink claims that need a reader on the scans

Settled here:
- 376: d = v_p(i), checked on the image (E11).
- 334: the order of composition, read alike by both passes (E09).
- 360: "pour X variable" is in the second pass (E15).

Still open:
1. **335, l.35.** Is the last factor of (λx)^(p) = λ^p x^p written x^(p) in the ink (D-C16)? Low stakes.
2. **The end of 376** (first pass K136-03 l.938): the run keeps two readings of an ambiguous glyph in the final Tor
   expression (D-C28).
3. **208.** The arrows and the coefficient ring of the "(??)" diagrams, against the transcription of 189-234
   (l.610-635). The refutation B-13 depends on what is drawn.
4. **184-188.** Does he impose the dX_0 part of ξ_i ξ_j = c_ij ξ_(i+j) anywhere before "sans autre condition !" on
   186? If he does, (M) is his, merely unused.
5. **L7, the dating.** This is a question about the physical leaves, not a mathematical one:
   - paper, ink, recto and verso, and the order of 142-212 in the folder;
   - the link, if any, to the printout dated 16 August 1982;
   - footnote 137 of the archive catalogue.

   It belongs to an archive reading.

## 7. Literature locators the main answers rest on

No literature was opened by this intake: its context was past the point where it reads literature. The main answers
rest on these, as the run cites them. Each is a check to make before the answer is cited outside.

- **Breen, "Extensions du groupe additif"**, Publ. Math. IHÉS 48 (1978), 39-125:
  - Theorem 1.3, p. 47, and p. 116, (7.22)-(7.23), for the exponent v_p(i)+1 (D018, B.8);
  - p. 41, for the perfect site (D019);
  - Theorem 4.3, p. 86, for the odd-primary operations (D015).
- **Milne, "Duality in the flat cohomology of a surface"**, Ann. Sci. ÉNS (4) 9 (1976), 171-201: Lemma 2.2, p. 181
  (D019).
- **Mandell, "Cochains and homotopy type"**, Publ. Math. IHÉS 103 (2006), 213-246: E∞ cochains determine finite-type
  nilpotent spaces (A-018, D006M, A.4).
- **Cartan, "Théories cohomologiques"**, Invent. Math. 35 (1976), 261-271: §7, pp. 269-271, credited by the run with
  "the endpoint and products".
- **Toën** (affine stacks), **Horel** (binomial rings) and **Kageyama** (PD simplices), for A-019 and A-020.
- **SGA 4 V**, for the notion of flasque behind C-C02 and C02. E14 checks only the consequence that the constant k is
  not flasque.
- **Caradot and Lin, "Differential graded algebras with divided powers and homotopy Lie algebras"**, arXiv
  2511.22614v4, Prop. 3.10, for D-031.

These titles and pages are taken from the run's `RESEARCH_SA08_references.bib`.

A-026 (both parts), the answer to B.2, and the counterexamples re-proved in E01, E05, E06, E07 and E12 use no outside
source; A-026 (2) uses only the weightwise comparison R1 of our prompt. The proofs of A.2 rest on the run's own
arguments and on the Pro notes of MPL_136_235-281.

## 8. Whether a finishing prompt is warranted

**A finishing prompt is warranted for C.3 alone, at low priority.**
- **Outcome (19 Nov ~11:55 UTC, at the coordinator's word):** no separate prompt. C.3 went into RESEARCH_SA09 as its
  item A.5, with the gate, the approaches tried and the files below; the check of D-031 went in as A.6. See
  claude_math_notes/PROMPT_UPDATES.md.
- C.3 is the one open mathematical item.
- The run spent its last two hours on it without moving the gate. A successor therefore has to start from the gates
  and the recorded failures, not from the settled parts.
- L7 is documentary. It goes to an archive reading of the leaves (section 6), not to a mathematics prompt.

**What it must carry.**
- **The item.** Common sources and terminal localization for admissible generalized de Rham theories over coefficient
  rings with infinitely many noninvertible primes, beginning with Z.
  - The two assertions are kept distinct.
  - The strict form 121(b) is refuted (C07), so the item is his form a).
- **The gates.**
  - C30: common sources from p-local repairs whose agreement depths d_p tend to infinity.
  - C32: terminal localization from local repairs of the pair target A ×_k B and of the homotopy equalizer H(f,g).
  - C34: only the finite form truncations need local completions.
  - What is missing: either a local finite-form completion theorem with actual target maps and uniform bounds, or an
    invariant of admissible theories that detects moving primes. C33 shows that a fixed, finitely generated group of
    operations cannot be that invariant.
- **The approaches tried, with where they failed.**
  - Ordinary tensor products: prime-power Tor in unbounded weights (C11).
  - Independently marked PD disks over Z (D022, D023).
  - Projection-preserving arithmetic gluing (C12).
  - Standard tails as an initial family (C13).
  - Free linear-disk replacements and free resolutions of the tails (C14, C15).
  - Ordinary common-target pushouts (C19).
  - Naive PD indecomposables (C26).
  - A simple arity-homology pattern (D032).
  - Delayed p-local closures without target maps (C18).
  - The global partial model, which needs floor((d+1)/2)! inverted (C21).
  - Automatic bar-boundary extension: a counterexample over Z_(2) (C31).
  - Rational halves of odd products (C35).
  - The finite-arity bar extensions C24, C25 and C27-C29, and C36, which do not meet infinitely many bounds at once.
  - The cited lifting result of Caradot-Lin (D-031).
- **The files of this final it restores from.**
  - In `notes/`:
    - `C_findings.md`, `C_finite_prime_proof.md`, `C_global_partial_model.md`, `C_local_completion_attempts.md`;
    - `C_terminal_repair_reduction.md`, `C_bar_boundary_failure.md`, `C_relative_bar_extension.md`;
    - `C_integral_approaches.md`, `C_odd_disk_closure.md`, `C_indec_counter.md`, `C_signed_shuffle_relative.md`;
    - `B_C3_*.md`, eight files;
    - `D_arithmetic_repair_gluing.md`, `D_global_local_repair_gate.md`, `D_final_local_repair_attempts.md`;
    - `D_Cintegral_source_obstruction.md`, `D_coordinated_bar_lifts.md`, `D_bar_mixed_torsion.md`,
      `D_nonfree_higher.md`, `D_padic_literature_caution.md`.
  - In `sections/`: the matching C_, B_C3_ and D_ files.
  - The C, C3 and D022-D032 rows of `RESEARCH_SA08_results.csv`, with their check events.
  - The reviews of 08:21-10:21 in `PROGRESS_LEDGER.md`, for the gate as last stated.
- **What it drops.**
  - A.1-A.5, B.1-B.8, C.1, C.2 and the leads L1-L6 and L8: all settled.
  - This intake re-proved or checked A-004, A-026, B-07, B-09 and the corrections of section 4. The rest stands on
    the run's own checks.
- **Not in it, but before any use:**
  - an outside check of D-031;
  - a reading of Breen's Theorem 1.3.

## 9. Rows for the register

**Check events:** the 20 rows INT-SA08-E01 to E20, in `INTAKE_RESEARCH_SA08_20261119_CHECK_EVENTS.tsv`. The columns
are id, statement_id, date_utc, who, type, outcome and where. They are ready to be merged into SA08/CHECK_EVENTS.tsv;
the topic tables are left as they were.

**Corrections.** The columns are as in SA08/CORRECTIONS.tsv. For every row, decided_by is "the RESEARCH_SA08 final,
GPT-6 Astra (ChatGPT Pro mode); intake by Claude Opus 5.5 at effort max, a34c04448e8299803"; that column is left out of
the table.

| id | where | kind | what | corrected | evidence |
|---|---|---|---|---|---|
| INT-SA08-K01 | prompt L1; STUDY; readings 136_142-376 and 136_282-376 | our lead corrected | the PD-Rees tensor formula for every X | true for graded direct-sum cochains; literally H^i(X; I_i), and the tensor form fails for infinite discrete X | A-002 to A-004; E01 |
| INT-SA08-K02 | STUDY l.85-86, 98; readings; prompt R4 | our error | the general Ext corollary and the derived unit are open | proved (D001-D006E), by the mechanism of the Pro notes of MPL_136_235-281, N32, N33 and N71 | E13 |
| INT-SA08-K03 | prompt L2; RESEARCH_PACKAGES l.49-51 | our lead refuted | a filtered numerical lift of the PD cochains | no such lift (A-026); gr Int(Z) = Γ_Z(T) stays true (A-015) | E02-E04, E20 |
| INT-SA08-K04 | prompt L4; HUNCHES | our lead refuted | Ω acts through Δ only | the action is coefficient substitution; T + T^[2] has Δ = 1 and acts | B-06, B-07; E05 |
| INT-SA08-K05 | RESEARCH_PACKAGES SA08-RP3; prompt B.3 | our reduction refuted | the operation test on Δ[i+1]/∂Δ[i+1] | that sphere has H^i = 0; use K(k,i) | B-09; E06 |
| INT-SA08-K06 | STUDY l.184-186; readings 136_142-376 l.122-130 | our claim qualified | torsion-free target ⇒ PD map | only if the scalar PD ideal is preserved | B-C02; E16 |
| INT-SA08-K07 | readings 136_142-376 l.133-139 | our reading corrected | the F_3 witness is reduced | F_3{T} is not reduced: (T^[5])^2 = 252 T^[10] = 0 | B-C04; E08 |
| INT-SA08-K08 | readings/136_002-141_CHECK_EVENTS.tsv row 37 (CE036) | our check event corrected | the constant k refutes scan 100 | k is not flasque in the manuscript's sense; CE036 refutes only the absolute Γ-acyclic reading | C-C02, C-C03; E14 |
| INT-SA08-K09 | readings 136_282-376 l.394-395 | our reading corrected | Ext^1(G_a, G_a) = 0 only modulo F-torsion, by the Witt extension | Ext^1_(F_p) = 0; the Witt class lies in Ext^1_Z | D-C26; E12 |
| INT-SA08-K10 | 136/184-186 | his text | the B_i "sans autre condition !" | (M) is needed; A = X, B_2 = 1 over F_2 violate it | B-C01; E07 |
| INT-SA08-K11 | 136/334 | his slip | γ^p(γ^q(x)) = (pq)!/((p!)^q q!) γ^pq(x) | (pq)!/(p!(q!)^p); the page's coefficient belongs to (x^(p))^(q) | D-C15; E09 |
| INT-SA08-K12 | 136/376 | his slip (ink confirmed) | Ext^(2i)(G_a, G_a) = k[F]/(F^d), d = v_p(i) | d = v_p(i)+1 per Breen 1978, Thm 1.3 (not checked) | D-C24, D-C25; E11 |
| INT-SA08-K13 | 136/335 l.35 | his slip or a misreading (open) | (λx)^(p) = λ^p x^p | λ^p x^(p) | D-C16; E10 |
| INT-SA08-K14 | 136/362-376 (first pass K136-03 l.721) | his claim qualified | H^*(X, R) = H^*(X, F_p) ⊗ R | needs a finiteness hypothesis | D-C17; E17 |
