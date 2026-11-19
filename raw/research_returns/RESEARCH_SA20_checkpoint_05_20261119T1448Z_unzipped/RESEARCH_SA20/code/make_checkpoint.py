#!/usr/bin/env python3
"""Create the scheduled immutable research checkpoint; invoke only when due."""
import hashlib, json, pathlib, sys, zipfile
ROOT=pathlib.Path(__file__).resolve().parents[1]
num=int(sys.argv[1]); out=ROOT.parent/f'RESEARCH_SA20_checkpoint_{num:02d}.zip'
if out.exists(): raise SystemExit('Refusing to overwrite an earlier checkpoint')
qa_path=ROOT/'logs/pdf_qa.json'
if (ROOT/'RESEARCH_SA20_paper.pdf').exists():
    qa=json.loads(qa_path.read_text())
    if qa.get('visual_review')!='passed': raise SystemExit('PDF visual QA has not passed')
    if qa['after']['over_2pt'] or qa['after']['missing_glyphs'] or qa['after']['undefined_refs']:
        raise SystemExit('PDF build QA has not passed')
    if hashlib.sha256((ROOT/'RESEARCH_SA20_paper.pdf').read_bytes()).hexdigest()!=qa['pdf_sha256']:
        raise SystemExit('PDF differs from the visually reviewed version')
    for rel,digest in qa['source_sha256'].items():
        if hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()!=digest:
            raise SystemExit('A paper source changed after visual review: '+rel)
files=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file(): continue
    rel=p.relative_to(ROOT)
    if '__pycache__' in rel.parts or 'sources' in rel.parts: continue
    if p.suffix.lower() in {'.zip','.pyc','.tar','.gz'}: continue
    if p.suffix.lower() in {'.pdf','.png','.jpg','.jpeg'}:
        if not (p.name=='RESEARCH_SA20_paper.pdf' or rel.parts[0]=='qa'):
            continue
    if p.suffix.lower() in {'.aux','.toc','.out','.fls','.fdb_latexmk','.synctex'}: continue
    files.append(p)
payload={str(p.relative_to(ROOT)):p.read_bytes() for p in files}
manifest=[{'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()} for rel,data in payload.items()]
(ROOT/'notes/checkpoint_file_manifest.json').write_text(json.dumps(manifest,indent=2))
payload['notes/checkpoint_file_manifest.json']=json.dumps(manifest,indent=2).encode()
with zipfile.ZipFile(out,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for rel,data in payload.items(): z.writestr(str(pathlib.Path('RESEARCH_SA20')/rel),data)
if out.stat().st_size>=500_000_000: raise SystemExit('Checkpoint unexpectedly exceeds 500 MB')
print(json.dumps({'path':str(out),'bytes':out.stat().st_size,'files':len(payload),'sha256':hashlib.sha256(out.read_bytes()).hexdigest()}))
