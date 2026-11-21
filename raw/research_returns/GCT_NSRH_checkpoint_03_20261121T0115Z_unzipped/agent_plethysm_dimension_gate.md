# F34: an explicit dimension obstruction to the literal compact-input PH1 bound

Author/checker: /root/rectangular_and_theta, GPT-6 Astra Pro. Date: 2026-11-21 UTC.

## Status and precise conclusion

This note gives an elementary, fully written deduction for the exact compact-input formulation in the supplied GCT VI version. It does not claim priority over the literature. In particular, Kahle–Michałek already disproved the universal ordinary Ehrhart-existence assertion in VI by a stronger fixed-small-parameter example; that known result must be cited when describing the status of PH1.

Here the purpose is different: an actual positive simplex model makes the necessary dimension grow linearly in an inner binary weight k. Consequently the universal polynomial-in-bitlength dimension bound in **VI, Hypothesis 1.6.4(2), printed p.23**, is false under VI's own nonzero-part encoding. The underlying coefficients remain nonnegative, have an explicit positive counting rule, and in this family are exact Ehrhart counts. No stipulated RH/GRH result is challenged.

This is currently an author proof and exact-source check. The root and the GCT statements agent are separately checking the source and deduction. No formal-kernel certificate is claimed.

## 1. Source and version checks

The supplied file is sources/LIT_Mulmuley_GCT_VI_flip_via_positivity/main.tex, SHA-256:

2772a098e172e906858696eb2aeb747c00b0a39469086a5e247f558a53729138.

The primary numbered PDF was independently downloaded from
https://arxiv.org/pdf/0704.0229v4
to primary_sources/GCT_VI_0704_0229v4.pdf, SHA-256:

c38318b128ea63c424560cd9d7bc3cc1dab79973a6b63b2fbde6569c8f62c6df.

Its layout text has SHA-256:

ff7c27c3074cf2d1e79712847e9945f1d8d4bb2088cc1fdf22b32bd28cafd376.

The numbered PDF and supplied TeX agree at every following locator.

| Issue | Exact v4 locator | Supplied TeX locator | Consequence |
|---|---|---|---|
| Meaning of plethysm | Problem 1.1.2, printed p.7 / PDF p.10 | problem label pintroplethysm, lines 414–431 | H is the original GL group; G=GL(V_mu(H)); outer lambda labels G and output pi labels H |
| Compact partition input | Section 1.1, printed p.9 / PDF p.12 | lines 545–555 | Zero parts are suppressed; height is the number of positive parts; bitlength is the sum of their binary lengths |
| Stretching | Equation (1.5), Section 1.6, printed p.20 / PDF p.23 | immediately before label tquasiplethysm, lines 1166–1180 | The stretch is a_(N lambda,mu)^(N pi); mu is fixed |
| Target PH1 | Hypothesis 1.6.4(1)–(3), printed p.23 / PDF p.26 | label hph1plethysmintro, lines 1304–1341 | One ordinary Ehrhart polytope must give the full ray, with the stated succinct dimension bound |
| Explicit zero-padding clarification | Opening of Section 3.4, before Section 3.4.1, printed p.53 / PDF p.56 | lines 2899–2915 | The nonzero-part convention is deliberate even if rank(G) is exponential in the bitlength of mu |

The crucial exact source phrases are “the zero parts of the partition are suppressed” (p.9), “mu is not stretched” (p.20), and “only nonzero parts of lambda are specified” (p.53). The mathematical content of PH1(2) is
\[
m\le \operatorname{poly}(\langle\mu\rangle,
                  \operatorname{ht}(\lambda),\operatorname{ht}(\pi)),
\]
where m is the ambient dimension and the polynomial is uniform across the family. PH1(1) requires the ordinary stretching identity
\[
a_{N\lambda,\mu}^{N\pi}=\#(N P_{\lambda,\mu}^{\pi}\cap\mathbf Z^m).
\]

There is no padding loophole: source p.53 explicitly motivates compact lambda input by the possibility that G has enormous rank. Adding the original H-rank as a parameter would also not repair this example, because H has fixed rank two.

Do not call this source statement Hypothesis 1.6.5 in v4: 1.6.5 is the following saturation hypothesis SH. Some other indexed versions have different numbering.

## 2. The actual binary-form family

For an arbitrary integer \(k\ge3\), take
\[
H=\mathrm{GL}_2,\quad
\mu=(k),\quad
V_\mu(H)=\operatorname{Sym}^{k}\mathbf C^2,\quad
G=\mathrm{GL}_{k+1},
\]
and
\[
\lambda=(1),\qquad \pi=(k-1,1).
\]
Both labels are legitimate: lambda is the defining G-module and pi has length two. At stretch N,
\[
c_k(N):=a_{(N),(k)}^{((k-1)N,N)}
=
[\operatorname{Sym}^{N}(\operatorname{Sym}^{k}\mathbf C^2):
                 S_{((k-1)N,N)}\mathbf C^2].
\tag{D1}
\]
This is exactly VI's stretch: the inner weight k stays fixed while the outer and output labels are multiplied by N.

The classical two-row specialization, restated in Pak–Panova–Swanson, Lemma 1.3(1)–(2), printed p.2, gives
\[
c_k(N)=p_N(N,k)-p_{N-1}(N,k),
\tag{D2}
\]
where \(p_r(N,k)\) counts partitions of r in the k by N rectangle. At r=N and r=N-1, the width bound N is automatic. Conjugating a partition identifies the remaining at-most-k-row condition with parts of size at most k. Therefore
\[
\begin{aligned}
c_k(N)
&=[z^N](1-z)\prod_{i=1}^{k}(1-z^i)^{-1}\\
&=[z^N]\prod_{i=2}^{k}(1-z^i)^{-1}\\
&=\#\{(x_2,\ldots,x_k)\in\mathbf Z_{\ge0}^{k-1}:
                          2x_2+\cdots+kx_k=N\}.
\end{aligned}
\tag{D3}
\]

For clarity, the weight interpretation also verifies the specialization directly. A monomial in \(\operatorname{Sym}^{N}(\operatorname{Sym}^{k}\mathbf C^2)\) has multiplicities \(a_0,\ldots,a_k\) with \(\sum a_i=N\) and second-coordinate weight \(\sum i a_i=r\). When r is N or N-1, \(a_0\ge0\) imposes no further constraint on \(a_1,\ldots,a_k\), since \(\sum a_i\le\sum i a_i=r\le N\). For GL2, the highest-weight multiplicity at r≤kN/2 is the difference of the adjacent weight multiplicities. This recovers (D3), with \(r=N\) allowed because k≥2.

Equation (D3) is an elementary specialized consequence of the known identity, not a new general plethysm rule.

## 3. A positive simplex exists, and its dimension is necessary

Define
\[
P_k=\{x\in\mathbf R_{\ge0}^{k-1}:
                            2x_2+\cdots+kx_k=1\}.
\tag{D4}
\]
It is the rational simplex with vertices \(e_i/i\), \(2\le i\le k\). Its affine dimension is k-2, and
\[
c_k(N)=\#(N P_k\cap\mathbf Z^{k-1})
\]
for every nonnegative integer N. Thus this family does have a completely explicit ordinary Ehrhart model. Its denominators divide \(\operatorname{lcm}(2,\ldots,k)\).

We now prove that no smaller-dimensional fixed polytope can represent the same full ray.

Put \(L_k=\operatorname{lcm}(2,\ldots,k)\). For N=L_k s and every nonnegative solution
\[
y_2+\cdots+y_k=s,
\]
set \(x_i=(L_k/i)y_i\). This is an injective map into the solution set in (D3), since
\(\sum i x_i=L_k\sum y_i=N\). Consequently
\[
c_k(L_k s)\ge
   \binom{s+k-2}{k-2}.
\tag{D5}
\]
In the other direction, choosing \(x_2,\ldots,x_{k-1}\) determines \(x_k\) if it exists; each chosen coordinate is at most N. Hence
\[
c_k(N)\le (N+1)^{k-2}.
\tag{D6}
\]
For each fixed k the growth exponent is therefore exactly k-2. In particular (D5) already gives the lower bound needed below; no asymptotic partition estimate is required.

Let Q be any fixed bounded polytope of affine dimension d in some finite-dimensional real coordinate space. Then
\[
\#(NQ\cap\mathbf Z^m)=O_Q(N^d).
\tag{D7}
\]
One elementary proof is to choose d coordinate functions whose restriction to the direction space of \(\operatorname{aff}(Q)\) is injective. Their joint projection is injective on every \(N\operatorname{aff}(Q)\). Since Q is bounded, the projected integral points lie in a d-dimensional integer box with side lengths \(O_Q(N)\). This proves (D7) even when the affine hull is not a rational linear subspace through zero.

If the Ehrhart count of Q equals c_k(N) for all N, apply (D7) along N=L_k s and compare with (D5). Necessarily
\[
\dim Q\ge k-2.
\tag{D8}
\]
The same conclusion follows if equality is only eventual, since (D5) holds on an unbounded progression. The simplex in (D4) attains the lower bound.

## 4. Contradiction to the literal uniform bound

For the fixed base labels in (D1),
\[
\langle\mu\rangle=O(\log k),\qquad
\operatorname{ht}(\lambda)=1,\qquad
\operatorname{ht}(\pi)=2.
\]
The total compact input length is also \(O(\log k)\). H=GL2 contributes only a fixed rank parameter. The k trailing zero coordinates of lambda in GL_(k+1) are expressly absent from the specified input.

If the supplied PH1(2) held uniformly, some fixed polynomial p would bound the ambient dimension of its polytope by
\[
m_k\le p(O(\log k),1,2).
\]
But affine dimension never exceeds ambient dimension, while (D8) says
\[
k-2\le\dim P_{\lambda,\mu}^{\pi}\le m_k.
\]
A linear function of k eventually exceeds every fixed polynomial in log k. This is a contradiction.

The contradiction concerns the **literal compact-input dimension claim**. Allowing the dimension to depend polynomially on the numerical k, including rank(G)=k+1 in the complexity parameter, or encoding k in unary avoids this contradiction. None of those alternatives is the wording of PH1(2) at the cited supplied locator. A different statement using weighted counts, succinct generating functions, or different parameter-dependent counting objects likewise needs its own formulation.

## 5. A direct output-length warning for wholly binary plethysm inputs

There is a complementary elementary reason not to interpret the PPS numerical dynamic-programming discussion as a uniform #P claim under the compact binary encoding of all three plethysm partitions.

Let \(m\ge2\), \(k=2m\), and \(N=m(m+1)\). In (D3), choose each \(x_{2i}\), \(2\le i\le m\), independently in \(\{0,1\}\); set every odd-indexed coordinate to zero, and then set
\[
x_2=\frac{N-\sum_{i=2}^{m}2i\,x_{2i}}2.
\]
The numerator is even and nonnegative, because
\[
\sum_{i=2}^{m}2i=m(m+1)-2=N-2.
\]
This constructs \(2^{m-1}\) distinct solutions. Therefore
\[
a_{(N),(2m)}^{((2m-1)N,N)}\ge2^{m-1}.
\tag{D9}
\]
All parts of these three input partitions have \(O(\log m)\) bits, and there are only four nonzero parts in total. The output consequently needs at least m bits on inputs of length \(O(\log m)\).

A #P function on input length L is at most \(2^{p(L)}\) for some fixed polynomial p, because its witnesses have at most p(L) bits. Inequality (D9) disproves such a uniform #P representation for this fully binary plethysm function, without any complexity-separation assumption. This statement concerns the specified compact encoding; it does not conflict with unary-input #P formulations.

In contrast, the corresponding rectangular Kronecker input explicitly lists k parts in each rectangle. Its input length is at least k, so this output-length obstruction disappears. This difference explains why the separate compressed KOH-tree witness construction can give a polynomial binary-part witness rule for that rectangular family while the analogous completely compact plethysm claim cannot hold.

## 6. Known stronger PH1 failure and historical scope

Kahle–Michałek, *Obstructions to combinatorial formulas for plethysm*, Electronic Journal of Combinatorics 25(1) (2018), P1.41, **Theorem 5 and Remark 6, p.4**, already give a fixed-small-parameter stretching ray that is not the Ehrhart function of any rational polytope. Their p.2 explicitly identifies the relevant question with VI Hypothesis 1.6.4. Their pp.3–4 separately distinguish the later 2011 inhomogeneous formulation; their result does not dispose of that later question in every dimension.

Primary source:
https://www.combinatorics.org/ojs/index.php/eljc/article/download/v25i1p41/pdf/

That published result should establish the historical status of the universal ordinary Ehrhart claim in the main paper. The present family is useful because it gives an independent direct obstruction to the **succinct dimension bound**, even on a ray with an actual positive simplex formula. No claim of novelty or priority is made for that elementary deduction.

## 7. Exact PPS version and source scope

The initial author-hosted PPS PDF remains a 12-page manuscript dated 4 November 2025. A primary arXiv check during this audit found version 3, submitted 27 July 2026, 13 pages, with the same Lemma 1.3 and KOH definitions. The later version corrects the previously noticed index in the proof of Lemma 4.2 and calls the general trees GOS rather than GOH.

Version used for the updated reference:
https://arxiv.org/abs/2511.02312v3
https://arxiv.org/pdf/2511.02312v3

Local primary_sources/Pak_Panova_Swanson_trees_v3.pdf has SHA-256
613040c2ec259527bfe4b45e5b8f67fbd4a12b468fefc1428b38ebafa0a3f360.
The layout text has SHA-256
391520d2e2ca63ab02df97988e57b700311cd4620f59c214b67d3c2c4ceb6cd8.

The source theorem is cited, not reclassified as a new result. The elementary identity (D3), exact simplex, dimension lower bound, compact-encoding check and output-length example were fully verified here.

## 8. Translation into the existing dictionary

In the effective representation ring,
\[
[\operatorname{Sym}^{N}(\operatorname{Sym}^{k}\mathbf C^2)]
=\sum_{\nu}a^\nu_{(N),(k)}[S_\nu\mathbf C^2],
\]
and (D3) identifies one actual nonnegative coefficient. Under ordinary geometric or motivic Satake, the corresponding Schur summand is available with the purity properties already recorded in F20/F31. Neither the effective K0 identity nor that pure realization changes the numerical growth of its multiplicity.

The obstruction is therefore not a failure of positivity or purity. It is a precise bound on the dimension of a proposed counting model for the full stretching family. The effective Grothendieck class, the actual simplex and the degree lower bound are mutually compatible; only the asserted uniform polynomial bound in the compact bitlength fails.

