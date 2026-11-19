#!/usr/bin/env python3
"""Index numbered mathematical statements; no inference of theorem validity."""
from pathlib import Path
import csv,re
root=Path(__file__).resolve().parent.parent
rows=[]
def arg(text,i):
    assert text[i]=='{'
    depth=1;j=i+1
    while depth:
        if text[j]=='{' and text[j-1]!='\\':depth+=1
        elif text[j]=='}' and text[j-1]!='\\':depth-=1
        j+=1
    return text[i+1:j-1],j
for path in sorted((root/'sections').glob('*.tex')):
    txt=path.read_text()
    for m in re.finditer(r'\\begin\{result\}',txt):
        pos=m.end();vals=[]
        for k in range(3):
            while txt[pos].isspace():pos+=1
            val,pos=arg(txt,pos);vals.append(val)
        ident,title,status=vals
        rows.append([ident,title,status,str(path.relative_to(root)), 'See explicit hypotheses and cited inputs in the statement', '', 'Exact statement and full proof are in the cited section; no unlabelled conjectural input is asserted.'])
rows.sort(key=lambda x: [int(v) if v.isdigit() else v for v in x[0].split('.')])
with (root/'RESEARCH_SA07_results.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']);w.writerows(rows)
print(f'Indexed {len(rows)} numbered statements.')
