"""Final manual distinction between author questions and editorial checks.

These decisions follow rereading the cited passages. An unproved assertion,
ordinary cancellation, or our need for a counterexample is not an author question.
"""
import copy
remove_reasons={
 4:'File 161-1:355 asserts the converse and deletes some coherence data. It contains no question or deferred proof request; the missing-coherence test is ours.',
 7:'File 161-1:621–636 asserts comparison isomorphisms and gives unexplained group symbols. Absence of definitions or proof is our identification problem, not an authorial question.',
 12:'File 161-2-01:520–524 states the localization and representable-inclusion characterization as a consequence. No authorial question is present.',
 32:'File 161-2-04:122–132 asserts evaluation invertibility and gives a canceled proof ending in monogenicity. Our correction of that conclusion is editorial. The actual surrounding property questions remain in problems 28–29.',
 34:'File 161-2-04:180–184 is headed Th. and asserts both the limit and colimit conclusions. It does not query the bicolimit assertion.',
 35:'File 161-2-04:171–179 and 219–263 assert changing representability and generator criteria. A truncated parenthetical margin does not establish the broad question previously formulated here.',
 40:'File 161-2-05:1–77 asserts the pointwise-model facts; file 07:415 supplies a later hypothesis correction. This is a correction history, not an authorial question.',
 47:'File 161-2-06:41 asserts the essential-point criterion. The actual universe warning at45 is retained as an occurrence of problem48; it does not make the criterion itself a question.',
 55:'File 161-2-06:408–419 asserts the pseudofield characterization and explicitly says the converse is true and known. The distinct actual field-definition question at421 is retained under problem57.',
 62:'File 161-2-07:613–618 corrects bijection to application, and646–659 proves the representable case. A correction and a proof are not an open question.',
 68:'File 161-2-02:174 asserts that the model category can be empty without a degenerate classifier. It is not phrased as a question; the pointless example is our explanatory verification.',
}
editorial=[];redirects={};origin_audit=[]
for p in list(problems):
    n=int(p['id'].rsplit('-',1)[1])
    if n in remove_reasons:
        e=copy.deepcopy(p);e['original_id']=e['id'];e['id']=e['id'].replace('MP-','ED-',1)
        e.update(origin='present-run editorial task',record_type='editorial task',source_cue=remove_reasons[n],cue_or_reason=remove_reasons[n])
        for o in e['occurrences']:o['drafting_status']='source assertion/correction or fragment; no authorial question at this endpoint'
        editorial.append(e);redirects[p['id']]=e['id'];problems.remove(p)
        origin_audit.append(dict(original_id=p['id'],destination=e['id'],decision='editorial task',reason=remove_reasons[n]))

by_problem={int(p['id'].rsplit('-',1)[1]):p for p in problems}
by_problem[16].update(as_he_states='The explicit Question at file02:280 asks for classifying topoi and subtopoi of the displayed arrow, endomorphism, point, and operation structures. The earlier B_G heading is contextual, not itself a question.',origin_cue='file02:280–288, Question Topos classifiant et sous-topos pour la structure')
by_problem[26].update(title='The zero-object convention in characteristic gluing',as_he_states='The characteristic gluing is accepted OK, but the common zero object is annotated (initial ?). The ensuing enough-points assertion is a conclusion, not an additional author question.',plausible_today='The empty affine is initial in the affine scheme category and corresponds to the terminal zero ring. The separate gluing and enough-points assertions have the precise scope of C055.',worth='Commentary work only: the initial-versus-terminal convention answers the explicit doubt and avoids enlarging the accepted gluing result into an invented open problem.',origin_cue='file03:817, (initial ?); file03:819, Donc OK')
by_problem[33].update(as_he_states='Clarify the ordinal filtration and the appropriate accessibility/Ind hypotheses; the page explicitly says Préciser and questions the ambient colimit assumption. The all-sufficiently-large-ranks assertion is an asserted consequence checked separately.',origin_cue='file04:137, stable par petites colimites ?; file04:150, Préciser la filtration ordinale; file04:202 competing modifié/vérifier reading')
by_problem[45].update(title='Adjoint existence in the model-category dictionary',as_he_states='The model-functor row asks whether preservation of the indicated limits gives a left adjoint: donc (?), ayant un adjoint à g. The finite-presentability condition itself is asserted and corrected, not posed as a question.',plausible_today='Between the specified locally finitely presentable model categories, an accessible limit-preserving functor is a right adjoint. Its left adjoint preserves finite presentables exactly when the right adjoint preserves filtered colimits.',state_of_art='C067 supplies the solution-set and adjoint criterion with its hypotheses; C084 proves the finite-presentability comparison and records the authorial correction. Riehl4.7.10 and Lack–Power8 provide the checked modern setting.',refs=['RiehlContextOnline','LackPower2009'],origin_cue='file06:379, donc (?), ayant un adjoint à g.')
by_problem[48]['occurrences'].append(occurrence(6,[81],'41–45','explicit warning of leaving the universe for topoi and essential topoi'))
by_problem[53].update(title='How faithful is the finitely-presentable nerve?',as_he_states='For the nerve defined by the finitely presentable objects, the source asks whether conservativity can be strengthened to full faithfulness or faithfulness. The finite-projective-limit envelope in the next assertion is not itself posed as a question.',plausible_today='For the locally finitely presentable model category of the specified finitary limit theory, the finitely presentable subcategory is dense, so its nerve is fully faithful. Its generally valid closure is under finite colimits and retracts, not finite limits.',state_of_art='Kelly’s density criterion and the locally finitely presentable model theorem settle the nerve question. C093 gives the square-zero-ring counterexample to the separate asserted finite-limit closure.',refs=['Kelly1982','MakkaiPitts1987','LackPower2009'],origin_cue='file06:328–333, conservatif [ou pleinement fidèle ? ou fidèle]')
by_problem[57]['occurrences'].insert(0,occurrence(6,[93],'421–428','explicit question whether fields are definable by limits and colimits under suitable exactness conditions'))
by_problem[67].update(as_he_states='The ring lattice asks about finiteness of the idempotent object and queries regularity, CM, Gorenstein and complete-intersection conditions before annotating non. The noetherian line is an asserted negative answer, retained as context.',origin_cue='file03:48, fini ?; file03:125–128, regularity/CM/Gor/complete-intersection question marks followed by non')

# The actual enough-points question must not be replaced by our check of D_n.
old22=copy.deepcopy(by_problem[22]);old22.update(id='ED-SA23-groupes-22',source_problem_id='MP-SA23-groupes-22',component_scope='Only the D_n and reflection verification formulation; the enough-points question remains MP22.',origin='present-run editorial task',record_type='editorial task',source_cue='The D_n calculation and reflection assertions are not questions. The actual authorial question at483 is retained in the corrected MP22.',cue_or_reason='Reclassified only the invented proof-verification formulation; the genuine enough-points question retains MP22.')
editorial.append(old22)
by_problem[22].update(title='Enough points for the zero-dimensional ring classifier',occurrences=[occurrence(3,[43],'478–483','explicit enough-points question; topology annotated noncoherent')],as_he_states='After the countable D_n covering condition, the margin asks whether this topology has enough points.',plausible_today='Yes for the ring site over Z used here: a countable finite-limit skeleton and countably many generating covering families make its sheaf topos separable.',state_of_art='Makkai–Reyes, First Order Categorical Logic, Theorem6.2.4, proves that every separable Grothendieck topos has enough points. Its precise definition and proof were opened in the author-hosted corrected retyping, printed p125. C115 verifies the countability hypotheses for the displayed ring site and separates this conclusion from coherence.',worth='Commentary work only: checking countability and applying the exact separable-topos theorem answers the explicit question; no new enough-points theorem is needed.',refs=['MakkaiReyes1977'],origin_cue='file03:483, A-t-elle assez de pts ??')

# Only the nested topology question is an authorial question in the detached material.
old69=copy.deepcopy(by_problem[69]);old69.update(id='ED-SA23-groupes-69',source_problem_id='MP-SA23-groupes-69',component_scope='Only identification of the cohomology and n-model fragments; the nested P1,P2 question remains MP69.',origin='present-run editorial task',record_type='editorial task',source_cue='The cohomology and n-model fragments have uncertain notation but no identified authorial question. Their identification is editorial; the explicit nested P1,P2 question remains MP69.',cue_or_reason='Partial separation, not a whole-problem redirect.')
old69['occurrences']=old69['occurrences'][:1]+[occurrence(3,[38],'206–224;232–244','unidentified fragment, not an established author question')]
editorial.append(old69)
by_problem[69].update(title='The unidentified nested ring-topology question',occurrences=[occurrence(3,[38],'226–230','explicit question mark beneath the nested P1,P2 display')],as_he_states='The nested display X_anneaute contains P1 contains P2 with a question-mark brace. The meaning of the intermediate objects is not supplied.',origin_cue='file03:228, the explicit question-mark brace under the nested P1,P2 display')

# Correct page statuses affected by the same literal source audit.
for c in claims:
    n=int(c['id'].rsplit('-',1)[1])
    if n in [29,67,73]:
        c['status_category']='stated without proof'
        c['status_on_pages']={29:'stated without proof; the representable-inclusion characterization is asserted, not queried',67:'stated without proof; the generator and exactness hypotheses are revised between assertions',73:'stated without proof; both parts are announced as a theorem, including the bicolimit assertion'}[n]
    if n==105:
        c['lines'].append(f'{source_file(7)}:645–660')
        c['status_on_pages']='corrected by himself: bijection deleted at614; the representable case is proved on the next sheet at646–659'
    c['reconstruction_boundary']=c['reconstruction_boundary'].replace('a short quotation or explicitly labeled paraphrase','a literal transcription excerpt; source_paraphrase separately holds the English gloss')

# An additional exact source question discovered in the origin-cue correction.
cid=addclaim(115,911,3,[43],'478–483',
 'A-t-elle assez de pts ??',
 'The zero-dimensional commutative-ring classifier on the stated finite-type affine Z-site has enough points. Its displayed countable covering family D_n has no finite subcover; this fact alone is not a Morita-invariant noncoherence theorem.',
 'open on the pages',
 'There are countably many finite presentations over Z and countably many maps between any two such rings, so choose a countable skeleton of the finite-type affine site; it has finite limits. The D_n family over the generic element is countable, and its pullbacks along the countably many site arrows generate a countable coverage. Makkai–Reyes6.2.4 therefore supplies enough points. No finite subfamily covers: for maximal exponent N, the element t in F_2[t]/(t^(N+1)) has neither a unit component nor t^n=0 for n≤N. This is a general nilpotence-order argument, not a finite-sample inference.',
 'Makkai–Reyes, First Order Categorical Logic (1977), Theorem6.2.4, proves enough points for separable topoi. The opened 2018 corrected retyping states the countable-category/countable-basic-cover hypothesis and gives the proof on printed p125. The original book metadata and retyping provenance were separately opened; no earlier circulation date is asserted.',
 ['MakkaiReyes1977'],'B',event='targeted proof check')
c=claims[-1]
c.update(status_category='open on the pages',status_assignment='Manual: explicit question marks at physical483.',record_origin='source question',source_paraphrase='Does the topology have enough points?',reconstruction_boundary='The enough-points question and countable D_n cover are on the page. Countability of the site and application of Makkai–Reyes are the present reconstruction.')
raw=(BASE.parents[2]/source_file(3)).read_text().splitlines()[482]
quote='A-t-elle assez de pts ??';assert quote in raw
c['his_statement']=quote;c['source_quotations']=[dict(file=source_file(3),physical_lines='483',literal_excerpt=quote)]
c['quotation_note']='Literal question inside the margin; transcription unchanged.'
c['computation']['proof_certificate']='SA23_work/parts/groupes/computations/proof_certificates.md#c-sa23-groupes-115'
qa=json.loads((BASE/'quotation_audit.json').read_text());qa.append(dict(id=cid,source_file=source_file(3),selected_lines=[(483,483)],literal_fragments=[quote]));(BASE/'quotation_audit.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2)+'\n')
bibliography.append('''@book{MakkaiReyes1977,
 author={Michael Makkai and Gonzalo E. Reyes},
 title={First Order Categorical Logic: Model-Theoretical Methods in the Theory of Topoi and Related Categories},
 series={Lecture Notes in Mathematics},
 volume={611},
 publisher={Springer-Verlag},
 address={Berlin},
 year={1977},
 url={https://reyes-reyes.com/wp-content/uploads/2018/04/makkai-reyes-book.pdf},
 urldate={2026-11-19},
 annote={Opened author-hosted corrected retyping by Francisco Marmolejo, posted 2018; Theorem 6.2.4 and proof, printed p.125. Original 1977 metadata and the retyping provenance also opened.},
 note={verified}
}
''')
search('separable topos enough points countable site theorem Makkai Reyes; zero dimensional rings classifying topos enough points; author-site verification of First Order Categorical Logic 6.2.4',[115],
 [dict(url='https://reyes-reyes.com/wp-content/uploads/2018/04/makkai-reyes-book.pdf',locators='Definition before Theorem6.2.4 and complete proof, printed p125/PDF133, tool lines10040–10098',match='Countable category with finite limits and countable system of basic covers; its sheaf topos has enough points.'),dict(url='https://reyes-reyes.com/1977/06/01/first-order-categorical-logic/',locators='author bibliography',match='1977, LNM611, Springer'),dict(url='https://reyes-reyes.com/2018/04/02/first-order-categorical-logic-2/',locators='description of linked PDF',match='Corrected retyping by Francisco Marmolejo, posted2018')],
 limits='The D_n family has no finite subcover, but that does not alone establish that the topos has no alternative coherent presentation. No manuscript date or priority is inferred.',engine='system2 then system1 verification; opened exact author-hosted book theorem and proof')
checked_ref('MakkaiReyes1977','Read the definition of separable site, Theorem6.2.4, and the complete countable-completeness proof; verify the ring site has the exact countability and finite-limit hypotheses.','targeted proof check')

for p in problems:
    p.setdefault('origin','authorial question, doubt, deferred step, or unfinished programme')
    p.setdefault('record_type','authorial problem')
    p.setdefault('origin_cue','The recorded occurrence contains the authorial question/deferred step described in as_he_states; cancellation and uncertainty remain in the source record.')
    origin_audit.append(dict(original_id=p['id'],destination=p['id'],decision='retained authorial problem',reason=p['origin_cue']))
for row in links:
    for j in range(len(row)):
        for old,new in redirects.items():row[j]=row[j].replace(old,new)
for e in editorial:
    e.setdefault('editorial_formulation',e['as_he_states'])
    e['as_he_states']=e['source_cue']
(BASE/'editorial_tasks.json').write_text(json.dumps(editorial,ensure_ascii=False,indent=2)+'\n')
(BASE/'problem_origin_audit.json').write_text(json.dumps(origin_audit,ensure_ascii=False,indent=2)+'\n')
(BASE/'problem_editorial_redirects.json').write_text(json.dumps(redirects,ensure_ascii=False,indent=2)+'\n')
