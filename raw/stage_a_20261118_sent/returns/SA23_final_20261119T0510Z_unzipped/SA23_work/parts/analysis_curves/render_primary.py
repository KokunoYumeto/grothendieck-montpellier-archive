"""Render image-only primary passages for visual verification; cache stays external."""
from pathlib import Path
import fitz
root=Path(__file__).resolve().parents[3]
cache=root/'sources/external/analysis_curves'
doc=fitz.open(cache/'GrothPTT1955.pdf')
for physical in [214,221,222]:
 out=cache/f'GrothPTT1955_physical_{physical}.png'
 if not out.exists():doc[physical-1].get_pixmap(matrix=fitz.Matrix(2,2)).save(out)
 print(f'physical {physical}: {out}',flush=True)
