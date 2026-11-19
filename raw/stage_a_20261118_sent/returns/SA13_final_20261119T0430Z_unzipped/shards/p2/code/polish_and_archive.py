#!/usr/bin/env python3
"""Mechanical final file cleanup; substantive judgments remain in authored records."""
from pathlib import Path
import datetime,shutil,json
O=Path(__file__).resolve().parents[1];ROOT=O.parents[2]
p=O/'directions.md';s=p.read_text()
for old,new in [('SA13-100–111;','SA13-100–112,122;'),('SA13-128–138;','SA13-117–118,125–138;'),('SA13-130–132;','SA13-131–132;'),('SA13-168–173;','SA13-169–173,195;'),('SA13-174–195;','SA13-174–182,187–191,193;'),('SA13-184–194;','SA13-183–186;')]:s=s.replace(old,new)
p.write_text(s)
d=ROOT/'work/p2_retrieval';d.mkdir(exist_ok=True)
moved=[]
for f in (O/'outputs').glob('web_*.json'):
 shutil.move(str(f),str(d/f.name));moved.append(f.name)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (O/'progress.log').open('a') as f:
 f.write(now+' Core stages1–6 complete:113manual verdicts,108items,142claims,49problems,82readings,10directions; bibliography/search/events/links saved. Supplemental K34-12 audit follows at parent request.\n')
with (O/'outputs/finalization_runs.txt').open('a') as f:
 f.write('refine_records.py rerun: fixed literal C191 raw-string quote; remaining C150 anchor then corrected by add_subsidiary_claims.py.\n')
 f.write('add_subsidiary_claims.py rerun:141claims; made idempotent for231–240.\n')
 f.write('finalize_records.py:142claims; original SGA7 locators, Faltings, Katz and2026 preprint scopes corrected.\n')
 f.write('author_problems.py:49problem records.\nauthor_evidence.py:43references,15searchgroups,406checkevents,86links,8readingbatches.\n')
 f.write('validate_p2.py:exit0; quote/scan/global-line, identifier, reference, computation and coverage checks passed.\n')
 f.write('ocr_sga7_locator.py: original-page rendering succeeded; parallel tesseract stalled; interrupted with Ctrl-C, exit130. Empty OCR output never used as evidence; images were read directly.\n')
 f.write('Raw external search bodies moved out of deliverable; concise actual search outcomes retained. Moved:'+','.join(moved)+'\n')
print(json.dumps({'moved_raw_retrieval_files':len(moved),'progress_time_UTC':now},indent=2))
