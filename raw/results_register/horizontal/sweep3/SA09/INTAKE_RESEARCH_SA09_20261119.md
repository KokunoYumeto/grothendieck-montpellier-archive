# Intake of RESEARCH_SA09: polynomial categories and the walking complex (cote 137), maps and the Galois action (cote 138)

- **The run.** GPT-6 Astra (ChatGPT Pro mode), on the prompt as sent at 11:03 UTC on 19 Nov 2026
  (`pro_prompt_builds/RESEARCH_SA09/PROMPT_as_sent_20261119.md`). That file is byte-identical to
  `PROMPT_before_SA08_results_20261119.md`. It therefore carried A.1-A.4, B.1-B.4, L1-L5 and R1-R10. It did not carry
  the results of RESEARCH_SA08, C.3 (A.5) or the check of D-031 (A.6): the update of about 11:50 UTC never ran.
  - The run worked from 11:03 to 11:46 UTC, 43 minutes, so the three-hour review never came due.
  - It reports every item and lead proved or refuted.
- **The return** is filed at
  `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA09_final_20261119T1146Z_unzipped/RESEARCH_SA09`.
  It contains:
  - a report of 4,611 words;
  - a paper of 41 pages (`RESEARCH_SA09_paper.tex` with eight section files, about 18,000 words of TeX);
  - a results register of 43 statements: 24 proved, 3 proved under stated hypotheses, 10 refuted, and 6 known (one of
    them "known, with comparison proved");
  - 180 check events, all by the run's own agents: 87 targeted proof checks, 52 computations or certificates, 15 used
    and rechecked, 12 independent re-proofs, 12 refuted and refined, and 2 carried as background;
  - `code/`, `qa/` and a short progress ledger.
- **Taken in by** Claude Opus 5.5 at effort max (agent a34c04448e8299803, which built the prompt), on 19 Nov 2026,
  finished at about 13:10 UTC.
- **What I read.**
  - In full: the outcome table and sections 1 and 4 of the report, the results register, and the proofs of A1.7,
    A3.2 and B4.1.
  - Measured: the length of every statement and proof in the paper (`intake_scripts/proof_depth_scan.py`).
  - Against these: our SA09 study as the prompt carried it (R1-R10, L1-L5), our transcription of 137:45-86
    (l.153-167), and RESEARCH_SA08's results and intake.
  - Not read: the other proofs, the programs of the return, and the PDF. No literature was opened.
- **Files beside this one:**
  - `INTAKE_RESEARCH_SA09_20261119_CHECK_EVENTS.tsv`: 17 check events, INT-SA09-E01 to E17.
  - `intake_scripts/intake_checks_sa09_B.py`, with its output: an independent recomputation of B.1-B.2 and of B.4 at
    levels 4 and 8, using itertools and sympy. It neither imports nor runs any program of the return.
  - `intake_scripts/proof_depth_scan.py`, with its output.

## 1. The main question (A.1) and the depth of the run

**A.1 is answered: L1 is false, and the right relation is proved.**
- His P_n(X,Y) = Hom(Γ^n X, Y) are the modules of homogeneous polynomial laws (Roby).
- The category Γ^d P of Friedlander and Suslin has the Hom modules Γ^d Hom(X,Y) instead. Over F_2 these have
  dimensions 2 and 3 for X = k, Y = k² (A1.3; re-proved, E11).
- The bridge is a polynomial-law action on the linear Hom modules.
- His closing question has a positive answer for all modules: f ↦ Γ^p(f) is a homogeneous polynomial law (A1.4).
- The unit axiom 1 ≅ Γ^q(1) is independent of the others (A1.5). The printed equivalence is false (A1.6) and needs the
  comonad conditions of A1.7.
- The grading is data, with the exact scalar ambiguity in A1.9.
- I read A1.7 in full. It is a correct characterization: the comonad and co-Kleisli conditions on B_m = ⊕_{i≤m} G^i.
  The equivalence of categories in its last paragraph is asserted in two sentences, not carried out (E16).

**Forty-three minutes for every item was a real concern, and the test was this.**
- Every statement but the two background ones (A1.1, B0.1) has a written proof. The proofs run from 67 to 675 words,
  most between 120 and 500 (`proof_depth_scan_output.txt`). They are compact proofs, not assertions.
- **The three proofs I read are carried out**, step by step: A3.2, B4.1, and A1.7 except its last paragraph.
- **Everything computable recomputes** (E01-E05, E07): the polynomial computation of B.2, the enumeration of the
  maps, the field of moduli and its Galois group, and the Kummer indices at levels 4 and 8.
- **The re-proofs hold** (E06, E10-E14): the torus count, the lens spaces, the L1 dimensions, the Dold-Kan rank
  criterion, the non-injective stalk, and the binomial operations.
- **Where the speed shows:**
  - several classifications are stated as complete on short proofs: B3.1 (675 words), B4.4 (489 words, from Schinzel
    and the S-unit theorem) and A1.8 (399 words);
  - A1.7's converse is brisk;
  - A3.2 reads Grothendieck's "structure supplémentaire" (137:38) in the strongest sense, the natural action on all
    test objects. That makes the reconstruction nearly formal, and the run says so (A3.4 refutes the weaker readings).
- I found no error.

## 2. Item by item against the prompt as it ran

| Item | The run's state | Statements | Checked by the intake | Is the table fair? |
|---|---|---|---|---|
| A.1 | L1 refuted; the correct relation, the Hom-law, unit independence, the failure and repair of the equivalence, and the grading proved | A1.1-A1.9 | A1.3 re-proved (E11); A1.7 read (E16) | fair; A1.7's converse is brisk, and A1.5, A1.6 and A1.8 rest on the run's own checks |
| A.2 | L3 refuted for the nonnegative source; essential image over every ring and over PIDs; exact variants; the Frobenius replacement | A2.1-A2.6 | A2.1 and the reading of the source (E13) | fair |
| A.3 | L2 proved for the full natural Γ-action; homotopy type recovered; weaker readings refuted | A3.1-A3.5 | A3.2 read (E08), A3.4 and A3.5 re-proved (E10, E14), A3.3 compared (E09) | fair, read with its interpretation of 137:38 (section 1) |
| A.4 | corrected rank criterion over every ring; perfection criteria for regular and nonregular rings; Prop. 1 e) false both ways | A4.1-A4.6 | A4.1-A4.2 re-proved (E12) | fair |
| B.1 | orbit-size formula and equality criterion; rigidity false; kernels classified | B1.1-B1.3 | B1.1-B1.2 re-proved (E06) | fair |
| B.2 | three Belyi maps, P = −δp/7776, field Q(∛2), one S_3 orbit; the δ-collisions have another passport | B2.1-B2.5 | all recomputed (E01-E05) | fair |
| B.3 | complete list of cellwise holomorphic groups (Aff⁺(R), R_{>0} for every orange, C_2 for the bouquets) | B3.1-B3.4 | no | fair as far as read; "complete" rests on the run's checks |
| B.4 | exact Kummer images and indices at every level; Fermat fibres; adelic openness under hypotheses | B4.1-B4.4 | B4.1 read and computed (E07) | fair |
| L1-L5 | L1 refuted, L2 proved, L3 refuted, L4 proved, L5 proved with P corrected | as above | as above | fair |

## 3. What the run settled, and what that changes

**Settled.** Every item of the prompt as it ran: all of Part A (cote 137) and all of Part B (cote 138).

**Our leads and study, corrected.**
- **L1** conflated polynomial laws with the Hom modules of Γ^d P (E11).
- **L3** assumed the source is the bounded complexes in all degrees. Grothendieck's source is the nonnegative category,
  which is not Frobenius (E13).
- **Our reading's "cubic P"** is the raw quintic δ·p (E01).
- **R6's "only after inverting the primes"** states a sufficient condition, not a necessary one (A1.9, not rechecked).

**Ours, confirmed.**
- R2: Prop. 1 e) is false both ways, and μ_i is restored.
- R8: rigidity fails; the torus example (E06).
- R9: three maps, and the roots of δ (E03, E05).
- R10: the groups are real (B3.1).
- L4 and L5 hold; L5 with the cubic p in place of "his polynomial".

**Set against RESEARCH_SA08.**
- **A.3 and the homotopy type: the two runs agree.**
  - SA08's A-018 and D006M recover the integral weak homotopy type of a nilpotent space of finite type from cote 136's
    weighted PD cochains, through Mandell. Its D006E recovers the E∞ cochain algebra.
  - SA09's A3.2-A3.3 recover the strict cosimplicial ring Z^X from cote 137's natural Γ-action, and through Horel the
    homotopy type and the mapping spaces. This is the stronger statement, about a different object.
  - Neither run proves the bridge R5 between the two objects. The prompt of SA09 cited R5; the run states that it did
    not re-prove R1 or R5.
- **A3.5 and A-026: they agree.**
  - A3.5 says numerical operations are not strict polynomial laws, and no divided power exists on an ideal of Z
    containing 1.
  - A-026 says no filtered numerical lift of the PD cochains has them as associated graded.
  - Both separate the numerical (binomial) world from the divided-power one. A-026 is the structural statement and A3.5
    the elementary one. No conflict.
- **No other overlap.** SA09's A.2 and A.4 do not touch SA08's shadows (D001-D006) or flasqueness (C02-C05). SA09's A.1
  and SA08's convolution laws (D007-D012) are about different Hom modules.
- **Same type of slip.** SA09's typed associativity G^p(α_{q,r}) α_{p,qr} = α_{p,q}^{G^r} α_{pq,r} (137, transcription
  l.1221-1223) corrects an order of composition, as SA08's D-C15 did on 136/334.

## 4. What is left open, and whether a successor prompt is warranted

**SA09's results do not warrant a finishing prompt.** No item of the prompt as it ran is undecided. What remains for
cotes 137-138 is checking, not research:
- A1.7's converse;
- the finite models of A1.5, A1.6 and A1.8;
- the completeness of B3.1;
- the hypotheses of B4.4 against Schinzel and the S-unit theorem;
- the reading of 137:38-39 behind A3.2.

A reader or a Claude check can do these, at the next use of those results.

**The update of about 11:50 UTC is superseded for its items A.1-A.4 and B.1-B.4.** Only its A.5 (C.3) and A.6 (D-031)
still have no run.

**The smallest home for C.3 and D-031.** No unsent prompt is in their cluster: SA21 has been sent, SA22 is surgery and
the 1964 thesis problems, SA11 is stratified spaces, and SA20 is the Esquisse.
- **D-031 needs no Pro slot.**
  - It is one proposition (Caradot and Lin, arXiv:2511.22614v4, Prop. 3.10, with §2.1 and Theorem 3.15) against one
    finite counterexample (RESEARCH_SA08's `sections/D_rejected_lifting_source.tex` and
    `logs/D_lifting_counterexample.json`).
  - One Claude agent at effort max can check it, against the arXiv LaTeX source, in a bounded task.
  - Nobody is told anything before that check.
- **C.3 goes into a small Pro prompt of its own, at low priority.**
  - Its core is the text of A.5 in the unsent update: the item over Z, what SA08 settled (C06-C10, C16, C17), the gate
    (C30, C32, C34), every approach tried with where it failed, and the SA08 files to restore from.
  - Its new tools are now proved results, not open items: SA09's A2.2 (relatively left-exact functors out of the
    nonnegative finite-free complexes are determined by their disks) and A3.1-A3.2 (the tests R_n and the
    reconstruction from the full Γ-action). It would carry them as background, with `SA08_RESULTS_20261119.md` and
    `SA08_final_paper_tex.zip`.
  - D-031 could ride along as its A.6, if a Claude check is not wanted. It is one of C.3's failed approaches anyway.

## 5. Corrections that bear on the transcription and the second passes (cotes 137-138)

The run states that none of its corrections rests on an inspection of the ink. Those that touch his text and need a
reader on the scans:
- **137** (MPL_137_045-086 l.1221-1223): the typed associativity of the α's (A1.5-A1.7).
- **137** (MPL_137_045-086 l.1038): the precomposition with n·id_X (A1.2).
- **138:106-112** (MPL_138_090-133 l.531-574, 606, 704-708, 733-784): the signs he left in doubt in the P, Q
  computation. The run uses (α − c), subtracts (β+1)c, obtains −(5c² − 10c − 4)/36, and corrects the divisor
  (z² − αz − β)². The mathematics is checked (E01-E05); which of these are his and which are the transcription's is not.
- **138**, Table II (l.481): ρ_s(r_5) = r_4, and the omitted mirror map.
- **138, the Fermat torsors** (MPL_138_001-045 l.1263-1267, 1562-1572): the N-th-power reading of the Fermat equation,
  and the origins θ_N^{-1} e^{±πi/N}.

The reading of the source category of 137 as nonnegative is confirmed in our transcription (E13).

## 6. Rows for the register

**Check events:** the 17 rows INT-SA09-E01 to E17 in `INTAKE_RESEARCH_SA09_20261119_CHECK_EVENTS.tsv`. The columns
are id, statement_id, date_utc, who, type, outcome and where. The topic table `SA09/CHECK_EVENTS.tsv` is left as it was.

**Corrections.** The columns are as in SA09/CORRECTIONS.tsv. For every row, decided_by is "the RESEARCH_SA09 final,
GPT-6 Astra (ChatGPT Pro mode); intake by Claude Opus 5.5 at effort max, a34c04448e8299803"; that column is left out of
the table.

| id | where | kind | what | corrected | evidence |
|---|---|---|---|---|---|
| INT-SA09-K01 | prompt L1; STUDY | our lead refuted | his polynomial categories are Γ^d P of Friedlander-Suslin | Hom(Γ^d X, Y) (laws) is not Γ^d Hom(X, Y); the bridge is a law action on linear Hom (A1.3-A1.4) | E11 |
| INT-SA09-K02 | prompt L3; readings SA09_137-138.md l.195-198 | our lead refuted | the Σ-exact source is a Frobenius category | the source of 137 is nonnegative and not Frobenius; the integer-graded enlargement is (A2.1, A2.6) | E13 |
| INT-SA09-K03 | readings SA09_137-138.md l.793; prompt R9 | our reading corrected | "the cubic P(c)" | the raw P is quintic, −δp/7776; the cubic is p (B2.1) | E01 |
| INT-SA09-K04 | prompt R6 | our claim qualified | the grading is recovered only after inverting the primes with (p−1) ∣ (n − n') | inverting them is sufficient, not necessary (A1.9) | A1.9, not rechecked |
| INT-SA09-K05 | 138:99 | his claim refuted (ours confirmed) | pinned maps are rigid; count = classes × ∏ a_n! b_n! c_n! | count = sum over classes C of #Γ_T / #I_C; torus E = Z/4 has 1 pinned class against 2 (B1.1-B1.2) | E06 |
| INT-SA09-K06 | 138:104-112 | his computation completed (ours confirmed) | two maps of passport [3,2,1; 2,2,1,1; 6]; P(c) unfinished | three maps over Q(∛2), one S_3 orbit; δ's roots 16/25 ± 12i/25 have passport [3,2,1; 3,1,1,1; 6] (B2.1-B2.5) | E01-E05 |
| INT-SA09-K07 | 137:14-15 (Prop. 1 e) | his claim refuted (ours confirmed) | boundedness ⇔ polynomial fibre ranks | bounded normalization ⇔ uniformly polynomial ranks over every ring; perfection needs separate criteria (A4.2-A4.5) | E12 |
