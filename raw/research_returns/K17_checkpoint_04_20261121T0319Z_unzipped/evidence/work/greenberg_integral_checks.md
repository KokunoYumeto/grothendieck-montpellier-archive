# Greenberg integral corollary: complete check record

Agent: /root/tripod_integral. Model: GPT-6 Astra Pro. Reasoning effort not exposed.
Date: 2026-11-21 UTC. Status: complete self-reading, reconstruction and
archive independent whole-proof review passed.

## Exact scope

The new fragment `greenberg_integral_corollary.tex` assumes the one-variable
CM Greenberg hypothesis that the norm-limit plus class-group module is finite.
It uses the already independently checked conditional kernel theorem
K17-GREENBERG-KERNEL and repeats the complete filtration argument from
K17-INTEGRAL-CLASSIFICATION. It removes Vandiver only from the hypothesis of
this conditional consequence, not from any theorem about normalized Soulé
characters.

The positive assertion at regular odd primes is the existing Sharifi/Brown
consequence. At an irregular odd prime satisfying the stated hypothesis,
the conclusion is nonzero finite p-torsion Lie indecomposables in infinitely
many even weights. No first defect weight or order is asserted.

## Fresh primary arithmetic check

Kenneth A. Ribet, *A modular construction of unramified p-extensions of
Q(mu_p)*, Inventiones Mathematicae 34 (1976), 151–162.
Author-hosted primary scan:
https://math.berkeley.edu/~ribet/Articles/invent_34.pdf
DOI: https://doi.org/10.1007/BF01403065 .

Fresh search retrieved the original introduction and Main Theorem (1.1),
printed p.151; the author-hosted scan was opened and its first two text
pages were rendered. Retrieval refs: `turn474049702search10`,
`turn474049702search0`, `turn301255340view0`,
`turn989449941view0`, `turn989449941view1`.

The introduction states Kummer's criterion for irregularity. Main Theorem
(1.1) states that for even 2≤k≤p−3, divisibility of B_k by p is equivalent
to nonvanishing of C(chi^(1−k)), where C is the class group modulo p-th
powers. In additive p-primary notation this is (A_0/pA_0)^(chi^(1−k)).
The character is odd, so this quotient is in the minus eigenspace.
The projector (1−c)/2 is integral and exact for odd p; consequently
A_0^- is nonzero. Conversely A_0^-≠0 implies p divides the full class
number. This proves the needed exact equivalence between irregularity
and nonvanishing of A_0^-, without Vandiver.

Only the theorem and its exact hypotheses and notation were freshly
verified; this check does not claim to re-prove Ribet's modular argument.
The underlying Sharifi notes references are the already fully read
Proposition 3.4.1 (minus injection), Proposition 3.4.7 (actual Kummer
duality), and Corollary 3.4.8 (Iwasawa comparison), at
https://www.math.ucla.edu/~sharifi/iwasawa.pdf .

## Full proof reconstruction

1. The conditional kernel theorem makes the actual weight filtration on
   the entire arithmetic group H separated. The checked outer saturation
   proposition identifies its grading with the actual integral one.
2. Iwasawa/Ferrero–Washington make H free pro-p and M=H/closed[H,H]
   torsion free. Kummer comparison and mu=0 make M^+ finite over Z_p.
   The nonzero A_0^- injects into the direct-limit minus class group;
   actual Pontryagin duality then makes M^+ nonzero, hence finite free
   of positive rank. A pseudo-isomorphism alone is not used to deduce
   nonvanishing.
3. Each image M^n of F^nH is compact and closed. Separatedness of this
   quotient filtration follows from nested compact fibres, not from a
   general false assertion that arbitrary quotient filtrations are
   separated.
4. Degreewise Lie abelianization surjects onto M^n/M^(n+1). Complex
   conjugation has sign (−1)^n there. Exact plus projection therefore
   makes every odd quotient in the filtration of M^+ vanish.
5. Outer Johnson embeddings make every graded Lie piece finite free.
   Degreewise brackets form a finite sum of finite generated submodules,
   so their quotient is finitely generated and localization commutes
   with it. Brown's rational odd freeness makes each even Lie
   indecomposable piece finite p-torsion.
6. If only finitely many even quotients of M^+ were nonzero, its
   separated filtration would terminate and would make M^+ finite.
   This contradicts positive free rank. Their surjecting even Lie
   indecomposable pieces are therefore nonzero in infinitely many
   weights. Odd homogeneous generators cannot produce such
   indecomposables.

The entire final TeX and bibliography were read back. A harmless LaTeX
exponent-spacing transcription was repaired to `chi^{1-k}` on readback;
no mathematical change was needed.

## Independent review received and read

The complete review in `work/greenberg_integral_archive_audit.md` was read.
It independently checks the exact Ribet primary theorem and every step
of the conditional filtration argument, with verdict PASS. The reviewed
mathematical TeX hash was b550f6592e44a1f802bd5720a4f29ffff6cd01c2ac316060c8a299fd1c0aaa63.
Only this status comment was subsequently updated; no mathematical text
changed. The parent was notified for integration.
