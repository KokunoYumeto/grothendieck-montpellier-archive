"""Crop and enlarge regions of MPL_149_001-090 scans into one montage.
Usage: python -I -B crop.py OUT.png SPEC [SPEC ...]
SPEC = NNNh:fx0,fy0,fx1,fy1[@scale][r90|r270|r180]
  NNN = scan number, h = a (top half) or b (bottom half) or p (whole page);
  fx/fy = fractions of that image's width/height.
Each crop is enlarged (default x2) and the crops are stacked vertically with a label."""
import sys, pathlib
from PIL import Image, ImageDraw

IMG = pathlib.Path("C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_149_001-090")
OUTDIR = pathlib.Path("C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/work/MPL_149_001-090_019-036")

def load(n, h):
    suf = {"a": "_a", "b": "_b", "p": ""}[h]
    return Image.open(IMG / f"MPL_149_001-090_scan{n}{suf}.jpg").convert("L")

crops = []
for spec in sys.argv[2:]:
    head, box = spec.split(":", 1)
    n, h = head[:3], head[3]
    rot = 0
    if "r" in box:
        box, r = box.split("r")
        rot = int(r)
    scale = 2.0
    if "@" in box:
        box, s = box.split("@")
        scale = float(s)
    fx0, fy0, fx1, fy1 = map(float, box.split(","))
    im = load(n, h)
    W, H = im.size
    c = im.crop((int(fx0 * W), int(fy0 * H), int(fx1 * W), int(fy1 * H)))
    c = c.resize((max(1, int(c.width * scale)), max(1, int(c.height * scale))), Image.LANCZOS)
    if rot:
        c = c.rotate(rot, expand=True)
    crops.append((spec, c))

width = max(c.width for _, c in crops)
height = sum(c.height + 22 for _, c in crops)
M = Image.new("L", (width, height), 255)
d = ImageDraw.Draw(M)
y = 0
for spec, c in crops:
    d.text((4, y + 4), spec, fill=0)
    y += 22
    M.paste(c, (0, y))
    y += c.height
out = OUTDIR / sys.argv[1]
M.save(out)
print(out, M.size)
