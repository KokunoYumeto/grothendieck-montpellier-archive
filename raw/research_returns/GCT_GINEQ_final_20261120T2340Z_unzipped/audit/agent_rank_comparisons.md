# Precisely scoped rank comparisons: determinant and permanent

Prepared by `/root/tensor_norms`, GPT-6 Astra Pro (inherited); effort setting not exposed. Source statements checked on 2026-11-20 UTC. These are literature comparisons, not claims of new results. Source computations cited below were not rerun.

## Conventions that must stay separate

- `D_n,P_n in (K^n)^{tensor n}` are the **row tensors**, sums of signed/unsigned permutation basis tensors.
- `S_det,S_per in Sym^n(K^{n^2})` are the **symmetric polynomial tensors** representing the determinant/permanent in `n^2` variables. Their coefficients are `+/-1/n!` on the `(n!)^2` compatible ordered sequences under our polynomial convention. Multiplying any of these tensors by a nonzero scalar changes none of the ranks discussed here.
- `R` and `border R` mean ordinary CP rank and ordinary CP border rank; `WR` and `border WR` mean Waring rank and symmetric border rank. In general only `R <= WR` and `border R <= border WR` are available. A lower bound on symmetric border rank alone does **not** lower-bound ordinary CP border rank.
- The symmetric row permanent `P_n` represents a nonzero scalar multiple of the **squarefree monomial** `x_1...x_n` in `n` variables. It is not the symmetric polynomial tensor `S_per` of the `n by n` permanent in `n^2` variables.

## L-01. Farnsworth's symmetric Koszul--Young comparison

Cameron Farnsworth, *Koszul--Young Flattenings and Symmetric Border Rank of the Determinant*, arXiv:1505.05079v2 (11 November 2015).

Primary PDF: https://arxiv.org/pdf/1505.05079

Safe field scope for this comparison: complex symmetric polynomial tensors. Lower bounds then also hold for real symmetric border rank. The paper uses characteristic-zero representation theory, and explicit later calculations use `C^9`; no broader field claim is needed here.

**Theorem 1.3, p.1:** for `n >= 5`,

- if `n` is even,
  `border WR(S_det) >= [1 + 8(n^3+6n^2-8)/((n-1)(n+2)(n+4)^2(n^2-2))] binom(n,n/2)^2`;
- if `n` is odd,
  `border WR(S_det) >= [1 + 16(n^2+8n+9)/((n+3)(n+5)^2(n^2-2))] binom(n,(n-1)/2)^2`.

An integer lower bound is obtained by taking a ceiling. These improve the ordinary catalecticant lower bound, but they are stated for **symmetric border rank**, so must not be transferred to row tensors or ordinary CP border rank.

**Theorem 1.6, p.2:** `border WR(S_det, n=4) >= 38`, versus ordinary catalecticant rank 36.

**Theorem 1.8, p.2:** `border WR(S_det, n=3) >=14` and `border WR(S_per, n=3) >=14`. These are computed using a Macaulay2 package, not independently recomputed here. **Corollary 1.11, p.2** also gives `14 <= border WR(S_per, n=3) <=16`.

For completeness, **Theorem 3.7, p.5**, valid for `n>=3`, gives weaker explicit factors `1+4/((n-1)(n+2)^2)` for even `n`, and `1+8/((n-1)(n+3)^2)` for odd `n`, multiplying the same central binomial square.

Do not call the lower bound 14 current best for `S_det, n=3`; see L-05 below.

## L-02. Recursive Koszul flattenings for the row tensors

Jong In Han, Jeong-Hoon Ju, Yeongrak Kim, *Recursive Koszul flattenings of determinant and permanent tensors*, arXiv:2503.12032v1 (15 March 2025).

Primary PDF: https://arxiv.org/pdf/2503.12032

The introduction explicitly places these tensors in `(K^n)^{tensor n}` and distinguishes them from polynomials in `n^2` variables. These are **ordinary row CP rank/border-rank** results.

**Proposition 3.2, p.6, equations (3.1)--(3.3):** the recursive Koszul linear map with wedge parameters `p_i` in factors of dimensions `m_i` has simple-tensor matrix rank at most `prod_i binom(m_i-1,p_i)`. Its matrix rank divided by that cost lower-bounds ordinary CP border rank. The main application has `n-2` wedge factors and parameters `(1,2,...,n-2)`. The source's extreme stated range for its auxiliary parameter `s` appears broader than its displayed map supports; none of the main results used here depends on that extreme case.

**Theorem 4.2, p.9:** over every characteristic-zero field,

`border R(D_n) >= n^(n-1)/(n-1)! = n^n/n!`.

For `n>=3` the displayed recursive construction applies directly; the `n=2` inequality is immediate separately. This gives the rounded bounds 5, 11, 27, 65, 164 for `n=3,4,5,6,7`, respectively. The proof makes the selected recursive Koszul matrix invertible by representation theory. Its final argument extends from `C` to all characteristic-zero fields via a nonzero rational determinant.

**Theorem 4.5, p.11:** for `char(K)>=3`, `border R(D_4)>=11`; for `char(K)>=5`, `border R(D_5)>=27`.

**Theorem 4.7, pp.11--12:** `R(D_4)=12` when `char(K) !=2`. This theorem concerns ordinary rank, not border rank. The later L-03 settles border rank over subfields of `C`.

**Theorem 5.6, pp.14--15:** characteristic zero,

| Tensor | Certified CP border lower bound | Ordinary rank / border equality supplied |
|---|---:|---|
| `P_4` | 8 | `R(P_4)=border R(P_4)=8` |
| `P_5` | 15 | no equality in this paper |
| `P_6` | 29 | no equality |
| `P_7` | 55 | no equality |

The matrix ranks used are 70, 1426, 70692, and 8763494, respectively, at sizes 96, 2500, 162000, and 26471025. These substantial literature computations have not been rerun.

**Theorem 5.7, p.15:** `R(P_4)=border R(P_4)=8` and `border R(P_5)>=15` also hold when `char(K) !=2`.

Do not reproduce the paper's Question 4.8 or its `n=5` case of Question 5.8 as open: see L-03 and L-06.

## L-03. Exact row determinant border rank in dimension four

Jong In Han, Jeong-Hoon Ju, Yeongrak Kim, *The border rank of the 4x4 determinant tensor is twelve*, arXiv:2510.11051v2 (18 August 2026).

Primary PDF: https://arxiv.org/pdf/2510.11051

**Theorem 1.1, p.2:** `border R(D_4)=12` over every subfield of `C`.

The tensor is the row tensor in `(C^4)^{tensor4}`. This goes beyond the recursive Koszul bound 11 by border apolarity and ideal tests. The substantial computational proof was not rerun here; statement, field, and object were checked in the source.

## L-04. Exact symmetric border rank of the row permanent / squarefree monomial

Jong In Han, *The border Waring rank of x_1...x_n is 2^(n-1)*, arXiv:2609.09141v1 (8 September 2026).

Primary PDF: https://arxiv.org/pdf/2609.09141

**Theorem A, p.2:** over every characteristic-zero field,

`border WR(x_1...x_n)=2^(n-1)`, equivalently `border WR(P_n)=2^(n-1)`.

The source defines Waring decompositions with scalar coefficients and uses Zariski-closure border rank. Its proof uses higher-order Koszul maps of the nonsymmetric row determinant. The theorem is specifically about symmetric border rank. It does **not** settle `border R(P_n)` or `R(P_n)` for general `n`.

Retrieved and read the actual arXiv PDF directly; a web-indexing error on the PDF endpoint was bypassed by ordinary direct download. Author's October 7, 2026 seminar notes independently confirm the statement, but the paper is the primary citation. No claim to have independently reproved the entire theorem is made.

## L-05. Exact CP border rank of the 3x3 determinant polynomial tensor

Austin Conner, Alicia Harper, J. M. Landsberg, *New lower bounds for matrix multiplication and det_3*, Forum of Mathematics, Pi 11 (2023), e17. DOI: 10.1017/fmp.2023.14. arXiv:1911.07981.

Primary publisher PDF:
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/170334CE1BE6A9604BD4D941258326F3/S2050508623000148a.pdf/new_lower_bounds_for_matrix_multiplication_and_operatorname_det3.pdf

**Theorem 1.2, Section 1.2, p.4:** `border R(S_det, n=3)=17` over `C`.

The preceding paragraph explicitly defines `det_3 in C^9 tensor C^9 tensor C^9` as the symmetric determinant polynomial tensor. It is not the row determinant in `(C^3)^{tensor3}`. The source's convention may differ by a nonzero scalar, which does not affect rank. Since ordinary CP border rank is at most symmetric border rank, the theorem implies `border WR(S_det, n=3)>=17`. It does not assert equality of symmetric border rank and ordinary border rank. Equality 17 over `R` is not inferred from the complex theorem.

The lower-bound proof uses computational border apolarity. It was not independently rerun. The same source **Theorem 1.1, p.4** gives `border R(M_3)>=17`. The historical lower bound `2n^2-ceil(log_2 n)-1` alone gives only 15 at `n=3`, so it must not be presented as current best in that small case.

## L-06. Exact ordinary row permanent rank in dimension five, and one-step border improvement

Jong In Han, Jeyoung Song, *The rank of the 5x5 permanent tensor is sixteen*, arXiv:2608.09708v2 (27 August 2026).

Primary PDF: https://arxiv.org/pdf/2608.09708

**Theorem A, p.3; proof in Section 3, pp.6--10:** `R(P_5)=16` over every characteristic-zero field. This is ordinary CP rank. The proof tests `P_5-S` for all nonzero simple tensors `S`, using higher-order Koszul flattenings, symmetry reduction, and exact symbolic rank-locus computations. Those computations were not rerun.

**Proposition 4.1, pp.10--11:** over `C` and its subfields, for `d>=3`,

`border R(P_d)>=binom(d,floor(d/2))+1`.

This is a strict improvement over the basic flattening bound for every such `d`. The full short proof was read and independently reconstructed as follows. Take an `a|(d-a)` flattening with `a=floor(d/2)` and `b=d-a>=2`. Its image has dimension `r=binom(d,a)` and consists of symmetric squarefree tensors of degree `b`. If border rank equaled `r`, a convergent sequence of rank-at-most-`r` decompositions would, after passing to the Grassmannian, force this image to be a limit of `r`-planes spanned by simple tensors. A subsequence of one projective simple tensor in each plane converges, by compactness of the Segre variety, to a nonzero simple tensor in the limit image. But a nonzero symmetric simple tensor is a scalar pure power, so has a nonzero diagonal coefficient `e_i^{tensor b}` for some `i`; the squarefree image has no such coefficient. Contradiction. The local ranks can be taken exactly `r` eventually, since the limiting flattening has rank `r` and its nonzero minor remains nonzero. Extension of independent simple spanning vectors to `r` of them, if needed, yields the same conclusion.

The source immediately after Proposition 4.1 explicitly leaves `border R(P_5)` equal to either 15 or 16 as an open question. Do not conflate Theorem A with a border-rank equality.

## Comparison to the valid full-tensor norm conversion

Under N-01, the strongest of the three stated full-tensor ratios yields the following lower bound before rounding. This is a valid inference, but is always dominated by the ordinary mode ranks, and therefore also by the balanced flattenings below.

| Tensor / order | Valid full-norm inference | Balanced ordinary flattening rank |
|---|---:|---:|
| `M_n`, order 3 | `n^(3/2)` | `n^2` |
| `D_n`, order n | `(n!)^(1/(n-1))` | `binom(n,floor(n/2))` |
| `P_n`, order n | `(n^n/n!)^(1/(n-1))` | `binom(n,floor(n/2))` |
| `S_det`, order n | `n^(n/(n-1))` | `binom(n,floor(n/2))^2` |
| `S_per`, order n | `(n^n/n!)^(2/(n-1))` | `binom(n,floor(n/2))^2` |

Here `n>=2`; integer lower bounds use ceilings. This table is elementary recomputation from our established exact norms. It is not an impossibility theorem for all norm-based, preconditioned, or nonlinear methods.

## Check events for incorporation

All checks below: 2026-11-20T23:14Z, GPT-6 Astra Pro (inherited), effort not exposed, run `GCT_GINEQ/tensor_norms`. No formal theorem prover used.

| ID | Actual event type | Result / limitation |
|---|---|---|
| B-Farnsworth-2015 | carried as background without fault found | Theorems 1.3,1.6,1.8,3.7 and Corollary 1.11 statements/normalizations/parity read. Specialized proofs and Macaulay2 computations not reverified. |
| B-HJK-2025 | carried as background without fault found | Definitions, Proposition 3.2 main-use scope, Theorems 4.2,4.5,4.7,5.6,5.7 read. Field distinctions, rounding and rank-vs-border scope checked; large computations not rerun. |
| B-HJK-D4-2026 | carried as background without fault found | Theorem 1.1 and tensor definition read; ordinary row CP border equality 12 correctly identified. Computation not rerun. |
| B-Han-monomial-2026 | carried as background without fault found | Actual PDF Theorem A, p.2, and definitions read. All characteristic-zero fields; symmetric border only. No full reproof claimed. |
| B-CHL-2023 | carried as background without fault found | Theorem 1.2 and adjacent object definition read in publisher PDF. Ordinary CP border of `C^9` symmetric polynomial tensor equals17. No computational reproof. |
| B-HanSong-rank5-2026 | carried as background without fault found | Theorem A, p.3, and proof architecture read. Ordinary rank16, not border16; symbolic computation not rerun. |
| B-HanSong-plus-one | independent re-proof | Full Proposition 4.1 proof read and reconstructed via limiting Grassmannian/Segre incidence, squarefree image, and symmetric simple tensor property. Pass over C and subfields. |
| N-comparison-table | targeted proof check | All full-norm exponents and basic balanced flattening ranks recomputed from established norms. Pass. |

Downloaded source PDFs/text are verification caches under `work/`; they need not be redistributed inside the final deliverable.
