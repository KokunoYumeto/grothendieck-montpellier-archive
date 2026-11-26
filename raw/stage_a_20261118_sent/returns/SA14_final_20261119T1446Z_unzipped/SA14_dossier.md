# SA14 — Picard

## A consolidated dossier of the Montpellier papers, cotes 57–60

**Assessment date: 19 November 2026.** This dossier consolidates the supplied diplomatic transcriptions and all 440 indexed research-note entries. It follows the programme on **57:66**, then treats the connectedness, formal Lefschetz, determinant and functional-equation investigations in their own order. The registers are the detailed evidence for this overview: an assertion's exact hypotheses, source passage, computation, search history and qualifications belong to its claim record, not just to the prose below.

The main result is a more discriminating map of the programme. A large part has precise published descendants in FGA, EGA and SGA, or in later work on Picard functors, local Picard groups, determinants and duality. Other pages contain stronger quantifiers than those the located theorems justify. Several formulas fail literally, and several apparent difficulties disappear when a cancellation or a later correction on the supplied pages is followed. The remaining problems are therefore not a list of 180 certified open research conjectures. They include historical questions now answered, incomplete comparisons of constructions, missing hypotheses, unresolved source formulations and bounded literature-search remainders.

### How to read the evidence

Four levels are kept distinct throughout:

1. **The diplomatic text:** what the supplied transcription says, including deletions, insertions and uncertainty macros.
2. **The earlier notes:** their interpretations and suggestions, with every indexed entry given an individually read verdict.
3. **The literature:** the actual statement located in an opened source, with its hypotheses and dates.
4. **This consolidation:** modern formulations, proofs, counterexamples and proposed next tasks, explicitly identified as reconstructions where they go beyond the words on the page.

`C-SA14-…`, `SA14-…` and `MP-SA14-…` identify claims, consolidated items and problems. Bracketed bibliographic keys resolve in `SA14_references.bib`; the claims give exact theorem locators and search receipts. Identifiers need not be consecutive: explicit cross-package mergers preserve the earlier identifiers in `research/consolidation_aliases.json` and the original part records. Those original records are an audit trail; the top-level registers are authoritative.

“Scan” means the number in `\scanpage{…}`, and a line number means a **one-based physical line of the supplied named `.tex` file**. It is not a reconstructed manuscript line. The archive contains no manuscript scan images and no second-pass replacements for this topic. Mathematical alarms have therefore been recorded without deciding the ink or changing any transcription. Inspection of published EGA or SGA page images is a different operation and is identified as such in the research notes.

## 1. What the folders contain

| Cote | Catalogue description and supplied material | Mathematical centre |
|---|---|---|
| **57** | *Picard[49]*; annotated typescript and letters, some dated 1962. Three Pro packages and twelve Codex transcriptions, including the two A57 packets. | Existence and properties of the Picard functor; connections; divisors and descent; formal and analytic comparison; local Picard groups; Albanese constructions; examples and question lists. |
| **58** | *Théorie de « Lefschetz–Grauert ». Applications en π₁, à Pic etc…*; one Pro package and two Codex transcriptions. | Connectedness in dimension, cutting by equations, formal comparison, effectivity, finite covers and local fundamental groups. |
| **59** | *Construction des faisceaux inversibles sur schémas de Picard[51]*; two Codex transcriptions. | Determinants of Poincaré families, Riemann–Roch, Fourier transforms, polarization torsors and autoduality of curves. |
| **60** | *Fonctions L / Équation fonctionnelle des fonctions L (cas géométrique)*; two Pro packages. | Determinant and duality formalism, boundary cohomology, local monodromy and functional equations; extensive reused printed algebra sheets. |

The supplied corpus has **22 transcription files**, containing **458 scan-marker occurrences**. This is an inventory of the supplied texts, not a claim to possess 458 distinct manuscript images. The catalogue's page totals, the numerical endpoints of packet names and the scan-marker counts measure different things. Gaps in a numerical range remain gaps. Printed or reused leaves are included in the mathematical inventory, but their imprint does not date neighboring handwriting and their assertions are not reassigned to Grothendieck as new discoveries. The inventory and source hashes record precisely what was available.

The handwritten plan on 57:66 gives the most useful internal order: absolute existence; relative existence; equivalence criteria and finiteness; numerical and τ-equivalence; square, cube and correspondences; separation and properness; duality; Albanese; curves; complements over a field; characteristic zero; and local Picard objects. Its physical order is less linear: section 6 appears before an inserted smoothness topic, section 8 before 7, and the square/cube section is renumbered 5 after section 9. The exposition below follows the resulting mathematical numbering and notes the inserted smoothness question. It does not turn this working plan into a chronological table of composition. [K57-04, scan66, lines6–46.]

## 2. Absolute existence: divisors, components and rigidification

The absolute construction begins with actual invertible sheaves and effective divisors. Passing to the Picard functor requires quotienting by bundles from the base and sheafifying in the chosen topology; a rational point of that functor need not already be a line bundle on the original scheme. This distinction is visible both in the connection passages and in the later local-Picard letters. The obstruction can be a Brauer class. An argument using a normalized Poincaré bundle must state why that bundle exists, or work locally and descend it. [C-SA14-001–004, 602, 623, 639; PE_MazurMessing1974; R_Kleiman2005, Theorem2.5 and §3.]

For a represented class with suitable base change, the fibre of the divisor-to-Picard map is the open locus of regular sections modulo units. It is not unconditionally a projective bundle: local freeness of the space of sections, base change, and the regularity of a nonzero section have their own hypotheses. With geometrically integral fibres the regular-section condition has the expected form. The exact sequence for an effective Cartier divisor also explains the tangent map and the obstruction group, which must not be confused with the independent representability step. [C-SA14-623, 647; R_Kleiman2005, Theorem3.13, Exercise3.14 and Remark5.18.]

Rigidification appears several times because it removes different automorphisms. The projective-frame construction on 57:158–162 uses a relatively very ample bundle with a locally free, base-change-compatible space of sections. Its frames form a PGL torsor of complete **marked** embeddings. It does not require the underlying variety to have no automorphisms: preserving a marked embedding pointwise is different from preserving its unmarked image. The finite Stein-factor version is another construction. If the global-functions factor is finite and the required universal equality of global functions holds, normalization along a section kills scalar automorphisms; over a local base its finite algebra is semilocal, so a line bundle there is trivial. No extra flatness of that finite factor is inserted into this argument. [C-SA14-646, 687; `research/root_proofs.md`, §§5,7.]

The Seshadri-type passages pursue existence through divisors, parameter spaces, flat relations and quotients. Their ingenuity does not collapse these steps into one theorem. Universal openness of a support, quasi-finiteness of a parameter map, flatness of an equivalence relation and existence of its quotient are separate assertions. The actual EGA IV₄ §§21.14.3–21.14.4 statements retain smoothness or normality assumptions and a separately treated product case. They do not validate every broader preliminary sentence in the draft. [C-SA14-028–041; PE_EGAIV4; PE_Seshadri1963.]

## 3. Relative existence: descent, quotients and representability

The relative programme adds base change and effective descent. One important correction to the earlier notes is the two-piece descent equalizer: the two local objects must satisfy the **coupled gluing equation**. Separate equalizers on the two pieces lose precisely the compatibility needed for a global bundle. The finite model in the saved computations checks that logical point; FGA's restricted gluing statement gives the exact published comparison. It is not a proof of arbitrary pushout descent. [SA14-36–39; C-SA14-050–059; PE_FGAV1962.]

Representability also has more than one possible output. Under the checked proper, flat, finite-presentation and universal-global-functions assumptions, modern Picard theory gives an algebraic space. A scheme, a separated scheme and a proper scheme are successively different conclusions. The question lists at 57:308–315 repeatedly test these boundaries. An existence theorem for the functor cannot by itself prove the separatedness required by a second theorem about correspondences. [C-SA14-247–263, 674; PE_Stacks0D2C; Kleiman2005Picard, Theorem4.8; R_Murre1966, §3(C), Theorem4.]

A useful exact match is the flat-kernel-pair quotient. When the relation defined by a morphism is flat, with the relevant finite-type or finite-presentation hypotheses, the quotient factorization has a faithfully flat first arrow and a monomorphic second arrow. Uniqueness comes from the quotient sheaf. It does not mean that the quotient may simply be replaced by a schematic image. The nearby DVR application needs its own flatness and separation hypotheses. The transcribed assertion that flatness of the subgroup alone makes the quotient flat fails for the additive finite group scheme defined by `R[x]/(πx,x^p)` over a characteristic-p DVR, with the identity as subgroup. The identity is flat; the quotient is the nonflat group itself. [C-SA14-679–680; R_Murre1966, §3(A), Corollary2; R_SGA3XVII, AppendixIII C.2.1 and C.3.1; R_Anantharaman1973.]

The question whether a smooth proper pointed family with one abelian fibre carries an abelian-scheme structure is deliberately left at the strength actually verified. The opened GIT Theorem6.14 assumes a **projective** family. Its infinitesimal Proposition6.15 is stated for proper smooth data over an Artinian local base. The latter is an exact match for one step of the manuscript's argument, but does not supply the remaining DVR closedness argument in its broader proper setting. A familiar slogan about deformation of abelian varieties would conceal this quantifier change. [C-SA14-609; R_GIT1994, second-edition text at Theorem6.14 and Proposition6.15; R_GenestierNgo.]

## 4. Equivalence criteria, finiteness, numerical and τ-equivalence

The next two parts of the plan link geometry of divisors with finite generation and boundedness. The distinction between Pic/Pic⁰ and Pic/Pic^τ is essential: the latter removes torsion in the Néron–Severi group. The FGA236 addendum gives precise finite-generation and numerical-equivalence assertions; SGA6 develops their proofs and relative forms. A quotient sheaf is still not automatically a quotient scheme. [C-SA14-205–210, 618, 629; Grothendieck1962FGA236Complement; R_FGA236Addendum; R_SGA6, XIII.]

Two exact computations sharpen this sequence. The surface Riemann–Roch positivity argument requires the strict inequality that forces `H⁰(K−D)=0`; the nonstrict reading permits a counterexample on the projective plane. The surface Betti formula is `b₂=c₂−2+2b₁`, with `b₁=2 dim Pic⁰` in the stated setting. Omitting that factor of two gives the wrong answer even for an abelian surface. These are local corrections to a numerical argument, not reasons to reject the finiteness programme. [C-SA14-617, 619; `outputs/root_computations.json`; R_SGA6, XIII, Remark5.3.]

The letters on proper-surjective pullback are also more precise than the shorthand “affine pullback theorem.” SGA6 XII Theorem1.1 gives generic quasi-affineness in the relative setting; Corollary1.5 gives affineness over a field. Remark1.7 records a remaining relative affineness issue in that text. The manuscript's request for a concrete relative quasi-affine but nonaffine example was searched separately. No exact example meeting its specified geometry was identified. C-SA14-677 is the sole class D record, in the explicitly bounded sense of that documented search; it is **not** a claim that no such example exists or that the question is new. [C-SA14-620, 677; R_SGA6, XII, printedpp596–598; `research/root_search_map.md`.]

Tame and wild torsion must be kept apart. FGA236 Proposition2.10(i) concerns **Pic^σ**, defined using torsion orders prime to residue characteristic. It does not establish the stronger Pic^τ propagation sentence on 57:311. Kummer arguments with an invertible exponent likewise do not control p-primary components. Later Picard-specific finiteness inputs cannot be retroactively read into a standalone group-scheme argument. [C-SA14-258, 631; Grothendieck1962FGA236, pp223,235; R_FGA236; R_FGA236Addendum.]

The specialization pages seek p-primary nonsaturation of a homomorphism or Néron–Severi lattice. The phenomenon is established: the checked modern result gives injectivity and a torsion-free cokernel away from the residue characteristic, together with an example of the remaining p-primary behavior. The manuscript's particular finite-subgroup construction is unfinished. In particular, a literal equality `pF=G` with `F⊂X[p]` cannot have nonzero G. Reversing a dubious inclusion might repair the mechanism, but cannot be done without the scan. [C-SA14-216–217; MaulikPoonen2012NS, Proposition3.6 and Example3.12.]

## 5. Square, cube, correspondences and rigidity

The cube calculation is one of the most effective joins between packets. Its n-variable exponents are `(n−1)(n−2)/2` for the base term, `2−n` for singletons and `1` for unordered pairs. Pair indices must be `i<j`; using `i≠j` counts them twice. The same calculation gives the multiplication formula with exponents `n(n+1)/2` and `n(n−1)/2`. The saved symbolic checks corroborate the coefficient identity, while the proof and geometric hypotheses remain in the claim. [C-SA14-607; R_Milne2008, §I.5.]

Normalizing a line bundle on a product along its two axes separates the factor Picard groups from the correspondence term. Infinitesimally, the two Künneth components of `H¹(O)` are removed by the two normalizations. This gives a clean rigidity calculation under the properness, flatness and universal-H⁰ assumptions; it is not a statement about arbitrary nonproper products. The later product calculation temporarily drops the Néron–Severi contribution by replacing full Pic(A) with its dual abelian variety, then restores the distinction in subsequent formulas. The consolidation credits that correction to the text itself. [C-SA14-608, 212; R_Murre1966, §3(C); `parts/picard_lefschetz/outputs/proof_checks.md`, P22.]

The general separatedness of the correspondence functor remains a more delicate comparison. Murre's exact representability statement assumes separatedness. Bertolin–Galluzzi's theorem treats extensions of abelian schemes by tori and points back to Raynaud's III Proposition4.3. The chapter metadata was verified, but that precise proposition was not accessible directly. The opened sources therefore do not justify erasing the manuscript's general hypothesis problem. The corresponding class C record states that boundary rather than converting a missing proof into a universal open-problem claim. [C-SA14-674; MP-SA14-674; R_Murre1966; R_BertolinGalluzzi2020; R_Raynaud1970Corr; `parts/picard_early/supplement_root_audit.md`.]

The group-theoretic rigidity notes contain useful corrections of their own. A nontrivial characteristic-zero extension of an abelian variety by G_a can be anti-affine and have dense torsion, so the proposed exclusion of additive behavior is withdrawn. Topological surjectivity is not faithful flatness: `Spec k→α_p` already separates the two notions. The power-map argument needs commutativity; the conjugacy family of involutions in GL₂ refutes a noncommutative reading. Finite étale rigidity needs closed embeddings or the relevant separated convention: a double-origin étale trait prevents an unrestricted argument from fibrewise agreement. [C-SA14-610–614, 683; R_Brion2009; R_SGA3XI, §6; `research/root_proofs.md`, §3.]

## 6. Separation, properness and the inserted smoothness question

The conic degeneration `xy−tz²=0` supplies a particularly clear history of revision. Its total space is regular and flat; the generic fibre is a projective line and the special fibre is two lines. Special bidegrees `(p,q)` specialize to generic degree `p+q`, and the vertical component classes have bidegrees `(−1,1)` and `(1,−1)`. The resulting Picard component has infinitely many origins. The proposed nonrepresentability conclusion is deleted and its intermediate argument cancelled: **nonseparatedness survives, nonrepresentability does not** in this example. [C-SA14-632–633; K57-07, scans214–219.]

The neighboring triple-line family gives another useful limit. The family `xy(x+y+tz)=0` is flat, but the naive Čech complex of the three **closed** components is not an acyclic-open-cover computation of its structure sheaf. For the concurrent fibre that complex gives zero H¹, whereas the plane-cubic exact sequence gives one-dimensional H¹. This is an independent counterexample with the displayed family retained. It should not be conflated with the valid unit-patching sequence for a specified pushout, developed elsewhere in the folder. [C-SA14-635, 234, 236–237; `research/root_proofs.md`, §5; Ferrand2003Pinching.]

The inserted smoothness question has a precise answer in characteristic zero. SGA3 VI B Proposition1.6 states, under local finite presentation along the unit, that smoothness there is equivalent to local freeness of the conormal module; prior flatness is not added. The authored chapter is Bertin's, so this is credited as a later established result by another author. Picard-specific smoothness is a separate matter: smoothness of Pic⁰ in the checked characteristic-zero family setting does not make every component of the full Picard scheme flat. Nor does a finite flat but nonsmooth 2-torsion factor in characteristic2 supply the separate nonflat example attributed to Mumford. [C-SA14-616, 686, 214, 247–258; R_SGA3VIB, Proposition1.6; R_Deligne1968, Theorem5.5; R_Kleiman2005, Proposition5.19 and Remarks/Examples5.21–5.22.]

Finally, the α/μ/λ dimension notes distinguish abelian, multiplicative and unipotent dimensions from tangent dimension and Néron–Severi rank. FGA236 §2.8 itself calls some further inequalities conjectural, while the checked SGA3 statement proves a smooth-group semicontinuity result and calls the merely flat extension probable. Neither old label establishes current openness; neither proves the unrestricted modern assertion. [C-SA14-263; MP-SA14-218; DemazureGrothendieck1970SGA3II, X, Remark8.7.]

## 7. Duality: connections, Poincaré bundles and determinant lines

The connection sequence on 57:80–94 begins with principal parts and the Leibniz rule. Local connection forms change by dlog of a unit, giving the obstruction in H¹(Ω¹); if it vanishes, connections form an affine space with the expected automorphism action. On the abelian product, restriction to the two zero sections removes the pure Künneth components, but leaves a mixed class. Its identity normalization and sign are expressly uncomputed. Mazur–Messing's universal extension theorem is an exact later comparison for rigidified, integrable, group-compatible connections. It must not silently replace the initial functor of all relative connections. Oda's de Rham/Dieudonné comparison is another later result, with a general smooth-proper injection distinguished from the abelian isomorphism. [C-SA14-001–010,142; SA14-16; MP-SA14-001–005,054; PE_MazurMessing1974; PE_Oda1969, Corollaries5.11–5.12.]

Cote59 turns the Poincaré family into an invertible sheaf on a Picard component by taking a determinant of cohomology. This requires relative perfectness; a bare proper morphism and arbitrary coherent coefficient do not suffice. With the convention

\[
\det R\Gamma=\bigotimes_i(\det H^i)^{(-1)^i},
\]

tensoring a perfect complex by a line bundle from the base multiplies its determinant by that line bundle to the Euler-characteristic exponent. Changing a chosen basepoint twists the normalized Poincaré bundle by an **inverse** evaluation line. The change of determinant is therefore the power `−χ`. This sign comes from normalization, independently of any theta-divisor terminology. [C-SA14-655–656; R_KnudsenMumford1976, Theorem1; `research/root_proofs.md`, §8.]

Grothendieck then asks for the Néron–Severi class of the determinant. Under the stated Riemann–Roch hypotheses, with `D=c₁(P)` and `a=ch(F)Td(T_X)exp(δ)`, its degree-two cohomological contribution is

\[
c_1(\det Rp_{2*}(P\otimes L\otimes F))
 =\frac12p_{2*}(a_{n-1}D^2).
\]

The rank term in `ch(F)` is indispensable. For a curve and a bundle of rank ρ and degree c, the correct Euler characteristic is `ρ(1−g+d)+c`, and the theta contribution is multiplied by ρ. The transcribed rank-one expression fails for a rank-two trivial bundle on an elliptic curve with a degree-one line bundle. Determinant additivity is additivity in the K₀ coefficient F; dependence on the tensor class δ is generally polynomial, of degree g−1 on an abelian g-fold. On a principally polarized threefold the transform scales by four under doubling δ, rather than by two. [C-SA14-658, 667–668; R_SGA6; R_Mukai1981; `outputs/root_computations.json`.]

The Fourier calculations identify several genuinely different issues. In the cohomological diagonal model, the standard determinant gives `−adj(A)`. Applying that operation twice gives `(-1)^g det(A)^(g−2) A`. Its sign depends on the determinant convention; changing to the inverse determinant changes the dictionary. Primitivity is a separate integral question: `diag(1,2,2)` is primitive but its adjugate `diag(4,2,2)` is not. Even Euler characteristic also does not imply divisibility by two in NS: polarization type `(1,2)` has χ=2 and a primitive class. For Chow groups, Beauville's actual grading is `CH^p_(s)→CH^(g−p+s)_(s)`; bare codimension reversal is justified only in the corresponding grade-zero setting. [C-SA14-659, 661–665; R_Beauville1983; R_Beauville1986, Proposition1; R_Mukai1981.]

The sign in tensor/translation equivariance required an independent correction to **this run's reconstruction**. With the positive Poincaré kernel,

\[
\Phi(L\otimes P_\beta)=t_\beta^*\Phi(L),\qquad
h_M(\beta)=t_\beta^*M\otimes M^{-1},
\]

the Picard-class difference is **+h_M(β)**. The support of the pulled-back divisor moves by −β, but does not supply a second minus to a definition already using pullback. The manuscript's negative expression agrees if its tilde homomorphism means `−h_M`, or if the inverse kernel is used consistently. Its own margin asks for exactly such a sign check. Under the declared convention, writing Q for Alb¹, P for Pic^δ and R for the determinant component on B, the relation is `R+χQ−h_*P`. A canonical trivialization needs the coherent determinant isomorphism and its descent data; equality of torsor classes alone gives only existence. The register retains this distinction instead of declaring the exact handwritten signed product certified. [C-SA14-657, 669; MP-SA14-655,669; R_Mukai1981, §3(3.1); `parts/lfunctions/cross_review_root_655_673.md`.]

## 8. Albanese objects and the chosen abelian Picard part

The Albanese programme occurs both in cote57 and in the determinant construction. It should be formulated with the **maximal abelian subvariety of the Picard identity component**, not automatically with its Chevalley abelian quotient. In families, a compatible family of such abelian subvarieties is a genuine condition. Laurent–Schröer's precise modern theorem constructs the relative Albanese torsor under that condition, and their proper-field corollary gives the expected universal object when H⁰ is the ground field. Their field-extension theorem explains the maximal-subvariety issue. This is a strong later match, but does not make the required abelian family exist in every degeneration. [C-SA14-615; R_LaurentSchroer2024, Theorems7.2,10.2 and Corollary10.5.]

The later cote59 version deliberately starts with a **specified** abelian scheme B mapping into Pic_X and an equivariant torsor mapping to a Picard component. Its dual recipient can be constructed without declaring B the whole Picard identity component. The resulting determinant relation has the same basepoint normalization. The further proposed universal property among arbitrary commutative group targets is a separate extension: proper connected schemes over a field have constant maps to affine schemes under the usual global-functions condition, but that observation is not a theorem about every relative or nonsmooth group target. [C-SA14-670–671; MP-SA14-670; R_LaurentSchroer2024; R_Alexeev2002.]

## 9. Relative curves, autoduality and theta torsors

For curves, Riemann–Roch specializes the determinant construction and connects it to the canonical principal polarization. The sign of the autoduality map depends on whether the Abel map uses `O(x−x₀)` or `O(x₀−x)`, as well as on the determinant and translation conventions. The word “canonical” cannot determine this sign by itself. The theta torsor is naturally Pic^(g−1), and the involution `L↦K_C⊗L⁻¹` supplies the expected doubled-torsor class. Alexeev's principal theta-pair construction and evaluation divisor give a precise modern comparison; results for arbitrary polarization types answer a broader but different question. [C-SA14-671–673; R_Kleiman2005, Remark5.26; R_PoonenStoll1999, §4; R_Alexeev2002, §3.0.5–3.0.11; R_Laga2025.]

The integer calculation behind annihilation of a torsor must use a **gcd**, not an lcm. For g≥2,

\[
\gcd_{\lambda\in\mathbb Z}(\chi\lambda^g-\lambda^{g-1})
=\gcd(\chi-1,2).
\]

The same conclusion follows using positive λ only. Parity gives the lower bound; λ=1,2,3 give the upper bound after reduction modulo χ−1. This establishes annihilation of the class, not equality of two chosen canonical sections. The separate question comparing the doubled class with the Poincaré pullback representing 2λ remains a comparison of normalized constructions. [C-SA14-664, 666; MP-SA14-664,666; `research/root_proofs.md`, §9.]

The universal-curve question has a strong Franchetta descendant for the generic curve of genus g≥3, with marked points added in the pointed version. Low genus cannot be slipped into that statement: on a pointed genus-one curve the origin divisor has degree one while the canonical class has degree zero. The distinction between a stack and a coarse universal family also matters. Schröer's theorem supplies the exact arbitrary-characteristic range used here; Fringuelli–Pirisi's abelian-variety Franchetta theorem has its own genus, ground-field and level assumptions. [C-SA14-660; R_Schroer2003, Theorem5.1; R_FringuelliPirisi2019.]

The curve calculations elsewhere in cote57 and at the end of cote58 have been joined without identifying every singularity with a node. Normalization gives

\[
p_a(C)=\sum_i g(\widetilde C_i)+\sum_s\delta_s-r+1.
\]

The δ-invariant is a normalization length, not merely a branch count. For a nodal connected curve this becomes the sum of component genera plus the first Betti number of its dual graph; the corresponding affine Picard part is a torus. The genus/graph computation is consolidated at C-SA14-642, retaining both source occurrences. The stable-graph dimension formula is likewise separated from unsupported extensions to unstable components. [C-SA14-642, 644; MP-SA14-642,644; Ferrand2003Pinching.]

For a smooth proper curve with a nonempty finite **étale** puncture and invertible n, the compact-support Kummer calculation relates to the generalized Jacobian and retains its Tate twist. Over an imperfect field “finite reduced” would not suffice. The proposed transgression comparison has a checked modern field-level semiabelian-torsor theorem in Petrov–Skorobogatov, published online in August2026. It is not thereby proved for every relative compact-support setting in the manuscript. [C-SA14-640–641; MP-SA14-641; R_MVW2006, §7; R_HarariSzamuely2009; R_PetrovSkorobogatov2026, Theorem5.1.]

## 10. Complements over a field and characteristic zero

The plan's field-theoretic complements concern noncomplete varieties, non-Cartier classes and birational behavior. The prose and calculations repeatedly need the difference between **R₁** and normality. For an affine target, codimension-one valuation tests extend functions only with the needed S₂ condition. The ring `k+(x,y)²⊂k[x,y]` is a finite-type R₁ domain whose normalization is unchanged off the origin, but x is regular at every height-one point and does not belong to the ring. Replacing an affine target by a proper target also changes the problem: `[x:y]:P²⇢P¹` extends over every codimension-one point while remaining undefined at one point. [C-SA14-648–650; `research/root_proofs.md`, §7.]

Several reused sheets make these distinctions especially visible. A Cohen–Macaulay module over a regular local ring need not be free unless it is **maximal** Cohen–Macaulay; the residue field of a DVR is the small counterexample. A reused field-theory “Zariski lemma” is the relative-constants coefficient lemma for a rational function algebraic over K(X), not the familiar finite-type-field theorem. The graded-module leaves have exact finite-support arguments, while infinite duals require products. These assertions are individually in the claim map, with their printed provenance retained. [C-SA14-638, 230, 654, 675.]

The characteristic-zero section includes the analytic comparison programme rather than merely a smoothness slogan. A letter dated **6 July 1962** and its later French proof distinguish the Picard group of an analytic germ from that of its closed fibre. Three maps must be separated: injection into formal Picard data, agreement of the images at each finite level, and realization of an entire compatible formal class by one analytic germ. The necessary-and-sufficient finite-length condition belongs to the third assertion. Grauert supplies the coherent input; the topological and integral-image input requires its own finiteness and compatible stratification assumptions. [C-SA14-070–089; PE_Grauert1960; PE_Grauert1963; PE_Lojasiewicz1964; PE_Goresky1978.]

Formal-functions comparison does not imply surjectivity at every finite order. A two-term complex with differential multiplication by t has finite-order kernels with zero transition maps; it refutes that intermediate inference. It is a countermodel to a logical step, not a proper analytic family contradicting the final Picard theorem. Likewise, a Mittag–Leffler argument selecting a compatible ample class does not imply that the entire Picard groups stabilize. Proper formal existence for an already algebraic model must be distinguished from algebraization of an abstract formal scheme. [C-SA14-081, 085, 100–116; `parts/picard_early/computations.md`, §§12–18.]

A modern proper relative GAGA comparison is available over complex affinoid germs in Abramovich–Temkin, including radius-zero germs in the precise framework cited by Hall. That establishes a modern bridge; it does not identify the first historical publication of the combined exposition the 1962 letter calls unwritten. Kresch–Mathur gives further exact statements about actual Picard groups and their Mittag–Leffler behavior, with characteristic-zero and complete-DVR positive-characteristic cases separately qualified. [PE_AbramovichTemkin2019, §6.3.4 and AppendicesB–C; PE_Hall2023; PE_KreschMathur2025.]

## 11. Local Picard objects and pro-objects

The last tentative part of the plan is already a substantial research line. For a proper regular resolution of a complete local scheme, restriction to the puncture gives a divisor localization sequence: the kernel is generated by exceptional **codimension-one** divisors. Proper formal existence then compares the resolved scheme with its infinitesimal neighborhoods. These two facts do not alone produce a representable quotient. Over a non-separably-closed residue field the exceptional lattice is a Galois module, and its H¹ obstruction must be distinguished from the Brauer obstruction attached to a Picard sheaf. The source's change from a constant to a twisted lattice is therefore mathematically consequential. [C-SA14-601–602; R_EGAIII1; R_Lipman1976; R_Kollar2014.]

If an exceptional model has an invertible defining ideal with ample conormal, the square-zero units sequence and Serre vanishing imply eventual stabilization of its Picard system. The existence of such a positive model is a separate assertion. In dimension two, negative definiteness of the exceptional intersection form controls injectivity of the divisor lattice into NS; a higher-dimensional statement needs its actual negativity and projectivity assumptions. The intrinsic-functor and independence-of-resolution questions are correspondingly retained at their stated generality. Kollár's precise modern geometric setting, for example, assumes S₂, pure dimension at least three and essential finite type over a field. [C-SA14-603–605, 676; R_Lipman1975; R_Boutot1978; R_Kollar2014, Condition3 and the resolution discussion.]

One later identification is unusually explicit. Lipman's article on a scheme over an Artin ring says that it answers a problem raised in a **September1969 letter from Grothendieck**. Its definition, representability theorem and comparison of rational points match the Witt-vector/Greenberg question recorded here. That date belongs to the identified problem's documented history, not to every page in cote57. The paper was received in December1973 and published in December1976. [C-SA14-606; R_Lipman1976, Introduction, Definition1.1, Theorem1.2, §5 and Theorem7.5.]

The repeated henselian question is consolidated at **C-SA14-626 / MP-SA14-626**. Elkik's precise result compares the complement of V(J) for a noetherian henselian pair (A,J) with the corresponding puncture after J-adic completion. The ideal defining the puncture and the ideal of completion are the same. This is an isomorphism on line-bundle isomorphism classes, not automatically full faithfulness of the line-bundle category. Finite-order approximation, descent after an étale local neighborhood, and comparison for an arbitrary open with a fixed maximal-ideal completion remain separate questions. Artin approximation is not equality of arbitrary Picard groups. [R_Elkik1973, III.1 Theorem3 and pp573–574; Artin1969Approximation; C-SA14-097, 202–203; the source variants retained under C-SA14-626.]

The cone examples make the differences computable. Under the normality and section-ring hypotheses, the local Picard group at an affine-cone vertex is obtained from Pic of the projective base by quotienting the polarization class. For a cone over a smooth projective curve, the positive-twist groups H¹(C,Lⁿ) supply the extra formal layers. For a smooth plane curve of degree d their total dimension is `binomial(d−1,3)` for d≥4; quartics already produce a nonzero layer. The draft's degree-six sufficient example is not the first possible degree. An affine cone, its puncture, a line-bundle total space and a projective cone are different schemes; the EGA II contraction hypotheses and the source's own correction of a missing Z summand prevent their formulas from being interchanged. [C-SA14-624–625, 634, 323–324, 329, 331; R_Kollar2014, Example25; R_EGAII, §§8.7–8.8; Traverso1970Seminormality.]

## 12. Cote58: connectedness, formal Lefschetz and fundamental groups

The beginning of cote58 treats local depth and connectedness in a specified dimension before passing to Picard or fundamental-group consequences. The complete-local cutting theorem and its converse have exact counterparts in SGA2 XIII2.1. The component-dimension bounds, the number of cutting equations and the exclusions of irreducible dimensions zero and one in the converse must be retained. A depth hypothesis used in a proof reduction should not be added to the final statement if the published theorem does not require it. [C-SA14-651–652; R_SGA2, XIII2.1 and the immediately following converse.]

Ordinary connectedness of a generic fibre is weaker than geometric connectedness, and the distinction produces a complete counterexample to the literal specialization statement. Over A=Z_(5), let B=A[T]/(T²+1) and take `P¹_B→Spec A`. The base is regular and geometrically unibranch, and the total space is proper and integral. The generic fibre is a connected projective line over Q(i); the special fibre is two disjoint projective lines because the polynomial splits modulo5. Higher projective spaces give the analogous example in every required dimension. This is not dismissed merely because related published text uses a conventional fibre formulation: its missing geometric convention must be stated. [C-SA14-273; `parts/picard_lefschetz/outputs/proof_checks.md`, P1.]

The formal Lefschetz sequence then separates comparison, full faithfulness, effectivity and applications to covers. A fully faithful functor on locally free sheaves can carry the multiplication and unit of a finite algebra, but an existence theorem is needed to algebraize the underlying object. Étaleness and shrinking are further steps. The formal-neighborhood group, the inverse limit over open neighborhoods and the global fundamental group cannot be identified without those steps. [C-SA14-279–299; Grothendieck1968SGA2, IX–XI.]

Line bundles reveal the low-degree issue particularly sharply. H¹ and H² control classes and obstructions, while H⁰ of the unit sheaf controls automorphisms. Over a DVR, the automorphisms 1 and 1+t have the same reduction even when the relevant higher cohomology vanishes. Thus a Picard-group comparison does not establish an equivalence of line-bundle categories. The categorical parafactorial statement also needs its depth/unit condition; a DVR tests the boundary. [C-SA14-292, 326; MP-SA14-241,260; Grothendieck1968SGA2, XI.]

Completion of coherent sheaves modulo supports missing the divisor introduces another distinction: an exact quotient functor need not be full. In the recorded three-variable complete local example, formal endomorphisms include a series with coefficients `z^(−n²)`, while inversion of one algebraic denominator allows only linear growth of pole order. The explicit counterexample fails the depth condition of the positive theorem, so it refutes the unrestricted formulation without refuting Raynaud's controlled comparison. Undefined symbols in the proposed essential image are left undefined rather than assigned the values a desired theorem would require. [C-SA14-300–307; Raynaud1974Lefschetz, I§0 and I1.1–1.5; `parts/picard_lefschetz/outputs/proof_checks.md`, P5–P7.]

The negative-twist and graded calculations distinguish four assertions: positive graded finite generation, negative-twist vanishing, coherence of higher direct images, and a separate degree-zero coherent-hull condition. Exactness reverses one transcribed injective/surjective word. A skyscraper away from the divisor separates the degree-zero claim from higher-cohomology vanishing. The inverse-limit step requires the stated Mittag–Leffler control; a lim¹ obstruction cannot simply be discarded. The reused existence theorem on the neighboring printed leaves has the actual projectivity, flatness, fibrewise regularity and depth hypotheses of SGA2 XII3.1–3.2. [C-SA14-308–317; Grothendieck1968SGA2, IX2.1 and XII3.1–3.2.]

The local fundamental-group conjecture remains a source of an important scope correction. Suzuki's 2023 theorem proves finite generation of the **maximal pro-nilpotent quotient** under its complete-local and connectivity assumptions. It does not prove finite generation of the full profinite group asked about in the manuscript and SGA2. Recent searches did not locate a complete later settlement. This reports the reached literature boundary, not a proof that the full question is still open on 19 November2026. [C-SA14-653; MP-SA14-653; R_Suzuki2023, Theorem1.2 and Conjecture1.1; R_SGA2, XIII3.1.]

## 13. Cote60: functional equations in the author's order

The opening calculations concern characteristic functions of endomorphisms. Exterior traces give the determinant, symmetric traces its reciprocal, exact sequences ordinary multiplication, and tensor products the operation now described by rational Witt multiplication. Semisimplicity is not needed. The source revises its λ/σ convention, so the deleted generating identity is recorded as a withdrawal. [C-SA14-401–405; Deligne1973Constants, §§10.3–10.5; BGT2013Endomorphisms.]

The next step introduces Frobenius, weights and selfduality. Purity controls complex absolute values; rationality constrains a determinant; a perfect pairing supplies selfduality; alternating symmetry controls the normalized sign. These are different premises. For q=pᵃ, rationality forces the parity of **a·rank·weight**, not always rank·weight alone. Rank-one and symmetric-pairing examples test those implications, but are not counterexamples to rational polarized motives satisfying all the stronger assumptions. [C-SA14-406–416; Deligne1974WeilI; Deligne1980WeilII; `parts/lfunctions/proof_notes.md`, §§1–2.]

The proper functional equation comes from duality and alternating determinants. “Compactifiable” is visibly replaced by “proper.” In the nonproper case the natural boundary object is `Cone(RΓ_c→RΓ)`, and dualizing the cone produces the shift −1 asked about on the page. Complete A¹ and G_m tests distinguish ordinary from compactly supported determinants; the two normalized factors are reciprocal, not literally equal in the A¹ example. The proposed bound expressed in terms of an undefined boundary “type” remains an identification problem. [C-SA14-417–426, 447; MP-SA14-403–405.]

For curves, ordinary inertia invariants are not exact. The skyscraper cokernel records their failure and contributes a local factor. Its support is not confined to ramification of the quotient representation: a nontrivial tame extension of unramified endpoints already has a nonzero defect. The corrected support bound uses the middle representation and the actual failure of exactness. This mixed example is not passed off as a counterexample in a pure geometrically semisimple category. [C-SA14-427–432; `parts/lfunctions/outputs/calculations.txt`.]

Grothendieck then rejects a global-composition-factor recipe because it lacks locality and étale compatibility. The succeeding local construction chooses a normal subgroup acting unipotently, filters and averages over the finite quotient. It gives an additive virtual class independent of that subgroup, not generally a tensor fibre functor. The separate defect α need not be additive. The combination μ is additive and, under the written quasi-unipotent hypotheses, vanishes by dévissage. That last vanishing is explicitly this run's consequence of the definition, not a claimed handwritten withdrawal. [C-SA14-433–441.]

The ending Euler-characteristic and determinant calculations match the GOS framework and Laumon's sign-sensitive epsilon-product theorem when closed-point degrees, the additive character and a differential are retained. A lost Tate shift is recorded as a separate alarm. The final normalization question requires the correction to have lower *niveau*. Solving an unrestricted rational cocycle equation does not solve that narrower problem when the allowed subgroup has not been defined in the supplied text. [C-SA14-442–451; MP-SA14-407–412; Laumon1987Fourier; `parts/lfunctions/literature_notes.md`.]

### The reused algebra is a second body of evidence

The printed sheets in cote60 include Haar integration, finite-length duality, differents and conductors, local Gorenstein criteria, determinantal ideals, formal series, characteristic-two derivations, class groups and reflexive lattices. Their claims have been read and checked individually. Several exact Samuel matches were recovered by following references backwards, including the full N(i,j) family, both alternatives of the weighted-cyclic factoriality criterion and the companion-series lemma. A talk dated November1962 survives in a text citing1965 publications, so talk date and surviving revision are not conflated. [C-SA14-452–567; `parts/lfunctions/literature_notes.md`, §§3–5.]

The most significant corrections have concrete witnesses. The global conductor formula through trace duals fails without reflexivity: for `A=Q[x,y]`, `B=Q(√2)[x,y]` and `C=A+(x,y)√2`, the conductor is `(x,y)B`, whereas `C*=B*=B`. The height-one or reflexive repair is stated separately. Two difficult local converses are independently proved using a socle argument and the regular trace on the Artinian fibre, with semilocal factors retained. [C-SA14-467, 472, 563–564; `parts/lfunctions/proof_notes.md`, §6.]

The formal-series construction has two distinct faults: permitting zero exponents, and a within-block normalization that divides by the wrong variable. The positive coprime example `z²=x⁵+y⁷` tests the latter under the intended inequalities, and the corrected recurrence has a full block proof. Other checked boundaries include the direction of Fitting-ideal inclusion under a quotient, signed lattice exponents without a containment hypothesis, the missing nonzero-module condition in a Hom–Ext criterion, and codimension-two defects invisible to height-one calculations. These belong to the printed algebra's assessment, not to a list of new Picard conjectures. [C-SA14-488–489, 503, 531–537, 546–551, 556, 565–567.]

## 14. What the earlier notes got right, and what changed

The earlier notes were often strongest when they preserved a local question: a sign to verify, a missing hypothesis, a cancelled argument, or a gap between an actual line bundle and a Picard-functor point. Merging their repeats does not diminish those observations. It makes the changes of formulation visible across the packets: henselian comparison, normalized products, Oda comparisons, normalization/genus formulas and cone calculations now have canonical destinations with the variants retained.

The main corrections are more precise than wholesale acceptance or rejection:

- The hyperplane counterexample now uses **P² embedded by O(3)**, so a general hyperplane really cuts a smooth cubic; a cubic in the ordinary linear embedding would not meet the hypothesis.
- The descent equalizer keeps its coupled gluing equation, and formal comparison is no longer confused with finite-order surjectivity.
- A finite flat but nonsmooth torsion example is distinguished from a nonflat Picard family; tame Pic^σ is distinguished from wild Pic^τ.
- The conic's nonrepresentability argument and the missing full-Pic factor in a product formula are credited with their **own later corrections** on the pages.
- Integral divisibility, parity of Euler characteristic, annihilation of a torsor class and a chosen canonical trivialization are kept separate.
- The conductor example corrects a global nonreflexive claim that the earlier order discussion did not qualify.

A false formula in the manuscript does not require a “corrected” verdict for a note that had already diagnosed the fault correctly. Similarly, an item recording a withdrawal can be based on a correctly retained source note. This explains why the note-verdict counts differ markedly from the numbers of false or withdrawn mathematical assertions. Ideas imported from the earlier runs' context are labelled as those runs' ideas; they have not become source claims by repetition.

## 15. Literature status, chronology and the next research tasks

The A–F class records **publication fate**, separately from status on the manuscript pages. A requires an exact own-author published counterpart or announcement, not merely an item somewhere in an EGA/SGA-associated programme. B identifies checked established developments in other authors' publications, retaining attribution where, for example, Murre or Raynaud explicitly reports a result of Grothendieck. E records the earlier or standard printed input; it does not date undated handwriting by the sheet on which it appears. C states the developed part and the exact mismatch. F identifies the missing predicate, antecedent or notation that prevents identification. The sole D record describes a bounded unsuccessful exact-example search and makes no novelty claim.

The searches used primary texts and the requested discovery routes, including arXiv, Numdam, zbMATH Open, MathOverflow, EGA, SGA, author bibliographies and collected works. Broad title matches were followed back to exact theorem statements. Failed or inaccessible endpoints remain recorded. Every claim has a search association; a later paper on the same subject was not accepted as an exact settlement without comparing hypotheses. The search logs distinguish a statement read directly from one checked through an explicitly identified later quotation. Bibliography `note={verified}` means the listed URL or DOI was opened; `annote` records whether the mathematical witness was the full text, a precise later citation, or metadata only. Unread primary witnesses remain labelled unverified rather than being upgraded by familiarity.

The chronology similarly distinguishes an exposé date, receipt date, preprint circulation, publication and later revision. Examples include the FGA236 addendum versus the May1962 exposé; Murre's May1965 talk versus the 1966 collected volume; Lipman's documented1969 letter versus its1976 publication; Mukai's1979 receipt versus1981 publication; the1998 Poonen–Stoll draft,1999 article and2014 correction; and the2024 preprint versus2026 publication of the semiabelian spectral-sequence theorem. No such date is used to date an undated manuscript page without documentary evidence.

The most useful next work is consequently targeted. Some tasks are finite source comparisons, such as reading the exact Raynaud correspondence proposition and settling the determinant symbol dictionary against the scans. Others are theorem-building tasks with a clear boundary, such as the analytic/formal Picard criterion or the exact original-field generic-hyperplane assertion. The ranked list in `SA14_directions.md` gives the source item, claim and problem IDs, the result sought, the known input and the first concrete step for each task. None of those directions is developed here.

The 42 links to other projects are preserved **as quarantined leads** with their note IDs and run names. An unavailable Longue Marche, Dérivateurs, S6 or earlier research-run endpoint cannot be checked by opening a paper on a related subject. These leads have their own table and are never counted among verified two-ended links. The supplied archive and published endpoints have been checked at both ends, with comparisons distinguished from explicit author cross-references.

## 16. Audit, reproducibility and final counts

The completed registers are accompanied by the actual reading and search logs, proof notes, calculation code and outputs, explicit merge decisions and `CHECK_EVENTS.tsv`. A documentary comparison is not labelled an independent proof. A finite example is not called a formal geometric certificate. A theorem invocation is not represented as a re-proof of its entire source. The independent checks also record the correction of the modern determinant sign reconstruction, so the audit includes corrections to this run as well as to prior notes.

Whole external books and downloaded primary PDFs are not redistributed. Their URLs, exact locators and retrieval receipts are retained. Original attached files and prior checkpoint archives are excluded from the final archive. The source hash inventory permits verification against the supplied ZIP, and the execution guide identifies the programs and their saved outputs. The top-level tables, rather than the preserved pre-merger part counts, give the final consolidated totals below.

<!-- FINAL_COUNTS -->

### Coverage and deliverables

| Measure | Count |
|---|---:|
| Indexed note entries | 440 |
| Consolidated items | 386 |
| Claims | 522 |
| Problem records | 180 |
| Undecided mathematical reading alarms | 234 |
| Ranked directions | 18 |
| Checked archive/publication links | 138 |
| Quarantined external-project links | 42 |
| Bibliographic records | 158 |
| Check events | 1959 |
| Named calculation groups | 91 |
| Transcription files | 22 |
| Scan-marker occurrences | 458 |

### Entry verdicts

| Measure | Count |
|---|---:|
| kept | 303 |
| merged | 126 |
| corrected | 11 |
| withdrawn | 0 |
| rests on a misreading | 0 |

### Item kinds

| Measure | Count |
|---|---:|
| conjecture | 46 |
| unproved claim | 108 |
| unpursued implication | 14 |
| idea of the earlier run | 29 |
| reading question | 51 |
| self-flagged step | 30 |
| withdrawn in the same text | 19 |
| title, date or page count | 16 |
| other | 73 |

### Claims by publication-fate class

| Measure | Count |
|---|---:|
| A | 82 |
| B | 94 |
| C | 105 |
| D | 1 |
| E | 198 |
| F | 42 |

### Claims by status on the pages

| Measure | Count |
|---|---:|
| proved there | 46 |
| proof sketched | 196 |
| stated without proof | 122 |
| corrected by himself later | 25 |
| false as stated | 39 |
| open on the pages | 94 |

### Bibliographic verification and link types

| Measure | Count |
|---|---:|
| verified | 152 |
| unverified | 6 |
| folder | 61 |
| published work | 77 |
| our projects | 42 |

The 91 calculation groups comprise root: 24, picard_early: 26, picard_lefschetz: 16, lfunctions: 25. Their assertions passed in the saved outputs. This count includes exact finite examples, symbolic identities and explicitly scoped models; it does not mean 91 independent general theorem proofs.

The 42 external-project rows are supplied separately in `SA14_project_leads.tsv`; the 138 checked rows are also available without them in `SA14_checked_links.tsv`. The required combined `SA14_links.tsv` preserves the requested kind vocabulary and labels every unavailable endpoint explicitly.
