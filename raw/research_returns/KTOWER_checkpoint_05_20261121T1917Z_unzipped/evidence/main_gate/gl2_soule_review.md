# Independent root-file review

Reviewer: `/root/geometry_tower`, GPT-6 Astra Pro, effort not exposed. Run KTOWER, 2026-11-21 UTC.

## GL2 dimension and algorithm

Read the entire `evidence/gl2_uniform_section.tex` and `evidence/gl2_uniform.py`.

**KT-GL2-CM passed.** The primitive conductor-three nebentypus prevents oldforms. The CM conductor formula forces the quadratic field Q(√−3) and conductor one. Class number one reduces existence to unit invariance of α^(2e), which is exactly 3|e; it also gives uniqueness. Conjugating the infinity type reindexes the theta series, rather than producing a second form. At inert primes there is no norm-p ideal. The complete argument has no hidden rational-coefficient restriction: Schütt, arXiv:math/0511228v5, Theorems 1.1 and 1.4, pp. 2–3, are stated for general CM newforms/Hecke characters. These source statements were retrieved directly from the paper text. The original Ribet proof of the classification was not re-proved.

**GL.4–GL.5 and the implementation passed.** The eta quotients both have initial q exponent one, matching the shift in `eta_coefficients`. The theta series uses 6 times the χ-divisor sum. Each leading-coefficient matrix is lower unitriangular, the column solve computes L-inverse B, and all Fourier accesses stay within the declared precision. The degree exponent p^(2e) is the weight-minus-one Hecke exponent. Polynomial orientation in the FLINT characteristic polynomial and Horner evaluation is correct. The direct determinant checks the same exact integer evaluation. The empty e=2 space is handled consistently.

Every one of the 15 degrees e=2,4,…,30 was independently replayed; after removing elapsed time, each output agrees exactly with the root JSON. `gl2_replay_review.json` records this check. This repeats the implementation execution, not a second independent implementation. The root's new eta recurrence differs from the carried predecessor implementation; the complete modular basis is carried from K17 as requested.

The only code scope note is that CLI `--primes` is not validated for primality or exclusion of 3. The documented defaults 7 and 13 satisfy all hypotheses. This is not a flaw in any recorded run.

## Soulé transcription

Read all of `evidence/soule_comparison.tex` against the original supplied `input/LIT_Soule_2003.pdf`, using extracted text and visual inspection of pp. 779–780. The definitions of card_b, w-tilde, h, k, a and c agree with pp. 777–778. Theorem 2 and Theorem 3 are accurately transcribed from p. 779. The coefficients 220, 210, 1120 and 510 are ordinary integers, verified visually. The general estimates use m≥2; the Q estimate is m≥9, with the separate m=7,8 bounds 40545 and 70130. The m=4k, k≥3 substitution and the comparison of logarithmic growth are valid.

**Material source-proof defect:** Lemma 9's general-field prime cutoff is false, because the proof ignores proper cyclotomic intersections. The explicit Q(√5), N=2, p=5 matrix and a safe rN+1 replacement are proved in `soule_stabilizer_correction.tex`; symbolic data are in `soule_lemma9_counterexample.json`. This does not refute the numerical Theorem 2, and does not impair its Q-specialization. The full source paper was not re-proved.

The root file's use of VK-EXP7, KT-C7-EXPLICIT and KT-QUARTIC-BOUND was reviewed only as a comparison of stated bounds. Those other proofs were not independently read in this subtask.

