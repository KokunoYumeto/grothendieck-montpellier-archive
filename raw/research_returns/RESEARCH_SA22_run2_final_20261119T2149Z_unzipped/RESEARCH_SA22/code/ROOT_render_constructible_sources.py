#!/usr/bin/env python3
"""Render the exact primary pages used in the constructible-category audit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
import fitz

root = Path(__file__).resolve().parents[1]
records = []
for stem, pages in [('ROOT_Olivier1968', [3, 4, 5]),
                    ('ROOT_Olivier1978', [2, 3, 4]),
                    ('ROOT_Ferrand2003', [29])]:
    path = root / 'literature' / (stem + '.pdf')
    doc = fitz.open(path)
    for page in pages:
        target = root / 'qa' / (stem + '_' + str(page) + '.png')
        doc[page - 1].get_pixmap(matrix=fitz.Matrix(1.4, 1.4)).save(target)
        records.append({'source': str(path.relative_to(root)),
                        'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                        'pdf_page_1_based': page,
                        'image': str(target.relative_to(root))})
record = {'rendered_utc': datetime.now(timezone.utc).isoformat(),
          'scope': 'Source pages rendered for actual visual inspection; rendering alone is not reading or proof approval.',
          'pages': records}
(root / 'logs' / 'ROOT_constructible_source_render.json').write_text(
    json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(record, ensure_ascii=False, indent=2))
