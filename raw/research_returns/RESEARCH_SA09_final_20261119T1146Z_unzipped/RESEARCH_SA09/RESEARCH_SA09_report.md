| Item | Outcome | Complete answer and paper statements |
|---|---|---|
| A.1 | **Proved corrected relation; printed identification and bare equivalence refuted.** | Polynomial laws, the divided-power Hom category, and its representations are distinguished. The module Hom-law holds over every commutative ring; explicit mixed-degree coherence repairs the abstract equivalence. **A1.1–A1.9.** |
| A.2 | **Proved complete essential-image criteria; L3 refuted for the manuscript's source.** | All-ring matrix kernels, PID reduction, ordinary/admissible/exact variants, and the correct two-sided Frobenius replacement. **A2.1–A2.6.** |
| A.3 | **Proved for the full natural Γ-action requested on scan 38.** | That action is constructed and recovers the cosimplicial function ring and integral homotopy type. The cohomology-only weakening is refuted. **A3.1–A3.5.** |
| A.4 | **Proved strengthened correction; original equivalence refuted both ways.** | Uniform polynomial fibre ranks characterize actual bounded normalization over every ring with finite terms. Derived perfection has separate regular and nonregular criteria. **A4.1–A4.6.** |
| B.1 | **Proved complete orbit formula and exact equality criterion.** | Pinned counts depend on the induced cell-permutation image; rigidity concerns its kernel. Torus counterexample and all connected nontrivial kernels determined. **B1.1–B1.3.** |
| B.2 | **Proved all functions, fields, and Galois action; raw-polynomial description corrected.** | Three explicit sextic Belyi maps, complete enumeration, effective cubic, collision factor, and doubtful signs. **B2.1–B2.5.** |
| B.3 | **Proved complete compact clean classification.** | Real groups for I–III and all oranges; positive-genus cellwise \(C_2\) exceptions; separate function-uniqueness classification. Noncompact extension has explicit hypotheses. **B3.1–B3.4.** |
| B.4 | **Proved exact images and indices at every level.** | Rank-one torsors, each full Fermat fibre, and adelic openness for independent number-field elements with scalar linear part. **B4.1–B4.4.** |
| L1 | **Refuted as written; correct relation proved.** | \(\operatorname{Hom}(\Gamma^dV,W)\) differs from \(\Gamma^d\operatorname{Hom}(V,W)\); the latter defines the category represented by strict polynomial functors. **A1.3–A1.4.** |
| L2 | **Proved in its full natural test-functor meaning.** | All \(\rho_{p,M}\) reconstruct multiplication through cross effects and recover the function algebra. Ambient Γ-functors alone do not supply that action. **A3.1–A3.3; weaker alternatives refuted in A3.4–A3.5.** |
| L3 | **Refuted for the actual nonnegative category.** | Bottom stalk projective but not injective. Integer-graded enlargement Frobenius, stable category \(K^b(\mathrm{free})\). **A2.1, A2.6.** |
| L4 | **Proved for the literal rank-one assertion.** | \(K(2)\) and \(K(1/2)\) have index two exactly at levels divisible by eight. Full rank-two fibre has scalar affine index \(Nd_N\). **B4.1–B4.3.** |
| L5 | **Proved with polynomial identification corrected.** | One \(S_3\) orbit and cubic moduli fields. Defining cubic \(p\) is a factor of raw quintic \(P=-\delta p/7776\). **B2.1, B2.4–B2.5.** |

# RESEARCH_SA09: final research report

**AI-produced by GPT-6 Astra, OpenAI, ChatGPT Pro mode, 19 November 2026.** We claim no priority. The complete numbered proofs are in RESEARCH_SA09_paper.tex and its sections; RESEARCH_SA09_results.csv records every numbered statement, and CHECK_EVENTS.tsv records the actual kinds of checks. The table reports completed mathematical outcomes, including refutations and proved replacements. Hypotheses remain explicit wherever the answer changes with the ring, target category, additional structure, or ambient Galois group.

The supplied study, transcriptions, leads, and earlier check events were treated as claims to verify where used. Earlier approval was not a substitute for proof. We did not certify handwriting from a transcription. The supplied ZIP's unpacked version governs. We did not directly consult Michel Hua's project; the supplied study credits that project and the Pro notes for the torus counterexample. We preserve that attribution and give our own complete proof and certificate.

## 1. Central findings and scope

### A.1. The main question

Over any commutative ring \(k\), homogeneous polynomial laws are represented by
\[
\operatorname{Pol}^d_k(V,W)=\operatorname{Hom}_k(\Gamma^dV,W).
\]
A law includes its natural values after every commutative scalar extension, not just a function on \(k\)-points. The divided-power category used for strict polynomial functors instead has morphisms \(\Gamma^d\operatorname{Hom}_k(V,W)\); its linear representations are the strict polynomial functors. For \(k=\mathbf F_2\), \(V=k\), \(W=k^2\), \(d=2\), these Hom modules have dimensions two and three and cardinalities four and eight. This finite counterexample refutes L1's identification. Furthermore, two degree-\(d\) laws compose in degree \(d^2\), so the homogeneous piece for \(d>1\) is not itself a category with degree-one identities. The correct bridge is a polynomial-law action on the **linear Hom modules**, compatible with identities and composition as laws. [A1.1–A1.3.]

The closing module question has an affirmative answer for **all** modules: \(f\mapsto\Gamma^p(f)\) is a canonical homogeneous degree-\(p\) polynomial law. Its coefficient formula uses divided-power multiplication and diagonal comultiplication. Independence of a tensor presentation is proved directly, without assuming that scalar extension commutes with Hom. Degree zero, torsion, and nonflat modules are included. [A1.4.]

The printed abstract equivalence needs more than homogeneous associativity. Exterior powers in characteristic two, with substitution by unordered block partitions, satisfy the other bare axioms while \(\Lambda^2(k)=0\); this proves independence of the missing unit isomorphism. A scalar twist of ordinary divided powers over \(\mathbf F_3\) satisfies the homogeneous associative and unit-isomorphism axioms but contradicts the prescribed mixed constant/tensor-unit comparison. Thus the full bare equivalence is false. A further internally graded characteristic-two example shows that abstract natural polynomial enrichment on Hom modules is not automatic. [A1.5–A1.6, A1.8.]

The exact repair in A1.7 defines every component of \(D_{d,m}:B_{dm}X\to B_dB_mX\), where \(B_mX=\bigoplus_{i=0}^mG^iX\). It imposes finite counit, coassociativity, and bound-projection diagrams, preservation of the full expanded multigrading, and a **whole-map normalization** for repeated inner degrees. That normalization gives the identity on the intended multidegree and zero on every other one. Finite co-Kleisli composition then has exactly the desired strict representing objects; conversely a strict polynomial category supplies these diagrams. This is a necessary-and-sufficient criterion, without an unproved minimality assertion. Independent review exposed and repaired the repeated-degree step before acceptance of the final proof.

The grading remains actual data. A1.9 computes the exact annihilator of ambiguity between scalar weights, including valuations and degree zero. Inverting relevant primes is sufficient, not necessary: torsion-free coefficient groups already separate weights. Requiring the identities after all scalar extensions separates weights integrally using the indeterminate \(t\).

### A.2 and A.4. Exactness and perfection

The source actually written is the category of bounded **nonnegative** finite-free complexes. Its bottom stalk is projective and not injective over every nonzero ring, so it is not Frobenius. Its restriction theorem is nevertheless fully faithful. An explicit disk copresentation proves that a target cochain complex \(C\) extends as an ordinary relatively left-exact functor precisely when, for every bounded finite-free chain complex \(L\), the kernel
\[
T_C(L)=\ker\left[(x_i)\longmapsto
(d^ix_i-\partial_{i+1}x_{i+1})_i\right]
\]
exists. The source and target are the finite copowers \(\bigoplus_iL_i\otimes C^i\) and \(\bigoplus_iL_i\otimes C^{i+1}\). This is the answer over **every** commutative ring, including principal ideal rings with zero divisors. Over a PID it reduces to \(\ker d^i\) and kernels of \((x,y)\mapsto(d^ix-ay,d^{i+1}y)\) for nonzero nonunits \(a\). The finite \(\mathbf Z/4\) example proves that \(\ker d^i\) alone is insufficient. [A2.1–A2.3.]

We resolve “Σ-kernel” in both ordinary and admissible senses. Exact functors into a Quillen exact category correspond to admissible nonnegative resolutions. The weaker printed Sex1–2 axioms are insufficient: a finite-abelian-group example has the permitted resolution but its forced pullback extension has middle exponent eight, whereas the permitted middle groups have exponent four or sixteen. A2.4 supplies the exact and strong-left-exact replacements and states the weak-idempotent-completeness hypothesis for the shorter test. The integer-graded enlargement is Frobenius with stable category \(K^b(\operatorname{Free}_{\rm fg}R)\) over every commutative ring. [A2.4–A2.6.]

For simplicial modules with finite levels, uniformly bounded eventual polynomial degrees of residue-field dimensions characterize **actual bounded normalization** over every ring:
\[
\dim_{\kappa(\mathfrak p)}(L_n\otimes\kappa(\mathfrak p))
=\sum_i\binom ni
\dim_{\kappa(\mathfrak p)}(N_iL\otimes\kappa(\mathfrak p)).
\]
Nonnegative coefficients and Nakayama prove the converse; maximal ideals suffice. Regularity is unnecessary for this rank criterion. Over regular noetherian rings, bounded finite homology characterizes derived perfection, without assuming finite Krull dimension. Over noetherian nonregular rings, the exact additional test is uniform boundedness of the **derived** residue-field fibres of the pseudo-coherent normalized complex. [A4.1–A4.3, A4.5.]

The original perfection/rank equivalence fails both ways over \(\mathbf Z\). Torsion at successively different primes gives polynomial ranks at each fibre without a uniform degree bound. An unbounded locally finite sum of contractible disks is perfect but has denormalized ranks \(2^{n+1}-1\). Over \(\mathbf F_2[\epsilon]/\epsilon^2\), a constant residue-field simplicial module has bounded normalization and nonzero Tor in every degree. The corrected block rank is
\[
\operatorname{rank}N_iL=
\mu_i+\mu_{i+1}+\beta_i+\beta_{i+1}+\nu_i.
\]
Derived perfection does not require finite support of the contractible disk multiplicities; strict perfection does. [A4.4–A4.6.]

### A.3. What the full natural Γ-action recovers

The relevant action is
\[
\rho_{p,M}:\Gamma^pF_X(M)\longrightarrow F_X(\Gamma^pM),
\qquad F_X(M)=\operatorname{Hom}_{s\mathsf{Ab}}(\mathbf Z[X],M),
\]
for every bounded finite-free normalized test \(M\) and \(p\ge0\). We construct it using divided powers of evaluation at each simplex. Its degree-two cross effect recovers the tensor pairing; its degree-zero part recovers the unit. The tests \(R_n\), with \((R_n)_m=\mathbf Z^{\operatorname{Hom}_\Delta([n],[m])}\), are proved to belong to the test category and to be the cosimplicial denormalization of the walking complex. Evaluating \(F_X\) on them reconstructs \(A_X^n=\operatorname{Map}(X_n,\mathbf Z)\) with its full cosimplicial ring structure. Conversely a typed equalizer reconstructs \(F_X\) and all these maps from \(A_X\). This is an equivalence of data on the image of spaces, not a claim about arbitrary additive functors or an unspecified localization. [A3.1–A3.2.]

Thus L2 holds for the full natural action requested on scan 38. For connected nilpotent finite-type spaces, this structure determines the integral weak homotopy type. Horel's binomial realization recovers entire derived mapping spaces. Mandell's integral \(E_\infty\) cochains detect objects and give a faithful, nonfull homotopy functor. Toën's simply connected affinization has a natural retraction and detects objects, but its integral derived points have additional \(\prod_p\pi_{i+1}(X)^\wedge_p\) terms in degree \(i\); the unit to those points need not be an equivalence. Finite disjoint unions are handled through primitive idempotents. The rational de Rham comparison requires \(\mathbf Q\subset k\), not merely characteristic zero. [A3.3.]

The lens spaces \(L(5,1)\), \(L(5,2)\) refute only the **weaker** data consisting of a cochain complex up to quasi-isomorphism, its graded cohomology ring, and degree-compatible positive even divided powers. Their linking forms distinguish them despite equality of that information. They are not a counterexample to the full action or to a coherent cochain-level multiplication. Numerical binomial operations also differ from strict polynomial laws: \(a\mapsto\binom a2\) fails naturality modulo two. We do not claim to have re-proved the original source-specific R1 or R5 assertions; R4's cohomology product is considered as weaker information and is not an unverified reconstruction premise. [A3.4–A3.5.]

### B.1–B.3. Counts, trees, and stabilizers

For a finite type \(T\), put \(\Gamma_T=\operatorname{Aut}(T)\), with order \(\prod_na_n!b_n!c_n!\). Let \(K_C,I_C\) be the kernel and image of \(\operatorname{Aut}C\) acting on graded cells. Then
\[
N_T=|\Gamma_T|\sum_{[C]}\frac{|K_C|}{|\operatorname{Aut}C|}
=\sum_{[C]}\frac{|\Gamma_T|}{|I_C|}.
\]
The manuscript's multiplication holds exactly when every \(I_C\) is trivial; rigidity instead concerns \(K_C\). The torus \(E=\mathbf Z/4,\rho=+1,\alpha=+2\) has one pinned class and pinned group \(C_2\), whereas the naive count gives two. The only connected nontrivial combinatorial cellwise kernels are \(C_2\) for opposite-paired one-vertex, one-face bouquets with \(2g\) edges. Half-edges and finite disconnected types are covered. [B1.1–B1.3.]

For \(h_c=z^3(z-1)^2(z-c)\), division by \(G_c=z^2-(5c+4)z/6+c/2\) gives \(Pz+Q\), with
\[
P=-\delta p/7776,\quad
\delta=25c^2-32c+16,\quad
p=25c^3-12c^2-24c-16,
\]
\[
Q=c(5c-8)(25c^3-6c^2+8)/2592.
\]
Raw \(P\) is **quintic**. On \(p=0\), \(Q=(32-52c-c^2)/1500\), and all three desired maps are
\[
\beta_c(z)=
\frac{1500z^3(z-1)^2(z-c)}{32-52c-c^2},\qquad p(c)=0.
\]
Unique normalization and exact nonvanishing/resultant checks establish completeness. The roots of \(\delta\) are \(16/25\pm12i/25\), are raw-\(P\) roots, and have the different passport \([3,2,1;3,1,1,1;6]\). The desired trees consist of one real dessin and a mirror pair. Writing \(r_j^3=2\), the parameters \(c_j=(4+18r_j+6r_j^2)/25\) give moduli and definition fields \(\mathbf Q(c_j)=\mathbf Q(r_j)\), with normal closure \(\mathbf Q(\sqrt[3]2,\zeta_3)\) and \(S_3\) action. Schneps's opened example already contains the equivalent cubic. [B2.1–B2.5.]

The complete compact clean cellwise holomorphic groups are \(\operatorname{Aff}^+(\mathbf R)\) for the one-loop sphere, \(\mathbf R_{>0}\) for **every** orange, \(C_2\) for the positive-genus bouquets, and the trivial group otherwise. Disconnected groups are products. Explicit models are \(-4z^n/(z^n-1)^2\) and \(y^2=x^{2g+1}-x,\ \beta=x^{2g}\). The finite involutions already preserve \(\beta\); function nonuniqueness occurs only in the continuous sphere cases. Cellwise preservation does not imply isotopy to the identity: the torus involution acts by \(-1\) on \(H_1\). The noncompact extension explicitly assumes locally finite ordinary cells with compact edge and face attachments; arbitrary asymptotic tracts are not silently treated as such cells. [B3.1–B3.4.]

### B.4. Every Kummer level

Let \(d_N=2\) for \(8\mid N\), otherwise \(d_N=1\). With compatible positive roots of two,
\[
H_2=\{(a,b):(-1)^b=\chi_2(a)\},\qquad
\chi_2(a)=(-1)^{(a^2-1)/8}.
\]
The adelic index is two; the level-\(N\) order is \(N\varphi(N)/d_N\). The proof excludes every additional radical obstruction, rather than inferring equality from the known \(\sqrt2\) obstruction. Reciprocation gives the same indices for \(K(1/2)\). For \(K(-1/2)\), origins \(\zeta_{2N}2^{-1/N}\) give \(c=(a-1)/2-b\) and \(\chi_{-2}(a)=(-1)^{(a-1)/2}\chi_2(a)\). [B4.1–B4.2.]

Every full Fermat fibre is \(K_N(-1/2)^2\). Equal origins give translations \((c,c)\); opposite phases give \((c-a+1,c)\). The image order remains \(N\varphi(N)/d_N\), so the index is \(Nd_N\) in the scalar affine group and \(d_NN^4\prod_{\ell\mid N}(1-\ell^{-2})\) in the full \(\operatorname{GL}_2\) affine group. Both adelic indices are infinite. At levels \(1,2,4,8\), rank-one indices are \(1,1,1,2\), and full-fibre scalar indices are \(1,2,4,16\). L4's literal rank-one statement is true. [B4.3.]

For independent \(\xi_1,\ldots,\xi_r\in K^\times\), \(K\) a number field, the image is open in \(\widehat{\mathbf Z}^{\,r}\rtimes\widehat{\mathbf Z}^{\times}\) with common cyclotomic scalar. If \(e\) annihilates their lattice saturation quotient in the \(S\)-unit group modulo torsion and \(D=e|\mu(K)|\), the translation kernel contains \(D\widehat{\mathbf Z}^{\,r}\). We derive this from Schinzel and the \(S\)-unit theorem, and independently from Perucca–Sgobba's uniform degree bound. For \(r\ge2\), this is not openness in the larger full-\(\operatorname{GL}_r\) affine group. Repeated Fermat radicands do not satisfy independence. [B4.4.]

## 2. Source reading and access coverage

The operative manuscript passages were read in the supplied transcription ranges where used: 137:14–17, 38–56, 65–86 and 138:19–20, 35–41, 98–112, 129–131. Corresponding reading entries, correction rows, and earlier check events were checked against the algebra. Historical working notes retain some intermediate gates; the final outcome table, sections, registry, and events supersede those dated states.

Every bibliography entry distinguishes opened material from unavailable theorem text. “Opened” below means the indicated passage was actually inspected, not that every page was read. URLs and metadata are retained in the bibliography and fetch logs. Copyrighted source PDFs, TeX, extracted pages, and source-page images are working caches and are **not redistributed** in the final package; their URLs, hashes where recorded, retrieval scripts, exact locators, and proof-use audits make the reading reproducible.

| Opened source | Checked locators and use |
|---|---|
| Roby (1963) | III.3–III.4, pp. 262–263; IV.1, pp. 266–267. Primary PDF: scalar extension, exponential decomposition, laws. |
| Friedlander–Suslin (1997) | §2, Definition 2.1, Lemma 2.2. Author-hosted PDF: strict polynomial functors. |
| Krause, arXiv:1203.0311 | §2, pp. 3–5, Remark 2.2; PDF and LaTeX. Divided-power Hom category. |
| Touzé, arXiv:2607.00631 | Proposition 1, Example 2, Definition 4, Theorem 5, §§3–4; PDF and LaTeX. Its universal property does not supply the missing bare coherence. |
| Dold–Puppe (1961) | §3, (3.3), Theorem 3.6, Corollary 3.8, pp. 219–220; (3.19)–(3.21), p. 223. Printed folios and chain splitting independently rechecked. |
| Bühler, Exact Categories | Proposition 7.6, Theorem 13.7, Example 13.8, Theorem A.1; PDF/arXiv source. Cancellation, Frobenius complexes, embedding. |
| Stacks Project | Tags 066Z and 0G99, Lemmas 15.76.14 and 15.79.2, statements and proofs. Regular perfection and derived fibre amplitude. |
| Mandell (2006) | Main Theorem, Theorems 0.1–0.2, pp. 213–216; published PDF/arXiv TeX. Object detection and nonfullness. |
| Mandell (2002) | Cochain multiplications, Theorems 5.5, 5.8, 4.9 and corollary p. 550; primary PDF. |
| Horel, arXiv:2211.02349v2 | Definition 1.1, Theorems 3.7, 5.4; full TeX/HTML, version 23 March 2025 verified. |
| Toën (2020), arXiv v3 | Theorem 4.1, Corollaries 5.1, 5.4, 5.5; TeX/PDF. Sheaves, integral points, retraction, detection. |
| Conway–Friedl–Herrmann | Linking forms revisited, Proposition 1.2; author PDF and publication metadata. |
| Sullivan (1977) | Theorem 10.1, p. 307; primary Numdam PDF, rational comparison hypotheses. |
| Schneps (1994) | Lemma I.1, Definition 1, Theorem I.5, IV Example 3, author-PDF pp. 27–28; example page visually inspected. Published chapter pp. 47–78. |
| Lando–Zvonkin (2004) | §1.3, Proposition 1.3.16, Construction 1.3.20, Definition 1.3.25, Euler (1.3); §2.2.1. Institutional PDF. |
| Jones, arXiv:1805.09764 | Theorems 1–2, §§2–3; PDF and original TeX. Centralizers and semiregularity. |
| Wendl, version 3.3 (2015) | §4.2.1, Theorem 4.2.1, following quotient classification, Corollary 4.2.7; printed pp. 152–154. |
| Schinzel (1977); corrigendum (1980) | Theorem 2, p. 245; entire corrigendum pp. 101–104 visually inspected. Exponent \(w_N\) verified; used theorem unchanged. |
| Milne, ANT v3.08 (2020) | Theorem 5.11, p. 90: \(S\)-unit finite generation. |
| Perucca–Sgobba (2019) | Author-preprint Theorems 1, 13, Remark 18, introduction pp. 1–2; primary text opened through cached PDF extraction despite direct-transfer failure. |
| Bashmakov (1972) | §5, pp. 50–54, lemma after Theorem 5, p. 53; primary English text opened through retrieval. Its fixed-prime elliptic result is not relabelled a split-torus adelic theorem. |
| Perissinotto–Perucca (2023) | Introduction, Theorems 1.1–1.2; primary PDF, background only. |
| Belyi (1979/1980) | English translation §4, Theorem 4 p. 255, corollary p. 256; primary cached PDF text. Russian/English dates distinguished; no A3/B4 dependency. |

The following passages were **not opened**, and no proof depends on them:

| Source | Actual access and replacement |
|---|---|
| Happel (1988), I.2.6 p. 16 | Metadata, index, lawful preview through p. 10 opened; theorem absent. Locator supplied by opened Bühler 13.7; A2.6 proves the complexes assertion. |
| Lang, Algebra (2002), VI §§8–9 | Official contents and pp. 261–262 preview opened, not section text. Contents locate Abelian Kummer theory in §8 p. 293, and the binomial-equation section in §9 p. 297. Explicit proofs and other opened sources are used. |
| Jones–Wolfart (2016) | Chapter-2 abstract and metadata opened; subscription text unavailable. Opened Jones article replaces the needed background. |
| Ribet (1979) | Author bibliography and article located. Current/legacy publisher routes returned blocking HTML, alternate author route 403. No invented theorem number. |
| Perucca–Sgobba–Tronto (2020) | Repository metadata opened, PDF transfer failed; no dependency. |

Searches covered exact titles and author archives, arXiv, official publishers and institutional mirrors; polynomial categories/exponential functors/Hom laws; Frobenius complexes/perfect complexes/derived fibres; Mandell–Toën–Horel comparisons; lens linking forms; the sextic passport and map centralizers; abelian binomials and uniform Kummer bounds. The separate requested-source audit records each Happel/Lang preview route. The sextic cubic was located in Schneps. We did not locate the precise combined B3 classification during these searches and claim no priority. A failed download is not conflated with failure to open primary text through another retrieval route.

## 3. Programs and computations

All four final mathematical certificates exited zero. These are whole-process wall times from logs/final_certificate_runs.json; earlier structured outputs retain internal arithmetic timings. Finite checks supplement general proofs.

| Certificate | Exact scope and counts | Final wall time |
|---|---|---:|
| code/a1_checks.py | Dimension/cardinality and exterior-unit witnesses; 38 positive triples \(pqr\le8\); 4,913 scalar-twist triples \(0\le p,q,r\le16\); all 16 pairs in \(\mathbf F_4\); 72 scalar-gcd cases with evaluations 0–200. | 0.062174 s |
| code/a2_a4_checks.py | Both \(\mathbf F_2\) retraction scalars; four \(\mathbf Z/4\) elements; all 64 pullback pairs, 16 admissible; 64 dual-number triples; rank degrees 0–16; eight disks in chain degrees 0–9. | 0.023564 s |
| code/a3_b4_verify.py | 135 rank checks; eight signed unit squares mod 5; mod-2 binomial obstruction; levels 1–128; 20,175 subgroup-composition pairs at levels 1,2,4,8,12,16. | 1.110261 s |
| code/B1_B2_B3_certificate.py | 24 permutations and three torus matchings; all 5,400 passport pairs, 2,160 admissible, three orbits of 720; polynomial identities/resultants/discriminants/radicals; oranges \(n=1,\ldots,8\), bouquets \(g=1,\ldots,8\). | 0.629007 s |

The retained outputs are logs/final_a1_checks.txt, final_a2_a4_checks.txt, final_a3_b4_verify.txt, and final_B1_B2_B3_certificate.txt, with earlier structured JSON. The 128-level check verifies finite affine formulas and group operations; it is not a numerical computation of 128 splitting fields. The field-theoretic equality is proved in B4.1–B4.3.

Every retained auxiliary program is accounted for below. Unrecorded aggregate timings are not invented. Download timings are per request, and some requests were concurrent.

| Programs | Scope, outputs, and timing evidence |
|---|---|
| fetch_a1_sources.py; inspect_a1_sources.py | Five retrievals, extraction and inspection. logs/fetch_a1_sources.json: 0.002, 6.368, 7.032, 223.409, 4.217 s. Inspection aggregate time not recorded. |
| a2_a4_fetch_sources.py | One reused arXiv source, three downloads. logs/a2_a4_source_downloads.json: 8.280870, 5.766825, 6.599685 s for new transfers. |
| a3_b4_fetch_sources.py; a3_b4_fetch_extra.py; a3_b4_fetch_final.py | Initial, extra, final/supplement retrievals; matching JSON preserves each result and elapsed time, including non-PDF/failed responses. Initial 3.870–5.937 s; extra 5.189, 4.422, 24.183 s; final/supplement 4.153–14.489 s. |
| a3_b4_inspect_sources.py | Three corrigendum spreads inspected; four Toën locators extracted. logs/a3_b4_inspect_sources.json; aggregate timing not recorded. Source images/text are excluded from redistribution. |
| B_fetch_sources.py | Five successful retrievals/extractions. logs/B_fetch_sources.json: 0.125, 11.031, 0.047, 8.080, 8.187 s. |
| requested_sources_audit.py | Four lawful preview/front-matter checks and Dold–Puppe folio audit. JSON metadata and use audit retained; reused-file checks 0.053, 0.023, 0.053, 0.028 s. Aggregate time not recorded. |
| a1_registry.py; a2_a4_registry.py; a3_b4_records.py; B_write_records.py | Generated result/event fragments; output records and merged registries retained. Record generation, not new proof tests; separate timings not recorded. |
| a2_a4_split_sections.py | Split authored A2/A4 fragments; logs/a2_a4_split_sections.txt. No mathematical transformation; timing not recorded. |
| tex_runtime_install.py; tex_runtime_probe.lua; tex_runtime.py | Workspace-local installation, probe, shared runtime helper. Four package-install times: 0.048317, 0.011147, 0.004729, 0.001241 s in logs/tex_runtime_install.json. Probe/helper times not separately recorded. |
| a2_a4_texcheck.py | Temporary fragment syntax/layout harness, 7.748293 s, exit zero, no overflow. logs/a2_a4_texcheck.json. |
| assemble.py | Combined sections/bibliography/registries. Final logs/assembly.json records 43 statements, 180 events and 30 references. Aggregate time not recorded. |
| final_verify.py | Reran all four certificates and recorded the wall times quoted above. |
| build_paper.py | Integrated BibTeX/LuaLaTeX sequence, command/status/layout metadata in logs/integrated_build.json. Final five steps: 0.007292, 10.165066, 0.008640, 9.971963, 9.599314 s. |
| render_qa.py | Rendered 41 pages at 90 dpi and made seven labelled contact sheets; final runtime 10.167952 s. Hash comparison found only page 8 changed after the last wording correction; it was directly re-inspected. |
| root_review_records.py | Recorded actual root and final independent A1 reviews and certificate reruns as metadata; final output records 70 events in 0.000579 s. |
| package_archive.py | Builds the archive, source-cache hash list and payload manifest; checks required files, all result/event records, single final PDF, CRCs, no nested ZIP, and the 500 MB ceiling. Its executed runtime and output are stored in the archive validation record. |

Exploratory exact algebra was consolidated and rerun in the certificates. Shell searches/source reading are inspection, not mathematical computation certificates. Missing requests support was replaced with standard-library downloads; gzip single-file arXiv sources were decompressed after initial tar-format mismatches. LuaLaTeX format/font dependencies were repaired locally; notes/TEX_REPRODUCTION.md records reproduction. Transient tool failures left no unavailable computation in the proof chain.

## 4. Corrections to attached materials

Paths are exact attached paths relative to the unpacked ZIP, except the separately attached prompt. Lines refer to unchanged input files. Corrections concern mathematics/types or completed claims, not asserted ink inspection.

| Attached file and lines | Correction or completed claim; proof |
|---|---|
| PROMPT(20261119-110155).md, 95 | Prime inversion sufficient, not necessary; exact torsion and degree-zero criterion. **A1.9.** |
| PROMPT(20261119-110155).md, 106, 122–123 | Raw \(P\) quintic; remove \(\delta\) for cubic moduli polynomial. Orbit claim proved. **B2.1, B2.4–B2.5.** |
| PROMPT(20261119-110155).md, 113–115 | L1 conflates three constructions; correct bridge and Hom-law. **A1.3–A1.4.** |
| PROMPT(20261119-110155).md, 116–117 | L2 interpreted as complete natural \(\rho_{p,M}\), constructed and proved sufficient. **A3.1–A3.3.** |
| PROMPT(20261119-110155).md, 118–121 | L3 false for nonnegative source; two-sided replacement proved. Literal rank-one L4 true; full-fibre extrapolation distinguished. **A2.1–A2.6, B4.1–B4.3.** |
| RESEARCH_SA09_study/study/readings/SA09_137-138.md, 229–233, 241–246, 753–759 | Scalar ambiguity refined; unit independence modeled; full bare equivalence and L1 corrected. **A1.3, A1.5–A1.9.** |
| RESEARCH_SA09_transcriptions/transcriptions/MPL_137_045-086_transcription.tex, 1038 | Precomposition of \(f:X\to Y\) uses \(n\operatorname{id}_X\). **A1.2.** |
| RESEARCH_SA09_transcriptions/transcriptions/MPL_137_045-086_transcription.tex, 1221–1223 | Typed associativity is \(G^p(\alpha_{q,r})\alpha_{p,qr}=\alpha_{p,q}^{G^r}\alpha_{pq,r}\). **A1.5–A1.7.** |
| RESEARCH_SA09_transcriptions/transcriptions/MPL_137_045-086_transcription.tex, 1278–1281, 1308–1310 | Bare equivalence needs A1.7; Hom-law target has \(\Gamma^pY\), with module proof A1.4 and abstract counterexample A1.8. |
| RESEARCH_SA09_study/study/readings/SA09_137-138.md, 195–198; RESEARCH_SA09_study/study/CHECK_EVENTS.tsv, 18 | Nonnegative source not Frobenius; full faithfulness survives via disk copresentations. **A2.1–A2.2, A2.6.** |
| RESEARCH_SA09_transcriptions/transcriptions/MPL_137_045-086_transcription.tex, 153–167, 309–321 | Definitions and stalk sequence fix nonnegative indexing; two-sided enlargement must be identified explicitly. **A2.1, A2.6.** |
| RESEARCH_SA09_transcriptions/transcriptions/MPL_137_045-086_transcription.tex, 279–302; RESEARCH_SA09_study/study/CORRECTIONS.tsv, 13; RESEARCH_SA09_study/study/CHECK_EVENTS.tsv, 19 | Additional nonunit kernels confirmed; full all-ring and PID criteria. **A2.2–A2.3.** |
| RESEARCH_SA09_transcriptions/transcriptions/MPL_137_045-086_transcription.tex, 168–204, 295–302, 530–533 | Sex1–2 insufficient; Quillen/admissible replacements A2.4, finite refutation A2.5. Abelian case with all exact sequences valid. |
| RESEARCH_SA09_transcriptions/transcriptions/MPL_137_002-044_transcription.tex, 510–539 | Proposition 1(e)/NB confuse boundedness and perfection; both directions fail. **A4.2–A4.5.** |
| RESEARCH_SA09_study/study/readings/SA09_137-138.md, 122–132; RESEARCH_SA09_study/study/CHECK_EVENTS.tsv, 10 | Rank criterion strengthened to all rings with finite terms; uniform degree does not repair perfection's converse. **A4.2–A4.4.** |
| RESEARCH_SA09_transcriptions/transcriptions/MPL_137_002-044_transcription.tex, 607–638; RESEARCH_SA09_study/study/CORRECTIONS.tsv, 8; RESEARCH_SA09_study/study/CHECK_EVENTS.tsv, 11 | Restore \(\mu_i\); finite support of every block family characterizes strict, not derived, perfection. **A4.6.** |
| RESEARCH_SA09_transcriptions/transcriptions/MPL_137_002-044_transcription.tex, 1527–1545, especially 1535 | Operations act on full test functor and change test object; doubtful glyph replaced by explicitly proved \(s\mathsf{Ab}\) formulation. **A3.1–A3.2.** |
| RESEARCH_SA09_transcriptions/transcriptions/MPL_137_002-044_transcription.tex, 1547, 1551–1567 | Rational de Rham comparison requires \(\mathbf Q\subset k\), stronger than characteristic zero. **A3.3.** |
| RESEARCH_SA09_study/study/readings/SA09_137-138.md, 745–752 | L2 completed by actual \(\rho\), cross effects, and reconstruction; cohomology-only weakening false. **A3.1–A3.5.** |
| RESEARCH_SA09_study/study/readings/SA09_137-138.md, 627–628 | Trivial cell image for counting differs from trivial pinned kernel for rigidity. **B1.1–B1.3.** |
| RESEARCH_SA09_transcriptions/transcriptions/MPL_138_090-133_transcription.tex, 271–280 | Pinned rigidity and naive factorial multiplication false; orbit formula and torus counterexample. **B1.1–B1.2.** |
| RESEARCH_SA09_transcriptions/transcriptions/MPL_138_090-133_transcription.tex, 481 | Table II requires \(\rho_s(r_5)=r_4\); omitted mirror included. **B2.3.** |
| RESEARCH_SA09_transcriptions/transcriptions/MPL_138_090-133_transcription.tex, 531–552, 567–574 | Use \((\alpha-c)\), subtract \((\beta+1)c\), obtain \(-(5c^2-10c-4)/36\); raw \(P,Q\) completed. **B2.1, B2.5.** |
| RESEARCH_SA09_transcriptions/transcriptions/MPL_138_090-133_transcription.tex, 606, 704–708 | Numerator \(f-1\), divisor \((z^2-\alpha z-\beta)^2\). **B2.5.** |
| RESEARCH_SA09_transcriptions/transcriptions/MPL_138_090-133_transcription.tex, 733, 755–757 | Collision-root imaginary part \(12/25\); both raw-\(P\) roots with alternative passport. **B2.5.** |
| RESEARCH_SA09_transcriptions/transcriptions/MPL_138_090-133_transcription.tex, 778–784 | Log derivative subtracts denominator sum; \(\lambda\) cancels. **B2.5.** |
| RESEARCH_SA09_study/study/readings/SA09_137-138.md, 793 | “Cubic P” conflates raw quintic and effective cubic. **B2.1.** |
| RESEARCH_SA09_transcriptions/transcriptions/MPL_138_090-133_transcription.tex, 1543–1547, 1560–1582, 1591–1595; RESEARCH_SA09_study/study/readings/SA09_137-138.md, 678–684 | Cellwise does not imply isotopic to identity; I is \(\operatorname{Aff}^+(\mathbf R)\), II/III \(\mathbf R_{>0}\); all oranges and finite positive-genus exceptions included. **B3.1–B3.3.** |
| RESEARCH_SA09_transcriptions/transcriptions/MPL_138_001-045_transcription.tex, 1263–1267 | Fermat equation fixes \(N\)th-power reading, negative radicand and product. **B4.3.** |
| RESEARCH_SA09_transcriptions/transcriptions/MPL_138_001-045_transcription.tex, 1562–1565, 1570–1572 | Finite origins use \(\theta_N^{-1}e^{\pm\pi i/N}\); inverse-limit expression must retain \(\theta_\infty^{-1}\). **B4.2–B4.3.** |
| RESEARCH_SA09_study/study/readings/SA09_137-138.md, 417–420 | Phase clash rechecked: compatible root of \(-1\) and \(\theta^{-1}\) required. **B4.3.** |
| RESEARCH_SA09_study/study/readings/SA09_137-138.md, 373–389, 412–416, 772–775; RESEARCH_SA09_study/study/STUDY.md, 141–146 | Formerly unverified all-level degree/openness statements completed with exact hypotheses; rank-one and full fibre separated. **B4.1–B4.4.** |

The prompt's references to R1, R4, and R5 are not promoted into proofs of all their original manuscript assertions. Assigned tasks and leads are established through the precise constructions above. Every earlier assertion actually used, independently re-proved, or refuted receives the corresponding check-event type, not a blanket “verified” label.

## 5. Compilation and final visual review

The initial integrated build had **one overfull horizontal box of 20.98811 pt**, from an unbreakable certificate path, and a separate array-syntax failure at a bracket-leading row. The path and syntax were repaired; an unescaped bibliography subscript was also corrected before the successful full build. No failed-build PDF is delivered.

The final paper has **41 pages, zero overfull boxes, zero boxes over 2 pt, zero missing characters, and no unresolved citations or references**. We rendered all 41 pages at 90 dpi and inspected all seven contact sheets. Direct full-page inspection covered pages 2, 8, 14, 20, 24, 28, 34, 36 and 41; the unchanged title page was also directly inspected in the earlier rendering. Page 34 contains the former overflow and page 36 the repaired table. The first full rendering revealed a one-line contents spill and a one-reference final page; adjusted contents spacing and bibliography size removed both, reducing 43 pages to 41.

After the final editorial correction, the render comparison found 40 page images byte-for-byte unchanged and only page 8 changed. We directly re-inspected that final page. No clipping, overlap, unreadable display or missing glyph was seen. See qa/QA_REPORT.md, render_manifest.json and final_image_comparison.json. The only PDF in the archive is this inspected integrated paper. All four exact certificates passed, and the final table has 43 statements with 180 actual check events and 30 bibliography entries. No mathematical item or lead remains labelled Open.
