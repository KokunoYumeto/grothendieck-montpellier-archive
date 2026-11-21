from pathlib import Path
import csv

base=Path(__file__).resolve().parent.parent
work=base/'work'
target=base/'K17_package'/'CHECK_EVENTS.tsv'
root=work/'root_checks.tsv'
if not root.exists(): root.write_text(target.read_text())
rows=[]
def classify(s):
    s=s.lower()
    if s in ('targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found'): return s
    if 'independent re-proof' in s or ('independent' in s and ('derivation' in s or 'reconstruction' in s)): return 'independent re-proof'
    if 'comput' in s or 'certificate' in s: return 'computation or formal certificate'
    if 'whole' in s or 'targeted' in s or ('proof' in s and ('read' in s or 'check' in s)): return 'targeted proof check'
    if 'background' in s: return 'carried as background without fault found'
    return 'used and rechecked in this run'

files=[root]+[p for p in sorted(work.glob('*checks.tsv')) if p!=root]
for p in files:
    with p.open(newline='') as f:
        for r in csv.DictReader(f,delimiter='\t'):
            if 'statement_id' in r:
                who=r.get('who_model_effort_run') or r.get('who','')
                if r.get('model'): who+='; '+r['model']+'; effort '+r.get('effort','not exposed')+'; run '+r.get('run','K17')
                orig=r.get('type','')
                scope=r.get('method_and_scope') or r.get('how','')
                rows.append([r['statement_id'],r.get('date','2026-11-21'),who,classify(orig),r.get('outcome',''),scope+' [Original event type: '+orig+'; evidence: '+p.name+']'])
            elif 'object' in r:
                who='; '.join([r.get('agent',''),r.get('model',''),'effort '+r.get('effort','not exposed'),'K17'])
                orig=r.get('check_type','')
                scope='; '.join(r.get(k,'') for k in ('scope','locator','notes'))
                rows.append([r['object'],r.get('date_utc','2026-11-21'),who,classify(orig),r.get('result',''),scope+' [Original event '+r.get('event_id','')+': '+orig+'; evidence: '+p.name+']'])
            elif 'finding_id' in r:
                who=r.get('reviewer','')+'; /root/archive_kummer; K17'
                orig=r.get('check_type','')
                scope=r.get('objects_checked','')+'; limitation: '+r.get('limitation','')
                rows.append([r['finding_id'],r.get('date_utc','2026-11-21'),who,classify(orig),r.get('result',''),scope+' [Original event type: '+orig+'; evidence: '+p.name+']'])
            else:
                raise ValueError('Unrecognized check-event schema: '+str(p))

unique=[]; seen=set()
for r in rows:
    t=tuple(r)
    if t not in seen: seen.add(t);unique.append(r)
with target.open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who_model_effort_run','type','outcome','method_and_scope']);w.writerows(unique)
print('Merged actual check events:',len(unique))

