#!/usr/bin/env python3
"""Fetch the PDF advertised as public in an opened archive metadata record.

No authentication, encrypted lending file, private-file endpoint, alternate
host or restriction bypass is used.  A failed ordinary request is terminal.
"""
import hashlib
import json
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[1]
identifier = 'london-mathematical-society-proceedings_1931-1932_33'
metadata_path = root / ('sources/gabriel1932_' + identifier + '_metadata.json')
m = json.loads(metadata_path.read_text())
file_name = identifier + '.pdf'
f = next(f for f in m['files'] if f['name'] == file_name)
restricted_values = (True, 1, 'true', '1')
assert m.get('metadata', {}).get('access-restricted-item') not in restricted_values
assert m.get('is_dark') not in restricted_values
assert f.get('private') not in restricted_values
url = 'https://archive.org/download/' + identifier + '/' + file_name
start = time.perf_counter()
out = {'started_utc': datetime.now(timezone.utc).isoformat(), 'url': url, 'metadata_evidence': str(metadata_path.relative_to(root)), 'private_flag': f.get('private'), 'access_restricted_flag': m.get('metadata', {}).get('access-restricted-item')}
try:
    with urllib.request.urlopen(url, timeout=45) as r:
        out.update(status=r.status, final_url=r.url, content_type=r.headers.get('Content-Type'))
        content = r.read()
    out['bytes'] = len(content)
    if out['status'] == 200 and content.startswith(b'%PDF'):
        target = root/'sources/gabriel1932_volume33.pdf'
        target.write_bytes(content)
        out.update(saved=str(target.relative_to(root)), sha256=hashlib.sha256(content).hexdigest())
    else:
        out['action'] = 'Not a public PDF response; no content saved and no alternate access tried.'
except Exception as e:
    out.update(error=f'{type(e).__name__}: {e}', action='Ordinary public request failed; no alternate access attempted.')
out['runtime_seconds'] = time.perf_counter()-start
Path(__file__).with_name('part_c_gabriel_fetch_output.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
