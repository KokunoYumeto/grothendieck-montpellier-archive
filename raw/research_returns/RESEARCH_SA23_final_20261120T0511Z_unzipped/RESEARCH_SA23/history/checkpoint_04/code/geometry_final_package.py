"""Plan a deduplicated final package; default execution creates NO archive.

This is packaging work, not mathematical movement.  The explicit
--create-final PATH branch is prepared for later use only after the parent
determines that the formal stopping rule has triggered.

Current paths and every checkpoint member are recoverable through the
manifest even when identical bytes at different names are stored only once.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import tempfile
import zipfile
import zlib

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT.name
CHUNK = 1024 * 1024
LIMIT = 500_000_000
LEVEL = 6
MANIFEST_MEMBER = f"{PREFIX}/final_package_manifest.json"


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def policy_reason(rel: PurePosixPath, *, historical=False):
    """Preserve checkpoint.py's exclusions; original inputs stay external."""
    if rel.parts[0] == "runtime" or "__pycache__" in rel.parts:
        return "runtime_or_python_cache"
    if rel.parts[0] in {"inputs", "upload"}:
        return "original_inputs"
    if rel.suffix == ".zip":
        return "no_nested_zip_archives"
    source_cache = (
        rel.parts[0] == "sources"
        or (rel.parts[0] == "notes" and rel.suffix == ".pdf")
        or (rel.parts[0] == "notes" and "web_" in rel.name and rel.suffix == ".json")
        or (rel.parts[0] == "notes" and rel.name.endswith("_full.txt"))
        or (rel.parts[0] == "verification" and "scan" in rel.name)
    )
    if source_cache:
        return "retrievable_source_cache"
    if rel.suffix in {".aux", ".toc", ".out"}:
        return "ephemeral_tex_auxiliary"
    # A checkpoint's own manifest is historical content and must be kept.
    if not historical and rel.name == "checkpoint_manifest.json":
        return "checkpoint_manifest_preserved_through_history"
    if not historical and str(rel) == "final_package_manifest.json":
        return "fresh_final_manifest_generated_in_archive"
    return None


def digest_stream(stream):
    h = hashlib.sha256()
    size = 0
    while block := stream.read(CHUNK):
        size += len(block)
        h.update(block)
    return h.hexdigest(), size


def digest_path(path):
    with path.open("rb") as stream:
        return digest_stream(stream)


def deflated_size_path(path):
    compressor = zlib.compressobj(LEVEL, zlib.DEFLATED, -15)
    total = 0
    with path.open("rb") as stream:
        while block := stream.read(CHUNK):
            total += len(compressor.compress(block))
    return total + len(compressor.flush())


def deflated_size_bytes(data):
    compressor = zlib.compressobj(LEVEL, zlib.DEFLATED, -15)
    return len(compressor.compress(data)) + len(compressor.flush())


def safe_checkpoint_relative(member):
    p = PurePosixPath(member)
    if p.is_absolute() or ".." in p.parts or "\\" in member or "\0" in member:
        raise ValueError(f"Unsafe checkpoint member: {member!r}")
    if not p.parts or p.parts[0] != PREFIX:
        raise ValueError(f"Unexpected checkpoint root: {member!r}")
    return PurePosixPath(*p.parts[1:]) if len(p.parts) > 1 else PurePosixPath(".")


def current_inventory():
    included, omitted = [], []
    for base, dirs, names in os.walk(ROOT, followlinks=False):
        base = Path(base)
        kept_dirs = []
        for name in sorted(dirs):
            path = base / name
            rel = PurePosixPath(path.relative_to(ROOT).as_posix())
            reason = policy_reason(rel)
            if path.is_symlink():
                reason = "symlink_directory_not_followed"
            if reason:
                omitted.append({"path": str(rel) + "/", "reason": reason})
            else:
                kept_dirs.append(name)
        dirs[:] = kept_dirs
        for name in sorted(names):
            path = base / name
            rel = PurePosixPath(path.relative_to(ROOT).as_posix())
            reason = policy_reason(rel)
            if path.is_symlink():
                reason = "symlink_not_dereferenced"
            if reason:
                item = {"path": str(rel), "reason": reason}
                try:
                    item["bytes"] = path.lstat().st_size
                except FileNotFoundError:
                    item["disappeared_during_plan"] = True
                omitted.append(item)
                continue
            if path.is_file():
                included.append((rel, path))
    # Prefer the main deliverables as canonical names for identical content.
    included.sort(key=lambda item: (len(item[0].parts) != 1, str(item[0])))
    return included, omitted


def checkpoint_paths():
    found = []
    pattern = re.compile(re.escape(PREFIX) + r"_checkpoint_(\d+)\.zip$")
    for path in ROOT.parent.glob(f"{PREFIX}_checkpoint_*.zip"):
        match = pattern.fullmatch(path.name)
        if match:
            found.append((int(match.group(1)), path))
    found.sort()
    numbers = [n for n, _ in found]
    if len(numbers) != len(set(numbers)):
        raise ValueError("More than one archive has the same checkpoint number")
    return found


def build_plan():
    created = now()
    checkpoints, prior_rows, prior_compressed = [], [], {}
    conflicts, directories, volatile = [], set(), []
    history_path = ROOT / "checkpoint_history.json"
    history = json.loads(history_path.read_text()) if history_path.exists() else []
    expected = {row["checkpoint"]: row for row in history}
    discovered = checkpoint_paths()
    missing = set(expected) - {n for n, _ in discovered}
    if missing:
        raise ValueError(f"Missing recorded checkpoint archives: {sorted(missing)}")

    for number, path in discovered:
        archive_sha, archive_bytes = digest_path(path)
        recorded = expected.get(number)
        if recorded and recorded.get("sha256") != archive_sha:
            raise ValueError(f"Checkpoint {number} hash differs from recorded history")
        info = {"checkpoint": number, "archive": path.name,
                "sha256": archive_sha, "bytes": archive_bytes,
                "entries": 0, "uncompressed_bytes": 0,
                "previous_compressed_payload_bytes": 0}
        with zipfile.ZipFile(path, "r") as archive:
            names = archive.namelist()
            if len(names) != len(set(names)):
                raise ValueError(f"Duplicate member names inside {path.name}")
            for zi in sorted(archive.infolist(), key=lambda x: x.filename):
                rel = safe_checkpoint_relative(zi.filename)
                info["entries"] += 1
                if zi.is_dir():
                    member = f"{PREFIX}/history/checkpoint_{number:02d}/"
                    if str(rel) != ".":
                        member += str(rel).rstrip("/") + "/"
                    directories.add(member)
                    prior_rows.append({"checkpoint": number, "original_member": zi.filename,
                        "kind": "directory", "final_member": member})
                    continue
                if str(rel) == ".":
                    raise ValueError(f"A file cannot be the package root: {zi.filename}")
                reason = policy_reason(rel, historical=True)
                if reason:
                    conflicts.append({"checkpoint": number, "member": zi.filename,
                                      "policy_reason": reason})
                with archive.open(zi, "r") as stream:
                    sha, size = digest_stream(stream)
                if size != zi.file_size:
                    raise ValueError(f"Size mismatch for {path.name}:{zi.filename}")
                key = (sha, size)
                if zi.compress_type == zipfile.ZIP_DEFLATED:
                    prior_compressed.setdefault(key, []).append(zi.compress_size)
                row = {"checkpoint": number, "original_member": zi.filename,
                    "relative_path": str(rel), "kind": "file", "sha256": sha,
                    "bytes": size, "previous_compressed_bytes": zi.compress_size,
                    "zip_crc32": f"{zi.CRC:08x}",
                    "source_archive": str(path), "source_member": zi.filename}
                prior_rows.append(row)
                info["uncompressed_bytes"] += size
                info["previous_compressed_payload_bytes"] += zi.compress_size
            manifest_name = f"{PREFIX}/checkpoint_manifest.json"
            if manifest_name in names:
                old_manifest = json.loads(archive.read(manifest_name))
                declared = {f"{PREFIX}/{p}" for p in old_manifest.get("included", [])}
                actual_files = {zi.filename for zi in archive.infolist() if not zi.is_dir()}
                # Checkpoint01 predates the later self-listing convention.
                # Its actual manifest member is still preserved and mapped.
                declared_with_self = declared | {manifest_name}
                info["manifest_lists_itself"] = manifest_name in declared
                if declared and declared_with_self != actual_files:
                    conflicts.append({"checkpoint": number,
                        "policy_reason": "checkpoint_manifest_inventory_mismatch",
                        "declared_only": sorted(declared_with_self-actual_files),
                        "archive_only": sorted(actual_files-declared_with_self)})
                info["checkpoint_manifest_present"] = True
                info["omitted_cache_entries_in_manifest"] = len(old_manifest.get("omitted_retrievable_caches", []))
        checkpoints.append(info)

    current, omitted = current_inventory()
    payloads, by_content, current_rows, current_by_path = [], {}, [], {}
    member_names = set()
    for rel, path in current:
        before = path.stat()
        sha, size = digest_path(path)
        after = path.stat()
        if (before.st_size, before.st_mtime_ns, before.st_ino) != (after.st_size, after.st_mtime_ns, after.st_ino):
            volatile.append(str(rel))
        key = (sha, size)
        proposed = f"{PREFIX}/{rel}"
        if key not in by_content:
            by_content[key] = proposed
            member_names.add(proposed)
            if key in prior_compressed:
                compressed = max(prior_compressed[key])
                method = "maximum_existing_checkpoint_deflate_size"
            else:
                compressed = deflated_size_path(path)
                method = "raw_deflate_level6_dry_run"
            payloads.append({"member": proposed, "sha256": sha, "bytes": size,
                "estimated_deflated_bytes": compressed, "compression_estimate": method,
                "source_kind": "current", "source_path": str(path)})
        row = {"path": str(rel), "final_member": by_content[key], "sha256": sha,
               "bytes": size, "canonical_current_path": by_content[key] == proposed}
        current_rows.append(row)
        current_by_path[str(rel)] = row

    history_rows = []
    for row in prior_rows:
        if row["kind"] == "directory":
            history_rows.append(row)
            continue
        key = (row["sha256"], row["bytes"])
        current_same_path = current_by_path.get(row["relative_path"])
        if current_same_path and current_same_path["sha256"] == row["sha256"]:
            relation = "unchanged_at_current_path"
        elif current_same_path:
            relation = "changed_at_current_path"
        elif row["relative_path"] == "checkpoint_manifest.json":
            relation = "historical_checkpoint_manifest"
        else:
            relation = "absent_from_current_included_tree"
        if key not in by_content:
            member = f"{PREFIX}/history/checkpoint_{row['checkpoint']:02d}/{row['relative_path']}"
            if member in member_names or member == MANIFEST_MEMBER:
                raise ValueError(f"Canonical member path collision: {member}")
            by_content[key] = member
            member_names.add(member)
            compressed = max(prior_compressed.get(key, [row["previous_compressed_bytes"]]))
            payloads.append({"member": member, "sha256": row["sha256"],
                "bytes": row["bytes"], "estimated_deflated_bytes": compressed,
                "compression_estimate": "maximum_existing_checkpoint_deflate_size",
                "source_kind": "checkpoint", "source_archive": row["source_archive"],
                "source_member": row["source_member"]})
        mapped = {k:v for k,v in row.items() if not k.startswith("source_")}
        mapped.update(final_member=by_content[key], relation_to_current_path=relation)
        history_rows.append(mapped)

    if len(payloads) != len(by_content):
        raise AssertionError("Global content deduplication invariant failed")
    canonical = {p["member"]:p for p in payloads}
    for row in [*current_rows, *[r for r in history_rows if r["kind"] == "file"]]:
        target = canonical[row["final_member"]]
        if (row["sha256"], row["bytes"]) != (target["sha256"], target["bytes"]):
            raise AssertionError("Manifest mapping does not preserve content")

    manifest = {"format": "RESEARCH_SA23_deduplicated_final_v1", "created_utc": created,
        "activity": "packaging only; not mathematical movement",
        "original_inputs": "Use the original attachments; extracted inputs and source scans excluded by checkpoint.py policy are not copied.",
        "source_scan_policy": "Preserves checkpoint.py runtime/source-cache/PDF/web-cache/full-text/scan/ZIP/TeX-auxiliary exclusions. Historical checkpoint manifests are retained as content.",
        "restore_instructions": "For a current view, copy each current_files final_member to its path. For checkpoint N, copy each checkpoint_members row with that number from final_member to original_member. Verify SHA256 and bytes. Identical regular-file content is stored once; directory entries are structural only.",
        "checkpoints": checkpoints, "current_files": current_rows,
        "checkpoint_members": history_rows,
        "canonical_files": [{k:v for k,v in p.items() if not k.startswith("source_")} for p in payloads],
        "current_omissions": omitted, "policy_conflicts": conflicts,
        "files_changed_during_plan": volatile,
        "compression": {"method": "ZIP_DEFLATED", "level": LEVEL, "zlib_version": zlib.ZLIB_VERSION},
        "totals": {"current_logical_files": len(current_rows),
                   "checkpoint_logical_entries": len(history_rows),
                   "canonical_regular_files": len(payloads),
                   "current_content_aliases": sum(not r["canonical_current_path"] for r in current_rows),
                   "historical_distinct_files": sum(p["source_kind"] == "checkpoint" for p in payloads),
                   "historical_changed_path_entries": sum(r.get("relation_to_current_path") == "changed_at_current_path" for r in history_rows),
                   "historical_absent_path_entries": sum(r.get("relation_to_current_path") == "absent_from_current_included_tree" for r in history_rows),
                   "unique_uncompressed_bytes": sum(p["bytes"] for p in payloads)}}
    manifest_bytes = (json.dumps(manifest, indent=2, ensure_ascii=False)+"\n").encode()
    payload_compressed = sum(p["estimated_deflated_bytes"] for p in payloads)
    manifest_compressed = deflated_size_bytes(manifest_bytes)
    all_names = [p["member"] for p in payloads] + [MANIFEST_MEMBER] + sorted(directories)
    # Standard ZIP local+central headers:30+46, two copies of each UTF8 name.
    # There are no comments; file sizes here are below the ZIP64 threshold.
    header_bytes = 22 + sum(76 + 2*len(n.encode("utf-8")) for n in all_names)
    directory_compressed = 2 * len(directories)
    estimate = {"created_utc": created, "activity": "packaging only; not mathematical movement",
        "archive_created": False, "mode": "estimate_only",
        **manifest["totals"], "prior_archive_bytes": sum(x["bytes"] for x in checkpoints),
        "checkpoint_count": len(checkpoints), "checkpoints": checkpoints,
        "estimated_payload_deflated_bytes": payload_compressed,
        "generated_manifest_uncompressed_bytes": len(manifest_bytes),
        "generated_manifest_deflated_bytes": manifest_compressed,
        "estimated_zip_headers_bytes": header_bytes,
        "estimated_total_archive_bytes": payload_compressed+manifest_compressed+header_bytes+directory_compressed,
        "conservative_reserve_bytes": 2_000_000,
        "delivery_limit_bytes": LIMIT, "policy_conflicts": conflicts,
        "files_changed_during_plan": volatile,
        "estimate_basis": "Existing ZIP entry compressed sizes (maximum for equal SHA256/size); raw DEFLATE level6 for new current content; exact generated manifest compression; standard ZIP headers. A2MB reserve allows changed packaging reports and minor metadata differences. Final creation replans and verifies actual bytes.",
        "prior_zip_files_before_run": [str(p) for _,p in discovered]}
    estimate["estimated_with_reserve_bytes"] = estimate["estimated_total_archive_bytes"] + estimate["conservative_reserve_bytes"]
    estimate["below_delivery_limit_with_reserve"] = estimate["estimated_with_reserve_bytes"] < LIMIT
    return manifest, manifest_bytes, payloads, directories, estimate


def copy_payload(out_archive, payload):
    info = zipfile.ZipInfo(payload["member"], date_time=dt.datetime.now().timetuple()[:6])
    info.compress_type = zipfile.ZIP_DEFLATED
    info._compresslevel = LEVEL
    info.external_attr = 0o100644 << 16
    h, size = hashlib.sha256(), 0
    source_zip = None
    if payload["source_kind"] == "current":
        source = Path(payload["source_path"]).open("rb")
    else:
        source_zip = zipfile.ZipFile(payload["source_archive"], "r")
        source = source_zip.open(payload["source_member"], "r")
    try:
        with source, out_archive.open(info, "w", force_zip64=payload["bytes"] >= zipfile.ZIP64_LIMIT) as target:
            while block := source.read(CHUNK):
                h.update(block)
                size += len(block)
                target.write(block)
    finally:
        if source_zip is not None:
            source_zip.close()
    if (h.hexdigest(), size) != (payload["sha256"], payload["bytes"]):
        raise RuntimeError(f"Source changed since plan: {payload['member']}")


def create_final(dest, manifest_bytes, payloads, directories, estimate):
    if dest.suffix != ".zip" or dest.exists():
        raise ValueError("Final output must be a new .zip path; never overwrite")
    if estimate["policy_conflicts"] or estimate["files_changed_during_plan"]:
        raise ValueError("Resolve policy conflicts/volatile files before creating a final package")
    if not estimate["below_delivery_limit_with_reserve"]:
        raise ValueError("Estimated final package exceeds the500MB delivery limit")
    dest.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temp_name = tempfile.mkstemp(prefix=dest.stem+"_", suffix=".partial", dir=dest.parent)
    os.close(descriptor)
    temp = Path(temp_name)
    try:
        with zipfile.ZipFile(temp, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=LEVEL) as archive:
            for payload in payloads:
                copy_payload(archive, payload)
            for directory in sorted(directories):
                archive.writestr(directory, b"")
            archive.writestr(MANIFEST_MEMBER, manifest_bytes)
        expected = {p["member"]:(p["sha256"],p["bytes"]) for p in payloads}
        expected[MANIFEST_MEMBER] = (hashlib.sha256(manifest_bytes).hexdigest(),len(manifest_bytes))
        with zipfile.ZipFile(temp, "r") as archive:
            if set(archive.namelist()) != set(expected) | directories:
                raise AssertionError("Final member inventory differs from manifest plan")
            seen = set()
            for member, fingerprint in expected.items():
                with archive.open(member) as stream:
                    actual = digest_stream(stream)
                if actual != fingerprint:
                    raise AssertionError(f"Final content verification failed: {member}")
                if actual in seen:
                    raise AssertionError("Identical regular-file content stored more than once")
                seen.add(actual)
        if temp.stat().st_size >= LIMIT:
            raise ValueError("Actual archive exceeds500MB; refusing to publish final path")
        # Hard-link creation is atomic and cannot replace a concurrently created path.
        os.link(temp, dest)
        sha, size = digest_path(dest)
        return {"activity":"packaging only; not mathematical movement", "archive_created":True,
                "file":str(dest),"sha256":sha,"bytes":size,"created_utc":now(),
                "regular_files":len(expected),"all_contents_verified":True}
    finally:
        temp.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--estimate", action="store_true", help="Default; no archive creation")
    mode.add_argument("--create-final", type=Path, metavar="NEW_ZIP_PATH",
                      help="Explicit later-use switch; only after the stopping rule triggers")
    parser.add_argument("--estimate-report", type=Path, default=ROOT/"notes/geometry_final_package_estimate.json")
    parser.add_argument("--plan-report", type=Path, default=ROOT/"notes/geometry_final_package_plan.json")
    args = parser.parse_args()
    manifest, data, payloads, directories, estimate = build_plan()
    if args.create_final is not None:
        # Do not overwrite report files that were hashed as current content.
        print(json.dumps(create_final(args.create_final.resolve(), data, payloads, directories, estimate), indent=2))
    else:
        args.plan_report.parent.mkdir(parents=True, exist_ok=True)
        args.estimate_report.parent.mkdir(parents=True, exist_ok=True)
        args.plan_report.write_bytes(data)
        args.estimate_report.write_text(json.dumps(estimate, indent=2)+"\n")
        after = [str(p) for _,p in checkpoint_paths()]
        if after != estimate["prior_zip_files_before_run"]:
            raise RuntimeError("Checkpoint inventory changed during estimate; rerun later")
        print(json.dumps(estimate, indent=2))


if __name__ == "__main__":
    main()
