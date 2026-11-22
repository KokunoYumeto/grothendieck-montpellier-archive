#!/usr/bin/env python3
"""Retain the exact official source and render the autoduality sign page."""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
from time import perf_counter
from urllib.request import urlopen

import fitz

root = Path(__file__).resolve().parents[1]
started = datetime.now(timezone.utc).isoformat()
t0 = perf_counter()
url = 'https://www.jmilne.org/math/xnotes/JVs.pdf'
with urlopen(url, timeout=30) as response:
    content = response.read()
if not content.startswith(b'%PDF'):
    raise RuntimeError('The primary URL did not return a PDF')
source = root / 'sources/milne2021_jacobian_varieties.pdf'
source.write_bytes(content)
doc = fitz.open(source)
page = doc[22]
render = root / 'rendered/milne2021_jacobian_sign_page23.png'
render.parent.mkdir(exist_ok=True)
page.get_pixmap(matrix=fitz.Matrix(1.6, 1.6), alpha=False).save(render)
record = {
    'started_utc': started,
    'completed_utc': datetime.now(timezone.utc).isoformat(),
    'runtime_seconds': perf_counter() - t0,
    'url': url,
    'source': str(source),
    'bytes': len(content),
    'sha256': sha256(content).hexdigest(),
    'pages': len(doc),
    'rendered_one_based_page': 23,
    'render': str(render),
    'scope': 'Acquisition and rendering only; source reading is recorded separately.',
}
(root / 'logs/milne2021_jacobian_sign_acquisition.json').write_text(
    json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
