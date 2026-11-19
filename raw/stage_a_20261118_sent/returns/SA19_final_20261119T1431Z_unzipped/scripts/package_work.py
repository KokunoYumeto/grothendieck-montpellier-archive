"""Package authored work; omit supplied originals and external full-text copies.

Usage: python3 package_work.py checkpoint NN UTC_TIMESTAMP
       python3 package_work.py final 0 UTC_TIMESTAMP
The caller schedules checkpoint calls at the requested 45-minute interval.
"""
import pathlib,sys,zipfile,json,hashlib
base=pathlib.Path(__file__).resolve().parents[1]
root=base.parent
mode,number,utc=sys.argv[1:]
name=f'SA19_checkpoint_{int(number):02d}.zip' if mode=='checkpoint' else 'SA19.zip'
target=root/name
if target.exists(): raise SystemExit('Refusing to overwrite existing archive: '+str(target))
def authored(p):
    rel=p.relative_to(base)
    if p.suffix in {'.pdf','.zip','.pyc'} or '__pycache__' in rel.parts: return False
    if p.name.startswith('ocr_') and p.suffix=='.txt' and p.stat().st_size>1024: return False
    if rel.parts[0]=='source_audit' and (p.name.endswith('_numbered.txt') or p.name.endswith('_entries.json')): return False
    if 'research' in rel.parts:
        if p.suffix.lower() in {'.txt','.png','.jpg','.jpeg','.tif','.tiff','.webp'}: return False
        if p.suffix=='.json':
            try: obj=json.loads(p.read_text())
            except Exception: return True
            # Raw retrieved source text is reproducible from URLs and not redistributed.
            if isinstance(obj,dict) and ('content' in obj or 'results' in obj): return False
            if p.name.startswith(('web_','search_','research_')): return False
    return True
files=sorted(p for p in base.rglob('*') if p.is_file() and authored(p))
manifest={'archive':name,'utc':utc,'mode':mode,'files':[
    {'path':str(p.relative_to(base)),'bytes':p.stat().st_size,
     'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files],
    'excluded':'Original attached files and their verbatim working copies; third-party full PDFs/extracted text and raw retrieval response text; earlier checkpoint ZIPs. Bibliographic access records, original analysis, programs and their outputs are retained.',
    'resume':'Unpack the supplied SA19_Jacobiennes.zip once to source/ and this archive to SA19_work/. Read METHOD.md, progress.log and current workstream ledgers. Input hashes are in source_audit/source_manifest.json. Full external papers are reproducible from URLs in references and download logs.'}
with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files: z.write(p,str(p.relative_to(base)))
    z.writestr('PACKAGE_MANIFEST.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    if mode=='checkpoint':
        z.writestr('RESUME.md','# SA19 checkpoint\n\nCreated '+utc+'.\n\n'+manifest['resume']+'\n\nThis is a complete snapshot of authored work so far, not the final dossier. Existing workstreams have individual claims, entry verdicts, mathematical checks and literature ledgers; consolidation is still in progress. Never overwrite an older checkpoint. Next checkpoint is due 45 minutes after the previous scheduled interval.\n')
with zipfile.ZipFile(target) as z:
    bad=z.testzip()
    if bad: raise SystemExit('Corrupt member: '+bad)
print(json.dumps({'path':str(target),'files':len(files),'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'utc':utc}))
