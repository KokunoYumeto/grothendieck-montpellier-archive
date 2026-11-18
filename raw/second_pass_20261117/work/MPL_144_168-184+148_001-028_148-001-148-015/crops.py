"""Crop, enlarge and rotate regions of the block's full-page scans; stack them in one montage.

Usage: python -I crops.py SPECFILE OUTNAME
Each spec line: scan x0 y0 x1 y1 scale rot [label]
  scan  = three-digit scan number of cote 148 (full-page image coordinates)
  scale = enlargement factor, rot = degrees counter-clockwise
"""
import sys
from PIL import Image, ImageDraw

IMG = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_144_168-184+148_001-028/MPL_144_168-184+148_001-028_148_scan{}.jpg"
OUT = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/work/MPL_144_168-184+148_001-028_148-001-148-015/"

spec, outname = sys.argv[1], sys.argv[2]
tiles = []
for line in open(spec, encoding="utf-8"):
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    parts = line.split()
    scan, x0, y0, x1, y1, scale, rot = parts[:7]
    label = " ".join(parts[7:]) or f"{scan} {x0},{y0}-{x1},{y1}"
    im = Image.open(IMG.format(scan)).convert("L")
    c = im.crop((int(x0), int(y0), int(x1), int(y1)))
    s = float(scale)
    c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
    r = float(rot)
    if r:
        c = c.rotate(r, expand=True, fillcolor=255)
    tiles.append((label, c))

W = max(t.width for _, t in tiles) + 10
H = sum(t.height + 22 for _, t in tiles)
m = Image.new("L", (W, H), 255)
d = ImageDraw.Draw(m)
y = 0
for label, t in tiles:
    d.text((4, y + 4), label, fill=0)
    y += 18
    m.paste(t, (5, y))
    y += t.height + 4
    d.line((0, y, W, y), fill=128)
m.save(OUT + outname)
print(OUT + outname, m.size)
