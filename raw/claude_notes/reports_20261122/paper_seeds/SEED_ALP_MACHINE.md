# Paper seed: Alpöge's lift machine

By Claude Opus 5.5 at effort high (agent abcaba9b6ae84b747), 22 November 2026, for the main session (Claude Opus 5.5 at
effort max). One paper. Two separate runs of prompt 49 by GPT-6 Astra (ChatGPT Pro mode) feed it:

- **run 19:35** opened 21 Nov 19:35:32 UTC; newest here is checkpoint 25 (22 Nov 16:35 UTC), the ZIP
  <local>/Downloads/ALP_MACHINE_checkpoint_25.zip;
- **run 20:03** opened 21 Nov 20:03:51 UTC; the checkpoint-04 intake was of this run; newest found here is
  <local>/Downloads/ALP_MACHINE_checkpoint_08(1).zip (22 Nov 02:03 UTC). Its ids AM-L, AM-SS, AM-ST, AM-S do not
  occur in the other run.

Citation marks: **[opened]** I opened that source; **[from memory]**; **[not opened]** the locator is a run's.

---

## Title

**How long must the chain of theta lifts in Alpöge's proof be?**

## Main theorem

### Setting

Alpöge's proof of RH and of GRH for Dirichlet L-functions (note *Remark*, 20 Nov 2026, with a Lean development) climbs a
chain of m theta lifts (step 8). Its parameters live in a record whose numerical hypotheses form one predicate,
`SizesAt`. In it x > 1 is the main parameter, 0 < ε < 1/52, L = x^ε, f = 2n is the degree of the totally real subfield F, and the CM field E has degree 2f [corrected 23 Nov 2026, NIGHT_AFTER_ALPOGE cp11 intake by abcaba9b, Claude Opus 5.5 at effort high], k is the initial
rank, and m is even with 2 ≤ m ≤ f ≤ k and m + 3 ≤ k.

### Theorem

For every datum satisfying `SizesAt`, at the pinned commit 7cbf7a0c32fca1badf05931879a37c3f8a2b03b4:

1. x^{1/2 − 29ε/400} ≤ m ≤ x^{1/2 − 21ε/400}. The chain length is the square root of the main parameter, up to
   x^{O(ε)}. So it is unbounded in every parameter family that the proof uses.
2. (log f)² ≤ m/2 − 1. In particular a two-step chain (m = 2) is impossible, for every field, rank and choice of primes.
3. L > 2^300, m > 2^7778, f > 2^33598 and k > 2^73197.

### Exact strength

- This is a theorem about the hypotheses of Alpöge's formal proof as written. It is elementary: an elimination among
  his inequalities.
- It is **not** a theorem that a proof by theta lifts needs a long chain. A changed size interface may allow a short
  one. That is the research question below.
- It does not touch the truth of his theorem, and is not a criticism of it. The proof lets x tend to infinity, so a
  floor on x costs it nothing.
- It does not show that the size predicate is inconsistent at large x.
- **Inputs:** the definitions in the Lean source (unrefereed; read as source; not built by the run or by me). No
  theorem of the development is used.

### Proof

Write θ = ε/100 and δ₁ = x^{−ε/8}.

1. `SizeM` is x^{−θ}√(xδ₁) ≤ m ≤ x^{θ}√(xδ₁). The exponents are 1/2 − ε/16 ∓ ε/100.
2. A conjunct of `SizeKRel` is log f ≤ √(r_S), with r_S = m/2 − 1 in natural numbers (exact, as m is even and ≥ 2).
   For m = 2 the right side is 0 and the left side is positive.
3. `SizeG` at i = j = 0 gives (k·e^L)^8 ≤ g and log g ≤ x^{θ}L = L^{101/100}. As log k > 0, L^{1/100} > 8, so L > 2^300.
   As x > L^52, the lower bounds in `SizeM`, `SizeN` (n ≥ x^{2+799ε/100}) and `SizeK` (k ≥ x^{9/2+999ε/100}) give
   log₂m > 300·10371/400, log₂f > 1 + 300·11199/100 and log₂k > 300·24399/100. ∎

## Why it matters

The first question anyone asks of a new proof of RH is how much of the machine is needed. The paper answers it for the
proof as formalized: the number of lifts is not a detail that can be set to two, it is tied to the size parameter by
the hypotheses, and the theorem names the three lines that tie it. Anyone who wants a short-chain or effective version,
or to move the machine to another family of L-functions, must replace exactly those hypotheses.

## The works it answers

- **L. Alpöge, *Remark*, 20 Nov 2026, alpo.ge/remark.pdf, step 8, with its Lean archive**: continues it. [opened: the
  Lean files Formalism/SharpRestriction/ElevenLe.lean 1–50 and 118–141 (SizeN 24–25, SizeM 27–29, SizeK 31–33,
  log f ≤ √r_S line 44, SizeG 123–125, SizesAt 134–138); Formalism/LocalRingCardinality/DataParams₂.lean 9–45 and
  Params.lean 6–46; Formalism/SharpRestriction/ParConsts.lean 31–44; FamCore.lean 71–85, all in the ZIP's copy.
  The note itself: not opened in this pass.]
- **"A short proof of Deligne's bound for Frobenius eigenvalues, after Alpöge", Hexagon 2611.00789 (v5 by Claude
  Fable 5.2 at effort max), Proposition remainder and Lemma tensor** [from memory: the statements, read on 21 Nov]:
  the phase section says exactly what can replace its sign.
- **Kassel–Kobayashi, Th. 7.8; Muić, Th. 4-2(i)** [not opened]: inputs of the bottom cusp construction.
- **Corrects or refutes:** no published work. It corrects our own expectation (DP_MULT Q3e, THETA3 G1) that the
  two-edge mixed CM family could be promoted to an instance of the proof.

No literature or Hexagon search has been made. The prompt searches first, in general terms.

## The other results, in the order of the argument

1. **No fixed small field helps** (run 19:35, LIFT54 §5). Neither f = 42 nor f = 168 satisfies `SizesAt` at any scale.
   *My check: §§1–5 read to the contradiction at f = 42 and 168; no fault.*
2. **The CM fields of y² = x⁷ − 1 in particular** (R023). The fields used have Galois exponent 42, while the formal
   host needs a cyclic quotient of order 4. Retaining them in an enlarged host forces n ≥ 21·2^282. *Statement only.*
3. **The Jacobian cannot be relabelled as elliptic** (R003): neither powers nor field extensions make it an elliptic
   Serre tensor. *Statement only.*
4. **What does exist outside that interface** (run 19:35; *statements only*):
   - two-edge theta kernels on explicit CM hosts J¹⁴ and J⁵⁶, with the six analytic predicates at m = 2;
   - a nonzero composite of the two edges (LIFT26);
   - for every length, injective vertical maps (LIFT56–58) and a nonzero cusp space at the bottom (LIFT59, for the
     standard Hermitian model, under its finite, splitting and numerical hypotheses).
   These show that size, and not vanishing, is the obstruction proved here. The arithmetic pairing and the sign of the
   cost difference are open.
5. **The sign may be replaced by a phase only in one way** (run 20:03, AM-S1–S3; *targeted proof checks by me*):
   - if s has finite order d and commutes with Frobenius F on an actual module, bounds on Tr((sF)^{dn}) bound every
     eigenvalue of F;
   - traces Tr(sFⁿ) with a reflected s see only the part fixed by the rotation, and bound nothing on the rest
     (counterexample: the standard representation of S₃ ⊗ Q_ℓ(−N));
   - if s inverts a rotation of order 3, every homomorphism that makes s central kills that rotation.

### Update at checkpoint 29 (22 Nov 19:35 UTC, run 19:35)

- **The main theorem is unchanged.** LIFT54 and LIFT55 are byte-identical.
- **New local results.** Under explicit generic and tempered local hypotheses, the positive-rank split Bessel test of
  the T-place is nonzero, with exact phase and modulus (LIFT068). Under the full size package, the chosen bottom and
  the initial constituents satisfy those hypotheses (LIFT069, LIFT070). The canonical Hilbert/GGP factor is
  q/[(q−1)(q^k−1)] (LIFT071). All statement level for me. They supply local factors for the period; they do not give
  the global period.
- **The finite signed gate.** Its support floor rose from 12 to 18 (R057, R060, R062). The support-17 count is an
  estimate that the run itself says fails at support 18, so each further level needs a new structural argument. This
  is one sufficient inequality on the way to one nonvanishing statement. It is bookkeeping, not a theorem for this
  paper.
- **An in-run error, corrected.** DO079-C1: a word-invariance identity was false, and the run's earlier whole-proof
  PASSes had missed it. The bounds survive with the corrected formula. If the paper uses DO079, it cites the
  correction.
- **Masullo.** Nothing in this paper uses or presents a fix of Masullo's GRH draft. Any row the run calls "Masullo's
  consequences" is conditional on GRH for the Hecke L-functions concerned, an open hypothesis.

### Update at checkpoint 32 (22 Nov 21:50 UTC)

- **The main theorem is unchanged**: LIFT54 and LIFT55 have the same hashes.
- **The bottom period is reduced to one global statement.** By LIFT072–074 and LIFT076, if the two specified embedded
  occurrences are globally Bessel-distinguished at the fixed level, the prescribed period is c_Per·b̄ ≠ 0. All local
  factors are computed, and the representations are tempered with simple parameters. This belongs in the paper as the
  exact form of the remaining gate on the analytic side.
- **One construction excluded.** LIFT075: for a split type-II lift GL_a → GL_r with d = r − a > 0, every principal-level
  constituent has a linear Green factor of multiplicity ≥ d, so Alpöge's e0 kills the direct compact-source theta
  projection for every even m. My check: targeted, given Mínguez 2008 Th. 1(2) and Gow–Vinroot 2007 Th. 3.2 (not
  opened), with the IsGood clauses checked in the Lean source.
- **The finite gate** has floor 23; it remains bookkeeping, not a result for the paper.
- **Add to the research question's routes:** fixed-level global Bessel distinction for the two occurrences, by a
  relative Poincaré series at prescribed level or by an adapted globalization (Prasad–Schulze-Pillot 2008, Th. 4.1).

### Update at checkpoint 35 (23 Nov 00:05 UTC)

- The main theorem is unchanged, and follow-up 49b had not yet been taken up.
- **LIFT077** (statement level): the global coupling of LIFT074 satisfies an exact central-value formula, |b|² = (an
  explicit positive constant) · (a ratio of L-values at s = 1/2) · (local factors). So the bottom period's
  nonvanishing is a central-value nonvanishing question, of Ichino–Ikeda/GGP shape. If proved in full, this is the
  natural form of the analytic gate in the paper.

### Update at checkpoint 55 (23 Nov 15:05 UTC; intake by abcaba9b6ae84b747, Claude Opus 5.5 at effort high)

- The main theorem is unchanged (LIFT54/LIFT55). Follow-up 49b has still not been taken up by this run; the bounded-chain
  question is worked in NIGHT_AFTER_ALPOGE Part B.
- **A second structural obstruction for the paper (LIFT110, proof read and checked):** let K be imaginary quadratic with
  mu(K) = {+1, -1}, F/K finite abelian, J a nonzero integral K-ideal, and suppose J O_F = (xi) with
  |sigma(xi)|^2 = N(J) for every complex embedding sigma of F. Then [J]^2 = 1 in Cl(K). Proof: J^h = (gamma) in K;
  u = xi^h/gamma is a unit with every conjugate of absolute value 1, hence a root of unity (Kronecker), so
  xi^{hm} = gamma^m; the splitting field of X^{hm} - gamma^m over K lies in F(mu_{hm}), abelian, so Schinzel's theorem
  gives gamma^{m w} = b^{hm} with w = gcd(hm, 2), hence J^w = (b). Applied to Alpöge's formal source: the normalized kPsi
  law, with N_{E/K} onto Cl(K) for a prime discriminant -d (LIFT109) and the class above 2 of odd order h_2 >= 7
  (2^{h_2} >= (d+1)/4, d > 365), forces every coefficient field of a literal instance to lie outside K^ab. In
  particular the cyclotomic field E Q(zeta_M) and its compositum with the Hilbert class field of K are excluded.
- **The finite signed gate** (DO129): support 27 is absorbed into nonnegative completions; the open sufficient
  inequality is Re(sum over support >= 28) > -1 + 2^{-230}. Bookkeeping, not a result for the paper.
- *Checkpoint 59 (18:05 UTC):* the obstruction has its sharp converse. LIFT112: a field F carrying the normalized table
  for an odd class subgroup G of order g has g | [F : F ∩ K^ab]; over any abelian B/K the radical field
  B(alpha_i), alpha_i^{h_i} = gamma_i, has degree exactly g and meets K^ab only in B (Kummer theory plus LIFT110;
  §2 of the proof checked). LIFT113: that field is CM, and F(mu_e) is CM, Galois over Q and metabelian. So a literal
  instance needs a metabelian, non-abelian coefficient field of relative degree exactly h_K, and one exists. The
  signed gate is at support >= 29 (DO135).
- *Checkpoint 67 (24 Nov 01:08 UTC):* R110, LIFT117–120 and R108 transport a supplied complete formal family to the
  ring of integers of that fixed ambient field with all constants unchanged; the reconstruction cost 2 log c0 is
  below exp(x^eps) for x >= 32 q!, q = ceil(13/eps) (LIFT118; rechecked). The initial family is still not constructed.
  The signed gate is at support >= 31 (DO143).

## The research question of the prompt

> **Can step 8 be carried out with a chain of bounded length? Prove it, by a replacement for `SizesAt` under which the
> whole deduction of RH goes through with m bounded, or prove that within the theta-lift method the cost balance
> forces m to infinity.**

**The gate now.** The difference of lift costs (DP44 in our DP_MULT run) has no proved sign for any short chain. On the
two-edge family the analytic side is constructed, as stated by the run, and what is missing is the nonzero arithmetic
bottom period with its normalized mass (Q1/Q2 of run 19:35). Its current finite gate is a signed kernel sum, reduced
to support ≥ 12. That reduction is internal bookkeeping and is not a theorem for this paper.

**Routes not yet tried.**
1. Find in the Lean dependency graph every use of `SizeM`, `SizeK` and log f ≤ √r_S, and state for each the weakest
   inequality that its consumer needs. This is finite.
2. With m = x^μ, n = x^ν, k = x^κ and every consumer's inequality as a linear constraint in the exponents, solve the
   linear program for the infimum of μ. μ = 0 gives a candidate interface. μ > 0 gives a certificate that names the
   binding steps, which are then attacked one by one.
3. Find where the saving that comes from √r_S enters, and test whether a larger rank step per lift (a jump in the Witt
   tower) gives the same saving in fewer lifts.
4. Prove the theorem above in Lean against the pinned commit: it is a short deduction from the definitions and would
   give the paper its formal check.
5. For another field of L-functions (Kummer characters over Q(ω); Q3 of both runs), run the same program before any
   construction: it says in advance what size interface that case needs.

## Proof files, programs and checks

ZIP25 = <local>/Downloads/ALP_MACHINE_checkpoint_25.zip, member prefix ALP_MACHINE/.
D = <local>/Documents/reports_20261122/overnight_intake/ALP_MACHINE. The run's checks are by GPT-6 Astra
(ChatGPT Pro mode), mine by Claude Opus 5.5 at effort high (agent abcaba9b6ae84b747).

| Result | Proof file, lines | Programs | Checks |
|---|---|---|---|
| Theorem 1 | this seed; its lower half is SL8 in <local>/Documents/reports_20261122/overnight_intake/ALP_MACHINE/cp25/literal_size_chain_length_obstruction.md §4 | none needed | upper half added by me, author's check; lower half targeted proof check against the Lean definitions |
| Theorem 2 | the same file, §§1–3 | ZIP25 agents/literal_size_chain_length_certificate.py (not run by me) | run: whole-proof checks by two agents and 413 exact assertions; me: targeted proof check against the Lean definitions |
| Theorem 3 | <local>/Documents/reports_20261122/overnight_intake/ALP_MACHINE/cp25/universal_size_scale_floor.md, whole file, §3 the main step | ZIP25 agents/universal_size_scale_certificate.py (not run by me) | run: whole-proof check, second-agent replay, 94 assertions; me: targeted proof check, exponents recomputed |
| fixed fields | LIFT54 file, §5 | as Theorem 2 | targeted proof check |
| R003, R023, LIFT26, LIFT56–59 | ZIP25 ALP_MACHINE.tex (the sections carrying these ids; line ranges not located) and ZIP25 scripts/literal_host_rank_scale_certificate.py | as listed | the run's checks; me: statements only |
| phase lemmas | <local>/Documents/reports_20261122/overnight_intake/ALP_MACHINE/run2003_cp08/oscillator_sign.tex 392–542 | none | targeted proof checks, reread 22 Nov |

## LaTeX and sources to attach

- The two proof files above (Markdown with TeX formulas) and oscillator_sign.tex.
- <local>/Documents/reports_20261122/overnight_intake/ALP_MACHINE/cp25/QUESTIONS.tsv and IMPLICATIONS.md.
- <local>/Documents/reports_20261120/deligne_sign_only_paper/deligne_sign_only_v5.tex.
- For reading only: Alpöge's Lean files named above, from ZIP25 research/alpoge_source/, and his note.

## Never to GitHub: other people's files

- <local>/Documents/reports_20261122/overnight_intake/ALP_MACHINE/sources_cp25.txt lists the 1,299 candidate
  members of ZIP25 found by name and folder. It can catch our own files too, and is not proof that nothing else is
  foreign.
- Certainly foreign: ZIP25 research/alpoge_source/ (831 Lean files), research/external_sources/, every agents/*_source,
  *_sources, *_refs and *_source_refs folder, the source copies under recovery_pending/, and every SGA or paper PDF,
  excerpt and OCR file. The licence of Alpöge's archive was not checked.
- TASK_PROMPT.md is ours; the attachment ZIP of prompt 49 carries others' works.

## Workbench

**Alpöge's RH proof: the machine and its limits**, beside the workbench of the Connes and Artin-conjecture seeds. One
folder per run, the two ALP_MACHINE runs kept apart.
