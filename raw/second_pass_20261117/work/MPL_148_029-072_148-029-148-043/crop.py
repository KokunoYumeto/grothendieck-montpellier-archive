"""Crop helper for the second pass of block MPL_148_029-072_148-029-148-043.

Usage: python -I -B crop.py NAME "SPEC;SPEC;..."
  SPEC = scan,x0,y0,x1,y1[,rot[,scale[,m]]]
  scan: 3-digit scan number; x0..y1: fractions (0-1) of the whole page image;
  rot: degrees counter-clockwise; scale: enlargement factor; m: mirror horizontally.
Several specs are stacked vertically into one montage (with a thin separator), saved in this folder.
"""
import sys
import os
from PIL import Image, ImageOps, ImageDraw

IMG = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_148_029-072"
OUT = os.path.dirname(os.path.abspath(__file__))


def one(spec):
    p = [s.strip() for s in spec.split(",")]
    scan = p[0]
    x0, y0, x1, y1 = (float(v) for v in p[1:5])
    rot = float(p[5]) if len(p) > 5 and p[5] else 0.0
    scale = float(p[6]) if len(p) > 6 and p[6] else 1.0
    mirror = len(p) > 7 and p[7] == "m"
    im = Image.open(os.path.join(IMG, "MPL_148_029-072_148_scan%s.jpg" % scan))
    w, h = im.size
    c = im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))
    if mirror:
        c = ImageOps.mirror(c)
    if rot:
        c = c.rotate(rot, expand=True, fillcolor="white")
    if scale != 1.0:
        c = c.resize((max(1, int(c.size[0] * scale)), max(1, int(c.size[1] * scale))), Image.LANCZOS)
    return c.convert("RGB")


def main():
    name = sys.argv[1]
    specs = [s for s in sys.argv[2].split(";") if s.strip()]
    ims = [one(s) for s in specs]
    W = max(i.size[0] for i in ims)
    H = sum(i.size[1] for i in ims) + 6 * (len(ims) - 1)
    mont = Image.new("RGB", (W, H), "white")
    y = 0
    d = ImageDraw.Draw(mont)
    for i in ims:
        mont.paste(i, (0, y))
        y += i.size[1]
        if y < H:
            d.rectangle([0, y, W, y + 5], fill=(255, 0, 0))
        y += 6
    m = max(mont.size)
    if m > 2000:
        f = 2000.0 / m
        mont = mont.resize((int(mont.size[0] * f), int(mont.size[1] * f)), Image.LANCZOS)
    path = os.path.join(OUT, "%s.jpg" % name)
    mont.save(path, quality=92)
    print(path, mont.size)


if __name__ == "__main__":
    main()
