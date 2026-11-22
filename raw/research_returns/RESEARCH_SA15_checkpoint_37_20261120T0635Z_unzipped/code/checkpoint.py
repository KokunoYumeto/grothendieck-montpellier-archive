from pathlib import Path
import hashlib,zipfile,json,sys,datetime
w=Path(__file__).resolve().parents[1]; number=int(sys.argv[1]);name=f'RESEARCH_SA15_checkpoint_{number:02d}.zip';dest=w.parent/name
if dest.exists():raise RuntimeError("Refusing to overwrite an existing checkpoint")
prior={}
for p in sorted((w/'notes').glob('checkpoint_*_manifest.json')):
 if int(p.name.split('_')[1])>=number:continue
 j=json.loads(p.read_text())
 for r in j['files']:prior[r['path']]=(r['sha256'],r.get('held_by',j['archive']))
files=[]; kept=[]
for p in sorted(w.rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(w).as_posix()
 if rel==f'notes/checkpoint_{number:02d}_manifest.json':continue
 problem_image=p.suffix=='.png' and p.parent.name.endswith('_overflow_evidence')
 if (p.suffix in ['.png','.jpg','.jpeg','.dvi','.ps','.fmt','.aux','.out','.toc','.blg'] and not problem_image) or p.name in ['lualatex.log','missfont.log'] or '/__pycache__/' in rel:continue
 if '/sources/' in rel or rel.startswith('references/') or p.name in ['koblitz1975.pdf','koblitz1975.txt']:continue
 if p.suffix=='.pdf' and p.name!='RESEARCH_SA15_paper.pdf':continue
 if p.suffix=='.txt' and p.with_suffix('.pdf').exists():continue
 if p.suffix=='.zip':continue
 digest=hashlib.sha256(p.read_bytes()).hexdigest()
 deliverable=rel.startswith(('sections/','code/','notes/')) or rel in ['RESEARCH_SA15_paper.tex','RESEARCH_SA15_paper.pdf','RESEARCH_SA15_references.bib','RESEARCH_SA15_results.csv','RESEARCH_SA15_report.md','CHECK_EVENTS.tsv','PROGRESS_LEDGER.md'] or rel.endswith(('.tex','.bib','.md'))
 old=prior.get(rel);include=deliverable or not old or old[0]!=digest
 files.append(dict(path=rel,sha256=digest,size=p.stat().st_size,included=include,held_by=name if include else old[1]))
 if include:kept.append(p)
manifest=dict(archive=name,created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),files=files,exclusions='Attached material, third-party acquired full texts, rendered QA images except expressly discussed overflow evidence, TeX runtime/auxiliary files, previous ZIPs. All user-facing deliverables included.')
mp=w/'notes'/f'checkpoint_{number:02d}_manifest.json';mp.write_text(json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=8) as z:
 for p in kept:z.write(p,p.relative_to(w))
 z.write(mp,mp.relative_to(w))
if dest.stat().st_size>=500_000_000:raise RuntimeError('Checkpoint exceeds 500MB')
print(json.dumps({'file':str(dest),'bytes':dest.stat().st_size,'files':len(kept)+1,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}))
