# SA18 — Variétés abéliennes

## Scope and principal findings

**Completed consolidation, status assessed on 19 November 2026.** This dossier
covers every one of the 335 indexed Pro-note entries and the complete supplied
transcriptions for cotes45–56. It also retains the cotes11,16 and44 material
physically included in the four Pro packages. Those additional witnesses are
identified by their actual cote; they have not been relabelled as abelian-variety
pages. The canonical tables contain **341 items, 553 claim records
and 160 problems** after the documented cross-package merges.

The central mathematical movement is from group schemes and torsors to the
duality of abelian schemes, Fourier convolution, reduction and Torelli, with
the operator and correspondence calculus providing a second organizing line.
Several apparent open questions are settled exactly by later work: the
perfect-field reconstruction from the full group scheme A[p], the derived
Fourier inversion theorem, degree-two quadratic invariants, and a number of
relative torus and Picard statements. Other obligations survive in a more
limited form than the earlier notes suggested: compatibility of a particular
constructed morphism, an unchecked pairing comparison, an integral
normalization, or a missing hypothesis in an abstract extension argument.
The records distinguish these source-level obligations from currently open
general research problems. [CL-SA18-16050, CL-SA18-16069, CL-SA18-45121;
MP-SA18-16007, MP-SA18-11036.]

The consolidation also finds substantive false statements. Some are already
cancelled or corrected on later pages; some are integral or characteristic-p
failures hidden by familiar characteristic-zero analogues; some are literal
sign, degree or missing-map errors; and some are overstatements introduced by
the earlier notes. An explicit counterexample is attached to the precise
assertion it tests. A counterexample to a weakened abstraction is never
reported as a counterexample to every stronger geometric formulation.
[Examples: CL-SA18-16001, CL-SA18-16086, CL-SA18-11064,
CL-SA18-45013, CL-SA18-46083.]

No scans were supplied. The existing second-pass corrections control where
they apply, but this run makes no new decision about the ink and changes no
diplomatic transcription. Its 240 reading alarms specify the written
reading, the mathematically suggested alternative, the evidence and the
consequence of the choice. A confirmed written error remains an authorial
error; mathematical convenience does not justify silently changing it.

## 1. The corpus and how to use the dossier

### Supplied witnesses

The attached archive contains 64 source files, including 26 transcription
files with 14,507 lines and 447 scan-marker units. These are **witness units**,
not 447 different physical manuscript pages: some Pro and Codex witnesses
overlap, and a package may include material outside the twelve topic cotes.
The catalogue's Pro/Codex columns are not a reliable test of whether a file is
actually present. In particular the supplied K49–K52 and K55 files were read
although their catalogue transcription columns contain zero. The hashed
manifest and `SA18_source_coverage.json` document the available corpus.
[Supplied `SA18_texts/TOPIC.md`; `source_manifest.json`;
`research/page_index.json`; the four owners' read logs.]

| Cote | Catalogue subject and supplied work, in archival order | Principal dossier content |
|---|---|---|
| 45 | Semisimple groups; annotated typescripts; quadratic and exterior forms | Distributions, infinitesimal groups, roots and Borels, classical groups, Clifford and Witt conventions; the1961 quadratic-invariant letter |
| 46 | Group schemes and principal bundles | Lang-type descent, Frobenius and Verschiebung, logarithmic differentials, divisors and Brauer–Severi spaces, H¹, semilocal arguments, reused chamber theory |
| 47 | Convolution and Fourier transformation on abelian varieties | Relative kernels, inversion, determinant line and shift, nondegenerate line bundles, Chern calculations and duality |
| 48 | Plan for EGA VII | An organizational programme for descent, representability, group schemes and cohomological tools; compare precise later statements rather than treating headings as theorems |
| 49 | Picard of abelian schemes | Duality and Picard representability with their base hypotheses |
| 50 | Notes on Lang's book | Rigidity, endomorphisms, isogenies, polarizations, intersection and characteristic-polynomial formulas |
| 51 | Good reduction, Shimura–Koizumi | Relative Hom, Hilbert/Picard questions, abelian parts, torsors, purity and completion |
| 52 | Torelli | Duality in the differential of Torelli, hyperelliptic failure, infinitesimal fibres, reduction and descent |
| 53 | Algebraic groups, including a1973 letter | Components, geometric reducedness, monoids, Hopf algebras, comodules and representability of module functors |
| 54 | Cohomological duality of abelian varieties | Universal vector extensions, Hodge–de Rham data, restricted Lie structure and the A[p] reconstruction question |
| 55 | Analytic spaces | Coherent sheaves and global sections, abstract equivalence criteria, coherent elimination, dimension, a complex-torus example |
| 56 | Lefschetz–Hodge and vanishing cycles; a1962 offprint | Quadrics and cones, specialization, relative tori and centres, Delzant's Stiefel–Whitney construction, reused GIT material |

The associated c11 correspondence formalism, c16 Lefschetz-operator and
standard-conjecture material, and c44 cycle-Jacobian programme are essential
to interpreting the supplied notes. Reused sheets also contain Brauer theory,
Matlis duality, étale morphisms, EGA fragments and Karoubi's named text. Physical
co-location supplies neither common authorship nor a theorem connecting all
these subjects. [Source-owner reviews; SA18_links.tsv.]

### Record identities and the three voices

`SA18_entries.tsv` has exactly one row and one verdict for each original index
ID. Its target is the canonical item. A broad indexed note may also provide
context for a supplemental transcription item; that relation is stored as
`related_note_entries`, not as a second verdict for the same entry.
There are 56 supplemental items without an
indexed source assignment. They retain direct transcription coordinates.

Claims are more granular than note entries. A single note can contain several
independent assertions, while a claim may occur in several folders. The
114 claims with an empty `items` array arise from
unindexed transcription passages, principally the fully read Codex witnesses.
This is deliberate: no Pro-note ID has been invented to cover them. The
canonical map also retains explicitly labelled earlier-run constructions and
comparators when the index asks that they be checked. Its total therefore
counts **claim records in the supplied corpus**, not 553 newly
discovered theorems by Grothendieck.

Every record separates the manuscript's short wording, the modern statement,
and the reconstruction. The owner files remain as the detailed pre-integration
audit trail. `SA18_aliases.json` explains every removed canonical ID; merged
occurrences retain authorship, source-specific hypotheses and different proof
statuses. `research/integration_decisions.md` gives the reasons for the
equivalences and the significant nonmerges.

### What the classifications mean

The A–F classification is independent of truth and of page-level proof status.
**A** identifies an exact result in Grothendieck's own later published work;
**B** an established development by another author; **C** a partial development
with the precise remaining clause stated; **D** a bounded search that did not
identify a development of the exact formulation; **E** a prior standard
result; **F** a statement that cannot be identified from the surviving words
and context. A false literal assertion may coexist with a published repaired
theorem. A named SGA exposition by another author is classB when it supplies
the match; the collective SGA label alone does not justify classA.

The six canonical page statuses describe the supplied pages. Additional
`status_detail` and occurrence records preserve such facts as a cancelled
proof, an earlier wrong formula, a corrected theorem with a stale proof line,
or a conditional false reading. Where a canonical claim has both an earlier
unproved occurrence and a later supplied proof sketch, the latter controls
its single summary status; both documentary statuses remain visible.

## 2. Groups, torsors and the approach to abelian schemes

### Cotes45–46: infinitesimal and relative structure

The distribution calculations in c45 use the augmentation filtration and
duality of finite locally free quotients. They belong to the Hopf-algebra and
formal-group framework; they are not another construction of the Poincaré
Fourier transform. The finite-projectivity conditions matter whenever a dual
is moved across a tensor product or an inverse/filtered limit. The proposed
recovery of global integral functions from identity distributions still needs
the manuscript's exact connectedness and separated-completion conventions.
The opened formal-group comparison does not make a global descent statement
automatic. [CL-SA18-45001–45006; MP-SA18-45001; [AG45-SGA3VIIA](SA18_reference_index.md#ag45-sga3viia),
[AG45-SGA3VIIB](SA18_reference_index.md#ag45-sga3viib).]

The semisimple-group and Borel discussions have exact later matches.
For a reductive group over an affine base, SGA3 XXVI Corollary 2.3 gives
H¹(S,L)≅H¹(S,P) for a parabolic P and a Levi subgroup L; a split-torus
hypothesis is unnecessary. Over a semilocal base, Corollary 5.2 gives
G(S)→(G/P)(S) surjective, and 5.5(iv) treats simultaneous parabolic–Levi
conjugacy. Corollaries 5.9–5.10 give Zariski-local triviality and the
twisted-fibre argument for H¹(S,B)→H¹(S,G) to be injective. Its image
consists of torsors admitting the specified Borel reduction, not necessarily
all G-torsors. These results are in Demazure's exposition and are classified
accordingly. A separate torus formula requires a different distinction:
over a connected base, endomorphisms of a split rank-r torus form Mat_r(Z),
whereas automorphisms form GL_r(Z). [CL-SA18-45027, CL-SA18-45029,
CL-SA18-45033, CL-SA18-45036; [AG45-SGA3XXVI](SA18_reference_index.md#ag45-sga3xxvi); [AG45-SGA3VIII](SA18_reference_index.md#ag45-sga3viii).]

C46 begins with a descent construction for rigidified torsors. For a right
G-torsor with endomorphism-compatible structure, changing a trivialization by
u gives the noncommutative equation b=uaf(u)⁻¹. The displayed simplification
on the page is false for a general noncommutative G; an S₃ example with f=id
checks the failure. Once the coordinate equation is corrected and the Lang
map is locally surjective, the objects are described by torsors under
Eq(f,id). The differential and open-orbit argument for the zero-differential
Lang lemma is separate from finiteness of the fixed subgroup. Infinite
constant groups show why étale alone does not imply finite.
[CL-SA18-46001–46005; parts/agent46/proofs.md §§1–2;
[Lang1956](SA18_reference_index.md#lang1956); [Stacks025F](SA18_reference_index.md#stacks025f).]

The same pages lead through Frobenius-fixed modules to local systems,
height-one groups and logarithmic differentials. A finitely presented
module M over a characteristic-p ring with F* M≅M is locally free, by the
Fitting-ideal argument; finite
generation alone has a perfect-valuation-ring counterexample. The supplied
Codex continuation also changes earlier judgments of incompleteness. The
Verschiebung construction now reads continuously across scans 24–27, and
the divisor-space question at scan 41 is developed at scans 58–60. The
revised records retain the questions and their actual continuations together.
[SA18-46015, SA18-46029, SA18-46035; CL-SA18-46007,
CL-SA18-46026–46028, CL-SA18-46057–46060; [Stacks07Z6](SA18_reference_index.md#stacks07z6);
parts/agent46/proofs.md §3; SA18_links.tsv.]

### Semilocal H¹: three assumptions that cannot be dropped

The c46 argument repeatedly moves among finite algebras, their invariant base,
and their residue algebras. The audit separates three failures. First, after
algebra finiteness is cancelled, a norm-one cocycle need not be a coboundary:
the Laurent-polynomial example with conjugation and t↦t⁻¹ has a parity
obstruction. Second, an action trivial on the residue field need not allow
invariant lifts; the dual-number derivation example exhibits the failure.
Third, invariants of a noetherian ring under a finite group need not be
noetherian without an additional hypothesis. [CL-SA18-46081–46086;
MP-SA18-46022–46024; parts/agent46/proofs.md §§21–23.]

For the third point there is an explicit zero-dimensional construction.
Let k=F_p(t₀,t₁,…) and let D(t_i)=t_(i+1). On the Artinian ring
k[ε]/(ε²), the order-p automorphism sends a+bε to a+(b+D(a))ε.
Its invariant ring is k^p⊕kε. The square-zero ideal kε is not finitely
generated over k^p because [k:k^p] is infinite. The source ring is nevertheless
Artinian and noetherian. The proof checks kerD=k^p by the largest variable
appearing in a rational function. Giokas–Singh's opened Theorem2.1 supplies a
separate published regular-local example. Their paper was received in 2022,
online in 2023 and printed in 2024; those dates are not conflated.
[CL-SA18-46083; parts/agent46/proofs.md §22;
[GiokasSingh2024](SA18_reference_index.md#giokassingh2024), Theorem 2.1.]

These examples delimit the repair of the manuscript theorem. The
noncommutative Hilbert 90 theorem for finite-dimensional algebras over a
field remains valid, including the finite-field case. Milne's *Algebraic
Groups*, Example 3.42(a), p. 78, gives that exact result; Lemma 3.44, p. 79,
gives the restriction-of-scalars H¹ comparison for smooth groups and finite
field extensions. [CL-SA18-46070, CL-SA18-46074;
[MilneAG2017](SA18_reference_index.md#milneag2017); MP-SA18-46018–46019, MP-SA18-46022.]

## 3. Fourier convolution and cohomological duality

### Cote47: the theorem and the unfinished chosen map

For an abelian scheme A/S of relative dimension g with normalized Poincaré
kernel, the relative double transform includes inversion, the base line
τ_A=detLie(A/S), and the shift[−g]. The manuscript corrects the theorem toward
antidiagonal support, but an obsolete identity target survives in the proof
and the earlier K₀ line omits the determinant factor. Mukai's Theorem2.2 is
the field comparison; Laumon's Theorem1.2.4 and Lemma1.2.5 give the relative
formulation with the line and shift. Mukai's recorded receipt date is
9October1979 and publication1981; Laumon's arXiv submission is5March1996.
[CL-SA18-16044, CL-SA18-16046–16049; [Mukai1981](SA18_reference_index.md#mukai1981); [Laumon1996](SA18_reference_index.md#laumon1996).]

The repeated unit-fibre notes concern one outstanding source obligation.
Writing e for the regular zero section and T for its rank-g normal bundle,
a Koszul calculation identifies the expected cohomology sheaves, for0≤i≤g:

\[
H^i(Le^*e_*\det(T)[-g])
\simeq \bigwedge^{g-i}T^\vee\otimes\det(T)
\simeq \bigwedge^iT.
\]

This calculation does not by itself show that the **particular comparison
morphism chosen in the manuscript** induces those isomorphisms. The opened
Laumon passage states the exact kernel theorem and recalls its construction;
it does not write out the manuscript's requested unit-fibre check. Items45002,
45003 and46003 therefore merge into16050 as occurrences of the same obligation.
A focused future task can complete that map-and-convention audit without
claiming new Fourier inversion. [CL-SA18-16050–16052; MP-SA18-16008.]

For an ample line bundle L over a field, let r=χ(L)>0, let E be its transformed
vector bundle and put D′=−c₁(E). Pullback along φ_L identifies E with a direct
sum of r copies of L⁻¹. In rational Chow groups this gives

\[
c_2(E)=\frac{r-1}{2r}D'^2,
\qquad
c_3(E)=-\frac{(r-1)(r-2)}{6r^2}D'^3.
\]

The literal expansion has an extra factor r. A product of elliptic curves
with polarization degrees1 and2 supplies a counterexample under the ample
field hypotheses. The weaker final integral-cycle coefficient is nevertheless
r(−1)^k c_k(E), so it survives separately. Translation signs also matter:
with T_t(b)=b+t, the transform of the corresponding degree-zero line is
supported at−t. [CL-SA18-16053–16055, CL-SA18-16057;
[Mukai1981](SA18_reference_index.md#mukai1981), Proposition3.11; parts/agent16/source_review.md.]

The GRR calculation keeps ordinary multiplication separate from Pontryagin
convolution. The complementary relative identity has the full base factor
T_A T_B ch(ω_A); its simplification uses the de Rham Todd-class result under
the stated Chow-theoretic hypotheses. Interpreting the literal unstarred
formula as ordinary multiplication is false already on an elliptic curve.
[CL-SA18-16059–16061; [Moonen2026](SA18_reference_index.md#moonen2026), §§2.4–2.7;
parts/agent16/outputs/status_certificates.json.]

Integral Fourier theorems have stricter boundaries. Beckmann–deGaayFortman
Theorem3.8 relates the integral-transform conditions to minimal-cycle data;
the principally polarized formulation retains a genuine symmetric ample
principal line bundle. Their Question3.9 is not replaced by rational inversion.
[CL-SA18-16058; MP-SA18-16010; [BF2023](SA18_reference_index.md#bf2023), Theorem3.8 and Question3.9.]

The2025 localized theorem assumes an abelian scheme of relative dimension
g>0 over a connected smooth quasi-projective base of dimension d over a field
and one of§3.2's alternatives: characteristic0,
a lift of the abelian scheme and base through a mixed-characteristic DVR,
or base change from such a liftable case. Its Fourier identities and Beauville
decomposition use coefficients Z[1/(2g+d+1)!]. The sl₂ refinement additionally
inverts ν(θ) for the chosen polarization θ, where degθ=ν(θ)². Thus it is a precise localization theorem,
not full integrality over Z. [[HHLLMM2025](SA18_reference_index.md#hhllmm2025), §3.2, Theorems5.5 and7.3;
CL-SA18-16058; MP-SA18-16010.]

### Cote54: what A[p] determines

The c54 sequence connects universal vector extensions, de Rham cohomology,
Cartier duality and restricted Lie structure. Variance matters: for dual
abelian varieties A and B, the tangent space of the universal vector extension
of A is identified with H¹_dR(B). The source still defers the degree-one
duality compatibility. [CL-SA18-16065–16066; [Coleman1998](SA18_reference_index.md#coleman1998); [Oda1969](SA18_reference_index.md#oda1969).]

The final question uses the **entire finite group scheme A[p]**, not merely
its geometric points, Lie algebra or underlying vector space. Over a perfect
field of characteristic p, Oda's functorial contravariant Dieudonné comparison
recovers H¹_dR(A), its F,V operators and Hodge filtration. Corollary5.11 is the
exact later match. Oda's thesis was completed in June1967; the journal paper
appeared in1969. [CL-SA18-16067–16069; [Oda1969](SA18_reference_index.md#oda1969), Corollary5.11.]

Corollary5.12 instead concerns X proper and smooth over a perfect field with
X(k) nonempty, and the specified iterated-Cartier-stable subspace associated
to Picard[p]. It does not identify all of H¹_dR(X) with arbitrary Picard data.
The c46 Picard[p], dlog and elliptic-diagnostic comparison therefore remains
separate; only the entry repeating the abelian A[p] question merges into16069.
[SA18-46030; CL-SA18-46019–46025; MP-SA18-46004–46006;
[Oda1969](SA18_reference_index.md#oda1969), Corollary5.12.]

## 4. Picard, reduction and Torelli: cotes48–52

These folders move from plans and foundational proof fragments to the
relative geometry of abelian schemes and curves. C48 contains an EGA plan
and an actual fibre-functor argument matching SGA4 VIII 7.8–7.9. The category
of geometric points with specialization arrows is equivalent to the
category of points of the étale topos, opposite to the fibre-functor
category. The comparison of the two Hom bijections leaves compatibility
to the reader in both the supplied fragment and the published sketch.
That source-level obligation now has its own problem record.
[CL-SA18-45133–45135; MP-SA18-45061; [AG45-SGA4VIII](SA18_reference_index.md#ag45-sga4viii), 7.9(a).]

For an arbitrary abelian scheme, the dual Pic⁰ is an abelian scheme and
coherent cohomology satisfies the exterior-algebra and base-change
statements. These results do not imply local projectivity over every base:
nonprojective abelian schemes occur even over dual numbers in characteristic
zero. Lan's Theorem 1.3.2.3 and Proposition 2.1.5.14 give the exact positive
statements, and Kleiman's Remark 5.24 supplies the projectivity boundary.
The relative Hom assertion is different: Bertolin's Proposition 1.3.1 gives
representability, separatedness, unramifiedness and essential properness,
without saying that the entire Hom scheme is finite or proper.
[CL-SA18-45136, CL-SA18-45139–45140, CL-SA18-45177;
MP-SA18-45038, MP-SA18-45045; [AG45-Lan2008](SA18_reference_index.md#ag45-lan2008); [AG45-Kleiman2005](SA18_reference_index.md#ag45-kleiman2005);
[AG45-Bertolin2009](SA18_reference_index.md#ag45-bertolin2009).]

Several small assertions around Lang's book become false when an omitted
qualification is made universal. An isogeny φ_L does not imply that L is
ample: an antiample line bundle already separates nondegeneracy from
positivity. The i-th characteristic coefficient is homogeneous of degree i,
not2i. A Rosati involution attached to a nonprincipal polarization naturally
acts on End⁰(A), and need not preserve End(A). An empty closed flat subscheme
can be stable under multiplication and inversion without being a subgroup:
the identity requirement is indispensable. [CL-SA18-45141,
CL-SA18-45154, CL-SA18-45158, CL-SA18-45166.]

The Hilbert-scheme assertion about all subgroup schemes also needs a
characteristic-p boundary. Lines of α_p-subgroups in a suitable superspecial
abelian surface vary in a projective line; thus the broad subgroup locus is
not unramified merely because homomorphisms of abelian schemes have rigidity.
This distinguishes a moduli problem for finite subgroup schemes from one
for abelian subschemes. For a proper group of finite type over a
characteristic-zero field, the connected identity component is an abelian
variety. The proposed relative “greatest abelian subscheme” over a reduced
base requires additional control of flatness and fibre dimension; those
hypotheses are not supplied by properness alone.
[CL-SA18-45174, CL-SA18-45206; MP-SA18-45044; [AG45-SGA3VIB](SA18_reference_index.md#ag45-sga3vib).]

### Two different purity questions

One question fixes an abelian scheme over the whole regular base and asks
whether its torsors extend across a subset of codimension at least two.
The opened Bouthier–Česnavičius–Scavia text, §4.2 and(4.2.0.1), supplies the
relevant result. Another question asks whether an abelian scheme initially
defined only on the open subset extends as a group model. The latter has
mixed-characteristic restrictions and counterexamples addressed by
Vasiu–Zink. These questions must not be merged simply because both are called
purity. [CL-SA18-45185–45187; MP-SA18-45052–45053;
[AG45-BCS2025](SA18_reference_index.md#ag45-bcs2025); [AG45-VasiuZink2010](SA18_reference_index.md#ag45-vasiuzink2010).]

Completion invariance has a similarly precise positive scope. Milne's
*Arithmetic Duality Theorems*, I Remark 3.10(a), proves H¹(K,A)≅H¹(K̂,A)
for an abelian variety over the fraction field of an excellent henselian
DVR with finite residue field. If A extends as an abelian scheme, H¹(R,A)=0
by Lang's theorem and henselian lifting, so the indicated local obstruction
quotient is invariant in this setting. The unrestricted DVR wording on the
page is not established by that comparator. The remaining p-primary kernel
questions in the relative Picard discussion are retained separately from
prime-to-p or smooth cases. [CL-SA18-45180–45183, CL-SA18-45204;
MP-SA18-45047–45050, MP-SA18-45060; [AG45-MilneADT](SA18_reference_index.md#ag45-milneadt).]

### Cote52: differential and infinitesimal Torelli

The source follows the duality between the differential of Torelli and
multiplication of canonical forms. The compatibility map itself deserves a
check; knowing the dimensions of its source and target is not that check.
For a smooth hyperelliptic curve of genus g≥2 over an algebraically closed
field of characteristic different from two, the cokernel of the canonical
multiplication map has dimension g−2. This corrects the dimension-one
assertion in the supplied transcription.
[CL-SA18-45195–45198; MP-SA18-45056; [AG45-Ricolfi2020](SA18_reference_index.md#ag45-ricolfi2020).]

The infinitesimal fibre is not uniformly a single dual-number direction.
For the Torelli morphism of moduli stacks in this setting, the precise
hyperelliptic fibre has local algebra

\[
k[s_1,\ldots,s_{g-2}]/(s_1,\ldots,s_{g-2})^2.
\]

It is reduced in genus 2 and is the dual-number fibre in genus 3. Ricolfi's
Theorem 3.6 and §3.2 identify this factor and the marked-fibre interpretation;
it is not a claim about the fibre of the coarse-moduli Torelli map.
Consequently, the dossier keeps both the historical nilpotent-fibre question
and its exact modern answer. The good-reduction discussion is bounded by
the distinction between smooth reduction of a curve and compact-type
recovery from its Jacobian; an overly strong absolute-simplicity equivalence
in a later draft is not used as a theorem. [CL-SA18-45199–45203;
MP-SA18-45057–45059; [AG45-Ricolfi2020](SA18_reference_index.md#ag45-ricolfi2020); [AG45-Robert2023](SA18_reference_index.md#ag45-robert2023).]

## 5. General groups, coalgebras and module schemes: cote53

The notebook's generality is a mathematical feature, not a nuisance to be
removed by default finite-type assumptions. Its component, image and quotient
statements must retain the distinctions among connectedness, irreducibility,
geometric reducedness, quasi-compactness, quasi-separatedness and finite
presentation. Over an imperfect field, a reduced finite-type group scheme
need not be geometrically reduced; the explicit characteristic-p equation in
the proof audit verifies the boundary. A qcqs result on component spaces does
not settle a source sentence that states only quasi-compactness.
[CL-SA18-46092–46112; MP-SA18-46026–46032; [SGA3VI_A](SA18_reference_index.md#sga3vi_a);
[StacksGroupSmooth](SA18_reference_index.md#stacksgroupsmooth); [Tarizadeh2026](SA18_reference_index.md#tarizadeh2026).]

The monoid sequence contains an explicit internal correction. A letter
provides the {0,1} monoid with an absorbing idempotent as a counterexample to
the proposed GL_n embedding. The rectification appears at scan 22, and the
corrected M_n construction is proved at scan 31. The original assertion is
therefore recorded as corrected by the author. The further statement about
finitely presented cancellative monoid schemes over arbitrary bases has
different quantifiers. Brion's opened criterion applies to reduced separated
finite-type monoids over an algebraically closed field; the nonreduced and
arbitrary-base formulations remain a separate scope question.
[CL-SA18-46117–46120; MP-SA18-46034–46035;
[Brion2014](SA18_reference_index.md#brion2014), conventions on p. 3 and Proposition 3(iii).]

The comodule and coefficient-algebra calculations are largely checkable by
coassociativity, counits, dual bases and finite generation of the relevant
coefficient spaces. The arbitrary-intersection assertion is the exception
that should not be declared false by an irrelevant tensor example. Flatness
preserves finite intersections in the appropriate setting; arbitrary
intersections require a stronger condition in the general module theorem.
Wisbauer's Theorem 7.12 and Datta–Epstein–Tucker's 2026 Theorem 4.3.1 locate
the exact boundary. Whether the **coalgebra and comodule hypotheses themselves** supply
the missing strength in the manuscript's claim is the retained question.
The failure of Q⊗_Z− to preserve arbitrary intersections of Z-submodules
alone does not answer it.
[SA18-46066; CL-SA18-46130–46131; MP-SA18-46038;
[WisbauerCoalgebras](SA18_reference_index.md#wisbauercoalgebras); [MittagLeffler2026](SA18_reference_index.md#mittagleffler2026).]

The representability question for W(M)(B)=M⊗_R B can be answered for any
commutative ring R without assuming that a representing scheme is affine.
At the zero section e of a representing scheme X, let Q=e*Ω_(X/R). Maps
Spec(R⊕L)→X restricting to e on Spec R give, naturally and R-linearly in
every R-module L,

\[
\operatorname{Hom}_R(Q,L)\simeq M\otimes_R L.
\]

The right side preserves filtered colimits and epimorphisms. The left side
therefore makes Q finitely presented and projective; evaluating at R gives
M≅Q∨, hence M is finite projective. Conversely, Spec Sym_R(M∨) represents
W(M) for finite projective M. The local affine calculation glues because the square-zero
thickening has the same underlying topological space. This closes the
specific arbitrary-scheme necessity gap. The 2009 paper supplies a
module-scheme theorem; the stronger arbitrary-scheme proof is this run's
reconstruction, kept separate from the source's product argument.
[CL-SA18-46136–46137; MP-SA18-46039;
parts/agent46/proofs.md §32; [ModuleSchemes2009](SA18_reference_index.md#moduleschemes2009), Theorem 1.1;
[Stacks04BU](SA18_reference_index.md#stacks04bu); [Stacks0G8P](SA18_reference_index.md#stacks0g8p).]

## 6. Correspondences, Lefschetz operators and cycles

### The two integral operator models

The c11 correspondence operations have a precise Chow realization: pull
back to the triple product, intersect, then push forward. The source's order
and graded-sign questions require its target-first convention. Diagonal
products additionally involve excess intersection. In the incidence-graph
calculation, cycle ranks give powers of c_top(T_X). In cohomology with a
one-dimensional top degree, c_top(T_X)=χ(X)[point]; that replacement is not a
universal equality of Chow zero-cycles with a chosen point. A full relation
ideal for the diagonal ring remains a separate question from checking the
listed products. [CL-SA18-11002, CL-SA18-11006–11015;
research/root_proofs.md R1–R2; [R-Stacks0FG0](SA18_reference_index.md#r-stacks0fg0); [R-Stacks0FG9](SA18_reference_index.md#r-stacks0fg9).]

The associated c16 integral exterior model fails hard Lefschetz as written.
For ξ=Σe_i∧f_i, expansion gives ξⁿ=n!vol. In rank4, multiplication by ξ²
from degree0 to the top degree has cokernel Z/2. This counterexample meets
the written free integral hypotheses, and the second pass confirms that
reading. Raw symplectic contraction also differs from unit-step lowering:
on the first string step it gives n rather than1.
[CL-SA18-16001–16002; parts/agent16/outputs/computations.json.]

The normalized abstract model is valid on its stated terms. Taking one
primitive string of length n−i+1 for each i=0,…,n and fixing the grading
projectors gives the operator algebra

\[
\prod_{i=0}^{n}\operatorname{Mat}_{n-i+1}(\mathbf Z).
\]

The mathematically correct position bound is n−i; the source's written
2n−i remains recorded as an error. The author also answers negatively the
question whether L alone determines the grading; requiring every π_i gives
a different, qualified universal statement. None of this identifies the raw
integral exterior order with the normalized matrix-unit algebra. The exact
integral-order and denominator comparison remains a focused question.
[CL-SA18-16003, CL-SA18-16026, CL-SA18-16027, CL-SA18-16029;
MP-SA18-16001; parts/agent16/outputs/status_certificates.json.]

The later c16:53 induction has a separate error. A source-degree cut does
not make L^(n−k) vanish on every unwanted degree: H*(P²), with n=2 and k=1,
gives LT₁(h)=h². Retaining a target cut repairs this isolation step. Another
inverse-condition display uses the wrong endpoint projector. These repairs
are present reconstructions, and neither proves algebraicity of the needed
inverse operators in general. [CL-SA18-16086, CL-SA18-16120;
MP-SA18-16003.]

### Standard conjectures and the c44 programme

The secure letter dictionary is partial: draft C matches published B, and
draft A matches published A. The remaining letters are not identified by
elimination. The current second pass confirms all π_i in the surface
sentence. The dated retraction and subsequent rational-characteristic-polynomial
repair remain distinct from a universal realization-independence assertion.
[SA18-16024; CL-SA18-16024, CL-SA18-16030, CL-SA18-16034–16035,
CL-SA18-16041; [Groth1969](SA18_reference_index.md#groth1969); [Kleiman1968](SA18_reference_index.md#kleiman1968).]

Jannsen's Theorem1 concerns numerical motives with characteristic-zero
coefficients. His Corollary1 assumes algebraic Künneth components and identifies
the kernel from the **homological correspondence algebra to the numerical
one** as a nilpotent radical; it is not a realization kernel, and nilpotent
does not mean zero. Katz–Messing prove finite-field Künneth algebraicity,
while Deligne proves cohomological hard Lefschetz. None of these supplies a
general algebraic lowering operator. The2025 Lagrangian-fibration results
retain their Ngô-type support and fibration hypotheses. [CL-SA18-16030,
CL-SA18-16038–16040; [Jannsen1992](SA18_reference_index.md#jannsen1992), Theorem1 and Corollary1, pp449–450;
[KatzMessing1974](SA18_reference_index.md#katzmessing1974), Theorem2; [Deligne1980](SA18_reference_index.md#deligne1980), Théorème4.1.1; [ACLS2025](SA18_reference_index.md#acls2025).]

C44's cycle-induced Jacobians lead to uniform dimension bounds, Tate-module
hopes, symmetric correspondences and positivity. Kahn's corrected existence
argument concerns codimension2. The Tate-module comparison cited here has
specified codimensions1,2 or dimX, a torsion-free target, and primes ℓ≠p avoiding
the relevant miniversal-cycle degree. The threefold symmetric-isogeny theorem
and the separate positivity results have further hypotheses, including the
stated lifting conditions. A symmetric isogeny alone is not a polarization.
The general all-codimension programme is therefore not settled by these
comparisons. [CL-SA18-16072–16077; MP-SA18-16014–16017;
[Kahn2021](SA18_reference_index.md#kahn2021), Theorem1; [ACMV2023](SA18_reference_index.md#acmv2023), Proposition8.2;
[ACMV2025](SA18_reference_index.md#acmv2025), Theorem12.12 and §13.]

The symbol τ-equivalence is undefined locally. If it means algebraic
equivalence up to a nonzero multiple, non-torsion Griffiths groups contradict
the proposed equality with numerical equivalence in higher codimension.
That conditional counterexample does not decide the manuscript's undefined
notation or refute its divisor-case precursor. [CL-SA18-16078;
MP-SA18-16018; [Clemens1983](SA18_reference_index.md#clemens1983); [PicardVI1962](SA18_reference_index.md#picardvi1962).]

### Distinct letter witnesses and later reassessment

The CSG edition dated12August1964 explicitly derives from Montpellier cote44
and is another transcription of that witness. Serre's *Motifs*, Annexe1,
reprints a **different letter dated16August1964**; p343 explicitly leaves the
higher-dimensional Hodge–Néron–Tate connection unclear. The8August1964
surface-fibration comparison is another dated letter. The dates identify
separate texts, not interchangeable proof witnesses.
[SA18-46004–46005; [GrothSerre1964CSG](SA18_reference_index.md#grothserre1964csg), provenance PDFp2 and textpp4–5;
[SerreMotifs1991](SA18_reference_index.md#serremotifs1991), Annexe1 pp342–344; [SerreLetter1964](SA18_reference_index.md#serreletter1964), p186.]

The31August1964 letter to Mumford records limited established results and
further hopes. On9August1968 Grothendieck distinguishes the standard
conjectures from the tempting identification of τ-equivalence with numerical
equivalence. On4September he explicitly reassesses the proposed
Hodge–Néron–Tate relationship and accepts a distinction between τ-equivalence
and homological equivalence. These are later correspondence, not a withdrawal
written on the c44 sheet. [SA18-46006–46007;
[GrothMumfordLetters](SA18_reference_index.md#grothmumfordletters), letter24 p89, letter43 p143 and letter44 p145;
[MumfordLetter1964](SA18_reference_index.md#mumfordletter1964).]

## 7. Cotes55–56: analysis, dimension, quadrics and relative tori

### Abstract analytic arguments

The global H¹-only criterion for equivalence between coherent sheaves and modules
over global sections is too weak. Constant C with its finite local systems
on RP² supplies a precise counterexample: the stated H¹ vanishing holds,
but the nontrivial sign local system has no global generator. This example
does not refute the separate neighborhood-basis variant. The repaired
criterion separates full faithfulness on globally presented objects from
generation of every coherent object, coherence of the section ring, and
flatness of stalks. An analytic theorem with stronger geometric hypotheses
does not prove the unqualified abstract lemma. [CL-SA18-11095–11098;
MP-SA18-11033; research/root_proofs.md R9;
[R-Siu1969](SA18_reference_index.md#r-siu1969); [R-BuchweitzFlenner2003](SA18_reference_index.md#r-buchweitzflenner2003); [R-Benoist2026](SA18_reference_index.md#r-benoist2026).]

The abstract LemmaB retains a real proof obligation. Its local uniqueness
hypothesis on sections of coherent integral quotients has not been shown
here to give one neighborhood on which all later members of a chain
stabilize. The analytic comparator is established, but the passage from
stalkwise stabilization to uniform-neighborhood stabilization under exactly
the abstract hypotheses remains unproved. The α-only extension to algebras
also retains its filtered-colimit and polynomial-filtration gap.
[CL-SA18-11101a–11101c, CL-SA18-11102;
MP-SA18-11035–11036.]

The coherent-elimination question has a definite negative answer. Let
A=∏_(n≥1)k[[u,v]]. Uniform bounds on the kernels of finite matrices make A
coherent. With U=(u), V=(v), W=(vⁿ), the two-generated ideal
(U−VT,W) in A[T] has contraction whose n-th coordinate is (u,v)ⁿ.
The required numbers of generators are unbounded, so that contraction is
not finitely generated. The proof is stronger than merely observing that
some polynomial ring over a coherent ring is not coherent. The opened
positive results for monic ideals and special base rings have their own
extra hypotheses. [CL-SA18-11100; MP-SA18-11034;
research/root_proofs.md R11; [R-LSY2012](SA18_reference_index.md#r-lsy2012); [R-Yengui2011](SA18_reference_index.md#r-yengui2011).]

The literal complex-torus lattice on c55 splits in the way the following
argument says it should not. A separate reconstructed lattice gives a
nonalgebraic extension of elliptic tori and matches Oort–Zarhin's exact
extension parameter criterion and Rosen–Shnidman's Proposition2.3. That
successful alternative is not evidence for changing the fourth generator
in the transcription. The next scan review must decide the ink.
[CL-SA18-11110a–11110b; MP-SA18-11039;
[R-OortZarhin1996](SA18_reference_index.md#r-oortzarhin1996), §3.1/Lemma3.2; [R-RosenShnidman2017](SA18_reference_index.md#r-rosenshnidman2017), §2.3.]

### Dimension and the EGA matches

The dimension notes mix local-ring dimension, dimensions of neighborhoods,
codimension and residue transcendence degree. These have been separated
before matching the statements to EGA. The associated-point and reduced-module
passages belong to EGA IV.2, §§3.1–3.2; the flat local dimension equality is
IV.2,6.1.2. The unfinished reduced-module definition is identified by3.2.2
and3.2.3, but the published missing clause is explicitly a reconstruction.
The direct-sum associated-points formula and the union-of-subsheaves formula
are neighboring, different clauses of3.1.7. [CL-SA18-11103a–11111;
[R-EGAIV2](SA18_reference_index.md#r-egaiv2); [R-Stacks00ON](SA18_reference_index.md#r-stacks00on); [R-Stacks07NB](SA18_reference_index.md#r-stacks07nb).]

The defective biequidimensionality implication in EGA0IV14.3.3 deserves
special treatment because a later printed occurrence does not make the
statement true. The semilocal counterexample in the proof audit checks
equidimensionality and maximal-point heights while exhibiting saturated
chains of different lengths. The componentwise equicodimensional repair is
kept separate. The source's generic-point map SpecK→SpecDVR is also
distinguished from the published EGA5.4.3 example that adds the closed point
to obtain a bijection. [CL-SA18-11105c, CL-SA18-11109a;
MP-SA18-11038; [R-EGAIV1](SA18_reference_index.md#r-egaiv1); [R-EGAIV2](SA18_reference_index.md#r-egaiv2);
[R-PilloniStroh2014](SA18_reference_index.md#r-pillonistroh2014); research/root_proofs.md R10.]

### Quadrics, cones and vanishing cycles

The quadric calculations have been redone integrally, with ordinary,
compactly supported and supported cohomology kept apart. The two middle
rulings, their parity-dependent self-intersection and the index-two change
of basis are essential. Punctured cones can have genuine 2-torsion; reduction
modulo2 must include universal-coefficient Tor terms. The n=0 and low-dimensional
endpoints cannot be absorbed into a uniform formula without checking them.
[CL-SA18-11037–11050; research/root_proofs.md R4–R5;
[R-SGA7XII](SA18_reference_index.md#r-sga7xii),3.3/3.7; [R-SGA7XV](SA18_reference_index.md#r-sga7xv),2.1/2.2.]

For the affine quadric, the tangent-bundle model gives the parity-dependent
Euler map. A weakly specified degeneration does not force nontrivial
quadratic monodromy: the base change t=s² shows the missing hypothesis.
The unfinished purity phrase remains classF where the actual assertion
cannot be recovered, instead of being replaced by a remembered theorem
about a similar local model. [CL-SA18-11046–11047;
MP-SA18-11011–11021.]

### Relative tori and centres

The torus and centre draft has exact later destinations in SGA3 XII and XIV,
including the G_m/G_a specialization example and the distinction between
artinian-base existence and the relative reductive case. XIV3.20 and3.21(c)
give the relevant Zariski-local maximal-torus statements. A prescribed
special-fibre torus has a different lifting question; an infinite-residue-field
qualification from one clause is not copied into every clause.
[CL-SA18-11058–11077, CL-SA18-11093;
[R-SGA3XII](SA18_reference_index.md#r-sga3xii), Remark1.6; [R-SGA3XIV](SA18_reference_index.md#r-sga3xiv),1.4,3.20–3.21.]

The broad nested-torus Weyl-group lemma fails without maximality. In SL₄,
the explicitly saturated rank-two cocharacter lattice used in the audit
contains a regular rank-one subtorus whose Weyl group has an extra involution;
the larger torus has trivial Weyl group. The hypotheses of the broad written
statement are met. The published XII2.3 proof uses maximality, yielding the
repaired statement. This is an exact correction target, not a failure of
maximal-torus Weyl theory. [CL-SA18-11064; MP-SA18-11025;
research/root_proofs.md R6; [R-SGA3XII](SA18_reference_index.md#r-sga3xii).]

## 8. Quadratic invariants across the1961 letter and1962 offprint

The cross-folder identity is particularly strong here. The c45 letter and
Delzant's c56 offprint both use the rank-retaining Grothendieck–Witt ring,
generated by one-dimensional forms with binary relations. They do not use
the rank-forgetting Witt quotient interchangeably. The presentation and the
binary-isometry criterion were split into atomic claims before being merged
across the two witnesses. Delzant remains the author of the offprint, and
the manuscript's broader general-ring conventions are not supplied by
Delzant's field definition. [SA18-45045; CL-SA18-11078,
CL-SA18-45117–45118; [R-Delzant1962](SA18_reference_index.md#r-delzant1962); [AG45-EKM2008](SA18_reference_index.md#ag45-ekm2008), §§2–4.]

For a field F of characteristic different from two, let J be the kernel of
rank on GW(F), and I the fundamental ideal of W(F). The degree-two
injectivity question is now settled exactly. The route is

\[
J^2/J^3\simeq I^2/I^3\simeq K_2^M(F)/2
\xrightarrow{\sim}H^2(F,\mathbf Z/2),
\qquad \operatorname{char}F\ne2.
\]

The identification of the two filtrations, Milnor's degree-two graded
comparison, and the norm-residue theorem are three distinct ingredients.
Milnor's degree-two result and Merkurjev's theorem jointly
answer the question; an appeal to Merkurjev without identifying the source
map would omit a step. The chronology records the22July1961 letter,
Delzant's1962 offprint, Milnor1970 and Merkurjev1981, with separately opened
modern exact formulations and no invented prepublication date.
[CL-SA18-45121; MP-SA18-45021; [R-Milnor1970](SA18_reference_index.md#r-milnor1970), Theorem4.1;
[AG45-EKM2008](SA18_reference_index.md#ag45-ekm2008), Proposition5.3 and Theorem44.1;
[R-Merkurjev2006](SA18_reference_index.md#r-merkurjev2006); [AG45-Zibrowius2018](SA18_reference_index.md#ag45-zibrowius2018), Proposition 4.1 and Remark 4.2.]

Two tempting stronger identifications are not made. On Jⁿ in GW(F), the
first possible positive degree of the ordinary Stiefel–Whitney class is
2^(n−1); ordinary w_n is therefore not generally the nth Milnor invariant
under the graded comparison with Iⁿ/Iⁿ⁺¹. Nor is a raw ungraded Clifford
Brauer difference equal to w₂ in every rank: the rank-four real example
contradicts that interpretation. This does not decide the assertion under
Delzant's potentially properly normalized intended descent construction.
That normalization has not been identified from the supplied text, and the
Springer passage remains unopened. [CL-SA18-11082, CL-SA18-45120;
MP-SA18-11032; [AG45-EKM2008](SA18_reference_index.md#ag45-ekm2008), Lemma 5.6 and Corollary 5.9;
[R-Springer1959](SA18_reference_index.md#r-springer1959), explicitly unverified.]

The total-class construction is also a partial, rather than total, merge.
The offprint specifies Grothendieck's1958 Chern-class ring law on its target.
The letter's wider universal target is not fully defined. Similarly, Serre's
pro-two suggestion must distinguish the standard maximal pro-2 Galois
extension from a literal union of all extensions of two-power degree.
The opened pro-2 result says that the standard quotient does not provide
finer mod2 cohomology in the suggested way; the ambiguous extension closure
remains a textual and mathematical task. [CL-SA18-11081,
CL-SA18-45122–45124; MP-SA18-45027;
[R-GrothChern1958](SA18_reference_index.md#r-grothchern1958); [AG45-MPQT2021](SA18_reference_index.md#ag45-mpqt2021), Remark 1.4.]

## 9. What the earlier notes got right, and what changed

The strongest earlier notes isolated actual question marks and deferred maps:
Fourier unit-fibre compatibility, reconstruction from A[p], local Brauer
pairing compatibility, degree-two quadratic invariants, cycle-induced
Jacobian positivity, and the abstract analytic criteria. They also kept many
integral/rational and Grothendieck–Witt/Witt distinctions visible. The dossier
preserves that work while merging repeated questions and retaining separate
historical occurrences. [CL-SA18-16050, CL-SA18-16069, CL-SA18-45121;
MP-SA18-16007, MP-SA18-16016, MP-SA18-11033–11036.]

The principal corrections fall into five groups.

1. **Reading beyond the cited leaf.** Verschiebung and divisor-space proofs
   occur in attached continuations; the c53 monoid assertion is expressly
   rectified. A cancelled proof does not automatically withdraw its theorem,
   and a question can be answered later within the supplied corpus.
   [SA18-46029, SA18-46035, SA18-46064.]
2. **Matching hypotheses.** Perfect fields, finite presentation, finite
   algebras, equicharacteristic coefficient fields, maximality, nonprincipal
   polarizations and mixed-characteristic bases can change the answer. The
   records give the exact theorem scope, including unresolved antecedents.
   [CL-SA18-16011, CL-SA18-16069, CL-SA18-11064; MP-SA18-46022.]
3. **Separating statements from maps.** An isomorphism between expected
   objects does not verify the chosen map. A modern theorem can establish
   the mathematical result while leaving a particular source-level
   naturality or sign calculation unwritten. [CL-SA18-16050, CL-SA18-16066.]
4. **Correcting computations without overcorrecting conclusions.** The
   factorial exterior obstruction, Chern coefficients, quadric degrees,
   hyperelliptic tangent directions and semilocal invariant examples affect
   particular assertions. Nearby weaker conclusions have separate checks.
   [CL-SA18-16001, CL-SA18-16055, CL-SA18-46083;
   MP-SA18-11020, MP-SA18-45056–45057.]
5. **Restoring authorship and documentary scope.** The Delzant offprint and
   Karoubi definitions leaf retain their named authors. Other reused
   expositions retain their own attributions or an explicit authorship limit;
   physical inclusion does not make them one Grothendieck manuscript.
   Earlier-run constructions and project ideas remain labelled separately.
   [CL-SA18-11078, CL-SA18-16107; [R-Delzant1962](SA18_reference_index.md#r-delzant1962); [Karoubi1966](SA18_reference_index.md#karoubi1966).]

The local Brauer example shows how a published account can retain a gap.
[BrauerIII](SA18_reference_index.md#braueriii)§8.4 identifies the local Néron–Severi/discriminant group for a
complete normal local surface with algebraically closed residue field, a
coefficient field k⊂A and the specified resolution of its punctured spectrum.
Remark8.5 expressly leaves compatibility of the pairings unchecked. The
inverse-matrix discriminant pairing and its invariance under point blowup
have been rechecked here; they do not alone identify the exact étale
cohomological pairing. No exact later proof matching these conventions was
located in the recorded searches. [CL-SA18-16004–16005,
CL-SA18-16011–16012; MP-SA18-16007; [BrauerIII](SA18_reference_index.md#braueriii), §8.4 and Remark8.5.]

The topological Brauer questions have different answers at different
quantifiers. Variable-degree torsion realization for finite CW complexes
does not imply realization in a prescribed degree: Antieau–Williams give a
finite six-dimensional CW complex with period 2 and index 8. Nor does the
finite-CW result extend to every infinite CW complex: Hornbostel–Schröer
prove Br(K(Z/n,2))=0 for n>1. The question about group multipliers is separate;
an order-two multiplier on an infinite direct sum of elementary abelian
2-groups can force projective-representation dimensions divisible by 2^m
for every m, so no finite dimension suffices. These precise negative
answers are recorded without conflating fixed degree, arbitrary degree,
topological spaces and abstract groups. [CL-SA18-46065–46068;
MP-SA18-46014–46017; [BrauerI1966](SA18_reference_index.md#braueri1966), §1.3;
[HornbostelSchroer2015](SA18_reference_index.md#hornbostelschroer2015), Theorem 3.1 and §5;
[AntieauWilliams2014](SA18_reference_index.md#antieauwilliams2014), Theorem B; parts/agent46/proofs.md §16.]

## 10. Literature search, links and remaining work

### Search and verification boundaries

`SA18_literature_search.tsv` attaches actual search/open operations and exact
match limits to every claim and problem. Search families include the named
databases, arXiv, Numdam, EGA and SGA, authors' publication lists and primary
papers, with MathOverflow used for leads rather than as a substitute for a
theorem proof. Backward references were followed when a title search did not
locate the exact formulation. Blocked zbMATH requests and inaccessible
historical sources are recorded as such, not counted as successful reads.

The bibliography has 232 key records. A `verified` note
means that the cited link was opened; its scope note says whether the exact
result was read or only metadata was confirmed. An original paper known only
through a later citation remains `unverified`. The dossier makes no claim
to have established the first historical occurrence when the opened sources
only establish receipt, thesis, preprint or publication dates. A2026 status
cutoff is not a universal assertion that no later or unlocated work exists.

`CHECK_EVENTS.tsv` records 2080 events. Source alignment,
targeted proof checking, an independent re-proof, an exact computation,
background use and refutation are different event types. A finite test is
never promoted to a proof of an unbounded statement. The general arguments
are in the proof records; code outputs record the exact cases actually run.
The independent root review checks the principal reconstructions and
counterexamples from a second source owner.

### Links

`SA18_links.tsv` contains 398 checked folder/publication links. Each
entry gives both endpoints or the exact published locator and explains
whether the relation is identity, continuation, correction, partial match
or a bounded comparison. The Fourier/Oda and quadratic-letter/offprint merges
are the strongest cross-package identities. The repeated letter editions
and the c44/c46 chamber material also show why provenance similarity need
not be mathematical duplication.

The 25 links to La Longue Marche, Les Dérivateurs and other
named research runs are kept in `SA18_project_links.tsv`. They are **leads
reported by earlier notes**. Where the corresponding external run or theorem
is not among the supplied files, its endpoint is explicitly unverified;
checking that a note makes the link is not checking the external result.
These leads did not determine the organization or the mathematical verdicts
of this dossier.

### Future tasks

`SA18_directions.md` ranks 47 concrete tasks by mathematical
interest and plausible progress in one session of a few hours. Each names
its source items, claims and problems, its exact known boundary, the result
it would establish and a first step. The high-interest unresolved obligations
include the local Brauer pairing diagram, the two integral Lefschetz orders,
arbitrary comodule intersections under flatness, the chosen Fourier fibre
morphism, and the relative abelian/Picard questions. High-yield editorial
tasks include the corrected Weyl lemma, quadric convention table,
projector induction, Oda dictionary and source-to-publication concordances.

These are task specifications, not results claimed by the present run.
The calculations necessary to evaluate the existing source statements have
been completed; the broader programmes have not been developed under Stage6.

## 11. Final counts

### Corpus and outputs

| Record | Count |
|---|---:|
| Original indexed entries | 335 |
| Canonical items | 341 |
| Supplemental items without an indexed assignment | 56 |
| Canonical claim records | 553 |
| Claims directly sourced without an item association | 114 |
| Problem records | 160 |
| Reading alarms | 240 |
| Folder and publication links | 398 |
| Separate earlier-project leads | 25 |
| Ranked future tasks | 47 |
| Bibliography keys | 232 |
| Opened-link verified references | 217 |
| Unverified references | 15 |
| Check events | 2080 |
| Per-statement literature-search/open associations | 2884 |

### Entry verdicts

| Verdict | Count |
|---|---:|
| kept | 263 |
| merged | 49 |
| corrected | 23 |
| withdrawn | 0 |
| rests on a misreading | 0 |

### Item kinds

| Kind | Count |
|---|---:|
| conjecture | 20 |
| idea of the earlier run | 45 |
| other | 26 |
| reading question | 52 |
| self-flagged step | 49 |
| title, date or page count | 10 |
| unproved claim | 111 |
| unpursued implication | 10 |
| withdrawn in the same text | 18 |

### Claims by literature class

| Class | Count |
|---|---:|
| A — own later publication | 86 |
| B — established development by others | 228 |
| C — partly developed, exact gap retained | 89 |
| D — no exact development identified in the recorded search | 18 |
| E — prior standard result | 104 |
| F — not identifiable from the supplied statement | 28 |

### Claims by status on the pages

| Status | Count |
|---|---:|
| proved there | 100 |
| proof sketched | 163 |
| stated without proof | 100 |
| corrected by himself later | 23 |
| false as stated | 67 |
| open on the pages | 100 |

The counts distinguish note verdicts, item kinds, page statuses and
literature classes. For example, a correct note about an authorial withdrawal
normally receives a **kept** verdict while its item kind is **withdrawn in
the same text**. The absence of a “withdrawn note” verdict therefore does
not mean the manuscript's withdrawals were omitted.

## Deliverable map

The ten requested deliverable groups are at the archive root. Additional
`SA18_aliases.json`, `SA18_counts.json`, `SA18_source_coverage.json`,
`SA18_reference_index.md`, `SA18_project_links.tsv` and
`SA18_literature_search.tsv` make the consolidation auditable. `parts/`
contains the complete source-owner records, `research/` the proof and
integration documentation, `scripts/` the root programs, and `outputs/`
their actual results. The final structural audit is
`outputs/master_audit.json`; the scientific evidence is the cited proof,
source-review and computation record, not the audit program's counts.

Source locators are relative to the original attachment after extraction.
The attachment itself, public-source PDF bodies and earlier checkpoint ZIPs
are not duplicated in this archive. `ARCHIVE_MANIFEST.json` gives the final
file hashes, and `progress.log` records the UTC start, stage events,
scheduled checkpoints and completion.
