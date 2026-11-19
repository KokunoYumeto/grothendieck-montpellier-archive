"""Manually consolidated open-step index for the fully read VI–VII corpus."""
from claim_records import CLAIMS
INDEX={c['id']:c for c in CLAIMS}
PROBLEMS=[]
def P(cote,n,title,nums,as_he,plausible,art,why,worth,refs):
    ids=[f'C-SA21-{cote}-{x:03d}' for x in nums]
    occ=[]
    for cid in ids:
        occ.extend(INDEX[cid]['lines'])
    PROBLEMS.append(dict(id=f'MP-SA21-{cote}-{n:02d}',title=title,occurrences=list(dict.fromkeys(occ)),
        as_he_states=as_he,plausible_today=plausible,state_of_art=art,why_open=why,
        worth=worth,refs=refs))

P(6,1,'Which relations determine an atelier?', [2,4],
  'Check the refinement-supremum/zero-infimum characterization of disjointness (VI13 “Vérifier”); determine whether refinement alone or face inclusion plus subdivision determines the remaining structure.',
  'Keep nested face/refinement orders and a separately specified compatibility/disjointness structure unless an exact representation theorem proves redundancy. Generation of refinement by face inclusion and subdivision is an additional condition, explicitly dropped at VI21.',
  'Opened Malgoire2002 confirms later exposition of the atelier vocabulary, not a theorem resolving this redundancy. S67-02,03,05,11,12 found no exact published implication. Complete-lattice duality in Massas2023 Theorem2.30 only handles the face-order component.',
  'The manuscript changes the definition of refinement and cancels the earlier minimal-data claim. No source establishes a later historical reason for the remaining check being left open.',
  'Worth a bounded axiom-dependency audit because false redundancy changes every reconstruction theorem.', ['Malgoire2002','Massas2023','CSGUnpublished'])
P(6,2,'Faithful large-shadow reconstruction and the complete At* list',[3,5,6,7,44],
  'Does the large multiombre give the announced equivalence with families of set figures, with no forgotten At* axiom, including finite-type versions?',
  'Use complete join-prime elementary figures, the least-receiving-face property, immediate-refinement transitivity, exact family closure conditions, and hereditary finite generation if every subfigure is required to have finite type. Interpret an equivalence of structures until morphisms are specified.',
  'Speed1968 §4C and §5 final corollary and Massas2023 Theorem2.30 settle the underlying downset representation. They do not contain the two-order At* reconstruction. Searches S67-02–05,11,12 located no exact published version.',
  'At7 is added after the composition proof exposes its absence. The author expressly worries about missing axioms; later Prat/Mag formulations replace the list.',
  'Worth formalizing as a small theorem suite because it separates the standard order representation from the original refinement data.', ['Speed1968','Massas2023','Malgoire2002'])
P(6,3,'Small-shadow faithfulness, morphisms and inverse-image constructions',[8,13,14,16,17,18,43],
  'When do small shadows recover an atelier, and which operations on figure sets produce covariant or contravariant stratum maps? Does every map of sets induce the proposed figure pullback?',
  'Complete local downset homomorphisms are inverse images of unique monotone maps without sobriety. Global faithfulness requires separate injection/refinement/compatibility hypotheses. The naive closed-preimage construction must remove empty open strata or restrict the allowed maps.',
  'Massas2023 Theorem2.30 gives the exact local order-map theorem; independently re-proved here. The finite pullback counterexample settles the literal VI51 formula. No exact global atelier morphism category was found in S67-02–05,09,11,12.',
  'The pages themselves observe affine/PL information loss and change direction between maps and comaps; VII58–59 withdraws stronger converse claims.',
  'Worth developing a carefully typed morphism definition before asserting categorical equivalences.', ['Massas2023','Speed1968','Malgoire2002'])
P(6,4,'Additional linking data for pseudodisk reconstruction',[9],
  'Recover geometry from shadow data enriched by the missing links between pseudodisks.',
  'First specify the geometric category, the incidence/link object, equivalence notion and reconstruction functor; no strongest precise theorem can be extracted without those choices.',
  'Esquisse §5 pp25–27 discusses canonical decomposition of stratified spaces and gluing pieces, with isotopy addressing noncanonical choices. It does not define this pseudodisk invariant. S67-03,05,06,11 found no exact later theorem; CSG still lists VGF as unpublished.',
  'The source leaves it at an idea. A later cause of nondevelopment is not documented by the opened sources.',
  'Worth only after the elementary structure is stabilized; the first task is a definition, not a proof.', ['Esquisse1997','CSGUnpublished','CruzMorales2021'])
P(6,5,'Subatelier closure, density and saturation',[10,11,12,42],
  'Does a lower family inherit all axioms, is the large-shadow image spacious, and can an atelier be saturated through thick/quasi-dense subateliers?',
  'Require Sousat2 in addition to lowerness, and disjointness reflection for inheritance of L2. Any saturation must state which compatible/infinite unions it adds and verify that it preserves the intended refinement and loci.',
  'The saved three-point example refutes unrestricted At3 inheritance. Downset closure methods are standard (Speed1968), but no exact thick/quasi-dense saturation theorem for this two-order structure was identified in S67-02–05,11,12. Malgoire2002 supplies only historical presentation evidence.',
  'The manuscript corrects the lower-family claim and explicitly postpones saturation; the L3 inheritance argument has an unresolved direction reading.',
  'Worth a finite countermodel audit first, because a saturation that changes disjointness would change virtual supports.', ['Speed1968','Malgoire2002','CSGUnpublished'])
P(6,6,'Compatibility and disjointness axioms in set-like examples',[19,20,21,41],
  'Which locus tests recover compatibility, and is disjointness stable under refinement without further assumptions?',
  'State stability as D0 or derive it from a fully specified L2/locality system. Distinguish pure set intersection, geometric compatibility and strict/polyhedral refinement; retain the empty-or-elementary common-face condition only in the polyhedral variant.',
  'Exact atelier-axiom searches S67-02,03,05,11,12 found no published resolution. Opened polarity literature explains how an orthogonality graph yields supports, but does not justify geometric compatibility from arbitrary set shadows.',
  'A selective-compatibility obstruction leads the author to add disjointness axioms; the later strict-refinement repair changes the intended examples.',
  'Worth checking on explicit small models before extending the axiom ladder.', ['LindenhoviusVetterlein2023','Malgoire2002'])
P(6,7,'Finite versus arbitrary gluing of refinements',[22,23,24,25,26,27,28,29,30,31],
  'Check restriction, compatible gluing and the implication diagrams; isolate the existence axiom needed for infinite families.',
  'Use the least-receiving-stratum inverse-image construction for restriction, At11′ for finite compatibility and a distinct directed local-supremum existence axiom for infinite gluing. The choice of intersection class Σ must be fixed.',
  'SGA4 ExposéII Definition2.1 gives the sheaf matching-family paradigm; it is a formal comparison because its objects/sites are not these ateliers. No exact At11/At11bis theorem was found in S67-05,08,11. Massas2023 handles only the local lattice maps.',
  'VI79–81 explicitly retracts a diagram that conflated finite compatibility with infinite join existence.',
  'Worth proving the finite and directed parts separately; the first concrete step is an axiom-by-axiom restriction/gluing proof.', ['SGA4II','Massas2023','Esquisse1997'])
P(6,8,'Support witnesses and subdivision maximality',[32,33,34,35],
  'Can an external witness separating the orthogonality profiles of F′≪F be found inside F, and does equality of profiles characterize face-maximal refinements?',
  'Retain the support-witness axiom, L2 and restriction locality; use maximality in face order, not refinement order. Any stronger common-refiner requirement is a different set-like hypothesis.',
  'Lindenhovius–Vetterlein2023 §§1,3 verifies the polarity background and shows why support equality is weaker than Boolean/set behavior. Searches S67-01,07,09–12 found no exact atelier maximality theorem. The P4 model checks the old witness axiom but not optional absorption.',
  'The manuscript alternates axiom/proposition labels and reduces to an elementary/locus case; it does not remove the reduced hypothesis.',
  'Worth a focused independent proof because this is the bridge from geometric subdivision to virtual support.', ['LindenhoviusVetterlein2023','Janowitz1963'])
P(6,9,'Extending a subdivision with unchanged exterior',[36,37,38,39],
  'Extend G′≼G≤F to F′≼F; preferably leave exterior strata unchanged and obtain a canonical/least extension, or one elementary filler for a subdivided boundary.',
  'Separate existence of an extension in a specified PL/semianalytic category from uniqueness and unchanged incidence. A strict simplicial elementary filler fails for a triangle with a subdivided edge. Any elementary-boundary uniqueness statement needs fixed support and an equivalence convention.',
  'Łojasiewicz1964 §3 Theorems1–2 pp463–464 proves simultaneous locally finite triangulation of locally finite semianalytic families. Baro2010 Theorem4.3 proves compatible normal triangulation for a closed finite definable complex. Neither asserts the exact unchanged-exterior/unique-elementary extension requested here.',
  'The author explicitly sees failure for strict simplicial ateliers and calls these axioms optional. No later source explains a historical abandonment.',
  'Worth reformulating only after choosing the geometric category; a few-hour task can test precise relative versions, not promise canonical uniqueness.', ['Lojasiewicz1964','Baro2010','Esquisse1997'])
P(6,10,'Finite type makes the directed local-existence axiom vacuous',[40],
  'Check the brief assertion that a locally finite increasing refinement family is stationary when all figures are of finite type.',
  'With face-directed increase, local face suprema, finite generation of each figure and complete join-prime elementary objects, the family is eventually constant. Do not replace these by refinement-directed increase.',
  'Independently proved in formalism_and_checks.md §3 from the standard compactness of finite joins of complete join-primes. Speed1968 verifies the pre1986 representation mechanism; no external exact atelier wording was found.',
  'The manuscript only gives a parenthetical assertion. The analyst’s initial concern was resolved after checking the strong definition of irreducibility.',
  'No new research is needed for this precise version; retain the proof and test only genuinely different variants.', ['Speed1968','Massas2023'])

P(7,1,'Polyhedral duality and the weak simplex criterion',[2,3,4],
  'Check self-duality under interval inductivity and the claimed finite-poset characterization of a simplex; use strict refinement for geometric examples.',
  'Keep chain-completeness hypotheses in the order-duality lemma. Replace the false predecessor-count criterion by Boolean principal intervals; a square is a complete counterexample to the written criterion.',
  'Stanley1991 §1 p319 states the Boolean interval definition of simplicial posets and the meet-semilattice specialization to simplicial complexes. It does not validate the manuscript’s weaker test. The square certificate checks every written hypothesis.',
  'The simplex induction misses that not every subset of minimal elements must occur as a face. No later self-correction occurs in the supplied VII pages.',
  'Worth a short editorial correction and a scan check; the false criterion itself is settled by the saved example.', ['Stanley1991','Lojasiewicz1964'])
P(7,2,'Atfil for refinement-increasing families',[5],
  'May face-increasing be replaced by refinement-increasing, and should the supremum then be taken for refinement?',
  'Treat this as a separate theorem with an explicit order of directedness, restriction notion and local-stationarity hypothesis; the face-order theorem does not answer it.',
  'SGA4II Definition2.1 supplies only a gluing analogy. S67-05,08,11 found no exact two-order directed-union result for these axioms.',
  'The margin leaves the choice open and the following corollary gives no full proof.',
  'Worth a small-model dependency search before attempting a general proof.', ['SGA4II','Malgoire2002'])
P(7,3,'Strong support witnesses and common refiners',[6],
  'If Y is disjoint from G but not from F, with G≪F, can one choose a nonzero witness refining both Y and F?',
  'The claim needs a common-refiner/disjointness equivalence such as AtensD; it is not expected in arbitrary orthogonality spaces. For loci it becomes x not⊥F⇒x≪F, a strong set-like condition.',
  'The opened orthogonality-space paper Lindenhovius–Vetterlein2023 distinguishes generic polarities from stronger geometric axioms; it contains no general common-refiner theorem. Exact searches S67-07,09–12 found none.',
  'The manuscript itself says this is scarcely true except for set-like ateliers and isolates it as an extra axiom.',
  'Worth identifying the exact additional condition, not pursuing it as an unconditional conjecture.', ['LindenhoviusVetterlein2023','Janowitz1963'])
P(7,4,'Completeness and redundancy of the ML reconstruction',[7,8,9,10,11,13],
  'Recover the atelier from M, two orders and the locus graph, proving the ML lemmas and the final theorem without missing hypotheses.',
  'Use the strengthened ML1 lifting condition, nonempty interior loci, receiving-face coverage and the graph disjointness axiom. Restore the common-ambient hypothesis in Lemma1 and VII41 LemmaA before applying their conclusions.',
  'Speed1968 and Massas2023 establish the one-order/downset component. No exact ML0–5 two-order reconstruction was found in the recorded named-database and terminology searches S67-02–05,11,12. Malgoire2002 only confirms later exposition.',
  'The proof itself forces ML1 to be strengthened on VII28; later formulations replace the same machinery with Prat and Mag.',
  'Worth a rigorous proof consolidation because the strongest statement is already identifiable and several omitted hypotheses are localized.', ['Speed1968','Massas2023','Malgoire2002'])
P(7,5,'Which infinite figure families are determined by elementary data?',[12,51],
  'When does a preatelier determine its figures uniquely, and what must be added for infinite or locally finite figures?',
  'Finite deployments are forced precisely with finite principal ideals and lower compatible finite unions. Infinite figures require an explicit admitted lower family and join closure. Finite generation alone requires hereditary finite generation and is a distinct condition.',
  'The downset construction is standard (Speed1968; Massas2023), but no exact classification of the manuscript’s admissibility choices was found in S67-02–05,11,12.',
  'VII61 explicitly notes the extra choice for general figures, while VII114 omits lowerness in its finite formula.',
  'Worth stating as an elementary classification with counterexamples separating finite deployment and finite type.', ['Speed1968','Massas2023'])
P(7,6,'Dense test objects Λ and the failure of graph-only reconstruction',[14,15,16],
  'Can lieux be replaced by any dense Λ and compatibility reconstructed solely from disjointness on Λ?',
  'A dense testing family must also detect disjointness and satisfy the common-refiner lifting/locality axioms. Density alone is insufficient; keep the compatibility relation primitive until those implications are proved.',
  'No exact MΛ/PratΛ result was found in S67-02,03,11,12. Generic orthogonality closure in Lindenhovius–Vetterlein2023 does not supply a face/refinement relation or the missing lifting axiom.',
  'The author explicitly writes “Non” and cancels the attempted derivation at VII48–50.',
  'Worth preserving as a documented failed simplification, then testing the minimal repaired list.', ['LindenhoviusVetterlein2023','Malgoire2002'])
P(7,7,'Global set realization versus local lattice isomorphisms',[17,18,19],
  'Do the set-like locus axioms imply a faithful embedding in Fig(L), and are Pratquas1–4 sufficient?',
  'Separate local subfigure-lattice isomorphism, global injection, compatibility reflection and refinement reflection. The latter need additional hypotheses; strict/polyhedral refinement can remain stronger even with injection.',
  'Massas2023 Theorem2.30 answers the local lattice question only. The manuscript’s affine/PL and strict-refinement examples show the global converse fails. S67-02–05,11,12 found no exact later global reconstruction under just the written axioms.',
  'The author retracts successive converse proofs on VII58–59 and leaves the quasi-set adequacy claim tentative.',
  'Worth fixing the exact morphism/embedding definition before using this theory categorically.', ['Massas2023','Malgoire2002'])
P(7,8,'What algebraic structure do virtual supports have?',[20,21,22,23],
  'Are orthoclosed virtual supports distributive, and does empty intersection with a cosupport imply containment?',
  'In general they form a complete ortholattice. Orthomodularity and Boolean distributivity are extra properties. Under L2 plus a complete distinct-locus orthogonality graph the lattice is P(L), but this special case does not generalize.',
  'Lindenhovius–Vetterlein2023 Example3.3 gives the exact six-element nonorthomodular P4 support lattice; Lemma3.4 states the Dacey criterion for orthomodularity. Janowitz1963 p1241 verifies the older orthomodular identity.',
  'The manuscript later computes counterexamples and abandons the blanket Boolean expectation; there is no evidence that the general claim remained an open theorem.',
  'Worth classifying additional geometric hypotheses only; the unconditional Boolean question is already answered negatively.', ['LindenhoviusVetterlein2023','Janowitz1963'])
P(7,9,'Canonical supports for interval figures on a poset',[24,25],
  'Construct a canonical point/cell realization for intervals over an arbitrary poset, including intervals with empty interior.',
  'Start with a totally ordered interval model or explicitly impose intersection/face conditions on the poset. Formal cells can retain endpoint versus open-interval information, but a full functorial realization needs stated axioms.',
  'The opened VGF catalogue and Malgoire2002 give no exact interval realization theorem. S67-03,05,11,12 found no later publication matching the arbitrary-poset formulation. Standard Boolean/polarity representation does not preserve its incidence and refinement data automatically.',
  'VII70 makes a broad claim without checking all poset intersections, and VII72 asks for a canonical construction; the earlier III tronçon construction has narrower hypotheses.',
  'Worth a tightly bounded finite-poset audit followed by a total-order theorem.', ['Malgoire2002','CSGUnpublished','LindenhoviusVetterlein2023'])
P(7,10,'Existence of support realizations and redundancy of axioms',[27,28,29,30,31],
  'Find P with support subsets satisfying clauses(i)–(vi), and decide which compatibility, subdivision, lieu and separation clauses follow from the others.',
  'Exact disjointness plus singleton support for every p yields Σ≅P(P), but does not construct such a realization from an arbitrary atelier. Redundancy of geometric clauses needs explicit incidence/refinement arguments beyond the Boolean lattice.',
  'Massas2023 Theorem2.29 gives the complete atomic Boolean/powerset equivalence. Lindenhovius–Vetterlein2023 Example3.3 blocks a universal Boolean realization for arbitrary orthogonality spaces. No exact theorem settling all six atelier clauses was found in S67-01,07,09–12.',
  'The pages prove implications under Hyp/Hyp′ and then say the remaining clauses are presumed; the two-strand margin exposes a failure of Supp1 in a tempting example.',
  'Worth an axiom-independence table; begin with the proven singleton theorem and separate the unproved existence step.', ['Massas2023','LindenhoviusVetterlein2023'])
P(7,11,'Two-strand support computations and their geometric scope',[32,33],
  'Check the rectangle closure and resulting lattice-law failure in the two-strand example.',
  'The polarity calculation proves non-distributivity. A full geometric atelier must separately verify its incidence/refinement axioms, and the natural endpoint realization fails Supp1; no nonmodularity conclusion follows from the displayed distributivity witness alone.',
  'The saved finite-grid computation reproduces the exact relation mechanism. The general non-Boolean ortholattice phenomenon is established in Lindenhovius–Vetterlein2023, but that paper does not verify this particular geometric ficelle construction.',
  'The manuscript itself flags the support-representation failure and uses a phrase that should not be expanded from distributivity to modularity.',
  'Worth completing the dense-order model only if it is needed as a geometric example; the algebraic obstruction already has a smaller exact certificate.', ['LindenhoviusVetterlein2023','Janowitz1963'])
P(7,12,'Absorption, strong interiors and virtual differences',[34,35,36,37,38,39,40],
  'Identify the virtual open stratum, prove absorption into X from supp(X) and boundary-disjointness, and reconstruct refinement from virtual differences.',
  'Distinguish the strong interior {Y≪X:Y⊥∂X}, immediate refinement and closure of interior loci. Equalities between these require explicit absorption; without L1, nonempty strata can have empty locus-based interior support. A recursive reconstruction also needs well-foundedness or a different construction.',
  'Janowitz1963 and Lindenhovius–Vetterlein2023 supply the ortholattice/orthomodular distinction, but no exact absorption theorem for these two orders. S67-07,09–12 found none. The finite P4 model violates optional AtSupp1, so it does not settle versions that add that axiom.',
  'The26June marginal note calls absorption artificial; the author replaces interior supports by primitive interior disjointness later in VII.',
  'Worth clarifying the conditional lemmas as editorial foundations; pursuing universal absorption would ignore his own withdrawal.', ['Janowitz1963','LindenhoviusVetterlein2023'])
P(7,13,'Local Boolean support algebra inside one figure',[41,42,43,44,45],
  'For A⊆~F, does S_A preserve all Boolean operations and satisfy S_{A\B}=S_A∩cosupp(S_B), at least with L1?',
  'Order embedding and arbitrary joins follow from nonzero orthogonal interior contributions. The relative-complement law requires a stronger algebraic/geometric condition; L1–L3, C,D and old AtSupp do not suffice. Orthomodularity repairs the corresponding two-element ortholattice identity, but absorption versions need separate analysis.',
  'Exact published P4 match: Lindenhovius–Vetterlein2023 Example3.3; Dacey criterion in Lemma3.4. The saved clique-atelier certificate verifies every stated L1 rescue hypothesis and refutes its equation. It does not satisfy optional AtSupp1.',
  'The manuscript first marks the formal lemma false, computes P4, then retains a narrower L1 hope. The present certificate closes that narrower hope under the enumerated hypotheses.',
  'Worth using as a precise boundary theorem and asking which explicitly stated additional axiom repairs it; do not re-open the refuted version.', ['LindenhoviusVetterlein2023','Janowitz1963'])
P(7,14,'Subdivision and the open-support set-difference equality',[46],
  'For a subdivision, do interior contributions reconstruct X°, and does a point realization give |X°|=|X|\|∂X|?',
  'Keep the support-join assertion separate from the pointwise equality; specify which X° is used and supply the reverse inclusion or an absorption/separation axiom that proves it.',
  'The general singleton Boolean representation is standard (Massas2023 Theorem2.29), but does not identify the geometric open stratum without the missing link. Exact searches S67-07,11,12 found no result addressing that reverse inclusion.',
  'VII101 proves only one inclusion before the equality interpretation; notation changed at VII100.',
  'Worth a short targeted proof audit once the interior convention is fixed.', ['Massas2023','LindenhoviusVetterlein2023'])
P(7,15,'Primitive interior disjointness and the final Mag system',[47,48,49,50,51,52],
  'Replace the divisibility-dependent axioms by primitive interior disjointness, prove the Mag reconstruction and its overlap with compatibility-based structures.',
  'Use the final VII111 Mag1–4, least receiving faces rather than merely minimal ones, and lower compatible figure families. The locus-defined δ correspondence needs L1–L3 and C(spac); categorical equivalence awaits a morphism definition.',
  'No exact final Mag1–4 theorem was found in S67-02,03,11,12 or the opened CSG bibliography/Malgoire notice. Standard downset representation (Speed1968, Massas2023) supplies only the one-order part. The primary manuscript is the evidence for the full proposed reduction.',
  'The author explicitly restarts the theory at VII109–111 to avoid the empty-interior obstruction; earlier drafts are canceled, not parallel final definitions.',
  'Highest editorial priority: consolidate one final axiom system and its finite-figure reconstruction before beginning new research.', ['Speed1968','Massas2023','Malgoire2002','CSGUnpublished'])
