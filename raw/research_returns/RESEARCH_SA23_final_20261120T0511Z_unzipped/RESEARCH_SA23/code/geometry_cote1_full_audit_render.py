"""Preserve full readable renders for date/correspondence inspection, physical25--72."""
from pathlib import Path
import hashlib
import json
import time
import fitz

root = Path(__file__).resolve().parents[1]
source = root / 'sources/root_manuscript1_ranged.pdf'
folder = root / 'notes/geometry_cote1_full'
folder.mkdir(exist_ok=True)
started = time.perf_counter()
doc = fitz.open(source)
files = []
for number in range(25, 73):
    page = doc[number - 1]
    scale = 1800 / page.rect.width
    target = folder / f'page_{number:03d}.jpg'
    page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False).pil_save(target, quality=94)
    files.append(str(target.relative_to(root)))
record = dict(source=str(source.relative_to(root)),
              sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
              physical_pages=list(range(25, 73)), width=1800,
              elapsed_seconds=time.perf_counter() - started, files=files)
(root / 'logs/geometry_cote1_full_audit_render.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({k: v for k, v in record.items() if k != 'files'}, indent=2))
