# Intake of GCT_NSRH, checkpoint 03 (what is new since checkpoint 01)

By Claude Opus 5.5 at effort high (the agent of the first intake, resumed), for the main session (Claude Opus 5.5 at
effort max), 21 Nov 2026. The run is GPT-6 Astra (ChatGPT Pro mode); it records its effort as "not exposed". It is still
going. First intake: `INTAKE_GCT_NSRH_20261121.md` (checkpoint 01, F01–F17). Work file:
`agent_notes\20261121_intake_GCT_NSRH_NOTES.md`.

## 0. What I read, and my scope

**Return:** `research_returns\GCT_NSRH_checkpoint_03_20261121T0115Z_unzipped\`, snapshot 01:15 UTC.
- The paper now has F01–F42.
- F43 and F44 exist as reports only, not yet integrated.
- No scheduled no-movement review has happened yet.
- I read: `QUESTIONS.tsv` (all 46 rows), `STATUS_TIME.txt`, and the archive table of the paper.
- `agent_rank3_positive_action.md` (F43): head only.
- `agent_kahle_michalek_audit.md`: head and conclusion.

**Read in full, with their proofs:**

| Finding | Content |
|---|---|
| F24 | Signed Euler spectra at even k |
| F26 | Rational normalization is not a finite trace |
| F42 | No common finite spectrum for all words |
| F34 | Dimension and #P obstruction for compact binary PH1 |

**Read in part:**
- F32 (countable spectra): the statement, and the proof as far as the generating-function part.
- F27 (derived and cone repairs): the statement.

**Read at the level of the statement only (QUESTIONS rows):** F18–F23, F25, F28–F31, F33, F35–F41, F43, F44. There are 25 new
findings in all; I gave the main-question ones (F24, F26, F32, F42) and F34 a full check.

## 1. Verdicts

### F24: signed Euler spectra at even k (main question). Targeted proof check, confirmed.

This replaces F03's input sign hypothesis by real nonzero coefficients on a finite visible spectrum, at even k.

The proof:
- Take the top-radius part F of the spectrum.
- F^k is not nilpotent, by a Vandermonde argument.
- Its coefficient sum is (Σc)^k ≥ 0, because k is even and the c are real.
- So at least one top-radius coefficient of F^k is strictly positive.
- That coefficient cannot be cancelled: products that involve a smaller root have smaller modulus, and the B_k spectrum
  adds only positive coefficients.
- F02 and the overhead bound then give the result.

Both counterexamples are checked.
- **Without visibility, under powering:** t_n alternates between 0 and 2, so M_n = q^n − (−q)^n, which vanishes for every
  even n.
- **Without real coefficients:** take t = i and k ≡ 2 mod 4. The pairing is nondegenerate, so the zero count is
  Q^m + (Q^m − 1)Q^{m−1}. That gives QN = −Q^k − Q^{k/2+1} + Q^{k/2}. With η = 0, the claimed bound |q| ≤ q^{1/2} would
  be false.

F24 strictly weakens F03's input gate: one-degree parity is not needed. Hidden (Euler-cancelled) roots stay out of reach,
and the paper says so.

### F32: admissible countable spectra. Statement and generating-function proof read; confirmed at that level.

The radius, uniqueness and residue argument are right.

The reciprocal-finiteness clause (a bounded visible dual forces a finite spectrum) is immediate: if every κ/α is visible
in a bounded dual support, the roots α accumulate only at 0, while the κ/α would then be unbounded.

### F26: a rational normalization cannot be a finite Weil trace. Targeted proof check, confirmed.

- The recurrence argument is right: f(b^n) is an exponential polynomial if and only if f is a Laurent polynomial.
- 24 + 16x²/(x + 1)⁴ has a genuine pole at x = −1, so it is not Laurent.
- The trace values 20 + 16/D + 4(D − 2)²/D² are taken from the run's F21 block decomposition, which I did not reread. The
  arithmetic closing to 24 + 16/D² is checked.

### F42: no common finite Frobenius spectrum carries all words. Targeted proof check, confirmed.

- 40D_n^k = 40 Σ_j C(2k, j) q^{(k−j)n} has 2k + 1 distinct roots, all with nonzero coefficients.
- A fixed finite F gives poles only at the inverses of its eigenvalues, so no fixed F can carry unbounded k.
- The multiplicity 40 = 20 + 16 + 4 is taken from F21 (statement level).

This is the sharpest new negative on the main question. The naive dictionary "substitute v = q^{n/2} into the traces of
the nonstandard algebra" cannot come from one finite Weil object. Any nonstandard RH must therefore use word-dependent
objects or an infinite or completed object (F35, F41); it cannot use one fixed cohomology.

### F34: VI Hypothesis 1.6.4(2) is false under compact binary input, and binary plethysm is not #P. Targeted proof check, confirmed.

- c_k(N) = [z^N] Π_{i=2}^k (1 − z^i)^{−1} is the classical two-row (Cayley–Sylvester) count. The (1 − z) factor comes from
  adjacent weights; checked.
- The simplex has dimension k − 2. Every bounded polytope with this Ehrhart function has dimension at least k − 2, by
  counting points in a box. VI's bound is poly(⟨μ⟩ = O(log k), ht λ = 1, ht π = 2), which is eventually smaller.
- Not #P: take k = 2m and N = m(m + 1). This gives at least 2^{m−1} solutions on O(log m) input bits. Checked.

### The other new findings (statement level, from QUESTIONS.tsv)

- **The rank-three geometry and coherent Frobenius models:** F19, F21, F22, F25, F36, F39, F40.
- **Satake and the Grassmannian:** F20, F23, F31, F33.
- **Rectangles and hooks:** F28, F29, F37.
- **The tower:** F30.
- **Stacks and finite windows:** F35, F38, F41.
- **The derived repair:** F27.

F18 was checked in my first intake. No fault was visible at the level of the statements; none of these is checked here.

## 2. What is new, and what it changes

**Against the literature.**
- **PH1.** The run itself establishes that VI's homogeneous Ehrhart PH1 is already refuted in print: Kahle–Michałek, EJC
  25(1) (2018) P1.41, Theorem 5 and Remark 6, p. 4 (the ray λ = (4), μ = (3), π = (7, 5); the run read the full paper).
  F34's compact-dimension and #P points are separate, and as far as the run and I can see they are new as written. A
  literature search on binary-encoded plethysm complexity is needed (Fischer–Ikenmeyer 2020, from memory, is the first
  place to look).
- **F24 and F32** extend F03. The tensor-power method itself is Deligne's (Weil I).
- **F26 and F42** are new and elementary.

**Against the other runs.**
- **HODGE_SIGN final (prompt 32; Hexagon candidate H01)** has the unconditional sign-only proof of Deligne's purity. F03 and
  F24 are the abstract criterion behind it. F24's real-coefficient condition and its counterexample (t = i, k ≡ 2 mod 4)
  are a useful lemma for H01's write-up: they show why the H01 route must keep integer Euler multiplicities.
- **ALPOGE_GCT, and Hexagon H02:** H02's claim that "the homogeneous Ehrhart form of PH1 fails" is Kahle–Michałek's Theorem 5.
  H02 must credit it. Whether KM already note the failure of VI Theorem 1.6.1(d) (the D₅ point) is still open; the run did
  not address it.

**My INT-NSRH-1 and INT-NSRH-2 from the first intake** are still not in the run.
- The sign identity: θ⊗θ fixes Ȟ_r, so the C′⊗C′ coordinates are (−1)^{l(x)+l(y)} times the C⊗C coordinates.
- The C⊗C-positive word basis of Ȟ₃.

Q3-AMBIENT still reads "REFUTED_FOR_FIXED_INCLUSION" with the C′ cone, and F43 builds a positive basis for the module, not
for the algebra in the dual cone. The successor should receive both points; see section 5.

**Cote 16.** The run now states its convention: a stamped archive scan s is PDF page s + 1. Our `ARCHIVE_16_scanNNN` files
follow the PDF page. So the run's "corrections" of our locators are a convention offset, and our locators stand. (My
first intake said this too.)

## 3. Scope of the two proofs

No new finding uses RH or GRH, from Alpöge or Masullo, as an input. Nothing claims more than its input gives.

## 4. Hexagon readiness (the five tests of `field_experts\HEXAGON_CANDIDATES.md`)

| Result | Complete | Self-contained | Stable | Checked | Interest | Verdict |
|---|---|---|---|---|---|---|
| F34 (VI Hyp. 1.6.4(2) false in compact binary; binary plethysm not #P) | yes | yes (classical count) | probably: no successor targets it | intake check only; an independent re-proof is needed | moderate (GCT) | **Candidate; gates left:** the literature search (Fischer–Ikenmeyer; KM) and one independent check. Best posted together with H02 as one GCT VI errata note, after the note to Mulmuley that H02 already plans. |
| F24 with its two counterexamples | yes | yes | no: H01 subsumes it | intake check | as part of H01 | Not separate: **fold into the H01 write-up** as its abstract lemma |
| F26 and F42 | yes | yes | yes | intake check | low alone | Not separate: a section of a later "nonstandard RH: what cannot work" note |
| The F19–F44 rank-three geometry | not checked here | — | no: the run is active | — | — | not ready |

Nothing here is timely enough to flag on its own. The timely item is still H01.

## 5. Integration and prompt updates

**QUESTIONS rows.**
- Q3-GCT: add the F42 conclusion: "no fixed finite Weil object; the target must be word-dependent or completed".
- Q1-PH: credit KM Theorem 5, as the run already does.

**Hexagon file.**
- H02: add "homogeneous PH1 failure: Kahle–Michałek EJC 25(1) P1.41, Thm 5, Rem. 6, p. 4 (prior)".
- Add F34 as a new row, sharing H02's gate.
- H01: note F24's real-coefficient counterexample as a lemma to include.

**Successor of GCT_NSRH.**
1. Give it INT-NSRH-1 and INT-NSRH-2, and ask it to restate Q3-AMBIENT accordingly. Then ask:
   - Ȟ₄ in the C⊗C cone, by exact computation;
   - the Koszul-dual heart as gate E.
2. Take F42 as the stated limit. Ask for the minimal completed object: is the F35 stack, or a word-graded family, compatible
   with the path-output sign of F24?
3. The archive convention is settled; no edit is needed.

**Prompt 32 (HODGE_SIGN) successor and H01:** cite F24 for the signed form, together with its two counterexamples.
