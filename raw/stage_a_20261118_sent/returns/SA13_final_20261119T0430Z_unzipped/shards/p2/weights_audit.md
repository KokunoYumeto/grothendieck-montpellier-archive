# Independent audit of K34-12, scans 201, 203, 205, 207 and 209

Reviewer: GPT-6 Astra Pro; configured effort not exposed; SA13 part 2/p2. Audit completed 2026-11-19. This supplements the root-owned claims C-SA13-654–663; it creates no additional Pro verdicts and does not rewrite the root's shard. The complete supplied K34-12 transcription, global lines 1–377, was read, including the intervening reused GIT pages. The findings below concern the five mathematical leaves requested for this audit.

## Findings requiring assembly action

1. **C-SA13-654–660:** the root's reconstructed statements agree with the independent calculation. Keep the distinct E2 and E3 degeneration pages. Add the nonzero differential example below to make the distinction concrete.
2. **C-SA13-661:** specify geometric special-fibre cohomology and the maximal unramified generic fibre. A literal (H^p(X_s,-)) over the finite residue field also includes its Galois cohomology and cannot be assigned the displayed geometric weights without that convention. The corresponding abutment is (H^i(X_{K^{nr}},\mathbf Q_\ell)). Geometric nearby cycles instead abut to (H^i(X_{\bar K},\mathbf Q_\ell)).
3. **C-SA13-662–663 / scan209:** record a further substantive reading alarm in the displayed exact sequence: the coinvariant term needs a Tate twist ((-1)), and the middle term is over (K^{nr}), not over (K) or \(\bar K\). The correct formula is displayed below. This is independent of the false purity assertion already recorded in C-SA13-663.
4. **C-SA13-655,662:** add van Dobben de Bruyn's 2020 theorem as the precise later result connecting the standard-conjecture/rank program to general independence of \(\ell\). It proves an equivalence of conjectures, not the unconditional independence claim. Wan–Zhang §1.1 provides a recent primary-source check that general compact-support Betti independence remains open.
5. **Scan205 diagram:** the source's two dimensions are consistent if \(\dim X'=n-1\). Do not silently impose \(\dim X'=n\) and declare an off-by-one error. In that convention the lower-left exponent must be \(2n-2-p-2q\), and the target intersection has \(q-1\) components. These are constrained alternatives to recheck against the scan, not emendations of the supplied transcription.

## 1. Proper normal-crossing variety: E2 degeneration

Source: `codex/K34-12_transcription.tex`, scan201, global lines57–74, especially the surviving words “(E_2^{pq}\) est de poids (q)” and “(d_r^{pq}\) est nulle pour tout (r).” Here “all” means the differentials on and after the displayed E2 page.

Use the modern finite-field setting explicitly: all cohomology is geometric, all maps are Frobenius-equivariant, \(\ell\) differs from the characteristic, and every component intersection is smooth projective. The augmented closed-cover Čech complex gives
\[
E_1^{p,q}=\bigoplus_{\alpha_0<\cdots<\alpha_p}H^q(Y_{\alpha_0\cdots\alpha_p},\mathbf Q_\ell)
\Longrightarrow H^{p+q}(Y,\mathbf Q_\ell).
\]
Each E1 term has weight q. Taking the kernel and quotient for d1 preserves this weight, so E2 has weight q. For (d_r:E_r^{p,q}\to E_r^{p+r,q-r+1}\), the two weights differ by (1-r); therefore d_r vanishes for r≥2. No Frobenius semisimplicity is needed: disjoint generalized eigenvalue sets suffice. Thus the possible weights of H^i are 0 through i. This proves degeneration, not independence of ranks of d1 as \(\ell\) varies.

For the compactification sequence on scan201 lines78–97 and scan203 lines119–128, set \(\varphi^i:H^i(X')\to H^i(Y)\). Exactness and the disjoint weight ranges give
\[
\ker[H_c^i(U)\to H^i(X')]=W_{i-1}H_c^i(U),\quad
\ker\varphi^i\simeq \operatorname{Gr}_i^W H_c^i(U),\quad
\operatorname{coker}\varphi^i\simeq W_iH_c^{i+1}(U).
\]
These identifications explain the claimed independence of compactification. The surviving (H^i(X)) in scan203 lines122–123 has to be checked against the original: the preceding definition of \(\varphi^i\) has domain \(H^i(X')\).

## 2. Local cohomology and the open-complement Leray sequence: E3

Source: scan203 lines130–153, scan205 lines198–234. For (j:U=X'\setminus Y\hookrightarrow X'\), regular ambient scheme and strict normal-crossing divisor, localization and purity identify
\[
\mathcal H_Y^q(\mathbf Q_\ell)=R^{q-1}j_*\mathbf Q_\ell
=\bigoplus_{|J|=q-1}\mathbf Q_{\ell,Y_J}(-(q-1))\qquad(q\ge2),
\]
and the local cohomology sheaves vanish for q<2. The equality here implicitly includes extension by zero along each closed stratum. The last twist ((-1)) in line141 disagrees with the preceding exterior power when q>2; the next displayed E2 term, line147, already has the correct twist (-(q-1)).

For the local-to-global support sequence E2 has weight (p+2q-2). For the ordinary open-complement Leray sequence it has weight (p+2q). In either case the target-minus-source weight of d_r is (2-r). Thus d2 is allowed and all d_r for r≥3 vanish.

An explicit nonzero d2 occurs for (\mathbf G_m\subset\mathbf P^1\), with boundary the two rational points 0 and infinity. Its relevant terms are
\[
d_2:\mathbf Q_\ell(-1)^2\longrightarrow\mathbf Q_\ell(-1),\qquad (a,b)\longmapsto a+b.
\]
This is the Gysin sum of the two point classes, of rank1. E3 has a one-dimensional surviving H1 term and no H2 term, as required for \(\mathbf G_m\). Replacing E3 by E2 would predict the wrong dimensions. A reindexed standard weight spectral sequence can start at E1 and degenerate at E2; that convention does not change the manuscript's Leray-page calculation.

The Poincaré duality diagram on205 can be tested without guessing n. Write (d=\dim X'\); then (\dim Y_J=d-|J|\), and
\[
[H^p(Y_J)(-q)]^\vee=H^{2d-2q-p}(Y_J)(d),\qquad |J|=q.
\]
For the d2 target with (|J|=q-1) and degree p+2, its dual degree is again (2d-2q-p\), with the same twist d. Substituting the source's d=n−1 selects the minus sign in the doubtful exponent and q−1 in the target index. These constraints do not prove what the ink says.

## 3. Arithmetic complement and geometric nearby cycles are different

Source: scan207 lines258–309. At a strict local crossing with r branches the arithmetic complement has r independent divisor Kummer classes:
\[
(R^qj_*\mathbf Q_\ell)_{\bar x}\simeq \bigwedge^q\mathbf Q_\ell(-1)^r.
\]
For a reduced semistable special fibre, geometric nearby cycles instead have the diagonal relation:
\[
(R^q\Psi\mathbf Q_\ell)_{\bar x}\simeq
\bigwedge^q\bigl(\mathbf Q_\ell^r/\mathbf Q_\ell(1,\ldots,1)\bigr)(-q).
\]
The ranks are \(\binom rq\) and \(\binom{r-1}q\), respectively. Already r=1 distinguishes them: the arithmetic puncture has nonzero H1, while smooth geometric nearby cycles have no positive-degree cohomology. The relation kills the Kummer class of the base uniformizer. With multiplicities the corresponding relation uses those multiplicities and can introduce a component permutation in degree0; the reduced semistable hypothesis matters.

This distinction was collated directly in the original SGA7 I, printed pp10–11: (3.1.2) computes the complement and Theorem3.3 uses the multiplicity complex. Illusie1994, (3.1.2–3) and Theorem3.2(b,c), printed pp34–35, gives both constructions and their relation by derived Galois invariants. These are exact primary locators, not a source-title identification.

After base change to the strict henselization of a trait with finite residue field, the q≥1 terms in the arithmetic-complement sequence have geometric weights p+2q; the q=0 row has weights≤p. A differential landing in q=0 has r=q+1. Its target weights are at most p+q+1, less than p+2q when q>1. Thus r≥3 also vanishes at the boundary row. The terminal filtration uses **E3**, and its first term can retain weights below i. The list of E2 terms at lines300–306 and the deletion of “≤” are not justified by this argument.

## 4. The exact sequence on209 and the Tate-curve counterexample

Source: scan209 lines338–358, especially lines345–348 and354. Let \(I=\operatorname{Gal}(\bar K/K^{nr})\), and write (V^j=H^j(X_{\bar K},\mathbf Q_\ell)\). For \(\ell\ne p\), the Hochschild–Serre sequence gives
\[
0\longrightarrow H^1(I,V^{i-1})\longrightarrow
H^i(X_{K^{nr}},\mathbf Q_\ell)\longrightarrow (V^i)^I\longrightarrow0.
\]
The tame-inertia calculation, with the finite prime-to-\(\ell\) parts first removed by exact averaging, identifies (H^1(I,V)\) with (V_I(-1)\), Frobenius-equivariantly. The twist cannot be dropped: even V=\(\mathbf Q_\ell\) has (H^1(I,V)=\operatorname{Hom}_{cts}(\mathbf Z_\ell(1),\mathbf Q_\ell)=\mathbf Q_\ell(-1)\). Thus the displayed middle field and twist require separate repair before the induction can be assessed.

For a concrete counterexample to the claimed purity, choose a split Tate elliptic curve (E_a/K\) with parameter a a uniformizer and finite residue field of cardinality Q. Tate uniformization gives
\[
0\to\mathbf Z_\ell(1)\to T_\ell(E_a)\to\mathbf Z_\ell\to0.
\]
The extension is nonzero on inertia: adjoining an \(\ell^n\)-th root of a uniformizer has ramification index \(\ell^n\), so the tame Kummer cocycle has infinite image. Dualizing gives H1 with a trivial subspace and quotient \(\mathbf Q_\ell(-1)\). Therefore
\[
H^1(E_{\bar K})^I=\mathbf Q_\ell\quad(\text{weight }0),\qquad
H^1(E_{\bar K})_I=\mathbf Q_\ell(-1)\quad(\text{weight }2).
\]
In a suitable rational basis the geometric Frobenius and monodromy matrices are (F=\operatorname{diag}(1,Q)\), (N=\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)\); then (FNF^{-1}=Q^{-1}N\). Choosing the Tate parameter with valuation at least2 gives a split polygonal semistable fibre, if that explicit normal-crossing model is desired. Invariants and coinvariants are not pure of weight i=1. This does not contradict weight–monodromy: its monodromy-graded weights are 0 and2, centered at1.

For the uniformization input and the torsion representation, the author-hosted Siksek2025 course notes §9, Theorem9 and Corollary9.1, printed pp11–12, were opened and read. The extension, ramification, dualization and weight conclusions above were independently derived. The notes explicitly describe themselves as rough; no chronology or original-priority claim is based on them.

## 5. Published fate and present limits

Van Dobben de Bruyn2020, Theorem1 (p3), proves the equivalence over \(\overline{\mathbf F}_p\) of independence of kernels of cycle-class maps on smooth projective varieties, ranks of algebraic correspondences, compact-support Betti numbers of all separated finite-type schemes, and those of smooth quasiprojective schemes. His introduction pp2–3 discusses exactly the proper Čech/weight degeneration and missing rank step seen here. This establishes a precise later formulation of the conditional program. It does not settle any of the equivalent conjectures. First arXiv submission:2018-08-01; published2020, article16, DOI10.46298/epiga.2020.volume4.5570. [Primary paper](https://epiga.episciences.org/6931/pdf); [submission record](https://arxiv.org/abs/1808.00119).

Wan–Zhang, *Betti number bounds for varieties and exponential sums*, author version §1.1 p2, explicitly retains general compact-support Betti independence as open for singular or nonproper varieties. The arXiv record begins2025-01-22. The publisher search result gives a2026 article, but its page returned403; that publication detail is not used as a verified exact locator. [Author PDF](https://zhangdingxin.gitlab.io/math/pdf/betti.pdf); [arXiv record](https://arxiv.org/abs/2501.12623).

For geometric weight–monodromy, Tetsushi Ito's Theorem1.1 in arXiv:math/0308141 distinguishes E2 degeneration of the Rapoport–Zink sequence, valid in any characteristic, from the monodromy isomorphisms, proved there in equal characteristic. The first version was submitted2003-08-14; the retrieved version is v2,2005-01-26. The PDF's automated2024 date is not its circulation date. [Paper](https://arxiv.org/pdf/math/0308141); [version history](https://arxiv.org/abs/math/0308141).

The October6,2026 Ito–Zou author preprint proves all-degree weight–monodromy for hyper-Kähler varieties over p-adic fields (TheoremB/4.4), including the p-adic realization. Its scope does not settle the general claim, and cannot rescue the invariant/coinvariant purity error. [Author text](https://www.math.uni-bielefeld.de/~hzou/papers/semisimplicity/).

The symbolic checks in `code/check_weights.py` and `outputs/weights_computations.json` verify the weight differences, the nonzero Gysin matrix, the local rank distinction, the duality exponents, and the Tate representation. They certify the displayed algebra; they are not proofs of Weil purity, absolute purity, Tate uniformization or existence of a general semistable model.
