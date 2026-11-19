"""Serialize the completed manual authorship/chronology and merge audit.

No owner register or merger is modified by this program. The three proposed
classification decisions and the merge decisions below were made after reading
the complete claim registers and the relevant original source endpoints.
"""
import csv
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

BASE=Path(__file__).resolve().parents[3]
OUT=BASE/'work/global_audit'
(OUT/'outputs').mkdir(parents=True,exist_ok=True)
stamp=datetime.now(timezone.utc).isoformat()
paths=[BASE/'work/cotes5_6/claims.json',BASE/'work/cotes6_7/claims.json',
       BASE/'work/root_review/claims_c7.json',BASE/'work/root_review/claims_c8.json',
       BASE/'work/cotes8_9_4/claims.json']

def tsv(name,fields,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(rows)

candidates=[
 {'id':'P56-C074','observed_class':'E','recommended_class':'A',
  'exact_source':'Grothendieck1968, Appendix, printed pp. 356–357 (PDF pages 50–51)',
  'author':'Alexander Grothendieck; notes by I. Coates and O. Jussila',
  'url':'https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.Grothendieck.CRCSscan.pdf',
  'web_ref':'turn107587248view1',
  'reason':'The exact compatible infinitesimal-diagonal and cocycle definition is in his own 1968 publication. Modern standardness and the BO1978 citation do not establish that this whole formulation was known before him.',
  'boundary':'No first-priority claim. The pseudo-stratification distinction is the explicit omission of the cocycle, not an independently dated theorem.',
  'status':'Recommendation sent to owner and root; owner controls its register.'},
 {'id':'P67-C069','observed_class':'E','recommended_class':'A',
  'exact_source':'Grothendieck1968 §3.3, printed pp. 325–326; compare KatzOda1968 §2 Theorem 1, p. 204, and §3',
  'author':'Alexander Grothendieck for the local construction; Nicholas M. Katz and Tadao Oda for the cited global theorem',
  'url':'https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.Grothendieck.CRCSscan.pdf',
  'web_ref':'turn867439943view0',
  'reason':'The row includes the Gauss–Manin action obtained from lifted base derivations, beyond the classical Cartan identity. His own later text gives the local formally smooth affine construction.',
  'boundary':'Retain the local/formally smooth affine scope. Only the Cartan homotopy identity by itself is the classical E ingredient. A general global formulation must use the separately stated theorem and hypotheses.',
  'status':'Recommendation sent to owner and root; owner controls its register.'},
 {'id':'P894-C070','observed_class':'E','recommended_class':'B',
  'exact_source':'Serre1958: historical surface; BerthelotEsnaultRulling2012 §9.2: later use; KatzSGA7XXII Theorem 3.3, (3.3.4), and Illusie1976: crystalline deduction inputs',
  'author':'Jean-Pierre Serre; Pierre Berthelot, Hélène Esnault and Kay Rülling; Nicholas M. Katz; Luc Illusie',
  'url':'https://annals.math.princeton.edu/wp-content/uploads/annals-v176-n1-p08-p.pdf',
  'web_ref':'turn485449693view2',
  'reason':'The 1958 attribution dates the free-quotient construction, not the entire crystalline torsion conclusion. The full row uses later crystalline and stable-augmentation results and this run’s explicit inference.',
  'boundary':'No first publication of this exact crystalline corollary is claimed. The construction remains credited to Serre, and the admitted integral-Lefschetz hypotheses remain explicit.',
  'status':'Root agreed; applied by this reviewer in the owned P894 register and logged in its check_events.tsv.'},
]
(OUT/'classification_candidates.json').write_text(json.dumps(candidates,ensure_ascii=False,indent=2)+'\n')
candidate_ids={x['id'] for x in candidates}

inventory=[];review=[]
for path in paths:
    data=json.loads(path.read_text())
    inventory.append({'date_utc':stamp,'source':str(path.relative_to(BASE)),
                      'records':len(data),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                      'read_scope':'Complete claim statements, statuses, fates, dates and references; A/E-focused review. The P894 register was already read completely and retained as a stable owned source.'})
    for c in data:
        if c['id'] in candidate_ids:
            outcome='Concrete candidate recorded in classification_candidates.json; owner-controlled implementation.'
        elif c['class']=='A':
            outcome='No additional strict-authorship mismatch found against the recorded author and exact source. This is not a fresh proof audit of the cited theorem.'
        elif c['class']=='E':
            outcome='No concrete reclassification supported by this focused audit. A modern exposition date alone was not treated as proof that an elementary or older result first arose later.'
        else:
            outcome='Read for context and consistent scope; outside the requested A/E reclassification target.'
        review.append({'claim_id':c['id'],'current_class_at_serialization':c['class'],
                       'source':str(path.relative_to(BASE)),'outcome':outcome})
tsv('classification_review.tsv',['claim_id','current_class_at_serialization','source','outcome'],review)

merges=[
 {'kind':'item','ids':'P56-I106;P67-I077;P78-I010','recommendation':'Keep P56-I106/P67-I077 for their exact common categorical core; detach P78-I010.',
  'source_endpoints':'cote 6:7, line 1551; cote 7:54–55, lines 1830 and 1838–1845; cote 7:71–72, lines 201–211',
  'reason':'The first two have the formally smooth crystal/stratified-module equivalence in common. The third asks a cohomology comparison. Equivalence of cartesian-object categories does not by itself identify ambient site-derived cohomology.',
  'limits':'Preserve the separate flat/coherent and arbitrary-fibred-category extensions in the first item’s component versions.'},
 {'kind':'item','ids':'P67-I080;P78-I001','recommendation':'Retain with the explicit compatibility and limit qualifications.',
  'source_endpoints':'cote 7:57–58, lines 1878–1932; cote 7:61–62, lines 6–49 in the following package',
  'reason':'The completed Čech–Alexander construction and its coefficient/limit justification continue across the package boundary.',
  'limits':'The continuation’s cartesian compatibility and Mittag–Leffler qualification must remain explicit.'},
 {'kind':'item','ids':'P78-I060;P894-I001','recommendation':'Retain.',
  'source_endpoints':'cote 8:78, lines 2755–2799; cote 8:79, lines 3–25',
  'reason':'This is a direct continuation of the derived character/co-Lie formula and its coefficient change.',
  'limits':'Keep the separate finite-generation proof scope and the arbitrary-character published result.'},
 {'kind':'claim','ids':'P78-C069;P78-C070;P894-C001','recommendation':'Retain as the continuous formula calculation, with component classes/statuses preserved.',
  'source_endpoints':'cote 8:78–79',
  'reason':'The two pages calculate the same co-Lie object, followed by derived coefficient-change associativity.',
  'limits':'The E-class elementary associativity ingredient must remain visible inside component_versions rather than becoming a new Bergh–Rydh priority claim.'},
 {'kind':'problem','ids':'P56-P021;P78-P003','recommendation':'Keep separate and link.',
  'source_endpoints':'cote 6:7, line 1551; cote 7:71–72, lines 201–211',
  'reason':'The first asks categorical equivalence for coherent objects with flat-lfp weakening; the second asks equality of site cohomology and nil-invariance. Their statements are not identical.',
  'limits':'Their relation is substantive but does not supply an equivalence of the two conjectures.'},
 {'kind':'problem','ids':'P56-P028;P67-P018','recommendation':'Keep separate and link as successive failures of the ordinary non-PD programme.',
  'source_endpoints':'cote 6:18–19, lines 1743–1751; cote 7:15–17, lines 1077–1133',
  'reason':'The first asks the field-level unit-coefficient comparison and proposes deriving in quasi-coherent crystals. The second asks a W(k)-valued inverse-limit comparison, possibly modulo torsion, and gives the ordinary-abelian obstruction.',
  'limits':'Do not erase the different coefficient bases or the proposed quasi-coherent-derived repair.'},
 {'kind':'problem','ids':'P56-P029;P56-P030;P67-P031','recommendation':'Keep all three separate and link.',
  'source_endpoints':'cote 6:19–20, lines 1759–1767; cote 7:51–52, lines 1763–1784',
  'reason':'Unchecked curvature, the entire Leray spectral sequence, and construction/descent of a global derived connection are distinct obligations. Katz–Oda Theorem 1 and Theorem 3/addendum settle different formulations.',
  'limits':'P56-P029 already mentions a derived object; the distinction is the obligation being checked, not merely the presence of derived notation.'},
 {'kind':'problem','ids':'P56-P014;P67-P021','recommendation':'Keep separate and link through the shared Euler-homotopy test.',
  'source_endpoints':'cote 5:37, lines 1007–1032; cote 7:24,26, lines 1269–1274 and 1309–1316',
  'reason':'The formal/local-algebra examples and the m³ kernel lemma differ from the alleged cusp Betti-number discrepancy. They have different hypotheses and conclusions.',
  'limits':'A common proof technique is not identity of research problems.'},
]
tsv('merge_audit.tsv',['kind','ids','recommendation','source_endpoints','reason','limits'],merges)
for path in [BASE/'work/code/merge_core.py',BASE/'work/code/merge_aux.py']:
    inventory.append({'date_utc':stamp,'source':str(path.relative_to(BASE)),
                      'records':'','sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                      'read_scope':'Full code read. The enumerated mathematical identities, component preservation and remapping behavior were inspected. No owner file was changed.'})
for name,scope in [
 ('MPL_5+6_001-037_transcription.tex','Targeted source rereading: lines 1535–1568 and 1725–1788, categorical comparison and the distinct Gauss–Manin/Leray questions.'),
 ('MPL_6_038-067+7_001-060_transcription.tex','Targeted source rereading: lines 1068–1144 and 1745–1865, ordinary non-PD failure, derived connection and categorical comparison.'),
 ('MPL_7_061-072+8_001-078_transcription.tex','Targeted source rereading: lines 193–218, the flat cohomology/nil-invariance question.'),
 ('MPL_8_079-081+9+4+100_transcription.tex','Targeted source rereading: lines 1280–1313, attribution of trace-surjectivity and the n=1 boundary refinement.')]:
    path=BASE/'sources/SA15_texts/pro'/name
    inventory.append({'date_utc':stamp,'source':str(path.relative_to(BASE)),
                      'records':'','sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                      'read_scope':scope})
tsv('source_read_log.tsv',['date_utc','source','records','sha256','read_scope'],inventory)

who='GPT-6 Astra Pro; effort setting not exposed; SA15-20261119/cotes8_9_4 global audit'
events=[
 {'statement_id':'P56-C074','date':'2026-11-19','who':who,'type':'used and rechecked in this run','outcome':'Independently opened Grothendieck1968 Appendix pp356–357 and matched the compatible infinitesimal-diagonal/cocycle definition. Recommended E→A for this exact published formulation; no priority inference.'},
 {'statement_id':'P67-C069','date':'2026-11-19','who':who,'type':'used and rechecked in this run','outcome':'Independently opened Grothendieck1968 §3.3 pp325–326. The local Gauss–Manin construction goes beyond the old Cartan identity; recommended A with its actual local hypotheses.'},
 {'statement_id':'Grothendieck1968','date':'2026-11-19','who':who,'type':'used and rechecked in this run','outcome':'Primary title/authorship, lecture dates, §3.3 local construction and Appendix stratification definition were independently read for the narrow authorship/chronology audit. No wholesale proof verification.'},
 {'statement_id':'KatzOda1968','date':'2026-11-19','who':who,'type':'used and rechecked in this run','outcome':'Primary title/authors and communication date checked; Theorem1 p204 distinguished from Theorem3 pp211–212 and Deligne’s addendum. Used to keep integrability and Leray questions separate.'},
]
tsv('classification_cross_events.tsv',['statement_id','date','who','type','outcome'],events)

report={'records_read':len(review),'source_claim_files':len(paths),
        'classes_at_serialization':dict(Counter(r['current_class_at_serialization'] for r in review)),
        'concrete_classification_candidates':len(candidates),'merge_groups_reviewed':len(merges),
        'new_strict_authorship_error_in_current_A_rows':0,
        'initial_snapshot_counts':{'claims':383,'A':35,'E':81},
        'note':'Initial counts predate owner corrections during this audit. The review table records the later serialization snapshot.',
        'owner_files_modified_by_this_audit_serializer':0}
(OUT/'outputs/audit_census.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
