"""Keep third-party retrieval bodies outside deliverables; retain exact request metadata."""
from pathlib import Path
import json,re,hashlib
P=Path(__file__).resolve().parents[1];cache=P.parents[2]/'external_cache/cote62/web_raw';cache.mkdir(parents=True,exist_ok=True)
count=0
for path in sorted((P/'outputs').glob('web_*.json')):
    data=json.loads(path.read_text())
    if 'result' not in data:continue
    raw=path.read_bytes();(cache/path.name).write_bytes(raw)
    sources=[];errors=[]
    for content in data['result'].get('content',[]):
        if content.get('type')!='text':continue
        for block in re.split(r'\n-{20,}\n',content.get('text','')):
            lines=block.strip().splitlines()
            if not lines:continue
            title=re.match(r'^(.*?) \((https?://[^\s]+)\)$',lines[0])
            refs=re.findall(r'【(turn\d+[A-Za-z]+\d+)】',block)
            if refs:
                sources.append(dict(title=title[1] if title else lines[0][:160],url=title[2] if title else None,ref_ids=list(dict.fromkeys(refs)),retrieval_date='2026-11-19'))
            for line in lines:
                if line.startswith(('Failed to fetch ','URL ')) or 'No matching text found' in line or line=='Internal Error ()':errors.append(line[:500])
    clean=dict(args=data['args'],retrieval_date='2026-11-19',sources=sources,errors=errors,raw_sha256=hashlib.sha256(raw).hexdigest(),raw_cache_path=str(cache/path.name),raw_body_in_deliverables=False,audit_summary='See the manually authored corresponding search_log.tsv row and claims.json for what the opened sources actually establish.')
    path.write_text(json.dumps(clean,ensure_ascii=False,indent=2)+'\n');count+=1
print('raw web bodies moved outside deliverables; metadata files prepared:',count)
