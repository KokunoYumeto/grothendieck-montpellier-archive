from pathlib import Path
import re,json,hashlib,datetime
r=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
bib=r/'RESEARCH_SA23_references.bib'
raw=bib.read_text(encoding='utf-8')
matches=list(re.finditer(r'^@\w+\s*\{\s*([^,]+),',raw,re.M))
papers=[r/'RESEARCH_SA23_paper.tex',*sorted((r/'sections').glob('*.tex'))]
flags=[]
for i,m in enumerate(matches):
    key=m.group(1).strip();end=matches[i+1].start() if i+1<len(matches) else len(raw)
    entry=raw[m.start():end].strip()
    if not re.search(r'not[\s~-]*opened|unopened|not.{0,35}(?:inspect|access)|metadata.only|abstract.only|not retrieved',entry,re.I):continue
    uses=[]
    for p in papers:
        lines=p.read_text(encoding='utf-8').splitlines()
        for j,line in enumerate(lines):
            if key in line:
                uses.append({'path':str(p.relative_to(r)),'line':j+1,'context':'\n'.join(f'{k+1}: {lines[k]}' for k in range(max(0,j-5),min(len(lines),j+7)))})
    flags.append({'key':key,'bib_line':raw[:m.start()].count('\n')+1,'entry':entry,'uses':uses})
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'bib_sha256':hashlib.sha256(bib.read_bytes()).hexdigest(),'entry_count':len(matches),'flagged_count':len(flags),'files_scanned':[str(p.relative_to(r)) for p in papers],'flags':flags}
(r/'notes/category_status_source_audit_extract.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
