"""Inspect public Math-Net archive HTML for the original 1959 Lidskii paper."""
from pathlib import Path
from time import perf_counter
from urllib.request import urlopen
from html import unescape
import re

base = Path(__file__).resolve().parents[1]
url = 'https://www.mathnet.ru/php/archive.phtml?jrnid=dan&option_lang=rus&wshow=contents'
start = perf_counter()
with urlopen(url, timeout=45) as response:
    raw = response.read()
out = base / 'notes' / 'geometry_mathnet_archive.html'
out.write_bytes(raw)
document = raw.decode('windows-1251')
print('public_source', url, 'bytes', len(raw))
for hit in re.finditer(r'125', document):
    context = document[max(0,hit.start()-500):hit.end()+3500]
    if '1959' not in context:
        continue
    print('context', unescape(re.sub(r'<[^>]+>', ' ', context)))
    for href, label in re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', context, re.S|re.I):
        print(unescape(re.sub(r'<[^>]+>', ' ', label)), unescape(href))
print('elapsed_seconds', round(perf_counter() - start, 3))
