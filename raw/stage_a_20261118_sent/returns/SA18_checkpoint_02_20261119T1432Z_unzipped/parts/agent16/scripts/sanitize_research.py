"""Keep factual request/source audit; remove copied public-source extracts and image binaries.
This script extracts metadata only. It never decides mathematical status or source matches.
"""
from pathlib import Path
import json,re
O=Path(__file__).resolve().parents[1]
total=0
for p in sorted((O/'research').glob('web_*.json')):
    d=json.loads(p.read_text())
    if 'result' not in d:continue
    refs=[]
    for c in d['result'].get('content',[]):
        if c.get('type')=='text':
            for block in c.get('text','').split('\n--------------------------------------------------------------------------------\n'):
                rid=re.search(r'【([^】]+)】',block)
                header=block.split('【')[0].strip()
                urls=re.findall(r'https?://[^\s)]+',header)
                if rid:
                    err=next((ln.strip() for ln in block.splitlines() if any(s in ln for s in ['Failed to fetch','not accessible via this tool','No matching text found','Content length is too large'])),None)
                    refs.append({'ref_id':rid.group(1),'source_header':header[:1200],'url':urls[-1] if urls else None,'access_result':err or 'Tool returned source metadata/content; mathematical matching is separately authored in claims and literature_search.tsv.'})
    d={'request':d.get('request',{}),'source_results':refs,'audit_note':'Public-source body excerpts removed. This preserves actual requests, returned source IDs, URLs and access results. Manual source matches, locators and conclusions are in the dossier.'}
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');total+=1
print(json.dumps({'logs_sanitized':total,'body_extracts_retained':0}))
