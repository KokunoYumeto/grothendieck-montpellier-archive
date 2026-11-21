# Alpöge and Masullo: primary-source review and reusable bridge proofs

Run: `/root/source_and_masullo`. Model: GPT-6 Astra Pro. Reasoning effort: not exposed by the runtime. Working date: 21 November 2026, Europe/Berlin (the corresponding UTC date during the initial work is 20 November).

This note records a bounded review of the supplied sources, exact mathematical scope, the parts needed for the comparison, and ten proved statements in `source_and_masullo.tex`. It is not a claim to have reviewed every proof in the 940-page Masullo manuscript or compiled the separate Alpöge Lean development. The assigned adopted premises are used as theorems, while check labels describe only work actually performed in this run.

## 1. Source facts and corrections

### 1.1 Alpöge exports

All five theorem declarations in the supplied `ALPOGE_Main.lean` were read, along with every definition in `ALPOGE_Statements.lean`, the complete 1,871-byte scan report, and the pinned Lake file.

| Source statement id | Exact declaration | Precise scope |
|---|---|---|
| ALP-RH | `riemannHypothesis : RiemannHypothesis := rhOfAll` | Mathlib's named Riemann hypothesis proposition. |
| ALP-RH-EXPLICIT | `riemannZeta_eq_zero_re : RiemannZetaZerosOnLine := rhOfAll` | Zeta zeros, excluding the negative even integers and `s = 1`, have real part `1 / 2`. |
| ALP-DIR-NV | `LFunction_ne_zero_of_half_lt_re : DirichletLNonvanishingRightOfHalf := allChi` | Every positive modulus and every complex Dirichlet character; nonvanishing for real part greater than one half; excludes principal character at `s = 1`. |
| ALP-DIR-GRH | `LFunction_eq_zero_re : DirichletLZerosOnLine := claimAll.2.1` | Every Dirichlet character, zero in the open strip `0 < Re(s) < 1` lies on one half. |
| ALP-DIR-PRIM | `LFunction_eq_zero_re_of_isPrimitive : PrimitiveDirichletLZerosOnLine := critAll` | The primitive-character specialization. |

The pin is `0df444a360eaa60ab8c11dca51a86af692955474`. The import `Supplements.Kernels.MainTheoremsAll` is not in the supplied archive. Neither `lean` nor `lake` was installed in this environment when checked. The scan table is supplied evidence about another source tree, not a fresh scan of the absent 175,187-file development. Therefore these inputs receive declaration/definition inspection events, never a computational or formal-certificate event.

The four-page `Remark` was text-extracted and read in full. Pages 1 and 4 were rendered; page 1 was visually inspected. Its chain length is **√X**, not X. Both page 1 and step 8 on page 4 contain the radical. The source's statement about K-groups is tentative: page 4, footnote 6 gives no degree, range, quantifier, or named theorem. No specified K-group vanishing follows merely by citation of that footnote.

### 1.2 Method map of the four-page note

| Steps | Exact locator | Mathematical object or operation actually named | Additional theorem needed for a categorical bridge |
|---|---|---|---|
| 1–2 | p.3 | Stepanov determinant, invariant derivation on a CM curve, inert-prime divisibility | An explicit integral/crystalline comparison and the exact divisibility statement with its quantified range. |
| 3 | p.3 | Path quadric, theta periods, sixfold metaplectic cover, CM torus C/Z[ω], Poincaré bundles | A constructed comparison with the archive's objects; the word “hexagon” does not supply one. |
| 4–6 | pp.3–4 | Weil functional positivity, von Mangoldt test function, zero-free-region bootstrap | Exact test-function class and estimates; these are not exported in the supplied Main file. |
| 5, footnote 3 | p.3 | Bertini, middle cohomology, iterated Parseval, no cancellation of inverse roots | Bounds for all finite extensions, noncancellation, and duality. F-SM-09 identifies the exact abstract implication. |
| 7–10 | p.4 | GGP periods, iterated definite unitary theta lifts, m about √X, divisibility and norm cancellation | Integral functoriality, lattice comparison, and exact quantified lift estimates. |
| 11, 19 | p.4 | Iwasawa tower; Behrend construction | A comparison map to any Teichmüller or motivic tower, with compatibility proved. |
| 12–16 | p.4 | Rallis seesaw, Bost slope inequality, integral structures across characters, relative trace formula | Exact operator/lattice constructions and all norm estimates; existence of RH is not their proof. |
| 17 | p.4 and footnote 6 | H¹ of S-integer rings with Q_l/Z_l(−e), a weakening of Vandiver | The actual cohomological theorem, including e, ℓ, E, and hypotheses, followed by the requisite K-theory comparison. |
| 18 | p.4 | Covolumes, theta-series index, congruences | Exact integral comparison; not implied by a complex zero-location theorem. |
| 20 | p.4 | GRH | Supplied declaration scope is Dirichlet GRH, rather than all automorphic L-functions. |

### 1.3 Primary web verification

Direct opens initially returned internal errors. A stronger primary-source search then retrieved both announcements, and both URLs were successfully opened through returned search references. A transient fetch error was not treated as evidence against the sources.

| Source | URL | Retrieved ref | What it establishes |
|---|---|---|---|
| Alpöge, *Remark* | https://alpo.ge/remark.pdf | `turn575499152view1`, also `turn466669506search2` | Public availability of the same four-page announcement and √X chain wording. |
| Vakil announcement | https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/ | `turn575499152view0`, also `turn466669506search0` | Posted 20 Nov 2026; describes a proposed proof, Conrad's prolonged feedback, and the release of the draft. |
| Masullo manuscript | https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf | `turn575499152view2`, also `turn466669506search3` | Public copy of the supplied work. |

The parent agent must reopen/search these sources itself if citing their tool refs in the final user-facing response. The local supplied PDFs may be cited directly in the paper by exact page and theorem number, without relying on search extraction.

## 2. Masullo's route and what its diagrams mean

The manuscript's p.6 identifies the intended generality as all number fields and all unitary Hecke characters. This would go beyond the supplied Alpöge Dirichlet theorem. Its core strategy is to form a divisor exact sequence in nuclear locally convex spaces, pass to Hardy–Sobolev completions whose spectral quotients retain only zeros in a chosen vertical strip, and compute the same geometric trace in those coarser topologies. Orbital Schauder/Markushevich bases are intended to preserve the local trace computations through completion.

The essential locators are:

| Component | Locator |
|---|---|
| Global divisor exact sequence | §1.2.1, pp.13–15 |
| Orbital decomposition and S-local reduction | §§1.2.2–1.2.3, pp.15–16; §§1.3.2–1.3.3, pp.26–27 |
| Holomorphic test-family deduction | §§1.4.2–1.4.5, pp.28–30 |
| Comparison with Connes and Deninger | §1.5, pp.32–33 |
| Orbital supports and quotient stacks | Definitions 8.2.0.1–8.2.0.2, pp.384–385; §8.4, pp.389–394 |
| S-local stack/divisor diagrams | (8.4.0.6)–(8.4.0.7), p.390; supplied crops p390_1 and p390_2 visually inspected |
| Global diagrams and their qualification | (8.4.0.8)–(8.4.0.9), Remark 8.4.0.1, p.391 |
| Spectral projection/convolution trace | Theorem 10.4.2.8, pp.463–471 |
| Basis-lift lemma with problematic inference | Lemma 10.4.2.5, pp.461–462; Remark 10.4.2.7, p.463 |
| Orbital nuclearity | Theorem 11.2.2.1, pp.490–491 |
| Primary divisorial strata | §11.3.1.1, pp.491–494 |
| Orbital trace | Theorem 11.3.2.1, pp.495–496 |
| Diagonal deconstruction apparatus | §12.2, pp.504–513 |
| Unwritten global-to-local assembly | §12.3, p.514 |
| S-local trace | Theorem 12.4.1.1, pp.514–519 |
| Main trace formula | Theorem 12.5.1.1, pp.519–520 |
| Incomplete final divisor theorem | Theorem 13.3.1.2, p.522 |
| Multiplicity discussion | §14.1.2, pp.528–533 |
| Why this method does not transfer to finite characteristic | §14.2, pp.534–536 |
| Classical full explicit formula | Theorem B.4.4.7, p.623 |

Remark 8.4.0.1 explicitly states that the vertical arrows in the four principal stack diagrams **are not morphisms**. They encode an interpretation of nuclear Fréchet spaces as analogues of bundles over quotient stacks/divisors. Consequently, the diagrams do not yet construct a motivic realization, étale cohomology of Spec Z, a six-functor formalism, or a derivator. This is an exact source restriction, not an inference from absence of familiar terminology.

## 3. Completed mathematical findings

Full proofs are in `source_and_masullo.tex`; this table gives their scope and role.

| Finding | Result | Status and role |
|---|---|---|
| F-SM-01 | A full zero trace equal to its restrictions to arbitrarily narrow vertical strips forces every zero onto the central line. | Proved. Uses regularized Laplace test functions and positive residues; no positivity criterion or unproved normal-family passage. |
| F-SM-02 | A correctly normalized shrinking-strip identity is equivalent to GRH for a fixed character, given the full explicit formula and standard zero summability. | Proved conditional equivalence. Under adopted Dirichlet GRH its numerical identity holds; this does not prove Masullo's operator realization. |
| F-SM-03 | GRH for all finite-order Hecke characters of all number fields gives holomorphy and nonvanishing of every finite-image Artin L-function in the open critical strip off its central line. | Proved conditional bridge using Brauer induction; does not prove holomorphy on the line. |
| F-SM-04 | Norm-unit strata and simultaneous-local-unit strata differ. | Explicit counterexample over Q(i) at 5; corrected criterion is the residue-degree weighted sum of valuations. |
| F-SM-05 | A maximal curve need not have gonality g+1. | Explicit smooth Hermitian quartic over F9, genus 3, 28 points, degree-at-most-3 map to P1; computational count agrees. |
| F-SM-06 | Imaginary spectrum does not imply skew-adjointness for a positive definite Hermitian form. | 2×2 Jordan counterexample, fully proved. Separates zero location from semisimplicity and unitary realization. |
| F-SM-07 | Boundedness and biorthogonality of lifts do not imply the Schauder basis property. | Explicit ℓ² example. This refutes the inference in p.462, not the Hilbert existence statement. |
| F-SM-08 | Suitable basis lifts into a prescribed linear subspace do exist in the Hilbert setting, via a bounded graph construction. | Full repair for both Schauder and Markushevich bases, with explicit summability control. |
| F-SM-09 | A bound on all power sums with nonzero surviving spectral coefficients bounds each eigenvalue; reciprocal duality gives purity. | Full rational-generating-function proof. Precisely identifies the no-cancellation gate in the Alpöge sketch. |
| F-SM-10 | Alternating traces can hide arbitrary eigenvalue sizes through cancellation. | Fully proved two-term graded counterexample. Explains why F-SM-09's surviving-coefficient hypothesis is essential. |

F-SM-01 was read independently by the parent agent, who reported that the proof passes. The parent also checked F-SM-02, 03, 05, 06, and 08. Parent comments on the exact source interpretation in F-SM-04, collar constants in F-SM-07, and geometric integrality in F-SM-05 were addressed in the text. The check-events file distinguishes self-checks, parent checks actually reported, and computation.

No claim is made that these elementary forms are historically new. “Finding” here means a statement established in this run, as requested, and often a precise bridge or counterexample not explicitly stated by the source.

## 4. Remaining mathematical gates and attempted repairs

### M-GATE-1: Global-to-S-local kernel deconstruction

The required identity is the one used at p.520:

\[
\int_{C_F}k(x,x)\,d\mu(x)
=\int_{C_F}k_S(x,x)\,d\mu(x)
+\sum_{p\nmid S}\int_{C_F}k_p(x,x)\,d\mu(x),
\]

with the correct indentation/lifting, smoothing, Hardy–Sobolev topology, and limiting operations. Section 12.3, where this assembly is advertised, is unwritten. The adjacent propositions in §12.2 supply machinery, and Theorem 11.3.2.1 supplies claimed orbital traces, but a valid proof must check their hypotheses for this particular lifted kernel and justify the passage to the global identity. This review did not complete that step. A pointwise partition or Hilbert–Schmidt convergence alone is insufficient to justify arbitrary diagonal traces.

Approaches tried: read the global trace proof, the orbital trace proof, the adjacent indentation/diagonal-integration machinery, and the earlier basis-lifting argument. Result: the final zero-location inference can be repaired independently by F-SM-01; a basis-lift inference can be repaired by F-SM-08; neither repair supplies the omitted deconstruction. Next step: specify the exact lifted kernel and construct a dominating integrable diagonal density or prove the required trace-norm convergence through the strata, with all normalization conventions fixed.

### M-GATE-2: Zero multiplicities

The claimed bound on noncentral multiplicities by [F:Q] is discussed in §14.1.2, but the named final theorem 13.3.1.2 is unwritten and the stated trace theorem 13.3.1.1 is flagged for correction. F-SM-01 concerns support, not multiplicity. Alpöge's supplied declarations concern locations and nonvanishing, not simplicity. Next step: state the intended corrected finite-codimension trace identity and prove exactly what its annihilator permits at central points. Do not upgrade the divisor-location theorem to a simplicity theorem.

### M-GATE-3: The categorical arrows

The vertical arrows of the diagram are declared interpretive, not morphisms. Next step: construct the objects and actual functors, then establish trace, tensor, duality, twist and local-term compatibility. RH does not supply these constructions. The draft does not prove a no-go theorem against all foliated or geometric realizations merely by choosing a different route.

### A-GATE-1: K-groups and Vandiver weakening

The four-page note's footnote 6 is not a specified statement. No exact integral K-group vanishing is exported by the supplied Main file. Next step: identify the actual theorem in the full development, including every field, prime, twist, integrality, torsion and degree hypothesis, before using motivic or étale comparison. The present report does not label this as refuted; it remains an unidentified assertion.

### A-GATE-2: New general motivic purity, crystals, GT, and Teichmüller towers

The method names several structures useful to these fields, but a theorem-specific comparison is needed. F-SM-09 isolates the eigenvalue argument once trace estimates and duality are supplied; F-SM-10 shows why alternating trace estimates alone do not suffice. Neither the analytic theorem nor a common hexagonal or tower vocabulary identifies the categories or functors.

## 5. Exact bibliographic inputs

- Alpöge, L. (2026, November 20). *Remark* [Four-page research announcement]. https://alpo.ge/remark.pdf. Adopted theorem locators are the five named declarations in `ALPOGE_Main.lean`; definitions in `ALPOGE_Statements.lean`.
- Masullo, A. M. (2026). *The music of the primes* [Unfinished manuscript released November 20]. https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf. Exact internal locators listed above.
- Vakil, R. (2026, November 20). *Hurried announcement: Alessandro Masullo GRH*. Math 216: Foundations of Algebraic Geometry. https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/.
- Serre, J.-P. (1977). *Linear representations of finite groups* (L. L. Scott, Trans.). Springer. https://doi.org/10.1007/978-1-4684-9458-7. Exact input: §10.5, Theorem 20, p.78 (Brauer induction). Authoritative publisher record retrieved; theorem text was inspected in a digitized book hosted by Rochester, search ref `turn163865242search13`.
- Cogdell, J. W. (n.d.). *On Artin L-functions*. Author manuscript, https://people.math.osu.edu/cogdell.1/artin-www.pdf. Exact inputs: §2.1, p.10, equation (2); §2.2, p.12, ramified Euler factors and inductivity. Retrieved ref `turn958042448view0`; full 31-page PDF saved as background. Use n.d. because this inspected manuscript has no explicit date. The author homepage now links a distinct 33-page PDF, https://people.math.osu.edu/cogdell.1/Artin-www.pdf, under the published title *L-functions and non-abelian class field theory, from Artin to Langlands* (2015), in D. Dumbaugh and J. Schwermer, *Emil Artin and Beyond—Class Field Theory and L-Functions* (pp.129–161), EMS, DOI 10.4171/146. Author page and publisher contents verified (`turn293215501view1`, `turn396021183search5`); publication date 31 March 2015 verified on publisher page (`turn293215501view0`). Do not transfer the inspected 31-page manuscript page numbers to that differently paginated chapter.
- The Stacks Project Authors. (2026). *Plane curves*, §53.9, Lemma 53.9.3. https://stacks.math.columbia.edu/tag/0BYA. Retrieved ref `turn213885719view0`. This supplies the exact plane-curve genus formula; no new proof of the known formula is claimed.

The F-SM-02 zero-counting input can be cited to Iwaniec and Kowalski, *Analytic Number Theory*, Theorem 5.8 (p.104). This locator was corroborated in search but the actual theorem page was not yet read during this subrun; it should remain a citation-check item until inspected or replaced by an already verified equivalent input. F-SM-01 itself assumes only the explicit summability condition and does not depend on this unresolved bibliographic detail.
