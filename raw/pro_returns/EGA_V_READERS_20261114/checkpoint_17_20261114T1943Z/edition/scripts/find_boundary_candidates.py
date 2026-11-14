#!/usr/bin/env python3
"""List source-ID boundaries for review; do not alter any reading or spacing."""
from pathlib import Path
import json
import re
from edition_core import no_comments,resolve_variants,write_tsv,read_tsv,arguments_at,command_at

EDITION=Path(__file__).resolve().parents[1]


def visible(s):
    s=no_comments(s)
    s=re.sub(r"\$[^$]*\$", "§",s)
    s=re.sub(r"\\\[[\s\S]*?\\\]", "§",s)
    s=re.sub(r"\\[A-Za-z@]+", "",s)
    return s.replace("{","").replace("}","")


def main():
    overridden=set()
    ov=EDITION/"records/VARIANT_OVERRIDES.tsv"
    if ov.is_file():overridden={r["source_id"] for r in read_tsv(ov)}
    rows=[]
    for meta in sorted((EDITION/"variant_records").glob("ega25*.json")):
        key=meta.stem
        source=(EDITION/"master_pages/fr"/(key+".tex")).read_text()
        for v in json.loads(meta.read_text()):
            if v["parent"] or v["math_mode"]=="true" or v["kind"] not in ("insertion","deletion","typewriter strike-out"):continue
            token=r"\var{"+v["page_reading"]+"}{"+v["corrected_reading"]+"}{"+v["kind"]+"}{"+v["source_id"]+"}"
            start=source.find(token)
            if start<0:continue
            try:
                left=resolve_variants(source[:start],1)
                right=resolve_variants(source[start+len(token):],1)
            except ValueError:continue
            inside=visible(resolve_variants(v["corrected_reading"],1))
            lv=visible(left);rv=visible(right)
            word=lambda c:c.isalnum() or c=="§"
            leading=bool(lv and inside and word(lv[-1]) and word(inside[0]))
            trailing=bool(inside and rv and word(inside[-1]) and word(rv[0]))
            deletion=bool(not inside and lv and rv and word(lv[-1]) and word(rv[0]))
            if leading or trailing or deletion or v["source_id"] in overridden:
                rows.append(dict(key=key,source_id=v["source_id"],kind=v["kind"],line=v["line"],
                    left_context=left[-100:],corrected_reading=v["corrected_reading"],right_context=right[:100],
                    leading_boundary=leading,trailing_boundary=trailing,deletion_join=deletion,
                    status="explicit override recorded" if v["source_id"] in overridden else "review: whole-word boundary or internal word edit"))
    write_tsv(EDITION/"records/INSERTION_BOUNDARY_REVIEW.tsv",rows,
        ["key","source_id","kind","line","left_context","corrected_reading","right_context","leading_boundary","trailing_boundary","deletion_join","status"])
    print('Candidate boundaries:',len(rows))


if __name__=="__main__":main()
