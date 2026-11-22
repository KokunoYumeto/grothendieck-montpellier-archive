"""Reproduce the independent-read comparison. Run in any directory with Python 3."""
import csv
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
def read_tsv(p):
    with p.open(newline="",encoding="utf-8") as f: return list(csv.reader(f,delimiter="\t"))[1:]
def split_pages(p):
    return {int(n): s for n,s in re.findall(r"(?ms)^%% SCAN (\d+)\n(.*?)(?=^%% SCAN |\Z)",p.read_text())}
def argument(s,i):
    depth = 1
    j = i
    while depth and j<len(s):
        if s[j] in "{}" and (j==0 or s[j-1]!="\\"):
            depth += 1 if s[j]=="{" else -1
        j += 1
    return s[i:j-1],j
def normalize(s,live=False):
    """Suppress encoding and layout; preserve the letters, alphabets and sign directions."""
    pattern=r"\\(unsure|deleted|inserted|handwritten|text|uline|uuline|underline|mathrm|operatorname|mathbin|mathpunct|textsuperscript)\{"
    pieces=[]
    while m:=re.search(pattern,s):
        pieces.append(s[:m.start()])
        a,end=argument(s,m.end())
        if m[1]=="unsure": a=a.split("|")[0]
        if m[1]!="deleted" or not live: pieces.append(normalize(a,live))
        s=s[end:]
    s="".join(pieces)+s
    s=unicodedata.normalize("NFC",s).replace("\u00ad","").replace("’","'")
    for x,y in [(r"\underset{\longleftarrow}{\lim}",r"\varprojlim"),(r"\underset{\longrightarrow}{\lim}",r"\varinjlim"),(r"\bar","@bar"),(r"\overline","@bar"),(r"\neq",r"\ne"),(r"\ldots","..."),(r"\quad",""),(r"\qquad",""),(r"\,",""),(r"\ ",""),(r"\`",""),(r"\circ)","°)"),("n^o","n°")]: s=s.replace(x,y)
    s=re.sub(r"\\(?:operatorname|mathrm|underline|uline|uuline|textsuperscript)(?![a-zA-Z])","",s)
    s=re.sub(r"[{}$\s]","",s)
    return s.replace("^o°","°").replace(r"^\circ)","°)").replace("n^o","n°")
def parts(s):
    return [normalize(x) for x in s.split(" ⫶ ")]
def has(s,reading):
    forms=(normalize(s),normalize(s,True))
    return all(any(x in form for form in forms) for x in parts(reading))
def safe(s): return s.replace("|",r"\|").replace("\n"," ")
def verbatim(s):
    """Make TeX and the transcriber's literal quotation strokes legible in a GFM cell."""
    fence = "`" * (1 + max((len(v) for v in re.findall(r"`+", s)), default=0))
    padding = " " if s.startswith(("`", " ")) or s.endswith(("`", " ")) else ""
    return fence + padding + safe(s) + padding + fence
def verify_witness(audited):
    if "witness check done " not in (ROOT/"progress.log").read_text(): return []
    actions={}
    for path in sorted((ROOT/"collation").glob("witness-review-*.tsv")):
        with path.open(newline="",encoding="utf-8") as f:
            for key,crop,other,why,action in csv.reader(f,delimiter="\t",quoting=csv.QUOTE_NONE):
                assert key not in actions, key
                actions[key]=(action,crop,why)
    reviewed=[];consumed=set()
    for n,source in audited.items():
        changes=[]
        for i,m in enumerate(re.finditer(r"\\(?:unsure|illegible)\{",source),1):
            key=f"{n}.{i}"
            if key not in actions: continue
            consumed.add(key)
            value,end=argument(source,m.end())
            action,crop,reason=actions[key]
            if action=="=": continue
            assert action.startswith(("!","+")),key
            target=action[1:]
            changes.append((m.start(),end,target))
            reviewed.append((n,1+source.count("\n",0,m.start()),source[m.start():end],target,crop,reason))
        final=source
        for start,end,target in reversed(changes):
            final=final[:start]+target+final[end:]
        path=ROOT/"pages"/f"K57-18_57_scan{n}.tex"
        assert final==path.read_text(),f"Difference outside adjudicated mark on scan {n}"
    assert consumed==set(actions)
    return reviewed



def run():
    first=split_pages(ROOT/"collation/first-reading.txt")
    audited=split_pages(ROOT/"collation/audited-reading.txt")
    decisions={(int(n),p):(a,b,why) for n,p,a,b,why in read_tsv(ROOT/"collation/decisions.tsv")}
    blind=read_tsv(ROOT/"K57-18_blind.tsv")
    places={(int(n),place) for n,place,_ in blind}
    assert len(places)==len(blind) and decisions.keys()<=places, "unmatched or duplicate blind location"
    reports=[]; pending=[]; moved=[]
    for num,place,reading in blind:
        n=int(num)
        page=(ROOT/"pages"/f"K57-18_57_scan{n}.tex").read_text()
        if (n,place) in decisions:
            a,b,why=decisions[n,place]
            assert has(first[n],a) and has(audited[n],b), (n,place,"source anchor")
            reports.append((n,place,a,reading,b,why))
            if not has(page,b) and has(audited[n],b): moved.append((n,place))
        elif not has(first[n],reading) or not has(audited[n],reading):
            pending.append((n,place,reading))
        elif not has(page,reading): moved.append((n,place))
    out=["# Independent reading and collation","",f"{len(blind)} image-only records were entered before reopening their page files. {len(reports)} required adjudication, including differences in the representation of the ink. The remaining {len(blind)-len(reports)-len(pending)} agree under the normalization in the accompanying script.","","The first and audited snapshots preserve the chronology. Each table entry gives the original, the independent reading and the decision taken on the scan. The final page files are checked separately for subsequent witness edits.","","| Scan | Place | First reading | Independent reading | Settled at audit | Ink or encoding decision |","|---|---|---|---|---|---|"]
    for n,place,a,reading,b,why in reports:
        out.append("| "+" | ".join((str(n),safe(place),verbatim(a),verbatim(reading),verbatim(b),safe(why)))+" |")
    if pending:
        out+=["","## Unadjudicated comparisons",""]+[f"- {n} {p} — {r}" for n,p,r in pending]
    if moved:
        out+=["","## Audited passages subsequently affected by the witness check",""]+[f"- Scan {n}, {p}." for n,p in moved]
    witness=verify_witness(audited)
    if witness:
        out.extend(["", "## Final witness decisions", "", f"The final pages reproduce the audited source byte for byte outside the {len(witness)} recorded witness edits. These decisions postdate the independent comparison.", "", "| Scan | Frozen source line | Frozen mark | Final form | Crop | Grounds |", "|---|---|---|---|---|---|"])
        out.extend("| "+" | ".join((str(n),str(line),verbatim(a),verbatim(b),safe(f"{n}-{crop}.jpg"),safe(why)))+" |" for n,line,a,b,crop,why in witness)
    (ROOT/"K57-18_blind_compare.md").write_text("\n".join(out)+"\n")
    print(f"{len(blind)} records; {len(reports)} adjudications; {len(pending)} pending. "
          f"{len(witness)} marked witness edits independently reproduce the final page files.")
    for row in pending:print(*row,sep="\t")
    return pending
if __name__=="__main__": raise SystemExit(bool(run()))

