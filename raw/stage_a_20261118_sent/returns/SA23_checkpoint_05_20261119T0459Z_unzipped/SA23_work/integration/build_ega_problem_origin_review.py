"""Serialize the manually adjudicated ega/analysis_curves problem-origin audit.

This is a proposal-only audit. It never writes owner registers. Decisions below
come from the complete earlier readings and targeted logged rereads; the code
only copies evidence and checks coverage/references.
"""
from pathlib import Path
import collections
import hashlib
import json

BASE = Path(__file__).resolve().parents[2]
WORK = BASE / 'SA23_work'
SPECS = {'ega': {}, 'analysis_curves': {}}


def add(owner, n, action, origin, evidence, reason, scope, title=None, claims=None):
    assert n not in SPECS[owner]
    SPECS[owner][n] = dict(action=action, origin_class=origin,
        evidence=evidence, rationale=reason, proposed_scope=scope,
        proposed_title=title, retained_claim_suffixes=claims)


def e(n, action, origin, evidence, reason, scope, title=None, claims=None):
    add('ega', n, action, origin, evidence, reason, scope, title, claims)


def a(n, action, origin, evidence, reason, scope, title=None, claims=None):
    add('analysis_curves', n, action, origin, evidence, reason, scope, title, claims)


# Every decision is entered explicitly. K=keep, N=narrow authorial scope,
# E=reclassify as an editorial / reader-verification record.
e(1,'E','reader verification of corrected assertion',[('K22-01',13,35)],
  'Jouanolou states propositions and the working hand corrects the coefficient module. Neither the correction nor the comment assez rare creates an authorial question about how often the criterion holds.',
  'Verify the printed differential-module criterion and its handwritten coefficient correction; preserve Jouanolou authorship and the separate annotation.')
e(2,'N','marginal mathematical questions',[('K22-01',39,40),('K22-01',113,114)],
  'The formal-series and Hopf-application margins contain actual question marks. The separate Cartier/hyperalgebra checklist is asserted and must not be swept into this question.',
  'The marginal doubts about the formal-power-series application and the Hopf application, with their precise hypotheses still to be recovered.',
  'Formal-series and Hopf-application marginal doubts',claims=[3,8])
e(3,'E','historical verification of an asserted gap',[('K22-01',66,70)],
  'The offprint says the result fills an apparent gap in Lang, and a margin says connu. It does not pose the later reader task of adjudicating Lang\'s proof.',
  'Compare Jouanolou\'s allegation with Lang\'s original proof and any correction; this historical task belongs outside the authorial mathematical-problem count.')
e(4,'N','explicit marginal doubt about a missing hypothesis',[('K22-01',78,80),('K22-01',93,98)],
  'The question-marked faux annotation is an actual source doubt. The separate Hopf question belongs to MP02.',
  'Does the stated analytic-reducedness lemma require the missing injectivity of A to B? Preserve the proposed insertion and marginal doubt.',
  'Injectivity in the analytic-reducedness lemma',claims=[7])
e(5,'K','explicit unresolved existence problem',[('K22-01',396,396)],
  'The text expressly says the general infinitesimal lifting problem is not known to have a solution; the later separable-residue existence case is distinguished.',
  'Existence of a Cohen lift in the stated general topological/noetherian setup, beyond the proved separable-residue case.')
e(6,'K','explicit questions under Questions ouvertes',[('K22-02',32,41)],
  'The source asks whether formal smoothness for the usual topology implies discrete formal smoothness and records pessimistic/negative annotations.',
  'Compare discrete and adic formal smoothness under exactly the hypotheses asked on the pages.')
e(7,'K','explicit open-locus question',[('K22-02',46,52),('K22-02',62,65)],
  'The source asks openness and localization stability, with conditional characteristic-zero annotations.',
  'Openness of the geometrically regular/formally smooth fibre locus for the stated noetherian maps and good-ring assumptions.')
e(8,'K','explicit flat-locus question',[('K22-02',67,67)],
  'The source asks est-il ouvert and marks the matter unknown, with a proposed generic-flatness reduction.',
  'Openness of the flat locus for a homomorphism of noetherian rings without adding finite presentation.')
e(9,'K','explicit unfinished proof step',[('K22-02',138,142)],
  'Il reste à prouver introduces a coefficient-selection step that ends in a fragment and ellipsis. The completed finite-support argument is our later reconstruction.',
  'Finish the stated choice of coefficients producing infinitely many nonzero differential coordinates in the nonsplitting argument.')
e(10,'E','reader verification of supplied counterexamples',[('K22-02',150,176),('K22-02',209,221)],
  'The source supplies examples and their arguments. Our checks of the field construction and printed EGA comparison are not questions asked by the author.',
  'Verify the supplied differential-kernel counterexamples and collate the extra generator in the printed field example.')
e(11,'E','reader verification and fragment identification',[('K22-02',191,205)],
  'The text announces formulas que l\'on vérifie comme l\'âne qui trotte, not an unperformed question. Missing preceding definitions are a reader limitation.',
  'Recover the preceding hypotheses/authorship of the reused trace, norm and idèle formulas and verify their stated identities.')
e(12,'E','reader verification of asserted adjunction formulas',[('K23-06',68,73)],
  'The map is expressly asserted to exist in all cases and to be an isomorphism under stated hypotheses. Extending/verifying this formulation and the discriminant computation is our task.',
  'Check the general adjunction construction, its isomorphism hypotheses and the asserted discriminant formulas.')
e(13,'E','reader verification of asserted base-change statements',[('K23-06',344,370)],
  'The primitive base-change conditions and Cartier/hyperalgebra checklist are assertions, not explicit questions or unfinished requests.',
  'Verify the primitive base-change and Cartier/hyperalgebra statements with their flatness or purity assumptions.')
e(14,'E','reader verification of asserted exponential criteria',[('K23-06',374,388),('K23-06',454,469)],
  'The exponential, nilpotent-ideal and derivation statements are presented as formulas/propositions. Target and uniformity issues were raised in our checking.',
  'Check the exponential criterion, the uniform nilpotence and central scalar-ideal hypotheses, and the stated derivation/base-change maps.')
e(15,'E','reader verification of an asserted Greenberg extension',[('K23-01',129,138)],
  'Ceci vaut ... sans ... augmentation asserts the extension and cites Greenberg. It is not a question; the actual cote26 Cas Greenberg? remains MP46.',
  'Check the unaugmented Greenberg extension of the infinitesimal principal homogeneous-space construction.')
e(16,'E','reader verification of a construction carried out on the pages',[('K23-01',302,306),('K23-01',344,353)],
  'Il suffit de définir ... et de vérifier introduces the construction that follows, not an expressly unresolved step. Our representability/locality check should not be attributed as a source question.',
  'Verify locality and representability of the principal-parts construction already given.')
e(17,'K','explicit classification programme',[('K23-02',161,170)],
  'On veut caractériser les foncteurs obtenus de cette façon explicitly introduces the classification task; the earlier diagrams supply its setting.',
  'Characterize the natural finite-order constructions obtained from the jet/principal-parts action, retaining the source locality and base assumptions.')
e(18,'N','explicit unfinished step in one example',[('K23-02',80,80)],
  'The source expressly leaves algebraic closure of k in A to be checked in example (i). The regularity argument for example (ii) is given and is not a separate authorial question.',
  'In example (i), verify that k is algebraically closed in A.',
  'Unfinished constant-field check in the first inseparable-curve example',claims=[42])
e(19,'N','cancelled mathematical query with unresolved reading',[('K23-02',99,103)],
  'A question mark survives inside a cancelled, partly unreadable df/delta-f comparison. It supports recording that narrow source query, not attributing all surrounding formal-diagonal assertions as questions.',
  'Record the cancelled df/delta-f comparison question only. Its exact formula cannot be recovered from the supplied transcription; do not replace it with a new well-posed theorem.',
  'Cancelled differential/formal-diagonal comparison query',claims=[43])
e(20,'N','authorial uncertainty about effects of definitional errata',[('K23-02',185,196)],
  'Lê explicitly says he does not know whether his definitional errata interfere with the demonstrations. This is an authentic unresolved check; the specific correction formulas themselves are proposed assertions.',
  'Determine whether Lê Dũng Tráng\'s definitional errata affect the proofs that use associated primes or depth, as his letter expressly leaves undecided.',
  'Effect of Lê’s definitional errata on the proofs',claims=[46])
e(21,'E','reader verification of an asserted gluing theorem',[('K23-02',249,266)],
  'The source states Alors il existe une unique section under its data. No question or deferred proof request is present.',
  'Verify the stated gluing theorem for a section of an unramified morphism.')
e(22,'N','explicit conjectural extension',[('K23-02',276,283)],
  'The margin says one should be able to remove local noetherianity and replace finite by integral. The finite theorem is an assertion.',
  'Remove the locally noetherian hypothesis and replace finite by integral in the stated unramified descent assertion.',
  'Integral nonnoetherian extension of unramified descent',claims=[48])
e(23,'K','explicit questioned definition and revision programme',[('K23-03',44,52)],
  'The cancelled reasonable-definition question and Vérifier §16 are explicit authorial checks; the nonnoetherian regular-immersion replacement is an unfinished revision programme.',
  'Assess the nonnoetherian regular-immersion definition, its permutation/Koszul behavior and the requested §16 revision.')
e(24,'K','explicit algebraic question and marginal doubts',[('K23-03',146,159),('K23-03',178,197)],
  'The finite-presentation base-kernel question and the question-marked separation objections are genuine source questions. Preserve Deligne\'s text separately from the annotating hand.',
  'The stated finite-presentation base-kernel question and the precise disputed separation hypotheses for A-subquotients.')
e(25,'N','question-marked Koszul equivalence',[('K23-03',214,214),('K23-03',416,426)],
  'The removal of separation at 19.5.5 is asserted and supported by a proof. The distinct Koszul-resolution condition carries an actual (?) and qualifies as a source doubt, subsequently addressed by the proof.',
  'The question-marked condition that the Koszul complex is a resolution in the stated equivalence for a minimally generated ideal of a local noetherian ring.',
  'Question-marked Koszul-resolution condition',claims=[58])
e(26,'E','reader verification of Deligne’s supplied refutation',[('K23-03',240,244)],
  'Deligne diagnoses the nonlinear lifting sets and supplies a finite-solvability counterexample, concluding that there is no hope for that compactness argument. Asking for a counterexample to the exact withdrawn theorem is our later refinement.',
  'Compare the withdrawn EGA0.19.3.12 statement with Deligne\'s refutation of its compactness proof; distinguish the theorem from the failed proof mechanism.')
e(27,'E','reader verification of an asserted relative theorem',[('K23-03',294,316)],
  'The relative Tor-dimension result is said to remain valid; the text supplies the pro-Tor proposition and proof route. Il faut savoir lists supporting ingredients, and the missing reference does not make the result an open question.',
  'Verify the stated relative Auslander–Buchsbaum and residue-field Tor-detection argument. The separate explicitly unresolved simplified reduction remains MP29.')
e(28,'E','reader verification of proved factorization',[('K23-03',322,345),('K23-03',384,392)],
  'The factorization is a proposition followed by its construction and flatness proof. Intermediate reste à voir steps are then discharged. A publication-placement aside or unclear index does not create a factorization problem.',
  'Verify the given minimal Cohen factorization and algebraic-extension reduction, preserving the local/complete hypotheses.')
e(29,'N','explicitly unresolved simpler proof',[('K23-03',531,531)],
  'Deligne says j\'en suis incapable about the direct N=A, M=B pro-Tor vanishing reduction. The general comparison was already proved earlier in the letter.',
  'Give the direct proof, requested by Deligne, that the indicated pro-Tor groups vanish in the N=A, M=B reduction.',
  'Deligne’s unfinished direct pro-Tor reduction',claims=[55,60])
e(30,'E','reader verification of an asserted equivalence',[('K23-03',483,505)],
  'The flatness/formal-projectivity proposition is stated and argued through to the flatness conclusion. It is not left as a source question.',
  'Verify the asserted flatness/topological formal-projectivity equivalence and the topology conventions.')
e(31,'N','marginal question about a proposed hypothesis weakening',[('K23-03',507,509)],
  'The literal question mark is attached to the proposed weakening at EGA0.19.4.6. The locality, sign and completion errata elsewhere are asserted corrections, not questions.',
  'The marginal doubt about the proposed replacement/removal of formal-projectivity hypotheses in EGA0.19.4.6.',
  'Questioned weakening in EGA0.19.4.6',claims=[61])
e(32,'E','reader verification of an asserted proof method',[('K23-04',14,30)],
  'The factorization/limit method is presented as an argument, not as a question whether the theorem holds.',
  'Compare the asserted Zariski Main Theorem limit/factorization argument with the exact published hypotheses.')
e(33,'E','reader verification of asserted approximation propositions',[('K23-04',34,68)],
  'The definitions and approximation propositions are assertions. The blank next list item does not authorize inventing a question about their validity.',
  'Verify the stated approximation-type and normal/geometrically-unibranch approximation propositions.')
e(34,'E','reader verification of a stated descent theorem',[('K23-04',126,153)],
  'Théorème9.4 explicitly asserts effective descent in four cases and starts the equalizer construction. It is not a source problem.',
  'Verify effective descent of étale sheaves under the four stated covering classes.')
e(35,'E','reader verification of asserted finite-cover criteria',[('K23-04',157,174),('K23-04',252,277)],
  'The clopen, h0 and finite-étale comparison conditions are propositions/criteria with arguments. The genuine broader étale-scheme caveat is kept separately in MP36.',
  'Verify the finite-étale full-faithfulness criteria and their base-change hypotheses.')
e(36,'N','explicit caveat and tentative extension',[('K23-04',304,322)],
  'Avec réserve, the U? diagram and il semble qu\'il faille supposer submersif make the extension genuinely tentative.',
  'Determine the additional separatedness or étale-base-change submersiveness required when extending the criterion to all étale schemes.',
  'Submersiveness in the extension to all étale schemes',claims=[69])
e(37,'E','reader identification of incomplete witnesses',[('K23-04',327,351),('K23-04',376,381)],
  'The truncated typed corollary and incomplete diagram lack readable data; no explicit authorial question is recorded. Identifying the maps and final published form is an editorial task.',
  'Identify and collate the constructibility/derived-comparison fragments without filling unreadable labels silently.')
e(38,'E','reader correction of asserted dimension statements',[('K23-05',10,32),('K23-05',80,99)],
  'The dimension and parameter statements are assertions. The counterexamples/corrections arise from our verification.',
  'Check the stated dimension-drop and parameter formulas, preserving the literal false versions and their present-run repairs.')
e(39,'N','explicit question-marked S_k implication',[('K23-05',349,355)],
  'The diagram explicitly marks the S_k transfer implication with ?. The much broader normality criterion and the definition of Z are assertions/reading issues.',
  'The question-marked implication that the indicated restricted/transported module retains S_k, with the change-of-ring depth caveat written immediately below.',
  'Questioned S_k transfer in the normalization notes',claims=[74])
e(40,'E','reader verification of asserted marginal Lefschetz statements',[('K23-05',220,220),('K23-05',375,393)],
  'The margins give implications and a theorem-style statement. The many transcription unsure markers are not authorial question marks. No explicit question or unfinished proof request can be established for this record.',
  'Verify and read the asserted Lefschetz/parafactorial margin statements; keep transcription uncertainty distinct from authorial uncertainty.')
e(41,'E','reader completion/verification of a claimed construction',[('K23-05',506,518)],
  'The source says Pour faire la construction d\'un exemple, chooses the projective input and hypersurface, and claims the conditions hold. Our concern about the existence choices is a proof audit, not an authorial question.',
  'Verify all existence choices and local-depth calculations in the supplied non-Cohen–Macaulay codimension-jump construction.')
e(42,'N','explicit deferred verification',[('K23-05',579,579)],
  'On devrait vérifier is an express authorial deferred check. Missing compatibility in the preceding asserted splitting is a separate present-run diagnosis.',
  'Verify that condition (b-double-prime) is independent of the chosen sections u^n.',
  'Independence of the sections in the graded condition',claims=[79])
e(43,'E','reader verification of an asserted Poincaré-series criterion',[('K23-05',582,621)],
  'The rank bounds and equality criterion are asserted. The extra hypotheses identified in checking them are not an authorial question.',
  'Verify the asserted Poincaré-series equality criterion with the required graded hypotheses.')
e(44,'K','explicit three-part mathematical question',[('K23-05',624,633),('K23-05',637,652)],
  'Question introduces the three flatness implications; the polynomial special case continues that request.',
  'The three stated graded flatness implications and their polynomial special case, including the literal false implication.')
e(45,'N','unfinished mathematical programme within an editorial plan',[('H26-01',44,44),('H26-01',185,196)],
  'The excellent-functor/morphism question and detached-equivalence-relation sketch are mathematical programme fragments. Chapter ordering and terminology substitutions are editorial tasks and must be separated.',
  'The question-marked excellent-functor/excellent-morphism programme and the tentative detached-pieces equivalence-relation construction. Their precise theorem statements remain unidentified.',
  'Mathematical programme fragments in the EGA V plan',claims=[83])
e(46,'N','explicit Greenberg-case question',[('H26-01',48,51)],
  'The plan literally asks Cas Greenberg? and about common treatment. The earlier unaugmented extension is asserted and belongs in ED15, not as an independent question here.',
  'Whether the elementary representability/restriction-of-scalars paragraph gives a common treatment including Greenberg\'s case.',
  'Greenberg’s case in the elementary representability plan',claims=[83])
e(47,'K','explicit unfinished Picard programme',[('H26-01',132,142)],
  'Manquent introduces missing topics and (?) attaches to the hyperplane-pencil Picard study.',
  'The stated missing qualitative Picard theory, especially the question-marked study using a hyperplane pencil.')
e(48,'K','problem listed under Problèmes-types à résoudre',[('H26-01',294,298)],
  'The problem heading supplies explicit authorial problem status.',
  'Rings of definition for structures without automorphisms, at the breadth of the source formulation.')
e(49,'K','problem listed under Problèmes-types à résoudre',[('H26-01',294,302)],
  'The heading and Résultats partiels annotation identify an authorial problem with only partial results recorded.',
  'Hilbert and Picard constructions without projectivity.')
e(50,'K','authorial problem marked solved later on the pages',[('H26-01',304,306)],
  'The problem-list entry is explicitly marked OK par Raynaud. A solved authorial question remains a legitimate problem record.',
  'The dual of a nonprojective abelian scheme, with the Raynaud resolution annotation retained.')
e(51,'K','problem listed under Problèmes-types à résoudre',[('H26-01',308,309)],
  'Entry c is an explicit problem-list item.',
  'Passage to quotients without a flatness hypothesis.')
e(52,'K','problem listed under Problèmes-types à résoudre',[('H26-01',314,318)],
  'Entry d is explicit; sans point fixe must not silently be replaced by a stronger modern freeness hypothesis.',
  'Quotients by GL_n acting sans point fixe, preserving the source ambiguity and Mumford annotation.')
e(53,'K','problem listed under Problèmes-types à résoudre',[('H26-01',316,318)],
  'Entry e explicitly asks for moduli of broadly general varieties and abelian schemes.',
  'Moduli of more or less arbitrary varieties, particularly abelian schemes.')
e(54,'K','problem listed under Problèmes-types à résoudre',[('H26-01',322,330)],
  'Entry f is an explicit classification problem, separating commutative and general affine groups.',
  'Relative classification of principal bundles with affine structural group, under the source distinctions.')
e(55,'K','explicit problem-list special case with ambiguous progress note',[('H26-01',324,335)],
  'Entry g identifies finite G as a special problem; the rédiger/vérifier/vérifié reading affects progress, not the existence of the problem entry.',
  'The finite structural group case, retaining the uncertain progress annotation.')
e(56,'K','explicit problem and well-posedness doubt',[('H26-01',337,338)],
  'The relative P1/GL_n case is explicitly marked Pb mal posé?.',
  'The relative P1 vector-bundle classification question and its well-posedness doubt.')
e(57,'K','explicit question marked affirmatively',[('H26-01',342,343)],
  'Sont-ils simples is a literal question, with oui circled.',
  'Formal moduli of an abelian variety being simples over the base, retaining the affirmative annotation.')
e(58,'K','problem listed under Problèmes-types à résoudre',[('H26-01',347,347)],
  'Entry j belongs to the explicit problem list.',
  'The theorem of the square in the nonprojective case.')
e(59,'N','cancelled mathematical programme with an explicit theta query',[('H26-01',205,221)],
  'The cancelled list is a prior mathematical programme; the theta-divisor entry contains ?. The separate Hom-notation question is editorial and should not broaden the mathematical problem.',
  'The cancelled Hilbert/Picard construction programme, particularly the theta-divisor query. Preserve cancellation; no chronology or unresolved modern status follows from it.',
  'Cancelled Hilbert/Picard construction programme',claims=[83])

a(1,'E','reader verification of asserted generator terminology',[('K21-01',13,33),('K21-01',35,52)],
  'The source states detection results and uses generator terminology. Our distinction between weak detection and a categorical generator is a verification task.',
  'Check exactly what generator/detection property the stated arguments establish.')
a(2,'N','explicit deferred mathematical exposition',[('K21-01',219,231)],
  'Il faudra expliciter les énoncés duals is an explicit deferred step. Sous réserve d\'existence elsewhere is a hypothesis convention, not by itself an existence conjecture.',
  'Write out the dual statements of2.6 and2.7 requested by the author, including their existence/product hypotheses. Do not attribute a general existence conjecture.',
  'Deferred dual statements in abstract representation',claims=[6])
a(3,'E','reader counterexample to an asserted recovery formula',[('K21-01',442,454)],
  'The representing-sheaf recovery formula is asserted. Its global failure and the counterexample were established in the present run.',
  'Verify and correct the global formula recovering the representing sheaf from evaluations at O_X/I^n.')
a(4,'K','explicit extension/generalization requests',[('K21-01',481,481),('K21-02',108,108)],
  'The margin asks to consider surjectivity, and the following leaf asks to generalize the localization lemmas.',
  'The stated surjectivity-only and general-localization extensions of the section-extension lemmas.')
a(5,'E','reader diagnosis of a claimed descent proof',[('K21-02',242,255)],
  'The proof explicitly claims that a glued object exists and concludes on a fini. Our effective-descent objection is not an authorial question.',
  'Identify the effective-descent hypothesis needed for the source\'s claimed categorical-depth gluing proof; retain the present-run prestack counterexample.')
a(6,'N','explicit marginal proof request',[('HC1-01',115,115),('HC1-01',137,137)],
  'The margin literally reads preuve/prouver for the phi comparison. The main trace-minimax proof is supplied; its cutoff normalization and atomic cases are our checks.',
  'The marginal request to prove phi_|1+A| <= phi_(1+|A|), preserving the preuve/prouver reading uncertainty and surrounding trace hypotheses.',
  'Marginal proof request for the absolute-value distribution inequality',claims=[24])
a(7,'E','reader verification with uncertain possible question glyph',[('K1-06',296,299)],
  'Non! is a correction, not a question. The only apparent question after unitary equivalence is transcribed as unsure{(?)|(2)}, so it cannot establish an authorial mathematical question without the missing scan.',
  'Verify the absolute-value spectral/unitary-equivalence assertion and locate Non!. Preserve the possible (?) versus (2) reading as an unresolved ink alarm, outside the confirmed problem count.')
a(8,'N','explicit deferred finite-rank verification',[('K1-02',511,514)],
  'The inserted imperative vérifier d\'après cas décomposable expressly defers a mathematical check. The broader request to add a preamble is editorial.',
  'Verify the finite-rank trace/exterior coefficient identity(14) from decomposable operators, as explicitly requested.',
  'Deferred decomposable-operator check for the exterior trace identity',claims=[35])
a(9,'N','explicit unfinished formulation',[('K1-02',91,91)],
  'Dans un sens évident à préciser expressly leaves the continuity statement to be formulated. Later spectral-cluster proofs are relevant fate evidence, not new source questions.',
  'Specify the sense in which the complete eigenvalue system of a compact operator depends continuously on the operator.',
  'Unspecified sense of spectral continuity',claims=[33,76,81])
a(10,'N','explicit deferred proof programme',[('K1-02',218,241)],
  'The theorem is asserted, but the future-tense Pour la preuve ... ramènera leaves the nonnormal reduction as a specific unexecuted proof step on this leaf. Later attempts/arguments remain evidence of its fate.',
  'Supply the announced reduction of the nonnormal trace/determinant formula to the positive Hermitian case; keep the theorem assertion separate from this deferred proof task.',
  'Announced nonnormal trace-formula reduction',claims=[37,60,64])
a(11,'N','tentative optimality conjecture',[('K1-02',389,389)],
  'Semblent les inégalités les plus fortes possibles is explicitly tentative. Index/exponent corrections to the asserted inequalities are separate reader tasks.',
  'The tentative strongest-possible claim for the indicated singular-value sum inequalities, with no invented exact modern extremal formulation.',
  'Tentative optimality of the singular-value sum bounds',claims=[38,39,40])
a(12,'K','explicit classification question',[('K1-02',466,468)],
  'Question Trouver la forme générale is unambiguous and is followed by a multivariable extension.',
  'Classify the scalar functions and the stated multivariable variants giving the requested singular-value subadditivity.')
a(13,'N','explicit marginal mathematical doubt',[('K1-03',469,475)],
  'The margin has an actual ? adjacent to(39), where symmetry is deleted. Other convexity variants are assertions and should remain claim-level checks.',
  'The question-marked product convexity inequality(39) after deletion of symmetry, with the source\'s finite-dimensional hypotheses.',
  'Question-marked convexity inequality after deleting symmetry',claims=[49])
a(14,'N','explicit marginal doubt in a reflexivity proof',[('K1-04',225,231)],
  'The ? follows the total-and-strongly-closed step in the asserted reflexivity equivalence. The broad duality/norm constructions have supplied arguments and are not independent questions.',
  'The marginal doubt about the total/strongly closed argument establishing the minimal/maximal sequence-space reflexivity equivalence.',
  'Marginal doubt in the reflexivity equivalence',claims=[53])
a(15,'E','reader correction of asserted formulas with a tentative aside',[('K1-05',108,135)],
  'Sauf erreur qualifies an asserted order example; it does not pose a formulated question or explicit deferred step. The wide collection of Cauchy/index/order repairs was assembled by the reader.',
  'Verify the stated entire-function order, genus and coefficient formulas; preserve the source\'s sauf erreur hesitation separately from an authorial problem.')
a(16,'E','reader correction of an asserted entire-function conclusion',[('K1-05',561,590)],
  'The source presents a proposition and concludes pas une fonction entière. The distinction between entire holomorphy and bounded type, and its counterexample analysis, are ours.',
  'Check the factorial elementary-symmetric-function example and distinguish holomorphy from bounded type without rewriting the source claim.')
a(17,'E','reader refutation of an asserted mixed determinant inequality',[('K1-06',50,81)],
  'The inequality is followed by Démonstration, not a question. The exact finite-dimensional counterexample is a present-run result.',
  'Verify/refute the literal mixed determinant inequality and preserve the valid surrounding inequalities.')
a(18,'N','explicit generalization questions and deferred reduction',[('K1-06',276,291),('K1-06',485,503)],
  'The Schatten-norm generalization?, Montrer finite-dimensional reduction, and ?? r>=1 margin are explicit mathematical requests. Dire quelles parties sont connues is bibliographic/editorial.',
  'The question-marked Schatten-norm and r>=1 trace extensions, together with the explicitly requested finite-dimensional reduction.',
  'Questioned Schatten and trace extensions of the analytic inequalities',claims=[69,73,75])
a(19,'K','explicit convergence and uniform-convexity questions',[('K1-07',183,188),('K1-07',278,282)],
  'Est-ce vrai and Question explicitly mark the conjectural convergence/uniform-convexity extensions.',
  'The stated finite-p convergence and uniform-convexity questions, retaining their p ranges and the source\'s Pas d\'importance annotation.')
a(20,'K','explicit fractional-power conjecture',[('K1-07',190,196),('K1-07',290,298)],
  'Est-ce que ... fonction croissante is an explicit question. The exact2x2 refutation is present-run fate evidence, not an authorial assertion.',
  'The stated monotonicity in the power parameter and the related precise-inequality request, with the exact source parameters preserved.')
a(21,'K','explicit eigenvalue-majorant question',[('K1-07',260,262)],
  'Majorations individuelles ... ou analogue? is a literal source question; the i/2 versus i/k reading remains unresolved.',
  'The individual eigenvalue majorant with the written i/2 or i/k index, or an analogous bound.')
a(22,'E','reader correction of an asserted adjugate theorem',[('K1-07',390,423)],
  'The page states a theorem and gives a proof ending in immediate spectral verification. The sign and monotonicity failures were detected in our checking.',
  'Verify the Fredholm-adjugate formulas, signs and asserted decreasing sequence; preserve the counterexamples and valid normal-operator bounds.')


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def evidence_record(file, start, end):
    p = BASE / 'sources/texts/codex' / (file + '_transcription.tex')
    lines = p.read_text().splitlines()
    assert 1 <= start <= end <= len(lines), (file, start, end, len(lines))
    return {'source': str(p.relative_to(BASE)), 'lines': f'{start}–{end}',
            'literal_transcription': '\n'.join(f'{i}: {lines[i-1]}' for i in range(start, end+1))}


rows = []
fingerprints = {}
directions = []
for owner, count in [('ega',59), ('analysis_curves',22)]:
    part = WORK / 'parts' / owner
    preserved=part/'provenance/pre_origin_audit'
    pp = (preserved if preserved.exists() else part) / 'problems.json'
    fingerprints[str(pp.relative_to(BASE))] = sha(pp)
    problems = json.loads(pp.read_text())
    claim_map = {c['id']: c for c in json.loads((part/'claims.json').read_text())}
    assert len(problems) == count
    assert set(SPECS[owner]) == set(range(1,count+1))
    for problem in problems:
        n = int(problem['id'].rsplit('-',1)[1])
        spec = SPECS[owner][n]
        ed = spec['action'] == 'E'
        target = problem['id'].replace('MP-', 'ED-', 1) if ed else problem['id']
        retained = problem['claims'] if spec['retained_claim_suffixes'] is None else [f'C-SA23-{owner}-{i:03}' for i in spec['retained_claim_suffixes']]
        assert all(c in claim_map for c in retained)
        assert all(c in problem['claims'] for c in retained)
        row = {
            'original_id': problem['id'], 'owner': owner,
            'action': {'E':'reclassify_to_editorial','N':'keep_narrowed','K':'keep'}[spec['action']],
            'proposed_id': target,
            'count_as_authorial_mathematical_problem': not ed,
            'origin_class': spec['origin_class'],
            'current_title': problem['title'],
            'current_as_he_states': problem['as_he_states'],
            'proposed_title': spec['proposed_title'] or (('Reader verification: ' if ed else '') + problem['title']),
            'proposed_scope': spec['proposed_scope'],
            'rationale': spec['rationale'],
            'source_evidence': [evidence_record(*ev) for ev in spec['evidence']],
            'existing_occurrences_preserved': problem['occurrences'],
            'retained_question_claims': [] if ed else retained,
            'claim_links_for_editorial_record': retained if ed else [],
            'asserted_context_claims_not_authorial_questions': [c for c in problem['claims'] if c not in retained],
            'source_authorship_as_current_claim_register': {c:claim_map[c].get('author','See source/claim attribution; not newly inferred') for c in retained},
            'authorship_caution': 'Printed/letter authorship remains unchanged. A marginal question is attributed to the annotating hand, not automatically to the printed author or letter writer.',
            'implementation_status': 'proposal only; owner register not changed',
        }
        rows.append(row)
    directions.extend(json.loads(((preserved if preserved.exists() else part)/'directions.json').read_text()))

by_id = {r['original_id']:r for r in rows}
impacts = []
for d in directions:
    affected = [by_id[p] for p in d['problems'] if p in by_id and by_id[p]['action'] != 'keep']
    if not affected:
        continue
    remaining = [p for p in d['problems'] if p in by_id and by_id[p]['count_as_authorial_mathematical_problem']]
    editorial = [by_id[p]['proposed_id'] for p in d['problems'] if p in by_id and not by_id[p]['count_as_authorial_mathematical_problem']]
    impacts.append({'id':d['id'],'title':d['title'],
       'remaining_authorial_problem_ids':remaining,
       'proposed_editorial_problem_ids':editorial,
       'narrowed_problem_scopes':[{'id':r['original_id'],'scope':r['proposed_scope']} for r in affected if r['action']=='keep_narrowed'],
       'recommendation': ('Keep as a reader/editorial research direction, explicitly outside the ranking of authorial open questions; do not invent an MP link to satisfy the schema.' if not remaining else 'Keep the direction but rewrite its provenance so only the remaining/narrowed MP records are described as authorial questions. ED links support reader verification tasks.')})

counts = {owner:dict(collections.Counter(r['action'] for r in rows if r['owner']==owner)) for owner in SPECS}
report = {
 'audit':'Manual bounded origin audit of all ega and analysis_curves problem records',
 'date':'2026-11-19',
 'status':'proposal only; no owner record mutation',
 'scope_counts': {'ega':59,'analysis_curves':22,'total':81},
 'decision_counts':counts,
 'rule':'An authorial mathematical problem requires an explicit question, explicit deferred mathematical step, tentative mathematical proposal, or unfinished mathematical programme. A proofless/false assertion, incomplete transcription, or our verification is insufficient. Source questions resolved later remain legitimate problem records.',
 'method':'Each row was assessed manually from the earlier complete source reading and targeted logged context rereads. The serializer only copies exact evidence and validates IDs; it does not infer verdicts from keywords.',
 'registers_unchanged_sha256':fingerprints,
 'rows':rows,
 'direction_impacts':impacts,
 'global_integration_notes':[
   'Keep all mathematical checks/counterexamples in the claim/check registers. Reclassification changes provenance and Stage3 counting, not the validity or value of those computations.',
   'Retain MP-to-ED aliases so old narrative IDs resolve; update direction problem fields and prose. Do not count aliases as additional problems.',
   'The tentative (?) versus (2) after unitary equivalence is an ink uncertainty, not a confirmed authorial question. It must remain in readings/editorial evidence.',
   'For narrowed records, preserve the old record and full occurrences in provenance, but distinguish asserted context from the specific source question.',
   'No new historical claim, literature research or mathematical verdict is introduced in this audit.'
 ],
 'additional_source_cues_for_parent_review':[
   {'source':'sources/texts/codex/K23-03_transcription.tex','lines':'236',
    'literal_transcription':evidence_record('K23-03',236,236)['literal_transcription'],
    'observation':'Deligne expressly defers proving the théorème de Lefschetz vache this year and hopes Grothendieck finds someone. This is a separate authorial proof request, not automatically identical to the asserted parafactorial margins in former MP40. Flagged for parent coverage review; no new record or mathematical identification is manufactured here.'}
 ],
 'validation':{'all_81_existing_ids_covered_once':len(rows)==81 and len(by_id)==81,
               'all_proposed_ids_unique':len({r['proposed_id'] for r in rows})==81,
               'source_line_ranges_valid':True,'retained_claim_ids_exist':True,
               'owner_registers_unchanged':all(sha(BASE/p)==h for p,h in fingerprints.items())}
}
assert all(report['validation'].values())
out = WORK/'integration/ega_problem_origin_review.json'
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'output':str(out),'counts':counts,
 'authorial_problems_retained':sum(r['count_as_authorial_mathematical_problem'] for r in rows),
 'editorial_reclassifications':[r['original_id'] for r in rows if not r['count_as_authorial_mathematical_problem']],
 'directions_without_authorial_MP':[d['id'] for d in impacts if not d['remaining_authorial_problem_ids']],
 'validation':report['validation']},ensure_ascii=False,indent=2))
