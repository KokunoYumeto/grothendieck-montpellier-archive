#!/usr/bin/env python3
"""Measure the only explicitly resized diagram in the checked source.

The typed node marker has the 10pt body font before resizebox. Its PDF text
matrix supplies the rendered font size, so the ratio measures the local scale.
The record does not assert that anyone has visually inspected the page.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re
import fitz
from edition_core import write_tsv

EDITION=Path(__file__).resolve().parents[1]
KEY="ega24_24_054"
READERS=("EGA_V24_EN_diplomatic","EGA_V24_EN_corrected_apparatus",
         "EGA_V24_EN_reading","EGA_V24_EN_master_annotated")


def main():
    scaled=[]
    for path in (EDITION/"checked_pages").glob("*.tex"):
        for line_no,line in enumerate(path.read_text().splitlines(),1):
            if re.search(r"\\(?:resizebox|scalebox)\b",line):
                scaled.append((path.stem,line_no,line))
    unexpected=[r for r in scaled if r[0]!=KEY or r[2].count(r"\resizebox{\linewidth}{!}")!=1]
    if unexpected:
        raise SystemExit("Unmeasured scaling locations: "+repr(unexpected))
    if len(scaled)!=1:
        raise SystemExit("The recorded single local scaling target is missing or duplicated.")
    rows=[]
    for name in READERS:
        folder=EDITION/"build"/name
        pdf=folder/(name+".pdf")
        report=json.loads((folder/"audit/report.json").read_text())
        page_no=report["source_physical_pages"].get(KEY)
        if page_no is None:
            raise SystemExit(name+": source54 is absent from this PDF.")
        doc=fitz.open(pdf)
        markers=[span for block in doc[page_no-1].get_text("dict")["blocks"]
                 for line in block.get("lines",[]) for span in line["spans"]
                 if span["text"]=="We always assume that"]
        if len(markers)!=1:
            raise SystemExit(name+": the typed scaling marker is not unique.")
        nominal=10*72/72.27
        rendered=markers[0]["size"]
        scale=rendered/nominal
        rows.append(dict(reader=name,source_key=KEY,pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),
            pdf_page=page_no,nominal_font_pdf_pt=nominal,rendered_font_pdf_pt=rendered,
            measured_scale=scale,minimum_allowed_scale=.7,
            result="above 70 percent" if scale>=.7 else "FAIL: below 70 percent",
            method="Read the PDF text-matrix font size of the typed node within the individually resized TikZ line; compare with the 10pt body font converted from TeX pt to PDF pt."))
    write_tsv(EDITION/"records/LOCAL_DIAGRAM_SCALE_AUDIT.tsv",rows)
    print(json.dumps([dict(reader=r["reader"],scale=r["measured_scale"],result=r["result"]) for r in rows]))
    if any(r["measured_scale"]<.7 for r in rows):
        raise SystemExit(1)


if __name__=="__main__":
    main()
