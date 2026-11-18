# Crops and montages for the second pass of block MPL_144_168-184+148_001-028_148-016-148-028.
# Usage: python -I crops.py <specfile.json> <outprefix>
# Each spec: [label, image_suffix ('' | '_a' | '_b'), scan, [x0,y0,x1,y1], zoom, flags]
# flags: string containing 'h' (mirror horizontally), 'e' (enhance contrast), 'r90'/'r180'/'r270' (rotate)
import json, sys, os
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance

IMG = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_144_168-184+148_001-028"
OUT = os.path.dirname(os.path.abspath(__file__))
MAXW, MAXH = 1500, 1950

try:
    FONT = ImageFont.truetype(r"C:/Windows/Fonts/arial.ttf", 22)
except Exception:
    FONT = ImageFont.load_default()

def make_crop(spec):
    label, suf, scan, box, zoom, flags = spec
    path = os.path.join(IMG, "MPL_144_168-184+148_001-028_148_scan%03d%s.jpg" % (scan, suf))
    im = Image.open(path).convert("RGB")
    x0, y0, x1, y1 = box
    x0, y0 = max(0, x0), max(0, y0)
    x1, y1 = min(im.size[0], x1), min(im.size[1], y1)
    c = im.crop((x0, y0, x1, y1))
    if "h" in flags:
        c = ImageOps.mirror(c)
    if "r90" in flags:
        c = c.rotate(90, expand=True)
    if "r180" in flags:
        c = c.rotate(180, expand=True)
    if "r270" in flags:
        c = c.rotate(270, expand=True)
    w, h = c.size
    z = zoom
    if w * z > MAXW:
        z = MAXW / w
    c = c.resize((max(1, int(w * z)), max(1, int(h * z))), Image.LANCZOS)
    if "e" in flags:
        g = ImageOps.grayscale(c)
        g = ImageOps.autocontrast(g, cutoff=2)
        g = ImageEnhance.Contrast(g).enhance(1.8)
        c = g.convert("RGB")
    bar = Image.new("RGB", (c.size[0], 28), (255, 235, 150))
    d = ImageDraw.Draw(bar)
    d.text((6, 2), "%s  [scan %03d%s %s z%.1f %s]" % (label, scan, suf, box, z, flags), fill=(0, 0, 0), font=FONT)
    out = Image.new("RGB", (c.size[0], c.size[1] + 28), (255, 255, 255))
    out.paste(bar, (0, 0))
    out.paste(c, (0, 28))
    return out

def main():
    specs = json.load(open(sys.argv[1], encoding="utf-8"))
    prefix = sys.argv[2]
    tiles = [make_crop(s) for s in specs]
    pages, cur, curh = [], [], 0
    for t in tiles:
        if cur and curh + t.size[1] + 8 > MAXH:
            pages.append(cur)
            cur, curh = [], 0
        cur.append(t)
        curh += t.size[1] + 8
    if cur:
        pages.append(cur)
    for i, p in enumerate(pages):
        W = max(t.size[0] for t in p)
        H = sum(t.size[1] + 8 for t in p)
        m = Image.new("RGB", (W, H), (60, 60, 60))
        y = 0
        for t in p:
            m.paste(t, (0, y))
            y += t.size[1] + 8
        fn = os.path.join(OUT, "%s_%02d.jpg" % (prefix, i + 1))
        m.save(fn, quality=92)
        print(fn, m.size, [t.size for t in p])

main()
