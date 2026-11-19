"""Remove provider search snippets retained inside metadata fields.

Preserve exact requests, URLs, reference IDs, dates, hashes and our authored
audit summary. Original JSONs are backed up outside the deliverable tree.
No mathematical verification status is inferred by this script.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT=Path('/workspace/scratch/208fb206de03')
BACKUP=ROOT/'external_cache/packaging_review_pre_sanitize'
changes=[]
for p in sorted((ROOT/'work').rglob('web_*.json')):
    raw=p.read_bytes()
    d=json.loads(raw)
    if not isinstance(d,dict) or not any(isinstance(x,dict) and 'reference_metadata' in x for x in d.get('sources',[])):
        continue
    relative=p.relative_to(ROOT)
    backup=BACKUP/relative
    backup.parent.mkdir(parents=True,exist_ok=True)
    assert not backup.exists(),str(backup)
    backup.write_bytes(raw)
    sha=hashlib.sha256(raw).hexdigest()
    sources=[]
    for old in d.get('sources',[]):
        header=old.get('header','')
        meta=old.get('reference_metadata','')
        urls=[]
        match=re.search(r'\((https?://.+)\)\s*$',header)
        if match: urls.append(match.group(1))
        refs=re.findall(r'【([^】]+)】',meta)
        source={'urls':urls,'reference_ids':refs}
        for field in ['Published','Crawled']:
            m=re.search(r'(?:^|[;\] ])'+field+r':\s*([^;]+);?',meta)
            if m: source[field.lower()+'_as_returned']=m.group(1).strip()
        sources.append(source)
    clean={k:d[k] for k in ['args','request','retrieval_date','raw_sha256','raw_cache_path','audit_summary'] if k in d}
    clean.update({'sources':sources,'retrieval_error_count':len(d.get('errors',[])),
                  'raw_body_in_deliverables':False,'provider_search_snippets_in_deliverables':False,
                  'pre_sanitation_sha256':sha,'pre_sanitation_external_cache':str(backup.relative_to(ROOT)),
                  'sanitation_note':'Provider search excerpts and reference_metadata bodies removed; exact original requests, URLs, reference IDs, dates and authored audit summary retained.'})
    p.write_text(json.dumps(clean,ensure_ascii=False,indent=2)+'\n')
    changes.append({'path':str(relative),'backup':str(backup.relative_to(ROOT)),
                    'before_sha256':sha,'after_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                    'sources_retained':len(sources),'bytes_before':len(raw),'bytes_after':p.stat().st_size})
result={'date':'2026-11-19','run':'SA16-2026-11-19-cote62','type':'packaging sanitation; no mathematical reclassification',
        'changed_files':changes,'count':len(changes),'raw_backups_excluded_from_final_zip':str(BACKUP.relative_to(ROOT)),
        'checks':{'reference_metadata_removed_from_touched_files':all('reference_metadata' not in json.loads((ROOT/x['path']).read_text()) for x in changes)}}
dest=ROOT/'work/outputs/web_metadata_sanitation_review.json'
dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'count':len(changes),'audit_output':str(dest.relative_to(ROOT)),
                  'bytes_removed':sum(x['bytes_before']-x['bytes_after'] for x in changes)}))
