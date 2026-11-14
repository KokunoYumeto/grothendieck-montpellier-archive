#!/usr/bin/env python3
"""Summarize actual checked-input build records without inferring visual review."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
from edition_core import read_tsv,write_tsv,extract_variants,sha256

EDITION=Path(__file__).resolve().parents[1]


def filehash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    records=EDITION/"records"
    cleanup=records/"CLEANUP_LOG_all.tsv"
    if cleanup.is_file():
        rows=read_tsv(cleanup)
        write_tsv(EDITION/"CLEANUP_LOG.tsv",rows,["key","line","before","after","action","reason"])
    fixes=[]
    for file in sorted(records.glob("TYPESETTING_FIXES_*.tsv")):
        fixes+=read_tsv(file)
    write_tsv(EDITION/"TYPESETTING_FIXES.tsv",fixes,["reader","page_key","source_line","issue","repair","before","after","occurrences"])
    visualfile=records/"PDF_VISUAL_REVIEW.tsv"
    viewed=read_tsv(visualfile) if visualfile.is_file() else []
    patchfile=records/"TYPESETTING_PATCHES.json"
    historicalkeys={p["key"] for p in json.loads(patchfile.read_text())} if patchfile.is_file() else set()
    text=["# Typesetting report","","This report is generated from actual compile logs, PDF annotations, source-mark inventories, and any separately recorded visual inspections. An error-free compilation does not certify a scan reading or a visual page review.",""]
    summaries=[]
    for file in sorted((EDITION/"build").glob("*/audit/report.json")):
        r=json.loads(file.read_text());name=r["reader"]
        source=EDITION/r["source"]
        pdf=file.parents[1]/(name+".pdf")
        phash=filehash(pdf) if pdf.is_file() else ""
        matching=[v for v in viewed if v.get("reader")==name and v.get("pdf_sha256")==phash]
        inspected=sorted({int(v["pdf_page"]) for v in matching})
        needed=set(r.get("required_visual_review_pages",[]))
        sourcepages=r.get("source_physical_pages",{})
        for key in historicalkeys:
            start=sourcepages.get(key)
            if start:
                following=[p for p in sourcepages.values() if p>start]
                stop=min(following)-1 if following else r.get("pdf_pages",start)
                needed.update(range(start,stop+1))
        needed=sorted(needed)
        remaining=sorted(set(needed)-set(inspected))
        boxes=r.get("overfull_boxes",[])
        widest=max((b["excess_pt"] for b in boxes),default=0)
        counts=r.get("logical_link_marks",{})
        current=bool(source.is_file() and r.get("source_sha256")==sha256(source.read_text()))
        inputs=r.get("source_files_sha256",{})
        stale_inputs=[rel for rel,digest in inputs.items()
            if not (EDITION/rel).is_file() or sha256((EDITION/rel).read_text())!=digest]
        inputs_current=(not stale_inputs) if inputs else "not recorded in this earlier build"
        text += ["## "+name,"",
            f"PDF pages: {r.get('pdf_pages','not produced')}. Compile exit codes: {r.get('exit_codes',[])}. Errors: {len(r.get('latex_errors',[]))}. Missing characters: {len(r.get('missing_characters',[]))}.",
            f"Overfull boxes: {len(boxes)}; wider than 2 pt: {sum(b['excess_pt']>2 for b in boxes)}; widest: {widest:.5f} pt.",
            f"Current reader-file hash matches the compiled version: {str(current).lower()}. Mechanical gates passed at this build: {str(r.get('mechanical_gates_passed',False)).lower()}.",
            f"Source files and rendering settings still match this compiled snapshot: {str(inputs_current).lower()}. Changed or missing inputs: {json.dumps(stale_inputs,ensure_ascii=False)}.",
            f"Logical link marks: {json.dumps(counts,sort_keys=True)}. PDF link annotations: {r.get('link_annotations','not counted')}; archive annotations: {r.get('archive_link_annotations','not counted')}. Source-mark counts match: {str(r.get('source_link_counts_match',False)).lower()}.",
            f"Distinct archive pages linked: {json.dumps(r.get('distinct_archive_pages',{}),sort_keys=True)}.",
            f"Text outside the sheet: {json.dumps(r.get('text_outside_sheet',[]),ensure_ascii=False)}.",
            f"Automated type-area flags requiring visual assessment: {json.dumps(r.get('text_outside_permitted_area',[]),ensure_ascii=False)}.",
            f"Landscape pages: {r.get('landscape_pages',[])}.",
            f"Pages required for the current visual review: {needed}.",
            f"Pages with an inspection record matching this exact PDF: {inspected}. Still pending: {remaining}.",""]
        for v in matching:text.append(f"- Page {v['pdf_page']}: {v.get('findings','')}")
        if matching:text.append("")
        history=file.parent/"BUILD_HISTORY.tsv"
        if history.is_file():
            rows=read_tsv(history)
            text += ["Recorded compile history:","",
                "| Build time (UTC) | Pages | Errors | Missing glyphs | Overfull > 2 pt | Widest (pt) |",
                "|---|---:|---:|---:|---:|---:|"]
            for h in rows:
                text.append(f"| {h['build_time_utc']} | {h['pdf_pages']} | {h['errors']} | {h['missing_characters']} | {h['overfull_gt_2pt']} | {h['widest_pt']} |")
            text.append("")
        summaries.append(dict(reader=name,pdf_pages=r.get("pdf_pages",""),errors=len(r.get("latex_errors",[])),
            missing_characters=len(r.get("missing_characters",[])),overfull_gt_2pt=sum(b["excess_pt"]>2 for b in boxes),
            widest_pt=widest,source_hash_matches=current,build_inputs_current=inputs_current,changed_build_inputs=" ".join(stale_inputs),logical_links=json.dumps(counts,sort_keys=True),
            source_link_counts_match=r.get("source_link_counts_match",False),visual_pages_viewed=" ".join(map(str,inspected)),
            visual_pages_pending=" ".join(map(str,remaining)),pdf_sha256=phash))
    text += ["## Development outputs","","The separate development tree contains explicitly unchecked diagnostics. Those outputs are not certified readers and are excluded from the checked-input status above. Their logs remain available as development records.",""]
    (EDITION/"TYPESETTING_REPORT.md").write_text("\n".join(text))
    write_tsv(records/"COMPILE_SUMMARY.tsv",summaries)
    apparatus=["# Apparatus counts","","Counts are of entries actually selected for each form. A nested physical correction retains its own source ID; restored copies link to the donor entry. English-only omissions are listed in EN_VARIANT_OMISSIONS.tsv.","",
        "| Reader | Source pages | Kind | Printed entries |","|---|---:|---|---:|"]
    for inventory in sorted(records.glob("READER_INVENTORY_*.tsv")):
        for r in read_tsv(inventory):
            counts={}
            if r["mode"]=="1":
                for key in r["source_keys"].split():
                    variants=json.loads((EDITION/"variant_records"/(key+".json")).read_text())
                    if r["family"]=="en":
                        present=extract_variants((EDITION/"master_pages/en"/(key+".tex")).read_text())
                        variants=[v for v in variants if v["source_id"] in present]
                    for v in variants:counts[v["kind"]]=counts.get(v["kind"],0)+1
            if not counts:counts={"none in this form":0}
            for kind,n in sorted(counts.items()):
                apparatus.append(f"| {r['reader']} | {r['source_pages']} | {kind} | {n} |")
    (EDITION/"APPARATUS_COUNTS.md").write_text("\n".join(apparatus)+"\n")
    print(f"Summarized {len(summaries)} checked-input PDF build reports; visual inspection status remains explicit.")


if __name__=="__main__":main()
