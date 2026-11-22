"""Audit the evidential limits of the completed public journal OCR search.

This is an offline source-discovery audit, not a mathematical certificate.
No requests are made and no full-text absence is inferred from bad OCR.
"""
from pathlib import Path
import json
import re
import time

ROOT = Path(__file__).resolve().parents[1]
started = time.perf_counter()
data = json.loads((ROOT / 'code/root_pfluger_public_ocr_inventory_output.json').read_text())
rows = []
for row in data['results']:
    front = row.get('frontmatter', '')
    alpha = sum(c.isalpha() for c in front)
    tamil = sum('\u0b80' <= c <= '\u0bff' for c in front)
    rows.append(dict(identifier=row['identifier'], downloaded='error' not in row,
                     front_alphabetic_characters=alpha,
                     front_tamil_codepoints=tamil,
                     suspect_ocr=tamil > 50,
                     ascii_year_tokens=sorted(set(re.findall(r'\b19[0-9]{2}\b', front))),
                     title=row.get('title'), matches=row.get('matched_terms'),
                     error=row.get('error')))
delta = []
for row in data['excluded']:
    if row['reason'] != 'no previously saved full metadata':
        continue
    path = ROOT / 'sources' / ('pfluger_delta_' + row['identifier'] + '.json')
    if not path.exists():
        delta.append(dict(identifier=row['identifier'], status='not found'))
        continue
    meta = json.loads(path.read_text()).get('metadata', {})
    delta.append(dict(identifier=row['identifier'], status='earlier metadata saved under delta prefix',
                      title=meta.get('title'), date=meta.get('date'), year=meta.get('year')))
out = dict(attempted=len(rows), downloaded=sum(r['downloaded'] for r in rows),
           errors=sum(not r['downloaded'] for r in rows),
           suspect_ocr=sum(r['suspect_ocr'] for r in rows),
           title_or_author_matching_files=sum(bool(r['matches']) for r in rows),
           qualification='No match is not absence evidence for misrecognized OCR. Year tokens are diagnostic only.',
           inventory_omission='Ten metadata records were saved under a different prefix and thus excluded by the initial OCR script. Their catalogue scope is recorded here. The ambiguous volume XVIII was already read as the 1931 conference.',
           rows=rows, alternate_metadata=delta, seconds=time.perf_counter()-started)
(ROOT / 'code/root_pfluger_ocr_quality_audit_output.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('rows','alternate_metadata')}, indent=2))
