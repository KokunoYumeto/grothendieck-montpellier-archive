"""Crop montage helper for the second pass of block MPL_151_032-075_151-047-151-061.

Usage: python -I -B crops_047_061.py OUTNAME spec [spec ...]
spec = SCAN:HALF:x0,y0,x1,y1[:scale[:rot]]
  SCAN  = 3-digit scan number (047..061)
  HALF  = a, b or f (whole page)
  scale = enlargement factor (default 2)
  rot   = rotation in degrees counter-clockwise (default 0)
The crops are stacked vertically, each under a small label, and saved as OUTNAME.jpg
in this folder (the block's own work folder).
"""
import os
import sys

from PIL import Image, ImageDraw, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.normpath(os.path.join(HERE, '..', '..', 'img', 'MPL_151_032-075'))


def load(scan, half):
    suffix = '' if half == 'f' else '_' + half
    return Image.open(os.path.join(IMG, 'MPL_151_032-075_151_scan%s%s.jpg' % (scan, suffix))).convert('L')


def main():
    out = sys.argv[1]
    tiles = []
    for spec in sys.argv[2:]:
        parts = spec.split(':')
        scan, half, box = parts[0], parts[1], [int(v) for v in parts[2].split(',')]
        scale = float(parts[3]) if len(parts) > 3 else 2.0
        rot = float(parts[4]) if len(parts) > 4 else 0.0
        im = load(scan, half).crop(tuple(box))
        if rot:
            im = im.rotate(rot, expand=True, fillcolor=255)
        im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
        im = ImageOps.autocontrast(im, cutoff=1)
        label = Image.new('L', (max(im.width, 400), 22), 230)
        ImageDraw.Draw(label).text((4, 4), spec, fill=0)
        tiles.append(label)
        tiles.append(im)
    width = max(t.width for t in tiles)
    height = sum(t.height for t in tiles) + 6 * len(tiles)
    sheet = Image.new('L', (width, height), 255)
    y = 0
    for t in tiles:
        sheet.paste(t, (0, y))
        y += t.height + 6
    path = os.path.join(HERE, out + '.jpg')
    sheet.save(path, quality=92)
    print(path, sheet.size)


if __name__ == '__main__':
    main()
