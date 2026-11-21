# A100. The first pair correction for hook jets

## Scope and conclusion

**PASS.** I read the complete T066 report, PB.1–PB.15 and all five sections, its full positive evaluator and checker, and the saved receipt. I reread the exact-complex, normal-order, stabilizer and determinant passages FA.4, FA.6, FA.8–FA.9 and FA.13–FA.15 in G027. The proof has the required exact maps at the singleton and pair terms, and the stated last-map surjectivity follows from the already proved exact complex.

The conclusion is the complete valid boundary $a=2k-1$, $k\ge2$. It has the stated stable-hook multiplicity minus the jet multiplicity plus the horizontal-two-strip pair indicator. The difference between the latter two correction multiplicities is itself the multiplicity of an actual image representation, hence is nonnegative. This supports the explicit positive deletion construction.

## 1. Parameter range and concentration

Write $R=m-2$ and $\alpha=(a^{R-r},(a-1)^r)$. Then
$$
|\alpha|-mk=(m-4)k-(m-2)-r.
$$
The valid range PB.1 is exactly $|\alpha|\ge mk$, the degree range of FA.4 and the first-gap condition on the original partition. The other parts are ordered, nonnegative, and sum to $m(k-1+t)$. The formal $m=4$ range is empty, as its upper leg bound is negative. The omitted $k=1,a=1$ endpoint has no valid partition.

Taking the $S_\alpha F$ multiplicity is exact over $\mathbb Q$, since these finite polynomial representation spaces are completely reducible. It preserves the actual signed restriction differential and the subset orientations.

At a selected subset of size $q$, the residual space has dimension $d=R-q+1$. A nonzero semistandard skew character $S_{\alpha/\rho}\mathbb Q^d$ requires
$\rho_i\ge\alpha_{i+d}$ for $1\le i\le q-1$. To check this directly, a column present in row $i+d$ of $\alpha$ but absent from row $i$ of $\rho$ remains in every skew row $i,\ldots,i+d$, giving $d+1$ boxes in that column. This is impossible with only $d$ entries.

The normal degree is bounded above by $q(k-1)$. Its necessary lower bound is
$(q-1)(a-1)=2(q-1)(k-1)$, which is strictly larger for $q\ge3$ because $k\ge2$. Thus all terms after the pair term vanish. Terms with still larger subsets have already vanished in the original degree-$|\alpha|$ complex. This proves actual concentration rather than an alternating-character simplification.

## 2. Ambient and singleton comparisons

The full exterior-column complement in the width-$a$ rectangle of height $\dim E=m-1$ sends the padded $\alpha$ to $(a,1^r)$ and gives
$S_\alpha E=\det(E)^a\otimes S_{(a,1^r)}E^*$.
The invariant rational form identifies the dual standard module with the standard module. Tensoring the complex by the determinant factor removes the exponent $a$ and leaves precisely the common determinant exponent $t$ on the original balanced module.

At a singleton, complementary pairing in height $R$ changes the residual horizontal-strip rule into multiplication of $(1^r)$ by a row of length $u$. Every resulting first part is at most $u+1\le k\le a$, so none is lost outside the rectangle. This proves the whole module identity
$$
S_{\alpha/(u)}W
=\det(W)^a\otimes
  \bigl(\operatorname{Sym}^uW^*\otimes\Lambda^rW^*\bigr)
$$
for $0\le u<k$, including $u=0$, $r=0$ and $r=R$. At the top leg, the determinant factors reduce to the same identity, so there is no hidden missing constituent.

The comparison with the actual jet map is specified by FA.8. Its substitution
$Y_{0a}\mapsto-\sum_jx_jY_{ja}$ preserves the least normal degree: over the fraction field of the generic complementary matrix it is an invertible linear substitution. Hence its degree-$u$ coefficient map is injective on the relevant Schur multiplicity.

The preceding complementary Pieri identity identifies the dimension of that source with the full degree-$u$ horizontal-form jet space. Thus this particular coefficient map is an isomorphism. The exterior pairing is a bundle isomorphism, and the local horizontal frames from HJ.7 are honest frames on the whole affine chart. The comparison of truncated jets is consequently filtered triangular with invertible diagonal blocks; finite triangular elimination gives its inverse. This proves that the singleton differential is the original hook jet evaluation, not merely a map between representations having the same character.

After the common determinant twist is removed, the singleton term is exactly the induction in PB.11. Its positive multiplicity is the previously verified monomial-orbit/exterior/LR formula FK.11.

## 3. The pair term and its determinant signs

At $r=0$, the pair residual dimension requires $\rho_1\ge a=2k-1$, beyond the maximum normal degree $2k-2$. There is no pair term.

At $r\ge1$, the necessary lower bound is $\rho_1\ge a-1=2k-2$. Consequently both normal slots must have their maximum degree $k-1$, and their only surviving normal shape is the single row $(2k-2)$. The Cartan projection is ordinary multiplication of the two symmetric powers. Its inverse on that summand is the bidegree polarization divided by $\binom{2k-2}{k-1}$. This scalar is nonzero over $\mathbb Q$. Slot interchange is therefore the trivial action on this summand.

For the residual Pieri factor, dimension forces the bottom row of $\alpha$ to be removed in full. It already contains all $2k-2$ normal boxes, so every other row remains unchanged. The residual partition is precisely
$(a^{R-r},(a-1)^{r-1})$.
Its rectangle complement is $(1^{r-1})$, giving the exact determinant-twisted exterior module on $\mathfrak h_{m-2}$.

The pair orientation contributes $\operatorname{sgn}_{S_2}$. The global determinant factor contributes $\operatorname{sgn}_{S_2}^{a+t}\operatorname{sgn}_{S_{m-2}}^{a+t}$, and the residual determinant contributes $\operatorname{sgn}_{S_{m-2}}^a$. Since $a$ is odd, both resulting exponents are $t$ modulo two. Removing the same common twist leaves
$$
\operatorname{Ind}_{S_2\times S_{m-2}}^{S_m}
\bigl(\mathbf1\otimes\Lambda^{r-1}\mathfrak h_{m-2}\bigr).
$$
This verifies the trivial $S_2$ action, including the orientation; using only the normal multiplication without that orientation would not establish it.

The standard exterior power is the hook $(m-r-1,1^{r-1})$. Frobenius induction with the trivial $S_2$ factor is multiplication by $h_2$, so its multiplicity is precisely the horizontal-two-strip indicator in PB.3. At $r=R$, its complementary exterior power is the top standard exterior power and the same hook becomes the sign partition of $m-2$, as required.

## 4. Exactness, image multiplicity and positive cells

The original exact restriction complex and the preceding actual comparisons give PB.15 with left term $\operatorname{sgn}^t$ times the balanced module. One can also check that twist directly: the original kernel is $\operatorname{sgn}^{a+t}$ times the balanced module, and making the ambient module the untwisted stable hook tensors everything by $\operatorname{sgn}^a$.

The last differential remains signed polynomial restriction, followed by the stated Cartan and exterior identifications. Since the next complex term is zero, it is surjective. Its kernel, the image of the original hook jet map, has multiplicity $d-e$. Therefore $0\le d-e\le d\le D_k$, and the first kernel has multiplicity $c_{\rm stable}-d+e$.

For a positive correction, the label occurs in the jet term. The diagonal-width and invariant-label leg bounds from T064 therefore apply without change. At $a=2k-1$, the nonrow excess is at most $2k-2$, and the invariant total degree is at most $3k-2$. Both are smaller than the earlier proved bounded enumeration ranges.

Exactness proves that enough complete stable-hook points exist to remove $d-e$ of them. The bounded enumerator lists such points directly at the endpoint; no translation in degree is used. The first-differing-coordinate partition of the unique owner cell removes exactly one selected lattice point. All pieces retain the original bounded constraints, and each deletion increases the number of tags by $2N_{\rm poly}-1$. This verifies the count, disjointness and variable bound in PB.5.

The evaluator implements these exact branches: the valid parameter test, determinant conjugation, jet multiplicity, one horizontal-two-strip LR test, direct bounded point enumeration, unique-owner deletion and routing to the higher endpoints. Its runtime does not construct the restriction matrices. The earlier fixed-order bit bounds therefore apply with the stated smaller budgets.

## Source and computation scope

The external Pieri, Frobenius induction and LR locators used here were independently read in A090/A096: Macdonald I§5, equations (5.16)–(5.17), p.73; I§7, equations (7.1)–(7.3), pp.112–113; and the complete I§9 proof, pp.142–147. The actual geometric complex and normal substitution were reread from G027 for this review.

The author checker computes the pair trace by literal stable two-subsets and complementary exterior traces, then compares coefficients, parity, selected points and exported cells. I read its complete code and receipt. Its 3,193 pair comparisons, 6,386 complete coefficient/parity comparisons and 105 literal-polytope cases are the author's executions. Rectangular's separate 456 original plethysm comparisons are also reported separately by their owner. This audit does not claim to repeat either sweep.
