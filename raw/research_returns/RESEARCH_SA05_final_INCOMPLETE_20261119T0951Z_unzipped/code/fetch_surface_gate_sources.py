"""Reproduce primary-source retrieval for the scoped B3 surface reduction."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / 'primary_sources/root_surface_gate'
TARGET.mkdir(parents=True, exist_ok=True)
sources = [
    ('Kahn2023Divisors.pdf', 'https://webusers.imj-prg.fr/~bruno.kahn/preprints/Tate-pour-les-diviseurs-ENT.pdf'),
    ('Morrow2019Variational.pdf', 'https://www.imo.universite-paris-saclay.fr/~matthew.morrow/Morrow,%20M.,%20Variational%20Tate.pdf'),
]
records = []
for filename, url in sources:
    start = time.monotonic()
    try:
        with urllib.request.urlopen(url, timeout=40) as response:
            data = response.read()
        if not data.startswith(b'%PDF'):
            raise ValueError('Response is not a PDF')
        (TARGET / filename).write_bytes(data)
        records.append(dict(file=str((TARGET/filename).relative_to(ROOT)), url=url,
                            status='downloaded', bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                            seconds=round(time.monotonic()-start, 6)))
    except Exception as error:
        records.append(dict(file=filename, url=url, status='failed', error=str(error),
                            seconds=round(time.monotonic()-start, 6)))
result = {'retrieved_at': datetime.now(timezone.utc).isoformat(), 'sources': records,
          'scope': 'Retrieval only; exact theorem statements and proofs were separately read. Source PDFs are excluded from deliverable archives.'}
(ROOT / 'code/fetch_surface_gate_sources_output.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
