"""Crop regions of scan halves and stack them into one labelled montage.

Usage: python -I -B crop.py OUTNAME SPEC [SPEC ...]
SPEC = scan:half:fx0,fy0,fx1,fy1[:rot[:width]]
  scan  = 019 etc.; half = a, b or full ("" -> full page)
  fx/fy = fractions of the image width/height
  rot   = degrees counterclockwise (0 default)
  width = target width in pixels of this crop in the montage (default 1500)
"""
import sys, os
from PIL import Image, ImageDraw

BASE = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass"
IMG = BASE + "/img/MPL_142_001-093/MPL_142_001-093_scan{}{}.jpg"
OUT = BASE + "/work/MPL_142_001-093_019-037/"

def main():
    outname = sys.argv[1]
    tiles = []
    for spec in sys.argv[2:]:
        parts = spec.split(":")
        scan, half, box = parts[0], parts[1], parts[2]
        rot = float(parts[3]) if len(parts) > 3 and parts[3] else 0.0
        width = int(parts[4]) if len(parts) > 4 and parts[4] else 1500
        suffix = "" if half in ("", "full") else "_" + half
        im = Image.open(IMG.format(scan, suffix)).convert("L")
        W, H = im.size
        fx0, fy0, fx1, fy1 = [float(v) for v in box.split(",")]
        c = im.crop((int(fx0 * W), int(fy0 * H), int(fx1 * W), int(fy1 * H)))
        if rot:
            c = c.rotate(rot, expand=True, fillcolor=255)
        f = width / c.size[0]
        c = c.resize((width, max(1, int(c.size[1] * f))), Image.LANCZOS)
        tiles.append((spec, c, (W, H)))
    gap = 30
    total_h = sum(t[1].size[1] + gap for t in tiles)
    total_w = max(t[1].size[0] for t in tiles)
    m = Image.new("L", (total_w, total_h), 255)
    d = ImageDraw.Draw(m)
    y = 0
    for spec, c, wh in tiles:
        d.text((5, y + 2), spec + "  size=%dx%d" % wh, fill=0)
        y += gap
        m.paste(c, (0, y))
        y += c.size[1]
    os.makedirs(OUT, exist_ok=True)
    m.save(OUT + outname + ".png")
    print(OUT + outname + ".png", m.size)

main()
