import sys, json
from PIL import Image, ImageDraw, ImageFont
IMG = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_147_048-137/MPL_147_048-137_scan%s.jpg"
OUT = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/work/MPL_147_048-137_048-065/"
spec = json.load(open(sys.argv[1], encoding="utf-8"))
prefix = sys.argv[2]
W = 1600; MAXH = 1550
pieces = []
for label, f, x0, y0, x1, y1, rot in spec:
    im = Image.open(IMG % f).convert("L")
    w, h = im.size
    c = im.crop((int(x0*w), int(y0*h), int(x1*w), int(y1*h)))
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255)
    c.save(OUT + "%s_%s.png" % (prefix, label.split()[0]))
    s = min(W / c.size[0], 2.6)
    c = c.resize((int(c.size[0]*s), int(c.size[1]*s)), Image.LANCZOS)
    if c.size[1] > MAXH:
        r = MAXH / c.size[1]; c = c.resize((int(c.size[0]*r), MAXH), Image.LANCZOS)
    pieces.append((label, c))
pages = []; cur = []; hh = 0
for label, c in pieces:
    if cur and hh + c.size[1] + 30 > MAXH:
        pages.append(cur); cur = []; hh = 0
    cur.append((label, c)); hh += c.size[1] + 30
if cur: pages.append(cur)
try:
    font = ImageFont.truetype("arial.ttf", 26)
except Exception:
    font = ImageFont.load_default()
for i, pg in enumerate(pages):
    H = sum(c.size[1] + 30 for _, c in pg)
    m = Image.new("L", (W, H), 255)
    d = ImageDraw.Draw(m); y = 0
    for label, c in pg:
        d.rectangle((0, y, W, y + 28), fill=200)
        d.text((5, y + 1), label, fill=0, font=font)
        m.paste(c, (0, y + 30)); y += c.size[1] + 30
    p = OUT + "%s_montage%d.png" % (prefix, i + 1)
    m.save(p); print(p, m.size)
