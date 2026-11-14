"""Verify frozen full-page image records, including direct-view equivalence proofs."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

EDITION=Path(__file__).resolve().parents[1]


def verify_visual_record(row, visual_rows, equivalences, freeze_rows, cache=None):
    cache={} if cache is None else cache
    issues=[]
    def digest(path):
        key=str(path)
        if key not in cache:cache[key]=hashlib.sha256(path.read_bytes()).hexdigest()
        return cache[key]
    def image_record(record):
        name=record.get("reader","");pdfhash=record.get("pdf_sha256","")
        if not any(r.get("reader")==name and r.get("pdf_sha256")==pdfhash for r in freeze_rows):
            return "Image record has no documented PDF freeze."
        manifestpath=EDITION/"build/visual_review"/name/pdfhash/"manifest.json"
        if not manifestpath.is_file():return "Frozen image manifest is absent."
        manifest=json.loads(manifestpath.read_text())
        if manifest.get("reader")!=name or manifest.get("pdf_sha256")!=pdfhash:
            return "Image manifest identifies a different PDF."
        image=manifest.get("images",{}).get(str(record.get("pdf_page")))
        if not image or image.get("path")!=record.get("image"):
            return "Full-page image is absent from its frozen manifest."
        path=EDITION/image["path"]
        if not path.is_file():return "Recorded full-page image is absent."
        actual=digest(path)
        if actual!=image.get("sha256") or actual!=record.get("image_sha256"):
            return "Recorded full-page image bytes differ from their hashes."
        return ""
    problem=image_record(row)
    if problem:issues.append(problem)
    if row.get("review_method")=="byte-identical full-page image":
        source_name=row.get("evidence_source_reader")
        source_hash=row.get("evidence_source_pdf_sha256")
        source_page=str(row.get("evidence_source_pdf_page"))
        candidates=[r for r in visual_rows if r.get("reader")==source_name and
            r.get("pdf_sha256")==source_hash and str(r.get("pdf_page"))==source_page]
        origin=candidates[-1] if candidates else {}
        if (origin.get("result")!="layout inspection passed" or
            origin.get("review_method")=="byte-identical full-page image" or
            origin.get("reviewed_utc")!=row.get("evidence_original_reviewed_utc")):
            issues.append("Equivalence has no current direct-view passing source observation.")
        else:
            problem=image_record(origin)
            if problem:issues.append("Equivalence source: "+problem)
            if origin.get("image_sha256")!=row.get("image_sha256"):
                issues.append("Equivalent source and target PNG hashes differ.")
        proof=any(p.get("source_reader")==source_name and p.get("source_pdf_sha256")==source_hash and
            str(p.get("source_pdf_page"))==source_page and p.get("source_image")==origin.get("image") and
            p.get("target_reader")==row.get("reader") and p.get("target_pdf_sha256")==row.get("pdf_sha256") and
            str(p.get("target_pdf_page"))==str(row.get("pdf_page")) and p.get("target_image")==row.get("image") and
            p.get("image_sha256")==row.get("image_sha256") and
            p.get("original_reviewed_utc")==row.get("evidence_original_reviewed_utc")
            for p in equivalences)
        if not proof:issues.append("The explicit complete-PNG equivalence proof is absent.")
    return issues
