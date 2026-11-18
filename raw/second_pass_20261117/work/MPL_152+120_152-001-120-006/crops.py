"""Crop montage for the second pass of block MPL_152+120_152-001-120-006.

Usage: python -I -B crops.py OUT.jpg SPEC [SPEC ...]
SPEC = IMG:x0,y0,x1,y1[:rot][:w]
  IMG   image name in second_pass/img/MPL_152+120 without .jpg, e.g. 152_scan002_a
  x0..  box in DISPLAY coordinates (the image as shown, long side scaled to 2000 px)
  rot   optional rotation in degrees (counter-clockwise), default 0
  w     optional target width in px of this crop in the montage, default 1400
Crops are enlarged (LANCZOS), labelled, and stacked vertically into OUT.jpg (in this folder).
"""
import sys, os
from PIL import Image, ImageDraw

IMG_DIR = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_152+120"
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


def load(name):
    p = os.path.join(IMG_DIR, "MPL_152+120_" + name + ".jpg")
    im = Image.open(p).convert("RGB")
    return im


def crop(spec):
    parts = spec.split(":")
    name = parts[0]
    x0, y0, x1, y1 = [float(v) for v in parts[1].split(",")]
    rot = float(parts[2]) if len(parts) > 2 and parts[2] else 0.0
    tw = int(parts[3]) if len(parts) > 3 else 1400
    im = load(name)
    w, h = im.size
    f = max(1.0, max(w, h) / 2000.0)
    box = (int(x0 * f), int(y0 * f), int(x1 * f), int(y1 * f))
    c = im.crop(box)
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=(255, 255, 255))
    s = tw / c.size[0]
    c = c.resize((tw, max(1, int(c.size[1] * s))), Image.LANCZOS)
    lab = Image.new("RGB", (tw, 22), (255, 255, 200))
    ImageDraw.Draw(lab).text((4, 4), spec, fill=(200, 0, 0))
    out = Image.new("RGB", (tw, c.size[1] + 22), (255, 255, 255))
    out.paste(lab, (0, 0))
    out.paste(c, (0, 22))
    return out


def save(group, outname):
    W = max(p.size[0] for p in group)
    H = sum(p.size[1] for p in group) + 6 * len(group)
    m = Image.new("RGB", (W, H), (90, 90, 90))
    y = 0
    for p in group:
        m.paste(p, (0, y))
        y += p.size[1] + 6
    m.save(os.path.join(OUT_DIR, outname), quality=90)
    print(outname, m.size)


def main():
    outname = sys.argv[1]
    pieces = [crop(s) for s in sys.argv[2:]]
    # split into montages of height <= 1990 so that they are shown unscaled
    groups, cur, h = [], [], 0
    for p in pieces:
        ph = p.size[1] + 6
        if cur and h + ph > 1990:
            groups.append(cur)
            cur, h = [], 0
        cur.append(p)
        h += ph
    if cur:
        groups.append(cur)
    base, ext = os.path.splitext(outname)
    for i, g in enumerate(groups):
        save(g, outname if len(groups) == 1 else "%s_%d%s" % (base, i + 1, ext))


if __name__ == "__main__":
    main()
