# Independent audit: projective three-space concordances and odd joint germs

AI-produced research audit by GPT-6 Astra, OpenAI, 20 November 2026.
Auditor: `/root/singularities_duality`.
Full mathematical/source audit completed at **02:11:36 UTC**.

## Audited source and verdict

Read every line of the 301-line, 15,057-character candidate
`agents/higher_comparison/logs/pending_RP3_equivariant_germ_fibre.tex`.
The audited version has SHA256
`65d269d360f1a6d93d1489b8f54e3e844fb8b41aaef9ca38e9d777d82635652e`.
The full file was read before checkpoint 20 and read again after its release.

**PASS**, including the full relative-family extension, the identity-fibre
identification, the ordinary (O(4)) comparison, and the group structure in
(EG.8). No mathematical correction is required. The literal missing backslash
in `r_t|_Z=operatorname{id}` was reported separately; it is a typesetting error.

This is a structural theorem about a precisely specified simplicial germ
model. It does not compute the remaining odd-germ homotopy group, the kernel
of PL-to-TOP concordance components, or zero-Casson--Sullivan sufficiency.
It is not credited as a reduction of the unresolved original main gate.

## Fresh primary-source verification

1. **Edwards--Kirby**, *Deformations of spaces of imbeddings*, Annals of
   Mathematics 93 (1971), 63--88. Original hosted at
   <https://www.maths.gla.ac.uk/~mpowell/Edwards%20Kirby.pdf>.
   Read definitions on printed pp. 64--65, Theorem 5.1(1) on p. 70, and the
   complete proof and following remark of Corollary 1.2 on p. 79. Theorem
   5.1 supplies a single continuous deformation of an embedding neighborhood,
   fixed at the inclusion and unchanged outside a compact neighborhood of
   the chosen compact set. The proof on p. 79 explicitly makes the ambient
   correction by composing the original local map with the inverse of its
   deformed map and extending by identity, then uses a finite subdivision of
   time. Both original pages 70 and 79 were downloaded, rendered, and
   **visually inspected**, not merely inferred from an OCR search.
   Web sources: `turn101611323view0`, `turn641346909view0`,
   `turn641346909view1`, `turn318634542view0`.
   The author-hosted Berkeley PDF was also opened, but its tool extraction
   had no readable text; the Glasgow copy supplied the actual readable and
   rendered source.

2. **Cerf**, *Groupes d'automorphismes et groupes de difféomorphismes des
   variétés compactes de dimension 3*, BSMF 87 (1959), 319--329,
   DOI 10.24033/bsmf.1528. Original opened at
   <https://www.numdam.org/item/10.24033/bsmf.1528.pdf>.
   Read §1.2 on p. 320: the paper's equivalence means the natural inclusion
   induces a component bijection and all based homotopy isomorphisms.
   Read §3.2 on p. 326: these are ordinary (C^0) homeomorphism and
   (C^\infty) diffeomorphism groups, with the stated boundary convention.
   Read Theorems 4 and 5 on p. 327 and Corollary 1 with its proof on p. 328.
   Theorem 4 imports the then-announced Smale assertion; that premise must
   be, and is, discharged by its later proof. For the closed manifold
   (\mathbb{RP}^3), the boundary condition is empty. No block comparison
   is substituted. Source: `turn479327092view0`, `turn643514958view0`.
   These pages were read as original full text. The web screenshots returned
   only display markers, so no fresh Cerf screenshot-inspection claim is made.

3. **Bamler--Kleiner**, *Ricci flow and contractibility of spaces of metrics*,
   arXiv:1909.08710v1, 18 September 2019, Theorem 1.3, printed p. 2:
   <https://arxiv.org/pdf/1909.08710>.
   Freshly opened and read before this audit. It covers every isometric
   round spherical quotient, including (\mathbb{RP}^3). Its p. 3 explicitly
   distinguishes the older result excluding projective three-space. The
   actual ordinary diffeomorphism-group topology is specified on p. 2.
   Source: `turn475829424view1`. Thus neither the nonequivariant sphere
   theorem alone nor the older exclusion is silently used.

4. **Boyle--Chen--Conway**, *Involutions on (S^4)*,
   arXiv:2512.22724v1, Theorem 2.3, printed p. 6, and Theorem 1.4,
   printed p. 15:
   <https://arxiv.org/pdf/2512.22724>.
   Opened and read this interval, sources `turn416261458view0/1`.
   Its free, end-preserving involution theorem is used only to extend an
   individual germ. It does not supply a parameter-family theorem.

5. **Kwasik--Schultz**, *On s-cobordisms of metacyclic prism manifolds*,
   Inventiones 97 (1989), 523--552, Theorem 2.1, printed p. 530,
   and proof pp. 530--532. The original author-uploaded full text was freshly
   opened at
   <https://www.academia.edu/9803950/On_s_cobordisms_of_metacyclic_prism_manifolds>,
   source `turn599931568view0`. It concerns TOP products; no PL marking or
   isotopy uniqueness is imported. This check corroborates the exact input
   cited in Boyle--Chen--Conway and does not strengthen its scope.

## Complete proof audit

### Joint germs and one normalized local operator

The definition uses a germ along the entire compact zero section of a
parameter simplex. Equality is joint neighborhood equality. Consequently a
finite collection of representatives or equality conditions admits a common
smaller ball. This is the correct convention for the horn proof; pointwise
germ equality would not justify that step. Composition, inverse, face
restriction, and degeneracy pullback respect this definition.

The quotient of the punctured odd ball is the ordinary manifold

\[
 (\operatorname{int}D^4\setminus\{0\})/\{\pm1\}
 \cong\mathbb{RP}^3\times(0,1).
\]

Edwards--Kirby therefore applies without an equivariant extension theorem.
The chosen compact collar lies in the interior of a larger compact annulus.
The deformation is fixed near the latter's boundary. Its image equals the
original image: the interior remains the same component of the complement
of the fixed boundary throughout the embedding deformation. Thus the formula
\(\bar f\,\varphi(\bar f,t)^{-1}\), extended by identity, is defined on the
claimed common image and is an ambient isotopy. After restricting the input
neighborhood, its support stays in one fixed compact annulus.

Lifting from the identity gives odd ambient maps, identity near both omitted
ends. On the connected collar the lifted map and the prescribed odd local
map differ by a constant deck transformation. Closeness at one point fixes
the identity choice uniformly in the normalized neighborhood. This is not
an arbitrary selection of a lift.

Pasting the given germ inside the intermediate sphere with the correction
outside is a homeomorphism. Both maps agree on a neighborhood of the joining
sphere, fix zero, and send its inner side to the component containing zero.
This checks global injectivity and surjectivity, in addition to continuity.
Joint evaluation continuity and the compact homeomorphism-group topology
give the asserted continuous extension operator, normalized at the identity.

### Individual extension and exact horn lifting

For a single odd germ, its small image ball is locally flat and nested in
the ambient ball. The TOP four-dimensional annulus theorem applies. The
inherited involution is free and preserves the two ends. The cited
Boyle--Chen--Conway theorem supplies an equivariant product. A fixed sphere
reparametrization along that product makes its inner parametrization exactly
the given germ. The outer boundary is free, so there is no extra endpoint
condition. This proves vertex surjectivity only.

For a horn, the global prescribed family extends by a strong deformation
retraction of the simplex onto its horn. Dividing the joint germ by that
global family makes the residual map literally identity on one common ball
over the horn. The deformation retraction then gives a family of residual
local maps starting at identity and staying identity on the horn. Compactness
and joint inverse continuity provide fixed source and image balls for all
increments. A single continuous extension operator and one finite diagonal
time mesh suffice; neighborhoods are not chosen separately at parameter
points. Each extension factor is exactly identity on the horn, and successive
factors paste at subdivision endpoints because the operator fixes identity.
The final product has the exact residual germ and the exact prescribed horn
values. Thus the asserted Kan lifting is proved in the stated finite-family
model.

### The strict fibre is the free-top concordance space

A simplex in the identity fibre fixes one common ball. The subgroup fixing
a chosen ball is identified with bottom-fixed, free-top concordances of
\(\mathbb{RP}^3\) by taking the quotient of the outer annulus. Conversely the
covering lift specified to be identity on the inner boundary is unique and
extends over the inner ball. The covering construction is continuous in
compact parameter families.

The radial conjugation expands a smaller fixed ball to the chosen fixed
ball. Its increasing radius map never decreases a radius; hence it preserves
the chosen-ball subgroup whenever the input was already in that subgroup.
For surjectivity on homotopy groups use the common radius of a finite
representative. For injectivity use the common radius of a nullhomotopy and
attach the boundary conjugation track within the fixed-radius subgroup.
This also proves the component assertion and retains the identity basepoint.
No contraction of a merely pointwise-germ kernel is assumed.

### The natural (O(4)) middle map

Boundary restriction has the actual homomorphic radial-cone section.
Its kernel contracts by the odd Alexander formula. This gives the required
weak equivalence of the middle groups, and its map to germs is precisely
the cone-germ map.

Every projective homeomorphism lifts to the sphere and both lifts commute
with the antipodal map. Local covering lifts give double covers of ordinary
homeomorphism groups; likewise for diffeomorphisms and isometries. The diagram
over

\[
 PO(4)\longrightarrow\operatorname{Diff}(\mathbb{RP}^3)
 \longrightarrow\operatorname{Homeo}(\mathbb{RP}^3)
\]

has the same discrete deck fibre throughout. Bamler--Kleiner and Cerf give
weak equivalences of its bases, so the lifted maps are weak equivalences on
all components. The top-left group is literally (O(4)), not an unspecified
space with its homotopy type. Composing with radial coning gives the linear
germ inclusion. Applying singular complexes before taking the simplicial
subgroup is correctly typed.

### The cokernel is a group cokernel

Vertex surjectivity and the middle-group equivalence give surjectivity on
components from (O(4)) to the odd germs. Local orientation separates its
two components, so this component map is bijective. The connecting map from
\(\pi_1|\mathcal G_\iota|\) to the component group of the strict fibre is a
homomorphism for a fibration of simplicial groups. It is surjective because
the following component map is injective. Its kernel is the image of
\(\pi_1O(4)\). Hence (EG.8) is an isomorphism of groups, not just of pointed
sets. In particular the group it describes is abelian. The coset fibration
also gives the claimed loop-space form of the homotopy fibre.

## Separately communicated algebraic corollary

The later proposed split-kernel reformulation was checked algebraically,
but is not part of the hashed 301-line version. Let (j) be the map from
\(\pi_1O(4)\) into the odd-germ group and (f) the forgetful map to the
ordinary joint TOP-four-germ group. Using the already audited A.132 low-degree
input that (f j) is an isomorphism, the homomorphism

\[
 x\longmapsto x-j\bigl((f j)^{-1}f(x)\bigr)
\]

identifies the cokernel of (j) with \(\ker f\). A.142--143 then gives the
proposed exact sequence after dividing by the PL component image. This still
does not evaluate that image or the zero-obstruction quotient. The present
audit does not re-open all of A.132's original low-degree inputs.

## Artifact and source provenance

The downloaded EK original and its two page images are outside the authored
research root, under
`/workspace/scratch/6b22741c5cd2/source_external/singularities_duality/`.
They must not be mistaken for authored deliverables. No original full-text
extract was copied into the authored root. This audit is an authored note.
