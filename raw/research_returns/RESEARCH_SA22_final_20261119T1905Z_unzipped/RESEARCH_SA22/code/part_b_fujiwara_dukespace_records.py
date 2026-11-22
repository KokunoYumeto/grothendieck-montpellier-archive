#!/usr/bin/env python3
"""Preserve compact metadata for one new route; raw source bodies remain outside.

This utility makes no network request and does not rerun the original searches.
"""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import time

start=time.monotonic()
root=Path(__file__).resolve().parents[1]
rawdir=root.parent/'source_reading/recorded_web_search'
records=[]
for key in ('part_b_fujiwara_dukespace_discovery','part_b_fujiwara_dukespace_home'):
    p=rawdir/(key+'_raw.json')
    raw=p.read_bytes(); data=json.loads(raw)
    sources=[]
    for block in data['result'].get('content',[]):
        if block.get('type')!='text': continue
        for segment in re.split(r'\n-{20,}\n',block.get('text','')):
            m=re.search(r'(?P<title>.+?)\s*\((?P<url>https?://[^\n]+)\)\s*\n【(?P<ref>[^】]+)】',segment)
            if m:
                sources.append({**m.groupdict(),'returned_block_sha256':sha256(segment.encode()).hexdigest(),
                                'source_body_retained_only_in':str(p)})
    records.append({'operation':key,'started_utc':data['started_utc'],
                    'elapsed_seconds':data['elapsed_seconds'],
                    'queries':data.get('queries'),'opened_url':data.get('url'),
                    'raw_record_path_outside_deliverable':str(p),
                    'raw_record_bytes':len(raw),'raw_record_sha256':sha256(raw).hexdigest(),
                    'sources':sources})
out={'recorded_at_utc':datetime.now(timezone.utc).isoformat(),
     'scope':'ONE distinct candidate route: public DukeSpace repository. Two targeted indexed queries and one homepage open. No target record, original file or preview located; not an exhaustive direct-repository search.',
     'new_search_queries':2,'new_open_commands':1,'direct_http_requests_by_this_utility':0,
     'original_mathematical_pages_obtained':0,'restricted_files_requested':0,
     'mathematical_programs_rerun':0,'records':records,
     'conclusion':'Fujiwara1995 relevant original remains NOT OPENED; no new credible advertised source link emerged.',
     'metadata_export_elapsed_seconds':time.monotonic()-start}
(root/'code/part_b_fujiwara_dukespace_output.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'record_count':len(records),'source_header_count':sum(len(x['sources']) for x in records),
                  'metadata_export_elapsed_seconds':out['metadata_export_elapsed_seconds']},indent=2))
