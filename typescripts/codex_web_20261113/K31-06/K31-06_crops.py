#!/usr/bin/env python3
"""Recreate the 3× reading details from the attached scans.

Usage: python K31-06_crops.py K31-06_scans.zip [--output DIRECTORY]
An extracted scan directory is accepted in place of the ZIP. Pillow is required.
The default destination is crops/ beside the out/ folder.
"""
import argparse
import csv
import io
from contextlib import ExitStack
from pathlib import Path
from zipfile import ZipFile

from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parent


def generate(source, output):
    with (ROOT / "K31-06_crop_index.tsv").open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    output.mkdir(exist_ok=True, parents=True)
    with ExitStack() as stack:
        archive = stack.enter_context(ZipFile(source)) if source.is_file() else None
        current = None
        for row in rows:
            scan = int(row["scan"])
            if current != scan:
                name = f"K31-06_31_scan{scan:03d}.jpg"
                path = io.BytesIO(archive.read(name)) if archive else source / name
                with Image.open(path) as original:
                    page = original.convert("L")
                current = scan
            box = tuple(int(row[k]) for k in ("x0", "y0", "x1", "y1"))
            detail = page.crop(box)
            angle = int(row["rotation_ccw"])
            if angle:
                detail = detail.rotate(angle, expand=True, fillcolor=255,
                                       resample=Image.Resampling.BICUBIC)
                subbox = tuple(int(row[k]) for k in ("dx0", "dy0", "dx1", "dy1"))
                detail = detail.crop(subbox)
            detail = ImageEnhance.Contrast(detail).enhance(1.4)
            detail = detail.resize((detail.width * 3, detail.height * 3),
                                   Image.Resampling.LANCZOS)
            detail.save(output / row["filename"], quality=91)
    return len(rows)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT.parent / "crops")
    args = parser.parse_args()
    print(f"Wrote {generate(args.source, args.output)} details to {args.output}")

