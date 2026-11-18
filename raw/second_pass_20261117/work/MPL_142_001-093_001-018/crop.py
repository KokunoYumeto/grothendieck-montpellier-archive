"""Crop and enlarge regions of the full-page scans and stack them in one montage.

Usage: python -I -B crop.py OUT.png SPEC [SPEC ...]
SPEC = NNN:x0,y0,x1,y1[:scale[:rot]]   coordinates in full-page pixels of scanNNN.jpg
"""
import sys
from PIL import Image, ImageDraw

IMG = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_142_001-093/MPL_142_001-093_scan%03d.jpg"
MAXW = 1700


def one(spec):
    parts = spec.split(":")
    n = int(parts[0])
    x0, y0, x1, y1 = [int(v) for v in parts[1].split(",")]
    scale = float(parts[2]) if len(parts) > 2 and parts[2] else 2.5
    rot = float(parts[3]) if len(parts) > 3 else 0.0
    im = Image.open(IMG % n).convert("L")
    c = im.crop((x0, y0, x1, y1))
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255, resample=Image.BICUBIC)
    w, h = c.size
    s = min(scale, MAXW / w)
    c = c.resize((max(1, int(w * s)), max(1, int(h * s))), Image.LANCZOS)
    lab = Image.new("L", (c.size[0], 22), 200)
    ImageDraw.Draw(lab).text((4, 4), spec, fill=0)
    out = Image.new("L", (c.size[0], c.size[1] + 22), 255)
    out.paste(lab, (0, 0))
    out.paste(c, (0, 22))
    return out


def main():
    out = sys.argv[1]
    tiles = [one(s) for s in sys.argv[2:]]
    W = max(t.size[0] for t in tiles)
    H = sum(t.size[1] + 8 for t in tiles)
    m = Image.new("L", (W, H), 120)
    y = 0
    for t in tiles:
        m.paste(t, (0, y))
        y += t.size[1] + 8
    m.save(out)
    print(out, m.size)


main()
