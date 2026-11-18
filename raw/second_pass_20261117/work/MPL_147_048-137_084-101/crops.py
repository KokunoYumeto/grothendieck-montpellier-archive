"""Make enlarged crops of scan halves and stack them into one labelled composite.

Usage: python -I -B crops.py OUTNAME spec [spec ...]
spec = NNNh:x0,y0,x1,y1[:scale[:rot]]   (h = a or b or f for the whole page; rot in degrees, counterclockwise)
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw

IMG = Path("C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_147_048-137")
OUT = Path("C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/work/MPL_147_048-137_084-101")

def load(tag):
    n, h = tag[:3], tag[3:]
    name = f"MPL_147_048-137_scan{n}" + ("" if h == "f" else "_" + h) + ".jpg"
    return Image.open(IMG / name).convert("L")

def main():
    outname = sys.argv[1]
    pieces = []
    for spec in sys.argv[2:]:
        parts = spec.split(":")
        tag = parts[0]
        box = [int(v) for v in parts[1].split(",")]
        scale = float(parts[2]) if len(parts) > 2 else 2.0
        rot = float(parts[3]) if len(parts) > 3 else 0.0
        im = load(tag)
        x0, y0, x1, y1 = box
        x0, y0 = max(0, x0), max(0, y0)
        x1, y1 = min(im.width, x1), min(im.height, y1)
        c = im.crop((x0, y0, x1, y1))
        c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
        if rot:
            c = c.rotate(rot, expand=True, fillcolor=255)
        c.save(OUT / f"{outname}_{tag}_{x0}_{y0}_{x1}_{y1}.png")
        pieces.append((spec, c))
    width = max(c.width for _, c in pieces)
    height = sum(c.height + 22 for _, c in pieces)
    comp = Image.new("L", (width, height), 255)
    d = ImageDraw.Draw(comp)
    y = 0
    for i, (spec, c) in enumerate(pieces):
        d.rectangle((0, y, width, y + 20), fill=200)
        d.text((4, y + 4), f"[{i + 1}] {spec}", fill=0)
        y += 22
        comp.paste(c, (0, y))
        y += c.height
    comp.save(OUT / f"{outname}.png")
    print(OUT / f"{outname}.png", comp.size)

main()
