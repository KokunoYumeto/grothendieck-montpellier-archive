"""Retrieve the publisher-advertised public PDF and render interview endpoints."""
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import urlparse
import hashlib, json, subprocess, urllib.request

ROOT = Path(__file__).resolve().parents[1]
url = 'https://spartacus-idh.com/pdfs/008/978-2-36693-008-5.pdf'
row = {'url': url, 'started_utc': datetime.now(timezone.utc).isoformat()}
class SameHostRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if urlparse(newurl).hostname != 'spartacus-idh.com':
            raise ValueError('Unadvertised redirect host')
        return super().redirect_request(req, fp, code, msg, headers, newurl)
try:
    with urllib.request.build_opener(SameHostRedirect).open(url, timeout=35) as r:
        data = r.read()
        row.update(status=r.status, final_url=r.url)
    if not data.startswith(b'%PDF'): raise ValueError('Not a PDF')
    pdf = ROOT / 'sources/category_schwartz_dialogues2015.pdf'
    pdf.write_bytes(data)
    row.update(path=str(pdf.relative_to(ROOT)), bytes=len(data),
               sha256=hashlib.sha256(data).hexdigest())
    info = subprocess.run(['pdfinfo', str(pdf)], capture_output=True, timeout=20)
    row['pdfinfo'] = info.stdout.decode(errors='replace')
    row['pdfinfo_returncode'] = info.returncode
    directory = ROOT / 'sources/category_schwartz_dialogues2015_pages'
    directory.mkdir(exist_ok=True)
    row['renders'] = []
    for page in [4, 13, 16]:
        prefix = directory / f'page_{page:03d}'
        cmd = ['pdftoppm', '-f', str(page), '-l', str(page), '-singlefile',
               '-scale-to', '2200', '-png', str(pdf), str(prefix)]
        p = subprocess.run(cmd, capture_output=True, timeout=35)
        image = prefix.with_suffix('.png')
        render = {'command': cmd, 'returncode': p.returncode,
                  'stderr': p.stderr.decode(errors='replace')}
        if image.exists():
            render.update(path=str(image.relative_to(ROOT)),
                          sha256=hashlib.sha256(image.read_bytes()).hexdigest())
        row['renders'].append(render)
except Exception as error:
    row['error'] = repr(error)
row['finished_utc'] = datetime.now(timezone.utc).isoformat()
(ROOT / 'logs/category_schwartz_dialogues_fetch.json').write_text(
    json.dumps(row, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(row, ensure_ascii=False, indent=2))
