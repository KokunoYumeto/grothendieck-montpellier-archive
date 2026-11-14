#!/usr/bin/env python3
"""Check final edition gates without editing sources or inferring visual review.

The report is always written. A nonzero exit means the release remains blocked;
--report-only changes only that exit behavior for working checkpoints.
"""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import re
import fitz
from build_readers import EDITION,PAGES,PAGE_MAP,validate_translation
from edition_core import (read_tsv,write_tsv,sha256,cleanup_page,annotate_page,
    apply_variant_overrides,resolve_variants,group_at,tex_escape,mark_counts)
from edition_render import CREDIT,RIGHTS_EN,RIGHTS_FR,order_keys
from visual_evidence import verify_visual_record
from build_report_provenance import verify_reports

SPECS={
 "EGA_V_FR_diplomatique":("fr",0),
 "EGA_V_FR_corrige_apparat":("fr",1),
 "EGA_V_FR_texte_de_lecture":("fr",2),
 "EGA_V_FR_master_annotated":("fr",1),
 "EGA_V_EN_corrected_translator_notes":("en",1),
 "EGA_V_EN_reading":("en",2),
 "EGA_V_EN_master_annotated":("en",1),
 "EGA_V24_EN_diplomatic":("blass",0),
 "EGA_V24_EN_corrected_apparatus":("blass",1),
 "EGA_V24_EN_reading":("blass",2),
 "EGA_V24_EN_master_annotated":("blass",1),
 "EGA_V_GUIDE":("guide",2),
}
PRIVATE={
 "email":re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}"),
 # A TeX expression such as g:\underline{Y}, or prose ending in
 # Then:\var, is not a Windows file path. Require path components.
 "absolute path":re.compile(r"/(?:workspace|home|tmp|mnt|usr|opt|etc|var|Users|data)/|(?<![\w])[A-Za-z]:\\(?:[^\\\s{}$]+\\)+[^\\\s{}$]+"),
}


def filehash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def public_error(exc):
    return str(exc).replace(str(EDITION)+"/","").replace(str(EDITION.parent)+"/","workspace-input/")


def calls(text,name,nargs):
    found=[]
    for match in re.finditer(r"(?m)^"+re.escape("\\"+name)+"\\{",text):
        pos=match.start()+len(name)+1
        args=[]
        for _ in range(nargs):
            while text[pos].isspace():pos+=1
            arg,pos=group_at(text,pos)
            args.append(arg)
        found.append(args)
    return found


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report-only",action="store_true")
    args=parser.parse_args()
    gates=[]
    def gate(name,ok,detail):
        gates.append(dict(gate=name,passed=bool(ok),detail=detail))
    def read(path):
        return read_tsv(path) if path.is_file() else []

    expected={r["key"] for r in PAGES}
    checked={p.stem for p in (EDITION/"checked_pages").glob("*.tex")}
    page_rows=read(EDITION/"PAGES_CHECKED.tsv")
    certified={r["key"] for r in page_rows}
    decisions=read(EDITION/"CHECK_DECISIONS.tsv")
    decision_counts=Counter(r["key"] for r in decisions)
    gate("checked-page coverage",checked==expected,dict(expected=len(expected),present=len(checked),
        missing=sorted(expected-checked),extra=sorted(checked-expected)))
    gate("page-review coverage",certified==expected and len(page_rows)==len(expected),
        dict(expected=len(expected),records=len(page_rows),missing=sorted(expected-certified)))
    bad_counts=[r["key"] for r in page_rows
        if int(r.get("number_of_decisions","0"))!=decision_counts[r["key"]]
        or int(r.get("lines_read","0"))<1 or not r.get("start_time") or not r.get("end_time")]
    gate("page-review record consistency",not bad_counts,bad_counts)
    decision_ids=[r["id"] for r in decisions]
    gate("unique decision IDs",len(decision_ids)==len(set(decision_ids)),len(decision_ids))
    notes_summary=EDITION/"records/NOTES_COVERAGE_SUMMARY.json"
    notes_issues=[]
    if notes_summary.is_file():
        notes=json.loads(notes_summary.read_text())
        if notes.get("source_pages")!=260 or notes.get("reviewer_mapping_required") or notes.get("invalid_reviewed_mappings"):
            notes_issues.append("One or more NOTES concerns need a valid documentary crosswalk.")
        if notes.get("decisions_sha256")!=sha256((EDITION/"CHECK_DECISIONS.tsv").read_text()):
            notes_issues.append("NOTES inventory predates the current scan decisions.")
        for relative,digest in notes.get("source_notes_sha256",{}).items():
            if sha256((EDITION.parent/"source"/relative).read_text())!=digest:
                notes_issues.append("Supplied NOTES hash differs: "+relative)
        reviewed=EDITION/"records/NOTES_CROSSWALK_REVIEWED.tsv"
        actual=sha256(reviewed.read_text()) if reviewed.is_file() else ""
        if notes.get("reviewed_mappings_sha256")!=actual:
            notes_issues.append("NOTES inventory predates the current reviewed mappings.")
    else:
        notes_issues.append("NOTES coverage inventory is absent.")
    gate("NOTES concern documentary coverage",not notes_issues,notes_issues)

    overrides=read(EDITION/"records/VARIANT_OVERRIDES.tsv")
    source_checks=[];source_counts=[]
    for record in PAGES:
        key=record["key"];path=EDITION/"checked_pages"/(key+".tex")
        if not path.is_file():continue
        try:
            original=path.read_text()
            family="fr" if record["cote"]=="25" else "blass"
            cleaned,fixes=cleanup_page(original,key)
            annotated,variants=annotate_page(cleaned,key)
            annotated=apply_variant_overrides(annotated,variants,[r for r in overrides if r["key"]==key])
            if key=="ega25_25_022":
                from author_restorations import restore_45_at_51
                annotated,variants=restore_45_at_51(annotated,variants,EDITION,PAGE_MAP,write_records=False)
            actual=(EDITION/"master_pages"/family/(key+".tex")).read_text()
            metadata=json.loads((EDITION/"variant_records"/(key+".json")).read_text())
            issues=[]
            if actual!=annotated:issues.append("annotated master is not current")
            expected_metadata=[v.as_record() for v in variants]
            if key=="ega25_25_021":
                from author_restorations import donor_restoration_metadata
                expected_metadata=donor_restoration_metadata(expected_metadata)
            if metadata!=expected_metadata:issues.append("variant metadata is not current")
            if resolve_variants(actual,0)!=cleaned:issues.append("diplomatic reconstruction differs")
            if re.findall(r"\\scanpage\{([^}]+)\}",cleaned)!=[record["cote"]+"/"+str(int(record["site"]))]:
                issues.append("source scan marker differs")
            if "not yet checked by eye" in original:issues.append("obsolete unreviewed header remains")
            source_checks.append(dict(key=key,passed=not issues,issues=issues,
                checked_sha256=sha256(original),cleaned_sha256=sha256(cleaned),
                annotated_sha256=sha256(actual),variants=len(variants),cleanup_actions=len(fixes)))
            supplied=(EDITION.parent/"source"/record["page_file"]).read_text()
            before=mark_counts(supplied);after=mark_counts(original)
            source_counts.append(dict(key=key,cote=record["cote"],site=record["site"],
                **{"before_"+k:v for k,v in before.items()},**{"after_"+k:v for k,v in after.items()}))
        except Exception as exc:
            source_checks.append(dict(key=key,passed=False,issues=[public_error(exc)]))
    gate("checked-source reconstruction",len(source_checks)==260 and all(r["passed"] for r in source_checks),
        [r for r in source_checks if not r["passed"]])
    write_tsv(EDITION/"records/SOURCE_MARK_COUNTS.tsv",source_counts)

    translation_rows={r["key"]:r for r in read(EDITION/"records/EN_TRANSLATION_STATUS.tsv")}
    translation_checks=[]
    for record in PAGES:
        if record["cote"]!="25":continue
        key=record["key"]
        try:
            french=(EDITION/"master_pages/fr"/(key+".tex")).read_text()
            english=(EDITION/"master_pages/en"/(key+".tex")).read_text()
            checked_text=(EDITION/"checked_pages"/(key+".tex")).read_text()
            audit=validate_translation(key,french,english)
            ledger=translation_rows.get(key,{})
            hashes=dict(french_master_sha256=sha256(french),english_master_sha256=sha256(english),
                        checked_page_sha256=sha256(checked_text))
            current=all(ledger.get(k)==v for k,v in hashes.items())
            translation_checks.append(dict(audit,passed=current,
                issues=[] if current else ["translation ledger is absent or stale"]))
        except Exception as exc:
            translation_checks.append(dict(key=key,passed=False,issues=[public_error(exc)]))
    gate("English translation coverage and fidelity",all(r["passed"] for r in translation_checks),
        [r for r in translation_checks if not r["passed"]])

    visual=read(EDITION/"records/PDF_VISUAL_REVIEW.tsv")
    equivalences=read(EDITION/"records/PDF_VISUAL_EQUIVALENCE.tsv")
    freezes=read(EDITION/"records/PDF_REVIEW_FREEZES.tsv")
    image_hash_cache={}
    geometry=read(EDITION/"records/PDF_GEOMETRY_REVIEW.tsv")
    scales=read(EDITION/"records/LOCAL_DIAGRAM_SCALE_AUDIT.tsv")
    canonical={}
    for family in ("fr","en","blass"):
        master=next(name for name,(fam,_) in SPECS.items() if fam==family and "master_annotated" in name)
        path=EDITION/"readers"/(master+".tex")
        if path.is_file():
            canonical[family]={row[0]:sha256(json.dumps(row[1:],ensure_ascii=False)) for row in calls(path.read_text(),"RegisterPage",3)}
    reader_checks=[]
    for name,(family,mode) in SPECS.items():
        source=EDITION/"readers"/(name+".tex")
        pdf=EDITION/"build"/name/(name+".pdf")
        report_path=pdf.parent/"audit/report.json"
        issues=[];required=[];pending=[];geometry_pending=[]
        if not source.is_file() or not pdf.is_file() or not report_path.is_file():
            issues.append("source, PDF or compile report missing")
        else:
            body=source.read_text();report=json.loads(report_path.read_text());phash=filehash(pdf)
            if report.get("source_sha256")!=sha256(body):issues.append("reader changed since compilation")
            if report.get("pdf_sha256")!=phash:issues.append("compiled PDF hash is absent or differs")
            inputs=report.get("source_files_sha256",{})
            stale=[rel for rel,digest in inputs.items() if not (EDITION/rel).is_file()
                   or sha256((EDITION/rel).read_text())!=digest]
            if not inputs or stale:issues.append("source inputs or rendering configuration are stale")
            if report.get("latex_errors") or report.get("missing_characters"):issues.append("LaTeX errors or missing glyphs")
            if any(x["excess_pt"]>2 for x in report.get("overfull_boxes",[])):issues.append("overfull box exceeds2pt")
            if not report.get("mechanical_gates_passed"):issues.append("mechanical compile gates failed")
            if not report.get("source_link_counts_match"):issues.append("source/PDF link counts differ")
            if not report.get("link_targets_match_source_pages"):issues.append("individual archive link targets are unverified")
            if not report.get("margin_notes_stay_with_anchors"):issues.append("marginal notes have no verified same-page anchors")
            if not report.get("margin_three_line_limit_passed") or not report.get("margin_content_counts_match"):
                issues.append("actual marginal-note line counts or their source coverage are unverified")
            if re.search(r"INCOMPLETE CHECKPOINT|UNCHECKED DEVELOPMENT BUILD|not yet checked by eye",body):
                issues.append("working or obsolete unchecked label remains")
            if re.search(r"\\hfuzz\s*(?:=|\{)",body):issues.append("hfuzz override is forbidden")
            for label,statement in (("credit",CREDIT),("English rights",RIGHTS_EN)):
                if tex_escape(statement) not in body:issues.append(label+" statement missing or changed")
            if family=="fr" and tex_escape(RIGHTS_FR) not in body:issues.append("French rights statement missing or changed")
            if family=="en" and "AI-translated by GPT-6 Astra (OpenAI, ChatGPT Pro mode)" not in body:
                issues.append("translation credit absent")
            if family in ("blass","guide") and "The translation in cote 24 is Piotr Blass's (1987); the rights in it belong to its translator or his heirs." not in body:
                issues.append("Blass rights statement missing or changed")
            if family!="guide":
                allkeys=[r["key"] for r in PAGES if r["cote"]==("24" if family=="blass" else "25")]
                expected_order=order_keys(allkeys,family,mode)
                printed=calls(body,"PrintPage",3)
                if [r[0] for r in printed]!=expected_order:issues.append("printed page coverage or order differs")
                registered={r[0]:sha256(json.dumps(r[1:],ensure_ascii=False)) for r in calls(body,"RegisterPage",3)}
                if set(registered)!=set(allkeys) or registered!=canonical.get(family):
                    issues.append("common annotated page data differs from its master")
                if set(report.get("source_physical_pages",{}))!=set(expected_order):
                    issues.append("PDF source-page destinations differ")
                for key,label,url in printed:
                    if label!=PAGE_MAP[key]["cote"]+"/"+str(int(PAGE_MAP[key]["site"])) or url.replace(r"\#","#")!=PAGE_MAP[key]["viewer"]:
                        issues.append("printed scan URL or label differs: "+key)
                cote="24" if family=="blass" else "25"
                pages=sorted(int(PAGE_MAP[k]["pdf_page"]) for k in expected_order)
                if report.get("archive_page_numbers",{}).get(cote)!=pages:issues.append("distinct archive-page URLs differ")
            required=report.get("required_visual_review_pages",[])
            latest_visual={int(r["pdf_page"]):r for r in visual
                           if r.get("reader")==name and r.get("pdf_sha256")==phash}
            open_layout_issues=sorted(page for page,r in latest_visual.items() if r.get("result")=="layout issue found")
            if open_layout_issues:issues.append("current PDF has unresolved inspected layout issues on pages "+", ".join(map(str,open_layout_issues)))
            inspected=set()
            for page,r in latest_visual.items():
                if r.get("result")!="layout inspection passed" or not r.get("findings"):continue
                evidence_issues=verify_visual_record(r,visual,equivalences,freezes,image_hash_cache)
                if evidence_issues:issues.append("PDF page "+str(page)+": "+"; ".join(evidence_issues))
                else:inspected.add(page)
            pending=sorted(set(required)-inspected)
            if pending:issues.append("required visual inspections pending")
            for field in ("text_outside_sheet","text_outside_permitted_area","vector_paths_outside_sheet",
                          "vector_paths_outside_permitted_area","images_outside_sheet","images_outside_permitted_area"):
                for flag in report.get(field,[]):
                    permitted={"single-letter-overhang"} if field=="text_outside_permitted_area" else {"conservative-rectangle-no-visible-overflow"}
                    resolved=any(r.get("reader")==name and r.get("pdf_sha256")==phash
                        and int(r.get("pdf_page","0"))==flag["pdf_page"] and r.get("flag_kind")==field
                        and r.get("decision") in permitted and r.get("reason") for r in geometry)
                    if not resolved:geometry_pending.append(dict(kind=field,**flag))
            if geometry_pending:issues.append("geometry flags require explicit visual disposition")
            if family=="blass":
                matched=[r for r in scales if r.get("reader")==name and r.get("pdf_sha256")==phash
                         and float(r.get("measured_scale","0"))>=.7]
                if not matched:issues.append("local diagram scale is unmeasured for this PDF")
        reader_checks.append(dict(reader=name,passed=not issues,issues=issues,
            required_visual_pages=required,pending_visual_pages=pending,pending_geometry=geometry_pending))
    gate("twelve standalone PDFs",all(r["passed"] for r in reader_checks),reader_checks)

    manifest=read(EDITION/"records/GUIDE_PARTS.tsv")
    guide_issues=[]
    for row in manifest:
        path=EDITION/"guide_parts"/row["file"]
        if row.get("required","true")=="true" and not path.is_file():guide_issues.append(row["file"]+": missing")
        if path.is_file() and re.search(r"(?mi)^%\s*WORKING GUIDE\b",path.read_text()):
            guide_issues.append(row["file"]+": working status")
    gate("guide manifest",bool(manifest) and not guide_issues,guide_issues)

    report_freshness=verify_reports(EDITION)
    gate("cumulative build-report freshness",report_freshness["passed"],report_freshness)

    private=[]
    roots=("readers","checked_pages","cleaned_pages","corrected_pages","master_pages","variant_records","records","guide_parts")
    paths={p for folder in roots for p in (EDITION/folder).rglob("*") if p.is_file() and p.suffix in {".tex",".tsv",".json",".md",".txt"}}
    paths.update(p for p in EDITION.iterdir() if p.is_file() and p.suffix in {".tsv",".json",".md",".txt"})
    paths.update(p for p in (EDITION/"build").glob("**/*") if p.is_file() and p.suffix in {".log",".txt",".json",".tsv"})
    for path in sorted(paths):
        for line_no,line in enumerate(path.read_text(errors="replace").splitlines(),1):
            for kind,pattern in PRIVATE.items():
                if pattern.search(line):private.append(dict(file=str(path.relative_to(EDITION)),line=line_no,kind=kind))
    for name in SPECS:
        path=EDITION/"build"/name/(name+".pdf")
        if not path.is_file():continue
        doc=fitz.open(path)
        for page_no,page in enumerate(doc,1):
            for kind,pattern in PRIVATE.items():
                if pattern.search(page.get_text()):private.append(dict(file=str(path.relative_to(EDITION)),pdf_page=page_no,kind=kind))
    gate("privacy screen",not private,private)
    report=dict(audited_utc=datetime.now(timezone.utc).isoformat(),
        status="PASS" if all(g["passed"] for g in gates) else "BLOCKED",
        gates=gates,source_checks=source_checks,translation_checks=translation_checks)
    (EDITION/"records/RELEASE_AUDIT.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    lines=["# Release audit","",f"Status: **{report['status']}**.","",
           "This audit checks source reconstruction, translation tokens, reader coverage, actual PDF reports, and separately recorded visual reviews. It does not infer that a page has been read or viewed.","",
           "| Gate | Result |","|---|---|"]
    lines += [f"| {g['gate']} | {'PASS' if g['passed'] else 'BLOCKED'} |" for g in gates]
    lines += ["","## PDF status",""]
    for row in reader_checks:
        lines += ["### "+row["reader"],"", "; ".join(row["issues"]) if row["issues"] else "All release gates passed.",
                  "", "Pending visual pages: "+str(row["pending_visual_pages"])+".",""]
    (EDITION/"records/RELEASE_AUDIT.md").write_text("\n".join(lines))
    print(json.dumps(dict(status=report["status"],checked_pages=len(checked),certified_pages=len(certified),
        translated_pages=sum(r["passed"] for r in translation_checks),
        failed_gates=[g["gate"] for g in gates if not g["passed"]])))
    if report["status"]!="PASS" and not args.report_only:raise SystemExit(1)


if __name__=="__main__":
    main()
