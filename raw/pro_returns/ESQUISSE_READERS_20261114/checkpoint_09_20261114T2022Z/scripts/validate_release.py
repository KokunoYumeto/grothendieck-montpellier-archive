#!/usr/bin/env python3
"""Verify the complete edition before final packaging.

This gate checks existing image-review declarations and actual visual-review
records. It never creates an inspection declaration or marks a PDF as viewed.
All documentary paths written by this script are edition-relative.
"""
from __future__ import annotations

import collections
import csv
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from zipfile import ZipFile

import fitz

from edition_core import clean_latex, macros, math_payloads, math_spans, replace_ranges, resolve_variants
from build_edition import FRENCH_RIGHTS, check_master_forms, input_snapshot
from release_bundle import eligible

ROOT = Path(__file__).resolve().parents[1]
COPY1 = [f"esq_119_{n:03d}" for n in range(2, 60)]
COPY2 = [f"esq119_119_{n:03d}" for n in range(78, 136)]
ALL_PAGES = COPY1 + COPY2
DOCUMENTS = {
    "ESQUISSE_FR_diplomatique": ("FR", ALL_PAGES),
    "ESQUISSE_FR_corrige_apparat": ("FR", COPY1),
    "ESQUISSE_FR_texte_de_lecture": ("FR", COPY1),
    "ESQUISSE_EN_corrected_translator_notes": ("EN", COPY1),
    "ESQUISSE_EN_reading": ("EN", COPY1),
    "ESQUISSE_FR_master_annotated": ("FR", COPY1),
    "ESQUISSE_EN_master_annotated": ("EN", COPY1),
    "ESQUISSE_GUIDE": ("GUIDE", []),
}
ENGLISH_RIGHTS = "The rights in the original work belong to its author or the author's representatives or heirs. Where we hold rights, in the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the public domain under CC0 1.0. This edition is published for educational, non-profit purposes, and we claim no rights we do not hold. If you hold rights in this work and object to its publication here, please open a GitHub issue and we will take it down."
CREDIT = "AI-transcribed by Claude Opus 5.5 (Anthropic, effort high, Message Batches API); checked against the scans, and this edition built, by GPT-6 Astra (OpenAI, ChatGPT Pro mode); prompts and records by Claude (Anthropic)"
TRANSLATION_CREDIT = "AI-translated by GPT-6 Astra (OpenAI, ChatGPT Pro mode)"
REQUIRED = [
    "README.md", "CHECK_DECISIONS.tsv", "COLLATION.tsv", "DIFFERENCES_OUTCOMES.tsv",
    "CHANGES.tsv", "APPARATUS_COUNTS.md", "CLEANUP_LOG.tsv", "TYPESETTING_FIXES.tsv",
    "TYPESETTING_REPORT.md", "SOURCE_COVERAGE.tsv", "TRANSLATION_COVERAGE.tsv",
    "NOTE_LINKS.json", "PDF_CHECKS.json", "FINAL_PDF_AUDIT.json", "VISUAL_QA.tsv",
    "MASTER_FORM_EQUIVALENCE.json", "BUILD_INPUTS.json", "RELEASE_STATUS.json",
    "records/CHECKPOINT_RECONCILIATION.tsv", "records/CHECKPOINT_RECONCILIATION.md",
    "records/INDEPENDENT_TEXT_REVIEW.tsv", "records/EDITORIAL_ADJUDICATIONS.tsv",
]
TEXT_SUFFIXES = {".py", ".tex", ".tsv", ".json", ".jsonl", ".md", ".txt", ".log"}
LOCAL_PATH = re.compile(r"/(?:workspace|home|mnt|tmp|usr|opt|var)/[^\s<>\"\)\}]+")
EMAIL = re.compile(r"(?<![\w@])[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9](?:[A-Za-z0-9.-]*[A-Za-z0-9])?\.[A-Za-z]{2,}")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(name, default=None):
    path = ROOT / name
    return json.loads(path.read_text()) if path.exists() else default


def read_tsv(name):
    path = ROOT / name
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def main():
    checks = []

    def check(name, passed, detail=None):
        checks.append({"check": name, "passed": bool(passed), "detail": detail})

    missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
    check("Required records exist", not missing, missing)
    checked = {p.stem for p in (ROOT / "checked_pages").glob("*.tex")}
    translated = {p.stem for p in (ROOT / "translated_pages").glob("*.tex")}
    check("All116 checked pages", checked == set(ALL_PAGES), {"present": len(checked), "missing": sorted(set(ALL_PAGES)-checked)})
    check("All58 translated pages", translated == set(COPY1), {"present": len(translated), "missing": sorted(set(COPY1)-translated)})

    page_map = read_tsv("records/PAGE_MAP.tsv")
    page_map_failures = []
    for row in page_map:
        key = row.get("key", "")
        try:
            site = int(key.rsplit("_", 1)[1])
            first_site = 2 if key in COPY1 else 78 if key in COPY2 else None
            expected_ts = "" if site == first_site else str(site - first_site)
            expected_url = "https://grothendieck.umontpellier.fr/web/viewer.html?file=../119.pdf#page=" + str(site + 1)
            valid = (first_site is not None and row.get("cote") == "119" and row.get("site") == str(site)
                     and row.get("pdf_page") == str(site + 1) and row.get("ts_page") == expected_ts
                     and row.get("viewer") == expected_url)
        except (ValueError, TypeError):
            valid = False
        if not valid:
            page_map_failures.append(key)
    check("Exact scan-page and viewer-URL mapping", [r.get("key") for r in page_map] == ALL_PAGES
          and not page_map_failures, {"pages": len(page_map), "invalid_keys": page_map_failures})

    replay = subprocess.run([sys.executable, str(ROOT / "scripts/audit_validate.py"), "--complete"], capture_output=True, text=True)
    audit = read_json("records/AUDIT_PROGRESS.json", {})
    check("Complete scan-decision replay and collation", replay.returncode == 0 and audit.get("status") == "complete", {
        key: audit.get(key) for key in ["status", "checked_pages", "difference_outcomes", "collated_page_pairs", "errors"]
    })
    source_integrity = read_json("records/SOURCE_INTEGRITY.json", {})
    integrity_failures = []
    input_counts = {}
    for archive, directory in [("ESQUISSE_TEXT.zip", "source"), ("ESQUISSE_SCANS.zip", "images")]:
        records = source_integrity.get(archive, [])
        base = ROOT.parent / directory
        manifest_path = base / "MANIFEST.tsv"
        if not manifest_path.exists():
            integrity_failures.append(archive + "!/MANIFEST.tsv")
            continue
        with manifest_path.open(newline="", encoding="utf-8") as stream:
            manifest = list(csv.DictReader(stream, delimiter="\t"))
        expected = {r["path"]: r for r in manifest}
        input_counts[archive] = {"manifest_entries": len(manifest), "integrity_entries": len(records)}
        if (len(expected) != len(manifest) or len(records) != len(manifest)
                or {r["path"] for r in records} != set(expected)):
            integrity_failures.append(archive + "!/manifest-coverage")
        for record in records:
            path = base / record["path"]
            original = expected.get(record["path"], {})
            if (record["expected_bytes"] != int(original.get("bytes", -1))
                    or record["expected_sha256"] != original.get("sha256") or not path.is_file()
                    or path.stat().st_size != record["expected_bytes"] or digest(path) != record["expected_sha256"]):
                integrity_failures.append(archive + "!/" + record["path"])
    check("Original inputs remain unchanged", set(source_integrity) == {"ESQUISSE_TEXT.zip", "ESQUISSE_SCANS.zip"}
          and not integrity_failures, {"counts": input_counts, "failures": integrity_failures})

    release = read_json("RELEASE_STATUS.json", {})
    build = read_json("BUILD_INPUTS.json", {})
    check("Final source status", release.get("final") is True and build.get("status") == "final", {"release": release, "generation": build.get("status")})
    current_inputs = input_snapshot(ROOT)
    recorded_inputs = build.get("input_sha256", {})
    changed = [name for name in sorted(set(current_inputs) | set(recorded_inputs)) if current_inputs.get(name) != recorded_inputs.get(name)]
    check("Generated documents use current inputs", not changed, changed)

    source_rows = read_tsv("SOURCE_COVERAGE.tsv")
    source_failures = []
    for row in source_rows:
        key = row["key"]
        path = ROOT / "checked_pages" / (key + ".tex")
        annotated = ROOT / "annotated_pages" / (key + ".tex")
        valid = path.is_file() and annotated.is_file()
        if valid:
            clean, events = clean_latex(path.read_text())
            valid = (digest(path) == row["checked_sha256"] and digest(annotated) == row["annotated_sha256"]
                     and not events and row["pending_cleanup"] == "0" and row["diplomatic_recovery_equal"] == "true"
                     and resolve_variants(annotated.read_text(), False) == clean)
        if not valid:
            source_failures.append(key)
    check("Exact diplomatic recovery and completed cleanup", {r["key"] for r in source_rows} == set(ALL_PAGES) and not source_failures, source_failures)

    index = read_json("translated_pages/TRANSLATION_INDEX.json", [])
    index_failures = []
    for row in index:
        key = row.get("key", "")
        if (row.get("source") != "checked_pages/" + key + ".tex"
                or row.get("translation") != "translated_pages/" + key + ".tex"):
            index_failures.append(key + ":noncanonical-provenance")
            continue
        for name, hash_key in [(row["source"], "source_sha256"), (row["translation"], "translation_sha256")]:
            path = ROOT / name
            if not path.is_file() or digest(path) != row[hash_key]:
                index_failures.append(name)
        french_path, english_path = ROOT / row["source"], ROOT / row["translation"]
        if french_path.is_file() and english_path.is_file():
            raw_fr, raw_en = french_path.read_text(), english_path.read_text()
            expected_fields = {
                "math_fragments": [span[2] for span in math_spans(raw_fr)],
                "diagram_fragments": [raw_fr[m.start:m.end] for m in macros(raw_fr, {"diagram"})],
                "translator_note_ids": [m.arguments[0] for m in macros(raw_en, {"tnote"})],
                "variant_ids": [m.arguments[3] for m in macros(raw_en, {"var"})],
                "french_source_apparatus_ids": [m.arguments[0] for m in macros(raw_en, {"frapparatus"})],
            }
            for field, expected in expected_fields.items():
                if row.get(field) != expected:
                    index_failures.append(key + ":" + field)
    check("Translation provenance and index contents replay exactly", len(index) == 58
          and {r["key"] for r in index} == set(COPY1) and not index_failures, index_failures)
    math_failures = []
    doubt_failures = []
    math_total = 0
    for key in COPY1:
        french = ROOT / "annotated_pages" / (key + ".tex")
        english = ROOT / "translated_pages" / (key + ".tex")
        if not french.exists() or not english.exists():
            math_failures.append(key)
            continue
        fr = resolve_variants(french.read_text(), True)
        en = resolve_variants(english.read_text(), True)
        for name in ["tnote", "frapparatus", "copytwo"]:
            en = replace_ranges(en, [(m.start, m.end, "") for m in macros(en, {name})])
        first, second = math_payloads(fr), math_payloads(en)
        math_total += len(first)
        if first != second:
            math_failures.append(key)
        fr_doubts = collections.Counter(m.name for m in macros(fr, {"unsure", "illegible"}))
        en_doubts = collections.Counter(m.name for m in macros(en, {"unsure", "illegible"}))
        if fr_doubts != en_doubts:
            doubt_failures.append({"key": key, "French": dict(fr_doubts), "English": dict(en_doubts)})
    check("English mathematics equals corrected French character for character", not math_failures, {"fragments_including_diagrams": math_total, "mismatched_pages": math_failures})
    check("English retains every corrected-French doubt mark", not doubt_failures, doubt_failures)
    coverage = read_tsv("TRANSLATION_COVERAGE.tsv")
    check("Generated English covers all58 pages with exact mathematics", {r["key"] for r in coverage} == set(COPY1) and all(r["math_equal"] == "true" for r in coverage), {"pages": len(coverage)})

    variants = read_json("VARIANTS.json", [])
    changes = read_tsv("CHANGES.tsv")
    variant_ids = [v["id"] for v in variants]
    check("One change record per French variant", len(set(variant_ids)) == len(variant_ids) and collections.Counter(variant_ids) == collections.Counter(r["variant_id"] for r in changes)
          and all(r.get("kind") and r.get("reason") and r.get("source_id") for r in changes), {"variants": len(variants), "changes": len(changes)})
    english_variants = []
    english_source_notes = []
    empty_variants = []
    misplaced_variants = []
    approved_variants = {v["id"]: v for v in read_json("editorial_variants.json", [])}
    for path in (ROOT / "translated_pages").glob("*.tex"):
        for mark in macros(path.read_text(), {"var", "frapparatus"}):
            identity = mark.arguments[3] if mark.name == "var" else mark.arguments[0]
            approved = approved_variants.get(identity)
            if (not approved or approved.get("key") != path.stem
                    or approved.get("english_variant_needed") is not (mark.name == "var")):
                misplaced_variants.append({"id": identity, "key": path.stem, "macro": mark.name})
            if mark.name == "var":
                english_variants.append(mark.arguments[3])
                if mark.arguments[0] == mark.arguments[1]:
                    empty_variants.append(mark.arguments[3])
            else:
                english_source_notes.append(mark.arguments[0])
    check("Shared French-English variant identities without empty English variants", not empty_variants
          and not misplaced_variants and set(approved_variants) == set(variant_ids)
          and not (set(english_variants) & set(english_source_notes))
          and collections.Counter(english_variants + english_source_notes) == collections.Counter(variant_ids), {
              "English_wording_variants": len(english_variants), "French_source_apparatus_notes": len(english_source_notes),
              "empty_variants": empty_variants, "wrong_page_or_variant_class": misplaced_variants})

    guide_files = sorted(p for p in (ROOT / "guide_fragments").glob("*.tex") if p.name != "00_preface.tex")
    headings = sum(len(re.findall(r"\\subsection\*\{", p.read_text())) for p in guide_files)
    guide_preface = ROOT / "guide_fragments/00_preface.tex"
    preface_ready = (guide_preface.exists() and bool(guide_preface.read_text().strip())
                     and not re.search(r"working (?:preface|collation)|incomplete|not yet|so far", guide_preface.read_text(), re.I))
    expected_guide_files = {"00_sommaire.tex"} | {f"{n:02d}_section{n}.tex" for n in range(1, 11)} | {f"{n+10:02d}_note{n}.tex" for n in range(1, 8)}
    check("Guide has all18 commentary units and a completed collation preface", {p.name for p in guide_files} == expected_guide_files
          and headings == 18 and preface_ready, {"units": len(guide_files), "headings": headings, "preface_ready": preface_ready})
    reviewed_hashes = collections.defaultdict(set)
    malformed_reviews = []
    for row in read_tsv("records/INDEPENDENT_TEXT_REVIEW.tsv"):
        names, hashes = row.get("reviewed_files", "").split("; "), row.get("sha256", "").split("; ")
        if len(names) != len(hashes) or not row.get("finding") or not row.get("action"):
            malformed_reviews.append(row.get("review_id"))
            continue
        for name, checksum in zip(names, hashes):
            reviewed_hashes[name].add(checksum)
    prose_paths = [ROOT / "translated_pages" / (key + ".tex") for key in COPY1] + guide_files + [guide_preface]
    unreviewed_prose = [p.relative_to(ROOT).as_posix() for p in prose_paths
                       if not p.exists() or digest(p) not in reviewed_hashes[p.relative_to(ROOT).as_posix()]]
    check("Current English and guide prose independently reviewed", len(prose_paths) == 77
          and not malformed_reviews and not unreviewed_prose,
          {"files": len(prose_paths), "unreviewed_current_hashes": unreviewed_prose, "malformed_records": malformed_reviews})
    note_links = read_json("NOTE_LINKS.json", {})
    check("All source endnote calls resolved", set(note_links) == {"FR", "EN"} and all(not item.get("unresolved_calls") for item in note_links.values()), {k: v.get("unresolved_calls") for k, v in note_links.items()})

    generated = [directory + "/" + name + ".tex" for name, (directory, _) in DOCUMENTS.items()]
    masters_ok = False
    if all((ROOT / name).exists() for name in generated):
        try:
            check_master_forms(ROOT, generated)
            masters_ok = True
        except (ValueError, KeyError):
            masters_ok = False
    check("All language forms share their annotated master body", masters_ok, read_json("MASTER_FORM_EQUIVALENCE.json", {}))

    probe = read_json("records/RENDERING_PROBE.json", {})
    check("Marginal and grouped-note rendering probe passes", probe.get("passed") is True and not probe.get("errors")
          and not probe.get("missing_characters"), {k: probe.get(k) for k in ["passed", "errors", "missing_characters", "note_text_occurrences", "printed_block_labels"]})

    pdf_audits = read_json("FINAL_PDF_AUDIT.json", {})
    pdf_records = {}
    for name, (directory, expected_keys) in DOCUMENTS.items():
        tex = ROOT / directory / (name + ".tex")
        pdf = tex.with_suffix(".pdf")
        r = pdf_audits.get(name, {})
        problems = []
        if not tex.exists() or not pdf.exists():
            problems.append("standalone source or PDF absent")
        else:
            source = tex.read_text()
            if r.get("source_sha256") != digest(tex) or r.get("pdf_sha256") != digest(pdf):
                problems.append("PDF audit hashes absent or stale")
            if not r.get("compiled_source_matches") or not r.get("compiled_pdf_matches"):
                problems.append("successful compilation hashes do not match")
            if r.get("source_keys") != expected_keys:
                problems.append("source-page projection differs from required ordered pages")
            if not source.startswith("% EDITION STATUS: final;"):
                problems.append("source retains provisional status")
            if re.search(r"\\(?:input|include|includegraphics|includepdf)\s*(?:\[|\{)", source):
                problems.append("source depends on an external content file")
            if re.search(r"\\[hv]fuzz\s*(?:=|\\|[0-9])", source):
                problems.append("fuzz override hides diagnostics")
            if ENGLISH_RIGHTS not in source or CREDIT not in source:
                problems.append("required exact English rights or credit missing")
            if directory == "FR" and FRENCH_RIGHTS not in source:
                problems.append("required exact French rights missing")
            if directory == "EN" and TRANSLATION_CREDIT not in source:
                problems.append("translation credit missing")
            for field in ["upstream_input_mismatches", "errors", "missing_characters", "ink_outside_sheet", "ink_outside_type_area",
                          "link_count_mismatches", "apparatus_entry_mismatches", "uninspected_required_pages"]:
                if field not in r or r[field]:
                    problems.append(field)
            if any(float(box["points"]) > 2 for box in r.get("overfull", [])):
                problems.append("overfull box exceeds2pt")
            if r.get("source_apparatus_entries") != r.get("executed_apparatus_entries") or r.get("source_apparatus_entries") != r.get("printed_apparatus_entries"):
                problems.append("apparatus projection/execution/printed counts differ")
            if any(not item.get("same_physical_page") for item in r.get("author_footnote_placements", [])):
                problems.append("starred source note split from its call")
            endnotes = r.get("endnote_link_audit", {})
            required_definitions = 14 if name.endswith("diplomatique") else 7 if expected_keys else 0
            if endnotes.get("problems") != 0 or endnotes.get("definitions") != required_definitions:
                problems.append("endnote definition or two-way-link audit incomplete")
            required = set(r.get("required_visual_pages", []))
            seen = set(r.get("visually_inspected_pages", []))
            if len(required) < min(40, r.get("pdf_pages", 0)) or not required <= seen:
                problems.append("required visual sample incomplete")
            if expected_keys and not r.get("author_footnote_placements"):
                problems.append("starred source notes were not checked")
            margins = r.get("marginal_note_audit", {})
            if "problems" not in margins or margins["problems"]:
                problems.append("marginal-note line/height/printed-label audit incomplete")
            for margin in r.get("marginal_note_placements", []):
                if margin.get("placement") == "margin":
                    if margin.get("lines", 99) > 3 or margin.get("within_three_line_height") is not True:
                        problems.append("a margin note exceeds the three-line limit")
                elif margin.get("placement") == "block":
                    if margin.get("labelled_block") is not True:
                        problems.append("a long marginal note lacks its block label")
                else:
                    problems.append("unknown marginal-note placement")
        check("PDF " + name, not problems, problems)
        pdf_records[name] = {k: r.get(k) for k in ["source_sha256", "pdf_sha256", "source_pages", "pdf_pages", "expected_link_count", "pdf_external_link_annotations", "source_apparatus_entries", "required_visual_pages", "visually_inspected_pages"]}

    privacy_findings = []
    scanned_files = 0
    for path in sorted(p for p in ROOT.rglob("*") if eligible(p)):
        relative = path.relative_to(ROOT).as_posix()
        if relative == "records/RELEASE_VALIDATION.json":
            continue
        if path.suffix in TEXT_SUFFIXES:
            text = path.read_text(errors="replace")
        elif path.suffix == ".pdf":
            with fitz.open(path) as document:
                text = "\n".join(page.get_text() for page in document) + json.dumps(document.metadata)
        else:
            continue
        scanned_files += 1
        for pattern, kind in [(LOCAL_PATH, "local path"), (EMAIL, "email address")]:
            for match in pattern.finditer(text):
                # A portable interpreter directive is code, not a copied
                # execution-environment path or documentary source reference.
                if path.suffix == ".py" and match.group() == "/".join(["", "usr", "bin", "env"]) and text.startswith("#!") and match.start() == 2:
                    continue
                privacy_findings.append({"path": relative, "line": text[:match.start()].count("\n") + 1, "kind": kind})
    check("No private local paths or email addresses in outputs", not privacy_findings, {"findings": privacy_findings})

    reconciliation = read_tsv("records/CHECKPOINT_RECONCILIATION.tsv")
    acceptable = {"unchanged", "superseded", "omitted supplied duplicate", "preserved with explicit archival name"}
    unresolved = [r for r in reconciliation if not r.get("reason") or r.get("status") not in acceptable]
    checkpoint_rows = read_tsv("records/CHECKPOINTS.tsv")
    expected_members = {}
    reconciliation_problems = []
    for checkpoint in checkpoint_rows:
        archive_name = checkpoint["checkpoint"]
        number = int(Path(archive_name).stem.rsplit("_", 1)[1])
        manifest_name = f"records/checkpoint_manifests/checkpoint_{number:02d}.tsv"
        manifest_path = ROOT / manifest_name
        if not manifest_path.exists():
            reconciliation_problems.append(archive_name + "!/missing-manifest")
            continue
        manifest = read_tsv(manifest_name)
        for item in manifest:
            pair = (archive_name, item["path"])
            if pair in expected_members:
                reconciliation_problems.append(archive_name + "!/duplicate-manifest-member")
            expected_members[pair] = item["sha256"]
        expected_members[(archive_name, "CHECKPOINT_CONTENTS.tsv")] = digest(manifest_path)
        archived = ROOT.parent.parent / "output" / archive_name
        if archived.exists():
            with ZipFile(archived) as bundle:
                actual = {name: hashlib.sha256(bundle.read(name)).hexdigest()
                          for name in bundle.namelist() if not name.endswith("/")}
            expected_archive = {name: checksum for (checkpoint_name, name), checksum in expected_members.items()
                                if checkpoint_name == archive_name}
            if actual != expected_archive:
                reconciliation_problems.append(archive_name + "!/archive-manifest-mismatch")
    actual_pairs = [(r.get("checkpoint"), r.get("path")) for r in reconciliation]
    if len(set(actual_pairs)) != len(actual_pairs) or set(actual_pairs) != set(expected_members):
        reconciliation_problems.append("reconciliation-member-coverage")
    for row in reconciliation:
        pair = (row.get("checkpoint"), row.get("path"))
        if row.get("checkpoint_sha256") != expected_members.get(pair):
            reconciliation_problems.append("!/".join(pair))
        target = row.get("final_path", "")
        if row.get("status") != "omitted supplied duplicate":
            relative = Path(target)
            if relative.is_absolute() or ".." in relative.parts or not (ROOT / relative).is_file():
                reconciliation_problems.append(target)
            # This report is regenerated by the gate itself; its current bytes
            # are reconciled between the two deterministic packaging passes.
            elif target != "records/RELEASE_VALIDATION.json" and digest(ROOT / relative) != row.get("final_sha256"):
                reconciliation_problems.append(target)
        diff = row.get("exact_passage_diff", "")
        if diff and (Path(diff).is_absolute() or ".." in Path(diff).parts or not (ROOT / diff).is_file()):
            reconciliation_problems.append(diff)
    check("Every checkpoint file accounted for", bool(checkpoint_rows) and bool(reconciliation) and not unresolved
          and not reconciliation_problems, {"members": len(reconciliation), "expected_members": len(expected_members),
          "unresolved": [{"checkpoint": r.get("checkpoint"), "path": r.get("path"), "status": r.get("status")} for r in unresolved],
          "integrity_problems": sorted(set(reconciliation_problems))})

    report = {
        "passed": all(c["passed"] for c in checks),
        "edition_date": release.get("edition_date", "2026-11-14"),
        "checks": checks,
        "documents": pdf_records,
        "source_counts": {"checked": len(checked), "translated": len(translated), "guide_units": len(guide_files)},
        "scope": "Machine verification of complete recorded evidence, exact text/mathematics and current PDF measurements; visual inspection is supplied only by the separate reviewer records.",
    }
    (ROOT / "records/RELEASE_VALIDATION.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    failed = [c["check"] for c in checks if not c["passed"]]
    print(json.dumps({"passed": report["passed"], "checks": len(checks), "failed_checks": failed}))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
