import sys
from PIL import Image, ImageDraw

IMG = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_147_048-137/MPL_147_048-137_scan{n}{h}.jpg"
WORK = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/work/MPL_147_048-137_120-137/"

# usage: crops_120_137.py OUTNAME spec spec ...
# spec = scan:half:x0,y0,x1,y1:scale[:rot]   half in {a,b,f}
out = sys.argv[1]
pieces = []
for spec in sys.argv[2:]:
    parts = spec.split(":")
    n, h, box, sc = parts[0], parts[1], parts[2], float(parts[3])
    rot = int(parts[4]) if len(parts) > 4 else 0
    hh = "" if h == "f" else "_" + h
    im = Image.open(IMG.format(n=n, h=hh)).convert("L")
    x0, y0, x1, y1 = [int(v) for v in box.split(",")]
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255)
    pieces.append((spec, c))
W = max(p[1].width for p in pieces)
H = sum(p[1].height + 22 for p in pieces)
M = Image.new("L", (W, H), 255)
d = ImageDraw.Draw(M)
y = 0
for spec, c in pieces:
    d.rectangle((0, y, W, y + 20), fill=200)
    d.text((4, y + 4), spec, fill=0)
    y += 22
    M.paste(c, (0, y))
    y += c.height
M.save(WORK + out, quality=92)
print(WORK + out, M.size)
