"""Serialize root-approved p3/p4 semantic decisions, after reading both audits."""
from pathlib import Path
import json,csv
R=Path(__file__).resolve().parents[2];D=R/'deliverable'
p=D/'shards/p3/cross_package_merge_map.tsv';rows=list(csv.DictReader(p.open(),delimiter='\t'))
out=[]
for r in rows:
 if r['action'] not in ['merge item','merge problem']:continue
 out.append({'kind':r['action'].split()[1],'from':r['old_id'],'canonical':r['canonical_id'],'reason':r['evidence']+' Preserve: '+r['preserve'],'source_entries':r['source_entries'].split(';'),'status':'accepted by root after reading cross_package_audit.md'})
(D/'shards/p3/cross_package_merge_map.json').write_text(json.dumps({'merges':out,'canonical_patches':{'SA13-327':{'title':'Rigidified torsors, extension laws and biextensions'},'MP-SA13-134':{'title':'Primitive torsors, the generalized NS quotient and the doubled Picard extension'}}},ensure_ascii=False,indent=2)+'\n')
print('Recorded4item aliases and1problem alias; no claim aliases. Occurrence/dependency additions are explicit in assemble.py.')
