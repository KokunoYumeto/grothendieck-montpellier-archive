# SA07 — Théorie des motifs, part 3

## Scope, authority and how to use the dossier

This dossier consolidates the **339 indexed note entries** in the three supplied packages for cotes 15, 16 and 18, including the related material from cotes 47, 54 and 44 bundled with cote 16. Every indexed entry was read together with its cited transcription passage. All three Pro transcriptions and all six supplied Codex transcriptions were read. Codex notes are leads, not additional rows in the entry-verdict table. The six second-pass files supplied for the cote-16 package were also read; their changed readings take precedence over the corresponding first-pass reading. There are no archive scans in this input, and this run changes no diplomatic transcription.

The principal result is a map of several distinct programmes: **realizations and their comparison torsors; the algebra of Lefschetz correspondences; Fourier operations on abelian varieties; the reconstruction of de Rham cohomology from finite group schemes; and universal quotients of algebraically trivial cycles**. Their common language is that of motives, tensor functors, correspondences, descent and polarization. The surviving pages also contain substantial reused material in analysis, Lie theory, root systems, Haar measure and commutative algebra. That material is included in the claims census, without presenting it as part of a single continuous treatise on motives.

The dossier distinguishes three kinds of evidence throughout: the actual surviving sentence, deletion or question; the exact result found in an opened publication; and a reconstruction or verification made in this run. A theorem can be established today although its proof is absent here. Conversely, an argument can be written confidently here while a necessary hypothesis is missing. Historical class A–F records the fate of the reconstructed assertion; it does not certify the literal formula, resolve an ink doubt, or establish priority from the location of a reused sheet.

The JSON registers contain the complete individual statements, hypotheses, short quotations, locators and assessments. The TSV verdict register has exactly one row per original entry. Retired duplicate identifiers remain resolvable through the alias tables; merged records retain the separate source assessments. Square-bracket citations below are keys in `SA07_references.bib`. Its `note={verified}` means that the named source was successfully opened; the separate verification-scope field states whether this was the theorem text, a particular passage, or metadata only. A metadata check is never used as a proof check.

All present-status assessments are dated **19 November 2026**. First circulation, revised version and publication are separated when the sources provide those dates. “No exact development found” describes the recorded search, not a claim that no such work exists. The literature-search ledger assigns actual query and retrieval batches to every claim; the reference register gives the passage used and its verification limit.

## 1. What the folders contain

`TOPIC.md` describes the whole three-part topic. The table below accounts for every listed folder while preserving this run’s boundary. The catalogue page counts are not counts of pages newly examined here and are not interchangeable with the numerical scan labels.

| Cote | Catalogue subject and count | Treatment in this part |
|---|---|---|
| 10 | Tensor categories; 197 catalogue pages | Other part. No note verdict or theorem assessment imported here. |
| 11 | Formalism of correspondences; 57 pages | Other part. Retained as an orientation endpoint. |
| 12 | Generalities and motivic Galois subgroups; 167 pages; tentative 1964 date | Other part. No claim to have read its absent transcription. |
| 13 | Motivic Galois group; 51 pages; letter dated 1965 in catalogue | Other part. |
| 14 | Algebraic cycles and Hodge, Tate, Lefschetz, Weil conjectures; 131 pages | Other part. Its earlier-note links remain external leads when the target text is unavailable. |
| 15 | Arithmetic and Galois theory of motives; 227 pages; catalogue date 1965 | Supplied Pro package, plus B15-01, B15-02, B15-03, K15-01, K15-02 and K15-08. |
| 16 | Correspondences and Poincaré–Hodge algebras; 55 pages; letters 1966–1967 | Entire supplied package, including bundled cotes 47, 54 and 44 and its second-pass corrections. |
| 18 | Motives and Hodge theory; 61 catalogue pages | Supplied portions 002–017 and 018–062, with intervening reused sheets retained in their own subjects. |
| 19 | Topoi; 95 pages | Other part. It is not a missing portion of this part’s 339-entry index. |

The package inventory and source hashes in the evidence directory distinguish the supplied files from later literature. Cote 15 is especially heterogeneous. Its earlier Codex leaves contain Deuring categories, gerbes and maximal orders, analytic differential equations, a motivic agenda, and exceptional root-lattice calculations. Its later Pro leaves develop motivic points and archimedean fibre functors. Cote 16 works through an algebraic formulary and letters about the standard conjectures. Cote 47 contains the abelian Fourier construction; cote 54 contains the de Rham/finite-group-scheme question; cote 44 contains the programme for abelian quotients of cycle families. Cote 18 moves from residue normalization and Hodge structures to comparison torsors, period fields and semilinear arithmetic actions.

A date visible in a transcription, a date inferred from mathematical context and a catalogue date are different evidence. In particular, the second-pass reading of the letter date remains the authority for the ink; a proposed contextual redating is not installed as a correction. The same rule applies to the current reading `π_i` in the surface-projector attribution, which supersedes the first-pass `π_1`. The precise claim about what Hodge proved in 1938 remains separately qualified because the original publisher page supplied metadata rather than the theorem text. [CL-SA07-307; Hodge1938; Kleiman1968, §§2A, 3.]

## 2. Cote 15: Deuring categories, forms and the obstruction at infinity

### 2.1 From a generator to a category of forms

The early leaves start with an A-linear category, a strict generator X, its endomorphism algebra and the objects obtained from finite projective modules. Their evaluation and tensor–Hom assertions belong to the projective-envelope mechanism of Morita theory. They are correct under the specified existence and idempotent-splitting assumptions. A “generator” without those conditions does not by itself establish the whole categorical equivalence. The word “jolie” and the proposed converse characterization by a filtered union of monogenic pieces remain insufficiently defined in the surviving fragment. [CL-SA07-701–706; MP-SA07-301; AbramsRuizTomforde2022, §1; EtingofRepresentation, Theorem 9.6.4.]

“Localisable sur A” is a descent condition. Under a stack hypothesis, a locally free module twists X by gluing local copies; the resulting local forms and their morphisms are controlled by the endomorphism algebra. The author correctly notices that this argument over Spec A does not prove the stronger assertion about localization of an action category over Spec R. That is a change of base and site, not a cosmetic change in notation. [CL-SA07-705, 709–710; MP-SA07-302; Ferrand2012, §1.]

One literal scalar-extension assertion fails before essential surjectivity is even considered. Let A=Z, R=Z[T]/(T(T−2)), let X=Z carry T=0 and Y=Z carry T=2, and reduce modulo 2. Both objects are finite free over A and R is finite free of rank two. Over Z a commuting map satisfies 2c=0 and is zero; after reduction every c commutes. Thus formation of the R-linear Hom space does not commute with arbitrary base change. Flatness repairs this finite-kernel calculation. It does not show that every newly available action comes from an action over the original ring. The counterexample and its limited refinement have separate claim identifiers. [CL-SA07-707–708; `evidence/root_computations.md`, §1; Stacks0C6I, Lemma 17.22.5 for the related flat sheaf-Hom statement.]

### 2.2 Norm data, gerbes and residual signs

The Deuring–Brauer discussion carries more structure than an unadorned module category. A determinant or norm datum changes the band from a multiplicative-group description to a μ_n description. The displayed ramification exact sequences must retain this norm-trivialization requirement. The familiar maximal-order sequence does not, on its own, prove every norm-refined surjectivity assertion in the fragment. The audit therefore separates the opened order-theoretic theorem from the unfinished structured-category assertion. [CL-SA07-711–716, 723; Voight2021Orders, §§18.1, 18.4–18.5; Ferrand2012, Lemma 1.1 and Proposition 1.2.]

The pages repeatedly move between an equivalence, its isomorphism class and uniqueness up to a unique isomorphism. The later sign qualifications matter. A connected comparison groupoid with a surviving μ₂ automorphism is not uniquely trivialized. Quotienting an explicitly displayed product group by the element f removes a group coordinate, but does not choose a point of the comparison torsor. Likewise, a proposed intrinsic norm object is an assumption where the author writes “Supposons qu’on ait pu…”, not a completed construction. [CL-SA07-714, 716–720; MP-SA07-303–305; Milne1994Finite, §§3.18–3.20.]

The real obstruction has two independent witnesses: the nontrivial real Deuring gerbe at 15/052 and the later doubt about real points of sufficiently large motivic pieces at 15/207. In the precise common case, a category contains h¹ of a supersingular elliptic curve and all geometric endomorphisms. The quaternion endomorphism algebra is ramified at infinity; after extension to R it is Hamilton’s division algebra. A faithful action on a two-dimensional real realization is impossible, because a nonzero quaternionic module has real dimension divisible by four. This also rules out neutralization over a totally real number field for that category. It does not rule out every smaller tensor category or a comparison with a nonneutral quaternionic model. [CL-SA07-013, incorporating former CL-SA07-721; SA07-15; MP-SA07-04; Voight2021Supersingular, Theorem 42.1.9.]

The proposed canonical finite-field recipe is another concrete failure. For p=2 and n=3, Φ₇ is the product of two distinct irreducible cubics over F₂. The full quotient is F₈×F₈, with 64 elements, not F₈. Selecting an irreducible factor gives the expected abstract field, but a compatible algebraic closure still requires compatible embeddings. The manuscript’s canonicity does not follow from the cyclotomic quotient alone. [CL-SA07-718–719; MP-SA07-306; ConradFiniteFields, Theorems 1.1 and 1.10; exact factorization in the root computation output.]

## 3. Cote 15: motivic points, realizations and paths

### 3.1 Fibre functors and geometric points

In 15/195–228 the author tries to recover geometric points, archimedean places and morphisms from their motivic fibres. The language moves among integral tensor functors, Hodge structures, real structures, torsors and discrete automorphism groups. These are not interchangeable. A Tannakian classification by tensor-isomorphism torsors does not characterize which torsors come from geometric points, and an algebraic envelope of monodromy does not identify its underlying discrete group with the topological fundamental group. [MP-SA07-05, 07–08, 18, 25–29; DM12, Theorems 2.11 and 3.2.]

Several assertions about fullness are expressly conditional on Hodge and Tate statements. The precise abelian Hom theorems of Tate and Faltings give important established cases, with their finite-field and number-field hypotheses. They do not prove algebraicity of every cycle class on every product. Similarly, a realization’s full faithfulness and a description of its essential image are different questions. Integral polarizable weight-one Hodge structures give an abelian-variety test case; they do not settle the proposed recognition of all motivic points. [MP-SA07-11–12, 26, 28; P15-Tate66; P15-Faltings83; P15-MilneSV, §§6.8–6.9.]

The claimed finiteness of integral fibre functors cites Borel–Harish-Chandra. The exact opened result concerns arithmetic orbits on a closed orbit in a rational representation with a fixed lattice. The pages do not supply the reduction from their integral tensor forms to that situation. The dossier retains the finiteness claim as a conditional application with a missing step, and keeps the subsequent question about abstract isomorphism of the resulting discrete groups separate. [MP-SA07-09–10; P15-BHC62, Theorem 6.9, pp.510–511.]

The one-fibre rigidity discussion also needs global hypotheses. For a smooth proper algebraic family, the fixed-part theorem controls a global flat section, and its abelian-scheme consequence can extend a local-system morphism known to be algebraic at one fibre. An arbitrary variation on a small analytic disc does not satisfy the same conclusion merely because the disc is connected. Reconstructing a map to a fine polarized abelian moduli space additionally uses compatible integral H¹ data and sufficient rigidification. The broader suggestion that this rigidity characterizes all motivic moduli spaces remains a programme. [CL-SA07-026–027; MP-SA07-15–17; D71, §§4.1.2–4.1.3; P15-MilneSV, §14.8.]

### 3.2 The comparison tower and what its counterexample proves

The author carefully distinguishes comparison of each finite tensor piece from comparison of the whole fibre functor. Finite presentation permits finite diagrams to descend to finite-type models. It does not manufacture a point in an arbitrary inverse limit of nonempty comparison sets. The countable inverse-limit argument is valid when the actual transition maps are surjective. [CL-SA07-032; MP-SA07-19–20; P15-EGAIV3, §§8.8.2–8.8.3 and 9.7.7.]

The proposed universal supply of suitable transition models is false. Take k to be an algebraic closure of Qbar(t), with algebraic part k₀=Qbar. It is countable. In an exhaustion by finitely generated k₀-domains with smooth geometrically connected transition fibres, each fraction field would be relatively algebraically closed in every later one, hence in their union k. Since k is algebraically closed, each such fraction field would itself be algebraically closed. A finitely generated field of positive transcendence degree over Qbar cannot have that property. An exhaustion containing t is therefore impossible with those transition conditions. [CL-SA07-134; SA07-33; MP-SA07-21; full argument in the p15 computation audit, §D8.]

This refutes the proposed tower, not the ultimate comparison of fibre functors. The distinction prevents a local proof failure from becoming a false global conclusion. Bakker–Tsimerman’s precise path/Betti comparison for finitely generated regular extensions is a useful later result, but it does not provide this tower for every countable field. The unfinished uncountable continuation is retained as unfinished, rather than supplied with a modern theorem by analogy. [MP-SA07-20–22; BT22/P15-BT25, Lemmas 4.12–4.13 and Proposition 4.14.]

The conjugate-variety discussion has another quantifier boundary. Charles proved the existence of conjugate smooth projective varieties with different real cohomology algebras, first circulated in 2007 and published in 2009. That answers an existential witness question. It does not distinguish every prescribed pair of embeddings, show that one fixed motive separates all places, or establish that every admissible motivic torsor comes from a place. [MP-SA07-23–27; P15-Charles09, Theorem 1.]

## 4. Cote 16: the algebra of Lefschetz correspondences

### 4.1 The manuscript dictionary must remain local

The letters A, B, C and D are not a stable global dictionary across the fragments. In the operative cote-16 passages, manuscript A concerns hard Lefschetz on algebraic classes and manuscript C concerns algebraicity of inverse Lefschetz, corresponding to printed A and B. The other proposed correspondences of letters remain contextual because independent definitions are missing. C(X) also denotes a vector space of cycle classes. All three earlier-note packages repeated this dictionary; they are consolidated into SA07-1 without removing its uncertainties.

The algebraic core is a graded ring with degree projectors, raising maps, opposite inverse maps and their corner identities. Kleiman’s Theorem 3.15 is an exact published counterpart of the intrinsic-projector argument. Both inverse identities matter, and their supports differ. It is not a theorem that an arbitrary graded ring with a nonzero extreme piece has canonically recoverable projectors. [CL-SA07-201–203, 211; Kleiman1968, Theorem 3.15, p.382.]

### 4.2 Three corrections to the operator calculus

First, the ordinary symplectic exterior algebra over Z does not satisfy the integral hard-Lefschetz isomorphisms claimed in the literal example. For ξ=Σe_j∧f_j, its top power is n! times the volume generator. Already n=2 makes the top integral map multiplication by 2. Rationalization removes this obstruction; a divided-power or modified-lattice construction requires extra choices. [CL-SA07-207; SA07-201.]

Second, ordinary contraction and the manuscript’s normalized lowering operator are different even over Q. On a primitive string of initial degree i,

\[
C(L^jp)=j(n-i-j+1)L^{j-1}p,
\]

whereas normalized Λ lowers by one with coefficient 1. The corresponding normalized string has positions 0 through n−i. The written bound 2n−i in the candidate matrix units is too long. The corrected units produce the expected product of matrix algebras, but this abstract integral string model does not validate the failed exterior-lattice example. [CL-SA07-208–209; SA07-226; Kleiman1968, introduction and §§1–2.]

Third, L alone in an ungraded algebra does not determine lowering. In a length-two string, conjugation by 1+tL fixes L while changing Λ by

\[
\Lambda\longmapsto\Lambda+t(\pi_2-\pi_0)-t^2L.
\]

The author’s circled negative answer and subsequent addition of grading data are therefore substantive. His separate example with nonzero top power but a rank-deficient middle multiplication map also works. These are corrected formulations inside the manuscript, not merely later objections. [CL-SA07-210, 212, 215; SA07-203; exact matrices and quotient-algebra calculation in the p16 audit.]

### 4.3 What the standard-conjecture implications establish

The hyperplane calculations use normalized lowering. For a smooth ample hyperplane inclusion, the correctly typed formula Λ_Y=i*Λ_X²i_* holds on the surviving strings and vanishes on the evanescent middle summand. The inverse Lefschetz condition descends to a smooth hyperplane. The initially stronger equivalence is struck out; a converse needs an additional inverse or surjectivity input on the ambient variety or a product. The clean published implication is A(X×X)⇒B(X). [CL-SA07-227–232, 244–246; Grothendieck1969, p.196; Kleiman1968, Propositions 2.12–2.14, pp.372–373.]

The homological semisimplicity argument has a precise conditional scope: Lefschetz algebraicity together with the appropriate Hodge-type positivity on a product yields a positive trace-adjoint form and excludes a nonzero radical. Jannsen’s unconditional theorem is about numerical motives with characteristic-zero coefficients. It does not identify numerical and homological equivalence or remove the manuscript’s positivity assumptions. The three packages’ repeated modern comparison is merged into SA07-87; the original conditional argument remains a separate item and claim. [CL-SA07-237–239; SA07-236; Kleiman1968, Propositions 3.12–3.14 and Lemma 3.13, p.381; Jannsen1992, Theorem 1 and Lemma 2.]

The same care is needed for the Weil bounds: the standard-conjecture route uses positivity in addition to algebraic inverse Lefschetz. Deligne’s proof by another method does not retrospectively prove that omitted implication or settle the standard conjectures. Known surface, abelian and other special cases should not be summarized as a solution for all threefolds. [CL-SA07-241, 245; Grothendieck1969, pp.196–198; Deligne1974WeilI, Theorem 1.6; DeligneWeilII1980.]

At 16/047 the proposed reduction through smooth hypersurfaces is expressly withdrawn: the birational and smooth-specialization chain would force an impossible simply-connectedness conclusion. The replacement hope concerns singular hypersurfaces. No singularity class, replacement cohomology or correspondence theorem is supplied. The withdrawal is more than a correction of novelty, and general modern singular theories are not an exact answer to its unspecified replacement. [CL-SA07-242–243; SA07-82 and SA07-241.]

## 5. The bundled abelian-variety and cycle programmes

### 5.1 Cote 47: a relative Fourier operation

The Poincaré line bundle defines a transform exchanging convolution with tensor product. Its correct general setting uses perfect complexes and derived base change; the page’s parameter scheme need not be only the dual abelian scheme. A margin extends the binary kernel identity to more general flat-group situations, but it does not construct a dual object or a Fourier equivalence for every flat group. A monoidal-functor claim would also require coherent unit and associativity data. [CL-SA07-265–267; Laumon1996, §§1.1–1.3; Stacks0FYP.]

Over a general base the inverse-transform formula retains three visible pieces:

\[
\Phi_{A^\vee}\Phi_A\simeq(-1_A)^*(-)\otimes\pi_A^*\det\operatorname{Lie}(A/S)[-g].
\]

The determinant line is not canonically trivial merely because it has rank one. The inversion and shift also matter. The kernel direct image is supported at the zero section with precisely this line and degree. Fibrewise vanishing for nontrivial degree-zero line bundles locates support, but does not by itself determine the scheme structure or verify the canonical map at the identity. These are the exact points left for checking in the draft and supplied by the published relative theorem. [CL-SA07-268–274; Laumon1996, Theorem 1.2.4 and Lemma 1.2.5.]

The Chern calculation contains a genuine arithmetic slip. In the ample field case, if r=χ(L)>0 and D′=−c₁(ΦL), then

\[
\operatorname{ch}(\Phi L)=r\exp(-D'/r),\qquad
c_t(\Phi L)=(1-D't/r)^r.
\]

The displayed expanded coefficient in the manuscript has one extra factor χ. On a product of elliptic curves with a line bundle of bidegree (1,2), the corrected formula gives c₂=[pt], whereas the literal extra factor gives 2[pt]. The weaker divisibility consequence survives because the erroneous expression for c_k is actually χ times the correct integral Chern class. [CL-SA07-277–279; Beauville1983, Proposition 5; p16 exact computation.]

The following question about formulas modulo torsion is narrower than the assertion that Fourier preserves the entire integral Chow group. For the verified ample-bundle formula, rational equality yields an integral equality modulo torsion after clearing denominators. The page’s relative-base and K-filtration meanings remain to be specified. Modern integral-Fourier counterexamples apply to a stronger whole-Chow statement; Kahn’s étale-Chow replacement has its own characteristic and 2-torsion qualifications. Neither is automatically a refutation or solution of every interpretation of this leaf. [CL-SA07-281; BeckmannFortman2023, Theorem 3.8; EngelFortmanSchreieder2025, Theorem 1.1; Kahn2026, Theorem 1.2 and Corollary 1.3.]

Relative Grothendieck–Riemann–Roch introduces Todd factors. The reverse product formula simplifies to the usual parity sign only after the relevant Todd class is shown to vanish. Moonen’s 2026 Corollary 2.7(1) gives the required vanishing for an abelian scheme over a connected smooth finite-type scheme over a Dedekind domain. This is a precise later result with base hypotheses, not permission to erase every relative Todd factor. The alleged sign error in Kleiman is also checked against what he actually printed: his forward convolution formula is sign-free and does not contain the reverse formula to which the parity objection applies. [CL-SA07-280–283; Moonen2026, §§2.3–2.7; Beauville1983, Proposition 3(ii); Kleiman1968, §§2A.12–2A.13.]

### 5.2 Cote 54: de Rham H¹ and A[p]

The universal vector extension has the dual abelian variety in a crucial place. If B=A^∨, the tangent sequence of E(A) identifies with the Hodge extension for B; invariant differentials on E(A) identify with H¹_dR(A). This prevents exchanging Lie E(A) and invariant forms without dualizing. The bigraded pairing also uses Ω_B on the B factor; the displayed Ω_A there is ill-typed. [CL-SA07-286–288; Coleman1998, Theorems 1.1 and 2.2.]

The final explicit question has a particularly exact later answer. For an abelian variety over a perfect field of characteristic p, Oda identifies the contravariant Dieudonné module of A[p] with H¹_dR(A), including the canonical sequence. Oda explicitly credits Grothendieck’s 1966 discussion. This is stronger than the equivalence between restricted Lie algebras and height-one infinitesimal group schemes, which alone does not recover the full F,V data. Oda’s subsequent statement for a general smooth proper variety with a rational point is an injection with a specified image, not the same full abelian theorem. [CL-SA07-289–291; SA07-48 and SA07-269; Oda69/Oda1969, Corollaries 5.11–5.12, p.131, with the following remark on p.132; G66, p.102; SGA3VIIb, Theorem 4.4.]

### 5.3 Cote 44: universal quotients of cycle families

The letter labels several assertions as theorems while admitting that little has been proved. Its intended “Albanese equivalence” is not defined on these leaves. The proposed abelian varieties J^i, dimensional bound, complementary duality, polarization and hyperplane behavior therefore form a programme, not an established all-codimension construction. The dossier states the strongest formulation supported by each actual sentence and separately gives a modern formulation in terms of universal regular representatives. [CL-SA07-295–303.]

The modern theory settles important endpoint and codimension-two cases. The existence criterion is a bound on dimensions of regular targets, and the codimension-two argument needs genuine torsion control. Tate-module injections retain restrictions involving the characteristic, torsion and the multiplier of a miniversal cycle. A general Abel–Jacobi target need not itself be the universal representative in codimension three, even where a representative exists. These boundaries prevent the known special cases from being read as a proof of the letter’s full programme. [Kahn2021, Theorem 1 and pp.2–4; ACMV2023, Theorems 6.1, 7.1, 7.9, 9.5 and Proposition 8.2; OttemSuzuki2020, Corollary 4.2.]

The proposed positivity is stronger than a symmetric nondegenerate divisor correspondence: a symmetric isogeny to the dual need not be a polarization. The height/intersection formula similarly needs vertical corrections, admissible lifts and sign conventions. Modern refined heights answer specified versions with those hypotheses; they do not validate the unqualified formula. [CL-SA07-298–299; KahnHeight2024, Theorems 4.14, 5.6 and 5.10; Kunnemann2001, Theorem 1.6 and Corollary 1.7.]

The all-cycle extension of numerical=τ-equivalence is false if τ means torsion modulo algebraic equivalence: the non-torsion Griffiths-group phenomenon on a very general quintic threefold supplies a counterexample. This is explicitly conditional on recovering that meaning of the manuscript’s undefined τ. The divisor theorem attributed to Matsusaka must not be generalized silently. [CL-SA07-301; Clemens1983, Theorem 0.2 and Corollary 0.3.]

## 6. Cote 18: periods, Hodge structures and real descent

### 6.1 The residue factor and the fixed topology

The local calculation in 18/015–017 and the later formula in 18/019–021 are one normalization claim. With the manuscript’s complex orientation and algebraic residue convention, the algebraic cycle class corresponds to (2πi)^p times the Betti class. Transporting through σ:C→k transports this scalar too. Proper pushforward of relative codimension p shifts degree by 2p. For a correspondence of codimension r on X×Y, with dim X=d, the combined scalar is (2πi)^(d−r), cancelling for a degree-preserving correspondence. [CL-SA07-073 and the adjacent p18 claims; SA07-71; MP-SA07-44, 202–203; D71, §§2.1.13–14, 2.2.4–6; ST03, Theorem 4.1.]

The local integral is redone, but its validity does not decide a written index. A transversal isolating a codimension-p intersection has dimension p, not n−p; an ordinary cohomological Gysin map has shift 2p, not p. The uncertain exponent −n or −m and the wrong-looking sheaf subscript remain alarms for the next scan reading. Trace formulas from another convention may carry a dimension sign and are not copied verbatim into this normalization.

The author also distinguishes the two topological isomorphisms of an already fixed complex topology from arbitrary abstract field automorphisms or new complex topologies. Independence in the first sense does not imply topology-independent integral period lattices. The stronger topology-independence sentence is deleted. The P¹/Tate example already explains why this distinction is mathematically substantive. [MP-SA07-204; CL-SA07-470, 480; D71, §2.1.]

### 6.2 Two conjugations, a tensor twist and the Artin obstruction

The identity marked “à vérifier” at 15/203 reappears in the real discussion. For compatible geometric realizations, coefficient conjugation and de Rham descent commute, with product the linear real Frobenius. Arbitrary semilinear involutions need not commute. The fixed real form is V⁺⊕iV⁻. Multiplication of complex coefficients makes this construction tensorial, but the evident additive map V→V⁺⊕iV⁻ has a minus sign on the negative-negative tensor component. [CL-SA07-009; SA07-10; MP-SA07-02, 206.]

The question whether ordinary and twisted Betti functors are tensor-isomorphic depends on the category. A real Artin sign object with square the unit forces a rational square equal to −1 under a proposed isomorphism, yielding an obstruction. A pure Tate category alone does not give that same argument. The stronger classification “real Frobenius is trivial only on even Tate motives” fails in a category containing Artin motives: the Artin sign object tensored with Q(−1) has trivial real Frobenius while retaining its Artin factor. These are algebraic Artin/Tate objects, so invoking the Hodge conjecture does not remove the counterexample. [MP-SA07-207, 210; DM12, Proposition 6.17; D71, §§2.1.13–14; p18 sign certificates.]

The related component-group argument needs the geometric kernel to equal G⁰. Corrected Deligne–Milne Propositions 6.22(a) and 6.23(a), footnote 21, restore an absolute-Hodge hypothesis omitted in 1982. An arithmetic exact sequence alone does not establish connectedness. Their Proposition 6.25 supplies an abelian case. The dossier merges the repeated real-Frobenius generation claim while preserving this boundary and the separate fullness assumptions. [CL-SA07-025; MP-SA07-14; DM12; Kahn25, Theorem 5.10.]

Finally, the distinguished complex comparison point being nonreal is not the statement that the entire tensor-isomorphism torsor has no real point. The ordinary Tate object can force the former through its real-Frobenius sign. The quaternionic obstruction of Section 2 concerns the latter in a different category. Confusing them would erase two different questions in the manuscript. [CL-SA07-479 and CL-SA07-013.]

### 6.3 Period genericity and the additional splitting coordinates

The period sheets consider both a comparison point and a Hodge-splitting point. The proposed joint transcendence degree g+u is stronger than ordinary period genericity. The object called Q is also described both as a space of Levi splittings of dimension u and as a torsor under a group that includes an extra Tate G_m. That ambiguity must be resolved before any numerical dimension is installed as the intended conjecture. [CL-SA07-058–063; MP-SA07-38–40.]

For a non-CM elliptic curve over Qbar, the full period/quasiperiod transcendence degree four remains beyond the verified results used here. The CM case and its degree-two statement have a different fate. The subgroup or torsor generated by a period locus is also a different invariant from the raw algebraic locus of the period point. Kreutz–Shen–Vial’s 2026 version, first circulated in 2022, proves specified generated de Rham–Betti torsor statements for elliptic products; it does not prove the full non-CM degree-four conjecture. Bakker–Tsimerman’s theorem is geometric over function fields, not a general arithmetic period theorem over a number field. [CL-SA07-068; MP-SA07-41–42; BC16, Definition 2.9 and Conjecture 2.12; P15-KSV26, Proposition 3.1 and Theorem 5.13; BT22, Theorem 4.25.]

The algebraicity of the Hodge splitting for an elliptic curve is a further question. The CM direction is established. The converse appears as Katz’s Question 4.0.8, following Lemma 4.0.7, and a related formulation appears in Bertrand. No verified resolution of that converse was found in the recorded searches through November 2026. A rational Betti-projector argument does not apply to an algebraic de Rham projector. The dossier rejects that shortcut without claiming to have proved the converse or a universal impossibility theorem. [CL-SA07-071–072; MP-SA07-43; P15-Katz76, p.501; P15-Bertrand78, §6, Conjecture 3; P15-BDP13, §1.4.1.]

On 18/045 the two-elliptic-product dimensions 7 for the relevant group and 5 for a Borel are consistent under the reconstructed non-CM and nonisogeny hypotheses. The author rejects a count of six for an incompletely defined field K. Without identifying K, that rejection cannot be promoted to a refutation of the full period conjecture. [MP-SA07-218; MZ99, Corollary 3.9; Imai76, metadata-only backward reference.]

## 7. Cote 18: integral and adelic comparisons, then semilinear actions

The four-part programme on 18/043 separates comparisons between Betti and de Rham lattices, between Betti lattices inside ℓ-adic realizations, mixed-characteristic comparison, and p-adic cohomology in characteristic p. Later theories answer substantial precise parts. Oda gives the abelian H¹ result; de Rham–Witt theory computes crystalline cohomology under its smooth perfect-base hypotheses; integral p-adic and prismatic theories give period-ring comparisons with their actual base conditions. The perfect-prism condition in the étale part of Bhatt–Scholze’s Theorem 1.8 is retained. [MP-SA07-214–217; Oda69; Illusie79, Theorem 3.2; BMS18, Theorems 1.7–1.8; BS22, Theorems 1.8 and 5.2.]

Ruimy–Tubach’s 2026 work, first circulated in 2024, gives an ordinary t-structure on geometric integral Nori motives, a derived equivalence for regular coefficient rings flat over Z, and arc-hyperdescent over finite-dimensional qcqs Q-schemes. These are major developments of the categorical framework. They do not assert that every integral tensor-comparison torsor written on these pages has a point. The existence of the proposed comparison g, its ambiguity modulo G(Z), and uniqueness after all finite components are fixed are therefore separated. Only the latter uniqueness calculation is formal once the required point and faithful torsion-free realization exist. [MP-SA07-224; RT26, Theorems 4.2.3, 4.3.2 and 4.4.2.]

The finite-index Galois-image premise is stronger than a Tate statement. For the minimal rank-one tensor category generated by Q(−2), without adjoining Q(1), the cyclotomic-square image has index at least 2^r when projected to r suitable odd-prime unit groups. It therefore has infinite index in the full product. This is a counterexample to that explicit reconstruction. The manuscript’s marginal “géom.” and its intended group convention are not clear enough to declare the same unqualified verdict on every possible reading. Hodge-maximality and the choice of a covering group matter in modern adelic results. [MP-SA07-219; CM20, Theorem A(ii); p18 computation audit, §8.]

The admitted generic-point lemma has a valid Baire proof: in a smooth analytic chart over a countable field of definition, countably many proper algebraic loci cannot fill a nonempty open subset of a geometrically irreducible component. It does not supply the arithmetic openness needed to apply it. Nor does the dimension (n−1)dim G of a free diagonal quotient prove genericity of a chosen arithmetic orbit. [MP-SA07-220–221.]

Strong approximation is another independent premise. The supplied SL_n argument is valid for the restricted finite adele ring under its Dedekind-domain setup. G_m does not satisfy the analogous general density statement: an appropriate open subset of finite integral units avoids the diagonal rational units, whose intersection with the full unit product is only {±1}. The restricted adeles must also be distinguished from an unrestricted product of local fields. [CL-SA07-456–457; MP-SA07-222; MilneANT20, Proposition 3.28; BourbakiAC65, exact printed match not fully collated.]

In the final sheets, Gal(k/k₀) denotes the full field-automorphism group of a field k abstractly isomorphic to C and transcendental over k₀. It is not the profinite absolute Galois group. The finite realizations factor through the algebraic Galois quotient, while the de Rham scalar action sees the transcendental kernel. The right-cocycle law, inversion to a left cocycle, change of reference and corrected coboundary are checked as noncommutative words. An ordinary homomorphism associated with such a cocycle belongs in a semidirect product retaining the scalar action. [CL-SA07-443–444, 475, 481; MP-SA07-226–230.]

Genericity of the period point corresponds to density of its actual automorphism orbit, and hence of the translated cocycle image under the stated finite-type and field hypotheses. Density of the subgroup generated by that image is weaker. The audit gives an explicit quadratic G_m example separating them. It also keeps the minimal-field-of-definition remark at its proper level: a curve with j=π shows that a minimal curve field can contain π, but this alone does not settle minimal descent of its motive up to isogeny. [MP-SA07-228–229; BC16, §§2.9–2.13; BT22, Theorem 4.25.]

## 8. Reused sheets and computations outside the motivic core

The analytic leaves are not discarded. Their local primitive, continuation, inverse-function, differential-equation and Frobenius arguments are checked with domain, regularity and convergence hypotheses. Several literal estimates are too strong: the binomial square-root line, a missing radius factor, boundary summability and a p-adic coefficient estimate all have explicit tests. The nonarchimedean ODE argument is repaired at the level of analytic germs in characteristic zero, using a formal flow and a factorial growth bound. Uniqueness of that germ must not be expanded to uniqueness among all locally analytic functions on a disconnected p-adic disc; a locally constant counterexample separates the two. [CL-SA07-735–759; root proof audit, §§4–7.]

A continuation remark about concatenating paths also needs its homotopy convention. For unrestricted free path homotopy, paths contract to their initial points; endpoint-fixed homotopies respect concatenation. The valid limited warning is that independently chosen homotopies may fail to have matching common-endpoint tracks. The literal broader claim is therefore not retained without additional restrictions. The reading is not altered. [CL-SA07-771; Hatcher2002, §1.1, pp.25–26.]

The E₆ and E₇ lattice calculations have finite exact certificates. The code constructs the Cartan matrices, enumerates 72 and 126 roots, computes quotient forms and Weyl-group actions, and verifies the stated group orders and kernels. It does not claim an independent proof of simplicity. The exact parallel was located in Bourbaki, Chapter VI, §4, Exercises 2–3, pp.242–243 of the opened English edition. The French chapters appeared in 1968; archival placement does not identify the individual contributor. [CL-SA07-760–761; BourbakiLie4to6; root lattice output.]

Other root-system fragments have equally precise publication matches: the closed-positive-subset argument at Chapter VI, §1, no.7, Proposition 22; contraction of an order-three Coxeter edge at §4, no.1, Lemma 6; the A_l root/weight lattices at §4, no.5; and the G₂ highest-root convention in Plate IX. Instructions about absent numbered propositions, factorial corrections and an unidentified operator of fourth power one remain unidentified. Familiar formulas are not substituted for those missing antecedents. [CL-SA07-445–451, 465, 476–478; MP-SA07-46–63; BourbakiLie4to6.]

The Haar fragments match Bourbaki’s extension and local-isomorphism results with changed draft numbering. Dedekind factorization, valuations, approximation, lengths and semilocal principal ideals are checked in their actual hypotheses. An anonymous English Hilbert-polynomial-like fragment and a deleted Čech-cohomology block remain class F: a valid local formal inference does not identify the missing geometric theorem or its author. The Karoubi reused leaf is explicitly his work; the exact 1966 note was located. Matlis’s theorem is likewise treated as an explicitly cited result, not as an original Grothendieck discovery. [CL-SA07-248–264, 452–468; BourbakiHaar63; MilneANT20; Matlis1958; Karoubi1966.]

## 9. What consolidation changes in the earlier notes

The earlier notes were generally careful about uncertain readings, cancelled text and conditional theorems. The chief gain is consolidation and sharper scope, rather than mass rejection. The same standard-conjecture dictionary, two-conjugation identity, cycle normalization, Oda comparison, numerical-versus-homological distinction and normalized matrix algebra had been recorded more than once. The canonical items retain all witnesses and preserve the evolution from a question to an explanation.

Several corrections matter disproportionately. A second-pass reading must supersede its older alternative. A smooth-hypersurface reduction is genuinely withdrawn. Ordinary contraction differs from normalized lowering. A rank-one determinant line is not a canonical trivialization. A corrected Chern coefficient can leave a weaker divisibility statement intact. Numerical semisimplicity is not homological semisimplicity. An exact arithmetic quotient is not geometric connectedness. A generated period torsor is not the full period locus. These distinctions are now enforced consistently across the three packages.

The earlier runs’ own comparisons remain labelled as theirs. The elliptic degree test distinguishing a period/Hodge SL₂ from the Lefschetz action, the G_m counterexample to a centre-free inference, and the matrix-algebra repairs are useful, but are not sentences on the archive pages. Similarly, this run’s explicit refinements and new counterexample formulations are marked as such and are excluded from counts of statements literally present in the manuscript.

## 10. Reading alarms and link boundaries

The reading register records mathematical pressure on a sign, index, quantifier, deletion scope, operator name or antecedent. It does not decide whether the author slipped or the transcription misread the ink. High confidence in a counterexample can coexist with low confidence in an ink reading. Second-pass confirmations are reported as supplied evidence, not as fresh scan inspection by this run.

The most consequential alarms concern the Lefschetz matrix range and opposite inverse supports; the missing Gysin factor 2 and transversal dimension; Hodge total degree p+q; the nonzero-versus-unit shorthand in formal coalgebra maps; flatness in an étale criterion; the field K and the 5/4 bound; the meaning of “géom.” in an adelic premise; and whole deleted paragraphs mistaken for retained assertions. Less consequential editorial and bibliographic alarms are still included, with their mathematical weight stated.

Archive and publication links with both endpoints available are checked directly and carry exact locators. The links register separately records where a target lies outside the supplied part, where a publication was verified only at metadata level, or where a source remains unidentified. Such rows are leads with an explicit unresolved endpoint, not two-ended verified links. The absence of those target materials is an evidentiary boundary that a completed audit must disclose; it cannot honestly be replaced by a claimed reading.

The project leads are also provided in their own table. LM7 C.1, LM7 C.8, LM7 E.23, LM6 A.22, FLAGGED_149 B.9 and WG2 §2.4 #3 retain the run names and statuses reported by the earlier notes. Targeted searches did not resolve their original endpoint texts, and the personal-context service was unavailable. No mathematical status from those leads is promoted on that basis. The same separation applies to broad references to La Longue Marche, Les Dérivateurs and S6: relevance does not supply the requested specialized theorem, and no solution of their open problems is inferred here.

## 11. Research tasks that this dossier can support

`SA07_directions.md` ranks the next tasks by mathematical interest and what a few-hour run could concretely achieve. The highest practical priorities are a scan-led convention audit, a repair or exact limitation of the countable comparison construction, a precise elliptic period/splitting dictionary, an integral normalized-Lefschetz model, and a relative Fourier normalization companion. The more ambitious recognition and all-codimension cycle programmes are included with smaller first deliverables and explicit barriers.

Each direction names its originating item, claim and problem identifiers, states what it would establish, separates known input from a new target, and gives a first concrete step. No direction is developed into a new research project in this dossier. The detailed checks already supplied belong to verifying the manuscript’s claims and computations, not to declaring those future programmes solved.

## 12. Counts and audit coverage

The following counts are generated from the final integrated registers. They distinguish the note-entry verdicts, canonical items, historical classes, manuscript status, editorial questions and verification events. A false literal formula can coexist with a class B published correction; a problem entry can be a settled deferred check or an unidentified fragment rather than a currently open mathematical problem.

<!-- FINAL_COUNTS -->
