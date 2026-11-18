"""Make one labelled montage of enlarged crops from full-page scans.

Usage: python -I -B crop.py OUT.png SPEC [SPEC ...]
SPEC = NNN:x0,y0,x1,y1:scale[:rot]   (full-page pixel coordinates; rot in degrees, counter-clockwise)
"""
import sys
from PIL import Image, ImageDraw, ImageOps

IMG = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_142_001-093/MPL_142_001-093_scan{}.jpg"
MAXW = 1900

def tile(spec):
    parts = spec.split(":")
    n = parts[0]
    x0, y0, x1, y1 = [int(v) for v in parts[1].split(",")]
    sc = float(parts[2]) if len(parts) > 2 else 2.0
    rot = int(parts[3]) if len(parts) > 3 else 0
    im = Image.open(IMG.format(n)).convert("L")
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((max(1, int(c.width * sc)), max(1, int(c.height * sc))), Image.LANCZOS)
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255)
    c = ImageOps.autocontrast(c, cutoff=1)
    if c.width > MAXW:
        r = MAXW / c.width
        c = c.resize((MAXW, int(c.height * r)), Image.LANCZOS)
    lab = Image.new("L", (c.width, 22), 255)
    ImageDraw.Draw(lab).text((4, 4), spec, fill=0)
    out = Image.new("L", (c.width, c.height + 22), 255)
    out.paste(lab, (0, 0))
    out.paste(c, (0, 22))
    return out

def main():
    out = sys.argv[1]
    tiles = [tile(s) for s in sys.argv[2:]]
    W = max(t.width for t in tiles)
    H = sum(t.height + 6 for t in tiles)
    m = Image.new("L", (W, H), 200)
    y = 0
    for t in tiles:
        m.paste(t, (0, y))
        y += t.height + 6
    m.save(out)
    print(out, m.size)

main()
