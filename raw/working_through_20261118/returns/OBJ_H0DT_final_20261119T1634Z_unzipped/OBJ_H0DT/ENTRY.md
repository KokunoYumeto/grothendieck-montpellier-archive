# H0DT — Entire functions: genus, order and Hadamard–Borel factorization

**Foundational entry.** Alexander Grothendieck’s Montpellier manuscripts, cote 1. Mathematical and documentary checks completed on 19 November 2026. The manuscript leaves are undated; the catalogue’s 1953 date belongs to a letter in the folder. This entry does not assign that date to the analytic notes.

**Outcome.** The central Hadamard–Borel statement is known and correct. The inventory contains **73 statement rows: 46 True as written, 6 Known, 20 Slip and 1 False**. The descriptive programme row is accompanied by separately proved precise versions. All seven supplied note entries are adjudicated through 55 subclaim records. No mathematical row is left Open. Some small handwritten marks and one paragraph’s scope retain qualified reading confidence; that uncertainty is explicitly distinguished from the mathematical verdict.

The most consequential false example is the product with zeros \(n^\alpha\), \(\alpha>1\): its order is \(1/\alpha\), whereas scan 110 writes \(1\), qualified by “sauf erreur.” The coefficient-majorant theorem is true, but its written proof requires several local repairs. The function \(S(\lambda)=\sum n!\alpha_n(\lambda)\) on \(\ell^1\) is globally holomorphic and unbounded on the unit ball. Its historical description as not an entire function is correct under Grothendieck’s stronger published definition; replacing that definition by today’s broader usage would manufacture an error (Grothendieck, 1956a, p. 324, equations 13–14).

## 1. The object in his terms and in today’s terms

**His terms.** The consecutive headings are “Décomposition en facteurs des fonctions entières,” “Genre d’une fonction entière” and “Ordre d’une fonction entière.” The notes use \(a_n\) for nonzero zeros, primary-factor degrees \(p_n\), an entire exponential factor \(g(z)\), a maximum \(M(r)\), and a numerical order \(\rho\). For sequences they compare power-summability and decay exponents. For \(\lambda\in l^1\), the elementary symmetric sums are \(\alpha_n(\lambda)\), and their factorially weighted sum is \(S(\lambda)\). See 1/107–108, 1/113–115 and 1/120–122.

**Today’s precise framework, ours.** Let \(f\) be a nonzero entire function of one complex variable. Remove its zero at the origin, if any, as a factor \(z^m\). For its remaining zeros \(a_j\), counted with multiplicities, put

\[
E_p(w)=(1-w)\exp\left(\sum_{k=1}^{p}\frac{w^k}{k}\right),\qquad
\tau=\inf\left\{s>0:\sum_j |a_j|^{-s}<\infty\right\}.
\]

When a finite least integer \(p\ge0\) satisfies \(\sum_j|a_j|^{-p-1}<\infty\), write

\[
f(z)=z^m e^{Q(z)}\prod_jE_p(z/a_j).
\]

If \(Q\) is a polynomial, the manuscript’s genus is
\(G=\max\{p,\deg Q\}\), with the constant case assigned degree zero for this purpose. If no such finite representation exists, there is no finite genus. Its order is

\[
\rho=\limsup_{r\to\infty}\frac{\log\log M_f(r)}{\log r},
\qquad M_f(r)=\max_{|z|=r}|f(z)|.
\]

Nonzero constants and polynomials have order zero. A harmless \(\max(e,M_f)\) convention makes the formula defined for small constants. The zero function is included when an algebra is discussed, but is not assigned a genus. These are explicit conventions of this entry. The prime on a sum over zeros excludes the origin and does not discard multiplicities.

The central theorem gives \(p\le\tau\le\rho\), polynomial degree at most \(\rho\), and \(\rho=\max\{\tau,\deg Q\}\). Consequently
\(\rho-1\le G\le\rho\). Nonintegral finite order determines \(G=\lfloor\rho\rfloor\); positive integral order \(q\) permits \(q-1\) or \(q\). At order zero only genus zero is possible. Valiron’s definition after Theorem XXIX uses the same maximum-of-degrees convention; McMullen’s primary-factor convention requires translation before comparing the word “genus” (Valiron, 1925, pp. 23–24; McMullen, 2025, Theorem 3.16, p. 89). Full derivations, including the boundary cases, are in H0DT.5–16 of `PROOFS.tex`.

## 2. Where he writes about it, in manuscript order

| Cote and scans | Content and exact connection | Date evidence |
|---|---|---|
| 1/071 | Exterior-power coefficient bounds and the Hilbert Fredholm determinant of genus zero; live Corollary 4 and Theorem 1. | No date on the inspected leaf. |
| 1/079–080 | Live coefficient/radial majorants, followed by a cancelled eigenvalue-product argument and its reduction to the scalar majorant theorem. | No date on the inspected leaves. |
| 1/107–110 | Weierstrass factors; genus and order; Hadamard–Borel; examples, operations and a coefficient criterion. | No date on the inspected leaves. |
| 1/111–112 | Coefficient-majorant proposition, sector argument and three rotated factors. | No date on the inspected leaves. |
| 1/113–115 | Sequence exponents, little-o estimate, positive products, maximum term and the Banach/Fréchet programme. | No date on the inspected leaves. |
| 1/116–119 | Counting functions, weighted sums, logarithmic circular means and the endpoint zero. | No date on the inspected leaves. |
| 1/120–122 | Elementary symmetric coefficients and \(S\) on \(l^1\); corrected coefficient argument, multilinear norms and unit-ball unboundedness. | No date on the inspected leaves. |
| 1/129–132 | Positive-product Mellin formula, determinant maxima and Jensen’s eigenvalue power-sum bound. | No date on the inspected leaves. |
| 1/137–138 | Positive determinant maximum comparison and the Mellin change of variables in the operator-product argument. | No date on the inspected leaves. |

The core supplied extract is 108–121. Targeted searches of the complete supplied transcription located its antecedent on 107, continuation on 122 and the determinant applications. The full transcription was not read through. Scans 4,8–9 occur in one entry’s metadata, but the entry’s actual remarks concern 116,119,120. Reading the early attached span 4,7–21 showed operator/singular-value material belonging to H0DJ, not an omitted H0DT genus theorem. `work/LOCATORS_AND_SCOPE.md` records both inclusions and exclusions.

Locators use **cote/scan.manuscript-line**, never the PDF footer or handwritten archive sheet number. The supplied line markers are retained for 108–121; additional pages were counted visually, with formula names supplied as extra anchors. Sideways text is labelled as margin. The official cote-1 PDF was matched to a supplied scan before rendering the additional pages. The manuscript was not OCRed. Decisive cropped enlargements and all disagreements with supplied readings are retained in `crops/` and `READINGS.tsv`.

The broad archive topic “Éléments de Géométrie Algébrique” is a filing context. It does not identify these functional-analysis leaves as a draft of an EGA theorem. The positive publication matches are in Fredholm theory. The catalogue description separates undated notes from a 1953 letter; no chronology of these individual leaves is inferred from that letter (Université de Montpellier, n.d., cote 1 catalogue).

## 3. Groundwork beside his words

### 3.1 Canonical products, type and the role of the zero sum

**His terms.** “Genre zéro,” “ordre fini,” the reciprocal-zero sum, and the positive product occur as different ingredients in 1/108–114. The proposition on 1/111 requires both coefficient domination by a genus-zero function and summability of the reciprocals of the nonzero zeros of \(f\).

**Our explanation.** Genus zero implies exponential type zero: for every \(\varepsilon>0\), \(M_f(r)\le C_\varepsilon e^{\varepsilon r}\). A finite polynomial head and a tail with arbitrarily small reciprocal-root mass prove this directly. Type zero is stronger than order at most one, and neither phrase permits replacing the other without proof. Combining type zero with the summable reciprocal-zero condition rules out a residual nonconstant exponential. In H0DT.21 the proof uses the written three-rotation idea after correcting the rotation, angular endpoint, constants and radial majorant. It does not drop either hypothesis.

The necessary zero-counting formula is derived here, rather than used under an unexplained branch choice:

\[
V_f(r)=\frac1{2\pi}\int_0^{2\pi}\log|f(re^{it})|\,dt
=\log|f(0)|+\sum_{|a_j|<r}\log\frac r{|a_j|}.
\]

For \(f(0)\ne0\), this function is locally absolutely continuous and \(V_f'(r)=n(r)/r\) almost everywhere. It remains well defined when the circle passes through a zero, since logarithmic singularities are integrable. The ordinary contour integral of \(f'/f\) requires avoiding such radii. The manuscript’s real-part annotation matters: a principal complex logarithm can jump even for a zero-free function, whereas its real part is \(\log|f|\). The finite-interval, weighted-tail and endpoint identities are separately proved in H0DT.40–51. McMullen’s Theorem 3.11 and Corollary 3.14 provide opened modern Jensen/zero-exponent counterparts (2025, p. 86).

### 3.2 Fredholm means a trace-class operator here

**His terms.** The analytic application concerns an “opérateur de Fredholm” in a Hilbert space, its \(\det(1+zu)\), exterior coefficients \(\alpha_n(u)\), and the positive operator \(|u|\). The cancelled passage on 1/080 explicitly invokes the scalar coefficient-majorant proposition.

**Our translation.** In the terminology of Grothendieck’s exposé, a Fredholm operator is obtained from a projective tensor kernel; in the Hilbert case at issue here it is a trace-class operator. It must not be confused with the broader modern use of “Fredholm operator” for an operator with finite-dimensional kernel and cokernel and closed range. The historical definition is in exposé 91, §2, p. 380. The same exposé’s Theorem 2, p. 381, gives the determinant’s spectral zeros, and §4(c), p. 383, states exactly the summable eigenvalue product of genus zero (Grothendieck, 1954/1957).

Our proof does not use the trace identity to prove itself. Singular-value decomposition gives the coefficient majorant. Finite-dimensional invariant root spaces and phase contractions give the absolute eigenvalue bound. The scalar proposition then removes the possible exponential factor, after which comparing coefficients yields the trace identity. The cancelled projected-trace estimate also suffices for absolute summability when its quantifier is correctly retained: bounds for **arbitrary finite subfamilies** imply absolute summability by splitting real and imaginary signs. Ordered partial sums alone would be insufficient. The final H0DT.4 verdict corrects an intermediate mistaken diagnosis in this run; the dated correction is preserved in the ledger.

### 3.3 “Entire” for the Banach-space example

**His terms.** On 1/120–122, \(S\) is defined at every point of \(l^1\), has holomorphic finite-dimensional restrictions, is unbounded on the unit ball, and is called not an entire function. The continuation’s margin also asserts global holomorphy.

**Our translation.** In Grothendieck’s published definition, an analytic entire map has a homogeneous expansion whose associated multilinear norms have nth roots tending to zero. This implies absolute uniform convergence on every bounded ball (Grothendieck, 1956a, Introduction §2, p. 324, equations 13–14). In modern Banach-space terminology the relevant distinction is global holomorphy versus bounded type. The example is globally Fréchet-holomorphic but not of bounded type.

Put \(P_n=n!\alpha_n\). Both its homogeneous polynomial norm on the unit ball and the norm of its associated symmetric multilinear form are exactly one. Thus the centered uniform convergence radius is one, even though the scalar series on every fixed line has infinite radius. The equal-coordinate vectors \(a^{(m)}=(1/m,\ldots,1/m,0,\ldots)\) have norm one and satisfy \(P_n(a^{(m)})\to1\) for each fixed \(n\); finite initial sums force \(S(a^{(m)})\to\infty\). Local holomorphy at an arbitrary point is proved using a uniformly small tail, not inferred merely from linewise convergence. These facts decide all clauses of the proposition without translating a historical definition into a supposed contradiction.

### 3.4 The sequence-order programme and what is ours

**His terms.** Scan 1/115 names “sommabilité forte” and “sommabilité absolue” as two approaches to the order of a Banach- or Fréchet-space sequence. It then defines the order of a bounded set by an infimum over closed convex balanced hulls. It does not write a complete vector-valued exponent formula.

**Our precise completions.** For a Hausdorff Fréchet space and continuous seminorm \(q\), the absolute version is the infimum of \(p>0\) for which every \(\sum q(x_n)^p\) is finite. The strong version uses the vanishing tail of

\[
\sup_{|\phi|\le q}\left(\sum_{n>N}|\phi(x_n)|^p\right)^{1/p}.
\]

At \(p=1\) the latter is unconditional summability in the complete locally convex topology. Both extend scalar power-summability order, are invariant under reindexing and equivalent seminorm systems, and behave monotonically under continuous linear maps. In \(\ell^2\), the sequence \(e_n/n\) has absolute order \(1\) and strong order \(2/3\), so the distinction is real. H0DT.37–38 prove these statements, including the range \(0<p<1\). The related published sequence paper is used for historical context, not as evidence that our entire exponent scale is written on scan 115 (Grothendieck, 1956b, §2, pp. 3–6 of the opened retypesetting).

For either chosen sequence order, the closed absolutely convex hull construction is a well-defined extended-valued invariant. Finite-order witnesses are null sequences and have compact closed absolutely convex hulls; a bounded set with noncompact closure consequently has infinite order. Exact-order and at-most-order witnesses give the same infimum in a nonzero space by adjoining a scalar sequence of the required order. The zero space distinguishes the literal exact-positive-order reading from our order-bound convention; that case is explicitly recorded. No unproved assertion that every compact set has finite order is added. The programme remains labelled programme in the ledger; its stated, supported precise versions are individually decided.

### 3.5 Period sources, later matches and limits of the historical inference

Poincaré’s genus-zero estimates (1883, pp. 136–138), Hadamard’s coefficient/genus discussion (1893, §33, p. 209), and Valiron’s systematic factorization statement (1925, Theorem XXIX, p. 24) provide period context. These works were in print by 1925. The manuscript names Hadamard and Hadamard–Borel, but supplies no bibliography proving which book or paper he consulted. This entry therefore separates a checked historical match from a claim about his reading or the date of composition.

The Hilbert determinant product has an exact match in Grothendieck’s Bourbaki exposé. Its talk date is March 1954, while the opened text ends with a June 1957 date and cites his 1956 article. Accordingly, the revised wording is cited as 1954/1957 and is not silently backdated. The modern trace-class product is also stated by Koutsonikos-Kouloumpis and Lesch (2024, §1.2, p. 2, equation 1.1); their next page treats regularized determinants. That extension is context, not a replacement for the manuscript’s exact Hilbert trace-class hypotheses.

No listed precise mathematical question remains open after the proofs and counterexamples in this entry. This is a conclusion about this inventory, not a claim that the surrounding theories have no open problems. The dating of the leaves, the faint argument on 120.7, several small indices and the scope of the normalization on 119 remain documentary qualifications. No uniqueness of an unwritten vector-order definition and no novelty of our completions are claimed. `REFERENCES_CHECKED.md` and `work/LITERATURE_SEARCH.md` distinguish opened theorem statements, bibliographical leads, unsuccessful zbMATH access and the limited negative EGA/SGA search.

## 4. His statements and their verdicts

Each item below separates the French statement or close paraphrase from our modern formulation. Short phrases in quotation marks are his; connected paraphrases retain his notation and order. The status concerns the written assertion in its historical setting. **Slip** identifies an evident local repair or omitted convention, with a literal counterexample and the evidence for the repair in `PROOFS.tex`. **False** is used for the mathematically wrong order-one example. **Known** includes an exact opened source and locator. Confidence describes the individual row, not an undifferentiated confidence score for the whole archive.

Every item has a dated check record in `CHECK_EVENTS.tsv`. The second audit was conducted by the same agent in a separate pass, in accordance with the one-stream instruction; it is not represented as an independent human review or formal verification. `work/SECOND_CHECK.md` records the alternative derivations and the audit correction. Stable IDs are displayed in manuscript order, so the later-discovered H0DT.69 comes first.

### H0DT.2 — 1/071.10–13 (live Corollaire 3, formula 5); repeated at 1/079.1–8

**His statement.**

« Corollaire 3 » : |α_n(u)|≤α_n(|u|)=‖Λⁿu‖₁≤‖u‖₁ⁿ/n!. Il le déduit de la formule de trace et de la puissance extérieure de |u|. Sur 1/079, « Corollaire 4 » reprend la majoration des coefficients par ceux de l’hermitien positif h; « Corollaire 5 » donne |det(1+zu)|≤det(1+|z|h).

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** For a trace-class operator u on a complex Hilbert space and every integer n≥0, |α_n(u)|≤α_n(|u|)=‖Λⁿu‖₁≤‖u‖₁ⁿ/n!. For every complex z, |det(I+zu)|≤det(I+|z||u|). The alternative positive square root h=(uu*)^(1/2) has the same nonzero singular spectrum, so it gives the same radial majorant.

**Reconstruction or correction, ours.** The same coefficient claim occurs first on 71 and is repeated on 79; both occurrences are retained under one stable id. Separate coefficient domination from radial domination; h and |u| give the same determinant. The exterior-power norm identity and factorial bound are proved as well.

**Status: True as written.** PROOFS.tex, H0DT.2. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** These coefficient bounds support the Hilbert determinant product published in Grothendieck (1954/1957), exposé 91, §4(c), p. 383. The trace-class product itself is also stated by Koutsonikos-Kouloumpis and Lesch (2024), §1.2, p. 2, (1.1); this does not claim that their displayed product is a separate printed statement of every bound here.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.2; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.69 — 1/071.16 (Corollaire 4, formula 6)

**His statement.**

« Corollaire 4 » : |det(1+u)|≤det(1+|u|). Le signe est ≤ sur le scan, contre = dans la transcription fournie.

**How he left it:** stated. **Date:** Undated manuscript. The catalogue dates a letter to 1953, not these leaves.

**Today’s precise statement, ours.** For every trace-class operator A on a complex Hilbert space, |det(I+A)|≤det(I+|A|); more generally |det(I+zA)|≤det(I+|z||A|).

**Reconstruction or correction, ours.** The reading differs from the supplied equality on direct visual evidence. A scalar A=−1 refutes that alternative equality, not his written inequality.

**Status: True as written.** PROOFS.tex, H0DT.69. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** The same radial majorant is written explicitly at 1/079, formula (19); it underlies the genus-zero Hilbert determinant product published in Grothendieck, exposé 91, §4(c), p. 383.

**Check and confidence.** CHECK_EVENTS.tsv, H0DT.69; second-pass record in `work/SECOND_CHECK.md`. High: native-resolution ink and a complete proof agree.

### H0DT.1 — 1/071.17–25 (Théorème 1 and formulas 7–10)

**His statement.**

« Théorème 1 » : si u∈L¹(E), (λ_i(u))∈l¹ et det(1+zu) est de « genre 0 »; det(1+zu)=∏_i(1+zλ_i(u)). Les coefficients sont les sommes symétriques des λ_i; pour n=1, Tr u=Σ_i λ_i(u). Pour |u|, les mêmes sommes donnent ||Λⁿu||₁.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** For a complex Hilbert space E and trace-class u, the eigenvalues with algebraic multiplicity are absolutely summable; the normalized Fredholm determinant is a genus-zero product. Its coefficients, trace, and positive-operator exterior-power norms have the stated absolutely convergent spectral sums.

**Reconstruction or correction, ours.** Hilbert setting inherited from the surrounding section; multiplicities, nonzero eigenvalues and α₀=1 are explicit in our formulation.

**Status: Known.** PROOFS.tex, H0DT.1; Grothendieck1954_1957, §4(c), p. 383; KoutsonikosLesch2024, §1.2, p. 2, (1.1). The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Exact published counterpart: Grothendieck (1954/1957), exposé 91, §4(c), p. 383. Modern statement: Koutsonikos-Kouloumpis and Lesch (2024), §1.2, p. 2, (1.1) and following paragraph.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.1; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.3 — 1/079.11–20 and cancelled margin

**His statement.**

Dans le « Théorème 2 » biffé, les valeurs propres d’un opérateur de Fredholm sur un Hilbert sont sommables et det(1+u)=∏(1+λ_i). Le corollaire biffé donne le genre 0 de det(1+zu), puis les sommes symétriques et la trace.

**How he left it:** cancelled. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** The same Hilbert trace-class product and coefficient theorem as H0DT.1, retained as a cancelled occurrence.

**Reconstruction or correction, ours.** Cancellation is not evidence of falsity; no extension to all nuclear Banach-space operators is asserted.

**Status: Known.** PROOFS.tex, H0DT.3; Grothendieck1954_1957, §4(c), p. 383. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Exact published counterpart: Grothendieck (1954/1957), exposé 91, §4(c), p. 383. Modern statement: Koutsonikos-Kouloumpis and Lesch (2024), §1.2, p. 2, (1.1) and following paragraph.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.3; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.4 — 1/080.1–26 and cancelled margin

**His statement.**

Le raisonnement biffé veut ramener le déterminant au cas hermitien positif. Une projection donne |z₁+…+z_n|≤||u||₁; la marge annonce Σ|λ_i|≤||u||₁ au numéro suivant. Avec la sommabilité des inverses des zéros et la majoration des coefficients par une série de genre 0, « il reste … seulement » à traiter det(1+zh).

**How he left it:** cancelled. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** The determinant proof reduces to the scalar criterion H0DT.21, the spectral identification of its zeros, absolute summability of eigenvalues, and the direct positive-operator product.

**Reconstruction or correction, ours.** Supply algebraic multiplicities through invariant generalized eigenspaces. Uniform bounds for arbitrary finite subfamily sums already imply absolute summability (constant 4 suffices); the phase contraction gives the sharper constant 1. An ordered-partial-sum counterexample is not applied to this stronger quantifier.

**Status: True as written.** PROOFS.tex, H0DT.4. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Exact published counterpart: Grothendieck (1954/1957), exposé 91, §4(c), p. 383. Modern statement: Koutsonikos-Kouloumpis and Lesch (2024), §1.2, p. 2, (1.1) and following paragraph.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.4; second-pass record in `work/SECOND_CHECK.md`. High for the reduction and finite-subfamily quantifier; medium for deciphering every cancelled word. The marginal announcement is retained.

### H0DT.5 — 1/107.1–10

**His statement.**

« Décomposition en facteurs des fonctions entières »; « Théorème 1 (Weierstrass) ». Pour f entière, f(0)≠0, et ses zéros a_n rangés en modules croissants, il existe des entiers croissants p_n≥0 et g entière tels que f=e^g∏(1−z/a_n)exp(z/a_n+…+z^{p_n}/(p_n a_n^{p_n})); convergence uniforme absolue sur toute région bornée.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** Every nonzero entire f with f(0)≠0 has the displayed Weierstrass factorization; one may take p_n=n, with zeros repeated by multiplicity and local absolute uniform convergence of the product tail.

**Reconstruction or correction, ours.** State multiplicities and the interpretation of convergence on compact sets containing zeros.

**Status: Known.** PROOFS.tex, H0DT.5; Valiron1925, §1, pp. 1–2; McMullen2025, Theorem 3.3, pp. 82–83. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Already classical: Valiron (1925), §1, pp. 1–2; McMullen (2025), Theorem 3.3, pp. 82–83.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.5; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.6 — 1/107.11–17

**His statement.**

Si Σ|r/a_n|^{p_n+1}<∞ pour tout r, cette suite d’entiers peut servir dans (1). Si Σ|a_n|^{−k−1}<∞, on peut choisir un degré constant p≤k; (2) est écrit avec le degré k.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** The displayed convergence criterion is sufficient for those primary factors; summability at k+1 permits degree k, or the least permissible p≤k, with a correspondingly adjusted residual entire function.

**Reconstruction or correction, ours.** Distinguish the two permissible choices p and k rather than forcing them to denote the same residual factor.

**Status: Known.** PROOFS.tex, H0DT.6; Valiron1925, §1, pp. 1–2 (admissible Weierstrass factors). The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Valiron (1925), §1, pp. 1–2; the fixed-degree construction remains standard.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.6; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.7 — 1/108.1–9

**His statement.**

« Genre d’une fonction entière ». On prend le plus petit k≥0 tel que Σ|a_n|^{−k−1}<∞. Si g dans (2) est un polynôme de degré r, le plus « grand » de r,k est le genre; g est déterminée à une constante près.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** With the minimal canonical degree p, the residual logarithm is unique modulo 2πiZ; if it is polynomial, genus is max(p,deg g). Otherwise genus is not finite.

**Reconstruction or correction, ours.** Constants have degree zero for genus; a finite zero at the origin is factored out. The visible replacement of petit by grand is retained.

**Status: True as written.** PROOFS.tex, H0DT.7. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Valiron (1925), §14, p. 24 explicitly uses the maximum of primary genus and polynomial degree; some modern notes use genus for the primary degree alone.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.7; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.8 — 1/108.10–11

**His statement.**

Si f est de genre ≤r, « on peut l’écrire » sous la forme (3), avec les facteurs exponentiels jusqu’au degré commun r et un polynôme de degré ≤r.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** A finite-genus function of genus at most r admits a common-degree-r canonical product and an exponential polynomial of degree at most r.

**Reconstruction or correction, ours.** Terminal small indices remain palaeographically doubtful; our formula is the precise identity with E_r and the absolutely convergent power sums.

**Status: True as written.** PROOFS.tex, H0DT.8. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Classical entire-function theory; exact factorization synthesis in Valiron (1925), §14, Theorems XXVII–XXIX, pp. 23–24; modern formulation in McMullen (2025), Theorem 3.16, p. 89.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.8; second-pass record in `work/SECOND_CHECK.md`. High for the proposition and proof; medium for terminal handwritten subscripts.

### H0DT.9 — 1/108.12–15

**His statement.**

« Dire que f(z) est de genre zéro » signifie f(z)=Cte×∏(1−z/a_n), avec Σ|a_n|^{−1}<∞.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** Under the standing f(0)≠0 convention, this is exactly the genus-zero characterization; generally include a finite factor z^m.

**Reconstruction or correction, ours.** The zero-at-origin extension is ours and is not inserted into the quoted formula.

**Status: True as written.** PROOFS.tex, H0DT.9. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Classical entire-function theory; exact factorization synthesis in Valiron (1925), §14, Theorems XXVII–XXIX, pp. 23–24; modern formulation in McMullen (2025), Theorem 3.16, p. 89.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.9; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.10 — 1/108.16–20; 1/109.1

**His statement.**

« Ordre d’une fonction entière » : M(r)=Sup|f(z)| sur le cercle, ρ=limsup log log M(r)/log r; l’ordre est fini si une borne exp(r^k) existe. ρ est la borne inférieure des σ tels que M(r)≤exp(r^σ) « pour r assez grand ».

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** For nonconstant entire f, the double-logarithmic upper limit equals the infimum of positive eventual power-exponential bounds. Nonzero polynomials and constants have order zero.

**Reconstruction or correction, ours.** Use |z|=r; disk maximum is equivalent. Repair only the standard constant/log convention. The eventual qualifier on the next sheet is part of his statement.

**Status: True as written.** PROOFS.tex, H0DT.10. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Borel’s order terminology is described in Valiron (1925), §5, p. 6; the same growth definition is used in McMullen (2025), §3.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.10; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.11 — 1/109.2–5

**His statement.**

« Théorème 2 (Hadamard-Borel) » : si ρ est fini, pour tout ε>0, Σ′|a_n|^{−ρ−ε}<∞; le prime exclut les racines nulles.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** For a nonzero entire function of finite order ρ, all reciprocal powers of its nonzero zeros above ρ are summable, with multiplicities.

**Reconstruction or correction, ours.** Jensen’s formula and the nonnegative counting-integral argument are supplied in full.

**Status: Known.** PROOFS.tex, H0DT.11; Valiron1925, Theorem XXVI, p. 22; McMullen2025, Corollary 3.14, p. 86. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Valiron (1925), §13, Theorem XXVI, p. 22; McMullen (2025), Corollary 3.14, p. 86.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.11; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.12 — 1/109.6–10

**His statement.**

En supposant f(0)≠0, f(z)=e^{P(z)}∏(1−z/a_n)exp(z/a_n+…+z^p/(p a_n^p)), où p≤ρ et P est un polynôme de degré ≤ρ : « genre de f ≤ ordre de f ».

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** MAIN. A nonzero finite-order entire f factors as z^m e^P times a minimal fixed-degree canonical product, with p≤ρ and deg P≤ρ; its manuscript genus is at most ρ. In fact ρ=max(deg P, zero exponent).

**Reconstruction or correction, ours.** The z^m extension, minimal p, and complete minimum-modulus proof are ours; his displayed case has m=0.

**Status: Known.** PROOFS.tex, H0DT.12; Valiron1925, Theorem XXIX and following genus paragraph, p. 24; McMullen2025, Theorem 3.16, p. 89. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Classical entire-function theory; exact factorization synthesis in Valiron (1925), §14, Theorems XXVII–XXIX, pp. 23–24; modern formulation in McMullen (2025), Theorem 3.16, p. 89.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.12; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.13 — 1/109.11–14

**His statement.**

« Corollaire » : si ρ<1, ou si M(r)≤exp(r^μ) pour r assez grand avec 0<μ<1, f est de genre zéro et a la forme Cte×∏(1−z/a_n).

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** Order strictly less than one forces genus zero; use the inherited f(0)≠0 convention for the displayed product, or include z^m.

**Reconstruction or correction, ours.** The equivalence of the growth condition is eventual; no small-radius bound is imposed.

**Status: True as written.** PROOFS.tex, H0DT.13. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Classical entire-function theory; exact factorization synthesis in Valiron (1925), §14, Theorems XXVII–XXIX, pp. 23–24; modern formulation in McMullen (2025), Theorem 3.16, p. 89.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.13; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.14 — 1/109.15–16

**His statement.**

« Il est très facile de se convaincre » que l’ordre de f est ≤ son genre plus 1.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** For every nonzero finite-genus entire function, order ≤ genus+1.

**Reconstruction or correction, ours.** Proof by the global primary-factor bound and polynomial exponential growth.

**Status: True as written.** PROOFS.tex, H0DT.14. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Classical entire-function theory; exact factorization synthesis in Valiron (1925), §14, Theorems XXVII–XXIX, pp. 23–24; modern formulation in McMullen (2025), Theorem 3.16, p. 89.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.14; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.15 — 1/109.16–18

**His statement.**

La phrase attribue à ω,g « le genre et l’ordre », puis encadre ω−1≤g≤ω.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** The boxed inequality is correct with ω=order and g=genus. With the nouns as literally written it fails for ∏(1−z/n²).

**Reconstruction or correction, ours.** Slip judgment, ours: exchange the adjacent nouns, supported by the two preceding inequalities; do not change the ink or box.

**Status: Slip.** PROOFS.tex, H0DT.15. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Classical entire-function theory; exact factorization synthesis in Valiron (1925), §14, Theorems XXVII–XXIX, pp. 23–24; modern formulation in McMullen (2025), Theorem 3.16, p. 89.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.15; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.16 — 1/109.19–21a

**His statement.**

Comme le genre est entier, il est connu dès que l’ordre l’est, sauf si l’ordre ω est entier; on peut alors avoir g=ω ou g=ω−1.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** For noninteger finite order ρ, genus=floor(ρ); for integer q≥1, genus is q or q−1, and both occur. At order zero only genus zero occurs.

**Reconstruction or correction, ours.** Respect nonnegativity at the endpoint zero; explicit sharp examples are ours. The sentence lists alternatives, not an assertion of genus −1.

**Status: True as written.** PROOFS.tex, H0DT.16. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Classical entire-function theory; exact factorization synthesis in Valiron (1925), §14, Theorems XXVII–XXIX, pp. 23–24; modern formulation in McMullen (2025), Theorem 3.16, p. 89.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.16; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.17 — 1/110.1–2

**His statement.**

« P. ex. » e^{z^ω} est d’ordre ω et de genre ω.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** For an integer ω≥0, the entire monomial exponential has order and genus ω.

**Reconstruction or correction, ours.** The integer-monomial convention is explicit in our version, consistent with the preceding integer-order discussion.

**Status: True as written.** PROOFS.tex, H0DT.17. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Classical entire-function theory; exact factorization synthesis in Valiron (1925), §14, Theorems XXVII–XXIX, pp. 23–24; modern formulation in McMullen (2025), Theorem 3.16, p. 89.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.17; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.18 — 1/110.2–3

**His statement.**

Pour α>1, ∏_n(1−z/n^α) est écrit d’ordre « 1 (sauf erreur) » et de genre 0.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** For every α>1 this is genus zero and has order exactly 1/α, so the asserted order 1 is false.

**Reconstruction or correction, ours.** The ink is retained. Correct the value to 1/α; a different product with roots n log²(n+1) realizes order 1 and genus 0 if that was the intended illustrative purpose.

**Status: False.** PROOFS.tex, H0DT.18. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Classical entire-function theory; exact factorization synthesis in Valiron (1925), §14, Theorems XXVII–XXIX, pp. 23–24; modern formulation in McMullen (2025), Theorem 3.16, p. 89.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.18; second-pass record in `work/SECOND_CHECK.md`. High for the visible plain 1 and the exact order 1/alpha; medium for the interpretive distinction between a false illustrative example and an intended pen slip.

### H0DT.19 — 1/110.4–9

**His statement.**

L’ordre du produit est au plus le maximum des deux ordres; « même chose pour la somme ». Les fonctions d’ordre <μ, respectivement ≤μ, forment une algèbre.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** Order(fg) and order(f+g) are at most max(order f,order g). With zero included, the classes at a positive cutoff μ are complex algebras; the non-strict zero cutoff also gives an algebra.

**Reconstruction or correction, ours.** State the zero-function and cutoff conventions explicitly; no claim of equality or of unitality at a vacuous cutoff.

**Status: True as written.** PROOFS.tex, H0DT.19. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Remains an elementary consequence of canonical products, Jensen’s formula, or summation by parts; no distinct later theorem or priority claim is established by this run.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.19; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.20 — 1/110.10–12

**His statement.**

« Théorème 3 (Hadamard) » : pour f(z)=Σc_nz^n, si n^α√[n]{|c_n|}→0, alors le genre est au plus 1/α.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** With α>0, the hypothesis implies log M_f(r)=o(r^{1/α}), hence order≤1/α and genus≤1/α. Without positive α the written statement is false or undefined.

**Reconstruction or correction, ours.** Slip, ours: supply the standard positive-exponent convention. Counterexample α=−1, f=e^z; the stronger minimal-type estimate is proved.

**Status: Slip.** PROOFS.tex, H0DT.20. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Hadamard (1893), introduction pp. 171–172 and §33 p. 209 discuss coefficient/genus converses; the exact modern implication here follows from the checked finite-order factorization.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.20; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.21 — 1/111.1–6; proof 1/111.8–1/112.23

**His statement.**

Si les coefficients de f sont majorés en module par ceux d’une fonction h de genre 0, et si les racines non nulles z_i de f vérifient Σ1/|z_i|<∞, alors f est de genre zéro.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** For nonzero entire f,h with coefficientwise modulus domination, h genus zero, and summable reciprocal nonzero zeros of f, f has genus zero.

**Reconstruction or correction, ours.** Complete the proof through a positive radial majorant, the corrected rotation and sector, and a three-rotation Liouville contradiction; include zero-free and zero-at-origin cases.

**Status: True as written.** PROOFS.tex, H0DT.21. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** The determinant use is explicit in the cancelled scan 80 and published in Grothendieck’s Hilbert-space Fredholm theorem (exposé 91, §4(c), p. 383); no separate exact publication of this scalar formulation was identified.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.21; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.22 — 1/111.8–10

**His statement.**

On peut supposer h de la forme Cte×Σ_i(1+α_i z), avec α_i>0 et Σα_i<∞; le signe écrit devant les facteurs est une somme.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** A positive product majorant exists, with Π replacing the written Σ; the literal infinite sum diverges at z=0.

**Reconstruction or correction, ours.** Slip, ours: use absolute reciprocal roots and finite factors (1+z) for any origin zero. Keep the supplied sum sign in his_words.

**Status: Slip.** PROOFS.tex, H0DT.22. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Remains an elementary consequence of canonical products, Jensen’s formula, or summation by parts; no distinct later theorem or priority claim is established by this run.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.22; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.23 — 1/111.14–17

**His statement.**

Pour supposer β>0 dans f=e^{α+βz}z^m∏(1−z/z_i), il remplace f(z) par f(Θz) avec Θ=β/|β|.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** For β≠0, the multiplier giving positive coefficient is conjugate(β)/|β|; β=i refutes the written multiplier.

**Reconstruction or correction, ours.** Slip, ours: add conjugation in the reconstruction only; coefficient moduli and zero moduli are invariant under unit rotation.

**Status: Slip.** PROOFS.tex, H0DT.23. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Remains an elementary consequence of canonical products, Jensen’s formula, or summation by parts; no distinct later theorem or priority claim is established by this run.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.23; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.24 — 1/111.18–21

**His statement.**

Toute fonction de genre zéro, telle h, admet |h(z)|≤Cte exp(ε|z|), où ε peut être pris « arbitraire ».

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** For every ε>0, a genus-zero entire h satisfies |h(z)|≤C_ε exp(ε|z|) for all z.

**Reconstruction or correction, ours.** The constant may depend on ε; a finite head and a small reciprocal-root tail prove the full quantifier.

**Status: True as written.** PROOFS.tex, H0DT.24. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Poincaré (1883), pp. 137–138, gives the early genus-zero growth argument; this remains the standard minimal exponential-type estimate.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.24; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.25 — 1/112.1–6

**His statement.**

Il choisit θ entre π/3 et π et affirme x≥c|z| avec c>0 dans −θ≤arg z≤θ, puis minore |f(z)| par exp(c|z|)|z|^m∏|1−z/z_i|.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** After the rotation has made β a positive real number, let f(z)=exp(α+βz)g(z), where α∈ℂ and g is entire. The valid choice π/3<θ<π/2 gives Re z≥cos θ |z| for |arg z|≤θ, and therefore |f(z)|≥|exp(α)|exp(β cos θ |z|)|g(z)| on that sector. The assertion at z=0 is understood by continuity.

**Reconstruction or correction, ours.** Slip, ours: correct the sector endpoint and retain/absorb the fixed positive constant and β when naming the exponential rate. θ=2π/3 refutes the written range.

**Status: Slip.** PROOFS.tex, H0DT.25. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Remains an elementary consequence of canonical products, Jensen’s formula, or summation by parts; no distinct later theorem or priority claim is established by this run.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.25; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.26 — 1/112.7–10 and margin 23

**His statement.**

Il écrit |f(z)|≤|h(z)|≤Cte exp(ε|z|), puis choisit ε<c pour obtenir une décroissance exponentielle de g dans le secteur.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** Coefficient domination gives |f(z)|≤Σ|h_n||z|^n, hence a type-zero radial bound; it does not imply the written pointwise |h(z)| comparison.

**Reconstruction or correction, ours.** Slip, ours: use h(|z|) after positive-coefficient replacement. A pair of degree-one polynomials refutes the same-argument comparison inside the sector.

**Status: Slip.** PROOFS.tex, H0DT.26. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Remains an elementary consequence of canonical products, Jensen’s formula, or summation by parts; no distinct later theorem or priority claim is established by this run.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.26; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.27 — 1/112.11–23

**His statement.**

Pour g=z^m∏(1−z/z_i), l’inégalité de décroissance dans le secteur force g « constante ». Avec ω=e^{2iπ/3}, G=g(z)g(ωz)g(ω²z) est bornée, donc constante; G=z^{3m}∏(1−z³/z_i³). La marge exclut alors le facteur e^{βz}.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** A nonzero entire type-zero g cannot decay exponentially on a sector of half-angle greater than π/3. The three rotated factors give a globally decaying entire G, hence G=0, a contradiction.

**Reconstruction or correction, ours.** The live word constante is retained; zero is our subsequent consequence of the decay bound. Constants and empty zero sets are handled explicitly.

**Status: True as written.** PROOFS.tex, H0DT.27. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Remains an elementary consequence of canonical products, Jensen’s formula, or summation by parts; no distinct later theorem or priority claim is established by this run.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.27; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.28 — 1/113.1–7, 10–12

**His statement.**

Pour α_n>0 décroissante vers zéro, ρ est l’infimum des s>0 donnant α_n=O(n^{−1/s}); σ est l’infimum des s>0 donnant Σα_n^s<∞. Le « critère de Riemann » donne σ≤ρ, et le lemme donne ρ≤σ.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** These two extended nonnegative exponents are equal, with inf empty=∞; convergence at the boundary exponent is not asserted.

**Reconstruction or correction, ours.** Proof includes both implications and the endpoint conventions.

**Status: True as written.** PROOFS.tex, H0DT.28. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Remains an elementary consequence of canonical products, Jensen’s formula, or summation by parts; no distinct later theorem or priority claim is established by this run.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.28; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.29 — 1/113.8

**His statement.**

« On a aussi » 1/ρ=limsup_n log(1/α_n)/log n; la limite supérieure est celle que montre l’encre.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** The correct reciprocal formula uses liminf, not limsup. Equivalently ρ=limsup log n/log(1/α_n).

**Reconstruction or correction, ours.** Slip judgment, ours, supported by the preceding infimum definition. A positive monotone block sequence has ρ=1, liminf=1 and limsup=2.

**Status: Slip.** PROOFS.tex, H0DT.29. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Remains an elementary consequence of canonical products, Jensen’s formula, or summation by parts; no distinct later theorem or priority claim is established by this run.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.29; second-pass record in `work/SECOND_CHECK.md`. High for counterexample and corrected formula; medium for classifying the reversal as a pen slip rather than a conceptual error.

### H0DT.30 — 1/113.13–23

**His statement.**

Le lemme est renforcé par insertion : si Σα_n^s<∞, alors α_n=o(n^{−1/s}), « α_n étant décroissant ! ». La preuve regroupe les termes entre n_{i−1} et n_i.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** For nonnegative nonincreasing a_n and s>0, finite s-power sum implies n^{1/s}a_n→0.

**Reconstruction or correction, ours.** Both the short dyadic-tail proof and the corrected starting index in his block proof are supplied.

**Status: True as written.** PROOFS.tex, H0DT.30. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Remains an elementary consequence of canonical products, Jensen’s formula, or summation by parts; no distinct later theorem or priority claim is established by this run.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.30; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.31 — 1/114.1–19

**His statement.**

Si Σα_i<∞, l’exposant ρ de la suite positive est aussi l’ordre de f(z)=∏(1+α_i z). Pour α_n=n^{−β}, il sépare à ν, majore la queue par exp(rΣ_{n>ν}n^{−β}), et prend ν=[r^{1/β}]+1.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** For a summable nonnegative sequence, the positive canonical product has order equal to its power-summability exponent. For β>1 the model order is exactly 1/β.

**Reconstruction or correction, ours.** Handle ρ=1 separately by the genus-zero bound; the displayed finite-head and tail estimates prove the comparison for ρ<1.

**Status: True as written.** PROOFS.tex, H0DT.31. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Classical entire-function theory; exact factorization synthesis in Valiron (1925), §14, Theorems XXVII–XXIX, pp. 23–24; modern formulation in McMullen (2025), Theorem 3.16, p. 89.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.31; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.32 — 1/114.20–22

**His statement.**

« Rappelons » : si f(r)=Σa_nr^n et B(r)=Sup_n(a_nr^n), alors ordre f=limsup log log B(r)/log r.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** The formula is true for the local nonnegative coefficients. For arbitrary complex coefficients take B(r)=sup_n |a_n|r^n.

**Reconstruction or correction, ours.** Cauchy gives B(r)≤M(r), while M(r)≤2B(2r); constant-function convention stated.

**Status: True as written.** PROOFS.tex, H0DT.32. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Maximum-term comparison is treated in Valiron (1925), §§4–5, pp. 5–7; the elementary two-radius estimate suffices here.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.32; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.33 — 1/115.1–7

**His statement.**

Pour f(z)=∏(1+λ_i z) dit de « genre 1 », il pose α_i=|λ_i| et F(z)=∏(1+α_i z), et affirme que f et F ont le même ordre.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** With absolute summability Σ|λ_i|<∞, both products have genus zero and the same order. The literal genus-one assertion need not define F at all.

**Reconstruction or correction, ours.** Slip, ours: replace genre 1 by genre 0, supported by the unregularized product and preceding page. Paired λ=±1/n provide the counterexample to the literal wording.

**Status: Slip.** PROOFS.tex, H0DT.33. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Classical entire-function theory; exact factorization synthesis in Valiron (1925), §14, Theorems XXVII–XXIX, pp. 23–24; modern formulation in McMullen (2025), Theorem 3.16, p. 89.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.33; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.34 — 1/115.8–11

**His statement.**

On peut parler de l’ordre d’un ensemble « dénombrable » de nombres complexes, non rangés en suite : inf{s>0:Σ|z_i|^s<∞}.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** This defines an enumeration-invariant extended exponent for a countable indexed family, with multiplicity. It agrees with the decreasing-rearrangement exponent when a summable power exists.

**Reconstruction or correction, ours.** Clarify indexed family versus deletion of repeated values and the finite/empty conventions.

**Status: True as written.** PROOFS.tex, H0DT.34. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Related published framework: Grothendieck (1956b), §2, pp. 3–6 of the opened retypeset version, distinguishes norm-power summability, scalar-power summability, and the completed injective sequence space. The manuscript does not identify a unique full exponent scale.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.34; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.35 — 1/115.11–12

**His statement.**

« Suite à décroissance rapide = d’ordre zéro ».

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** The equivalence is true for nonincreasing moduli, or for the decreasing rearrangement of an unordered family; it fails for arbitrary enumeration.

**Reconstruction or correction, ours.** Slip, ours: carry the monotone/rearrangement convention from 113. Explicit sparse large-index values give all power sums finite without rapid decay in that enumeration.

**Status: Slip.** PROOFS.tex, H0DT.35. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Related published framework: Grothendieck (1956b), §2, pp. 3–6 of the opened retypeset version, distinguishes norm-power summability, scalar-power summability, and the completed injective sequence space. The manuscript does not identify a unique full exponent scale.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.35; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.36 — 1/115.13–15

**His statement.**

« Ordre d’une suite » dans un espace de Banach ou de Fréchet : « deux définitions », suivant la sommabilité forte ou la sommabilité absolue.

**How he left it:** programme. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** The programme supports two distinct summability extensions; their precise well-defined versions and strict separation are H0DT.37 and H0DT.38. No unique vector-power criterion is written on the page.

**Reconstruction or correction, ours.** Programme row retained in the ledger; the two versions, their hypotheses and their proofs are ours. The status covers the stated distinction, not an invented conjecture.

**Status: True as written.** PROOFS.tex, H0DT.36. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Related published framework: Grothendieck (1956b), §2, pp. 3–6 of the opened retypeset version, distinguishes norm-power summability, scalar-power summability, and the completed injective sequence space. The manuscript does not identify a unique full exponent scale.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.36; second-pass record in `work/SECOND_CHECK.md`. High for the textual distinction and the proved versions; medium for choosing a particular full p-scale, which is explicitly ours.

### H0DT.37 — 1/115.13–15 [absolute version of programme]

**His statement.**

La « sommabilité absolue » est l’une des deux voies nommées; la page ne donne pas sa formule vectorielle détaillée.

**How he left it:** programme. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** Our precise version: σ_a(x)=inf{p>0:Σq(x_n)^p<∞ for every continuous seminorm q} on a Hausdorff Fréchet space. It is intrinsic, permutation invariant, monotone under continuous linear maps, and agrees with scalar order.

**Reconstruction or correction, ours.** The entire displayed definition and its stated properties are ours; it is a supported completion rather than a quotation.

**Status: True as written.** PROOFS.tex, H0DT.37. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Related published framework: Grothendieck (1956b), §2, pp. 3–6 of the opened retypeset version, distinguishes norm-power summability, scalar-power summability, and the completed injective sequence space. The manuscript does not identify a unique full exponent scale.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.37; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.38 — 1/115.13–15 [strong version of programme]

**His statement.**

La « sommabilité forte » est l’autre voie nommée; aucun choix de puissance vectorielle n’est écrit.

**How he left it:** programme. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** Our precise version uses vanishing uniform weak-p tails W_{p,q}(N)=sup_{|φ|≤q}(Σ_{n>N}|φ(x_n)|^p)^{1/p}. The exponent σ_u is intrinsic, agrees with scalar order, satisfies σ_u≤σ_a, and at p=1 gives unconditional strong summability. For x_n=e_n/n in ℓ², σ_u=2/3 and σ_a=1.

**Reconstruction or correction, ours.** The full p-scale is ours, with completeness for the unconditional-sum interpretation; it is not identified with mere scalar summability at an endpoint.

**Status: True as written.** PROOFS.tex, H0DT.38. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Related published framework: Grothendieck (1956b), §2, pp. 3–6 of the opened retypeset version, distinguishes norm-power summability, scalar-power summability, and the completed injective sequence space. The manuscript does not identify a unique full exponent scale.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.38; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.39 — 1/115.16–18

**His statement.**

L’ordre d’une partie bornée est la « borne inférieure » (remplaçant plus petit) des s>0 tels que cette partie soit contenue dans l’enveloppe convexe cerclée fermée d’une suite d’ordre s.

**How he left it:** programme. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** For a Hausdorff Fréchet space E and a bounded subset B, choosing either of H0DT.37–38 makes the written hull infimum a well-defined extended value. Our order-bound convention is inclusion-monotone and decreases under continuous linear maps; every bounded subset of a finite-dimensional space has order zero, while a bounded set with noncompact closure has infinite order. The literal exact-positive-order convention agrees in every nonzero E; in E={0} it instead has empty witness set and value +∞. No choice between these conventions is attributed to the page.

**Reconstruction or correction, ours.** Specify the chosen sequence notion, absolute convex hull, infinity convention, and equivalent <s/≤s formulations under the infimum. Added properties are ours and are proved. Our order-bound formulation agrees with exact positive order in nonzero spaces by padding with a scalar sequence; in the zero space the exact-order literal infimum is infinity, whereas the at-most-order convention gives zero. Both are explicitly distinguished.

**Status: True as written.** PROOFS.tex, H0DT.39. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Related published framework: Grothendieck (1956b), §2, pp. 3–6 of the opened retypeset version, distinguishes norm-power summability, scalar-power summability, and the completed injective sequence space. The manuscript does not identify a unique full exponent scale.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.39; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.40 — 1/116.1–4

**His statement.**

Pour r_ν>0 croissant vers l’infini, n(r)=#{ν:r_ν≤r}; avec 0≤a≤b<∞, la somme sur a<r_ν<b est n(b−0)/b^α−n(a+0)/a^α+α∫_a^b n(r)r^{−α−1}dr.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** The finite open-interval identity is valid for α>0 and 0≤a<b<∞, with zero boundary convention at a=0. Equality a=b at an atom invalidates the written one-sided boundary difference.

**Reconstruction or correction, ours.** Slip, ours: replace a≤b by a<b, supported by the strict annulus on 118. Retain both endpoint exclusions and one-sided counts.

**Status: Slip.** PROOFS.tex, H0DT.40. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Remains an elementary consequence of canonical products, Jensen’s formula, or summation by parts; no distinct later theorem or priority claim is established by this run.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.40; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.41 — 1/116.5–7

**His statement.**

La série Σr_ν^{−α} converge si et seulement si l’intégrale ∫_0^∞n(r)r^{−α−1}dr converge.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** For α>0, Σr_ν^{−α}=α∫_0^∞n(r)r^{−α−1}dr as an extended nonnegative identity.

**Reconstruction or correction, ours.** Use Tonelli to prove the equivalence without first assuming a boundary limit.

**Status: True as written.** PROOFS.tex, H0DT.41. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Remains an elementary consequence of canonical products, Jensen’s formula, or summation by parts; no distinct later theorem or priority claim is established by this run.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.41; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.42 — 1/116.7–8; proof 1/117.1–7

**His statement.**

Dans ce cas n(r)/r^α→0. La preuve choisit des blocs disjoints; les bornes nommées b_i deviennent λ_i dans les formules.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** Convergence of the reciprocal α-power sum forces r^{−α}n(r)→0.

**Reconstruction or correction, ours.** A finite-head/tail proof is supplied; the b_i/λ_i switch is a harmless name slip recorded in READINGS, not a new sequence hypothesis.

**Status: True as written.** PROOFS.tex, H0DT.42. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Remains an elementary consequence of canonical products, Jensen’s formula, or summation by parts; no distinct later theorem or priority claim is established by this run.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.42; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.43 — 1/116.9; 1/117.8–9

**His statement.**

La formule de queue écrit Σ_{r_ν>a}1/r_ν=−n(a)/a^α+α∫_a^∞n(r)r^{−α−1}dr.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** Under convergence, the left side must be Σ_{r_ν>a}r_ν^{−α}; with that exponent the formula is exact.

**Reconstruction or correction, ours.** Slip, ours: restore α, as in the preceding finite formula and the unchanged integral. For r_ν=2^ν, a=0, α=2 the literal two sides are 1 and 1/3.

**Status: Slip.** PROOFS.tex, H0DT.43. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Remains an elementary consequence of canonical products, Jensen’s formula, or summation by parts; no distinct later theorem or priority claim is established by this run.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.43; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.44 — 1/117.10–17

**His statement.**

« Des résultats analogues » valent pour λ(r) décroissante vers zéro, dérivable, avec μ=−λ′ : Σλ(r_ν) et ∫nμ convergent ensemble, λ(r)n(r)→0, et la somme de queue vaut −λ(a)n(a)+∫_a^∞nμ.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** For a nonincreasing C¹ weight tending to zero, the nonnegative sum equals the counting integral, with infinite values allowed. In the finite case the boundary limit and tail identity hold.

**Reconstruction or correction, ours.** State local smoothness, μ≥0, and the boundary convention; locally absolutely continuous weights also suffice.

**Status: True as written.** PROOFS.tex, H0DT.44. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Remains an elementary consequence of canonical products, Jensen’s formula, or summation by parts; no distinct later theorem or priority claim is established by this run.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.44; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.45 — 1/118.1–3

**His statement.**

Les r_ν sont les modules des zéros de f entière; « on aura » n(r)=(1/2π)∫_0^{2π}(f′(re^{iφ})/f(re^{iφ}))re^{iφ}dφ.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** The argument-principle count holds on circles without zeros, with f(0)≠0 for the nonzero-zero count; otherwise factor out the origin multiplicity.

**Reconstruction or correction, ours.** Slip, ours: make the standard exceptional-radius convention explicit. f=1−z, r=1 refutes an unrestricted ordinary contour-integral reading.

**Status: Slip.** PROOFS.tex, H0DT.45. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Jensen and argument-principle forms are classical; Valiron (1925), §13, pp. 21–22, (25), gives the relevant circular-mean formula.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.45; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.46 — 1/118.4–8

**His statement.**

Il échange les intégrations sur a<r<b et φ, « car les intégrales … doubles … sont convergentes ».

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** On a positive compact annulus, the weighted logarithmic derivative is absolutely area-integrable: its singularities are simple poles, whose absolute values are locally integrable in two real dimensions. Thus Fubini applies.

**Reconstruction or correction, ours.** Require continuous bounded weight on the annulus; later integration by parts requires its indicated derivative.

**Status: True as written.** PROOFS.tex, H0DT.46. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Remains an elementary consequence of canonical products, Jensen’s formula, or summation by parts; no distinct later theorem or priority claim is established by this run.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.46; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.47 — 1/118.8–14 and oblique annotation

**His statement.**

L’intégration radiale emploie Log f, en prenant une détermination principale; une annotation dit « en prenant les parties réelles ».

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** Principal Log is not a globally differentiable radial primitive across its branch cut. The real-part annotation repairs the subsequent real logarithmic-mean identity.

**Reconstruction or correction, ours.** Slip in the intermediate complex step, ours: use continuous radial branches or log|f|. f(z)=exp(iz), a=π/2, b=3π/2, μ=1/r gives a 2πi discrepancy. The annotation is retained.

**Status: Slip.** PROOFS.tex, H0DT.47. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Remains an elementary consequence of canonical products, Jensen’s formula, or summation by parts; no distinct later theorem or priority claim is established by this run.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.47; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.48 — 1/118.14–17

**His statement.**

Il pose V(r)=(1/2π)∫log|f(re^{iφ})|dφ et obtient ∫_a^b n(r)μ(r)dr=[rμ(r)V(r)]_a^b−∫_a^b V(r)d(rμ(r)).

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** For f(0)≠0, 0<a<b and μ∈C¹[a,b], Jensen gives locally absolutely continuous V with V′=n/r almost everywhere, proving this identity even across zero radii.

**Reconstruction or correction, ours.** Use a real absolutely continuous function; no principal-log branch assumption remains.

**Status: True as written.** PROOFS.tex, H0DT.48. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Remains an elementary consequence of canonical products, Jensen’s formula, or summation by parts; no distinct later theorem or priority claim is established by this run.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.48; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.49 — 1/118.18–21

**His statement.**

Avec μ=−λ′, la somme pondérée sur a<r_ν<b égale λ(b)n(b−0)−λ(a)n(a+0)−[rλ′V]_a^b+∫_a^b Vd(rλ′).

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** For a C² real weight on 0<a<b, the finite weighted zero identity holds with exactly the displayed plus sign on the final integral.

**Reconstruction or correction, ours.** C² is a convenient sufficient regularity; absolute continuity of rλ′ suffices. The finite formula itself need not assume monotonicity.

**Status: True as written.** PROOFS.tex, H0DT.49. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Remains an elementary consequence of canonical products, Jensen’s formula, or summation by parts; no distinct later theorem or priority claim is established by this run.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.49; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.50 — 1/119.1–2

**His statement.**

Si r²μ(r)→0 pour r→0 et |f(0)|=1, il fait a→0 : Σ_{r_ν<b}λ(r_ν)=λ(b)n(b−0)−bλ′(b)V(b)+∫_0^bVd(rλ′).

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** Under normalization and the local weight regularity, this endpoint-zero identity is valid; V and n vanish identically below the first zero, so the displayed decay condition on the weight is unnecessary.

**Reconstruction or correction, ours.** Stronger sufficiency proof by exact Jensen vanishing, retaining his condition in his_words.

**Status: True as written.** PROOFS.tex, H0DT.50. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Remains an elementary consequence of canonical products, Jensen’s formula, or summation by parts; no distinct later theorem or priority claim is established by this run.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.50; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.51 — 1/119.3–5

**His statement.**

« Comme |V(r)|≤M(r)=Sup|f(z)| », il annonce une majoration de ∫n(r)μ(r)dr en fonction de M.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** With the preceding |f(0)|=1 normalization, 0≤V≤log M≤M proves the written weaker bound. Without normalization, |V|≤M is false; generally log|f(0)|≤V≤log M.

**Reconstruction or correction, ours.** Scope judgment, ours: retain normalization from the immediate preceding line. The constant e^{−2} gives the standalone counterexample; an explicit weighted bound is supplied.

**Status: True as written.** PROOFS.tex, H0DT.51. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Remains an elementary consequence of canonical products, Jensen’s formula, or summation by parts; no distinct later theorem or priority claim is established by this run.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.51; second-pass record in `work/SECOND_CHECK.md`. High for the symbol M and the normalized mathematics; medium for scope across the parenthesis.

### H0DT.52 — 1/120.1–7

**His statement.**

Pour λ=(λ_i)∈l¹ et n>0, α_n(λ)=Σ_{i₁<…<i_n}λ_{i₁}…λ_{i_n}. Ce sont les coefficients d’une fonction entière de genre zéro, f(?)=∏(1+λ_i z).

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** The elementary symmetric sums are absolutely convergent continuous homogeneous polynomials and are precisely the Taylor coefficients of the locally uniformly convergent genus-zero product. Set α₀=1.

**Reconstruction or correction, ours.** The argument of f remains doubtful (λ/n/z); z is used only in the precise reconstruction, supported by 121.

**Status: True as written.** PROOFS.tex, H0DT.52. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Grothendieck (1956a), Introduction §2, p. 324, (13)–(14), supplies the historical entire-map definition. In modern language the example is globally holomorphic but not of bounded type.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.52; second-pass record in `work/SECOND_CHECK.md`. High for mathematics; low for the frozen handwritten argument of f.

### H0DT.53 — 1/120.4

**His statement.**

Il écrit α_n(λ)≤||λ||₁^n/n!, sans module autour de α_n.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** For complex inputs the valid sharp inequality is |α_n(λ)|≤α_n(|λ|)≤||λ||₁^n/n!.

**Reconstruction or correction, ours.** Slip, ours: insert modulus in the corrected statement; λ=(i,0,…) makes the literal real inequality meaningless.

**Status: Slip.** PROOFS.tex, H0DT.53. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Grothendieck (1956a), Introduction §2, p. 324, (13)–(14), supplies the historical entire-map definition. In modern language the example is globally holomorphic but not of bounded type.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.53; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.54 — 1/120.8–10

**His statement.**

On obtient « à un facteur constant près » les coefficients les plus généraux d’une fonction entière de genre zéro.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** This is exact for genus-zero functions nonzero at the origin. In full generality include C z^m, giving a shifted coefficient sequence.

**Reconstruction or correction, ours.** Slip if read without the inherited convention: f=z is a counterexample. The scope evidence is 107 f(0)≠0 and 108 formula (4).

**Status: Slip.** PROOFS.tex, H0DT.54. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Grothendieck (1956a), Introduction §2, p. 324, (13)–(14), supplies the historical entire-map definition. In modern language the example is globally holomorphic but not of bounded type.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.54; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.55 — 1/120.11–12

**His statement.**

« Proposition » : pour tout λ∈l¹, Σ_{n≥0}n!α_n(λ) est absolument convergente; S(λ) est sa somme.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** The series is absolutely convergent at every point of complex ℓ¹. It also equals ∫_0^∞e^{−t}∏_i(1+tλ_i)dt.

**Reconstruction or correction, ours.** The integral representation and finite-head/small-tail proof are ours; α₀=1 is explicit.

**Status: True as written.** PROOFS.tex, H0DT.55. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Grothendieck (1956a), Introduction §2, p. 324, (13)–(14), supplies the historical entire-map definition. In modern language the example is globally holomorphic but not of bounded type.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.55; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.56 — 1/120.13–14; 1/122.13–26

**His statement.**

S est holomorphe au voisinage de 0, « avec un rayon de convergence égal à 1 »; la continuation conclut R₀=R₁=1.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** Both the homogeneous polynomial-norm radius and the associated symmetric multilinear-norm radius at zero equal one. Pointwise convergence along every line has infinite radius.

**Reconstruction or correction, ours.** Distinguish these radii from the domain of global holomorphy; compute the exact homogeneous norms.

**Status: True as written.** PROOFS.tex, H0DT.56. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Grothendieck (1956a), Introduction §2, p. 324, (13)–(14), supplies the historical entire-map definition. In modern language the example is globally holomorphic but not of bounded type.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.56; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.57 — 1/120.15–16; 1/122 margin after line 4

**His statement.**

Les restrictions aux sous-espaces vectoriels complexes de dimension finie sont holomorphes; la marge de la continuation affirme la holomorphie sur l¹ à distance finie.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** S is in fact Fréchet-holomorphic at every λ∈ℓ¹, hence all its finite-dimensional restrictions are entire holomorphic.

**Reconstruction or correction, ours.** Supply local uniform convergence near each λ, which pointwise convergence alone would not justify.

**Status: True as written.** PROOFS.tex, H0DT.57. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Grothendieck (1956a), Introduction §2, p. 324, (13)–(14), supplies the historical entire-map definition. In modern language the example is globally holomorphic but not of bounded type.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.57; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.58 — 1/120.17–19; 1/122.24–26

**His statement.**

S « n’est pas bornée dans la boule unité » de l¹, et n’est par suite « pas une fonction entière » de λ.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** S is unbounded even on the open unit ball and fails Grothendieck’s historical entire-map definition (norm-root decay on every ball), although it is globally holomorphic in the modern sense.

**Reconstruction or correction, ours.** Translate the historical terminology with Grothendieck (1956a), p. 324, (13)–(14); do not refute it using today’s broader entire terminology.

**Status: True as written.** PROOFS.tex, H0DT.58. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Grothendieck (1956a), Introduction §2, p. 324, (13)–(14), supplies the historical entire-map definition. In modern language the example is globally holomorphic but not of bounded type.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.58; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.59 — 1/120.20–24

**His statement.**

« Corollaire » : √[n]{n!|α_n(λ)|}→0; √[n]{|α_n(λ)|}=o(1/n); α_n(λ)=ε_n^n/n! avec ε_n→0. Les coefficients de toute fonction de genre zéro ont ces propriétés.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** For every genus-zero entire function, its Taylor coefficients c_n satisfy (n!|c_n|)^{1/n}→0, equivalently |c_n|^{1/n}=o(1/n), equivalently c_n=ε_n^n/n! with complex ε_n→0.

**Reconstruction or correction, ours.** Allow constants, a finite zero at the origin and zero coefficients; choose any complex nth roots in the last representation.

**Status: True as written.** PROOFS.tex, H0DT.59. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Poincaré (1883), pp. 137–138, is the early growth/coefficient background; the bound follows from genus-zero type zero and the correct Cauchy estimate.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.59; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.60 — 1/120.25; 1/121.1–5

**His statement.**

Σn!α_n(λz)=Σn!α_n(λ)z^n converge pour tout z. Les deux autres relations sont équivalentes à la première, en tenant compte de « Stirling » : √[n]{n!}~n/e.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** Homogeneity and pointwise convergence of S on ℓ¹ give an entire scalar series on every line; the root test and (n!)^{1/n}~n/e give all coefficient equivalences.

**Reconstruction or correction, ours.** Prove the factorial estimate at the exact strength used by integral comparison, without relying on a stronger unproved asymptotic.

**Status: True as written.** PROOFS.tex, H0DT.60. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Grothendieck (1956a), Introduction §2, p. 324, (13)–(14), supplies the historical entire-map definition. In modern language the example is globally holomorphic but not of bounded type.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.60; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.61 — 1/121.7–14

**His statement.**

Pour λ_i>0 décroissants, l’« inégalité de Cauchy » est écrite α_n≤M(R)/R^{n+1}, puis le produit est séparé en n+1 facteurs initiaux.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** Cauchy gives α_n≤M(R)/R^n. The written bound fails already for f=1+z, n=1, R=2; a strictly positive infinite summable example is also supplied.

**Reconstruction or correction, ours.** Slip, ours: restore the contour-length factor R, then reindex the head consistently.

**Status: Slip.** PROOFS.tex, H0DT.61. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Grothendieck (1956a), Introduction §2, p. 324, (13)–(14), supplies the historical entire-map definition. In modern language the example is globally holomorphic but not of bounded type.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.61; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.62 — 1/121.15–18

**His statement.**

La queue vérifie ∏_{i=n+2}∞(1+λ_iR)≤exp(ρ_{n+1}R), ρ_{n+1}=Σ_{k=n+2}∞λ_k. Pour R=(n+1)/ρ_{n+1}, les facteurs vivants sont écrits e^n.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** The tail exponential estimate is true; the stated substitution produces e^{n+1}, not e^n. If the tail is zero, treat the polynomial case separately.

**Reconstruction or correction, ours.** Slip, ours: correct the exponent. A positive decreasing summable sequence makes the tail product exceed e^n at the written radius.

**Status: Slip.** PROOFS.tex, H0DT.62. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Grothendieck (1956a), Introduction §2, p. 324, (13)–(14), supplies the historical entire-map definition. In modern language the example is globally holomorphic but not of bounded type.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.62; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.63 — 1/121.19–22

**His statement.**

Comme λ_n=o(1/n) et ρ_n/n=o(1/n), il introduit des ε_n→0 et aboutit à une borne avec produit d’ε et (n+1)!; plusieurs indices sont décalés ou douteux.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** The valid bound is α_N≤e^N/N! ∏_{j=1}^N(ρ_j+jλ_j), with ρ_j=Σ_{i>j}λ_i and each factor tending to zero.

**Reconstruction or correction, ours.** Replace the entire inconsistent chain by our explicitly reindexed derivation; retain palaeographic ambiguity in the original epsilon subscripts. Literal-chain failure is witnessed by H0DT.61–62.

**Status: Slip.** PROOFS.tex, H0DT.63. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Grothendieck (1956a), Introduction §2, p. 324, (13)–(14), supplies the historical entire-map definition. In modern language the example is globally holomorphic but not of bounded type.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.63; second-pass record in `work/SECOND_CHECK.md`. High for the corrected bound and limits; medium for the small original epsilon subscripts.

### H0DT.64 — 1/122.1–5

**His statement.**

La continuation prend les racines n-ièmes, utilise (ε₁…ε_n)^{1/n}→0, et en déduit √[n]{n!α_n}→0 puis la convergence absolue de S.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** Geometric means of a nonnegative null sequence tend to zero; combined with H0DT.63 this proves the coefficient root limit and absolute convergence.

**Reconstruction or correction, ours.** The live conclusion is sound after the preceding correction; handle a zero factor separately. The proof does continue beyond scan 121.

**Status: True as written.** PROOFS.tex, H0DT.64. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Grothendieck (1956a), Introduction §2, p. 324, (13)–(14), supplies the historical entire-map definition. In modern language the example is globally holomorphic but not of bounded type.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.64; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.65 — 1/122.6–13

**His statement.**

La forme n fois linéaire associée à α_n est (1/n!)Σ_{indices distincts}λ^{(1)}_{i₁}…λ^{(n)}_{i_n}; il obtient ||α_n||≤1/n!, donc n!||α_n||≤1 et R₀≥1.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** The displayed absolutely convergent symmetric n-linear form has norm exactly 1/n!, diagonal α_n, and normalized norm one for n!α_n.

**Reconstruction or correction, ours.** Prove equality using distinct unit vectors; distinguish multilinear and diagonal polynomial norms, both computed.

**Status: True as written.** PROOFS.tex, H0DT.65. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Grothendieck (1956a), Introduction §2, p. 324, (13)–(14), supplies the historical entire-map definition. In modern language the example is globally holomorphic but not of bounded type.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.65; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.66 — 1/122.14–24

**His statement.**

Il prend a_i^{(m)}=1/m pour i≤m, sinon 0; ||a^{(m)}||₁=1 et n!α_n(a^{(m)})=∏_{j=0}^{n−1}(1−j/m)→1. Alors S(a^{(m)})→∞ et R₁≤1; donc R₀=R₁=1.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** The formulas and divergence are valid; finite initial sums prove S→∞, and exact polynomial/multilinear norms give both radii one.

**Reconstruction or correction, ours.** The open-ball variant and exact four-coordinate model computation 891/512 are ours.

**Status: True as written.** PROOFS.tex, H0DT.66. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Grothendieck (1956a), Introduction §2, p. 324, (13)–(14), supplies the historical entire-map definition. In modern language the example is globally holomorphic but not of bounded type.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.66; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.67 — 1/129.19–25; 1/130.1–7

**His statement.**

« Lemme 1 » : pour α_i≥0 et 0<p<1, f(z)=∏(1+α_i z), Σα_i^p=(p sin πp/π)∫_0^∞log f(r)r^{−1−p}dr; les deux membres peuvent être infinis. Le corollaire remplace α_i par les valeurs propres de |A|.

**How he left it:** stated. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** The identity is valid as an extended nonnegative real identity for every nonnegative family. For an entire complex product assume Σα_i<∞. For trace-class A it gives S_p(A) from log det(I+r|A|).

**Reconstruction or correction, ours.** Do not restore the cancelled p-summability hypothesis; Tonelli and the one-factor integral prove the infinity-allowed formulation.

**Status: True as written.** PROOFS.tex, H0DT.67. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** This scalar Mellin representation is used here to pass from determinant majorants to Schatten power sums (H0DJ); the exact application is on scans 130–131.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.67; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.70 — 1/130.1

**His statement.**

Il pose M_A(r)=Sup_{|z|=r} det(1+zA), sans module extérieur dans la formule.

**How he left it:** stated. **Date:** Undated manuscript. The catalogue dates a letter to 1953, not these leaves.

**Today’s precise statement, ours.** For trace-class A, M_A(r)=max_{|z|=r}|det(I+zA)| is a finite continuous radial maximum. If A≥0, M_A(r)=det(I+rA).

**Reconstruction or correction, ours.** Slip, ours: insert the outer modulus. For A=[1] the values 1+z on |z|=1 are not an ordered real set; the literal supremum has no stated meaning. The definition on 108 and the next positive-operator computation provide local evidence.

**Status: Slip.** PROOFS.tex, H0DT.70. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** This is the maximum modulus used in the Mellin and Jensen determinant estimates on 130–131; the operator consequences belong to H0DJ.

**Check and confidence.** CHECK_EVENTS.tsv, H0DT.70; second-pass record in `work/SECOND_CHECK.md`. High: native-resolution ink and a complete proof agree.

### H0DT.71 — 1/130.8–17, formula (10)

**His statement.**

Pour la somme A+B, il écrit M_{|A+B|}(r)≤M_{|A|}(r)M_{|B|}(r), puis intègre les logarithmes pour retrouver la formule de sous-additivité.

**How he left it:** proved on the page. **Date:** Undated manuscript. The catalogue dates a letter to 1953, not these leaves.

**Today’s precise statement, ours.** For Hilbert trace-class A,B and r≥0, det(I+r|A+B|)≤det(I+r|A|)det(I+r|B|). Hence S_p(A+B)≤S_p(A)+S_p(B) for 0<p<1, with extended values.

**Reconstruction or correction, ours.** Supply the exterior-power coefficient-convolution proof of the determinant bound, then apply H0DT.67. This proves the stated entire-function step and the displayed application, without assuming Schatten subadditivity.

**Status: True as written.** PROOFS.tex, H0DT.71. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** Used in the manuscript’s Schatten quasi-norm discussion, H0DJ and H0E0; the scalar mechanism is the positive-product Mellin identity.

**Check and confidence.** CHECK_EVENTS.tsv, H0DT.71; second-pass record in `work/SECOND_CHECK.md`. High: native-resolution ink and a complete proof agree.

### H0DT.68 — 1/131.1–26; 1/132.1–3

**His statement.**

Une majoration « classique » donne s_p(A)≤p²∫log M_A(r)r^{−p−1}dr pour p<1; avec le déterminant positif, s_p(A)≤(pπ/sin πp)S_p(A). Il applique ensuite la formule à A^n et p/n, invoquant l’inégalité de Hölder annoncée plus bas.

**How he left it:** proved on the page. **Date:** Undated manuscript (s.d.); the catalogue separately dates a letter 1953.

**Today’s precise statement, ours.** For normalized entire f, the reciprocal-zero p-sum equals p²∫V(r)r^{−1−p}dr and is at most the same integral of log M. For compact A in S_p, the determinant argument on sufficiently large powers proves Σ|λ_i(A)|^p≤Σs_i(A)^p.

**Reconstruction or correction, ours.** Prove the Jensen integral for every p>0 and the needed Schatten Hölder gate independently via exterior powers and log-majorization; the determinant itself is used only when trace class.

**Status: True as written.** PROOFS.tex, H0DT.68. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** The determinant-to-spectrum bridge is part of the Hilbert trace-ideal theory in Grothendieck (1954/1957), §4(c), p. 383; modern determinant formulation is Koutsonikos-Kouloumpis and Lesch (2024), §1.2, pp. 2–3.

**Check and confidence.** CHECK_EVENTS.tsv: events with id H0DT.68; second-pass record in `work/SECOND_CHECK.md`. High: explicit hypotheses and complete argument; decisive readings checked against the scan.

### H0DT.72 — 1/131.8–10, second Mellin integral

**His statement.**

Après le dénominateur r^{p+1} dans la première intégrale, la seconde intégrale porte r^{p−1}; il dit appliquer alors la formule (9).

**How he left it:** proved on the page. **Date:** Undated manuscript. The catalogue dates a letter to 1953, not these leaves.

**Today’s precise statement, ours.** The second denominator must also be r^{p+1} to invoke the Mellin identity and obtain the finite factor pπ/sin(πp). With p−1 the displayed upper bound is generally infinite and does not give the next line.

**Reconstruction or correction, ours.** Slip, ours: the first display and formula (9) supply the correction. For A=[1], p=1/2, the second integral with r^{p−1} diverges, while the intended integral is finite. The bare inequality with infinity is not itself called false.

**Status: Slip.** PROOFS.tex, H0DT.72. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** The corrected argument proves the eigenvalue power-sum estimate in H0DT.68; no new unresolved spectral assertion remains.

**Check and confidence.** CHECK_EVENTS.tsv, H0DT.72; second-pass record in `work/SECOND_CHECK.md`. High for the corrected calculation; medium for the second exponent’s short horizontal stroke.

### H0DT.73 — 1/137.14–23; 1/138.1–13

**His statement.**

Avec L=(AB)(AB)*, H=A*A, K=BB*, p′=1/p, q′=1/q, r′=1/r et p′r+q′r=1, il majore M_{L^m}(ρ) par M_{H^m}(ρ^{p′r})M_{K^m}(ρ^{q′r}); il pose ensuite σ=ρ^{p′r} dans l’intégrale logarithmique.

**How he left it:** proved on the page. **Date:** Undated manuscript. The catalogue dates a letter to 1953, not these leaves.

**Today’s precise statement, ours.** For A∈S_p, B∈S_q, positive finite p,q,r with 1/p+1/q=1/r, choose integer m>max(p,q)/2. Then M_{L^m}(t)≤M_{H^m}(t^{r/p})M_{K^m}(t^{r/q}). For any positive coefficient determinant M and θ,β>0, ∫log M(t^θ)t^{−1−β}dt=(1/θ)∫log M(s)s^{−1−β/θ}ds, including infinite values.

**Reconstruction or correction, ours.** The coefficient product estimate is proved through exterior powers and the elementary ideal singular-value bound. The change of variables is evaluated with all factors, and the resulting weighted Schatten inequality is checked.

**Status: True as written.** PROOFS.tex, H0DT.73. The full proof or counterexample is in the identically numbered section of `PROOFS.tex`.

**What became of it.** This is a further explicit use of H0DT’s entire positive determinants in the H0DJ product inequalities on 137–138; it repeats and transforms H0DT.67 rather than introducing a new genus theorem.

**Check and confidence.** CHECK_EVENTS.tsv, H0DT.73; second-pass record in `work/SECOND_CHECK.md`. High: native-resolution ink and a complete proof agree.

## 5. Links to neighbouring objects

Only links with an explicit mathematical or documentary connection are retained. A shared archive topic alone is not a link.

| Other tag | Relation to H0DT | Evidence |
|---|---|---|
| H0D8 | H0DT is used by the Fredholm determinant argument, and uses its spectral-zero input. | 1/071 Theorem 1; 1/079–080 reduction; scalar proposition at 1/111–112. H0DT.1–4,21–27,69. |
| H0DJ | H0DT is used in singular-value and Schatten estimates. | Mellin positive-product formula and Jensen bound at 1/129–132; powered determinant comparison at 1/137–138. H0DT.67–68,70–73. |
| H0E0 | The same Banach-space power-series example overlaps this object. | S begins at 1/120 and continues at 1/122 with multilinear norms and the equal-coordinate example. H0DT.52–66. |
| H0CT | Documentary headings and pagination are used to identify the sequence. | 1/107–108 headings and continuation across 1/121–122; scan, sheet and PDF-footer numbers kept distinct. |

The neighbouring tags and their descriptions come from the supplied `OBJECTS_NEARBY.tsv`; their sweep statuses are not treated as proofs. The exact edge records are in `LINKS.tsv`.

## 6. The seven note entries

All entries were read in full, independently of the sweep’s index-row placements. The detailed record contains 55 subclaim verdicts in `work/NOTE_CLAIMS.tsv` and seven complete rows in `NOTES_VERDICTS.tsv`.

| Entry | Final assessment |
|---|---|
| work:K1-05#6 | The two finite computations are correct; the normalization warning is valid; the small argument of f remains a reading question. Its early-page metadata is extraneous to its actual remarks and belongs to H0DJ. |
| codex:K1-05#1 | Correctly locates the explicit reservation on the false order-one example. Its negative observation is confined to scans 108–121. |
| work:K1-05#1 | The seventeen-part descriptive summary is useful and largely faithful; repeated defective formulas are corrected, the programme is made precise without attributing our choices to him, and continuation on 122 is supplied. |
| work:K1-05#2 | Its eleven proof-status observations are accurate at the extract level. They do not establish open problems; the mathematical claims are now proved, corrected or refuted. |
| work:K1-05#3 | Correctly distinguishes the explicit reservation from the unmarked page boundary. The boundary after D’où is followed by the proof on 122. |
| work:K1-05#4 | All twelve proposed mathematical diagnoses were checked. The order-one example receives the final status False here; the note’s numerical correction is right. Uncertain labels and small indices stay reading leads. |
| work:K1-05#5 | All seven pointer rows are resolved to their local referents or checked literature. Representation (2) is on 107. No bibliographical attribution is invented for a local label. |

## 7. Our research-run results — checked last

The complete independent entry draft was written at **2026-11-19 16:24:31 UTC**. Only afterwards, at **2026-11-19 16:24:42 UTC**, was the supplied results folder opened, with the required `results opened` entry in `progress.log`. The independent draft is preserved unchanged in `work/ENTRY_independent_draft.md`; post-draft changes are itemized separately.

The supplied register contains **zero research-run statements** citing these folders and pages. Its README reports zero rows, and `RESULTS_CITING.tsv` has a header with no data rows. Accordingly, `CONSEQUENCES.tsv` is intentionally header-only: there is no statement tag to assess and no supported cross-run relation to add. This finding concerns the supplied register; it is not a claim about all research elsewhere. The comparison and source-member hashes are recorded in `work/RESULTS_COMPARISON.md` and `work/RESULTS_OPENING.json`.

## 8. References

The following list uses author–date citations. Exact source-to-statement matches and access qualifications are in `REFERENCES_CHECKED.md`; machine-readable entries, including the explicitly unverified inaccessible zbMATH record, are in `references.bib`.

Grothendieck, A. (n.d.). *Analyse fonctionnelle: Notes manuscrites (s.d.), lettre (1953)* [Manuscript, cote 1]. Fonds Grothendieck, Université de Montpellier. https://grothendieck.umontpellier.fr/1.pdf

Grothendieck, A. (1954/1957). La théorie de Fredholm. In *Séminaire Bourbaki* (Vol. 2, Exposé 91, pp. 377–384). Société Mathématique de France. Talk March 1954; opened revised text dated June 1957. https://www.numdam.org/item/SB_1951-1954__2__377_0.pdf

Grothendieck, A. (1956a). La théorie de Fredholm. *Bulletin de la Société Mathématique de France, 84*, 319–384. https://doi.org/10.24033/bsmf.1476

Grothendieck, A. (1956b). Sur certaines classes de suites dans les espaces de Banach, et le théorème de Dvoretzky–Rogers. *Boletim da Sociedade de Matemática de São Paulo, 8*, 81–110. Opened retypeset copy, separately paginated 1–23: https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-26.pdf

Hadamard, J. (1893). Étude sur les propriétés des fonctions entières et en particulier d’une fonction considérée par Riemann. *Journal de mathématiques pures et appliquées*, 4th series, *9*, 171–215. https://www.numdam.org/item/JMPA_1893_4_9__171_0.pdf

Istituto Grothendieck. (n.d.). *Published works*. Retrieved November 19, 2026, from https://csg.igrothendieck.org/published-works/

Koutsonikos-Kouloumpis, N., & Lesch, M. (2024). *The product formula for regularized Fredholm determinants: Two new proofs* (Version 2) [Preprint]. arXiv. https://arxiv.org/pdf/2202.12923v2

McMullen, C. T. (2025, December 2). *Advanced complex analysis: Math 213a* [Course notes]. Harvard University. https://people.math.harvard.edu/~ctm/papers/home/text/class/harvard/213a/course/course.pdf

Poincaré, H. (1883). Sur les fonctions entières. *Bulletin de la Société Mathématique de France, 11*, 136–144. https://www.numdam.org/article/BSMF_1883__11__136_0.pdf

Université de Montpellier. (n.d.). *Archives Grothendieck: Catalogue*. Retrieved November 19, 2026, from https://grothendieck.umontpellier.fr/archives-grothendieck/

Valiron, G. (1925). *Fonctions entières et fonctions méromorphes d’une variable* (Mémorial des sciences mathématiques, No. 2). Gauthier-Villars. https://www.numdam.org/item/MSM_1925__2__1_0.pdf

## 9. Audit and use of this package

`ENTRY.md` is the final reading guide; `STATEMENTS.tsv` is the row-level register; `PROOFS.tex` contains the complete proofs and counterexamples as a LaTeX fragment. The reading, notes, links, consequences, bibliography, dated ledger and check-event tables are separate so that documentary changes need not erase mathematical provenance. Cropped images are derivative visual-check records. Supplied attachments and full scans are not duplicated.

The final records supersede intermediate diagnoses preserved in the checkpoint history. In particular, use the corrected finite-subfamily argument of H0DT.4. All repairs, counterexamples and vector-programme completions identified as ours are work of this run, not newly attributed manuscript text. The precise status vocabulary does not convert an uncertain reading into a mathematical theorem.

### Final checks and checkpoint history

The final tables have the requested schemas and contain 73 unique statement ids, seven note-entry verdicts, 55 note-subclaim verdicts, 51 decisive-reading records and five supported neighbouring-object links. Every statement has its own proof section and check events; no final mathematical status is Open. The 263 check events distinguish targeted checks, genuinely different re-proofs, recorded computations and literature use. The second audit was a separate pass by the same agent, not an external referee or a proof-assistant certificate.

The LaTeX fragment was compiled successfully in a minimal wrapper; the wrapper compilation checks syntax, not mathematical correctness. Exact finite computations and counterexamples have their own retained scripts and outputs. `work/FINAL_QA.md` and `work/FINAL_QA.json` record the consistency checks. `work/OPERATIONS.md` explains the chronological scripts and their dependencies.

The first scheduled checkpoint was made just after the 45-minute deadline. Its archive is not nested here. Every byte of each of its member files is preserved either in the current file or, when changed, under `work/checkpoint_01_prior_versions/`. Those prior versions are historical evidence and are explicitly superseded by the final root-level files. In particular, their earlier H0DT.4 Slip diagnosis must be read with the dated correction in `PROGRESS_LEDGER.md`. The unchanged independent draft likewise records the state before results were opened. `ENTRY.md` is written last, after the tables, audit, results comparison and checkpoint-material preservation.
