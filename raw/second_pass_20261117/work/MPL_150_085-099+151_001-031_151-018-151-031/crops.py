"""Crop and enlarge regions of the scans of block 151-018..151-031 into one sheet.

Usage: python -I -B crops.py OUT.png "scan,x0,y0,x1,y1,scale[,rot]" ...
Coordinates are in the full-page image (MPL_..._151_scanNNN.jpg).
Each crop is enlarged by `scale` (and rotated by `rot` degrees if given),
labelled, and stacked vertically into OUT.png (in this work folder).
"""
import os
import sys
from PIL import Image, ImageDraw

IMG = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_150_085-099+151_001-031"
WORK = os.path.dirname(os.path.abspath(__file__))


def main():
    out = sys.argv[1]
    pieces = []
    for spec in sys.argv[2:]:
        parts = spec.split(",")
        cote = "151"
        if "/" in parts[0]:
            cote, sc = parts[0].split("/")
            scan = int(sc)
        else:
            scan = int(parts[0])
        x0, y0, x1, y1 = map(int, parts[1:5])
        scale = float(parts[5])
        rot = float(parts[6]) if len(parts) > 6 else 0.0
        path = os.path.join(IMG, f"MPL_150_085-099+151_001-031_{cote}_scan{scan:03d}.jpg")
        im = Image.open(path).convert("L")
        c = im.crop((x0, y0, x1, y1))
        c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
        if rot:
            c = c.rotate(rot, expand=True, fillcolor=255)
        lab = Image.new("L", (c.width, 22), 255)
        ImageDraw.Draw(lab).text((4, 4), f"scan {scan} box {x0},{y0},{x1},{y1} x{scale} r{rot}", fill=0)
        pieces.append(lab)
        pieces.append(c)
    w = max(p.width for p in pieces)
    h = sum(p.height for p in pieces) + 6 * len(pieces)
    sheet = Image.new("L", (w, h), 200)
    y = 0
    for p in pieces:
        sheet.paste(p, (0, y))
        y += p.height + 6
    sheet.save(os.path.join(WORK, out))
    print(os.path.join(WORK, out), sheet.size)


if __name__ == "__main__":
    main()
