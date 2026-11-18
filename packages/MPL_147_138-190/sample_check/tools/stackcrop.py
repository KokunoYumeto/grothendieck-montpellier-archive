# usage: python -I -B stackcrop.py <out.jpg> <src>::<x0>,<y0>,<x1>,<y1>[::scale][::rot][::name] [more specs ...]
# Several crops are stacked into one image; each crop is also saved next to <out> when a name is given.
import sys, os
from PIL import Image

out = sys.argv[1]
tiles = []
for spec in sys.argv[2:]:
    parts = spec.split('::')
    src = parts[0]
    box = tuple(int(v) for v in parts[1].split(','))
    scale = float(parts[2]) if len(parts) > 2 and parts[2] else 2.0
    rot = int(parts[3]) if len(parts) > 3 and parts[3] else 0
    name = parts[4] if len(parts) > 4 else ''
    im = Image.open(src).convert('RGB')
    box = (max(box[0], 0), max(box[1], 0), min(box[2], im.width), min(box[3], im.height))
    im = im.crop(box)
    if rot:
        im = im.rotate(rot, expand=True, fillcolor=(255, 255, 255))
    im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
    if name:
        im.save(os.path.join(os.path.dirname(os.path.abspath(out)), name), quality=90)
    tiles.append(im)
W = max(t.width for t in tiles)
H = sum(t.height for t in tiles) + 8 * (len(tiles) - 1)
canvas = Image.new('RGB', (W, H), (255, 0, 0))
y = 0
for t in tiles:
    canvas.paste(t, (0, y))
    y += t.height + 8
canvas.save(out, quality=90)
print(out, canvas.size)
