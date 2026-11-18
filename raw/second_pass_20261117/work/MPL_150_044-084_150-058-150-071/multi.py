"""Stack several enlarged crops of one or more scans into a single image.

Usage: python -I -B multi.py OUTNAME SCAN:x0,y0,x1,y1[:scale[:rot]] [SCAN:...] ...
Coordinates are in the full-page image (MPL_150_044-084_150_scanNNN.jpg).
Each crop is labelled with its scan and box. Output goes to this folder only.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "..", "..", "img", "MPL_150_044-084")
MAXW = 1900


def one(spec):
    parts = spec.split(":")
    scan = parts[0].zfill(3)
    x0, y0, x1, y1 = (int(v) for v in parts[1].split(","))
    scale = float(parts[2]) if len(parts) > 2 and parts[2] else 2.0
    rot = float(parts[3]) if len(parts) > 3 and parts[3] else 0.0
    im = Image.open(os.path.join(IMG, f"MPL_150_044-084_150_scan{scan}.jpg")).convert("L")
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((max(1, int(c.width * scale)), max(1, int(c.height * scale))), Image.LANCZOS)
    c = ImageOps.autocontrast(c, cutoff=1)
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255)
    if c.width > MAXW:
        r = MAXW / c.width
        c = c.resize((MAXW, int(c.height * r)), Image.LANCZOS)
    return f"{scan} [{x0},{y0},{x1},{y1}] x{scale} r{rot}", c


def main():
    name = sys.argv[1]
    tiles = [one(s) for s in sys.argv[2:]]
    w = max(t.width for _, t in tiles)
    h = sum(t.height + 22 for _, t in tiles)
    out = Image.new("L", (w, h), 255)
    d = ImageDraw.Draw(out)
    y = 0
    for label, t in tiles:
        d.rectangle((0, y, w, y + 20), fill=200)
        d.text((4, y + 4), label, fill=0)
        out.paste(t, (0, y + 22))
        y += t.height + 22
    p = os.path.join(HERE, name + ".png")
    out.save(p)
    print(p, out.size)


if __name__ == "__main__":
    main()
