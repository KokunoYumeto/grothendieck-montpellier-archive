# Crop helper for the second pass of block MPL_150_044-084_150-044-150-057 (own folder only).
# Usage: python -I -B crops.py OUTNAME spec [spec ...]
#   spec = SCAN:x0,y0,x1,y1[:scale[:rot]]   (coordinates in the whole-page image; rot in degrees, counterclockwise)
# All crops are enlarged and stacked vertically (with a thin separator) into OUTNAME.png in this folder.
import sys, os
from PIL import Image, ImageDraw, ImageOps

IMG = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_150_044-084"
HERE = os.path.dirname(os.path.abspath(__file__))

def one(spec):
    parts = spec.split(":")
    scan = int(parts[0])
    x0, y0, x1, y1 = [int(v) for v in parts[1].split(",")]
    scale = float(parts[2]) if len(parts) > 2 and parts[2] else 2.0
    rot = float(parts[3]) if len(parts) > 3 and parts[3] else 0.0
    im = Image.open(os.path.join(IMG, "MPL_150_044-084_150_scan%03d.jpg" % scan)).convert("L")
    c = im.crop((x0, y0, x1, y1))
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255, resample=Image.BICUBIC)
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c = ImageOps.autocontrast(c, cutoff=1)
    return c

def main():
    out = sys.argv[1]
    crops = [one(s) for s in sys.argv[2:]]
    W = min(max(c.width for c in crops), 1900)
    rows = []
    for c in crops:
        if c.width > W:
            c = c.resize((W, int(c.height * W / c.width)), Image.LANCZOS)
        rows.append(c)
    H = sum(c.height for c in rows) + 6 * (len(rows) - 1)
    canvas = Image.new("L", (W, H), 255)
    d = ImageDraw.Draw(canvas)
    y = 0
    for c in rows:
        canvas.paste(c, (0, y))
        y += c.height
        if y < H:
            d.rectangle([0, y, W, y + 5], fill=0)
        y += 6
    canvas.save(os.path.join(HERE, out + ".png"))
    print(out, canvas.size)

main()
