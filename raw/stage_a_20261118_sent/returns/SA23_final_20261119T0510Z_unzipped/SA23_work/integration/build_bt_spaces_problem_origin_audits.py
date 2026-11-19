"""Manual provenance decisions for bt/spaces; no owner/source mutations.

All source selections and decisions below are authored individually. Code only
copies their exact text and serializes metadata.
"""
from pathlib import Path
import collections
import hashlib
import json
import re

ROOT = Path('/workspace/scratch/0394364129a2')
PATHS = {
    'bt': 'sources/texts/pro/MPL_93_221-236+161-5_transcription.tex',
    's31': 'sources/texts/codex/K161-3-01_transcription.tex',
    's32': 'sources/texts/codex/K161-3-02_transcription.tex',
    's33': 'sources/texts/codex/K161-3-03_transcription.tex',
    's41': 'sources/texts/codex/K161-4-01_transcription.tex',
    's42': 'sources/texts/codex/K161-4-02_transcription.tex',
}
SOURCE_LINES = {key: (ROOT/path).read_text().splitlines() for key,path in PATHS.items()}
SNAPSHOT = ROOT/'SA23_work/integration/bt_spaces_problem_origin_inputs.json'
if SNAPSHOT.exists():
    INPUTS = json.loads(SNAPSHOT.read_text())
else:
    INPUTS = {owner: json.loads((ROOT/f'SA23_work/parts/{owner}/problems.json').read_text())
              for owner in ['bt','spaces']}
    SNAPSHOT.write_text(json.dumps(INPUTS,ensure_ascii=False,indent=2)+'\n')
ORIGINAL = {owner: {int(p['id'].rsplit('-',1)[1]):p for p in ps}
            for owner,ps in INPUTS.items()}
DECISIONS = {'bt': [], 'spaces': []}


def quote(key, lo, hi):
    lines = SOURCE_LINES[key]
    scans = []
    current = None
    for i,line in enumerate(lines[:hi],1):
        m = re.search(r'\\scanpage\{([^}]+)\}',line)
        if m: current = m.group(1)
        if i >= lo and current is not None and current not in scans: scans.append(current)
    return {'source': PATHS[key], 'physical_lines': [lo,hi],
            'scan_markers': scans, 'verbatim': '\n'.join(lines[lo-1:hi])}


def add(owner,n,decision,origin,cues,reason,wording=None,confidence='high',notes=None,author=None):
    p = ORIGINAL[owner][n]
    row = {'original_id':p['id'], 'original_title':p['title'],
           'original_as_he_states':p['as_he_states'],
           'original_occurrences':p['occurrences'],
           'decision':decision, 'origin':origin, 'confidence':confidence,
           'source_cues':[quote(*cue) for cue in cues], 'reason':reason,
           'source_question_found':decision != 'reclassify_to_editorial_task',
           'proposed_id': f'ED-SA23-{owner}-{n:02}' if decision == 'reclassify_to_editorial_task' else p['id']}
    if wording: row['recommended_as_he_states']=wording
    if notes: row['notes']=notes
    if author: row['source_author']=author
    DECISIONS[owner].append(row)


add('bt',1,'keep','authorial explicit characteristic question',[('bt',10,22)],
    'The circled Spécial à car.0? is an actual question; its uncertainty is authorial, not inferred from a missing proof.')
add('bt',2,'keep_narrow','authorial search for a criterion, answered on the pages',
    [('bt',73,84),('bt',175,179)],
    'Cherchons une condition suffisante maniable is the real authorial task. The Stein warning is an affirmative restriction; it does not itself ask for a repair. Preserve the criterion question and treat the extra hypothesis audit separately.',
    'Find a manageable infinitesimal/global sufficient criterion for an operator tuple to be Picard–Fuchs, and the indicated converse via fiber de Rham.',
    notes='Add the explicit cue at73 to the occurrence; the old76 start misses it.')
add('bt',3,'reclassify_to_editorial_task','present-run check of routine source assertions',
    [('bt',87,87),('bt',104,114)],
    'The operators are asserted to commute with the differential and the cohomology formula is said to be verified immediately. No question, exercise, or deferred proof is requested.',
    'Editorial task: verify differential compatibility and the displayed cohomology formula.')
add('bt',4,'keep','authorial explicitly admitted proof step',
    [('bt',167,175)],
    'The text expressly says that formula15 will not be proved here and is admitted. This is a self-flagged proof step, not merely a theorem lacking a written proof.',
    notes='Do not describe the formula as conjectural: it is admitted as a fact on the pages.')
add('bt',5,'keep','authorial explicit unfinished calculation',
    [('bt',187,187),('bt',190,206)],
    'The author explicitly asks for a formula without horizontal endpoints and ends by saying the two local terms must be calculated.',
    notes='The authorial request begins at187, before the old190 occurrence start.')
add('bt',6,'keep_narrow','authorial marginal deferred write-up',
    [('bt',224,243)],
    'The formal-exactness consequences are affirmative assertions, not questions. A separate uncertain margin says à rédiger and the heading specifies a relative version. Retain that real write-up instruction, not our demand to reconstruct the absent definition or repair order shifts.',
    'Write up the indicated relative version of the formal differential-operator exactness argument.',
    confidence='medium',notes='The cue à rédiger is itself inside unsure markup. Preserve that uncertainty; formal-exactness meaning and finite-order shifts remain reading/proof checks in Stage2/4.')
add('bt',7,'keep','authorial explicit injectivity question',
    [('bt',269,277)],
    'The arrow is explicitly labelled injectif?; the later conditional proof does not erase this source question.')
add('bt',8,'reclassify_to_editorial_task','present-run completion of an abbreviated condition list',
    [('bt',308,313)],
    'The text says that rho_infinity satisfies special conditions and lists surjectivity plus integrability. It does not ask what the conditions are or promise to supply them later. Turning that abbreviated qualification into a problem is reader reconstruction.',
    'Editorial task: identify the precise integrability/cocycle conditions intended by the abbreviated list.',
    confidence='medium',notes='The trailing dash remains an incompleteness alarm; it is not enough by itself to establish an authorial question.')
add('bt',9,'reclassify_to_editorial_task','present-run scope check of a marginal assertion',
    [('bt',324,325)],
    'The margin affirms that local T-isomorphism suffices. It has no question mark or request to check which consequences survive. The scope question is ours.',
    'Editorial task: determine the scope of the asserted weakening from smoothness to local T-isomorphism over X0.')
add('bt',10,'reclassify_to_editorial_task','present-run verification of a completed construction',
    [('bt',379,400),('bt',442,459)],
    'On veut en conclure introduces the construction’s goal; the following pages construct the derived morphism and state the conclusion. There is no separate doubt, promised later step, or request to finish it. Conflicting notation generates our verification task.',
    'Editorial task: verify the torsor/homotopy construction of the derived morphism, distinguishing the source formulas from present-run repairs.',
    confidence='medium')
add('bt',11,'reclassify_to_editorial_task','present-run expansion of a known proof sketch',
    [('bt',566,570)],
    'Serre calls the invariant-tensor lemma well known and immediately sketches its proof. He neither asks a question nor defers an unresolved step.',
    'Editorial task: check and, if useful, expand the supplied reductive invariant-tensor proof.',author='Jean-Pierre Serre, attached printed text')
add('bt',12,'reclassify_to_editorial_task','present-run verification of elementary asserted formulas',
    [('bt',634,638)],
    'The dual formula is stated and its verification called immediate; tensor stability is also asserted. Neither is a question or deferred step.',
    'Editorial task: check the Hodge–Tate dual and tensor conventions.',author='Jean-Pierre Serre, attached printed text')
add('bt',13,'keep','authorial expressly provisional admission answered later',
    [('bt',866,868),('bt',875,875),('bt',913,918)],
    'Admettons provisoirement explicitly marks a deferred lemma. The same text then proves it, so the correct status is an answered deferred step, not a current open problem.',
    author='Jean-Pierre Serre, attached printed text')
add('bt',14,'reclassify_to_editorial_task','present-run verification of an asserted extension',
    [('bt',926,927)],
    'Serre asserts the centralizer equality and says its proof is analogous but more complicated. He does not ask for it or promise a later proof. The margin voir Sen is a bibliographic pointer, not an open-question cue.',
    'Editorial task: verify the asserted general formal-group centralizer equality and identify the Sen reference.',author='Jean-Pierre Serre, attached printed text; marginal annotator not identified here')
add('bt',15,'keep','source-author explicitly missing direct proof',
    [('bt',929,935)],
    'The author states that he knows no direct proof. The source problem is methodological, even though inertia openness is already established by the indirect proof.',
    author='Jean-Pierre Serre, attached printed text')
add('bt',16,'keep','source-author explicit ramification question',
    [('bt',937,950)],
    'The source explicitly asks the relation between the filtrations and whether the proposed asymptotic equation holds.',
    author='Jean-Pierre Serre, attached printed text')
add('bt',17,'keep','source-author conjecture with later marginal resolution',
    [('bt',1037,1043)],
    'Il est probable explicitly marks the general neutral-envelope characterization as conjectural; the marginal Sen resolution is a distinct later layer.',
    author='Jean-Pierre Serre, attached course summary; marginal annotator not identified here')
add('bt',18,'reclassify_to_editorial_task','present-run research direction partly imported from later literature',
    [('bt',1068,1075)],
    'The supplied course summary reports an essai de classification and gives a later Springer pointer; it does not pose the realization question. That question was imported from the separately consulted Serre1979 text. It must not be attributed to these pages.',
    'Editorial/literature task: compare the reported two-weight classification with the distinct realization problem in later Serre literature.',
    confidence='medium',notes='Retain the classification program as a source subject and the later realization question as an external literature lead, not a new archival question.',
    author='Jean-Pierre Serre, attached course summary')
add('bt',19,'keep','source-author tentative extension to equal characteristic',
    [('bt',1081,1081)],
    'The summary explicitly says Raynaud’s different proof might adapt to equal characteristic. This is a real tentative extension rather than a condition assumed in a theorem.',
    author='Jean-Pierre Serre, attached course summary')
add('bt',20,'keep','source report of unresolved technical proof difficulties',
    [('bt',1083,1083)],
    'The report explicitly says the technical difficulties of Tate’s alternative method were not entirely resolved. Keep the proof-method problem distinct from the already-proved theorem.',
    author='Jean-Pierre Serre reporting Tate’s seminar method')
add('bt',21,'keep','authorial explicit tensor-extension question',
    [('bt',1188,1202)],
    'Question Peut-on prolonger is explicit and lists the tensor/internal-Hom/filtration compatibilities sought.')
add('bt',22,'keep','authorial explicit uniqueness question',
    [('bt',1200,1202)],
    'A-t-on unicité ... à isom unique près? is an explicit separate uniqueness clause of the extension question.')
add('bt',23,'keep_narrow','authorial unfinished qualification of a uniqueness assertion',
    [('bt',1363,1365),('bt',1399,1404)],
    'Du moins si leaves an identifiable condition unfinished after the uniqueness assertion. Preserve that narrow unfinished proposal. The separate torsor-triviality phrase is an uncertain assertion, not another authorial question.',
    'What is the unfinished Du moins si qualification attached to the asserted uniqueness of j? The precise condition is not supplied.',
    confidence='medium',notes='Do not invent the missing hypothesis. The R_L triviality wording remains an editorial reading alarm, not a source question.')
add('bt',24,'reclassify_to_editorial_task','present-run existence question inferred from a conditional construction',
    [('bt',1433,1448),('bt',1454,1458),('bt',1470,1486)],
    'The text packages the action into an extension and then assumes a section in order to classify other sections. A conditional existence hypothesis is not a question asking whether a section exists. The genuine question that follows is uniqueness/conjugacy, under MP25.',
    'Editorial task: identify Gamma and the extension and determine which existence assumptions the subsequent cocycle classification uses.')
add('bt',25,'keep_narrow','authorial explicit relative conjugacy question',
    [('bt',1489,1498)],
    'The final paragraph explicitly asks whether extensions of the fixed partial section are conjugate. The comparison of Pro/Codex deletion scope is our source-fidelity task and should not be part of the mathematical question.',
    'Are the sections alpha extending alpha0 conjugate under the indicated group? Would injectivity, or the stated weaker trivial-kernel condition, of H1 restriction suffice?',
    notes='Preserve the conflicting deletion witnesses in the occurrence/status record. No scan-based adjudication is made by this audit.')


add('spaces',1,'keep','authorial explicit missing formula',[('s31',80,85)],
    'The inverse-image display has an authorial question mark and an empty right side; this is a genuine formula request.')
add('spaces',2,'keep_narrow','authorial explicit product-equivalence and embedding questions',
    [('s42',4,7),('s42',33,41),('s42',66,79),('s41',731,750)],
    'The product comparison is explicitly asked in cote161-4, and the embedding is separately questioned in its margin. The affirmative general product construction and its completed finite-limit proof are supporting claims, not additional open questions. The final essential-image assertion is the proposed route to the answer and is not itself a separately phrased question.',
    'Is the presheaf/product-topos comparison an equivalence? Can one verify that the indicated comparison alpha is an embedding? The page proposes, but does not complete, an essential-image argument.',
    notes='The independently checked cancelled question at161-6 scan23 is a repeated witness being consolidated by root from MP-SA23-misc-19; preserve its cancelled status. The false two-direct-image test remains a Stage2 claim and correction, not a newly invented source question. Cote161-4 scan16 also has a cancelled explicit le faire instruction to verify an intersection of functor subcategories. This genuine deferred verification is distinct from the false projection-direct-image test; preserve that distinction.')
add('spaces',3,'keep_narrow','authorial cancelled unfinished construction proposal',
    [('s31',311,346)],
    'The cancelled sentence Pour avoir la limite ... il faut breaks off into unfinished descent diagrams. It is an identifiable abandoned construction proposal rather than a proved/asserted theorem whose missing proof we have promoted into a question.',
    'Unfinished cancelled proposal: construct the general limit of a fibred topos using the indicated descent diagram. The necessary coherences and indexing hypotheses are not supplied.',
    confidence='medium',notes='Retain only as an unfinished proposal, not a fully formulated universal existence conjecture. No missing hypotheses are invented.')
add('spaces',4,'keep','authorial explicit search for comparison conditions, answered in part',
    [('s31',350,376),('s31',387,393)],
    'The author expressly asks for conditions for equivalence at360, says voir si at372, and calls it la question at376. The following sufficient-condition proposition and proof do not erase that actual question.',
    'Find conditions under which the canonical comparison from the topos of a product of spaces to the product of their topoi is an equivalence; equivalently, when the two rectangle-cover topologies coincide.')
add('spaces',5,'reclassify_to_editorial_task','present-run review of an asserted and proved refinement',
    [('s31',434,447),('s31',468,477)],
    'The refinement is introduced by Je dis qu’alors and followed by a completed proof ending OK. No question, exercise, or later proof request occurs.',
    'Editorial task: check and explain the proved locally closed compact-point refinement and its exact hypotheses.')
add('spaces',6,'reclassify_to_editorial_task','present-run hypothesis check of a proved theorem',
    [('s31',483,491),('s31',532,542)],
    'The infinite-product comparison is asserted under displayed assumptions and the proof ends cqfd. A broader classification or hypothesis audit is our follow-up, not an authorial question.',
    'Editorial task: check the finite-tail and compactness hypotheses in the supplied infinite-product argument.')
add('spaces',7,'keep_narrow','authorial explicit unfinished covering question',
    [('s31',550,576)],
    'The counterexample attempt contains a margin question mark, the deleted phrase la question est de voir, and an unfinished test of whether a covering family is always covering for pi. These are actual questioning cues even though the proposed blanket counterexample is too broad.',
    'In the proposed infinite-discrete product example, is the displayed family always covering for pi? The attempted contrary example and the reformulation ending ou encore are unfinished.',
    notes='Keep the counterexample conclusion separate from the covering question; preserve deletion and transcription uncertainty.')
add('spaces',8,'keep','authorial explicit doubt and missing projection formula',
    [('s31',588,590),('s31',613,618)],
    'Il est douteux marks actual doubt about remaining essential, and the projection inverse-image display is left blank.')
add('spaces',9,'keep_narrow','authorial explicit cocontinuity question',
    [('s31',785,793),('s31',851,852)],
    'The source asks to determine the colimit-preserving functors and explicitly says automatic cocontinuity of beta(u0) is not clear. The adjacent adjunction assertion itself is not an additional question.',
    'Determine the functors from the sheaf topos to E commuting with small colimits; in particular, is beta(u0) automatically cocontinuous for every u0?')
add('spaces',10,'keep','authorial explicit question answered on the same page',
    [('s31',895,904)],
    'Est-il vrai explicitly asks whether colimit-preserving functors correspond through the localization. The following calculation answers OK; keep as an answered source question.')
add('spaces',11,'keep','authorial explicit sufficiency question with marginal negative answer',
    [('s31',936,942),('s32',1,7)],
    'Cela est-il suffisant? and the marginal non are explicit. The following attempted argument is unfinished, but the question does not depend on inferring openness from that omission.')


add('spaces',12,'keep_narrow','authorial explicit exercises, answered on the pages',
    [('s32',62,79),('s32',101,114),('s32',119,131)],
    'Montrer que explicitly assigns the specialization-stability and adjunction verifications. The subsequent proof answers the adjunction exercise; surrounding corollaries are not additional questions.',
    'Show that opens are stable under generalization and that rho and sigma are associated adjunction morphisms giving Hom_Esp(beta I,X) ≃ Hom_Preord(I,alpha X).')
add('spaces',13,'keep','authorial explicit exercises and interpretation request',
    [('s32',170,188),('s32',199,212)],
    'En conclure, Prouver que, and Interpréter are explicit requests concerning irreducible closed sets, the sheaf/presheaf equivalence, and points as pro-objects.')
add('spaces',14,'reclassify_to_editorial_task','present-run proof check of an equivalence list',
    [('s32',214,224),('s32',226,244)],
    'The sobriety/artinian conditions are simply listed as equivalent. The Prouver que phrases occur in the subsequent j)-paragraph and concern spatial presheaf topoi, already MP15; they must not be quoted as a request to prove i).',
    'Editorial task: verify the asserted sobriety/descending-chain criterion and resolve the X versus sobrification wording in condition delta.',
    notes='The old as_he_states misplaced the later exercise cue. Its mathematical claim C-SA23-spaces-018 remains unchanged.')
add('spaces',15,'keep_narrow','authorial explicit exercises and repeated answered question',
    [('s32',226,244),('s33',31,31)],
    'The two Prouver que instructions explicitly ask for the presheaf/preorder criterion and the very-dense essential-point criterion. Scan41 repeats the main subject as Question and supplies an answer.',
    'Prove that PSh(C) satisfies the displayed spatial-essential conditions exactly when C is a preorder, and that Sh(X) does so exactly when the essential points of X are very dense. The later leaf asks again when PSh(C) can equal Sh(X).')
add('spaces',16,'reclassify_to_editorial_task','present-run correction of an unqualified asserted equivalence',
    [('s32',247,255)],
    'On a des équivalences is an assertion; the NB says one recovers X and is not phrased as a question. Choosing essential rather than arbitrary morphisms is our necessary correction, not an archival question.',
    'Editorial task: correct the morphism class in the asserted preorder/topos 2-equivalence and audit the recovery statement.')
add('spaces',17,'keep','authorial explicit frame-map questions',
    [('s32',258,269),('s32',356,382)],
    'The source explicitly asks preservation of finite meets, bijectivity of the restriction map, and the last rectangle value. The finite-meet calculation supplies a partial answer.')
add('spaces',18,'keep_narrow','authorial deleted question answered by the subsequent proof',
    [('s32',434,450),('s32',551,588)],
    'The general Morita equivalence and rigidified uniqueness are asserted/proved, so they are not themselves open problems. There is, however, a literal deleted question whether the target gerbe is banded by GL(e)×GL(g). Preserve that narrow momentary question, answered by the automorphism computation.',
    'Deleted question: is the gerbe C-prime_(g,e) banded by GL(e)×GL(g)? The later calculation identifies the automorphism group and completes the proof.',
    notes='The question mark at438 lies outside the unsure markup but inside deleted. Do not promote the routine reste à prouver proof transitions or the compressed corollary into separate source questions.')
add('spaces',19,'reclassify_to_editorial_task','present-run identification of an unreadably specified diagram',
    [('s32',470,476),('s32',498,518)],
    'The diagrams display proposed isomorphisms and uncertain arrow labels, but no identifiable authorial question or assigned task. Recovering their coefficients and degree conventions is a source-reading task.',
    'Editorial task: identify the higher-torsor/hypercohomology diagram before attributing a theorem or question to it.',
    confidence='medium',notes='Keep the genuinely unidentifiable mathematical fragment as a Stage2 class-F claim; its uncertainty is not converted into an authorial open question.')
add('spaces',20,'reclassify_to_editorial_task','present-run expansion of an asserted known theorem',
    [('s32',640,655),('s32',767,769)],
    'Bijectivity is asserted, called a little more subtle, and referred to an existing SGA/Hakim exercise. This is not an express request to solve or defer that proof on these pages. The margin Start with describes exposition order, not an unresolved mathematical step.',
    'Editorial task: supply the cited sober-space reconstruction proof and clarify the exposition order.',
    notes='Retain the source-author editorial outline as such; do not turn its citation of an external exercise into a newly assigned archival exercise.')
add('spaces',21,'keep','authorial explicit foundational motivation question',
    [('s32',918,934)],
    'What will insure ... ? explicitly asks how the chosen axioms entail other topos properties. The question is answered at the foundational level by the cited Giraud theorem.')
add('spaces',22,'keep_narrow','authorial tentative universal extension',
    [('s32',771,776)],
    'Possibly all marks an explicitly uncertain extension from most structures to all structures. Retain only this tentative scope speculation, not the uncontroversial assertion that many structures have classifying topoi.',
    'Tentative extension: can the classifying-topos construction apply to all the algebraic and nonalgebraic structures being discussed? The word structures is not delimited on this leaf.',
    confidence='medium',notes='This is a qualified conjectural broadening, not a precise unrestricted theorem or a conditional representability hypothesis. Its formulation needs specification before mathematical development.')
add('spaces',23,'reclassify_to_editorial_task','present-run existence question inferred from an explicit hypothesis',
    [('s32',827,842),('s32',844,870)],
    'Supposons qu’il existe assumes a representing object before giving its 2-Yoneda consequences. It neither asks whether one exists nor asserts universal representability. The uncertain Ex/Exp heading does not supply a reliable exercise instruction.',
    'Editorial task: specify the representation hypotheses under which the displayed 2-Yoneda consequences apply.')
add('spaces',24,'keep_narrow','authorial explicit investigation of existence and uniqueness',
    [('s32',938,951),('s33',34,35)],
    'On se propose ... d’étudier l’existence et l’unicité is an explicit program for varying lambda, with the field models prescribed over Sets. The subsequent nonexistence assertion and ring-map tests are attempted answers, not additional questions.',
    'For the displayed types lambda, study existence and uniqueness of a full subtype of the ring theory whose Set-models are exactly fields.',
    notes='The cancelled continuation explicitly calls this la question. Its false field-recognition assertion is a proposed answer preserved under C-SA23-spaces-035 and an editorial correction, not a duplicate question.')
add('spaces',25,'reclassify_to_editorial_task','present-run correction of a cancelled asserted criterion',
    [('s33',43,49)],
    'Cette application est bijective ssi C est un corps asserts the criterion; the following connectedness argument is unfinished but contains no separate query. It is an attempted answer within MP24, not a new authorial question generated by our counterexample.',
    'Editorial task: explain why the cancelled criterion recognizes a larger class than fields and retain its relation to the genuine MP24 investigation.')


add('spaces',26,'keep_narrow','authorial explicit reconstruction and functoriality questions',
    [('s33',98,119),('s33',178,192)],
    'The margin asks for R_T in terms of T(Ens), the list has genuine question marks, and the next leaf explicitly asks how to define T(f) and when the comparison is an equivalence. These are actual questions, unlike the earlier representability assumption.',
    'Recover the theory from T(Ens) and its underlying-set functors: how is T(f) defined from these data, and under what conditions is T(C)→Hom_lambda(R,C) an equivalence? The earlier list also questions colimits and the proposed reconstruction formula.',
    notes='The later cancelled cocompletion assertions are attempted answers. Their cancelled status is retained; the audit does not turn every hypothesis in the reconstruction argument into a question.')
add('spaces',27,'reclassify_to_editorial_task','present-run completion of a lecture outline',
    [('s33',201,214)],
    'The right adjoint is called more complicated without being questioned, and Topos somme is only an undeveloped heading. No explicit problem, assignment, or promise to supply the formula later occurs.',
    'Editorial task: supply the dependent-product formula and identify the intended sums-of-topoi exposition.')
add('spaces',28,'keep','authorial explicit foundational write-up task',
    [('s33',383,400)],
    'See how to fix universe and restrict to U-sites explicitly assigns the size issue to be handled. It is a known foundational exposition task, not a new set-theoretic conjecture.')
add('spaces',29,'reclassify_to_editorial_task','present-run verification of an asserted criterion and proof',
    [('s41',13,22),('s41',34,36)],
    'The criterion is asserted and proved; the marginal Suffisant: ellipsis is an abbreviated proof, not a question or explicit later-proof request. The missing flatness hypothesis in the module margin is our correction.',
    'Editorial task: check the faithful-flat fiber criterion, retaining flatness as an independent hypothesis.')
add('spaces',30,'keep_narrow','authorial explicit question on an exactness row',
    [('s41',94,116)],
    'The extra locally-closed row ends in an authorial question mark. Open/closed exactness and the subsequent corollary are asserted and should not be separately presented as questions.',
    'Does the bracketed locally-closed exactness row, with the uncertain rc/qc qualifier, hold under the stated descent hypotheses?',
    notes='The qualifier is transcribed as unsure{rc|qc}; do not silently settle it or replace subset descent by effective descent of arbitrary immersions.')
add('spaces',31,'keep','authorial explicit checklist doubt',
    [('s41',176,182)],
    'The literal parenthetical question mark after formal smoothness marks a genuine doubt about descent.')
add('spaces',32,'keep_narrow','authorial explicit explanatory exercise',
    [('s41',206,208)],
    'Expliquer ce que cela signifie assigns an explanatory task. The effective-descent theorem is asserted; the source does not ask to prove it or express doubt about it.',
    'Explain what it means that a faithfully flat quasi-compact morphism is universally of effective descent for quasi-coherent modules.')
add('spaces',33,'keep','authorial explicit questions with later asserted answer',
    [('s41',174,178),('s41',228,228),('s41',246,248)],
    'The cancelled Question about immersions and the margin Peut-on descendre are literal questions. The later unqualified corollary is an attempted answer, not grounds to erase their provenance.',
    notes='Preserve both cancellation and the uncertain marginal immersion qualifier. The modern distinction between quasi-compact/fppf cases and arbitrary fpqc descent remains in Stage2 fate.')
add('spaces',34,'keep_narrow','authorial explicit unfinished topic of questions',
    [('s41',294,296)],
    'The numbered heading explicitly says Questions d’effectivité des données de descente. It identifies planned questions but gives no precise general theorem to prove. The preceding claim about projective and quasi-projective morphisms is not itself phrased as a question.',
    'Unfinished planned topic: questions of effectivity of descent data. No more precise question is written under the heading.',
    confidence='medium',notes='Keep as an authorial unfinished questions-program, not as a claim that he asked for a classification of all effective descent data or a proof of the preceding exclusivity remark.')
add('spaces',35,'reclassify_to_editorial_task','present-run expansion of an asserted known converse',
    [('s41',300,314)],
    'On peut prouver la réciproque affirms that the converse is provable and calls it more delicate. There is no question, express promise of a later proof, or exercise instruction. The earlier summary calling it deferred was too strong.',
    'Editorial task: supply the known converse characterization of universal homeomorphisms and its hypotheses.')
add('spaces',36,'keep_narrow','authorial explicit exercise',
    [('s41',465,485),('s41',525,547),('s41',583,585)],
    'Ex: vérifier sur diagonal, sections, noyaux is an explicit exercise; the earlier deleted Ex is a second witness. The many adjacent morphism-property assertions are not all separate questions.',
    'Verify the diagonal, section, and equalizer examples and the stated base-change/composition argument for the indicated class of morphisms.')
add('spaces',37,'keep_narrow','authorial explicit formulation question',
    [('s41',704,714)],
    'Comment exprimer ... qu’un co-foncteur ... est un faisceau? explicitly asks for a commutative-algebra formulation. The later representability proposition is a supporting development, not a separately asked theorem.',
    'Express in commutative-algebra terms when a contravariant functor on affine k-schemes is a Zariski sheaf.')
add('spaces',38,'keep_narrow','authorial explicit formula to be supplied',
    [('s42',173,184)],
    'The line formule pour the closure names an absent formula to be supplied; the next line gives only the related dominance condition. Retain this modest computation task.',
    'Supply the formula for the closure of phi(V(J)) under the affine morphism associated to A→B.')
add('spaces',39,'keep_narrow','authorial explicit example request',
    [('s42',225,228),('s42',249,263)],
    'The margin donner exemple explicitly asks for a product example. The point-set fiber formula itself is asserted, so the question should be the example request rather than a new theorem-proof task.',
    'Give the indicated example showing that the underlying-spectrum construction does not commute with products, even over an algebraically closed field.')
add('spaces',40,'keep_narrow','authorial explicit missing algebra formula',
    [('s42',489,511)],
    'The square literally has C=?. This is a real formula request, despite the neighboring quotient-ring formula already indicating the answer.',
    'Identify C in the displayed pushout square B←A⊗A→A.')
add('spaces',41,'keep_narrow','uncertain authorial punctuation marking a formula doubt',
    [('s42',550,568)],
    'A single question mark is transcribed after the idempotent description, but the mark itself is inside unsure. Preserve it as a possible authorial doubt with explicit uncertainty; do not promote the preceding non-bijectivity assertion or the infinite-family extrapolation into questions.',
    'Possible question, conditional on the uncertain punctuation: is the stated idempotent description of maps from a finite product algebra correct?',
    confidence='medium',notes='The only questioning cue is unsure{?} at563. Final counts should identify this as an uncertain source question, not a securely read literal question. Finiteness comes from the surrounding paragraph.')
add('spaces',42,'keep_narrow','authorial explicit deferred quotient discussion and definition task',
    [('s42',541,548),('s42',594,594)],
    'The margin asks to define the equivalence relation associated to a subgroup, and On reviendra dessus expressly defers the finite-relation quotient discussion. Those are real authorial steps. The G/B collapse example and finite-case OK are assertions, not separate questions.',
    'Define the relation associated to a subgroup, and return later to the quotient question for an equivalence relation finite over X.',
    notes='The word quotient is not specified sufficiently to identify effectivity, geometric existence, and affine coequalizer as one theorem. Keep the established distinctions in the fate record.')
add('spaces',43,'reclassify_to_editorial_task','present-run completion of an abbreviated proof',
    [('s42',754,768)],
    'The sheaf theorem is asserted and the proof reduced to f=1, ending with an ellipsis. There is no explicit exercise, doubt, provisional admission, or promise of a later proof. Missing exposition alone does not establish a source question.',
    'Editorial task: supply the remaining elementary localization-equalizer proof of the asserted affine sheaf theorem.')


if __name__ == '__main__':
    for owner, expected in [('bt',25),('spaces',43)]:
        rows=sorted(DECISIONS[owner],key=lambda r:r['original_id'])
        if not rows: continue
        assert len(rows)==len({r['original_id'] for r in rows})
        done={int(r['original_id'].rsplit('-',1)[1]) for r in rows}
        paths=sorted({q['source'] for row in rows for q in row['source_cues']})
        payload={
            'audit_date':'2026-11-19',
            'auditor':'GPT-6 Astra Pro; owner bt; SA23-20261119',
            'scope':f'Manual provenance audit of the original{expected} {owner} problem records; proposals only, no source or owner register mutations.',
            'method':'Decisions are manually assigned from exact source cues. Routine assertion, proof sketch, conditional hypothesis, transcription uncertainty, and reader repair are not automatically authorial questions. Express provisional/deferred steps and genuine questions remain source records even when answered later.',
            'completion':'complete' if len(rows)==expected else 'incremental',
            'audited_count':len(rows),'total_input_count':expected,
            'pending_original_ids':[ORIGINAL[owner][n]['id'] for n in sorted(ORIGINAL[owner]) if n not in done],
            'decision_counts':dict(collections.Counter(r['decision'] for r in rows)),
            'source_hashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
            'decisions':rows,
        }
        out=ROOT/f'SA23_work/integration/{owner}_problem_origin_audit.json'
        out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps({'owner':owner,'completion':payload['completion'],'audited_count':len(rows),'decision_counts':payload['decision_counts']}))
