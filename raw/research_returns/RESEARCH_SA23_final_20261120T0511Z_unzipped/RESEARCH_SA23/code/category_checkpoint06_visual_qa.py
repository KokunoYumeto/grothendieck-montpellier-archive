"""Bind the actual five-page visual inspection to the final checkpoint PDF."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import time

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('mode', choices=['start', 'finish'])
parser.add_argument('--manifest', required=True)
parser.add_argument('--sha256', required=True)
parser.add_argument('--pages', required=True, nargs='+', type=int)
args = parser.parse_args()
manifest_path = ROOT / args.manifest
manifest = json.loads(manifest_path.read_text())
pdf = ROOT / 'RESEARCH_SA23_paper.pdf'
pdf_hash = hashlib.sha256(pdf.read_bytes()).hexdigest()
assert pdf_hash == manifest['pdf_sha256'] == args.sha256
assert args.pages[-1] == manifest['pdf_pages']
assert set(args.pages).issubset(set(manifest['pages_rendered']))
images = dict(zip(manifest['pages_rendered'], manifest['rendered']))
image_records = [
    {'page': page, 'path': images[page],
     'sha256': hashlib.sha256((ROOT / images[page]).read_bytes()).hexdigest()}
    for page in args.pages]
start_path = ROOT / 'logs/category_checkpoint06_visual_QA_start.json'
finish_path = ROOT / 'logs/category_checkpoint06_visual_QA_finish.json'
if args.mode == 'start':
    assert not start_path.exists(), 'Do not replace an earlier review start.'
    record = {'started_utc': datetime.now(timezone.utc).isoformat(),
              'started_monotonic': time.monotonic(),
              'pdf_path': str(pdf.relative_to(ROOT)),
              'pdf_sha256': pdf_hash, 'pdf_pages': manifest['pdf_pages'],
              'manifest_path': args.manifest,
              'manifest_sha256': hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
              'planned_pages': args.pages, 'images': image_records,
              'scope': 'Five actual displayed page images; not a full-document visual review.'}
    destination = start_path
else:
    record = json.loads(start_path.read_text())
    assert record['pdf_sha256'] == pdf_hash
    assert record['planned_pages'] == args.pages
    assert record['images'] == image_records
    assert record['manifest_sha256'] == hashlib.sha256(manifest_path.read_bytes()).hexdigest()
    assert (ROOT / 'notes/category_checkpoint06_visual_QA.md').exists()
    assert not finish_path.exists(), 'Do not replace an earlier review finish.'
    record.update(completed_utc=datetime.now(timezone.utc).isoformat(),
                  elapsed_seconds=time.monotonic()-record['started_monotonic'],
                  actual_pages_inspected=args.pages,
                  result='All five page images individually displayed and inspected; findings in notes/category_checkpoint06_visual_QA.md')
    destination = finish_path
destination.write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
