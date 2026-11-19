#!/usr/bin/env python3
"""Keep execution provenance and opened-source locators, not copied articles."""
from pathlib import Path
import json,re
base=Path('/workspace/scratch/c38eb4e8f07f/SA18_work/parts/agent46/outputs')
for p in sorted(list(base.glob('search_*.json'))+list(base.glob('open_*.json'))):
    d=json.loads(p.read_text())
    if 'result' not in d: continue
    r=d.pop('result')
    records=[]
    for content in r.get('content',[]):
        if content.get('type')!='text': continue
        for part in content.get('text','').split('\n--------------------------------------------------------------------------------\n'):
            lines=part.strip().splitlines()
            if not lines: continue
            keep={'source_title_and_url':lines[0]}
            m=re.search(r'【([^】]+)】',part)
            if m:keep['ref_id']=m.group(1)
            m=re.search(r'Source: (.*?)(?:; Total lines:|$)',part,re.M)
            if m:keep['opened_locator']=m.group(1)
            m=re.search(r'Total lines: (\d+)',part)
            if m:keep['total_lines']=int(m.group(1))
            m=re.search(r'Number of pages: (\d+)',part)
            if m:keep['pdf_pages']=int(m.group(1))
            m=re.search(r'Failed to fetch ([^\n]+)',part)
            if m:keep['error']=m.group(1)
            keep['returned_line_locators']=re.findall(r'^(L\d+(?:@P\d+(?:-\d+)?)?):',part,re.M)
            records.append(keep)
    d['retrieval_metadata']=records
    d['retention_note']='Tool call and source locators retained; long copied source text intentionally omitted. Own assessments are in literature_search.tsv and the claims.'
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    print(p.name, len(records))
