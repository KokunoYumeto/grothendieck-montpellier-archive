"""Problem formulations authored after the complete manuscript and reference reading."""
import json
from pathlib import Path
I={x['id']:x for x in json.loads(Path('agents/p15/items_partial.json').read_text())}
P=[]
def p(n,title,ids,st,today,art,why,worth,refs):
    P.append(dict(id=f'MP-SA07-{n:02}',title=title,occurrences=[{'item_id':f'SA07-{i}','cote':I[f'SA07-{i}']['cote'],'scans':I[f'SA07-{i}']['scans'],'lines':I[f'SA07-{i}']['lines']} for i in ids],as_he_states=st,plausible_today=today,state_of_art='As of 2026-11-19: '+art,why_open=why,worth=worth,refs=refs))
p(1,'Mixed-characteristic fibre comparison',[4,8],
 'Compare the characteristic-p crystalline fibre with a characteristic-zero integral p-adic fibre; the author expects nonisomorphism in general and retains an uncertain finite-field exception, without fixing every structure.',
 'Specify a smooth proper object, a good-reduction model, coefficient rings, Frobenius and filtration, then ask for the appropriate period-ring comparison; no bare canonical Q_p comparison is presumed.',
 'Deligne82 §1 gives Betti/de Rham and étale comparisons; Colmez–Fontaine TheoremA gives rational semistable admissibility, with crystalline subcase N=0. Oda5.11 concerns H¹ and A[p], not this whole mixed-characteristic comparison.',
 'The pages leave the integral and Frobenius conventions incomplete; the sources do not identify that omission with a single historical open problem.',
 'Worth clarifying the category and coefficients first, because otherwise different valid comparison theorems answer different questions.', ['P15-D82','P15-CF00','P15-Oda69'])
p(2,'Compatibility of the real conjugations',[10,11],
 'Verify the commuting involutions and their product, called real Frobenius, including the l-adic comparison.',
 'For a smooth proper real variety, use the same Betti/de Rham/étale comparison and distinguish scalar conjugation from geometric pullback.',
 'Deligne82 pp7–9 supplies the real comparison setting. D2 proves commutation there; C09 disproves an argument using arbitrary semilinear involutions alone.',
 'The manuscript explicitly marks the compatibility for verification; this is a normalization check, not a presently open theorem in the geometric setting.',
 'Worth a short convention audit linking all three realizations.', ['P15-D82'])
p(3,'The proposed motivic level subspace',[12,13],
 'The indicated rational intersection of Hodge filtration and real-Frobenius translate is motivic and represents the stated level.',
 'Replace the naive intersection by the largest rational sub-Hodge structure in the specified filtration; algebraicity/coniveau equality is a further generalized Hodge question.',
 'Grothendieck1969 §§1–2 explicitly corrects the naive formulation. D3 and C12 give a dimension-five odd-weight obstruction, also embedded in the real setting. The manuscript index rho still needs an ink check.',
 'Grothendieck’s later paper explains the elementary defect of the original Hodge-conjecture formulation; no claim is made that this exact leaf already has his corrected definition.',
 'Worth resolving the index and comparing the two formulations before treating it as an open coniveau conjecture.', ['P15-G69','P15-D71'])
p(4,'Real and totally real neutralization in characteristic p',[15],
 'For sufficiently large motivic pieces in characteristic p, perhaps T_alpha(R) is empty; ask whether a totally real extension can provide a point.',
 'For a category containing h¹ of a supersingular elliptic curve with all geometric endomorphisms and ordinary dimension-two realizations, no real or totally real neutralization exists.',
 'Voight42.1.9 identifies the geometric quaternion endomorphism algebra; D4 proves it cannot act on R². Deligne–Milne4.17/4.27/4.29 distinguish real fibre functors and polarization conventions.',
 'The manuscript poses the question; the quaternion obstruction explains the stated large-category obstruction, not the fate of every smaller category.',
 'Worth identifying the minimal tensor subcategory and its precise gerbe, with the Codex Deuring gerbe kept separate until matched.', ['P15-Voight21','P15-DM82'])
p(5,'Geometric points versus enriched fibre functors',[18],
 'A suitably enriched transcendental motivic point should correspond bijectively to a complex point modulo conjugation.',
 'Fix the category and integral Hodge/real descent data, then formulate injectivity and essential-image recognition separately.',
 'Deligne–Milne3.2 classifies fibre functors by torsors after a neutralization. Milne6.8 classifies polarizable integral weight-one Hodge structures by complex abelian varieties. Neither classifies all points of an arbitrary X through its proposed motives.',
 'The pages themselves call for additional structure; the opened sources give no general historical explanation or complete theorem with these quantifiers.',
 'Worth testing a precisely defined abelian or elliptic subcategory before asserting an all-motives correspondence.', ['P15-DM82','P15-MilneSV'])
p(6,'Characteristic-p points with Witt and F,V data',[19],
 'Revisit the proposed Witt-valued fibre functors and Frobenius/Verschiebung structures characterizing characteristic-p points.',
 'For an abelian variety over a perfect field, use the contravariant Dieudonné module of A[p] to recover H¹_dR with its specified structure; keep the general point-recognition programme separate.',
 'Oda Cor5.11, printed131, gives M(A[p])≅H¹_dR(A). Cor5.12 for smooth proper X over a perfect field with X(k) nonempty gives an injection from DM of the p-kernel of Pic_X, not all H¹. This does not supply an integral motivic essential image.',
 'The page says Questions and À revoir; the concrete abelian reconstruction was subsequently proved, while the surrounding universal category remains unspecified.',
 'Worth tracing the exact link to cote54/007; avoid treating Oda as a solution to the larger programme.', ['P15-Oda69'])
p(7,'Filtered characteristic-zero points',[20],
 'Characterize characteristic-zero geometric points by filtered fibre functors over the realization field.',
 'State the necessary tensor, polarization, integrality and admissibility conditions for one fixed category, then ask whether they are sufficient.',
 'Hodge theory and Colmez–Fontaine give specific realization categories; Milne6.8–6.9 provides the weight-one integral/rational distinction. None of the opened theorems gives the proposed universal geometric essential image.',
 'The conditions are not fully stated on the page, so the obstruction is partly one of formulation rather than an identified unsolved theorem.',
 'Worth formulating a sharply bounded recognition problem.', ['P15-D71','P15-CF00','P15-MilneSV'])
p(8,'Discrete motivic group and topological monodromy',[21],
 'Compare Aut^tensor(xi)=G_xi(Z) with the topological fundamental group when xi comes from a geometric fibre.',
 'A geometric local system gives a monodromy homomorphism into the tensor automorphism group; its kernel, image and closure depend on the tensor category and integral model.',
 'Deligne–Milne tensor reconstruction and Arapura §§6–7 distinguish a Tannakian algebraic envelope from the underlying discrete topological group. No equality of the two groups follows from the notation pi_1.',
 'The page announces the comparison but supplies no complete category or theorem; no later exact universal equality was verified.',
 'Worth computing the image in one explicit variation, keeping discrete, algebraic and profinite completions distinct.', ['P15-DM82','P15-Arapura13'])
p(9,'Finiteness of integral fibre functors',[22],
 'For fixed alpha there are finitely many integral fibre functors, by Borel–Harish-Chandra.',
 'Prove a reduction to integral points on finitely many closed rational reductive orbits with fixed lattice, or impose hypotheses that give such a reduction.',
 'Borel–Harish-Chandra Theorem6.9, printed510–511, proves finiteness of arithmetic orbits on a closed orbit in a rational representation. The supplied pages omit the reduction of their integral tensor forms to that situation.',
 'The manuscript gives only the citation. The published theorem shows exactly where closedness, reductivity and a fixed lattice enter; it does not explain whether this particular application was later completed.',
 'Worth checking the missing reduction because it controls a concrete finiteness assertion.', ['P15-BHC62','P15-BHC61'])
p(10,'Are the resulting discrete groups isomorphic?',[22],
 'After asserting finitely many integral fibre functors, ask whether their discrete automorphism groups are all isomorphic up to an unspecified qualification.',
 'For specified integral torsors, compare the integral points of the resulting inner forms; first recover the missing qualification near isomorphes.',
 'Deligne–Milne3.2 identifies torsor twists and inner forms; Borel–Harish-Chandra6.9 gives a finiteness result, not an abstract-group isomorphism theorem for all those forms.',
 'The qualifier is unreadable and no exact modern assertion can be extracted beyond the comparison question.',
 'Worth an ink check before an arithmetic-group investigation.', ['P15-DM82','P15-BHC62'])
p(11,'Hodge and Tate conditional fullness',[23],
 'The proposed realization is fully faithful in virtue of the Hodge and Tate conjectures, with normality of X part of the setup.',
 'For pure homological motives, reduce Hom fullness to algebraicity of the corresponding Hodge or Tate tensors on products and twists; retain the conjectural premise.',
 'Deligne’s absolute-Hodge theorem and Arapura’s abelian-type results concern specified enlarged categories. Tate1966 proves abelian Hom over finite fields and Faltings1983 over number fields; neither is the all-cycle Tate conjecture.',
 'The author explicitly treats Hodge and Tate as hypotheses; the opened sources do not remove them for algebraic-correspondence motives.',
 'Worth a theorem-by-theorem conditional dictionary, not an unconditional reconstruction claim.', ['P15-D82','P15-Arapura13','P15-Tate66','P15-Faltings83'])
p(12,'Essential image of Hodge realization',[24],
 'Caractériser l’image of the realization into representations with Hodge structure.',
 'Separate full faithfulness from an intrinsic criterion for which polarized tensor representations are geometric.',
 'Milne6.8 proves the integral weight-one equivalence with abelian varieties; Arapura §7 records stronger general motivic fullness questions. Neither Hom fullness nor a Tannakian equivalence with representations identifies the geometric essential image by Hodge data alone.',
 'The text marks the question with a double question mark; no general criterion was verified in the searched sources.',
 'Worth isolating a low-weight or fixed-family essential image.', ['P15-MilneSV','P15-Arapura13','P15-DM82'])
p(13,'Conjugate fundamental groups as a test',[25],
 'Analyze Serre’s example of conjugate varieties with nonisomorphic topological fundamental groups.',
 'Identify the exact Serre example before asking which motivic tensor invariants distinguish it; do not replace fundamental groups by cohomology rings.',
 'Charles Theorem1 proves an existential conjugate smooth projective pair with different real cohomology algebras. That is a distinct stronger cohomological witness, not a verification of every detail of the unnamed Serre example.',
 'The page names Serre but gives no complete reference or construction. The exact historical example remains an external identification task.',
 'Worth locating the original example and comparing its actual realization data.', ['P15-Charles09'])
p(14,'Connected geometric group and real Frobenius',[26],
 'The connected component together with real Frobenius generates the real motivic group and yields the asserted fullness.',
 'Assume an exact quotient by Gal(C/R) and identify its geometric kernel with G^0 under the appropriate absolute-Hodge hypothesis.',
 'Corrected Deligne–Milne6.22(a)/6.23(a), footnote21, restores an omitted absolute-Hodge hypothesis for connectedness;6.25 supplies the abelian-motive case. D6 proves the remaining group-generation implication.',
 'The published correction documents the missing hypothesis; the all-motives conclusion cannot be read as unconditional.',
 'Worth carrying the correction into every use of real motivic connectedness.', ['P15-DM82'])
p(15,'Variation from one Hodge fibre',[27],
 'Study how the Hodge structure varies, with a one-fibre rigidity expectation in the surrounding reconstruction argument.',
 'For a smooth proper algebraic family over a reduced connected separated finite-type C-base, use a global flat section or global local-system morphism; an arbitrary local VHS is insufficient.',
 'Deligne4.1.2 and4.1.3.1, printed42, give fixed Hodge type for a global flat section;4.1.3.2,43, extends an abelian-scheme local-system morphism algebraic at one fibre.',
 'The sources settle these precise geometric versions. General algebraic-cycle statements require separate conjectures, and no historical cause for the broader programme’s incompleteness is stated.',
 'Worth expressing the global algebraic hypotheses explicitly before applying one-fibre rigidity.', ['P15-D71'])
p(16,'Moduli maps from one value and monodromy',[28],
 'A map to polarized rigidified motivic moduli is determined by one value and the induced pi_1 map.',
 'For fine moduli of polarized abelian varieties with sufficient level over a reduced connected finite-type C-base, require a global compatible integral H¹ local-system identification and one algebraic fibre isomorphism.',
 'Deligne4.1.3.2 plus Milne14.8 proves the abelian-family reconstruction used in D7. No theorem for arbitrary unspecified motivic moduli follows.',
 'The broad moduli category is not constructed on the pages. The literature verifies a restricted setting, not the full quantifier.',
 'Worth testing exactly which extra tensors and rigidification are needed for the desired moduli problem.', ['P15-D71','P15-MilneSV'])
p(17,'Characterizing motivic moduli by rigidity',[29],
 'Perhaps every variety with the preceding rigidity property is a moduli space of motives of suitable type.',
 'Specify the rigidity property, class of varieties and meaning of moduli, including stack versus fine scheme and level structures.',
 'Milne’s period-domain and abelian-moduli results give important examples, while Arapura constructs motivic sheaves in specified settings. No converse characterization with the page’s quantifiers was found.',
 'The page says Peut-être and does not state the proposed converse precisely; the searched literature does not identify a single settled theorem.',
 'Worth a formulation exercise only after excluding vacuous rigidity examples.', ['P15-MilneSV','P15-Arapura13'])
p(18,'Motivically pointed objects',[30],
 'Introduce motivically pointed objects/fibre data as part of the reconstruction programme.',
 'Distinguish an actual geometric point, a tensor fibre functor and a chosen comparison isomorphism, then define a category of pointed objects.',
 'Deligne–Milne3.2 makes the fibre-functor/torsor distinction precise. The page does not establish that every such point is geometric.',
 'The construction is exploratory and its full category is not specified; no independent historical explanation is available.',
 'Worth stabilizing notation, with no new classification claim until the objects are fixed.', ['P15-DM82'])
p(19,'Finite tensor pieces versus one global isomorphism',[31],
 'When does isomorphism of every finite tensor restriction imply isomorphism of the full integral fibre functors?',
 'Treat the tensor-Isom sets as an inverse system and prove compatible nonemptiness using a suitable compactness, lifting or descent theorem.',
 'EGA8.8.2–8.8.3 handles finite diagrams; Deligne–Milne3.2 handles the comparison torsor. Neither turns separate integral points on all finite restrictions into a compatible integral point without further hypotheses.',
 'The author distinguishes the finite and global questions explicitly. The missing compatibility is a real logical issue, not resolved by finite spreading.',
 'Worth a precise pro-torsor formulation with the actual transition maps.', ['P15-EGAIV3','P15-DM82'])
p(20,'Spreading the finite motivic comparison',[32],
 'If two places agree on the algebraic part of the field, spread a finite tensor piece and compare by transcendental paths.',
 'For a fixed finite collection of varieties, morphisms and tensor relations over a characteristic-zero field, descend to a suitable finite-type geometrically connected model and identify the required local systems.',
 'EGA8.8.2–8.8.3 descends finite diagrams;9.7.7 controls geometric connectedness after shrinking. Bakker–Tsimerman Lemmas4.12–4.13 gives a precise related path/Betti comparison for finitely generated regular extensions.',
 'The integral category and all required tensor data are not fully defined on the leaf; finite descent does not settle global compatibility.',
 'Worth a complete finite-piece proof in one specified motivic category.', ['P15-EGAIV3','P15-BT25'])
p(21,'The countable path tower',[33],
 'For countable k, choose smooth geometrically connected transition models so that path torsors have surjective transitions and a nonempty inverse limit.',
 'Retain the elementary inverse-limit lemma under actual surjectivity, but replace the impossible universal geometric tower by a valid construction under additional hypotheses.',
 'CL-SA07-134 and D8 refute the asserted tower for an algebraic closure of Qbar(t). EGA finite spreading does not supply it. Bakker–Tsimerman4.12–4.13 treats finitely generated regular extensions, not all countable fields.',
 'The manuscript supplies no construction of the transition models. The obstruction is proved in this run; it does not refute the final fibre-functor comparison.',
 'Worth finding the exact repair or the missing restriction in the surrounding archive.', ['P15-EGAIV3','P15-BT25'])
p(22,'The uncountable continuation',[34],
 'Si k pas dénombrable, with no surviving completion.',
 'Formulate the comparison for a fixed category over an uncountable field, including the indexing system and the desired compatible paths or torsor point.',
 'Bakker–Tsimerman Proposition4.14 constructs specified rational Nori categories via countable subfields; this is a useful later framework, not a theorem identifying the unfinished integral assertion.',
 'The sentence ends before a statement is made, so no exact conjecture can be assigned a solved/open fate.',
 'Worth seeking continuation sheets before mathematical development.', ['P15-BT25','P15-CG17'])
p(23,'Separation on the algebraic part',[35],
 'If the places differ on E, some finite tensor subcategory should distinguish their integral Betti functors.',
 'Specify whether places are modulo conjugation, what E is, and whether Hodge data are included; ask separation for those exact equivalence classes.',
 'Charles proves existence of a conjugate pair with different real cohomology rings; it does not separate every prescribed pair of embeddings. The later Hodge-enriched elliptic test has additional hypotheses.',
 'The page only says je pense, and the deleted reduction does not supply a proof.',
 'Worth first testing the universal quantifier against the real-conjugation identifications already present in the manuscript.', ['P15-Charles09','P15-MilneSV'])
p(24,'Different cohomology rings of conjugate varieties',[36],
 'Find a smooth projective variety whose conjugates have nonisomorphic cohomology rings.',
 'The existential real-cohomology-algebra statement for two embeddings of a number field is precise and established; prescribed-pair separation is stronger.',
 'Charles Theorem1 proves the existential statement; first arXiv circulation25 June2007, publication2009, with both dates checked.',
 'The source establishes the later result but does not document the fate of every stronger place-separation variant.',
 'Worth a direct historical link; no new proof is needed for the established existential claim.', ['P15-Charles09'])
p(25,'One motive separating archimedean places',[37],
 'For a number field and M sufficiently large, is the map from places into integral Isom-torsor classes injective?',
 'Fix M, its integral tensor category, the quotient on embeddings, and whether Hodge/real data are retained.',
 'Tannakian torsors are established by Deligne–Milne3.2. Charles’s existential example supplies some separating tensors for some pairs, not a uniform theorem for all places of every field.',
 'The dependence on M and the integral category is not specified; no exact uniform result was verified.',
 'Worth a finite-field-of-definition test with explicit motives and torsors.', ['P15-DM82','P15-Charles09'])
p(26,'Which motivic torsors come from places?',[38],
 'Does every principal homogeneous space under the integral motivic group come from an archimedean place, after adding the Riemann–Hodge conditions?',
 'Separate arbitrary torsors from torsors possessing a complex comparison point and an admissible polarized integral Hodge structure.',
 'Deligne–Milne3.2 classifies fibre functors by torsors, not geometric origins. Milne6.8 gives the abelian weight-one essential image only.',
 'The manuscript itself warns that an unqualified torsor is inadequate and requests extra conditions.',
 'Worth identifying necessary conditions before testing surjectivity.', ['P15-DM82','P15-MilneSV'])
p(27,'Hodge enrichment and separation of embeddings',[40,41],
 'What changes if the Hodge structures are retained, after the bare-place conjecture was rejected?',
 'For a category containing all specializations of the explicit elliptic test family, an integral Hodge-preserving comparison over the identity of C separates chosen embeddings.',
 'Milne6.8 identifies integral weight-one Hodge structures with complex abelian varieties; D9 and C01 prove the conditional elliptic test. It does not settle torsor essential-image surjectivity or places modulo conjugation.',
 'The page explicitly retracts the unfiltered version and proposes the elliptic test rather than a general proof.',
 'Worth formalizing the minimum family-availability and integral hypotheses.', ['P15-MilneSV'])
p(28,'Recovering maps from tensor functors',[42],
 'To what extent is a scheme morphism known from its induced contravariant motivic tensor functor?',
 'Specify source, target, motivic category, coefficient and enrichment, then separate faithfulness from characterization of geometric functors.',
 'Tate/Faltings recover Hom of abelian varieties from l-adic modules under their field hypotheses; Mochizuki TheoremA recovers dominant maps to hyperbolic pro-curves from open Galois-compatible group maps over sub-p-adic fields. These are distinct restricted settings, not a universal motivic theorem.',
 'The manuscript asks an open-ended question; later theorems do not identify its entire domain.',
 'Worth choosing one precise target class and one realization before making a reconstruction conjecture.', ['P15-Tate66','P15-Faltings83','P15-Mochizuki99'])
p(29,'The immersive moduli criterion',[43],
 'A global polarized motive giving an immersion of Y into moduli should make Y recoverable in the proposed anabelian sense.',
 'State an actual fine moduli map and prove that the tensor functor recovers its image and factorization, not merely the ambient family.',
 'Deligne4.1.3.2 controls abelian families; Milne14.8 gives their Hodge description. Neither theorem alone recognizes an arbitrary subvariety in moduli or every map into it.',
 'The note is an abbreviated programme without all quantifiers or the needed essential-image statement.',
 'Worth separating family rigidity from recognition of the subvariety.', ['P15-D71','P15-MilneSV'])
p(30,'The unclear local true case',[44],
 'An insertion says the assertion is true for an uncertain local k-scheme and refers to a first case.',
 'No precise formulation is justified until the local hypothesis and antecedent are recovered.',
 'The surrounding Hodge/Tannakian sources explain the context but identify no theorem with the unread condition. This remains classF rather than a manufactured special case.',
 'The essential words and reference are uncertain in the supplied transcription.',
 'Worth only an ink and continuation check at present.', ['P15-DM82','P15-D71'])
p(31,'Six conjectural descriptions of motives',[45],
 'Describe motives by six combinations of Betti, de Rham, Hodge, Gauss–Manin, Tate and filtered crystalline data.',
 'Treat each description as a proposed realization category with its own coefficients and admissibility, rather than an asserted equivalence of six unspecified categories.',
 'Deligne–Milne gives abstract tensor reconstruction; Choudhury–Gallauer9.1 compares Nori/Ayoub groups for a fixed embedding and coefficients; Colmez–Fontaine addresses a specified local rational category. None proves the six-fold list as written.',
 'The heading itself says conjectural and the entries do not state essential-image axioms.',
 'Worth a precise realization-by-realization table before a new theorem is proposed.', ['P15-DM82','P15-CG17','P15-CF00'])
p(32,'Missing local analogues of1′ and4′',[46,49],
 'For p-divisible groups up to isogeny, what replaces the Betti/de Rham and Betti/Gauss–Manin entries?',
 'Fix a mixed-characteristic complete discretely valued field and distinguish rational Tate representations, crystalline modules and Hodge–Tate filtrations; clarify the transcribed l versus p.',
 'Colmez–Fontaine TheoremA supplies rational semistable admissibility; it does not create a literal integral Betti lattice over a p-adic field. Oda concerns characteristic-p H¹ and finite group schemes.',
 'The page explicitly leaves the two slots empty; a modern analogy is not an exact missing manuscript definition.',
 'Worth reconstructing the local dictionary with all variance and weight conventions.', ['P15-CF00','P15-Oda69'])
p(33,'Filtered Frobenius essential image',[47],
 'Which filtered crystalline data arise in the intended p-divisible or pseudo-motivic category?',
 'For rational semistable representations use weakly admissible filtered(phi,N)-modules; impose N=0 for crystalline representations, appropriate two Hodge–Tate weights for p-divisible groups, and lattice conditions for integral models.',
 'Colmez–Fontaine TheoremA proves weakly admissible implies admissible in its rational category. The cited theorem alone does not establish the extra p-divisible or integral equivalence.',
 'The page does not separate these categories. The established rational theorem is a partial precise fate, not a blanket answer.',
 'Worth documenting the exact narrower p-divisible classification before claiming the local list is solved.', ['P15-CF00'])
p(34,'Equality of the two modified sections',[76,83],
 'After modifying two splittings by u and jχ, write that the modified sections agree.',
 'State that equality as an additional comparison compatibility, or prove it from a specified geometric comparison; centralization only ensures each is a homomorphism.',
 'C05 and D10 give a complete split-extension counterexample to the missing implication. Deligne–Milne torsor formalism does not identify this local extension with an arithmetic motivic exact sequence.',
 'The page says On écrit que, without deriving the equality from the previous centralization observations.',
 'Worth recovering the intended compatibility datum before using the resulting cocycle formula.', ['P15-DM82'])
p(35,'The kernel and cyclotomic condition',[50],
 'Infer keru=kerχ∩kerφ from φ=u(jχ)^{-1}.',
 'The equality is valid exactly with the extra implication keru⊆kerχ; otherwise only kerχ∩keru=kerχ∩kerφ follows.',
 'C06 verifies a counterexample on C₂ and D10 proves the corrected identity. No unseen LM6 A22/A50 statement is assumed to provide the missing premise.',
 'The needed implication is not written in the supplied passage.',
 'Worth finding the omitted Tate-character hypothesis; the elementary correction is already complete.', ['P15-DM82'])
p(36,'Integral Chow specialization with torsion',[51,52],
 'Develop integral Chow-ring specialization compatible with Chern classes, rather than only the rational comparison; the wording is weakened to il semble.',
 'Specify a smooth proper family over a trait and the chosen Chow specialization, then check the integral diagram with torsion and its exact hypotheses.',
 'SGA6 X7.13.11 is the exact later locator. Original printed579 and581 were viewed, but printed580 is absent from the accessible scan assembly; the integral middle diagram is not independently original-verified in this run.',
 'The author explicitly says this would require developing specialization. The verification limit here is source access, not evidence that the standard specialization theorem is open.',
 'Worth obtaining the missing original page and matching every arrow before a final historical identification.', ['P15-SGA6'])
p(37,'Tate graded-index consistency',[53],
 'Use the written Tate weight/Hodge shifts together with a possibly unshifted associated-graded expression.',
 'Use Gr_i^W(E(n))=Gr_{i+2n}^W(E)(n); decide on the scan whether the disputed line already says this.',
 'Deligne82 p9 fixes Q(n); C14 verifies the shifts and the pure Tate counterexample to an unshifted reading.',
 'This is a transcription/index question rather than an unsolved mathematical conjecture.',
 'Worth an ink check because the wrong index propagates into the Hodge torsor construction.', ['P15-D82','P15-D71'])
p(38,'Which object is the splitting torsor Q?',[54,55,57,58],
 'Q is called a space of Levi subgroups and also an H′-torsor; the arrows and dimensions are used in the period field diagram.',
 'Distinguish the U-torsor of splittings from an H′-torsor that includes the Tate G_m, and specify any quotient or chosen Tate trivialization.',
 'The parabolic/Levi dimensions are elementary and C08 checks GL₂: splitting dimension1, H′ dimension2. Deligne–Milne5.1 distinguishes identity-functor central grading from a realization grading.',
 'The page uses overlapping notation and a reverse forgetful arrow; no opened reference decides its intended convention.',
 'Worth resolving first, since the strong g+u conjecture depends on this dimension.', ['P15-DM82','P15-MilneLAG'])
p(39,'The strong g+u transcendence conjecture',[59,60,61],
 'For k⊂Qbar, trdeg_k k(α,β)=dimG+dimU′, with the displayed consequences for α,β,γ and flags.',
 'After fixing Q and all bases, distinguish the ordinary period point from the extra Hodge-splitting coordinates; state field bounds and genericity over the correct base.',
 'Bost–Charles Definition2.9/Conjecture2.12 and KSV2026 separate generated torsors from period genericity. The full non-CM elliptic arithmetic period conjecture is not proved by these results; Bakker–Tsimerman proves a function-field theorem.',
 'The page states a conjecture, and its Q-dimension ambiguity is an additional formulation problem. No source gives a historical explanation of this exact stronger version.',
 'Worth reconstructing the torsor diagram before comparing it to current period conjectures.', ['P15-BC16','P15-KSV26','P15-BT25'])
p(40,'The cancelled normalized period draft',[62,64,65,70],
 'After removing the Tate determinant, the only relations should leave dimensiong−1; the elliptic examples and base-field qualification are all cancelled.',
 'Preserve the withdrawn layer; a precise normalized period conjecture needs the determinant relation, square-root field and the intended algebraic or transcendental base.',
 'C15 verifies determinant normalization only. Grothendieck1966 note10 distinguishes individual transcendence from algebraic independence. The modern period-torsor formulation is in Bost–Charles, not a proof of the cancelled equality.',
 'The author struck out the entire page; the reason for cancellation is not stated. No reason is invented from later literature.',
 'Worth a historical comparison and an ink check of the undefined normalization symbol, not resurrection as a live theorem.', ['P15-G66','P15-BC16'])
p(41,'Elliptic full-period degrees four and two',[66],
 'For an elliptic curve over Qbar, ask trdeg Q(α)=4 without CM and2 with CM.',
 'Use the full period/quasiperiod matrix and its Tate determinant, over the algebraic definition field, with the motivic group GL₂ or the CM torus.',
 'Bost–Charles §2.2 records the CM elliptic period result and the remaining genericity conjecture. KSV5.13 proves a generated de Rham–Betti torsor statement for elliptic products; it does not prove full non-CM transcendence degree4.',
 'The live page leaves question marks. The known CM result and unresolved full non-CM claim are different fates.',
 'Worth preserving as a central historical period-conjecture formulation, with no claim of a short-run solution.', ['P15-BC16','P15-KSV26','P15-G66'])
p(42,'The subgroup generated by the period locus',[67],
 'After translating the algebraic locus of the comparison point to contain1, is its generated algebraic subgroup H equal toG?',
 'Fix Qbar coefficients, the tensor category and the minimal algebraic torsor; distinguish its generated torsor from the raw Zariski closure of the point.',
 'KSV2026 Proposition3.1 identifies the minimal generated torsor with the appropriate de Rham–Betti torsor; Theorem5.13 supplies elliptic-product equality under its coefficient hypotheses. It is weaker than full period genericity.',
 'The manuscript separates this question from transcendence degree. The modern theorem confirms why collapsing them would overstate the result.',
 'Worth an exact notation match to the modern minimal-torsor construction.', ['P15-KSV26','P15-BC16'])
p(43,'Algebraic Hodge splitting for a non-CM elliptic curve',[68,69],
 'Can the Hodge splitting parameter h be algebraic for a non-CM elliptic curve? CM is asserted to give an algebraic splitting.',
 'Ask whether an elliptic curve over Qbar with a Qbar-de Rham splitting equal to its complex Hodge splitting must have CM.',
 'Katz4.0.7 proves the CM direction and4.0.8 asks the converse; Bertrand1978 §6 Conjecture3 gives a related analytic formulation. BDP1.4.1 verifies the CM eigenspace construction. No verified resolution of the converse was found in the recorded2026 searches; the MathOverflow question is discovery evidence, not proof of openness.',
 'The sources explicitly pose the converse. A rational-Betti projector argument does not apply to an algebraic-de Rham projector, explaining one invalid shortcut.',
 'Worth a focused literature and equivalence audit, while treating the converse as unresolved by the sources actually opened.', ['P15-Katz76','P15-Bertrand78','P15-BDP13','P15-MO-Katz'])
p(44,'Completing the local-to-global residue comparison',[71,74],
 'Faire le raisonnement after the local(2πi)^p computation, and finish the commutativity argument for the global square.',
 'Use oriented complex normal bundles, Thom classes, excision and functoriality to compare the codimension-p algebraic and topological cycle classes.',
 'C02 and D16 check the local integral. Bost–Charles §1.1.2 gives a precise modern cycle-class convention; p18 continues with the same inverse factor and proper direct images. General duality traces may have extra signs.',
 'The page explicitly leaves the final argument unfinished; the standard comparison is established, but its normalization must be matched.',
 'Worth writing the convention-preserving proof for the companion commentary.', ['P15-BC16','P15-G66'])
p(45,'Transversal dimension and Gysin degree',[72,73],
 'A transversal has written dimensionn−p and a global Gysin target has written degreei+p.',
 'For codimensionp in an n-fold, use a p-dimensional isolated transversal and cohomological shift2p, pending an ink decision.',
 'D16 derives both dimensions. The adjacent p18 proper trace explicitly uses degree2i+2p and the same scalar, independently supporting the alarm.',
 'The notation can only be settled on the missing scans; the mathematics flags the inconsistent ordinary interpretation.',
 'Worth a high-priority scan check because both errors alter the main comparison square.', ['P15-BC16'])
p(46,'The deferred Casimir calculation',[95],
 'Supply the Casimir calculation and finite-dimensional restrictions in the representation-theory revision.',
 'Recover the normalization of the invariant form and the missing operator before assigning a numerical eigenvalue.',
 'Milne5.18/5.20 and§9 give the standard Casimir and highest-weight framework; D17 checks the supplied sl₂ string formulas. The absent Casimir expression is not uniquely determined by the leaf.',
 'The source explicitly delegates the calculation and omits the antecedent formula.',
 'Worth locating the original typescript page; no new spectral formula should be guessed.', ['P15-MilneLAG'])
p(47,'The unchecked rank formula',[96],
 'A formula on source page9 has not been checked for correctness.',
 'Recover the formula and its characteristic assumptions; retain rank as minimum zero multiplicity of adX in this context.',
 'Milne8.6 gives the exact rank convention and D19 verifies the nilpotent example. This does not identify the missing formula.',
 'The manuscript itself says its accuracy was not checked, and the cited source page is absent.',
 'Worth retrieving the source leaf before mathematical work.', ['P15-MilneLAG'])
p(48,'Withdrawn positive-characteristic propositions',[97,98],
 'Several propositions are declared false and removed; sl₂ in characteristic2 is the explicit warning.',
 'Retain each deletion as a withdrawal; only the explicit sl₂ counterexample has enough data for a complete check.',
 'C03 proves characteristic-two sl₂ is nilpotent of class2. Standard characteristic-zero Cartan theory in Milne§8 does not restore the unnamed deleted propositions in positive characteristic.',
 'The author expressly rejects them. Their full statements are not supplied, so no replacement theorem is inferred.',
 'Worth a historical editorial concordance, not treating deleted assertions as live claims.', ['P15-MilneLAG'])
p(49,'The corrected half-root summation',[98],
 'A sum should run over half of the roots rather than all roots.',
 'Identify the original invariant form or trace expression and a positive-root choice before computing the factor.',
 'Milne§§7–9 supplies root-pair and highest-weight conventions, but the missing summand is not recoverable from the instruction alone.',
 'The source formula is absent and several distinct standard formulas differ by a factor2.',
 'Worth only a source-page recovery and sign audit at this stage.', ['P15-MilneLAG'])
p(50,'Generalizing missing propositions5 and6',[105],
 'Extend two source propositions to a product of a commutative algebra and sl₂ factors.',
 'Recover the two statements, their module hypotheses and characteristic before attempting a product argument.',
 'Milne’s reductive and sl₂ theory supplies surrounding examples, but does not identify the absent propositions. This is an editorial problem with classF fate.',
 'The sheet gives only source numbers and a proposed target generalization.',
 'Worth retrieving the antecedent propositions.', ['P15-MilneLAG'])
p(51,'Theorem3(c) and the root-pair normalization',[106,107],
 'Complete a missing theorem3(c) proof and choose the root-pair map phi with the stated normalization.',
 'Fix a split characteristic-zero semisimple Lie algebra, root vectors and their sl₂ triple normalization; identify the missing theorem separately.',
 'Milne8.24–8.27 and§9 verify split-Cartan and rank-one structures. SGA3 XXI supplies root-datum conventions. Neither identifies the absent theorem3(c).',
 'The instruction is local to another typescript whose proof is not supplied.',
 'Worth recovering the root-vector conventions before comparing formulas.', ['P15-MilneLAG','P15-SGA3XXI'])
p(52,'Exhaustion by holomorphic representations',[109],
 'Establish an assertion about all holomorphic representations in the missing surrounding discussion.',
 'Specify the group, global form, finite dimensionality and whether the statement is integration of Lie-algebra representations.',
 'Conrad’s character-lattice classification and Milne§9 distinguish Lie-algebra highest weights from representations integrating to a chosen global group. The page lacks enough data to select the exact theorem.',
 'The quantifier and antecedent group are not present.',
 'Worth recovering the source statement; a global-form hypothesis may be decisive.', ['P15-ConradPi1','P15-MilneLAG'])
p(53,'The fourth-power operator identity',[109],
 'Prove theta or phi to the fourth power equals1, with the operator letter uncertain.',
 'Identify the operator and normalization before checking its order; do not substitute a familiar Weyl lift.',
 'Root-vector and Weyl-group sources supply several order-two/four constructions, but none identifies this missing operator. The formula remains classF.',
 'Both the symbol and its definition are absent or uncertain.',
 'Worth an ink and preceding-page check only.', ['P15-MilneLAG','P15-SGA3XXI'])
p(54,'Elementary automorphisms and Cartan conjugacy',[110],
 'Verify normality of Aut_el and its transitive action on Cartan subalgebras.',
 'Use finite-dimensional characteristic-zero Lie algebras over an algebraically closed field, or the precise split rational variant; arbitrary real Cartans are not all conjugate.',
 'D18 proves normality by conjugating nilpotent exponentials. Milne8.17 proves Cartan conjugacy in the algebraically closed case and8.27 treats split Cartans.',
 'The sheet requests an editorial proof; the standard result is established with the field hypotheses.',
 'Worth restoring those hypotheses in the companion text.', ['P15-MilneLAG'])
p(55,'Nested Cartans and self-normalizers',[111],
 'Add nested-Cartan and self-normalizer assertions, with a corollary using equal rank and a regular element.',
 'In the finite-dimensional characteristic-zero setting, retain the manuscript’s Fitting/rank convention and distinguish the two normalizer statements.',
 'Milne8.4 and8.21 give the precise surrounding results; D18 proves the nested and Fitting-quotient implications. Modern regular-nilpotent terminology is not substituted.',
 'The source is an abbreviated editorial instruction; the established theorem needs its rank convention spelled out.',
 'Worth a compact proof and terminology check.', ['P15-MilneLAG'])
p(56,'Cartans under restriction of scalars',[112],
 'Cartan subalgebras do not change on restricting the scalar field.',
 'For finite K/k of characteristic zero and finite-dimensional g/K, use nilpotent+self-normalizing Cartans; a k-Cartan must be K-linear.',
 'D18 supplies an independent normalizer proof. Milne8.5 is extension of scalars and is not mis-cited as the restriction theorem. Finiteness keeps the algebra in the standard finite-dimensional category.',
 'The finite-extension convention is not explicit on the sheet; the algebraic argument is valid but its category must be fixed.',
 'Worth preserving the short proof rather than an inaccurate extension-of-scalars citation.', ['P15-MilneLAG'])
p(57,'The adjoint eigenvalue-one bound',[113],
 'Ad(x) has eigenvalue1 with multiplicity at least the rank on an open subgroup; for connected real/complex G take all ofG.',
 'Use finite-dimensional characteristic-zero analytic groups and the minimum-zero-multiplicity rank convention; real/complex connectedness allows analytic continuation.',
 'D19 verifies the exponential and characteristic-polynomial argument. Milne8.6 fixes rank; no exact missing Lefschetz lemma is recovered.',
 'The explicit bound can be checked, but the source of the referenced generalization is not identified.',
 'Worth a hypothesis-preserving proof with no transfer to arbitrary characteristic.', ['P15-MilneLAG'])
p(58,'Generalized weights and Galois descent',[114],
 'Repair characteristic-space statements, use an equivariant bilinear map, and replace algebraic closure by a Galois extension in descent.',
 'For commuting additive or multiplicative operators use generalized eigenspaces and tensor nilpotence; for descent require a stable subspace and actual descent data.',
 'D20 proves the generalized-weight product rule. Standard scalar descent in Deligne82 §1 addresses the compatible-data part, but the missing corrected characteristic-space formula is not supplied.',
 'The exact source formula and descent argument belong to absent pages; only the explicit product mechanism is determined.',
 'Worth recovering the original formula before assigning a characteristic-free theorem.', ['P15-MilneLAG','P15-D82'])
p(59,'Nilpotence written Ad rather than ad',[115],
 'A remark is to give nilpotence of Ad(x) under a missing proposition’s hypotheses.',
 'If x is a Lie-algebra element, ad(x) may be nilpotent; if x is a group element, Ad(x) is invertible and cannot be nilpotent on a nonzero algebra.',
 'D20 proves the invertibility obstruction. The surrounding Lie sources distinguish the two operators, but the manuscript may use an older convention.',
 'The source proposition and notation are unavailable, so the ink decides the proposed correction.',
 'Worth a high-priority notation check.', ['P15-MilneLAG'])
p(60,'Infinite highest weights and Harish-Chandra',[116],
 'Develop infinite W(lambda) modules, Harish-Chandra formulas and invariant differential operators.',
 'Separate Verma modules, their central characters, and invariant differential-operator results; recover any requested commutant formula before stating it.',
 'Etingof’s MIT18.757 Theorem14.1 gives the Harish-Chandra isomorphism and rho-shift; Milne§9 gives finite highest weights. The manuscript is a programme, not a novel complete theorem.',
 'The sheet assigns future exposition and references existing work; no explicit unresolved formula is written.',
 'Worth identifying the intended exposition and its historical sources.', ['P15-MIT-HC','P15-MilneLAG'])
p(61,'The Jacobson–Morozov programme entry',[116],
 'Include the item written Jacobson-Mort aux Off in a list of future complements.',
 'Treat identification with Jacobson–Morozov as a contextual reading, not a theorem whose hypotheses are written here.',
 'The surrounding semisimple Lie and sl₂ sources make that interpretation plausible, but no exact manuscript assertion or proof can be extracted from the title alone.',
 'Only a humorous title is supplied; no mathematical statement is present.',
 'Worth an editorial identification, with any theorem statement sourced independently in the next companion run.', ['P15-MilneLAG'])
p(62,'D4 triality',[117],
 'Show the triality automorphisms of D4.',
 'For the split simply connected or adjoint D4 group, specify an order-three diagram automorphism and its chosen realization.',
 'Ruether2024 TheoremA and Cor2.4 give explicit triality over schemes; its introduction attributes the classical phenomenon to Cartan1925. The manuscript supplies no construction to compare termwise.',
 'This is an expository assignment concerning established mathematics, not an announced new open conjecture.',
 'Worth finding the intended classical construction, with global form and integral coefficients explicit.', ['P15-Ruether24'])
p(63,'Cartier’s integral structures',[118],
 'Cartier is to write an arithmetic supplement on Z-structures.',
 'Distinguish integral highest-weight lattices, integral forms of enveloping algebras and group schemes; recover the intended scope.',
 'D17 verifies the supplied rank-one divided-power lattice. SGA3 XXI treats root data; neither identifies the missing supplement or every intended integral theorem.',
 'The page records an assignment without a precise statement.',
 'Worth a bibliographic/source concordance before declaring a specific later integral-form result its exact fate.', ['P15-MilneLAG','P15-SGA3XXI'])
p(64,'Local extensions of propositions3 and3bis',[101],
 'Leave to the reader the extension of propositions3 and3bis to local groups.',
 'Recover the antecedent propositions and retain all product-domain conditions.',
 'Olver Definition2 supplies the precise local associativity convention; Bruhat Chapter2 gives local analytic constructions. The missing numbered statements remain unidentifiable.',
 'The previous typescript pages are absent.',
 'Worth retrieving them; no blanket extension is claimed here.', ['P15-Olver','P15-Bruhat58'])
p(65,'Convolution for finite differentiability',[101],
 'Extend the distribution algebra to a local C^r group, with a warning that multiplication is partial for finite r.',
 'Define products only when total distribution order is at most r; use all orders for C∞.',
 'D24 proves associativity and functoriality from the multiplication germ. Beltiță–Nicolae5.2 gives the smooth operator correspondence, not an unrestricted finite-r algebra.',
 'The manuscript recognizes the differentiability limitation; the verification is elementary once it is retained.',
 'Worth recording the order bound explicitly in the companion text.', ['P15-BN14'])
p(66,'The tangent local group',[101],
 'Verify that TG with Tm,Ttheta and0_e is a C^{r−1} local group and the projection is a morphism.',
 'Identify the domain as TΩ⊂TG×TG and assume r≥1, with the relevant differentiable category fixed.',
 'D24 checks all identities by the tangent functor and chain rule; Olver’s exact local axioms fix the domain requirements.',
 'The claim is left as easy verification and the transcription has blank domain notation.',
 'Worth a brief diagram proof plus scan check.', ['P15-Olver'])
p(67,'Remaining local extensions and propositions11–12',[101],
 'Extend the other results of sections12–16 and propositions11–12, with their corollaries, to local groups.',
 'Only the individually stated convolution and tangent constructions can be checked until the earlier statements are supplied.',
 'Bruhat and Beltiță–Nicolae give precise neighboring results; no source establishes an unspecified list of missing assertions.',
 'The antecedent pages are absent, so the mathematical target is not identifiable.',
 'Worth source recovery rather than a generic claim of completion.', ['P15-Bruhat58','P15-BN14'])
p(68,'Deferred unimodularity of Lie groups',[102],
 'Later prove that connected semisimple and nilpotent Lie groups are unimodular.',
 'For connected real/complex Lie groups, prove trace(adX)=0 and use the determinant modular formula.',
 'Bruhat1958 Chapter7§3.1 explicitly proves the semisimple case; Li1.40 gives the determinant formula. D28 independently proves both cases and keeps connectedness.',
 'The leaf labels the proof for later exposition; the result is established, not presently open.',
 'Worth inserting the short proof and its connectedness hypothesis.', ['P15-Bruhat58','P15-Li26'])
p(69,'Formal coalgebra maps and the degree-zero condition',[103],
 'Recover formal maps from diagonal-compatible linear maps carrying U0 ontoU0; the proof writes only a00 nonzero and changes module letters.',
 'For finite free formal disks over a commutative ring, retain ontoU0, which makes a00 a unit, and use continuous augmented substitution on completed coordinate rings.',
 'D29 proves the finite-free statement and resolves the idempotent issue without assuming a field. Strickland4.59/4.62 gives a qualified good-basis coalgebra/formal-scheme equivalence. Infinite-chart conventions remain unavailable.',
 'The other supplied package18/018 and18/022 supplies the filtered coalgebra and chart definitions; still earlier polynomial-map and infinite-free conventions are not supplied here. The nonzero shorthand is weaker than the actual proposition hypothesis.',
 'Worth recovering those definitions, since no mathematical counterexample to the finite-free proposition remains.', ['P15-Strickland00'])
p(70,'Density of nonempty open subsets',[119],
 'Add that every nonempty open is dense, with proof by references.',
 'Assume the ambient space is irreducible, for example affine space in the stated algebraic setting.',
 'D21 proves the irreducible-space assertion and gives a reducible two-point counterexample. The polynomial setting in Milne supplies the surrounding classical context.',
 'The source proposition is absent, so its irreducibility hypothesis must be recovered rather than presumed.',
 'Worth a simple context check, not a new density problem.', ['P15-MilneLAG'])

# A problem register also preserves questions raised by this audit. They are not
# silently attributed to Grothendieck as conjectures or explicit question marks.
editorial={3,9,11,14,20,21,30,34,35,37,38,45,53,54,55,56,57,58,59,65,69,70}
for x in P:
    n=int(x['id'].rsplit('-',1)[1])
    x['problem_origin']=('this run’s reading/verification question' if n in editorial else 'manuscript question/deferred step')
    if n==40:
        x['problem_origin']='manuscript question/deferred step; withdrawn draft'
    if n in {48,49}:
        x['problem_origin']='manuscript correction/deferred step; exact antecedent unavailable'

Path('agents/p15/problems.json').write_text(json.dumps(P,ensure_ascii=False,indent=2)+'\n')
print(len(P),'individually formulated problems')
