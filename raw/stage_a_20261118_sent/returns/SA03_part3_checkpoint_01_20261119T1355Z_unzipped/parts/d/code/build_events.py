"""Serialize check scopes after the recorded passage and source inspections."""
from pathlib import Path
import json,csv
out=Path(__file__).resolve().parents[1]
events=[]
who='GPT-6 Astra Pro; inherited effort not exposed; SA03-part3/root'
def event(i,t,o):events.append(dict(statement_id=i,date='2026-11-19',who=who,type=t,outcome=o))
for i in json.loads((out/'items.json').read_text()):
    event(i['id'],'used and rechecked in this run','Entry and cited transcription passage read; textual check '+i['check']+'. '+i['check_reason']+' This event certifies the comparison, not an unproved mathematical assertion.')
for c in json.loads((out/'claims.json').read_text()):
    event(c['id'],'used and rechecked in this run','Claim statement and page status compared with the supplied passage; literature route is stated in fate. '+c['computation'])
for r in json.loads((out/'references.json').read_text()):
    event(r['key'],'used and rechecked in this run' if r['note']=='verified' else 'carried as background without fault found',r['scope'])
for n in [604,605,606,608,609,610,614,616,620,625,626,640,641]:
    event(f'CL-SA03-{n}','computation or formal certificate','Exact symbolic or finite-field calculation passed; see code/check_computations.py, outputs/computations.txt, and additional_computations.txt. Certificate scope is stated in the claim; it does not prove surrounding representability or classification theorems.')
for n in [601,636,638]:
    event(f'CL-SA03-{n}','independent re-proof','The specific reduction/sign/identity-locus/conditional estimate is proved in proof_checks.md; general invoked background and missing source hypotheses are explicitly excluded.')
for n,refined in [(605,611),(615,621),(616,624),(624,614)]:
    event(f'CL-SA03-{n}',f'refuted, with refined statement id SA03-{refined}','The literal formula or global-section reading is refuted; see exact computation/argument and retained correction. This is not an ink adjudication or refutation of the corrected statement.')
for n,o in [(644,'Explicit rank2 connection has invertible p-curvature for every oddp; disproves the prior run’s broad implication, not a manuscript assertion.'),(666,'Independent p-torsion-free cancellation proof; exactness only.'),(667,'xy=p linear algebra countermodel to automatic local freeness, with no claimed crystal structure.'),(669,'Dual-number ordinary-Frobenius counterexample; actual crystallineφ not tested.'),(677,'Square-zero graph calculation gives Hom(F,H/F)⊗I and rankg²; no effectivity proof.')]:
    event(f'SA03-{n}','computation or formal certificate',o+' See proof_checks.md and outputs/computations.txt.')
with (out/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)
print('Scoped check events:',len(events))
