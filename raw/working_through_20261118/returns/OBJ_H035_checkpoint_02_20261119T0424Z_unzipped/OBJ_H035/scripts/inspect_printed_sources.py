"""Locate and render decisive pages in printed sources (not archival OCR)."""
from pathlib import Path
import fitz

root = Path(__file__).resolve().parents[2]
out = root / 'OBJ_H035_work' / 'research' / 'printed_checks'
out.mkdir(exist_ok=True)
jobs = [
    ('EGA_III_1', ['Proposition (4.5.1)', 'Corollaire (4.5.2)']),
    ('Bourbaki_Topologie_5_10', ['PROPOSITION', 'valeurs absolues non']),
]
for name, needles in jobs:
    doc = fitz.open(root / 'sources' / 'literature' / (name + '.pdf'))
    hits = []
    for i, page in enumerate(doc):
        text = page.get_text()
        if name == 'EGA_III_1':
            match = any(s in text for s in needles)
        else:
            match = 'valeurs absolues non' in text and 'PROPOSITION' in text
        if match:
            hits.append(i)
    print(name, 'PDF page indices (zero based):', hits)
    for i in hits:
        target = out / f'{name}_{i+1:03}.png'
        doc[i].get_pixmap(matrix=fitz.Matrix(1.5, 1.5)).save(target)
        print(target.relative_to(root))
