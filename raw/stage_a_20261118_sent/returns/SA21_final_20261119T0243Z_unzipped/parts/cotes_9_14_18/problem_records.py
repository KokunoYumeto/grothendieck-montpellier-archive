"""Hand-consolidated open-step index for IX14–18. No keyword verdicts."""
from claim_records import locations
PROBLEMS=[]
def P(n,title,spec,as_he,plausible,state,why,worth,refs):
    lines,_=locations(spec)
    PROBLEMS.append(dict(id=f'MP-SA21-9-{n:02d}',title=title,occurrences=lines,
      as_he_states=as_he,plausible_today=plausible,state_of_art=state,
      why_open=why,worth=worth,refs=refs))

P(20,'Which powerset-map identities survive for general spatios?',[(14,[107,108])],
 'For conjugate join maps of spatios, determine when orthogonality preservation implies meet/difference preservation and, with top preservation, complement preservation; he hopes suitable commensurable or constructible supports suffice.',
 'The unrestricted implication is false even for a complete lattice embedding B4→O6 preserving orthogonality and top. A useful correct formulation must require Boolean compatibility of the images of the relevant complementary partitions, or specify an equivalent exact hypothesis.',
 'As of2026-11-19: C-SA21-9-086 and certificate general_spatios_corollary_failure give an independent negative answer in the unrestricted case. Janowitz1963 pp1241–1242 treats orthogonal adjoints in orthomodular lattices; Paseka–Vetterlein2025§§3–4 treats adjointable orthoset maps with explicit hypotheses. Neither is an exact theorem for the manuscript’s unspecified constructible restriction. Searches S9E-01–05 plus shared S67 relation/support families found no exact matching formulation.',
 'On scan107 he says his proofs use severe hypotheses close to Booleanity and worries that global supports create irrelevant problems; no external historical reason for abandonment was found.',
 'Worth a narrowly defined follow-up: characterize the image-partition condition for complement preservation before attaching geometric terminology.',
 ['Janowitz1963','PasekaVetterlein2025','Ore1944'])
P(21,'Both conjugate maps preserve complement: are they inverse?',[(14,[108])],
 'If α_* and its orthogonal transpose β_* both commute with complement, are they inverse spatios isomorphisms?',
 'Yes, for complete ortholattices and exact conjugacy u(a)⊥b iff a⊥v(b); no Boolean or orthomodular hypothesis is needed.',
 'Independent proof C-SA21-9-088/R-SA21-9E-002: complement converts the conjugacy into both u⊣v and v⊣u. Ore1944 gives the older Galois framework; Janowitz1963 p1242 records orthogonal adjoints, while Paseka–Vetterlein2025 uses the same exact conjugacy. The manuscript itself inserts “oui”.',
 'The page answers the question affirmatively in the margin but leaves the proof unwritten.',
 'No separate research project is needed; include the two-adjunction proof in the folder commentary.',
 ['Ore1944','Janowitz1963','PasekaVetterlein2025'])
P(22,'Do the Boolean-pair conditions always hold, or force global Booleanity?',[(14,[109,111]),(15,[113,117])],
 'Are the comparable-pair/orthogonal-family conditions automatic for spatios, at least finite ones, and if imposed do they force Σ Boolean, perhaps after strengthening to infinite orthogonal families?',
 'They characterize orthomodularity, not Booleanity. O6 disproves automatic validity; MO2 is complete, nonBoolean and satisfies the arbitrary-orthogonal-family condition. The10-element manuscript example needs the listed ink checks before literal acceptance.',
 'C-SA21-9-090–095,098; Janowitz1963 p1241 and Lemma1 identify the standard orthomodular/commutation condition. Harding–Navara2011 discusses MO2 and Boolean subalgebras. Finite certificates check all hypotheses and the infinite-family reduction for MO2. The original Dacey1968 thesis was sought but not obtained; LV2023 Lemma3.4 supplies the modern exact criterion.',
 'The author recognizes the issue locally and supplies a later diagram; the pages do not connect his condition to the established name orthomodularity.',
 'Worth resolving in the commentary through a terminology concordance and the two smallest countermodels, with no claim of a new open problem.',
 ['Janowitz1963','HardingNavara2011','LindenhoviusVetterlein2023'])
P(23,'Orthomodularity of strict-comparability polarities of posets',[(14,[111])],
 'Determine what happens when the disjoncteur relation on an ordered set is x<y or y<x.',
 'Not always orthomodular: the height-two poset0<1,2<1,2<3 has comparability graphP4 and support latticeO6. A classification would require further order-theoretic hypotheses.',
 'C-SA21-9-094/R-SA21-9E-004. LV2023 Example3.3 and Jenča2024preprint/2026publication Example2.6 give the exact P4 obstruction; its orientation as the manuscript’s strict-comparability relation is verified here. Jenča2026 Theorem4.2 concerns INcomparability, so it is only a neighboring result. An11Aug2026 correction exists; its metadata were opened, but the corrected theorem was not accessible and is not asserted.',
 'The manuscript leaves this special model for later verification. No source was found explaining why it was not pursued.',
 'Worth a separate bounded project only after fixing comparability versus incomparability; the universal yes/no question is already negative.',
 ['LindenhoviusVetterlein2023','Jenca2026','JencaCorrection2026'])
P(24,'Can commensurable refinement form an atelier?',[(16,[119,120,121,122,123])],
 'Can one restrict spatial figures to commensurable supports and strengthen refinement by joint commensurability, while preserving transitivity? Are residue-family tests sufficient for entire diagrams?',
 'For arbitrary complete ortholattices the strengthened refinement of commensurable discrete figures is nontransitive. The residual criterion is valid after explicitly requiring each predecessor-fiber plus residue to reconstruct its parent; this is available underγ². Orthomodular ambient lattices avoid these particular nonBoolean-block defects.',
 'C-SA21-9-100–105; R-SA21-9E-007,008. The18-element certificate verifies the complete ortholattice and the two adjacent Boolean8 subalgebras, while endpoint generation yields nonBoolean18. Janowitz1963 Lemma1 explains why orthomodularity improves compatibility. No exact later publication of this atelier construction was identified in S9E-01–07 and shared support searches.',
 'On scan123 he explicitly identifies the possible nontransitivity and says the proposed construction does not seem to work; he also questions whether it is expressible on strata alone.',
 'Worth a follow-up on corrected categorical objects or additional hypotheses, starting from the saved18-element obstruction.',
 ['Janowitz1963','HardingNavara2011','CSGUnpublished'])
P(25,'Does faithful external support imply joint commensurability?',[(16,[124])],
 'Does a faithful external support in VIIIp62 implyγ³, especially for faithful morphisms? He compares a Corollaire1 at an uncertain page71/74.',
 'No for faithfulness as explicitly defined in VIII68–71: a normalized faithful external realization of the discrete P4 atelier fails even supp1. Full faithfulness is a different, stronger condition and must be investigated separately.',
 'C-SA21-9-106/R-SA21-9E-005 and its complete certificate give the negative answer. Both source endpoints were read: VIII68 conditions(i)–(iv), VIII71 Suppfid, and VIII87 Corollary1, which actually uses full faithfulness. LV2023 Example3.3 supplies the established P4 lattice; the external realization is our independently checked construction. No exact published atelier theorem was found by the bounded searches.',
 'The page explicitly leaves the implication to check. Its cross-reference is uncertain and the actual earlier corollary has a stronger hypothesis.',
 'Worth including the counterexample immediately; a new research run should address the fully faithful version rather than repeat the false weaker implication.',
 ['LindenhoviusVetterlein2023','CSGUnpublished','Malgoire2002'])
P(26,'Intrinsic constructible supports and localization by subdivisions',[(16,[124,125]),(17,[126,127,128])],
 'Construct the supports relevant to a figure independently of the global spatios, with complement and partially defined commensurable joins/meets; possibly recover closed constructible supports by inverting subdivisions in(F,≪). Is the resulting category thin and does it embed inΣ?',
 'Specify the partial algebra and the actual classW first. A calculus of fractions/common-refinement theorem can make localization manageable, but a separate theorem must prove thinness and identify the support image. None follows merely becauseF is a poset.',
 'C-SA21-9-107,108. Stacks§4.27 Definition4.27.1 and Lemma4.27.2 give exact sufficient conditions for the fraction construction and cite Gabriel–Zisman1967I§2. SGA4II§§1–2 and Esquisse§5 are useful conceptual comparisons, not this construction. Named-database and exact-term searches found no matching atelier theorem. The original Gabriel–Zisman book was not inspected.',
 'Scans124–127 explicitly object to composing unrelated supports and state uncertainty about both thinness and the embedding; scan128 lists other tasks to pursue first.',
 'High-interest follow-up once the subdivision axiom is fixed: check the Ore square condition on small explicit ateliers and state the intended universal property.',
 ['Stacks04VB','SGA4II','Esquisse1997','CSGUnpublished'])
P(27,'Support embeddings for four subatelier constructions',[(17,[130,131])],
 'For open-shadow, figure/maquette, strict residual and compatible broad-residual subateliers, verifyΣ_A′↪Σ_A.',
 'Each case needs a specified map and specified preserved operations. Candidate maps by ambient closure are generally different from literal inclusion of subsets; an orthogonal adjunction or a separation criterion may provide an embedding.',
 'C-SA21-9-110–115. Ore1944 gives general polarity closure; Paseka–Vetterlein2025 Lemmas3.7–3.8 describes consequences of adjointability, which cannot be assumed for arbitrary inclusion. The exact four constructions have no matched published embedding theorem in S9E-01,03–05/sharedS67 atelier searches.',
 'The question is explicit after the four examples; no proof or later resolution occurs in the owned pages.',
 'Worth one bounded run that checks the four cases separately and records which lattice operations each candidate embedding preserves.',
 ['Ore1944','PasekaVetterlein2025','CSGUnpublished'])
P(28,'From provisional atelier morphisms to virtual-support maps',[(17,[132,133]),(18,[134,135,136,137])],
 'Choose a morphism notion covering subateliers, inverse images and injective direct images, then determine whether it always induces a conjugate correspondence on associated spatios and whether its kernel is a support.',
 'The bare three-relation pointed maps form a category and have open-refinement-lower kernels, but automatic support-closedness fails. A closure-compatible or adjointable morphism condition must be added; the elementary-generator map must also be distinguished from full figure pullback.',
 'C-SA21-9-116–121/R-SA21-9E-009,010. The P4endpoint-deletion certificate verifies a nonclosed kernel under exact IX134zero conventions. Paseka–Vetterlein2025 Lemma3.8 proves closed kernels under adjointability, a stronger hypothesis; IX90–97 itself already requires closure compatibility for lifted correspondences. No exact published atelier equivalence was found.',
 'Definition134 is explicitly provisional, omits earlier VIII condition(d), and scan135 already anticipates supplementary conditions; scan137 defers the support analysis.',
 'High-interest follow-up: compare the provisional category with the closure-compatible morphisms already developed earlier in IX.',
 ['PasekaVetterlein2025','Ore1944','CSGUnpublished'])
P(29,'Universal excision by an open-refinement-lower subset',[(18,[135,136,137])],
 'ForN lower under≪°, constructA/N universal among maps killingN, and decide whether its kernel is exactlyN. Treat the set-figure example and maquettes.',
 'The maquette constructionA\\N is valid for everyN with the provisional zero conventions. The general existence and exact-kernel properties require proof in the actual atelier axiom class; the set example must separate closed-support killing from open-top-stratum killing.',
 'C-SA21-9-122–124. The maquette universal property is independently proved, including incidence acrossN. Exact searches for Grothendieck atelier/excision yielded no published general solution. Stacks localization is an adjacent universal construction, not an answer to this quotient problem.',
 'Scan137 says even the set case does not look obvious and explicitly leaves the support formalism aside; no external explanation for subsequent abandonment was found.',
 'Worth a follow-up beginning with finite set figures and exact kernels; the maquette base case is already resolved.',
 ['CSGUnpublished','Malgoire2002','Stacks04VB'])
P(30,'A direct image of figures for a noninjective set map',[(17,[133])],
 'He doubts that there is a direct figure map for noninjectiveg:E→E′ and asks for a support-level test of the injective direct-image case.',
 'The naive images of open strata can overlap and fail to form a figure. A canonical corrected pushforward would need a specified coarsening rule or universal property. At support level, a disjointness-preserving relation map is direct image by an injection exactly when its transpose preserves complement.',
 'C-SA21-9-118,119 and exhaustive set_relation_classification settle the support criterion. Ore1944/Massas2023 establish the relation/powerset context; they do not construct a corrected figure pushforward. The exact atelier/figure searches found no such publication.',
 'The source gives only the obstruction expectation and an uncertain marginal criterion, not a functorial definition.',
 'Worth only after deciding which face/incidence data a pushforward must retain; the support criterion needs no further research.',
 ['Ore1944','Massas2023','CSGUnpublished'])
P(31,'Final subdivision axioms and local support detection',[(18,[138,139,140])],
 'Compare fiberwise coverage, total support equality, absence of disjoint refining strata/loci, and face-inclusion maximality; a quotient-topology strengthening is considered and canceled.',
 'Fiberwise versus total equality is valid with joint Boolean commensurability. Recovering fiber coverage from absence of disjoint local refinements additionally needs a local density/detection property unless the named Atmag supp² already contains it. The canceled quotient-topology equivalence must distinguish generated comparabilities from single-pair lifting.',
 'C-SA21-9-125–128/R-SA21-9E-011,012. The Boolean3-stratum certificate shows commensurability alone cannot prove(iii)⇒(ii); its applicability to the named source axiom is explicitly conditional. A separate finite-poset certificate checks the deleted quotient-topology claim only at the poset level. No exact published theorem identifying these final atelier axioms was found in the bounded searches.',
 'The page self-corrects maximality from≪to⊂ and cancels the extra topology requirement. The discrepancy in the support-axiom label cannot be resolved without the scan.',
 'High-priority follow-up: identify the exact supp² ink and test the local detection implication before using the final subdivision equivalences.',
 ['Janowitz1963','CSGUnpublished','Stacks04VB'])
P(32,'Moderation and saturation after the set-theoretic framework',[(17,[128])],
 'The next tasks are subdivisions, moderate ateliers and saturation axioms/constructions for an atelier or atelier-magasin; morphisms and their support relation may come first.',
 'A research task must select one stable axiom version and a defined saturation operation. No universal saturation or moderation theorem with all hypotheses is yet stated in this list.',
 'The list is a source program rather than a precise theorem. CSG’s checked unpublished-work catalogue and Malgoire’s2002 seminar notice document continued interest, not a published solution. Esquisse§5 gives the broader stratified-topology motivation; exact atlas/atelier searches found no identified theorem matching this unfinished list.',
 'The author explicitly sets an order of future work; no additional historical cause is inferred.',
 'Worth preserving as program context, but cut any follow-up into a concrete axiom-completion question rather than a general saturation project.',
 ['CSGUnpublished','Malgoire2002','Esquisse1997'])

assert [p['id'] for p in PROBLEMS]==[f'MP-SA21-9-{n:02d}' for n in range(20,33)]
