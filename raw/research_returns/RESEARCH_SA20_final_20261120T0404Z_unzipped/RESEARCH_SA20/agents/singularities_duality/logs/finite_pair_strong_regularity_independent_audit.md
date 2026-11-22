# Independent full audit of finite-pair contractions and real TOP recognition

Auditor: singularities_duality. Date: 2026-11-20; completed after the observed 03:26:01 UTC clock reading.

Candidate read literally in full:
`agents/maximal_locus/notes/finite_pair_contractions_0310.tex`.
Audited SHA256: `81e740f2cdf1e9974a65f66ebf1f98e4261163a24910f2977b36eb854bcb561e`.

**Verdict: PASS in precisely the written scope.** I find no logical defect in the implication from the uniform ball-pair contraction predicate to strong regularity, or in its ensuing real TOP recognition consequence for closed manifold fibres of dimension at least five. This audit does not supply a definable bundle chart or an all-field controlled-mesh argument.

## Finite pair certificates

For a fixed named-coefficient complete o-minimal theory, compatible triangulation holds in every model. Uniform one-variable finiteness makes every model o-minimal. A finite graph formula with coefficient variables can certify a homeomorphism of one rational finite pair onto the actual pair, including both continuity assertions and the marked-subset equality. If no finite collection of these certificates covered the parameter set, compactness would give a parameter in a model with no compatible triangulation. This proves the finite certificate pool without enumerating or deciding the theory.

The Baro--Otero comparison used in the candidate determines the nullhomotopy truth value of each rational finite pair independently of the model. A positive finite semialgebraic homotopy format reflects to the real algebraic field by real-closed-field elementary equivalence. Transporting those finitely many homotopies through the certificate homeomorphisms gives the finite witness pool. No jointly continuous selection of a certificate is asserted or needed.

## Controlled construction and strong regularity

I checked the relative simplex induction, including prescribed simplices. At a new j-simplex, its boundary lies within `2 r_(j-1)+r_0 <= 3 r_(j-1)` of the chosen vertex label. A nullhomotopy of that ball-pair inclusion cones the boundary inside the next radius; adding at most `r_0` changes reference vertex and gives the stated `2 r_j` bound. The cone-point continuity is valid because the contraction is continuous on a compact domain and constant at its terminal time.

For maps between close fibres, a finite fine triangulation of the source and nearby vertex labels suffice. For close maps into a fixed target, the triangulated product has only top and bottom vertices. The prescribed top map need not have its own initially small modulus: closeness to the bottom map and the bottom simplex-diameter bound give the required top control. The resulting homotopy has track diameter less than the prescribed epsilon.

The two independent backward radius chains are essential and are present. The first produces a uniform threshold for small homotopies into every nearby fibre. The second produces ambient-small maps in both directions. Their composites are within twice the map displacement of the respective identities, **without any Lipschitz hypothesis on either map**. The first threshold therefore supplies homotopies of both composites in their respective fibres. Their tracks and the maps can be made as small as desired. No continuity of these choices as the base point varies is required by strong regularity.

Properness and openness give Hausdorff continuity on a compact target neighbourhood. The necessity argument for the contraction predicate uses uniform continuity of a compact restriction of a TOP bundle chart and inverse. All fibres involved are compact definable sets and hence triangulable. Ordinary contractions of the definable ball pairs have the same truth value as definable contractions by the finite-pair comparison.

## Exact TOP recognition step

The candidate correctly distinguishes strong and complete regularity. Given a cover beta of the target fibre, a sufficiently small homotopy in the source remains beta-small after the small ambient-displacement forward map. Thus the nearby-fibre map is a beta-equivalence in Chapman--Ferry's exact sense. Their alpha-approximation theorem, with closed fibres so no boundary correction is needed, gives an arbitrarily small homeomorphism. This is complete regularity. Proposition 7.1 then supplies local triviality over the locally finite-dimensional base.

I freshly reopened Gauld's full original and read Theorem (1) and its Corollary on printed p.3. These give local contractibility of the compact-open homeomorphism group of every finite polyhedron; no parametric definable assertion is extracted from the limiting contraction.

## Original-source verification

* Chapman--Ferry, *Approximating homotopy equivalences by homeomorphisms*, AJM 101 (1979), 583--607. Full original: `https://webhomes.maths.ed.ac.uk/~v1ranick/papers/chapferr.pdf`. I read the retained original OCR of pp.583--584 and 605--606, and explicitly viewed the actual images of printed pp.583 and 605 in this audit. The p.583 image plainly states **n >= 5**, and displays the exact alpha-equivalence conditions. The p.605 image displays Proposition 7.1 and the strong-regularity definition with small homotopies in the respective point inverses. I do not substitute Proposition 7.2's Hurewicz-fibration hypothesis for the candidate's independently proved strong regularity.
* Gauld, *Local contractibility of spaces of homeomorphisms*, Compositio Math.32 (1976), 3--11. Full original: `https://www.numdam.org/item/CM_1976__32_1_3_0.pdf`; fresh web reference `turn215503307view0`. Printed p.3 and the topology convention on p.4 were read.
* The Baro--Otero original and its stated homotopy-set locators had been independently opened in the preceding finite-pair discussions; the present verdict rechecks their use in the full authored argument, not a new stronger comparison theorem.

The downloaded Chapman--Ferry original and page images are external material under `/tmp/A5_originals_chapman_ferry/`, outside the authored project.

## Minor optional wording

One may explicitly impose `3 r_j <= r_(j+1)` in (LC.6). The word "inclusion" already requires the relevant set inclusion, and the actual backward radius construction imposes the stronger `r_j < r_(j+1)/4`, so this is not a proof gap. The two previously noticed missing TeX backslashes are repaired in the audited version.

## Scope

The exact formula describes the **real TOP** local bundle locus with closed n-manifold fibres for n >= 5. It neither proves TOP-to-definable local trivialization nor addresses all real closed fields, dimensions three or four, or arbitrary compact polyhedral fibres. The finite pool consists of nullhomotopies, not homeomorphisms. No main-task completion or review movement is inferred merely from this audit.
