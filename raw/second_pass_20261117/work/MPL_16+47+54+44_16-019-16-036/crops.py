# Crop helper for the second pass of block MPL_16+47+54+44_16-019-16-036 (cote 16, scans 19-36).
# Usage: python -I -B crops.py OUTNAME spec [spec ...]
#   spec = SCAN:x0,y0,x1,y1[:scale[:rot]]   coordinates in whole-page pixels; rot in degrees (counterclockwise)
# All crops of one call are stacked vertically into OUTNAME.jpg in this folder, with a grey bar between them.
import sys, os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, '..', '..', 'img', 'MPL_16+47+54+44')

def crop(spec):
    parts = spec.split(':')
    scan = parts[0].zfill(3)
    x0, y0, x1, y1 = [int(v) for v in parts[1].split(',')]
    scale = float(parts[2]) if len(parts) > 2 and parts[2] else 2.0
    flip = len(parts) > 3 and parts[3] == 'h'
    rot = float(parts[3]) if len(parts) > 3 and parts[3] and not flip else 0.0
    im = Image.open(os.path.join(IMG, 'MPL_16+47+54+44_16_scan%s.jpg' % scan)).convert('L')
    c = im.crop((x0, y0, x1, y1))
    if flip:
        c = c.transpose(Image.FLIP_LEFT_RIGHT)
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255)
    c = c.resize((max(1, int(c.size[0] * scale)), max(1, int(c.size[1] * scale))), Image.LANCZOS)
    return c

def main():
    out = sys.argv[1]
    tiles = [crop(s) for s in sys.argv[2:]]
    W = max(t.size[0] for t in tiles)
    H = sum(t.size[1] for t in tiles) + 12 * (len(tiles) - 1)
    canvas = Image.new('L', (W, H), 255)
    y = 0
    d = ImageDraw.Draw(canvas)
    for i, t in enumerate(tiles):
        canvas.paste(t, (0, y))
        y += t.size[1]
        if i < len(tiles) - 1:
            d.rectangle((0, y + 3, W, y + 8), fill=128)
            y += 12
    path = os.path.join(HERE, out + '.jpg')
    canvas.save(path, quality=92)
    print(path, canvas.size)

main()
