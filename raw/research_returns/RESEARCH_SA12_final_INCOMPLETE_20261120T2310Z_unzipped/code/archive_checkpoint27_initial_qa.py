"""Retain the already observed546-page QA before integrating later auxiliary proofs."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

root = Path(__file__).resolve().parents[1]
dest = root / 'qa/checkpoint27_initial_verified'
assert not dest.exists()
dest.mkdir()
pdf = root / 'build/RESEARCH_SA12_paper.pdf'
assert hashlib.sha256(pdf.read_bytes()).hexdigest() == '494cd186beadb129731efbfcdac822e8b5c1f2f3211374a4e0f67e6a07b20455'
shutil.copy2(pdf, dest / 'RESEARCH_SA12_paper_build178.pdf')
paths = sorted((root / 'qa').glob('checkpoint27_*.webp'))
paths += [root / 'qa/checkpoint27_actual_inspection.json', root / 'qa/checkpoint27_render.json', root / 'qa/pdf_verified_checkpoint27.json']
mapping = []
for p in paths:
    q = dest / p.name
    sha = hashlib.sha256(p.read_bytes()).hexdigest()
    p.rename(q)
    assert hashlib.sha256(q.read_bytes()).hexdigest() == sha
    mapping.append(dict(original_path=str(p.relative_to(root)), retained_path=str(q.relative_to(root)), sha256=sha))
record = dict(utc=datetime.now(timezone.utc).isoformat(), reason='The546-page build178 and all actual observed images are retained before integrating six later four-audited auxiliary statements. No archive or formal review is created.', certified_pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(), files=mapping)
(dest / 'relocation_map.json').write_text(json.dumps(record, indent=2) + '\n')
current = root / 'qa/pdf_verified.json'
verification = json.loads(current.read_text())
assert verification['sha256'] == record['certified_pdf_sha256']
verification['actual_inspection_record'] = str((dest / 'checkpoint27_actual_inspection.json').relative_to(root))
verification['inspection_relocation_map'] = str((dest / 'relocation_map.json').relative_to(root))
current.write_text(json.dumps(verification, indent=2) + '\n')
print(json.dumps(dict(retained_directory=str(dest.relative_to(root)), moved_files=len(mapping), certified_pdf_sha256=record['certified_pdf_sha256'])))
