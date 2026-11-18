"""Make labelled montages of enlarged crops from the full-page scans.

Usage: python -I -B montage.py SPEC OUTPREFIX START_INDEX
SPEC lines: scan x0 y0 x1 y1 scale [rot]   (full-page pixel coordinates; rot in degrees, counter-clockwise)
Each montage is at most MAXW x MAXH pixels; tiles are packed in rows and numbered 1.. within each montage.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

IMG = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_142_001-093"
MAXW, MAXH = 1650, 1250
LABEL_H = 22


def load_tiles(spec):
    tiles = []
    for line in open(spec, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        scan, x0, y0, x1, y1, scale = parts[0], *map(int, parts[1:5]), float(parts[5])
        rot = int(parts[6]) if len(parts) > 6 else 0
        im = Image.open(os.path.join(IMG, "MPL_142_001-093_scan%s.jpg" % scan)).convert("RGB")
        c = im.crop((x0, y0, x1, y1))
        c = c.resize((max(1, int(c.width * scale)), max(1, int(c.height * scale))), Image.LANCZOS)
        if rot:
            c = c.rotate(rot, expand=True, fillcolor=(255, 255, 255))
        if c.width > MAXW:
            f = MAXW / c.width
            c = c.resize((MAXW, int(c.height * f)), Image.LANCZOS)
        label = "%s:%d,%d,%d,%d:%g%s" % (scan, x0, y0, x1, y1, scale, (":r%d" % rot) if rot else "")
        tiles.append((label, c))
    return tiles


def main():
    spec, prefix, start = sys.argv[1], sys.argv[2], int(sys.argv[3])
    tiles = load_tiles(spec)
    font = ImageFont.load_default()
    pages, cur, rows, row, rx, rh, y = [], [], [], [], 0, 0, 0
    # greedy row packing
    layout = []  # list of pages, each a list of (label, img, x, y)
    page, x, y, rowh = [], 0, 0, 0
    for label, im in tiles:
        w, h = im.width, im.height + LABEL_H
        if x + w > MAXW:
            x, y, rowh = 0, y + rowh + 6, 0
        if y + h > MAXH and page:
            layout.append(page)
            page, x, y, rowh = [], 0, 0, 0
        page.append((label, im, x, y))
        x += w + 6
        rowh = max(rowh, h)
    if page:
        layout.append(page)
    n = start
    for page in layout:
        W = max(px + im.width for _, im, px, _ in page)
        H = max(py + im.height + LABEL_H for _, im, _, py in page)
        canvas = Image.new("RGB", (W, H), (200, 200, 200))
        d = ImageDraw.Draw(canvas)
        for k, (label, im, px, py) in enumerate(page, 1):
            d.rectangle([px, py, px + im.width, py + LABEL_H - 1], fill=(255, 255, 210))
            d.text((px + 3, py + 4), "%d) %s" % (k, label), fill=(200, 0, 0), font=font)
            canvas.paste(im, (px, py + LABEL_H))
        out = "%s%02d.png" % (prefix, n)
        canvas.save(out)
        print(out, canvas.size, len(page), "tiles:", ", ".join("%d=%s" % (k, l) for k, (l, _, _, _) in enumerate(page, 1)))
        n += 1


if __name__ == "__main__":
    main()
