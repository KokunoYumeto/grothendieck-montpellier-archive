"""Reconstruct the two readings, verify the recorded alignments and print the discrepancies."""
import csv
from collections import defaultdict
from html import escape
from pathlib import Path
ROOT = Path(__file__).resolve().parent
TAG = "K64-02"
def table(name):
    with (ROOT/(TAG+name)).open(encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))
def code(s):
    return "<code>"+escape(s).replace("\n"," ")+"</code>"
def run():
    blind = {(int(r["scan"]),r["place"]):r["what the crop shows"] for r in table("_blind.tsv")}
    alignment = table("_blind_alignment.tsv")
    wfile = ROOT/(TAG+"_witness_choices.tsv")
    witness = table("_witness_choices.tsv") if wfile.exists() else []
    output = ["# Comparison of the two visual readings","",
              "The same AI transcriber made both readings. The blind entries were recorded before reopening the corresponding page file. They include prose, symbols and brief location cues. An arrow drawn in a blind entry, a candidate word, or a proposed correction was checked against the local stroke. TeX syntax and typographic equivalents such as ∧ and its TeX command are treated alike. Condensed location cues do not stand for omitted manuscript text.","",
              "Each entry below gives the blind reading, the change to the first transcription or the reading retained, and the disposition. The script starts with the delivered page, reverses the recorded witness changes, checks the blind anchors in the audited page, and reverses the audit edits at their recorded offsets. It verifies the original bytes' text against the recorded first-reading hashes.",""]
    case_count=0
    counts_by_scan=[]
    import hashlib
    hashfile=ROOT/(TAG+"_first_reading_hashes.tsv")
    originalhash={int(r["scan"]):r["sha256_utf8_lf"] for r in table("_first_reading_hashes.tsv")}
    for n in range(15,28):
        delivered=(ROOT/"pages"/f"{TAG}_64_scan{n:03}.tex").read_text(encoding="utf-8")
        frozen=delivered
        for r in sorted([r for r in witness if int(r['scan'])==n],key=lambda r:int(r['final_offset']),reverse=True):
            pos=int(r['final_offset']);end=pos+len(r['final'])
            assert frozen[pos:end]==r['final'],(n,"witness",pos)
            frozen=frozen[:pos]+r['frozen']+frozen[end:]
        instructions=[r for r in alignment if int(r['scan'])==n]
        initial=frozen
        for r in reversed([r for r in instructions if r["operation"]=="edit"]):
            pos=int(r["offset"]);new=r["audited"]
            assert initial[pos:pos+len(new)]==new,(n,r["place"],"audit")
            initial=initial[:pos]+r["first"]+initial[pos+len(new):]
        assert hashlib.sha256(initial.encode()).hexdigest()==originalhash[n],n
        anchors={r['place']:r for r in instructions if r['operation'] in ('retain','anchor')}
        assert set(anchors)=={p for nn,p in blind if nn==n}
        output.extend([f"## Scan {n}",""])
        good=0
        scan_cases=0
        scan_edits=0
        places_edited=0
        for (nn,key),independent in blind.items():
            if n!=nn:continue
            loc=anchors[key]
            a=loc["audited"];pos=int(loc["offset"])
            assert frozen[pos:pos+len(a)]==a,(n,key)
            edits=[r for r in instructions if r['operation']=='edit' and r['place']==key and r['first']!=r['audited']]
            if not edits and not loc["decision"]:
                good+=1
                continue
            case_count+=1
            scan_cases+=1
            scan_edits+=len(edits)
            places_edited+=bool(edits)
            output.extend(["**"+key+"**","","Blind entry — "+code(independent),""])
            for r in edits:
                output.extend(["- "+code(r["first"])+" → "+code(r["audited"])])
            if edits:output.append("")
            if loc["decision"]:output.extend([loc["decision"],""])
            elif edits:output.extend(["The local strokes support the audited form at right. A retained doubt mark gives the readings still possible.",""])
        if good:
            noun = "entry has a matching reading" if good == 1 else "entries have matching readings"
            output.extend([f"{good} further independent {noun} at the recorded locations.",""])
        counts_by_scan.append((n,good+scan_cases,scan_cases,places_edited,scan_edits))
    output[2:2]=[f"{len(blind)} independent entries across 13 scans. {case_count} entries have a difference, a competing blind reading, or a location requiring an explicit decision. The second reading changed {sum(c[3] for c in counts_by_scan)} passages in {sum(c[4] for c in counts_by_scan)} individual edits.","",
        "| Scan | Blind entries | Entries discussed below | Passages edited | Individual edits |","|---|---:|---:|---:|---:|",
        *["| "+" | ".join(map(str,c))+" |" for c in counts_by_scan],""]
    (ROOT/(TAG+"_blind_compare.md")).write_text("\n".join(output),encoding="utf-8")
    return len(blind),case_count
if __name__=="__main__":
    print(run())

