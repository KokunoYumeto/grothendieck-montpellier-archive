"""Enlarged crops of scan halves for the 102-119 second pass, stacked in one montage.

Usage: python -I -B crop102119.py OUTNAME spec [spec ...]
spec = scan:half:x0:y0:x1:y1[:scale[:rot]]   (half = a, b, or f for the whole page)
Crops and the montage are written next to this script.
"""
import os
import sys
from PIL import Image, ImageDraw, ImageOps

IMG = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_147_048-137/"
WORK = os.path.dirname(os.path.abspath(__file__)) + "/"
MAXW = 1600

out = sys.argv[1]
tiles = []
for spec in sys.argv[2:]:
    p = spec.split(":")
    scan, half = p[0], p[1]
    x0, y0, x1, y1 = map(int, p[2:6])
    scale = float(p[6]) if len(p) > 6 else 2.0
    rot = int(p[7]) if len(p) > 7 else 0
    suffix = "" if half == "f" else "_" + half
    im = Image.open(f"{IMG}MPL_147_048-137_scan{scan}{suffix}.jpg").convert("L")
    c = im.crop((x0, y0, x1, y1))
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255, resample=Image.BICUBIC)
    s = min(scale, MAXW / c.width)
    c = c.resize((max(1, int(c.width * s)), max(1, int(c.height * s))), Image.LANCZOS)
    c = ImageOps.autocontrast(c, cutoff=1)
    c.save(f"{WORK}s{scan}{half}_{x0}_{y0}_{x1}_{y1}_r{rot}.png")
    t = Image.new("L", (c.width, c.height + 20), 255)
    ImageDraw.Draw(t).text((4, 3), spec, fill=0)
    t.paste(c, (0, 20))
    tiles.append(t)

W = max(t.width for t in tiles)
H = sum(t.height + 6 for t in tiles)
m = Image.new("L", (W, H), 170)
y = 0
for t in tiles:
    m.paste(t, (0, y))
    y += t.height + 6
m.save(f"{WORK}{out}.png")
print(f"{WORK}{out}.png", m.size)
