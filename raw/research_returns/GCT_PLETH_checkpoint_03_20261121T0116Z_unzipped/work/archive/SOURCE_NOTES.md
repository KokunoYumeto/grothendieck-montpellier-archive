# Verified source locators for the archive and geometric dictionaries

Run `/root/archive_audit`; model GPT-6 Astra Pro; effort not exposed. This document records source inspection, not an independent reproof of every cited theorem. Archive evidence consists of the supplied TeX transcriptions. No manuscript scan images or Lean files were supplied.

## Archive and supplied secondary material

All thirteen `ARCHIVE_*.tex` and all of `SA17_STUDY_cote133_lambda.md` were read. The report preserves the difference between transcribed statements, transcription uncertainty, supplied study additions, and current-run arguments. In particular, the study's alleged equivariant finite-set check on 133/019 is refuted in A-001. No claim about scans merely mentioned in the study is treated as a new scan inspection.

## SGA 6: exact K theory, exterior operations, and the free λ-ring

Bibliography: P. Berthelot, A. Grothendieck, L. Illusie, with collaborators, *Théorie des intersections et théorème de Riemann–Roch*, SGA 6, Lecture Notes in Mathematics 225, Springer, 1971.

| Locator | Statement used | Inspection |
|---|---|---|
| Exposé V, Definition 2.1 | Pre-λ definition | French mathematical transcription inspected |
| V, Lemma 2.2.1 | Exterior-power filtration for short exact sequences | Exact citation confirmed in Zibrowius 2016, Lemma 2.2 |
| V, 2.4.1 | Universal product and iterate identities | Exact citation confirmed in Zibrowius 2015, §3.1 |
| V, 3.2–3.4 | γ substitution and equivalent formulas | French mathematical transcription inspected |
| V, 3.10 | γ filtration | French mathematical transcription inspected |
| V, Proposition 4.2; Definition 4.4 | Unique evaluation of the free λ-ring | Statement and proof text inspected |
| V, Proposition 4.8; Corollary 4.9 | Finite-rank quotient and its λ-ideal | Statement and proof text inspected |
| V, §6 | Chern-ring universal construction | Section located; entire proof not independently rederived |
| VI, Theorem 3.3 | λ structure on exact K₀ of a locally ringed topos; transfer via frame torsors | Theorem and proof transcription inspected, exact locator corroborated in Zibrowius 2015 p.1057 and 2016 §2.2 |

Inspected transcriptions: https://grothendiecksga.com/read/sga6/fr/V-3.html ; https://grothendiecksga.com/read/sga6/fr/V-4.html ; https://grothendiecksga.com/read/sga6/fr/VI-3.html . Local HTML/text copies are in this directory. The attempted original scan download from `iut-theory.org` returned HTTP 503. The paper must not say the original SGA 6 scan was visually inspected.

## Zibrowius: precise quadratic-form quotient and splitting

Marcus Zibrowius, *Symmetric representation rings are λ-rings*, New York J. Math. 21 (2015), 1055–1092. Primary PDF: https://nyjm.albany.edu/j/2015/21-49v.pdf .

- Main theorem, p.1056: special λ structure on the Grothendieck–Witt representation ring defined with metabolic relations.
- Lemma 1.1, p.1059: the natural hyperbolic isometry for a symmetric object and its negative, with 2 invertible.
- Definition 1.2, p.1060: the exact K₀ relations and, explicitly, the additional relation `[M]=[H(L)]` for metabolic `M` with Lagrangian `L`.
- §3.1, pp.1068–1069: universal special-λ identities and their SGA 6 locator.

Marcus Zibrowius, *The γ-filtration on the Witt ring of a scheme*, arXiv:1411.3198v2, submitted 11 August 2016, title-page date 12 August 2016. Primary PDF: https://arxiv.org/pdf/1411.3198 .

- Theorem 2, displayed p.3, and Theorem 2.5, displayed p.11: schemes over a field of characteristic different from two.
- Proposition 2.15, displayed pp.17–18: orthogonal torsors carrying pairs of symmetric bundles.
- **Proposition 3.3, displayed pp.19–20: the preceding sentence explicitly says “any scheme over Z[1/2]”.** This proposition supplies a morphism that splits the given symmetric bundle into symmetric lines and induces an injection on étale cohomology with Z/2 coefficients. Its scope is broader than Theorem 2. The report's scheme-over-Z[1/2] scope is verified.
- Proposition 4.8, displayed p.23: again explicitly over Z[1/2], consistent with that broader splitting scope; not needed for our main argument.

## Macdonald: symmetric functions and Schur–Weyl

I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, second edition, Oxford, 1995. Primary book PDF inspected: https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf . Local copy `Macdonald.pdf` and extracted text `Macdonald.txt`.

| Locator and printed page | Exact role |
|---|---|
| I (4.2), p.62 | Cauchy kernel expanded as the sum of monomial times complete symmetric functions |
| I (4.3), p.63 | Cauchy kernel expanded as the sum of Schur times Schur functions |
| I (7.3), pp.113–114 | Frobenius characteristic is an isometric graded-ring isomorphism; its proof sends induced trivial Young modules to `h_ν` |
| I (7.5)–(7.6), p.114 | Irreducible character basis maps to the Schur basis |
| Appendix A (5.3)–(5.4), p.155 | Homogeneous polynomial functors from symmetric-group modules and the characteristic-zero equivalence |
| Appendix A (5.6), p.156 | Functorial tensor-power decomposition `Tⁿ(X)=⊕M_λ⊗F_λ(X)` |
| Appendix A (7.2), p.160 | Character of the irreducible polynomial functor is `s_λ` |
| Appendix A (7.4), p.160 | Nonnegative integral Schur coefficients for Schur plethysm through functor composition |

These numbered statements were inspected in the primary PDF, including the previously pending Appendix A (5.6). The PDF's page index is printed page plus 10.

## Akin–Buchsbaum–Weyman: the integral Cauchy filtration

K. Akin, D. A. Buchsbaum, J. Weyman, *Schur functors and Schur complexes*, Advances in Mathematics 44 (1982), 207–278, DOI 10.1016/0001-8708(82)90039-1. The author's current research page is https://jerzyweyman.webflow.io/research/schur . Its linked original paper was downloaded completely from https://cdn.prod.website-files.com/69c19dc391eb37d617c813ce/69cc3be3405f5e9e171b7db4_JW%231_Schur.pdf and retained as `ABW1982.pdf`, with extracted text `ABW1982.txt`.

- Theorem II.2.16, printed p.232: the universal standard-tableau basis for a Schur module, proving freeness and compatibility with arbitrary scalar extension.
- Theorem III.1.4, printed pp.245–246: the natural integral filtration of a symmetric power of a tensor product, with tensor products of Schur modules as its associated graded.

The paper's indexing uses `L_(a)=Λᵃ`. A-012 explicitly defines `S_λ^int=L_(λ′)` to translate its convention to the archive's usual Schur partitions. Three exact torus-weight extractions from this one filtration prove the arbitrary-characteristic tensor-power formula, including its virtual exact-K₀ extension. The source theorem is carried as verified background; A-012's deduction is independently checked in full.

## Witt vectors and Borger

Michiel Hazewinkel, *Witt vectors. Part 1*, primary author PDF: https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Hazewinkel-Witt.pdf .

- §§14.1–14.4, pp.71–72: big Witt operation polynomials in coordinate `n` involve only divisor coordinates. The resulting `p`-power coordinate polynomials define the `p`-typical Witt ring functor and the natural quotient from the big Witt functor.
- Definition 14.5 and §14.8, pp.72–73: divisor-stable index sets (“nests”) and their Witt functors.
- §14.15, equation (14.16): canonical big-to-typical projection. No `p`-local hypothesis is needed for the quotient. The stronger decomposition involving sections later in §14.21 uses `p`-local rings and is not invoked here.

James Borger, supplied `lrfoe13.tex`, §§1.1–1.2 and §2.2, inspected in the input file. The first locators give the free λ-ring, arithmetic jet-space, and Witt-space adjunction framework; §2.2 gives monoidal Frobenius lifts. The report verifies the explicit character-ring map `ψᵖ f(x)=f(xᵖ)` and its congruence modulo `p` directly.

## EGA I: schematic image

A. Grothendieck and J. Dieudonné, *Éléments de géométrie algébrique. I. Le langage des schémas*, Publ. Math. IHÉS 4 (1960), 5–228. Primary original PDF downloaded completely and its text inspected: https://www.numdam.org/item/PMIHES_1960__4__5_0.pdf . Local copies `EGAI.pdf`, `EGAI.txt`.

| Locator and printed page | Exact role |
|---|---|
| Proposition 9.5.1, p.176 | Existence of a smallest closed subprescheme through which the morphism factors when direct image of the structure sheaf is quasi-coherent |
| Corollary 9.5.2, p.176 | The defining ideal is `ker(O_Y→f_*O_X)` |
| Definition 9.5.3, p.177 | Names that closed image |
| Proposition 9.5.4, p.177 | Its underlying space is the closure of the image |
| Proposition 9.5.8, p.178 | Formation commutes with restriction to an open of the target; the following paragraph points forward to flat base change |
| Proposition 9.5.9, p.178 | Reducedness and irreducibility/integrality pass to the closed image in the stated range |

For the parent's affine morphism `μ:Spec B→Spec C`, the actual algebra map `C→B` identifies the closed image with `Spec(C/ker μ*)=Spec(im μ*)`. Affineness gives the required quasi-coherence directly. The elementary tensor-exactness proof gives compatibility with a flat extension of scalars in this affine case; no unverified global EGA base-change number is required.

## FGA: Quot and Hilbert

A. Grothendieck, *Techniques de construction et théorèmes d'existence en géométrie algébrique. IV. Les schémas de Hilbert*, Séminaire Bourbaki, exposé 221 (1960–1961), pp.249–276 in the Numdam collected pagination. Primary PDF inspected: https://www.numdam.org/item/SB_1960-1961__6__249_0.pdf .

- Theorem 3.1, printed p.259 (PDF index 11): Quot represented by a disjoint sum of projective schemes in the setting stated there.
- Theorem 3.2, printed p.260 (PDF index 12): the fixed-Hilbert-polynomial Quot piece is projective.
- Following Proposition 3.8, printed p.265 (PDF index 17): `Quot(O_X)` is the Hilbert functor representing flat families of closed subschemes.
- Remarks 3.9, printed p.266: reduction used for projective schemes over Z.

## Fitting ideals: verified alternative locator, no invented EGA citation

The requested exact EGA locator for the determinantal/Fitting formulation was not established in this run. The precise primary reference inspected is the Stacks Project, Section 15.8, tag `07Z6`: Lemma 15.8.2 defines the presentation-independent ideal of minors; Definition 15.8.3 names it; Lemma 15.8.4(3) proves arbitrary scalar-extension compatibility. https://stacks.math.columbia.edu/tag/07Z6 . For locally closed constant-rank strata, Lemma 31.9.6, tag `05P8`, supplies the sheaf statement: https://stacks.math.columbia.edu/tag/05P8 .

In the parent's explicit matrix model, all claims about a rank bound are proved directly by the vanishing/nonvanishing of minors. Those proofs do not require an inaccurately numbered EGA theorem.

## SGA 3: the group scheme and comodule dictionary

M. Demazure and A. Grothendieck, *Schémas en groupes*, SGA 3, Exposé I, by M. Demazure. The primary editor-maintained PDFs were located and inspected: https://webusers.imj-prg.fr/~patrick.polo/SGA3/origExp1.pdf (original text in the editor's typesetting, carrying the original marginal pagination) and https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp1-13oct24.pdf (corrected edition of 13 October 2024).

- I §4.5, original marginal p.29: constructs the classical general linear group by the determinant-open coordinate algebra. An earlier tentative §4.6 locator is corrected to **§4.5**.
- I Definition 4.6.1 and 4.6.3: the `V(F)` and `W(F)` module functors, with the former represented by `Spec Sym F`; EGA II 1.7.8 is explicitly cited for this representing scheme.
- I Proposition 4.7.2, original marginal pp.34–35; corrected edition displayed pp.29–30: a group action is a coaction `F→F⊗A(G)` satisfying the counit and coassociativity diagrams. This identifies representations with comodules and supplies the precise dictionary for integral polynomial representations.
- I Proposition 4.7.3, original marginal pp.35–36: diagonalizable-group actions correspond to weight gradings, by the orthogonal projectors given by coefficient extraction in the group algebra.

No manuscript scan inspection is implied by these typeset primary editions.

## Weil II: purity for the finite étale sign example

P. Deligne, *La conjecture de Weil. II*, Publ. Math. IHÉS **52** (1980), 137–252; DOI 10.1007/BF02684780. Primary original scan inspected at https://publications.ias.edu/sites/default/files/Number40.pdf . The IAS landing-page metadata says volume 42; the correct journal volume is 52, as recorded by Numdam and the DOI.

- Definition 1.2.1 and Definition 1.2.2, printed p.153 (PDF index 16): numerical weights and pointwise purity of a sheaf.
- Variants 1.2.3–1.2.4, p.154: terminology for Galois representations over a finite field and vector spaces with Frobenius.
- Stability 1.2.5(i), p.154: pointwise pure sheaves of a fixed weight are stable under subquotients and finite direct image.
- §1.1.7, pp.150–151: geometric Frobenius is inverse to the field's power Frobenius, and the finite-field sheaf/continuous-Galois-representation equivalence is spelled out.

The sign summand of the degree-two finite étale permutation representation has geometric Frobenius `−1`; every complex conjugate has absolute value one. This directly verifies weight zero from the cited definitions. It also follows from the finite-direct-image and subobject assertions in 1.2.5(i). No general cohomological purity theorem is needed for that example.

## Remaining historical-source gates

- Original SGA 6 scan visual verification was not completed; exact source numbering is corroborated as detailed above.
- An exact EGA Fitting-ideal locator remains unverified; the Stacks primary locators above are verified.

## Field Witt cancellation, exact scope checked

Elman–Karpenko–Merkurjev, *The Algebraic and Geometric Theory of Quadratic Forms*, AMS Colloquium Publications56 (2008), §8: Lemma8.2 and Theorem8.3 pp47–48, Theorem8.4 p48. Author-hosted PDF: https://www.math.ucla.edu/~merkurev/Book/Kniga-final/Kniga.pdf . Full proof of these three statements read; characteristic-free cancellation requires zero polar radical for the cancelled summand. This covers the hyperbolic stabilizer in original133/008. Local copies EKM2008.pdf/.txt; consequence A019 in FIELD_CANCELLATION.md.

## James: modular rank and the integral Specht lattices

G.D. James, *The Representation Theory of the Symmetric Groups*, Lecture Notes in Mathematics682, Springer,1978; DOI10.1007/BFb0067708. Public university-hosted original book scan: https://www-users.cse.umn.edu/~webb/oldteaching/Year2010-11/the-representation-theory-of-the-symmetric-groups-SLN.pdf . Local copies `James1978.pdf/.txt`.

- Theorem8.4, pp29–30: standard polytabloid basis. Corollaries8.6–8.11, pp30–31: integral coefficients/action matrices and reduction of the integral lattice to the modular Specht module.
- Definition10.1 and Lemma10.2, p36: p-regular partition labels and equality of their count with the count of p-regular conjugacy classes, by the displayed Euler-product identity.
- Theorem11.5, p40: complete simple-module list over every field, absolute irreducibility and splitting over every field. Its proof and the explicitly cited general modular-theory dependencies were read.
- Corollary12.2, p42, and Corollary12.3, p43: the p-regular Specht rows give a unitriangular decomposition submatrix. The preceding Theorem12.1 proof was read as well.

These statements supply the exact basis/absolute-base-change input for A-020 and A-021. The torsion boundary, commensurability and generator-preserving rationalization proof in `MIXED_CHAR_LATTICES.md` were checked independently. The original standard-basis page locator is29–31, rather than32–33.

## EKV: the hyperbolic characteristic-class formula

H. Esnault, B. Kahn, E. Viehweg, *Coverings with odd ramification and Stiefel–Whitney classes*, Journal für die reine und angewandte Mathematik441 (1993),145–188. Author-hosted original scan: https://page.mi.fu-berlin.de/esnault/preprints/helene/29-es_ka_vi.pdf . Local copy `EKV1993.pdf`.

- §5.1, p179: scheme over `Z[1/2]` and unimodular quadratic bundles.
- §5.2, pp179–181: the nonisotropic-line pullback and its étale-cohomology decomposition.
- Lemma5.3, pp181–182: the line-class identity `c̄₁(M)=w₁(M)²+(-1)w₁(M)`, with the Kummer/twisted-Bockstein cocycle proof.
- §5.4, p182: regularity is introduced. This hypothesis is retained when citing the following proposition.
- Proposition5.5, pp183–184: the full metabolic/hyperbolic class formula in the Chern classes of the Lagrangian. Both pages and the complete proof were visually read. The rank-two proof's integral Picard-isomorphism sentence needs qualification; A-022 gives a direct argument using injective mod2 cohomology instead.

Marcus Zibrowius, *Witt groups of curves and surfaces*, author PDF https://www.math.uni-duesseldorf.de/~zibrowius/Research/Zibrowius_WCS.pdf , §1.4, printedp8/PDFpage9, equations(6)–(8), reproduces the formula with exact reference to EKVProposition5.5. Its preceding statement explicitly discusses schemes over `Z[1/2]`. Zibrowius's gamma-filtration paper Proposition3.3, pp19–20, independently supplies the injectivity used in A-022's arbitrary-`Z[1/2]`-scheme line-bundle proof.

A-022 now proves the full hyperbolic formula over every `Z[1/2]`-scheme using that same exact injectivity result. The construction applies `P_nd` to `H(E)`; its tautological pair `(v,f)` gives the globally defined projector `z↦v f(z)/f(v)`, so `E` splits a line after this cohomologically injective pullback. Iteration and the actual orthogonal hyperbolic-sum isomorphism supply the formula. Thus no affine-bundle invariance theorem is needed for the extension.

For reference, the exact affine-space invariance locator requested during this check is **SGA4 XV, Corollary2.2**, with the meaning of acyclicity in **XV, Proposition1.6 and Definition1.7**. The French transcription of these statements was read at https://grothendiecksga.com/read/sga4/fr/XV-2.html and https://grothendiecksga.com/read/sga4/fr/XV-1.html . Corollary2.2 treats affine space over an arbitrary scheme, with torsion primes invertible on the base. No original SGA4 scan inspection is claimed for this locator check.
