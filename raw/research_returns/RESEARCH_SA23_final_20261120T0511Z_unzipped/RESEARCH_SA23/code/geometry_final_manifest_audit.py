#!/usr/bin/env python3
"""Read-only independent inspection of the actual final ZIP after creation.

The existing creator verifies every canonical payload. This separate audit
checks the completed archive's identity, manifest inventory, recovery mappings
and saved checkpoint receipts. It creates no ZIP or restored tree. Its sole
output must be a new file outside the frozen research directory.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import zipfile

# Keep the post-creation inspection from writing project bytecode caches.
sys.dont_write_bytecode = True
import restore_checkpoint_from_final as restore

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_COUNTS = {1: 106, 2: 256, 3: 473, 4: 1240, 5: 2125, 6: 2573}


def digest_path(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while block := stream.read(1024 * 1024):
            digest.update(block)
    return digest.hexdigest()


def checked_small_member(archive, row):
    data = archive.read(row["final_member"])
    assert (hashlib.sha256(data).hexdigest(), len(data)) == restore.fingerprint(row)
    return data


def audit(archive_path, receipt_path):
    receipt = json.loads(receipt_path.read_text())
    assert receipt["archive_created"] is True and receipt["all_contents_verified"] is True
    size = archive_path.stat().st_size
    sha = digest_path(archive_path)
    assert size < 500_000_000 and size == receipt["bytes"] and sha == receipt["sha256"]
    with zipfile.ZipFile(archive_path) as archive:
        document, infos = restore.read_manifest(archive)
        canonical = {row["member"]: row for row in document["canonical_files"]}
        assert len(canonical) == len(document["canonical_files"])
        assert len({restore.fingerprint(row) for row in canonical.values()}) == len(canonical)
        structural = {row["final_member"] for row in document["checkpoint_members"] if row["kind"] == "directory"}
        assert set(infos) == set(canonical) | structural | {restore.MANIFEST}
        assert sum(not info.is_dir() for info in infos.values()) == receipt["regular_files"]
        assert document["policy_conflicts"] == [] and document["files_changed_during_plan"] == []
        checkpoints = {row["checkpoint"]: row for row in document["checkpoints"]}
        assert set(checkpoints) == set(EXPECTED_COUNTS)
        assert len(checkpoints) == len(document["checkpoints"])
        current = {row["path"]: row for row in document["current_files"]}
        assert len(current) == len(document["current_files"])
        required = ["checkpoint_history.json", "logs/root_checkpoint06_receipt.json", "logs/root_checkpoint06_receipt.txt", "logs/checkpoint06_creation.txt", "notes/geometry_final_package_README.md", "code/restore_checkpoint_from_final.py", "code/geometry_final_manifest_audit.py", "RESEARCH_SA23_README.md", "PROGRESS_LEDGER.md", "RESEARCH_SA23_report.md", "RESEARCH_SA23_results.csv", "CHECK_EVENTS.tsv", "CORRECTIONS.tsv", "RESEARCH_SA23_paper.tex", "RESEARCH_SA23_paper.pdf", "RESEARCH_SA23_references.bib"]
        assert all(name in current for name in required)
        history = json.loads(checked_small_member(archive, current["checkpoint_history.json"]))
        history_by_number = {row["checkpoint"]: row for row in history}
        assert len(history_by_number) == len(history) == 6
        assert set(history_by_number) == set(EXPECTED_COUNTS)
        checks = []
        for number, expected_count in EXPECTED_COUNTS.items():
            checkpoint = checkpoints[number]
            saved = history_by_number[number]
            assert checkpoint["entries"] == saved["files"] == expected_count
            assert (checkpoint["sha256"], checkpoint["bytes"]) == (saved["sha256"], saved["bytes"])
            delivery_id = saved.get("library_file_id") or saved.get("library_identity", {}).get("library_file_id")
            assert delivery_id
            files, directories = restore.restoration_plan(document, infos, checkpoint=number)
            assert len(files) == expected_count  # These six actual ZIPs have only regular entries.
            checks.append({"checkpoint": number, "logical_members": expected_count, "recovery_mapping_checked": True, "saved_delivery_identity_present": True, "archive_sha256": checkpoint["sha256"]})
        current_files, _ = restore.restoration_plan(document, infos, current=True)
        assert len(current_files) == document["totals"]["current_logical_files"]
        assert receipt["source_snapshot_rechecked"] == {"current_files": len(current_files), "checkpoints": 6}
        assert len(canonical) == document["totals"]["canonical_regular_files"]
        assert len(document["checkpoint_members"]) == sum(EXPECTED_COUNTS.values())
        top_guide = checked_small_member(archive, current["RESEARCH_SA23_README.md"]).decode("utf-8")
        package_guide = checked_small_member(archive, current["notes/geometry_final_package_README.md"]).decode("utf-8")
        assert "restore_checkpoint_from_final.py" in top_guide
        assert "all six checkpoints" in package_guide
        current_log_paths = sorted(name for name in current if name.startswith("logs/"))
        manifest_sha = hashlib.sha256(archive.read(restore.MANIFEST)).hexdigest()
    return {"utc": datetime.now(timezone.utc).isoformat(), "activity": "Independent final archive inventory/recovery inspection; no mathematical movement", "archive": str(archive_path), "bytes": size, "sha256": sha, "creation_receipt": str(receipt_path), "matches_verified_creation_receipt": True, "manifest_sha256": manifest_sha, "checkpoint_checks": checks, "historical_logical_members": sum(EXPECTED_COUNTS.values()), "current_logical_files": len(current_files), "canonical_regular_files": len(canonical), "current_log_files_included": len(current_log_paths), "required_current_paths_present": required, "saved_cp06_receipts_present": True, "all_recovery_mappings_checked_against_actual_zip_inventory": True, "creator_verified_every_canonical_payload": True, "historical_source_payload_checks_repeated": False, "restored_tree_created": False, "archive_created_or_modified_by_this_audit": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--creation-receipt", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.absolute()
    try:
        output.resolve().relative_to(ROOT.resolve())
    except ValueError:
        pass
    else:
        parser.error("Post-creation output must stay outside the frozen research tree")
    if output.exists() or output.is_symlink():
        parser.error("Refusing to overwrite an existing output")
    record = audit(args.archive.absolute(), args.creation_receipt.absolute())
    with output.open("x") as stream:
        json.dump(record, stream, indent=2)
        stream.write("\n")
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
