"""Recreate manuscript enlargements from the supplied full-resolution JPEGs.

Usage: python K39-01_recreate_crops.py PATH_TO_UNPACKED_SCANS DESTINATION
Requires Pillow. Keep both TSV indices beside this script. Boxes use pixel
coordinates, origin at top left, with the right and bottom edges excluded.
"""
import argparse
import csv
from pathlib import Path

from PIL import Image, ImageEnhance

INDEX_DIR = Path(__file__).resolve().parent

def indexed_rows(name):
    with (INDEX_DIR / name).open(encoding="utf-8", newline="") as stream:
        yield from csv.DictReader(stream, delimiter="\t")

def box(row):
    return tuple(int(row[axis]) for axis in ("left", "top", "right", "bottom"))

def from_scan(source, row):
    filename = f"K39-01_39_scan{int(row['scan']):03}.jpg"
    with Image.open(source / filename) as image:
        patch = image.convert("L").crop(box(row))
    degrees = float(row["rotation_ccw_degrees"])
    if degrees:
        patch = patch.rotate(degrees, resample=Image.Resampling.BICUBIC,
                             expand=True, fillcolor=255)
    patch = ImageEnhance.Contrast(patch).enhance(1.4)
    scale = int(row["magnification"])
    return patch.resize((patch.width * scale, patch.height * scale),
                        Image.Resampling.LANCZOS)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    args.destination.mkdir(parents=True, exist_ok=True)
    for row in indexed_rows("K39-01_crop_index.tsv"):
        from_scan(args.source, row).save(args.destination / row["crop"])
    for row in indexed_rows("K39-01_detail_index.tsv"):
        if row["source"] == "context_png":
            with Image.open(args.destination / row["context_crop"]) as parent:
                patch = parent.crop(box(row))
        elif row["source"] == "scan_jpeg":
            patch = from_scan(args.source, row)
        else:
            raise ValueError(f"Unknown coordinate space in {row['crop']}")
        patch.save(args.destination / row["crop"])

if __name__ == "__main__":
    main()
