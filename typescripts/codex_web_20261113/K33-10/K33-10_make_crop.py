"""Recreate a named close-up from an attached whole-page JPEG using the crop register.

Usage: python K33-10_make_crop.py /path/to/extracted/images 172-etale-map.jpg output.jpg
The output path must not already exist. Pillow is required.
"""
import csv
import sys
from pathlib import Path
from io import BytesIO
from PIL import Image, ImageEnhance

folder, name, target = sys.argv[1:]
dest = Path(target)
if dest.exists():
    raise FileExistsError(dest)
register = Path(__file__).with_name("K33-10_crop_regions.tsv")
with register.open(newline="") as stream:
    row = next(x for x in csv.DictReader(stream, delimiter="\t") if x["name"] == name)
path = Path(folder) / ("K33-10_33_scan" + row["scan"] + ".jpg")
with Image.open(path) as src:
    img = src.convert("L")
if row["whole_turned"] == "True":
    img = img.transpose(Image.Transpose.ROTATE_180)
    # The turned reading copies were saved as JPEGs before their regions were selected.
    # Reproduce that intermediate encode so the resulting close-up has the original pixels.
    with BytesIO() as turned:
        img.save(turned, format="JPEG", quality=int(row["orientation_jpeg_quality"]))
        turned.seek(0)
        with Image.open(turned) as stage:
            img = stage.copy()
img = img.crop(tuple(int(row[k]) for k in ("left", "top", "right", "bottom")))
angle = int(row["rotation_ccw"])
if angle:
    img = img.rotate(angle, expand=True, resample=Image.Resampling.BICUBIC, fillcolor=255)
img = ImageEnhance.Contrast(img).enhance(1.45)
img = img.resize((3 * img.width, 3 * img.height), Image.Resampling.LANCZOS)
img.save(dest, quality=94)
