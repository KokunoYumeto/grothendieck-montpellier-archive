# Degree selection and positivity for nonstandard Hecke algebras

**Lead with a coefficient a reader can check against the original paper.** In GCT VIII, Figure 2 displays the coefficient of γ²₂₁ in its own square. I compared the figure with the draft and divided its displayed Laurent polynomial by $(q^{1/2}-q^{-1/2})^2$. The residual coefficients are **1, 1, 3, 2, 3, 1, 1**. Their sum at $q=1$ is 12, so the exponent is forced for any nonzero residual with nonnegative coefficients. The drop from 3 to 2 and rise to 3 disprove the claimed unimodality for this printed coefficient. The external-degree prescription independently has an unbounded descending sequence in rank one. GCT VI's general existence question concerns a wider choice of quantizations and bases. [Mulmuley, GCT VIII, Conjecture 3.4](https://arxiv.org/pdf/0709.0751v2#page=24) · [Reported verification](https://arxiv.org/pdf/0709.0751v2#page=29) · [Figure 2](https://arxiv.org/pdf/0709.0751v2#page=34)

**Rank-four check.** I read the five-coordinate proof and independently solved its triangular system over the rational function field. From the displayed pivot matrices and the column of $H_1$, I recovered all five coefficients, ending in $c(H_1,H_{109};H_{109})=-D^2+6D-6$. Its values at $D=9/2,5$ are $3/4,-1$. Since both correspond to $v>1$, the sign change precludes signed nonnegative Laurent positivity for this specified maximal-scaling Hermite basis. For the paper, state the ordering and repair at the first mention of this counterexample. The calculation takes the displayed pivot matrices as input. The global 114-element basis, 204,876 nonzero rank-four entries, full 132-entry rank-three count, and categorical constructions remain outside my independent check.

**Source correction.** In root `NONSTANDARD_BASES.tex`, lines 1687 and 1755 write `DA` in the formula for Σ, although $A$ names the coefficient ring and the intended scalar is $A_2=(D-2)^2$. The introduction's line 111 and expansion of the relation at lines 1751–1753 give `DA_2`. At line 601 specify “the root in the attainable range $D>4$” since $3-\sqrt{3}$ is also positive. Both corrections preserve the arguments above.

Archive `NONSTANDARD_BASES_checkpoint_01.zip`, SHA-256 `b5a296729b1fd849eb4c5f9391fca20cfd7805d1300e947b98775221af15009c`. In the root TeX, the rank-one proof is at lines 179–188, the rank-four system starts at 529, and the rank-three multiplication proof is at 1720–1880. The scope of the rank-four repairs is in lines 70–100.

## Manuscript organization

**Manuscript corrections.** In `NONSTANDARD_BASES.tex`, lines 1687 and 1755 should read $DA_2$, with $A_2=(D-2)^2$, in the formula for $\Sigma$. The printed $DA$ uses the name of the coefficient ring. At line 601 qualify the root by its attainable range $D>4$; $3-\sqrt3$ is positive as well. Lead with the recoverable Figure 2 calculation and specify the rank-four basis and ordering before the sign change. The general GCT existence question allows other choices of quantization and basis.


Replay files are in `CODEX_CP01_20261122_EVIDENCE/`. The check-event table sits beside this note. These are targeted Codex reads, GPT-6.2 Astra, effort ultra.
