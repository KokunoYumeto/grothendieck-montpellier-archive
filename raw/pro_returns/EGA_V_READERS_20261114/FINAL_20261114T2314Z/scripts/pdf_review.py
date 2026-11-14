#!/usr/bin/env python3
"""Freeze, render, and record actual page inspections against an exact PDF hash.

Rendering creates review images; it never creates a successful inspection record.
The record command accepts observations only after the reviewer has viewed them.
All paths written to the documentary records are edition-relative.
"""
from __future__ import annotations
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
from pathlib import Path
import re
import fitz
from edition_core import read_tsv, write_tsv, sha256

EDITION = Path(__file__).resolve().parents[1]
FIELDS = ("text_outside_sheet", "text_outside_permitted_area",
          "vector_paths_outside_sheet", "vector_paths_outside_permitted_area",
          "images_outside_sheet", "images_outside_permitted_area")
FREEZES = EDITION / "records/PDF_REVIEW_FREEZES.tsv"
REVIEW = EDITION / "records/PDF_VISUAL_REVIEW.tsv"
GEOMETRY = EDITION / "records/PDF_GEOMETRY_REVIEW.tsv"


def filehash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rows(path):
    return read_tsv(path) if path.is_file() else []


def write_table(path, records):
    fields = list(dict.fromkeys(key for row in records for key in row))
    write_tsv(path, records, fields)


@contextmanager
def lock():
    with (EDITION / "records/PDF_REVIEW.lock").open("a") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def paths(name):
    if not re.fullmatch(r"[A-Za-z0-9_]+", name):
        raise SystemExit("Invalid reader name.")
    out = EDITION / "build" / name
    return out / (name + ".pdf"), out / "audit/report.json"


def load_current(name, frozen=True):
    pdf, report_path = paths(name)
    report = json.loads(report_path.read_text())
    digest = filehash(pdf)
    if report.get("pdf_sha256") != digest:
        raise SystemExit("PDF differs from its compile report; regenerate the report.")
    active = [r for r in rows(FREEZES) if r["reader"] == name and r["status"] == "active"]
    if frozen and (len(active) != 1 or active[0]["pdf_sha256"] != digest):
        raise SystemExit("This exact PDF has no active review freeze.")
    return pdf, report, digest


def manifest_path(name, digest):
    return EDITION / "build/visual_review" / name / digest / "manifest.json"


def freeze(name):
    pdf, report, digest = load_current(name, frozen=False)
    source = EDITION / report["source"]
    body = source.read_text()
    if sha256(body) != report.get("source_sha256"):
        raise SystemExit("Reader source differs from its compiled version.")
    if not report.get("mechanical_gates_passed"):
        raise SystemExit("Mechanical compile gates must pass before a final review freeze.")
    if re.search(r"INCOMPLETE CHECKPOINT|UNCHECKED DEVELOPMENT BUILD|not yet checked by eye", body):
        raise SystemExit("Working or obsolete unchecked labels remain.")
    stale = [p for p, h in report.get("source_files_sha256", {}).items()
             if not (EDITION / p).is_file() or sha256((EDITION / p).read_text()) != h]
    if stale:
        raise SystemExit("Build inputs have changed; revalidate or rebuild before freezing.")
    with lock():
        ledger = rows(FREEZES)
        active = [r for r in ledger if r["reader"] == name and r["status"] == "active"]
        if active and any(r["pdf_sha256"] != digest for r in active):
            raise SystemExit("An older PDF is frozen. Release it with a recorded reason before freezing a replacement.")
        if not active:
            ledger.append(dict(reader=name, pdf_sha256=digest, source_sha256=report["source_sha256"],
                frozen_utc=datetime.now(timezone.utc).isoformat(), status="active", released_utc="", reason=""))
            write_tsv(FREEZES, ledger)
        manifest = manifest_path(name, digest)
        manifest.parent.mkdir(parents=True, exist_ok=True)
        if not manifest.is_file():
            content = dict(reader=name, pdf_sha256=digest, pdf=str(pdf.relative_to(EDITION)),
                pdf_pages=report["pdf_pages"], source_sha256=report["source_sha256"],
                evenly_spread_sample_pages=report["evenly_spread_sample_pages"],
                landscape_pages=report["landscape_pages"],
                historical_overflow_source_keys=report["historical_overflow_source_keys"],
                margin_line_limit_review_source_keys=report.get("margin_line_limit_review_source_keys",[]),
                required_visual_review_pages=report["required_visual_review_pages"],
                source_physical_pages=report["source_physical_pages"],
                geometry_flags={field: report.get(field, []) for field in FIELDS},
                images={}, note="Images and sample lists do not establish that an inspection has occurred.")
            manifest.write_text(json.dumps(content, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(dict(reader=name, pdf_sha256=digest,
        manifest=str(manifest.relative_to(EDITION)), required_pages=report["required_visual_review_pages"])))


def release(name, reason):
    with lock():
        ledger = rows(FREEZES)
        found = False
        for row in ledger:
            if row["reader"] == name and row["status"] == "active":
                row.update(status="released for revision", released_utc=datetime.now(timezone.utc).isoformat(), reason=reason)
                found = True
        if not found:
            raise SystemExit("No active freeze exists for this reader.")
        write_tsv(FREEZES, ledger)
    print("Released the review freeze with a recorded reason: " + name)


def parse_pages(value, manifest):
    if value == "required":
        return manifest["required_visual_review_pages"]
    pages = set()
    for component in value.split(","):
        numbers = component.strip().split("-")
        if len(numbers) == 1:
            pages.add(int(numbers[0]))
        elif len(numbers) == 2:
            a, b = map(int, numbers)
            if b < a:
                raise SystemExit("Invalid reversed page range.")
            pages.update(range(a, b + 1))
        else:
            raise SystemExit("Use a comma-separated list of page numbers or ranges.")
    if not pages or min(pages) < 1 or max(pages) > manifest["pdf_pages"]:
        raise SystemExit("A requested page lies outside this PDF.")
    return sorted(pages)


def latest_reviews(name, digest):
    latest = {}
    for row in rows(REVIEW):
        if row["reader"] == name and row["pdf_sha256"] == digest:
            latest[int(row["pdf_page"])] = row
    return latest


def list_pages(name, pending=False):
    _, report, digest = load_current(name)
    manifest = json.loads(manifest_path(name, digest).read_text())
    latest = latest_reviews(name, digest)
    starts = sorted((p, k) for k, p in report["source_physical_pages"].items())
    result = []
    pages=set(manifest["required_visual_review_pages"])
    pages.update(n for n,row in latest.items() if row.get("result")=="layout issue found")
    for number in sorted(pages):
        reviewed = latest.get(number, {})
        if pending and reviewed.get("result", "").startswith("layout inspection passed"):
            continue
        source = next((key for page, key in reversed(starts) if page <= number), "frontmatter")
        reasons = []
        if number in manifest["evenly_spread_sample_pages"]:
            reasons.append("evenly spread sample")
        if number in manifest["landscape_pages"]:
            reasons.append("landscape")
        if source in manifest["historical_overflow_source_keys"]:
            reasons.append("historical overflow or local typesetting repair")
        if source in report.get("margin_line_limit_review_source_keys",[]):
            reasons.append("four-line marginal-note routing repair")
        flags = [field for field in FIELDS if any(r["pdf_page"] == number for r in report.get(field, []))]
        result.append(dict(pdf_page=number, source_key=source, reasons=reasons, geometry_flags=flags,
            review=reviewed.get("result", "pending")))
    print(json.dumps(dict(reader=name, pdf_sha256=digest, pages=result), ensure_ascii=False, indent=2))


def render(name, selection, dpi):
    pdf, _, digest = load_current(name)
    manifest_file = manifest_path(name, digest)
    manifest = json.loads(manifest_file.read_text())
    doc = fitz.open(pdf)
    result = []
    for number in parse_pages(selection, manifest):
        path = manifest_file.parent / f"p{number:03}.png"
        prior = manifest["images"].get(str(number))
        if prior:
            if not path.is_file() or filehash(path) != prior["sha256"]:
                raise SystemExit("A previously rendered inspection image changed.")
        else:
            doc[number - 1].get_pixmap(dpi=dpi, alpha=False).save(path)
            manifest["images"][str(number)] = dict(path=str(path.relative_to(EDITION)),
                sha256=filehash(path), dpi=dpi)
        result.append(dict(pdf_page=number, image=str(path.relative_to(EDITION))))
    # The same reader is rendered sequentially; different readers have separate manifests.
    manifest_file.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(dict(reader=name, pdf_sha256=digest, images=result)))


def record(name, observations):
    _, report, digest = load_current(name)
    manifest = json.loads(manifest_path(name, digest).read_text())
    data = json.loads(Path(observations).read_text())
    if data.get("reader") != name or data.get("pdf_sha256") != digest:
        raise SystemExit("Observation file does not identify this exact frozen PDF.")
    if not data.get("reviewer") or not data.get("observations"):
        raise SystemExit("Explicit reviewer and page observations are required.")
    visual_rows = []
    geometry_rows = []
    starts = sorted((p, k) for k, p in report["source_physical_pages"].items())
    for observation in data["observations"]:
        number = int(observation["pdf_page"])
        image = manifest["images"].get(str(number))
        if not image or not (EDITION / image["path"]).is_file():
            raise SystemExit("Render every page before recording its inspection.")
        if filehash(EDITION / image["path"]) != image["sha256"]:
            raise SystemExit("Inspection image hash changed.")
        findings = observation.get("findings", "").strip()
        result = observation.get("result", "")
        if not findings or result not in ("layout inspection passed", "layout issue found"):
            raise SystemExit("Every page needs concrete findings and an explicit passed/issue result.")
        source = next((key for page, key in reversed(starts) if page <= number), "frontmatter")
        visual_rows.append(dict(reader=name, pdf_sha256=digest, pdf_page=number, source_key=source,
            image=image["path"], image_sha256=image["sha256"], reviewed_utc=datetime.now(timezone.utc).isoformat(),
            reviewer=data["reviewer"], findings=findings, result=result))
        for flag in observation.get("geometry", []):
            field = flag["flag_kind"]
            if field not in FIELDS or not any(r["pdf_page"] == number for r in report.get(field, [])):
                raise SystemExit("Geometry disposition has no matching automated page flag.")
            permitted = ("single-letter-overhang",) if field == "text_outside_permitted_area" else ("conservative-rectangle-no-visible-overflow",)
            if flag.get("decision") not in permitted or not flag.get("reason", "").strip():
                raise SystemExit("Geometry requires an admissible, explained visual disposition; repair actual overflow.")
            geometry_rows.append(dict(reader=name, pdf_sha256=digest, pdf_page=number,
                flag_kind=field, decision=flag["decision"], reason=flag["reason"],
                reviewer=data["reviewer"], reviewed_utc=datetime.now(timezone.utc).isoformat()))
    with lock():
        write_table(REVIEW, rows(REVIEW) + visual_rows)
        if geometry_rows:
            write_table(GEOMETRY, rows(GEOMETRY) + geometry_rows)
    print(f"Recorded {len(visual_rows)} explicit page inspections and {len(geometry_rows)} geometry dispositions.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("freeze", "list", "render", "record", "release"):
        part = sub.add_parser(command)
        part.add_argument("reader")
        if command == "list":
            part.add_argument("--pending", action="store_true")
        if command == "render":
            part.add_argument("--pages", default="required")
            part.add_argument("--dpi", type=int, default=160)
        if command == "record":
            part.add_argument("--observations", required=True)
        if command == "release":
            part.add_argument("--reason", required=True)
    args = parser.parse_args()
    if args.command == "freeze": freeze(args.reader)
    elif args.command == "release": release(args.reader, args.reason)
    elif args.command == "list": list_pages(args.reader, args.pending)
    elif args.command == "render": render(args.reader, args.pages, args.dpi)
    elif args.command == "record": record(args.reader, args.observations)


if __name__ == "__main__":
    main()
