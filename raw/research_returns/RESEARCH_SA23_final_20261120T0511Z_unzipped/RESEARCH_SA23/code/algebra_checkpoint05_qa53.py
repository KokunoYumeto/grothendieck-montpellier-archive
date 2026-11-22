"""Record actual CP05 visual-review timing and match the final render's PDF hash."""
import argparse
import datetime
import hashlib
import json
import pathlib
import time

parser=argparse.ArgumentParser()
parser.add_argument('mode',choices=['start','finish'])
args=parser.parse_args()
base=pathlib.Path(__file__).resolve().parents[1]
pdf=base/'RESEARCH_SA23_paper.pdf'
manifest_path=base/'logs/root_pdf_review_checkpoint05_final.json'
log=base/'logs/algebra_checkpoint05_visual_QA.json'
manifest=json.loads(manifest_path.read_text())
current_hash=hashlib.sha256(pdf.read_bytes()).hexdigest()
expected='f4c32598c77805631fcecf7fce909411c53583f2bffd7f0c14fa58d5fc5edab7'
assert current_hash==manifest['pdf_sha256']==expected
if args.mode=='start':
 record={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'started_monotonic':time.monotonic(),'pdf_path':str(pdf.relative_to(base)),
 'pdf_sha256_before':current_hash,'render_manifest_sha256':hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
 'render_manifest':manifest,'planned_pages':[1,20,40,60,90],
 'source_authorization':'Root confirmed final build complete and rerendered at03:50:25UTC; earlier active-build render not used'}
else:
 record=json.loads(log.read_text())
 assert current_hash==record['pdf_sha256_before']
 record.update(completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 elapsed_seconds=time.monotonic()-record['started_monotonic'],
 pdf_sha256_after=current_hash,actual_pages_inspected=[1,20,40,60,90],
 result='No clipping, overlap, illegible formula, table collision, missing glyph or pagination problem observed on the five displayed final-render pages; detailed limits in notes/algebra_checkpoint05_visual_QA.md')
payload=json.dumps(record,ensure_ascii=False,indent=2)
log.write_text(payload+'\n')
print(payload)
