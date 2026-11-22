"""Render four existing manuscript scans for a definition-scope audit; no math test."""
from pathlib import Path
import json, time
import fitz
base=Path(__file__).resolve().parents[1]
started=time.perf_counter()
doc=fitz.open(base/'sources/cote67.pdf')
folder=base/'notes/original_scans_a567'
folder.mkdir(exist_ok=True)
pages=[79,80,81,82]
paths=[]
for page in pages:
    path=folder/f'a1_scope_67_{page:03d}.png'
    doc[page-1].get_pixmap(matrix=fitz.Matrix(1.3,1.3)).save(path)
    paths.append(str(path.relative_to(base)))
out={'scope':'Render existing official cote67 physical PDF pages79-82, whose physical page numbers equal transcription scan numbers. No network or mathematical computation.','pages':pages,'paths':paths,'wall_seconds':time.perf_counter()-started}
(base/'code/part_a567_a1_scope_scan_read_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
