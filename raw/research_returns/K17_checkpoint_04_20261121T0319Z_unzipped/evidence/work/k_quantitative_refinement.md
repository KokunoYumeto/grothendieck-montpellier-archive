# K17 quantitative refinement: a seventh-power bound

Date: 2026-11-21 UTC. Agent: /root/vandiver_k. Model: GPT-6 Astra Pro. Effort: not exposed.

This is a mathematical reconstruction from the recovered source proof, together with standard highest-weight theory. It is not a claim that the proposition HeightAndVanishing/Counts.lean:CorG has been proved, nor a new compiled Lean declaration. The source's arithmetic and automorphic theorems are used under the parent's source contract.

## 1. Outcome (VK-EXP7)

The recovered argument can be sharpened to

\[
\exists C\in\mathbb N\quad\forall k\ge1,\qquad
\log|K_{4k}(\mathbb Z)|\le C(2k)^7
\le C(2k+1)^7.
\]

The exponent is explicit; the multiplicative constant remains an existential bound for cohomology at finitely many fixed arithmetic levels. No new numerical vanishing degree follows.

There is also a useful exact computation route (VK-TRACE-GCD). For each even \(e=2k>0\), construct the two nonzero trace-product integers \(n_7(e),n_{11}(e)\) described below. Then

\[
|K_{4k}(\mathbb Z)|\mid
\gcd\bigl(|n_7(e)|,|n_{11}(e)|\bigr)^2.
\]

The \(7\)- and \(11\)-primary parts already vanish, so either individual integer gives a divisibility bound as well. An exact gcd with no prime factor at least \(2^{31}\) would prove vanishing in that degree. This is an explicit finite computation target, not a computation completed here.

## 2. Source path and numerical exponents before improvement

All downloaded files have URLs, byte counts, and SHA-256 hashes in work/quantitative_sources/manifest.json. The source base is

https://raw.githubusercontent.com/CocoSgt/riemann-hypothesis-lean/main/src/Development/AutomorphicArithmetic/AutomorphicVarieties/.

Relevant paths and declarations:

1. AutomorphicForms/TemperedLocalComponents/WeylC.lean:weylC supplies, for a degree-\(d\) totally complex field and rank \(n\), coefficient-dimension exponent \(n^2d\).
2. AutomorphicForms/TemperedLocalComponents/CohBoundFree.lean:cohBound_of, cohBoundFree supplies level exponent \(dn^2\); before uniform coarsening its estimate is a constant times \(M^{dn^2}\dim\Xi\).
3. AutomorphicForms/TemperedLocalComponents/KlevThree.lean:cardK adds those two exponents.
4. GaloisLibrary/CrystallineBaseChange/KlevThree.lean:cardP does the same.
5. GaloisLibrary/CrystallineBaseChange/CountQuadraticOfHyp.lean:count_quadratic_of_hypotheses uses six imaginary quadratic fields for rank two and sums their exponents.
6. AutomorphicForms/TemperedLocalComponents/CongruenceNumberRankThree.lean:numberU3_of_admissible adds the rank-three and rank-two exponents, then adds one.

Following the displayed witnesses literally, rank three over an imaginary quadratic field gives \(18+18=36\); each rank-two field gives \(8+8=16\); the six-field sum gives \(96\); the final exponent is \(36+96+1=133\).

Two elementary improvements would already give \(37\): use the common exponent \(16\), instead of its sixfold sum, for the rational rank-two count; then use \(\max(36,16)+1=37\), instead of the sum plus one. The stronger argument below retains fixed levels and the exact coefficient dimensions.

## 3. The exact source weights

The source WeylC.lean uses zero-based indices and sets

\[
\nu_j=j+1+H-m_{n-1-j},\qquad N_{\rm det}=n+H.
\]

It constructs a polynomial representation of highest weight \(\nu\), then uses the determinant twist \(-N_{\rm det}\) at each complex embedding. These formulas are read directly in WeylC.lean and GaloisLibrary/WeylCharacterRegularity/ExistsTens.lean:exists_tens.

For the rank-three branch, FrobeniusTraceCountBoundOfCmEigensystemCount.lean uses

\[
n=3,\quad m=(e-1,-1,-e-1),\quad H=e+1.
\]

Thus

\[
\nu=(2e+3,e+4,5),\quad N_{\rm det}=e+4,\quad
\lambda=\nu-N_{\rm det}(1,1,1)=(e-1,0,1-e).
\]

For rank two, FrobeniusTraceCountBoundOfRatEigensystemCount.lean uses \(m=(e,-e)\), \(H=e\). Thus

\[
\nu=(2e+1,2),\quad N_{\rm det}=e+2,\quad
\lambda=(e-1,-e).
\]

The common determinant shifts have no effect on dimension.

### Why the exact dimensions apply to the implementation

GaloisLibrary/WeylAlgebraQuantumDet/ExistsScalar.lean:existsScalar obtains a nonzero highest-weight vector in a finite polynomial representation. Its call to Scalar.lean:scalar explicitly replaces that representation by

\[
S=\operatorname{span}_{\mathbb C}
\{\rho(y)v:y\in\operatorname{Mat}_n(\mathbb C)\}.
\]

This is the cyclic highest-weight module of weight \(\nu\). Here is the complete short justification that it is one irreducible \(L_\nu\), so that the crude polynomial-space dimension need not be retained. Finite-dimensional polynomial representations of \(\operatorname{GL}_n(\mathbb C)\) are completely reducible. Project \(v\) to the irreducible summands. Each nonzero projection is killed by the upper nilpotent algebra and has weight \(\nu\), so each such summand has highest weight \(\nu\). Consequently \(v\) lies in the highest-weight line tensored with a single vector in the multiplicity space, and its generated submodule is one copy of \(L_\nu\). The span using all matrices equals the span using invertible matrices: a linear functional annihilating the latter produces a polynomial in matrix entries that vanishes on the Zariski-dense invertible locus, hence on every matrix. This proves the required equality of spans and dimensions.

ExistsTens.lean:exists_tens gives an irreducible coefficient representation \(\Xi\) with

\[
\dim\Xi\le(\dim L_\nu)^{\#\operatorname{Hom}(F,\mathbb C)}.
\]

It preserves the required infinitesimal character and the determinant twist. This inequality is sufficient; no assertion about uniqueness from the quantum determinant alone is required.

Weyl's formula is

\[
\dim L_\nu=\prod_{0\le i<j<n}
\frac{\nu_i-\nu_j+j-i}{j-i}.
\]

In the rank-three case this is \(e\cdot e\cdot(2e/2)=e^3\), and in rank two it is \(2e\). Every field used here is imaginary quadratic, with two complex embeddings. Hence the usable coefficient bounds are

\[
\dim\Xi_3\le e^6,\qquad \dim\Xi_2\le4e^2.
\]

Primary background locators: Pavel Etingof, MIT 18.755 Spring 2024, Lecture 01, sections 27.2--27.3, printed pp.145--147, for highest-weight classification and determinant twists; Lecture 02, section 28.1, printed pp.151--152, for the displayed Weyl dimension formula. URLs:

- https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec01.pdf
- https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec02.pdf

Web refs: turn526954240view0, turn526954240view1. These standard representation theorems are cited, not reproved here; the cyclic-submodule application, source weight arithmetic, and dimension products are proved above.

## 4. Fixed levels, finite fields, and multiplicities

Fix \(K=\mathbb Q(\sqrt{-3})\), \(N=2\). The cardK proof bounds every finite set of pairwise nonisomorphic relevant cuspidal representations by total cohomology with coefficient \(\Xi_3\) at the subgroup KLev K 3 6. This is because it passes from level \(N\) to \(3N\). cohBoundFree therefore gives a fixed positive natural \(B_0\) such that this total cohomology is at most \(B_0\dim\Xi_3\), uniformly in \(e\); increase the witness to one if necessary.

For the rational rank-two branch the level is \(M=N|\operatorname{disc}K|=6\). Choose six fixed imaginary quadratic fields with pairwise coprime discriminants, as allowed in the quadFam argument; for example the fields of discriminants \(-3,-7,-11,-19,-23,-31\). At a prime \(p\), at most one of these discriminants is divisible by \(p\), leaving five fields. The source needs five because rank two has at most \(n^2=4\) distinct quadratic self-twists. Thus one of the five restrictions is irreducible, exactly as in CountQuadraticOfHyp.lean.

For each field choose a fixed positive natural \(B_i\) bounding total cohomology at KLev K_i 2 18 by \(B_i\dim\Xi_2\). The fields, ranks, and levels are fixed independently of \(e,p,\ell\). These constants exist by cohBoundFree. This is the precise remaining input that has not been numerically evaluated.

CountSys.lean:exists_eigData indexes whole eigenvalue systems, and its classification map identifies representations only up to isomorphism. The following count therefore keeps multiplicities needed by the trace norm; it does not replace systems by their distinct values at a single Frobenius.

The rank-three trace data have cardinality at most \(B_0e^6\). In rank two, RootSum.lean:rootSum takes at most \(2^n\) choices of roots of eigenvalues, and an extra Boolean factor for the two possible lifts, giving exactly \(2^{n+1}=8\). If \(I_p\) is the five-element subset avoiding \(p\), the resulting rational trace data have cardinality at most

\[
8\sum_{i\in I_p}B_i(4e^2)
\le32\left(\sum_{i=1}^6B_i\right)e^2.
\]

The trace conversions preserve the indexing cardinality (FrobeniusTraceCountBoundOfCmEigensystemCount.lean, FrobeniusTraceCountBoundOfRatEigensystemCount.lean). Taking their disjoint union therefore gives data \(D_{p,e}\) with

\[
\#D_{p,e}\le B_0e^6+
32\left(\sum_{i=1}^6B_i\right)e^2
\le D e^6,\qquad
D=B_0+32\sum_{i=1}^6B_i.
\]

The finite-index and multiplicity arguments are the existing source arguments, with their pointwise coefficient-dimension bounds retained before the uniform coarsenings. This does not require re-proving the automorphy or classification statements.

## 5. Trace products and the exponent seven

For a prime \(p\ge7\) with \(p\nmid6\), choose \(w\mid p\) in \(K\), write \(q=Nw=p^f\), \(1\le f\le2\), and use the trivial character orbit. The source has

\[
\operatorname{eis}_3(q,e,1)=q^{-e}+1+q^e.
\]

For the Galois-stable trace data \(t_s\) just counted,

\[
n_p(e)=\prod_{s\in D_{p,e}}
q^e\bigl(t_s-(q^{-e}+1+q^e)\bigr)
\quad\in\mathbb Z\setminus\{0\}.
\]

These are the integers constructed in FrobeniusTraceNormNonzeroLogBound.lean:frobenius_trace_norm_nonzero_log_bound. Each scaled factor is integral, their product is Galois invariant, and every factor is nonzero because \(|t_s|\le3\) while \(q^{-e}+1+q^e>3\).

The source proves

\[
\log|n_p(e)|\le\#D_{p,e}(2e\log q+1).
\]

Since \(q\le p^2\), \(e\ge1\), and \(\log p\ge1\),

\[
2e\log q+1\le 4e\log p+1
\le5e\log p,
\]

so

\[
\log|n_p(e)|\le5D e^7\log p.
\]

The unchanged OneChar/orbit argument gives

\[
\operatorname{length}_{\mathbb Z_\ell}\mathcal S_\ell(\mathbb Q,e)
\le2v_\ell(n_p(e))
\]

when \(\ell\ne p\), \(\ell\ge5\), and \((\ell-1)\nmid2e\). In the rational-field specialization, every other admissibility condition was checked in ClassNumberThree.lean:gd.

Use the already-proved negative-Selmer/K bridge and exception removal in vandiver_k.md, sections 4 and 9. The 2- and 3-primary parts vanish, all divisibility exceptions vanish, and the 7-primary part vanishes because 7 is regular. Consequently for \(e=2k\), **every** prime satisfies

\[
v_\ell(|K_{4k}(\mathbb Z)|)\le2v_\ell(n_7(e)).
\]

Thus \(|K_{4k}(\mathbb Z)|\mid|n_7(e)|^2\), and

\[
\log|K_{4k}(\mathbb Z)|
\le10D\log7\,(2k)^7<20D(2k)^7.
\]

This proves the claimed exponent-seven estimate, with the natural constant \(C=20D\). The second auxiliary prime is not needed for this inequality because its one missing primary part is already known to vanish. Taking \(p=11\) as well proves the gcd divisibility above, since the 11-primary part also vanishes. Here \(q_7=7\), while \(q_{11}=121\), because 7 splits and 11 is inert in \(\mathbb Q(\sqrt{-3})\).

## 6. Numerical limitation and a logical illustration

The source's original specialization chooses \(C=36c_5\,2^A\). If \(c_5\ge1\), then \(C\ge36>\log(2^{31})\), so the particular sufficient vanishing criterion \(C(2k+1)^A<\log(2^{31})\) can never hold. This observation does not prove that no sharper estimate or trace computation could succeed. The exponent-seven refinement still supplies no values of \(B_0,B_1,\ldots,B_6\), so it supplies no newly verified small degree.

The following illustrates only the logical weakness of an existential size estimate plus selected numerical patterns. Choose a prime \(q>2^{31}\), put \(m=(q-1)/2\), and define abstract groups

\[
M_k=
\begin{cases}
\mathbb Z/q,&k\equiv3\pmod m,\\
0,&\text{otherwise}.
\end{cases}
\]

They have no 2-primary or below-\(2^{31}\) primary parts; \(M_1=M_2=0\); their fixed-prime vanishing is periodic in the prescribed modulus; and \(\log|M_k|\le\lceil\log q\rceil(2k+1)^7\), yet \(M_3\ne0\). These are not arithmetic K-groups, not actual cyclotomic class data, and not a counterexample to Vandiver. They show that the specifically listed patterns and existential estimate alone cannot force \(K_{12}\)-type vanishing.

## 7. Current small-degree literature check

The current Cambridge publication is Dutour Sikirić--Elbaz-Vincent--Kupers--Martinet, JIMJ 25 (January 2026), 565--590, DOI 10.1017/S1474748025101394, online 24 November 2025. Its stated K-theory result is \(K_8(\mathbb Z)=0\). Official primary metadata was opened, not inferred from the old K-book.

Kupers's author note, dated 21 October 2019, was downloaded and read in full (work/references/KupersK8short.pdf, four pages). Remark 2.6, p.4, says that the Church--Farb--Putman conjecture with coefficients \(\mathbb Z[1/(n+1)!]\) would imply \(K_{12}=0\). The subsequent Brück--Miller--Patzt--Sroka--Wilson result, Adv. Math.451 (2024),109795, arXiv:2204.11967v3, proves the **rational codimension-two** case. It does not state the integral/higher-codimension conclusion needed by that route. An available primary Münster research poster by Brück--Sroka presents \(K_{12}=0\) as a research objective.

Targeted current primary-source searches did not locate a proof of \(K_{12}=0\) or \(K_{16}=0\). This is a report of the search outcome, not an exhaustive negative theorem about the entire literature. No new vanishing of either group is asserted.

Useful primary URLs:

- https://www.cambridge.org/core/journals/journal-of-the-institute-of-mathematics-of-jussieu/article/abs/voronoi-complexes-in-higher-dimensions-cohomology-of-glnmathbbz-for-ngeqslant-8-and-the-triviality-of-k8mathbbz/6C1E2AA4FA1AD29554384C091A51D8E5
- https://www.utsc.utoronto.ca/people/kupers/wp-content/uploads/sites/50/2021/01/k8zshorter.pdf
- https://arxiv.org/abs/2204.11967
- https://arxiv.org/html/2204.11967v3
- https://www.uni-muenster.de/imperia/md/content/MathematicsMuenster/research/poster_yrg_brueck-sroka.pdf

Web refs: turn411713733view0, turn488751294view1, turn411713733view1, turn488751294view0, turn411713733view2.

## 8. Check record and scope

The whole coefficient/count/norm/K derivation above was read after writing. All quantifiers fixing fields and levels, the rank-two factor eight, indexing multiplicities, auxiliary-prime exclusions, and unchanged local arithmetic hypotheses were checked. The constants were explicitly chosen positive to justify the displayed strict final inequality. All source files named in sections 2--5 and the complete Scalar.lean, ExistsScalar.lean, ExistsTens.lean, RootSum.lean, CountQuadraticOfHyp.lean, and CohBoundFree.lean were read. No new compiler run and no numerical computation of automorphic spaces is claimed.
