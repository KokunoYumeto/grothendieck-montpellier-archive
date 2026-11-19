"""Fetch the public cote 94 PDF; no OCR is performed."""
from pathlib import Path
from urllib.request import urlopen
from datetime import datetime, timezone
import hashlib

root = Path(__file__).resolve().parents[2]
target = root / 'sources' / 'montpellier_94.pdf'
url = 'https://grothendieck.umontpellier.fr/94.pdf'
with urlopen(url, timeout=50) as response:
    data = response.read()
if not data.startswith(b'%PDF'):
    raise ValueError('The response is not a PDF')
target.write_bytes(data)
print(datetime.now(timezone.utc).isoformat())
print(url)
print('bytes', len(data))
print('sha256', hashlib.sha256(data).hexdigest())
print('saved', target)
