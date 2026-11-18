"""Crop, enlarge, rotate and stack regions of the scan images into labelled montages.

Usage: python -I -B montage.py SPEC.json OUTPREFIX
SPEC: list of [label, scan, half, x0, y0, x1, y1, scale, angle]
  half: "" (whole page), "a" or "b"; coordinates in that image's pixels;
  angle: degrees counter-clockwise (180 for upside-down typescript pages).
Montages are at most 1600 px wide and 1950 px high; several files if needed.
"""
import json
import sys
from PIL import Image, ImageDraw

IMG = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_16+47+54+44/"
MAXW, MAXH = 1600, 1950


def load(scan, half):
    name = "MPL_16+47+54+44_16_scan%03d%s.jpg" % (scan, ("_" + half) if half else "")
    return Image.open(IMG + name).convert("RGB")


def main():
    spec = json.load(open(sys.argv[1], encoding="utf-8"))
    out = sys.argv[2]
    tiles = []
    cache = {}
    for label, scan, half, x0, y0, x1, y1, scale, angle in spec:
        key = (scan, half)
        if key not in cache:
            cache[key] = load(scan, half)
        im = cache[key].crop((x0, y0, x1, y1))
        if angle:
            im = im.rotate(angle, expand=True, fillcolor=(255, 255, 255))
        w, h = im.size
        s = scale
        if w * s > MAXW:
            s = MAXW / w
        im = im.resize((max(1, int(w * s)), max(1, int(h * s))), Image.LANCZOS)
        bar = Image.new("RGB", (im.size[0], 22), (255, 235, 120))
        ImageDraw.Draw(bar).text((4, 4), label, fill=(0, 0, 0))
        tile = Image.new("RGB", (im.size[0], im.size[1] + 22), (255, 255, 255))
        tile.paste(bar, (0, 0))
        tile.paste(im, (0, 22))
        tiles.append(tile)
    pages, cur, curh = [], [], 0
    for t in tiles:
        if cur and curh + t.size[1] + 6 > MAXH:
            pages.append(cur)
            cur, curh = [], 0
        cur.append(t)
        curh += t.size[1] + 6
    if cur:
        pages.append(cur)
    for k, page in enumerate(pages):
        W = max(t.size[0] for t in page)
        H = sum(t.size[1] + 6 for t in page)
        m = Image.new("RGB", (W, H), (90, 90, 90))
        y = 0
        for t in page:
            m.paste(t, (0, y))
            y += t.size[1] + 6
        path = "%s_%d.png" % (out, k + 1)
        m.save(path)
        print(path, m.size)


if __name__ == "__main__":
    main()
