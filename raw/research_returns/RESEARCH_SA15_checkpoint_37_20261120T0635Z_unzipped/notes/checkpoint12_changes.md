## Current state

This checkpoint remains **INCOMPLETE**. Main rows A.3, A.4, B.3 in higher dimension, and B.4 retain explicitly stated open gates. The simultaneous locally Noetherian/coherent refinement of E.2 is now proved. The unrestricted E.2 assertion remains refuted. All assertions promoted below passed a complete independent proof audit; finite arithmetic checks are separately identified and do not substitute for geometric existence proofs.

## Coherent crystals over a Noetherian base

For every flat locally finitely presented morphism X→S with S locally Noetherian, restriction gives an equivalence between ordinary coherent stratified modules and quasi-coherent infinitesimal crystals whose value on X is coherent. The statement holds on both the small and big infinitesimal sites, including arbitrary classical tests, and in every characteristic. Values are coherent on Noetherian tests and finitely presented on arbitrary tests. The coefficient module need not be flat.

The proof establishes a universally exact completed augmented Cech complex by filtering along the nilpotent test ideal. This descends finite Hom modules and proves ordinary full faithfulness. Flatness of the completed formal-nerve projections lifts the coherent stratification to derived complete data. Jiang's precisely checked comparison yields a derived crystal. A finite nilpotent filtration proves that its values are in D≤0; taking H0 then gives ordinary Cartesian pullback. The proof does not claim that the intermediate derived crystal is discrete. Finite-type graph neighbourhoods, common refinements and equalizers extend it to arbitrary tests. The root, monodromy and reduction/descent agents independently checked the entire proof and its original source bridge.

The prior nonfaithfulness examples are unchanged: dropping coherence can fail even over a regular Noetherian base, and dropping the Noetherian condition can fail for a rank-one structure crystal. Their scope remarks now point to the proved narrower theorem, rather than describing it as undecided.

## Every polarization on an ordinary surface

Let A be an ordinary abelian surface in characteristic two, let M be any ample line bundle, put D=chi(M), and use the embedding L=M³. For every positive d the geometric generic smooth curve in |L^d| is ordinary of genus 9Dd²+1, and its relative stable rank is exactly 9Dd²−1. No parity restriction on D or d remains.

The integral dual polarization is constructed by descent along lambda_M. In its two-primary kernel, the connected multiplicative factor is maximal isotropic. Choosing it makes the dual principal-source isogeny finite etale even when its degree is even. A sharp genus-ten ordinary source curve has a nodal norm image; the collision incidence proof is checked for even-order translations. An arbitrary target translation puts the norm in the exact desired linear system. Transverse unions of ordinary members then prove every degree. The existing ambient regularity bound remains explicit; no assertion about an arbitrary embedding being a cube is made.

## Sharp ranks for inseparable supersingular product types

On A=E×E, E:y²+y=x³ in characteristic two, let M=O_E(aO) external O_E(bO), where a,b are positive integers, and put L=M³. If exactly one factor is even and that integer has 2-adic valuation one, the generic relative ranks are 9abd²−2 for odd d and 9abd²−3 for even d. If both a,b are even, the rank is 9abd²−3 for every d. The coherent relative dimension is 9abd²−1. Types with exactly one even factor of higher 2-adic valuation are not covered by this theorem.

The proof first obtains global Cartier-kernel relations from the canonical connection on an even-degree factor. An exact (6,3) base matrix has rank(C)=rank(C²)=16. Odd-degree product isogenies propagate this sharp base, with a complete nodality proof allowing kernel projections that are not injective. Transverse unions of two sharp odd product types give the both-even lower bound. The complete independent audit also reconstructed all eighteen matrix columns from the curve-ring identity f=a²+x b², without importing the author's monomial Cartier formula.

## The supersingular global contact witness

The local self-tacnode and triple-point Cartier lemmas are now proved after full independent audits. One global norm-family witness has also been certified over GF64. Its source is geometrically smooth; its degree-three norm image has exactly one simple self-tacnode and otherwise ordinary nodes. The relative Hasse divisor is smooth at this image. The exact coefficient vector is (38,14,10,47,47,43,30,4,8), in the specified monomial tensor basis. All four smooth-source charts and all144 collision ideals were checked over the algebraic closure, with genuine rational translation identities and nilpotent-support tests. A separate truncated elliptic-addition calculation verifies the simple-contact coefficient55 and mixed Cartier value60.

The first two candidates failed because of unwanted triple collisions; their inputs, outputs and failure transcripts remain in the archive. Two implementation errors in the initial finite-field interface are retained as failed runs as well. No rational-point sampling was used to assert a global exclusion. The candidate finite collision reduction remains explicitly unpromoted: two distinct tangent-triple orbit witnesses and the later uniform propagation step still have to be completed. The known full groups in degrees one through three are unchanged.

## The remaining height-two character test is elliptic

For p=3, absolute ramification e=2 and height h=2, the least manuscript index remains either2 or3; 81-torsion always suffices. Every potentially supersingular norm-one comparison in the remaining case can now be realized by elliptic curves, preserving the integral Tate lattice and the special inertia action. The proof uses explicit integral quaternion conjugacy, labelled Serre–Tate deformation, algebraization and generic Galois descent. It does not descend a good model across ramification.

For a potentially supersingular elliptic curve, the tame special-inertia quotient has order t=4/gcd(4,v(Delta)). Thus the residual level27 ambiguity is equivalent to two triples (a2,a4,a6) over W(k)[pi]/(pi²−3), for an algebraically closed field k of characteristic three, with 0≤v(Delta)≤23, 3v(c4)>v(Delta), isomorphic generic27-torsion, and discriminant valuations in different columns of {0 mod4,2 mod4,odd}. This is a proved six-coefficient criterion. Its existence or nonexistence has not been decided.

## New computation record

Every output listed here is retained verbatim. Independent reruns use separate output paths; no author output was overwritten.

| Program | Inputs and exact scope | Runtime, seconds | Output |
|---|---|---:|---|
| code/supersingular_rectangular_rank.py | Seed202611191719; two exact binary sections for the (6,3) system; all18 columns and ranks C,C² |0.0006987419983488508|outputs/supersingular_rectangular_rank.json|
| agents/obstructions_crystals/code/independent_ss_rectangular_reconstruction.py | Independent curve-ring Cartier reconstruction for section74594; all18 columns and rank16 |0.0006671840019407682|Same stem .output.json|
| agents/obstructions_crystals/code/A3_ordinary_all_rank_checks.py |211 polarization types, including146 even types, and27008 degree cases; integral dual matrices and norm/graph identities |0.016162138999789022 author;0.014947520998248365 root|Author output and outputs/root_A3_ordinary_all_rank_checks.json|
| agents/reduction_descent/code/verify_elliptic_inertia_conjugacy.py | Exact quaternion conjugacy and integral valuation checks for the elliptic-realization theorem |0.15318646800005808 author;0.16175238999858266 root;0.16004351700030384 independent|Author output, outputs/root_verify_elliptic_inertia_conjugacy.json, independent agent output|
| agents/reduction_descent/code/verify_discriminant_tame_character.py |24 discriminant rows,4221 equation shifts,977 bound cases, c4/c6/Delta and Cartier identities |0.04732804800005397 author;0.04524370399667532 root;0.061048945997754345 independent|Author output and outputs/root_verify_discriminant_tame_character.json|
| agents/monodromy/code/supersingular_level3_kernel_orbits.py | ExactGF4 group law, kernel graph, all8 nonzero translations and the12/72 affine triple orbits |0.007294220002222573|agents/monodromy/outputs/supersingular_level3_kernel_orbits.json|
| code/ss_contact_witness.py | Separate seeded discovery inputs01 and02; local contact and Cartier checks only |Actual elapsed values in each complete JSON|outputs/ss_contact_witness.json and outputs/ss_contact_witness_02.json|
| code/ss_contact_witness_screened.py | Seed202611191119;729 rational kernel orbits used only for rejection; successful candidate03 at trial29 |0.9476508590014419|outputs/ss_contact_witness_03.json|
| code/verify_ss_contact_geometry.py | Four projective product charts; exact smooth-source ideals for each candidate; all field products/divisions independently compared |3.2001894870008982 for03|outputs/verify_ss_contact_witness_03_geometry.json; all earlier runs retained|
| code/verify_ss_contact_collisions.py | Actual projective translations;32 pair and112 triple ideals for03, all over the algebraic closure |74.52918819499973 for03|outputs/verify_ss_contact_witness_03_collisions.json; failed01/02 outputs retained|
| agents/monodromy/code/verify_level3_contact_local.py | Independent first-candidate field, Cartier and actual branch-series checks; local only |0.003499177997582592|agents/monodromy/outputs/verify_level3_contact_local.json|
| agents/monodromy/code/verify_level3_contact03_local.py | Independent successful-candidate field, Cartier and actual branch-series checks |0.0036840360007772688|agents/monodromy/outputs/verify_level3_contact03_local.json|
| agents/monodromy/code/rerun_contact03_global_audit.py | Read-only complete independent rerun of all source and collision ideals |3.4523235300002852 source;72.10777428700021 collisions|Independent same-basename outputs and independent_contact03_global_run.log|

The current mathematical programs and their complete outputs are also exported into code/ where applicable. Later search runs present at the checkpoint freeze remain explicitly bounded discovery attempts until their full geometric verification passes. Their individual JSON records contain the exact seeds, scope and elapsed times.

## Sources, corrections and retained history

ROOT_SEARCH_LOG_12.md records the exact new source passages, original-text reads and targeted searches. New proof inputs include Jiang2023 Theorem2.1/Remark2.4, Proposition6.2/Theorem6.3 and AppendixB; Stacks00MA/00MB/00IP/0H0L; the specified AV group-scheme, duality and descent propositions; Katz1981 Theorem1.2.1; Lazard1955 TheoremIV; EGAIII1 Theorems5.4.1/5.4.5; and the original Serre–Tate1968 page496. All access limitations remain recorded. No manuscript scans were supplied, Michel Hua's project remains unused, and no priority is claimed.

The self-tacnode and triple-point files lose their former candidate suffix only because their complete proofs have now passed independent audits. Their old names are listed in the monodromy change log. The broad E.2 counterexamples are not removed; only the statements that left the narrower coherent Noetherian refinement undecided have been superseded by the new theorem. The conditional collision reduction remains a separate candidate file and is not presented as an established global theorem.

The actual hourly review06 remains immutable. The post-review06 odd-polarization and logarithm promotions, and the new results in this checkpoint, will be assessed at the actual review07 due11:50:40UTC. Packaging, source retrieval and certificate reruns alone are not counted as mathematical movement.

## Final checkpoint verification

The final paper has305 pages and2,289,105 bytes. The reproducible final build passed in31.906 seconds with zero overfull boxes and no unresolved references or citations. The initial build had one123.4066pt overflow in the coherent-category equivalence display. That display was split into two compact arrays, rebuilt, and explicitly inspected on page266. Both build records are retained.

All47 selected pages were actually inspected:8 by the root,12 by monodromy,12 by reduction/descent and15 by obstruction/crystals. The sample covers the complete new sections and a spread through the existing text; the precise page lists and actual observation time are in outputs/visual_qa_checkpoint12.json. No clipping, overlap, broken glyphs or margin failures remained.

The final register contains348 numbered statements, and the source census has140 rows including the explicitly unused Hua witness. The remaining source scans are unavailable as before. Only complete, independently audited mathematics is promoted in the paper.

During the paper freeze, the two additional tangent-triple certificates also passed independent full global reruns:76.3690687260023 and74.86146398200071 seconds for144 collision ideals each, plus source smoothness3.7411868540002615 and3.3895406299998285 seconds and an independent local-series check0.007957189001899678 seconds. Their candidate witness proof and complete outputs are retained separately. A further ordinary arbitrary-embedding proof and a bounded probe of rectangular types(12,3),(24,3),(48,3),(96,3) are also retained as unintegrated work. The latter probe took0.6945195179941948 seconds and is explicitly not an all-valuation theorem. None of this post-freeze work is silently promoted into the already inspected PDF.

## Actual hourly review07

The actual review was recorded at 2026-11-19T11:51:02.675118+00:00, against immutable review06. It found the structural A.3 extensions, the closed coherent Noetherian E.2 refinement, and the strictly smaller B.4 least-index gate described in notes/review07_assessment.json. The consecutive no-movement count is 0; disposition: Continue. Post-freeze candidates, packaging and repeated calculations were excluded from this progress count. The next review is due12:50:40UTC and the next checkpoint is due12:35:40UTC.
