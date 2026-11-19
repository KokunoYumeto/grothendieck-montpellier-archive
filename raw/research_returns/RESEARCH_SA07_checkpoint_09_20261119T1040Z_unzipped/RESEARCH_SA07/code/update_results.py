#!/usr/bin/env python3
"""Index numbered mathematical statements; no inference of theorem validity."""
from pathlib import Path
import csv,re
root=Path(__file__).resolve().parent.parent
rows=[]
pages={
 'A.1':'18:10-11', 'A.2':'18:11', 'A.3':'18:11-13',
 'A.4':'18:12-13', 'A.5':'18:53-62',
 'B.1':'18:5', 'B.2':'18:5;18:43', 'B.3':'18:43', 'B.4':'18:6',
 'C.1':'18:32-34;15:213-215', 'C.2':'18:35', 'C.3':'18:36-38',
 'C.4':'18:38-41', 'C.5':'18:41;RH19[II]',
 'D.1':'18:47-48', 'D.2':'18:42-45', 'D.3':'18:49-51',
 'D.4':'18:51', 'D.5':'18:53-62',
 'E.1':'15:207;15:219-221;15:225', 'E.2':'15:223',
 'E.3':'15:209-211;15:225-227',
 'F.1':'18:15-29', 'F.2':'18:9', 'F.3':'See assertion-level audit_claims.csv',
 'G.2':'18:5;18:13;18:43'
}
aux=(root/'RESEARCH_SA07_paper.aux').read_text() if (root/'RESEARCH_SA07_paper.aux').exists() else ''
pdf_pages=dict(re.findall(r'\\newlabel\{([A-G]\.\d+\.\d+)\}\{\{[^}]*\}\{([^}]+)\}',aux))
# These entries are explicitly discussed only as literature comparisons in
# the surrounding prose, and are not premises of the indicated proof.
comparison_only={'F.3.25':{'AuditGoodman2026','AuditShimura1998Gate'}}
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
    matches=list(re.finditer(r'\\begin\{result\}',txt))
    for index,m in enumerate(matches):
        pos=m.end();vals=[]
        for k in range(3):
            while txt[pos].isspace():pos+=1
            val,pos=arg(txt,pos);vals.append(val)
        ident,title,status=vals
        body_end=txt.index(r'\end{result}',pos)
        claim=' '.join(txt[pos:body_end].split())
        end=matches[index+1].start() if index+1<len(matches) else len(txt)
        proof=txt[pos:end]
        cited=[]
        for cm in re.finditer(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',proof):
            cited.extend(cm[1].split(','))
        cited=[key for key in cited if key not in comparison_only.get(ident,set())]
        local=sorted(set(re.findall(r'\b[A-G]\.\d+\.\d+\b',proof))-{ident})
        dependencies='; '.join(['result '+z for z in local]+['source '+z for z in sorted(set(cited))])
        if 'hypothes' in status.lower():
            dependencies+='; named conjectural hypotheses are stated explicitly in the claim'
        where=str(path.relative_to(root))+'; result '+ident
        if ident in pdf_pages:where+='; current PDF p. '+pdf_pages[ident]
        prefix='.'.join(ident.split('.')[:2])
        actual=sorted(set(re.findall(r'\b(?:18|15):\d+(?:--?\d+)?\b',proof)))
        manuscript='; '.join(actual) if actual else pages.get(prefix,'See named note entry in the full proof')
        note='The statement is reproduced in LaTeX notation; its stated scope and any remaining obligation are part of the claim.'
        if ident in comparison_only:
            note+=' Literature-comparison entries '+', '.join(sorted(comparison_only[ident]))+' are not proof dependencies; their individual access status remains in the source record.'
        rows.append([ident,title+'. '+claim,status,where,dependencies or 'Direct proof in the indicated section',manuscript,note])
ids=[r[0] for r in rows]
assert len(ids)==len(set(ids)), 'Duplicate result identifiers'
rows.sort(key=lambda x: [int(v) if v.isdigit() else v for v in x[0].split('.')])
with (root/'RESEARCH_SA07_results.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']);w.writerows(rows)
print(f'Indexed {len(rows)} numbered statements.')
