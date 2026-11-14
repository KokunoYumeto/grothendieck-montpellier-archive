#!/usr/bin/env python3
"""Publish the actual packed-line routing audit; this does not infer visual review."""
from pathlib import Path
import json
from audit_release import SPECS, calls
from edition_core import write_tsv, resolve_variants, no_comments

EDITION=Path(__file__).resolve().parents[1]

def main():
    rows=[];fixes=[];summary=[]
    for name,(family,mode) in SPECS.items():
        reportpath=EDITION/"build"/name/"audit/report.json"
        if not reportpath.is_file():continue
        report=json.loads(reportpath.read_text())
        source=EDITION/"readers"/(name+".tex")
        routes=report.get("margin_content_routes",[])
        for row in routes:
            key=row["key"]
            record=dict(reader=name,pdf_sha256=report.get("pdf_sha256",""),page_key=key,
                source_start_pdf_page=report.get("source_physical_pages",{}).get(key,""),**row)
            record["three_line_limit_passed"]=row["route"]!="margin" or 0<=row["measured_lines"]<=3
            rows.append(record)
            if row["measured_lines"]>3:
                fixes.append(dict(reader=name,page_key=key,source_line="margin ordinal "+str(row["ordinal"]),
                    issue="A height-only threshold did not prove the required three-line margin limit; one four-line source25/47 note exposed the gap.",
                    repair="Count actual packed rows at margin width; place this "+str(row["measured_lines"])+"-row note in a labeled, ruled block at its attachment in the running text.",
                    before="height-only routing; no claim that this particular note previously remained in the margin",
                    after="body block after actual "+str(row["measured_lines"])+"-row measurement",occurrences=1))
        summary.append(dict(reader=name,pdf_sha256=report.get("pdf_sha256",""),
            notes=len(routes),margin=sum(r["route"]=="margin" for r in routes),
            body=sum(r["route"]=="body" for r in routes),inline_math=sum(r["route"]=="inline-math" for r in routes),
            source_counts_match=report.get("margin_content_counts_match",False),
            three_line_limit_passed=report.get("margin_three_line_limit_passed",False)))
    write_tsv(EDITION/"records/MARGIN_LINE_AUDIT.tsv",rows,
        ["reader","pdf_sha256","page_key","source_start_pdf_page","key","ordinal","measured_lines","route","log_line","three_line_limit_passed"])
    write_tsv(EDITION/"records/MARGIN_LINE_SUMMARY.tsv",summary)
    write_tsv(EDITION/"records/TYPESETTING_FIXES_margin_line_limit.tsv",fixes,
        ["reader","page_key","source_line","issue","repair","before","after","occurrences"])
    print(json.dumps(dict(readers=len(summary),notes=len(rows),routed_to_body=len(fixes),
        all_counts_current=all(r["source_counts_match"] for r in summary),
        all_three_line_limits_passed=all(r["three_line_limit_passed"] for r in summary))))

if __name__=="__main__":main()
