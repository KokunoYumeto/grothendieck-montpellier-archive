#!/usr/bin/env python3
"""Reuse an actually viewed complete image only after exact PNG-byte identity.

Both source and target PDFs must be frozen. This records visual evidence
equivalence, not an additional act of viewing. Differing target images stay pending.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
from pdf_review import (EDITION, REVIEW, GEOMETRY, FIELDS, FREEZES, filehash, rows,
                        lock, write_table, load_current, manifest_path, latest_reviews)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_reader")
    parser.add_argument("target_reader")
    parser.add_argument("--source-sha256",help="Use the retained manifest and actual reviews of this earlier frozen PDF, including a subsequently released version.")
    args=parser.parse_args()
    if args.source_sha256:
        source_hash=args.source_sha256
        if not any(r["reader"]==args.source_reader and r["pdf_sha256"]==source_hash for r in rows(FREEZES)):
            raise SystemExit("The specified source hash has no recorded review freeze.")
    else:
        _,_,source_hash=load_current(args.source_reader)
    _,target_report,target_hash=load_current(args.target_reader)
    source_manifest=json.loads(manifest_path(args.source_reader,source_hash).read_text())
    target_manifest=json.loads(manifest_path(args.target_reader,target_hash).read_text())
    direct={}
    for number,review in latest_reviews(args.source_reader,source_hash).items():
        if review.get("result")!="layout inspection passed" or review.get("review_method")=="byte-identical full-page image":
            continue
        image=source_manifest["images"].get(str(number))
        if not image or review.get("image")!=image["path"] or not (EDITION/image["path"]).is_file():
            continue
        digest=filehash(EDITION/image["path"])
        if digest!=image["sha256"]:
            raise SystemExit("Source inspection image changed.")
        if review.get("image_sha256") and review["image_sha256"]!=digest:
            raise SystemExit("Source record does not identify the current image bytes.")
        direct[digest]=(number,review,image)
    target_reviews=latest_reviews(args.target_reader,target_hash)
    source_geometry={}
    for row in rows(GEOMETRY):
        if row["reader"]==args.source_reader and row["pdf_sha256"]==source_hash:
            source_geometry[(int(row["pdf_page"]),row["flag_kind"])]=row
    starts=sorted((p,k) for k,p in target_report["source_physical_pages"].items())
    additions=[];equivalences=[];dispositions=[]
    for number in target_manifest["required_visual_review_pages"]:
        if target_reviews.get(number,{}).get("result")=="layout inspection passed":
            continue
        image=target_manifest["images"].get(str(number))
        if not image or not (EDITION/image["path"]).is_file():
            continue
        digest=filehash(EDITION/image["path"])
        if digest!=image["sha256"]:
            raise SystemExit("Target review image changed.")
        if digest not in direct:
            continue
        original_page,review,original_image=direct[digest]
        stamp=datetime.now(timezone.utc).isoformat()
        origin=f"{args.source_reader}, PDF page {original_page}, PDF SHA-256 {source_hash}"
        proof=dict(source_reader=args.source_reader,source_pdf_sha256=source_hash,
            source_pdf_page=original_page,source_image=original_image["path"],
            target_reader=args.target_reader,target_pdf_sha256=target_hash,
            target_pdf_page=number,target_image=image["path"],image_sha256=digest,
            original_reviewed_utc=review["reviewed_utc"],recorded_utc=stamp,
            result="Exact complete-PNG byte identity with an actually viewed page.")
        equivalences.append(proof)
        source_key=next((k for p,k in reversed(starts) if p<=number),"frontmatter")
        additions.append(dict(reader=args.target_reader,pdf_sha256=target_hash,pdf_page=number,
            source_key=source_key,image=image["path"],image_sha256=digest,reviewed_utc=stamp,
            reviewer=review.get("reviewer","GPT-6 Astra"),
            findings="The complete rendered image is byte-identical to the actually viewed image from "+origin+". Original findings: "+review["findings"],
            result="layout inspection passed",review_method="byte-identical full-page image",
            evidence_source_reader=args.source_reader,evidence_source_pdf_sha256=source_hash,
            evidence_source_pdf_page=original_page,evidence_source_image=original_image["path"],
            evidence_original_reviewed_utc=review["reviewed_utc"]))
        for field in FIELDS:
            if not any(r["pdf_page"]==number for r in target_report.get(field,[])):
                continue
            disposition=source_geometry.get((original_page,field))
            if disposition:
                dispositions.append(dict(reader=args.target_reader,pdf_sha256=target_hash,pdf_page=number,
                    flag_kind=field,decision=disposition["decision"],
                    reason="The complete image is byte-identical to "+origin+". Original disposition: "+disposition["reason"],
                    reviewer=disposition.get("reviewer",review.get("reviewer","GPT-6 Astra")),
                    reviewed_utc=stamp,review_method="byte-identical full-page image"))
    with lock():
        if additions:
            write_table(REVIEW,rows(REVIEW)+additions)
            path=EDITION/"records/PDF_VISUAL_EQUIVALENCE.tsv"
            write_table(path,rows(path)+equivalences)
        if dispositions:
            write_table(GEOMETRY,rows(GEOMETRY)+dispositions)
    print(json.dumps(dict(source=args.source_reader,target=args.target_reader,
        equivalent_previously_viewed_pages=len(additions),equivalent_geometry_dispositions=len(dispositions))))


if __name__=="__main__":
    main()
