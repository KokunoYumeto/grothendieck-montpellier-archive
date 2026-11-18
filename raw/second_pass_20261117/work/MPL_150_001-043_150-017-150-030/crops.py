"""Crops for the second pass of MPL_150_001-043, scans 17-30 (this checker's own script).

Usage: python -I -B crops.py OUTNAME SCAN:half:x0,y0,x1,y1[:rot[:scale]] [...]
  half is a (top half image), b (bottom half image) or f (whole page);
  coordinates are pixels in that image; rot in degrees (counter-clockwise); scale default 2.
All regions are stacked vertically into one montage OUTNAME.png in this folder, each with a thin label.
"""
import sys
import os
from PIL import Image, ImageDraw, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, '..', '..', 'img', 'MPL_150_001-043')


def load(scan, half):
    suffix = {'a': '_a', 'b': '_b', 'f': ''}[half]
    return Image.open(os.path.join(IMG, 'MPL_150_001-043_150_scan%03d%s.jpg' % (scan, suffix))).convert('L')


def main():
    out = sys.argv[1]
    tiles = []
    for spec in sys.argv[2:]:
        parts = spec.split(':')
        scan = int(parts[0])
        half = parts[1]
        x0, y0, x1, y1 = [int(v) for v in parts[2].split(',')]
        rot = float(parts[3]) if len(parts) > 3 and parts[3] else 0.0
        scale = float(parts[4]) if len(parts) > 4 else 2.0
        im = load(scan, half).crop((x0, y0, x1, y1))
        if rot:
            im = im.rotate(rot, expand=True, fillcolor=255)
        im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
        im = ImageOps.autocontrast(im, cutoff=1)
        lab = Image.new('L', (im.width, 22), 255)
        ImageDraw.Draw(lab).text((4, 4), spec, fill=0)
        tiles.append(lab)
        tiles.append(im)
    w = max(t.width for t in tiles)
    h = sum(t.height for t in tiles) + 4 * len(tiles)
    canvas = Image.new('L', (w, h), 200)
    y = 0
    for t in tiles:
        canvas.paste(t, (0, y))
        y += t.height + 4
    path = os.path.join(HERE, out + '.png')
    canvas.save(path)
    print(path, canvas.size)


if __name__ == '__main__':
    main()
