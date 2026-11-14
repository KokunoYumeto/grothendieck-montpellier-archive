#!/usr/bin/env python3
"""Record each reader page affected by the short-margin placement repair."""
from __future__ import annotations
from pathlib import Path
import re
from audit_release import SPECS, calls
from edition_core import resolve_variants, write_tsv

EDITION = Path(__file__).resolve().parents[1]


def main():
    records = []
    for name, (family, mode) in SPECS.items():
        if family == "guide":
            continue
        path = EDITION / "readers" / (name + ".tex")
        if not path.is_file():
            continue
        text = path.read_text()
        printed = {row[0] for row in calls(text, "PrintPage", 3)}
        for key, body, _ in calls(text, "RegisterPage", 3):
            if key not in printed:
                continue
            running = resolve_variants(body, 0 if mode==0 else 1)
            pattern = r"\\(?:margin|placedmargin|scanpage|mspage)\{" if mode == 2 else r"\\(?:margin|placedmargin)\{"
            matches = list(re.finditer(pattern, running))
            if not matches:
                continue
            records.append(dict(reader=name, page_key=key,
                source_line=running.count("\n", 0, matches[0].start()) + 1,
                issue="Independent placement of marginal items allowed items at nearby attachment points to overlap; the full-page screen found concrete collisions.",
                repair="Queue short margin boxes with 3 pt clearance, start their actual text lines before measuring placement, combine adjacent scan/folio labels, and verify paired destinations remain on the attachment page.",
                before="independent marginal boxes", after="queued margin boxes with paired page destinations",
                occurrences=len(matches)))
    write_tsv(EDITION / "records/TYPESETTING_FIXES_margin_queue.tsv", records,
        ["reader","page_key","source_line","issue","repair","before","after","occurrences"])
    print(f"Recorded margin placement repair on {len(records)} reader/source-page combinations.")


if __name__ == "__main__":
    main()
