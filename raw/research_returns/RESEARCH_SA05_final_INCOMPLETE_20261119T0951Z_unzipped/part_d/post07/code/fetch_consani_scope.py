"""Capture the exact primary version consulted for the C6 reverse-route audit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
from urllib.request import Request, urlopen

work = Path(__file__).resolve().parents[1]
raw = work.parents[2] / 'pending_post07_sources_d'
raw.mkdir(exist_ok=True)
(work / 'sources').mkdir(exist_ok=True)
(work / 'output').mkdir(exist_ok=True)
url = 'https://arxiv.org/pdf/math/9801080'
record = {'url': url, 'checked_utc': datetime.now(timezone.utc).isoformat()}
try:
    request = Request(url, headers={'User-Agent': 'Research source audit'})
    with urlopen(request, timeout=45) as response:
        content = response.read()
    if not content.startswith(b'%PDF'):
        raise ValueError('Response is not a PDF')
    pdf = raw / 'Consani1998LocalMonodromy.pdf'
    pdf.write_bytes(content)
    txt = work / 'sources' / 'Consani1998LocalMonodromy.txt'
    subprocess.run(['pdftotext', '-layout', str(pdf), str(txt)], check=True)
    record.update(status='obtained', bytes=len(content),
                  sha256=hashlib.sha256(content).hexdigest(),
                  retained_text=str(txt.relative_to(work)),
                  read_scope='Introduction pp1-3; statements of Theorems4.2,5.3,6.2. No full theorem proof audit.')
except Exception as exc:
    record.update(status='not_obtained', error=repr(exc))
(work / 'output' / 'consani_scope_fetch_output.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
