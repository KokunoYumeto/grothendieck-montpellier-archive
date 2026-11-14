#!/usr/bin/env python3
"""Compile, inspect logs, count PDF links, and prepare visual-review targets.

No visual review is inferred from a successful compilation or a rasterization.
The JSON/TSV reports state that the human-visible page inspection is pending.
"""
from __future__ import annotations
import argparse
import collections
from datetime import datetime, timezone
import hashlib
import math
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import fcntl

import fitz
from pypdf import PdfReader
from edition_core import write_tsv, read_tsv, sha256

EDITION=Path(__file__).resolve().parents[1]
WORKSPACE=EDITION.parent


def environment() -> dict:
    env=os.environ.copy()
    # The supplied runtime has TeX packages but lacks its normal ls-R database.
    # Avoid !! database-only lookup and use the task-local missing packages.
    local=WORKSPACE/"tex_runtime"
    if local.is_dir():
        probe=subprocess.run(["kpsewhich","-var-value=TEXMF"],capture_output=True,text=True)
        installed=[Path(s.lstrip("!")) for s in re.split(r"[{},]",probe.stdout.strip()) if s.lstrip("!")]
        roots=[local/"texmf-dist",local]+[p for p in installed if p.is_dir()]
        env["TEXMF"]="{"+",".join(str(x) for x in roots)+"}"
    return env


def sanitize(s: str) -> str:
    replacements=[(str(EDITION)+"/",""),(str(WORKSPACE/"source")+"/","EGA_V_TEXT.zip::"),
        (str(WORKSPACE/"tex_runtime")+"/","TeX-runtime/"),
        (str(WORKSPACE)+"/","workspace-input/"),(str(Path.home())+"/","runtime-user/")]
    for a,b in replacements:s=s.replace(a,b)
    s=re.sub(r"(?:[A-Za-z]:)?[/\\](?:usr|opt|etc|var)[/\\][^\s(){}<>]*[/\\]([^/\\\s(){}<>]+\.(?:sty|tex|def|cfg|fd|map|pfb|otf|lua|cnf|fmt))",r"TeX-package/\1",s)
    s=re.sub(r"(?:[A-Za-z]:)?[/\\](?:usr|opt|etc|var)[/\\][^\s(){}<>]*",r"TeX-package/[wrapped-path]",s)
    return s


def parse_log(s: str) -> dict:
    overflow=[];errors=[];missing=[];warnings=[];source="frontmatter";source_ranges=[];margin_routes=[]
    lines=s.splitlines()
    logical=[];i=0
    while i<len(lines):
        line=lines[i];n=i+1
        # TeX wraps the source line number itself at its log width, e.g.
        # reader.tex:61 followed by 84: Missing $ inserted.
        if re.search(r"\.tex:\d*$",line) and i+1<len(lines) and re.match(r"\d+: ",lines[i+1]):
            line+=lines[i+1];i+=1
        logical.append((n,line));i+=1
    for n,line in logical:
        m=re.search(r"EGA-SOURCE-BEGIN (\S+) PDF-PAGE (\d+)",line)
        if m:source=m[1];source_ranges.append(dict(key=source,start_printed_page=int(m[2])))
        m=re.search(r"EGA-SOURCE-END (\S+) PDF-PAGE (\d+)",line)
        if m and source_ranges:source_ranges[-1]["end_printed_page"]=int(m[2])
        m=re.search(r"EGA-MARGIN (\S+) (\d+) LINES (-?\d+) ROUTE (\S+)",line)
        if m:margin_routes.append(dict(key=m[1],ordinal=int(m[2]),measured_lines=int(m[3]),route=m[4],log_line=n))
        m=re.search(r"Overfull \\[hv]box \(([\d.]+)pt too (?:wide|high)\)",line)
        if m:overflow.append(dict(key=source,log_line=n,excess_pt=float(m[1]),message=line))
        if line.startswith("!") or re.search(r"\.tex:\d+: (?:LaTeX Error|Package .* Error|Undefined control|Missing |Extra |Too many|Illegal |Misplaced |You can't)",line):
            errors.append(dict(key=source,log_line=n,message=line))
        if "Missing character:" in line:missing.append(dict(key=source,log_line=n,message=line))
        if "Warning:" in line or line.startswith("warning  "):warnings.append(dict(key=source,log_line=n,message=line))
        if "Fatal error occurred" in line and not errors:
            errors.append(dict(key=source,log_line=n,message=line))
    return dict(overfull_boxes=overflow,latex_errors=errors,missing_characters=missing,warnings=warnings,source_ranges=source_ranges,
        margin_content_routes=margin_routes,
        margin_three_line_limit_passed=all(r["route"]!="margin" or 0<=r["measured_lines"]<=3 for r in margin_routes))


def mechanical_gates(report: dict) -> bool:
    return not any([
        report.get("latex_errors"), report.get("missing_characters"),
        any(x["excess_pt"]>2 for x in report.get("overfull_boxes",[])),
        report.get("text_outside_sheet"), not report.get("source_link_counts_match",False),
        not report.get("reader_matches_build_manifest",False),
        not report.get("source_unchanged_during_compile",False),
        not report.get("link_targets_match_source_pages",False),
        not report.get("margin_notes_stay_with_anchors",False),
        not report.get("margin_content_counts_match",False),
        not report.get("margin_three_line_limit_passed",False)])


def inspect_pdf(path: Path) -> dict:
    doc=fitz.open(path)
    reader=PdfReader(path)
    destinations=reader.named_destinations
    markcounts=collections.Counter()
    sourcepages={}
    logical_destinations=[]
    for name,dest in destinations.items():
        if name.startswith("egamark:"):
            markcounts[name.split(":")[1]]+=1
            logical_destinations.append((name,dest))
        if name.startswith("source:"):
            key=name.split(":",1)[1].split(".")[0]
            sourcepages[key]=reader.get_destination_page_number(dest)+1
    uris=collections.Counter();annotation_count=0;links=[];outside_sheet=[];outside_type=[];landscape=[]
    vectors_outside_sheet=[];vectors_outside_type=[];images_outside_sheet=[];images_outside_type=[]
    vector_count=0;image_count=0;margin_overlaps=[]
    annotation_pages={}
    mm=72/25.4
    for pno,page in enumerate(doc,1):
        if page.rect.width>page.rect.height:landscape.append(pno)
        # Text, paths and image bounds use unrotated page coordinates in PyMuPDF.
        # Transform all of them, and the permitted area, to the displayed sheet.
        unrotated=page.rect*page.derotation_matrix
        permitted=fitz.Rect(21*mm,12*mm,unrotated.width-9*mm,unrotated.height-10*mm)
        permitted=permitted*page.rotation_matrix
        def outside(box,limit,tolerance=0):
            return (box.x0<limit.x0-tolerance or box.y0<limit.y0-tolerance or
                box.x1>limit.x1+tolerance or box.y1>limit.y1+tolerance)
        page_links=page.get_links()
        annotation_pages[pno]=page_links
        for link in page_links:
            annotation_count+=1
            uri=link.get("uri","")
            if uri:
                uris[uri]+=1
                links.append(dict(pdf_page=pno,uri=uri,rectangle=list(link["from"])))
        # Text geometry is an automated screen, not a replacement for viewing.
        # The area includes header/footer and the expressly required note margin.
        margin_lines=[]
        for block in page.get_text("dict")["blocks"]:
            if "lines" not in block:continue
            for line in block["lines"]:
                marginal=[s for s in line["spans"] if s["text"].strip()
                          and s["bbox"][0] >= unrotated.width-40*mm]
                if marginal:
                    margin_lines.append(dict(text="".join(s["text"] for s in marginal),
                        box=fitz.Rect(min(s["bbox"][0] for s in marginal),min(s["bbox"][1] for s in marginal),
                                      max(s["bbox"][2] for s in marginal),max(s["bbox"][3] for s in marginal)),
                        baseline=sum(s["origin"][1] for s in marginal)/len(marginal),
                        size=min(s["size"] for s in marginal)))
                for span in line["spans"]:
                    text=span["text"]
                    if not text.strip():continue
                    box=fitz.Rect(span["bbox"])*page.rotation_matrix
                    if outside(box,page.rect,.5):
                        outside_sheet.append(dict(pdf_page=pno,text=text,rectangle=list(box)))
                    # Two points screen normal glyph side bearings; every flag
                    # still requires visual inspection, including landscape pages.
                    text_area=fitz.Rect(permitted.x0-2,permitted.y0,permitted.x1+2,permitted.y1)
                    if outside(box,text_area):
                        outside_type.append(dict(pdf_page=pno,text=text,rectangle=list(box)))
        for index,first in enumerate(margin_lines):
            for second in margin_lines[index+1:]:
                a,b=first["box"],second["box"]
                distance=abs(first["baseline"]-second["baseline"])
                overlap=min(a.x1,b.x1)-max(a.x0,b.x0)
                if overlap>2 and distance<.4*min(first["size"],second["size"]):
                    margin_overlaps.append(dict(pdf_page=pno,first_text=first["text"],second_text=second["text"],
                        baseline_distance_pt=round(distance,5),first_rectangle=list(a),second_rectangle=list(b)))
        for index,drawing in enumerate(page.get_drawings()):
            kind=drawing.get("type","")
            stroke=("s" in kind and drawing.get("color") is not None and drawing.get("stroke_opacity",1)>0)
            fill=("f" in kind and drawing.get("fill") is not None and drawing.get("fill_opacity",1)>0)
            if not (stroke or fill):continue
            vector_count+=1
            box=fitz.Rect(drawing["rect"])
            width=float(drawing.get("width") or 0)
            if stroke and width:
                half=width/2
                caps=drawing.get("lineCap",(0,0,0))
                caps=(caps,) if isinstance(caps,(int,float)) else caps
                capped=any(c!=0 for c in caps)
                # Butt-ended horizontal/vertical rules extend only in their
                # normal direction; expanding their endpoints would flag every
                # correctly placed header rule as a false overhang.
                dx=half if box.height>0.0001 or capped else 0
                dy=half if box.width>0.0001 or capped else 0
                box=fitz.Rect(box.x0-dx,box.y0-dy,box.x1+dx,box.y1+dy)
            box=box*page.rotation_matrix
            row=dict(pdf_page=pno,drawing_index=index,sequence=drawing.get("seqno"),
                path_type=kind,stroke_width_pt=width,rectangle=list(box))
            if outside(box,page.rect,.05):vectors_outside_sheet.append(row)
            if outside(box,permitted,.05):vectors_outside_type.append(row)
        for index,info in enumerate(page.get_image_info(xrefs=True)):
            image_count+=1
            box=fitz.Rect(info["bbox"])*page.rotation_matrix
            row=dict(pdf_page=pno,image_index=index,xref=info.get("xref",0),rectangle=list(box))
            if outside(box,page.rect,.05):images_outside_sheet.append(row)
            if outside(box,permitted,.05):images_outside_type.append(row)
    archive={u:c for u,c in uris.items() if "grothendieck.umontpellier.fr/web/viewer.html" in u}
    bycote=collections.defaultdict(set)
    for u in archive:
        m=re.search(r"file=\.\./(\d+)\.pdf#page=(\d+)",u)
        if m:bycote[m[1]].add(int(m[2]))
    target_audit=[]
    for name,dest in logical_destinations:
        parts=name.split(":")
        page_no=reader.get_destination_page_number(dest)+1
        label=parts[2] if len(parts)>=4 else ""
        match=re.fullmatch(r"(\d+)/(\d+)",label)
        if not match:
            target_audit.append(dict(destination=name,pdf_page=page_no,archive_page=label,
                result="legacy target has no encoded source page"))
            continue
        cote,site=match.groups()
        expected_uri=f"https://grothendieck.umontpellier.fr/web/viewer.html?file=../{cote}.pdf#page={int(site)+1}"
        page=doc[page_no-1]
        point=fitz.Point(float(dest.left),page.mediabox.height-float(dest.top))*page.rotation_matrix
        candidates=[]
        for annotation in annotation_pages[page_no]:
            if annotation.get("uri")!=expected_uri:continue
            box=annotation["from"]
            distance=math.hypot(max(box.x0-point.x,0,point.x-box.x1),
                                max(box.y0-point.y,0,point.y-box.y1))
            candidates.append(distance)
        nearest=min(candidates,default=float("inf"))
        # The zero-width destination can precede a math strut or a paragraph
        # break. Twelve points cover one normal baseline; the named destination
        # and URI also carry the exact same source-page identifier.
        target_audit.append(dict(destination=name,pdf_page=page_no,archive_page=label,
            expected_uri=expected_uri,nearest_matching_annotation_pt=round(nearest,5) if math.isfinite(nearest) else "",
            result="matching source-page link" if nearest<=12 else "missing nearby source-page link"))
    margin_anchors={name.split(":",1)[1]:reader.get_destination_page_number(dest)+1
                    for name,dest in destinations.items() if name.startswith("marginanchor:")}
    margin_notes={name.split(":",1)[1]:reader.get_destination_page_number(dest)+1
                  for name,dest in destinations.items() if name.startswith("marginnote:")}
    margin_pages=[dict(margin_id=identity,anchor_pdf_page=margin_anchors.get(identity),
                      note_pdf_page=margin_notes.get(identity),
                      same_page=margin_anchors.get(identity)==margin_notes.get(identity))
                  for identity in sorted(set(margin_anchors)|set(margin_notes))]
    return dict(pdf_pages=len(doc),link_annotations=annotation_count,archive_link_annotations=sum(archive.values()),
        logical_link_marks=dict(markcounts),distinct_archive_pages={k:len(v) for k,v in bycote.items()},
        archive_page_numbers={k:sorted(v) for k,v in bycote.items()},source_physical_pages=sourcepages,
        text_outside_sheet=outside_sheet,text_outside_permitted_area=outside_type,landscape_pages=landscape,
        vector_paths=vector_count,images=image_count,vector_paths_outside_sheet=vectors_outside_sheet,
        vector_paths_outside_permitted_area=vectors_outside_type,images_outside_sheet=images_outside_sheet,
        images_outside_permitted_area=images_outside_type,margin_overlap_candidates=margin_overlaps,
        margin_note_page_audit=margin_pages,margin_notes_stay_with_anchors=all(r["same_page"] for r in margin_pages),
        graphics_geometry_note="Path and image rectangles are conservative flags, not findings of visible ink outside the area. Clipping and path bounding boxes require visual assessment.",
        link_target_audit=target_audit,
        link_targets_match_source_pages=all(r["result"]=="matching source-page link" for r in target_audit),
        visual_review="not performed by this script",links=links)


def compile_one(source: Path, args) -> dict:
    name=source.stem
    # A reviewer may be inspecting this exact PDF in another task. Its bytes
    # must remain stable until the freeze is explicitly released for repair.
    freezes=EDITION/"records/PDF_REVIEW_FREEZES.tsv"
    if freezes.is_file() and any(r["reader"]==name and r["status"]=="active" for r in read_tsv(freezes)):
        raise SystemExit("Reader is frozen for visual review; release its freeze with pdf_review.py before recompiling: "+name)
    buildbase=EDITION/"development/build" if "development" in source.parts else EDITION/"build"
    out=buildbase/name;out.mkdir(parents=True,exist_ok=True)
    reportdir=out/"audit";reportdir.mkdir(exist_ok=True)
    # Raw TeX logs never enter documentary/checkpoint directories. Compile an
    # immutable source snapshot privately, then publish sanitized log copies.
    stage=WORKSPACE/"tex_runtime/compile_work"/name
    stage.mkdir(parents=True,exist_ok=True)
    compile_lock=(stage/"compile.lock").open("a")
    try:
        fcntl.flock(compile_lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except BlockingIOError:
        raise SystemExit("A compilation of this reader is already running: "+name)
    source_snapshot=source.read_text()
    staged_source=stage/(name+".tex")
    staged_source.write_text(source_snapshot)
    priorpath=reportdir/"report.json"
    prior=json.loads(priorpath.read_text()) if priorpath.is_file() else {}
    env=environment()
    fmt=WORKSPACE/"tex_runtime/formats/lualatex.fmt"
    if not fmt.is_file():fmt=EDITION/"build/lualatex.fmt"
    cmd=["lualatex"]
    if fmt.is_file():cmd.append("-fmt="+str(fmt))
    cmd += ["-interaction=nonstopmode","-halt-on-error","-file-line-error","-output-directory="+str(stage),str(staged_source)]
    codes=[]
    for run in range(1,args.passes+1):
        proc=subprocess.run(cmd,cwd=WORKSPACE,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        codes.append(proc.returncode)
        stdout=sanitize(proc.stdout)
        (out/f"pass_{run}.stdout.txt").write_text(stdout)
        rawlog=stage/(name+".log")
        if rawlog.is_file():
            s=sanitize(rawlog.read_text(errors="replace"))
            (out/(name+".log")).write_text(s)
            (out/f"pass_{run}.log").write_text(s)
        if proc.returncode:break
    logpath=out/(name+".log")
    log=parse_log(logpath.read_text(errors="replace")) if logpath.exists() else {}
    report=dict(reader=name,source=str(source.relative_to(EDITION)),build_time_utc=datetime.now(timezone.utc).isoformat(),exit_codes=codes,**log)
    report["source_sha256"]=sha256(source_snapshot)
    report["compiler_sha256"]=sha256(Path(__file__).read_text())
    report["source_unchanged_during_compile"]=source.read_text()==source_snapshot
    overflowhistory=reportdir/"OVERFLOW_HISTORY.tsv"
    earlier=read_tsv(overflowhistory) if overflowhistory.is_file() else []
    known={(r["key"],r["excess_pt"],r["message"]) for r in earlier}
    for snapshot in (prior,report):
        for row in snapshot.get("overfull_boxes",[]):
            identity=(row["key"],str(row["excess_pt"]),row["message"])
            if identity not in known:
                earlier.append(dict(reader=name,build_time_utc=snapshot.get("build_time_utc",""),**row))
                known.add(identity)
    write_tsv(overflowhistory,earlier,["reader","build_time_utc","key","log_line","excess_pt","message"])
    pdf=out/(name+".pdf")
    staged_pdf=stage/(name+".pdf")
    if codes[-1]==0 and staged_pdf.is_file():
        temporary=out/(name+".pdf.pending")
        shutil.copyfile(staged_pdf,temporary)
        os.replace(temporary,pdf)
    if pdf.is_file() and codes[-1]==0:
        report.update(inspect_pdf(pdf))
        report["pdf_sha256"]=hashlib.sha256(pdf.read_bytes()).hexdigest()
        recordsbase=EDITION/"development/records" if "development" in source.parts else EDITION/"records"
        expectation=recordsbase/("LINK_EXPECTATIONS_"+name+".json")
        if expectation.is_file():
            expected=json.loads(expectation.read_text())
            report["source_files_sha256"]=expected.get("source_files_sha256",{})
            report["expected_reader_sha256"]=expected.get("reader_sha256","")
            report["reader_matches_build_manifest"]=(not report["expected_reader_sha256"] or
                report["expected_reader_sha256"]==report["source_sha256"])
            wanted=expected["logical_link_marks"]
            actual=report["logical_link_marks"]
            report["expected_logical_link_marks"]=wanted
            report["source_link_count_comparison"]={k:dict(expected=wanted.get(k,0),pdf=actual.get(k,0)) for k in set(wanted)|set(actual)}
            report["source_link_counts_match"]=all(v["expected"]==v["pdf"] for v in report["source_link_count_comparison"].values())
            actual_margins=collections.Counter(r["key"] for r in report.get("margin_content_routes",[]))
            expected_margins=expected.get("running_margin_content_counts",{})
            report["margin_content_count_comparison"]={k:dict(expected=expected_margins.get(k,0),measured=actual_margins.get(k,0))
                for k in set(expected_margins)|set(actual_margins)}
            report["margin_content_counts_match"]=all(r["expected"]==r["measured"] for r in report["margin_content_count_comparison"].values())
        else:
            report["source_link_counts_match"]=False
            report["source_link_count_error"]="Expected source-mark inventory is absent; regenerate this reader."
        n=report["pdf_pages"]
        samples=sorted(set(round(i*(n-1)/39)+1 for i in range(40))) if n>=40 else list(range(1,n+1))
        required=set(samples)|set(report["landscape_pages"])
        sourcepages=report["source_physical_pages"]
        ordered=sorted((v,k) for k,v in sourcepages.items())
        historicalkeys={row["key"] for row in earlier}
        if expectation.is_file():
            historicalkeys.update(expected.get("typesetting_patch_source_keys",[]))
        report["historical_overflow_source_keys"]=sorted(historicalkeys)
        # Four packed rows are the concrete boundary at which the prior 36 pt
        # estimate could admit an overlong margin note. Inspect these source
        # pages explicitly after the routing repair, even when no box overflow
        # was reported by TeX.
        margin_limit_keys={r["key"] for r in report.get("margin_content_routes",[]) if r["measured_lines"]==4}
        report["margin_line_limit_review_source_keys"]=sorted(margin_limit_keys)
        historicalkeys.update(margin_limit_keys)
        for key in historicalkeys:
            start=sourcepages.get(key)
            if start:
                following=[p for p,k in ordered if p>start]
                stop=min(following)-1 if following else n
                required.update(range(start,stop+1))
        required.update(x["pdf_page"] for x in report["text_outside_sheet"])
        required.update(x["pdf_page"] for x in report["text_outside_permitted_area"])
        for field in ("vector_paths_outside_sheet","vector_paths_outside_permitted_area",
                "images_outside_sheet","images_outside_permitted_area"):
            required.update(x["pdf_page"] for x in report[field])
        required.update(x["pdf_page"] for x in report.get("margin_overlap_candidates",[]))
        reviews=EDITION/"records/PDF_VISUAL_REVIEW.tsv"
        visual_issue_keys={r.get("source_key") for r in read_tsv(reviews)
            if r.get("reader")==name and r.get("result")=="layout issue found"} if reviews.is_file() else set()
        report["historical_visual_issue_source_keys"]=sorted(visual_issue_keys)
        for key in visual_issue_keys:
            start=sourcepages.get(key)
            if start:
                following=[p for p,k in ordered if p>start]
                stop=min(following)-1 if following else n
                required.update(range(start,stop+1))
        report["evenly_spread_sample_pages"]=samples
        report["required_visual_review_pages"]=sorted(required)
        report["mechanical_gates_passed"]=mechanical_gates(report)
    else:
        report["mechanical_gates_passed"]=False
    historyfile=reportdir/"BUILD_HISTORY.tsv"
    history=read_tsv(historyfile) if historyfile.is_file() else []
    seen={r["build_time_utc"] for r in history}
    for snapshot in (prior,report):
        stamp=snapshot.get("build_time_utc")
        if not stamp or stamp in seen:continue
        boxes=snapshot.get("overfull_boxes",[])
        history.append(dict(reader=name,build_time_utc=stamp,source_sha256=snapshot.get("source_sha256",""),pdf_sha256=snapshot.get("pdf_sha256",""),
            exit_code=snapshot.get("exit_codes",[""])[-1],pdf_pages=snapshot.get("pdf_pages",""),
            errors=len(snapshot.get("latex_errors",[])),missing_characters=len(snapshot.get("missing_characters",[])),
            overfull_boxes=len(boxes),overfull_gt_2pt=sum(x["excess_pt"]>2 for x in boxes),
            widest_pt=max((x["excess_pt"] for x in boxes),default=0),mechanical_gates_passed=snapshot.get("mechanical_gates_passed",False)))
        seen.add(stamp)
    write_tsv(historyfile,history,["reader","build_time_utc","source_sha256","pdf_sha256","exit_code","pdf_pages","errors","missing_characters","overfull_boxes","overfull_gt_2pt","widest_pt","mechanical_gates_passed"])
    (reportdir/"report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    for field in ("overfull_boxes","latex_errors","missing_characters","warnings"):
        rows=report.get(field,[])
        write_tsv(reportdir/(field+".tsv"),rows,list(rows[0]) if rows else ["key","log_line","message"])
    write_tsv(reportdir/"margin_content_routes.tsv",report.get("margin_content_routes",[]),
        ["key","ordinal","measured_lines","route","log_line"])
    if "links" in report:
        write_tsv(reportdir/"links.tsv",report["links"],["pdf_page","uri","rectangle"])
    if "link_target_audit" in report:
        write_tsv(reportdir/"link_targets.tsv",report["link_target_audit"],
            ["destination","pdf_page","archive_page","expected_uri","nearest_matching_annotation_pt","result"])
    if "margin_note_page_audit" in report:
        write_tsv(reportdir/"margin_note_pages.tsv",report["margin_note_page_audit"],
            ["margin_id","anchor_pdf_page","note_pdf_page","same_page"])
        write_tsv(reportdir/"margin_overlap_candidates.tsv",report["margin_overlap_candidates"],
            ["pdf_page","first_text","second_text","baseline_distance_pt","first_rectangle","second_rectangle"])
    print(json.dumps({"reader":name,"exit":codes[-1],"pages":report.get("pdf_pages"),
        "errors":len(report.get("latex_errors",[])),"missing":len(report.get("missing_characters",[])),
        "overfull_gt_2pt":sum(x["excess_pt"]>2 for x in report.get("overfull_boxes",[])),
        "widest_pt":max((x["excess_pt"] for x in report.get("overfull_boxes",[])),default=0),
        "links":report.get("logical_link_marks"),"distinct_archive_pages":report.get("distinct_archive_pages"),
        "source_link_counts_match":report.get("source_link_counts_match"),
        "last_error":report.get("latex_errors",[])[-1:]},ensure_ascii=False),flush=True)
    compile_lock.close()
    return report


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("files",nargs="+")
    p.add_argument("--passes",type=int,default=2)
    args=p.parse_args()
    reports=[compile_one(Path(s).resolve(),args) for s in args.files]
    if any(not r["mechanical_gates_passed"] for r in reports):raise SystemExit(1)


if __name__=="__main__":main()
