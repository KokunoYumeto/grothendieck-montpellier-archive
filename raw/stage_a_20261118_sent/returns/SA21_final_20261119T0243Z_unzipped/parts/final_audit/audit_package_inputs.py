"""Inspect the packager's exclusion/redaction decisions without creating a ZIP.

Only metadata and potential-copy filenames are saved, never retrieved full text.
The packager is loaded without importing it, avoiding external __pycache__ edits.
"""
from pathlib import Path
import json,hashlib,collections

P=Path(__file__).parent;R=P.parents[1]
src=R/'code/package.py'
ns={'__name__':'package_policy_readonly_audit','__file__':str(src)}
exec(compile(src.read_text(),str(src),'exec'),ns)
excluded=[];sanitized=[];raw_json=[];retained_txt=[];total=0

def text_payloads(o,path=''):
    found=[]
    if isinstance(o,dict):
        for k,v in o.items():
            child=path+'.'+k
            if k in ['text','html','body','content'] and isinstance(v,str) and len(v)>500:
                found.append({'key_path':child,'characters':len(v)})
            else:found.extend(text_payloads(v,child))
    elif isinstance(o,list):
        for i,v in enumerate(o):found.extend(text_payloads(v,path+f'[{i}]'))
    return found

for f in sorted(R.rglob('*')):
    if not f.is_file() or P in f.parents:continue
    p=f.relative_to(R);b=f.read_bytes();total+=1
    rec={'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
    if ns['external_input'](p):excluded.append(rec);continue
    packed,redacted=ns['sanitize'](p,b)
    if redacted:sanitized.append(dict(rec,packed_bytes=len(packed)));continue
    if p.suffix=='.json':
        try:o=json.loads(b)
        except Exception:continue
        hits=text_payloads(o)
        if hits:raw_json.append(dict(rec,payload_fields=hits,top_keys=list(o) if isinstance(o,dict) else ['array']))
    if p.suffix=='.txt' and len(b)>2000:
        retained_txt.append(rec)

out={'scope':'Read-only dry-run of package.py decisions. Does not certify copyright status or full semantic absence of copied text.',
     'packager_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
     'files_inspected_excluding_audit_self':total,'excluded_count':len(excluded),
     'sanitized_count':len(sanitized),'retained_json_text_candidates':raw_json,
     'retained_large_text_files':retained_txt,'excluded':excluded,'sanitized':sanitized}
(P/'package_input_audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['excluded','sanitized']},ensure_ascii=False,indent=2))
