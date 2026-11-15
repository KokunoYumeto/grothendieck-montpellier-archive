"""Carry actual image observations across PDFs only by verified raster identity.

Every old/new PDF page is compared at 144 dpi, with exact page geometry and
page-count checks. A carried observation additionally requires the retained
old PNG and current PNG to match their respective PDF renders at the original
1.4 scale, and any previously recorded PNG SHA-256 to match the retained file.
This script never claims that a current image was opened by a reviewer.

Example:
    python3 scripts/carry_forward_visual_qa.py PS_GUIDE \
        --old-pdf qa/pre_final_visual_repairs/PS_GUIDE.pdf \
        --old-image-dir qa/rendered/final_PS_GUIDE_acdf3a8a
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

import fitz
from PIL import Image


PROJECT = Path(__file__).resolve().parents[1]
METHOD = "raster identity with an actually opened image"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(PROJECT))


def project_path(value: str) -> Path:
    path = (PROJECT / value).resolve()
    path.relative_to(PROJECT)
    return path


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(path)


def preserve_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != data:
            raise RuntimeError(f"Refusing to alter a preserved evidence snapshot: {relative(path)}")
    else:
        path.write_bytes(data)


def rows_from(data: object) -> list[dict]:
    return data if isinstance(data, list) else data.get("entries", [])


def row_hash(row: dict, data: object) -> str | None:
    return row.get("pdf_sha256") or (data.get("pdf_sha256") if isinstance(data, dict) else None)


def actual_observation(row: dict) -> bool:
    return (
        row.get("viewed") is True
        and bool(row.get("observation", "").strip())
        and row.get("inspection_method") != METHOD
        and row.get("direct_image_opened") is not False
        and row.get("image_opened") is not False
        and row.get("status", "pass") not in {"issue", "fail", "failed", "unresolved"}
    )


def geometry(page: fitz.Page) -> dict:
    return {
        "rect_pt": list(page.rect),
        "mediabox_pt": list(page.mediabox),
        "cropbox_pt": list(page.cropbox),
        "rotation": page.rotation,
    }


def pixel_signature(width: int, height: int, samples: bytes) -> dict:
    return {"width_px": width, "height_px": height, "colorspace": "RGB", "pixels_sha256": sha256(samples)}


def render(page: fitz.Page, scale: float) -> tuple[fitz.Pixmap, dict]:
    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), colorspace=fitz.csRGB, alpha=False)
    return pix, pixel_signature(pix.width, pix.height, pix.samples)


def read_png(path: Path) -> tuple[str, dict]:
    raw = path.read_bytes()
    with Image.open(path) as im:
        im.load()
        if im.mode != "RGB":
            raise ValueError(f"Expected the original RGB image: {relative(path)} ({im.mode})")
        signature = pixel_signature(im.width, im.height, im.tobytes())
    return sha256(raw), signature


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stem")
    parser.add_argument("--old-pdf", required=True)
    parser.add_argument("--old-image-dir", required=True)
    parser.add_argument("--new-pdf")
    parser.add_argument("--selection")
    args = parser.parse_args()
    old_pdf = project_path(args.old_pdf)
    new_pdf = project_path(args.new_pdf or f"readers/{args.stem}.pdf")
    old_images = project_path(args.old_image_dir)
    new_images = project_path(f"qa/rendered/final_{args.stem}")
    if old_images == new_images:
        raise ValueError("Retained old images must have a distinct versioned directory.")
    old_bytes, new_bytes = old_pdf.read_bytes(), new_pdf.read_bytes()
    old_sha, new_sha = sha256(old_bytes), sha256(new_bytes)
    if old_sha == new_sha:
        raise ValueError("PDF bytes are unchanged; existing direct evidence already applies.")
    old_doc = fitz.open(stream=old_bytes, filetype="pdf")
    new_doc = fitz.open(stream=new_bytes, filetype="pdf")
    selection_path = project_path(args.selection or f"records/QA_SELECTION_{args.stem}.json")
    selection = json.loads(selection_path.read_text())
    if selection["pdf_sha256"] != new_sha:
        raise ValueError("Current selection does not identify the current PDF.")
    chosen = {int(row["page"]): row for row in selection["selections"]}
    if selection.get("pdf_pages") != len(new_doc) or any(n < 1 or n > len(new_doc) for n in chosen):
        raise ValueError("Current selection page numbers/count do not match the current PDF.")
    archive = PROJECT / "records/historical_visual_qa" / f"{args.stem}_{old_sha[:12]}"
    audit_path = PROJECT / "records" / f"RASTER_EQUIVALENCE_{args.stem}_{old_sha[:8]}_{new_sha[:8]}.json"
    output_path = PROJECT / "records" / f"FINAL_VISUAL_QA_{args.stem}_raster_equivalence.json"
    candidates: dict[int, list[dict]] = defaultdict(list)
    current_direct: dict[int, list[dict]] = defaultdict(list)
    sources, normalized_records = [], []
    issues = []

    # Freeze source evidence as byte-for-byte snapshots before creating new rows.
    for evidence in sorted((PROJECT / "records").glob("FINAL_VISUAL_QA_*.json")):
        raw = evidence.read_bytes()
        data = json.loads(raw)
        old_rows = []
        for index, row in enumerate(rows_from(data)):
            if not actual_observation(row):
                continue
            source_sha = row_hash(row, data)
            if source_sha == new_sha:
                current_direct[int(row["page"])].append({"row": row, "file": relative(evidence), "entry_index": index})
            if source_sha != old_sha:
                continue
            page = int(row["page"])
            archived_image = old_images / f"page_{page:04d}.png"
            original_snapshot = archive / "original" / evidence.name
            normalized_path = archive / "normalized" / evidence.name
            item = {
                "row": row,
                "file": relative(evidence),
                "file_sha256": sha256(raw),
                "entry_index": index,
                "original_snapshot": relative(original_snapshot),
                "normalized_record": relative(normalized_path),
                "old_image": relative(archived_image),
            }
            candidates[page].append(item)
            old_rows.append(item)
        if old_rows:
            preserve_bytes(archive / "original" / evidence.name, raw)
            sources.append({
                "original_evidence_file": relative(evidence),
                "original_evidence_file_sha256": sha256(raw),
                "preserved_original": relative(archive / "original" / evidence.name),
                "normalized_archive": relative(archive / "normalized" / evidence.name),
                "actual_observation_rows": len(old_rows),
            })
            normalized_records.append((archive / "normalized" / evidence.name, old_rows))

    count_equal = len(old_doc) == len(new_doc)
    geom_equal = count_equal and all(geometry(old_doc[i]) == geometry(new_doc[i]) for i in range(len(old_doc)))
    if not count_equal:
        issues.append("Page counts differ; no observations may be carried by page number.")
    if not geom_equal:
        issues.append("Page geometry differs; no observations may be carried by page number.")
    pages = []
    changed = []
    validated_candidates: dict[int, list[dict]] = defaultdict(list)
    verified_current_direct = set()
    carried = []
    compare_at_original_scale = set(chosen) | set(candidates) | set(current_direct)

    for number in range(1, max(len(old_doc), len(new_doc)) + 1):
        old_page = old_doc[number - 1] if number <= len(old_doc) else None
        new_page = new_doc[number - 1] if number <= len(new_doc) else None
        page_record = {"page": number, "old_geometry": geometry(old_page) if old_page else None,
                       "new_geometry": geometry(new_page) if new_page else None}
        old144 = render(old_page, 2.0)[1] if old_page else None
        new144 = render(new_page, 2.0)[1] if new_page else None
        same144 = old144 is not None and old144 == new144
        page_record.update(old_144dpi=old144, new_144dpi=new144,
                           geometry_identical=page_record["old_geometry"] == page_record["new_geometry"],
                           pixels_identical_144dpi=same144)
        if not same144 or not page_record["geometry_identical"]:
            changed.append(number)
        needs_original_scale = number in compare_at_original_scale or not same144 or not page_record["geometry_identical"]
        if needs_original_scale and old_page is not None and new_page is not None:
            oldpix, old14 = render(old_page, 1.4)
            newpix, new14 = render(new_page, 1.4)
            page_record.update(old_scale_1_4=old14, new_scale_1_4=new14, pixels_identical_scale_1_4=old14 == new14)
            if old14 != new14 and number not in changed:
                changed.append(number)
            old_image = old_images / f"page_{number:04d}.png"
            current_image = project_path(chosen[number]["image"]) if number in chosen else new_images / f"page_{number:04d}.png"
            old_png_sha = None
            old_png_matches = False
            if old_image.exists():
                old_png_sha, old_png_pixels = read_png(old_image)
                old_png_matches = old_png_pixels == old14
                page_record["retained_old_png"] = {
                    "image": relative(old_image), "image_sha256": old_png_sha,
                    "pixels": old_png_pixels, "matches_old_pdf_scale_1_4": old_png_matches,
                }
            elif number in candidates:
                issues.append(f"Missing retained actual-view image for page {number}.")
            if not current_image.exists():
                current_image.parent.mkdir(parents=True, exist_ok=True)
                newpix.save(current_image)
                page_record["current_png_rendered_by_this_audit"] = True
            new_png_sha, new_png_pixels = read_png(current_image)
            new_png_matches = new_png_pixels == new14
            page_record["current_png"] = {
                "image": relative(current_image), "image_sha256": new_png_sha,
                "pixels": new_png_pixels, "matches_current_pdf_scale_1_4": new_png_matches,
            }
            if not new_png_matches:
                issues.append(f"Current PNG does not match current PDF on page {number}.")
            for item in candidates.get(number, []):
                recorded_png_sha = item["row"].get("image_sha256")
                recorded_matches = recorded_png_sha is None or recorded_png_sha == old_png_sha
                item["image_verification"] = {
                    "retained_image_sha256": old_png_sha,
                    "previously_recorded_image_sha256": recorded_png_sha,
                    "previously_recorded_hash_present": recorded_png_sha is not None,
                    "previously_recorded_hash_matches": recorded_matches if recorded_png_sha is not None else None,
                    "retained_png_matches_old_pdf_scale_1_4": old_png_matches,
                }
                item["valid"] = bool(old_png_matches and recorded_matches)
                if item["valid"]:
                    validated_candidates[number].append(item)
                else:
                    issues.append(f"Retained image integrity failed for page {number}, {item['file']} entry {item['entry_index']}.")
            for item in current_direct.get(number, []):
                row = item["row"]
                recorded = row.get("image_sha256")
                row_image = project_path(row["image"])
                try:
                    actual_sha, actual_pixels = read_png(row_image)
                    valid = actual_pixels == new14 and (recorded is None or recorded == actual_sha)
                except (OSError, ValueError):
                    valid = False
                if valid:
                    verified_current_direct.add(number)
            valid_sources = validated_candidates.get(number, [])
            if count_equal and geom_equal and same144 and old14 == new14 and new_png_matches and valid_sources:
                source = valid_sources[0]
                prior = source["row"]
                row = dict(chosen.get(number, {}))
                row.update({
                    "pdf": relative(new_pdf), "pdf_sha256": new_sha, "page": number,
                    "image": relative(current_image), "image_sha256": new_png_sha,
                    "key": row.get("key", prior.get("key")),
                    "viewed": True, "status": "pass", "image_opened": False,
                    "direct_image_opened": False, "inspection_method": METHOD,
                    "observation": "Current page verified pixel-identical at 144 dpi and the original 1.4 image scale. Prior actual-image observation: " + prior["observation"],
                    "prior_actual_image_observation": prior["observation"],
                    "provenance": {
                        "source_evidence_file": source["file"],
                        "source_evidence_file_sha256": source["file_sha256"],
                        "source_entry_index": source["entry_index"],
                        "preserved_original_evidence_file": source["original_snapshot"],
                        "normalized_historical_evidence_file": source["normalized_record"],
                        "old_pdf": relative(old_pdf), "old_pdf_sha256": old_sha,
                        "old_image": relative(old_image), "old_image_sha256": old_png_sha,
                        "old_image_verification": source["image_verification"],
                        "prior_reviewer": prior.get("reviewer"),
                        "equivalence_audit": relative(audit_path),
                        "page_pixels_sha256_144dpi": new144["pixels_sha256"],
                        "page_pixels_sha256_scale_1_4": new14["pixels_sha256"],
                    },
                })
                carried.append(row)
            del oldpix, newpix
        pages.append(page_record)
        if number % 50 == 0 or number == max(len(old_doc), len(new_doc)):
            print(json.dumps({"stem": args.stem, "compared_pages": number, "total_pages": max(len(old_doc), len(new_doc)), "changed_so_far": len(changed)}), flush=True)

    for destination, items in normalized_records:
        normalized = []
        for item in items:
            row = dict(item["row"])
            row.update({
                "original_pdf_path": row.get("pdf"), "pdf": relative(old_pdf),
                "original_image_path": row.get("image"), "image": item["old_image"],
                "original_evidence_file": item["file"],
                "original_evidence_file_sha256": item["file_sha256"],
                "preserved_original_evidence_file": item["original_snapshot"],
                "image_integrity_verification": item.get("image_verification"),
            })
            if item.get("image_verification", {}).get("retained_image_sha256"):
                row["image_sha256"] = item["image_verification"]["retained_image_sha256"]
            normalized.append(row)
        write_json(destination, {"pdf": relative(old_pdf), "pdf_sha256": old_sha, "entries": normalized})

    if sha256(old_pdf.read_bytes()) != old_sha or sha256(new_pdf.read_bytes()) != new_sha:
        issues.append("A PDF changed while this audit was running; carry-forward is invalid.")
        carried = []
    if json.loads(selection_path.read_text())["pdf_sha256"] != new_sha:
        issues.append("Page selection changed while this audit was running; carry-forward is invalid.")
        carried = []
    inherited_pages = {row["page"] for row in carried}
    timestamp = datetime.now(timezone.utc).isoformat()
    audit = {
        "audit_completed_utc": timestamp,
        "old_pdf": relative(old_pdf), "old_pdf_sha256": old_sha,
        "new_pdf": relative(new_pdf), "new_pdf_sha256": new_sha,
        "old_page_count": len(old_doc), "new_page_count": len(new_doc),
        "page_count_identical": count_equal, "all_page_geometry_identical": geom_equal,
        "all_pages_compared_144dpi": len(pages) == max(len(old_doc), len(new_doc)),
        "renderer": {"library": "PyMuPDF", "version": fitz.VersionBind, "dpi": 144,
                     "matrix_scale": 2.0, "original_image_scale": 1.4, "colorspace": "RGB", "alpha": False,
                     "pixel_hash_definition": "SHA-256 of decoded row-major RGB samples; dimensions compared separately"},
        "evidence_sources": sources,
        "old_actual_observation_rows": sum(len(v) for v in candidates.values()),
        "old_actually_opened_pages": sorted(candidates),
        "old_actual_pages_with_verified_retained_images": sorted(validated_candidates),
        "current_directly_opened_pages_with_verified_images": sorted(verified_current_direct),
        "inherited_raster_identity_pages": sorted(inherited_pages),
        "changed_pages": changed,
        "changed_pages_requiring_fresh_opening": sorted(set(changed) - verified_current_direct),
        "selected_pages_requiring_fresh_opening": sorted(set(chosen) - inherited_pages - verified_current_direct),
        "integrity_issues": issues,
        "audit_complete": not issues,
        "pages": pages,
    }
    write_json(audit_path, audit)
    audit_sha = sha256(audit_path.read_bytes())
    for row in carried:
        row["provenance"]["equivalence_audit_sha256"] = audit_sha
        row["provenance"]["old_page"] = row["page"]
        row["provenance"]["preserved_original_evidence_file_sha256"] = row["provenance"]["source_evidence_file_sha256"]
    write_json(archive / "MANIFEST.json", {
        "old_pdf": relative(old_pdf), "old_pdf_sha256": old_sha,
        "retained_image_directory": relative(old_images), "source_evidence": sources,
        "equivalence_audit": relative(audit_path),
        "preservation_note": "Original snapshots preserve exact record bytes. Normalized copies resolve image and PDF paths to retained old versions; no historical observation is relabeled as a direct current-image opening.",
    })
    write_json(output_path, {
        "pdf": relative(new_pdf), "pdf_sha256": new_sha,
        "inspection_method": METHOD,
        "direct_current_image_openings_claimed": 0,
        "equivalence_audit": relative(audit_path),
        "equivalence_audit_sha256": audit_sha,
        "entries": carried,
    })
    print(json.dumps({
        "audit": relative(audit_path), "evidence": relative(output_path), "audit_complete": not issues,
        "inherited_pages": len(inherited_pages), "changed_pages": changed,
        "changed_pages_requiring_fresh_opening": audit["changed_pages_requiring_fresh_opening"],
        "selected_pages_requiring_fresh_opening": audit["selected_pages_requiring_fresh_opening"],
        "integrity_issues": issues,
    }), flush=True)
    return 0 if not issues else 1


if __name__ == "__main__":
    sys.exit(main())
