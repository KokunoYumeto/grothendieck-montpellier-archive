#!/usr/bin/env python3
"""Create one immutable scheduled checkpoint; never nests earlier ZIPs."""
from pathlib import Path
import argparse,datetime,hashlib,json,zipfile,time
root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('number',type=int);p.add_argument('--due',required=True)
a=p.parse_args();now=datetime.datetime.now(datetime.timezone.utc)
due=datetime.datetime.fromisoformat(a.due)
if now<due:raise SystemExit('Checkpoint not yet due; no ZIP created.')
target=root.parent/f'RESEARCH_SA22_checkpoint_{a.number:02d}.zip'
if target.exists():raise SystemExit('Immutable checkpoint already exists; refusing overwrite.')
start=time.perf_counter()
published_pdf=root/'RESEARCH_SA22_paper.pdf'
if published_pdf.exists():
 build_record=json.loads((root/'logs/integrated_build_summary.json').read_text())
 qa_record=json.loads((root/'logs/paper_visual_qa.json').read_text())
 pdf_hash=hashlib.sha256(published_pdf.read_bytes()).hexdigest()
 if build_record.get('overfull_above_2pt') or build_record.get('undefined_warnings') or build_record.get('missing_glyphs') or build_record.get('rerun_warnings'):
  raise SystemExit('Publication blocked: unresolved compiler issues.')
 if pdf_hash!=qa_record.get('pdf_sha256') or not str(qa_record.get('inspection','')).startswith('PASS'):
  raise SystemExit('Publication blocked: this PDF lacks a matching passed visual inspection.')
 if 'pdf_sha256' in build_record and pdf_hash!=build_record['pdf_sha256']:
  raise SystemExit('Publication blocked: inspected PDF differs from the latest build.')
 stale=[name for name,digest in build_record.get('source_hashes_after',{}).items()
        if hashlib.sha256((root/name).read_bytes()).hexdigest()!=digest]
 if stale:
  raise SystemExit('Publication blocked: sources changed after the inspected build: '+repr(stale))
source_manifest=[]
for f in sorted((root/'literature').rglob('*')):
 if f.is_file():source_manifest.append({'path':str(f.relative_to(root)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
(root/'notes/source_file_manifest.json').write_text(json.dumps({'at':now.isoformat(),'note':'Downloaded literature and supplied scans are not redistributed. Bibliography, exact hashes and retrieval logs identify every source. Authored proof material, certificates, logs and current deliverables are included.','files':source_manifest},indent=2))
note=root/f'notes/CHECKPOINT_{a.number:02d}.md'
note.write_text(f'''# Scheduled checkpoint {a.number:02d}\n\nCreated {now.isoformat()}; due {due.isoformat()}. This is a preservation snapshot. Any formal movement review due at the same time is recorded separately in PROGRESS_LEDGER.md and logs/progress_review_*.json.\n\nAll authored deliverables, registries, proof/source notes, code and logs are included. Raw downloaded literature and source-scan image files are identified by the source manifest and fetch logs; original attachments are omitted. Earlier immutable checkpoint ZIPs are neither changed nor nested. Any paper PDF present has passed the recorded build/visual gate.\n\nFirst mandatory progress review scheduled for19 November2026 17:39UTC /18:39Europe/Berlin; subsequent reviews are hourly. The ledger records the actual review times. Next checkpoint:{(due+datetime.timedelta(minutes=45)).isoformat()}.\n''')
files=[]
for f in sorted(root.rglob('*')):
 if not f.is_file():continue
 rel=f.relative_to(root)
 if rel.parts[0] in {'literature','build','__pycache__'}:continue
 if '__pycache__' in rel.parts or f.suffix in {'.zip','.pyc'}:continue
 if rel.parts[0]=='qa' and f.suffix.lower() not in {'.txt','.json','.md'} and not f.name.startswith('paper_'):continue
 if f.suffix=='.pdf' and rel.parts[0]=='qa':continue
 files.append(f)
names={root.name+'/'+str(f.relative_to(root)) for f in files}
previous=root.parent/f'RESEARCH_SA22_checkpoint_{a.number-1:02d}.zip'
if previous.exists():
 with zipfile.ZipFile(previous) as z:missing=set(z.namelist())-names
 if missing:raise SystemExit('Earlier checkpoint files missing: '+repr(sorted(missing)))
inventory={'checkpoint':a.number,'created_utc':now.isoformat(),'due_utc':due.isoformat(),'previous_checkpoint':previous.name if previous.exists() else None,'file_count_before_inventory':len(files),'files':[{'path':str(f.relative_to(root)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in files]}
ip=root/f'notes/checkpoint_{a.number:02d}_inventory.json';ip.write_text(json.dumps(inventory,indent=2));files.append(ip)
with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for f in files:z.write(f,root.name+'/'+str(f.relative_to(root)))
assert target.stat().st_size<500_000_000
with zipfile.ZipFile(target) as z:assert z.testzip() is None
result={'path':str(target),'files':len(files),'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'seconds':round(time.perf_counter()-start,4)}
print(json.dumps(result,indent=2))
