"""Recompare the preserved blind readings with the page files.

The first comparison is saved as a sparse set of observations (one selected
passage per blind row). Later runs retain it and also compare the current text.
Run with Python 3 in the unpacked out directory. No packages are required.
"""
import csv
import difflib
import re
import sys
from pathlib import Path

base=Path(__file__).resolve().parent
prefix="K64-06"
def arg(s,i):
    depth=1
    j=i+1
    while j<len(s):
        if s[j]=="\\" and j+1<len(s) and not s[j+1].isalpha():
            j+=2;continue
        if s[j]=="{":depth+=1
        elif s[j]=="}":
            depth-=1
            if depth==0:return s[i+1:j],j+1
        j+=1
    raise ValueError("Unclosed group")
def groups(s,token):
    return [arg(s,m.end()-1)[0] for m in re.finditer(r"\\"+token+r"\s*\{",s)]
def strip_macros(s):
    pattern=r"\\(unsure|inserted|deleted|uline|uuline|text|mathrm|mathit|textnormal|operatorname|mathbin)\s*\{"
    while m:=re.search(pattern,s):
        a,j=arg(s,m.end()-1)
        if m[1]=="unsure":a=a.split("|")[0]
        s=s[:m.start()]+a+s[j:]
    return s
def normal(s):
    s=strip_macros(s).replace("’","'").replace("“","``").replace("”","''")
    s=s.replace("\\ "," ")
    s=re.sub(r"\\[,;!]","",s)
    s=s.replace("&","")
    s=re.sub(r"\\(?:quad|qquad|left|right|bigl|bigr|big|Bigl|Bigr|,|;|!)(?![a-zA-Z])","",s)
    s=s.replace(r"\longrightarrow",r"\to").replace(r"\rightarrow",r"\to")
    s=s.replace(r"\longmapsto",r"\mapsto").replace(r"\ldots","...")
    s=s.replace(r"\ast","*").replace(r"\vert","|")
    s=re.sub(r"\\tag\*\{(?:[^{}]|\{[^{}]*\})*\}","",s)
    s=re.sub(r"\s+","",s).replace("$","")
    return s.replace("{","").replace("}","")
def chosen(page,place,blind):
    key=place.partition(" ")[0]
    # Several readings on scan 68 divide the writing by physical line.
    # The TeX groups join an interlinear replacement across the two lines.
    if place in {"D2 right of unruled J","D3 over relative pinning"}:
        words=groups(page,"deleted")[1]
        head,_,tail=words.partition("une section")
        return head.strip() if place.startswith("D2") else "une section"+tail
    if place=="D4 before la donnée":return groups(page,"deleted")[2]
    if place=="I1 superscript substitute":return groups(page,"inserted")[0].split(" `",1)[0]
    if place=="I2 above struck words":
        return groups(page,"inserted")[0].partition(" ")[2].strip()
    if place=="S above the sixth line":return groups(page,"inserted")[-1]
    if place=="S spelling in third octahedron":
        return re.search(r"(\\unsure\{[^}]+\}|\w+) standart",page)[1]
    if place=="D9 after avec":return groups(page,"deleted")[-1]
    if place=="S isomorphism label":return groups(page,"overset")[-1]
    if place=="S parenthetic qualification":
        return re.search(r"\\uline\{NB\}\s+(.*?)\s+\$\\underline G",page)[1]
    if place=="S cancelled start before lambda":return groups(page,"deleted")[-1]
    if place=="S before revêtements":return groups(page,"deleted")[1]
    if place=="S struck ending before brace":
        tail=groups(page,"deleted")[-1]
        return re.search(r"(\\unsure\{[^}]+\}|\S+) le groupe des",tail)[0]
    if place in {"S first struck line island","S last word of second strike","S second struck line island"}:
        crossed=groups(page,"deleted")[0]
        if place=="S first struck line island":return r"\unsure{"+groups(crossed,"unsure")[0]+"}"
        if place=="S last word of second strike":return r"\unsure{"+groups(crossed,"unsure")[-1]+"}"
        after=crossed.partition("$Q_0$}")[2].lstrip()
        if after.startswith(r"\unsure"):
            return r"\unsure{"+groups(after,"unsure")[0]+r"} \illegible{"+groups(after,"illegible")[0]+"}"
        return r"\illegible{"+groups(after,"illegible")[0]+"}"
    if place=="S number remaining":
        return re.search(r"Il y en.*?deux",page)[0]
    if place in {"S crossed stabilizer index","S first crossed clause","S crossed below opère","S struck tangent at next line"}:
        i={"S crossed stabilizer index":0,"S first crossed clause":2,"S crossed below opère":3,"S struck tangent at next line":4}[place]
        return groups(page,"deleted")[i]
    if place=="S tangent tensor power":return re.findall(r"\\\[(.*?)\\\]",page,re.S)[-1].split(r"\xrightarrow")[0].strip()
    if place=="U5 last parenthesis":
        return re.search(r" section (.*?)\n% archive",page)[1].strip()
    indexed=re.fullmatch(r"([DIMUPF])(\d+)",key)
    if indexed:
        group,n=indexed[1],int(indexed[2])-1
        if group=="F": seq=re.findall(r"\\\[(.*?)\\\]",page,re.S)
        else:seq=groups(page,{"D":"deleted","I":"inserted","M":"margin","U":"unsure","P":"mspage"}[group])
        if n>=len(seq):return "[selector absent]"
        value=seq[n].strip()
        return value.split("|")[0] if group=="U" else value
    if key=="N":
        # Numbered display labels, including the labels written in diagram cells.
        labels=re.findall(r"\\tag\*\{(?:\\deleted\{)?\((\d+)\)|\\text\{\((\d+)\)\}",page)
        return ", ".join(a or b for a,b in labels)
    if key=="A":
        return re.search(r"% archive sheet number: *(.*)",page)[1].strip()
    if key=="S":
        whole=normal(page)
        wanted=normal(blind)
        if wanted in whole:return blind
        # Near-match for locating a divergent phrase. Mark its status explicitly
        # and preserve the original comparison in the first-observation table.
        match=difflib.SequenceMatcher(None,wanted,whole,autojunk=False).find_longest_match(0,len(wanted),0,len(whole))
        start=max(0,match.b-match.a)
        return "[nearest] "+whole[start:start+len(wanted)]
    raise ValueError(place)
def same(a,b):
    return normal(a)==normal(b)
def readtsv(path):
    if not path.exists():return []
    with path.open(encoding="utf-8",newline="") as f:return list(csv.reader(f,delimiter="\t"))[1:]
def write_table(path,header,rows):
    with path.open("w",encoding="utf-8",newline="") as f:
        writer=csv.writer(f,delimiter="\t",lineterminator="\n")
        writer.writerow(header);writer.writerows(rows)
def inline(s):
    import html
    return "<code>"+html.escape(s.replace("\n"," "),quote=False).replace("|","&#124;")+"</code>"
def main():
    samples=readtsv(base/f"{prefix}_blind.tsv")
    first=base/f"{prefix}_blind_first.tsv"
    original={(r[0],r[1]):r[2] for r in readtsv(first)}
    decisions={(r[0],r[1]):r[2] for r in readtsv(base/f"{prefix}_blind_decisions.tsv")}
    lines=["# Blind comparison of cote 64, scans 66–77","","The 203 blind readings were written from the images before the corresponding page file was reopened. Twenty-four differed on the first comparison. The tables retain the two original observations, the current LaTeX at each place and the decision on the ink. The raw readings and page-by-page audit are included in the ZIP.","","The comparison disregards formatting, thin spaces, editorial wrappers and unselected alternatives. Labels such as F4 or D1 identify the physical places recorded in the original blind table.",""]
    mismatches=0
    for n in sorted({r[0] for r in samples}):
        source=(base/"pages"/f"{prefix}_64_scan{int(n):03}.tex").read_text(encoding="utf-8")
        lines.extend([f"## Scan {int(n)}",""])
        diff=[]
        selected=[r for r in samples if r[0]==n]
        for _,place,eye in selected:
            now=chosen(source,place,eye)
            original.setdefault((n,place),now)
            was=original[n,place]
            if not same(eye,was):
                diff.append([place,eye,was,now,decisions[n,place]])
        mismatches+=len(diff)
        noun="difference" if len(diff)==1 else "differences"
        lines.append(f"{len(selected)} places compared. {len(diff)} {noun} on the first comparison.")
        if diff:
            lines.extend(["","| Place | Blind reading | Page at first comparison | Final page reading | Decision |","| --- | --- | --- | --- | --- |"])
            for place,eye,was,now,why in diff:
                lines.append("| "+" | ".join([place,inline(eye),inline(was),inline(now),why])+" |")
        lines.append("")
    lines.extend(["## Totals","",f"{len(samples)} places compared; {mismatches} differences in the first comparison."])
    if not first.exists():
        write_table(first,["scan","place","page_at_first_comparison"],[[n,p,v] for (n,p),v in original.items()])
    assert len(decisions)==mismatches
    with (base/f"{prefix}_blind_compare.md").open("w",encoding="utf-8",newline="\n") as report:
        report.write("\n".join(lines)+"\n")
    if len(sys.argv)>1:
        n=sys.argv[1]
        for s,p,v in samples:
            if s==n and not same(v,original[s,p]):
                print(p,":",v,"<>",original[s,p])
    else:print(f"{len(samples)} places; {mismatches} first-comparison differences")
if __name__=="__main__":main()
