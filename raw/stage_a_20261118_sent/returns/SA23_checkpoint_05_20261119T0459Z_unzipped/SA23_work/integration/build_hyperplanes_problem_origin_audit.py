"""Manual provenance decisions; code only copies selected literal source ranges.

This integration audit never changes the source or the owner's registers.
"""
from pathlib import Path
import collections
import hashlib
import json
import re

ROOT = Path('/workspace/scratch/0394364129a2')
SOURCE = ROOT / 'sources/texts/api/ega_v_cote25_combined.tex'
PROBLEMS = ROOT / 'SA23_work/parts/hyperplanes/problems.json'
OUT = ROOT / 'SA23_work/integration/hyperplanes_problem_origin_audit.json'
lines = SOURCE.read_text().splitlines()
input_records = json.loads(PROBLEMS.read_text())
# Root may append the newly found MP69 while this audit is running. Its remit
# remains the original68 records; the new cue is reported separately below.
original = {int(p['id'].rsplit('-', 1)[1]): p for p in input_records
            if int(p['id'].rsplit('-', 1)[1]) <= 68}
decisions = []


def excerpt(lo, hi):
    scans = []
    current = None
    for i, line in enumerate(lines[:hi], 1):
        m = re.search(r'\\scanpage\{25/(\d+)\}', line)
        if m:
            current = int(m.group(1))
        if i >= lo and current is not None and current not in scans:
            scans.append(current)
    return {'source': 'sources/texts/api/ega_v_cote25_combined.tex',
            'physical_lines': [lo, hi], 'cote': '25', 'scans': scans,
            'verbatim': '\n'.join(lines[lo-1:hi])}


def add(n, decision, origin, cues, reviewed, reason, wording=None,
        confidence='high', notes=None):
    p = original[n]
    row = {'original_id': p['id'], 'original_title': p['title'],
           'original_as_he_states': p['as_he_states'],
           'original_claim_ids': p.get('claims', []),
           'original_occurrences': p.get('occurrences', []),
           'decision': decision, 'origin': origin,
           'confidence': confidence,
           'source_cues': [excerpt(*x) for x in cues],
           'reviewed_physical_ranges': reviewed,
           'reason': reason}
    if decision == 'reclassify_to_editorial_task':
        row['proposed_id'] = f'ED-SA23-hyp-{n:02}'
        row['source_question_found'] = False
    else:
        row['proposed_id'] = p['id']
        row['source_question_found'] = True
    if wording:
        row['recommended_as_he_states'] = wording
    if notes:
        row['notes'] = notes
    decisions.append(row)


add(1, 'keep', 'authorial deferred reference/proof request',
    [(675,685)], [(609,692)],
    'He explicitly leaves the choice and copying of a proof to his collaborator, rather than merely asserting the field lemma.')
add(2, 'keep', 'authorial reference request',
    [(467,469)], [(415,476),(738,830)],
    'The instruction to supply the references ensuring closedness and first constructibility is explicit.')
add(3, 'keep', 'authorial requested generalization and proof/exposition step',
    [(855,863),(1078,1085)], [(693,735),(831,866),(1053,1102)],
    'The author explicitly asks for the generalization, corrects the quasi-finite hypothesis, and offers either doing the exercise or recording the omission in a remark.')
add(4, 'keep', 'authorial mathematical exposition request',
    [(1011,1015)], [(738,830),(868,1032)],
    'He says an explicit list must replace a reference to another fascicle; this is a real requested exposition step, not an unsolved Bertini theorem.',
    notes='Retain the distinction between an authorial request for a complete list and a new research problem.')
add(5, 'keep', 'cancelled authorial question',
    [(1036,1042)], [(1035,1052)],
    'The deleted passage explicitly says he has not read Seidenberg and wonders which hypothesis and argument are used.',
    notes='Preserve cancelled status; cancellation does not erase the historical question.')
add(6, 'reclassify_to_editorial_task', 'present-run consistency and hypothesis audit',
    [(1225,1249)], [(1108,1293)],
    'Proposition7.4, its induction, and the contrary nonprojective assertion in7.5 are stated affirmatively. Neither asks the currently formulated question. The inconsistency and missing projectivity motivate our verification task; an assertion that examples can be given is not an explicit unresolved request.',
    'Editorial task: diagnose the conflict between the proper-flat statement7.4 and the nonprojective warning7.5; identify valid hypotheses and a counterexample.')
add(7, 'keep_narrow', 'authorial marginal proposed extension',
    [(1251,1251)], [(1225,1293)],
    'The margin really records the possibility of avoiding a prescribed set. The word fini is uncertain in the transcription; retain that limitation and do not attach every later projection claim to this brief cue.',
    'Margin: “Possibilité d’éviter un ensemble [fini, uncertain] ...”. Develop the avoidance variant of the multisection construction.',
    confidence='medium', notes='The later prescribed-point projection exercise has its own explicit cue and belongs to MP-SA23-hyp-36.')
add(8, 'reclassify_to_editorial_task', 'present-run exposition and proof-check task',
    [(1406,1407),(1433,1440)], [(1382,1441)],
    'The author gives the proof and calls the write-up floppy, explaining that it used algebraically closed points. He does not ask that the codimension argument be proved or cleaned up. The register has converted an assessment of the prose into a request.',
    'Editorial task: make the geometric reduction in the written proof of8.4 explicit and check the transcribed codimension hypotheses.')
add(9, 'reclassify_to_editorial_task', 'present-run hypothesis and transcription audit',
    [(1448,1455),(1465,1488),(1490,1497)], [(1298,1379),(1442,1500)],
    'The same-S_k criterion is stated and then simplified and justified. The source does not pose the current “find and verify” question. Its instruction to state the criterion as a corollary is editorial, not uncertainty about the mathematical criterion.',
    'Editorial task: compare the inserted same-S_k wording, the counterexamples, and the proved criterion8.5–8.6; preserve uncertain symbols.')
add(10, 'keep_narrow', 'authorial deferred mechanical verification',
    [(1640,1647),(5788,5814)], [(1508,1726),(5706,5905)],
    'The source explicitly calls for the mechanical diagram verification and later for a more precise identity of ramification and polar degeneracy. Preserve the different formulation and hypotheses of these two witnesses.',
    'Verify the displayed conormal/differential comparison, and formulate the scheme-level ramification identity with the indicated conormal structures.',
    notes='The later signs and two specific conormal identifications also support MP54; consolidate only if the final index intentionally treats them as the same requested step.')
add(11, 'reclassify_to_editorial_task', 'present-run diagnosis of a withdrawn proof',
    [(1595,1605),(5749,5765)], [(1572,1726),(5747,5821)],
    'The first proof is cancelled and replaced; the other passage asserts an injectivity/smoothness conclusion. Neither asks for an explanation of the defect. The useful modern diagnosis is a reader task.',
    'Editorial task: explain why the withdrawn smooth-reduction argument and the injectivity inference require stronger hypotheses.')
add(12, 'keep_narrow', 'authorial requested strengthening and collected statement',
    [(1870,1890),(2413,2416),(2427,2429),(2473,2479)], [(1852,1930),(2386,2557)],
    'He explicitly says the general-pencil assertion should be stated more precisely, including the at-most-one singular point conclusion. The source cue supports a strengthened collected statement; separate any additional reader reconstruction of blow-up geometry.',
    'State the general-pencil conclusion more precisely, and collect it with the regular-base and blow-up description: a bad member has at most one ordinary singular point, under the hypotheses actually imposed in the surrounding theorem.')
add(13, 'keep', 'authorial deferred example construction',
    [(1913,1918)], [(1852,1930),(2270,2305),(6262,6370)],
    'He explicitly says positive-characteristic examples of inseparable duality should be given and that he has not constructed them.')
add(14, 'keep_narrow', 'authorial terminology replacement request',
    [(2112,2115)], [(1907,1918),(2083,2116)],
    'The actual unresolved step is to invent a better term after retracting réglée; the earlier terminology is already rejected on the pages.',
    'After retracting réglée, invent a more adequate word for the intended duality condition.',
    notes='This is an authorial terminology/exposition task, not an open geometrical theorem.')

add(15, 'keep', 'authorial explicitly doubted necessity claim',
    [(2038,2052)], [(1931,2061)],
    'The final parenthesis explicitly questions the R_k argument and suggests that S1 and equidimensionality may still be needed; this is more than a deleted necessity symbol.')
add(16, 'keep', 'authorial conjectural generalization',
    [(2083,2087)], [(2083,2116)],
    'Il est possible que explicitly marks the codimension-two assertion without normality or unramifiedness as tentative.',
    notes='The occurrence must start by2083, not2086, to include the conjectural cue and hypotheses.')
add(17, 'reclassify_to_editorial_task', 'present-run elaboration of a completed proof sketch',
    [(2167,2172)], [(2117,2179)],
    'The text proves the normal case and says the normalization argument is immediate and is not detailed. It does not ask for that argument, leave an uncertainty, or promise a later proof. The current request to prove8.18 is reader-generated.',
    'Editorial task: expand and check the stated reduction of8.18 to the normalization, preserving the dimensional edits.')
add(18, 'keep', 'authorial question answered on the same pages',
    [(2187,2195),(2207,2214)], [(2186,2264),(2306,2373)],
    'The words on se pose la question de savoir explicitly introduce a question about generic irreducibility with a fixed linear base. Its subsequent answer does not remove the historical question.',
    notes='Separate the actual question from our alarm about the asserted density away from the base and a missing fixed-divisor condition.')
add(19, 'keep_narrow', 'authorial deferred proof after correction',
    [(6326,6343)], [(2270,2305),(6262,6370)],
    'The initial universal separability assertion is not itself posed as a question, and the later text explicitly rejects it. The real remaining authorial step is the proposed proof of the ordinary-singularity conclusion that he says should remain correct.',
    'After retracting universal Veronese separability in odd-dimensional characteristic2, prove the remaining assertion by constructing a degree-n hypersurface with an ordinary quadratic singularity, for n≥2.',
    notes='Do not retain the already-retracted universal separability assertion as an unanswered question. The separate tentative inseparable degree is MP58.')
add(20, 'reclassify_to_editorial_task', 'present-run verification of a completed coordinate construction',
    [(2324,2334),(2345,2366),(2368,2375)], [(2306,2376)],
    'The low-degree point/tangent-jet construction is asserted and explicit P,Q,R choices are supplied. The source asks for a subsequent collected theorem, not for this proof to be supplied. That separate formulation request is already supported under MP12, while the unfinished fundamental-group cue is MP21.',
    'Editorial task: verify the explicit degree2/degree3 coordinate constructions and the exceptional planar case in9.3.')
add(21, 'keep_narrow', 'authorial unfinished proposed theorem and tentative topic',
    [(2368,2376)], [(2370,2385)],
    'The actual fragment requests a collected theorem and tentatively asks to mention a pi1 result. It is an unfinished authorial proposal; its exact mathematical conclusion cannot be recovered from these lines.',
    'In the unfinished collected theorem9.5, signal a result on [pi1, transcription uncertain]? No precise conclusion is supplied.',
    confidence='medium', notes='Keep fragment status and uncertainty. Do not turn it into a fully specified Lefschetz theorem or a present-run request to interpret a blank heading.')
add(22, 'keep', 'cancelled authorial explicitly unperformed exercise',
    [(2508,2522)], [(2386,2528),(3432,3554)],
    'The cancelled passage explicitly calls the higher-rank result an exercise not done in detail and says the collaborator should do it. Cancellation and the valid rank2 statement must remain distinct.')
add(23, 'reclassify_to_editorial_task', 'present-run representability and finiteness audit',
    [(2562,2574),(2592,2608)], [(2560,2716)],
    'The Grassmannian construction and charts are assertions with a proof sketch; no request to prove representability or decide surviving finiteness is made. Deleted wording and the chart scope motivate our editorial audit, not an authorial question.',
    'Editorial task: check the Grassmannian chart argument and its finiteness/splitting hypotheses without treating a deleted finite-type qualifier as a question.')
add(24, 'keep', 'authorial explicit deferred treatment',
    [(2639,2643)], [(2610,2716)],
    'The intrinsic characterization is explicitly said to be given in a later chapter and not needed here. This is a genuine deferred step even if its mathematical content is already indicated.',
    notes='Add scan63 and physical2639–2643 to the problem occurrence; the old2650 start misses the cue.')
add(25, 'keep', 'authorial explicit verification request',
    [(2845,2849),(2860,2862)], [(2720,2888)],
    'The parenthesis explicitly says that independence of the local basis must be checked. Preserve the local regular-sequence convention rather than adding a new global claim.')
add(26, 'keep', 'authorial optional exercises and requested generalization',
    [(2883,2887),(2902,2916),(2987,3000)], [(2879,3004)],
    'He explicitly leaves the arbitrary-m statements as exercises, authorizes omission, and offers a more precise contact statement on request. These are source requests even though the author doubts their immediate usefulness.')
add(27, 'keep', 'authorial tentative assertion and proposed verification',
    [(2940,2953),(2954,2959)], [(2918,3004)],
    'Several sauf erreur clauses and the explicit description of the study needed for verification supply a real authorial open step, beyond the general absence of a proof.')
add(28, 'keep', 'authorial explicit remaining lemma',
    [(3034,3045)], [(3005,3054)],
    'The source says that a further Grassmannian intersection lemma remains to be proved and spells it out. This supports the question as stated, including its tentative hypothesis wording.')
add(29, 'keep_narrow', 'authorial requested general proof exposition',
    [(3152,3154),(3209,3218),(3253,3257),(3270,3272)], [(3058,3272)],
    'Admettons ce lemme followed by Reste à prouver and a completed proof is ordinary proof organization, not by itself a request to prove13.3. There is, however, an explicit request to write the general independent-hyperplane induction once so it can be cited. Narrow the record to that real request, retaining the lemma as its application.',
    'Write out once, in general, the induction using independent generic hyperplanes that is used to pass to linear sections of arbitrary codimension in13.3 and2.6.',
    notes='The reason for narrowing is the absence of a question/deferment cue for the whole lemma, not the fact that a genuine question could have been answered later. Genuine questions and explicit promised/deferred steps remain historical records after a subsequent answer.')
add(30, 'keep', 'authorial conjectural removal of a hypothesis',
    [(3294,3302)], [(3208,3302)],
    'The author says that the infinite-field hypothesis is plausibly unnecessary and that no finite-field argument has been attempted. This is a clear authorial question.')
add(31, 'reclassify_to_editorial_task', 'present-run verification of an asserted variant',
    [(3334,3348)], [(3334,3348)],
    'The finite affine-set variant is asserted and proved by adapting13.3. Its optional inclusion in the theorem is an editorial placement suggestion, not a request to establish the variant.',
    'Editorial task: check the finite-set variant and its nonrational-conjugate and affine-neighborhood hypotheses.')
add(32, 'reclassify_to_editorial_task', 'present-run verification of an asserted definition variant',
    [(3304,3309)], [(3270,3314)],
    'The author affirmatively says the weakened conclusion follows from the proof already given. He does not ask whether geometric irreducibility can be dropped.',
    'Editorial task: document the altered definition and verify the claimed disconnected-fiber variant.')
add(33, 'reclassify_to_editorial_task', 'present-run hypothesis audit of an unproved assertion',
    [(3312,3313),(3323,3332)], [(3312,3332)],
    'Sans démonstration announces an asserted variant, with no request, conjecture, or promise of a later proof. The missing residue-field hypotheses are our finding; missing proof alone is not a source question.',
    'Editorial task: determine the valid hypotheses and proof of the asserted relative elementary-neighborhood variant.')
add(34, 'reclassify_to_editorial_task', 'present-run verification of source assertions',
    [(3362,3369)], [(3340,3427)],
    'The K(pi,1), group-extension, and universal-cover claims are asserted affirmatively. No question, deferred proof, or request to show them occurs in this passage.',
    'Editorial task: check the topological claims about complex poly-elementary neighborhoods and distinguish their separate strengths.')

add(35, 'keep_narrow', 'authorial question answered by the subsequent proposition',
    [(3513,3515),(3566,3570)], [(3480,3586)],
    'The source explicitly says that the question of fiber dimension and flatness arises, then offers14.1–14.3. Preserve that question even though an answer is supplied. The modern generic-versus-all-fibers defect is our diagnosis, not the question’s literal wording.',
    'What are the dimensions of the fibers of the generic conical projection, and when is that projection flat? Also formulate the indicated Cohen–Macaulay module variant.',
    notes='The problem occurrence should include3513–3515, before the old3516 start.')
add(36, 'keep', 'authorial expressly delegated proof',
    [(3602,3613),(3623,3627)], [(3588,3629)],
    'The proof of the indicated projection properties is expressly left to Dieudonné; this is a genuine authorial step.')
add(37, 'keep', 'authorial unresolved question and requested investigation',
    [(3709,3718),(3843,3844)], [(3690,3854)],
    'He explicitly has not clarified the global Bertini extension, has written to Serre and Zariski, and asks for independent investigation if they cannot settle it.')
add(38, 'keep', 'authorial recommended generalization',
    [(3846,3854)], [(3690,3854)],
    'The text explicitly recommends developing the exceptional/contact results in the axiomatic setting and offers to return to the difficulties.')
add(39, 'reclassify_to_editorial_task', 'present-run bibliographic verification of a cited standard lemma',
    [(4033,4036)], [(4004,4080)],
    'The lemma is invoked as standard, with a tentative suggestion that it is in Bourbaki. There is no explicit request to find or prove it, and no doubt about its mathematical truth. A source lookup is useful, but the current imperative is ours.',
    'Editorial task: identify the standard graded rank-one lemma and verify the tentative Bourbaki attribution.',
    confidence='medium', notes='Retain the archival bibliographic uncertainty as a reading/reference alarm; reclassification does not erase the words sans doute.')
add(40, 'keep', 'authorial marginal proof request',
    [(4217,4225)], [(4086,4230)],
    'The margin says le faire! and specifies the determinant-open construction. This converts an otherwise routine asserted deduction into an explicit requested step.')
add(41, 'reclassify_to_editorial_task', 'present-run elaboration of an asserted deduction',
    [(4329,4345),(4365,4379)], [(4314,4390)],
    'On peut déduire asserts that multiprojective morphisms and automorphisms follow by the same method. The divisor statements are also supplied. There is no request or promised later proof corresponding to the current imperative.',
    'Editorial task: spell out the multiprojective automorphism deduction and verify the divisor formulas and omitted base twist.')
add(42, 'reclassify_to_editorial_task', 'present-run verification of a completed representability argument',
    [(4398,4405),(4447,4470)], [(4396,4474)],
    'The text announces the object to determine, states the representability theorem, and finishes the proof via openness and noetherian reduction. It neither leaves that step unresolved nor asks the collaborator to prove it. Nous nous proposons introduces the exposition, rather than an open/deferred problem.',
    'Editorial task: verify the completed fixed-line-bundle divisor representability proof and its cohomology/base-change assumptions.')
add(43, 'reclassify_to_editorial_task', 'present-run verification of the transposition construction',
    [(4503,4509),(4525,4551),(4567,4583),(4599,4603)], [(4479,4629)],
    'The fixed-point closedness, Cartier transposition, maximal open, and associated-point obstruction are stated and argued. The deleted promise in4493–4501 concerns representability of a divisor functor, not proving these transposition assertions. It does not support the current problem wording.',
    'Editorial task: verify the fixed-point and broad fixed-point loci, their closedness hypotheses, and the maximal Cartier-transposition open.',
    notes='A separate explicit deleted deferred claim about Div for projective X appears at4493–4501; it is flagged in additional_authorial_cues rather than silently repurposed as a transposition question.')
add(44, 'keep_narrow', 'authorial requested rewrite and extraction of a corollary',
    [(4826,4826),(4840,4845)], [(4673,4914)],
    'The main uniqueness/extension proof is written and ends in cqfd. The real outstanding authorial task is explicit: rewrite its end as one necessary-and-sufficient argument and first isolate the corollary; a difficult marginal explanation request is also present but uncertain.',
    'Rewrite the end of the extension proof in terms of necessary and sufficient conditions, and first extract the stated corollary on locally free sheaves and relative Cartier divisors.',
    notes='Keep the actual exposition request; do not describe all Hartogs uniqueness and extension claims as unproved authorial questions. Preserve uncertainty in the margin at4826.')

add(45, 'reclassify_to_editorial_task', 'present-run reading alarm about an uncertain assertion',
    [(5053,5053),(5082,5082)], [(4999,5083)],
    'The uncertain marginal transcription affirmatively says that the property is not preserved by base change; it does not ask whether it is. The apparent contradiction and uncertain wording call for a reading check, not an attributed authorial question.',
    'Editorial task: resolve the transcribed marginal negation and its relation to the fiberwise completeness criterion without silently repairing the text.',
    notes='Preserve the full unsure markup. A question generated by uncertainty in transcription is distinct from an authorial question.')
add(46, 'reclassify_to_editorial_task', 'present-run analysis of an authorial correction',
    [(5054,5067),(5076,5098),(5100,5108)], [(5041,5200)],
    'The faithful-flatness claim is asserted, then withdrawn and replaced with a stronger hypothesis and an explicit counterexample. No question is posed. Historical correction is a claim-status event; it does not by itself create a Stage3 problem.',
    'Editorial task: document the withdrawn monomorphism assertion, corrected hypotheses, and authorial counterexample.')
add(47, 'keep_narrow', 'authorial explicitly deferred general formalism',
    [(5184,5194),(5225,5234),(5258,5264)], [(5168,5279)],
    'The source expressly places the general criterion in a future chapter and the tangent-deviation formalism in later sections, and says this part cannot reasonably be written without those calculations. This is a genuine deferred dependency; the special-case proof is already sketched.',
    'Supply the promised general functorial monomorphism/tangent-deviation formalism and the cross-reference to its later treatment, so the sketched infinitesimal argument can be written without circularity.')
add(48, 'keep_narrow', 'authorial explicit deferred descent treatment',
    [(5290,5296)], [(5284,5320)],
    'Descent is explicitly deferred to the later descent machinery, and admitting twisted projective parameter spaces is promised for the next number. The text already states the need for twists; it does not ask us to decide whether an ordinary projective bundle always survives.',
    'Develop the indicated faithfully flat descent of linear systems, admitting twisted projective parameter spaces in the promised subsequent treatment.')
add(49, 'keep_narrow', 'authorial explicitly designated optional exercise',
    [(5302,5307),(5336,5339)], [(5284,5355)],
    'The proof is explicitly called an exercise and withheld unless the collaborator requests it. Retain it as an optional authorial exercise, not a currently open theorem or a request to invent new field hypotheses.',
    'Give the optional exercise proof of Proposition4.4a using4.1, under the hypotheses displayed on the page.',
    notes='Sauf réclamation is a conditional offer to supply a proof, not an unconditional demand that the collaborator do it.')
add(50, 'keep_narrow', 'authorial optional exercise and requested reformulation',
    [(5336,5348)], [(5308,5355)],
    'The optional exercise is real, and the author explicitly asks for a formulation of b) without the supplementary hypotheses by imposing the condition after algebraic closure. The statement that counterexamples are easy to give is not a separate request for examples.',
    'Prove the indicated optional b)/c) exercise and formulate b) without supplementary hypotheses on k or X by expressing the condition on E after algebraic closure; record the geometric-integrality simplification.')
add(51, 'reclassify_to_editorial_task', 'present-run verification of a cancelled proof instruction',
    [(5415,5421)], [(5360,5428)],
    'The cancelled passage supplies the constructibility/limit argument affirmatively and calls it the usual argument. It does not leave a step unresolved or ask for a proof. Its cancellation creates a historical status question for the reader, not an authorial mathematical question.',
    'Editorial task: verify and annotate the cancelled eventual-good-locus argument and its constructibility assumptions.')
add(52, 'reclassify_to_editorial_task', 'present-run interpretation of an unidentifiable mathematical fragment',
    [(5447,5454)], [(5433,5458)],
    'The transcribed formula has no identifiable question or specified deferred step. A deleted fragment begins with an uncertain Donner une, but the object is illegible; it cannot support the current request to interpret the Hodge formula.',
    'Editorial task: identify the upside-down Hodge/filtration fragment from better source evidence before assigning a precise mathematical statement or question.',
    notes='Keep C-SA23-hyp-077 as an unidentifiable mathematical fragment. Do not treat the uncertain deleted instruction as a confidently recovered authorial question.')
add(53, 'keep_narrow', 'authorial terminology question and proposed additional definition',
    [(6306,6323)], [(5520,5701),(6266,6347)],
    'The modern task to reconcile definitions is ours. The source nevertheless asks for the collaborator’s opinion about ordinary versus elementary terminology and extension to arbitrary multiplicity, then explicitly proposes adding the ultra-singular subscheme using the corrected discriminant. Narrow the problem to those real steps.',
    'Should ordinary be replaced by elementary and extended to singularities of arbitrary multiplicity? Also introduce, at least in a remark, the ultra-singular subscheme defined with the corrected discriminant.',
    notes='The explicit correction is on scans158–160. Scans140–141 supply the earlier live/cancelled definitions, not the later correction.')
add(54, 'keep', 'authorial undetermined sign and requested explicit comparison',
    [(5847,5855),(5873,5895)], [(5706,5905),(6153,6250)],
    'The sign is expressly left to be determined and the source asks for a collected formulation with an invertible coefficient module. These are genuine outstanding local identifications/exposition steps.',
    notes='Avoid describing all conormal or ramification assertions as open merely because they have short proofs. MP10 and MP57 retain their distinct explicit comparison cues.')
add(55, 'keep_narrow', 'cancelled authorial proof delegation followed by a proof sketch',
    [(5989,6015),(6427,6427)], [(5947,6150),(6427,6429)],
    'The delegation je te laisse le soin de démontrer is explicit but deleted; a field-reduction proof follows. Preserve this historical requested exercise as subsequently sketched, and the explicit higher-degree formulation instruction. The binomial-index correction is our check, not an authorial question.',
    'Prove the multiplication/Hilbert-rank lemma as requested in the deleted delegation, and formulate its stated degree-n variant.',
    notes='The general degree-n command at6427 also occurs in the broader MP59; it is a shared clause, not two independent authorial questions.')
add(56, 'keep_narrow', 'authorial choice of generality and terminology',
    [(5950,5964),(6043,6050)], [(5947,6110),(6375,6490)],
    'He explicitly leaves the choice of starting in the general m-generator setting to the collaborator and asks regular versus quasi-regular terminology. The rank-one-relation criterion itself is asserted and called nearly trivial, not separately left as a question. Its degree-n variant is an explicit command under MP59.',
    'Decide whether to begin with the general augmented-algebra/m-generator setting, and choose regular versus quasi-regular terminology consistently with§19.',
    notes='Remove the present-run imperative to prove all of Proposition9 from the source-question wording; keep its claim/proof assessment in Stage2.')
add(58, 'keep', 'authorial expressly unguaranteed conjecture',
    [(6344,6347)], [(6262,6370)],
    'The author says he believes the inseparable degree is exactly2 but gives no guarantee. Preserve the surrounding Veronese/immersion context rather than interpreting it as a universal statement about every conormal map.')
add(59, 'keep', 'authorial explicit generalization and definition tasks',
    [(6427,6436),(6471,6478)], [(6338,6490)],
    'The source explicitly commands the degree-n variants of the previous propositions and the introduction of the corresponding geometric definitions.',
    notes='The Hilbert-rank part shares6427 with MP55. The full higher-degree program additionally includes the presentation criterion and geometric variants; do not count that shared clause as a second independent request.')
add(60, 'keep_narrow', 'authorial explicitly promised later proof',
    [(6460,6469)], [(5871,5942),(6375,6526)],
    'Nous montrerons au par.20 expressly promises a blow-up proof of isolation. Cohen–Macaulayness is already deduced immediately before it, and normality/reducedness are stated as consequences. This is an actual deferred step, not merely an unproved assertion.',
    'Give the promised§20 blow-up proof that the closed point is the only singular point of an elementary local ring, with the stated normality/reducedness consequences.',
    notes='The distinct earlier placement question Où le mettre? at5918–5919 is editorial and can be associated with MP68. Do not silently replace the intrinsic dimension threshold by an ambient one.')
add(61, 'keep', 'authorial tentative removal of a hypothesis',
    [(6501,6506)], [(6454,6526)],
    'The aside sans doute finie est inutile expressly leaves the removal of finiteness tentative and requests insertion of the comparison as a corollary or proposition.')
add(62, 'keep', 'authorial explicitly unverified conjecture',
    [(6704,6706),(6717,6725)], [(6658,6807)],
    'He explicitly says that the invariance has not really been verified and is only conjectural, then identifies the factorization and independence he wants checked. This is the clearest possible authorial open-step cue.')
add(63, 'keep', 'authorial proposed extension with explicitly uncertain hypothesis',
    [(6827,6844)], [(6773,6847)],
    'He asks for the theory to be written in the smooth-pair setting and says that only a detailed write-up will reveal whether an étale hypothesis is needed. He also offers joint work and promises further notes.')
add(64, 'reclassify_to_editorial_task', 'present-run verification of asserted functoriality and formula',
    [(6964,6975),(6990,7000),(7006,7016)], [(6940,7041)],
    'Functoriality and base-change compatibility are stated in Proposition16.6; the note explains their proper order of exposition. The direct-sum law is asserted and called trivial. None is posed as an unresolved question or requested proof. The coefficient error and verification task are ours.',
    'Editorial task: verify the functorial construction over two-torsion bases and correct the direct-sum coefficient in a separately labelled refinement.')
add(65, 'keep_narrow', 'authorial marginal request to extract a general lemma',
    [(7132,7148)], [(7047,7162),(7218,7254)],
    'The orbit-flatness proof and torsor argument are supplied; their mere proof structure does not support the present request to prove them. A margin at7141 does, however, ask to extract a lemma on morphisms of homogeneous spaces. Retain only that actual proposed step.',
    'Extract a general lemma about morphisms of homogeneous spaces from the generic-flatness/transitivity argument used to prove16.11.',
    confidence='medium', notes='The marginal cue is inside unsure markup. Preserve that uncertainty and do not present the whole torsor equivalence as an authorial open question.')
add(68, 'keep', 'authorial editorial and authorship questions; not a mathematical research problem',
    [(85,92),(105,118),(5366,5373),(5395,5398),(5409,5413)], [(43,129),(5355,5413)],
    'The requests for a new plan, placement suggestions, section titles, and reconsideration of joint authorship are explicit. Keep them as authorial editorial questions, separately typed so that they do not inflate the count of mathematical open problems.',
    notes='Additional actual placement questions occur at5918–5919 and6794–6803; they belong to this editorial family, not to invented proof problems.')

# Priority cases checked at the beginning of the audit.
add(57, 'keep_narrow', 'authorial explicitly unverified scheme-level identification',
    [(6233,6239),(6241,6245)], [(6153,6250),(6581,6583)],
    'Lines6233–6239 explicitly say the ramification identity has not been checked in detail. The following rank-stratum dimension bound is simply asserted; its verification/repair is a separate present-run task and must not be included as an authorial question.',
    'Verify and make precise the identity between V² and the locus where V¹→Y is ramified, including the intended scheme structures.',
    notes='Claim090’s later i.e. correction targets the earlier wording at6162–6174, not automatically the distinct exterior-power lemma at6201–6207. Do not invent an additional open question from that correction.')
add(66, 'reclassify_to_editorial_task', 'present-run source lookup and verification',
    [(7263,7275),(7277,7280),(7292,7300)], [(7218,7304)],
    'The text asserts the finite étale cover result, cites SGADXXIV, and supplies the exceptional odd-rank characteristic2 mechanism and a rank-one counterexample. No cover-specific question is present. The question about what is known and terminology belongs to MP67 and concerns the corrected discriminant, not a second cover question.',
    'Editorial task: verify the cited SGADXXIV finite-cover theorem and document the stated odd-rank characteristic2 finite-flat exception.',
    notes='Affected original claims: C-SA23-hyp-104 and C-SA23-hyp-105. Retain their source assertions; remove only the false attribution of an open cover question.')
add(67, 'keep', 'authorial priority and terminology question',
    [(7193,7199),(7210,7216)], [(7167,7304)],
    'Both passages explicitly ask what is already known, whom to credit, and which discriminant terminology to use. This is the real question near the cover discussion.',
    notes='Do not duplicate this question under MP66 or describe it as a request for a cover theorem.')


if __name__ == '__main__':
    decisions.sort(key=lambda r: r['original_id'])
    assert len(decisions) == len({r['original_id'] for r in decisions})
    done = {int(r['original_id'].rsplit('-', 1)[1]) for r in decisions}
    payload = {
        'audit_date': '2026-11-19',
        'auditor': 'GPT-6 Astra Pro; owner bt; SA23-20261119',
        'scope': 'Manual question-origin audit of all68 hyperplanes problem records. No source or owner register is modified.',
        'method': 'Each decision is manually assigned from actual manuscript wording. The program copies only manually selected literal line ranges and original register metadata. An unproved assertion, a completed proof sketch, a correction, or an incomplete fragment alone is not treated as an authorial question.',
        'source': str(SOURCE.relative_to(ROOT)),
        'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'input_problems_sha256': hashlib.sha256(PROBLEMS.read_bytes()).hexdigest(),
        'completion': 'complete' if len(decisions) == 68 else 'incremental',
        'audited_count': len(decisions),
        'total_input_count': len(original),
        'current_owner_file_record_count': len(input_records),
        'pending_original_ids': [original[n]['id'] for n in sorted(original) if n not in done],
        'decision_counts': dict(collections.Counter(r['decision'] for r in decisions)),
        'additional_authorial_cues': [
            {
                'id': 'hyp-origin-extra-veronese',
                'source_cues': [excerpt(3283,3292)],
                'origin': 'authorial explicitly proposed question',
                'scope': 'Whether the obstruction to smooth generic sections through a positive-dimensional fixed linear subspace can persist after Veronese degree n≥2.',
                'handling': 'Root acknowledged and reserved SA23-608, C-SA23-hyp-108/108R and MP-SA23-hyp-69; root is supplying the checked counterexample and exact literature fate. No independent claim is created by this audit.',
                'distinction': 'Smoothness of a generic section with positive-dimensional fixed linear base differs from MP18 irreducibility and the already-proved point/tangent-jet construction formerly attributed to MP20.'
            },
            {
                'id': 'hyp-origin-extra-divisor-functor',
                'source_cues': [excerpt(4492,4501)],
                'origin': 'cancelled authorial explicit deferred treatment',
                'scope': 'Nous verrons au Chap V promises representability of Div for projective X; the following text separately discusses the easier projective-bundle case and its possible placement.',
                'handling': 'Check whether this explicit future-chapter promise already has a canonical problem in the Divisor/Hilbert material. It is not the maximal-transposition-open question currently attributed to MP43, and the general projective-X promise must not be silently identified with the fixed-L proof under MP42.',
                'confidence': 'high'
            }
        ],
        'decisions': decisions,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: payload[k] for k in ['completion','audited_count','decision_counts','pending_original_ids']}, ensure_ascii=False))
