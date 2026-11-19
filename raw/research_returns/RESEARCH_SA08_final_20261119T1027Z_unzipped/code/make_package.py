"""Create a new, never-overwritten checkpoint or final ZIP with a manifest.

Fetched publications and archive scans are retained in scratch for checking,
but not redistributed. Their URLs and inspection records are included.
Original attachments and previous ZIPs are never included.
"""
from pathlib import Path
import argparse, hashlib, json, zipfile
from datetime import datetime, timezone

p=argparse.ArgumentParser();p.add_argument('name');p.add_argument('--final',action='store_true');args=p.parse_args()
root=Path(__file__).resolve().parents[1]
if args.final:
    review=json.loads((root/'logs/PROGRESS_REVIEW_03.json').read_text())
    if not review.get('stop_required'):
        raise SystemExit('The binding final review has not been recorded.')
dest=root.parent/args.name
if dest.exists(): raise SystemExit('Refusing to overwrite '+str(dest))
excluded_parts={'sources','B_scan_images','C_cartan_pages','__pycache__','tex-cache'}
excluded_suffixes={'.zip','.aux','.toc','.out','.synctex.gz','.pyc','.png','.jpg','.jpeg','.partial'}
files=[]
approval=root/'logs/PDF_QA_APPROVED.json'
approved=json.loads(approval.read_text()) if approval.exists() else {}
required=['RESEARCH_SA08_paper.tex','RESEARCH_SA08_paper.pdf',
          'RESEARCH_SA08_results.csv','RESEARCH_SA08_references.bib',
          'RESEARCH_SA08_report.md','PROGRESS_LEDGER.md','CHECK_EVENTS.tsv']
for rel in required:
    if not (root/rel).is_file():
        raise SystemExit('Missing required deliverable: '+rel)
if 'Passed explicit image inspection:' not in approved.get('visual_review',''):
    raise SystemExit('The current PDF needs explicit image inspection.')
if hashlib.sha256((root/'RESEARCH_SA08_paper.pdf').read_bytes()).hexdigest()!=approved.get('pdf_sha256'):
    raise SystemExit('The current PDF differs from its visual approval.')
if args.final and not (root/'RESEARCH_SA08_report.md').read_text().startswith('INCOMPLETE\n'):
    raise SystemExit('The incomplete final report must say so on its first line.')
for rel,expected in approved.get('source_sha256',{}).items():
    file=root/rel
    if not file.exists() or hashlib.sha256(file.read_bytes()).hexdigest()!=expected:
        raise SystemExit('Source changed after approved PDF build: '+rel)
for file in sorted(root.rglob('*')):
    if not file.is_file(): continue
    rel=file.relative_to(root)
    if any(x in excluded_parts for x in rel.parts): continue
    if file.suffix in excluded_suffixes and not (file.suffix=='.png' and 'pdf_qa' in rel.parts): continue
    if file.name=='RESEARCH_SA08_paper.pdf' and hashlib.sha256(file.read_bytes()).hexdigest()!=approved.get('pdf_sha256'): continue
    if file.name=='PACKAGE_MANIFEST.json': continue
    data=file.read_bytes()
    # Preserve the exact bytes hashed here, even if an active research run
    # appends a note while the ZIP is being compressed.
    files.append((rel,data,len(data),hashlib.sha256(data).hexdigest()))
manifest={'package':args.name,'created_utc':datetime.now(timezone.utc).isoformat(),
    'status':('INCOMPLETE; final package after the required second consecutive no-movement review' if args.final else 'INCOMPLETE during active investigation'),
    'exclusions':'Original attachments; fetched full publications and archive scans; earlier ZIPs; unverified PDFs; transient LaTeX files.',
    'files':[{'path':str(rel),'bytes':size,'sha256':sha} for rel,data,size,sha in files]}
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for rel,data,size,sha in files:z.writestr(str(rel),data)
    z.writestr('PACKAGE_MANIFEST.json',json.dumps(manifest,indent=2))
if dest.stat().st_size>=500_000_000: raise SystemExit('Package exceeds 500 MB')
print(json.dumps({'file':str(dest),'bytes':dest.stat().st_size,'files':len(files)+1,'created_utc':manifest['created_utc']},indent=2))
