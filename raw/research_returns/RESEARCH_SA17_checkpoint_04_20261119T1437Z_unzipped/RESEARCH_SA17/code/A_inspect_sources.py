#!/usr/bin/env python3
"""Render exact manuscript scans for visual inspection; no OCR conclusions."""
from pathlib import Path
from datetime import datetime, timezone
import fitz,json,time
root=Path(__file__).resolve().parents[1]
ext=root.parent/'external_sources'
start=time.perf_counter()
with fitz.open(ext/'131.pdf') as pdf:
    out=ext/'scan131';out.mkdir(exist_ok=True)
    scans=[2,14,16,17,35,37,39,41]
    for n in scans:
        pdf[n-1].get_pixmap(matrix=fitz.Matrix(1.6,1.6)).save(out/f'scan{n:03d}.png')
    record={'source':'https://grothendieck.umontpellier.fr/131.pdf','scans_rendered':scans,
       'pdf_pages':len(pdf),'utc':datetime.now(timezone.utc).isoformat(),
       'seconds':time.perf_counter()-start}
    (root/'logs/A_manuscript_renders.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record))
