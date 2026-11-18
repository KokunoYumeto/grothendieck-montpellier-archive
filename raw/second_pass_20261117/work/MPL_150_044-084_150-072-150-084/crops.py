"""Crop, enlarge and optionally rotate regions of the full-page scans of block 150-072..084.

Usage: python -I -B crops.py SCAN x0 y0 x1 y1 [scale] [rotate_deg] [tag]
Coordinates are in the full-page image (about 1680 x 2360).
Output goes next to this script: crop_SCAN_tag.png
"""
import sys
import os
from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, '..', '..', 'img', 'MPL_150_044-084')


def main():
    scan = sys.argv[1].zfill(3)
    x0, y0, x1, y1 = (int(v) for v in sys.argv[2:6])
    scale = float(sys.argv[6]) if len(sys.argv) > 6 else 2.0
    rot = float(sys.argv[7]) if len(sys.argv) > 7 else 0.0
    tag = sys.argv[8] if len(sys.argv) > 8 else f'{x0}_{y0}'
    src = os.path.join(IMG, f'MPL_150_044-084_150_scan{scan}.jpg')
    im = Image.open(src).convert('L')
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255)
    c = ImageOps.autocontrast(c, cutoff=1)
    out = os.path.join(HERE, f'crop_{scan}_{tag}.png')
    c.save(out)
    print(out, c.size)


if __name__ == '__main__':
    main()
