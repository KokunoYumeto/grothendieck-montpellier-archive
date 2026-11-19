# Source review: MPL_16+47+54+44

Reviewed by GPT-6 Astra Pro / inherited effort / agent16, 19 November 2026. This is the completed package contribution for integration into the parent dossier. The master counts and machine-readable audit are in `outputs/finalize_counts.json` and `outputs/audit.json`.

## Coverage and source discipline

All 85 indexed entries were read against their corresponding passages. The complete mathematical transcription, absolute lines27–3001, was also read, including the reused and off-topic matter in cotes16 and44. The cover material was inspected as context, not treated as a mathematical claim. The complete doubts file and all six applicable second-pass files—three changes files and their three notes_checked companions—were read. There is no second-pass file for cotes47,54 or44 in this package. The read log and line-numbered reading outputs document these actions. They are documentation, not alternate attachment editions.

The source coordinate is always the cote and scan together with the **absolute, one-based line number in `SA18_texts/pro/MPL_16+47+54+44_transcription.tex`**. Page-local numbers inside the second-pass reports are not silently substituted for that coordinate. The current second-pass reading controls whenever it changes or resolves the Pro transcription. No scans were supplied to this run, and no source text was edited. A mathematically necessary alternative is therefore either a reconstruction or a new scan-review alarm, never a newly decided ink reading.

The 103 items include all indexed material, merged within the package where appropriate, plus findings from the complete transcription. There are 97 claim records. Some record an earlier-run construction or a later comparator, because the index explicitly asks to assess it; those are labelled as such rather than attributed to the author. The additional items16086 and16100–16120 identify material that an index-only review would have missed. Empty `sources` arrays on such items mean that no indexed entry asserted the particular claim; they are not invented entry numbers.

The files retain three voices: the manuscript’s brief words, the earlier notes’ assertions, and the present reconstruction. In particular, the cancelled root-system text, the author’s negative answer about recovering the grading from L, the retracted realization-independence assertion, and the cancelled finite-kernel clause are not revived as live conjectures.

## What the four cotes contain

Cote16 begins with a formal algebra of graded correspondence operators. It moves from orthogonal projectors and graded inverse pairs to primitive strings, a normalized lowering operator, and an attempted integral universal model. It later develops hyperplane restriction/Gysin identities and letters on the standard conjectures, including algebraic inverses, rationality of characteristic polynomials, positivity and semisimplicity. Between those mathematical threads are reused sheets on local/global Brauer theory, Matlis injectives, derived Hom, étale morphisms and differents, a S.G.A.D. errata sheet, an English cohomology fragment, and an explicitly named Karoubi typescript. These are retained as off-topic context and are not all assigned Grothendieck authorship.

Cote47 develops the transform defined by a rigidified line kernel on an abelian scheme: convolution becomes tensor product, the double transform has antidiagonal support, and a determinant line and shift enter the relative formula. It then studies a nondegenerate line bundle, Chern classes, integral-cycle consequences, rational Chow transforms and derived duality. The proof leaves a concrete unit-fibre compatibility check unfinished.

Cote54 connects universal vector extensions of dual abelian varieties with Hodge–de Rham cohomology, then asks in characteristic p how much is determined by the finite group scheme A[p]. It also contains reused flattening and chamber-theory material. Cote44 contains the intermediate-Jacobian programme, uniform dimension and Tate-module hopes, a pencil-height formula, positivity questions, an undefined τ-equivalence assertion, a cancelled graded-completion draft and the cancelled root axioms. Its reused scan7, absolute lines2948–2964, is editorial commentary on a rédaction, graph terminology, roots, weights and coweights. It does not state the Coxeter-element conjugacy theorem found on the cote46 reused pages; that cross-folder relation is a provenance/theme lead, not a duplicate mathematical claim or established authorship.

## The operator algebra: two models that must remain distinct

Items16001–16003 and16026–16029 are tightly related but not interchangeable. In the literal exterior model over Z, let

\[
\xi=e_1\wedge f_1+\cdots+e_n\wedge f_n.
\]

Then ξⁿ=n!vol. In rank4, multiplication by ξ² from Λ⁰ to Λ⁴ has cokernel Z/2. This checks every hypothesis of the literal free integral exterior example and disproves its claimed integral hard-Lefschetz property. The second pass confirms the Z and the hard-Lefschetz assertion; this is not an OCR repair. The tests for ranks2,4,6,8,10 are exact, and the general factorial formula follows by expanding the product: only permutations of the n distinct degree-two factors survive, and those factors commute.

Raw contraction is a second issue. If Λ₀ is contraction by the dual symplectic form, Λ₀L₀(1)=n. Unit-step lowering on a primitive string has ΛL(1)=1. A rational weighted sl2 treatment cannot by itself identify the integral orders generated by these different operators. The opened Akhtar–Joshua paper is used as a rational comparator, not as a solution of the exact integral formulation. Kleiman’s normalized formalism is also distinguished from the failed exterior model. See `AkhtarJoshua` and `Kleiman1968` in the bibliography.

For the normalized algebra, take one abstract primitive string in each degree i=0,…,n, of length n−i+1. Raising and unit lowering generate its matrix units after the endpoint projectors are fixed. The resulting integral algebra is

\[
\prod_{i=0}^{n}\operatorname{Mat}_{n-i+1}(\mathbf Z),
\qquad
\operatorname{rank}_{\mathbf Z}=
\frac{(n+1)(n+2)(2n+3)}6.
\]

The code checks every matrix-unit product and the endpoint identities for n=1,…,5; the block construction is the general proof. The written bound2n−i for string positions is wrong: the positions are0,…,n−i. The second pass confirms the wrong written bound, which belongs in the readings table as an author slip.

The source itself answers negatively whether L alone determines the grading. For n=1, conjugating by1+tL fixes L and changes Λ to Λ+t(π₂−π₀)−t²L. This supplies a fully explicit independent proof of the author’s negative answer. It does not contradict uniqueness when L **and every π_i** are prescribed. The second pass confirms that final requirement, including the abbreviation “en = temps”.

### A new defect in the later induction

Claim16086 concerns c16:53, absolute lines1932–1936. The source defines

\[
T_k=1-\sum_{i<k}\pi_i-\sum_{j>2n-k}\pi_j
\]

and asserts that Lⁿ⁻ᵏT_k vanishes on all degrees other than k. On H*(P²), with basis1,h,h² and n=2,k=1, T₁ retains h and kills1,h². Thus LT₁(h)=h², even though h lies in degree2. Choosing unit lowering u gives uLT₁=π₂, whereas π₁=0. The required inverse on H¹ is vacuous, so this is a counterexample to the actual hypotheses of the claimed step, not an arbitrary unrelated endomorphism.

The repair is to retain a target cut:

\[
\pi_k=u_kT_kL^{n-k}T_k.
\]

The source cut kills input degrees below k. For input degree r>k, multiplication lands above2n−k, so the target cut kills it. On degree k the desired inverse remains. For the primitive induction with j>0, use target T_(k−2j) before applying u_(k−2j). That cut is already available earlier in the induction. The correction is a present reconstruction; the literal page is unchanged. The wrong projector in the earlier scan17 inverse equation is a separate error, claim16120, also certified by an exact two-dimensional matrix.

## Standard conjectures and the limits of later solutions

The secure letter dictionary is draft C→published B, and draft A→published A. The full draft B/D dictionary and the ℓ|χ subscript remain unresolved. The current second pass changes the surface statement from π₁ to **all π_i**; the externally opened CSG transcription derives from the same scans and does not override that correction. The literal date6.1.1966 is retained. The author’s retraction and later conditional repair are separate layers.

The verified comparisons are [Grothendieck1969](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/StandardConjs.pdf), §§2–3, and [Kleiman1968](https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf), especially2.9–2.10 and3.11–3.15. A finite-dimensional rational correspondence algebra with a positive trace involution has zero radical: the involution preserves the radical, xx* is nilpotent for x in it, and positivity forces x=0. Similarly, a positive adjoint makes u*u invertible; Cayley–Hamilton makes its inverse an algebraic rational polynomial. Rationality and positivity are real hypotheses.

[Jannsen1992](https://epub.uni-regensburg.de/26642/1/jannsen10.pdf), Theorem1, is a theorem about **numerical** motives with characteristic-zero coefficients. Corollary1 assumes algebraic Künneth components before identifying a nilpotent kernel with the radical. It does not prove that the kernel is zero. The elementary ideal(ε) in Q[ε]/ε² is the logical counterexample to that last inference. The bibliography records receipt in1991 and publication in1992, not an invented first-preprint date.

[Katz–Messing1974](https://web.math.princeton.edu/~nmk/old/katzmessing.pdf), Theorem2, supplies finite-field algebraic Künneth projectors. [Deligne1980](https://publications.ias.edu/sites/default/files/Number40.pdf), Théorème4.1.1, supplies cohomological hard Lefschetz. Neither constructs general algebraic lowering operators. The current search also opened [Ancona–Cavicchi–Laterveer–Saccà2025](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms.70133), whose Lagrangian-fibration results have specific support and fibration hypotheses. General B remains unresolved as of the search date. Class A in this package is reserved for an exact match in Grothendieck’s own opened work; matches through Kleiman or Stacks are class B.

## Brauer text: a published gap is still a gap

The elementary discriminant calculation is complete. For nonsingular symmetric integral Q, the pairing on cokerQ is xᵀQ⁻¹y modulo Z. Changing a representative adds an integer, and nonsingularity identifies its dual. A point blowup changes Q to

\[
Q'=\begin{pmatrix}Q-vv^t&v\\v^t&-1\end{pmatrix},
\]

which is integrally congruent to Q⊕[−1] by the triangular matrix recorded in the computation. Passing between arbitrary resolutions additionally uses a common resolution and surface factorization; the local matrix identity does not prove those geometric inputs.

The opened [BrauerIII](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/Alltenlectures.pdf), §8.4, includes a coefficient field k⊂A in its complete normal local dimension-two setting. Omitting it silently produces an unjustified mixed-characteristic extension. The published Remark8.5 explicitly says that the pairing verification was not carried out. Thus the indexed compatibility concern is not disposed of by finding the later publication. The exact boundary-map/sign comparison remains a proof obligation in this dossier; no claim is made that all modern local duality is unknown. The book contents records the IHES prepublication in March1966; the book is1968.

The global Kummer sequence, rational NS-orthogonal complement and ℓ-primary torsion statements are separated from this local comparison. A rational nondegenerate pairing need not be unimodular over Zℓ. [Mumford1961](https://www.numdam.org/article/PMIHES_1961__9__5_0.pdf), §1, proves negative definiteness; it does not by itself establish local Picard representability or the cohomological comparison.

## Fourier transform: precise later theorems and precise surviving errors

For an abelian scheme A/S of relative dimension g and its dual, the relative inversion formula contains both inversion and the line τ_A=detLie(A/S), shifted by−g. The earlier K0 formula omits[τ_A], and an old identity target remains in the proof after the theorem is corrected. Antidiagonal support is explicit on scan6. [Mukai1981](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/BDBEBAC584BE15236C2D62C383A34245/S002776300001922Xa.pdf/duality-between-dx-and-with-its-application-to-picard-sheaves.pdf), Theorem2.2, and [Laumon1996](https://arxiv.org/pdf/alg-geom/9603004), Theorem1.2.4/Lemma1.2.5, provide the verified later comparisons. Mukai’s receipt date is9October1979; its later web-publication date is not the original publication date. Laumon’s arXiv first submission is5March1996.

At the zero section, the Koszul calculation gives

\[
H^i(Le^*e_*\det(T)[-g])
\cong\bigwedge^{g-i}T^\vee\otimes\det(T)
\cong\bigwedge^iT.
\]

This checks the expected cohomology objects. It does **not** verify that the manuscript’s specific comparison morphism induces those isomorphisms. That is the source’s expressly deferred step. A missing e_* in the classifying-map formula is a typing error; ordinary pullback also requires the displayed flatness/Tor conditions. Translation signs are assessed only after fixing T_t(b)=b+t, which puts Φ(P_t) at−t.

The nondegenerate line-bundle theorem has an index and |χ| in general. In the ample field case, E=Φ(L) is a bundle of rank r=χ(L)>0 and φ_L*E is a direct sum of r copies of L⁻¹. The corresponding rational Chern character gives

\[
c_2(E)=\frac{r-1}{2r}D'^2,
\qquad
c_3(E)=-\frac{(r-1)(r-2)}{6r^2}D'^3.
\]

The manuscript has an extra factor r. On a product of elliptic curves with polarization degrees1,2, the correct c₂ has degree1 while the written expression has degree2. This error survives passing modulo torsion. The weaker final coefficient nevertheless equals r(−1)^kc_k(E), so its qualified integrality conclusion survives.

Full integral Fourier duality remains distinct from that salvage. [Beckmann–deGaayFortman2023](https://olivierfortman.github.io/degaaybeckman-integralfourierAVs.pdf), Theorem3.8 and Question3.9, retain a general integral question. [Hasan–Hassan–Lin–Manivel–McBeath–Moonen2025](https://link.springer.com/article/10.1007/s00229-025-01662-7), Theorems4.5,5.5 and7.3, control denominators over a smooth quasi-projective base of dimension d, with §3.2 assumptions: the coefficient ring inverts(2g+d+1)!, and the sl2 refinement additionally invertsν(θ), where degθ=ν(θ)². These restrictions are not suppressed.

The relative Todd formulas also require care. [Moonen2026](https://www.math.ru.nl/~bmoonen/Papers/RPDM.pdf), §§2.4–2.7, corrects a Deninger–Murre bundle-duality slip and gives the qualified Todd cancellation. Its first arXiv version is July2024, while the journal volume is2026. Stronger Chern-class vanishing requires the stated additional comparison. The allegation that Kleiman omitted a parity sign was not verified by the opened2A12–13 candidate; its Pontryagin-to-cup formula has no missing sign under that convention.

## De Rham reconstruction and intermediate Jacobians

[Oda1969](https://www.numdam.org/item/ASENS_1969_4_2_1_63_0.pdf), Corollary5.11, answers the c54:7 question over a **perfect field** of characteristic p: the Dieudonné module of A[p] identifies functorially with H¹_dR(A), with F,V and the Hodge subspace VM. The DOI is10.24033/asens.1175. The paper records a June1967 thesis. The finite group scheme, rather than its geometric points, is essential. The restricted p-operation in the source is also essential; SGA3VII_B4.4.1 provides the height-one restricted-Lie comparison.

[Coleman1998](https://www.numdam.org/article/AIF_1998__48_5_1379_0.pdf), Theorems1.1 and2.2, supplies the canonical universal-extension/de Rham duality comparison for the stated reduced or flat-over-Z bases. The source’s characteristic-zero question is covered; an arbitrary-base theorem is not inferred. The written Ω_A on B is a separate scan-review issue.

The c44 programme is broader and less defined. Its unknown Albanese-type equivalence is not automatically the modern universal regular quotient. [Kahn2021](https://webusers.imj-prg.fr/~bruno.kahn/preprints/Murre-regular3.pdf) corrects the codimension-two boundedness/existence argument. [Achter–Casalaina-Martin–Vial2023](https://api.algebraicgeometry.nl/Article/19846/2023-1-003.pdf), Proposition8.2, requires the specified codimensions1,2,d, a miniversal-cycle degree r, ℓ≠p with ℓ∤r, and a torsion-free target. It cannot establish the manuscript’s all-codimension, all-prime quantifier.

[Ottem–Suzuki](https://arxiv.org/pdf/1906.08994), Corollary4.2, shows that an Abel–Jacobi map in codimension3 need not be universal. That is not nonexistence of an algebraic representative. [ACMV2025](https://smf.emath.fr/system/files/filepdf/smf_ast_455.pdf), Theorem12.12 and§13, distinguishes a qualified symmetric isogeny from positivity in characteristic p; lifting and other hypotheses remain. The2026 torsor refinement, arXiv2506.17033v2, presupposes a regular homomorphism and does not solve general existence.

The historical endpoints were read directly: PicardVI1962 p242; the31August1964 Mumford letter p89; and the **8August1964**, not12August, Serre letter p186. The last supports a surface-fibration height comparison. Künnemann2001 Theorem1.6/Corollary1.7 is a higher-height result for abelian varieties over number fields, not an exact resolution of the underdefined pencil formula. The undefined τ-equivalence is evaluated conditionally: if it means algebraic equivalence up to a nonzero multiple, Clemens1983 supplies higher-codimension counterexamples. No notation is filled from unseen context.

## Auxiliary findings and attribution limits

The cancelled c44:5 root inference is false. In P=Z² take

\[
\Delta=\{\pm3e_1,\pm3e_2,\pm(e_1+e_2),\pm(e_1-e_2)\}.
\]

The set is reduced and spans P as a lattice: e₁=3e₁−(e₁+e₂)−(e₁−e₂), with the analogous expression for e₂. Each ordinary reflection permutes the eight roots. Yet3e₁ is not primitive and its coroot pairs to2/3 with e₁+e₂. The script checks the reflections, reducedness, generation and invariant quadratic form22I₂. [Conrad2014](https://math.stanford.edu/~conrad/papers/luminysga3.pdf), Definition1.3.3, imposes integrality separately. Reflection uniqueness remains true; the weaker paired-lattice variant is not automatically an integral perfect root datum. Both distinctions preserve the paragraph’s cancellation.

The finite-field monogenicity argument fails on F₂³: every element generates at most four of its eight elements. Replacing the unclear word “homogènes” by “principaux” would not save it. The finite-fibre/flatness issue has a separate elementary example A=k[t], B=A×A/(t), with finite étale fibres but torsion as an A-module. The RHom counterexample to an overweak reading uses bounded-below complexes of finite-dimensional vector spaces whose degree-zero Hom is an infinite product; it does not refute the actual alternative with a uniform Ext bound. The ordinary module k[x]/(x−1) has zero(x)-adic completion, but it is not a counterexample in the source’s finite graded category.

The Hodge-algebra orbit examples are earlier-run reconstructions. Their normalization is fixed in the code. The dimension6 witness has detQ=2097152/59049, Q(ξ,ξ)=1 and a cyclic determinant−32/27; a positive row-sum estimate proves an infinite orbit. For the unbounded family, at zero perturbation the chosen block weights give a Vandermonde minor. It remains nonzero for sufficiently small rational perturbation; the finitely many nondegeneracy polynomials are avoided, and a rational overall scaling normalizes ξ. Exact m=1,…,4 checks supplement that argument. This establishes qualified existence, not the dimension4 minimum or geometric realization. A nondegenerate Q does not make every inverse image of φ nonisotropic, and scalar normalization also has a square-class restriction.

Karoubi’s name and initial paragraph on c16:35 match the opened1966 definitions note. The printed dates are12September1966 for definitions and5September1966 for applications; that order is retained. The English Shatz/Amitsur fragment remains unattributed and lacks antecedents. Its Shatz citation was found, but the opened JSTOR page supplied only a wrapper. The proposed EGAIV18.11.6 comparison likewise remains unverified because the49.9MB PDF was blocked by the reader. Hodge1938 and Matsusaka1957 are metadata-verified leads with inaccessible full text; their BibTeX notes are `unverified`.

The S.G.A.D. sheet is now partly located. c16:26 lines1066–1068 and1095 point to [SGA3XVII](https://webusers.imj-prg.fr/~patrick.polo/SGA3/Expo17.pdf), AppendixIII C.1 and C.3; the Cartan replacement at1091 matches [SGA3XV](https://webusers.imj-prg.fr/~patrick.polo/SGA3/Expo15.pdf), proof6.2(iii)(b). The consulted2008 re-edition has a local H_eta/G_eta variation, and no full old-galley collation is claimed.

## Research audit, project links and integration

Every claim and every problem has rows in `literature_search.tsv` pointing to actual executed queries, opened URLs, exact locators and hypothesis matching. Search-group reuse represents shared searches of one tightly related theorem family, not automatic verdict assignment. arXiv version histories, Numdam metadata/PDFs, primary author/journal sites, EGA/SGA, correspondence volumes and bibliographies were consulted. MathOverflow was used as a lead, never as the final theorem authority. zbMATH was queried and direct access attempted; the relevant direct opens were blocked. Its absence is recorded as an access limitation, not a negative literature result. Class D means no exact development was identified in these recorded searches; it does not prove that none exists.

`CHECK_EVENTS.tsv` separates source-alignment checks, targeted mathematical checks, independently reconstructed proofs, exact computations, and source results actually read. A theorem whose URL yielded only metadata is not labelled verified. The computational outputs are finite certificates with expressly bounded scope; no proof or literature fate was inferred from keywords or test success. Public-source response bodies and PDF binaries are not retained in the deliverable; the web logs preserve requests, source IDs, URLs and access outcomes.

The external-project table is empty deliberately. No supplied passage established a mathematical link to La Longue Marche, Les Dérivateurs or a named external S6 project. A local section label and a second-pass mention of Michel Hua’s transcription project are not evidence of such a link. Parent-owned cross-package endpoints should be merged into the canonical items listed in `integration_notes.md`; this agent’s links table includes only endpoints it read directly.

The supplementary c55 lattice and RP² checks were requested by the parent and are kept in a separate file. This agent did not read the c55 source; the parent owns that source verification and canonical identifiers.
