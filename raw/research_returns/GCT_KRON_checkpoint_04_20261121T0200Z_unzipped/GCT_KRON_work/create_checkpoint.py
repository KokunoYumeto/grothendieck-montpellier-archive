#!/usr/bin/env python3
"""Create a complete, fresh scheduled checkpoint; never overwrite an archive."""
from pathlib import Path
import sys, json, datetime, csv, hashlib, zipfile, subprocess
ROOT=Path(__file__).resolve().parent
CWD=ROOT.parent
number=int(sys.argv[1])
meta=json.loads((ROOT/'RUN_METADATA.json').read_text())
start=datetime.datetime.fromisoformat(meta['started_utc'].replace('Z','+00:00'))
due=start+datetime.timedelta(minutes=45*number)
now=datetime.datetime.now(datetime.timezone.utc)
if now<due:
    raise SystemExit(f'Checkpoint {number:02} is not due until {due.isoformat()}')
archive=CWD/f'GCT_KRON_checkpoint_{number:02}.zip'
if archive.exists():
    raise SystemExit('Refusing to overwrite an earlier checkpoint')
subprocess.run([sys.executable,str(ROOT/'build_package.py')],check=True)
# External publications are recorded by source locator and hash, not redistributed.
def external_reference_copy(p):
    rel=p.relative_to(ROOT).as_posix()
    return (
        rel.startswith('agents/obstructions/SGA4_evidence/')
        or (rel.startswith('agents/archive/') and p.name.startswith('sga6_scan'))
        or rel.startswith('agents/archive/EGA_II_evidence/')
        or rel.startswith('agents/archive/DD2011_evidence/')
        or (rel.startswith('checks/') and p.name.startswith('WeilII_scan'))
    )
reference_rows=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and external_reference_copy(p):
        reference_rows.append([p.relative_to(ROOT).as_posix(),p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest(),'External primary-source reproduction; exact source and locator in agent notes'])
for p in sorted((CWD/'external_sources').rglob('*')):
    if p.is_file():
        reference_rows.append(['external_sources/'+p.relative_to(CWD/'external_sources').as_posix(),p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest(),'External primary source; exact URL and locator in source catalogs'])
with (ROOT/'REFERENCE_COPY_MANIFEST.tsv').open('w',newline='') as h:
    w=csv.writer(h,delimiter='\t')
    w.writerow(['local_reference_name','bytes','sha256','retrieval_note'])
    w.writerows(reference_rows)
state={
    'created_utc':now.isoformat(),'checkpoint':number,'run':meta['run_id'],
    'status':'WORK IN PROGRESS',
    'scheduled_due_utc':due.isoformat(),
    'next_checkpoint_due_utc':(start+datetime.timedelta(minutes=45*(number+1))).isoformat(),
    'first_review_due_utc':meta['first_review_due_utc'],
    'timed_reviews_completed':len(json.loads((ROOT/'TIMED_REVIEWS.json').read_text())) if (ROOT/'TIMED_REVIEWS.json').exists() else 0,
    'pdf_status':'Working PDF compiled and rendered; latest mathematical additions are in self-contained TeX. Final visual review remains required.',
    'reference_policy':'External publications and page reproductions are recoverable from exact URLs, locators and hashes, and are not copied into this ZIP. The user-supplied source corpus is included.'
}
(ROOT/'CHECKPOINT_STATE.json').write_text(json.dumps(state,indent=2))
with (ROOT/'LEDGER.md').open('a') as h:
    h.write(f'\n## Checkpoint {number:02}, {now.isoformat()}\n\nScheduled 45-minute checkpoint, due {due.isoformat()}. This is not a timed progress review. Includes the current complete work, source corpus, proof fragments, checks, computations, ledgers and working paper. Earlier checkpoint ZIPs are excluded.\n')
entries=[]
for base,arcbase in [(ROOT,'GCT_KRON_work'),(CWD/'sources','sources')]:
    for p in sorted(base.rglob('*')):
        if not p.is_file():continue
        if '__pycache__' in p.parts or p.suffix in {'.pyc','.fmt'}:continue
        if p.suffix.lower()=='.zip':continue
        if base==ROOT and external_reference_copy(p):continue
        entries.append((p,arcbase+'/'+p.relative_to(base).as_posix()))
entries.append((CWD/'upload'/'PROMPT(20261120-225936).md','PROMPT.md'))
with zipfile.ZipFile(archive,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    manifest=[]
    for p,arc in entries:
        data=p.read_bytes()
        z.writestr(arc,data)
        manifest.append({'name':arc,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
    z.writestr('PACKAGE_MANIFEST.json',json.dumps(manifest,indent=2))
with zipfile.ZipFile(archive) as z:
    bad=z.testzip()
    if bad:raise RuntimeError('ZIP CRC error: '+bad)
result={'archive':str(archive),'bytes':archive.stat().st_size,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'files':len(entries),'created_utc':now.isoformat()}
(ROOT/f'CHECKPOINT_{number:02}_RECEIPT.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result))

