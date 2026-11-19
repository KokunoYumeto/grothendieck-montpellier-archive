#!/usr/bin/env python3
"""Explicitly selected and formulated problems; shared fields copied from checked claim records."""
import json
from pathlib import Path
O=Path(__file__).resolve().parents[1]
C={int(x['id'].split('-')[-1]):x for x in json.loads((O/'claims.json').read_text())}
P=[]
def p(n,title,cc,question,today,why,worth):
 cs=[C[i] for i in cc]
 occ=[]
 for c in cs:
  for z in c['lines']:
   zz=dict(z,claim_id=c['id'])
   if zz not in occ:occ.append(zz)
 P.append(dict(id=f'MP-SA13-{n}',title=title,occurrences=occ,as_he_states=question,plausible_today=today,state_of_art=[{'claim_id':c['id'],'result':c['literature_fate'],'locators':c['references']} for c in cs],why_open=why,worth=worth,refs=list(dict.fromkeys(k for c in cs for k in c['refs'])),claim_ids=[c['id'] for c in cs],authorship=list(dict.fromkeys(c['authorship'] for c in cs))))
p(30,'Inverse Verdier pairing and external Hom comparison',[103,104,105],
'Construct the comparison in the reverse direction and prove that it is invertible; determine the external-Hom formula after the target bounds are revised.',
'Bounded constructible finite-Tor complexes over a separably closed field with invertible finite coefficients admit the well-typed Künneth/duality comparison. The literal η/β formulas still require collation.',
'The manuscript reduces the problem to a pairing and invokes resolution; Illusie documents the distinct historical finiteness and compatibility gaps. No personal motive for stopping is inferred.',
'High value for a companion: one focused run could identify the precise SGA5 exchange maps and separate existence from invertibility.')
p(31,'Local/global pairing and trace compatibility',[100,124,125],
'Show that the local correspondence pairing, after global sections and trace, agrees with the cohomological supertrace.',
'Use proper support and a perfect cohomology complex; the ordinary supertrace is defined for a bounded finite-projective model.',
'The page marks this verification; Illusie’s chronology explicitly confirms it was an obligation in the oral seminar.',
'High historical value and feasible: collate SGA5 III§4 and sign conventions.')
p(32,'Finite-flat resolutions and trace models',[125],
'Justify using complexes whose components are finite flat in the supertrace calculation.',
'A bounded finite-projective model suffices; degreewise finite flatness without a boundedness or perfectness argument does not.',
'The manuscript itself places a qualification in the margin; it does not supply the required bounded-model proof.',
'Worth a short proof audit, especially when transferring the trace construction to a different coefficient ring.')
p(33,'Pushforward of correspondences and the support counit',[123],
'Construct the displayed pushforward of correspondences through Ru_* and the indicated counit.',
'Use Ru_!u!→id, or assume u proper so Ru_!=Ru_*; specify any proper support restriction.',
'The transcribed diagram has no visible properness qualifier for u. This may be an omitted standing assumption or a misread star/exclamation mark.',
'High editorial value: a scan check can decide whether the repair is typographical or mathematical.')
p(34,'Constructible biduality and coefficient generality',[106,107,162],
'Establish local biduality on a regular noetherian scheme with locally constant coefficient rings and fibrewise dualizing complexes.',
'For excellent noetherian schemes with a dimension function and invertible Z/n coefficients, bounded constructible biduality is established; arbitrary noetherian coefficient sheaves need their own dualizing hypotheses.',
'The text lists coefficient generalizations but leaves their exact range open; the all-Dᵇ line omits the constructible restriction.',
'Worth developing as a hypothesis concordance, not as a new claim of universal biduality.')
p(35,'Unbounded constructible duality',[108],
'Extend D_X as an involution or anti-equivalence on the written D_c, D_c± and Dᵇ_c categories.',
'First fix constructibility, uniform finite quasi-injective amplitude and totalization conventions; bounded constructible duality is the verified baseline.',
'The page supplies no complete unbounded convention and cannot be settled solely by a bounded theorem.',
'Medium value: a few hours can produce a precise candidate and truncation proof or counterexample, but this task does not do that new research.')
p(36,'Uniform quasi-injective dimension and stalks',[109,110],
'Prove the equivalence (**) between a uniform Ext bound against all constructible tests and finite injective dimensions of geometric fibres, then derive the Gorenstein consequence.',
'A uniform global finite bound requires finite-dimensionality and careful internal/global Ext conventions; the coefficient-ring Gorenstein conclusion remains conditional on the comparison.',
'The reverse implication is only an instruction to use biduality; no uniformity proof appears.',
'High value: spell out the uniform quantifier and compare SGA5 I with ILO XVII6.2.')
p(37,'The proposed 2dim bound',[111,112],
'Verify the displayed Ext vanishing above2n, with stalk-flat or stalk-injective targets.',
'The internal dualizing-complex bound is established in finite-dimensional regular excellent scope. A global2n bound over an arbitrary field is false, as Spec F7 with F3 coefficients shows.',
'The page marks verification and changes field assumptions; internal versus global Ext is not securely transcribed.',
'Highest editorial priority because the same line changes from true to false under one missing sheaf mark.')
p(38,'Constructible approximation preserving injective stalks',[113,114],
'Is a sheaf with injective stalks a filtered colimit of constructible sheaves with injective stalks?',
'Keep the exact coefficient ring, noetherian topology and preservation condition explicit; no theorem establishing the manuscript’s full scope was found.',
'The manuscript asks this with double question marks. Ind-constructibility and injectivity of the whole sheaf are different facts.',
'High focused-research value: settle the finite self-injective coefficient case before considering arbitrary noetherian rings.')
p(39,'Spectral-sequence support polygons and top edge',[115,116],
'Complete the polygon inequalities and justify the proposed top-degree Ext edge isomorphism.',
'An exact theorem needs the spectral-sequence page, total grading, support-dimension convention and all vanishing regions. Ordinary-codimension reading fails the smooth-curve purity test.',
'The diagrams contain incomplete inequalities and ambiguous indices; no completed proof is on these leaves.',
'High value only after scan collation; symbolic completion before that risks solving an invented problem.')
p(40,'Perfect duality in localization',[117,118,119,120],
'Is the open-term pairing perfect, and do the displayed stalk/costalk and amplitude formulas have the stated indices?',
'Use finite-Tor constructible coefficients, normalized dualizing complexes and complementary supports; duality reverses cohomological shifts.',
'The page explicitly says dualité parfaite?? and retains competing Hom–tensor formulas.',
'Worth one careful derived-category calculation once the precise diagram and conventions are fixed.')
p(41,'Strict cohomological dimension estimates',[163],
'Bound injective/cohomological dimension by support dimension and fibre injective dimensions; consult Verdier’s notes.',
'Separate ordinary global cohomological dimension from geometric-local quasi-injective dimension and retain residue-field contributions.',
'The manuscript labels these possible applications and points to a source not supplied in the archive packet.',
'Medium value: exact recovery of the meaning of strict dimension is the first step.')
p(42,'Derived exterior powers and lambda operations',[126],
'Develop exterior powers in derived categories and related λ-ring structures.',
'Illusie and SGA6 develop substantial parts under precise categorical/coefficient hypotheses; the page is a programme rather than one universal theorem.',
'No cancellation or reason for abandoning this programme is recorded; later publication is not proof that every intended variant was completed.',
'Medium historical value: a source concordance is achievable in a few hours; a new universal theory is not the next step.')
p(43,'Analytic duality and cohomological descent',[127],
'Develop analytic duality and cohomological descent with analytic/algebraic finiteness applications.',
'Ramis–Ruget1970 provides a precise coherent-analytic duality theorem; descent and coefficient ranges must be specified independently.',
'The leaf offers only programme headings, so no single missing proof or personal reason is recoverable.',
'Medium value: build a bibliographic concordance preserving the separation between analytic duality and descent.')
p(44,'Quasi-coherent Künneth and the stratifying site',[128],
'Extend Künneth to quasi-coherent complexes and duality to differential complexes and the stratifying site.',
'No unique statement is recoverable without definitions of the site, complexes and allowable tensor operations.',
'The passage is a list of research topics without a theorem or construction; literature similarity cannot determine the intended formulation.',
'Low immediate research yield until the surrounding manuscript definitions are located.')
p(45,'Lefschetz and depth applications',[129],
'Use the proposed bounds for local/global cohomological Lefschetz theorems and depth phenomena.',
'Classical SGA2 and later results establish defined variants; the partly cancelled programme is broader and underspecified.',
'The application paragraph is cancelled, but the sources give no reason and no counterexample.',
'Medium value: cross-reference the root shard’s precise SGA2 XIV6.2–6.3 problem before cutting a research task.')
p(46,'Roos minimum-topos characterization',[130],
'Prove the deferred representable criterion(A),(B) and hence the minimum-topos characterization of the small Zariski topos.',
'The completed étalé-space equivalence is clear; the exact affine-homeomorphism and filtered-limit criterion needs a direct proof and EGA8.14 collation.',
'The typescript explicitly postpones the lemma to§3. Published SGA4VII is a related, differently authored redaction.',
'High source-history value: identify whether the deferred§3 survives in another archive folder.')
p(47,'Universe bookkeeping and another small/big comparison',[131,135],
'Check the change of universe and later reuse of the small/big-site comparison proof.',
'SGA4VII4.1 and its universe footnote give a precise small/big étale comparison; this does not identify the whole big topos with the small one.',
'The reader is assigned the universe check; another topology is promised without naming it on the reused leaf.',
'Useful short companion task; no unresolved foundational crisis is inferred.')
p(48,'EVT separation and editorial dependency',[150,151,152],
'Check that the revised separation theorem suffices, and that deleting the Krein–Milman preparatory material does not break the new Intégration edition.',
'The convexity statements can be proved under their stated separation assumptions; the editorial dependency needs the exact old and revised editions.',
'The leaf itself asks for the dependency check. The underlying old-book statements and edition are absent.',
'Medium historical value; first identify Tribu63/53 and the precise edition rather than attributing these reused pages to the handwriter.')
p(49,'Completeness and inductive topology of direct sums',[153,154],
'Prove that a direct sum of complete locally convex spaces is complete and that the reorganized E has the intended inductive-limit topology.',
'The complete Hausdorff locally convex direct-sum theorem is proved in this review; equality with a specific inductive-limit topology still needs its E_n and topology.',
'The source postpones completeness to a theorem of Grothendieck and directs a later editorial definition.',
'Low need for new mathematics, high usefulness for recovering the intended dependency structure.')
p(50,'Vague metrizability and the missing false proposition',[155],
'Identify the last sentence of old Proposition11 said to imply false vague metrizability, and the hypotheses of the proper-addition cone statement.',
'Product-positive-cone properness has a direct proof; the general metrizability assertion is not identifiable from this fragment.',
'The old proposition itself is not supplied, so neither its original quantifiers nor the author of the correction can be recovered.',
'Worth source identification, not a new proof of an absent theorem.')
p(51,'Common-completion lemma and quadratic sequences',[156,157,158],
'Verify the delegated local-algebra lemmas and the quadratic-transform chain assertions, retaining the distinct source-identification obligations.',
'The full Lemma2 recovered across33:173→137→135 assumes R⊂Rbar regular local domains of the same dimension, common residue field and mRbar=mbar. It gives equal completions, ideal contraction, descent of principality and Frac(R)∩Rbar=R. The quadratic-sequence claim still needs its own valuation and absent-lemma hypotheses.',
'The common-completion mathematical statement is now recovered and independently proved. What remains unresolved is the exact printed source and the separate C158 dependencies[A6]/[A7] and Lemmas9–10; no universal termination claim follows.',
'High source-identification value: recover the original reference and quadratic-sequence dependencies; the common-completion proof itself need not be redone.')
p(52,'Operator symbol and regularization source',[159,160],
'Prove the printed symbol epimorphism with compact kernel and the asserted regularization criterion with unchanged solutions.',
'A parametrix modulo compact operators gives Fredholm reduction. Equality of solution sets requires control of kerK in addition.',
'The printed proof cuts off before the final adjustment and the operator algebra/function space is defined on missing pages.',
'High bibliographic value but low research value until the source and full proof are identified.')
p(53,'Gegenbauer integral evaluation and normalization',[161],
'Evaluate the two parity-dependent integrals for γ_n and compare with the missing result referred to as[18a].',
'For standard C_n^λ, beta/digamma formulas and low-degree tests are verified; the missing w_p normalization prevents certification of the original final formula.',
'The odd integrand lacks an n subscript and the referenced identity is not supplied.',
'Good short task after source identification; the present certificates already isolate what can be checked without inventing normalization.')
p(54,'Néron-model and invariant-cycle promises',[140],
'Explain the promised relation between special-fibre cohomology and inertia invariants of the generic fibre.',
'Local invariant cycle statements need regularity, properness and rational/integral coefficient scope fixed; no universal integral isomorphism follows from the introduction.',
'The introduction says in certain cases and gives no theorem or proof.',
'Medium value as a bridge to the later SGA7 pages; first collate the exact subsequent hypotheses.')
p(55,'Picard restriction and missing genericity',[141],
'Assess the announced degree≥4 surface Picard isomorphism in arbitrary characteristic.',
'The universal statement is false; a very-general Noether–Lefschetz statement is the plausible repair, with characteristic and torsion qualifications.',
'No genericity word appears in the supplied transcription. It could be an omission or a scan issue; no motive is inferred.',
'Highest scan priority; the Fermat quartic certificate settles the mathematical consequence of the literal wording.')
p(56,'Tame-inertia map under ramified base change',[146],
'Determine the homomorphism on tame inertia for a dominant trait map.',
'It is multiplication by the ramification indexe in the canonical Tate module; integral invertibility requires ℓ∤e.',
'This question is answered by Proposition3.12 on the next leaf. It belongs in the historical problem index as resolved on the pages.',
'No new research needed; retain the completed calculation as a dependency for later monodromy.')
p(57,'Completion and cancelled excellence hypothesis',[147],
'Prove that completion preserves the full inertia/Galois exact sequence after removing excellence.',
'SGA4X2.2.1 proves equivalence of finite étale fraction-field algebras for any henselian DVR and its completion.',
'The first proof is cancelled; the next page supplies an approximation proof. The exact theorem needs no excellence.',
'Useful companion audit of the replacement proof; no need to revive the cancelled hypothesis.')
p(58,'Inertia intersection and inseparable residue index',[148],
'Check I′=I∩π′ and interpret[I:I′] in terms of ramification.',
'For finite separable extensions of henselian DVR fraction fields, the intersection holds; the index includes inseparable residue degreee f_i.',
'The text expressly asks to verify the intersection and inserts the inseparable correction.',
'High editorial value because the adjacent π′0→π′ label is ill-typed, while the intended theorem is standard.')
p(59,'Central tame quotient and splitting',[149],
'Deduce the final central extension from canonical equivariance of tame inertia.',
'1→I′_t→I/P′→I/I′→1 is central for open normalI′⊂I; no splitting is asserted.',
'The proof is a transport-of-structure sketch; the earlier notes rightly separate centrality from splitting.',
'No new research needed; a short proof and the C((t)) nonsplitting example suffice.')
# Supplementary Codex problems, using the extension granted by the parent.
p(160,'Quasi-unipotent envelope and splitting choices',[173,174,175,176,178,179],
'Construct the algebraic envelope and its canonical filtration, splitting and tensor-category description.',
'Connected-unipotent envelope and nilpotent-operator descriptions are established. Splittings are generally unique only up to unipotent conjugacy, and H⁰(Γ,V) need not vanish.',
'The draft includes cancelled filtrations and an unfinished continuation; false uniqueness cannot be fixed by H¹-vanishing alone.',
'High value: identify exactly which functorial constructions survive after removing the noncanonical splitting.')
p(161,'General-radical extension of the coinvariant criterion',[180,181],
'Extend the solvable-image argument to the radical of an arbitrary connected algebraic image, using the asserted isogeny to its abelianization.',
'The torus quotient can be controlled, but R/[R,R]→H/[H,H] is not generally an isogeny; SL2⋉Ga² refutes that step.',
'The revised argument contains this unsupported structural claim, not merely a missing reference.',
'High short-task value: rewrite the proof using the reductive quotient and distinguish torus from unipotent kernels.')
p(162,'Geometric local monodromy conjecture',[184],
'Prove inertia quasi-unipotence on every degree of ordinary and compact-support cohomology of a finite-type variety over a henselian DVR fraction field.',
'The full invertible-ℓ theorem is established; it does not require the strong-resolution hypothesis of the draft proof route.',
'The pages label it conjecture and develop reductions; Illusie1994 records the later smoothing route.',
'High historical value, low new-research need: map draft reductions to the final theorem.')
p(163,'Degreewise integral and independent inertia traces',[185,186],
'Show that the trace of each inertia element in each degree is a nonnegative integer independent ofℓ.',
'Nonnegative is false, already trace−2 for a quadratic elliptic twist. Replace by rational integer and distinguish degreewise statements from verified alternating-trace independence.',
'The draft proposes it explicitly. Kato/Lu–Zheng only settle the broader generality after taking alternating sums, so they do not close this exact formulation.',
'High research interest; first isolate smooth proper, H¹ and general nonproper scopes in a precise theorem matrix.')
p(164,'Weil traces, weights and a common rational model',[187,188],
'Find a common rational local-monodromy representation with the stated Weil eigenvalue weights.',
'Trace compatibility, individual-degree weights and descent toQ are separate assertions. A rational character need not admit aQ-model, as the manuscript’s own warning observes.',
'The text adds an obstruction to rational realizability; no claim that weight–monodromy is fully solved is justified.',
'High conceptual value but limited one-run reach: formulate the exact coefficient-field and degree conditions first.')
p(165,'Regular trait approximation and local uniformization',[189,190],
'Obtain cofinal regular models with smooth divisor and prove the normal-crossings prime-to-p fundamental-group calculation.',
'Characteristic-zero resolution gives the model reduction; higher-dimensional tame Kummer structure uses purity/Abhyankar. General monodromy has other proofs.',
'The pages explicitly make the positive/mixed-characteristic route conditional on local uniformization; the normal-crossings demonstration is left to the reader.',
'Medium historical interest; do not mistake the eventual monodromy theorem for a solution of strong resolution.')
p(166,'Nonproper cohomology in the spreading argument',[191,192],
'Extend the proper spreading proof without a properness hypothesis.',
'Ordinary direct-image constructibility and generic base-change/finiteness supply the missing input in the verified modern scope.',
'The page marks this as requiring an additional finiteness statement; shrinking separately for everyℓ-power is not by itself one common open.',
'High proof-audit value: identify the common adic open and the exact finiteness theorem.')
p(167,'Birational and descent reductions',[193,194,195],
'Relate H and Hc, prove birational invariance of the monodromy property under induction, and reduce by resolution and proper descent.',
'Use complementary degree in Poincaré duality, the correct compact-support localization triangle and resolution in all dimensions needed for Čech powers.',
'The draft cancels a narrower proposition and replaces it on34:50; several displayed arrows or degrees are defective.',
'High companion value: a finite diagram audit can turn the surviving sketch into a readable conditional proof.')
p(168,'The unfinished H1 curve reduction',[197,198,223,227,228],
'Complete Proposition9.8 and transfer H¹ monodromy through a generic curve and a dominating valuation.',
'The curve/fundamental-group and boundary arguments give the result with controlled valuations; arbitrary dominating valuation must not be assumed to have open inertia image.',
'Proposition9.8 is blank on34:51; later pages provide most of the construction and leave valuation and degree labels imprecise.',
'High short-task value after scan collation, especially for the final H²/H¹ line.')
p(169,'Finite geometric abelian coinvariants',[199,200,219,220,221,223,225],
'Prove finiteness of the geometric pro-ℓ abelian coinvariants under arithmetic Galois action and eventual vanishing for almost allℓ.',
'For the stated normal geometrically connected finite-type schemes over finitely generated fields, the draft’s later curve and finite-field argument establishes the conclusion.',
'The early theorem is a deferred task, substantially discharged by§§2–4. Published SGA7II has a different author/topic and is not an exact numbering match.',
'High historical value: write a dependency map and identify any later publication of this exact exposition.')
p(170,'Abelian schemes with solvable or unipotent monodromy',[203,204,205],
'Adapt the cited constant-part theorem to essentially solvable or unipotent geometric Tate action, including radicial isogeny and level rigidity.',
'Geometric semisimplicity and the abelian-scheme constant-part theorem yield the corrected conclusion; char0 turns radicial isogeny into an isomorphism.',
'The draft cites Grothendieck1966Prop4.4, but this run only verified the bibliographic record, not that proposition’s exact text.',
'Highest literature-follow-up priority: obtain and collateProp4.4 before calling the manuscript a literal draft of it.')
p(171,'Potential isotriviality and constant field extensions',[206],
'Deduce a constant abelian variety after an extension explicitly written K′=Kk′.',
'A finite extension ofK may be required that is not constant: the CM twist y²=x³−t²x overQ(t) needs√t. The proof’s finite étale cover has the broader correct scope.',
'The conclusion and the proof use different kinds of extension; the explicit twist refutes the literal constant-only requirement.',
'High editorial priority; check the prime and field labels on34:59 before propagating the theorem.')
p(172,'Potentially solvable Tate action and CM',[207,208,216],
'Prove that essentially solvable Tate action forces CM and use it to obtain potential good reduction, including at the coefficient prime.',
'For number fields, Faltings semisimplicity and the endomorphism theorem give the CM implication; CM gives potential good reduction at all finite places.',
'The author identifies semisimplicity and cross-ℓ comparison as missing inputs. The printed later Frobenius argument treats only nilpotent image.',
'High historical value; a rigorous proof of the modern implication is short once the exact Faltings theorem is inserted.')
p(173,'Killing the unipotent factor by Frobenius density',[211,212],
'Prove U=1 in the nilpotent algebraic monodromy group.',
'The same leaf discharges it using semisimple Frobenius elements, density and the torus×unipotent decomposition of a connected nilpotent group.',
'This is resolved on the supplied pages; it is not a surviving conjecture about arbitrary solvable groups.',
'No new research needed; preserve the local resolution and its restricted group-theoretic scope.')
p(174,'Geometric semisimplicity and motivic extension',[209,210,229],
'Prove geometric semisimplicity of smooth-family cohomology and extend the solvable-monodromy arguments once motives are founded.',
'Deligne WeilII Cor3.4.13 settles smooth proper geometric semisimplicity over a normal connected base. General arithmetic/motivic semisimplicity is a different problem.',
'The earlier abelian-scheme footnote is cancelled after a direct argument; the later broader conjecture remains explicit on the pages.',
'High historical interest: exact theorem matching is now possible, while the motivic programme needs a separate task.')
p(175,'Good reduction and p-adic inertia semisimplicity',[213,214,215],
'Prove potential good reduction iff the inertia representation is semisimple, even whenℓ equals residue characteristic.',
'Theℓ≠p equivalence is established. Thep-adic converse is false by a non-torsion ordinary Serre–Tate good-reduction lift; the sufficiency direction needs its own exact hypotheses.',
'The manuscript refers the proof to a later exposé and begins a toric-rank argument. SGA7IX5.13 uses Barsotti–Tate good reduction, not this equivalence.',
'Highest mathematical priority for the companion: keep the false converse, the plausible sufficiency, and the actual BT theorem separate.')
p(176,'Invariants, coinvariants and the open-curve twist',[219,220,222,226],
'Check the dual formulation and the finite-field corollary, and justify the warning that invariants alone do not control coinvariants.',
'Dual invariants characterize finite coinvariants under finite generation; Gysin has twist−1; the finite-field pro-ℓ target isZℓ, not allZhat.',
'The argument is mostly present but has a sign reversal and a mismatched target; the warning itself is sound.',
'High editorial value with a short linear-algebra and Gysin audit.')
p(177,'Nonabelian solvable pro-ell coinvariants',[230],
'The wholly cancelled remark proposes an open commutator subgroup for a solvable pro-ℓ geometric quotient.',
'The action, commutator closure and ambient group of openness must first be specified; no exact surviving conjecture is identifiable.',
'The remark is cancelled and breaks off. Sources do not say why; no later theorem can be assigned to the ambiguous wording.',
'Low immediate value until scan and surrounding-text recovery identify a definite statement.')
p(178,'The EVT cap exercise and its missing definition',[241,233],
'Replace the extreme point x by a chapeau in the preceding corollary.',
'A precise cap version requires the source definition and original corollary; the compact extreme-point slice statement alone is established here.',
'The reused editorial sheet omits its prior definitions. No abandonment or unresolved modern conjecture is inferred from this exercise.',
'Low research priority but useful editorial task: identify the exact Bourbaki edition and recover the definition before formulating a theorem.')
(O/'problems.json').write_text(json.dumps(P,ensure_ascii=False,indent=2)+'\n')
print(f'Saved {len(P)} manually selected problem records; all inherit opened-source fate locators and exact global passage coordinates.')
