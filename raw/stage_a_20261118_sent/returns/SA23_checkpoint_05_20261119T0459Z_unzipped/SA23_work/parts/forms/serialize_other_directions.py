"""Manual numeric/provenance serialization of the completed bt and spaces directions."""
from pathlib import Path
import json
B=Path(__file__).resolve().parents[1]
def ids(prefix,nums,width=0):return [prefix+(str(n).zfill(width) if width else str(n)) for n in nums]
def row(title,interest,feasible,items,claims,problems,known,residual,first):
 return dict(title=title,interest=interest,feasible_progress_in_one_run=feasible,items=items,claims=claims,problems=problems,known=known,residual=residual,first_step=first)
def it(ns):return ids('SA23-',ns)
def c(w,ns):return ids('C-SA23-'+w+'-',ns,3)
def p(w,ns):return ids('MP-SA23-'+w+'-',ns,2)
bt=[
 row('Align the square-zero lift manuscript with its publication',5,5,it(range(226,236)),c('bt',list(range(22,32))+[88]),p('bt',[9,10]),'Grothendieck1968 section3.4 is an exact counterpart; additive homotopies and the derived-Hom arrow are checked.','The ink must determine degrees, notation and the local-isomorphism weakening.','Compare93/234–236 with section3.4 line by line, fixing the coefficient category before any stronger crystal theorem.'),
 row('Separate the two tensor-extension questions',5,4,it(list(range(259,270))+[278,279]),c('bt',range(65,72)),p('bt',[21,22,23]),'The BT-generated crystalline category has the standard admissible comparison; the Tate curve distinguishes it from all two-weight Hodge–Tate objects.','The actual generator notation, field direction and comparison data determine the remaining literal question.','Inspect161-5 scans23–24, state the two source categories, and test each on the unit, Tate line and Tate-curve extension.'),
 row('Identify finite-order formal exactness',5,4,it([206,220,221,223,224,225]),c('bt',[1]+list(range(15,22))),p('bt',[1,6,8]),'Principal parts and formal de Rham exactness provide conditional frameworks; the indicated injection is proved.','The quoted finite-order exactness has unspecified order shifts and Hom-exactness.','Compute orders0–3 for trivial stratified lines on affine one- and two-space, keeping characteristic-p tests separate.'),
 row('Fix the semilinear Gamma problem and its admissibility',5,3,it([261,272,273,274,275,276,277,278,279,281,282,283,284,285,286,287,288,299]),c('bt',range(74,82)),p('bt',[24,25]),'Normalized cocycles and stabilizers are checked; unrestricted rank-one uniqueness fails.','Deletion scope, coefficient fields, topology, Frobenius and admissibility remain essential.','Adjudicate scan29’s cancellation and list the actual definitions on scans25–28 before choosing a rank-one test model.'),
 row('Write the moving-endpoint Picard–Fuchs formula',4,5,it([208,209,210,211,212,213,214,215,216,218]),c('bt',range(3,15)),p('bt',[2,3,4,5]),'First-order endpoint terms and counterexamples are checked; canonical Gauss–Manin comparison is known.','Higher endpoint jets and their dependence on a local splitting need a carefully scoped commentary statement.','Derive second-order terms for a smooth holomorphic submersion and compare two splittings while retaining Stein/base-change assumptions.'),
 row('Build the precise two-weight classification table',4,3,it([240,250,251,258]),c('bt',[43,44,45,46,60,61,86]),p('bt',[18]),'Serre’s algebraic classification route and the coprime criterion are checked; arithmetic realization is separate.','The Springer correspondence and multiplicity-one corollary need an exact hypothesis table.','Read Springer section11 and match each case to Serre’s Theorem7 before considering BT realization.')
]
spaces=[
 row('Repair the product-subtopos proof',5,5,it([701,702,703]),c('spaces',[1,2,3,4,72]),p('spaces',[1,2]),'The product-site theorem is established; the direct-image membership test has a counterexample.','The three leaves need a correct localization and inverse-image argument.','Write the generated covering topology, its two sheaf conditions and the product universal property against each leaf.'),
 row('Identify the deferred finite-quotient statement',5,3,it([776]),c('spaces',[81]),p('spaces',[42]),'Finite locally free quotients and qualified later existence theorems are known; nonflat equivalence relations can be ineffective.','The intended categorical/geometric/effective meaning of the deferred assertion is not fixed.','Compare the wording with SGA3V and the exact Kollár/Witaszek references; use the small counterexample only for the intended stronger claim.'),
 row('Clarify compact-point refinements and infinite products',5,3,it([707,708,709,720]),c('spaces',[8,9,10,21]),p('spaces',[5,6,7,17]),'Local compactness is sufficient; blanket countable-discrete failure is false.','The precise locally closed compact-point quantifiers and their primary literature identity need clarification.','Translate the maximal-open proof into frame relations and test the relative-neighborhood quantifiers.'),
 row('Correct immersion descent and its provenance',4,5,it([754]),c('spaces',[58]),p('spaces',[33]),'Quasi-compact fpqc descent and arbitrary fppf descent are checked; the unqualified fpqc assertion fails.','The queried and later asserted leaves require a scan concordance.','Inspect both leaves and compare exact EGA/SGA numbering, keeping later web commentary separate from first publication.'),
 row('Interpret the cancelled inverse algebra',4,4,it([731,732]),c('spaces',[33,34,35]),p('spaces',[24,25]),'CRT and finite counterexamples are checked; Lawvere’s generalized-inverse theory is a relevant exact lead.','The cancelled text may be an algebraic regular-ring construction rather than a field classification.','Read the cancellation and compare the original1963/1968 texts with the later reprint without inferring influence.'),
 row('Fix essential-point and morphism conventions',4,5,it([710,715,716,717,718,719]),c('spaces',[11,16,17,18,19,20]),p('spaces',[8,12,13,14,15,16]),'SGA4IV7.6 supplies the exact presheaf/localic criteria and Karoubi qualification; the Cantor inverse-limit example is checked.','Variances and specialization orders differ between the leaves.','Draw each adjunction and translate every order convention before comparing essential and arbitrary geometric morphisms.'),
 row('State rigidified Morita cancellation precisely',4,5,it([722]),c('spaces',[23,24]),p('spaces',[18]),'Matrix-unit reconstruction works with positive finite rank; unrigidified uniqueness fails through line-bundle twists.','A clean groupoid statement with compatible morphisms needs a primary-source concordance.','Write the quadruple groupoid explicitly and match its compatibility data to an accessible Morita/Azumaya source.'),
 row('Specify structure-theory representation hypotheses',4,3,it([729,730,731,732,733,734]),c('spaces',[31,32,33,34,35,36,37]),p('spaces',[22,23,24,25,26]),'Conditional2-Yoneda reconstruction is valid; fields fail finite-product closure; geometric theories are a different framework.','The exact small sketch and change-of-topos assumptions are compressed.','Rewrite them as finite-limit or finite-product data and test each against the set-valued reconstruction.'),
 row('Prepare the affine-functor and principal-open commentary',3,5,it([767,772,773,774,775,776,777,778,779]),c('spaces',[71,77,78,79,80,81,82,83,84]),p('spaces',[37,40,41,42,43]),'The local algebra and explicit computations are checked.','Several arrows, powers and the omitted localization proof need a readable source companion.','Attach each short proof to its physical line after scan adjudication of the ambiguous symbols.'),
 row('Identify the cancelled torsor and limit fragments',2,1,it([704,723,774]),c('spaces',[5,25,79]),p('spaces',[3,19]),'The present text does not supply unique maps or coherence data.','A precise mathematical question must be recovered before literature development.','Start with scans and retain classF if the fragment still has no identifiable assertion.')
]
def ed(w,ns):return ids('ED-SA23-'+w+'-',ns,2)
# Manual scope changes after the source-question audit. No absent proof is
# promoted into an authorial MP merely to give a direction a provenance field.
bt_editor=[bt[0],bt[5]]
bt_editor[0]['problems']=[];bt_editor[0]['editorial_tasks']=ed('bt',[9,10])
bt_editor[1]['problems']=[];bt_editor[1]['editorial_tasks']=ed('bt',[18])
bt_editor.append(row('Identify the lower torus diagram before interpreting it',3,2,
 it([289,290,291]),c('bt',[82,83,84]),[],
 'Restriction of scalars and valuation splitting are understood in the stated fields.',
 'The model symbol, field labels and oblique pi are not identified by the transcription.',
 'Check the original symbols before comparing generic and special fibers.'))
bt_editor[-1]['editorial_tasks']=[]
bt_editor[-1]['editorial_task_description']='Stage4 prerequisite; no authorial question is invented for this diagram.'
bt=[bt[1],bt[2],bt[3],bt[4]]
bt[1]['title']='Write the relative formal-de Rham argument with its characteristic boundary'
bt[1]['problems']=p('bt',[1,6]);bt[1]['editorial_tasks']=ed('bt',[8])
bt[1]['residual']='The source asks the characteristic question and marks a relative-version write-up; the intended complex and finite-order quantifiers are editorial prerequisites.'
bt[1]['first_step']='Identify the relative complex behind the marginal instruction, then test the characteristic boundary and small principal-parts orders without attributing those reader tests to the author.'
bt[2]['title']='Specify the relative semilinear conjugacy question'
bt[2]['problems']=p('bt',[25]);bt[2]['editorial_tasks']=ed('bt',[24])
bt[2]['residual']='The actual question is conjugacy of sections extending alpha0; existence is assumed in the surrounding construction and remains an editorial prerequisite.'
bt[3]['problems']=p('bt',[2,4,5]);bt[3]['editorial_tasks']=ed('bt',[3])

spaces_editor=[spaces[9]]
spaces_editor[0]['problems']=p('spaces',[3]);spaces_editor[0]['editorial_tasks']=ed('spaces',[19])
spaces_editor[0]['editorial_task_description']='Reading and identification prerequisite; the cancelled limit proposal is too incomplete for a ranked research task.'
spaces=spaces[:9]
spaces[2]['title']='Compare the actual product-equivalence questions in frame language'
spaces[2]['items']=it([705,706,707,708,709,720])
spaces[2]['claims']=c('spaces',[6,7,8,9,10,21])
spaces[2]['problems']=p('spaces',[4,7,17]);spaces[2]['editorial_tasks']=ed('spaces',[5,6])
spaces[2]['residual']='The source asks for comparison conditions and for the infinite-discrete covering test; the proved compact-point refinement is supporting context.'
spaces[2]['first_step']='Translate the asked equivalence into frame relations, then compare the sufficient compact-point conditions with the exact failed discrete-cover attempt.'
spaces[4]['title']='Compare field-model subtypes with the cancelled regular-ring construction'
spaces[4]['problems']=p('spaces',[24]);spaces[4]['editorial_tasks']=ed('spaces',[25])
spaces[4]['residual']='The real program varies the allowed diagram types; the cancelled ring test is a failed proposed answer within that program.'
spaces[5]['problems']=p('spaces',[8,12,13,15]);spaces[5]['editorial_tasks']=ed('spaces',[14,16])
spaces[6]['title']='Explain the answered Morita gerbe-band question'
spaces[6]['interest']=3
spaces[6]['known']='The source computes the compatible automorphism group GL(e)×GL(g) and answers its deleted question; the matrix-unit reconstruction confirms it.'
spaces[6]['residual']='Only a precise source companion and primary-source concordance remain; no new cancellation theorem is being proposed.'
spaces[6]['first_step']='Write the automorphism calculation with its evaluation compatibility beside the deleted band question.'
spaces[7]['problems']=p('spaces',[22,24,26]);spaces[7]['editorial_tasks']=ed('spaces',[23,25])
spaces[8]['items']=it([767,772,773,774,775,777,778,779])
spaces[8]['claims']=c('spaces',[71,77,78,79,80,82,83,84])
spaces[8]['problems']=p('spaces',[37,40,41]);spaces[8]['editorial_tasks']=ed('spaces',[43])
spaces[8]['residual']='The source asks the ring sheaf formulation and C=?; the idempotent punctuation is uncertain. The abbreviated localization proof is an editorial dependency.'

for who,rows,editor in [('bt',bt,bt_editor),('spaces',spaces,spaces_editor)]:
 for i,r in enumerate(rows,1):
  r['rank']=i;r['record_type']='ranked direction from authorial problem'
  original_number=([2,3,4,5] if who=='bt' else list(range(1,10)))[i-1]
  r['id']=f'D-SA23-{who}-{original_number:02d}'
  r['original_rank']=original_number
  r.setdefault('editorial_tasks',[])
 for i,r in enumerate(editor,1):
  r.pop('rank',None)
  original_number=([1,6,7] if who=='bt' else [10])[i-1]
  r['id']=f'D-SA23-{who}-{original_number:02d}';r['original_rank']=original_number
  r['record_type']='editorial follow-up outside Stage6'
  r['reason_outside_stage6']='The main task is source identification or a reader-generated verification, not an independently formulated authorial research question.'
 (B/who/'directions.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
 (B/who/'editorial_directions.json').write_text(json.dumps(editor,ensure_ascii=False,indent=2)+'\n')
 md=[f'# Ranked directions from {who}', '',
     'Every ranked direction cites an actual surviving source question or explicit deferred step. Solved exercises are labelled as commentary; editorial dependencies are recorded separately.', '']
 for r in rows:
  md += [f"## {r['rank']}. {r['title']}", '',
         f"Interest {r['interest']}/5; feasible progress in one run {r['feasible_progress_in_one_run']}/5.", '',
         'Provenance: '+', '.join(r['items']+r['claims']+r['problems'])+'.', '',
         'Known: '+r['known'], '', 'Remaining scope: '+r['residual'], '',
         'First step: '+r['first_step'], '']
  if r['editorial_tasks']:md += ['Editorial prerequisites: '+', '.join(r['editorial_tasks'])+'.', '']
 md += ['## Editorial follow-ups outside Stage6', '',
        'These remain useful work but are excluded from the ranked authorial-problem directions.', '']
 for r in editor:
  md += [f"### {r['title']}", '',
         'Provenance: '+', '.join(r['items']+r['claims']+r['problems']+r.get('editorial_tasks',[]))+'.', '',
         r['known']+' '+r['residual'], '', 'First step: '+r['first_step'], '']
 (B/who/'directions.md').write_text('\n'.join(md)+'\n')
print('Serialized 4 bt and 9 spaces ranked directions; 3 bt and 1 spaces editorial follow-ups are outside Stage6.')
