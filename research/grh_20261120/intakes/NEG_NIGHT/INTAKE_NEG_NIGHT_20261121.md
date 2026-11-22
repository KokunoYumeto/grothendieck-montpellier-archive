# Intake of NEG_NIGHT (prompt 54), checkpoint 04: the findings NN-S, NN-A and NN-C, 22 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent a17221e5; launched by the main session, Claude Opus 5.5 at effort max).
The user asked on 21 Nov, about 23:5x UTC: "do the intake in general ... I also want the full intake".

**The run.** GPT-6 Astra (ChatGPT Pro mode), started 21 Nov 20:04:37 UTC, still going. This is checkpoint 04 of 23:05
UTC, taken right after its first formal movement review (movement: yes). The run's own effort is not exposed.

**Scope.** This intake covers everything except the GCT findings NN-G001 to NN-G031, which agent a8d75352 takes
(`INTAKE_NEG_NIGHT_20261121_G.md`, in this folder). My part is 76 findings:
- NN-S001 to S016: the split-zero framework and sign-fixed loci;
- NN-A001 to A030: zeta labels, CUE, heat flow;
- NN-C001 to C030: complexity consequences of E and the finite Weil objects.

## 0. What was read

- **Return folder:** `research_returns\NEG_NIGHT_checkpoint_04_20261121T2305Z_unzipped`, the only one present.
- **Read:**
  - `README.md` and `INPUTS_AND_SOURCE_STATUS.md`;
  - `TASK_PROMPT.md`, the cited results and the task list;
  - `LEDGER.md` in full, including the first formal movement review;
  - `CONSEQUENCES.json`: the statements and inputs of all 76 findings of my part;
  - `IMPLICATIONS.md` and `QUESTIONS.tsv` at the level of the main gates.
- **Read in full, with proofs:** in `paper_parts\analytic.tex`, NN-A001, A002, the statement and core steps of A003
  (lines 179-300), A010, and A017's formula; in `paper_parts\checked.tex`, NN-C001 to C004 (lines 1-124) and NN-S001 to
  S003 (lines 6397-6540).
- **Computations, all in my work folder (scratchpad `negnight\`, never inside the return):**
  1. *The run's checkers, rerun with `python -I -B`:* `check_label_1169.py` (A001, FLINT/Arb),
     `check_cue_agreement.py` (A017), `check_finite_detection.py` (A014) and `check_central_jets.py` (A018). All PASS,
     with outputs matching the run's certificates.
  2. *`a001_mpmath.py`, my own code (mpmath, independent of FLINT):* it recomputes ρ_n, ζ'(ρ_n), ζ(ρ_n + 1), the
     velocity v_n, Siegel's θ, W_n and δ_n at n = 1, 871, 1169. It also checks the identity (A001.1) numerically
     (Z' by numerical differentiation of Siegel's Z). At n = 1169:
     - γ = 1613.0788554510274235;
     - W = −6.06299724188·10⁻⁵ and δ/π = 9.86653178528·10⁻⁵;
     - sin πW = −1.90·10⁻⁴ < 0, while sin(πW + δ) = 1.19·10⁻⁴ > 0;
     - Re v = 0.0259256519671638 > 0, equal to the right side of (A001.1) to 15 digits.
  3. *`a017_bornemann.py`, my own code:* Bornemann's Gauss-Legendre Nyström discretization of det(I − K_s) for the sine
     kernel, a method different from the run's Taylor/Arb one. It gives E(1), ..., E(6), agreeing with the run's
     values to 20 digits (E(1) = 0.17021742137918523073), and A_adj = 0.66654660183721072007, inside the run's certified
     interval (0.66654660183721072003, 0.66654660183721072008).

## 1. Verdicts

### Confirmed by targeted proof check (12), two of them also by independent re-proof

| id | statement | check |
|---|---|---|
| NN-S001 | a G(R)-semimodule is a disjoint union of R-modules M_b over the join-semilattice B = eM. So Fix(u) = ⨆ ker(u−1 on M_b) and Fix(−1) = ⨆ M_b[2]. It is Boolean iff no fibre has 2-torsion; Z/2 over G(Z) is a counterexample | proof read: the identities e+e=e, 1+e=1, 1+(−1)=e give the fibre module structure |
| NN-S002 | the sign-fixed scheme on 𝔸^d_Z is Spec Z[x]/(2x), non-flat, with the whole affine space as its characteristic-two fibre | proof read (elementary; the run credits SGA 3 I, Rem. 4.7.1.2, corrected edition 2024) |
| NN-S003 | additive maps from idempotent monoids are zero; R ⊗_{G(R)} 𝔹 = 0; Boolean data do not determine Weil weights | proof read |
| NN-A001 | the exact right-mover criterion is sin(πW_n + δ_n) > 0, δ_n = arctan(1/(2γ_n)); the uncorrected rule fails at zero 1169 | (A001.1) rederived by hand: implicit differentiation with DLMF 25.11.17, ζ'(ρ) = −ie^{−iθ}Z'(γ), sign of Z' equal to (−1)^{n+1}, the trigonometric identities. **Independent re-proof by computation** (mpmath), and the run's Arb certificate rerun |
| NN-A002 | a CLT for S(γ_n) does not give equidistribution of W_n mod 2; the sufficient gate is odd Fourier modes plus boundary control (A002.1); exact mode formula (A002.2) | proof read: the counterexample X_j = 2⌊σ_jG/2⌋ + 1/4, the Fejér argument, the identity (A002.2) |
| NN-A010 | Hurwitz-completed residues at −2m are −2(−1)^m π^m B_{2m+1}(1+t)/(m!(2m+1)): zero at t = 0, nonzero derivative, nonzero at t = 1 | checked: Γ(s/2) residues, ζ(−2m, a) = −B_{2m+1}(a)/(2m+1), B_{2m+1}(1) = 0, B'_{2m+1}(1) = (2m+1)B_{2m} ≠ 0, B_{2m+1}(2) = 2m+1 |
| NN-A017 | the limiting adjacent CUE label agreement equals 1 − 2Σ(−1)^{n+1}E(n), certified in (0.66654660183721072003, ...072008) | formula rederived by me from A003.1: integrate the triangle wave d_2(1−s) against P⁰(D_1 > s) = −E'(s). **Independent re-proof by computation** (Bornemann), and the run's Arb certificate rerun |
| NN-C001 | quasilinear sparse systems over F₂ compress to at most 6n combinations with the same Boolean zeros, at E's cost | proof read: E Lemma 6.1 code distance m/P; greedy conditional-expectation rows (rejection at least 1/4 per round); (27/32)^n < 1 after 3n rounds; Lemma D.2 interface. Conditional only on E's lemmas, which are cited |
| NN-C002 | fixed F_{2^r}: counts, lexicographically first witnesses, exact uniform sampling | proof read (restriction of scalars to F₂, prefix self-reduction, telescoping sampling) |
| NN-C003 | exact rational weighted partition functions with polynomial bit cost | proof read (bit encoding, high-incidence branching, common denominator Ω, Cramer readout); given E Prop. 3.4, Lemmas 4.7-4.8, App. B |
| NN-C004 | fixed algebraic tensor alphabets and quantum amplitudes in 2^{O(s/√log s)} | proof read (primitive element, integer coefficient polynomial in V, precision bound, D.1) |
| NN-C005 | N mod 2 = [x_1⋯x_n] ML(Π(1 + f_i)), and this is ⊕P-complete for O(n) sparse quadratics | checked: Π(1 + f_i(x)) is the indicator of the common zeros, and summation over the cube keeps only the top multilinear coefficient mod 2 |

### Checked by reading the statement against known results, without a full proof reading (9)

| id | point checked | outcome |
|---|---|---|
| NN-A003 | the determinantal identity (A003.2), the leakage bound (A003.3-5) and the odd-mode reduction read | consistent; the rest of the proof not read |
| NN-A007 | positivity of c_k(t) from Φ > 0; the PF ↔ Laguerre-Pólya equivalence (Aissen-Schoenberg-Whitney-Edrei) gives total nonnegativity exactly for t ≥ 0 under A, with Rodgers-Tao for t < 0 | consistent |
| NN-A015 | the limit weights 8/[π²(2j−1)²] are the zeros of cosh √(2w) = Π(1 + 8w/(π²(2j−1)²)), and they sum to 1 | checked |
| NN-A016 | σ_j = sqrt(log j)/π matches the classical variance of sine-process counts | consistent |
| NN-A018 | the certificate: C_* gives exp(2C_*) = 4370.59 < 4371; the Q8 bound C_K < −3.5197 | the run's checker rerun PASS |
| NN-A024 | A_N ≥ −log cos(δ/2) ≥ δ²/8; the pair-collision time is δ²/8 (dδ²/da = −8); the Weibull-3/2 law is the image of Ben Arous-Bourgade's N^{4/3}δ_min/(72π)^{1/3} ⇒ e^{−x³} | consistent with the cited theorem; proof not read |
| NN-A026 | conjugate factors pair into real quadratics with cos θ ≥ 1/2, so the coefficients are positive; the zeros at −e^{±iπ/3} | consistent |
| NN-C014 | singletons are zero sets of n sparse linear equations, so any hitting set is the whole cube | checked (trivial) |
| NN-C023, C024 | the coefficient of z_1⋯z_r in F is the Hasse-Witt (Frobenius) scalar of the degree-r hypersurface in P^{r−1} over F₂; the Fermat pencil H + uF is smooth for odd r | mechanism checked; proofs not read |

### At statement level only (55)

The statements were read in CONSEQUENCES.json, with no fault found, and the proofs were not read:
- NN-S004 to S016;
- NN-A004 to A006, A008, A009, A011 to A014, A019 to A023, A025, A027 to A030;
- NN-C006 to C013, C015 to C022, C025 to C030.

A014 and A018 have their certificates rerun.

**Counts:** 12 confirmed by targeted proof check, 2 of them also by independent re-proof by computation (A001, A017).
9 checked by a partial reading or a check against known results. 55 at statement level. **None refuted.**

## 2. What is new, and how it bears on the programme

1. **NN-A001: the corrected zero-motion label.** It is new. It corrects our consult ad855737 (`OURS_CONSULT_ad855737_ZETA_LABELS.md`,
   Q1, Proposition 1) and the label rule in our prompt's item 11. That rule omits the arctangent phase δ_n.
   - *The counterexample.* At zero 1169, sin πW < 0 but the zero is a right-mover. It is certified, and I re-proved it
     independently.
   - *How it bears.* The Boolean label of zeros is a sign of a normal velocity, not a character. NN-A001 and A002 make
     the "half the labels positive" question an exact Fourier gate on (−1)^n e^{−ikθ(γ_n)}e^{−ikφ_n}, for odd k.
   - *What A does here.* A turns the ordinates real, and Arias de Reyna's cancellation for e^{2iκθ(γ)}, κ < 6/5, then
     applies. The alternating sign and the exterior phase are the missing pieces.
   - *The attack this opens.* Prove the odd-mode cancellation with the (−1)^n twist. Pair the twisted sum with
     Gram-point counting: (−1)^n e^{−iθ(γ_n)} is the sign of Z' times a unit, which Gram's law statistics
     (Korolev, Trudgian) control at the fixed frequency k = 1.
2. **The CUE model (A003, A016, A017, A024, A025).** A complete model theory for the labels and for backward-heat
   collisions:
   - the marked label is uniform and independent of the gaps (A003);
   - long-range decorrelation (A016);
   - the adjacent agreement constant 0.666546601837... (A017, independently checked);
   - the first collision at time δ_min²/8 with a Weibull-3/2 law (A024);
   - a Poisson collision process of intensity (3/2)√v dv (A025).

   The arithmetic transfer, the extreme-gap process for zeta zeros, is the named open gate (main gate 7).
3. **Backward heat and simplicity of zeros (A014, A020 to A022, A027 to A030).** Under A, the least order of a
   negative Toeplitz minor at time −a diverges as a → 0.
   - *A028.* All nontrivial zeros are simple if and only if √a·m_*(−a) → ∞. This turns simplicity of the zeros (an
     open problem even under RH) into a growth rate of finite positivity detection.
   - *A029 and A030.* They make the constants explicit (Hermite orbital radii as Wronskian zeros).
   - *A010.* It closes a two-endpoint principal-part model.
4. **The split-zero framework (NN-S001 to S016).** The sign-fixed Boolean pair is a fibrewise 2-torsion phenomenon,
   with a non-flat characteristic-two fibre (S001, S002). Linearization kills the support skeleton (S003). The
   remaining S findings place counting and parity in actual geometric objects, without any algorithmic gain.
5. **Complexity (NN-C001 to C030).**
   - *From E.* E extends to quasilinear sparse systems (C001), fixed finite fields and rings (C002, C017, C018),
     weighted partition functions and quantum amplitudes (C003, C004), symbolic partition polynomials (C016) and
     ideal certificates (C029).
   - *The limits it meets.* PIT (C012), universal hitting sets (C014), proof systems (C008, C009, C021) and isolation
     (C007, C019) are all located exactly.
   - *The arithmetic-geometry line.* Counting and parity sit in genuine smooth Weil objects. C023 and C030 give
     ⊕P-hardness of the Frobenius scalar on the top coherent cohomology of an explicit smooth hypersurface, with a
     deterministic specialization. C026 gives a smooth projective curve with #C(F_q) = 1 + 2#SAT. C027 gives a smooth
     sparse cubic scheme over Z with [X] = 𝕃^{v+h} + N𝕃^h, and S016 its Chow ring and homotopy type. C028 makes
     embedding comparison of actual Tate cohomology PP-complete.
   - *How it bears on A.* These results say exactly where purity stops helping: A controls the zeros of
     ζ_X(s) = ζ(s−v−h)ζ(s−h)^N, but the counting difficulty is in the multiplicity N. That is the gate.
6. **The GRH scope.**
   - *C010.* Bürgisser's characteristic-zero transfer (VP_C = VNP_C ⇒ #P ⊆ FP/poly) needs RH for Dedekind zeta
     functions of arbitrary number fields. So it is conditional on M; A does not suffice.
   - *C015.* The constant-free version needs neither A nor M.

   Both agree with our CX_GRH and GRH_NIGHT audits.

## 3. Errata and literature points

1. **Our consult ad855737 (ZETA_LABELS).**
   - *Q1, Proposition 1.* Its stated equivalence omits the correction term that its own proof displays. The correct
     criterion is sin(πW + δ) > 0; the counterexample is n = 1169 (NN-A001).
   - *Q2, Proposition 4.* The claimed CLT ⇒ half-proportion implication is invalid (NN-A002).
   - *Our prompt 54, item 11.* It repeats the uncorrected rule.
2. **Our split-zero corpus, paper 16** (NN-A012, statement level).
   - *The tensor-inverse identity fails.* A_n(S4) = n for both q and −q, so the identity is off by n².
   - *The adelic-curve completeness claim needs a hypothesis* such as localizability. The countable/cocountable
     counting-measure example is σ-complete but not complete.
3. **Our prompt item 10(a).** The unrestricted claim that the sign-fixed part is Boolean for arbitrary coefficient
   semimodules is false. The correct form is fibrewise 2-torsion (NN-S001).
4. **Buss-Grigoriev-Impagliazzo-Pitassi (polynomial calculus modulo distinct primes), Corollary 21** (literature, NN-C021,
   statement level).
   - *The run's claim.* The printed proof appeals to Lemma 2 in the wrong direction, a reduction from the Boolean system
     to the root-of-unity system, where the reverse one is needed. The run supplies the reverse reduction.
   - *What it needs.* To be checked against the published paper before it is reported.
5. **SGA 3 I, Remark 4.7.1.2** (corrected edition of 13 Oct 2024, note 39). The run credits it as the source of the
   rank-one fixed-scheme example. That attribution is correct as stated: it is an editorial addition of that edition.

## 4. Hexagon readiness (the five tests of `field_experts\HEXAGON_CANDIDATES.md`)

None passes all five. The run is still going, so test 3 fails for all. The candidates:

| candidate | 1 complete | 2 self-contained | 3 stable | 4 checked | 5 interest | gate left |
|---|---|---|---|---|---|---|
| **NN-A028**: simplicity of all zeta zeros ⇔ √a·m_*(−a) → ∞ (under A), with A029-A030's explicit constants | yes as written | inputs A (Lean-checked), Rodgers-Tao, classical | no (run going) | statement level only | high (de Bruijn-Newman and simplicity) | an intake proof check of A020-A022 and A027-A030; a literature search (Csordas-Varga, Rodgers-Tao, Polymath 15); the final |
| **NN-A024, A025**: the CUE first heat collision (Weibull 3/2) and the Poisson collision process | yes | Ben Arous-Bourgade, published | no | partial (statement against the cited theorem) | moderate (random matrices) | a proof check; a literature search on heat flow of random polynomials (Kabluchko and others) |
| **NN-C027, C028, S016**: one sparse smooth cubic over Z with [X] = 𝕃^{v+h} + N𝕃^h. Recognising affine space is equivalent to unsatisfiability, and comparing Tate cohomology is PP-complete | yes | classical inputs | no | statement level | moderate to high (affine-space recognition, motivic complexity) | a proof check; a literature search (complexity of the Zariski cancellation problem) |
| **NN-C023, C024, C030**: deciding the Hasse-Witt scalar of an explicit smooth hypersurface over F_{2^b} is ⊕P-hard, deterministically | yes | classical | no | mechanism checked only | moderate | a proof check; literature (hardness of zeta-function and Hasse-Witt computations) |
| **NN-A001**: the corrected label with the certified counterexample at zero 1169 | yes | yes | yes for itself | yes, with independent re-proof | low to moderate (it corrects our own consult) | goes into the companion, not a post |

## 5. The attack each open gate opens

These are the run's main gates within my part.

- **Gate 6 (zeta labels).** The odd-mode cancellation with the (−1)^n twist. Use the identity
  (−1)^n e^{−iθ(γ_n)} = unit × sgn Z'(γ_n), and Gram-law statistics at fixed frequency. A (real ordinates) lets
  Arias de Reyna's κ < 6/5 theorem enter; the twist is what remains.
- **Gate 7 (the arithmetic collision height-time law).** Transfer A024 and A025 through the extreme-gap statistics of
  zeta zeros:
  - conditional on the pair-correlation and higher-correlation conjectures (Montgomery: proved by A for Fourier support
    in (−1, 1), CUE_GCT P-Z01);
  - or unconditionally at the level of A023's isolated-pair law, for every pair below a computable gap threshold.
- **Gates 10 and 11 (detection and multiplicity).** A028 reduces simplicity of zeros to a detection-growth statement.
  The next attack is to bound √a·m_*(−a) from below using the known proportion of simple zeros (Conrey's 2/5 and its
  improvements). This would give a positive-density statement on the detection side, unconditionally given A.
- **Gate 3 (NP isolation) and gate 2 (PIT).** C007, C012, C014 and C019 locate the obstacles exactly. E's counting
  constructs instance-dependent isolating weights (C019), but no polynomial-time uniform family. The next attack is the
  CUE_GCT isolation line (I-31 to I-44), which works with explicit ROABP structure instead of counting.
- **The geometric counting line (C023 to C030, S015, S016).** Purity (A for the zeta factors) does not touch the
  multiplicity N. The open question this opens is whether any cohomological operation of polynomial complexity (a
  Frobenius trace on a known line, a cycle class, a Chow-group rank) can extract N mod p for a prime p ≥ 3 on these
  families. C028 suggests the answer is PP-hard, and a proof would close the line.

## 6. What a successor prompt (or the continuing run) needs

1. **Literature search before novelty** for A024/A025, A028 and C027/S016 (section 4).
2. **Intake-grade rerunnable certificates for A029 and A030** (the Hermite orbital radii), so the constants can be
   checked independently.
3. **The BGIP Corollary 21 direction (C021).** Check it against the published text.
4. **Erratum notices** to our own consult ad855737 and to corpus paper 16 (section 3), to go into the records.
5. **Provenance:** GPT-6 Astra (ChatGPT Pro mode). No ways out.
