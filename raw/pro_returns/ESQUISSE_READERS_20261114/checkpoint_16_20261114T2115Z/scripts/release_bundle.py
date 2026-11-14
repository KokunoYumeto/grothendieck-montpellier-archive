#!/usr/bin/env python3
"""Create immutable checkpoints and reconcile/package the final edition.

All archive members and documentary references use edition-relative paths.
No original input archive or earlier checkpoint ZIP is embedded in an output.
"""
from __future__ import annotations

import argparse
import csv
import difflib
import fcntl
import hashlib
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time
from zipfile import ZipFile, ZIP_DEFLATED
from privacy_rules import redact_history

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT.parent.parent / "output"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def tsv_bytes(rows, fields):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def read_tsv(path):
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def eligible(path):
    relative = path.relative_to(ROOT)
    return path.is_file() and not any(p.startswith(".") or p == "__pycache__" for p in relative.parts) and path.suffix not in {".pyc", ".lock", ".zip"}


def snapshot():
    result = {}
    for path in sorted(p for p in ROOT.rglob("*") if eligible(p)):
        for attempt in range(5):
            before = path.stat()
            data = path.read_bytes()
            after = path.stat()
            if (before.st_mtime_ns, before.st_size) == (after.st_mtime_ns, after.st_size):
                result[path.relative_to(ROOT).as_posix()] = data
                break
        else:
            raise RuntimeError("File changed repeatedly during snapshot: " + path.name)
    return result


def preserve_details():
    source = ROOT.parent / "crops"
    destination = ROOT / "records" / "review_details"
    destination.mkdir(parents=True, exist_ok=True)
    rows = []
    for path in sorted(source.glob("*")):
        if not path.is_file():
            continue
        target = destination / path.name
        data = path.read_bytes()
        if not target.exists() or target.read_bytes() != data:
            target.write_bytes(data)
        rows.append({"path": target.relative_to(ROOT).as_posix(), "bytes": len(data), "sha256": sha(data), "role": "Targeted enlargement or comparison made from the supplied scans for the recorded review; full original scans remain in the supplied SCANS archive."})
    (ROOT / "records" / "REVIEW_DETAILS.tsv").write_bytes(tsv_bytes(rows, ["path", "bytes", "sha256", "role"]))


def progress():
    audit_path = ROOT / "records" / "AUDIT_PROGRESS.json"
    audit = json.loads(audit_path.read_text()) if audit_path.exists() else {}
    checked = sorted((ROOT / "checked_pages").glob("*.tex"))
    copy1 = [p for p in checked if p.stem.startswith("esq_")]
    copy2 = [p for p in checked if p.stem.startswith("esq119_")]
    translated = sorted((ROOT / "translated_pages").glob("esq_*.tex"))
    guide = sorted(p for p in (ROOT / "guide_fragments").glob("[0-9][0-9]_*.tex") if p.name != "00_preface.tex")
    text = "# Edition progress\n\n"
    text += "Both supplied archives passed all manifest byte-count and SHA-256 checks. The source images and original transcription are preserved unchanged in the supplied inputs.\n\n"
    text += f"Checked source pages: {len(checked)}/116; copy 1: {len(copy1)}/58; copy 2: {len(copy2)}/58. "
    text += f"The last committed copy2 site is {int(copy2[-1].stem.rsplit('_',1)[1]) if copy2 else 'none'}. "
    text += f"Recorded difference outcomes: {audit.get('difference_outcomes','see current table')}/468; collated page pairs: {audit.get('collated_page_pairs','see current table')}/58.\n\n"
    text += f"English source-page translations present: {len(translated)}/58. Guide commentary units present: {len(guide)}/18. "
    text += "These counts record authored material; final release status is governed by RELEASE_STATUS.json, the audit validation and exact-PDF visual records.\n\n"
    text += "The rounded ring glyph has an embedded vector definition and linked doubt marks. The six diagonal arrows on typescript p.56 are marked as handwritten while its horizontal hooks and objects retain their checked typing classification. Detailed comparisons and second readings are retained in records/.\n\n"
    text += "Current reader build measurements are in PDF_CHECKS.json and FINAL_PDF_AUDIT.json. Earlier build results remain in BUILD_HISTORY.jsonl. Superseded scan reviews are retained in reviews/history/. A checkpoint is a working snapshot and does not by itself certify a completed reader.\n"
    (ROOT / "records" / "PROGRESS.md").write_text(text)


def checkpoint(number=None):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    existing = list(OUTPUT.glob("ESQUISSE_READERS_checkpoint_*.zip"))
    if number is None:
        number = 1 + max([int(p.stem.rsplit("_",1)[1]) for p in existing] or [0])
    target = OUTPUT / f"ESQUISSE_READERS_checkpoint_{number:02d}.zip"
    if target.exists():
        raise FileExistsError("An immutable checkpoint already has this name")
    preserve_details()
    progress()
    with (ROOT / ".audit-records.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        files = snapshot()
        manifest = tsv_bytes([{"path": name, "bytes": len(data), "sha256": sha(data)} for name, data in files.items()], ["path", "bytes", "sha256"])
        with ZipFile(target, "x", ZIP_DEFLATED, compresslevel=9) as archive:
            for name, data in files.items():
                archive.writestr(name, data)
            archive.writestr("CHECKPOINT_CONTENTS.tsv", manifest)
    manifest_dir = ROOT / "records" / "checkpoint_manifests"
    manifest_dir.mkdir(exist_ok=True)
    (manifest_dir / f"checkpoint_{number:02d}.tsv").write_bytes(manifest)
    print(json.dumps({"checkpoint": target.name, "files": len(files), "bytes": target.stat().st_size, "sha256": sha(target.read_bytes())}))


def record_checkpoint(name, library_id):
    if not re.fullmatch(r"ESQUISSE_READERS_checkpoint_\d+\.zip", name):
        raise ValueError("Unexpected checkpoint filename")
    path = ROOT / "records" / "CHECKPOINTS.tsv"
    fields = ["checkpoint", "last_checked_copy1_site", "copy2_status", "library_file_id"]
    rows = read_tsv(path)
    old = next((r for r in rows if r["checkpoint"] == name), None)
    if old:
        if old["library_file_id"] != library_id:
            raise ValueError("Checkpoint identity already recorded differently")
        print(json.dumps({"checkpoint": name, "status": "identity already recorded"}))
        return
    one = sorted((ROOT / "checked_pages").glob("esq_*.tex"))
    two = sorted((ROOT / "checked_pages").glob("esq119_*.tex"))
    rows.append({"checkpoint": name, "last_checked_copy1_site": int(one[-1].stem.rsplit("_",1)[1]) if one else "", "copy2_status": "through site " + str(int(two[-1].stem.rsplit("_",1)[1])) if two else "not yet checked", "library_file_id": library_id})
    path.write_bytes(tsv_bytes(rows, fields))
    print(json.dumps({"checkpoint": name, "status": "identity recorded"}))


def reconciliation_reason(name):
    if name.startswith(("FR/", "EN/", "GUIDE/")):
        return "Superseded by the final complete, regenerated and validated file at the same relative path. Earlier coverage, apparatus or typesetting was provisional; its build history is retained."
    if name.startswith(("checked_pages/", "reviews/")):
        return "Superseded by the final scan decision and replayable checked source at the same relative path. Prior reading decisions remain in review history and the accompanying exact text diff."
    if name.startswith(("translated_pages/", "guide_fragments/")):
        return "Superseded by the complete reviewed translation or commentary at the same relative path. The exact text diff identifies all replaced or removed passages."
    if name.startswith(("scripts/", "templates/")):
        return "Superseded by the final generation or validation implementation at the same relative path; the exact text diff preserves replaced implementation passages."
    return "Superseded by the final accumulated or regenerated record at the same relative path; retained histories and the exact text diff identify the earlier state."


def reconcile():
    history = ROOT / "records" / "checkpoint_history"
    history.mkdir(exist_ok=True)
    manifest_dir = ROOT / "records" / "checkpoint_manifests"
    manifest_dir.mkdir(exist_ok=True)
    omitted = {r["omitted_path"]:r for r in read_tsv(ROOT / "records" / "OMITTED_CHECKPOINT_FILES.tsv")}
    files = snapshot()
    rows = []
    redactions = []
    for source in sorted(OUTPUT.glob("ESQUISSE_READERS_checkpoint_*.zip")):
        number = int(source.stem.rsplit("_",1)[1])
        with ZipFile(source) as archive:
            for name in archive.namelist():
                if name.endswith("/"):
                    continue
                old = archive.read(name)
                target_name = name
                diff_name = ""
                if name == "CHECKPOINT_CONTENTS.tsv":
                    target_name = f"records/checkpoint_manifests/checkpoint_{number:02d}.tsv"
                    (ROOT / target_name).write_bytes(old)
                    current = old
                    status = "preserved with explicit archival name"
                    reason = "The checkpoint-specific manifest is retained verbatim under its numbered archival name."
                elif name in files:
                    current = files[name]
                    status = "unchanged" if current == old else "superseded"
                    reason = "Byte-identical content retained." if status == "unchanged" else reconciliation_reason(name)
                    if current != old:
                        try:
                            before_text = old.decode("utf-8")
                            after_text = current.decode("utf-8")
                        except UnicodeDecodeError:
                            reason += " Binary replacement is identified by both hashes; no old reader PDF is presented as the final reader."
                        else:
                            diff_name = "records/checkpoint_history/" + sha((source.name + "!/" + name + sha(old) + sha(current)).encode())[:24] + ".diff.txt"
                            before_text, old_redactions = redact_history(before_text, name)
                            after_text, new_redactions = redact_history(after_text, name)
                            for side, items in [("checkpoint", old_redactions), ("final", new_redactions)]:
                                for item in items:
                                    redactions.append({"checkpoint":source.name,"path":name,"side":side,
                                        "line":item["line"],"column":item["column"],"start_character":item["start"],
                                        "removed_characters":item["end"]-item["start"],"kind":item["kind"],
                                        "removed_sha256":item["removed_sha256"],"diff":diff_name,
                                        "reason":"Excluded from the historical diff under the requested privacy rule. The current file at the same relative path supersedes this older implementation passage; original checkpoint bytes remain identified by their recorded hash."})
                            if old_redactions or new_redactions:
                                reason += " Path/address spans in the historical diff are explicitly redacted and individually accounted for in records/CHECKPOINT_PRIVACY_REDACTIONS.tsv."
                            before = before_text.splitlines(keepends=True)
                            after = after_text.splitlines(keepends=True)
                            patch = "".join(difflib.unified_diff(before, after, fromfile=source.name + "!/" + name, tofile="final!/" + name))
                            (ROOT / diff_name).write_text(patch)
                elif name in omitted:
                    current = b""
                    status = "omitted supplied duplicate"
                    target_name = omitted[name]["superseded_by"]
                    reason = omitted[name]["reason"]
                else:
                    raise RuntimeError("Unaccounted checkpoint member: " + source.name + "!/" + name)
                rows.append({"checkpoint": source.name, "path": name, "checkpoint_sha256": sha(old), "final_path": target_name, "final_sha256": sha(current) if current else "", "status": status, "reason": reason, "exact_passage_diff": diff_name})
    referenced_diffs = {row["exact_passage_diff"] for row in rows if row["exact_passage_diff"]}
    archived_diffs = {row["path"] for row in rows if row["path"].startswith("records/checkpoint_history/")}
    for previous_diff in history.glob("*.diff.txt"):
        relative = previous_diff.relative_to(ROOT).as_posix()
        if (re.fullmatch(r"[0-9a-f]{24}\.diff\.txt", previous_diff.name)
                and relative not in referenced_diffs and relative not in archived_diffs):
            previous_diff.unlink()
    fields = ["checkpoint", "path", "checkpoint_sha256", "final_path", "final_sha256", "status", "reason", "exact_passage_diff"]
    (ROOT / "records" / "CHECKPOINT_RECONCILIATION.tsv").write_bytes(tsv_bytes(rows, fields))
    redaction_fields=["checkpoint","path","side","line","column","start_character","removed_characters","kind","removed_sha256","diff","reason"]
    (ROOT / "records" / "CHECKPOINT_PRIVACY_REDACTIONS.tsv").write_bytes(tsv_bytes(redactions, redaction_fields))
    counts = {state:sum(r["status"] == state for r in rows) for state in sorted({r["status"] for r in rows})}
    text = "# Checkpoint reconciliation\n\nEvery member of every immutable checkpoint is accounted for in CHECKPOINT_RECONCILIATION.tsv. Its earlier hash, final destination and hash, status, and reason are explicit. For replaced UTF-8 files, the linked unified diff lists removed passages and their replacements, with the privacy redactions described below. Earlier partial reader PDFs are identified by hash and superseded by the final compiled PDF; their build measurements remain in BUILD_HISTORY.jsonl.\n\n"
    text += "| Status | Checkpoint members |\n|---|---:|\n" + "".join(f"| {state} | {count} |\n" for state,count in counts.items())
    text += "\nThe supplied input-table duplicates removed after checkpoint03 remain in the original TEXT archive and are individually listed in OMITTED_CHECKPOINT_FILES.tsv. No original archive or earlier checkpoint ZIP is embedded in these final packages.\n"
    text += f"\nHistorical text diffs contain {len(redactions)} explicit path/address-span redactions, individually listed in CHECKPOINT_PRIVACY_REDACTIONS.tsv by checkpoint, relative file, original line/column, character range, removed-span SHA-256 and reason. Each redacted span is replaced by a labelled hash marker; the other diff text is exact. This accounts for the omitted path strings without copying them into the final records. The immutable earlier checkpoints are unchanged.\n"
    (ROOT / "records" / "CHECKPOINT_RECONCILIATION.md").write_text(text)
    print(json.dumps({"checkpoint_members":len(rows), "statuses":counts, "privacy_redactions":len(redactions), "unaccounted":0}))


def package():
    gate_path = ROOT / "records" / "RELEASE_VALIDATION.json"
    # Recheck current sources/PDFs, then account for the final gate report itself
    # in checkpoint history. The gate is deterministic, so this second pass must
    # leave it unchanged; this avoids a self-referential timestamp/hash cycle.
    reconcile()
    gate_command = [sys.executable, str(ROOT / "scripts" / "validate_release.py")]
    first = subprocess.run(gate_command, capture_output=True, text=True)
    if first.returncode or not gate_path.exists() or not json.loads(gate_path.read_text()).get("passed"):
        raise RuntimeError("Current final release validation failed; see records/RELEASE_VALIDATION.json")
    index = subprocess.run([sys.executable, str(ROOT / "translated_pages" / "refresh_index.py")], capture_output=True, text=True)
    if index.returncode:
        raise RuntimeError("The final translation index failed its source, math or doubt-mark replay")
    readme = subprocess.run([sys.executable, str(ROOT / "scripts" / "write_readme.py"), "--strict"], capture_output=True, text=True)
    if readme.returncode:
        raise RuntimeError("The final README still has an open release gate; see README.md")
    approved_gate = gate_path.read_bytes()
    reconcile()
    second = subprocess.run(gate_command, capture_output=True, text=True)
    if second.returncode or gate_path.read_bytes() != approved_gate:
        raise RuntimeError("Release evidence changed during final reconciliation; review the gate before packaging")
    files = snapshot()
    # The content manifest deliberately excludes itself. A previous attempt's
    # generated manifest must not become a stale self-entry in a retry.
    files.pop("records/FINAL_CONTENTS.tsv", None)
    groups = {"ESQUISSE_READERS_FR.zip":{}, "ESQUISSE_READERS_EN.zip":{}, "ESQUISSE_READERS_RECORDS.zip":{}}
    for name, data in files.items():
        if name.startswith("FR/"):
            groups["ESQUISSE_READERS_FR.zip"][name] = data
        elif name.startswith(("EN/", "GUIDE/")):
            groups["ESQUISSE_READERS_EN.zip"][name] = data
        else:
            groups["ESQUISSE_READERS_RECORDS.zip"][name] = data
    for contents in groups.values():
        contents["README.md"] = files["README.md"]
    manifest = [{"archive":archive,"path":name,"bytes":len(data),"sha256":sha(data)} for archive,contents in groups.items() for name,data in sorted(contents.items())]
    manifest_data = tsv_bytes(manifest,["archive","path","bytes","sha256"])
    (ROOT / "records" / "FINAL_CONTENTS.tsv").write_bytes(manifest_data)
    groups["ESQUISSE_READERS_RECORDS.zip"]["records/FINAL_CONTENTS.tsv"] = manifest_data
    result=[]
    for name, contents in groups.items():
        destination = OUTPUT / name
        if destination.exists():
            raise FileExistsError("Final package already exists; do not overwrite a published package")
        with ZipFile(destination,"x",ZIP_DEFLATED,compresslevel=9) as archive:
            for member,data in sorted(contents.items()):
                archive.writestr(member,data)
        result.append({"archive":name,"files":len(contents),"bytes":destination.stat().st_size,"sha256":sha(destination.read_bytes())})
    print(json.dumps(result))


def main():
    parser=argparse.ArgumentParser()
    sub=parser.add_subparsers(dest="command",required=True)
    checkpoint_parser=sub.add_parser("checkpoint");checkpoint_parser.add_argument("--number",type=int)
    record_parser=sub.add_parser("record-checkpoint");record_parser.add_argument("name");record_parser.add_argument("library_id")
    sub.add_parser("preserve-details");sub.add_parser("reconcile");sub.add_parser("package")
    args=parser.parse_args()
    if args.command=="checkpoint":checkpoint(args.number)
    elif args.command=="record-checkpoint":record_checkpoint(args.name,args.library_id)
    elif args.command=="preserve-details":preserve_details()
    elif args.command=="reconcile":reconcile()
    elif args.command=="package":package()


if __name__=="__main__":
    main()
