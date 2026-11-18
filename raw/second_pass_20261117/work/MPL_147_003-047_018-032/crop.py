"""Montage of enlarged crops from the full scans (second pass, MPL_147_003-047, scans 018-032).

Usage: python -I -B crop.py OUT.jpg SPEC [SPEC ...]
SPEC = label:scan:x0:y0:x1:y1[:scale[:rot]]  (coordinates in the full-page image; rot in degrees, counter-clockwise)
"""
import sys
from PIL import Image, ImageDraw

IMG = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_147_003-047/MPL_147_003-047_scan%03d.jpg"
OUT_DIR = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/work/MPL_147_003-047_018-032/"

def main():
    out = sys.argv[1]
    tiles = []
    for spec in sys.argv[2:]:
        parts = spec.split(":")
        label, scan = parts[0], int(parts[1])
        x0, y0, x1, y1 = map(int, parts[2:6])
        scale = float(parts[6]) if len(parts) > 6 else 2.0
        rot = int(parts[7]) if len(parts) > 7 else 0
        im = Image.open(IMG % scan).convert("L").crop((x0, y0, x1, y1))
        if rot:
            im = im.rotate(rot, expand=True, fillcolor=255)
        im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
        tile = Image.new("L", (im.width, im.height + 28), 255)
        tile.paste(im, (0, 28))
        ImageDraw.Draw(tile).text((4, 4), "%s  (scan %03d, %d,%d-%d,%d, x%.1f)" % (label, scan, x0, y0, x1, y1, scale), fill=0)
        tiles.append(tile)
    w = max(t.width for t in tiles)
    h = sum(t.height for t in tiles) + 6 * len(tiles)
    sheet = Image.new("L", (w, h), 200)
    y = 0
    for t in tiles:
        sheet.paste(t, (0, y))
        y += t.height + 6
    sheet.save(OUT_DIR + out, quality=92)
    print(out, sheet.size)

main()
