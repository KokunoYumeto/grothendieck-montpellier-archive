#!/usr/bin/env python3
"""Compile, inspect logs, count PDF links, and prepare visual-review targets.

No visual review is inferred from a successful compilation or a rasterization.
The JSON/TSV reports state that the human-visible page inspection is pending.
"""
from __future__ import annotations
import argparse
import collections
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

import fitz
from pypdf import PdfReader
from edition_core import write_tsv

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
    overflow=[];errors=[];missing=[];warnings=[];source="frontmatter";source_ranges=[]
    for n,line in enumerate(s.splitlines(),1):
        m=re.search(r"EGA-SOURCE-BEGIN (\S+) PDF-PAGE (\d+)",line)
        if m:source=m[1];source_ranges.append(dict(key=source,start_printed_page=int(m[2])))
        m=re.search(r"EGA-SOURCE-END (\S+) PDF-PAGE (\d+)",line)
        if m and source_ranges:source_ranges[-1]["end_printed_page"]=int(m[2])
        m=re.search(r"Overfull \\[hv]box \(([\d.]+)pt too (?:wide|high)\)",line)
        if m:overflow.append(dict(key=source,log_line=n,excess_pt=float(m[1]),message=line))
        if line.startswith("!") or re.search(r"\.tex:\d+: (?:LaTeX Error|Package .* Error|Undefined control|Missing |Extra |Too many|Illegal |Misplaced |You can't)",line):
            errors.append(dict(key=source,log_line=n,message=line))
        if "Missing character:" in line:missing.append(dict(key=source,log_line=n,message=line))
        if "Warning:" in line or line.startswith("warning  "):warnings.append(dict(key=source,log_line=n,message=line))
    return dict(overfull_boxes=overflow,latex_errors=errors,missing_characters=missing,warnings=warnings,source_ranges=source_ranges)


def inspect_pdf(path: Path) -> dict:
    doc=fitz.open(path)
    reader=PdfReader(path)
    destinations=reader.named_destinations
    markcounts=collections.Counter()
    sourcepages={}
    for name,dest in destinations.items():
        if name.startswith("egamark:"):
            markcounts[name.split(":")[1]]+=1
        if name.startswith("source:"):
            key=name.split(":",1)[1].split(".")[0]
            sourcepages[key]=reader.get_destination_page_number(dest)+1
    uris=collections.Counter();annotation_count=0;links=[];outside_sheet=[];outside_type=[];landscape=[]
    mm=72/25.4
    for pno,page in enumerate(doc,1):
        if page.rect.width>page.rect.height:landscape.append(pno)
        for link in page.get_links():
            annotation_count+=1
            uri=link.get("uri","")
            if uri:
                uris[uri]+=1
                links.append(dict(pdf_page=pno,uri=uri,rectangle=list(link["from"])))
        # Text geometry is an automated screen, not a replacement for viewing.
        # The area includes header/footer and the expressly required note margin.
        for block in page.get_text("dict")["blocks"]:
            if "lines" not in block:continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text=span["text"]
                    if not text.strip():continue
                    box=fitz.Rect(span["bbox"])
                    if box.x0<-.5 or box.y0<-.5 or box.x1>page.rect.width+.5 or box.y1>page.rect.height+.5:
                        outside_sheet.append(dict(pdf_page=pno,text=text,rectangle=list(box)))
                    if page.rect.width<page.rect.height:
                        # Two points allow a single glyph's normal side bearing;
                        # every flagged item still needs visual inspection.
                        if box.x0<21*mm-2 or box.x1>201*mm+2 or box.y0<12*mm or box.y1>287*mm:
                            outside_type.append(dict(pdf_page=pno,text=text,rectangle=list(box)))
    archive={u:c for u,c in uris.items() if "grothendieck.umontpellier.fr/web/viewer.html" in u}
    bycote=collections.defaultdict(set)
    for u in archive:
        m=re.search(r"file=\.\./(\d+)\.pdf#page=(\d+)",u)
        if m:bycote[m[1]].add(int(m[2]))
    return dict(pdf_pages=len(doc),link_annotations=annotation_count,archive_link_annotations=sum(archive.values()),
        logical_link_marks=dict(markcounts),distinct_archive_pages={k:len(v) for k,v in bycote.items()},
        archive_page_numbers={k:sorted(v) for k,v in bycote.items()},source_physical_pages=sourcepages,
        text_outside_sheet=outside_sheet,text_outside_permitted_area=outside_type,landscape_pages=landscape,
        visual_review="not performed by this script",links=links)


def compile_one(source: Path, args) -> dict:
    name=source.stem
    buildbase=EDITION/"development/build" if "development" in source.parts else EDITION/"build"
    out=buildbase/name;out.mkdir(parents=True,exist_ok=True)
    reportdir=out/"audit";reportdir.mkdir(exist_ok=True)
    env=environment()
    fmt=WORKSPACE/"tex_runtime/formats/lualatex.fmt"
    if not fmt.is_file():fmt=EDITION/"build/lualatex.fmt"
    cmd=["lualatex"]
    if fmt.is_file():cmd.append("-fmt="+str(fmt))
    cmd += ["-interaction=nonstopmode","-halt-on-error","-file-line-error","-output-directory="+str(out),str(source)]
    codes=[]
    for run in range(1,args.passes+1):
        proc=subprocess.run(cmd,cwd=WORKSPACE,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        codes.append(proc.returncode)
        stdout=sanitize(proc.stdout)
        (out/f"pass_{run}.stdout.txt").write_text(stdout)
        logpath=out/(name+".log")
        if logpath.is_file():
            s=sanitize(logpath.read_text(errors="replace"))
            logpath.write_text(s)
            (out/f"pass_{run}.log").write_text(s)
        if proc.returncode:break
    logpath=out/(name+".log")
    log=parse_log(logpath.read_text(errors="replace")) if logpath.exists() else {}
    report=dict(reader=name,source=str(source.relative_to(EDITION)),build_time_utc=datetime.now(timezone.utc).isoformat(),exit_codes=codes,**log)
    pdf=out/(name+".pdf")
    if pdf.is_file() and codes[-1]==0:
        report.update(inspect_pdf(pdf))
        n=report["pdf_pages"]
        samples=sorted(set(round(i*(n-1)/39)+1 for i in range(40))) if n>=40 else list(range(1,n+1))
        required=set(samples)|set(report["landscape_pages"])
        sourcepages=report["source_physical_pages"]
        ordered=sorted((v,k) for k,v in sourcepages.items())
        for over in report["overfull_boxes"]:
            start=sourcepages.get(over["key"])
            if start:
                following=[p for p,k in ordered if p>start]
                stop=min(following)-1 if following else n
                required.update(range(start,stop+1))
        required.update(x["pdf_page"] for x in report["text_outside_sheet"])
        required.update(x["pdf_page"] for x in report["text_outside_permitted_area"])
        report["evenly_spread_sample_pages"]=samples
        report["required_visual_review_pages"]=sorted(required)
        report["mechanical_gates_passed"]=not any([
            report["latex_errors"],report["missing_characters"],
            any(x["excess_pt"]>2 for x in report["overfull_boxes"]),report["text_outside_sheet"]])
    else:
        report["mechanical_gates_passed"]=False
    (reportdir/"report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    for field in ("overfull_boxes","latex_errors","missing_characters","warnings"):
        rows=report.get(field,[])
        write_tsv(reportdir/(field+".tsv"),rows,list(rows[0]) if rows else ["key","log_line","message"])
    if "links" in report:
        write_tsv(reportdir/"links.tsv",report["links"],["pdf_page","uri","rectangle"])
    print(json.dumps({"reader":name,"exit":codes[-1],"pages":report.get("pdf_pages"),
        "errors":len(report.get("latex_errors",[])),"missing":len(report.get("missing_characters",[])),
        "overfull_gt_2pt":sum(x["excess_pt"]>2 for x in report.get("overfull_boxes",[])),
        "widest_pt":max((x["excess_pt"] for x in report.get("overfull_boxes",[])),default=0),
        "links":report.get("logical_link_marks"),"distinct_archive_pages":report.get("distinct_archive_pages"),
        "last_error":report.get("latex_errors",[])[-1:]},ensure_ascii=False),flush=True)
    return report


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("files",nargs="+")
    p.add_argument("--passes",type=int,default=2)
    args=p.parse_args()
    reports=[compile_one(Path(s).resolve(),args) for s in args.files]
    if any(not r["mechanical_gates_passed"] for r in reports):raise SystemExit(1)


if __name__=="__main__":main()
