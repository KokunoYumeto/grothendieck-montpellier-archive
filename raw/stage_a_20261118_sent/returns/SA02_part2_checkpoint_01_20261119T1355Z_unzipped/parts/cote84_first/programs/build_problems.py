"""Hand-written problem catalogue, including problems closed on later sheets."""
from pathlib import Path
import json
P=Path(__file__).resolve().parent.parent
I={int(x['id'].split('-')[-1]):x for x in json.loads((P/'items.json').read_text())}
problems=[]
def Q(n,title,items,his,today,art,why,worth,refs):
 occ=[{'item':f'SA02-{i}','cote':'84','scans':I[i]['scans'],'lines':I[i]['lines']} for i in items]
 problems.append(dict(id=f'MP-SA02-{n:02}',title=title,occurrences=occ,as_he_states=his,plausible_today=today,state_of_art=art,why_open=why,worth=worth,refs=refs))
Q(1,'Signs in determinant-twisted duality',[2,3],
 'Check the middle mapg and the endpoint sign in the extension duality; then compare the quadratic-form and norm conventions.',
 'For an extension of invertible modules the alternating pairing gives endpoint signs−id andid. The discriminant identity has the minus specified at98 under the earlier definitions.',
 'The two97 checks close on that page. CL-SA02-001 gives a local basis proof; CL-SA02-002 is cross-checked against root calculations on47/53. Loos1997 is a comparison for pointed norm forms, not an authority for the doubtful ink.',
 'The author explicitly worries about signs and twice writes that the checks work; the remaining symbol uncertainty is transcriptional.',
 'A further research run is unnecessary for the elementary duality; scan inspection should settle the remaining signs.', ['Loos1997','Roby1963'])
Q(2,'Constructing the transpose into the tensor algebra',[4,5,6],
 'Find the mapA→A1⊗A2 from the extension product and its duality; the initial99 construction is cancelled.',
 'The transpose is defined by perfect line-valued pairings; in the quadratic case it is the algebra map of CL-SA02-005. Boundary agreement gives the pushout trace.',
 'Loos1997 §2.9 constructs the canonical map into diagonal invariants. The surviving100–105 route and the universal coefficient check settle the quadratic local construction.',
 'The abandoned99 block is replaced by a live transpose and trace construction, not left as a standing objection.',
 'Useful only as a short exposition and convention comparison, since the construction is already verified.', ['Loos1997','Voight2016'])
Q(3,'Existence and uniqueness of the nonflat relative norm',[8,13,14],
 'Define a quadraticA-valued norm onA1⊗A2 with pure-tensor valuesN1N2 and polarization given by the relative trace.',
 'For genuine quadratic inputs the explicit integral polynomial gives a unique multiplicativeA-quadratic law, natural by its characterization. It need not arise from a determinant of a locally freeA-module.',
 'CL-SA02-008–010 prove the coefficient formula and tower laws. Loos/Voight construct the contracted quadratic algebra. EGAII §6.5 gives norms for finite locally free algebras, plus a reduced generically free case with extra base-change restrictions. Ferrand1998 and Biesel2024 retain finite locally free base hypotheses.',
 '103 is tentative,105–106 states the characterization,107 closes the total-norm calculation. The author later isolates the nonflat obstacle for a more general triple construction; no stated reason for abandoning that broader programme is supplied.',
 'A focused run could give a clean basis-free theorem for this verified special norm and compare it precisely with universal polynomial-law norms.', ['Roby1963','Loos1997','Voight2016','EGAII','Ferrand1998','Biesel2024'])
Q(4,'When does the abstract product equal tensor invariants?',[7,30],
 'The canonical product map tends to be universally injective, but general injectivity and surjectivity are not known on104; the NB on102 gives a characteristic2/étale sufficient condition.',
 'For two inputs, (2,b1,b2)=R suffices for universal injectivity and equality with diagonal invariants. For three, outside characteristic2 points with at least two nonétale inputs the triple invariant map is an isomorphism. These are sufficient conditions, not claimed necessary.',
 'CL-SA02-006 proves the binary cover criterion directly. CL-SA02-024 proves the triple statement by eigenbasis when2 is a unit and by étale splitting otherwise. Loos1997 §2.8 warns that invariant modules can be too large and Prop2.9 gives the map.',
 'The source explicitly distinguishes its conditional result from the general uncertainty; the characteristic2 degenerations explain the warning.',
 'Worth a finite local classification of kernels and excess invariants, provided it is separated from the already settled sufficient criteria.', ['Loos1997','SGA1','Stacks04HN'])
Q(5,'Trace and norm transitivity through the contracted product',[14],
 'Check that the composed norm equals the ordinary norm of the rank-four tensor algebra; a tentative four-factor product is followed by anOK.',
 'For genuine quadratic inputs, the explicit relative norm and trace satisfy both transitivity identities over every base.',
 'CL-SA02-010 compares against the regular multiplication matrix exactly. Biesel Lemma2.6 proves the usual finite locally free tower theorem, which alone is insufficient here if the middle extension is nonflat.',
 'The local proof closes on107. The image map is suppressed in one line but the scalar map into the tensor algebra is faithful in this setting.',
 'No new theorem search is needed beyond a concise proof note and explicit handling of the suppressed map.', ['Biesel2024','Ferrand1998'])
Q(6,'Which quasi-quadratic axioms survive nonfaithful scalars?',[15,18,19,20,21],
 'Allow nonflatA/k and noninjectivek→A; impose the scalar polarization identity directly and list an optional tower law. The five numbered recap omits the earlier multiplicativity clause.',
 'Keep a strong definition with universally multiplicative quadratic norm separate from the weaker five-axiom definition. Faithful scalars recover multiplicativity from the other identities; nonfaithful scalars require additional hypotheses.',
 'TheZ/4 counterexample in CL-SA02-016 satisfies all five recap axioms as polynomial laws but fails multiplicativity. Roby1963 supplies quadratic-law extension; Chenevier2014 §1.19 gives the strong degree-two Cayley–Hamilton comparison. No exact later use of the manuscript term was found.',
 'The text deliberately permits noninjectivity but gives no explanation for the missing clause. It is not legitimate to decide from the algebra whether this is an intentional weakening or an abbreviated recap.',
 'High value for a short run: state the two categories precisely and determine which later constructions require the stronger one.', ['Roby1963','Chenevier2014','EGAII'])
Q(7,'Compatibility of base-changed norm diagrams',[24,25,26],
 'After matching pure tensors, verify equality of the associated bilinear forms in the norm diagram.',
 'Use the normn1, not the trace, and base change to the actual targetA2. Under all stipulated compatibilities the quadratic laws agree; norm compatibility recovers trace compatibility.',
 'The source writesOK at113. CL-SA02-020 checks the argument using Roby PropII.1, pp236–238. The two doubtful tokens remain in the reading ledger.',
 'This is a completed local proof obligation, not an open present-day problem.',
 'No separate research run is needed; checking the two symbols on the scans would stabilize the exposition.', ['Roby1963'])
Q(8,'Common scalar traces and norms in a quasi-biquadratic system',[27,28,29],
 'Find additive and multiplicative identities for the three relative structures; equality of composed scalar traces/norms is qualified by injectivity and, for traces, separately imposed otherwise.',
 'The four-conjugate identities hold inA; equality in the scalar ring requires injectivity or an explicit scalar-level axiom. The compatible symmetry group isΓ of order4.',
 'CL-SA02-021–023 give independent expansions and the finite parity check. The finite étale case lies inSGA1 Galois-set theory; generalized nonfaithful equalities do not follow from that case.',
 '115 replaces a cancelled expectation with a qualified calculation endingOK. The trace caveat is inserted explicitly on114.',
 'A future axiomatic comparison is useful only if it keeps image equalities and scalar equalities distinct.', ['SGA1','Biesel2024','Chenevier2014'])
Q(9,'Scalar image of the contracted triple product',[32,33,34],
 'For a compatible triple of quasi-quadratic subalgebras inA, withk→A injective for simplicity, prove thatB0→A lands ink·1.',
 'Scalar invariantsA^Γ=k suffice; they hold when2 is invertible. In characteristic2 they may fail even when the requested product image is scalar. The full broad compatibility system remains to be classified.',
 'CL-SA02-025 records a completeF2 counterexample to the stronger fixed-ring assertion and confirms scalar image in it; CL-SA02-026 proves the averaging case. No exact published theorem for the broad nonflat data was identified after the recorded biquadratic/quadratic-law searches.',
 'The author offers a sufficient condition, observes characteristic2 trouble, and proves only the2-invertible case here; no reason for later abandonment is stated.',
 'Worth developing after the precise quasi-quadratic axiom choice is fixed; one run could test the scalar-image assertion in controlled nilpotent families.', ['SGA1','Loos1997','Chenevier2014'])
Q(10,'The étale parity-fibre characterization and its lemma',[35,36],
 'Prove the direct direction carefully, reducing it to a transitive group action on a subscheme of a constant scheme; the proof closes on121.',
 'Retain allAi étale, scalar faithfulness, generation andA^Γ=k. Correct the standalone lemma to a closed subscheme with injectivity into its own global functions.',
 'CL-SA02-027 and056 give the repaired proof; CL-SA02-028 supplies both counterexamples to the literal and target-only repairs. Finite étale splitting and descent are available inSGA1 and Stacks04HN/09Y8.',
 'The local ideal argument is completed; its statement suppresses two conditions used by that argument. The main proposition already supplies closedness by generation.',
 'A short corrective commentary is useful; this is not a new open theorem after the hypotheses are made explicit.', ['SGA1','Stacks04HN','Stacks09Y8'])
Q(11,'Nonétale inverse images of a section',[38,39],
 'Generalize the canonical biquadratic structure to the inverse image of a section of a triple contracted product, without any étaleness assumption; construct relative traces and norms in the universal diagram.',
 'The fibre need not be finite locally free or flat; a viable statement must specify quasi-quadratic polynomial laws and their exact base module and scalar-compatibility requirements, without assigning ranks4 and2 automatically.',
 'CL-SA02-029 and051 separate finite/surjective from flat. The triple-dual-number example has an8-dimensional fibre and proves nonflatness. EGAII caseII covers reduced generically free situations under extra restrictions; Ferrand/Biesel do not cover this arbitrary nilpotent base. The exact universal construction remains unmatched in opened literature.',
 '122 explicitly names nonflatness as a difficulty, marks the proposed ranks and norm with question/exclamation marks, and ends with unfinished linearity/quadraticity conditions.',
 'The most promising substantial local research task, after the weak/strong axiom distinction is settled.', ['EGAII','Ferrand1998','Biesel2024','Loos1997','Chenevier2014'])
Q(12,'Equivalence of retraction and complementary-section compatibility',[42],
 'Does aπ=π′β hold if and only ifβω=ω′γ for the map of extension rows?',
 'Yes, assuming both complementary identitiesaπ+ωq=χI and the exact rows; subtract the identities and use the monomorphism/epimorphism, without dividing byχ.',
 'CL-SA02-030 gives the complete conditional proof. It is elementary exact-sequence algebra; no special literature theorem is needed.',
 'The sheet asks the equivalence and breaks off; the earlier-run answer is independently rechecked here.',
 'Closed under the stated assumptions; only the notation and diagram on the scan need confirmation.', ['SGA1'])
Q(13,'Functoriality on the correct extension morphisms',[44,64,66],
 'The product/comparison is declared functorial for isomorphisms and then homomorphisms;144 experiments with submodule-preserving endomorphisms.',
 'Use maps of exact rows preservingχ-retractions. Under that compatibility the pushout relation descends; arbitrary submodule-preserving maps do not suffice.',
 'CL-SA02-031 gives the boundary proof and045 the explicitχ=1 shear counterexample. Loos §2.10 andVoight Lemma3.18 establish their quadratic-algebra categories, not this broader unrestricted map class.',
 '126 asserts that it works;144’s example is unfinished and the final displayed equation reveals the missing compatibility. No written decision to abandon it appears.',
 'Worth a precise category definition; a few hours should settle the local functoriality once endpoints and scalar data are fixed.', ['Loos1997','Voight2016','Pirashvili2019'])
Q(14,'Comparing complementary constructions whenγχ=2',[45,46,47,49],
 'Find the translation changing the output coefficientb to−b and make it compatible with changes of splittings; assumeγχ=2 and choosev=−γb.',
 'This recipe works for a chosenγ under a coherent coordinate convention. It can depend onγ, and it is a comparison theorem rather than a condition for existence of the original product.',
 'CL-SA02-032 computes the square defect and034 checks choice dependence overZ/4. Pirashvili §3.1 hasp=−χ,q=γ but requires a rank-two torsor object and unit discriminant; it is only a specialized counterpart.',
 '128 introduces the hypothesis explicitly. Competing signs and identifications remain visible; the text does not assert uniqueness ofγ.',
 'Useful after the ink review: distinguish canonicalχ=2 comparison from the general chosen-γ comparison and its automorphisms.', ['Loos1997','Pirashvili2019'])
Q(15,'Transition cocycle and general coherence',[50,51,53,67],
 'ShowU″=U+U′ for successive changes of input splittings, and use the product formulas functorially.',
 'The plus convention satisfies the cocycle exactly. A full monoidal category also requires associativity, symmetry, unit constraints and coherence; these are not implied by the single cocycle.',
 'CL-SA02-036 checks both the working branch and the precise residual of the mixed convention. Loos1997 §§2.8–2.10 proves a coherent quadratic-algebra version. The unavailable Hua register cannot be used as a checked theorem.',
 '132 contains inconsistent intermediate conventions and an unfinished final expansion; no complete all-χ coherence argument occurs in this package.',
 'High value if posed as an explicit local category and global descent task, with comparisons to Loos restricted to their shared object class.', ['Loos1997','Pirashvili2019'])
Q(16,'The strange minus in products of functionals',[55,56,57,60],
 'Explain the negativeχ term for products of quotient-linear maps and its relation to the positive vector product.',
 'The negative sign follows from the functional formula at scalar restrictionsλ_i=0; the positive sign is the restriction of the vector product toL1⊗L2. They have different domains.',
 'CL-SA02-038–041 gives the coefficient calculation and separates the isolated erroneous2−χ=1 line. Loos’s duality/product conventions are an opened comparison, not a reason to overwrite the manuscript sign.',
 'The author writes signe étrange on134 and136, and later performs a restriction check; not all notation is stabilized.',
 'Worth an explanatory diagram with types after scan review, but it does not require a new general theorem.', ['Loos1997'])
Q(17,'Descent of the functional product and division byχ',[57,58],
 'Verify the functional product’s boundary compatibility; compareπ1*π2 withπ using the displayed1/χ notation.',
 'The functional prescription and scalar prescription agree on both mixed boundaries and overlap. The integral identity isπ1*π2=χπ; unique division needs additional hypotheses.',
 'CL-SA02-038 and040 check the exact polynomial identities. The source’s one-stratum verification closes withOK on138.',
 'The main restriction check is completed. The fraction notation does not by itself assertχ invertible and should not be promoted to a new hypothesis.',
 'Closed locally; a future global proof should keep the integral identity and avoid cancellingχ.', ['Loos1997','Pirashvili2019'])
Q(18,'Existence of the middle comparison blockF11',[61,62,63],
 'IfF11 can be defined with two prescribed composites, the comparison is an isomorphism. A candidate is written assumingγχ=2 and specialized atχ=2.',
 'The short-five-lemma implication is valid. Atχ=2 the candidate becomesI+σ1⊗σ2 underPi=a_iπ_i, and2-retractions correspond integrally to endpoint-sign involutions. Existence and all comparison squares remain separate.',
 'CL-SA02-042–044 checks the conditional implication, operator identity and involution correspondence. Loos proves coherence for quadratic algebras; Pirashvili’s torsor category is narrower than arbitrary modules.',
 'The opening is explicitly conditional; the formula uses doubtful primed operators and no completed four-square proof is given here.',
 'A focused next run could write the exact pushout/pullback maps and test the full comparison with fixed endpoint conventions.', ['Loos1997','Pirashvili2019'])
Q(19,'The standard conjectures recalled on the reused prose',[81,82,83],
 'The author questions the validity of the standard conjectures on cycles while treating the question as fundamental, and recalls pairing it with resolution atBombay1968.',
 'Separate algebraicity of Lefschetz operators, Künneth projectors and Hodge-type positivity for smooth projective varieties and a Weil cohomology; this leaf does not choose a narrower version.',
 'Grothendieck1969 pp195–198 gives exact formulations and implications. Deligne1974 proves the Weil estimate without settling the whole package. Agugliaro2025 Cor1.3 establishes Hodge-type positivity for powers of abelian threefolds over any field; the full programme remains open.',
 'The prose records a change of confidence and an assessment of importance, not a failed proof or a reason a specific attempted argument was abandoned.',
 'Historically central but too broad for a few-hour research task; a precise bibliographic companion is the realistic next step.', ['Grothendieck1969','Deligne1974','Agugliaro2025','GrothendieckRS'])
Q(20,'Resolution of singularities recalled with the standard conjectures',[83],
 'Resolution is named as one of two fundamental questions, with no choice of characteristic, base class or embedded/functorial formulation.',
 'Specify a birational regular-model problem before comparing results; alterations that enlarge the function field are a different assertion.',
 'Cossart–Piltant2019 Th1.1 gives proper birational regular models for reduced separated Noetherian quasi-excellent schemes of dimension≤3, preserving the regular locus. deJong1996 Th4.1 gives arbitrary-dimensional alterations of varieties. General positive-characteristic resolution remains open in the primary2026 status source.',
 'No proof attempt occurs here and no personal account explains why the general problem remained open; the leaf is a retrospective statement of priority.',
 'A new mathematical attack is not a bounded follow-up to these pages; the useful task is an exact historical and hypothesis concordance.', ['Grothendieck1969','CossartPiltant2019','deJong1996','Berczi2026'])
(P/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2))
print('Wrote',len(problems),'manually authored problems, including completed and withdrawn steps')
