"""Additional human-selected disputed loci. No OCR is used."""
from pathlib import Path
from PIL import Image
import csv

root = Path(__file__).resolve().parents[2]
out = root / 'OBJ_H035_work/readings'
items = [
    (5, 'singular_f_agreement', (240, 580, 1540, 780)),
    (6, 'singular_f_agreement', (300, 1570, 1650, 1760)),
    (8, 'egal_egale', (760, 780, 1490, 900)),
    (10, 'parameter_index', (1320, 130, 1660, 250)),
    (11, 'de_cancellation', (340, 1740, 760, 1880)),
    (13, 'expliciter_margin', (40, 1600, 340, 1870)),
]
with (out / 'CROP_MANIFEST.tsv').open('a') as stream:
    writer = csv.writer(stream, delimiter='\t')
    for scan, label, box in items:
        src = root / f'sources/OBJ_H035_scans/94_scan{scan:03d}.jpg'
        im = Image.open(src).crop(box)
        im = im.resize((im.width * 2, im.height * 2))
        dest = out / f'94_{scan:03d}_{label}.jpg'
        im.save(dest, quality=90)
        writer.writerow([dest.name, str(src.relative_to(root)), ','.join(map(str, box)), 2])
        print(dest.name, im.size)
