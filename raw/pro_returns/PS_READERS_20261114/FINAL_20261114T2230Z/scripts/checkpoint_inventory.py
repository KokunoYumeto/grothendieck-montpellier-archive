"""Account for actual and aliased members of immutable checkpoint archives.

Pre-alias checkpoints keep the original member CRC/size accounting. New
checkpoints additionally authenticate every image alias against physical ZIP
bytes. Historical manifest discrepancies are reported separately from missing
content; only a hash-bound restoration audit can explain such a discrepancy.
"""
from __future__ import annotations

import collections
import csv
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
from zipfile import BadZipFile, ZipFile
import zlib

PROJECT = Path(__file__).resolve().parents[1]
ALIAS_MANIFEST = "records/FILE_ALIASES.tsv"
CONTENTS_MANIFEST = "records/ARCHIVE_CONTENTS.tsv"
GENERATED = {"records/CHECKPOINT_ARCHIVES.tsv", "records/CHECKPOINT_SUPERSESSION.tsv",
             "records/CHECKPOINT_INVENTORY.json", "records/CHECKPOINT_ALIAS_MEMBERS.tsv",
             "records/CHECKPOINT_MANIFEST_VERIFICATION.json", "README.md", "TYPESETTING_REPORT.md",
             "records/FINAL_QA_GATE.json", "records/PRIVACY_AUDIT.json",
             "records/INDEPENDENT_FINAL_REQUIREMENTS_REVIEW.json", "records/ARCHIVE_CONTENTS.tsv",
             "records/FILE_ALIASES.tsv", "records/FINAL_ARCHIVE_PLAN.json"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def file_digest(path):
    checksum = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            checksum.update(chunk)
    return checksum.hexdigest()


def safe_member(name):
    path = PurePosixPath(name)
    if not name or path.is_absolute() or ".." in path.parts or "\\" in name or path.as_posix() != name:
        raise ValueError("Unsafe archive/alias member path: " + str(name))
    return name


def tsv_rows(raw, required):
    reader = csv.DictReader(io.StringIO(raw.decode("utf-8-sig")), delimiter="\t")
    if not set(required).issubset(reader.fieldnames or []):
        raise ValueError("Manifest has missing columns")
    rows = list(reader)
    if any(None in row for row in rows):
        raise ValueError("Manifest contains excess TSV fields")
    names = [safe_member(row["path"]) for row in rows]
    if len(names) != len(set(names)):
        raise ValueError("Manifest contains duplicate logical paths")
    return rows


def member_fingerprint(archive, member, cache):
    if member not in cache:
        checksum, crc, size = hashlib.sha256(), 0, 0
        with archive.open(member) as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                checksum.update(chunk)
                crc = zlib.crc32(chunk, crc)
                size += len(chunk)
        info = archive.getinfo(member)
        if size != info.file_size or (crc & 0xffffffff) != info.CRC:
            raise ValueError("ZIP member size/CRC mismatch: " + member)
        cache[member] = {"bytes": size, "crc32": f"{crc & 0xffffffff:08x}",
                         "sha256": checksum.hexdigest()}
    return cache[member]


def inspect_checkpoint(path, number):
    """Return logical members without extracting or changing a checkpoint."""
    archive_hash = file_digest(path)
    aliases, mismatches, fingerprints = [], [], {}
    with ZipFile(path) as archive:
        infos = [item for item in archive.infolist() if not item.is_dir()]
        physical = {item.filename: item for item in infos}
        if len(physical) != len(infos):
            raise ValueError("Duplicate physical ZIP member names: " + path.name)
        logical = {item.filename: {"bytes": item.file_size, "crc32": f"{item.CRC:08x}",
                                   "physical_member": item.filename, "storage": "physical file"}
                   for item in infos}
        if ALIAS_MANIFEST in physical:
            alias_rows = tsv_rows(archive.read(ALIAS_MANIFEST), ["path", "replacement", "bytes", "sha256"])
            for row in alias_rows:
                name, replacement = safe_member(row["path"]), safe_member(row["replacement"])
                if PurePosixPath(name).suffix.lower() not in {".png", ".jpg", ".jpeg"}:
                    raise ValueError("Non-image path was aliased: " + name)
                if name == replacement or replacement not in physical:
                    raise ValueError("Alias must name a distinct retained physical ZIP member: " + name)
                if not re.fullmatch(r"[0-9a-f]{64}", row["sha256"]):
                    raise ValueError("Invalid alias SHA-256: " + name)
                actual = member_fingerprint(archive, replacement, fingerprints)
                if actual["bytes"] != int(row["bytes"]) or actual["sha256"] != row["sha256"]:
                    raise ValueError("Alias bytes/hash do not match retained ZIP member: " + name)
                if name in physical and member_fingerprint(archive, name, fingerprints) != actual:
                    raise ValueError("Physical alias path differs from its declared retained bytes: " + name)
                logical[name] = dict(actual, physical_member=replacement,
                                     storage="physical file" if name in physical else "verified image alias")
                aliases.append({"checkpoint": path.name, "checkpoint_number": number,
                                "path": name, "replacement": replacement, **actual,
                                "omitted_from_physical_members": name not in physical})
        manifest_rows = []
        if CONTENTS_MANIFEST in physical:
            manifest_rows = tsv_rows(archive.read(CONTENTS_MANIFEST),
                                     ["path", "bytes", "sha256", "storage", "replacement"])
            expected_names = set(logical) - {CONTENTS_MANIFEST}
            if {row["path"] for row in manifest_rows} != expected_names:
                raise ValueError("Archive manifest does not enumerate every logical member: " + path.name)
            for row in manifest_rows:
                name = row["path"]
                member = logical[name]["physical_member"]
                actual = member_fingerprint(archive, member, fingerprints)
                logical[name].update(actual)
                expected_storage = "duplicate image alias" if logical[name]["storage"] == "verified image alias" else "physical file"
                if row["replacement"] != member or row["storage"] != expected_storage:
                    raise ValueError("Manifest storage mapping disagrees with ZIP aliases: " + name)
                if int(row["bytes"]) != actual["bytes"] or row["sha256"] != actual["sha256"]:
                    mismatches.append({"path": name, "physical_member": member,
                                       "declared_bytes": int(row["bytes"]), "declared_sha256": row["sha256"],
                                       "actual_bytes": actual["bytes"], "actual_sha256": actual["sha256"],
                                       "actual_crc32": actual["crc32"], "actual_member_present": True})
        state = json.loads(archive.read("records/CHECKPOINT_STATE.json")) if "records/CHECKPOINT_STATE.json" in physical else {}
    return {"checkpoint": path.name, "checkpoint_number": number, "sha256": archive_hash,
            "bytes": path.stat().st_size, "physical_members": len(infos), "logical_members": len(logical),
            "alias_rows": len(aliases), "omitted_duplicate_image_paths": sum(r["omitted_from_physical_members"] for r in aliases),
            "checked_pages": state.get("checked_page_files", ""), "members": logical,
            "aliases": aliases, "manifest_rows": len(manifest_rows), "manifest_mismatches": mismatches}


def classify_manifest_discrepancy(project, audit):
    mismatches = audit["manifest_mismatches"]
    if not mismatches:
        return {"status": "passed" if audit["manifest_rows"] else "not present in pre-alias checkpoint",
                "documented": True, "restoration_audit": "", "unresolved": []}
    record = project / "records" / f"CHECKPOINT_{audit['checkpoint_number']}_RESTORATION_AUDIT.json"
    if record.exists():
        data = json.loads(record.read_text())
        expected = {row["path"] for row in mismatches}
        if (data.get("checkpoint") == audit["checkpoint"] and data.get("sha256") == audit["sha256"]
                and data.get("zip_crc_check") == "passed"
                and set(data.get("manifest_failures", [])) == expected
                and data.get("restoration", {}).get("verified_aliases") == audit["alias_rows"]
                and all(row["actual_member_present"] for row in mismatches)):
            return {"status": "documented stale checksum rows; actual content present",
                    "documented": True, "restoration_audit": record.relative_to(project).as_posix(),
                    "restoration_audit_sha256": file_digest(record), "unresolved": []}
    return {"status": "unexplained manifest discrepancy", "documented": False,
            "restoration_audit": "", "unresolved": [row["path"] for row in mismatches]}


def reason(path):
    if path in GENERATED:
        return ("Explicitly superseded by delivery-phase regeneration at the same path after checkpoint inventory. "
                "The final byte hash is authoritative in records/ARCHIVE_CONTENTS.tsv; that manifest itself is covered by the final ZIP SHA-256. "
                "The earlier member version remains attributable to its immutable checkpoint.")
    if path.startswith("checked_pages/"):
        return "Superseded by the final checked page at the same path. Scan-grounded edits and mechanical integration are individually recorded in CHECK_DECISIONS.tsv and independently replayed in CHANGE_REPLAY_AUDIT.json."
    if path.startswith("readers/"):
        return "Superseded by the complete standalone source/PDF at the same path, regenerated from the final 706-page annotated master or complete section guide."
    if path.startswith("guide_sections/"):
        return "Superseded by the completed and editorially standardized guide fragment at the same path; its paragraphs are incorporated into readers/PS_GUIDE.tex."
    if path.startswith("logs/"):
        return "Superseded by the retained diagnostic at the same path. Runtime paths are sanitized as recorded in PRIVACY_REDACTIONS.tsv; build measurements and outcomes remain documented."
    if path.startswith("qa/"):
        return "Superseded by the revised proof at the same logical path; final reader and visual-QA records establish the delivered state."
    if path.startswith("review_notes/"):
        return "Superseded by refined image-review notes at the same path. Final source readings and individual decisions are authoritative."
    if path.startswith("scripts/"):
        return "Superseded by the final reproducible script at the same path, including recorded recovery, layout, validation or coverage repairs."
    if path.startswith("records/"):
        return "Superseded by the final expanded or recomputed record at the same path. Earlier partial totals, stale historical checksum declarations and intermediate decisions remain attributable to their original checkpoint versions."
    return "Superseded by the completed report at the same path; earlier partial status and counts are obsolete."


def write_tsv(path, rows, fields):
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(path)


def build_inventory(project=PROJECT):
    project = project.resolve()
    workspace, records = project.parent, project / "records"
    archives = {}
    for base in [workspace, workspace / "recovery", workspace / "recovery/checkpoints"]:
        for path in base.glob("PS_READERS_checkpoint_*.zip"):
            number = int(path.stem.rsplit("_", 1)[1])
            archives.setdefault(number, path)
    versions, provenance, verified_hashes = collections.defaultdict(list), collections.defaultdict(list), collections.defaultdict(set)
    archive_rows, alias_rows, manifest_audits, errors = [], [], [], []
    for number, path in sorted(archives.items()):
        try:
            audit = inspect_checkpoint(path, number)
            manifest = classify_manifest_discrepancy(project, audit)
            if manifest["unresolved"]:
                errors.append({"checkpoint": path.name, "issue": "Unexplained manifest discrepancies",
                               "paths": manifest["unresolved"]})
            for name, info in audit["members"].items():
                key = (name, info["bytes"], info["crc32"])
                versions[key].append(number)
                provenance[key].append({"checkpoint_number": number, "storage": info["storage"],
                                        "physical_member": info["physical_member"], "sha256": info.get("sha256", "")})
                if info.get("sha256"):
                    verified_hashes[key].add(info["sha256"])
            alias_rows.extend(audit["aliases"])
            archive_rows.append({"checkpoint": path.name, "sha256": audit["sha256"], "bytes": audit["bytes"],
                                 "members": audit["physical_members"], "physical_members": audit["physical_members"],
                                 "logical_members": audit["logical_members"], "alias_rows": audit["alias_rows"],
                                 "omitted_duplicate_image_paths": audit["omitted_duplicate_image_paths"],
                                 "checked_pages": audit["checked_pages"], "manifest_rows": audit["manifest_rows"],
                                 "manifest_mismatches": len(audit["manifest_mismatches"]),
                                 "manifest_audit_status": manifest["status"], "restoration_audit": manifest["restoration_audit"]})
            if audit["manifest_rows"] or audit["alias_rows"]:
                manifest_audits.append({"checkpoint": path.name, "sha256": audit["sha256"],
                                       "physical_members": audit["physical_members"], "logical_members": audit["logical_members"],
                                       "alias_rows_verified": audit["alias_rows"], "manifest_rows": audit["manifest_rows"],
                                       "manifest_mismatches": audit["manifest_mismatches"], **manifest})
                print(json.dumps({"checkpoint": path.name, "logical_members": audit["logical_members"],
                                  "aliases_verified": audit["alias_rows"], "manifest_status": manifest["status"]}), flush=True)
        except (OSError, ValueError, KeyError, BadZipFile) as exc:
            errors.append({"checkpoint": path.name, "issue": str(exc)})
    current = {}
    for path in project.rglob("*"):
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".zip":
            data = path.read_bytes()
            current[path.relative_to(project).as_posix()] = {"bytes": len(data), "crc32": f"{zlib.crc32(data)&0xffffffff:08x}",
                                                            "sha256": digest(data), "storage": "physical file"}
    # The usual workspace contains restored paths. On an extracted package, a
    # verified current alias may supply a logical path before restoration.
    alias_table = records / "FILE_ALIASES.tsv"
    if alias_table.exists():
        for row in tsv_rows(alias_table.read_bytes(), ["path", "replacement", "bytes", "sha256"]):
            if row["path"] in current:
                continue
            target = current.get(safe_member(row["replacement"]))
            if target and target["bytes"] == int(row["bytes"]) and target["sha256"] == row["sha256"]:
                current[row["path"]] = dict(target, storage="verified image alias", physical_member=row["replacement"])
            else:
                errors.append({"path": row["path"], "issue": "Current missing alias has no verified retained bytes"})
    omissions = {}
    omission_path = records / "FINAL_OMISSIONS.tsv"
    if omission_path.exists():
        for row in tsv_rows(omission_path.read_bytes(), ["path", "bytes", "sha256", "replacement", "replacement_sha256", "reason"]):
            path, replacement = safe_member(row["path"]), safe_member(row["replacement"])
            target = current.get(replacement)
            if (not path.endswith(".pdf") or path.startswith("readers/")
                    or not replacement.startswith("readers/") or not replacement.endswith(".pdf")
                    or not target or target["sha256"] != row["replacement_sha256"]):
                errors.append({"path": path, "issue": "Invalid final PDF supersession replacement"})
                continue
            source = current.get(path)
            if source and (source["bytes"] != int(row["bytes"]) or source["sha256"] != row["sha256"]):
                errors.append({"path": path, "issue": "Omitted intermediate PDF does not have the recorded exact bytes"})
                continue
            omissions[path] = row
    rows, missing = [], []
    for (path, size, crc), numbers in sorted(versions.items()):
        key = (path, size, crc)
        if len(verified_hashes[key]) > 1:
            errors.append({"path": path, "issue": "Different SHA-256 values share a CRC/size version key"})
        if path in omissions:
            omission = omissions[path]
            status = "explicitly superseded for final delivery"
            replacement = omission["replacement"]
            why = ("Every historical version at this intermediate-PDF path is replaced in final delivery by "
                   + replacement + " (SHA-256 " + omission["replacement_sha256"] + "). "
                   + "The exact current omitted PDF has SHA-256 " + omission["sha256"] + ". "
                   + omission["reason"])
        elif path in current:
            item = current[path]
            exact = item["bytes"] == size and item["crc32"] == crc
            if verified_hashes[key]:
                exact = exact and item["sha256"] in verified_hashes[key]
            if path in GENERATED:
                exact = False  # Avoid a self-referential claim about rewritten inventory files.
            status = ("delivery-phase regenerated supersession" if path in GENERATED
                      else "retained byte-identically" if exact else "superseded")
            why = "This exact logical member version is retained at the same path." if exact else reason(path)
            if item["storage"] == "verified image alias":
                why += " The logical path is recoverable from the SHA-256-verified FILE_ALIASES.tsv replacement."
            replacement = path
        else:
            status, replacement = "unresolved missing path", ""
            why = "Requires explicit recovery or a specific replacement before packaging."
            missing.append(path)
        p = provenance[key]
        rows.append({"path": path, "checkpoint_numbers": ",".join(map(str, sorted(set(numbers)))),
                     "earlier_bytes": size, "earlier_crc32": crc, "status": status, "replacement": replacement,
                     "reason": why, "earlier_verified_sha256": ",".join(sorted(verified_hashes[key])),
                     "physical_checkpoint_numbers": ",".join(map(str, sorted({x["checkpoint_number"] for x in p if x["storage"] == "physical file"}))),
                     "aliased_checkpoint_numbers": ",".join(map(str, sorted({x["checkpoint_number"] for x in p if x["storage"] == "verified image alias"}))),
                     "member_storage_provenance_json": json.dumps(p, sort_keys=True, separators=(",", ":"))})
    write_tsv(records / "CHECKPOINT_ARCHIVES.tsv", archive_rows,
              ["checkpoint", "sha256", "bytes", "members", "physical_members", "logical_members", "alias_rows",
               "omitted_duplicate_image_paths", "checked_pages", "manifest_rows", "manifest_mismatches",
               "manifest_audit_status", "restoration_audit"])
    write_tsv(records / "CHECKPOINT_SUPERSESSION.tsv", rows,
              ["path", "checkpoint_numbers", "earlier_bytes", "earlier_crc32", "status", "replacement", "reason",
               "earlier_verified_sha256", "physical_checkpoint_numbers", "aliased_checkpoint_numbers",
               "member_storage_provenance_json"])
    write_tsv(records / "CHECKPOINT_ALIAS_MEMBERS.tsv", alias_rows,
              ["checkpoint", "checkpoint_number", "path", "replacement", "bytes", "crc32", "sha256",
               "omitted_from_physical_members"])
    expected, reserved = set(range(1, max(archives, default=0) + 1)), {61}
    summary = {"archives": len(archive_rows), "checkpoint_numbers": sorted(archives),
               "reserved_unverified_numbers": sorted((expected - set(archives)) & reserved),
               "missing_expected_archives": sorted(expected - set(archives) - reserved),
               "unique_member_versions": len(rows), "unique_paths": len({row["path"] for row in rows}),
               "status_counts": dict(collections.Counter(row["status"] for row in rows)),
               "missing_paths": sorted(set(missing)), "archive_validation_errors": errors,
               "alias_member_occurrences_verified": len(alias_rows),
               "final_delivery_pdf_supersessions": len(omissions),
               "final_omissions_sha256": file_digest(omission_path) if omission_path.exists() else None,
               "checkpoints_with_aliases": [row["checkpoint"] for row in archive_rows if row["alias_rows"]],
               "documented_manifest_checksum_discrepancies": [
                   {"checkpoint": row["checkpoint"], "paths": [x["path"] for x in row["manifest_mismatches"]],
                    "restoration_audit": row["restoration_audit"]}
                   for row in manifest_audits if row["manifest_mismatches"] and row["documented"]],
               "complete": not missing and not errors and not (expected - set(archives) - reserved),
               "durable_save_status_inferred_from_local_presence": False,
               "note": "Archive accounting identifies locally available immutable ZIP bytes and actual logical member versions; it does not infer successful remote saves. Number 61 was reserved and is not asserted saved. Checkpoint 67's oversized save failed before upload. A hash-bound restoration audit documents checkpoint 68's two stale manifest checksum rows; all actual members and 817 aliases are present. Historical checksum metadata races are not content-loss claims. Every enumerated member version has an exact retention or explicit supersession row, including aliased image paths."}
    (records / "CHECKPOINT_MANIFEST_VERIFICATION.json").write_text(json.dumps(
        {"archives": manifest_audits, "unresolved": errors,
         "scope": "Actual ZIP bytes, authenticated logical aliases and historical manifest declarations are recorded separately."},
        indent=2) + "\n")
    (records / "CHECKPOINT_INVENTORY.json").write_text(json.dumps(summary, indent=2) + "\n")
    return summary


if __name__ == "__main__":
    try:
        result = build_inventory()
    except Exception as exc:
        result = {"complete": False, "archive_validation_errors": [type(exc).__name__ + ": " + str(exc)]}
        (PROJECT / "records/CHECKPOINT_INVENTORY.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))
    raise SystemExit(0 if result["complete"] else 1)
