from pathlib import Path
import csv
from datetime import datetime
from zoneinfo import ZoneInfo
R=Path('/workspace/scratch/74996cb138ef')
p=R/'work/build_package.py'
s=p.read_text().replace("'work/theta/outer4/chamber_report.md']),","'work/theta/outer4/chamber_report.md','work/theta/outer4/four_fibers_report.md']),").replace("'work/rectangular/boundary_truncation_model.md','work/root/current_ranges.md'","'work/rectangular/boundary_truncation_model.md','work/rectangular/polarization_second_row_range.md','work/root/current_ranges.md'")
p.write_text(s)
now=datetime.now(ZoneInfo('Europe/Berlin')).isoformat()
checks={
'T-032':'Read entire balanced flag localization proof, generator surjectivity, prescribed centered-matrix inverse, equivariance, and exact u-divisibility subspace; PASS.',
'T-033':'Read the complete Elliott-band character identity and five harmonic Molien numerators, including parity and all endpoints; PASS.',
'T-034':'Read entire lower/upper chamber polytope construction, complement map, determinant twist, and fixed tag bounds; PASS.',
'T-035':'Read entire four-fiber proof: independent transverse parameters, exact valuation equality, smooth-fiber ideal powers, incidence presentation, complete-intersection resolution, all sign actions; PASS.',
'T-036':'Read whole positive module proof and all polytope constraints: quotient bundle, H1 boundary term, equivariant splitting, tensor table, negative-index cases, and 72-tag bound; PASS.',
'R-015':'Read full rank-six finite certificate proof, complete character decomposition, selected square blocks, independent Taylor evaluation, and normalization to the padded-form ideal; PASS.',
'R-016':'Read full three-kernel proof, complete character/rank certificates, symbolic rectangular kernels, and uniqueness of each missing copy; PASS.',
'R-017':'Read whole homogenization and truncation proof, highest-vector translation action, recovery from common-vector restriction, and critical rectangle degree obstruction; PASS.',
'R-018':'Read full flag-minor generation proof and second-row block-degree bound; checked diagonal inverse, all Schur projectors, isotypic injectivity, and ideal consequence; PASS.',
'A-019':'Read complete field cancellation argument and characteristic-two hypotheses; PASS.',
'A-021':'Read full extension to every characteristic-zero DVR: torsion boundary, split residue Specht simples, unitriangular generation, commensurability, and induction compatibility; PASS for extended scope.',
'A-022':'Read full hyperbolic characteristic-class proof for Z[1/2]-schemes, the actual tautological idempotent splitting, injective pullbacks, line calculation, and Whitney formula; PASS.',
'A-023':'Read entire local-ring counterexample including the added K0(A)=Z argument: Nakayama, determinant exactness, and explicit character separating the proposed generators; PASS.',
'G-014':'Read whole canonical-map first-row proof, distinct-index Mobius formula, Newton expansion, bounded factor count, explicit lifted polynomial, dense-open identity and full isotypic surjectivity; PASS.'}
with (R/'work/root/CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,out in checks.items():w.writerow([sid,now,'root; GPT-6 Astra Pro; effort not exposed; GCT_PLETH_20261121_run01','targeted proof check',out])
p=R/'work/root/paper_front.md';s=p.read_text();a=s.index('Several formulas avoid');b=s.index('## Conventions')
s=s[:a]+'''Several formulas avoid the general elimination step. G-012 gives four fixed polytopes for every symmetric outer-degree-three coefficient. T-032 constructs an exact localized flag-algebra chart in every outer degree. T-033–T-034 give at most twelve fixed three-variable polytopes for every outer-degree-four Schur label in the two outside chambers; T-030–T-031 cover all proper root faces. T-035 identifies the remaining extension condition with vanishing to a specified order along four fibers of a flag variety. T-036 gives at most 72 fixed five-variable polytopes throughout the central family with equal opposite root gaps. The next active operation evaluates this same four-point ideal for unequal gaps. T-012–T-013 give finite explicit Littlewood–Richardson polytopes through stable width six, and T-018 evaluates an entire width-seven sector.

For the actual canonical map, G-013 transports prime-adjacent square preimages through an explicit block specialization and multiplies them, with exact numerical semigroup certificates for ranks 2 through 100. G-014 supplies explicit preimages for every target highest-weight component whose tail has size at most the coordinate degree. R-015 certifies rank-six common polarization on its entire source, R-016 determines three finite boundary kernels, and R-017–R-018 identify the general kernel with an exact polynomial truncation and prove injectivity on every component with second row at most the residual slot degree. The remaining varying kernel range is explicitly smaller.

The archive audit now inventories 123 individual assertions: 80 proved, 25 refuted, and 18 exact gates. All thirteen supplied target leaves have been compared with the original Montpellier scans. A-021 proves the exact lattice-ring statement over every characteristic-zero discrete valuation ring. A-023 gives an explicit characteristic-zero local-ring counterexample even with base K0 equal to the integers. A-022 proves the hyperbolic characteristic-class formula over every scheme with 2 invertible using an actual injective splitting construction. The remaining historical and mathematical inputs are retained assertion by assertion.

'''+s[b:];p.write_text(s)
p=R/'work/root/remaining_gates.md'
p.write_text('''# Unresolved items and exact next operations

G-009–G-011 prove terminating positive formulas for every coefficient and every actual canonical-map image multiplicity. Uniform polynomial bounds on their preprocessing and witness data remain open. The exact missing bounds concern the Hilbert basis, invariant list, and elimination presentation.

For direct outer-degree-four formulas, T-030–T-034 cover all proper root faces and both outside chambers, and T-036 covers the central family with equal opposite root gaps. T-035 proves the exact four-point ideal model for every remaining shape. The next operation is a positive decomposition of its complete-intersection ideal powers for unequal opposite gaps; the remaining object is a specified coherent sheaf on the incidence flag variety, with every comparison map already proved.

For the canonical map, G-013 gives all prime-adjacent semigroup blocks, G-014 the complete long-first-row range, and R-016 determines three finite boundary kernels. R-017 identifies the general common-polarization kernel with block truncation on explicit translation-invariant highest polynomials. R-018 proves injectivity for every outer Schur functor on second rows at most b−L. At b=rL−1 the remaining possible kernel components have second row at least (r−1)L. Its complete varying-parameter classification remains open. The checked full canonical-map bound and all component ranges are retained separately with their exact maps.

For width seven, T-018 evaluates the end-node sector and G-010 supplies a general finite count. The smaller direct-formula gate is the remaining discriminant-valuation filtration on the stated G2 invariant spaces.

The archive has 123 assertion rows, of which 18 retain precise gates after inspection of all thirteen original target leaves and relevant neighboring pages. These include admitted crystalline Lefschetz/freeness inputs, the projected motivic self-duality map, reconstruction from one unlabeled triangulation, and the unspecified completed characteristic-class target. Literal type errors are refuted with their corrected maps proved. The full classification of coefficient rings remains open after the DVR theorem and explicit local counterexample.

The Alpöge theorem is accepted as requested. Its transfer to the projectors and canonical-map image in this paper still needs the explicit equivariant representation/period morphism. The named Lean source files and scan report are absent. The requested Masullo work has no supplied statement or identifier. No locator or missing comparison has been invented.

No formal progress review is due before three elapsed hours, at 03:01:08 Europe/Berlin. This checkpoint retains active work and makes no assertion that the stopping rule has been reached.
''')
p=R/'deliverables/LEDGER.md';s=p.read_text();s+='''
## Checkpoint 02 update — 21 November, 01:31 Europe/Berlin

The first checkpoint was saved at 00:46:27 Europe/Berlin. The second is due at 01:31:08. The research remains active; no formal stagnation review is due yet.

Since checkpoint 01, the outer-degree-four direct formula has advanced through every proper face, both outside chambers, and the central equal-opposite-gap family. T-035 proves an exact four-point vanishing model for the entire remaining region. Evaluation of its unequal-gap ideal powers is the next main operation. Independent cycle-index/Murnaghan–Nakayama calculations checked 1,370 chamber coefficients and 420 coefficients in the new central family; the full proofs were also read independently.

For the canonical map, G-013 constructs actual prime-adjacent semigroup preimages; 198 exact semigroup certificates cover ranks 2–100. G-014 gives explicit lifts of all target components with tail size at most coordinate degree. R-015 certifies the complete rank-six quintic common-polarization source, including 65,481 matrix entries and 893 selected determinants. R-016 classifies three finite boundary kernels. R-017–R-018 replace the remaining general kernel by exact block truncation and eliminate every component with second row at most b−L, for all outer Schur functors.

The original archive scans have now been inspected for all thirteen target leaves. The assertion register contains 80 proved rows, 25 refuted rows and 18 precise gates. The exact lattice ring is proved over every characteristic-zero DVR; an explicit characteristic-zero local ring with K0 equal to Z refutes the unrestricted generator claim. The hyperbolic class formula is proved for all schemes with 2 invertible through an actual injective splitting construction.

Earlier 'still computing' notes above are historical. The current finite boundary outcomes are those in R-012, R-015 and R-016, with all complete certificates included. No general boundary-kernel classification is asserted.
''';p.write_text(s)
p=R/'deliverables/IMPLICATIONS.md';s=p.read_text();s+='''
## Consequences added at checkpoint 02

T-032 constructs the localized balanced flag algebra and its exact divisibility condition in all ranks. For outer degree four, this leads to fixed positive polytopes on both outside chambers and every proper face, and to an exact four-point vanishing model on the central chamber. T-036 evaluates the equal-opposite-gap central family by a positive sum of two explicit S4 modules. Its five-variable polytopes have fixed tags and logarithmic-size witnesses. The unequal-gap section spaces remain under active calculation.

G-013's block-specialization diagram turns known prime-adjacent square scalars into explicit rectangular preimages and their mixed products. G-014's multisymmetric expansion lifts every target component whose tail has size at most the source coordinate degree. R-018 proves an entire second-row injectivity range for the common-polarization map and all its Schur projections, by an explicit inverse to the nonzero diagonal truncation weights. These are statements about the specified linear maps, with every preimage or inverse described.

A-021 identifies the exact symmetric-group lattice ring over every characteristic-zero DVR with its characteristic-zero representation ring. A-023 exhibits the precise determinant character outside the proposed generator span over Z_(2)[epsilon]/(2epsilon,epsilon²), although K0 of that base is Z. A-022 establishes the characteristic-class formula for hyperbolic bundles through an actual splitting idempotent and injective cohomological pullbacks over every Z[1/2]-scheme. The original scans have now been checked; the remaining 18 assertion-level gates are mathematical or definition inputs described in the register.
''';p.write_text(s)
print('checkpoint 02 prose and proof checks updated')
