#!/usr/bin/env python3
"""Summarize actual checked-input build records without inferring visual review."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
from edition_core import read_tsv,write_tsv,extract_variants,sha256
from build_report_provenance import capture_inputs, seal_reports

EDITION=Path(__file__).resolve().parents[1]


def filehash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_cell(value):
    return str(value).replace("|", r"\|").replace("\n", " ")


def geometry_summary(report, reader, pdf_hash, ledger):
    latest={(int(row["pdf_page"]),row["flag_kind"]):row for row in ledger
        if row.get("reader")==reader and row.get("pdf_sha256")==pdf_hash}
    groups={}
    for kind in ("text_outside_sheet","text_outside_permitted_area",
                 "vector_paths_outside_sheet","vector_paths_outside_permitted_area",
                 "images_outside_sheet","images_outside_permitted_area"):
        for flag in report.get(kind,[]):
            identity=(int(flag["pdf_page"]),kind)
            groups[identity]=groups.get(identity,0)+1
    rows=[]
    pending=0
    for (page,kind),count in sorted(groups.items()):
        record=latest.get((page,kind),{})
        allowed={"single-letter-overhang"} if kind=="text_outside_permitted_area" else {"conservative-rectangle-no-visible-overflow"}
        accepted=record.get("decision") in allowed and bool(record.get("reason"))
        if accepted:
            outcome={"single-letter-overhang":"Permitted single-letter overhang",
                "conservative-rectangle-no-visible-overflow":"Conservative rectangle; no visible overflow"}[record["decision"]]
            reason=record["reason"]
        else:
            pending+=1
            outcome="Pending accepted disposition"
            reason=record.get("reason") or "No accepted disposition is recorded for this exact PDF hash, page and flag kind."
        rows.append((page,kind,count,outcome,reason))
    lines=[f"Geometry flag groups: {len(groups)}; with accepted recorded dispositions: {len(groups)-pending}; still pending: {pending}.",""]
    if rows:
        lines += ["| PDF page | Raw flag kind | Flag instances | Recorded outcome | Recorded reason |",
                  "|---:|---|---:|---|---|"]
        lines += ["| "+" | ".join(table_cell(value) for value in row)+" |" for row in rows]
        lines.append("")
    return lines,len(groups),pending


def main():
    report_inputs=capture_inputs()
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
    geometryfile=records/"PDF_GEOMETRY_REVIEW.tsv"
    geometry=read_tsv(geometryfile) if geometryfile.is_file() else []
    patchfile=records/"TYPESETTING_PATCHES.json"
    historicalkeys={p["key"] for p in json.loads(patchfile.read_text())} if patchfile.is_file() else set()
    text=["# Typesetting report","","This report is generated from actual compile logs, PDF annotations, source-mark inventories, and separately recorded visual evidence. Direct inspections and byte-identical full-page image equivalences are distinguished below. An error-free compilation does not certify a scan reading or a visual page review.","",
        "The input and output hashes for this generation are recorded in records/BUILD_REPORT_PROVENANCE.json; the release audit rejects a missing or stale proof.",""]
    summaries=[]
    for file in sorted((EDITION/"build").glob("*/audit/report.json")):
        r=json.loads(file.read_text());name=r["reader"]
        source=EDITION/r["source"]
        pdf=file.parents[1]/(name+".pdf")
        phash=filehash(pdf) if pdf.is_file() else ""
        matching=[v for v in viewed if v.get("reader")==name and v.get("pdf_sha256")==phash]
        latest={int(v["pdf_page"]):v for v in matching}
        inspected=sorted(page for page,v in latest.items()
            if v.get("result","").startswith("layout inspection passed"))
        equivalent=sorted(page for page in inspected
            if latest[page].get("review_method")=="byte-identical full-page image")
        direct=sorted(set(inspected)-set(equivalent))
        open_issues=sorted(page for page,v in latest.items() if v.get("result")=="layout issue found")
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
        geometry_lines,geometry_groups,geometry_pending=geometry_summary(r,name,phash,geometry)
        text += ["## "+name,"",
            f"PDF SHA-256: {phash}.",
            f"PDF pages: {r.get('pdf_pages','not produced')}. Compile exit codes: {r.get('exit_codes',[])}. Errors: {len(r.get('latex_errors',[]))}. Missing characters: {len(r.get('missing_characters',[]))}.",
            f"Overfull boxes: {len(boxes)}; wider than 2 pt: {sum(b['excess_pt']>2 for b in boxes)}; widest: {widest:.5f} pt.",
            f"Current reader-file hash matches the compiled version: {str(current).lower()}. Mechanical gates passed at this build: {str(r.get('mechanical_gates_passed',False)).lower()}.",
            f"PDF hash matches the compile report: {str(phash==r.get('pdf_sha256')).lower()}. Individual source-page link destinations match: {str(r.get('link_targets_match_source_pages',False)).lower()}.",
            f"Source files and rendering settings still match this compiled snapshot: {str(inputs_current).lower()}. Changed or missing inputs: {json.dumps(stale_inputs,ensure_ascii=False)}.",
            f"Logical link marks: {json.dumps(counts,sort_keys=True)}. PDF link annotations: {r.get('link_annotations','not counted')}; archive annotations: {r.get('archive_link_annotations','not counted')}. Source-mark counts match: {str(r.get('source_link_counts_match',False)).lower()}.",
            f"Distinct archive pages linked: {json.dumps(r.get('distinct_archive_pages',{}),sort_keys=True)}.",
            f"Text outside the sheet: {json.dumps(r.get('text_outside_sheet',[]),ensure_ascii=False)}.",
            f"Automated type-area flags requiring visual assessment: {json.dumps(r.get('text_outside_permitted_area',[]),ensure_ascii=False)}.",
            f"Vector paths screened: {r.get('vector_paths','not yet screened')}; images screened: {r.get('images','not yet screened')}. Graphics rectangles are screening bounds; the disposition table below records the observed result.",
            f"Vector-path sheet flags: {json.dumps(r.get('vector_paths_outside_sheet',[]))}. Vector-path type-area flags: {json.dumps(r.get('vector_paths_outside_permitted_area',[]))}.",
            f"Image sheet flags: {json.dumps(r.get('images_outside_sheet',[]))}. Image type-area flags: {json.dumps(r.get('images_outside_permitted_area',[]))}.",
            f"Marginal note/attachment pairs: {len(r.get('margin_note_page_audit',[]))}; all remain on the same physical page: {str(r.get('margin_notes_stay_with_anchors',False)).lower()}.",
            f"Automated marginal-text overlap candidates requiring visual assessment: {json.dumps(r.get('margin_overlap_candidates',[]),ensure_ascii=False)}.",
            f"Landscape pages: {r.get('landscape_pages',[])}.",
            f"Pages required for the current visual review: {needed}.",
            f"Pages covered by passed evidence matching this exact PDF: {inspected}. Still pending: {remaining}.",
            f"Directly inspected pages: {direct}. Pages covered by explicitly recorded byte-identical full-page image equivalence: {equivalent}.",
            f"Unresolved layout issues on any inspected page, including optional pages: {open_issues}.",""]
        text += geometry_lines
        for v in matching:
            method=v.get("review_method") or "direct inspection"
            text.append(f"- Page {v['pdf_page']}: {v.get('result','unclassified')}. Evidence: {method}. {v.get('findings','')}")
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
            source_link_counts_match=r.get("source_link_counts_match",False),visual_pages_viewed=" ".join(map(str,direct)),
            visual_pages_equivalent=" ".join(map(str,equivalent)),visual_pages_covered=" ".join(map(str,inspected)),
            visual_open_layout_issues=" ".join(map(str,open_issues)),
            individual_link_targets_match=r.get("link_targets_match_source_pages",False),
            compiled_pdf_hash_matches=phash==r.get("pdf_sha256"),
            marginal_notes_same_page=r.get("margin_notes_stay_with_anchors",False),
            marginal_overlap_candidates=len(r.get("margin_overlap_candidates",[])),
            vector_paths=r.get("vector_paths",""),images=r.get("images",""),
            graphic_geometry_flags=sum(len(r.get(f,[])) for f in ("vector_paths_outside_sheet","vector_paths_outside_permitted_area","images_outside_sheet","images_outside_permitted_area")),
            geometry_flag_groups=geometry_groups,geometry_dispositioned_groups=geometry_groups-geometry_pending,
            geometry_pending_groups=geometry_pending,
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
    seal_reports(report_inputs)
    print(f"Summarized {len(summaries)} checked-input PDF build reports; visual inspection status remains explicit.")


if __name__=="__main__":main()
