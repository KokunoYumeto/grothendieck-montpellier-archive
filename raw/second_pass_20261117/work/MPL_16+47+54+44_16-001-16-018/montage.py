# Stack several enlarged crops into one labelled PNG (second pass, block 16-001-16-018).
# usage: python -I -B montage.py OUTNAME SCAN x0 y0 x1 y1 scale [SCAN x0 y0 x1 y1 scale ...]
# coordinates are fractions (0..1) of the whole page image; rotation: append r90/r-90 to scale e.g. 2.5r90
import sys, os
from PIL import Image, ImageOps, ImageDraw
IMG = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_16+47+54+44"
OUT = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/work/MPL_16+47+54+44_16-001-16-018"
a = sys.argv[1:]
outname = a[0]; a = a[1:]
tiles = []
k = 0
while k < len(a):
    scan = int(a[k]); x0, y0, x1, y1 = map(float, a[k+1:k+5]); sc = a[k+5]; k += 6
    rot = 0
    if 'r' in sc:
        sc, r = sc.split('r'); rot = float(r)
    sc = float(sc)
    im = Image.open(os.path.join(IMG, "MPL_16+47+54+44_16_scan%03d.jpg" % scan))
    W, H = im.size
    c = im.crop((int(x0*W), int(y0*H), int(x1*W), int(y1*H))).convert("L")
    c = c.resize((max(1,int(c.width*sc)), max(1,int(c.height*sc))), Image.LANCZOS)
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255)
    c = ImageOps.autocontrast(c, cutoff=1)
    tiles.append((scan, (x0, y0, x1, y1), c))
Wm = min(1900, max(t[2].width for t in tiles))
tot = sum(min(t[2].height, int(t[2].height*Wm/max(t[2].width,1))) + 22 for t in tiles)
M = Image.new("L", (Wm, tot), 255)
d = ImageDraw.Draw(M)
y = 0
for scan, box, c in tiles:
    if c.width > Wm:
        c = c.resize((Wm, int(c.height*Wm/c.width)), Image.LANCZOS)
    d.text((4, y+4), "scan %d box %s" % (scan, box), fill=0)
    y += 22
    M.paste(c, (0, y)); y += c.height
p = os.path.join(OUT, outname + ".png")
M.save(p); print(p, M.size)
