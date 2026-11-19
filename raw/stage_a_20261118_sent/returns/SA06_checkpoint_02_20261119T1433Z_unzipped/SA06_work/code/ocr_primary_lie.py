#!/usr/bin/env python3
"""Read selected published-book pages; no manuscript OCR or transcription edits."""
from pathlib import Path
import fitz, subprocess, json, concurrent.futures, os
base=Path(__file__).resolve().parents[1]
cache=base/'cache_sources'; out=base/'research'
pdf=cache/'HumphreysLie.pdf'
pages=list(range(28,42))+list(range(78,86))
doc=fitz.open(pdf)
for printed in pages:
    name=cache/f'HumphreysLie_p{printed}.png'
    if not name.exists(): doc[printed+11].get_pixmap(matrix=fitz.Matrix(2,2)).save(name)
def one(printed):
    name=cache/f'HumphreysLie_p{printed}.png'
    env=dict(os.environ, OMP_THREAD_LIMIT='1')
    t=subprocess.run(['tesseract',str(name),'stdout','--psm','3'],capture_output=True,text=True,check=True,timeout=45,env=env).stdout
    (cache/f'HumphreysLie_p{printed}.txt').write_text(t)
    return {'printed':printed,'pdf_page_1_based':printed+12,'characters':len(t),'image':str(name)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
    rows=list(ex.map(one,pages))
(out/'Humphreys_primary_read_manifest.json').write_text(json.dumps(rows,indent=2))
print(json.dumps(rows,indent=2))
