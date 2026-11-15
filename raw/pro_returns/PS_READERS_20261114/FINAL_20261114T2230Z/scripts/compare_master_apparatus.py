"""Prove exact master/apparatus body raster equality after the final build.

This compares every physical page from 2 through the last page at 144 dpi.
It records hashes of both decoded RGB samples and losslessly encoded PNGs,
and checks byte equality directly. It does not assert that any image was
opened by a reviewer. The distinct master front page is rendered for a
separate, actual visual inspection.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import fitz


PROJECT = Path(__file__).resolve().parents[1]
MASTER = "PS_EN_master_annotated"
APPARATUS = "PS_EN_corrected_apparatus"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def geometry(page: fitz.Page) -> dict:
    return {"rect_pt": list(page.rect), "mediabox_pt": list(page.mediabox),
            "cropbox_pt": list(page.cropbox), "rotation": page.rotation}


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(path)


def render(page: fitz.Page):
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), colorspace=fitz.csRGB, alpha=False)
    samples = pix.samples
    png = pix.tobytes("png")
    return samples, png, {
        "width_px": pix.width, "height_px": pix.height, "colorspace": "RGB",
        "pixels_sha256": digest(samples), "png_sha256": digest(png),
    }


def main() -> int:
    paths = {name: PROJECT / "readers" / (name + ".pdf") for name in (MASTER, APPARATUS)}
    snapshots = {name: path.read_bytes() for name, path in paths.items()}
    hashes = {name: digest(data) for name, data in snapshots.items()}
    docs = {name: fitz.open(stream=data, filetype="pdf") for name, data in snapshots.items()}
    master, apparatus = docs[MASTER], docs[APPARATUS]
    issues = []
    if len(master) != len(apparatus):
        issues.append("Master and apparatus page counts differ; body reuse is unproved.")
    pages = []
    mismatch_dir = PROJECT / "qa/master_body_comparison" / (hashes[MASTER][:12] + "_" + hashes[APPARATUS][:12])
    for number in range(2, max(len(master), len(apparatus)) + 1):
        if number > min(len(master), len(apparatus)):
            pages.append({"page": number, "pixels_byte_identical": False,
                          "png_byte_identical": False, "geometry_identical": False,
                          "issue": "Page absent from one PDF"})
            continue
        mp, ap = master[number - 1], apparatus[number - 1]
        mraw, mpng, msig = render(mp)
        araw, apng, asig = render(ap)
        mg, ag = geometry(mp), geometry(ap)
        row = {"page": number, "master_geometry": mg, "apparatus_geometry": ag,
               "geometry_identical": mg == ag,
               "master_144dpi": msig, "apparatus_144dpi": asig,
               "pixels_byte_identical": mraw == araw,
               "png_byte_identical": mpng == apng}
        if not (row["geometry_identical"] and row["pixels_byte_identical"] and row["png_byte_identical"]):
            mismatch_dir.mkdir(parents=True, exist_ok=True)
            for label, content in (("master", mpng), ("apparatus", apng)):
                target = mismatch_dir / f"{label}_{number:04d}.png"
                target.write_bytes(content)
                row[label + "_mismatch_image"] = target.relative_to(PROJECT).as_posix()
            issues.append(f"Master/apparatus body mismatch on physical page {number}.")
        pages.append(row)
        if number % 50 == 0 or number == len(master):
            print(json.dumps({"compared_body_pages": len(pages),
                              "expected_body_pages": max(len(master), len(apparatus)) - 1,
                              "mismatches": len(issues)}), flush=True)
    front = PROJECT / "qa/rendered" / ("final_" + MASTER) / "page_0001.png"
    front.parent.mkdir(parents=True, exist_ok=True)
    _, front_png, front_signature = render(master[0])
    front.write_bytes(front_png)
    for name, path in paths.items():
        if digest(path.read_bytes()) != hashes[name]:
            issues.append(f"PDF changed during comparison: {name}.")
    audit = {
        "schema_version": 1,
        "audit_completed_utc": datetime.now(timezone.utc).isoformat(),
        "master_pdf": paths[MASTER].relative_to(PROJECT).as_posix(),
        "master_pdf_sha256": hashes[MASTER], "master_page_count": len(master),
        "apparatus_pdf": paths[APPARATUS].relative_to(PROJECT).as_posix(),
        "apparatus_pdf_sha256": hashes[APPARATUS], "apparatus_page_count": len(apparatus),
        "renderer": {"library": "PyMuPDF", "version": fitz.VersionBind, "dpi": 144,
                     "matrix_scale": 2.0, "colorspace": "RGB", "alpha": False,
                     "comparison": "Direct byte equality of row-major RGB samples and losslessly encoded PNG bytes; geometry and dimensions checked separately"},
        "scope": "Every physical page from 2 through the end; page 1 is the distinct front and requires a direct current-PDF image opening.",
        "page_count_identical": len(master) == len(apparatus),
        "all_body_pages_compared": len(pages) == len(master) - 1 == len(apparatus) - 1,
        "all_body_pages_byte_identical": not issues,
        "body_pages_compared": len(pages),
        "direct_image_openings_claimed": 0,
        "master_front": {"page": 1, "image": front.relative_to(PROJECT).as_posix(),
                         "image_sha256": digest(front_png), "raster_dpi": 144,
                         "signature": front_signature, "viewed": False},
        "integrity_issues": issues, "audit_complete": not issues, "pages": pages,
    }
    audit_path = PROJECT / "records/MASTER_APPARATUS_RASTER_EQUIVALENCE.json"
    write_json(audit_path, audit)
    selection = {
        "pdf": paths[MASTER].relative_to(PROJECT).as_posix(), "pdf_sha256": hashes[MASTER],
        "pdf_pages": len(master), "systematic_sample_pages": [],
        "body_equivalence_audit": audit_path.relative_to(PROJECT).as_posix(),
        "body_equivalence_audit_sha256": digest(audit_path.read_bytes()),
        "selections": [{"pdf": paths[MASTER].relative_to(PROJECT).as_posix(),
                        "pdf_sha256": hashes[MASTER], "page": 1,
                        "key": "distinct annotated-master title/front matter",
                        "image": front.relative_to(PROJECT).as_posix(), "raster_dpi": 144,
                        "reasons": ["direct inspection of the distinct master front"], "viewed": False}],
    }
    write_json(PROJECT / "records" / ("QA_SELECTION_" + MASTER + ".json"), selection)
    print(json.dumps({"audit": audit_path.relative_to(PROJECT).as_posix(),
                      "audit_complete": audit["audit_complete"],
                      "body_pages_compared": len(pages), "issues": issues,
                      "master_front_to_open": front.relative_to(PROJECT).as_posix()}), flush=True)
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
