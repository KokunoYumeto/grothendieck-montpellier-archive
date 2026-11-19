"""Retain targeted retrieval provenance without unrelated personal-file excerpts."""
import hashlib,json
from pathlib import Path
D=Path(__file__).resolve().parents[1]
rows=[]
for p in sorted((D/'evidence').glob('external_project_library_search_*.json')):
    raw=p.read_bytes();x=json.loads(raw)
    if x.get('sanitized'):continue
    r=x['response']
    matches=[dict(name=z.get('name'),library_file_id=z.get('library_file_id'),
                  selected=False,reason='No exact named research-run endpoint was resolved from this candidate.')
             for z in r.get('results',[])]
    out=dict(sanitized=True,request=x['request'],raw_response_sha256=hashlib.sha256(raw).hexdigest(),
             candidate_metadata=matches,warnings=r.get('warnings',[]),
             conclusion='These searches did not resolve the original LM7,LM6,FLAGGED_149 orWG2 endpoint texts. Fuzzy matches to unrelated prompts and research papers were not read or used as mathematical evidence. This is an access/retrieval boundary, not proof that the requested files do not exist.')
    p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    rows.append({'file':p.name,'candidates':len(matches),'selected':0})
print(json.dumps(rows,indent=2))
