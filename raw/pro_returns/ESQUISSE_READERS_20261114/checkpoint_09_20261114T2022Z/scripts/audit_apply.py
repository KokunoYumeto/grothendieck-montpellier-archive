#!/usr/bin/env python3
"""Apply an explicit visual-review declaration; never infer review from a file.

Example: python work/edition/scripts/audit_apply.py review.json
The JSON records exactly which images the reviewer viewed and the decisions made.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, re, fcntl
from pathlib import Path
from audit_inventory import read_tsv, write_tsv, parse_marks

CHECK_FIELDS=["decision_id","source_item_id","key","cote","site","line","transcription_reading","image_reading","decision","reason","images"]
DIFF_FIELDS=["difference_id","key","cote","site","typescript_page","class","draft","page","note","outcome","reason","decision_ids"]
COLLATION_FIELDS=["collation_id","typescript_page","line","copy1_key","copy2_key","copy1_reading","copy2_reading","kind","decision","reason","decision_ids"]

def clean_record(value):
    # Newline-safe TSV cells still retain literal LaTeX through csv quoting.
    return str(value)

def require_text(value,name):
    if not isinstance(value,str) or not value.strip():raise ValueError(f"{name} requires the reviewer's nonempty observation")
    return value

def update_tsv(path,new,fields,key_field="key",key=None):
    old=read_tsv(path) if path.exists() else []
    if key is not None:old=[r for r in old if r.get(key_field)!=key]
    write_tsv(path,old+new,fields)

def main():
    ap=argparse.ArgumentParser();ap.add_argument("review");ap.add_argument("--work",default="work");args=ap.parse_args()
    root=Path(args.work);out=root/"edition";review=json.loads(Path(args.review).read_text())
    lock=(out/".audit-records.lock").open("w")
    fcntl.flock(lock.fileno(),fcntl.LOCK_EX)
    key=review["key"];packet=json.loads((root/"review_packets"/f"{key}.json").read_text())
    source=packet["source_text"];meta=packet["metadata"]
    if set(review.get("inspected_images",[]))!=set(packet["required_images"]):
        raise ValueError("Explicit inspected_images must name both required page halves, with ZIP-relative paths")
    observed=require_text(review.get("inspection_statement"),"inspection_statement")
    images=" ".join(packet["required_images"]);checks=[];serial=0;current=source
    def row(item,line,before,after,decision,reason):
        nonlocal serial
        serial+=1
        checks.append(dict(decision_id=f"C-{key}-{serial:03d}",source_item_id=item,key=key,
            cote=meta["cote"],site=meta["site"],line=line,transcription_reading=before,
            image_reading=after,decision=decision,reason=require_text(reason,"decision reason"),images=images))
        return checks[-1]["decision_id"]
    patch_log=[]
    for i,patch in enumerate(review.get("patches",[]),1):
        old=patch["old"];new=patch["new"];reason=require_text(patch.get("reason"),"patch reason")
        matches=[m.start() for m in re.finditer(re.escape(old),current)] if old else []
        if not matches:raise ValueError(f"Patch {i}: old text not found")
        if len(matches)>1 and "occurrence" not in patch and not patch.get("replace_all"):
            raise ValueError(f"Patch {i}: {len(matches)} matches; supply occurrence or explicit replace_all")
        chosen=matches if patch.get("replace_all") else [matches[int(patch.get("occurrence",1))-1]]
        origpos=source.find(old);line=patch.get("line",source.count("\n",0,origpos)+1 if origpos>=0 else "")
        did=row(patch.get("source_item_id",f"P-{key}-{i:03d}"),line,old,patch.get("image_reading",new),patch.get("decision","transcription corrected"),reason)
        for pos in reversed(chosen):current=current[:pos]+new+current[pos+len(old):]
        patch_log.append({**patch,"decision_id":did,"line":line})
    def changed_reading(original):
        value=original
        for patch in patch_log:
            if patch["old"] in value:value=value.replace(patch["old"],patch["new"])
        return value
    macro_overrides=review.get("macro_observations",{})
    if review.get("confirm_all_original_macros") is True:
        macro_default=require_text(review.get("macro_confirmation_reason",observed),"macro_confirmation_reason")
    else:macro_default=None
    for mark in packet["marks"]:
        entry=macro_overrides.get(mark["item_id"])
        if entry is None and macro_default is None:continue
        if isinstance(entry,str):entry={"reason":entry}
        entry=entry or {};after=entry.get("image_reading",changed_reading(mark["raw"]))
        decision=entry.get("decision","transcription corrected" if after!=mark["raw"] else "confirmed on image")
        row(mark["item_id"],mark["line"],mark["raw"],after,decision,entry.get("reason",macro_default))
    note_overrides=review.get("note_observations",{})
    note_default=review.get("notes_confirmation_reason") if review.get("confirm_all_notes") is True else None
    for note in packet["note_items"]:
        entry=note_overrides.get(note["item_id"])
        if entry is None and note_default is None:continue
        if isinstance(entry,str):entry={"image_reading":entry,"reason":entry}
        entry=entry or {}
        row(note["item_id"],entry.get("line","see note"),note["text"],entry.get("image_reading",note_default),entry.get("decision","note checked on image"),entry.get("reason",note_default))
    diff_overrides=review.get("difference_outcomes",{})
    diff_default=require_text(review.get("differences_confirmation_reason",observed),"differences_confirmation_reason") if review.get("confirm_all_differences") is True else None
    diffrows=[]
    for diff in packet["differences"]:
        entry=diff_overrides.get(diff["difference_id"])
        if entry is None and diff_default is None:continue
        if isinstance(entry,str):entry={"reason":entry}
        entry=entry or {};after=entry.get("image_reading",changed_reading(diff["page"]))
        outcome=entry.get("outcome","our transcription corrected" if after!=diff["page"] else "the typescript reads as our transcription")
        reason=entry.get("reason",diff_default)
        did=row(diff["difference_id"],entry.get("line",",".join(map(str,diff["literal_matching_lines"])) or "see difference note"),diff["page"],after,outcome,reason)
        diffrows.append({**diff,"outcome":outcome,"reason":reason,"decision_ids":did})
    for i,entry in enumerate(review.get("additional_decisions",[]),1):
        row(entry.get("source_item_id",f"A-{key}-{i:03d}"),entry.get("line",""),entry.get("transcription_reading",""),entry["image_reading"],entry["decision"],entry["reason"])
    if review.get("full_text_confirmation"):
        reason=require_text(review["full_text_confirmation"],"full_text_confirmation")
        for number,line in enumerate(source.splitlines(),1):
            if not line.strip() or line.lstrip().startswith("%"):continue
            after=changed_reading(line)
            row(f"L-{key}-{number:03d}",number,line,after,"full line checked on image",reason)
    covered={r["source_item_id"] for r in checks}
    required={m["item_id"] for m in packet["marks"]}|{n["item_id"] for n in packet["note_items"]}|{d["difference_id"] for d in packet["differences"]}
    missing=sorted(required-covered)
    finalize=review.get("finalize",True)
    if finalize and missing:raise ValueError("Unreviewed targets: "+", ".join(missing))
    if finalize and not review.get("full_text_confirmation"):raise ValueError("Finalization requires explicit full_text_confirmation")
    # Keep the supplied attribution; add exact new review status as comments.
    if finalize:
        current=current.replace("not yet checked by eye.","source transcription; scan review recorded in CHECK_DECISIONS.tsv.")
        current="% Scan-checked edition: both supplied image halves reviewed; see CHECK_DECISIONS.tsv.\n"+current
        dest=out/"checked_pages"/f"{key}.tex";dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(current)
    for path,new,fields in [(out/"CHECK_DECISIONS.tsv",checks,CHECK_FIELDS),(out/"DIFFERENCES_OUTCOMES.tsv",diffrows,DIFF_FIELDS)]:
        update_tsv(path,new,fields,key=key)
    if not (out/"COLLATION.tsv").exists():write_tsv(out/"COLLATION.tsv",[],COLLATION_FIELDS)
    archive=out/"reviews";archive.mkdir(exist_ok=True)
    (archive/f"{key}.json").write_text(json.dumps(review,ensure_ascii=False,indent=2)+"\n")
    status={"key":key,"finalized":finalize,"original_sha256":packet["source_sha256"],
        "checked_sha256":hashlib.sha256(current.encode()).hexdigest() if finalize else None,
        "checks":len(checks),"differences":len(diffrows),"patches":len(patch_log),"missing_targets":missing}
    (archive/f"{key}_status.json").write_text(json.dumps(status,indent=2)+"\n")
    print(json.dumps(status,ensure_ascii=False))

if __name__=="__main__":main()
