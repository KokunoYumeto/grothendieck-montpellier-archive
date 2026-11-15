"""Integrate the locally proofed final visual repairs, with exact replay records."""
from pathlib import Path
import csv,hashlib,json
P=Path(__file__).resolve().parents[1];R=P/'records'
repairs=[
 {'key':'ps_134-4_041','before':'bend right=50','after':'bend right=75','problem':'The outer curved arrow passed through the subscript of the middle Q_0 node.','action':'Increase only this arrow curvature to75 degrees, preserving endpoints, direction and every label.'},
 {'key':'ps_134-4_042','before':r'''"\hand{\ensuremath{\mathrm{Hom}_3}}" ' ''','after':r'''"\hand{\ensuremath{\mathrm{Hom}_3}}" '{xshift=12pt} ''','problem':'The Hom_3 label on a bent implication crossed the neighboring straight downward arrow.','action':'Move only the Hom_3 label12pt right; keep both arrows and the star label unchanged.'},
 {'key':'ps_134-5_028','before':r'''"\hand{if A,B \underline{W}-asph.}"' ''','after':r'''"\hand{if A,B \underline{W}-asph.}" ''','problem':'The condition on a dashed curved implication obscured the central iv-prime node.','action':'Place the same condition outside the left curve by removing its label-side swap; retain all arrows and words.'},
 {'key':'ps_134-7_035','before':r', viewed as an object in D.(Ab_{k}),','after':r'\text{, viewed as an object in }D.(Ab_{k}),','problem':'English prose inside the formula(U) insertion was interpreted as a joined italic mathematical word.','action':'Put the prose words in text mode inside the existing insertion; retain D.(Ab_k), every word, and punctuation.'},
 {'key':'ps_134-7_035','before':r'in Ab_{k},','after':r'\text{in }Ab_{k},','problem':'The final English word in in formula(U) was interpreted as two adjacent mathematical variables.','action':'Put in and its following space in text mode; retain Ab_k and the comma in the existing handwritten span.'},
 {'key':'ps_134-5_068','before':r'\inserted{corresponding} notion of weak equivalence W_{\hand{a}} in M','after':r'\inserted{\text{corresponding}}\text{ notion of weak equivalence }W_{\hand{a}}\text{ in }M','problem':'Formula(*) treated the inserted corresponding and subsequent explanatory prose as joined mathematical letters.','action':'Put only the English words and their spaces in text mode inside the existing formula; retain the insertion, W_a, M, arrows and punctuation.'}
]
for r in repairs:
 r['before']=r['before'].rstrip();r['after']=r['after'].rstrip()
mathpath=R/'MATH_PROSE_PROPOSED_PATCHES.json'
if mathpath.exists():
 proof=json.loads((R/'MATH_PROSE_PROOF_VALIDATION.json').read_text())
 assert proof['all_proof_hashes_match'] and proof['overfull_boxes']==0 and proof['missing_characters']==0
 observations=json.loads((R/'MATH_PROSE_PROOF_VISUAL_OBSERVATIONS.json').read_text())
 assert len(observations)==proof['actual_proof_pages']
 for observation in observations:
  assert observation['viewed']
  for field in ['pdf','image']:
   assert hashlib.sha256((P/observation[field]).read_bytes()).hexdigest()==observation[field+'_sha256']
 repairs.extend(json.loads(mathpath.read_text()))
statepath=R/'SOURCE_NORMALIZATION.json';state=json.loads(statepath.read_text())
patchpath=R/'TYPESETTING_PATCHES.json';patches=json.loads(patchpath.read_text())
def read(path):return list(csv.DictReader(path.open(),delimiter='\t'))
def write(path,rows):
 with path.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
decisionpath=R/'CHECK_DECISIONS_NORMALIZATION.tsv';decisions=read(decisionpath)
fixpath=R/'TYPESETTING_FIXES_NORMALIZATION.tsv';fixes=read(fixpath)
integrated=[]
for i,r in enumerate(repairs,1):
 key=r['key'];rid=r.get('id',f'LAYOUT:{key}:final-visual:{i}')
 if any(x['id']==rid for x in patches):continue
 path=P/'checked_pages'/(key+'.tex');s=path.read_text();entry=state['pages'][key]
 assert hashlib.sha256(s.encode()).hexdigest()==entry['after_sha256']
 assert s.count(r['before'])==1,(key,r['before'],s.count(r['before']))
 line=s.count('\n',0,s.index(r['before']))+1;out=s.replace(r['before'],r['after'],1)
 before_sha=entry['after_sha256'];after_sha=hashlib.sha256(out.encode()).hexdigest()
 entry['recorded_hunks']+=1;entry['mechanical_operations']+=1;entry['after_sha256']=after_sha;entry['changed']=True
 entry.setdefault('final_visual_repairs',[]).append({'patch_id':rid,'before_sha256':before_sha,'after_sha256':after_sha})
 source_id=f"MECH:{key}:integrated:{entry['recorded_hunks']}"
 decisions.append({'key':key,'cote':key.split('_')[1],'site':key.rsplit('_',1)[1].lstrip('0'),'line':line,'transcription_reading':r['before'],'image_reading':r['after'],'arxiv_reading':'','decision':'mechanical source integration; reading unchanged','reason':r['problem']+' '+r['action']+' The local proof was actually opened before integration. ['+rid+']','source_id':source_id})
 fixes.append({'reader':'all','page_key':key,'source_line':line,'what_was_wrong':r['problem'],'what_was_done':r['action']+' ['+rid+']'})
 patches.append(dict(r,id=rid));path.write_text(out);integrated.append(rid)
state['changed_pages']=sum(x['changed'] for x in state['pages'].values())
state['recorded_hunks']=sum(x['recorded_hunks'] for x in state['pages'].values())
state['mechanical_operations']=sum(x['mechanical_operations'] for x in state['pages'].values())
write(decisionpath,decisions);write(fixpath,fixes)
statepath.write_text(json.dumps(state,indent=2)+'\n');patchpath.write_text(json.dumps(patches,indent=2)+'\n')
print(json.dumps({'integrated_repairs':integrated,'mechanical_hunks':state['recorded_hunks']}))
