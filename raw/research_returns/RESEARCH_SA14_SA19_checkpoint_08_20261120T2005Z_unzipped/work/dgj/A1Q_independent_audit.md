# Independent audit of A1Q

**Status: PASS for the stated target hypotheses.**

Audited `work/root/A1_known_targets.tex` and the previously written formal-neighborhood vanishing criterion A4c in `sections/A.tex`. Independently opened these primary PDFs:

- Alexander Petrov, *Decomposition of de Rham complex for quasi-F-split varieties*, arXiv:2502.13356v1 (19 February 2025), https://arxiv.org/pdf/2502.13356 . Definition/Theorem 1.1, printed p. 1; Corollary 4.10(2), printed p. 16; the splitting convention is explained again in Corollary 4.6, p. 15.
- Tatsuro Kawakami and Hiromu Tanaka, *Liftability and vanishing theorems for Fano threefolds in positive characteristic I*, arXiv:2503.10236v3 (25 August 2026), https://arxiv.org/pdf/2503.10236 . Theorem 6.3, printed p. 50.
- Same authors, Part II, arXiv:2404.04764v2 (9 May 2025), https://arxiv.org/pdf/2404.04764 . Theorem 7.2 and its proof, printed p. 56.

For a target of dimension d, Petrov gives H^(d-i)(omega_Y tensor A^m)=0 whenever 0<i<d, since the sum of differential-form and cohomological degrees is d+(d-i)>d. Serre duality then gives H^i(A^-m)=0 for every m>0. Thus the exact required first group vanishes for d>=2, and the first and second groups vanish for d>=3. This is independent of p and requires no ambient lifting.

Part II Theorem 7.2 states the full Akizuki–Nakano assertion for every smooth Fano threefold in every positive characteristic. Its proof splits into rho>1 or index>1 (quasi-F-split), rank-one index-one with non-very-ample anticanonical class (Lemma 6.28), and the remaining very-ample case (Part I Theorem 6.3). The root cites both papers and preserves those scopes. Differential degree zero with cohomological degree 1 or 2 is exactly the required negative-line-bundle vanishing.

The final warning that this is a target hypothesis, not a theorem for arbitrary targets, is necessary and present. No gap found in the deduction. This audit checks the application and exact primary theorem statements, not a complete re-proof of all of Petrov or Kawakami–Tanaka.

AI reviewer: GPT-6 Astra (OpenAI), inherited reasoning setting, separate dgj run, 20 November 2026.
