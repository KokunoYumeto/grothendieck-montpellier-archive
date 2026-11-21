# Exact integral K-theory consequences and the remaining Alpöge export

Run: `/root/source_and_masullo`, within `ALPOGE_BRIDGES`. Model: GPT-6 Astra Pro. Effort: not exposed. Source reading and complete draft proof reading completed on 2026-11-21 Europe/Berlin; clock 2026-11-20 23:54:57 UTC. The complete statements and proofs are in `source_K_bridge.tex`.

## 1. Main mathematical result

For every odd prime \(p\) and integer \(n\geq1\), there is an isomorphism of finite-dimensional vector spaces over \(\mathbb F_p\):

\[
K_{2n}(\mathbb Z)/p\cong
H^2_{\mathrm{\acute et}}(\mathbb Z[1/p],\mu_p^{\otimes(n+1)})
\cong (C_p/pC_p)(\omega^{-n}),
\]

where \(C_p\) is the \(p\)-primary part of the class group of 

\[
\mathbb Q(\zeta_p),\qquad
\omega:\operatorname{Gal}(\mathbb Q(\zeta_p)/\mathbb Q)\longrightarrow\mathbb Z_p^\times
\]

is the Teichmüller character. Consequently

\[
K_{2n}(\mathbb Z)\{p\}=0
\quad\Longleftrightarrow\quad C_p(\omega^{-n})=0.
\]

F-SM-14 states this precisely and proves the class-group specialization. The first isomorphism is an established comparison theorem, read directly in Weibel, Chapter VI, Corollary 8.3, chapter p. 48; its proof refers to Theorem 8.2, chapter p. 47. This is a comparison of reductions modulo \(p\), with a consequent vanishing criterion. It does not assert an isomorphism of the complete finite \(p\)-primary groups.

The specialization is explicit. Set \(R=\mathbb Z[\zeta_p,1/p]\). Its finite étale Galois cover of \(\mathbb Z[1/p]\) has group of order (p-1), so taking invariants in mod-\(p\) cohomology is exact. The Kummer sequence identifies \(H^2(R,\mu_p)\) with \(\operatorname{Pic}(R)/p\), since the Brauer group vanishes: there is only one prime over \(p\), and the field has no real places. That prime is principal, so localization leaves the class group unchanged. The remaining coefficient twist has character \(\omega^n\), making the invariant space exactly the class-group component of character \(\omega^{-n}\). Finally, a finite \(p\)-group is zero precisely when its reduction modulo \(p\) is zero.

No complex zero-location theorem enters this comparison.

## 2. A complete existing integral vanishing

Dutour Sikirić, Elbaz-Vincent, Kupers, and Martinet prove \(K_8(\mathbb Z)=0\) in Theorem 6.4, p. 19 of their updated author manuscript. Their Corollary 7.1, p. 20, gives

\[
C_p(\omega^{p-5})=0\qquad(p>3).
\]

The journal article is in *Journal of the Institute of Mathematics of Jussieu, 25*(1), 565–590, with online publication on November 24, 2025 and a January 2026 issue. The result was announced earlier; it is not an outcome first obtained by the present use of Alpöge.

The final deduction of \(K_8=0\) uses these precise inputs:

| Input | Exact consequence |
|---|---|
| DEKM Proposition 6.1, author p. 18 | \(H_9(BQ;\mathbb Z)\) is zero modulo the Serre class of finite groups supported at primes at most 7. |
| DEKM Proposition 6.3, author p. 19 | The kernel of \(\pi_9(BQ)\to H_9(BQ;\mathbb Z)\) is supported at primes at most 5. |
| \(K_8(\mathbb Z)=\pi_9(BQ)\) | \(K_8\) can have torsion only at (2,3,5,7). |
| Weibel VI, Proposition 10.5, chapter p. 63 | An odd regular prime divides no positive even (K)-group of \(\mathbb Z\). This removes \(3,5,7\). |
| Weibel VI, Corollary 9.8, chapter p. 55 | \(K_8(\mathbb Z)\{2\}=0\). |

The final prime-two input is not stated in the very short updated manuscript proof of Theorem 6.4; it supplies that omitted step. The small odd primes are regular: their relevant Bernoulli numerators are those of \(B_2=1/6\) and \(B_4=-1/30\). The Voronoi enumerations and integral homology calculations underlying Proposition 6.1 remain published computational inputs; they were not rerun here.

F-SM-14 with \(n=4\) gives the class-group consequence because 

\[
-4\equiv p-5\pmod{p-1}.
\]

This route also corrects two imprecisions in the explanatory prose of DEKM §7 without disputing the stated \(K_8\) theorem. An uncompleted finitely generated integral (K)-group cannot surject onto a positive-rank \(\mathbb Z_p\)-module; the comparison in such odd degrees uses \(p\)-adic coefficients or completion. Also, the blanket claim \(H^1_{\mathrm{\acute et}}(\mathbb Z[1/p],\mathbb Z_p(j))=0\) for (p>j+1) needs a positive even twist in the range under discussion. For odd (j>1), that group has rank one over \(\mathbb Z_p\), as the exact formula in Weibel VI, Exercise 8.3, chapter p. 50, shows. The mod-\(p\), degree-two comparison above avoids both problems.

## 3. Density-one partial regularity gives two explicit degree families

Chen et al. (2026), arXiv:2602.05090v1, Theorem 1.1, p. 2, prove that for each \(\alpha>1/2\), with

\[
M_\alpha(p)=\left\lfloor\frac{\sqrt p}{(\log p)^\alpha}\right\rfloor,
\]

all but \(O_\alpha(X/(\log X)^{2\alpha})\) primes \(p\leq X\) avoid divisibility of the numerator of every \(B_{2k}\) in the range

\[
2\leq2k\leq\min\{M_\alpha(p),p-3\}.
\]

The Herbrand–Ribet statement on p. 3, equation (4), gives vanishing of \(C_p(\omega^{1-2k})\). Leopoldt reflection, in the direction stated immediately before Corollary 1.4, then gives vanishing of \(C_p(\omega^{2k})\). This implication uses only the direction

\[
C_p(\omega^{2k})\ne0\ \Longrightarrow\ C_p(\omega^{1-2k})\ne0;
\]

there is no inference of a converse.

F-SM-15 proves the following precise consequence. For the same nonexceptional primes, the following hold simultaneously for every \(k\) in that range and every integer \(b\geq0\):

\[
K_{4k-2+2b(p-1)}(\mathbb Z)\{p\}=0,
\qquad
K_{2p-2-4k+2b(p-1)}(\mathbb Z)\{p\}=0.
\]

The proof substitutes (n=2k-1+b(p-1)) and (n=p-1-2k+b(p-1)), respectively, in F-SM-14. The second is at least 2 because \(2k\leq p-3\). The first family lies in degrees congruent to 2 modulo 4. The second lies in degrees divisible by 4; it is the explicit (K)-theoretic consequence of the partial Vandiver components. The same exceptional set controls every \(b\); no union over new exceptional sets is taken. Dividing its bound by \(\pi(X)\sim X/\log X\) gives density one since \(1-2\alpha<0\).

The first family with \(b=0\) is already Chen et al., Corollary 1.7(4), p. 5. The second displayed family makes the reflected consequence fully explicit. No historical novelty claim is made for this short deduction. These assertions concern \(p\)-primary subgroups. They do not assert that an entire (K)-group vanishes integrally at all primes, nor that every prime is regular.

The paper's natural-language proof of its main quantitative theorem was read throughout §§2–3, pp. 6–10. Its proof uses bounds for Bernoulli numerators, products of these numerators, the number of distinct prime divisors, and the prime number theorem. The supplied paper reports a Lean formalization of that elementary estimate in §4, pp. 10–11; this run did not compile that repository. The paper itself distinguishes its formalized elementary theorem from its cited deep arithmetic consequences. Its p. 5 reference to “Chapter 18” of Weibel does not supply a valid chapter locator for the six-chapter book; the exact usable locators are VI.8 and VI.10 above.

## 4. Degree one and the exact remaining export gate

F-SM-16 gives the elementary complete proof

\[
K_1(\mathbb Z)=\operatorname{GL}_\infty(\mathbb Z)^{\mathrm{ab}}
\cong\mathbb Z^\times=\{\pm1\}.
\]

Euclidean row and column reduction generates the determinant-one subgroup by elementary matrices. In stable size each elementary matrix is a commutator, \(e_{ij}(a)=[e_{ir}(a),e_{rj}(1)]\), so the determinant gives the abelianization. The exact standard source is Weibel III, Example 1.3.5, chapter p. 4, following Whitehead's Lemma 1.3.3.

This nonzero integral group rules out a blanket interpretation of Alpöge's tentative final footnote as vanishing of all positive-degree integral (K)-groups. A useful export of that analytic method would instead specify:

1. The degree set and whether the assertion concerns an integral group, its rationalization, a finite quotient, or a \(p\)-primary subgroup.
2. The prime range and class-group character, or an equally precise arithmetic object.
3. The actual comparison map and the theorem showing that the analytic construction controls its source or target.

An exported statement \(C_p(\omega^{-n})=0\) would feed directly into the proven vanishing criterion F-SM-14. To obtain full integral vanishing of a finite even (K)-group, one must cover every prime and account separately for (2). The five supplied Alpöge declarations identify complex zero locations and nonvanishing regions; they do not themselves provide this integral eigenspace or divisibility export. This is a precise missing step, not a rejection of the adopted analytic input.

## 5. Primary references and source-reading record

Chen, E., et al. (2026). *Almost all primes are partially regular* (arXiv:2602.05090v1). https://arxiv.org/abs/2602.05090 . Submitted February 4, 2026. Direct HTML: https://arxiv.org/html/2602.05090v1 . Primary retrieval refs: `turn547806336view0`, `turn810397964view0`. Exact used locators: Theorem 1.1, p. 2; equation (4), reflection statement and Corollary 1.4, p. 3; Corollary 1.7(4), p. 5; main theorem proof §§2–3, pp. 6–10; formalization scope §4, pp. 10–11. Authors' formal archive: https://github.com/AxiomMath/partial-regularity (not compiled in this run).

Dutour Sikirić, M., Elbaz-Vincent, P., Kupers, A., & Martinet, J. (2026). Voronoi complexes in higher dimensions, cohomology of \(\mathrm{GL}_N(\mathbb Z)\) for \(N\geq8\) and the triviality of \(K_8(\mathbb Z)\). *Journal of the Institute of Mathematics of Jussieu, 25*(1), 565–590. https://doi.org/10.1017/S1474748025101394 . Updated author PDF: https://jamartin.perso.math.cnrs.fr/Publications/DEKM.pdf . Primary publisher refs: `turn547806336view1`, `turn810397964view1`, `turn810397964view4`; author page `turn860608882view1`; updated PDF `turn255194608view0`. Exact used locators: Proposition 6.1, author p. 18; Proposition 6.3 and Theorem 6.4, author p. 19; Corollary 7.1 and the explanatory cohomology statements, author p. 20. These final deductions were read completely; the upstream computer calculations were not reproduced.

Weibel, C. A. (2013). *The K-book: An introduction to algebraic K-theory* (Graduate Studies in Mathematics, Vol. 145). American Mathematical Society. https://doi.org/10.1090/gsm/145 . Author page: https://sites.math.rutgers.edu/~weibel/Kbook.html . Chapter III: https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.III.pdf . Chapter VI: https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.VI.pdf . Primary refs: `turn833600216search1`, `turn833600216search3`, `turn564553513view0`, `turn564553513view1`. The author page notes that online chapter pagination differs from the printed book while theorem numbering is unchanged. All page locators in this note refer to the chapter PDFs. Relevant statements and their adjacent proofs were read directly; foundational motivic comparison theorems were used as established mathematics, not independently reproved.

The private downloaded book chapters and their full text extractions are working references, not deliverable source reproductions. The final package should contain the original proofs, bibliographic information, exact locators, and short necessary paraphrases, rather than complete copyrighted book chapters.

## 6. Check classification

The proofs of F-SM-14, F-SM-15, and F-SM-16 were each read in their entirety after drafting and checked against the indicated primary theorem statements. These are complete drafter self-checks of the written deductions, with explicitly carried comparison inputs. No independent re-proof of the Quillen–Lichtenbaum theorem, Herbrand–Ribet, reflection, or the Voronoi computations is claimed. No formal kernel verification was performed. Parent independently read all three complete proofs and the exact Weibel VI.8.3, VI.9.8, VI.10.5 and Chen Theorem 1.1 / Corollaries 1.4 and 1.7 inputs; all passed, reported 2026-11-21 00:02:03 UTC. This is a separately logged whole-proof reading, not an independent re-proof or kernel verification. The check ledger is `source_and_masullo_checks.tsv`.
