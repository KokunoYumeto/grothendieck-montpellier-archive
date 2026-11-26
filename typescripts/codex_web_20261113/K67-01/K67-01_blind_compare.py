import re
from pathlib import Path
import csv, json, hashlib

def argument(s, start):
    depth = 1
    i = start + 1
    while i < len(s) and depth:
        if s[i] == "\\" and i + 1 < len(s) and s[i+1] in "{}":
            i += 2
            continue
        depth += (s[i] == "{") - (s[i] == "}")
        i += 1
    return s[start+1:i-1], i

def replace_macro(s, name, transform):
    pattern = re.compile(r'\\'+name+r'(?![A-Za-z])\s*\{')
    pos = 0
    while m := pattern.search(s, pos):
        arg, end = argument(s, m.end()-1)
        val = transform(arg)
        s = s[:m.start()] + val + s[end:]
        pos = m.start()
    return s

def normal(s, *, deleted=True):
    # This tests text content. A separate collation records corrections,
    # font/hand distinctions, attachments, and non-textual visual evidence.
    s = replace_macro(s, "unsure", lambda v:v.split("|")[0])
    s = replace_macro(s, "deleted", (lambda v:v) if deleted else (lambda v:""))
    s = re.sub(r'\\overset\{\\handwritten\{\\sim\}\}',lambda _:r'\widetilde',s)
    s = re.sub(r'\\(?:mathrm|operatorname|text)(?:\s+)([A-Za-z])',r'\1',s)
    for macro in ("inserted","handwritten","uline","uuline","mathrm","operatorname","text","mathbin","textcircled","textsuperscript"):
        s = replace_macro(s, macro, lambda a:a)
    s = re.sub(r'\\(?:frac|tfrac)\s*\{?([0-9]+?)\}?\s*\{?([0-9])\}?',r'(\1/\2)',s)
    s = re.sub(r'\\(?:quad|qquad|displaystyle|scriptstyle|bigl|bigr)\b','',s)
    for x,y in [(r'\longrightarrow',r'\to'),(r'\rightarrow',r'\to'),(r'\geq',r'\ge'),(r'\tilde',r'\widetilde'),(r'\prime',"'"),(r'\,',''),(r'\ ',' '),("“",'"'),("”",'"'),("''",'"'),(chr(96)*2,'"')]:
        s=s.replace(x,y)
    return re.sub(r'[\s{}$]+','',s)

ROOT=Path(__file__).resolve().parent
ID="K67-01"
def reverse(text, edits):
    for i,j,have,want in reversed(edits):
        if text[i:j]!=have:
            raise ValueError(f"page change at {i} does not match the documented collation")
        text=text[:i]+want+text[j:]
    return text
def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()
def safe(s):
    return s.replace('|',r'\|').replace('\n',' ')
def main():
    data=json.loads((ROOT/f"{ID}_collation.json").read_text())
    readings=list(csv.reader((ROOT/f"{ID}_blind.tsv").open(),delimiter='\t'))[1:]
    special=[]
    counts={}
    excerpts={}
    for n,v in data["pages"].items():
        raw=(ROOT/'pages'/f"{ID}_67_scan{int(n):03}.tex").read_text()
        audited=reverse(raw,v["final_to_audit"])
        first=reverse(audited,v["audit_to_first"])
        assert (sha(raw),sha(audited),sha(first))==(v["finalsha"],v["auditsha"],v["firstsha"]),n
        excerpts[n]=first.splitlines()
    for i,(n,loc,b) in enumerate(readings,1):
        line, *context = data["locations"][str(i)]
        source = excerpts[n][line-1]
        if context:
            assert context[0] in source, (i,loc,context)
            source = context[0]
        count=counts.setdefault(n,[0,0])
        count[0]+=1
        rule=data["alignment"].get(str(i))
        if rule:
            anchor,kind,result=rule
            assert anchor in source,(i,anchor)
            special.append((n,f"{loc} (l. {line})",b,anchor,kind,result))
            if kind=='D':count[1]+=1
        else:
            assert normal(b) in normal(source) or normal(b) in normal(source,deleted=False),(i,loc,b)
    out=['# Blind collation','',f'{len(readings)} recorded places on {len(counts)} scans. The comparison uses the first page files, reconstructed from the final files and the recorded changes. All three sets of page hashes are checked. Every blind entry is compared at its recorded first-pass TeX line. For repeated short forms the collation also specifies a surrounding passage. Line citations refer to the first-pass files.','',
         '| Scan | Blind rows | Different readings |','|---:|---:|---:|']
    out.extend(f'| {n} | {allrows} | {changed} |' for n,(allrows,changed) in counts.items())
    out.extend(['','## Differences and their settlement before the witness','',
        '| Scan | Place | Blind record | First transcription at this place | Result on the crop |','|---:|---|---|---|---|'])
    def row(n,loc,b,anchor,kind,result):
        return f'| {n} | {safe(loc)} | '+chr(96)+safe(b)+chr(96)+' | '+chr(96)+safe(anchor)+chr(96)+f' | {safe(result)} |'
    out.extend(row(*x) for x in sorted(special,key=lambda r:int(r[0])) if x[4]=='D')
    out.extend(['','## Changes of markup and layout equivalents','',
        '| Scan | Place | Blind record | First transcription at this place | Resolution |','|---:|---|---|---|---|'])
    out.extend(row(*x) for x in special if x[4]!='D')
    out.extend(['','Other records agree in the letters or signs compared. Their full readings and locators are in K67-01_blind.tsv. The crop discussion, including every page-file change made at the audit, is in K67-01_audit.md. The last table of K67-01_doubts.md records subsequent witness decisions.',''])
    (ROOT/f'{ID}_blind_compare.md').write_text('\n'.join(out))
    print(f'{len(readings)} blind entries; {sum(x[1] for x in counts.values())} differences; {len(special)-sum(x[1] for x in counts.values())} markup or layout entries.')
if __name__=='__main__':
    main()
