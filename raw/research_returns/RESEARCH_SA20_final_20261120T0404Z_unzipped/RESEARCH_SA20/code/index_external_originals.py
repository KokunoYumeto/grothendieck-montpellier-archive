#!/usr/bin/env python3
"""Record fetched original-text identities without republishing whole works."""
from pathlib import Path
import hashlib, json

root = Path(__file__).resolve().parents[1]
names = [
    'baro_otero2008v1.txt', 'burghelea1976.txt', 'cerf1970.txt',
    'cerf_cartan1962.txt', 'galvin_nonino2025.txt',
    'kirby_siebenmann1977.txt', 'kuiper_lashof1966II.txt',
    'laudenbach1974.txt', 'mccullough_reducible.txt', 'negami1981.txt',
    'blr1975_ch3_preview.txt', 'orson_powell_randal_williams_current.txt'
]
items = []
for name in names:
    p = root / 'agents/singularities_duality/logs' / name
    if p.exists():
        data = p.read_bytes()
        items.append({'path': str(p.relative_to(root)), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest(),
            'kind': 'fetched original text or original preview, not an authored research output'})
record = {'policy': 'The research package retains source locators, exact-page audits, mathematical derivations and computational evidence. Fetched whole-source text copies are identified here and kept locally for consultation, rather than republished in subsequent deliverables.',
          'excluded_from_archive': items}
(root / 'notes/external_originals_manifest.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'original_texts_indexed': len(items), 'bytes': sum(i['bytes'] for i in items)}))
