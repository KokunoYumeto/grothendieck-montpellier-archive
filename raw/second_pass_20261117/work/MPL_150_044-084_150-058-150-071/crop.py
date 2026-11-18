"""Crop, enlarge and optionally rotate a region of a full-page scan image.

Usage: python -I -B crop.py SCAN x0 y0 x1 y1 [scale] [rotate_degrees] [name]
Coordinates are in the full-page image (MPL_150_044-084_150_scanNNN.jpg).
Output goes to this folder only.
"""
import os
import sys

from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "..", "..", "img", "MPL_150_044-084")


def main():
    a = sys.argv[1:]
    scan = a[0].zfill(3)
    x0, y0, x1, y1 = (int(v) for v in a[1:5])
    scale = float(a[5]) if len(a) > 5 else 2.0
    rot = float(a[6]) if len(a) > 6 else 0.0
    name = a[7] if len(a) > 7 else f"s{scan}_{x0}_{y0}_{x1}_{y1}"
    src = os.path.join(IMG, f"MPL_150_044-084_150_scan{scan}.jpg")
    im = Image.open(src).convert("L")
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c = ImageOps.autocontrast(c, cutoff=1)
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255)
    out = os.path.join(HERE, name + ".png")
    c.save(out)
    print(out, c.size)


if __name__ == "__main__":
    main()
