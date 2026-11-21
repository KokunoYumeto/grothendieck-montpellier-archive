# Independent review of the fixed-prime infinite family

Date: 2026-11-21 UTC. Reviewer: `/root/lean_chain`, GPT-6 Astra Pro; effort not exposed.

## Verdict and exact scope

**PASS for KT-TWOFIELD-FAMILY**, under the same carried class-group/K-group comparison and modular-form inputs as its seed. I read all of `two_field_eisenstein_obstruction.tex`, `two_field_global_obstruction.tex`, and `two_field_infinite_family.tex`, and both complete small certificate scripts. The new conclusion is an unbounded family of weights at the fixed prime 661. It constructs non-CM classical residual systems in both ambient field spectra; it does not assert that these systems arise from actual points of the deformation problem or imply nonzero Selmer groups.

For every t>=0, e=268+330t and w=537+660t. Both level-3 and level-7 primitive quadratic-character cusp spaces contain a non-CM eigenform whose normalized rank-three residual system is the Eisenstein triple at every Galois element. At the same time K_(536+660t)(Z){661}=0. Only t=0 satisfies 661>2e+2. Consequently this proves neither infinitely many distinct common primes in that large-prime range nor failure of the proposed reflected exclusion TF.9.

## Primary source check: the weight propagation

I read Zhi-Hong Sun, *Congruences concerning Bernoulli numbers and Bernoulli polynomials*, Discrete Applied Mathematics 105 (2000), Lemma 8.1(a), printed pp.219–220, including its entire proof. The PDF images confirm the hypothesis **p−1 does not divide b**. With n=1 it equates successive Euler-corrected normalized generalized Bernoulli values at indices b and b+p−1 modulo p. Here p does not divide D, and every b=w_t is congruent to 537 modulo 660. Both Euler factors are units congruent to one because b>1. Induction from the certified seed therefore proves the claimed positive valuation. Even when 661 divides w_t, this argument divides rational numbers before taking congruences; it never inverts that residue class in F_661. The proof of the imported lemma uses its earlier p-regular-function results, which I have not separately reproved.

Primary PDF: <https://maths.hytc.edu.cn/__local/6/FC/FC/1ABF8BB04EF342FE2E847D09D24_C25CB165_314DA.pdf>. Statement and complete part-(a) proof were checked in PDF pages 26–27 (printed 219–220), not inferred from the later theorem's imperfect text layer.

I also read Fretwell–Roberts, *Newform Eisenstein congruences of local origin*, Theorem 3.6 and its complete printed proof. Its sufficient condition requires k>2, a coefficient prime away from 6NM, and positive valuation of its displayed L-value/Euler-factor product. It has no condition ell>k+1. Substituting N=D, M=1, psi=1 and phi=chi_D makes the Euler-factor product empty. Both conductors are prime and the nebentypus has full conductor, so the eigenform produced in this case is new. The paper's different necessary-condition Theorem 3.5 is not being substituted for Theorem 3.6.

Primary article: <https://link.springer.com/article/10.1007/s11139-024-00838-1>, printed pp.517–518, Theorem 3.6. The residual semisimplification follows from the good-prime congruences and the attached two-dimensional Galois representation, then restriction to E_D and twisting; no small-weight local condition enters this inference.

## Non-CM and rational vanishing checks

The carried CM classification at full level 3 requires e congruent to zero modulo 3. Here every e is congruent to one. At level 7, a CM form has zero third Hecke eigenvalue, since 3 is inert. The congruence instead gives 1−3^(536+660t)=50 modulo 661. Thus deleting CM systems does not remove the displayed obstruction.

The two possible e-residues modulo 660 are 268 and 598. The carried K17-REFLECTOR applies to both: they are even, between 2 and 658, and their reflected Bernoulli indices are 392 and 62. The freshly checked residues are respectively 53 and 511 modulo 661. I read the entire carried REFLECTOR proof (input K17.tex lines 4533–4619), and the carried all-positive-k comparison (K2) at lines 696–705. The conclusion uses periodicity of the class-group character index, not an identification of K-groups in different degrees. Hence the claimed primary vanishing is valid for every t.

## Exact computational events

Both original scripts were read in full. Byte-identical copies were executed in this review directory so that the author's reports were not overwritten:

- `bernoulli_661_replay.py`: trial-division primality of 661; ordinary Bernoulli recurrence; both generalized Bernoulli seed residues zero by the Bernoulli-polynomial formula and an independent finite character power sum modulo 661 squared; reflected B392 residue 53. **PASS**. The complete output is `bernoulli_661_replay.json` and `.log`.
- `infinite_family_661_replay.py`: ordinary B62 residue 511, inert-prime residue 50, and the two alternating e-residues. **PASS**. The complete output is `infinite_family_661_replay.log`.

These are finite arithmetic replays, not computations of all family members. The infinite statement comes from the fully checked induction above. No new Lean kernel check, general coefficient-independence assertion, or actual-admissibility claim is made.
