#!/usr/bin/env python3
"""Merge authored translation annotations without losing concurrent page work."""
from __future__ import annotations
import argparse
from contextlib import contextmanager
import fcntl
import json
from pathlib import Path
from edition_core import read_tsv,write_tsv

EDITION=Path(__file__).resolve().parents[1]
TABLES={
    "omissions":("EN_VARIANT_OMISSIONS.tsv",["key","source_id","reason"],["key","source_id"]),
    "variant_notes":("EN_VARIANT_NOTES.tsv",["source_id","note"],["source_id"]),
    "glossary":("GLOSSARY_CONTEXT_DECISIONS.tsv",["key","french","english","glossary_entry","reason"],["key","french"]),
}


@contextmanager
def translation_lock():
    folder=EDITION/"build";folder.mkdir(exist_ok=True)
    with (folder/"translation_records.lock").open("a") as handle:
        fcntl.flock(handle,fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(handle,fcntl.LOCK_UN)


def merge_annotations(payload: dict, replace: bool=False) -> dict:
    unknown=set(payload)-set(TABLES)
    if unknown:raise ValueError("Unknown annotation tables: "+", ".join(sorted(unknown)))
    changes={};staged=[]
    with translation_lock():
        for kind,additions in payload.items():
            filename,fields,keyfields=TABLES[kind]
            path=EDITION/"records"/filename
            rows=read_tsv(path) if path.is_file() else []
            bykey={tuple(r[k] for k in keyfields):r for r in rows}
            changed=0
            for supplied in additions:
                if not all(isinstance(supplied.get(k),str) and supplied[k].strip() for k in fields):
                    raise ValueError("Every field is required and must be nonempty for "+kind)
                row={k:supplied[k] for k in fields};identity=tuple(row[k] for k in keyfields)
                old=bykey.get(identity)
                if old is not None and old!=row and not replace:
                    raise ValueError("Conflicting existing annotation for "+" / ".join(identity))
                if old!=row:bykey[identity]=row;changed+=1
            staged.append((path,[bykey[k] for k in sorted(bykey)],fields))
            changes[kind]=changed
        for path,rows,fields in staged:
            write_tsv(path,rows,fields)
    return changes


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_files",nargs="+")
    parser.add_argument("--replace",action="store_true",help="Replace conflicting authored records after reviewing them")
    args=parser.parse_args()
    payload={}
    for file in args.json_files:
        for kind,rows in json.loads(Path(file).read_text()).items():
            payload.setdefault(kind,[]).extend(rows)
    print(json.dumps(merge_annotations(payload,args.replace),ensure_ascii=False))


if __name__=="__main__":main()
