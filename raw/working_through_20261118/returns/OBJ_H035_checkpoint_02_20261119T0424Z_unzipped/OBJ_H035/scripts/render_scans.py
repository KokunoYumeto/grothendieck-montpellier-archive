"""Render additional manuscript scans and make explicitly requested crops.

Rendering/cropping only; this program performs no text recognition.
"""
from pathlib import Path
import subprocess
from PIL import Image, ImageEnhance, ImageFilter

root = Path(__file__).resolve().parents[2]
out = root / 'sources' / 'additional_scans'
out.mkdir(exist_ok=True)
subprocess.run(['pdftoppm', '-f', '15', '-l', '24', '-scale-to', '2300',
                '-jpeg', '-jpegopt', 'quality=92',
                str(root / 'sources' / 'montpellier_94.pdf'), str(out / '94_scan')], check=True)
for p in sorted(out.glob('*.jpg')):
    im = Image.open(p)
    print(p.name, im.size)

cropdir = root / 'OBJ_H035_work' / 'readings'
crops = [
    (3, 'completion', (190, 1420, 1660, 1645)),
    (6, 'lemma5_v', (310, 1585, 1665, 1760)),
    (8, 'remark5bis', (180, 70, 1660, 1160)),
    (10, 'tor_criterion', (150, 350, 1660, 1590)),
    (11, 'header_and_margin', (70, 30, 1660, 1570)),
    (13, 'cancelled_corollary', (150, 620, 1650, 2010)),
]
for scan, name, box in crops:
    src = root / 'sources' / 'OBJ_H035_scans' / f'94_scan{scan:03d}.jpg'
    im = Image.open(src).crop(box)
    im.resize((im.width * 2, im.height * 2), Image.Resampling.LANCZOS).save(cropdir / f'94_{scan:03d}_{name}.png')
    print('crop', scan, name, box)
