"""Collate the image-first register with the individual page sources.
Run with Python 3 from any directory. The collation TSV locates a literal
page passage for each image description and records its editorial settlement.
The witness ledger allows the comparison to recover the pre-witness page.
"""
from pathlib import Path
from collections import defaultdict
import csv
import re

root=Path(__file__).resolve().parent
prefix="K105-02"
def table(name):
    with (root/f"{prefix}_{name}.tsv").open(newline="") as file:
        return list(csv.DictReader(file,delimiter="\t"))
def keyed(rows):
    result={(int(r["scan"]),r["place"]):r for r in rows}
    if len(rows)!=len(result):raise ValueError("Duplicate scan and place")
    return result
def normalize(s):return " ".join(s.split())
def escape(s):return s.replace("|",r"\|").replace("\n"," ")
def witness_outcome(col, scan, by_id):
    ids=col.get("witness place ids", "")
    if not ids:
        return "Audited reading retained."
    entries=[]
    for ordinal in ids.split(","):
        entry=by_id[scan, int(ordinal)]
        outcome=entry["result"]
        entries.append(f"{outcome}, `{entry['final source']}`")
    return " · ".join(entries)
def audited_source(scan,ledger):
    source=(root/"pages"/f"{prefix}_105_scan{scan:03}.tex").read_text()
    chunks=[];previous=0;shift=0
    for item in ledger:
        before=item["frozen mark"];after=item["final source"]
        at=int(item["frozen character offset"])+shift
        if source[at:at+len(after)]!=after:
            raise ValueError(f"Witness passage moved: scan {scan}, place {item['place id']}")
        chunks.extend((source[previous:at],before));previous=at+len(after)
        shift+=len(after)-len(before)
    chunks.append(source[previous:])
    return "".join(chunks)
def main():
    blind=keyed(table("blind"))
    matched=keyed(table("collation"))
    if blind.keys()!=matched.keys():raise ValueError("Unmatched image or source record")
    records=defaultdict(list)
    if (root/f"{prefix}_witness_changes.tsv").exists():
        for item in table("witness_changes"):records[int(item["scan"])].append(item)
    by_id={(n,int(r["place id"])):r for n,rows in records.items() for r in rows}
    sources={n:normalize(audited_source(n,records[n])) for n,_ in blind}
    differences=defaultdict(list)
    for key,seen in blind.items():
        n,place=key
        col=matched[key]
        if normalize(col["page source at audit"]) not in sources[n]:
            raise ValueError(f"Unlocated source in scan {n}: {place}")
        if col["comparison with first pass"]!="agrees":
            differences[n].append((place,seen["what the crop shows"],col))
    count=sum(map(len,differences.values()))
    report=["# Blind collation","","The image readings were recorded before the respective page file was opened on the second pass. The literal source anchors in the collation table were located in the audited page text. Editorial comparison accounts for descriptions of ink, orientation and overwriting that a character-by-character diff between prose and TeX cannot align.","",f"{len(blind)} registered places on {len(sources)} scans. {count} differences are itemized below; {len(blind)-count} passages agreed.",""]
    for n in sorted(sources):
        report.extend((f"## Scan {n:03}",""))
        if not differences[n]:
            report.extend(("No difference at the registered places.",""));continue
        report.extend(("| Place | Blind record | Difference from first pass | Audited source anchor | Settlement on the crop | Final status of associated marks |","|---|---|---|---|---|---|"))
        for place,reading,col in differences[n]:
            fields=(place,reading,col["comparison with first pass"],chr(96)+col["page source at audit"]+chr(96),col["settlement"],witness_outcome(col,n,by_id))
            report.append("| "+" | ".join(map(escape,fields))+" |")
        report.append("")
    (root/f"{prefix}_blind_compare.md").write_text("\n".join(report)+"\n")
    print(f"{len(blind)} pairs; {count} differences; {len(sources)} scans")
if __name__=="__main__":main()
