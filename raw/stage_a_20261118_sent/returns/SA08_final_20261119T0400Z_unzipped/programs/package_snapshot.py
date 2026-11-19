"""Package a dated working snapshot, or final deliverable, without input copies.
External published full texts/OCR are retrievable by the audited download scripts;
we preserve retrieval metadata and authored checks rather than redistribute them.
"""
import argparse,datetime,hashlib,json,pathlib,re,time,zipfile
R=pathlib.Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--name',required=True);p.add_argument('--due');a=p.parse_args()
if a.due:
 due=datetime.datetime.fromisoformat(a.due.replace('Z','+00:00'))
 while datetime.datetime.now(datetime.timezone.utc)<due:time.sleep(min(1,max(0,(due-datetime.datetime.now(datetime.timezone.utc)).total_seconds())))
D=R/'outputs';D.mkdir(exist_ok=True)
path=R.parent/a.name
if path.exists():raise SystemExit('Refusing to overwrite existing archive')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (D/'progress.log').open('a') as f:f.write(now+'\tCHECKPOINT\t'+a.name+'; complete current authored work and audit metadata.\n')
files=[];skipped=[]
for f in sorted(R.rglob('*')):
 if not f.is_file():continue
 q=f.relative_to(R);s=q.as_posix()
 if ('/logs/' in '/'+s and ('search' in f.name or 'web_' in f.name)) or s.startswith(('sources/','work/numbered/','work/reference_pdfs/','research/','checkpoint_metadata/')) or '__pycache__' in s or '/references/' in s or f.suffix.lower() in ('.pdf','.png','.dvi','.zip') or s.endswith(('_entries_source.json','_scan_index.json','embedded_source.json','embedded_read.txt','sga4_excerpt.txt','Garvin1998.txt')):
  skipped.append({'path':s,'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()});continue
 files.append(f)
meta={}
for f in sorted(list((R/'research').rglob('*.json'))+list((R/'logs').glob('*search*.json'))):
 try:data=json.loads(f.read_text())
 except Exception:continue
 raw=json.dumps(data,ensure_ascii=False)
 meta[str(f.relative_to(R))]={'request':data.get('request',data.get('query',data.get('queries'))),'urls':sorted(set(re.findall(r'https?://[^\s<>"\\)]+',raw))),'source_refs':sorted(set(re.findall(r'turn\d+(?:search|view|fetch)\d+',raw))),'raw_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'note':'Primary source text bodies omitted; authored source assessments are in work records.'}
manifest={'created_utc':now,'archive':a.name,'previous_checkpoints':[x.name for x in sorted(R.parent.glob('SA08_checkpoint_*.zip'))],'included':[str(f.relative_to(R)) for f in files],'excluded_retrievable_inputs_and_published_source_cache':skipped,'restoration':'Extract archive, restore attached zip contents through programs/setup.py, and use download/OCR scripts only if source-cache reinspection is needed. Original supplied attachments are intentionally absent.'}
with zipfile.ZipFile(path,'x',zipfile.ZIP_DEFLATED,compresslevel=8) as z:
 for f in files:z.write(f,f.relative_to(R))
 z.writestr('research/retrieval_audit.json',json.dumps(meta,ensure_ascii=False,indent=2))
 z.writestr('SNAPSHOT_MANIFEST.json',json.dumps(manifest,ensure_ascii=False,indent=2))
 z.writestr('RESTORE.md','# Restoring this snapshot\n\nThis archive contains the current authored tables, proof audits, programs, outputs and retrieval metadata. Re-extract the two original attached archives using programs/setup.py. Full copyrighted published PDFs and OCR are not redistributed; their URLs, hashes and retrieval scripts are retained. No earlier checkpoint is embedded.\n')
print(json.dumps({'archive':str(path),'files':len(files),'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'created_utc':now}))
