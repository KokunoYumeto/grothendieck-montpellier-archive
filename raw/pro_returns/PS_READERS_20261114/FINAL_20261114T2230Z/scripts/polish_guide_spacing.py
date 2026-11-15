"""Separate joined editorial prose references; protect quotations and formulas."""
from pathlib import Path
import csv,json,re
from standardize_editorial import PROTECTED
P=Path(__file__).resolve().parents[1];R=P/'records'
def plain(s):
    s=re.sub(r'\b([A-Za-z]{2,})(?=\d)',r'\1 ',s)
    s=re.sub(r'\b([A-Za-z]{2,})(?=\()',r'\1 ',s)
    s=re.sub(r'\b(p|pp|cf)\.(?=\d)',r'\1.~',s)
    s=re.sub(r'(?<=[,;:])(?=[A-Za-z])',' ',s)
    s=re.sub(r"(?<='s)(?=\d)",' ',s)
    s=re.sub(r'\b(shift|to)(?=\[)',r'\1 ',s)
    s=s.replace('ChapterI','Chapter I').replace('an projective','a projective')
    return s
def polish(s):
    out=[];start=0
    for m in PROTECTED.finditer(s):
        prose=plain(s[start:m.start()])
        if m[0].startswith('$'):
            if (re.search(r'[A-Za-z]{2,}$',prose) and not m[0].startswith(("$'",'$^'))) or re.search(r'[,;:]$',prose):prose+=' '
            if out and out[-1].startswith('$') and re.match(r'[A-Za-z]',prose) and not re.match(r'(?:th|st|nd|rd|bis)\b',prose):prose=' '+prose
        out.extend([prose,m[0]]);start=m.end()
    out.append(plain(s[start:]));return ''.join(out)
rows=[]
for path in sorted((P/'guide_sections').glob('*.tex')):
    before=path.read_text();after=polish(before)
    assert [m[0] for m in PROTECTED.finditer(before)]==[m[0] for m in PROTECTED.finditer(after)],('Protected span changed',path.name)
    if before!=after:
        path.write_text(after)
        rows.append({'file':str(path.relative_to(P)),'before':before,'after':after,'reason':'Insert normal editorial prose spacing at references, prose/math boundaries and punctuation; repair the article before projective. All mathematical spans and exact quotations are asserted unchanged; no source reading is changed.'})
out=R/'GUIDE_SPACING_FIXES.tsv';old=list(csv.DictReader(out.open(),delimiter='\t')) if out.exists() else []
if rows:
    with out.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(old+rows)
print(json.dumps({'changed_guide_fragments':len(rows)}))
