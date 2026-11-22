# Simon 1977 and the alternative proof obtainable from Grothendieck 1956

Date: 2026-11-20 UTC. Independent source and proof audit by crystalline_categories.

## Result and scope

The alternative mathematical route proposed by the parent is valid. The 1956 paper prints determinant estimates, algebraic identities and spectral correspondence from which a short complete proof of the Hilbert trace formula can be reconstructed. In particular, it would be wrong to describe its results as mathematically insufficient for that theorem. The reconstruction below explicitly identifies the added steps; the paper does not itself present the minimal-type argument, the zero-free logarithm argument, or the final global trace deduction. This is a narrower documentary conclusion than denying Grothendieck's knowledge, proof or priority. The undated manuscript independently contains his argument, and the particular manuscript sheets still lack a dated identification.

The exact historical lead in the prompt is cautious: cote 1 *may* predate 1959, and the printing question was not yet checked. An uncollated first physical printing is an edition qualification, not an additional task imposed by this audit.

## Opened primary sources

- A. Grothendieck, *La théorie de Fredholm*, Bulletin de la Société Mathématique de France **84** (1956),319–384. Opened full primary PDF: https://www.numdam.org/article/BSMF_1956__84__319_0.pdf . Saved as `notes/geometry_Fredholm1956.pdf`; SHA256 `ed38ba04cb7b00848a9e4fa73860efaae76b64873c15aa8a26cd5715d713f9f1`.
- B. Simon, *Notes on infinite determinants of Hilbert space operators*, Advances in Mathematics **24** (1977),244–273. Opened author bibliography https://math.caltech.edu/simon/biblio.html , actual item74 link https://math.caltech.edu/SimonPapers/74.pdf . Saved as `notes/category_Simon1977.pdf`; SHA256 `9820c0b7a05d4b89e3896282d02cf80cf0bb100325d3fabcc1b2ce1adc1e2fd8`. The successful final URL is74.pdf; the neighboring75.pdf link was not used.
- Kostenko's lecture notes, https://users.fmf.uni-lj.si/kostenko/teach/IdealsNotes.pdf , printedp44 Remark3.4.5 and bibliography[20],[49],[50], were opened as a finding aid. They attribute the theorem to1956 and say Simon rediscovered Grothendieck's approach. That historical assertion is not used as primary proof evidence. Bibliography[49] is precisely the Simon paper above.

## Exact comparison

| Ingredient | Grothendieck 1956 | Simon 1977 |
| --- | --- | --- |
| Mixed exterior product vanishes when more than `rank(A)` arguments equal `A` | I§1,Proposition1 and its Corollary,p327 | Included in the exterior-algebra framework |
| Exterior coefficients; linear coefficient is trace | I§2,p328,eq(4); I§3,pp330–331 | §3,p254,definition(3.3) |
| Entire determinant and multilinear coefficient bound | II§2,Proposition1,pp346–348; Hilbert specialization `k_n=1` onp348 | Lemma3.1p253; Theorem3.2p254 |
| Minimal exponential type | Follows by the finite-rank-tail argument proved below; that argument is not printed at the corresponding1956 passage | Theorem3.4,p254,with proof by splitting the singular-value product |
| Multiplicativity | II§2,p348,eq(4),by continuation of I§3 | Theorem3.8,p256,explicitly citing[8]=Grothendieck1956 |
| Zeros exactly at reciprocal eigenvalues; algebraic multiplicity | II§4,Theorem2 and corollary,pp354–355; Theorem4,pp359–361 | Theorems3.9–3.10,pp256–257 |
| Genus-zero entire-function lemma and application | Not supplied in the inspected1956 proof architecture | Theorem4.1,pp257–258; Theorem4.2,p258 |
| Full trace formula | Additional reconstruction below; no printed general Hilbert conclusion found | Corollary4.3,p258,by comparing linear coefficients |

Simon introduces his proof as new onp244 and explains its Hadamard-factorization method onp246. He explicitly credits Grothendieck for the determinant definition/algebra onp245 and for multiplicativity in Theorem3.8. His introductory reference to “our Theorem3.9” beside multiplicativity has an apparent theorem-number mismatch: the displayed multiplicativity theorem is3.8, whereas3.9 is invertibility. Neither his introduction nor his added notes onp272 supply a1956 full-proof locator. This is a positive citation check, not an inference about whether he knew every earlier result.

## Complete reconstruction from the1956 determinant ingredients

The proof in this section is ours. It is deliberately separated from the description of what the1956 text prints.

Let `H` be a complex Hilbert space and `T` a trace-class operator. Write `a_n(T_1,...,T_n)` for Grothendieck's symmetric multilinear exterior coefficient, normalized so that

\[
D_T(z)=\det(1+zT)=\sum_{n\ge0}z^n a_n(T,\ldots,T),\qquad
a_1(T)=\operatorname{Tr}(T).
\]

His Hilbert specialization of Proposition1 gives

\[
|a_n(T_1,\ldots,T_n)|\le \frac1{n!}\prod_{i=1}^n\|T_i\|_1.
\]

### 1. Minimal type from a finite-rank tail

Choose `A` of finite rank `m` with `R=T-A` and `||R||_1<epsilon/2`. If more than `m` arguments of `a_n` equal `A`, the coefficient vanishes. This is explicitly the Corollary to I§1 Proposition1,p327, combined with the trace definition I§2p328: every summand of the defining exterior product contains more than `m` vectors in the `m`-dimensional image of `A`. The printed corollary concerns finite-rank arguments; continuity from Proposition1 in II§2 proves it for arbitrary trace-class remaining arguments.

Multilinearity and the displayed bound therefore give, for `r=|z|`,

\[
\begin{aligned}
|D_T(z)|
&\le \sum_{n\ge0}\sum_{j=0}^{\min(m,n)}
 \binom nj\frac{r^n}{n!}\|A\|_1^j\|R\|_1^{n-j}\\
&=e^{r\|R\|_1}\sum_{j=0}^{m}\frac{(r\|A\|_1)^j}{j!}
\le C_\epsilon e^{\epsilon r}.
\end{aligned}
\]

The last inequality only absorbs a fixed polynomial into `exp(epsilon*r/2)`. Thus `D_T` is of minimal exponential type. This obtains exactly the input in Simon Theorem3.4 without presupposing Lidskii's theorem or spectral continuity.

### 2. Zero trace for a quasinilpotent operator

Suppose `sigma(T)={0}`. The printed zero/invertibility theorem shows that `D_T` has no zero. It has an entire logarithm `h` with `h(0)=0`, and

\[
\Re h(z)\le \epsilon|z|+\log C_\epsilon.
\]

For completeness, fix `w` and apply the Carathéodory derivative inequality on the radius-`R` disk about `w` to `h(z)-h(w)`. It gives

\[
|h'(w)|\le \frac2R\bigl(\epsilon(R+|w|)+\log C_\epsilon-\Re h(w)\bigr).
\]

Let `R` tend to infinity and then `epsilon` tend to zero. Hence `h'=0`, so `D_T=1`. Its coefficient of `z` gives `Tr(T)=0`. This argument is the zero-free case of the entire-function step and does not require the full genus-zero lemma.

### 3. General trace from finite primary spaces

Let `M` be the closed linear span of all finite-dimensional generalized eigenspaces of `T` for nonzero eigenvalues. List these spaces, choose Jordan flags inside them, and apply Gram–Schmidt along successive invariant finite-dimensional sums. The resulting orthonormal basis of `M` is triangular for `T|_M`, with diagonal entries equal to the nonzero eigenvalues, counted algebraically. Since `T|_M` is trace class, its diagonal is absolutely summable and

\[
\operatorname{Tr}(T|_M)=\sum_j\lambda_j(T).
\]

The quotient operator on `H/M`, equivalently the compression `Q` to `M^\perp`, is compact and quasinilpotent. Here is the relevant verification, rather than an assumption about completeness of eigenvectors. If a nonzero `lambda` is outside `sigma(T)`, its inverse resolvent preserves each primary space and therefore `M`, so it induces an inverse on the quotient. If `lambda` lies in `sigma(T)`, split off its finite primary space by the spectral projection of Grothendieck's Theorem4. This space is contained in `M`; on the complementary invariant space `T-lambda` is invertible, and its inverse again preserves the closed span of the other primary spaces. It consequently induces an inverse on the quotient. Thus every nonzero `lambda` is outside the quotient spectrum.

The compression `Q` is trace class, so step2 gives `Tr(Q)=0`. Compute the trace in an orthonormal basis of `M` together with one of `M^\perp`:

\[
\operatorname{Tr}(T)=\operatorname{Tr}(T|_M)+\operatorname{Tr}(Q)
=\sum_j\lambda_j(T).
\]

If `H` is nonseparable, reduce first to the separable invariant support generated by the ranges of `T` and `T^*`; `T` is zero on its orthogonal complement. The argument therefore does not need separability as an additional theorem hypothesis.

This proves the full trace formula from the1956 printed determinant foundations plus the explicitly supplied elementary complex-analysis and global decomposition steps. It also exposes exactly why checking only the absence of a three-sector genus-zero argument would have been too narrow.

## Preserved reading and verification record

The full relevant1956 architecture was independently read as recorded in `category_fredholm1956_audit.md`; the present check revisits the multilinear proof, finite-rank identities, the square-zero radical lemma (which is **not** the general quasinilpotent statement), and spectral blocks. Simon's introduction, §3, all of§4 and added notes/bibliography were read directly in the primary PDF extraction; pp254,257,258 were also visually collated at readable resolution. Grothendieck pp348,354 were visually revisited. The comparison rendering/extraction program and full output are `code/category_simon_fredholm_comparison.py` and `logs/category_simon_fredholm_comparison.txt`; the source-fetch program/output are separately retained.

Root independently audited this complete reconstruction and passed it, specifically checking mixed-coefficient rank vanishing, the quotient-resolvent argument and trace decomposition. Geometry is integrating a separately numbered proposition and may use the already opened Hadamard zero-free case in place of step2's derivative inequality.

The final historical wording should distinguish: explicit printed theorem or proof; a consequence we reconstruct from printed ingredients; a scholarly attribution; and the still-undated particular manuscript. None of these categories supplies the date of another by itself.
