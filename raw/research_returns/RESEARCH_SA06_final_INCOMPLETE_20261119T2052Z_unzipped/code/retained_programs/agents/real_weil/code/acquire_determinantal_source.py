#!/usr/bin/env python3
"""Retain the exact author-authorized primary PDF and acquisition metadata."""
from pathlib import Path
from datetime import datetime, timezone
from time import perf_counter
from urllib.request import urlopen
from hashlib import sha256
import json

t=perf_counter()
base=Path(__file__).resolve().parents[1]
path=base.parents[1]/'sources'/'bruns_vetter1988_determinantal_rings.pdf'
url='https://www.home.uni-osnabrueck.de/wbruns/brunsw/detrings.pdf'
with urlopen(url,timeout=45) as response:
    data=response.read()
assert data.startswith(b'%PDF'), 'Response is not a PDF'
path.write_bytes(data)
record={'utc':datetime.now(timezone.utc).isoformat(),
        'url':url,'path':str(path),'bytes':len(data),
        'sha256':sha256(data).hexdigest(),
        'runtime_seconds':perf_counter()-t,
        'access_scope':'Full author-authorized 244-page PDF; source reading is separately recorded.'}
(base/'output'/'determinantal_source_manifest.json').write_text(
    json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
