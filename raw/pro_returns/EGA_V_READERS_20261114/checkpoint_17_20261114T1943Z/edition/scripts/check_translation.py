#!/usr/bin/env python3
"""Validate completed page translations and retain their source-version hashes."""
from __future__ import annotations
import argparse
from datetime import datetime,timezone
import json
from pathlib import Path
from build_readers import EDITION,validate_translation
from edition_core import read_tsv,write_tsv,sha256,mark_counts


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("keys",nargs="*")
    p.add_argument("--record",action="store_true",help="Record a completed translation against its current source hash")
    args=p.parse_args()
    ledger=EDITION/"records/EN_TRANSLATION_STATUS.tsv"
    old={r["key"]:r for r in read_tsv(ledger)} if ledger.exists() else {}
    keys=args.keys or [f.stem for f in sorted((EDITION/"master_pages/en").glob("*.tex"))]
    results=[]
    for key in keys:
        fr=(EDITION/"master_pages/fr"/(key+".tex")).read_text()
        en=(EDITION/"master_pages/en"/(key+".tex")).read_text()
        checked=(EDITION/"checked_pages"/(key+".tex")).read_text()
        audit=validate_translation(key,fr,en)
        record=dict(key=key,french_master_sha256=sha256(fr),checked_page_sha256=sha256(checked),
            english_master_sha256=sha256(en),recorded_utc=datetime.now(timezone.utc).isoformat(),
            formulas=audit["formulas"],variants=audit["variants"],omitted_variant_ids=audit["omitted_variant_ids"],
            translator_notes=mark_counts(en)["tnote"],status="translated; formulas and variant IDs checked")
        prior=old.get(key)
        stale=prior is not None and (prior["french_master_sha256"]!=record["french_master_sha256"] or prior["checked_page_sha256"]!=record["checked_page_sha256"])
        translation_changed=prior is not None and prior["english_master_sha256"]!=record["english_master_sha256"]
        if args.record:old[key]=record
        results.append(dict(key=key,formula_audit="pass",source_changed_since_record=stale,translation_changed_since_record=translation_changed,ledger_missing=prior is None,recorded=bool(args.record)))
    if args.record:write_tsv(ledger,[old[k] for k in sorted(old)])
    print(json.dumps(results,ensure_ascii=False))
    if not args.record and any(r["source_changed_since_record"] or r["translation_changed_since_record"] or r["ledger_missing"] for r in results):
        raise SystemExit(1)


if __name__=="__main__":main()
