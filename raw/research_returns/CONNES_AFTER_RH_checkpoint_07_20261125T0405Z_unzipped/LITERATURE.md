# Literature gate: the cutoff, harmonic measure, and the remaining upper bound

Audit date: 24 November 2026. Research agent: GPT-6 Astra, `literature_gate`, same-model review. The run did not expose a separate child reasoning-setting label; none is invented here. This file contains original audit notes, not source transcriptions. Downloaded publications remain outside the deliverable. `literature_sources.tsv` records the versions, paths, SHA-256 hashes, locators, and web retrieval references.

## 1. Findings that govern the paper

Connes (1999, §VIII, Theorem 5, arXiv p. 42) proves the equivalence between a global cutoff trace formula and the Riemann hypotheses for all Hecke characters of a positive-characteristic global field. In that setting the zero count in each character sector is finite modulo the imaginary period. Lemma 3 (pp. 44–45) computes the cutoff defect before any hypothesis about zero location: each centered zero contributes its harmonic measure on the imaginary axis, with its full multiplicity. Applying the known function-field Riemann hypothesis gives the trace formula. Appendix II, Theorem 6 (pp. 77–78), is the explicit formula over every global field; its validity does not by itself establish convergence of a Hilbert-space cutoff.

For characteristic zero, Connes specifies the even prolate selection through index approximately (4\Lambda^2), tensored with the finite-place unramified vector, and asserts the analogues of Lemma 1, Theorem 5, and Lemma 3 (§VIII, after equation (33), pp. 46–47). Those pages contain no quantitative argument controlling the theta-image Gram matrix, the leakage at the prolate transition, or the sum over infinitely many zero conditions. They explicitly restrict their construction to the zeta function of \(\mathbb Q\). This is an existing claim of the proposed zeta result, and must be credited as such. It is not a printed proof of the conductor-dependent selection for every primitive Dirichlet character.

The later sources examined below establish substantial results for different objects: a fixed-scale Sonin trace identity, restricted archimedean Weil positivity, nuclear-space trace formulas, exact Hardy closures, finite semilocal embeddings, spectral counting asymptotics, and conditional ground-state constructions. None of the statements inspected proves the exact growing theta-image prolate limit with index (4\Lambda^2/q\) for every primitive Dirichlet character, much less the proposed family over \(\mathbb Q(\sqrt{-3})\). This is a statement about the documented search, not a claim of novelty or proof of absence from the literature.

The requested assertion that the difference between harmonic balayage and Weil's zero functional has a definite sign on convolution squares is false as a formal zero-packet assertion. Section 3 gives two elementary counterexamples of opposite signs. The positive object in Connes's argument is the harmonic-measure defect itself. Weil positivity follows if the geometric trace formula identifies that defect with Weil's zero functional; it does not follow from positivity of the harmonic measure alone.

## 2. Required sources opened at the relevant statements

All page numbers in this section refer to the downloaded arXiv PDF named in the source register, unless a printed journal page is explicitly specified. They should not be silently converted to journal pagination.

### Connes (1999): three separate trace statements

| Locator | Field, object, and test space | What the result establishes | What it does not establish |
|---|---|---|---|
| §VI | Formal global scaling trace on the adele class space | Geometric origin of the local terms in the explicit formula | A proved global cutoff limit |
| §VII, Theorem 4, p. 31 | Every global field; a fixed finite set (S\) of places; compactly supported Bruhat test (h\) on (C_S\); cutoff (R_\Lambda=\widehat P_\Lambda P_\Lambda\) | The semilocal trace equals its logarithmic main term plus local principal-value terms and (o(1)\) | (R_\Lambda\) is a product of projections, generally not an orthogonal projection; (S\) is fixed, with no uniform assertion for (S=S(\Lambda)\) |
| §VIII, Lemma 1, p. 39 | Positive characteristic; joint support of a Schwartz function and its Fourier transform | Eventual compatibility of the support cutoffs and the finite-dimensional cutoff construction in each fixed character sector | Its archimedean counterpart with no exact joint compact support |
| §VIII, Theorem 5, p. 42 | Positive characteristic; orthogonal projection onto the theta image of the joint-support space; compact Bruhat tests on (C_k\) | Equivalence of the trace limit and all Hecke RH; with Weil's theorem, the trace formula | A proved characteristic-zero analogue with prolate leakage |
| §VIII, Lemma 3, pp. 44–45 | Same cutoff and field, without a zero-location assumption | Exact limit of the defect as the sum of harmonic measures of all zeros, including multiplicities | A direct inequality between that sum and the Weil point-evaluation sum |
| §VIII, equations (31)–(33), pp. 46–47 | (k=\mathbb Q\), even prolate functions through index (4\Lambda^2\), time and frequency radius \(\Lambda\), unramified finite-place vector | Specification and assertion of the zeta analogues | A written proof of those analogues; primitive ramified Dirichlet sectors; the complex archimedean place |
| Appendix II, Theorem 6, pp. 77–78 | Every global field and compact Bruhat tests | Explicit formula with ordinary point evaluation at all zeros and the polar terms | A Hilbert cutoff convergence theorem |

Write a centered zero as (z_\rho=\rho-\tfrac12=a+i\gamma\). With the Mellin convention (F(z)=\int f(x)|x|^z\,d^*x\), the harmonic measure is

\[
 d\mu_{a+i\gamma}(iu)=\frac{|a|}{\pi((u-\gamma)^2+a^2)}\,du\quad(a\ne0),
 \qquad d\mu_{i\gamma}=\delta_\gamma.
\]

Thus the lemma's contribution is \(m_\rho\int F(iu)\,d\mu_{z_\rho}(iu)\), whereas the explicit formula's zero contribution is \(m_\rho F(z_\rho)\). The absolute value of (a\) is essential. In positive characteristic one can use the corresponding Poisson kernel on the period circle. All multiplicities occur in Lemma 3; they are not limited by the Sobolev weight used in the earlier spectral-realization theorem.

**Proof-detail caution.** On p. 45 the printed argument says the normalized truncated exponentials associated with distinct off-circle points become mutually orthogonal. This is not true for two points on the same side of the circle. For real (z,w>1\), after translation to the upper endpoint the normalized vectors converge to multiples of (z^{-n}\) and (w^{-n}\), (n\ge0\), whose inner product is

\[
 \frac{\sqrt{(1-z^{-2})(1-w^{-2})}}{1-(zw)^{-1}}>0.
\]

This invalidates that individual orthogonality justification, not the finite-packet trace identity. The joint finite-dimensional space is the appropriate finite Blaschke model space, and its diagonal kernel is the sum of the Poisson kernels, including repeated zeros. A transport of Lemma 3 must use this joint-space computation. It must not add the limits of nonorthogonal rank-one vectors as if their sum were a projection.

### Connes and Consani (2021), arXiv:2006.13771

Theorem 4.7 (p. 27) is an exact archimedean identity for every (f\in C_c^\infty(\mathbb R_+^*)\). Its trace is the scaling action compressed to the even Sonin space: functions in (L^2(\mathbb R)\) that vanish on ([-1,1]\), as do their Fourier transforms. The trace equals the archimedean Weil distribution plus an explicit correction distribution expressed by prolate matrix coefficients. The trace functional is positive on multiplicative convolution squares. This is a fixed cutoff parameter (1\) and an infinite-dimensional complement; it is not the growing finite-dimensional theta-image projection used in the supplied checkpoint.

Theorem 1 in the introduction (p. 3), with the detailed estimate in Theorem 6.11 (p. 48), treats (g\) supported in ([2^{-1/2},2^{1/2}]\), with a polar Mellin moment removed. The latter theorem bounds the archimedean Weil form below by the Sonin trace minus (c|\widehat g(0)|^2\), where the explicit constant lies between 13 and 17. Imposing the additional zero at (0\) gives the stated positivity comparison. The introduction and the final theorem use opposite signs for the polar transform point; the involution converts them. One must state the chosen transform convention, rather than combine their displayed signs.

Appendix C, Proposition C.1 (p. 51), shows that Weil's criterion can be tested after imposing finitely many additional Mellin zeros away from the zeta zero set. Its test functions still range over unrestricted compact supports. This does not justify replacing the global criterion by the single small-support interval of Theorem 6.11. The proof of the explicit numerical constant uses the paper's computational estimates; those estimates were read as part of the source theorem, not independently reproduced in this audit.

### Connes, Consani, and Marcolli (2007), arXiv:math/0703392

Theorem 6.1 (p. 28) is a Lefschetz-type trace formula in the cohomological/nuclear setting and identifies the trace with the explicit formula over global fields. Proposition 6.2 and Corollary 6.3 (p. 29) express RH for all Grössencharacters as positivity of the trace pairing on the paper's Schwartz test space. In the uncentered convention the involution is (f^\sharp(g)=|g|^{-1}\overline{f(g^{-1})}\); the equivalent centered statement inserts the half-modulus normalization.

These are the Weil positivity criterion in the stated cohomological model and its reformulation. They do not identify a positive Hilbert realization of every nonsemisimple zero jet, and they do not compute the limit of the user-specified prolate projection. Multiplicity in a trace or a positive scalar zero measure is compatible with repeated zeros; this must not be confused with a faithful unitary representation of a nontrivial Jordan block.

### Meyer (2005), arXiv:math/0311468

The correct Duke article is *On a representation of the idele class group related to primes and zeros of L-functions*, Duke Mathematical Journal, 127(3), 519–595, DOI 10.1215/S0012-7094-04-12734-4. The similarly named *A spectral interpretation for the zeros of the Riemann zeta function*, arXiv:math/0412277, is a different, shorter exposition.

Theorem 5.8 (p. 43) gives a smooth summable virtual representation with character equal to Weil's explicit-formula distribution, with the stated uniform absolute convergence on bounded subsets of the compact Bruhat test space. Theorem 5.11 (p. 47) identifies zeros and poles, with algebraic multiplicity, in its spectral data. The construction works for global fields and has no RH assumption. It uses nuclear Fréchet/bornological representation spaces and ordinary point evaluation at zeros. It is not a positive Hilbert representation of all off-line zeros and is not the harmonic-measure prolate defect. Meyer's introduction explicitly motivates the altered spaces by the difficulty of computing the character in Connes's Hilbert construction.

### Connes and Consani, arXiv:2106.01715

Theorem 1.1 (p. 4), proved as Theorem 6.4 (pp. 52–53), characterizes zeta cycles of (\mathbb R_+^*/\mu^{\mathbb Z}\) by non-density of a periodized theta-image space. The input is the even Schwartz space with its value and integral moments removed. Spectral characters of the orthogonal complement correspond to critical-line zeta ordinates compatible with the circle length. An ordinate \(\gamma\) yields cycle lengths that are positive integer multiples of (2\pi/\gamma\).

This correspondence is unconditional as a statement about zeros on the line. It does not say all zeros are on the line, prove their simplicity, or establish the growing prolate trace limit. Once zeta RH is supplied externally, its critical-line spectral set becomes the full nontrivial zero set; the theorem still does not turn a one-dimensional character eigenspace into a full jet space at a repeated zero.

### Connes and Moscovici, arXiv:2112.05500

Theorem 2.6 (p. 7) constructs the specified selfadjoint extension of the prolate differential operator, with its Fourier and support-projection symmetries, and a discrete spectrum unbounded in both directions. Theorem 6.1 (p. 13) gives a Dirac-type operator at the distinguished parameter \(\lambda=\sqrt2\), with simple spectrum on the real and imaginary axes, whose positive imaginary counting function has the zeta leading asymptotic
\[
 N(E)=\frac{E}{2\pi}\left(\log\frac E{2\pi}-1\right)+O(1).
\]
Matching this counting function does not identify individual eigenvalues with zeta ordinates. Neither statement computes the theta-image cutoff defect, and neither imposes a zero-location hypothesis.

### Connes, Consani, and Moscovici, arXiv:2310.18423

The semilocal embedding and Fourier/Mellin identities are stated as Theorem 1 in the introduction (p. 5) and proved in Propositions 4.1–4.2. Theorem 2 there is Theorem 4.6 (p. 23): for a fixed finite (S\) containing infinity, the specified map identifies the archimedean and semilocal Sonin spaces as Hilbertian spaces for every cutoff parameter. The operator is a bounded invertible topological isomorphism; one should not replace that assertion with an unqualified isometry. The induced inner product depends on (S\).

These results operate in the unramified even zeta setting. They supply genuine finite-semilo-cal structure, but do not give estimates uniform as (S\) grows with \(\Lambda\), nor a global Dirichlet- or Hecke-character prolate defect formula. The published title includes the subtitle *Semilocal adelic operators*; the journal is Annals of Functional Analysis, 15(4), article 87 (2024).

### Connes (2015/2016), arXiv:1509.05576

Section 3.1, equation (17) (p. 10), recalls Weil positivity after removal of the pole moments. Section 3.2 (p. 11) explains the absorption sign in the spectral picture. The arithmetic-site and Riemann–Roch discussion develops the geometric programme. This essay is valuable for the interpretation and attribution of the criterion; it does not add the missing quantitative characteristic-zero cutoff argument. Its positivity statements must be read with the displayed pole conditions and transform convention.

### Suzuki (2026), arXiv:2610.32704

The main spectral framework assumes RH. Theorem 1.1 (pp. 1–2) gives convergence of local spectral approximants to the distinct positive zeta ordinates. Theorem 1.2 (p. 2) gives the corresponding normalized entire-product limit over distinct ordinates. The weighted sampling identification in §2.3 (pp. 6–8) retains multiplicities as weights in (\ell^2(\Gamma,m)\); the inverse global operator has one eigendirection per distinct ordinate. A weight (m_\gamma\) in that scalar product is not an eigenspace of dimension (m_\gamma\).

Theorem 3.3 (p. 10) identifies the chosen local selfadjoint inverse with a compression of the global compact operator. Equation (4.1) and the argument in §4 (pp. 11–12) give Hilbert–Schmidt convergence of the compressions. The remark at the end of §4 explains multiplicity recovery by an appropriate probe. The supplied S50 observation should therefore be credited to Suzuki's sampling model and probe construction. These compressions are not the arithmetic prolate theta-image projections, and their convergence under RH supplies no identification of off-line harmonic measures for a different cutoff.

## 3. Independent sign audit

This derivation was completed and sent to the parent before receiving either the parent's proof or the cutoff auditor's proof. The parent subsequently reported agreement of all three derivations. It is independent same-model reasoning, not a different-model review.

Use additive logarithmic coordinates (t\), let (g\in C_c^\infty(\mathbb R)\), and put (g^*(t)=\overline{g(-t)}\), (f=g*g^*\). Set
\[
 G(z)=\int_{\mathbb R}g(t)e^{zt}\,dt,
 \qquad F(z)=G(z)\overline{G(-\overline z)}.
\]
Then (F(iu)=|G(iu)|^2\ge0\). Consider a single reflected pair of centered off-line zeros (a+i\gamma,-a+i\gamma\), (a>0\), of equal multiplicity one. Its harmonic and point-evaluation functionals are
\[
 H_{a,\gamma}(f)=2\int_{\mathbb R}|G(iu)|^2
       \frac{a}{\pi(a^2+(u-\gamma)^2)}\,du,
 \qquad W_{a,\gamma}(f)=F(a+i\gamma)+F(-a+i\gamma).
\]
The Fourier transform of the Cauchy density yields
\[
 H_{a,\gamma}(f)-W_{a,\gamma}(f)
 =-2\int_{\mathbb R}f(t)e^{i\gamma t}\sinh(a|t|)\,dt.
\]

For a negative example, choose nonzero real (g\ge0\) and first take \(\gamma=0\). Its autocorrelation (f\) is nonnegative and positive on an interval about zero. The last integral is strictly positive before the minus sign. Hence (H-W<0\).

For a positive example, choose a nonzero real \(\psi\in C_c^\infty(\mathbb R)\) and take \(g=(\partial_t^2-a^2)\psi\). Integration by parts gives (G(\pm a)=0\), so (W_{a,0}(f)=0\). The Cauchy density is strictly positive and (g\ne0\), so (H_{a,0}(f)>0\). Thus (H-W>0\).

Both examples occur on convolution squares, the positive tests relevant to Weil's criterion. To place the packet at a prescribed nonzero \(\gamma\), replace (g(t)\) by (e^{-i\gamma t}g(t)\). Multiplicities scale the examples. The examples are abstract zero packets, not assertions that any particular (L\)-function has those zeros. They refute the proposed universal termwise sign principle that was supposed to make the off-line weights themselves enforce RH. A half-plane bound can instead control the absolute deviation through its kernel; it cannot repair the claimed ordering.

The converse argument can still work through the ordinary Weil criterion: if a trace formula yields the point-evaluation functional (W\), and the cutoff defect is asymptotically positive, then (W\) is positive. That is a different logical statement from (H-W\) having a fixed sign.

## 4. Burnol and the missing closure-to-cutoff step

Burnol (2001), *An adelic causality problem related to abelian L-functions*, J. Number Theory 87(2), 253–269, arXiv:math/0001013v3, treats every global field. In the consulted 18-page preprint, Theorem 1.11 is p. 5; Theorem 2.7 p. 11; Definition 3.1 and Theorem 3.2 pp. 14–15. With \(\Delta=\overline{E(\mathcal S_{\le1})}\), it proves
\[
 V\Delta=B H^2.
\]
Here (H^2\) is the half-plane Hardy space (a disk in positive characteristic); (B\) has precisely the off-line zeros on the right, with multiplicity. (V\) is the identity in nonprincipal sectors and has multiplier ((s-1)/s\) in the principal sector. Analytic continuation removes a singular boundary factor; the Bercovici–Foias argument removes the remaining exponential inner factor. Critical-line zeros are boundary zeros and do not enter (B\). The support condition is one-sided adelic box support, not simultaneous time/Fourier support.

This is the exact closure theorem relevant to a model-space approach. It proves no uniform approximation rate by finite prolate theta images. Consequently it cannot alone turn convergence on fixed zero jets, or strong convergence of projections, into convergence of a trace involving a non-trace-class translation-invariant multiplier. Tightness remains a separate requirement.

**Finite-packet mechanism.** The finite Blaschke model space has dimension equal to the total multiplicity. Its boundary reproducing-kernel diagonal is the sum of the Poisson densities of its zeros. Therefore the trace of a compressed nonnegative Fourier multiplier equals the sum of the corresponding harmonic integrals. The proof uses the whole model space and includes derivative constraints. In a two-sided expanding interval, zero packets in opposite open half-planes concentrate at opposite endpoints; critical-line packets require the separate bulk calculation. This repairs the finite-packet computation in Connes's proof. It still leaves the global sum and upper estimate for the actual arithmetic cutoff.

The parent is developing the unconditional lower bound by combining finite-packet jet approximation with the checkpoint's unconditional positivity estimate. No claim of independent verification of that new proof is made in this gate file; the present audit identifies the applicable literature and the distinction between a finite packet and an infinite trace.

## 5. Forward literature and what remains conditional

The forward search used arXiv, the authors' publication pages, journal records, Hexagon, and ECCC. It followed the semilocal, Sonin, prolate, and ground-state branches relevant to this task. An exhaustive traversal of every citation of every paper is not claimed. Search queries and retrieval outcomes are recorded separately.

| Source opened | Exact relevant statement | Scope and residual condition |
|---|---|---|
| Connes–Consani, arXiv:2008.10974, *Quasi-inner functions and local factors* | Theorem 4.1, p. 15; Theorem 4.4, p. 17; Theorem 5.3, p. 23 | Finite products of local-factor ratios including infinity are quasi-inner; for infinity plus one prime the off-diagonal part has the stated order (1/2\). The Sonin spaces form a compatible system under adjoining primes. No uniform global cutoff limit. |
| Connes–Consani–Moscovici, arXiv:2403.01247 | Theorem 5.6, p. 20 (the introduction mislabels it 5.9); Theorem 6.5, p. 25 | Local-factor moment/Jacobi problem, especially (S=\{\infty,p\}\), with (q=1/p\) expansions and coefficients in \(\mathbb Z[1/\sqrt2]\). The statements concern moment algebra, not zero-balayage convergence. No trace-limit claim is extracted from this paper. |
| Connes–Consani–Moscovici, arXiv:2511.22755, *Zeta Spectral Triples* | Theorem 5.10, p. 23; proposed limits, p. 27; remaining steps, p. 32 | The finite Weil matrix's smallest eigenvalue is **assumed simple**, its eigenvector **assumed even**, and a stated normalization is required. Then a perturbed scaling operator is selfadjoint, its regularized determinant is the ground vector's transform, and that transform has real zeros. The simple/even hypothesis for the actual ground state and quantitative approximation by the prolate candidate are not proved there. |
| Connes–van Suijlekom, arXiv:2511.23257 | Theorem 6.1, p. 13 | A lower-bounded essentially selfadjoint form on trigonometric polynomials, with simple isolated lowest eigenvalue and even eigenfunction, has a ground-state Fourier transform with only real zeros. These hypotheses are substantive. RH alone does not furnish their simplicity/evenness or the needed approximation rate. |
| Connes, arXiv:2602.04022 | Theorem 6.1, p. 26; §6.6, p. 30; §§7.1–7.4, pp. 30–32 | Survey of the preceding ground-state and local/semilocal programme. Section 6.6 expressly retains simple/even lowest eigenvector and adequate comparison of (k_\lambda\) with the actual ground vector. The fixed local and semilocal formulas do not supply the requested global prolate limit. |
| Andrews–Connes–La Gatta, arXiv:2611.13129 | Hypothesis 3.4; Theorem 8.14, p. 47; Lemma 8.16 and Propositions 8.17–8.18, pp. 48–50; §8.8, p. 52 | Numerical ground-state evidence; conditional Fuchs-ladder approximation; positivity outside a finite-dimensional near-self-dual subspace under the quantitative localization hypothesis H2′. A Schur complement isolates the remaining transition/pole sector. Uniform semilocal localization, Gram control, transition-sector positivity, and ground normalization remain listed problems. No full characterwise cutoff limit. |

Theorem 8.14 in the last source is especially relevant: it controls a complement after finitely many conditions, not the full Weil form. Its finite codimension depends on the selected scale and near-self-dual modes. One must not omit H2′, treat the numerical Fuchs ladder as a proved uniform lower estimate, or infer a growing-(S\) theorem from the fixed archimedean verification.

The same source attributes a ground-state upper estimate to Connes–Kastoris and cites Kastoris computational certificates. The submitted Connes–Kastoris manuscript was not independently located and audited here. Accordingly this audit does not promote that attribution into a separately verified theorem or use it to close any gate. Specific numerical certificates at finitely many parameters would not be a uniform asymptotic lower bound.

## 6. Contemporary arithmetic inputs: statement versus verification

### Alpöge

This is not a case in which a 2026 claim should be dismissed because it postdates training information. The live Lean FRO/Mathlib joint statement of 21 November 2026 explicitly endorses the correctness of both the RH statement and the formally checked proof. Sutherland's MIT verification page, updated 24 November 2026 at 05:25 UTC, records independent compilation, standard-axiom checks, kernel verification, and statement comparison for five headline theorems. Its displayed Mathlib-only statements include RH for zeta and critical-line location of every nontrivial zero of every primitive Dirichlet (L\)-function. Rubinstein's separate verification page provides additional checking records.

The permissible assertion is that these external primary verification records establish the cited arithmetic input. This audit did not compile the roughly seventeen-million-line library or rerun the independent kernels. It did open the public statements and their exact theorem formulations. The result does not assert RH for all Hecke characters of an arbitrary number field, and it does not assert simple zeros.

Primary records: <https://leanprover-community.github.io/blog/posts/riemann-hypothesis/>; <https://math.mit.edu/~drew/grh/>; <https://mrubinst.github.io/grh-lean-verification/>. The author PDF at `https://alpo.ge/remark.pdf` was linked by those records but a direct local download returned HTTP 403 in this audit; no hash for that inaccessible download is asserted.

### Liu and Hu

The live Hexagon record for Liu, 2611.00741v1, agrees with the supplied 68-page manuscript: the current threshold is \(\theta_G\), with
\[
0.8733326374459049352<\theta_G<0.8733326374459051924,
\]
and the stated scope is every number field and continuous unitary Hecke character, plus the stated Artin/Weil extensions. The record says formalization is in progress. The exact strongest manuscript theorem is Theorem 7.33, printed p. 66; the earlier (B_*\) constant and older theorem labels must not be substituted. The extensions auditor owns the line-by-line intake of this theorem.

Hu's live 2610.00216v2 record states the (7/8\) zero-free half-plane for unitary Weil (L\)-functions and all unitary Hecke characters, including infinite-order characters. Its provenance now reports a Lean formalization of the rank-one Theorem 1.2 with a comparator-checked Mathlib-only statement, linking `Rogerhu12/hecke-seven-eighths`. This is the author's provenance statement; this audit did not rerun that code or an independent checker. The PDF's Theorems 1.1 and 1.2 are on printed pp. 1–2. These inputs are not evidence for a prolate trace formula or RH over \(\mathbb Q(\sqrt{-3})\). The manuscript theorem, public provenance assertion, and independent verification status must remain distinct in the paper.

## 7. Landau: the edge estimate is genuine, but is not the arithmetic tightness estimate

The primary scan of Landau's 1985 overview was opened and its relevant pages visually inspected. In its normalization \(\Omega=\pi\), printed p. 209 (PDF p. 9) states the middle eigenvalue limit at index (2T\); printed p. 211 (PDF p. 11) gives the logistic transition
\[
 \lambda_{[2T+b\log T]}\longrightarrow(1+e^{\pi^2b})^{-1}.
\]
The paper attributes the proved transition asymptotic to Landau–Widom. Setting (T=2\Lambda^2/q\) gives the edge (4\Lambda^2/q\). Monotonicity and a squeeze with fixed (b=\pm\varepsilon\) handle bounded index-rounding errors and yield convergence of the selected edge eigenvalue to (1/2\), hence the eventual lower bound (1/4\). Fixed conductor is required for this substitution.

This controls the scalar time-band limiting spectrum. It does not control the smallest eigenvalue of the theta-image Gram matrix, nor the trace norm of the difference between its orthogonal projection and a window compression. In particular the positive proportion of leakage at the edge cannot be discarded by saying every selected vector is almost entirely inside the band.

## 8. How the findings should constrain the manuscript

1. Credit the positive-characteristic exact defect computation to Connes, the zeta prolate assertion to his number-field discussion, the restricted archimedean positivity and exact Sonin identity to Connes–Consani, and the full nuclear explicit formula to Meyer/Connes–Consani–Marcolli.
2. State the cutoff and test space every time a trace theorem is used. Distinguish a product of projections, an orthogonal projection on a theta image, a Sonin complement, a Hardy closure, and a compact-operator compression.
3. Give no definite-sign claim for the difference of harmonic and point-evaluation zero functionals. The independent counterexamples above rule it out.
4. An infinite sum of positive harmonic weights may be justified from finite-packet lower bounds by monotone convergence. Equality still requires a matching upper bound and tightness for the actual cutoff. Burnol's closure theorem does not provide their rate.
5. Any claimed comparison between Suzuki moment defects and prolate trace defects must identify the operators and normalizations; shared terminology does not establish equality.
6. Alpöge's verified Dirichlet theorem supplies an arithmetic input only. It neither proves the prolate estimates by itself nor resolves multiplicity-sensitive ground-state questions.
7. No novelty sentence is supported merely by this search. The manuscript should report established results, the precise partial result actually proved in this run, and the unresolved upper/tightness gate.

## References and source discipline

Author/year references in the body identify the primary works; full titles, publication metadata where checked, version URLs, hashes, and source locators are in `literature_sources.tsv`. The local archive paths identify user-supplied source material. The newly downloaded PDFs are in `research_sources/`, outside `research_output/`. Web reference IDs are retained for the parent to reopen and cite; they are not bibliographic identifiers. No downloaded source PDF, extracted source text, or third-party LaTeX belongs in the returned deliverable.


## Later discovery: Burnol systems and Li's related trace formulas

During the independent lower-bound review, the extensions auditor found Burnol (2004), *Two complete and minimal systems associated with the zeros of the Riemann zeta function*. Its arXiv preprint math/0203120 was downloaded and opened at §2 (p. 5) and Theorems 3.1–3.2 (p. 6). The extended Sonine space consists of functions and cosine transforms constant on (0,a); the ordinary Sonine space has both constants zero. Theorem 3.1 identifies the completeness/minimality threshold of the full zero-evaluation systems, including derivative multiplicities, and identifies the co-Poisson orthogonal complement below the threshold. Theorem 3.2 accounts for the two missing polar coordinates in the ordinary Sonine version. These are additional existing zero-space completeness results, not a claimed rate for the growing finite arithmetic cutoff.

The same search identified **Xian-Jin Li**, not Burnol, as author of the 2012 JMAA paper *Prolate spheroidal wave functions, Sonine spaces, and the Riemann zeta function*, DOI 10.1016/j.jmaa.2011.11.068. The publisher abstract describes an explicit-formula trace on a direct sum of a Sonine space and two prolate-type spaces. Direct full-text retrieval returned HTTP 403; the exact operator, test class, and theorem have therefore **not been audited**. This is a material coverage limit and precludes any exhaustive statement that no related characteristic-zero Hilbert trace theorem exists. Li's 2010 publisher abstract describes local and S-local Hankel formulas, and his 2015 publisher abstract describes a global Fréchet trace. These distinctions are source-reported scopes, not substitutes for reading their proofs.

The author page also links a 40-page manuscript dated 3 April 2024, *On the location of zeros of the Riemann zeta-function*. Its introductory Theorems 1.2–1.7 and cutoff definitions were opened. It asserts a semilocal Weil-positivity argument and RH for zeta, using different operators and restricted constructed tests. This audit has not verified that proof and does not use its assertion as a theorem. It must not be confused with the independently documented 2026 Alpöge verification. The appropriate literature status is accessible claimed manuscript, with the exact initial statements identified, not a verified resolution of the prolate cutoff question.

## Additional primary-source checks, 25 November 2026, 00:00–00:14 UTC

- Borger, *Lambda-rings and the field with one element*, arXiv0906.3146: Theorem0.1, Corollary6.2 p20, Remark6.8 p22 opened. The Tate-normalized smooth proper category is finite abelian; the converse uses cyclotomic finite etale regular representations. This is background for the geometric scope, not an input to the analytic trace proof.
- SGA6, ExposeXIV, section6.1–6.4, printedpp682–685: the supplied LaTeX edition was read. This is an open-problem discussion: the Gysin morphism is assumed available, regularity/purity cases are specified, and universal singular cases are not asserted. No scan was fetched.
- Clunie and Kuijlaars(1994), Corollary1.3, printedp110, was visually read from the primary university-hosted PDF. Convergence in measure on a positive-measure real set, nonzero on a positive-measure subset, implies local uniform entire convergence for the restricted-zero polynomial sequence. It validates a conditional ground-vector upgrade; it does not prove the missing spectral ratio.
- Jiang and Luo(2023), arXiv2108.03566v2: eq3.6 and Proposition3.2/Definition3.3 pp16–17; Theorem4.7 p27; Theorem8.2 p50. The standard GLn Poisson theta formula and a critical-line spectral quotient already exist. The quotient multiplicity is truncated by its Hilbert weight. No finite arithmetic concentration theorem is obtained merely from this source.
- Jiang and Li, arXiv2306.02554v4(2024), Theorems6.9 and6.13 pp34,39: Godement–Jacquet kernels characterize zeros as distributions. This is cited before formulating the additional finite-section problem.
- Humphries, *Archimedean newform theory for GLn*, Theorem4.22 and section2.3.2: local test vectors and zeta normalization checked. Published metadata verified: JIMJ24(1)(2025),41–116; DOI10.1017/S1474748024000227. Statement locators used in the paper refer to the opened arXiv version.
- Booker, Milinovich, and Ng(2019), arXiv1707.01576v3, Theorem1.1 p2: fixed primitive holomorphic cusp forms of arbitrary level satisfy a t^(1/3)logt bound; no weight-one exclusion is present. Used for irreducible finite-order Hecke theta series.
- Petrow and Young(2023), arXiv1908.10346v3, Theorem1.1 p1: all primitive Dirichlet characters satisfy the hybrid Weyl exponent1/6+epsilon, with no conductor restriction. Used for reducible Hecke theta sectors. Metadata checked on the author's page and UCL repository: Duke172(10),1879–1960.
- The primary PDFs of Bhargava2610.00228v1,2610.00294v1,2610.00699v1 were reopened at their first statements. Exact titles replaced earlier descriptive bibliography entries. Their conclusions are positive lower densities, not uniform occupancy for every prime. Hexagon landing pages failed; /pdf/ version URLs succeeded.

Downloaded-source hashes and URLs are recorded in research/programme_source_downloads.json and research/gln_source_downloads.json. External PDFs and extracts remain outside every deliverable archive.

## Further natural-cutoff search, 25 November 2026, 00:42–00:58 UTC

Searches used both internet engines for Hecke ideal Möbius sums with norm twists uniform to polynomial height. They rediscovered the classical integer Möbius uniformity papers and recent cubic-family moment/zero-density work; no inspected result supplied the full fixed-character high-frequency inverse estimate needed by the natural Hankel cutoff. This is a search outcome, not a claim that no such result exists.

The official OpenAI repository was opened at `preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex`, Section From the mean-square estimate to the zero-free region, Proposition thm:ms and equation eq:ms. Its bound explicitly depends on finitely many smooth seminorms of the weight. Inserting a norm twist into that weight costs a power of its height; the displayed statement therefore cannot simply be read as an arbitrary-polynomial-height estimate. The argument is not used as an input to the deep-Hankel theorem. URL: https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex . The source was read through the web interface, not downloaded as a byte-identical file, so no file SHA-256 is asserted.

The analytic status described earlier in this dated register has moved: the rational and explicit deep-Hankel upper/tightness arguments are now proved and targeted-checked. Earlier search notes describing them as open are historical entries, not the current theorem status.

## 25 November 2026, 01:12–01:22 UTC: classical arithmetic inputs for the natural Hankel selection

The newly derived exterior-functional estimate needs only a fixed-character untwisted ideal Möbius bound. Searches for Hecke Mertens/reciprocal bounds first found secondary or later applications; these were not used as theorem inputs. A stronger primary-source search found Thorner and Zaman (2019), *A unified and improved Chebotarev density theorem*, Algebra & Number Theory 13(5),1039–1068, DOI10.2140/ant.2019.13.1039. The publisher PDF was opened at Theorem3.1,p1051 and its factorization context. It gives the classical zero-free region for finite abelian Hecke factors, with at most one real exceptional zero. For a fixed character that zero is excluded by reducing the region constant. The original record fixed_hecke_mertens_and_mean_square.md supplies Borel–Carathéodory reciprocal control and a sharp Perron argument using a proved divisor short-interval bound. A separate targeted check passes this deduction. This uses neither RH nor the recent constant half-planes.

Chandrasekharan and Narasimhan (1964), *On the mean value of the error term for a class of arithmetical functions*, Acta Mathematica112,41–67, DOI10.1007/BF02391764, was opened in an institutional PDF. The complex-coefficient setup on pp43–44 and Theorem1,p62,eq57 cover the exact finite-order Hecke functional equation. The equality case 2beta−delta−1/A=0 was verified on a rendered page by the parent and independently by a separate reader. Taking delta=A=beta=1 and beta'=3 gives the required mean-square discrepancy bound. This is a known mean-square result, not a novelty claim. Its detailed mapping and the bounded constant-term difference are recorded and target-checked. The additional original Riesz-series derivation remains a separate research record.

The alternative Iosevich–Sawyer–Seeger lattice discrepancy source was not used because its translated-coset scope was not verified. The KCL-hosted dihedral paper returned HTTP403. No source-access claim is made for its inaccessible contents. Exact download hashes and byte sizes for both used primary PDFs are in research/natural_cutoff_source_downloads.json; external PDFs and their text extractions are excluded from all returned ZIPs.

## 25 November 2026, after01:56 UTC: bounded source follow-up

A further primary-source search for Xian-Jin Li's exact2012 prolate/Sonine paper and2010 generalization again found the publisher records and the author's official BYU publication list. The2012 record is marked open archive, but direct full-page retrieval still returns HTTP403; the author home page links only the2024 preprint already inspected. No missing exact theorem statement is claimed read, and no priority conclusion is drawn. A further forward search for Hecke Hankel cutoff zero limits and Connes harmonic measures rediscovered Andrews–Connes–La Gatta2611.13129 and Li's local/S-local Hankel trace work; these are already separately scoped above. The ACL arXiv abstract was reopened and still states conditional ladder and complement-positivity hypotheses. These are bounded searches, not an exhaustive negative result.

NIST DLMFSections10.6,10.17,10.22 were opened at the derivative identities, fixed-order Bessel expansion, and product integral10.22.4. The independent natural-cutoff proof uses exactly these formulas. They have no arithmetic or zero-location hypothesis. No external page content is copied into the workbench.

The complete format1 specification at the public mathematics-workbenches raw repository was read. Its SHA256 and source URL are in SOURCES.tsv. Stable staging identifiers, distinct check events and cited-only external sources are preserved; permanent WB allocation and a public commit belong to later filing and are not invented here. CA-048 retains the earlier deep-selection main statement; CA-059 identifies the strengthened fixed-threshold main statement.

## Earlier automorphic zero-space sources followed, 2026-11-25 after 02:12 UTC

The references of Jiang–Luo led to Soulé (2001), *On zeroes of automorphic L-functions*, Contemporary Mathematics290, pp167–179, and Deitmar (2001), *A Pólya–Hilbert operator for automorphic L-functions*, Indagationes Mathematicae12(2), pp157–175. The official Soulé author list and AMS contents confirm the citation. Indexed primary text states a weighted critical-line quotient theorem, with multiplicity limited by the Hilbert weight, and explicitly proposes a matrix analogue of Connes’s Lemma3 for the noncritical zeros. Complete copies could not be fetched from the Vienna institution (404), CERN (bot wall), or CiteSeer mirror (403/404). This remains an access limitation, and the full proof is not recorded as read. The manuscript relies instead on the directly read Jiang–Luo statements; it makes no claim of priority for the Godement–Jacquet zero-space construction.

Deitmar’s arXiv:math/9903061v3 (17 March1999), 12pages, was read in full; its SHA256 is 928691e2d312f6c4ad7b8fbef629803e7b4d55dcce3f1e841d45ce69e4de3d8c. Theorem3.4 p12 states a discrete critical-line spectral realization in a weighted quotient. This is not an all-zero cutoff-defect theorem. The downloaded preprint’s Lemma3.2 p7 claims norm-one unramified Satake parameters from unitarity, which fails for complementary series; its remark after Lemma3.3 p8 claims entireness beyond the cuspidal case. Neither claim is used here. These observations concern the precise preprint version read, not the uninspected 2001 published revision. The source receipts retain successful and failed addresses, and no downloaded source is included in the deliverables.

## 2026-11-25 — Artin induction and conductor normalization

Horawa, A. (n.d.). *L-functions*. Author-hosted research report, https://people.maths.ox.ac.uk/horawa/L-functions.pdf. Theorems4.2–4.4 (pp52–53), Proposition5.2 (p56), Theorem5.10 and Lemma5.12 (pp59–61), and Proposition5.58(2) (p78) were opened and read. They provide the classical Artin–Hecke dictionary, every local factor under induction, and the discriminant-times-conductor norm formula. These identities, including ramified primes, transfer the proved fixed-field Hecke cutoff to irreducible induced degree-two Artin functions. This is a formal consequence, not a new induction theorem or a generic degree-three analytic result. The source PDF has765395bytes and SHA256 b946b33639ebc6dd1fbfdb975e593d6e0511cfa248e8ad633048b496d8b2793b. Only the citation/receipt and our own derivation are returned; the external PDF is excluded. The report contains an incorrect non-negative wording for Brauer coefficients in the proof of Theorem5.15; that passage is not used. The cited induction statement and our explicit local determinant/conductor checks do not depend on it.

## 2026-11-25 — exploratory holomorphic GL2 specialization

A bounded search of arXiv, journals, author pages, ECCC and Hexagon for holomorphic cusp-form Hankel cutoffs, harmonic zero measures and reciprocal coefficients found related spectral/one-level-density and zero-density work, not an inspected exact fixed-threshold theorem for the present theta image. No exhaustive or priority conclusion is drawn.

Hoffstein and Ramakrishnan (1995), *Siegel zeros and cusp forms*, IMRN1995(6),279–308, DOI10.1155/S1073792895000225: the actual scan of TheoremC(3), printedp299/PDFpage21, and the holomorphic gamma normalization on printedp282/PDFpage4 were visually opened. This supplies the fixed-form GL2 zero-free region for an exploratory extension. The author PDF URL, byte size908728 and SHA256 cd39c6e3a1349710c22b63bc9409ebc7b2d1ee6388a4aed8b9c73c6557961e58 are recorded in research/hoffstein_ramakrishnan_receipt.json. Its OCR was used only for navigation; the theorem formula was read in the scan.

Booker–Milinovich–Ng's holomorphic fixed-form Weyl estimate and the shifted-gamma setup of Chandrasekharan–Narasimhan were rechecked for this specialization. A first-pass proof develops an original weighted angular tent and twice-Abel calculation, because a direct replacement of the order-zero Bessel kernel in the unweighted Riesz formula is invalid. The resulting exploratory extension remains outside the manuscript pending its separate targeted review and statement-only reproof attempt.


## 2026-11-25 — holomorphic forms and odd two-dimensional Artin representations

Primary-source checking of the enlarged fixed-form cutoff uses Deligne (1974), Theorem8.2, printedp302, for normalized unramified coefficients at weight at least two; Deligne–Serre (1974), §§1.7–1.8, Theorems4.1 and4.6, Corollary4.8, and equation9.3, for the weight-one coefficients, ramified factors, exact conductor, and all-prime Artin equality; and Khare–Wintenberger (2009), author-preprint Theorem10.1(ii), p20, and Corollary10.2(ii), p21, for modularity of every odd irreducible continuous complex two-dimensional Galois representation overQ. The last statement includes projective A5. It is an established input, not a modularity theorem of this work. Publisher metadata for Khare–Wintenberger was verified at https://link.springer.com/article/10.1007/s00222-009-0205-7. Each receipt records the exact PDF hash and read locations.

The fixed-form zero-free region is Hoffstein–Ramakrishnan TheoremC(3), printedp299; it supplies reciprocal Möbius cancellation after the contour argument proved in the candidate. Booker–Milinovich–Ng Theorem1.1 and §2 include all fixed primitive holomorphic forms, with weight one discussed in their coefficient estimates. Chandrasekharan–Narasimhan Theorem1, equation57, includes the equality branch for the shifted gamma factor and complex dual coefficients. The original level-one candidate, the broadened candidate, and their different independent/targeted review scopes are preserved separately.

A fresh forward search used “Hankel Connes cusp forms”, “prolate modular L-functions”, and “harmonic measure automorphic zeros”. It rediscovered Li’s previously recorded local/Hankel and inaccessible exact prolate papers. Bondarenko–Radchenko–Seip (2023), Theorems1.1,5.1,5.2 and §5.3.1, gives analytic-strip interpolation from zero jets and logarithmic samples, with sketched quadratic/modular extensions. The inspected statements do not identify this full-Gram growing projection. No exhaustive negative or priority claim is drawn.
