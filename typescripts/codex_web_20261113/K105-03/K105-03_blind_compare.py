"""Compare the independent readings to their named places. Python 3, standard library."""
import csv
import re
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = "K105-03"
def compact(s):
    for a,b in (("’","'"),("′","'"),(r"\operatorname",r"\mathrm"),(r"\overline",r"\bar"),
                (r"\longrightarrow",r"\to"),(r"\colon",":"),(r"\&","&")):
        s=s.replace(a,b)
    # Use the first diplomatic candidate. Keep letters, case, indices, primes and punctuation.
    for _ in range(7):
        old=s
        s=re.sub(r"\\unsure\{([^{}]*)\}",lambda m:m[1].split("|")[0],s)
        s=re.sub(r"\\(?:mathrm|text|textit|textnormal|mspage|textcircled|uline|uuline|inserted|deleted|handwritten|margin)\s*(?:\{([^{}]*)\}|([A-Za-z]))",lambda m:m[1] or m[2] or "",s)
        if s==old:break
    s=re.sub(r"\\(?:quad|qquad|left(?!arrow)|right(?!arrow))\b|\\[,;! ]|\\\\|[{}$&\s]","",s)
    return s

def cell(s):
    return "<code>"+html.escape(s).replace("|","&#124;")+"</code>"
def read_tsv(name):
    with (ROOT / (BASE+name)).open(newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))
def main():
    loci=read_tsv("_blind_loci.tsv")
    rows=read_tsv("_blind.tsv")
    assert len(loci)==len(rows)
    report=["# Independent reading compared with the page files","",
            "The blind column was saved before opening the corresponding page file. The locator points to lines in that page. A recorded decision can concern the first reading, the independent reading, or both. Layout comparisons include lists of objects read around a square and printer banners read across several rows.",""]
    differences=0
    for a,b in zip(rows,loci):
        assert (a['scan'],a['place'])==(b['scan'],b['place'])
        n=a['scan'];loc=b['lines']; first,*last=map(int,loc.split('-'))
        lines=(ROOT/'pages'/(BASE+'_105_scan'+n+'.tex')).read_text().splitlines()
        locus="\n".join(lines[first-1:(last or [first])[0]])
        match=compact(a['what the crop shows']) in compact(locus)
        if not b['decision'] and match and b['first_match']=='yes':
            continue
        if not differences or prev!=n:
            report.extend(["",f"## Scan {n}","","| TeX line | Place | Blind reading | Comparison and decision |","|---|---|---|---|"])
        note=b['decision'] or ("Blind wording is present in the audited line." if match else "See the source and locus.")
        report.append(f"| {loc} | {a['place']} | {cell(a['what the crop shows'])} | {html.escape(note).replace('|','&#124;')} |")
        prev=n;differences+=1
    report[3:3]=[f"Compared {len(rows)} places. The register records {differences} differences or individually adjudicated comparisons, including differences in representation. An exact match here means a matching character sequence after typographical normalization.",""]
    (ROOT/(BASE+'_blind_compare.md')).write_text('\n'.join(report)+'\n')
    print(len(rows),differences)
if __name__=="__main__":
    main()
