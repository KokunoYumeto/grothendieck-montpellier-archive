"""Crop-and-stack helper for the second pass, block MPL_147_048-137_066-083.

Usage: python -I crop.py OUT.png SPEC [SPEC ...]
SPEC = NNN{a|b|f}:x0,y0,x1,y1:scale[:rot]
  NNN = scan number, a/b = half, f = full page; box in that image's pixels;
  scale = enlargement factor; rot = degrees counter-clockwise (optional).
Crops are stacked vertically with a small label.
"""
import sys
from PIL import Image, ImageDraw, ImageOps

IMG = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_147_048-137/MPL_147_048-137_scan{n}{s}.jpg"


def load(spec):
    parts = spec.split(":")
    key, box, scale = parts[0], parts[1], float(parts[2])
    rot = float(parts[3]) if len(parts) > 3 else 0.0
    n, half = key[:3], key[3:]
    suffix = "" if half == "f" else "_" + half
    im = Image.open(IMG.format(n=n, s=suffix)).convert("L")
    x0, y0, x1, y1 = [int(v) for v in box.split(",")]
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255)
    c = ImageOps.autocontrast(c, cutoff=1)
    return spec, c


def main():
    out = sys.argv[1]
    crops = [load(s) for s in sys.argv[2:]]
    w = max(c.width for _, c in crops)
    h = sum(c.height + 22 for _, c in crops)
    canvas = Image.new("L", (w, h), 255)
    d = ImageDraw.Draw(canvas)
    y = 0
    for spec, c in crops:
        d.text((4, y + 4), spec, fill=0)
        y += 18
        canvas.paste(c, (0, y))
        y += c.height + 4
        d.line((0, y, w, y), fill=128)
    canvas.save(out)
    print(out, canvas.size)


if __name__ == "__main__":
    main()
