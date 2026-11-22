"""Recreate the two crop registers from the original K58-04 scan ZIP.

Usage: python K58-04_crops.py K58-04_scans.zip [--output DIRECTORY]
Requires Pillow. The default output is crops/, beside out/.
"""
import argparse
import csv
import io
import zipfile
from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps


ROOT = Path(__file__).resolve().parent


def rows(filename):
    with (ROOT / filename).open(encoding="utf-8", newline="") as source:
        return list(csv.DictReader(source, delimiter="\t"))


def box(row):
    return tuple(int(row[edge]) for edge in ("left", "top", "right", "bottom"))


def enlarge(scan, bounds, degrees=0, contrast=1.45, scale=3):
    area = ImageOps.grayscale(scan.crop(bounds))
    if degrees:
        area = area.rotate(degrees, expand=True, fillcolor=255)
    area = ImageEnhance.Contrast(area).enhance(contrast)
    return area.resize((area.width * scale, area.height * scale), Image.Resampling.LANCZOS)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scan_zip", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT.parent / "crops")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    contexts = rows("K58-04_crops.tsv")
    details = rows("K58-04_detail_crops.tsv")

    with zipfile.ZipFile(args.scan_zip) as archive:
        for number in sorted({row["scan"] for row in contexts}, key=int):
            member = f"K58-04_58_scan{int(number):03}.jpg"
            with Image.open(io.BytesIO(archive.read(member))) as scan:
                for row in (r for r in contexts if r["scan"] == number):
                    image = enlarge(scan, box(row), int(row["rotation CCW degrees"]),
                                    float(row["contrast"]), int(row["scale"]))
                    image.save(args.output / row["crop filename"], quality=90)
                for row in (r for r in details if r["scan"] == number):
                    if row["coordinate space"] == "whole scan pixels":
                        image = enlarge(scan, box(row))
                    else:
                        with Image.open(args.output / row["context crop"]) as context:
                            image = context.crop(box(row))
                    image.save(args.output / row["detail crop"], quality=93)
    print(f"Recreated {len(contexts)} context and {len(details)} detail crops in {args.output}")


if __name__ == "__main__":
    main()
