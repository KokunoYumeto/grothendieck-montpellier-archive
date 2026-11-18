# crops.py: crop, enlarge and optionally rotate regions of a scan image.
# usage: python -I -B crops.py SCAN x0 y0 x1 y1 SCALE ROT OUTNAME
# coordinates are in the whole-page image (1681 x 2357); ROT in degrees (counterclockwise).
import sys
from PIL import Image, ImageOps
IMG = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_148_029-072/MPL_148_029-072_148_scan%s.jpg"
OUT = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/work/MPL_148_029-072_148-044-148-058/"
args = sys.argv[1:]
# allow several crops: groups of 8 args
while args:
    scan, x0, y0, x1, y1, scale, rot, name = args[:8]
    args = args[8:]
    im = Image.open(IMG % scan).convert("L")
    c = im.crop((int(x0), int(y0), int(x1), int(y1)))
    s = float(scale)
    c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
    r = float(rot)
    if r:
        c = c.rotate(r, expand=True, fillcolor=255)
    c = ImageOps.autocontrast(c, cutoff=1)
    c.save(OUT + name + ".png")
    print(name, c.size)
