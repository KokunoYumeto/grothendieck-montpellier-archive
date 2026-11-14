#!/usr/bin/env python3
"""Hash the exact inputs and outputs of the cumulative build reports.

Paths in the proof are relative to the records ZIP. A changed ledger, PDF,
compiled-source dependency, report output, or matching-file inventory makes the
proof stale. The release audit remains responsible for validating the evidence
and the substantive compile and review gates.
"""
from __future__ import annotations
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path, PurePosixPath

EDITION = Path(__file__).resolve().parents[1]
PROOF = "records/BUILD_REPORT_PROVENANCE.json"
OUTPUTS = (
    "CLEANUP_LOG.tsv", "TYPESETTING_FIXES.tsv", "TYPESETTING_REPORT.md",
    "records/COMPILE_SUMMARY.tsv", "APPARATUS_COUNTS.md",
)
FIXED_INPUTS = (
    "scripts/generate_build_reports.py", "scripts/build_report_provenance.py",
    "scripts/edition_core.py", "records/CLEANUP_LOG_all.tsv",
    "records/TYPESETTING_PATCHES.json", "records/PDF_VISUAL_REVIEW.tsv",
    "records/PDF_GEOMETRY_REVIEW.tsv", "records/PDF_VISUAL_EQUIVALENCE.tsv",
    "records/PDF_REVIEW_FREEZES.tsv",
)
INPUT_GLOBS = (
    "records/TYPESETTING_FIXES_*.tsv", "records/READER_INVENTORY_*.tsv",
    "build/*/audit/report.json", "build/*/audit/BUILD_HISTORY.tsv",
    "build/*/*.log", "build/*/pass_*.stdout.txt",
    "variant_records/*.json", "master_pages/en/*.tex",
)


def relative_path(value):
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or "\\" in value:
        raise ValueError("Build-report input paths must be ZIP-relative.")
    return path.as_posix()


def filehash(path):
    if not path.is_file():
        return None
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def capture_inputs(edition=EDITION):
    file_sets = {
        pattern: sorted(p.relative_to(edition).as_posix()
                        for p in edition.glob(pattern) if p.is_file())
        for pattern in INPUT_GLOBS
    }
    names = set(FIXED_INPUTS)
    for members in file_sets.values():
        names.update(members)
    for relative in file_sets["build/*/audit/report.json"]:
        report = json.loads((edition / relative).read_text())
        names.add(relative_path(report["source"]))
        name = report["reader"]
        if not name.replace("_", "").isalnum():
            raise ValueError("Invalid reader name in build-report inputs.")
        folder = PurePosixPath(relative).parent.parent
        names.add((folder / (name + ".pdf")).as_posix())
        names.update(relative_path(p) for p in report.get("source_files_sha256", {}))
        digest = report.get("pdf_sha256", "")
        if digest and len(digest) == 64 and all(c in "0123456789abcdef" for c in digest):
            names.add(f"build/visual_review/{name}/{digest}/manifest.json")
    return {
        "inputs": {relative: filehash(edition / relative) for relative in sorted(names)},
        "file_sets": file_sets,
    }


def differences(before, after):
    changed = []
    for field in ("inputs", "file_sets"):
        left, right = before.get(field, {}), after.get(field, {})
        for key in sorted(set(left) | set(right)):
            if key not in left or key not in right or left[key] != right[key]:
                changed.append(field + ": " + key)
    return changed


def seal_reports(before, edition=EDITION):
    after = capture_inputs(edition)
    changed = differences(before, after)
    if changed:
        raise SystemExit("Build-report inputs changed during generation; rerun after the current writes finish: "
                         + "; ".join(changed))
    outputs = {relative: filehash(edition / relative) for relative in OUTPUTS}
    missing = [name for name, digest in outputs.items() if digest is None]
    if missing:
        raise SystemExit("Cumulative report outputs are missing: " + ", ".join(missing))
    record = dict(schema_version=1, generated_utc=datetime.now(timezone.utc).isoformat(),
                  generator="scripts/generate_build_reports.py", **after, outputs=outputs,
                  scope="Exact input and output bytes, plus matching-file inventories. Visual evidence and release requirements are validated separately by audit_release.py.")
    path = edition / PROOF
    temporary = path.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(path)
    return record


def verify_reports(edition=EDITION):
    path = edition / PROOF
    if not path.is_file():
        return {"passed": False, "issues": ["Cumulative build-report provenance is absent."],
                "provenance": PROOF}
    try:
        record = json.loads(path.read_text())
        issues = []
        if record.get("schema_version") != 1 or record.get("generator") != "scripts/generate_build_reports.py":
            issues.append("Unrecognized build-report provenance schema or generator.")
        if not record.get("generated_utc"):
            issues.append("Build-report generation time is absent.")
        current = capture_inputs(edition)
        issues += ["Changed report input: " + item for item in differences(record, current)]
        expected = record.get("outputs", {})
        if set(expected) != set(OUTPUTS):
            issues.append("Cumulative report output coverage differs.")
        for relative in OUTPUTS:
            digest = filehash(edition / relative)
            if digest is None or expected.get(relative) != digest:
                issues.append("Changed or missing cumulative report: " + relative)
        return {"passed": not issues, "issues": issues, "provenance": PROOF,
                "generated_utc": record.get("generated_utc"),
                "inputs": len(current["inputs"]), "outputs": len(OUTPUTS)}
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return {"passed": False, "issues": ["Build-report provenance could not be validated (" + type(exc).__name__ + ")."],
                "provenance": PROOF}
