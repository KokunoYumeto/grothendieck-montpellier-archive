#!/usr/bin/env python3
"""Build standalone readers only from explicitly selected, verified inputs.

Preparation: python edition/scripts/build_readers.py prepare --partial
Release:     python edition/scripts/build_readers.py build --family fr
Development: python edition/scripts/build_readers.py prepare --development

Development output has a separate root and an explicit unchecked label.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

from edition_core import (cleanup_page, annotate_page, apply_variant_overrides, resolve_variants, math_fragments,
    mark_counts, read_tsv, write_tsv, sha256, ParseError, without_translator_notes, extract_variants, arguments_at, no_comments, bare_numerals)

EDITION = Path(__file__).resolve().parents[1]
WORKSPACE = EDITION.parent
SOURCE = WORKSPACE / "source"
PAGES = read_tsv(SOURCE / "records/PAGES_EGA_V.tsv")
PAGE_MAP = {r["key"]: r for r in PAGES}


def certified_keys() -> set[str]:
    keys: set[str] = set()
    candidates = [EDITION/"PAGES_CHECKED.tsv", EDITION/"records/PAGES_CHECKED.tsv"]
    candidates += list((EDITION/"review_work").glob("**/PAGES_CHECKED*.tsv"))
    candidates += list((EDITION/"records").glob("PAGES_CHECKED_*.tsv"))
    for f in candidates:
        if f.is_file():
            for row in read_tsv(f):
                if row.get("key"): keys.add(row["key"])
    return keys


def selected_records(args) -> list[dict]:
    if args.family == "blass":
        return [r for r in PAGES if r["cote"] == "24"]
    if args.family in ("fr", "en"):
        return [r for r in PAGES if r["cote"] == "25"]
    return PAGES


def prepare(args) -> Path:
    target = EDITION/"development" if args.development else EDITION
    records = selected_records(args)
    certified = certified_keys()
    overridefile=EDITION/"records/VARIANT_OVERRIDES.tsv"
    overrides=read_tsv(overridefile) if overridefile.is_file() and not args.development else []
    changes, cleanup, proofs, statuses = [], [], [], []
    errors: list[dict] = []
    for r in records:
        key = r["key"]
        family = "fr" if r["cote"] == "25" else "blass"
        infile = SOURCE/r["page_file"] if args.development else EDITION/"checked_pages"/(key+".tex")
        present = infile.is_file()
        if not present:
            statuses.append(dict(key=key, status="missing checked page"))
            if not args.partial: errors.append(dict(key=key, error="Missing checked page"))
            continue
        if not args.development and key not in certified:
            statuses.append(dict(key=key, status="checked file lacks page-review record"))
            # Preparation may expose a reviewed page while the aggregate record is
            # being written. Release mode below always requires the record.
            if not args.partial:
                errors.append(dict(key=key,error="Checked file has no PAGES_CHECKED record"))
                continue
        try:
            original = infile.read_text(encoding="utf-8")
            cleaned, fixes = cleanup_page(original, key)
            annotated, variants = annotate_page(cleaned, key)
            annotated=apply_variant_overrides(annotated,variants,[r for r in overrides if r["key"]==key])
            if key=="ega25_25_022" and not args.development:
                from author_restorations import restore_45_at_51
                annotated,variants=restore_45_at_51(annotated,variants,target,PAGE_MAP)
            diplomatic = resolve_variants(annotated, 0)
            if diplomatic != cleaned:
                raise ParseError("Diplomatic reconstruction differs from mechanically cleaned source")
            scan = re.findall(r"\\scanpage\{([^}]+)\}", cleaned)
            if scan != [r["cote"]+"/"+str(int(r["site"]))]:
                raise ParseError("Scan marker differs from the page record")
            for sub, content in (("cleaned_pages",cleaned), (f"master_pages/{family}",annotated),
                    (f"corrected_pages/{family}",resolve_variants(annotated,1))):
                path = target/sub/(key+".tex"); path.parent.mkdir(parents=True,exist_ok=True)
                path.write_text(content,encoding="utf-8")
            vpath = target/"variant_records"/(key+".json")
            vpath.parent.mkdir(parents=True,exist_ok=True)
            vpath.write_text(json.dumps([v.as_record() for v in variants],ensure_ascii=False,indent=2)+"\n")
            changes += [v.as_record() for v in variants]
            cleanup += fixes
            statuses.append(dict(key=key,status="UNCHECKED DEVELOPMENT" if args.development else "prepared from checked page"))
            proofs.append(dict(key=key, input="transcription/"+r["page_file"].split("transcription/")[-1] if args.development else "checked_pages/"+key+".tex",
                input_sha256=sha256(original),cleaned_sha256=sha256(cleaned),annotated_sha256=sha256(annotated),
                diplomatic_reconstruction="exact",variants=len(variants),
                source_marks=json.dumps(mark_counts(cleaned),sort_keys=True),
                corrected_math_sha256=sha256(json.dumps(math_fragments(resolve_variants(annotated,1)),ensure_ascii=False))))
        except Exception as e:
            errors.append(dict(key=key,error=f"{type(e).__name__}: {e}"))
    # Per-page records make repeated preparation incremental and stable. Aggregate
    # files enumerate all prepared pages, including other independently built cotes.
    all_changes = []
    for f in sorted((target/"variant_records").glob("*.json")):
        all_changes += json.loads(f.read_text())
    write_tsv(target/"CHANGES.tsv",all_changes,list(all_changes[0]) if all_changes else ["source_id","key","cote","site","place","page_reading","corrected_reading","kind","reason"])
    # Cleanup is regenerated for this selected source set and kept with that set.
    write_tsv(target/"records"/("CLEANUP_LOG_"+args.family+".tsv"),cleanup,
        ["key","line","before","after","action","reason"])
    write_tsv(target/"records"/("SOURCE_RECONSTRUCTION_"+args.family+".tsv"),proofs,
        ["key","input","input_sha256","cleaned_sha256","annotated_sha256","diplomatic_reconstruction","variants","source_marks","corrected_math_sha256"])
    write_tsv(target/"records"/("PREPARATION_STATUS_"+args.family+".tsv"),statuses,["key","status"])
    write_tsv(target/"records"/("PREPARATION_ERRORS_"+args.family+".tsv"),errors,["key","error"])
    print(json.dumps({"prepared":len(proofs),"variants":len(changes),"mechanical_changes":len(cleanup),"errors":errors,"development":args.development},ensure_ascii=False))
    if errors: raise SystemExit(1)
    return target


def validate_translation(key: str, french: str, english: str) -> dict:
    fr_ids = re.findall(r"\}\{(ega25_25_\d+-v\d+)\}",french)
    en_ids = re.findall(r"\}\{(ega25_25_\d+-v\d+)\}",english)
    omitted=[]
    omissionfile=EDITION/"records/EN_VARIANT_OMISSIONS.tsv"
    if omissionfile.is_file():
        omitted=[r["source_id"] for r in read_tsv(omissionfile) if r["key"]==key and r.get("reason","").strip()]
    expected=[sid for sid in fr_ids if sid not in omitted]
    if expected != en_ids:
        raise ParseError(f"{key}: translation variant IDs/order differ")
    fm = math_fragments(resolve_variants(french,1))
    source_english=without_translator_notes(english)
    em = math_fragments(resolve_variants(source_english,1))
    if fm != em:
        differing = [i+1 for i,(a,b) in enumerate(zip(fm,em)) if a!=b]
        raise ParseError(f"{key}: translated formulas differ: French {len(fm)}, English {len(em)}; first differing positions {differing[:5]}")
    # Also check formulas in the page-reading side used by the apparatus.
    if math_fragments(resolve_variants(french,0))!=math_fragments(resolve_variants(source_english,0)):
        raise ParseError(f"{key}: page-reading-side formulas differ")
    for side in (0,1):
        if bare_numerals(resolve_variants(french,side))!=bare_numerals(resolve_variants(source_english,side)):
            raise ParseError(f"{key}: numerals outside explicit math differ in branch {side}")
    source_marks=mark_counts(resolve_variants(french,1))
    translation_marks=mark_counts(resolve_variants(source_english,1))
    for name in ("unsure","illegible"):
        if source_marks[name]!=translation_marks[name]:
            raise ParseError(f"{key}: live {name} mark count differs: French {source_marks[name]}, English {translation_marks[name]}")
    if key=="ega25_25_022":
        from author_restorations import translated_passage
        donor=(EDITION/"master_pages/en/ega25_25_021.tex").read_text()
        metadata=json.loads((EDITION/"variant_records/ega25_25_021.json").read_text())
        expected=translated_passage(donor,metadata)
        restores=[v for v in extract_variants(english).values() if v["kind"]=="author-directed restoration"]
        if len(restores)!=1:raise ParseError("The English site22 restoration is not unique")
        actual=arguments_at(restores[0]["corrected_reading"],0,"restoredfrom")[0][2]
        if no_comments(actual).strip()!=no_comments(expected).strip():
            raise ParseError("The English site22 restored passage differs from its translated site21 source")
    return dict(key=key,variants=len(en_ids),omitted_variant_ids=" ".join(omitted),formulas=len(fm),formula_tokens_identical="true",
        bare_numerals_identical="true",live_uncertainty_marks_identical="true")


def build(args) -> None:
    target = prepare(args)
    from edition_render import build_family
    families = ["fr","blass","en"] if args.family=="all" else [args.family]
    for family in families:
        pagekeys = [r["key"] for r in PAGES if r["cote"]==("24" if family=="blass" else "25")]
        present = [k for k in pagekeys if (target/"master_pages"/family/(k+".tex")).is_file()]
        if not args.partial and len(present)!=len(pagekeys):
            raise SystemExit(f"Refusing incomplete {family} reader: {len(present)}/{len(pagekeys)} source pages")
        if not present:
            print(f"No prepared {family} pages; no reader emitted.")
            continue
        if family=="en":
            audits=[]
            ledgerfile=EDITION/"records/EN_TRANSLATION_STATUS.tsv"
            ledger={r["key"]:r for r in read_tsv(ledgerfile)} if ledgerfile.is_file() else {}
            for k in present:
                french=(target/"master_pages/fr"/(k+".tex")).read_text()
                english=(target/"master_pages/en"/(k+".tex")).read_text()
                audits.append(validate_translation(k,french,english))
                if not args.development:
                    prior=ledger.get(k)
                    checked=(target/"checked_pages"/(k+".tex")).read_text()
                    hashes=dict(french_master_sha256=sha256(french),english_master_sha256=sha256(english),checked_page_sha256=sha256(checked))
                    if prior is None or any(prior.get(field)!=value for field,value in hashes.items()):
                        raise SystemExit(f"Refusing unrecorded or stale translation {k}; review its current source and record the completed translation with check_translation.py --record.")
            write_tsv(target/"records/TRANSLATION_FORMULA_AUDIT.tsv",audits)
        outputs=build_family(target,family,present,PAGE_MAP,partial=args.partial,development=args.development)
        print(json.dumps({"family":family,"files":[p.name for p in outputs],"pages":len(present)}))


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("command",choices=["prepare","build"])
    p.add_argument("--family",choices=["all","fr","en","blass"],default="all")
    p.add_argument("--partial",action="store_true",help="Prepare available reviewed pages; label resulting previews incomplete")
    p.add_argument("--development",action="store_true",help="Use original unverified input ONLY in a separate development output tree")
    args=p.parse_args()
    if args.command=="prepare":prepare(args)
    else:build(args)


if __name__=="__main__":main()
