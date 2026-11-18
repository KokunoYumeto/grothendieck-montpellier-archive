"""Crop, enlarge and montage regions of the block's scan images.

Usage: python -I -B crops.py SPEC.txt OUT.png
SPEC lines: label | NNN_h | x0,y0,x1,y1 | scale | rot
  NNN_h: scan number and half, e.g. 003_a, 003_b, or 003 for the whole page.
  Coordinates are pixels of that image. rot in degrees (counter-clockwise).
"""
import sys
from PIL import Image, ImageDraw, ImageOps

IMG = ("C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/"
       "MPL_150_085-099+151_001-031/MPL_150_085-099+151_001-031_151_scan%s.jpg")


def main(spec, out):
    tiles = []
    for line in open(spec, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        label, sh, box = parts[0], parts[1], parts[2]
        scale = float(parts[3]) if len(parts) > 3 and parts[3] else 2.0
        rot = float(parts[4]) if len(parts) > 4 and parts[4] else 0.0
        im = Image.open(IMG % sh).convert("L")
        x0, y0, x1, y1 = [int(v) for v in box.split(",")]
        c = im.crop((x0, y0, x1, y1))
        if rot:
            c = c.rotate(rot, expand=True, fillcolor=255)
        c = c.resize((max(1, int(c.width * scale)), max(1, int(c.height * scale))), Image.LANCZOS)
        c = ImageOps.autocontrast(c, cutoff=1)
        lab = Image.new("L", (c.width, 22), 255)
        ImageDraw.Draw(lab).text((4, 4), label, fill=0)
        t = Image.new("L", (c.width, c.height + 22), 255)
        t.paste(lab, (0, 0))
        t.paste(c, (0, 22))
        tiles.append(t)
    W = max(t.width for t in tiles)
    H = sum(t.height + 6 for t in tiles)
    m = Image.new("L", (W, H), 200)
    y = 0
    for t in tiles:
        m.paste(t, (0, y))
        y += t.height + 6
    m.save(out)
    print(out, m.size)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
