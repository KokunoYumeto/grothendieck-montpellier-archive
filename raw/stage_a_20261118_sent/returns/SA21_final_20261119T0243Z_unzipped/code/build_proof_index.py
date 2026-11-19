"""Index explicit proof/refinement headings; this is navigation, not proof checking."""
from pathlib import Path
import csv,json,re
R=Path(__file__).resolve().parents[1]
rows=[]
for p in R.rglob('*.md'):
    if not ('proof' in p.name or p.name=='formalism_and_checks.md'):continue
    for n,line in enumerate(p.read_text().splitlines(),1):
        if line.startswith('#'):
            for id in re.findall(r'R-SA21-[A-Za-z0-9-]+',line):
                rows.append({'statement_id':id,'file':str(p.relative_to(R)),'line':n,'heading':line.lstrip('# ')})
tail=R/'parts/cotes_9_14_18/refinements.json'
if tail.exists():
    text=tail.read_text();lines=text.splitlines()
    for x in json.loads(text):
        n=next(i for i,s in enumerate(lines,1) if '"id": "'+x['id']+'"' in s)
        rows.append({'statement_id':x['id'],'file':str(tail.relative_to(R)),'line':n,'heading':x['title']+'; source claims: '+', '.join(x['source_claim_ids'])})
with (R/'audit/proof_anchor_index.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','file','line','heading'],delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'explicit_named_proof_headings':len(rows)}))
