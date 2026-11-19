"""Apply individually authored provenance decisions, preserving all claim records.

This is a serialization of the manual source audit, not a keyword classifier.
The original task register is retained in bt_spaces_problem_origin_inputs.json.
"""
from pathlib import Path
import copy
import csv
import datetime
import json
import re

ROOT=Path(__file__).resolve().parents[2]
WORK=ROOT/'SA23_work'
SNAPSHOT=WORK/'integration/bt_spaces_problem_origin_inputs.json'
ORIGINAL=json.loads(SNAPSHOT.read_text())
PATHS={
 'bt':'sources/texts/pro/MPL_93_221-236+161-5_transcription.tex',
 's31':'sources/texts/codex/K161-3-01_transcription.tex',
 's32':'sources/texts/codex/K161-3-02_transcription.tex',
 's33':'sources/texts/codex/K161-3-03_transcription.tex',
 's41':'sources/texts/codex/K161-4-01_transcription.tex',
 's42':'sources/texts/codex/K161-4-02_transcription.tex',
}

# Exact question occurrences, selected manually, separate from broader claims.
# Each tuple is source-key, inclusive physical start/end, associated claim number.
LOCATIONS={
 'bt':{
  1:[('bt',10,22,1)],
  2:[('bt',73,84,5),('bt',175,179,7)],
  4:[('bt',167,175,11)],
  5:[('bt',187,206,13)],
  6:[('bt',224,243,15)],
  7:[('bt',269,277,19)],
  13:[('bt',866,868,51),('bt',875,918,51)],
  15:[('bt',929,935,54)],
  16:[('bt',937,950,55)],
  17:[('bt',1037,1043,57)],
  19:[('bt',1081,1081,62)],
  20:[('bt',1083,1083,63)],
  21:[('bt',1188,1202,70)],
  22:[('bt',1202,1202,71)],
  23:[('bt',1357,1365,69)],
  25:[('bt',1489,1495,77),('bt',1496,1498,79)],
 },
 'spaces':{
  1:[('s31',80,85,2)],
  2:[('s42',4,7,72),('s42',33,41,72),('s42',66,79,72),('s41',731,750,72)],
  3:[('s31',311,346,5)],
  4:[('s31',350,376,6)],
  7:[('s31',550,576,10)],
  8:[('s31',588,590,11),('s31',613,618,11)],
  9:[('s31',785,793,13),('s31',851,852,13)],
  10:[('s31',895,904,14)],
  11:[('s31',936,942,15),('s32',1,7,15)],
  12:[('s32',62,79,16),('s32',101,114,16)],
  13:[('s32',170,188,17),('s32',199,212,17)],
  15:[('s32',226,244,19),('s33',31,31,19)],
  17:[('s32',258,269,21),('s32',356,382,21)],
  18:[('s32',434,450,23)],
  21:[('s32',918,934,30)],
  22:[('s32',771,776,31)],
  24:[('s32',938,951,33),('s33',34,35,33)],
  26:[('s33',98,119,36),('s33',178,192,36)],
  28:[('s33',383,400,49)],
  30:[('s41',94,116,53)],
  31:[('s41',176,182,55)],
  32:[('s41',206,208,56)],
  33:[('s41',174,178,58),('s41',228,228,58),('s41',246,248,58)],
  34:[('s41',294,296,61)],
  36:[('s41',465,485,66),('s41',583,585,66)],
  37:[('s41',704,714,71)],
  38:[('s42',173,184,75)],
  39:[('s42',225,228,74)],
  40:[('s42',489,511,80)],
  41:[('s42',550,568,82)],
  42:[('s42',541,548,81),('s42',594,594,81)],
 }
}

# Only changes in mathematical/expository scope caused by the origin audit are
# supplied here. Unaffected checked fates and references are retained verbatim.
PATCHES={
 'bt':{
  2:{'title':'A manageable Picard–Fuchs criterion',
     'plausible_today':'Formulate the infinitesimal and fiber de Rham criterion with relative hypercohomology and the necessary comparison/base-change hypotheses; the Stein warning limits a particular quotient formula.',
     'why_open':'The source expressly seeks a manageable sufficient condition and later invokes fiber de Rham for the converse. It gives no historical reason for the remaining exposition.',
     'worth':'A short commentary is worthwhile because the source criterion must distinguish relative hypercohomology from its Stein simplification.'},
  6:{'title':'The marginal relative-version write-up',
     'plausible_today':'Write up the indicated relative formal differential-operator argument. First determine the intended exact complex; finite-order shifts and missing definitions are editorial prerequisites, not additional authorial questions.',
     'state_of_art':'The principal-parts representation and characteristic-zero formal-Poincaré framework are matched in EGA IV4 §16.8 and Crystals §6. The marginal relative-version instruction itself remains too compressed to identify a uniquely quantified finite-order theorem.',
     'why_open':'The margin says à rédiger within unsure markup. No further historical reason is supplied.',
     'worth':'Worth an editorial write-up only after the intended relative complex is identified, because the uncertain cue does not license a new universal exactness claim.'},
  23:{'title':'The unfinished qualification of cocharacter uniqueness',
      'plausible_today':'A specified tensor grading determines its cocharacter; the missing Du moins si clause may impose further data or hypotheses, but its content cannot be inferred from pi-invariance alone.',
      'state_of_art':'C-SA23-bt-069 verifies the uniqueness of the cocharacter attached to a specified grading. The source’s missing qualification remains unidentified; the distinct torsor-triviality assertion is only a reading/prerequisite issue.',
      'why_open':'Du moins si is left unfinished. The source supplies no reason and no missing condition to recover from mathematics alone.',
      'worth':'Scan-first commentary is worthwhile because the unfinished condition changes what uniqueness is being asserted.'},
  25:{'title':'Relative nonabelian conjugacy of sections',
      'plausible_today':'For specified Gamma, pi and coefficient action, classify sections extending alpha0 by the neutral restriction fiber in nonabelian H1; distinguish trivial neutral fiber from full injectivity and account for stabilizers.',
      'why_open':'The final paragraph expressly asks conjugacy and the restriction criterion. The conflicting Pro/Codex cancellation readings are present editorial evidence, not an explanation of why the author asked it.',
      'worth':'A bounded formulation is worthwhile because the nonabelian neutral-fiber distinction gives a concrete correction once the source’s group data and cancellation are fixed.'},
 },
 'spaces':{
  1:{'as_he_states':'The inverse-image display asks “π(u,v)^*(φ)(X,Y) = ?” and leaves the right side empty.'},
  2:{'title':'Product-topos equivalence and the requested comparison checks',
     'plausible_today':'Establish the product comparison by the product-site sheaf conditions and its universal property. Verify the embedding/intersection steps with their actual localizations; the two-projection-direct-image membership test is false.',
     'why_open':'The pages explicitly ask whether the comparison is an equivalence and whether alpha is an embedding; a cancelled margin also says le faire for the intersection verification. No historical explanation is supplied.'},
  3:{'plausible_today':'Identify the cancelled descent-diagram construction and its missing coherences before formulating a specific pseudolimit theorem.',
     'why_open':'The construction is cancelled and ends before its conditions are stated. The source does not explain why.',
     'worth':'Scan first: the cancelled proposal identifies a construction topic but no precise pseudolimit theorem to develop without inventing hypotheses.'},
  4:{'as_he_states':'“on veut des conditions pour que ce soit une équivalence”; the margin calls this “la question” and identifies enough points as the equivalent issue.',
     'why_open':'The source asks for conditions and then proves a sufficient compact-point criterion. This is an answered-in-part comparison question, not an inferred gap.'},
  7:{'plausible_today':'Test the particular displayed covering family in an infinite discrete product; separate the unfinished cover test from the overbroad blanket nonspatiality assertion, which the countable Baire case refutes.',
     'why_open':'The source literally asks whether the family is covering, then breaks off at ou encore; the reason for not completing it is not given.'},
  8:{'as_he_states':'“Il est douteux” that the inverse-limit topos and projections remain essential; a later projection inverse-image display is left blank.'},
  9:{'plausible_today':'Characterize those u0:C→E for which the site extension is cocontinuous. Restriction is fully faithful on cocontinuous functors, but arbitrary u0 need not satisfy the sheaf relations.',
     'why_open':'Automatic cocontinuity is explicitly said not to be clear. The following localization and cover tests investigate it.'},
  10:{'as_he_states':'“Est-il vrai ... que ... les foncteurs qui commutent aux ... petites se correspondent?” The calculation immediately below concludes “OK”.',
      'why_open':'This did not remain open on the pages: the source asks the question and then proves the needed descent of colimit preservation.'},
  11:{'as_he_states':'“Cela est-il suffisant ?” beside cover-to-epimorphism preservation; a margin answers “non”.'},
  12:{'why_open':'The source presents explicit Montrer que exercises and supplies the adjunction proof; these are pedagogical tasks rather than research conjectures.'},
  13:{'as_he_states':'“En conclure” the irreducible-closed criterion; “Prouver que” the sheaf/presheaf equivalence; “Interpréter” Points(PSh(X))≃Pro(X).',
      'why_open':'The source assigns these exercises and interpretations without a fully expanded proof; it supplies no further reason.'},
  15:{'why_open':'Two Prouver que exercises are followed on another leaf by the literal Question about spatial presheaf topoi, with an answer. They remain source questions even where answered.'},
  18:{'title':'The deleted question about the Morita gerbe band',
      'plausible_today':'For the positive-rank quadruple gerbe with the displayed evaluation compatibility, verify that the automorphism group of the trivializing object is GL(e)×GL(g).',
      'state_of_art':'The source’s subsequent local-inner and tensor-automorphism calculation answers this deleted band question. The direct matrix-unit/Morita proof in C-SA23-spaces-023 confirms the precise compatible statement; no open general cancellation problem is left.',
      'why_open':'The question is deleted and then answered by the completed automorphism calculation. No historical reason for its initial uncertainty is supplied.',
      'worth':'Commentary only: the completed automorphism calculation answers the narrow deleted question, while its compatibility data explain why unrigidified uniqueness would differ.'},
  21:{'as_he_states':'“What will insure that a given set will ... imply whatever other property ... comes up?” after the Giraud axioms heading.'},
  22:{'title':'The tentative “possibly all” classifying-topos extension',
      'plausible_today':'Specify the class of structures and its inverse-image preservation before asking universal classifiability; geometric theories supply a precise positive framework, but the word all is undelimited here.',
      'why_open':'The source itself adds possibly all. It does not define the proposed larger class or explain the hesitation.',
      'worth':'A bounded scope note is worthwhile because the tentative extension has no fixed quantifiers until the allowed structures and morphisms are specified.'},
  24:{'title':'Existence and uniqueness of field-model subtypes',
      'plausible_today':'For each specified lambda of allowed diagrams, ask whether the ring theory has a full subtype whose Set-models are exactly fields and whether it is unique. The finite-product algebraic case is negative; geometric-field theories use different logical operations.',
      'state_of_art':'Lawvere semantics gives the product-closure obstruction in the finite-product case. The source’s broader varying-lambda program is not converted into a single unconditional theorem. The later cancelled ring-map criterion is an attempted answer and is false as a field test.',
      'why_open':'On se propose ... d’étudier l’existence et l’unicité is explicit. The pages investigate cases, including a cancelled failed criterion, without supplying a full varying-lambda classification.',
      'worth':'A bounded comparison of specified theory types is worthwhile because ordinary algebraic and geometric field semantics have different preservation requirements.'},
  26:{'why_open':'The source explicitly asks reconstruction, functoriality and equivalence conditions; it supplies necessary conditions and cancels a further cocompletion attempt. No reason for the incomplete treatment is documented.'},
  28:{'as_he_states':'“See how to fix universe and restrict to U-sites. (Not to small sites, as we like to include topoi as sites...)”.',
      'why_open':'The margin explicitly assigns an exposition/size task. The standard universe conventions answer it; no set-theoretic conjecture is intended.'},
  30:{'plausible_today':'Determine which locally closed subsets and rc/qc finiteness qualifier make the bracketed equalizer statement valid under the displayed flat/generizing descent assumptions.',
      'why_open':'The bracketed row is explicitly questioned, while its rc/qc qualifier is transcribed uncertainly. The source does not explain more.'},
  31:{'as_he_states':'The descent checklist explicitly writes “formellement lisse (?)”.'},
  32:{'plausible_today':'Explain descent data and their effective reconstruction by the usual quasi-coherent-module equalizer; do not recast the asserted theorem as a conjecture.',
      'why_open':'The source says Expliquer ce que cela signifie, a pedagogical instruction after an asserted theorem.',
      'worth':'Commentary only: describing cocycle descent data and the equalizer construction directly answers the explanatory request.'},
  34:{'title':'The unfinished effectiveness-questions heading',
      'plausible_today':'The planned topic is effectiveness of scheme descent data; distinguish effective descent with specified polarization from arbitrary scheme descent, without supplying an absent authorial quantifier.',
      'state_of_art':'The checked descent references give examples of ineffective scheme descent and positive affine/polarized results. They contextualize the unfinished heading but cannot identify a unique unwritten question.',
      'why_open':'A numbered heading says Questions d’effectivité des données de descente and has no developed content. The source gives no reason for stopping.',
      'worth':'A short contextual note is worthwhile, but a new research problem should wait until a more precise source formulation is located.'},
  36:{'why_open':'An explicit Ex: vérifier instruction assigns the categorical examples. The surrounding property list is exposition, not a list of unanswered questions.'},
  37:{'plausible_today':'Give the principal-open covering equalizer condition for a covariant ring functor, including the empty cover. The later open-affine representability criterion is a distinct asserted development.',
      'why_open':'Comment exprimer is an explicit formulation question, answered by the later local-algebra construction.'},
  38:{'plausible_today':'For u:A→B, show that the closure of the image of V(J) is V(u^(-1)(J)); identify the corresponding dominance condition.',
      'why_open':'The line formule pour names the computation to be supplied but writes only the adjacent dominance condition.'},
  39:{'plausible_today':'Use the generic points of A1_k×A1_k over algebraically closed k, or the displayed residue-field tensor description, to exhibit a non-singleton fiber of the underlying-set comparison.',
      'why_open':'The margin expressly says donner exemple. The source separately states the general residue-field formula.'},
  40:{'plausible_today':'The lower algebra is B⊗_(A⊗A)A, equivalently B modulo the ideal generated by u(a)−v(a).',
      'why_open':'C=? is explicitly written in the square; the neighboring quotient formula already supplies the mathematical answer.'},
  41:{'plausible_today':'For finite I, a map from product A_i to k-prime is equivalent to orthogonal idempotents summing to one and maps into the corresponding factors. Confirming whether the trailing question mark is authorial remains a reading issue.',
      'why_open':'Only the transcribed unsure{?} marks possible doubt. The audit cannot certify that punctuation from a scan and does not attribute a stronger open problem.',
      'worth':'Commentary only, with punctuation verification first: the finite idempotent formula is elementary and the possible authorial doubt is not securely read.'},
  42:{'why_open':'The source explicitly asks for the subgroup relation definition and promises On reviendra dessus for finite relations; it does not specify the exact quotient notion.'},
 }
}

def occurrences(owner,n,claims):
 out=[]
 for key,lo,hi,cn in LOCATIONS[owner][n]:
  c=claims[f'C-SA23-{owner}-{cn:03d}'];lines=(ROOT/PATHS[key]).read_text().splitlines()
  scans=[];current=None
  for i,line in enumerate(lines[:hi],1):
   m=re.search(r'\\scanpage\{([^}]+)\}',line)
   if m:current=m.group(1)
   if i>=lo and current is not None and current not in scans:scans.append(current)
  out.append({'claim':c['id'],'cote':c['cote'],'scans':scans,'lines':f'{PATHS[key]}:{lo}-{hi}',
              'role':'actual source question or explicit deferred step; wider claim context retained separately'})
 return out

def apply_owner(owner):
 p=WORK/'parts'/owner
 audit=json.loads((WORK/f'integration/{owner}_problem_origin_audit.json').read_text())
 assert audit['completion']=='complete'
 decisions={r['original_id']:r for r in audit['decisions']}
 claims={c['id']:c for c in json.loads((p/'claims.json').read_text())}
 keep=[];eds=[]
 for original in ORIGINAL[owner]:
  q=copy.deepcopy(original);n=int(q['id'].rsplit('-',1)[1]);a=decisions[q['id']]
  q['original_task_title']=q['title'];q['origin']=a['origin'];q['origin_confidence']=a['confidence']
  q['source_cues']=a['source_cues'];q['origin_reason']=a['reason'];q['origin_audit_decision']=a['decision']
  q['source_author']=a.get('source_author','Alexander Grothendieck')
  if 'notes' in a:q['origin_notes']=a['notes']
  if a['decision']=='reclassify_to_editorial_task':
   q['original_id']=q['id'];q['id']=a['proposed_id'];q['record_type']='editorial task'
   q['source_assertion_as_recorded']=q.pop('as_he_states')
   q['previous_why_open']=q.pop('why_open')
   q['task']=a.get('recommended_as_he_states',q['title'])
   q['cue_or_reason']=a['reason'];q['why_editorial']=a['reason'];q['count_as_authorial_problem']=False
   eds.append(q);continue
  q['record_type']='authorial problem';q['count_as_authorial_problem']=True
  q['context_occurrences']=copy.deepcopy(q['occurrences'])
  q['occurrences']=occurrences(owner,n,claims)
  q['related_claims']=list(dict.fromkeys(x['claim'] for x in q['context_occurrences']))
  if 'recommended_as_he_states' in a:q['as_he_states']=a['recommended_as_he_states']
  q.update(PATCHES[owner].get(n,{}))
  if owner=='spaces' and n==41:q['source_question_certainty']='uncertain punctuation; possible authorial question'
  else:q['source_question_certainty']='explicit cue or identified unfinished proposal; see origin_confidence'
  keep.append(q)
 assert {int(q['id'].rsplit('-',1)[1]) for q in keep}==set(LOCATIONS[owner])
 (p/'problems.json').write_text(json.dumps(keep,ensure_ascii=False,indent=2)+'\n')
 (p/'editorial_tasks.json').write_text(json.dumps(eds,ensure_ascii=False,indent=2)+'\n')
 local_audit=copy.deepcopy(audit);local_audit['application']='Applied to owner problem/editorial registers; all mathematical claims retained.'
 local_audit['authorial_count']=len(keep);local_audit['editorial_count']=len(eds)
 (p/'problem_origin_audit.json').write_text(json.dumps(local_audit,ensure_ascii=False,indent=2)+'\n')
 eventsfile=p/'check_events.tsv'
 if eventsfile.exists():
  with eventsfile.open(newline='') as f:
   reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;events=list(reader)
  events=[e for e in events if e['type']!='manual source-question provenance audit']
  for a in audit['decisions']:
   events.append({'statement_id':a['proposed_id'],'date':'2026-11-19',
     'who':'GPT-6 Astra Pro; owner bt/spaces; SA23-20261119',
     'type':'manual source-question provenance audit',
     'outcome':a['original_id']+' → '+a['proposed_id']+'; '+a['decision']+'. '+a['reason']})
  with eventsfile.open('w',newline='') as f:
   w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(events)
 print(json.dumps({'owner':owner,'authorial_problems':len(keep),'editorial_tasks':len(eds),'claims_unchanged':len(claims)}))
 return keep,eds

if __name__=='__main__':
 import sys
 for owner in (sys.argv[1:] or ['bt','spaces']):apply_owner(owner)
