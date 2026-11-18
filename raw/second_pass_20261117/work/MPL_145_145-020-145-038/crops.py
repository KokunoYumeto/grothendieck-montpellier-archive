"""Crop/enlarge/rotate helper for the MPL_145 second pass (scans 20-38).

Usage: python -I -B crops.py SPEC.json OUT.jpg
SPEC is a list of {"scan": 20, "box": [x0, y0, x1, y1], "rot": 0, "scale": 2.0, "label": "..."}
Coordinates are in the whole-page image (MPL_145_145_scanNNN.jpg).
rot is applied counter-clockwise in degrees (PIL convention), after cropping.
All crops are stacked vertically into one montage with their labels.
"""
import json
import sys
from PIL import Image, ImageDraw, ImageOps

IMG = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_145/MPL_145_145_scan%03d.jpg"
MAXW = 1900


def main():
    spec = json.load(open(sys.argv[1], encoding="utf-8"))
    out = sys.argv[2]
    tiles = []
    for s in spec:
        im = Image.open(IMG % s["scan"]).convert("L")
        x0, y0, x1, y1 = s["box"]
        c = im.crop((x0, y0, x1, y1))
        rot = s.get("rot", 0)
        if rot:
            c = c.rotate(rot, expand=True, fillcolor=255)
        sc = s.get("scale", 2.0)
        c = c.resize((max(1, int(c.width * sc)), max(1, int(c.height * sc))), Image.LANCZOS)
        if s.get("contrast"):
            c = ImageOps.autocontrast(c, cutoff=1)
        if c.width > MAXW:
            r = MAXW / c.width
            c = c.resize((MAXW, int(c.height * r)), Image.LANCZOS)
        lab = Image.new("L", (c.width, 26), 230)
        ImageDraw.Draw(lab).text((4, 6), s.get("label", ""), fill=0)
        tile = Image.new("L", (c.width, c.height + 26 + 6), 255)
        tile.paste(lab, (0, 0))
        tile.paste(c, (0, 26))
        tiles.append(tile)
    W = max(t.width for t in tiles)
    H = sum(t.height for t in tiles)
    mont = Image.new("L", (W, H), 255)
    y = 0
    for t in tiles:
        mont.paste(t, (0, y))
        y += t.height
    mont.save(out, quality=92)
    print(out, mont.size)


if __name__ == "__main__":
    main()
