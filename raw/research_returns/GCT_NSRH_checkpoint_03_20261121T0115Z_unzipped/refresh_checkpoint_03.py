from pathlib import Path
import csv, hashlib, json, re
from datetime import datetime, timezone
root=Path(__file__).resolve().parent
now=datetime.now(timezone.utc).isoformat()
ep=root/'CHECK_EVENTS.tsv'
with ep.open() as f:
 r=csv.DictReader(f,delimiter='\t'); fields=r.fieldnames; events=list(r)
def add(sid,who,kind,outcome,record):
 item=dict(zip(fields,[sid,'2026-11-21',who,'GPT-6 Astra Pro','not exposed','GCT_NSRH_20261121',kind,outcome,record]))
 if not any(e['statement_id']==sid and e['who']==who and e['type']==kind and e['locator_or_record']==record and e['outcome']==outcome for e in events):events.append(item)
for row in csv.DictReader((root/'agent_grothendieck_check_events.tsv').open(),delimiter='\t'):
 add(row['statement_id'],'/root/grothendieck_dictionary',row['type'],row['outcome'],'agent_grothendieck_check_events.tsv; original who: '+row['who'])
for sid,name,who in [
 ('F35','REVIEW_STACK_TRACE_THETA.md','/root/rectangular_and_theta'),
 ('F36-NORMALIZATION','REVIEW_COHERENT_FROBENIUS_NORMALIZATION_THETA.md','/root/rectangular_and_theta'),
 ('F39','REVIEW_NC_WEIL_THETA.md','/root/rectangular_and_theta'),
 ('F40','REVIEW_AUSLANDER_COLLISION_GCT.md','/root/gct_statements'),
 ('F41','REVIEW_FINITE_WEIGHT_WINDOW_GCT.md','/root/gct_statements')]:
 p=root/name
 if p.exists():add(sid,who,'targeted proof check','PASS, full proof and exact source/final-fragment scope in review; SHA256 '+hashlib.sha256(p.read_bytes()).hexdigest(),name)
for sid,name,desc in [
 ('F33','finding_F33.tex','Full known-motive application proof read; subset reindexing, every twist, finite-field applicability and complete SL8 degree15 mixed example checked.'),
 ('F34-RAY-FRAGMENT','finding_F34_ray.tex','Full generated proof and scheme paragraph read and matched to report; actual free coordinates and characteristic-zero ray kernel checked.'),
 ('F40','finding_F40.tex','Whole report and generated proof read. Every diagonal map/kernel, all corner module actions, non-right-admissibility, exceptional decomposition and Frobenius-enriched TP application checked.'),
 ('F41','finding_F41.tex','Whole report and generated proof read. Finite window, actual Tate multiplicity85, non-Laurent pole, fixed-q full action transport and exact limits checked.'),
 ('F42-REPORT','agent_fixed_q_operator_gate.md','Whole proof read. Actual rank40 generator, all pole counts including eventual equality and normalization, exact fixed-q tensor action, coefficient-object repair and affine sign countermodel checked.')]:
 p=root/name
 if p.exists():add(sid,'/root','targeted proof check','PASS. '+desc+' SHA256 '+hashlib.sha256(p.read_bytes()).hexdigest(),name)
add('SRC-MERKURJEV-SL','/root','used and rechecked in this run','Primary perfect-field setting, §5 multi-index notation and Corollary5.5 checked; motive theorem cited as known, not reproved.','Merkurjev author530.pdf, §2 p3; §5 pp7–8, Corollaries5.3/5.5; root source read 01:04–01:05UTC')
add('SRC-TABUADA-ADDITIVITY','/root','used and rechecked in this run','Read enriched TP equation6.9 with its q-linear Frobenius convention, Example12.3 semiorthogonal additivity, and Thm2.12 proof12.6. Exact hypotheses match explicit smooth proper Γ/Λ; no blanket nilinvariance assumed.','Tabuada arXiv1808.00950v7, §6.1–6.2 pp15–16; §7 p17; Example12.3 p24; proof12.6 p26')
with ep.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(events)

qp=root/'QUESTIONS.tsv'
with qp.open() as f:
 r=csv.DictReader(f,delimiter='\t'); qfields=r.fieldnames;rows=list(r)
by={x['id']:x for x in rows}
def update(key, **kw):by[key].update(kw)
def qadd(vals):
 r=dict(zip(qfields,vals))
 if r['id'] in by:by[r['id']].update(r)
 else:rows.append(r);by[r['id']]=r
update('Q3-NCWEIL',state='DIRECT_OBSTRUCTION_AND_SMOOTH_CORNER_REPAIR_PROVED',finding_ids='F39,F40',current_gate='The direct collision category is nonsmooth, but explicit smooth proper Λ recovers the exact algebra as End(P) and actual specialized tensor module as Hom(P,Mtilde). Whole-category TP is four unit eigenvalues. This does not realize designated coefficient morphisms or recover relative order by itself.',next_step='Construct/check the relative smooth order retaining collision length, and specify the quantum-grade/Weil/basis comparison.')
update('QNEW-H3',finding_ids='F19,F21,F25,F36,F39,F40',current_gate='Exact algebra/module, coherent Frobenius, commutant defects and smooth special-fiber corner realization are proved. Relative smooth order and simultaneous based left/right action are under active proof checking.',next_step='Finish relative and based-action constructions; identify arithmetic coefficient and path-output comparisons.')
update('Q6',finding_ids='F01–F41',current_gate='Every integrated paper finding F01–F41 has a separate PartIII translation. New additions undergo final scope matching; exact archived anchors remain framework references.')
qadd(['Q4-HOOK-GEOMETRY','IP Prop6.4; Merkurjev Cor5.5 p8','Can rectangular hook coefficients be realized by ordinary split-group cohomology?','PROVED_KNOWN_SOURCE_APPLICATION_WITH_EXACT_WEIGHT_LIMIT','F33','The coefficient equals dim H^k(SL_min(n,d)); actual Tate summands are explicit. H15(SL8) has weights16 and18, so this realization is mixed.','Known motive decomposition plus subset-degree computation','No designated nonstandard action or basis follows from this equality of dimensions.'])
qadd(['Q3-SMOOTH-CORNER','F39; Tabuada Example12.3/eq6.9; F40','Can a smooth proper category retain the actual collision algebra and tensor action?','PROVED_EXPLICIT_CORNER_AND_PERFECT_MODULE_LIFT','F40','Λ=k²×M2(End_B(B⊕k)) is smooth proper, with exact A1 corner and actual M1=Hom(P,Mtilde), dim Mtilde104. Its TP spectrum is four ones. Corner embedding is not right-admissible.','Complete finite diagonal resolution; exact module recovery; exceptional pair; enriched TP','Extend to the actual relative collision order and compare designated coefficients/operations with the invariant.'])
qadd(['Q3-FINITE-WINDOW','F35 actual groups; F26 normalized trace; F41','Can a finite weight subquotient preserve the normalized extension trace and actual action?','FINITE_TRACE_PRESERVATION_REFUTED; FIXED_Q_TRANSPORT_PROVED','F41','Every bounded weight window is finite and cannot preserve h_n. A chosen64-subspace of Q_l(6)^85 after twisting supports the exact fixed-q action; it is transported, not restricted from an existing stack action.','Exact degree/weight enumeration; rational pole; actual cohomological subspace and generator transport','Specify the required all-extension comparison; fixed-q action is insufficient.'])
qadd(['Q3-ALL-WORDS','F19/F21 actual P1; F42 report','Does clearing denominators yield one finite Weil space for every actual word?','PROVED_IN_ROOT_CHECKED_REPORT; FINAL_FRAGMENT_IN_PROGRESS','F42','Tr(P1^k)=40(q^n+2+q^-n)^k has2k+1 genuine poles. No common finite Frobenius spectrum supports unbounded k, even with scalar/sign/Tate shifts. Fixed-q tensor actions and word-dependent coefficient objects exist.','Exact pole count; actual fixed-q operator/tensor axiom; coherent one-generator coefficient functor','Integrate final fragment; test simultaneous positive graded operator models and the path comparison.'])
with qp.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=qfields,delimiter='\t');w.writeheader();w.writerows(rows)

external=[]
for p in sorted((root/'primary_sources').rglob('*')):
 if p.is_file():external.append({'local_research_input':str(p.relative_to(root)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'redistributed':False,'locator_reference':'GCT_NSRH.tex bibliography and source/review reports; exact version and archive scan/folio distinguished'})
(root/'EXTERNAL_INPUT_MANIFEST.json').write_text(json.dumps(external,indent=2)+'\n')
(root/'STATUS_TIME.txt').write_text('WORK IN PROGRESS\nStatus refreshed UTC: '+now+'\nFirst scheduled progress review: 2026-11-21 02:00UTC /03:00Europe-Berlin\nCheckpoint03 due: 2026-11-21 01:15UTC /02:15Europe-Berlin\nNo scheduled no-movement review has yet occurred.\n')
for file in ['README.md','IMPLICATIONS.md']:
 p=root/file;s=p.read_text().replace('F01–F32 and F34–F39','F01–F41')
 s=s.replace('A smooth corner-resolution repair remains active.', 'F40 supplies a checked smooth corner resolution retaining the actual collision algebra and tensor action. Its relative extension and a joint positive left/right action are actively being tested.')
 s=s.replace('An action-preserving smooth corner-resolution repair is now being pursued.', 'F40 supplies the action-preserving smooth corner repair: the actual algebra is End(P) and its tensor module is Hom(P,Mtilde) in a smooth proper category with four unit TP eigenvalues. Its nonsmooth corner is not an admissible motivic summand; the based-operation and relative comparisons remain distinct.')
 p.write_text(s)
with (root/'LEDGER.md').open('a') as f:
 f.write(f'''\n## {now}: smooth corner repair and finite extraction\n\nNot a scheduled review. The F39 direct obstruction is now followed by the checked F40 smooth proper repair, with exact actual corner and tensor-module action. This closes the previously open smooth-categorical-retention row and reduces its remaining gate to relative deformation and designated morphism/weight/basis comparison. F41 closes finite-window extraction under the literal normalized trace condition, while constructing a chosen effective fixed-q action. F42's entire report has a root proof check and narrows the denominator-clearing approach to word-dependent coefficient objects or different comparison laws. The actual joint positive left/right action and a relative Auslander order are in progress.\n\nThe first scheduled review has not occurred; the no-movement counter remains unstarted.\n''')
print(json.dumps({'questions':len(rows),'events':len(events),'external_input_files':len(external),'refreshed_utc':now}))
