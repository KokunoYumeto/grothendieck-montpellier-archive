from pathlib import Path
from datetime import datetime,timezone
import csv,json,hashlib,zipfile,shutil,re
root=Path('/workspace/scratch/59e0d6e3e1d5');p=root/'GHOSTS_package'
now=datetime.now(timezone.utc)
verification='''# Final artifact verification\n\nRun GHOSTS-20261121. Final mathematical status: all21 treated question rows have proved or refuted dispositions at the explicit scope in the paper. No unchecked candidate is used as a conclusion.\n\n## Mathematical checks\n\nEvery accepted proof received a complete reading; CHECK_EVENTS.tsv records the actual method, model identity, run, date, outcome and source locator. The new complex minimum24 uses a computer-assisted finite proof. Its mathematical exhaustiveness was independently checked by root, bounded_specialization, cm_transport and prime_arithmetic. Root separately regenerated the entire original catalog/comparison, then executed the self-contained portable program to PASS W04. Target, projector, sign symmetry and upper certificate were also checked independently in all70 integral exterior coordinates. The program uses exact integer arithmetic and no external input files. These checks are not described as proof-assistant verification.\n\n## Document checks\n\nThe final PDF has69 pages. The final LaTeX build has no unresolved citations, unresolved references, duplicate-label warnings or overfull boxes. All55 theorem/proposition/lemma/corollary environments have explicit proof blocks. Underfull line notices in bibliography/table paragraphs are typographical and do not indicate missing content.\n\nAll69 pages were rendered and visually reviewed in six contact sheets. Bounded_specialization inspected pages1–24 and enlarged1,11,17,19,23,24. Prime_arithmetic inspected25–36 and enlarged34–38 at130dpi. CM_transport inspected37–48 and61–69, enlarging37,45,46,48,64,65,67,69. Root inspected49–60 and checked the final single-line reflow. No clipped content, missing mathematical glyphs, overlapping formulas or table collisions was observed. Long bibliography URLs and the repeated framework-table headers render within the margins.\n\n## Archive checks\n\nThe final ZIP is tested for CRC integrity and every archived file is compared with its recorded SHA-256 manifest entry. It includes the six requested deliverables, PDF reading copy, all section/bibliography files, proof and source audits, computational scripts and outputs. It excludes temporary TeX build files, rendering images, Python bytecode, and earlier checkpoint ZIPs. The original supplied source attachments remain separate and are referenced at exact locators.\n\nTwo checkpoints were captured at their45-minute schedule. Final completion occurs before the next checkpoint and before the first three-hour progress review; no unscheduled checkpoint or fictional stagnation review is recorded.\n'''
(p/'research/FINAL_VERIFICATION.md').write_text(verification)
meta=p/'research/RUN_METADATA.json';d=json.loads(meta.read_text())
d.update(status='COMPLETED at the explicit scope of the final paper',completed_utc=now.isoformat(),elapsed_seconds=(now-datetime.fromisoformat(d['started_utc'])).total_seconds(),timed_progress_reviews_performed=0,stopping_reason='All treated question rows resolved before the first scheduled three-hour review',next_checkpoint_due_utc=None)
meta.write_text(json.dumps(d,indent=2)+'\n')
with (p/'LEDGER.md').open('a') as f:
 f.write('\n## Final package verification — '+now.strftime('%Y-%m-%d %H:%M:%S UTC')+'\n\n')
 f.write('The69-page paper and all requested audit files are complete. All21 treated question rows are resolved at their stated scopes. Every accepted proof has a complete-read event. The portable W04 certificate and the separate root rerun pass. The final PDF has no unresolved references/citations or overfull boxes, and all pages have been visually reviewed. Final archive CRC and per-file SHA-256 checks are performed by the packaging script. Completion precedes the next45-minute checkpoint and the first three-hour progress review; no unscheduled checkpoint or stagnation review is added.\n')
shutil.copy2(__file__,p/'research/finalize_package.py')
# Do not admit unresolved current question rows or missing required deliverables.
questions=list(csv.DictReader((p/'QUESTIONS.tsv').open(),delimiter='\t'))
assert len(questions)==21 and all('proved' in r['state'] or 'refuted' in r['state'] for r in questions)
required=['GHOSTS.tex','GHOSTS.pdf','QUESTIONS.tsv','LEDGER.md','CHECK_EVENTS.tsv','IMPLICATIONS.md','TRANSCRIPTION_NOTES.tsv']
assert all((p/f).is_file() for f in required)
assert 'PASS W04' in (p/'research/w_exact24_certificate.out').read_text()
assert 'PASS W04' in (p/'research/w_exact24_certificate.root.out').read_text()
log=(root/'work/texbuild/build10.txt').read_text()
assert not any(s in log for s in ['undefined','Overfull','multiply defined','LaTeX Error'])
files=[]
for f in sorted(p.rglob('*')):
 if not f.is_file() or '__pycache__' in f.parts:continue
 if f.name in ['DELIVERABLE_MANIFEST.tsv','missfont.log']:continue
 if f.suffix in {'.aux','.log','.toc','.zip','.pyc'}:continue
 if f.suffix=='.out' and f.parent.name!='research':continue
 files.append(f)
manifest=p/'DELIVERABLE_MANIFEST.tsv'
manifest.write_text('relative_path\tbytes\tsha256\n'+''.join(f'{f.relative_to(p)}\t{f.stat().st_size}\t{hashlib.sha256(f.read_bytes()).hexdigest()}\n' for f in files))
files.append(manifest)
zip_path=root/'GHOSTS_final.zip'
assert not zip_path.exists(), 'Refusing to replace an existing final archive'
with zipfile.ZipFile(zip_path,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for f in files:z.write(f,f.relative_to(p))
with zipfile.ZipFile(zip_path) as z:
 assert z.testzip() is None
 assert not any('checkpoint_' in name.lower() and name.endswith('.zip') for name in z.namelist())
 entries=list(csv.DictReader(z.read('DELIVERABLE_MANIFEST.tsv').decode().splitlines(),delimiter='\t'))
 for entry in entries:
  data=z.read(entry['relative_path'])
  assert len(data)==int(entry['bytes']) and hashlib.sha256(data).hexdigest()==entry['sha256']
print(json.dumps({'file':str(zip_path),'bytes':zip_path.stat().st_size,'entries':len(files),'pages':69,'check_events':sum(1 for _ in (p/'CHECK_EVENTS.tsv').open())-1,'sha256':hashlib.sha256(zip_path.read_bytes()).hexdigest(),'completed_utc':now.isoformat()}))
