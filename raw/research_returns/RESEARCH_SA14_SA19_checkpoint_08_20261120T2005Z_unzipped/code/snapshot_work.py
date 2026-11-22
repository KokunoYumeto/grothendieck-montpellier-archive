"""Integrate the currently written fragments, without editing agent files."""
from pathlib import Path
import re,json,datetime
root=Path(__file__).resolve().parents[1]
copied=[]
titles={
'B':"Seshadri's divisor question",'C':'Henselian comparison questions',
'D':'Quotient pathologies for Picard schemes','E':'The relative Picard functor',
'F':'The local fundamental group','G':'Canonical points on polarization torsors',
'H':'Geometric class field theory in higher degrees',
'I':'Endomorphisms of the residual complex','J':'The programme of 1964'}
owners={**dict.fromkeys('BCE','bce'),**dict.fromkeys('DGJ','dgj'),**dict.fromkeys('FHI','fhi')}
for part,owner in owners.items():
    src=root/'work'/owner/f'section_{part}.tex'
    if not src.exists(): src=root/'work'/owner/f'{part}.tex'
    if src.exists():
        content=src.read_text()
        if not re.search(r'\\section\{',content):content='\\section{'+titles[part]+'}\n'+content
        (root/'sections'/f'{part}.tex').write_text(content)
        copied.append(str(src.relative_to(root)))
for part,relative in [('E','work/bce/additional_leads.tex'),('H','work/fhi/priority.tex')]:
    src=root/relative
    if src.exists():
        with (root/'sections'/f'{part}.tex').open('a') as f:
            f.write('\n\n'+src.read_text()+'\n')
        copied.append(relative)
refs=[];keys=set()
for owner in ['root','bce','dgj','fhi']:
    p=root/'work'/owner/'references.bib'
    if not p.exists():continue
    content=p.read_text()
    for block in re.split(r'(?=^@)',content,flags=re.M):
        match=re.match(r'@\w+\s*\{\s*([^,]+)',block)
        if match and match[1] not in keys:
            keys.add(match[1]);refs.append(block.strip())
(root/'RESEARCH_SA14_SA19_references.bib').write_text('\n\n'.join(refs)+'\n')
report={'time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'copied':copied,'bibliography_entries':len(keys)}
(root/'code'/'snapshot_work_output.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
