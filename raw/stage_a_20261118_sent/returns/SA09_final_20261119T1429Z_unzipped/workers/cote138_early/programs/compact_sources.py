"""Keep reproducible retrieval metadata and own research conclusions, not redistributed full books."""
from pathlib import Path
import json,hashlib,re
W=Path(__file__).resolve().parents[1];O=W/'outputs'
records=[]
for name in ['EGAIV3.pdf','EGAIV3.txt','Schinzel1977.pdf','Schinzel1977.txt','IharaInvent1986.pdf','Schinzel1977_page-01.png','Schinzel1977_page-02.png','Schinzel1977_page-03.png']:
    p=O/name
    if p.exists():
        b=p.read_bytes();records.append({'filename':name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'retention':'Consulted source or failed retrieval removed from deliverable; results and limits recorded in reference_verification.md.'});p.unlink()
if records:(O/'source_materials.json').write_text(json.dumps(records,indent=2)+'\n')
for p in list(O.glob('web*.json'))+list(O.glob('search_batch_*.json')):
    d=json.loads(p.read_text())
    if 'result' not in d:continue
    result=d.pop('result');headers=[]
    for content in result.get('content',[]):
        if content.get('type')=='text':
            for line in content.get('text','').splitlines():
                if re.search(r'^.{1,300}\(https?://',line) or line.startswith('【'):
                    headers.append(line.split('[wordlim')[0].strip())
    d['retrieval_headers']=headers
    d['research_outcomes']='See search_log.tsv, source_attempts.tsv, reference_verification.md and references.bib for manually checked results and exact limits. Original third-party extracts are not redistributed.'
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'source_files_removed':len(records),'retrieval_metadata_compacted':True}))
