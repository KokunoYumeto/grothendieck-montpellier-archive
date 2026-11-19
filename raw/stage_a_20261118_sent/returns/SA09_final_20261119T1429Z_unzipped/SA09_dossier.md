# SA09 — Complexe de De Rham, part 2

## Consolidated research dossier: cotes 137 and 138

**Status date: 19 November 2026.** This dossier consolidates the supplied research notes against their diplomatic transcriptions. It separates three evidential levels throughout: the statements and revisions visible in those transcriptions; results located in opened literature; and mathematical reconstructions or counterexamples supplied by the earlier runs or by this run. No manuscript scan was supplied or inspected. No transcription has been altered.

The two folders pursue different mathematical programmes. Cote 137 moves from the decomposition of simplicial modules to universal coefficient functors, relative exactness, multiplication and polynomial/divided-power structures. Cote 138 begins with descent and covering automorphisms, develops explicit Kummer and Fermat towers, and turns to cartographic groups, arithmetic actions, small-map calculations and operations on maps. The catalogue's common topic title is retained, but it does not justify rewriting either sequence as a chapter of a later project.

The complete item, claim and problem records are the accompanying JSON files. Original one-based line numbers and scan markers locate every mathematical assessment. The four component proof audits, exact programs and saved outputs give the arguments behind the conclusions summarized here. The global alias table records the small number of cross-packet identity merges; it allows a citation in a component audit to be resolved without renumbering the source record.

## 1. Corpus, chronology and method

### 1.1 What is actually supplied

| Cote | Catalogue description in TOPIC.md | Catalogue pages | Treatment in this part |
|---|---|---:|---|
| 136 | Divided-power de Rham complex; IHÉS conference of 1976 | 375 | Orientation only: explicitly assigned to the other part; no transcription is supplied here. |
| 137 | Dévissage of ∂-perfect semi-simplicial complexes and multiplicative structures; catalogue suggests 1975 or 1976 | 85 | Both supplied transcription packets read completely. |
| 138 | *Cartes. Étude arithmétique*; catalogue suggests 1976, 1977? | 132 | All three supplied transcription packets read completely. |
| 139 | Émile Picard prize medal | 2 | Orientation only: explicitly assigned to the other part. |

The prompt describes 380 indexed entries from five packages. The supplied index actually has 380 entries from **four** packages. A fifth source package, MPL_137_002-044, is present with substantial notes but has no rows in that index. It was nevertheless read for the claim and problem maps. Its unindexed R-notes create no additional verdict rows. The attachment contains no second-pass or Codex material for this part; that is an expected source configuration, not an unfinished checking stage.

There are 84 supplied scan markers in cote 137, covering 2–86 with 6 absent, and 129 in cote 138, covering 1–133 with 24, 79, 88 and 92 absent: **213 supplied scan markers in all**. These counts describe the transcriptions. They do not silently repair the catalogue page counts or infer what missing physical pages contained. The source manifest records the files, line counts and hashes.

| Indexed package | Entries | Local read coverage |
|---|---:|---|
| MPL_137_045-086 | 104 | Every indexed entry and both cote 137 transcriptions. |
| MPL_138_001-045 | 102 | Every indexed entry, complete transcription and doubts table. |
| MPL_138_046-089 | 47 | Every indexed entry, all 1,724 transcription lines and doubts. |
| MPL_138_090-133 | 127 | Every indexed entry, complete transcription and doubts table. |

Administrative leaves carry June 1978 dates and a 1980 order form. They do not date all adjoining mathematics. The source therefore does not establish priority relative to Schinzel's 1977 publication or Belyi's 1978 submission. Two printed English inserts in cote 137 are Sullivan material, not Grothendieck's autograph assertions: the author-hosted extended typescript was matched at its printed pages 112 and 105. Its pagination differs from that of the associated1975 proceedings item. The separate provenance claim CL-SA09-137-052 prevents those statements from being counted as Grothendieck-original theorems.

### 1.2 How the classifications are used

Every verdict was written after reading the note and its source passage. Scripts serialize those decisions, assemble explicitly chosen merges and check coverage; they do not classify notes from headings or keywords. A source may agree with a note even when the source's mathematical assertion is false: the item check concerns fidelity, while the claim record concerns mathematical truth and development.

The six fate classes are the requested development classes, not truth values. Class C can describe a false broad assertion with an established corrected theorem, a construction with an unresolved coherence obligation, or an identifiable programme with only partial development. It does not automatically mean that the literal assertion is still open. Class F means that the text does not identify a definite mathematical statement at the necessary precision. No class D novelty inference has been made merely because a search returned nothing. A current-run proof or an AI-assisted contemporary report is not, by itself, evidence that a result is historically established in the literature.

Search records distinguish first circulation, publication and later revision where those dates were verified. One illustrative correction is Guillot's paper: arXiv circulation began on 8 September 2013; its journal volume is dated 2014; the publisher records release on 27 April 2015. Bibliographic verification is also distinguished from proof inspection. Higgins's official reprint record was opened, but its large full PDF was not read. A González-Diez–Jaikin-Zapirain theorem was recovered as exact indexed primary text, but direct full-source opens failed, so its entry remains explicitly unverified under the requested rule. These limits do not weaken conclusions independently supported by other opened sources.

## 2. Cote 137: from elementary complexes to structured cochains

### 2.1 The elementary objects and the first correction

The opening pages organize nonnegative chain complexes through identity disks and spheres. Write D_i(P) for P→P with identity differential in degrees i and i−1, and S_j(P) for P in degree j. A nonnegative acyclic complex of projectives splits successively from degree zero. If its homology is projective, disks and spheres separate after choices. The coefficient modules have intrinsic isomorphism classes; the splitting maps need not be canonical. This is the appropriate Dold–Puppe setting for the initial dévissage, rather than a claim about arbitrary unbounded complexes (CL-SA09-137-001–005; Dold & Puppe, 1961).

The surviving version of Lemma 2 at scan 4 does not follow from projectivity alone. The constant object Z, with the displayed equality case q=q′=1 and coefficient module Z, supplies an identity morphism in the Hom group claimed to vanish. Strict degree separation gives a valid support argument; equality requires an additional vanishing condition. The cancelled acyclicity qualifier therefore matters. The counterexample is mathematical evidence for the reading table, not a decision about the ink.

The nearby divided-power de Rham comparison is weightwise. Its later occurrence at scan 73 expressly withdraws the untruncated formulation. These two occurrences are one problem, MP-SA09-01: identify and prove the exact finite-weight comparison, its terminal kernel and its naturality. They are not evidence for an already established unbounded reconstruction of all supplementary operations.

### 2.2 Rank polynomials do not replace the objects they count

For the split case the source's rank formula is

\[
\rho(n)=\sum_{i\geq1}\mu_i\binom{n+1}{i}+\sum_{j\geq0}\nu_j\binom nj.
\]

Its nonnegative coefficients detect a bound on normalized degrees in the strict finite-free setting. The leading coefficient in degree N is (μ_N+ν_N)/N!, and evaluation at−1 gives the Euler characteristic of the sphere coefficients. The audit independently checks the formula and records the missing factorial and omitted degree-zero sphere as separate alarms. The binomial basis is a basis for integer-valued polynomials, not the monomial-integral ring Z[t].

Tensor closure and nonlinear closure have different outcomes. For tensor products, integral free disk/sphere models, Künneth and base change supply the strict free argument; actual projective coefficients must still be retained in the general case. In contrast, normalizing Γ²K(Z,1) gives a two-term differential −2 and homology Z/2. The author's withdrawal of nonlinear preservation of projective homology is therefore supported by an explicit calculation (CL-SA09-137-007–008).

Nor do equal ranks classify projective modules over an arbitrary ring. The invertible nonprincipal ideal (2,1+√−5) in Z[√−5] gives a rank-one counterexample, with invertibility and nonprincipality checked in the proof audit. Over a PID, the torsion factors themselves remain indispensable: D_1(2) and D_1(3) have the same numerical term counts and different homology.

The finiteness discussion on scans 14–15 also distinguishes properties of a chosen complex from properties of its derived isomorphism class. An infinite-rank contractible disk represents a perfect zero object. An unbounded contractible complex with finite-free normalized terms can have exponentially growing simplicial ranks. Conversely, placing Z/p_i in degree i for distinct primes yields residue-field calculations whose degrees are individually finite but not uniformly bounded; the resulting complex is not perfect. A bounded representative need not map degreewise surjectively onto an arbitrary unbounded representative. These examples refute the broad formulations without discarding the useful strict criteria (CL-SA09-137-011–014; Illusie, 1971, ExposéI; StacksPerfect; StacksPseudo).

### 2.3 Bricks, density and the coefficient functor

The PID calculation enlarges the brick list by torsion disks. Their chain maps obey actual differential equations: in equal degrees the two scalars satisfy mq=np, and compositions use the resulting scalar or matrix formulas. Several apparent index slips can be tested against one disk. This detects an omitted rank summand, a displaced saturation index and a questionable equality arrow between an identity disk and a nonunit disk. Completing these concrete tables is different from proving an abstract recognition theorem over a Dedekind or general base (CL-SA09-137-015–019; MP-SA09-04–06).

The next step asks whether a subcategory of bricks recovers the larger category and its functors. Mere existence of colimit presentations is insufficient for ordinary set-valued density. In finite-dimensional Q-vector spaces, the object Q generates by finite sums, but the restricted ordinary nerve remembers scalar action alone. A scalar-homogeneous, nonadditive map Q²→Q then defines a natural transformation that is not linear. Additive-envelope reconstruction is valid; ordinary density needs the appropriate canonical presentation or enriched hypothesis (CL-SA09-137-020–022; Isbell, 1960).

Variance is equally material. The functor M↦Hom(X,M) is covariant in M and contravariant in X. The source's finite tensor/Hom weights do not justify arbitrary presheaf coends or unrestricted derived enrichment. Calling the finite-free complex category abelian is false: multiplication by 2 on Z[0] is a noninvertible bimorphism there. A same-index pairing in the universal cochain category also fails on a suitable adjacent generator; a shifted target is a mathematical repair requiring scan confirmation.

These observations locate the central programme of scans 38–39. Additive generators may determine an additive functor on its finite envelope. Recovering tensor, divided powers and the additional operations from that functor is a further construction. Comparing the resulting cochains with de Rham data, and determining how much homotopy type they retain, are stronger questions again (CL-SA09-137-023–029; MP-SA09-06–11).

### 2.4 Relative exactness and the multiplication square

The second packet uses bounded nonnegative finite-free complexes and degreewise exact sequences. Those sequences are degreewise split, but an arbitrary class of purported exact sequences in another additive target does not automatically inherit all of the needed axioms. A restricted left-exact evaluation theorem can be proved from the finite kernel construction and two successive cone sequences. It must not be extended silently to arbitrary relative-exact targets.

The distinction between P and its split-homology subcategory Q is especially consequential. Free terms, cycles and boundaries do not imply free homology: D_1(2) supplies the obstruction. Moreover,

\[
0\longrightarrow S_0(\mathbf Z)\longrightarrow D_1(2)
\longrightarrow S_1(\mathbf Z)\longrightarrow0
\]

is degreewise split, has endpoints in Q and middle object outside Q. Thus Q is not automatically an extension-closed exact subcategory of P. The example blocks an unqualified appeal to an inherited Quillen exact structure; it does not rule out every possible exact structure one might define on Q. Relative Ext, resolution and derived-evaluation claims retain their corresponding obligations (CL-SA09-137-030–036; Bühler, 2009).

Multiplication introduces an independent issue. The product transported from simplicial degreewise tensor is not simply declared identical to ordinary total tensor. The unit arrow on scan 66 is an ordinary morphism, not a stipulated isomorphism, and the contractible generator category has no tensor unit. In the extension square on scan 71, a monomorphism gives uniqueness of a factorization **if it exists**. It does not prove existence. The audit isolates a sufficient kernel-preservation condition, which must still be checked for the actual product (CL-SA09-137-037–040; SA09-21–24).

The cup product is asserted with homotopies and signs. The interval calculation distinguishes it from strictly commutative rings of degreewise functions. Later coherent cochain operations provide a meaningful comparison, but the manuscript's binary data do not by themselves supply all such coherence (Berger & Fresse, 2004; CL-SA09-137-041). Likewise characteristic zero does not imply that every integer factorial is invertible; an argument requiring rational coefficients must say so.

### 2.5 Polynomial categories, constants and divided powers

The closing pages replace scalar recognition by actual polynomial structure. Over characteristic p, λ and λ^p can act identically on p-torsion while defining different polynomial laws after extension to F_p[T]. The author's added multidegrees and coefficient-algebra tests address a real defect, rather than merely changing terminology.

Here strict representability means stability of a universal property with additional parameters; it does not assert identity associators. The homogeneous composition core uses maps α_(p,q):Γ^(pq)→Γ^pΓ^q, naturality, correctly typed coassociativity and degree-one units. A displayed superscript fails that type check. Constants require an additional degree-zero axiom, which the source adds after the initial list. The homogeneous construction therefore does not settle the full mixed-degree, tensor and multigrading equivalence (CL-SA09-137-043–049; Roby, 1963; SGA 4 XVII5.5.2; Friedlander & Suslin, 1997).

Universal substitution must also be distinguished from divided-power evaluation. In rank one, their composite has coefficient

\[
\frac{(pq)!}{p!(q!)^p},
\]

already3 when p=q=2. The maps are not mutually inverse. A canonical divided-power structure belongs on an appropriate positive-degree ideal: imposing it on the unit ideal over Z would force 2γ_2(1)=1. The Hom-module enrichment question remains separate from set-level functoriality (CL-SA09-137-050–051; Richter, 2009; StacksPD).

### 2.6 What later reconstruction results establish

Sullivan's rational theory, Mandell's structured integral cochains, Toën's affinization framework and Horel's binomial approach have different hypotheses, targets and mapping behaviour. The opened statements are compared in the claim map rather than treated as interchangeable answers. No missing functor from the exact strict structure of cote 137 to one of those models has been supplied by analogy (Sullivan, 1977; Mandell, 2006; Toën, 2020; Horel, 2024).

The public *Pursuing Stacks* text contains genuine later discussions of operation theories, normalization and the difference between conservativity and full faithfulness. These are verified continuations of questions, not a retroactive proof of every 1970s claim. A November 2026 Hua preprint also treats the restricted additive theorem and a homogeneous polynomial core while excluding broader variants. It is identified as a contemporary, AI-assisted report. Its Lean code was not run here, and neither full essential surjectivity nor the complete tensor/multigrading equivalence is credited on that basis. The relevant claims remain class C.

## 3. Cote 138/1–45: descent, Kummer theory and Fermat geometry

### 3.1 Descent and finite kernels

Scans5–14 pass from fields of definition to semilinear automorphism groups and partial splittings. An automorphism of the constant field need not preserve the isomorphism class of the scheme. The author's change from surjectivity to equality of arithmetic images is therefore substantive. For a Galois pro-cover corresponding to N, the compatible automorphism group is a normalizer quotient; lifting all base automorphisms requires invariance of N. Topological finite generation supplies cofinal characteristic open subgroups.

Finite presentation and effective descent are separate inputs. The finite-extension assertions match EGA IV.3, Théorème8.8.2 and its corollaries. Quasi-projective effectivity is supplied by SGA 1 VIII, Corollaire7.7, rather than assumed for every abstract section. Both original sources were opened at the relevant hypotheses and proof passages (Grothendieck & Dieudonné, 1966; Grothendieck et al., 1971).

For a profinite extension 1→H→E→Γ→1 with finite H, choosing an open normal U disjoint from H proves that the extension is pulled back from a finite quotient after shrinking Γ. That existence statement is sound. The claimed converse for a **specified** partial section is not: centralizing H makes its image normal in the inverse image of its domain, but normality in all E additionally requires equivariance under ambient conjugation.

The audit provides a geometric example as well as the earlier finite-group witness. Remove the nine rational points

\[
\{-1,-1/2,-1/4,1/2,2/3,4/5,2,3,5\}
\]

from P¹_Qbar and use the identity covering. Exact enumeration of all504 Möbius candidates gives geometric automorphism group C3, generated by 1/(1−z), with all automorphisms defined over Q. Hence E=C3×G_Q. Over G_(Q(√−3)), take the graph of the C3 character from the splitting field of X³−2. It centralizes the geometric kernel, but complex conjugation inverts that character, so the graph is not normal in E. The example satisfies finite presentation over Qbar and descends to Q. The source's separate literal “over k” at scan 10 remains a k/bar-k reading alarm; the example is not claimed to satisfy an inconsistent finite-type-over-Q condition with infinite algebraic constants (CL-SA09-138E-009–010).

The subsequent centralizer extension and its H² obstruction/H¹ torsor description are valid at their proper scope. They classify centralizing sections, not the missing global conjugation compatibility.

### 3.2 Cocycles, completions and the exact radical image

The punctured-line discussion separates three notions that the earlier notes sometimes compressed: a root torsor, its full affine automorphism group after an origin is chosen, and the arithmetic subgroup actually realized by Galois. Even Aut(G_m) needs inversion unless the two punctures are ordered.

Kummer coefficients carry the cyclotomic action. At finite level the exact sequence is

\[
0\to\mu_n/\mu_n(\mathbf Q)\to Z^1(G_\mathbf Q,\mu_n)
\to H^1(G_\mathbf Q,\mu_n)\to0,
\qquad H^1\simeq\mathbf Q^*/\mathbf Q^{*n}.
\]

For n=2 the coboundary group is zero. At the full Tate limit, Z¹(G_Q,Zhat(1)) is torsion-free pointwise while the Kummer completion has the nonzero order-two class [−1]. Consequently its extension by the Tate module does not split even as an abstract sequence of abelian groups. This is a proof about the actual extension, not a denial of an accidental abstract isomorphism between unrelated infinite groups (CL-SA09-138E-021; Milne, 2020).

The valuation completion is also a restricted product: a tuple (a_p) in the product of Zhat's must be zero modulo each n at all but finitely many primes. The all-ones tuple fails; the factorial tuple has infinite support and satisfies the restriction. Neither the direct sum nor the unrestricted product is correct.

For radicals of2 the exact arithmetic image has index two:

\[
\{(a,b)\in\widehat{\mathbf Z}^{\times}\ltimes\widehat{\mathbf Z}:
(-1)^b=(2/a)\}.
\]

The character on the right has conductor 8. At level 8 there are sixteen allowed affine pairs out of thirty-two; the field degree calculation and multiplication law were checked exactly. The full-tower sufficiency comes from the opened radical-intersection theorem, not extrapolation from that finite example. Lenstra, Moree and Stevenhagen first circulated their treatment in December 2011 and published it in 2014; their backward reference led to Schinzel's 1977 Theorem 2, which was read in the published scan. For a rank-r rational multiplicative group Γ, put Γ_∞={x : x^n∈Γ for some n≥1} and Γ_0=Γ_∞∩Q^×. The exact quadratic-entanglement index 2^r applies in the intrinsic ambient group A=Aut_{Γ_0}(Γ_∞). It does not automatically apply in coordinates chosen from unsaturated generators. Over a general number field, a verified uniform Kummer degree bound establishes finite index, while the same exact numerical index is not asserted (Moree & Stevenhagen, 2014; Perucca & Sgobba, 2019; CL-SA09-138E-020,037).

### 3.3 The geometric tower and its marked fibres

The primary object from scan 25 is

\[
C_n:x^n+y^n+z^n=0\longrightarrow C_1,
\qquad[x:y:z]\longmapsto[x^n:y^n:z^n].
\]

Its degree is n², its geometric deck group is μ_n³/μ_n, and its genus is (n−1)(n−2)/2. The triangulation has 3n vertices, 3n² edges and 2n² faces. Coordinate powers supply the tower; over the three-punctured line its limit is the maximal geometric abelian cover with module T³/T. The symbolic Euler and genus checks are saved.

The finite automorphism formulas belong to the marked covering pair, not the unrestricted proper curve. The deck group has rank two, and homogeneous fibre descriptions require projective scaling. The mod-two and mod-three quotient actions genuinely use multiplication by 2 and 3 respectively; those factors are conventions to retain, not defects to correct away. The centre module gives sign·χ_3 after the action on its invariant line is identified. Characteristic-p versions require p∤n, and the special centre/midpoint formulas impose additional exclusions at 2 and 3.

The eighteen-transport programme is unfinished. Its reduction to two representatives still needs stabilizer and composition compatibility. A midpoint formula mixes a half-turn root system with the previously defined cubic-root system and fails direct substitution. The proposed corrected origins are explicitly reconstructions. At n=2, by contrast, the octahedral identification is fully checked, including V4 versus the colour-permuting S4 action. The clipped universal-cover sentence remains unidentified (MP-SA09-44–48).

## 4. Cote 138/46–89: explicit maps, groupoids and peripheral groups

### 4.1 The conic and the dihedral map

The dihedral map f_n(x)=1/2−(x^n+x^(−n))/4 has degree 2n. Its deck transformations are rotations and inversion; for n≥2 its branch indices are(2,2,n). The n=1 boundary has two branch values. The tame Riemann–Hurwitz argument yields precisely the spherical signatures (2,2,n),(2,3,3),(2,3,4),(2,3,5), with strict positivity excluding four branch points. A cancelled wild draft must be read separately: finite p-subgroups of PGL2 are elementary abelian translation groups, but a finite group quotient of function fields is separable even in characteristic p (Faber, 2011/2023; CL-SA09-138M-001,014–018).

For the nonsplit conic C:x²+y²+z²=0, adjoining i gives u=(y−ix)/z with conjugation u↦−u⁻¹. Thus the specific map u↦u^m descends exactly when m is odd. Writing (y−ix)^m=B_m−iA_m gives the global coordinate morphism (A_m:B_m:z^m). The general descent and basepoint argument accompanies the exact polynomial computations. The cubic is the source's displayed example; the expansion requires coefficient3, not9. The parametrization (1−t²,2t,1+t²) instead lies on x²+y²−z²=0. No sign or conic model has been silently changed.

The quadratic Kummer base change in the cancelled dihedral reduction has **two** rational normalization components in the displayed model. This answers that explicit genus test, while leaving the source's incomplete general reduction distinguishable from it.

### 4.2 Groupoid coordinates and surfaces

Choosing one root object per component and transport arrows identifies a functor from a groupoid with its root homomorphisms and invertible rays. The reconstruction formula proves the statement directly. For a target that is merely a category, full faithfulness still needs the condition on all target arrows between image objects. The shortened equivalence criterion later drops this condition: the one-object monoid {0,1}, with unit group {1}, is a finite counterexample. Likewise not every object permutation of a disconnected groupoid lifts; unequal isotropy groups obstruct it. The correct connected statements agree with the opened GAP Groupoids manual and the general fully-faithful/essentially-surjective criterion (Moore & Wensley, 2026; Stacks02C3).

The surface discussion separates an orientation line from the full exterior square of homology. For genus g≥2, the latter has rank g(2g−1), so it cannot be isomorphic to a rank-one orientation module. The corrected object is the orientation-valued alternating pairing. Finite marking removes the identity-component exceptions for the torus and open annulus, under the explicitly stated topology and finite-marking hypotheses; it does not trivialize the marked mapping-class group or an arbitrary operator centralizer. Quintas (1965, Theorem (c), (h), and equation (2.2)) supplies an exact pre-manuscript homotopy-group result; Yagasaki (2000, Theorem 1.1 and Lemma 2.1(i)) supplies the stronger contractibility statements in the specified setting. These and the source's broader deferred groupoid comparison are distinguished in CL-SA09-138M-019–022.

The S3 quotient provides an instructive cross-packet merge. The seven marked finite points on scan 78 match the finite part of the eight-point special-fibre set of the rational function written on scan 19; infinity is implicit in the later projective-line diagram. It is therefore a directly supported same-cote comparison, stronger than the earlier middle-packet guess. Assigning that equation to the later unlabelled arrow nevertheless remains an interpretation. Item SA09-129 retains both levels.

### 4.3 Arithmetic action without an image theorem

For a punctured rational curve, the arithmetic étale extension supplies a canonical **outer** action. At rational punctures, full tame inertia is Zhat(1), with the common cyclotomic character; for P¹ the full inertia inclusion requires at least two punctures. Actual generators require basepoints and paths. Scans93–95 later repeat this construction and explicitly state independence of the puncture index. These occurrences are merged in CL-SA09-138M-027, with the doubtful i/ν glyph retained as an alarm.

The cyclic group μ_n and its unit automorphism group are different targets. The action by exponent 2 on μ_5 already distinguishes the cyclotomic permutation from a translation. The earlier rank-one inner-embedding assertion is also false: Inn(Zhat)=1. Rank at least two, stated on 89 and inherited by 90, repairs that issue. The late note's isolated warning at 90 is corrected accordingly.

The proposed reversal is sensitive to its lower summation index. One reading preserves the product-one relation; the other leaves a nontrivial commutator for ν≥2. For the working reading, the chosen lift squares to an inner automorphism and has outer order exactly two when ν≥2. At ν=1 the displayed reversal is the identity. This does not prove that every profinite involution is conjugate to that one.

The rational S3 action commutes with arithmetic transport in outer automorphisms. Guillot's precise centralizer description of GT0 is a suitable modern comparison. Full GT adds a pentagon relation; an arbitrary peripheral automorphism group, GT0, GT and the arithmetic image must remain separate. Current2026 reconstruction statements also have extra conditions: Collas's BGT framework explicitly uses cofilteredness and uniqueness conditions, and the opened dihedral-quotient work proves specified quotients rather than full Ihara surjectivity (Guillot, 2014/2015, §5.6; Collas, 2026, §4.2; Bortnovskyi et al., 2024/2026).

## 5. Cote 138/90–133: completed geometry, moduli, examples and operations

### 5.1 The normality questions have different answers

For this paragraph, Γ_ν denotes the profinite outer group preserving the **named** peripheral classes with a common multiplier. Its multiplier-one kernel is Γ_ν°. The geometric subgroups are closures of pure discrete sphere mapping classes, with or without orientation reversal. These conventions are read from 89–90; they are not interchangeable with the full puncture-permuting groups.

Genus-zero congruence results justify identifying the appropriate profinite completion with its geometric closure. They do not prove that this closure is normal in every larger peripheral group (McReynolds, 2012, Theorem 1.1, with the earlier references recorded in the ledger).

The full extended geometric closure is **not normal for any ν≥2** under these conventions. The proof in this run uses the explicit three-dessin S3 Galois orbit described below. In rank two the pure oriented geometric group is trivial and the extended image is C2 generated by reflection. A Galois three-cycle conjugates that reflection to another transposition outside C2. For higher rank, choose rational real punctures and forget all but three. Named-peripheral automorphisms preserve the normal subgroup generated by the forgotten loops, so the comparison descends. The geometric images are still 1 and C2, and the same obstruction applies.

Similarly, the pure oriented geometric closure is strictly smaller than Γ_ν° for every ν≥2. An arithmetic commutator has cyclotomic multiplier one and a nontrivial three-cycle image, whereas the oriented geometric subgroup maps trivially in rank two. This is a present-run all-rank deduction with its own proof events, not a separately located published theorem or a sentence attributed to the manuscript (CL-SA09-138L-004,006; MP-SA09-70,72).

The remaining question is different: normality of the oriented closure **inside Γ_ν°**. Rank two is trivially normal. For ν≥3 the exact unrestricted question was not resolved by the located sources. The two counterarguments above do not answer it. The problem index records that bounded state-of-the-art conclusion rather than converting a failed search into a universal claim that no answer exists.

### 5.2 Cell pinning is not sufficient rigidity

The proposed precarte morphism law using fibre cardinalities fails composition. Replacing it by local ramification degrees repairs the multiplicative rule, but faithfulness of the facet functor is a separate question. The genus-one map with rotations r=(1234) and edge involution σ=(13)(24) has a nontrivial automorphism fixing every vertex, edge and face. Pinning cells therefore leaves a kernel. The number of pinned classes is corrected by that kernel, and a relabeling stabilizer is the effective image of Aut(C), not automatically the entire automorphism group.

There is an arithmetic obstruction to the raw fine-moduli assertion as well. For

\[
E_d:d y^2=x^3-x,\qquad f=x^2,\qquad d=1,2,
\]

all cells can be labelled rationally. The labelled pairs become isomorphic over Q(√2) but are not isomorphic over Q. Their presheaf of isomorphism classes is not a sheaf and cannot be represented as claimed. This does **not** refute the finite étale scheme attached to the finite Galois set of geometric classes. At fixed degree δ, primes p>δ do not divide any monodromy group order, and tame specialization supplies the corresponding finite étale class scheme over Z[1/δ!]. Raw objects with descent data, their geometric classes and coarse arithmetic class schemes are kept separate (CL-SA09-138L-015–026; SGA 1; Stacks03QR; Stacks03SF).

### 5.3 The sextic computation and the finite catalogue

The small rational functions, passports and pinning counts were recomputed. The substantial example is

\[
H(z)=z^3(z-1)^2(z-c),\qquad
g(z)=z^2-\frac{5c+4}{6}z+\frac c2,
\qquad H'=6z^2(z-1)g.
\]

Requiring the two remaining critical points to map to1 gives a cubic factor

\[
R(c)=25c^3-12c^2-24c-16.
\]

The other quadratic factor is excluded by its double-critical-point degeneration. Exact remainders, resultants and discriminants verify the desired passport (3,2,1)|(2,2,1,1)|(6), the nonvanishing conditions and the correct localized parameter algebra. Quotienting by a product PQ would retain unwanted points. The cubic is irreducible with discriminant −3·1296²; the certified change of variable c=(4+18t+6t²)/25, where t³=2, identifies Q(c) with Q(∛2). Its three normalized covers form one S3 orbit, one real/reflexible member and a conjugate chiral pair.

Backward reference checking located this exact family in the 1992 tree catalogue and Bétréma–Zvonkin's1993 treatment, before the later2004 and 2013 accounts. The source computes the local parameter problem; the complete S3 orbit identification is the earlier/current reconstruction completing that programme (CL-SA09-138L-037–046; Bétréma & Zvonkin, 1993, §4.3; Jones, 2013, Example 7.7).

An exhaustive permutation enumeration also checks the low-degree catalogue. In degrees 1 through 6 the oriented spherical counts, allowing folded edges, are 1,3,3,9,14,47; identifying mirror images gives 1,3,3,9,13,42. These are this run's counts, not transcribed numbers. The group type matters beyond its order: the indicated degree-four digon has full symmetry C2³, whereas conventional D4 has elements of order four. The nested planar three-loop bouquet likewise has full group V4 under the diagram interpretation, not C2. Both are conditional scan alarms: the drawn embedding and the handwritten group convention still have to be checked on the images.

### 5.4 Operations and conformal rigidity

The operation programme asks for compatible pullbacks of subsets and reference graphs. For a finite cellular graph A on the sphere, the precise reconstructed universal cellularity test is that each open face contain at most one of {0,1,∞}. Two branch points in one face already admit a cyclic cover whose preimage face is not a disk. Joint finiteness of A∪[0,1] is another requirement: two separately embedded finite graphs can intersect infinitely often if no compatible tameness condition is imposed. An unclear negation or A_X/S¹ symbol is not decided by this argument.

The operation q(t)=(2t−1)² preserves Belyi branching but does not universally make a cover strict-clean: an old index three over 0 can remain index three over the new white value1. The exact local-index conditions for a strict-clean-preserving postcomposition are recorded separately from the source's folded-edge convention. They match the need to state the branch and ramification hypotheses in Belyi-extending constructions (Ellenberg, 2000/2002; Wood, 2003/2006).

The claimed uniqueness of a compatible holomorphic function on a fixed embedded unparametrized map is too strong. For every n≥1,

\[
F_n(z)=\frac{4z^n}{(1+z^n)^2}
\]

and F_n(az), a>0 and a≠1, have the same orange graph and black vertices while their functions differ. Their white midpoints move. Thus a theorem fixing all coloured dessin vertices does not contradict this example. Positive dilations survive for every n, not only a short list of the smallest oranges.

A face with at least three distinct boundary prime ends fixed by a map-isotopic holomorphic automorphism does force identity. That is a useful sufficient criterion, not the asserted complete classification of all exceptions. Marking suitable centres or midpoints can remove the continuous freedom in the displayed spherical examples. The proposed space of invariant rigidifications, however, is not defined sufficiently to certify all its equivalences or its contractibility. Infinite-map results require still more: local finiteness, finite-sided disk faces, proper covering conventions and control of accumulation. Opened modern infinite-dessin theorems retain such hypotheses (CL-SA09-138L-063–076; Constantin & Kolev, 1994; Morvan, 2017; Cañas et al., 2022).

## 6. What the earlier notes got right, and where consolidation changes them

The earlier notes were strongest when they retained a cancelled qualifier, noticed a type mismatch, separated an explicit example from a universal theorem, or distinguished outer from actual actions. Many of their algebraic alarms survive exact recomputation. They were also right to avoid identifying the arithmetic-image problem with mere faithfulness.

The main corrections concern scope. Degree growth does not by itself prove derived perfectness; additive evaluation does not furnish all multiplicative coherence; a normal partial section is stronger than a centralizing one; cell pinning does not remove all automorphisms; and a fixed finite class set cannot carry a faithful action of the whole absolute Galois group. A corrected finite or marked statement is retained alongside the failed broad statement.

Cross-packet reading improves three specific judgements. The equation guessed for the diagram on 78 is actually written on 19. The common cyclotomic character is revisited explicitly on 94–95. And the rank condition immediately before 90 removes an apparent new defect in the late packet, although the earlier rank-one assertion on 81 remains defective. The merged whole-cote scope item SA09-110 also prevents repeated absence findings from being mistaken for multiple independent claims.

The apparatus never treats mathematical necessity as a reading decision. Every alarm keeps the transcribed reading, the suggested alternative, its mathematical evidence and its weight. Particularly consequential targets are the projectivity/acyclicity qualifier in 137/4; the P/Q and homology symbols in 137/60–63; the conic signs and cubic digits in 138/49–51; the reversal lower index; the S3 quotient factors; the sextic discriminant and localization; and the catalogue's group labels and embeddings.

## 7. Links and the separate project record

Verified links to published Grothendieck work include finite-presentation descent in EGA IV.3, effective and arithmetic descent in SGA 1, the later cartographic dictionary and arithmetic faithfulness assertion in the *Esquisse*, and the distinctions among operation theories in *Pursuing Stacks*. Each main link record names both read endpoints. Related material in cotes136,145 or147 is not invented from a title: only actually retrieved endpoints receive verified links.

The named project leads remain a separate category. During this run, targeted retrieval located selected GALOIS, RESIDUE, TOTASPH, TOTEX2, CATHOT, LM4, LM7_PUSH and LM6 materials, and cote 145. These now support verified **textual correspondences**. They do not certify the projects' proofs. One meaningful chronology is explicit: older TOTASPH/RESIDUE returns leave a total-to-exact implication open, while TOTEX2 checkpoint03 later claims a strict separation. That change is recorded as the sequence of reported statuses; the full later construction was not refereed here.

Similarly, the actual LM7_PUSH and referee passages distinguish a gentle GT0 result from the still-uncomputed restriction to full GT and retain their listed unchecked dependencies. LM6 A.22 keeps its residual full-group normalizer problem. LM4 C.12, D.12 and F.7, and successor B.38/B.39, remain different questions from the elementary calculations of cote 138. The successor text expressly does not claim to refute the published nonsolvable centralizer assertions. SA09 does not import those external claims as mathematical inputs.

Unlocated EXIT_TOWER, internal LM140/Hua versions and other named reports remain in `SA09_project_leads.tsv`, with the originating note IDs and run names. A search returning no match is not evidence that the files do not exist. The public Longue Marche transcription is used at its actually read sections; its unfilled sections are not treated as proof sources. The requested Stage5 distinction is therefore explicit: the main links table contains checked correspondences, while the separate lead table preserves the original project leads with their updated verification status, including leads whose selected endpoints were subsequently read. `SA09_project_links.tsv` separately collects the checked project correspondences; no project report is silently promoted into an established result.

## 8. Present state, directions and audit counts

The stable foundation is substantial: elementary dévissage with its correct finiteness hypotheses, finite-presentation descent, precise Kummer statements, the explicit Fermat and conic maps, groupoid coordinates, tame spherical signatures, arithmetic outer actions, the sextic orbit and the finite geometric class-set constructions. The principal unfinished authorial programmes concern the additional structures and comparisons: multiplicative extension, full polynomial/tensor-PD coherence, the exact peripheral tower, genuine rigidification, and functorial operations with all marking conventions present.

The problem index contains authorial questions, hopes and checking flags, including ones answered or withdrawn by the subsequent text or by established theory. Its size is not a count of currently open mathematical problems. The ranked directions choose concrete next tasks from that index. They state what a few hours could establish and what would remain; none has been developed beyond the proof and computation checks needed for this consolidation.

<!-- BEGIN COUNT TABLES -->
| Measure | Count |
|---|---|
| Indexed source entries | 380 |
| Canonical items | 252 |
| Canonical claim records | 216 |
| Problems | 73 |
| Readings awaiting images | 173 |
| Ranked global directions | 12 |
| Checked correspondence rows | 107 |
| Original project-lead inventory rows | 105 |
| Bibliographic records | 95 |
| Check events | 867 |

The 216 canonical claim records include one explicitly identified Sullivan-insert provenance record (CL-SA09-137-052). Thus 215 records concern Grothendieck's manuscript assertions, computations or identifiable programmes; the provenance record is not credited as his original theorem. The fifth, unindexed packet contributes claims and problems but no invented verdict rows. Six item identifiers and one duplicate claim identifier are retired through explicit aliases, leaving all original component records recoverable.

#### Entry verdicts

| Verdict | Count |
|---|---|
| kept | 247 |
| merged | 126 |
| corrected | 3 |
| withdrawn | 4 |
| rests on a misreading | 0 |

A zero in the last row does not mean that no mathematical reading alarm was found: without the scans, suspected readings remain conditional. Their evidence is retained in the 173-row reading register. Corrected and withdrawn verdicts retain their original reasons and source locations.

#### Item kinds

| Kind | Count |
|---|---|
| conjecture | 4 |
| unproved claim | 47 |
| unpursued implication | 40 |
| idea of the earlier run | 43 |
| reading question | 46 |
| self-flagged step | 26 |
| withdrawn in the same text | 22 |
| title, date or page count | 17 |
| other | 7 |

#### Claims by literature class

| Class | Meaning | Count |
|---|---|---|
| A | In his own later published work | 2 |
| B | Developed by others into established results | 13 |
| C | Partly developed; exact limitation recorded | 81 |
| D | No development located after the stated search | 0 |
| E | Known before the manuscript context | 106 |
| F | Not identifiable at the required precision | 14 |

Classes concern development and provenance, not truth. In particular, class A may record a later published continuation of a programme without claiming that every hoped-for theorem was proved; class C may contain a refuted broad statement with a valid restricted result. First circulation and publication dates remain distinct in the individual records.

#### Claims by status on the pages

| Reporting group | Count |
|---|---|
| proved there | 10 |
| proof sketched | 48 |
| stated without proof | 67 |
| corrected by himself later | 14 |
| false as stated | 40 |
| open on the pages | 36 |
| not identifiable | 1 |

`claim_status_groups.tsv` gives the explicit, individually reviewed grouping used only for these counts. The complete `status_on_pages` string remains unchanged in every claim. Thus conditional failures under a literal reading remain conditional; a construction stated to work is grouped with statements without proof; and the single isolated fragment that cannot be formulated is listed separately. The 40 records grouped as false as stated include qualified or reading-dependent failures and are not 40 unconditional judgments about the autograph.

<!-- END COUNT TABLES -->

### Audit and reproduction

`SA09_claim_search_coverage.tsv` maps every canonical claim to its search records. `CHECK_EVENTS.tsv` distinguishes source consistency, targeted proof checks, independent arguments, exact computations, background use and refutations. No finite sample is called a proof of an all-rank assertion, and no reported Lean formalization is called a formal certificate of this run.

The exact programs use ordinary integer/rational arithmetic, symbolic polynomial calculations, reduced free-group words and finite permutation enumeration. Their outputs and the unsuccessful initial attempts that materially affected a computation are retained. The component proof audits supply the general arguments that finite runs cannot establish. `VALIDATION.json` records schema, coverage, cross-reference, search and event checks; it is a structural audit, not a replacement for semantic review.

The final source-hash comparison confirms that the attached transcriptions remain unchanged. The checkpoint and final archives exclude the attached source files themselves, retrieved full reference PDFs and external project archives. Their identities and exact read locators remain documented. The final ZIP is a consolidated dossier and evidence package, not an edited edition of the manuscripts.

### Selected references in author–date form

The complete bibliography, including precise verification scopes and all additional works, is `SA09_references.bib`.

- Belyi, G. V. (1980). On Galois extensions of a maximal cyclotomic field. *Mathematics of the USSR-Izvestiya, 14*(2), 247–256. https://doi.org/10.1070/IM1980v014n02ABEH001096 . Russian original 1979; received 2 August 1978.
- Berger, C., & Fresse, B. (2004). Combinatorial operad actions on cochains. See `BergerFresse2004` for the opened article and exact scope.
- Bétréma, J., & Zvonkin, A. (1993). La vraie forme d'un arbre. See `BetremaZvonkin1993`, especially §4.3.
- Bühler, T. (2009). *Exact categories* (Version 2) [Preprint]. arXiv. https://arxiv.org/abs/0811.1480 . First posted 10 November 2008; opened version dated 22 April 2009. See `Buhler2009` for verification scope.
- Collas, B. (2026). *Anabelian perspectives in Galois–Teichmüller theory*. https://arxiv.org/abs/2603.02848 . First circulated 3 March; checked revision 5 November 2026.
- Dold, A., & Puppe, D. (1961). Homologie nicht-additiver Funktoren. Anwendungen. See `DoldPuppe1961` for the opened original.
- Faber, X. (2023). Finite p-irregular subgroups of PGL(2,k). *La Matematica, 2*, 479–522. https://doi.org/10.1007/s44007-023-00051-4 . First preprint 2011; checked revision 2024.
- Farb, B., & Margalit, D. (2012). *A primer on mapping class groups*. Princeton University Press. The opened version and page concordance are specified in the bibliography.
- Grothendieck, A., & Dieudonné, J. (1966). Éléments de géométrie algébrique IV, troisième partie. *Publications Mathématiques de l'IHÉS, 28*. See `EGAIV3`, §8.8.
- Grothendieck, A., et al. (1971). *Revêtements étales et groupe fondamental (SGA 1)*. Lecture Notes in Mathematics 224. Springer. https://arxiv.org/pdf/math/0206203 . The electronic re-edition has separate pagination.
- Grothendieck, A. (1997). Esquisse d'un programme. In *Geometric Galois Actions 1* (pp. 5–48). Cambridge University Press. Written January 1984.
- Guillot, P. (2014). An elementary approach to dessins d'enfants and the Grothendieck–Teichmüller group. *L'Enseignement Mathématique, 60*(3/4), 293–375. https://doi.org/10.4171/LEM/60-3/4-5 . Volume date 2014; released 27 April 2015; preprint 2013.
- Lenstra, H. W., Moree, P., & Stevenhagen, P. (2014). Character sums for primitive root densities. See `LMS2014`, Lemma 2.5 and Theorem 2.9; first preprint 2011.
- Mandell, M. A. (2006). Cochains and homotopy type. See `Mandell2006` for the opened statement, hypotheses and limits of its application here.
- Moree, P., & Stevenhagen, P. (2014). Computing higher rank primitive root densities. See `MoreeStevenhagen2014`, Theorem 2.5; first preprint 2012.
- Perucca, A., & Sgobba, P. (2019). Kummer theory for number fields and the reductions of algebraic numbers. See `PeruccaSgobba2019`, Theorem 1.1; statement inspected, full proof not independently checked.
- Quintas, L. V. (1965). The homotopy groups of the space of homeomorphisms of a multiply punctured surface. *Illinois Journal of Mathematics, 9*(4), 721–725. The full primary scan and exact locators are recorded under `M-Quintas1965`.
- Roby, N. (1963). Lois polynomes et lois formelles en théorie des modules. See `Roby1963` and the independently opened SGA 4 XVII comparison.
- Sullivan, D. (1977). Infinitesimal computations in topology. The earlier inserted typescript is recorded separately; these are not treated as the same paginated source.
- Wood, M. M. (2006). Belyi-extending maps and the Galois action on dessins d'enfants. See `Wood2006`; first preprint 2003.
- Yagasaki, T. (2000). *Homotopy types of homeomorphism groups of noncompact 2-manifolds* [Preprint]. https://arxiv.org/abs/math/0010223 . First posted 24 October 2000; exact theorem scopes are recorded under `M-Yagasaki2000`.

All formulas, source distinctions and claims in this overview are further qualified at their full scope in the linked item and claim ledgers. The bibliography's `verified` flag means that the stated link or source was opened; its annotation and check events specify whether the verification was bibliographic, theorem-level or a proof check.
