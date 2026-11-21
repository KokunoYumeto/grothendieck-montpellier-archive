#!/usr/bin/env python3
"""Refresh hashes of this separate comparison audit; no uploads or root edits."""
from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

root = Path(__file__).resolve().parent
sources = {
    'primary/bellaiche_chenevier_arxiv.pdf': 'https://arxiv.org/pdf/math/0602340',
    'primary/urban_eisenstein_klingen_1998v1.pdf': 'https://arxiv.org/pdf/math/9803171v1',
    'primary/berger_klosin_hd32.pdf': 'https://kklosin.github.io/files/hd32.pdf',
    'primary/berger_klosin_onlifting21.pdf': 'https://kklosin.github.io/files/bergerklosinonlifting21.pdf',
    'primary/berger_klosin_2026_arxiv.pdf': 'https://arxiv.org/pdf/2611.19007v1',
    'primary/berger_klosin_2026_mirror.pdf': 'https://borowiecki.dev/pdf/2611.19007',
    'primary/berger_local_notes.pdf': 'https://perso.ens-lyon.fr/laurent.berger/autrestextes/barcelone.pdf',
}
items = []
for path in sorted(root.rglob('*')):
    if not path.is_file() or path.name == 'manifest.json' or 'build' in path.relative_to(root).parts:
        continue
    rel = path.relative_to(root).as_posix()
    data = path.read_bytes()
    item = {'path': rel, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
    if rel in sources:
        item['source_url'] = sources[rel]
    items.append(item)
report = {
    'verified_utc': datetime.now(timezone.utc).isoformat(),
    'model': 'GPT-6 Astra Pro',
    'effort': 'not exposed',
    'scope': 'Primary-source applicability audit, algebraic and local scope checks, and conditional ordinary rank-two source exclusion; the general strict Selmer gate remains open',
    'files': items,
}
(root / 'manifest.json').write_text(json.dumps(report, indent=2) + '\n')
(root / 'build').mkdir(exist_ok=True)
print(json.dumps({'files': len(items), 'manifest': str(root / 'manifest.json')}))
