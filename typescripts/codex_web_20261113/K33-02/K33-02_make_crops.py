"""Regenerate the 3× reading crops from the supplied scan ZIP and the coordinate index.

Run: python out/K33-02_make_crops.py K33-02_scans.zip
Pillow is required. Unless a directory is specified, crops are placed beside out/.
"""
import argparse
import csv
import io
from pathlib import Path
import zipfile

from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parent

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scan_zip", type=Path)
    parser.add_argument("--destination", type=Path, default=ROOT.parent / "crops")
    args = parser.parse_args()
    args.destination.mkdir(parents=True, exist_ok=True)
    with (ROOT / "K33-02_crop_index.tsv").open(encoding="utf-8", newline="") as table:
        rows = list(csv.DictReader(table, delimiter="\t"))
    with zipfile.ZipFile(args.scan_zip) as archive:
        sources = {r["source"] for r in rows}
        files = {Path(name).name: name for name in archive.namelist() if Path(name).name in sources}
        assert files.keys() == sources
        for source in sorted(sources):
            with Image.open(io.BytesIO(archive.read(files[source]))) as page:
                for row in (r for r in rows if r["source"] == source):
                    bounds = tuple(int(row[key]) for key in ("left", "top", "right", "bottom"))
                    crop = page.crop(bounds)
                    angle = float(row["rotation_degrees_ccw"])
                    if angle:
                        crop = crop.rotate(angle, expand=True, fillcolor=255)
                    crop = ImageEnhance.Contrast(crop).enhance(1.5)
                    crop = crop.resize((3 * crop.width, 3 * crop.height), Image.Resampling.LANCZOS)
                    crop.save(args.destination / row["crop_at_3x"], quality=93)
    print(f"Created {len(rows)} crops.")

if __name__ == "__main__":
    main()
