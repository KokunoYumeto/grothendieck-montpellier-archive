# 60 · Plethysm in degrees five and six

**Checkpoint 02, 22 November 2026.** The paper now gives a vanishing criterion on every boundary face in outer degree six. Checkpoint 01 covered the strict interior. The new catalogue has 436 printed representatives and 836 distinct gap vectors after reversal. The paper also gives a positive construction in at most ten coordinates in degree six. Its finite preliminary list is specified algorithmically. A separate open question asks for a directly decoded basis uniform in the second row length.

**One new formula verified for its full range.** For the three-dimensional standard representation of the permutation group on four letters, the paper counts each irreducible multiplicity in a two-row Schur functor using at most six tagged sets of four nonnegative integers. I converted the counting rule to a generating function and compared it with the Schur characters on all five conjugacy classes. All five rational-function differences vanish identically, which proves the count for every pair of row lengths and every irreducible label. This character argument checks the multiplicities. The paper supplies its own maps from lattice points to summands. See standalone TeX line 3869.

**One degree-six boundary checked independently.** Reading the actual table gives 36 palindromic rows and coordinate maxima of 64, 54, 8, 54 and 64. For output partition (54,54) and inner degree 18, the binary Schur character gives the 11 multiplicities **16, 23, 68, 39, 11, 74, 54, 41, 23, 23, 0**, in the paper’s order. Thus the sign label is absent at second gap 54, which witnesses sharpness of the paper’s sufficient threshold 55. The 5,273-point exhaustion and the ten-coordinate construction remain outside this intake. See standalone TeX lines 240, 5457 and 5664.

**Editable paper.** All 21 included TeX sections are present. Recursively expanding the modular manuscript reproduces the standalone source exactly after newline normalization. The 102-page root and modular PDFs have identical extracted text on every page. These are archive and text checks. TeX compilation and layout inspection belong to the producing team.

The checkpoint arrived at 20:07:45 UTC in the configured Edge download folder. Its 234 ZIP members passed CRC checks. Archive SHA-256 is `5cc12a9cacd31852218fa89267e3bce99c305f0e8b8d29a2853488a170a2a789`.

## Proof of the four-letter counting identity

Write $V=W_4$, $r=a-b$, $d=\mathrm{sgn}(g)$, $z=dy$ and $D_g(q)=\det(I-qg|V)$. The bivariate character series for $S_{(r+b,b)}V$ is
\[
 \frac{1-dxy}{D_g(x)D_g(dy)}.
\]
Indeed $\bigwedge^2V=\det(V)\otimes V^*$ and $V$ is self-dual on $S_4$. Pieri decomposes $\mathrm{Sym}^rV\otimes\mathrm{Sym}^b(\bigwedge^2V)$ into one copy of each $\det^k\otimes S_{(r+b-2k,b-k)}V$ for $0\le k\le\min(r,b)$. This gives the displayed numerator. For a permutation with cycle lengths $m$, the denominator factor is $D_g(q)=\prod_m(1-q^m)/(1-q)$ by the splitting of the permutation representation.

For the counting formula of `workbench/paper/two_row_rank_four.tex`, lines 8–32, put
\[
 A_g(t)=\frac{\sum_{\eta\vdash 4}\chi_\eta(g)\sum_{h\in J_\eta}t^h}{(1-t^3)(1-t^4)} .
\]
Set $r'=r-2i-\epsilon$ and $b'=b-2j-\epsilon$. The last lattice equation uses coefficient $[t^{r'+b'+\epsilon}]A_g(t)$. Conjugating the label when $b+\epsilon$ is odd multiplies its character by $d^{b'}$. The unrestricted sums over $i,j$ give the two factors $1/(1-x^2)$ and $1/(1-y^2)$. Summing the other indices along diagonals gives
\[
 \frac{xA_g(x)-zA_g(z)+xy\bigl(A_g(x)-A_g(z)\bigr)}
 {(x-z)(1-x^2)(1-y^2)} .
\]
Using the standard character, the sign character, and the action on the three perfect matchings to construct the five irreducible characters, I simplified the difference between the two displayed bivariate character formulas to zero in each conjugacy class. Comparing irreducible characters proves the numerical identity for every $a\ge b\ge0$. The rational equality is an independent alternative proof and does not entail the paper's additional statement identifying each individual point with a summand through specific maps.

## Degree-six check and source files

The 436 printed representatives have coordinate sum parity governing the label conjugation under reversal. Parsing their gaps reproduced the distinct catalogue and maxima reported above. To check the sharpness witness directly, I evaluated the hook-content product $s_\mu(1,t,\ldots,t^{18})$ for all eleven $\mu\vdash6$. For binary output $(54,54)$ its multiplicity is the coefficient at weight 54 minus the adjacent coefficient at 53. The complete vector agrees with the supplied degree-six catalogue, including the sign zero. At the reversed gap the determinant twist is even, so rectangle complementation gives the same vector for the fourth-gap witness. The third-gap sharpness witness and global full-support implication were outside this calculation.

The archive is in `Documents/Papors/Chatnotes/CHat translates and clean/Noether Multilingual`. Its manifest records assembly at 19:45:37 UTC. The local modification time is 20:07:45 UTC. The previous receipt is `PLETHYSM_FORMULAS_checkpoint_01.zip`, SHA-256 `d3bb8ba140cf034ca49930285401efef22bfc53834e03c97a76b8e0a763761a3`. The root TeX retains the historical filename `plethysm_degree_five.tex` though the title now includes degree six. Its SHA-256 is `74286cbb922320a72b3709b217dcb42a17c59f9042dad8f559b32a3e6a46b550`. The project includes the inline bibliography, all project inputs and the build command in `workbench/README.md`. This was a source and PDF-text comparison without a fresh compile or visual audit.

The check program and output are in `CODEX_CP02_20261122_EVIDENCE/`. Private worker identity from the current turn record is GPT-6.2 Astra, reasoning effort ultra.
