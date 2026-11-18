"""Stacked, enlarged crops for the second pass of MPL_149_001-090, scans 037-054.

usage: python -I -B crop149.py OUTNAME SPEC [SPEC ...]
SPEC = NNNh:x0,y0,x1,y1[:scale[:rot]]
  NNN = scan number, h = 'a' or 'b' (half image) or '' (whole page); coordinates in that image's pixels;
  scale default 2; rot in degrees counter-clockwise (applied before scaling).
Output: second_pass/work/MPL_149_001-090_037-054/OUTNAME.png
"""
import sys
from PIL import Image, ImageDraw, ImageOps

BASE = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/"
IMG = BASE + "img/MPL_149_001-090/MPL_149_001-090_scan{}{}.jpg"
OUT = BASE + "work/MPL_149_001-090_037-054/{}.png"

pieces = []
for spec in sys.argv[2:]:
    parts = spec.split(":")
    key = parts[0]
    n, h = key[:3], key[3:]
    box = tuple(int(v) for v in parts[1].split(","))
    scale = float(parts[2]) if len(parts) > 2 and parts[2] else 2.0
    rot = float(parts[3]) if len(parts) > 3 else 0.0
    im = Image.open(IMG.format(n, "_" + h if h else "")).convert("L")
    c = im.crop(box)
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255)
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c = ImageOps.autocontrast(c, cutoff=0.5)
    pieces.append((spec, c))

W = max(p.width for _, p in pieces)
H = sum(p.height + 24 for _, p in pieces)
canvas = Image.new("L", (W, H), 255)
d = ImageDraw.Draw(canvas)
y = 0
for spec, p in pieces:
    d.text((4, y + 4), spec, fill=0)
    y += 20
    canvas.paste(p, (0, y))
    y += p.height + 4
    d.line([(0, y - 2), (W, y - 2)], fill=128)
canvas.save(OUT.format(sys.argv[1]))
print(OUT.format(sys.argv[1]), canvas.size)
