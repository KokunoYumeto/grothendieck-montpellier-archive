#!/usr/bin/env python3
"""Package the complete checked edition after all release gates pass.

--plan is read-only and can run while work continues. --build reruns the release
audit, refreshes README, accounts for every member of every saved checkpoint,
writes the final file manifest, and verifies all three ZIPs before naming them.
The account and manifest are generated after the last checkpoint, so neither
document has to contain its own future digest.
"""
from __future__ import annotations

import argparse
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

EDITION = Path(__file__).resolve().parents[1]
WORK = EDITION.parent
CHECKPOINTS = WORK / "checkpoints"
OUTPUT = WORK / "deliverables"
PACKAGES = {k: "EGA_V_READERS_" + k + ".zip" for k in ("FR", "EN", "RECORDS")}
FR = (
    "EGA_V_FR_diplomatique", "EGA_V_FR_corrige_apparat",
    "EGA_V_FR_texte_de_lecture", "EGA_V_FR_master_annotated",
)
EN = (
    "EGA_V_EN_corrected_translator_notes", "EGA_V_EN_reading",
    "EGA_V_EN_master_annotated", "EGA_V24_EN_diplomatic",
    "EGA_V24_EN_corrected_apparatus", "EGA_V24_EN_reading",
    "EGA_V24_EN_master_annotated",
)
GUIDE = "EGA_V_GUIDE"
STEMS = FR + EN + (GUIDE,)
ACCOUNT = "records/CHECKPOINT_MEMBER_ACCOUNT.tsv"
SUMMARY = "records/CHECKPOINT_MEMBER_ACCOUNT_SUMMARY.json"
MANIFEST = "records/FINAL_FILE_MANIFEST.tsv"
POLICY = "records/PACKAGE_POLICY.md"
GENERATED = {ACCOUNT, SUMMARY, MANIFEST, POLICY}
TEXT_SUFFIXES = {".tex", ".tsv", ".json", ".md", ".txt", ".py", ".log", ".diff", ".started"}
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg"}
AUX_SUFFIXES = {".aux", ".out", ".fmt", ".fls", ".fdb_latexmk", ".synctex"}
PRIVATE = {
    "email": re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}"),
    "absolute path": re.compile(r"/(?:workspace|home|tmp|mnt|usr|opt|etc|var|Users|data)/|(?<![\w])[A-Za-z]:\\(?:[^\\\s{}$]+\\)+[^\\\s{}$]+"),
}


def sha_stream(stream):
    digest = hashlib.sha256()
    while block := stream.read(1024 * 1024):
        digest.update(block)
    return digest.hexdigest()


def sha(path):
    with path.open("rb") as stream:
        return sha_stream(stream)


def read_tsv(path):
    with path.open(newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def write_tsv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".new")
    with temporary.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(path)


def family(stem):
    return "FR" if stem in FR else "EN"


def primary_pdf(stem):
    return ("FR" if stem == GUIDE else family(stem), stem + ".pdf")


def file_destinations(relative):
    """Return final destinations and an explicit reason for any omission."""
    path = PurePosixPath(relative)
    suffix = path.suffix.lower()
    if "__pycache__" in path.parts or suffix == ".pyc":
        return [], "Regenerable Python bytecode cache; the authored Python source is retained."
    if suffix == ".lock" or path.name.endswith(".new"):
        return [], "Runtime coordination or atomic-write temporary file; the completed documentary records are retained."
    if suffix in AUX_SUFFIXES or path.name.endswith(".synctex.gz"):
        return [], "Regenerable TeX auxiliary or engine-format state; standalone TeX, final PDFs and sanitized build logs are retained."
    if suffix == ".pdf":
        stem = path.stem
        if stem in STEMS and relative == f"build/{stem}/{stem}.pdf":
            packages = ("FR", "EN") if stem == GUIDE else (family(stem),)
            return [(p, stem + ".pdf") for p in packages], ""
        if stem in STEMS:
            return [], "Earlier development PDF superseded by the final PDF of the same named work."
        if stem in {"texput", "MARGIN_DIAGNOSTIC"}:
            return [], "Toolchain or margin-routing diagnostic PDF; it is not a reader. Its diagnostic source/logs and the resulting repair records are retained."
        raise ValueError("Unclassified PDF: " + relative)
    if suffix in IMAGE_SUFFIXES and path.parts[:2] != ("build", "visual_review"):
        return [], "Reproducible crop of supplied scan or working render; the supplied image source remains external, while final full-page PDF-review evidence is retained."
    if suffix not in TEXT_SUFFIXES | IMAGE_SUFFIXES:
        raise ValueError("Unclassified file type: " + relative)
    destinations = [("RECORDS", relative)]
    if relative == "README.md":
        destinations += [("FR", relative), ("EN", relative)]
    if len(path.parts) == 2 and path.parts[0] == "readers" and suffix == ".tex" and path.stem in STEMS:
        packages = ("FR", "EN") if path.stem == GUIDE else (family(path.stem),)
        destinations += [(p, path.name) for p in packages]
    return destinations, ""


def collect(include_generated=True):
    selected = {}
    omitted = {}
    entries = []
    for path in sorted(EDITION.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(EDITION).as_posix()
        if not include_generated and relative in GENERATED:
            continue
        destinations, reason = file_destinations(relative)
        if not destinations:
            omitted[relative] = reason
            continue
        selected[relative] = dict(path=path, destinations=destinations)
        for package, member in destinations:
            entries.append(dict(package=package, member=member, edition_source=relative, path=path))
    identities = [(entry["package"], entry["member"]) for entry in entries]
    if len(set(identities)) != len(identities):
        raise ValueError("Duplicate package member destination.")
    return selected, omitted, sorted(entries, key=lambda row: (row["package"], row["member"]))


def checkpoint_inventory():
    catalog = read_tsv(EDITION / "records/CHECKPOINT_CATALOG.tsv")
    catalog.sort(key=lambda row: int(row["number"]))
    expected = [int(row["number"]) for row in catalog]
    if expected != list(range(1, len(catalog) + 1)):
        raise ValueError("Checkpoint catalog does not contain a continuous numbered sequence.")
    actual = {p.name for p in CHECKPOINTS.glob("EGA_V_READERS_checkpoint_*.zip")}
    if actual != {row["filename"] for row in catalog}:
        raise ValueError("Checkpoint directory and saved catalog differ.")
    for row in catalog:
        if row["status"] != "saved" or not row["library_file_id"]:
            raise ValueError("Checkpoint lacks a successful persistence receipt: " + row["filename"])
    return catalog


def successor_reason(relative):
    if relative.startswith("checked_pages/"):
        return "Superseded by the complete checked page; reading changes and later physical-layer decisions remain in CHECK_DECISIONS.tsv, with explicit supersessions where applicable."
    if relative.startswith(("master_pages/", "translations/", "variant_records/", "cleaned_pages/", "corrected_pages/", "readers/")):
        return "Superseded by the complete source generated from the final checked page and recorded translation/variant/layout decisions; the corresponding audit records are retained."
    if relative.startswith("scripts/"):
        return "Superseded by the final build or audit script; its current implementation reproduces the completed edition and its records."
    if relative.startswith("guide_parts/"):
        return "Superseded by the completed guide paragraph; its source references and documented revisions are retained."
    if relative.startswith("build/"):
        return "Superseded by the final build diagnostic, audit, or review manifest for the named work; build-attempt and exact-PDF review histories remain in the records."
    if relative.startswith("development/"):
        return "Superseded by the retained documentary development version, including sanitization of runtime paths where required; final reader sources and build records are separately identified."
    return "Superseded by the completed cumulative record or report at this path; earlier decisions and their explicit supersessions remain in the documentary history."


def checkpoint_account(catalog, selected, omitted, *, hashes):
    """Every historical ZIP member receives one explicit disposition."""
    aliases = {
        "build/lualatex.log": "development/toolchain_smoke/lualatex.log",
        "build/texput.log": "development/toolchain_smoke/texput.log",
    }
    rows = []
    totals = []
    for checkpoint in catalog:
        archive = CHECKPOINTS / checkpoint["filename"]
        if hashes:
            if archive.stat().st_size != int(checkpoint["bytes"]) or sha(archive) != checkpoint["sha256"]:
                raise ValueError("Saved checkpoint bytes or SHA-256 differs: " + archive.name)
        counts = Counter()
        with ZipFile(archive) as source:
            names = source.namelist()
            if len(names) != len(set(names)):
                raise ValueError("Duplicate member in " + archive.name)
            for info in source.infolist():
                if info.is_dir():
                    continue
                old = PurePosixPath(info.filename)
                if old.parts[0] != "edition" or ".." in old.parts:
                    raise ValueError("Unexpected checkpoint path: " + info.filename)
                relative = PurePosixPath(*old.parts[1:]).as_posix()
                if relative in GENERATED:
                    raise ValueError("Generate the final account only after the last checkpoint; a generated account is already present in " + archive.name)
                old_hash = ""
                if hashes:
                    with source.open(info) as stream:
                        old_hash = sha_stream(stream)
                replacement = relative
                package = member = new_hash = ""
                if relative in selected:
                    target = selected[relative]
                    package, member = target["destinations"][0]
                    new_hash = target.get("sha256", "")
                    disposition = "retained" if hashes and old_hash == new_hash else "superseded"
                    reason = "Identical bytes retained at the stated final member." if disposition == "retained" else successor_reason(relative)
                elif old.suffix.lower() == ".pdf" and old.stem in STEMS:
                    package, member = primary_pdf(old.stem)
                    replacement = f"build/{old.stem}/{old.stem}.pdf"
                    if replacement not in selected:
                        raise ValueError("Final replacement PDF missing for " + info.filename)
                    new_hash = selected[replacement].get("sha256", "")
                    disposition = "retained" if hashes and old_hash == new_hash else "superseded"
                    reason = "Identical PDF bytes retained in the language package." if disposition == "retained" else "Earlier PDF superseded by the final compiled and visually reviewed PDF of the same named work; source, attempt, repair and review histories are retained."
                elif relative in aliases:
                    replacement = aliases[relative]
                    target = selected[replacement]
                    package, member = target["destinations"][0]
                    new_hash = target.get("sha256", "")
                    disposition = "retained" if hashes and old_hash == new_hash else "superseded"
                    reason = "Bootstrap diagnostic relocated to the documentary toolchain directory; the retained version is sanitized for publication."
                else:
                    destinations, reason = file_destinations(relative)
                    if destinations:
                        raise ValueError("Historical member lacks an explicit successor: " + info.filename)
                    disposition = "omitted"
                    replacement = ""
                counts[disposition] += 1
                rows.append(dict(checkpoint_number=checkpoint["number"], checkpoint=archive.name,
                    member=info.filename, bytes=info.file_size, sha256=old_hash,
                    disposition=disposition, final_package=PACKAGES[package] if package else "",
                    final_member=member, final_sha256=new_hash, successor_source=replacement, reason=reason))
        totals.append(dict(number=int(checkpoint["number"]), checkpoint=archive.name,
            bytes=int(checkpoint["bytes"]), sha256=checkpoint["sha256"],
            library_file_id=checkpoint["library_file_id"], members=sum(counts.values()), counts=dict(counts)))
    return rows, totals


def privacy_screen(selected):
    failures = []
    for relative, item in selected.items():
        path = item["path"]
        if path.suffix.lower() in TEXT_SUFFIXES:
            for number, line in enumerate(path.read_text(errors="replace").splitlines(), 1):
                if number == 1 and line.startswith("#!"):
                    continue  # Generic interpreter directive, not a source-machine path.
                for kind, pattern in PRIVATE.items():
                    if pattern.search(line):
                        failures.append(dict(file=relative, line=number, kind=kind))
        elif path.suffix.lower() == ".pdf":
            import fitz
            with fitz.open(path) as document:
                for number, page in enumerate(document, 1):
                    for kind, pattern in PRIVATE.items():
                        if pattern.search(page.get_text()):
                            failures.append(dict(file=relative, pdf_page=number, kind=kind))
    if failures:
        raise ValueError("Publication privacy screen failed: " + json.dumps(failures, ensure_ascii=False))


def run_release_command(script):
    result = subprocess.run([sys.executable, str(EDITION / "scripts" / script)],
        cwd=WORK, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise ValueError(script + " failed; inspect its retained report before packaging.")


def write_policy():
    text = """# Final package contents and checkpoint account

The two language ZIPs contain twelve unique final PDF editions and their standalone
TeX sources. The guide PDF and guide TeX are repeated in both language packages.
README.md is repeated in all three packages. The records ZIP uses edition-relative
paths at its root; extract it into a directory named edition to use the supplied
build commands. FINAL_FILE_MANIFEST.tsv maps each final package member back to
that edition-relative source path and gives its byte count and SHA-256.

All 260 checked page sources, cumulative decisions, full-page review records,
full-page PDF review images (including historical versions), guide paragraphs,
translations, intermediate sources, authored scripts, sanitized logs and other
documentary outputs are retained. The development directory preserves documentary
source and diagnostic history; the current standalone books are named in README.

Earlier development PDFs are superseded by the current reviewed PDFs of the same
work. Toolchain and margin-diagnostic PDFs are omitted as diagnostic artifacts;
their source, sanitized logs and resulting repair records remain. Regenerable TeX
auxiliaries, engine-format files, Python bytecode and runtime locks are omitted.
Source-scan crops remain reproducible from the supplied scans and are omitted;
the original input archives and scans are not copied into the release.

CHECKPOINT_MEMBER_ACCOUNT.tsv contains one row for every file member of every
saved numbered checkpoint, with the exact old bytes and SHA-256. Each row states
retained, superseded, or omitted; retained and superseded rows name the final ZIP
member and its SHA-256. Omission rows give a concrete reason. The companion summary
identifies every immutable checkpoint and totals its dispositions. No checkpoint
ZIP is nested in a final package.

The account and final manifest are created after the last numbered checkpoint.
The manifest lists every final member except its own row: its complete bytes are
contained in the records ZIP, whose digest is recorded in the release receipt.
The packaging script reopens each ZIP, verifies its member list and every member's
SHA-256, checks for CRC errors, and checks that the source files remained unchanged
while packaging. It names the three final ZIPs only after these checks pass.

The final PDF paths in build records correspond to the edition_source column of
FINAL_FILE_MANIFEST.tsv. Their actual delivered locations are the final_package
and member columns; copying a delivered PDF to its recorded build path restores
that exact layout for review tooling without recompilation.
"""
    (EDITION / POLICY).write_text(text)


def build_zip(path, entries):
    with ZipFile(path, "x", compression=ZIP_DEFLATED, compresslevel=6, allowZip64=True) as archive:
        for row in entries:
            info = ZipInfo(row["member"], date_time=(2026, 11, 14, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o644 << 16
            with archive.open(info, "w", force_zip64=True) as target, row["path"].open("rb") as source:
                shutil.copyfileobj(source, target, 1024 * 1024)
    expected = {row["member"]: row for row in entries}
    with ZipFile(path) as archive:
        if set(archive.namelist()) != set(expected) or len(archive.namelist()) != len(expected):
            raise ValueError("ZIP member list differs: " + path.name)
        for info in archive.infolist():
            row = expected[info.filename]
            if info.file_size != row["bytes"]:
                raise ValueError("ZIP member byte count differs: " + info.filename)
            with archive.open(info) as source:
                if sha_stream(source) != row["sha256"]:
                    raise ValueError("ZIP member SHA-256 differs: " + info.filename)
        if archive.testzip() is not None:
            raise ValueError("ZIP CRC verification failed: " + path.name)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--plan", action="store_true")
    action.add_argument("--build", action="store_true")
    args = parser.parse_args()
    catalog = checkpoint_inventory()
    selected, omitted, entries = collect(include_generated=False)
    if not args.build:
        accounts, totals = checkpoint_account(catalog, selected, omitted, hashes=False)
        print(json.dumps(dict(mode="read-only plan", checkpoints=len(catalog),
            historical_members=len(accounts), included_sources=len(selected),
            omitted_current_files=len(omitted), package_members=dict(Counter(row["package"] for row in entries)),
            package_source_bytes={p: sum(row["path"].stat().st_size for row in entries if row["package"] == p) for p in PACKAGES},
            final_manifest_created=False), indent=2))
        return
    OUTPUT.mkdir(exist_ok=True)
    for filename in PACKAGES.values():
        if (OUTPUT / filename).exists() or (OUTPUT / (filename + ".partial")).exists():
            raise ValueError("Refusing to overwrite an existing release file: " + filename)
    run_release_command("audit_release.py")
    audit = json.loads((EDITION / "records/RELEASE_AUDIT.json").read_text())
    if audit.get("status") != "PASS":
        raise ValueError("Every release gate must pass before packaging.")
    run_release_command("generate_readme.py")
    selected, omitted, entries = collect(include_generated=False)
    for relative, item in selected.items():
        item["sha256"] = sha(item["path"])
    accounts, totals = checkpoint_account(catalog, selected, omitted, hashes=True)
    fields = ("checkpoint_number", "checkpoint", "member", "bytes", "sha256", "disposition",
        "final_package", "final_member", "final_sha256", "successor_source", "reason")
    write_tsv(EDITION / ACCOUNT, fields, accounts)
    (EDITION / SUMMARY).write_text(json.dumps(dict(generated_utc=datetime.now(timezone.utc).isoformat(),
        checkpoint_count=len(totals), historical_file_members=len(accounts),
        disposition_counts=dict(Counter(row["disposition"] for row in accounts)),
        checkpoints=totals), ensure_ascii=False, indent=2) + "\n")
    write_policy()
    # Remove an earlier uncheckpointed manifest from the source set until rewritten.
    selected, omitted, entries = collect()
    entries = [row for row in entries if row["edition_source"] != MANIFEST]
    selected.pop(MANIFEST, None)
    privacy_screen(selected)
    for relative, item in selected.items():
        item["sha256"] = sha(item["path"])
        item["bytes"] = item["path"].stat().st_size
    for row in entries:
        row.update({key: selected[row["edition_source"]][key] for key in ("bytes", "sha256")})
    manifest_fields = ("package", "member", "edition_source", "bytes", "sha256")
    manifest_rows = [{key: (PACKAGES[row[key]] if key == "package" else row[key]) for key in manifest_fields} for row in entries]
    final_targets = {(row["package"], row["member"]): row for row in manifest_rows}
    for row in accounts:
        if not re.fullmatch(r"[0-9a-f]{64}", row["sha256"]):
            raise ValueError("A checkpoint member lacks its exact SHA-256.")
        if row["disposition"] != "omitted":
            target = final_targets.get((row["final_package"], row["final_member"]))
            if target is None or target["sha256"] != row["final_sha256"]:
                raise ValueError("A checkpoint successor differs from the final manifest: " + row["member"])
    write_tsv(EDITION / MANIFEST, manifest_fields, manifest_rows)
    manifest_path = EDITION / MANIFEST
    entries.append(dict(package="RECORDS", member=MANIFEST, edition_source=MANIFEST,
        bytes=manifest_path.stat().st_size, sha256=sha(manifest_path), path=manifest_path))
    entries.sort(key=lambda row: (row["package"], row["member"]))
    snapshot = {row["edition_source"]: (row["path"], row["sha256"]) for row in entries}
    pdf_entries = [row for row in entries if row["member"].endswith(".pdf")]
    if len(pdf_entries) != 13 or {Path(row["member"]).stem for row in pdf_entries} != set(STEMS):
        raise ValueError("The release must contain exactly twelve named PDF editions, with only the guide repeated.")
    receipts = []
    for package, filename in PACKAGES.items():
        members = [row for row in entries if row["package"] == package]
        partial = OUTPUT / (filename + ".partial")
        build_zip(partial, members)
        receipts.append(dict(filename=filename, bytes=partial.stat().st_size, sha256=sha(partial),
            members=len(members), verified=True))
    changed = [relative for relative, (path, digest) in snapshot.items() if sha(path) != digest]
    if changed:
        raise ValueError("Sources changed while packaging; review the partial files before retrying: " + ", ".join(changed))
    for receipt in receipts:
        (OUTPUT / (receipt["filename"] + ".partial")).rename(OUTPUT / receipt["filename"])
    result = dict(status="VERIFIED", generated_utc=datetime.now(timezone.utc).isoformat(),
        unique_pdf_editions=len(STEMS), physical_pdf_members=len(pdf_entries),
        checked_pages=260, checkpoints_accounted=len(catalog), checkpoint_file_members=len(accounts),
        final_manifest_sha256=sha(manifest_path), packages=receipts)
    (OUTPUT / "RELEASE_RECEIPT.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
