"""Inspect the public IHES archive's complete GABBER-tag catalogue."""
import datetime
import hashlib
import html
import json
import pathlib
import re
import time
import urllib.parse
import urllib.request

root = pathlib.Path(__file__).resolve().parents[1]
url = 'https://archives.ihes.fr/items/browse?sort_field=Dublin+Core%2CCreator&tags=GABBER'
start = time.perf_counter()
with urllib.request.urlopen(url, timeout=35) as response:
    raw = response.read()
    status = response.status
    final_url = response.url
text = raw.decode('utf-8', errors='replace')
records = []
for block in re.findall(r'<h2\b[^>]*>(.*?)</h2>', text, re.S | re.I):
    links = re.findall(r'<a\b[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', block, re.S | re.I)
    for href, title in links:
        records.append({'title': html.unescape(re.sub('<[^>]+>', '', title)).strip(),
                        'url': urllib.parse.urljoin(final_url, html.unescape(href))})
pagination = []
for href, title in re.findall(r'<a\b[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', text, re.S | re.I):
    if 'page=' in href:
        pagination.append({'title': html.unescape(re.sub('<[^>]+>', '', title)).strip(),
                           'url': urllib.parse.urljoin(final_url, html.unescape(href))})
data = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'url': url, 'status': status, 'final_url': final_url,
        'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
        'records': records, 'pagination': pagination,
        'advertised_total': re.findall(r'Parcourir les contenus[^<]*', text),
        'elapsed_seconds': time.perf_counter() - start}
path = root / 'logs' / 'B_IHES_Gabber_tag.json'
path.write_text(json.dumps(data, ensure_ascii=False, indent=2))
print(json.dumps(data, ensure_ascii=False, indent=2))
