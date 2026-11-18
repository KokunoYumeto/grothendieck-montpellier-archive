# Crop helper for the second pass of MPL_145 scans 1-19 (this checker's own copy).
# Usage: python -I -B crops.py OUT.png SPEC [SPEC ...]
# SPEC = "IMG:x0,y0,x1,y1[:scale[:rot]]" with coordinates as fractions (0-1) of the image size,
# IMG = path to the jpg; scale = enlargement factor (default 2); rot = degrees counter-clockwise (default 0).
# The crops are stacked vertically into OUT.png, each with a thin separator line.
import sys
from PIL import Image, ImageDraw, ImageOps

def one(spec):
    parts = spec.split(':')
    # path may contain a drive letter "C:" -> rejoin
    if len(parts[0]) == 1 and len(parts) > 1:
        parts = [parts[0] + ':' + parts[1]] + parts[2:]
    path = parts[0]
    box = [float(v) for v in parts[1].split(',')]
    scale = float(parts[2]) if len(parts) > 2 and parts[2] else 2.0
    rot = float(parts[3]) if len(parts) > 3 and parts[3] else 0.0
    im = Image.open(path).convert('L')
    W, H = im.size
    c = im.crop((int(box[0] * W), int(box[1] * H), int(box[2] * W), int(box[3] * H)))
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255)
    c = c.resize((max(1, int(c.width * scale)), max(1, int(c.height * scale))), Image.LANCZOS)
    c = ImageOps.autocontrast(c, cutoff=1)
    return c

def main():
    out = sys.argv[1]
    crops = [one(s) for s in sys.argv[2:]]
    w = max(c.width for c in crops)
    h = sum(c.height for c in crops) + 6 * (len(crops) - 1)
    canvas = Image.new('L', (w, h), 255)
    y = 0
    d = ImageDraw.Draw(canvas)
    for i, c in enumerate(crops):
        canvas.paste(c, (0, y))
        y += c.height
        if i < len(crops) - 1:
            d.rectangle((0, y + 2, w, y + 3), fill=0)
            y += 6
    canvas.save(out)
    print(out, canvas.size)

if __name__ == '__main__':
    main()
