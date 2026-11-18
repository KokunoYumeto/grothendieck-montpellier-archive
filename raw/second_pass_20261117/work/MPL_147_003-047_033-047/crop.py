"""Crop montage helper for the second pass of MPL_147_003-047, scans 033-047.

Usage: python -I -B crop.py OUT.png SCAN:HALF:x0,y0,x1,y1:SCALE[:ROT] ...
HALF is a, b or f (full page). Coordinates are pixels of that image.
Each crop is enlarged by SCALE (and rotated by ROT degrees if given), labelled, and stacked vertically.
"""
import sys
from PIL import Image, ImageDraw

IMG = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_147_003-047/"
OUTDIR = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/work/MPL_147_003-047_033-047/"


def main():
    out = sys.argv[1]
    tiles = []
    for k, spec in enumerate(sys.argv[2:], 1):
        parts = spec.split(":")
        scan, half, box, scale = parts[0], parts[1], parts[2], float(parts[3])
        rot = float(parts[4]) if len(parts) > 4 else 0.0
        name = f"MPL_147_003-047_scan{scan}" + ("" if half == "f" else f"_{half}") + ".jpg"
        im = Image.open(IMG + name).convert("L")
        x0, y0, x1, y1 = [int(v) for v in box.split(",")]
        c = im.crop((x0, y0, x1, y1))
        c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
        if rot:
            c = c.rotate(rot, expand=True, fillcolor=255)
        lab = Image.new("L", (c.width, 22), 255)
        ImageDraw.Draw(lab).text((4, 4), f"[{k}] {scan}{half} {box} x{scale}", fill=0)
        t = Image.new("L", (c.width, c.height + 22), 255)
        t.paste(lab, (0, 0))
        t.paste(c, (0, 22))
        tiles.append(t)
    W = max(t.width for t in tiles)
    H = sum(t.height + 6 for t in tiles)
    m = Image.new("L", (W, H), 160)
    y = 0
    for t in tiles:
        m.paste(t, (0, y))
        y += t.height + 6
    m.save(OUTDIR + out)
    print(OUTDIR + out, m.size)


if __name__ == "__main__":
    main()
