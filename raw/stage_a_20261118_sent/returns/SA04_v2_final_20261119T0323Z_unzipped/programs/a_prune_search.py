"""Keep reproducible query/source metadata, not downloaded copyrighted excerpts.
User-provided manuscript extracts in outputs remain; external texts stay in /tmp.
"""
from pathlib import Path
import json,re,shutil
work=Path(__file__).resolve().parents[1]
dest=Path('/tmp/SA04_a_external/raw_search');dest.mkdir(parents=True,exist_ok=True)
records=[]
for path in sorted((work/'evidence').glob('a_web_*.json')):
    data=json.loads(path.read_text())
    result=data.get('result',data)
    sources=[]
    for block in result.get('content',[]):
        if block.get('type')!='text':continue
        for part in block['text'].split('\n--------------------------------------------------------------------------------\n'):
            lines=part.splitlines()
            # First two lines identify title, URL, tool reference and operation.
            sources.append('\n'.join(lines[:2]))
    records.append({'batch':path.name,'query':data.get('query',data.get('args',{})),'sources':sources})
    shutil.move(str(path),str(dest/path.name))
(work/'parts/a/search_capture_01_10.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
pdf=work/'evidence/a_Groth_ICM1970.pdf'
if pdf.exists():shutil.move(str(pdf),str(dest/pdf.name))
print(json.dumps({'metadata_batches':len(records),'external_excerpts_moved_outside_deliverable':True}))
