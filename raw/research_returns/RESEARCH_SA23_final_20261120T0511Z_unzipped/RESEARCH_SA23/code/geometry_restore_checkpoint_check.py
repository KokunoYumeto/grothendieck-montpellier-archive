"""One focused restoration-safety check; all test ZIPs stay in memory."""
from pathlib import Path
import copy
from datetime import datetime, timezone
import hashlib
import importlib.util
import io
import json
import tempfile
import time
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("restore", ROOT / "code/restore_checkpoint_from_final.py")
restore = importlib.util.module_from_spec(spec)
spec.loader.exec_module(restore)
started = time.perf_counter()

payloads = {"RESEARCH_SA23/current.txt": b"current\n", "RESEARCH_SA23/history/checkpoint_01/old.txt": b"old\n"}
fingerprints = {name: {"sha256": hashlib.sha256(value).hexdigest(), "bytes": len(value)} for name, value in payloads.items()}
directory = "RESEARCH_SA23/history/checkpoint_01/empty/"
document = {"format": restore.FORMAT, "created_utc": "fixture", "canonical_files": [{"member": name, **fingerprints[name]} for name in payloads],
    "checkpoints": [{"checkpoint": 1, "entries": 4}],
    "current_files": [{"path": "current.txt", "final_member": "RESEARCH_SA23/current.txt", **fingerprints["RESEARCH_SA23/current.txt"]}, {"path": "alias.txt", "final_member": "RESEARCH_SA23/current.txt", **fingerprints["RESEARCH_SA23/current.txt"]}],
    "checkpoint_members": [
        {"checkpoint": 1, "kind": "file", "original_member": "RESEARCH_SA23/unchanged.txt", "final_member": "RESEARCH_SA23/current.txt", **fingerprints["RESEARCH_SA23/current.txt"]},
        {"checkpoint": 1, "kind": "file", "original_member": "RESEARCH_SA23/changed.txt", "final_member": "RESEARCH_SA23/history/checkpoint_01/old.txt", **fingerprints["RESEARCH_SA23/history/checkpoint_01/old.txt"]},
        {"checkpoint": 1, "kind": "file", "original_member": "RESEARCH_SA23/deleted.txt", "final_member": "RESEARCH_SA23/history/checkpoint_01/old.txt", **fingerprints["RESEARCH_SA23/history/checkpoint_01/old.txt"]},
        {"checkpoint": 1, "kind": "directory", "original_member": "RESEARCH_SA23/empty/", "final_member": directory}]}

def memory_archive(doc, *, extra=None, corrupt=False):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as z:
        for name, value in payloads.items():
            z.writestr(name, value if not corrupt or name != "RESEARCH_SA23/current.txt" else b"damaged\n")
        z.writestr(directory, b"")
        z.writestr(restore.MANIFEST, json.dumps(doc))
        if extra is not None:
            z.writestr(extra, b"unsafe")
    buffer.seek(0)
    return zipfile.ZipFile(buffer)

checks = []
with tempfile.TemporaryDirectory(prefix="geometry_restore_check_") as tmp:
    tmp = Path(tmp)
    with memory_archive(document) as archive:
        parsed, infos = restore.read_manifest(archive)
        files, dirs = restore.restoration_plan(parsed, infos, checkpoint=1)
        destination = tmp / "checkpoint"
        summary = restore.restore(archive, files, dirs, destination)
        assert (destination / "RESEARCH_SA23/unchanged.txt").read_bytes() == b"current\n"
        assert (destination / "RESEARCH_SA23/changed.txt").read_bytes() == b"old\n"
        assert (destination / "RESEARCH_SA23/deleted.txt").read_bytes() == b"old\n"
        assert (destination / "RESEARCH_SA23/empty").is_dir()
        assert summary["logical_files"] == 3 and summary["verified_canonical_payloads"] == 2
        checks.append("Exact unchanged, changed and deleted logical paths plus an empty directory restored from two canonical payloads")
        try:
            restore.restore(archive, files, dirs, destination)
        except FileExistsError:
            checks.append("Existing destination refused without overwrite")
        else:
            raise AssertionError("Existing destination accepted")
        files, dirs = restore.restoration_plan(parsed, infos, current=True)
        restore.restore(archive, files, dirs, tmp / "current")
        assert (tmp / "current/RESEARCH_SA23/current.txt").read_bytes() == (tmp / "current/RESEARCH_SA23/alias.txt").read_bytes()
        checks.append("Current logical aliases restored as separate identical files")

    bad = copy.deepcopy(document)
    bad["checkpoint_members"][0]["original_member"] = "RESEARCH_SA23/../escape.txt"
    with memory_archive(bad) as archive:
        parsed, infos = restore.read_manifest(archive)
        try:
            restore.restoration_plan(parsed, infos, checkpoint=1)
        except ValueError:
            checks.append("Traversal in logical destination refused")
        else:
            raise AssertionError("Traversal accepted")
    bad = copy.deepcopy(document)
    bad["canonical_files"][0]["sha256"] = "0" * 64
    for row in bad["checkpoint_members"] + bad["current_files"]:
        if row.get("final_member") == "RESEARCH_SA23/current.txt":
            row["sha256"] = "0" * 64
    with memory_archive(bad) as archive:
        parsed, infos = restore.read_manifest(archive)
        files, dirs = restore.restoration_plan(parsed, infos, checkpoint=1)
        try:
            restore.restore(archive, files, dirs, tmp / "corrupt")
        except ValueError:
            assert not (tmp / "corrupt").exists()
            checks.append("Corrupt manifest fingerprint refused before output creation")
        else:
            raise AssertionError("Bad fingerprint accepted")
    link = zipfile.ZipInfo("RESEARCH_SA23/link")
    link.create_system = 3
    link.external_attr = 0o120777 << 16
    with memory_archive(document, extra=link) as archive:
        try:
            restore.read_manifest(archive)
        except ValueError:
            checks.append("Symlink ZIP member refused")
        else:
            raise AssertionError("Symlink accepted")

# Validate the precise actual manifest schema for every recorded checkpoint.
# This is a mapping check only: no final archive or fabricated source-content
# verification is claimed.
actual_path = ROOT / "notes/geometry_final_package_plan_cp05.json"
actual = json.loads(actual_path.read_text())
actual_infos = {}
for row in actual["canonical_files"]:
    info = zipfile.ZipInfo(row["member"])
    info.file_size = row["bytes"]
    actual_infos[info.filename] = info
for row in actual["checkpoint_members"]:
    if row["kind"] == "directory":
        info = zipfile.ZipInfo(row["final_member"])
        actual_infos[info.filename] = info
counts = []
for row in actual["checkpoints"]:
    files, dirs = restore.restoration_plan(actual, actual_infos, checkpoint=row["checkpoint"])
    counts.append({"checkpoint": row["checkpoint"], "logical_entries": row["entries"], "files": len(files), "directories_including_implicit_parents": len(dirs)})
files, dirs = restore.restoration_plan(actual, actual_infos, current=True)
record = {"utc": datetime.now(timezone.utc).isoformat(), "activity": "Packaging usability and safety verification; not mathematical movement", "archive_files_created": 0, "fixture": "Small in-memory ZIP only; temporary restored directories removed after assertions", "checks": checks, "actual_plan_path": str(actual_path.relative_to(ROOT)), "actual_plan_sha256": hashlib.sha256(actual_path.read_bytes()).hexdigest(), "actual_checkpoint_mapping_checks": counts, "actual_current_logical_files": len(files), "actual_payload_verification_claimed": False, "runtime_seconds": time.perf_counter() - started, "utility_sha256": hashlib.sha256((ROOT / "code/restore_checkpoint_from_final.py").read_bytes()).hexdigest()}
(ROOT / "logs/geometry_restore_checkpoint_check.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
