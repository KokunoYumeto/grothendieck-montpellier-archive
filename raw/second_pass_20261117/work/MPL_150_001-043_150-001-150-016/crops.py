# Crop helper for the second pass of MPL_150_001-043, scans 001-016 (Claude Opus 5.5, effort max).
# Usage: python -I -B crops.py OUT.jpg "scanNNN[_a|_b]:x0,y0,x1,y1[:rot][:w]" ...
# Coordinates are fractions (0-1) of the source image. Each crop is resized to width w (default 1800)
# and the crops are stacked vertically with a label strip.
import sys
from PIL import Image, ImageDraw
IMG = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_150_001-043/MPL_150_001-043_150_"
out = sys.argv[1]
tiles = []
for spec in sys.argv[2:]:
    parts = spec.split(":")
    name = parts[0]
    x0, y0, x1, y1 = [float(v) for v in parts[1].split(",")]
    rot = float(parts[2]) if len(parts) > 2 and parts[2] else 0.0
    w = int(parts[3]) if len(parts) > 3 else 1800
    im = Image.open(IMG + name + ".jpg").convert("RGB")
    W, H = im.size
    c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=(255, 255, 255))
    h = max(1, int(c.size[1] * w / c.size[0]))
    c = c.resize((w, h), Image.LANCZOS)
    lab = Image.new("RGB", (w, 28), (200, 200, 255))
    ImageDraw.Draw(lab).text((5, 5), spec, fill=(0, 0, 0))
    tiles.append(lab)
    tiles.append(c)
Wt = max(t.size[0] for t in tiles)
Ht = sum(t.size[1] for t in tiles)
m = Image.new("RGB", (Wt, Ht), (255, 255, 255))
y = 0
for t in tiles:
    m.paste(t, (0, y))
    y += t.size[1]
m.save(out, quality=90)
print(out, m.size)
