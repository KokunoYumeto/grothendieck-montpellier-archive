#!/usr/bin/env python3
"""Render selected external-source pages for reading; caches excluded from deliverable ZIP."""
import fitz,sys
from pathlib import Path
O=Path(__file__).resolve().parent/'cache_sources'; O.mkdir(exist_ok=True)
source=Path(sys.argv[1]);stem=sys.argv[2]
with fitz.open(source) as doc:
 for n in map(int,sys.argv[3:]):
  out=O/f'{stem}-{n}.png';doc[n-1].get_pixmap(matrix=fitz.Matrix(1.6,1.6)).save(out)
  print(f'{source.name} PDFpage{n} -> {out.name}')
