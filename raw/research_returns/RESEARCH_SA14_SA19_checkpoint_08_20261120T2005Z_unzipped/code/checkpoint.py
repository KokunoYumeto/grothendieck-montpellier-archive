"""Create an immutable timed checkpoint with an explicit file manifest.

Only project deliverables, research notes, programs and outputs are included.
Inputs, downloaded primary sources, generated QA images and older ZIPs are not.
"""
from pathlib import Path
import csv,hashlib,io,json,sys,zipfile,datetime
root=Path(__file__).resolve().parents[1]
number=int(sys.argv[1]);name=f'RESEARCH_SA14_SA19_checkpoint_{number:02d}.zip'
target=root/name
if target.exists():raise SystemExit('Refusing to overwrite an existing checkpoint')
selected=[];excluded=[]
for p in root.rglob('*'):
    if not p.is_file():continue
    rel=p.relative_to(root);parts=rel.parts
    if parts[0] in ['upload','background','sources','tmp']:continue
    if any(x in parts for x in ['sources','__pycache__']):continue
    if p.suffix.lower() in ['.zip','.png','.jpg','.jpeg','.aux','.fls','.fdb_latexmk','.toc','.out','.pyc']:continue
    if p.suffix.lower()=='.pdf' and p.name!='RESEARCH_SA14_SA19_paper.pdf':continue
    if parts[0] not in ['code','sections','work','output'] and not (p.name.startswith('RESEARCH_SA14_SA19_') or p.name in ['CHECK_EVENTS.tsv','PROGRESS_LEDGER.md']):continue
    selected.append(p)
manifest=io.StringIO();w=csv.writer(manifest,delimiter='\t')
w.writerow(['path','bytes','sha256','included_in','unchanged_in_earlier_checkpoint'])
for p in sorted(selected):
    data=p.read_bytes();w.writerow([str(p.relative_to(root)),len(data),hashlib.sha256(data).hexdigest(),name,''])
meta={'checkpoint':number,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':len(selected),'previous_checkpoint_dependencies':[],
      'pdf_available':(root/'RESEARCH_SA14_SA19_paper.pdf').exists(),
      'note':'Timed snapshot of all current deliverables and own research files. No unchanged own files are omitted, so no earlier checkpoint is needed to restore this snapshot. Inputs, downloaded external sources and rendered QA images are intentionally excluded.'}
qa=sorted((root/'code').glob('visual_qa_*.json'))
meta['latest_visual_qa']=str(qa[-1].relative_to(root)) if qa else None
with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=8) as z:
    for p in selected:z.write(p,p.relative_to(root))
    z.writestr('FILE_MANIFEST.tsv',manifest.getvalue())
    z.writestr('CHECKPOINT_STATUS.json',json.dumps(meta,indent=2)+'\n')
if target.stat().st_size>=500_000_000:raise SystemExit('Checkpoint exceeds 500 MB; split before upload')
print(json.dumps(dict(path=str(target),bytes=target.stat().st_size,**meta),indent=2))
