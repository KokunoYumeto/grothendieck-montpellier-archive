# Check of GCT_POS's refutation of numerical PH3 for Kronecker coefficients

Main session e0d20ada (Claude Opus 5.5 at effort max), 22 Nov 2026, 08:3x UTC.
The run is GPT-6 Astra (ChatGPT Pro mode): `GCT_POS_final_20261122T0219Z_unzipped`, results K023, R-NEW004, K024, PNEW013.

## The statement checked

Let k_n(s) = g((s^n),(s^n),(s^n)). For every n ≥ 2 the series Σ_s k_n(s) t^s has a pole at the primitive roots of order
2^(n-1)·3^r for some r ≥ 0. So every form P(t)/∏(1 − t^(a_i)) has some a_i ≥ 2^(n-1), while GCT VI asks for a positive
form with max a_i polynomial in rank(x) = n² + 5n. The existence clause of PH3 fails for Kronecker coefficients.

**Result: no gap found.** This is a targeted proof check with computations by the same checker. It is not an independent
re-proof, not a formal certificate, and not a literature search.

## The argument, as checked

1. **K023.** The trace of the cyclic permutation of the three factors on the degree-s invariants is
   b_n(s) = dim of the SL_n-invariants of weighted degree ns on W ⊕ S_(2,1)W (weights 1 and 3). An order-three operator on
   a rational space has trace congruent to its dimension, so k_n(s) ≡ b_n(s) mod 3.
2. **R-NEW004 and K024.** The vector z_n has zero Lie stabilizer, so a finite stabilizer, which is cyclic of order
   M = 2^(n-1) with det faithful. By P-F30 it gives the only nonzero μ_M-fixed orbit of the quotient. By P-F23 the series
   of b_n has a simple pole at the primitive M-th roots, with residue a unit at 3, and none at order M·3^r, r ≥ 1.
3. **PNEW013.** Modulo 3 the two series are one rational function, so the Kronecker series has a pole at some order M·3^r.

Read in full, statement and proof: the four files in FILES_READ.sha256; in ALPOGE_GCT checkpoint 09, P-F23, P-F27, P-F30.
Standard theorems used there were taken as known (Schur-Weyl, Kempf-Ness, Luna, Cramer, Hadamard). P-F26 and P-F19 are
cited inside P-F27's closing remarks and are not needed for the steps above; they were not reread.

## Computations (check_ph3.py, output result.txt; code written from the statements)

| Step | Test | Result |
|---|---|---|
| K023 | trace = b_n(s) and k_n(s) ≡ b_n(s) mod 3, by two unrelated methods, 37 pairs (n, s) with n ≤ 7 | no failure |
| R-NEW004 | rank n² of the stabilizer system on associative words, n = 2..14 (mod 1000003, which implies full rank over Q) | no failure |
| P-F30 as used in K024 | every set of at most n hook weights, n ≤ 6 (36,684,858 sets at n = 6): maximum two-part 2^(n-1); exactly n! maximizers, all chains; the chain element fixes exactly n weights | no failure |
| K024, the residue | equals that of the exact series at n = 2, 3 | agrees |
| The congruence at the pole | the residue formula modulo 3 against the run's separately computed tensor residues at n = 4, 5 | agrees, at the same root |

The all-n statement rests on the proofs. The computations test them in small rank.

## GCT VI, read in the source of the revised version

- **Cite Hypothesis 3.3.4.** It is the form of PH3 that names the Kronecker problem (through 3.3.1, item 1 = Problem
  1.1.1). PNEW013 cites 1.6.7, which is stated for plethysm constants, with Kronecker only as a special case of the
  generalized problem. The run's parameter is the one of section 3.4: ranks of H = GL_n × GL_n and G = GL_(n²), plus the
  heights, so 2n + n² + 3n = n² + 5n.
- **Definition of a positive form (1.6 and 3.3 use the same one):** positive integers a_i, nonnegative integer numerator,
  constant term 1. The lower bound uses only the denominator.
- **Version:** v4 (22 Jan 2009) is the newest on arXiv, seen 22 Nov 2026. It already carries the corrected SH.

## What stays open

- the exact value r = 0 for n ≥ 6 (n = 2, 3, 4, 5 have it);
- PH2 and SH(a) for Kronecker coefficients (positivity and saturation indices);
- novelty: nothing was searched, Hexagon included.

## Added 22 Nov 2026 08:57 UTC

- Hypothesis 3.3.4 was already refuted in two other settings of ours: subgroup restriction from a torus (P-F14, a rank-one
  torus in GL_2) and plethysm (P-F31). What is added here is the Kronecker case.
- The final's intake: field_experts/intake_20261121/intakes/GCT_POS/INTAKE_GCT_POS_20261122_final.md. Its scripts
  k008_complete.py and check_final.py were read and rerun by the main session with the same output
  (final_intake_scripts/). That is a rerun of the agent's code, not a separate check.
