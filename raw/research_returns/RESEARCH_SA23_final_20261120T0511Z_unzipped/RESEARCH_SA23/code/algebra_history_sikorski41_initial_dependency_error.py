"""Bounded public PAN inventory retrieval; no requests to private correspondence."""
import datetime, hashlib, json, pathlib, re, time, urllib.request
from bs4 import BeautifulSoup

base = pathlib.Path(__file__).resolve().parents[1]
start = time.monotonic()
url = 'https://archiwum.pan.pl/index.php?Itemid=208&catid=17&id=511:spis-inwentarzy&option=com_content&view=article'
out = {'utc_started': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'url': url, 'purpose': 'Read public finding-aid list and search Sikorski case-insensitively; this is not an examination of every archival unit.'}
try:
    with urllib.request.urlopen(url, timeout=25) as response:
        raw = response.read()
        out.update(http_status=response.status, final_url=response.url, content_type=response.headers.get('Content-Type'))
    html_path = base / 'sources/algebra_history_pan_inventory.html'
    html_path.write_bytes(raw)
    soup = BeautifulSoup(raw, 'html.parser')
    text = soup.get_text('\n', strip=True)
    (base / 'sources/algebra_history_pan_inventory.txt').write_text(text)
    out.update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest(), text_chars=len(text), source_path=str(html_path.relative_to(base)))
    out['sikorski_hits'] = [text[max(0,m.start()-150):m.end()+150] for m in re.finditer('sikors', text, re.I)]
    out['kuratowski_hits'] = [text[max(0,m.start()-150):m.end()+150] for m in re.finditer('kuratows', text, re.I)]
    out['mathematics_rows'] = [r.get_text(' | ', strip=True) for r in soup.find_all('tr') if re.search('matematy', r.get_text(' ', strip=True), re.I)]
except Exception as exc:
    out.update(error=repr(exc))
out['utc_completed'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
out['elapsed_seconds'] = time.monotonic() - start
payload = json.dumps(out, indent=2, ensure_ascii=False)
(base / 'logs/algebra_history_sikorski41.json').write_text(payload+'\n')
print(payload)
