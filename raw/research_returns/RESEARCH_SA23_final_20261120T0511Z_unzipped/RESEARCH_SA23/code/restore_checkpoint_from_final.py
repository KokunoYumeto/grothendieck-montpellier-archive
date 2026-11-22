#!/usr/bin/env python3
"""Restore original logical paths from the deduplicated final-package ZIP.

This utility reads an existing final archive. It never creates an archive.
It validates paths, byte counts and SHA256 before creating a new destination,
and refuses an existing destination, symlinks and special ZIP members.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import zipfile

PREFIX = "RESEARCH_SA23"
FORMAT = "RESEARCH_SA23_deduplicated_final_v1"
MANIFEST = f"{PREFIX}/final_package_manifest.json"
CHUNK = 1024 * 1024


def safe_path(value, *, directory=False, require_root=True):
    """Reject aliases and traversal before treating a ZIP name as a path."""
    if not isinstance(value, str) or not value or "\\" in value or "\0" in value or ":" in value:
        raise ValueError(f"Unsafe member path: {value!r}")
    raw = value[:-1] if directory and value.endswith("/") else value
    parts = raw.split("/")
    if any(part in {"", ".", ".."} for part in parts):
        raise ValueError(f"Noncanonical member path: {value!r}")
    path = PurePosixPath(raw)
    if path.is_absolute() or (require_root and parts[0] != PREFIX):
        raise ValueError(f"Member is outside the package root: {value!r}")
    if require_root and len(parts) == 1 and not directory:
        raise ValueError("A regular file cannot be the package root")
    return path


def fingerprint(row):
    sha, size = row.get("sha256"), row.get("bytes")
    if not isinstance(sha, str) or re.fullmatch(r"[0-9a-f]{64}", sha) is None:
        raise ValueError("Missing or invalid SHA256 in manifest")
    if type(size) is not int or size < 0:
        raise ValueError("Missing or invalid byte count in manifest")
    return sha, size


def read_manifest(archive):
    infos = {}
    for info in archive.infolist():
        safe_path(info.filename, directory=info.is_dir())
        if info.filename in infos:
            raise ValueError(f"Duplicate ZIP member: {info.filename}")
        kind = stat.S_IFMT(info.external_attr >> 16)
        allowed = {0, stat.S_IFDIR if info.is_dir() else stat.S_IFREG}
        if kind not in allowed:
            raise ValueError(f"Symlink or special ZIP member: {info.filename}")
        if info.flag_bits & 1:
            raise ValueError(f"Encrypted member is unsupported: {info.filename}")
        infos[info.filename] = info
    if MANIFEST not in infos or infos[MANIFEST].is_dir():
        raise ValueError("Final-package manifest is missing")
    document = json.loads(archive.read(MANIFEST))
    if not isinstance(document, dict) or document.get("format") != FORMAT:
        raise ValueError("Unsupported final-package manifest format")
    return document, infos


def restoration_plan(document, infos, *, checkpoint=None, current=False):
    canonical = {}
    for row in document["canonical_files"]:
        name = row["member"]
        safe_path(name)
        expected = fingerprint(row)
        if name in canonical:
            raise ValueError(f"Duplicate canonical mapping: {name}")
        if name not in infos or infos[name].is_dir() or infos[name].file_size != expected[1]:
            raise ValueError(f"Canonical payload missing or wrong size: {name}")
        canonical[name] = expected

    if current:
        selected = []
        for original in document["current_files"]:
            relative = safe_path(original["path"], require_root=False)
            selected.append({**original, "original_member": f"{PREFIX}/{relative}", "kind": "file"})
    else:
        checkpoints = [row for row in document["checkpoints"] if row["checkpoint"] == checkpoint]
        if len(checkpoints) != 1:
            raise ValueError(f"Checkpoint {checkpoint} is not uniquely recorded")
        selected = [row for row in document["checkpoint_members"] if row["checkpoint"] == checkpoint]
        if len(selected) != checkpoints[0]["entries"]:
            raise ValueError("Checkpoint mapping does not cover its recorded entry count")

    files, directories, seen = [], set(), set()
    for row in selected:
        kind = row.get("kind")
        if kind not in {"file", "directory"}:
            raise ValueError(f"Unsupported logical member kind: {kind!r}")
        target = safe_path(row["original_member"], directory=kind == "directory")
        if target in seen:
            raise ValueError(f"Duplicate logical destination: {target}")
        seen.add(target)
        source = row["final_member"]
        safe_path(source, directory=kind == "directory")
        if kind == "directory":
            if source not in infos or not infos[source].is_dir():
                raise ValueError(f"Mapped structural directory is missing: {source}")
            directories.add(target)
        else:
            expected = fingerprint(row)
            if canonical.get(source) != expected:
                raise ValueError(f"Logical/canonical fingerprint mismatch: {source}")
            files.append((target, source, expected))
        directories.update(p for p in target.parents if str(p) != ".")
    file_paths = {row[0] for row in files}
    if file_paths & directories:
        raise ValueError("A logical file is also required as a directory")
    return sorted(files), sorted(directories, key=lambda p: (len(p.parts), str(p)))


def transfer_checked(archive, member, expected, output=None):
    digest, size = hashlib.sha256(), 0
    with archive.open(member) as stream:
        while block := stream.read(CHUNK):
            size += len(block)
            if size > expected[1]:
                raise ValueError(f"Payload exceeds declared byte count: {member}")
            digest.update(block)
            if output is not None:
                output.write(block)
    if (digest.hexdigest(), size) != expected:
        raise ValueError(f"Payload SHA256 or byte count mismatch: {member}")


def restore(archive, files, directories, destination=None):
    # Check every distinct selected payload before making any output directory.
    verified = {}
    for _, source, expected in files:
        if source not in verified:
            transfer_checked(archive, source, expected)
            verified[source] = expected
    report = {"logical_files": len(files), "logical_directories": len(directories),
              "verified_canonical_payloads": len(verified), "bytes_restored": sum(r[2][1] for r in files)}
    if destination is None:
        return {**report, "mode": "verify_only", "destination_created": False}

    destination = Path(destination).absolute()
    if not destination.parent.is_dir():
        raise ValueError("Destination parent must already be a directory")
    # mkdir without exist_ok rejects files, empty directories and dangling symlinks.
    destination.mkdir(mode=0o700)
    try:
        for relative in directories:
            path = destination.joinpath(*relative.parts)
            path.mkdir(mode=0o700)  # Every directory is new and listed only once.
        for relative, source, expected in files:
            path = destination.joinpath(*relative.parts)
            flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0)
            fd = os.open(path, flags, 0o600)
            with os.fdopen(fd, "wb") as output:
                transfer_checked(archive, source, expected, output)
    except BaseException:
        print(f"Restoration failed; the new directory may contain partial files: {destination}", file=sys.stderr)
        raise
    return {**report, "mode": "restored", "destination_created": True,
            "destination": str(destination), "package_root": str(destination / PREFIX)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path, help="Existing deduplicated final-package ZIP")
    choice = parser.add_mutually_exclusive_group(required=True)
    choice.add_argument("--list", action="store_true", help="List available checkpoint numbers; writes nothing")
    choice.add_argument("--checkpoint", type=int, help="Restore every logical member of this checkpoint")
    choice.add_argument("--current", action="store_true", help="Restore the current logical files")
    parser.add_argument("--destination", type=Path, help="New, nonexistent directory under an existing parent")
    parser.add_argument("--verify-only", action="store_true", help="Validate selected contents without writing files")
    args = parser.parse_args(argv)
    if args.list and (args.destination is not None or args.verify_only):
        parser.error("--list takes neither --destination nor --verify-only")
    if not args.list and (args.verify_only == (args.destination is not None)):
        parser.error("Choose exactly one of --destination or --verify-only")
    if args.checkpoint is not None and args.checkpoint < 1:
        parser.error("--checkpoint must be positive")
    try:
        with zipfile.ZipFile(args.archive) as archive:
            document, infos = read_manifest(archive)
            if args.list:
                report = {"format": document["format"], "created_utc": document["created_utc"],
                          "checkpoints": document["checkpoints"],
                          "current_logical_files": len(document["current_files"]), "destination_created": False}
            else:
                files, directories = restoration_plan(document, infos, checkpoint=args.checkpoint, current=args.current)
                report = restore(archive, files, directories, args.destination)
                report["view"] = "current" if args.current else f"checkpoint_{args.checkpoint:02d}"
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError, zipfile.BadZipFile) as exc:
        print(f"Refused restoration: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
