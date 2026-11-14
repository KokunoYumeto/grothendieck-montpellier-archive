#!/usr/bin/env python3
"""Re-screen existing compiled PDFs without claiming a new compilation or view."""
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
from compile_readers import EDITION,inspect_pdf


def main():
    fields=("text_outside_sheet","text_outside_permitted_area","vector_paths","images",
        "vector_paths_outside_sheet","vector_paths_outside_permitted_area",
        "images_outside_sheet","images_outside_permitted_area","graphics_geometry_note")
    summaries=[]
    for path in sorted((EDITION/"build").glob("*/audit/report.json")):
        report=json.loads(path.read_text())
        pdf=path.parents[1]/(report["reader"]+".pdf")
        if not pdf.is_file() or report.get("exit_codes",[1])[-1]!=0:
            continue
        screen=inspect_pdf(pdf)
        for field in fields:report[field]=screen[field]
        required=set(report.get("required_visual_review_pages",[]))
        for field in fields:
            if isinstance(screen[field],list):
                required.update(row["pdf_page"] for row in screen[field])
        report["required_visual_review_pages"]=sorted(required)
        report["geometry_audit_utc"]=datetime.now(timezone.utc).isoformat()
        report["geometry_pdf_sha256"]=hashlib.sha256(pdf.read_bytes()).hexdigest()
        if screen["text_outside_sheet"]:report["mechanical_gates_passed"]=False
        path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
        summaries.append(dict(reader=report["reader"],vector_paths=screen["vector_paths"],images=screen["images"],
            vector_sheet_flags=len(screen["vector_paths_outside_sheet"]),vector_area_flags=len(screen["vector_paths_outside_permitted_area"]),
            image_sheet_flags=len(screen["images_outside_sheet"]),image_area_flags=len(screen["images_outside_permitted_area"])))
    print(json.dumps(summaries))


if __name__=="__main__":main()
