"""Crop, rotate and enlarge regions of the full-page scans of cote 150 (block 150-085..150-099).

Usage: python -I -B crops.py SCAN:X0:Y0:X1:Y1:ANGLE:SCALE:NAME [...]
Coordinates are in the full-page image (MPL_..._150_scanNNN.jpg). ANGLE is in degrees
(PIL convention: positive = counter-clockwise). Output: <this folder>/sNNN_NAME.png
"""
import os
import sys
from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "..", "..", "img", "MPL_150_085-099+151_001-031")

for spec in sys.argv[1:]:
    scan, x0, y0, x1, y1, ang, scale, name = spec.split(":")
    path = os.path.join(IMG, "MPL_150_085-099+151_001-031_150_scan%03d.jpg" % int(scan))
    im = Image.open(path).convert("L")
    c = im.crop((int(x0), int(y0), int(x1), int(y1)))
    a = float(ang)
    if a:
        c = c.rotate(a, resample=Image.BICUBIC, expand=True, fillcolor=255)
    s = float(scale)
    if s != 1:
        c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
    c = ImageOps.autocontrast(c, cutoff=1)
    out = os.path.join(HERE, "s%03d_%s.png" % (int(scan), name))
    c.save(out)
    print(out, c.size)


def stack(paths, out, maxw=1700):
    ims = [Image.open(p) for p in paths]
    ims = [i if i.width <= maxw else i.resize((maxw, int(i.height * maxw / i.width)), Image.LANCZOS) for i in ims]
    W = max(i.width for i in ims)
    H = sum(i.height for i in ims) + 12 * len(ims)
    canvas = Image.new("L", (W, H), 255)
    y = 0
    for i in ims:
        canvas.paste(i, (0, y))
        y += i.height
        canvas.paste(0, (0, y + 4, W, y + 8))
        y += 12
    canvas.save(out)
    print("stack", out, canvas.size)


if os.environ.get("STACK"):
    outs = []
    for spec in sys.argv[1:]:
        scan, *_rest, name = spec.split(":")
        outs.append(os.path.join(HERE, "s%03d_%s.png" % (int(scan), name)))
    stack(outs, os.path.join(HERE, os.environ["STACK"] + ".png"))
