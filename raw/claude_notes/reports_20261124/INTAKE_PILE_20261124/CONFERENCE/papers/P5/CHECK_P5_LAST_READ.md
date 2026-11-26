# Last read of paper 5: "The positivity hypotheses of GCT VI fail for Kronecker and plethysm coefficients"

By the conference convener ae84c4aa572daf430 (Claude Fable 5.2 at effort max), 25 November 2026, for the main session
329fb1e6 (Claude Opus 5.5 at effort max). Brief: `agent_notes/ae84c4aa_P5_LAST_READ_BRIEF_20261125.md`.
The paper: `src/P5_paper.tex` of 25 Nov 2026, 08:54 (1802 lines; `P5_paper.pdf`, 25 pages), written by a0805369bae2ebddc
(Claude Opus 5.5 at effort high). I did not edit it.

**Result.** I found no error in a theorem, proposition, lemma or proof. Every proof printed in the paper was followed
step by step, except the coefficient computation of Lemma 5.2, which I read and tested by an exact computation for
n = 2..7. Sections 6, 7 and 8 and the steps the writer added were redone by hand in full and tested by computations
of my own. Eight repairs are needed in the text. Three of them correct something false as printed:
a broken cross-reference (R1), a misquoted formula of Briand, Orellana and Rosas (R2), and a remark at the end of
Section 8 that says the opposite of what the examples show (R3). The others are precision of a statement (R4), of
wording (R5, R6), of the literature sentences (R7) and of the title (R8). Exact replacement text is in section 3.

This is a targeted proof check of the printed proofs with computations by the same checker. It is not an independent
re-proof and not a formal certificate.

**What I read.** The whole source, every line; the PDF at pages 3 and 19 and the PDF text at page 4; `ABSTRACT.md`,
`PROVENANCE.md`, `CHECK_EVENTS.tsv`, `checks/p5_checks_output.txt`; the check of 22 Nov by e0d20ada (Claude Opus 5.5 at
effort max), `reports_20261122/gct_pos_ph3_check/CHECK.md`; and, in the writer's saved copies (shared scratchpad,
`p5/`): GCT VI v4 at Definitions 1.2.2, 1.2.4, 1.2.7, Theorem 1.6.1, Hypotheses 1.6.5 to 1.6.7 and 3.3.1 to 3.3.4,
Problem 1.1.3 and all of Section 3.4 (3.4.1 to 3.4.3), with page 52 also as an image; Briand-Orellana-Rosas at
Theorem 2.4, Sections 2.4 and 2.5 and Mulmuley's appendix; Losev, page 1; Luna at the slice theorem. I did not read
the runs' own files.

## 1. Verdict per statement

"Followed" means: every step of the printed proof was checked by me. "Redone" means: I re-derived every count,
identity and constant on paper. Computations are in `checks/last_read_*.py`, with their outputs beside them.

| Statement | Verdict | What I did |
|---|---|---|
| Section 2, Definitions 2.1, 2.2 and the hypotheses | As printed in GCT VI and in the appendix, with one difference to state (R6) | compared with the source texts |
| Lemma 3.1 (isolated fixed point) | holds | followed |
| Prop. 3.2 (fixed component gives a pole) | holds | followed |
| Lemma 3.3 (e_Y = 1) | holds | redone |
| Lemma 3.4 (two-power lifts) | holds | followed |
| Lemma 3.5, Thm 3.6 (transfer), Remark 3.7 | hold | followed; both examples of the remark redone |
| Lemma 4.1, Prop. 4.2, Thm 4.3 (cubic support) | hold | followed, including the small-sum table, the minor factorization (11), Hadamard and the case q = c, f = 0 |
| Thm 5.1 (trace identity) | holds | followed |
| Lemma 5.2 (zero Lie stabilizer) | holds for n = 2..7 by my exact computation; the proof for all n was read, not recomputed | computation |
| Thm 5.3 (hook-chain pole) | holds | followed; Kempf-Ness data, the fixed-weight count and the single pair {η, −η} redone |
| Thm 5.4 = Theorem A, Cor. 5.5 | hold | followed; hypotheses of Thm 3.6 matched one by one |
| Prop. 6.1 (1) smooth, closed orbit | holds | redone |
| Prop. 6.1 (2) stabilizer | proof holds; the statement needs a condition (R4) | redone, every case of the Hessian locus; locus computed for n = 4, 5 |
| Prop. 6.1 (3) grading stabilizer μ_M, all n | holds | redone; computed for n = 2..59 |
| Prop. 6.1 (4) | holds | redone |
| Thm 6.2 = Theorem B, Cor. 6.3 | hold | followed |
| Section 7.1, Fourier normalization | holds | redone; tested exactly at n = 4 |
| Prop. 7.1 (wave identity) | holds | redone; tested exactly at n = 4, all 120 residues |
| Prop. 7.2 (product formula) | holds | redone; character identity computed for n = 4..10; value at n = 4 against Salmon's series |
| Prop. 7.3, inequality (24) and the window | hold | redone; (24) computed for n = 4..14 |
| Cor. 7.4 | holds | redone |
| Prop. 7.5 (recursion, sibling ratio) | holds | redone; recursion computed for every odd a, n = 5..11 |
| Lemma 7.6, the cube-root formula (29), the sine estimate | hold | redone |
| Prop. 7.7 (near increments) | holds | redone, every constant |
| Prop. 7.8 (far increments) | holds | redone, every constant |
| Thm 7.9 = Theorem C, Cor. 7.10 | hold | redone, every threshold |
| Prop. 8.1, Prop. 8.2 = Theorem D | hold | redone; computed from the definitions |
| Remark closing Section 8 (bit length) | false as printed (R3) | compared with GCT VI, Section 3.4.2 |
| Section 9, paragraph on Briand-Orellana-Rosas | one formula misquoted (R2) | compared with the source text |
| Section 9, "What we searched"; Introduction, "Earlier work" | wording wider than the search (R7) | compared with PROVENANCE.md |
| Section 10 (who proved and checked what) | agrees with the records | compared with PROVENANCE.md and CHECK_EVENTS.tsv |

The proofs of the two runs (GPT-6 Astra (ChatGPT Pro mode)) that were checked before are K023, R-NEW004, K024,
PNEW013, P-F23, P-F27 and P-F30, by e0d20ada (Claude Opus 5.5 at effort max) on 22 Nov, and P-F19, P-F31 and P-F57, by
a0805369 (Claude Opus 5.5 at effort high) on 21 Nov. The paper states them with the hypotheses under which it uses
them, and each use was matched. I compared the paper with CHECK.md of 22 Nov, not with the runs' files.

## 2. The eight things only the writer had read

**1. Kempf-Ness for the chain cubic (Prop. 6.1(1)).** Holds. With r_i = (1 − (−1/2)^i)/3 for i < n and
r_n = (1 − r_{n−1})/3, all r_i are positive and Σ r_i a_i = (1, …, 1): the coordinates give 2r_1 = 1,
r_{i−1} + 2r_i = 1 and r_{n−1} + 3r_n = 1. Distinct monomials have distinct weights under the diagonal torus of SU_n,
so they are orthogonal. The differences a_i − a_j are 2e_i − e_{i+1} − e_{i+2}, 2e_{n−1} − 2e_n, or carry an entry
±2 or −3; none is a root, so the off-diagonal part of the moment map vanishes. The diagonal part is the image of
Σ r_i a_i modulo (1, …, 1), which is zero. The a_i are independent (determinant 3·2^{n−1}), so a diagonal matrix
carries the zero of the moment map to F_n, and a diagonal matrix normalizes SL_n. Losev's Theorem 4, page 1, is the
Kempf-Ness criterion as used. The same data for z_n in Thm 5.3 (with a_n = e_n, q_n = 1 − q_{n−1}, squared norm 6 of
the Lie words) also hold. Computed for n = 2..39.

**2. The grading stabilizer is exactly μ_M for all n, so e_Y = 1 also when 3 | n (Lemma 3.3, Prop. 6.1(3)).** Holds.
A grading element fixes p_n exactly when it is (det b)^{−γ} for some b in the stabilizer of F_n: this uses that
the orbit of F_n is closed and that a fibre holds one closed orbit. The image is generated by a_1^{−γS} with a_1 of
order 3M; S is odd and S ≡ n mod 3, so gcd(3M, γS) = 3 in both cases ν = 1 and ν = 3, and the order is M. Lemma 3.3
then gives e_Y = 1: the degrees at which some function is nonzero at p form a semigroup with greatest common divisor
M, so it holds all large multiples of M. Computed for n = 2..59. An outside test with 3 | n:
for n = 3 (not in the paper's range) the series is 1/((1 − t⁴)(1 − t⁶)), its residue in the paper's normalization at
t = i is 1/2, and the mechanism of the paper gives 1/(1 − (−1)) = 1/2 with e_Y = 1.

**3. The counts of fixed weights.** Hold. In Thm 5.3: e_i is fixed only for i = n; 2e_i + e_j only for j = i + 1
(n − 1 weights, each of multiplicity one); e_i + e_j + e_k never; total n, and dim sl_n^g = n − 1, so the fixed
tangent space has dimension one. In Prop. 6.1(4): the fixed cubic monomials are exactly the n chain monomials (the
least valuation among the nonzero terms must occur twice). Computed for n = 2..15.

**4. Inequality (24) through the product formula (Prop. 7.3).** Holds. Z_n = M^{−1} Π (1 − θ^b)^{−1} with θ³ = ζ; a
triple i < j < k ≤ n − 2 has weight w divisible by 3 with |w| < 2^{k+1}, so |1 − θ^w| = |1 − ζ^{w/3}| ≤ 8·2^k/M. The sum
of n − 1 − k over these triples is C(n,4); at most n − 2 of them lie in E_n; there are at most C(n−1,3) of them, each
losing 3; the other factors lose at most 1 each and M^{−1} loses n − 1. That is the first line of (24). The second
line follows with a total cubic loss of (7/6)n³ ≤ 2n³. Computed: the exact log₂|Z_n| is above the first line for
n = 4..14, and the first line is above n⁴/24 − 2n³ for 4 ≤ n < 200. The second half of Prop. 7.3 (some x in
[X, X + 8]) holds for n ≥ 6 as stated: 2π/M ≤ 1/4 needs M ≥ 32.

**5. The Fourier normalization (Section 7.1).** Holds. The product of 1 − ρ/ρ′ over the other M-th roots ρ′ is M,
so H_n(t) = (C_n(ρ)/M)/(1 − t/ρ) + O(1) and P_ρ = A_n(ρ). Tested with Prop. 7.1 and Prop. 7.2 together at n = 4: with
A = C/M from the product formula, q_r(X) − q_{r+60}(X) = 2W_4(r) holds for all 120 residues, the constituents being
taken by exact interpolation from Salmon's series (1 + t²⁵)/((1 − t²)(1 − t⁴)(1 − t⁶)(1 − t⁸)(1 − t¹⁰)).

**6. The two torus propositions (Theorem D).** Hold. Prop. 8.1: the weight of y_1^a y_2^{n−a} is n + Na. Prop. 8.2:
the weight is n + 2b + Nc; g_N(2Nq + r) = q + 1 for even r and q + 1_{r ≥ N} for odd r; the constant terms and the
values at X = 1 give p = s = N − 2. Computed from the definitions for N ≤ 12 and for odd N ≤ 19. Against GCT VI:
tori are allowed in Problem 1.1.3 and in Section 3.4; a sum of polynomial characters is an explicit polynomial
representation (3.4.1); "rank(x) is defined to the sum of the ranks of H and G and ‖λ‖ and ‖π‖", the combinatorial
bit lengths, with no term for ρ (Section 3.4, p. 52; read on the page image, since the text extraction drops the
symbols). So the hypotheses fail "as stated". The remark after Prop. 8.2 is wrong (R3).

**7. The use of P-F24 (Prop. 6.1(2)).** The proof holds. Half the Hessian is tridiagonal with diagonal
(x_2, …, x_n, 3x_n) and off-diagonal entries x_1, …, x_{n−1}. I redid every case of the rank ≤ 2 locus (two nonzero
off-diagonal entries: j ≥ i + 2; j = i + 1 with i ≥ 2; i = 1, where the 3×3 block has determinant −x_2³ − x_1²x_4, so
n = 4 needs the extra singleton; one nonzero entry: j = 1, 2 ≤ j ≤ n − 2, j = n − 1; none). The locus is [e_1], [e_n]
and [±√3 e_{n−1} + e_n]. The induction to the ternary cubic and the three coefficient comparisons there (y, y², zw²)
are right. Computed exactly by Gröbner bases for n = 4 and 5. The statement needs R4.

**8. The constants of the index section.** All hold.
- Prop. 7.5: count of T_n is C(n−1,2); log₂δ_n ≤ 3B − C(n−2,3) + (n − 4) + (n − 2)² = −n³/6 + 4n² − 107n/6 + 19;
  this is ≤ −n³/12 for n ≥ 48 (already from smaller n on).
- Lemma 7.6: the margin is 1/3 − 1/48 = 5/16 ≥ 1/6.
- Prop. 7.7: low factors divisible by three contribute an error below n/24; high ones 12nR²; exceptional ones
  10nR²; in all 30nR² + nR ≤ 100nR². For the consequence, 2502/10⁵ < 1/12.
- Prop. 7.8: N_u ≤ C(r,2) + 3r + 3 (the "three" could be two); the other factors number 2n − 4; the first four terms
  sum to n³/6 + 3n² + 11n/6 − 3 ≤ n³/6 + 4n²; log₂J_n(b_n) ≥ n³/6 − 3n² + 71n/6 − 11; thresholds 16/δ and 2688/δ³.
- Thm 7.9: 48/δ³ = 4.8·10¹⁶ and 2688/δ³ = 2.7·10¹⁸ are below N = 10²⁰; Q_n ≤ 2^{n⁴}; n ≥ 2N⁴ = 2·10⁸⁰; the last
  inequality 3n⁴/80 + 2n³/5 < n⁴/24 − 2n³ − 1 holds from n = 577 on and is used for n ≥ 1024.

A by-product of my computation, for the main session to use or not: E_n/|Z_n| is 4.8, 24, 25 and 3.4 for
n = 4, 5, 6, 7, and then 0.094, 9.7·10⁻⁴, 1.2·10⁻⁶, 1.1·10⁻¹⁰, 4.6·10⁻¹⁶, 6.5·10⁻²³, 2.0·10⁻³¹ for n = 8, …, 14. So the
dominance that Theorem 7.9 proves from 2·10⁸⁰ on is there numerically from n = 8 (`checks/last_read_checks.out`).

## 3. Repairs, with the exact replacement text

**R1. Broken cross-reference (line 207; PDF page 4 prints "Section efsec:provenance").**
Replace
`Section~ef{sec:provenance} says who proved and checked what.`
by
`Section~\ref{sec:provenance} says who proved and checked what.`
No other command lost its backslash (the source was scanned for the traces such a loss leaves).

**R2. Misquoted formula (Section 9, lines 1711-1713).** The display (2.5) of Briand-Orellana-Rosas is
N/2 + {1 for even N, −1/2 for odd N}. Replace
`the stretched coefficient is $N/2+1$ for even $N$ and $-1/2$ for odd $N$ \cite[Theorem 2.4, p.~7]{BOR};`
by
`the stretched coefficient is $N/2+1$ for even $N$ and $(N-1)/2$ for odd $N$, so it vanishes at $N=1$ and is positive for every $N>1$ \cite[Theorem 2.4, p.~7]{BOR};`

**R3. False remark (end of Section 8, lines 1688-1693).** In GCT VI the specification of a torus character has
"the bitlength of the specification" (Section 3.4.2, the specification of ρ, item (4), printed page 56; I confirmed
the page in the PDF), so ρ_N has bit length O(log N), and the indices N − 2 and N are exponential in it. The remark
as printed says that a dependence on the bit length would make the examples harmless; it would not. Replace the
paragraph
`Neither example touches the density clause 3.3.2(b). They show that, for the general subgroup restriction problem, the polynomial bounds must also depend on the bit length of the embedding; with that dependence these two examples are harmless. The Kronecker and plethysm families of Sections~\ref{sec:kronecker}--\ref{sec:indices} have no such parameter: their embeddings are fixed by $n$.`
by
`Neither example touches the density clause 3.3.2(b). In both, the index is of the size of the exponent $N$ of the embedding, while the specification of a torus character has bit length $O(\log N)$ \cite[Section 3.4.2, p.~56]{GCT6}. So the bounds fail in $\rank(x)$ and also in the bit length of the input. For the general subgroup restriction problem a bound would have to depend on the exponents of $\rho$ themselves; with that dependence these two examples are harmless. The Kronecker and plethysm families of Sections~\ref{sec:kronecker}--\ref{sec:indices} have no such parameter: their embeddings are fixed by $n$.`

**R4. Prop. 6.1(2), a missing condition (lines 1035-1039).** A matrix diag(a_1, a_1^{−2}, …) with general a_1
multiplies x_n³ by a_1^{3(−2)^{n−1}} and the other chain monomials by 1, so it preserves F_n up to a scalar only when
a_1^{3M} = 1. Replace item (2) by
`\item Every linear transformation preserving $F_n$ up to a scalar is a scalar multiple of a diagonal matrix $\diag(a_1,a_1^{-2},a_1^4,\dots,a_1^{(-2)^{n-1}})$ with $a_1^{3M}=1$. These matrices form the stabilizer of $F_n$ in $GL_n$, a cyclic group of order $3M$; the stabilizer in $SL_n$ is the scalar group $\mu_\nu$, which acts trivially on cubic forms.`
and in the proof, before `A diagonal $\diag(a_1,\dots,a_n)$ preserves $F_n$ exactly when`, insert
`Dividing $T$ by a cube root of $c$, we may take $c=1$.`

**R5. "All three refutations of PH3" (Introduction, Method, line 180).** The refutation by the torus (Prop. 8.1) is a
direct count and uses no fixed locus. Replace
`All three refutations of PH3 detect a pole`
by
`The refutations of PH3 for Kronecker and for plethysm coefficients detect a pole`
and add at the end of that paragraph: `The torus examples of Theorem~D are elementary.`

**R6. Definition 2.2 against the printed definition (after line 234).** GCT VI, eq. (1.4), and Theorem 1.6.1(d),
eq. (1.6), print the numerator as h_d t^d + ⋯ + h_0, with the letter d of the degree of f. The paper allows any
degree e. Add after the definition:
`In \cite[eq.~(1.4)]{GCT6} the numerator is printed as $h_dt^d+\dots+h_0$, with the letter $d$ of the degree of $f$. We allow a numerator of any degree $e$; this only enlarges the class of positive forms.`

**R7. The literature sentences.** PROVENANCE.md records three web searches and seven Hexagon queries. It records no
search of arXiv as such, none of zbMATH or MathSciNet, and no pass through the papers that cite GCT VI. The printed
"We searched arXiv, the web and the Hexagon repository" and "we searched the web and arXiv" are wider than that, and
"no claim of priority beyond it" reads as a claim within it.
- Introduction, "Earlier work". Replace the first sentence by
  `On 25 November 2026 we ran web searches and searched the Hexagon repository for earlier statements that PH3, PH2 or SH fails in these forms; Section~\ref{sec:literature} lists the queries and what was not searched.`
  and the last sentence by
  `In these searches we found no earlier refutation of PH3, or of the relaxed SH(a) and PH2.`
- Section 9, "What we searched". Replace the paragraph by
  `On 25 November 2026 we ran three web searches: for counterexamples to Mulmuley's hypotheses PH2, PH3 and SH on the stretching quasi-polynomials of Kronecker and plethysm coefficients; for the poles and periods of stretched rectangular Kronecker coefficients; and for the work of Kahle and Micha\l{}ek on the quasi-polynomials of plethysm. They led to \cite{BOR} and \cite{KM}. We also searched the Hexagon repository (\url{https://hexagonmath.org}) for ``Mulmuley'', ``plethysm'', ``Kronecker'', ``geometric complexity'', ``positivity hypothesis'', ``saturation hypothesis'' and ``modular index''; these searches returned no work on the hypotheses (the matches for ``plethysm'' and ``Kronecker'' concern other questions). We did not search zbMATH or MathSciNet, and we did not go through the papers that cite \cite{GCT6} or \cite{BOR}. This is a bounded search, and we claim no priority.`

**R8. The title.** "The positivity hypotheses of GCT VI fail for Kronecker and plethysm coefficients" reads as PH2 and
PH3 failing for both families. Proved: PH3 for both; PH2 and SH(a) for plethysm; for Kronecker coefficients PH2 and
SH(a) are left open by the paper (it says so in Section 9), and PH1 is not touched. A title that claims no more:
`Counterexamples to the positivity and saturation hypotheses of GCT~VI`
The abstract is exact on which hypothesis fails for which family and needs no change for this. If the title
changes, `ABSTRACT.md` and the first line of `PROVENANCE.md` change with it.

**Smaller points, each optional.**
- Prop. 6.1(1), line 1056: `its diagonal part is proportional to $\sum_ir_ia_i-\one$, which is zero` is loose. Exact:
  `its diagonal part is the restriction of $\sum_ir_ia_i$ to the trace-free diagonal matrices, which is zero because $\sum_ir_ia_i=\one$`.
- The letter B is the number C(n−3,2) − 1 of bulk pairs in the proof of Prop. 7.5, the number (n−1)(n−4)/2 of
  weights divisible by three in the proof of Prop. 7.7, and the first number again as B′ in the proof of Prop. 7.8.
  Use `B_3` in the proof of Prop. 7.7 and `B` in that of Prop. 7.8.
- Proof of Thm 7.9, line 1588: `the two nonselected children of any parent other than $\pm b_{n-1}$` → `the two children of any parent other than $\pm b_{n-1}$`.
- Proof of Prop. 7.8, line 1531: "at most three of one class" is true; two is the exact number.
- Section 10: after this read, add
  `Claude Fable~5.2 at effort max then read the whole text, followed every proof, redid the added steps, the constants of Section~\ref{sec:indices} and Section~\ref{sec:torus} by hand, and tested them with computations of its own (25 November).`

## 4. The abstract and the introduction against what is proved

- Theorems A, B, C and D of the introduction are Theorem 5.4, Theorem 6.2, Theorem 7.9 and Propositions 8.1, 8.2,
  with the same hypotheses and the same constants (n ≥ 2; n ≥ 4; c < 1/4, n ≥ 2·10⁸⁰; ranks 5 and 6).
- The abstract claims nothing beyond them. "A signed trace of these poles dominates all other terms" stands for:
  2W_n(x) > f_n(x) at some x within 8 of 2^{cn}. "Larger than 2^{cn} for every c < 1/4" is right for s(f_n) as well,
  since c is arbitrary below 1/4.
- "Bounded by a polynomial in the size of the input": the hypotheses bound by rank(x). The families of the paper
  defeat a bound in the bit length too (the inputs are columns of height n; for the torus see R3), so "size" does
  not overstate.
- "A semistable cubic" in the abstract is the span condition of Theorem 4.3, which semistability implies (Lemma 4.1).
- The input ranks n² + 5n, 2n + m + 1, 5 and 6 and the parameters h = n and h = m² + n + 1 agree with GCT VI,
  Section 3.4, Hypothesis 1.6.5 and the appendix.
- "What is not claimed" is right. Its remark that the run computed r = 0 for n = 2, 3, 4, 5 is given as the run's
  and is not used.
- Not exact: the title (R8) and "All three refutations" (R5).

## 5. The literature paragraph

The statement "we found no earlier refutation of PH3, or of the relaxed SH(a) and PH2" is true of the searches on
record, and Section 9 calls the search bounded. The wording of what was searched is wider than the record (R7).

I ran three web searches of my own on 25 November 2026 (PH3 and the modular index with counterexamples; stretched
rectangular Kronecker coefficients with saturation; "positivity index" or "saturation index" with Mulmuley's
hypothesis). They showed no refutation of PH3 or of the relaxed SH(a) and PH2. They showed four texts that a reader
of this field will expect to see named. I saw them in search results and did not open them; the writer should open
each and cite it by its statement before the paper is posted:
- C. Ikenmeyer, K. Mulmuley, M. Walter, *On vanishing of Kronecker coefficients*, arXiv:1507.02955: deciding
  positivity of Kronecker coefficients is NP-hard; it also treats triples with vanishing coefficient and
  nonvanishing stretched coefficient. It concerns the exact decision problem, not the relaxed hypotheses.
- N. Fischer, C. Ikenmeyer, *The computational complexity of plethysm coefficients*, arXiv:2002.00788: the same for
  plethysm coefficients.
- C. Ikenmeyer, G. Panova, *Rectangular Kronecker coefficients and plethysms in geometric complexity theory*,
  arXiv:1512.03798: the family of rectangular Kronecker coefficients, to which k_n belongs.
- The workshop report arXiv:1203.2888, which states the relaxed bounds as a conjecture of Mulmuley.
The Oberwolfach report 9/2020 on Kronecker, plethysm and Sylow branching coefficients, which I opened as text, has
nothing on these hypotheses.

Still not done by anyone: a pass through the papers that cite GCT VI and the appendix, and a search of zbMATH.
I recommend it as a gate before posting. Once the first two papers above are opened, Section 9 should get a short
paragraph on them, and the sentence of R7 on what was not searched is then adjusted.

## 6. Section 2 against the sources (beyond the brief)

Only the writer had compared Section 2 with GCT VI beyond Hypotheses 1.6.7 and 3.3.4, so I did.
- Definitions 1.2.2 and 1.2.4 are as the paper states them, including "for every n ≥ 1" in strict saturation.
- Definition 1.2.7: as stated, except for the numerator (R6).
- Hypotheses 3.3.2(a), 3.3.3, 3.3.4 bound by O(poly(rank(x))); 1.6.5(a), 1.6.6, 1.6.7 by a polynomial in
  h = dim G + ht λ + ht π; the appendix by a polynomial in the largest height, with PH3 on the minimal positive form.
  All as the paper states.
- Theorem 1.6.1(b) is the quasi-polynomiality the paper cites in Section 7.1.

## 7. What this check does not cover

- The runs' own files were not opened; the comparison "as checked" is with CHECK.md of 22 Nov and with the paper.
- Lemma 5.2 for all n: read, and computed for n = 2..7 only.
- Standard results were taken as known: Schur-Weyl duality, the Frobenius formula, the Kempf-Ness criterion, Luna's
  slice theorem, the Koszul lemmas, and the quasi-polynomiality of GCT VI, Theorem 1.6.1(b).
- `src/ERRATA_GCT_VIII_DRAFT.tex` is not part of the paper and was not read.
- Pages of the PDF other than 3, 4 and 19 were not looked at by me; the build log has no overfull box and no
  warning, and the writer viewed all pages.

## 8. Files of this check

- `CHECK_P5_LAST_READ.md` (this file) and `CHECK_P5_LAST_READ_CHECK_EVENTS.tsv`.
- `checks/last_read_checks.py`, `.out`; `checks/last_read_hessian.py`, `.out`; `checks/last_read_lie.py`, `.out`
  (each ends "ALL AS CLAIMED").
- Work file: `agent_notes/ae84c4aa572daf430_NOTES.md`.
