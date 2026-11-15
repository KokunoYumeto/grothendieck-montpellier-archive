"""Validate current structural, ink, and provenance-backed visual QA evidence.

Direct openings of current-PDF images and observations inherited through exact
raster equality are separate evidence classes. Rendering and selection do not
constitute image openings. Historical observations retain their original hashes.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path, PurePath
import re

import fitz
from PIL import Image

PROJECT = Path(__file__).resolve().parents[1]
STEMS = ["PS_EN_diplomatic", "PS_EN_corrected_apparatus", "PS_EN_reading",
         "PS_EN_master_annotated", "PS_GUIDE"]
INHERITED_METHOD = "raster identity with an actually opened image"
DIRECT_METHOD = "direct opening of an image rendered from the current PDF"
ALLOWED_INK = {"permitted single-letter overhang", "allowed page-number/footer region",
               "raster quantization only"}


class EvidenceError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise EvidenceError(message)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def valid_sha(value):
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


def rows_from(data):
    return data if isinstance(data, list) else data.get("entries", [])


def geometry(page):
    return {"rect_pt": list(page.rect), "mediabox_pt": list(page.mediabox),
            "cropbox_pt": list(page.cropbox), "rotation": page.rotation}


def signature(width, height, samples):
    return {"width_px": width, "height_px": height, "colorspace": "RGB",
            "pixels_sha256": sha256(samples)}


def valid_signature(value):
    return (isinstance(value, dict) and isinstance(value.get("width_px"), int)
            and value["width_px"] > 0 and isinstance(value.get("height_px"), int)
            and value["height_px"] > 0 and value.get("colorspace") == "RGB"
            and valid_sha(value.get("pixels_sha256")))


def direct_observation(row):
    return (row.get("viewed") is True and isinstance(row.get("observation"), str)
            and bool(row["observation"].strip())
            and row.get("inspection_method") != INHERITED_METHOD
            and row.get("image_opened") is not False
            and row.get("direct_image_opened") is not False
            and row.get("status", "pass") in {"pass", "ok", "clean"})


class EvidenceValidator:
    def __init__(self, project, allow_omitted_historical_pdfs=False):
        self.project = project.resolve()
        self.files, self.json_cache, self.pdf_cache = {}, {}, {}
        self.png_cache, self.audit_cache = {}, {}
        self.allow_omitted_historical_pdfs = allow_omitted_historical_pdfs
        self.omissions = None
        self.historical_pdf_verification = {}

    def path(self, relative):
        require(isinstance(relative, str) and bool(relative), "Missing evidence path")
        require(not Path(relative).is_absolute(), "Evidence paths must be project-relative")
        path = (self.project / relative).resolve()
        require(path.is_relative_to(self.project), "Evidence path escapes the project")
        return path

    def bytes(self, relative, expected=None):
        data = self.path(relative).read_bytes()
        digest = sha256(data)
        if expected is not None:
            require(valid_sha(expected) and digest == expected, "Hash mismatch: " + relative)
        if relative in self.files:
            require(self.files[relative] == digest, "Evidence changed during gate: " + relative)
        self.files[relative] = digest
        return data

    def json(self, relative, expected=None):
        raw = self.bytes(relative, expected)
        if relative not in self.json_cache:
            self.json_cache[relative] = json.loads(raw)
        return self.json_cache[relative]

    def pdf(self, relative, expected=None):
        raw = self.bytes(relative, expected)
        if relative not in self.pdf_cache:
            self.pdf_cache[relative] = fitz.open(stream=raw, filetype="pdf")
        return self.pdf_cache[relative]

    def png(self, relative, expected):
        require(valid_sha(expected), "Missing PNG hash: " + str(relative))
        raw = self.bytes(relative, expected)
        cache_key = (relative, sha256(raw))
        if cache_key not in self.png_cache:
            with Image.open(self.path(relative)) as im:
                im.load()
                require(im.mode == "RGB", "Expected an RGB proof image: " + relative)
                self.png_cache[cache_key] = signature(im.width, im.height, im.tobytes())
        return self.png_cache[cache_key]

    def rendered_signature(self, pdf, page, scale):
        pix = pdf[page - 1].get_pixmap(matrix=fitz.Matrix(scale, scale),
                                     colorspace=fitz.csRGB, alpha=False)
        return signature(pix.width, pix.height, pix.samples)

    def final_omissions(self):
        if self.omissions is not None:
            return self.omissions
        raw = self.bytes("records/FINAL_OMISSIONS.tsv")
        reader = csv.DictReader(io.StringIO(raw.decode("utf-8-sig")), delimiter="\t")
        required = {"path", "bytes", "sha256", "replacement", "replacement_sha256", "reason"}
        require(set(reader.fieldnames or []) == required, "Unexpected final-omission manifest schema")
        rows = list(reader)
        require(len({row["path"] for row in rows}) == len(rows), "Duplicate final-omission path")
        finals = {"readers/" + stem + ".pdf" for stem in STEMS}
        result = {}
        for row in rows:
            path = self.path(row["path"])
            require(row["path"] not in finals and not row["path"].startswith("readers/")
                    and path.suffix.lower() == ".pdf" and int(row["bytes"]) > 0
                    and valid_sha(row["sha256"]) and bool(row["reason"].strip()),
                    "Omission is not an explicitly superseded intermediate PDF")
            require(row["replacement"] in finals and valid_sha(row["replacement_sha256"]),
                    "An omitted PDF lacks a published-reader replacement")
            self.bytes(row["replacement"], row["replacement_sha256"])
            if path.exists():
                raw_pdf = self.bytes(row["path"], row["sha256"])
                require(len(raw_pdf) == int(row["bytes"]), "Omitted PDF byte count disagrees with its exact hash row")
            else:
                require(self.allow_omitted_historical_pdfs,
                        "Workspace PDF is missing; explicit extracted-delivery mode is required: " + row["path"])
            result[row["path"]] = row
        actual_extra = {path.relative_to(self.project).as_posix() for path in self.project.rglob("*.pdf")
                        if path.relative_to(self.project).as_posix() not in finals}
        require(actual_extra <= set(result), "An intermediate PDF lacks explicit final supersession")
        self.omissions = result
        return result

    def omitted_old_pdf(self, old_path, old_hash, current_path, current_hash):
        require(self.allow_omitted_historical_pdfs,
                "Old PDF is absent and extracted-delivery omission mode was not requested")
        row = self.final_omissions().get(old_path)
        require(row is not None and row["sha256"] == old_hash and row["replacement"] == current_path
                and row["replacement_sha256"] == current_hash,
                "Absent old PDF is not explicitly superseded by the exact current PDF")
        return row

    def current_row(self, row, pdf_path, pdf_hash, page_count):
        require(row.get("pdf") == pdf_path and row.get("pdf_sha256") == pdf_hash,
                "Visual evidence identifies a different PDF")
        page = row.get("page")
        require(isinstance(page, int) and 1 <= page <= page_count, "Invalid visual-evidence page")
        require(row.get("viewed") is True and isinstance(row.get("observation"), str)
                and bool(row["observation"].strip()), "Missing actual observation")
        require(row.get("status", "pass") in {"pass", "ok", "clean"},
                "Current visual evidence records an unresolved issue")
        return self.png(row.get("image"), row.get("image_sha256"))

    def validate_direct(self, row, pdf_path, pdf_hash, pdf):
        pixels = self.current_row(row, pdf_path, pdf_hash, len(pdf))
        require(direct_observation(row), "Entry is not a direct current-image opening")
        scale = row.get("raster_scale", row.get("raster_dpi", 100.8) / 72)
        require(scale in (1.4, 2.0), "Unrecognized direct-review raster scale")
        require(pixels == self.rendered_signature(pdf, row["page"], scale),
                "Direct-review image does not render the claimed current PDF page")

    def equivalence_audit(self, provenance, current_pdf, current_hash):
        path = provenance.get("equivalence_audit")
        audit_hash = provenance.get("equivalence_audit_sha256")
        require(valid_sha(audit_hash), "Inherited evidence lacks equivalence-audit SHA-256")
        audit = self.json(path, audit_hash)
        cache_key = (path, audit_hash, current_hash)
        if cache_key in self.audit_cache:
            return self.audit_cache[cache_key]
        require(audit.get("audit_complete") is True and not audit.get("integrity_issues"),
                "Raster-equivalence audit is incomplete or has integrity issues")
        require(audit.get("new_pdf") == current_pdf and audit.get("new_pdf_sha256") == current_hash,
                "Raster-equivalence audit is stale for the current PDF")
        require(valid_sha(audit.get("old_pdf_sha256")), "Old PDF hash is missing")
        old_path = audit.get("old_pdf")
        old_present = self.path(old_path).exists()
        if old_present:
            old_pdf = self.pdf(old_path, audit["old_pdf_sha256"])
            old_count = len(old_pdf)
            self.historical_pdf_verification[old_path] = {"mode": "old PDF bytes and geometry verified in workspace",
                "old_pdf_sha256": audit["old_pdf_sha256"]}
        else:
            omitted = self.omitted_old_pdf(old_path, audit["old_pdf_sha256"], current_pdf, current_hash)
            old_pdf = None
            old_count = audit.get("old_page_count")
            self.historical_pdf_verification[old_path] = {"mode": "explicitly superseded PDF absent from extracted delivery; preserved old PNG and prior evidence verified against fresh current renders",
                "old_pdf_sha256": audit["old_pdf_sha256"], "omission_manifest": "records/FINAL_OMISSIONS.tsv",
                "omission_manifest_sha256": self.files["records/FINAL_OMISSIONS.tsv"], "replacement": omitted["replacement"]}
        new_pdf = self.pdf(current_pdf, current_hash)
        count = len(new_pdf)
        require(audit.get("page_count_identical") is True
                and audit.get("all_page_geometry_identical") is True
                and audit.get("all_pages_compared_144dpi") is True
                and audit.get("old_page_count") == audit.get("new_page_count") == old_count == count,
                "Raster audit lacks an equal-count, all-page geometry comparison")
        renderer = audit.get("renderer", {})
        require(renderer.get("dpi") == 144 and renderer.get("matrix_scale") == 2.0
                and renderer.get("original_image_scale") == 1.4
                and renderer.get("colorspace") == "RGB" and renderer.get("alpha") is False,
                "Unexpected raster-equivalence render parameters")
        records = audit.get("pages", [])
        require(len(records) == count and {x.get("page") for x in records} == set(range(1, count + 1)),
                "Raster audit omits or duplicates pages")
        indexed = {x["page"]: x for x in records}
        for number, entry in indexed.items():
            require((not old_present or entry.get("old_geometry") == geometry(old_pdf[number - 1]))
                    and entry.get("new_geometry") == geometry(new_pdf[number - 1])
                    and entry.get("geometry_identical") is True
                    and entry["old_geometry"] == entry["new_geometry"],
                    "Raster-audit geometry differs from its PDFs")
            require(valid_signature(entry.get("old_144dpi")) and valid_signature(entry.get("new_144dpi")),
                    "Raster audit lacks a valid 144-dpi signature")
            require(entry.get("pixels_identical_144dpi") == (entry["old_144dpi"] == entry["new_144dpi"]),
                    "Raster audit has an inconsistent equality result")
        self.audit_cache[cache_key] = (audit, indexed, old_present)
        return audit, indexed, old_present

    def validate_inherited(self, row, container, pdf_path, pdf_hash, pdf):
        pixels = self.current_row(row, pdf_path, pdf_hash, len(pdf))
        require(row.get("inspection_method") == INHERITED_METHOD
                and row.get("image_opened") is False and row.get("direct_image_opened") is False,
                "Inherited review must explicitly disclaim a current-image opening")
        require(isinstance(container, dict) and container.get("direct_current_image_openings_claimed") == 0,
                "Inherited evidence container claims direct openings")
        p = row.get("provenance", {})
        require(container.get("equivalence_audit") == p.get("equivalence_audit")
                and container.get("equivalence_audit_sha256") == p.get("equivalence_audit_sha256"),
                "Inherited row and container cite different audit provenance")
        audit, audit_pages, old_pdf_present = self.equivalence_audit(p, pdf_path, pdf_hash)
        number = row["page"]
        require(p.get("old_page") == number and number in audit.get("inherited_raster_identity_pages", []),
                "Inherited page is absent from its raster audit")
        require(p.get("old_pdf") == audit.get("old_pdf")
                and p.get("old_pdf_sha256") == audit.get("old_pdf_sha256"),
                "Inherited old-PDF provenance disagrees with its audit")
        entry = audit_pages[number]
        require(entry.get("pixels_identical_144dpi") is True
                and entry.get("pixels_identical_scale_1_4") is True
                and valid_signature(entry.get("old_scale_1_4"))
                and entry.get("old_scale_1_4") == entry.get("new_scale_1_4"),
                "Inherited page is not identical at both required raster scales")
        require(p.get("page_pixels_sha256_144dpi") == entry["new_144dpi"]["pixels_sha256"]
                and p.get("page_pixels_sha256_scale_1_4") == entry["new_scale_1_4"]["pixels_sha256"],
                "Inherited pixel hashes disagree with the audit")
        old_png, new_png = entry.get("retained_old_png", {}), entry.get("current_png", {})
        require(old_png.get("matches_old_pdf_scale_1_4") is True
                and new_png.get("matches_current_pdf_scale_1_4") is True,
                "Raster audit did not bind retained/current PNGs to their PDFs")
        require(old_png.get("image") == p.get("old_image")
                and old_png.get("image_sha256") == p.get("old_image_sha256"),
                "Old-image provenance disagrees with the audit")
        old_pixels = self.png(p.get("old_image"), p.get("old_image_sha256"))
        require(new_png.get("image") == row["image"] and new_png.get("image_sha256") == row["image_sha256"]
                and old_pixels == old_png.get("pixels") == entry["old_scale_1_4"]
                and pixels == new_png.get("pixels") == entry["new_scale_1_4"] == old_pixels,
                "Retained/current image bytes do not have the audited identical pixels")
        if not old_pdf_present:
            require(self.rendered_signature(pdf, number, 1.4) == old_pixels,
                    "Fresh current render does not equal the preserved actually-opened old PNG")
            require(self.rendered_signature(pdf, number, 2.0) == entry["new_144dpi"],
                    "Fresh 144-dpi current render disagrees with the preserved equivalence proof")
        original_hash = p.get("preserved_original_evidence_file_sha256")
        require(original_hash == p.get("source_evidence_file_sha256") and valid_sha(original_hash),
                "Original evidence snapshot hash is missing or inconsistent")
        original = self.json(p.get("preserved_original_evidence_file"), original_hash)
        old_rows = rows_from(original)
        index = p.get("source_entry_index")
        require(isinstance(index, int) and 0 <= index < len(old_rows), "Invalid original evidence entry index")
        prior = old_rows[index]
        prior_hash = prior.get("pdf_sha256") or (original.get("pdf_sha256") if isinstance(original, dict) else None)
        require(direct_observation(prior) and prior.get("page") == number
                and prior_hash == p["old_pdf_sha256"]
                and prior["observation"] == row.get("prior_actual_image_observation"),
                "Preserved source entry is not the claimed prior actual-image observation")
        verify = p.get("old_image_verification", {})
        recorded_hash = prior.get("image_sha256")
        require(verify.get("retained_image_sha256") == p["old_image_sha256"]
                and verify.get("retained_png_matches_old_pdf_scale_1_4") is True
                and verify.get("previously_recorded_image_sha256") == recorded_hash
                and verify.get("previously_recorded_hash_present") == (recorded_hash is not None),
                "Old-image integrity metadata disagrees with the original entry")
        if recorded_hash is not None:
            require(recorded_hash == p["old_image_sha256"]
                    and verify.get("previously_recorded_hash_matches") is True,
                    "Originally recorded image hash does not match the retained old image")
        else:
            require(verify.get("previously_recorded_hash_matches") is None,
                    "Missing original image hash was falsely described as checked")
        require(any(s.get("original_evidence_file") == p.get("source_evidence_file")
                    and s.get("original_evidence_file_sha256") == original_hash
                    and s.get("preserved_original") == p.get("preserved_original_evidence_file")
                    and s.get("normalized_archive") == p.get("normalized_historical_evidence_file")
                    for s in audit.get("evidence_sources", [])),
                "Original evidence is not registered in the raster audit")
        normalized = self.json(p.get("normalized_historical_evidence_file"))
        require(normalized.get("pdf") == p["old_pdf"] and normalized.get("pdf_sha256") == p["old_pdf_sha256"],
                "Normalized historical evidence identifies the wrong old PDF")
        require(any(n.get("page") == number and n.get("observation") == prior["observation"]
                    and n.get("image") == p["old_image"] and n.get("image_sha256") == p["old_image_sha256"]
                    and n.get("original_evidence_file_sha256") == original_hash
                    and n.get("preserved_original_evidence_file") == p["preserved_original_evidence_file"]
                    for n in normalized.get("entries", [])),
                "Normalized archive lacks the matching prior observation")

    def master_body(self, selection, master_hash, apparatus_hash):
        path, audit_hash = selection.get("body_equivalence_audit"), selection.get("body_equivalence_audit_sha256")
        require(valid_sha(audit_hash), "Master selection lacks body-equivalence audit hash")
        audit = self.json(path, audit_hash)
        mp, ap = "readers/PS_EN_master_annotated.pdf", "readers/PS_EN_corrected_apparatus.pdf"
        master, apparatus = self.pdf(mp, master_hash), self.pdf(ap, apparatus_hash)
        require(audit.get("master_pdf") == mp and audit.get("master_pdf_sha256") == master_hash
                and audit.get("apparatus_pdf") == ap and audit.get("apparatus_pdf_sha256") == apparatus_hash,
                "Master-body equivalence audit identifies stale PDFs")
        require(audit.get("audit_complete") is True and not audit.get("integrity_issues")
                and audit.get("page_count_identical") is True and audit.get("all_body_pages_compared") is True
                and audit.get("all_body_pages_byte_identical") is True and audit.get("direct_image_openings_claimed") == 0,
                "Master-body equality has not been proved without a false direct-opening claim")
        require(audit.get("master_page_count") == audit.get("apparatus_page_count") == len(master) == len(apparatus),
                "Master-body comparison has inconsistent page counts")
        renderer = audit.get("renderer", {})
        require(renderer.get("dpi") == 144 and renderer.get("matrix_scale") == 2.0
                and renderer.get("colorspace") == "RGB" and renderer.get("alpha") is False,
                "Master-body comparison was not rendered at 144 dpi in RGB")
        pages = audit.get("pages", [])
        require(audit.get("body_pages_compared") == len(pages) == len(master) - 1
                and {x.get("page") for x in pages} == set(range(2, len(master) + 1)),
                "Master-body comparison omits or duplicates body pages")
        for row in pages:
            number = row["page"]
            m, a = row.get("master_144dpi", {}), row.get("apparatus_144dpi", {})
            require(valid_signature(m) and valid_signature(a) and valid_sha(m.get("png_sha256"))
                    and m == a and row.get("pixels_byte_identical") is True and row.get("png_byte_identical") is True
                    and row.get("geometry_identical") is True
                    and row.get("master_geometry") == geometry(master[number - 1])
                    and row.get("apparatus_geometry") == geometry(apparatus[number - 1])
                    and row["master_geometry"] == row["apparatus_geometry"],
                    f"Master body page {number} lacks an exact byte-equality proof")
        return {"audit": path, "audit_sha256": audit_hash, "raster_dpi": 144,
                "all_body_pages_compared": True, "body_pages_byte_identical": sorted(x["page"] for x in pages),
                "apparatus_pdf_sha256": apparatus_hash, "direct_image_openings_claimed": 0}

    def assert_unchanged(self):
        for path, digest in self.files.items():
            require(sha256(self.path(path).read_bytes()) == digest, "Evidence changed during final gate: " + path)


def validate_selection(v, stem, sha, page_count):
    selection = v.json("records/QA_SELECTION_" + stem + ".json")
    require(selection.get("pdf") == "readers/" + stem + ".pdf" and selection.get("pdf_sha256") == sha
            and selection.get("pdf_pages") == page_count, "Stale page selection: " + stem)
    require(not selection.get("unmapped_historical_keys") and not selection.get("unmapped_historical_overflow_keys"),
            "Historical overflow source absent from PDF map: " + stem)
    rows = selection.get("selections", [])
    pages = [r.get("page") for r in rows]
    require(len(pages) == len(set(pages)) and all(isinstance(p, int) and 1 <= p <= page_count for p in pages),
            "Invalid or duplicate selected pages: " + stem)
    for row in rows:
        require(row.get("pdf") == selection["pdf"] and row.get("pdf_sha256") == sha,
                "A selected page identifies a stale PDF: " + stem)
    if stem in STEMS[:3]:
        expected = {round(i * (page_count - 1) / 39) + 1 for i in range(40)} if page_count >= 40 else set(range(1, page_count + 1))
        require(set(selection.get("systematic_sample_pages", [])) == expected and expected <= set(pages),
                "Systematic forty-page sample is incomplete: " + stem)
    if stem == "PS_GUIDE":
        require(set(pages) == set(range(1, page_count + 1)), "Complete guide selection is missing pages")
    if stem == "PS_EN_master_annotated":
        require(1 in pages, "Distinct master front is not selected")
    mapping = selection.get("historical_raster_overflow_mapping", [])
    if stem == "PS_EN_corrected_apparatus":
        expected = set()
        for history in sorted((v.project / "records").glob("INK_HISTORY_PS_EN_corrected_apparatus_*.json")):
            relative = history.relative_to(v.project).as_posix()
            for item in v.json(relative).get("candidate_pages", []):
                if any(c["bbox_pt"][1] >= 779 for c in item.get("components", [])):
                    expected.add((relative, item["page"]))
        actual = [(m.get("history"), m.get("old_pdf_page")) for m in mapping]
        require(len(actual) == len(set(actual)) and set(actual) == expected,
                "Historical bottom-overflow sheet mapping is incomplete or duplicated")
        selected_by_page = {r["page"]: r for r in rows}
        for m in mapping:
            require(m.get("final_pdf_page") in selected_by_page
                    and m.get("source_key") == selected_by_page[m["final_pdf_page"]].get("key"),
                    "A historical bottom-overflow sheet lacks its selected current source page")
    return selection


def run_gate(project, allow_omitted_historical_pdfs=False):
    project = project.resolve()
    v = EvidenceValidator(project, allow_omitted_historical_pdfs)
    issues, results, visual, historical = [], {}, [], []
    v.bytes("scripts/final_qa_gate.py")
    v.bytes("scripts/write_final_reports.py")
    structure = v.json("records/FINAL_STRUCTURE_AUDIT.json")
    if structure.get("complete") is not True or structure.get("issues"):
        issues.append("Final structural audit has unresolved issues.")
    try:
        coverage = v.json("records/COVERAGE_AUDIT.json")
        require(coverage.get("complete") is True
                and coverage.get("source_pages") == coverage.get("checked_page_files")
                == coverage.get("pages_with_complete_ledger") == 706,
                "Source-review coverage is incomplete")
        for field in ["required_differences_without_decisions_on_reviewed_pages",
                      "original_doubts_without_decisions_on_reviewed_pages", "notes_without_decisions_on_reviewed_pages",
                      "duplicate_source_ids", "concordance_followups"]:
            require(coverage.get(field) == [], "Unresolved source-review coverage: " + field)
        for path in ["records/REVIEW_COVERAGE.tsv", "records/CHANGES_EN.tsv", "records/CHECK_DECISIONS.tsv",
                     "records/GUIDE_MANIFEST.json", "records/MARK_COUNT_CORRECTION.json"]:
            v.bytes(path)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        issues.append(str(exc))
    try:
        replay = v.json("records/CHANGE_REPLAY_AUDIT.json")
        require(replay.get("schema_version") == 2 and replay.get("complete") is True
                and replay.get("source_coverage_complete") is True
                and replay.get("pages") == replay.get("equal_pages") == 706
                and replay.get("unmatched_records") == [] and replay.get("adjudication_issues") == []
                and replay.get("exceptions") == [],
                "Change replay has an unexplained record, unequal page, exception, or source-coverage gap")
        require(valid_sha(replay.get("adjudication_sha256")), "Change replay lacks the adjudication-file hash")
        v.json(replay.get("adjudication_file"), replay["adjudication_sha256"])
    except (OSError, ValueError, TypeError, KeyError) as exc:
        issues.append(str(exc))
    current = {}
    for stem in STEMS:
        pdf_path = "readers/" + stem + ".pdf"
        pdf = v.pdf(pdf_path)
        current[stem] = (pdf_path, v.files[pdf_path], pdf)
    try:
        v.final_omissions()
    except (OSError, ValueError, TypeError, KeyError) as exc:
        issues.append(str(exc))
    for file in sorted((project / "records").glob("FINAL_VISUAL_QA_*.json")):
        relative = file.relative_to(project).as_posix()
        container = v.json(relative)
        for index, row in enumerate(rows_from(container)):
            visual.append((relative, index, container, row))
    for stem in STEMS:
        pdf_path, sha, pdf = current[stem]
        result = {"pdf_sha256": sha, "selected_pages": [], "direct_current_pdf_viewed_pages": [],
                  "inherited_exact_raster_review_pages": [], "verified_visual_review_pages": [],
                  "actually_viewed_pages": [], "validated_visual_evidence": []}
        results[stem] = result
        if structure.get("pdfs", {}).get(stem, {}).get("pdf_sha256") != sha:
            issues.append("Stale structural PDF audit: " + stem)
        try:
            source_hash = structure.get("forms", {}).get(stem, {}).get("source_sha256")
            require(valid_sha(source_hash), "Missing structural source hash: " + stem)
            v.bytes("readers/" + stem + ".tex", source_hash)
            build = v.json(structure["forms"][stem]["latest_build_record"])
            require(build.get("source_sha256") == source_hash and build.get("pdf_sha256") == sha
                    and build.get("pdf_pages") == len(pdf) and build.get("exit") == 0
                    and build.get("source_changed_during_build") is False
                    and build.get("missing_character_lines") == 0
                    and isinstance(build.get("widest_pt"), (int, float)) and build["widest_pt"] <= 2
                    and not build.get("link_mark_count_mismatches") and not build.get("unexpected_link_mark_keys"),
                    "Build record is stale or has unresolved errors/overflow/link mismatches: " + stem)
            v.bytes(build.get("log"))
            ink = v.json("records/INK_AUDIT_" + stem + ".json")
            require(ink.get("pdf") == pdf_path and ink.get("pdf_sha256") == sha, "Stale ink audit: " + stem)
            require(ink.get("pages_screened") == len(pdf) and ink.get("raster_dpi") == 144,
                    "Ink screening did not cover every current page at 144 dpi: " + stem)
            require(not ink.get("objects_outside_sheet"), "Ink objects outside the sheet: " + stem)
            require(ink.get("complete_visual_adjudication") is True, "Ink candidates not fully adjudicated: " + stem)
            candidates = ink.get("candidate_pages", [])
            require(len({x.get("page") for x in candidates}) == len(candidates), "Duplicate ink candidate pages")
            for row in candidates:
                require(isinstance(row.get("page"), int) and 1 <= row["page"] <= len(pdf)
                        and row.get("adjudication") in ALLOWED_INK and bool(row.get("observation", "").strip()),
                        "Unresolved ink candidate: " + stem + " page " + str(row.get("page")))
            expected_components = {(row["page"], index) for row in candidates
                                   for index in range(1, len(row.get("components", [])) + 1)}
            inspected_components = set()
            for inspection in ink.get("actual_crop_inspections", []):
                require(inspection.get("viewed") is True, "Ink contact sheet was not actually opened: " + stem)
                v.png(inspection.get("image"), inspection.get("image_sha256"))
                map_path = str(PurePath(inspection["image"]).parent / "CONTACT_MAP.json")
                contact_map = v.json(map_path)
                require(contact_map.get("pdf_sha256") == sha,
                        "Ink contact sheet map identifies a stale PDF: " + stem)
                matches = [item for item in contact_map.get("contacts", []) if item.get("image") == inspection["image"]]
                require(len(matches) == 1 and matches[0].get("components") == inspection.get("components"),
                        "Opened ink contact sheet disagrees with its component map: " + stem)
                inspected_components.update((item["page"], item["component"]) for item in inspection["components"])
            require(inspected_components == expected_components,
                    "Ink candidates lack complete actual-contact-image coverage: " + stem)
            result.update(ink_pages_screened=ink["pages_screened"],
                          ink_candidate_pages=[r["page"] for r in candidates], objects_outside_sheet=0)
        except (OSError, ValueError, TypeError, KeyError) as exc:
            issues.append(str(exc))
        selection = None
        try:
            selection = validate_selection(v, stem, sha, len(pdf))
            result["selected_pages"] = [r["page"] for r in selection["selections"]]
            mapping = selection.get("historical_raster_overflow_mapping", [])
            result["historical_bottom_overflow_sheets_mapped"] = len(mapping)
            result["historical_bottom_overflow_target_pages"] = sorted({r["final_pdf_page"] for r in mapping})
            result["historical_log_overflow_source_pages"] = len(selection.get("historical_overflow_keys", []))
            result["landscape_pages"] = selection.get("landscape_pages", [])
            result["systematic_sample_pages"] = selection.get("systematic_sample_pages", [])
        except (OSError, ValueError, TypeError, KeyError) as exc:
            issues.append(str(exc))
        direct, inherited = set(), set()
        for file, index, container, row in visual:
            row_sha = row.get("pdf_sha256") or (container.get("pdf_sha256") if isinstance(container, dict) else None)
            if row_sha != sha:
                continue
            try:
                if isinstance(container, dict) and container.get("pdf_sha256"):
                    require(container["pdf_sha256"] == sha, "Evidence container and row identify different PDFs")
                if row.get("inspection_method") == INHERITED_METHOD:
                    v.validate_inherited(row, container, pdf_path, sha, pdf)
                    inherited.add(row["page"])
                    basis = INHERITED_METHOD
                else:
                    v.validate_direct(row, pdf_path, sha, pdf)
                    direct.add(row["page"])
                    basis = DIRECT_METHOD
                result["validated_visual_evidence"].append(dict(row, evidence_file=file,
                    evidence_file_sha256=v.files[file], evidence_entry_index=index, review_basis=basis))
            except (OSError, ValueError, TypeError, KeyError, IndexError) as exc:
                issues.append(f"Invalid current visual evidence {file} entry {index}: {exc}")
        result.update(direct_current_pdf_viewed_pages=sorted(direct),
                      inherited_exact_raster_review_pages=sorted(inherited - direct),
                      verified_visual_review_pages=sorted(direct | inherited), actually_viewed_pages=sorted(direct))
        changed_pages = set()
        audited_paths = set()
        for record in result["validated_visual_evidence"]:
            if record["review_basis"] != INHERITED_METHOD:
                continue
            provenance = record["provenance"]
            if provenance["equivalence_audit"] in audited_paths:
                continue
            audited_paths.add(provenance["equivalence_audit"])
            audit = v.json(provenance["equivalence_audit"], provenance["equivalence_audit_sha256"])
            changed_pages.update(audit["changed_pages"])
        result["changed_pages_requiring_direct_opening"] = sorted(changed_pages)
        if changed_pages - direct:
            issues.append("Changed raster pages lack direct current-image openings: " + stem + " "
                          + ",".join(map(str, sorted(changed_pages - direct))))
        missing = sorted(set(result["selected_pages"]) - direct - inherited)
        if missing:
            issues.append("Selected pages lack validated visual review: " + stem + " " + ",".join(map(str, missing)))
        if stem == "PS_EN_master_annotated":
            if 1 not in direct:
                issues.append("Distinct master front lacks a direct current-PDF image opening.")
            if selection is not None:
                try:
                    result["master_body_equivalence"] = v.master_body(selection, sha, current["PS_EN_corrected_apparatus"][1])
                except (OSError, ValueError, TypeError, KeyError) as exc:
                    issues.append(str(exc))
    master = results["PS_EN_master_annotated"].get("master_body_equivalence")
    if master:
        master["reviewed_apparatus_pages_reused"] = sorted(set(master["body_pages_byte_identical"])
            & set(results["PS_EN_corrected_apparatus"]["verified_visual_review_pages"]))
    hashes = {value[1] for value in current.values()}
    for file, index, container, row in visual:
        row_sha = row.get("pdf_sha256") or (container.get("pdf_sha256") if isinstance(container, dict) else None)
        if row_sha not in hashes:
            historical.append({"evidence_file": file, "entry_index": index, "pdf_sha256": row_sha,
                               "page": row.get("page"), "status": row.get("status"),
                               "counted_as_current_review": False})
    try:
        checkpoint = v.json("records/CHECKPOINT_INVENTORY.json")
        require(checkpoint.get("complete") is True, "Checkpoint inventory is not complete.")
        v.assert_unchanged()
    except (OSError, ValueError, TypeError) as exc:
        issues.append(str(exc))
    return {"schema_version": 2, "complete": not issues, "issues": issues, "pdfs": results,
            "evidence_counting_policy": {
                "actually_viewed_pages": "Direct current-PDF image openings only; alias of direct_current_pdf_viewed_pages.",
                "inherited_exact_raster_review_pages": "Prior actual-image observations with preserved provenance and equality at 144 dpi and original scale; excludes pages also opened directly.",
                "master_body_equivalence": "Every body page compared at 144 dpi; only reviewed corresponding apparatus pages inherit visual coverage. Comparison is not an image opening."},
            "visual_evidence_files": sorted({item[0] for item in visual}),
            "superseded_visual_evidence_not_counted": historical,
            "final_omissions": list((v.omissions or {}).values()),
            "historical_pdf_verification": v.historical_pdf_verification,
            "extracted_delivery_omission_mode": allow_omitted_historical_pdfs,
            "validated_input_sha256": dict(sorted(v.files.items()))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=PROJECT)
    parser.add_argument("--allow-omitted-historical-pdfs", action="store_true",
                        help="For extracted delivery only: validate explicit supersessions and preserved old-PNG provenance when historical PDFs are absent.")
    parser.add_argument("--check-only", action="store_true", help="Validate without rewriting the archived FINAL_QA_GATE.json.")
    args = parser.parse_args()
    project = args.project.resolve()
    try:
        result = run_gate(project, args.allow_omitted_historical_pdfs)
    except (OSError, ValueError, TypeError, KeyError, IndexError) as exc:
        result = {"schema_version": 2, "complete": False,
                  "issues": ["Final QA gate could not complete: " + str(exc)], "pdfs": {}}
    if not args.check_only:
        path = project / "records/FINAL_QA_GATE.json"
        temporary = path.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
        temporary.replace(path)
    print(json.dumps({"complete": result["complete"], "issues": result["issues"], "check_only": args.check_only,
                      "extracted_delivery_omission_mode": args.allow_omitted_historical_pdfs}))
    return 0 if result["complete"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
