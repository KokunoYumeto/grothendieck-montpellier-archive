"""Crop and enlarge regions of the full-page scans of block MPL_151_032-075_151-062-151-075.

Usage: python -I -B crops.py OUTNAME SCAN x0 y0 x1 y1 SCALE [ROT] -- SCAN x0 y0 x1 y1 SCALE [ROT] -- ...
Coordinates are in pixels of the whole-page image (about 1690 x 2360).
ROT is a rotation in degrees (counter-clockwise), default 0.
All crops of one call are stacked vertically into one montage OUTNAME.png, each with a numbered label,
and also saved one by one as OUTNAME_k.png.
"""
import sys
import os
from PIL import Image, ImageOps, ImageDraw

IMG = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_151_032-075"
OUT = os.path.dirname(os.path.abspath(__file__))


def one(args):
    scan = args[0]
    x0, y0, x1, y1 = (int(a) for a in args[1:5])
    scale = float(args[5])
    rot = float(args[6]) if len(args) > 6 else 0.0
    im = Image.open(os.path.join(IMG, f"MPL_151_032-075_151_scan{scan}.jpg"))
    c = im.crop((x0, y0, x1, y1)).convert("L")
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255, resample=Image.BICUBIC)
    c = ImageOps.autocontrast(c, cutoff=1)
    return c


def main():
    argv = sys.argv[1:]
    name = argv[0]
    groups, cur = [], []
    for a in argv[1:]:
        if a == "--":
            groups.append(cur)
            cur = []
        else:
            cur.append(a)
    if cur:
        groups.append(cur)
    crops = [one(g) for g in groups]
    for k, c in enumerate(crops, 1):
        c.save(os.path.join(OUT, f"{name}_{k}.png"))
    w = max(c.width for c in crops)
    h = sum(c.height + 30 for c in crops)
    m = Image.new("L", (w, h), 255)
    d = ImageDraw.Draw(m)
    y = 0
    for k, c in enumerate(crops, 1):
        d.rectangle((0, y, w, y + 26), fill=200)
        d.text((5, y + 6), f"[{k}] scan {groups[k-1][0]} box {groups[k-1][1:5]} x{groups[k-1][5]}", fill=0)
        y += 30
        m.paste(c, (0, y))
        y += c.height
    p = os.path.join(OUT, name + ".png")
    m.save(p)
    print(p, m.size)


if __name__ == "__main__":
    main()
