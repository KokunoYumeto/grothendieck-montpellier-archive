"""Check all six actual checkpoint payloads against the CP06 restoration map.

No final archive exists in this check; no archive or restored tree is created.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
import time
import zipfile
from datetime import datetime, timezone

root = Path(__file__).resolve().parents[1]
output = root / "logs/geometry_restore_checkpoint_mapping_cp06.json"
note = root / "notes/geometry_final_package_audit_cp06.md"
if output.exists() or note.exists():
    raise SystemExit("Refusing to overwrite the CP06 mapping audit")
spec = importlib.util.spec_from_file_location("restore", root / "code/restore_checkpoint_from_final.py")
restore = importlib.util.module_from_spec(spec)
spec.loader.exec_module(restore)
plan_path = root / "notes/geometry_final_package_plan_cp06.json"
estimate_path = root / "notes/geometry_final_package_estimate_cp06.json"
plan = json.loads(plan_path.read_text())
estimate = json.loads(estimate_path.read_text())
assert [r["checkpoint"] for r in plan["checkpoints"]] == [1, 2, 3, 4, 5, 6]
started = time.perf_counter()

def digest(path):
    result = hashlib.sha256()
    with path.open("rb") as stream:
        while block := stream.read(1024 * 1024):
            result.update(block)
    return result.hexdigest()

# These describe the proposed final payloads, not an already-created final ZIP.
infos = {}
for row in plan["canonical_files"]:
    info = zipfile.ZipInfo(row["member"])
    info.file_size = row["bytes"]
    infos[info.filename] = info
for row in plan["checkpoint_members"]:
    if row["kind"] == "directory":
        info = zipfile.ZipInfo(row["final_member"])
        infos[info.filename] = info

records = []
for checkpoint in plan["checkpoints"]:
    number = checkpoint["checkpoint"]
    source_path = root.parent / checkpoint["archive"]
    assert source_path.stat().st_size == checkpoint["bytes"]
    assert digest(source_path) == checkpoint["sha256"]
    selected = [r for r in plan["checkpoint_members"] if r["checkpoint"] == number]
    by_original = {r["original_member"]: r for r in selected}
    files, directories = restore.restoration_plan(plan, infos, checkpoint=number)
    assert len(by_original) == len(selected) == checkpoint["entries"]
    file_targets = {str(item[0]) for item in files}
    assert file_targets == {r["original_member"] for r in selected if r["kind"] == "file"}
    total_bytes, count_files, count_dirs = 0, 0, 0
    with zipfile.ZipFile(source_path) as archive:
        assert len(archive.namelist()) == len(set(archive.namelist()))
        assert set(archive.namelist()) == set(by_original)
        for info in archive.infolist():
            row = by_original[info.filename]
            if info.is_dir():
                assert row["kind"] == "directory"
                count_dirs += 1
                continue
            assert row["kind"] == "file"
            assert info.file_size == row["bytes"]
            assert f"{info.CRC:08x}" == row["zip_crc32"]
            restore.transfer_checked(archive, info.filename, restore.fingerprint(row))
            total_bytes += info.file_size
            count_files += 1
    assert total_bytes == checkpoint["uncompressed_bytes"]
    records.append({"checkpoint": number, "archive": source_path.name, "archive_sha256": checkpoint["sha256"], "logical_entries": len(selected), "regular_files_with_verified_sha256_and_bytes": count_files, "explicit_directories": count_dirs, "restoration_directories_including_parents": len(directories), "verified_uncompressed_bytes": total_bytes})

current_files, current_dirs = restore.restoration_plan(plan, infos, current=True)
assert len(current_files) == plan["totals"]["current_logical_files"]
reserve = estimate["estimated_with_reserve_bytes"]
margin = 500_000_000 - reserve
assert margin > 0
record = {"utc": datetime.now(timezone.utc).isoformat(), "activity": "Packaging and restoration mapping verification only; not mathematical movement", "archive_files_created": 0, "restored_trees_created": 0, "final_archive_exists_or_verified_claimed": False, "plan": str(plan_path.relative_to(root)), "plan_sha256": digest(plan_path), "estimate": str(estimate_path.relative_to(root)), "estimate_sha256": digest(estimate_path), "restoration_utility_sha256": digest(root / "code/restore_checkpoint_from_final.py"), "actual_checkpoint_checks": records, "total_historical_logical_entries": sum(r["logical_entries"] for r in records), "actual_checkpoint_payloads_read_and_verified": True, "current_mapping_count": len(current_files), "current_mapping_only_not_second_payload_read": True, "estimated_archive_bytes": estimate["estimated_total_archive_bytes"], "estimated_with_reserve_bytes": reserve, "margin_below_500MB_after_reserve": margin, "policy_conflicts": plan["policy_conflicts"], "files_changed_during_plan": plan["files_changed_during_plan"], "runtime_seconds": time.perf_counter() - started}
output.write_text(json.dumps(record, indent=2) + "\n")
table = "\n".join(f"| {r['checkpoint']:02d} | {r['logical_entries']:,} | {r['regular_files_with_verified_sha256_and_bytes']:,} | {r['verified_uncompressed_bytes']:,} |" for r in records)
note.write_text(f"""# Checkpoint-06 final-package estimate and restoration audit

Snapshot: {record['utc']}. This is packaging verification, not mathematical
movement. No ZIP or restored tree was created.

The fresh plan includes all six checkpoint archives and **{record['total_historical_logical_entries']:,}
historical logical entries**. It also includes **{len(current_files):,} current
logical files**, represented by **{plan['totals']['canonical_regular_files']:,} canonical
regular-file payloads** after content deduplication.

The compressed estimate is **{record['estimated_archive_bytes']:,} bytes**.
With the 2,000,000-byte reserve it is **{reserve:,} bytes**, leaving
**{margin:,} bytes** below 500,000,000. These are dated estimates, not an
assertion that a final ZIP has been created. Actual final creation replans
and checks the real archive size.

| Checkpoint | Original logical entries | Actual file payloads hash-checked | Uncompressed bytes checked |
|---|---:|---:|---:|
{table}

For each actual checkpoint ZIP, the audit checked its whole-file SHA256
and size, exact member-name set, member kind, CRC and byte count, then read
every regular member and checked its SHA256 against the new manifest. It
also ran the restoration utility's real mapping logic for all six
checkpoints, checking canonical payload fingerprints and every original
logical path. All six inventories are complete. The current-view mapping
was checked against this plan; a second current-payload read was not
claimed. The package estimator itself hashes current contents while
building the plan.

No policy conflict or changing current file was reported by the estimate.
Source scans and other excluded caches remain subject to the established
checkpoint exclusions, with their per-file provenance fingerprints in the
plan. Their contents are not silently counted as retained checkpoint files.

Records: `notes/geometry_final_package_plan_cp06.json`,
`notes/geometry_final_package_estimate_cp06.json`,
`logs/geometry_final_package_cp06_estimate.json` and
`logs/geometry_restore_checkpoint_mapping_cp06.json`. The mapping audit
took {record['runtime_seconds']:.3f} seconds. Earlier estimate and audit
files were not overwritten. Final creation must still use a fresh plan
after writers are quiescent and the formal stopping decision is recorded.
""")
print(json.dumps(record, indent=2))
