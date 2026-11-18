"""Montage of enlarged crops from the scan halves.
Usage: python -I -B crops.py OUTNAME 'spec;spec;...'
spec = file,x0,y0,x1,y1,rot,scale   (file like 002_a ; rot in degrees, counter-clockwise)
"""
import sys
from PIL import Image, ImageDraw, ImageOps

IMG = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_143+141/MPL_143+141_143_scan{}.jpg"
OUT = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/work/MPL_143+141_143-001-143-017/{}.png"

out = sys.argv[1]
specs = [s for s in sys.argv[2].split(";") if s.strip()]
tiles = []
for s in specs:
    f, x0, y0, x1, y1, rot, sc = s.split(",")
    im = Image.open(IMG.format(f.strip())).convert("L")
    c = im.crop((int(x0), int(y0), int(x1), int(y1)))
    if float(rot) != 0:
        c = c.rotate(float(rot), expand=True, fillcolor=255)
    sc = float(sc)
    c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
    c = ImageOps.autocontrast(c, cutoff=1)
    lab = Image.new("L", (c.width, 22), 255)
    ImageDraw.Draw(lab).text((4, 4), s, fill=0)
    t = Image.new("L", (c.width, c.height + 22), 255)
    t.paste(lab, (0, 0))
    t.paste(c, (0, 22))
    tiles.append(t)
W = max(t.width for t in tiles)
H = sum(t.height + 6 for t in tiles)
m = Image.new("L", (W, H), 200)
y = 0
for t in tiles:
    m.paste(t, (0, y))
    y += t.height + 6
m.save(OUT.format(out))
print(OUT.format(out), m.size)
