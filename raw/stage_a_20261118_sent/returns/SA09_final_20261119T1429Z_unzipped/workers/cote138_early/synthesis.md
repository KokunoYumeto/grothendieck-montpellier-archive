# Cote 138, scans 1–45: descent, Kummer torsors and the Fermat tower

## Scope and evidence

This worker read all 102 indexed entries of `MPL_138_001-045_notes.md`, the complete accompanying doubts table, and the entire 1,801-line `MPL_138_001-045_transcription.tex`. The 102 entries have individual semantic verdicts and are consolidated into 70 items. The mathematical claim ledger contains 48 claims; the problem index contains ten questions or unfinished steps; the scan-review table contains 40 alarms. These counts precede the root dossier's cross-package merges. Claim IDs are `CL-SA09-138E-001` through `048`; problems are `MP-SA09-40` through `49`.

All manuscript locators below refer to the supplied Pro transcription, using its original one-based lines and scan markers. No archival image was opened, and no uncertain glyph has been decided or changed. The mathematical statements labelled reconstructions are either the earlier run's explicitly attributed ideas or the present run's independently checked formulations. A primary published statement is distinguished from a bibliographic record whose full article could not be read.

The packet contains 44 scan markers at positions 1–45; scan 24 is absent. It does not supply an authorial mathematical date or an authorial total page count. The administrative material includes a 1980 order form and leaves dated 15 and 22 June 1978, but those dates do not date every mathematical leaf. The Montpellier catalogue's approximate 1976–1978 description is external metadata, not an autograph terminus for each argument (Université de Montpellier, n.d., cote 138). These distinctions matter when comparing a question to Schinzel's 1977 article, Belyi's 1978 submission, and the 1984 *Esquisse*. See items SA09-106–108, 178, 180 and 183.

## The manuscript's progression

### 1. Descent of objects and covering pairs

Scans 5–14 develop a dictionary between fields of definition, semilinear automorphisms and partial splittings. The setting is a connected geometric scheme over a separable closure, with a hypothesis identifying that closure inside its ring of global constants. A field automorphism need not preserve the isomorphism class of the scheme, so the arithmetic image of its semilinear automorphism group can be proper. The author's replacement of “surjective” by “same image” at scan 8, line 296, is substantive: surjectivity of a morphism of extensions follows from surjectivity on geometric kernels and equality of their arithmetic images, not necessarily from surjectivity onto the entire absolute Galois group.

The universal profinite covering object introduces an extension by the geometric fundamental group. For an intermediate Galois pro-cover corresponding to a normal subgroup N, the compatible automorphisms are the normalizer quotient N_E(N)/N. Lifting every base automorphism requires N to be invariant under the whole extension. Characteristic open subgroups supply a cofinal system when the fundamental group is topologically finitely generated. The proof is short: there are finitely many homomorphisms from a d-generated profinite group to each finite symmetric group, hence finitely many open subgroups of bounded index; intersecting their conjugate or characteristic families produces open characteristic subgroups. Haran, Jarden and Pop's author manuscript states this exact construction and gives a backward reference (2009, §1, p.6). We do not assign its first historical occurrence from that later exposition.

Effectivity is not silently discarded. Continuous semilinear actions are descent data; to turn data into models requires an effectiveness result. SGA 1 VIII Corollaire 7.7 supplies the quasi-projective criterion, and Proposition 7.8 treats an ample invertible sheaf. The finite-presentation assertions match EGA IV.3 Théorème 8.8.2 and its corollaries: finitely many equations, gluing maps and relations descend through a filtered system of finite extensions, and equalities of finite-presentation morphisms hold at a sufficiently late stage. The original theorem and proof were read, including the standing hypotheses. The uncertain base symbol at scan 8, line 300, and the literal k at scan 10, line 355, remain scan alarms because the usable finite-presentation hypothesis is over the geometric constant field (Grothendieck & Dieudonné, 1966, §8.8; Grothendieck et al., 1971, VIII, IX).

The finite-kernel argument has one genuine overstatement. Let

\[
1\longrightarrow H\longrightarrow E\overset p\longrightarrow\Gamma\longrightarrow1
\]

be an extension of profinite groups, with H finite. Choose an open normal subgroup U of E disjoint from H. Then p(U)=Γ_i is open normal, U maps isomorphically to Γ_i, and

\[
E\simeq(E/U)\times_{\Gamma/\Gamma_i}\Gamma.
\]

Injectivity of the natural map follows from U∩H=1. For surjectivity, choose a representative of the first coordinate; its discrepancy from the requested second coordinate lies in p(U), and an element of U corrects it. This proves the manuscript's existence-after-shrinking statement, claim 009.

The subsequent equivalence for a prescribed partial section is false. A normal section image centralizes H: its commutator with H lies both in H and in the section image, whose intersection is trivial. Conversely, centralization proves normality only inside p⁻¹(Γ_i). Normality in all E additionally requires

\[
e s(\gamma)e^{-1}=s\bigl(p(e)\gamma p(e)^{-1}\bigr).
\]

The earlier notes supplied an abstract D8 witness. This run adds a geometric witness under the coherent geometric-base hypothesis of finite presentation over the separable closure and descent to a finite extension of the ground field. The literal “over k” at scan10, line355, is a separate reading alarm: an object with constants containing the infinite extension Qbar cannot be finitely presented over Q. That literal clause is not claimed satisfied or silently corrected. Put

\[
S=\{-1,-\tfrac12,-\tfrac14,\tfrac12,\tfrac23,\tfrac45,2,3,5\},\qquad
X=\mathbf P^1_{\overline{\mathbf Q}}\setminus S,
\]

and take the identity covering X′=X. The set S is the union of the three orbits of 2, 3 and 5 under r(z)=1/(1-z). Every automorphism of X extends to the smooth projective completion and permutes S. The images of a fixed ordered triple determine a Möbius map, so there are exactly 9·8·7=504 candidates to inspect. Because both triples are rational, all candidates have rational coefficients. Exact rational enumeration retains precisely 1,r,r². Thus the full geometric automorphism group is C3, every automorphism is defined over Q, and E=C3×G_Q.

Let Γ_i=G_{Q(√−3)} and let c:Γ_i→C3 be the quotient supplied by the splitting field Q(√−3,∛2) of X³−2. Its graph is a section centralizing H=C3. Complex conjugation in G_Q acts by inversion on the C3 quotient. Conjugation in the direct product leaves the first graph coordinate c(g) unchanged, whereas the section at the conjugated argument has first coordinate c(g)⁻¹. Choose c(g)≠1; the graph is not normal. Here X is connected affine, finitely presented over Qbar and descended to Q; the geometric pair-automorphism kernel is finite; the arithmetic group is infinite; and the covering is finite of degree one, with trivial covering deck group. This checks the coherent geometric interpretation in addition to the unconditional abstract group refutation. It does not settle the k/ks glyph. C02–C03 record the exact finite calculations; claim 010 is the refuted group assertion and claim 009 its valid existence refinement.

The centralizer continuation is sound after this distinction. For Z=C_E(H), the kernel of Z→Γ is Z(H), and its image is open because the conjugation action on the finite group H has finite image. If Z(H)=1, centralizing sections over subgroups of that image are unique. For a nontrivial centre z, the obstruction to a continuous centralizing section is its class in H²_cont(Γ_i,z); when a section exists, the set of sections is a torsor under H¹_cont(Γ_i,z)=Hom_cont(Γ_i,z). Factor sets and changes of lifts give the standard proof. This is not an obstruction theory for the additional whole-E conjugation condition (Milne, 2020, II, Example 1.18 and §4).

### 2. Punctured lines, roots and Kummer cocycles

Scans 15–23 specialize to characteristic zero. P¹ and A¹ have no nontrivial connected finite étale covers; connected covers of G_m are power maps after coordinate choices. These follow from complex comparison and the corresponding topological fundamental groups (SGA 1 XII, Théorème 5.1 and Corollaire 5.2). The displayed unrestricted automorphism group of G_m omits inversion. It becomes correct either with ordered punctures or with the additional C2 factor. The limiting translation-lift group lim_(power maps) Qbar* must also be distinguished from its Tate-module kernel T=lim μ_n.

Three distinct labelled points normalize uniquely to 0,1,∞. With more points, the field generated by the labelled cross-ratios is the natural field of definition; unlabelled configurations introduce permutation stabilizers and descent questions. A normalized isomorphism class is not a canonical choice of an ordered coordinate system. These qualifications prevent the notes' broad formulations from absorbing genuine marking issues.

The degree-six function

\[
g(z)=\frac{27z^2(z-1)^2}{4(z^2-z+1)^3}
\]

is invariant under z↦1-z and z↦1/z, hence gives the S3 quotient. Its zero fibre consists of 0,1,∞ with index two; its fibre over one consists of −1,1/2,2 with index two; and its poles are the roots of z²-z+1, each with index three. The total ramification is 3+3+4=10=2·6−2. The required factorization is

\[
4(z^2-z+1)^3-27z^2(z-1)^2=(z+1)^2(2z-1)^2(z-2)^2.
\]

Symbolic expansion, both invariance identities and the derivative are saved in C01. An intermediate factor in the transcription does not satisfy this identity and is retained as an alarm, not silently repaired. The distinguished point set has eight elements, six real and two conjugate nonreal points (C17).

The root fibres separate cyclotomic information from radicals of two. Over a field containing μ_n, adjoining one nth root of two has degree equal to the order of [2] in K*/K*ⁿ. A chosen field Q(2^(1/n)) need not be normal; the full root fibre generates Q(μ_n,2^(1/n)). This is the exact finite Kummer statement needed here (Milne, 2020, VII, Appendix A).

The manuscript's transition from Hom to crossed homomorphisms is a visible mathematical correction. The coefficients carry their cyclotomic action:

\[
H^1(G_Q,\mu_n)\simeq Q^*/Q^{*n},\qquad
0\to\mu_n/\mu_n(Q)\to Z^1(G_Q,\mu_n)\to H^1(G_Q,\mu_n)\to0.
\]

At n=2 every coboundary is trivial. Consequently a further Z/2 kernel in the displayed extension is wrong, even though indiscriminate abstract isomorphisms between some infinite groups could conceal the issue.

At the full Tate limit the contradiction is stronger. T is torsion-free, so Z¹(G_Q,T) is torsion-free pointwise. Yet the Kummer completion contains the nonzero order-two class [−1]. Complex conjugation acts as −1 on T, so T^{G_Q}=0 and B¹≅T. Therefore

\[
0\to T\to Z^1(G_Q,T)\to\varprojlim_nQ^*/Q^{*n}\to0
\]

does not split even as an abstract sequence of abelian groups. A split quotient would embed its nonzero torsion into torsion-free Z¹. The inverse-limit H¹ identification uses continuous cochains and the finite-invariant Mittag–Leffler condition on a factorial cofinal subsystem. This argument is an independent reconstruction of the present run, not a corrected phrase attributed to the manuscript.

Nor is the valuation completion the full product Zhat^P. Its elements are tuples (a_p) with finite support modulo every n: for every positive n, a_p∈nZhat for all but finitely many p. The all-ones tuple fails this condition modulo two. The factorial tuple a_(p_i)=i! has infinite support but satisfies it, because n divides i! for i≥n. Thus neither the direct sum nor the unrestricted product is the correct lattice. C05–C06 record the finite witness and the general proofs.

### 3. The exact arithmetic-image question

The finite-index question at scan 20 and the explicit “surjective?” question at scan 36 have a precise modern answer in the rational case. With compatible roots θ_n=2^(1/n), write g(ζ_n)=ζ_n^a and g(θ_n)=ζ_n^b θ_n. The image is

\[
G=\{(a,b)\in\widehat{\mathbf Z}^{\times}\ltimes\widehat{\mathbf Z}:
(-1)^b=(2/a)\},
\]

where (2/a) is the quadratic character of conductor eight. It has index two. Lenstra, Moree and Stevenhagen prove the exact general rank-one image through a quadratic-character kernel; their Lemma 2.5 identifies the radical/cyclotomic intersection and Theorem 2.9 gives sufficiency as well as necessity (2014, §2; first preprint 20 December 2011). Their backward reference leads to Schinzel (1977, Theorem 2, pp.245–246), whose statement was read in the published original. The present report does not claim to have independently re-proved that full original theorem, or to have dated the manuscript securely enough to assign priority.

The obstruction is already visible at level eight. Since θ_8⁴=√2=ζ_8+ζ_8⁻¹, the parity of b is constrained by the quadratic action on √2. There are sixteen allowed pairs among the thirty-two elements of the ambient affine group. The polynomial X⁸−2 is Eisenstein, so Q(θ_8) has degree eight and is real. Adjoining i doubles the degree; ζ_8=(1+i)/√2 shows that Q(θ_8,ζ_8)=Q(θ_8,i). Thus all sixteen allowed pairs occur. C04 verifies their multiplication and exact cardinality. This finite calculation demonstrates nonsurjectivity; the full-tower equality relies on the opened exact theorem, not on extrapolation from one level.

For a rank-r finitely generated subgroup of Q*, Moree and Stevenhagen's Theorem 2.5 gives index 2^r in the intrinsic automorphism group of its saturated radical group, together with the perfect quadratic-character pairing (2014; first preprint 20 March 2012). The more general finite-index question for independent algebraic generators is also settled. Perucca and Sgobba's Theorem 1.1 gives a uniform bound C for the failure of maximal Kummer degree over K(ζ_n), for any number field K and finitely generated torsion-free subgroup of rank r (2019, p.1617). Its publisher-provided first-page preview was opened after the repository failed; the theorem statement and hypotheses were read, while the full proof was not opened. The mod-n affine index is at most C[K:Q]. Since the full image is closed and its finite quotient indices are uniformly bounded, it has finite index. This last deduction is independently checked here. Passing to a finite splitting field handles the manuscript's finite Galois-stable set or torus, provided independent coordinates and the character-module action are specified.

The exact value 2^r remains specific to the rational saturated formulation, not arbitrary number fields or unsaturated coordinates. The ℓ-adic Lie dimension is r+1; calling this the manuscript's “dimension” still requires that explicit interpretation, and the glyph remains uncertain. Perissinotto and Perucca's opened Theorems 1.1–1.2 give explicit torsion-and-division degree procedures for products of one-dimensional tori (2023, p.110). The source's open-image question is therefore mathematically settled in its independent-coordinate number-field scope, while an exact degree formula or historical normalization requires further specification. Perucca–Sgobba's preview dates receipt to9July2018 and publication to20May2019; its first public circulation date was not established, and none of these dates is claimed to mark the first historical proof of bounded Kummer index.

The ambient affine torsor group splits after choosing an origin. Its arithmetic subgroup need not split over the cyclotomic quotient; LMS §2 explicitly separates the two. This prevents the ambiguous “splitté” margin in scan 23 from being used as a completed theorem about the arithmetic extension.

### 4. Fermat covers, special fibres and the octahedron

From scan 25 the principal geometric object is

\[
C_n:x^n+y^n+z^n=0,\quad C_n\longrightarrow C_1,
\quad[x:y:z]\longmapsto[x^n:y^n:z^n].
\]

The degree is n², the geometric deck group is Π_n=μ_n³/μ_n, and each of the three coordinate branch fibres has n points with ramification index n. Riemann–Hurwitz gives g(C_n)=(n−1)(n−2)/2. The triangular map has V=3n, E=3n² and F=2n². The coordinate dth-power map C_(nd)→C_n supplies the inverse system. Over the three-punctured line its limit is the maximal geometric abelian cover, with module M=T³/T≅T². Coordinate permutations give S3, and G_Q acts on the coefficients through the cyclotomic character. C07 checks the genus and Euler identities symbolically, not only at sampled levels; sampled n merely make the output inspectable.

Markings matter again. The proper conic C_1 is P¹, whose full automorphism group is much larger than S3. Thus the finite affine semidirect-product formula must refer to the marked covering pair. Its deck group has rank two, not a single μ_n. Likewise a branch fibre described by homogeneous coordinate pairs requires projective scaling; quotienting an unnormalized affine set only by μ_n is visibly wrong even at n=1.

The mod-two module has three nonzero classes, corresponding to the three inertia types, with S3≅GL_2(F_2). The action on a selected mod-two coset is explicitly through multiplication by two in the source. Therefore its quotient by a named inertia line means the doubled action, equivalently quotient by 2Z_i in ordinary translation coordinates. The earlier notes correctly retain that convention; it is not a missing factor to be added by this dossier. A marginal claim of three rational points cannot literally describe C_2:x²+y²+z²=0: over Q the sum of three squares vanishes only at the forbidden zero vector. The uncertain object label remains for scan review.

For the centres, the coherent final construction uses six bijections I→μ_3. At level n there are 6n³ cone points; dividing by the free diagonal μ_(3n) gives 2n² points, the two centre fibres. The inverse-limit action is through multiplication by three. On F_3³/diag F_3, a three-cycle has a unique invariant line; its two nonzero vectors are interchanged by an odd permutation. In arithmetic coordinates the character is sign·χ_3. Exact line enumeration and the finite counts are C09–C10; the general count is six choices of ordered residues, n³ lifts and scalar orbit size 3n.

The midpoint parameters are 2,−1,1/2. A root torsor K(a) requires a≠0: at zero it is a singleton and cannot be a free μ_n-torsor for n>1. The root system exp(2πi/(3n)) is coherent in lim μ_(3n), and cofinal reindexing identifies that limit with T. It should not be silently replaced by exp(2πi/n). The chosen point (bar(ζ_n),ζ_n,1) lies over −bar(j), and complex conjugation exchanges the two centres. Naming the centre differently in another context does not refute this internally coherent convention.

The proposed eighteen transports are unfinished. The source deletes general Γ-equivariance in favour of S3 and complex conjugation. It asserts a reduction to two representatives but does not finish stabilizer compatibility or composition. Worse, the midpoint identity equates exp(±πi/n) with the previously defined cubic-root system. Substitution gives a nonzero residual 1/2. A later line also changes inverse roots to roots. C12 separates the two errors. A candidate repair uses η_n=exp(πi/n) and θ_n⁻¹, but it is explicitly this run's proposal, not read ink. The functorial three-element-set formulation leaves its last arrow label deleted, so it cannot supply the missing definition by implication.

At n=2 the triangulation is the octahedron: six vertices, twelve edges, eight triangles and graph K_(2,2,2). The affine group on F_2² has twenty-four elements and is S4. It describes orientation-preserving map automorphisms allowing permutation of vertex colours; fixing the colours leaves V4. The three inertia lines give three degree-two quotients, each branched at the remaining two branch values. The author's “sauf erreur” is resolved by C14. Under the explicit convention of a two-digon sphere with two vertices, two edges and two faces, barycentric subdivision also gives the octahedron. The clipped universal-cover continuation is still unidentifiable. Neither a polyhedron name nor a later broad cartographic theorem restores its missing words.

The extension to prime fields must be limited. Fermat covers with p∤n survive, and the prime-to-p abelian tower follows from SGA 1 XIII Corollaire 2.12. The midpoint 1/2 is undefined at p=2; the two centres merge at p=3. Wild Artin–Schreier phenomena invalidate the unrestricted characteristic-zero fundamental-group statement, and the procyclic finite-field Galois group cannot have the same open image in a rank-one affine group as G_Q. These are mathematical scope corrections, not decisions that the transcription has misread the author's words.

## What the earlier notes add, and their limits

The strongest earlier-run contributions survive checking: the D8 counterexample, restricted valuation completion, distinction between Z¹ and H¹, sign character on the mod-three line, coordinate residuals, and marking qualifications. Their computations have been redone. The present run strengthens the normality refutation geometrically and the inverse-limit direct-sum refutation by torsion. Several notes also correctly preserve the author's own withdrawals: equality of arithmetic images, cancelled Hom, reversed transition direction, discarded cone definitions, relabelled midpoints and reduced equivariance.

The notes' comparisons with Longue Marche, CM-parity, Hua, EXIT_TOWER and other named research runs do not become manuscript claims. The separate `project_leads.tsv` preserves the initial lead inventory and reported qualifications. A subsequently materialized background archive enabled 23 targeted project correspondences, now recorded in `verified_project_links.tsv` and `project_endpoint_audit.md`. These checks confirm what the target returns and referees say; they are not independent proofs of the external projects' results. In particular E.65 expressly leaves the full-GT restriction of its character uncomputed, E.58 concerns the gentle group, and LM6 A.22 retains its full residual normalizer question. Targets still absent remain leads. A further direct comparison with cote145 scans11/24 confirms its cocycle and permutation-centralizer formulations, including an explicitly unknown equality. `links.tsv` contains only links for which both manuscript and public target passages were read. Bibliographic-only Ihara comparisons are not presented as verification of the exact eighteen-arrow construction.

The packet does not state a universal theorem that every smooth projective algebraic curve admits a three-point map, nor a faithful action on every finite dessin. Belyi's opened Theorem 4 and corollary, and the *Esquisse*'s discussion, are exact external comparators, not statements to insert into these leaves (Belyi, 1980, pp.255–256; Grothendieck, 1984, §§2–3). The Fermat abelian module has scalar cyclotomic action and its linear centralizer is GL_2(Zhat); that observation does not determine the centralizer of the full outer action on a free profinite group. Similarly, filling the nine punctures of the Fermat cubic passes from a free profinite group of rank ten to the proper elliptic curve's rank-two abelian fundamental group. A bridge to a Tate-module or de Rham construction requires that filling step and an actual comparison map. Nothing in these early leaves supplies a de Rham complex merely because the archive topic bears that catalogue title.

## Present mathematical status and check discipline

The descent, characteristic-subgroup, cohomology, finite Kummer and geometric Fermat constructions are established mathematics. The rank-r rational image and the exact radical-of-two image have precise later published formulations matching stated hypotheses. False literal assertions are paired with explicit repairs or bounded counterexamples; incomplete statements remain identifiable as incomplete rather than being transformed into speculative universal problems.

Every claim has a recorded search row with actual issued query families, opened sources, an exact matched outcome and limitations. The search, opening and find operations are indexed separately, with the later general-number-field follow-up preserved in its own log. zbMATH access failures and unavailable repository PDFs are recorded honestly. A `verified` bibliography note means the linked reference was opened; its annotation separately states whether this was a complete theorem passage, a proof, or bibliographic metadata only. No inaccessible theorem is used to settle a problem.

`programs/computations.py` produces seventeen computation groups, including the exhaustive 504-candidate Möbius calculation, level-eight arithmetic image, exact polynomial identities, finite module actions and face-poset counts. Finite samples are never used as proof of an infinite-level assertion. `CHECK_EVENTS.tsv` distinguishes transcription comparison, independent proofs, computations, used-and-rechecked reference results and refutations. The program files serialize human-read decisions; no verdict was inferred by keyword matching or note-heading classification.
