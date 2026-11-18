# Crop helper for block MPL_16+47+54+44_16-001-16-018 (second pass, Claude Opus 5.5 at effort max).
# usage: python -I -B crops.py SCAN NAME x0 y0 x1 y1 [scale] [rot]
# coordinates are fractions (0..1) of the WHOLE page image (scanNNN.jpg)
import sys, os
from PIL import Image, ImageOps
IMG = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_16+47+54+44"
OUT = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/work/MPL_16+47+54+44_16-001-16-018"
args = sys.argv[1:]
i = 0
while i < len(args):
    scan, name = args[i], args[i+1]
    x0, y0, x1, y1 = map(float, args[i+2:i+6])
    scale = float(args[i+6]); rot = float(args[i+7])
    i += 8
    im = Image.open(os.path.join(IMG, "MPL_16+47+54+44_16_scan%03d.jpg" % int(scan)))
    W, H = im.size
    c = im.crop((int(x0*W), int(y0*H), int(x1*W), int(y1*H)))
    if scale != 1:
        c = c.resize((int(c.width*scale), int(c.height*scale)), Image.LANCZOS)
    if rot:
        c = c.rotate(rot, expand=True, fillcolor="white")
    c = ImageOps.autocontrast(c.convert("L"), cutoff=1)
    p = os.path.join(OUT, "s%03d_%s.png" % (int(scan), name))
    c.save(p)
    print(p, c.size)
