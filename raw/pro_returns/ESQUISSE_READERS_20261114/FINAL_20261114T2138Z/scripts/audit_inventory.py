#!/usr/bin/env python3
"""Inventory supplied source records and prepare image-review packets.

Run from the directory containing the extracted `work/source` and `work/images`.
This program never assigns a visual outcome.
"""
from __future__ import annotations
import argparse, collections, csv, hashlib, json, re, tempfile
from pathlib import Path

MACROS = {"hand":1,"handcircle":1,"over":2,"inserted":1,"margin":1,"deleted":1,"xout":1,
          "unsure":1,"illegible":1,"uline":1,"uuline":1,"diagram":1,
          "mspage":1,"scanpage":1}
HAND = {"hand","handcircle","over","inserted","margin","deleted","xout"}

def read_tsv(path):
    with Path(path).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def write_tsv(path, rows, fields):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.NamedTemporaryFile("w",encoding="utf-8",newline="",dir=path.parent,prefix=path.name+".",delete=False) as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n",extrasaction="ignore")
        w.writeheader(); w.writerows(rows)
        temporary=Path(f.name)
    temporary.replace(path)

def escaped(text, pos):
    n=0; pos-=1
    while pos>=0 and text[pos]=="\\": n+=1; pos-=1
    return n%2==1

def comment_spans(text):
    return [(m.start(),text.find("\n",m.start()) if "\n" in text[m.start():] else len(text))
            for m in re.finditer("%",text) if not escaped(text,m.start())]

def group(text,start,opening="{",closing="}"):
    if start>=len(text) or text[start]!=opening: return None
    level=1; i=start+1
    while i<len(text):
        ch=text[i]
        if ch=="%" and not escaped(text,i):
            j=text.find("\n",i); i=len(text) if j<0 else j+1; continue
        if not escaped(text,i):
            if ch==opening:level+=1
            elif ch==closing:
                level-=1
                if not level:return (text[start+1:i],i+1)
        i+=1
    return None

def parse_marks(text,key=""):
    comments=comment_spans(text); result=[]
    for m in re.finditer(r"\\([A-Za-z]+)",text):
        name=m.group(1)
        if name not in MACROS:continue
        containing=next(((a,b) for a,b in comments if a<=m.start()<b),None)
        commented=False
        if containing:
            # A content command after an end-of-line hyphen's percent sign is a
            # supplied syntax defect and remains a review target. Full comment
            # lines are explanatory records and do not contribute content.
            line_start=text.rfind("\n",0,containing[0])+1
            if not text[line_start:containing[0]].strip():continue
            commented=True
        cursor=m.end(); args=[]; optional=None; error=None
        while cursor<len(text) and text[cursor].isspace():cursor+=1
        if name=="inserted" and cursor<len(text) and text[cursor]=="[":
            opt=group(text,cursor,"[","]")
            if opt:optional,cursor=opt
        for _ in range(MACROS[name]):
            while cursor<len(text) and text[cursor].isspace():cursor+=1
            part=group(text,cursor)
            if part is None: error="missing or unbalanced argument"; break
            arg,cursor=part;args.append(arg)
        result.append(dict(item_id=f"M-{key}-{len(result)+1:03d}",macro=name,
            line=text.count("\n",0,m.start())+1,end_line=text.count("\n",0,cursor)+1,
            start=m.start(),end=cursor,raw=text[m.start():cursor],arguments=args,
            optional=optional,parse_error=error,commented=commented))
    return result

def note_items(value,key):
    result=[]; metadata=[]
    for item in value.split(" | "):
        item=item.strip()
        if not item:continue
        if item.startswith("LONG-HANDWRITING:"): metadata.append(item);continue
        result.append(dict(item_id=f"N-{key}-{len(result)+1:03d}",text=item))
    return result,metadata

def verify_manifest(base):
    rows=read_tsv(base/"MANIFEST.tsv"); outcomes=[]
    for row in rows:
        p=base/row["path"]; data=p.read_bytes()
        outcome=dict(path=row["path"],bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),
                     expected_bytes=int(row["bytes"]),expected_sha256=row["sha256"])
        outcome["verified"]=outcome["bytes"]==outcome["expected_bytes"] and outcome["sha256"]==outcome["expected_sha256"]
        outcomes.append(outcome)
    if not all(r["verified"] for r in outcomes):raise ValueError("Manifest integrity failure")
    return outcomes

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--work",default="work");args=ap.parse_args()
    root=Path(args.work);source=root/"source";images=root/"images"
    out=root/"edition";packets=root/"review_packets"
    records=out/"records";records.mkdir(parents=True,exist_ok=True);packets.mkdir(parents=True,exist_ok=True)
    integrity={"ESQUISSE_TEXT.zip":verify_manifest(source),"ESQUISSE_SCANS.zip":verify_manifest(images)}
    (records/"SOURCE_INTEGRITY.json").write_text(json.dumps(integrity,ensure_ascii=False,indent=2)+"\n")
    pages=read_tsv(source/"records/PAGES_ESQUISSE.tsv")
    all_diffs=[];notes={};diffs=collections.defaultdict(list)
    for copy,folder in [(1,"esquisse"),(2,"esquisse_copy2")]:
        base=source/"transcription"/folder
        for row in read_tsv(base/"NOTES.tsv"):notes[row["key"]]=row
        for i,row in enumerate(read_tsv(base/"DIFFERENCES.tsv"),1):
            entry={"difference_id":f"D{copy}-{i:03d}","copy":copy,"source_record":f"transcription/{folder}/DIFFERENCES.tsv","source_row":i+1,**row}
            all_diffs.append(entry);diffs[row["key"]].append(entry)
    counts=collections.defaultdict(collections.Counter);page_counts=[];targets=[]
    for page in pages:
        key=page["key"];copy=1 if key.startswith("esq_") else 2
        source_bytes=(source/page["page_file"]).read_bytes()
        text=source_bytes.decode("utf-8").replace("\r\n","\n")
        marks=parse_marks(text,key);items,meta=note_items(notes[key]["notes"],key)
        for mark in marks: counts[copy][mark["macro"]]+=1
        counts[copy]["pages"]+=1;counts[copy]["note_items"]+=len(items);counts[copy]["difference_rows"]+=len(diffs[key])
        lines=[{"line":i,"text":s} for i,s in enumerate(text.splitlines(),1)]
        for d in diffs[key]:
            needle=d["page"]
            d["literal_matching_lines"]=[l["line"] for l in lines if needle and needle in l["text"]]
        packet={"key":key,"copy":copy,"metadata":page,"source_sha256":hashlib.sha256(source_bytes).hexdigest(),
            "source_text_newlines":"CRLF decoded as LF for line-addressed review" if b"\r\n" in source_bytes else "LF unchanged",
            "source_text":text,"source_lines":lines,"marks":marks,"note_items":items,
            "note_metadata":meta,"notes_record":notes[key],"differences":diffs[key],
            "required_images":page["images"].split(),"inspection_status":"unreviewed"}
        (packets/f"{key}.json").write_text(json.dumps(packet,ensure_ascii=False,indent=2)+"\n")
        page_counts.append({"key":key,"copy":copy,"site":page["site"],"typescript_page":page["ts_page"],
            "lines":len(lines),"marks":len(marks),"note_items":len(items),"difference_rows":len(diffs[key]),
            **{k:sum(m["macro"]==k for m in marks) for k in MACROS}})
        targets.extend([{"key":key,"source_item_id":m["item_id"],"target_type":"macro","line":m["line"],"original":m["raw"]} for m in marks])
        targets.extend([{"key":key,"source_item_id":n["item_id"],"target_type":"note","line":"","original":n["text"]} for n in items])
        targets.extend([{"key":key,"source_item_id":d["difference_id"],"target_type":"difference","line":"","original":d["page"]} for d in diffs[key]])
    write_tsv(records/"SOURCE_PAGE_INVENTORY.tsv",page_counts,list(page_counts[0]))
    write_tsv(records/"REVIEW_TARGETS.tsv",targets,["key","source_item_id","target_type","line","original"])
    write_tsv(records/"DIFFERENCES_SOURCE_INDEX.tsv",all_diffs,["difference_id","copy","source_record","source_row","key","cote","site","typescript_page","class","draft","page","note"])
    total=counts[1]+counts[2]
    report=["# Source inventory","", "This inventory is mechanical. It assigns no scan-reading outcome.","",
        "Both attached manifests were read before the inventories were prepared. Every listed file matched its byte count and SHA-256 digest.","",
        "| Source | Manifest entries | Verified |","| --- | ---: | ---: |"]
    for name,rows in integrity.items():report.append(f"| {name} | {len(rows)} | {sum(x['verified'] for x in rows)} |")
    report += ["","| Item | Copy 1 | Copy 2 | Total |","| --- | ---: | ---: | ---: |"]
    for k in ["pages","note_items","difference_rows",*MACROS]:report.append(f"| {k} | {counts[1][k]} | {counts[2][k]} | {total[k]} |")
    report += ["","The source inventory counts parsed content commands, including nested commands and a content command unintentionally suppressed after an inline percent sign (flagged in its packet). Full comment lines are excluded. Original uncertainty and handwriting assignments remain unverified until an explicit review is recorded.","",
        "## Stable identifiers","","Difference identifiers retain original row order: D1-001 through D1-327 and D2-001 through D2-141. Macro identifiers are M-<page key>-<three-digit occurrence>; note identifiers are N-<page key>-<three-digit item>. Each packet records the original file hash, complete text, numbered lines, exact macro spans, all note items, original difference rows, archive metadata, and both required image names.","",
        "Original input tables are read directly from the supplied text archive; they are not duplicated among the deliverables. The authored inventories add stable IDs, parsed targets and integrity outcomes. Review packet strings use LF line endings; the recorded source hash always describes the original bytes in the attachment. This newline decoding has no printed effect.",""]
    (records/"SOURCE_INVENTORY.md").write_text("\n".join(report))
    print(json.dumps({"pages":len(pages),"packets":len(pages),"counts":{str(k):dict(v) for k,v in counts.items()},"integrity_verified":True},ensure_ascii=False))

if __name__=="__main__":main()
