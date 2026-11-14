#!/usr/bin/env python3
"""Refresh recorded translations only after proving a comment-only source change."""
from __future__ import annotations
import argparse
import contextlib
import io
import json
from pathlib import Path
from build_readers import EDITION, validate_translation
from check_translation import check
from edition_core import read_tsv, write_tsv, sha256
from translation_records import translation_lock


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    header_path = EDITION / "records/CHECKED_HEADER_METADATA.tsv"
    metadata = {r["key"]: r for r in read_tsv(header_path)}
    proofs = []
    blocked = []
    with translation_lock():
        ledger = read_tsv(EDITION / "records/EN_TRANSLATION_STATUS.tsv")
        for row in ledger:
            key = row["key"]
            checked = (EDITION / "checked_pages" / (key + ".tex")).read_text()
            french = (EDITION / "master_pages/fr" / (key + ".tex")).read_text()
            english = (EDITION / "master_pages/en" / (key + ".tex")).read_text()
            current = dict(checked_page_sha256=sha256(checked), french_master_sha256=sha256(french),
                           english_master_sha256=sha256(english))
            if all(row[k] == v for k, v in current.items()):
                continue
            change = metadata.get(key)
            valid = bool(change and change["page_body_unchanged"] == "true"
                         and current["checked_page_sha256"] == change["after_sha256"]
                         and row["checked_page_sha256"] in (change["before_sha256"], change["after_sha256"])
                         and row["english_master_sha256"] == current["english_master_sha256"])
            if valid:
                before_line, after_line = change["before"], change["after"]
                valid = french.count(after_line) == 1 and checked.count(after_line) == 1
                if valid:
                    prior_french = french.replace(after_line, before_line, 1)
                    prior_checked = checked.replace(after_line, before_line, 1)
                    valid = (sha256(prior_checked) == change["before_sha256"] and
                             row["french_master_sha256"] in (sha256(prior_french), current["french_master_sha256"]))
            if not valid:
                blocked.append(key)
                continue
            validate_translation(key, french, english)
            proofs.append(dict(key=key, previous_checked_sha256=row["checked_page_sha256"],
                current_checked_sha256=current["checked_page_sha256"],
                previous_french_master_sha256=row["french_master_sha256"],
                current_french_master_sha256=current["french_master_sha256"],
                english_master_sha256=current["english_master_sha256"],
                proof="Only the recorded obsolete-status comment differs; English bytes and all page-body tokens are unchanged."))
        if args.apply and proofs:
            with contextlib.redirect_stdout(io.StringIO()):
                check(argparse.Namespace(keys=[r["key"] for r in proofs], record=True,
                    note="Metadata-only source refresh after all 260 page audits. The CHECKED_HEADER_METADATA record and HEADER_TRANSLATION_HASH_PROOF establish that only the obsolete review-status comment changed; English and all body tokens are unchanged."))
            path = EDITION / "records/HEADER_TRANSLATION_HASH_PROOF.tsv"
            previous = read_tsv(path) if path.is_file() else []
            write_tsv(path, previous + proofs)
    print(json.dumps(dict(comment_only_refreshes=len(proofs), applied=args.apply,
                          other_stale_or_in_progress_translations=blocked)))


if __name__ == "__main__":
    main()
