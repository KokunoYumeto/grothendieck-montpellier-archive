"""Package checked deliverables without inputs, runtime caches or older ZIPs."""
import hashlib
import json
import zipfile
from datetime import datetime,timezone
from pathlib import Path

root=Path(__file__).resolve().parents[1]
dest=root.parent/'RESEARCH_SA21_final.zip'
assert not dest.exists(), 'Do not silently overwrite a delivered final package.'
required=['RESEARCH_SA21_paper.tex','RESEARCH_SA21_paper.pdf','RESEARCH_SA21_results.csv','RESEARCH_SA21_references.bib','RESEARCH_SA21_report.md','PROGRESS_LEDGER.md','CHECK_EVENTS.tsv','RESEARCH_SA21_corrections.tsv','README.md']
assert all((root/name).is_file() for name in required)
assert (root/'RESEARCH_SA21_report.md').read_text().startswith('| Item |'), 'The final outcome table must come first.'
audit=json.loads((root/'code/outputs/final_metadata_audit.json').read_text())
assert not audit['build_errors_or_undefined_references'] and not audit['rerun_requested'] and not audit['overfull_boxes_above_2pt']
assert hashlib.sha256((root/'RESEARCH_SA21_paper.pdf').read_bytes()).hexdigest()==audit['pdf_sha256']
def include(p):
 rel=p.relative_to(root)
 if any(x in {'__pycache__','build','scans'} for x in rel.parts):return False
 if p.suffix in {'.zip','.pyc','.fmt','.aux','.toc','.out','.bbl','.blg'}:
  return p.suffix=='.out' and 'logs' not in rel.parts
 if p.suffix=='.pdf' and rel.as_posix()!='RESEARCH_SA21_paper.pdf':return False
 if 'sources' in rel.parts and p.suffix in {'.pdf','.png','.jpg'}:return False
 return True
now=datetime.now(timezone.utc).isoformat()
(root/'FINAL_PACKAGE_NOTE.md').write_text('# Final package\n\nCreated: '+now+'\n\nAI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). All requested mathematical tasks are resolved as recorded in the outcome table. This package contains current versions of all deliverables and retained work documentation from the checkpoints. Earlier ZIPs, supplied input files and source facsimiles, runtime dependencies, and transient unchecked build PDFs are excluded. The sole delivered PDF is the visually checked LuaLaTeX paper.\n')
files=sorted(p for p in root.rglob('*') if p.is_file() and include(p) and p.name!='RESEARCH_SA21_manifest.tsv')
manifest=root/'RESEARCH_SA21_manifest.tsv'
lines=['path\tbytes\tsha256']
for p in files:lines.append(f'{p.relative_to(root)}\t{p.stat().st_size}\t{hashlib.sha256(p.read_bytes()).hexdigest()}')
manifest.write_text('\n'.join(lines)+'\n')
files=sorted(files+[manifest])
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in files:z.write(p,Path('RESEARCH_SA21')/p.relative_to(root))
assert dest.stat().st_size<500_000_000
with zipfile.ZipFile(dest) as z:
 assert z.testzip() is None
 names=z.namelist()
 assert sum(n.endswith('.pdf') for n in names)==1
 assert not any(n.endswith('.zip') for n in names)
 assert all('RESEARCH_SA21/'+name in names for name in required)
print(json.dumps({'file':str(dest),'files':len(files),'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'created_utc':now},indent=2))
