#!/usr/bin/env python3
"""Record the metadata-only replacement of obsolete source-review comments.

Run after the page audits finish. The attached originals remain unchanged.
This changes no page body, reading, formula, or editorial annotation.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from build_readers import EDITION, PAGES, certified_keys
from edition_core import sha256, read_tsv, write_tsv


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply",action="store_true")
    args=parser.parse_args()
    certified=certified_keys()
    missing=[r["key"] for r in PAGES if r["key"] not in certified or not (EDITION/"checked_pages"/(r["key"]+".tex")).is_file()]
    if missing:
        raise SystemExit(f"Header finalization requires all 260 page-review records and checked files; {len(missing)} remain.")
    old="; not yet checked by eye."
    new="; original AI transcription, subsequently checked against both supplied scan parts; see PAGES_CHECKED.tsv and CHECK_DECISIONS.tsv."
    ledger=EDITION/"records/CHECKED_HEADER_METADATA.tsv"
    rows=read_tsv(ledger) if ledger.is_file() else []
    proposed=[]
    for r in PAGES:
        path=EDITION/"checked_pages"/(r["key"]+".tex")
        before=path.read_text()
        lines=before.splitlines(keepends=True)
        hits=[i for i,line in enumerate(lines) if line.startswith("%") and old in line]
        if not hits:continue
        if len(hits)!=1:raise SystemExit("Ambiguous obsolete status comment: "+r["key"])
        i=hits[0];oldline=lines[i]
        lines[i]=oldline.replace(old,new)
        after="".join(lines)
        # Prove that only the single comment changed.
        assert before.replace(oldline,"",1)==after.replace(lines[i],"",1)
        row=dict(key=r["key"],line=i+1,before=oldline.rstrip(),after=lines[i].rstrip(),
            before_sha256=sha256(before),after_sha256=sha256(after),
            page_body_unchanged="true",time_utc=datetime.now(timezone.utc).isoformat(),
            reason="Replace the original unreviewed-status comment after the independent page review; preserve the attached original and every page-body token.")
        proposed.append(row)
        if args.apply:path.write_text(after)
    if args.apply:
        rows.extend(proposed)
        write_tsv(ledger,rows,["key","line","before","after","before_sha256","after_sha256","page_body_unchanged","time_utc","reason"])
    print(f"{len(proposed)} metadata comments {'updated and recorded' if args.apply else 'eligible for recorded update'}.")


if __name__=="__main__":main()
