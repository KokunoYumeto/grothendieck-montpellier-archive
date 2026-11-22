#!/usr/bin/env python3
"""Create an immutable final archive only after the requested stopping gate."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re
import time
import zipfile

root=Path(__file__).resolve().parents[1]
out=root.parent/'RESEARCH_SA20_final.zip'
assert not out.exists(),'Refusing to overwrite an immutable final package'
reviews=[]
for p in (root/'logs').glob('review*.json'):
    if re.fullmatch(r'review\d+\.json',p.name):reviews.append(json.loads(p.read_text()))
reviews.sort(key=lambda r:r['review'])
assert len(reviews)>=2
previous,last=reviews[-2:]
assert last['review']==previous['review']+1
assert last['stopping_rule_triggered']
assert not previous['movement'] and not last['movement']
assert last['consecutive_no_movement']>=2
assert datetime.now(timezone.utc)>=datetime.fromisoformat(last['scheduled_utc'])
report=(root/'RESEARCH_SA20_report.md').read_text()
assert report.startswith('INCOMPLETE\n')
assert 'We therefore return this INCOMPLETE final package.' in report
assert 'REVIEW_STATUS_PLACEHOLDER' not in report
assert 'No mandatory stopping review has yet authorized a final return.' not in report
qa=json.loads((root/'logs/pdf_qa.json').read_text())
assert qa['visual_review']=='passed'
for k in ['over_2pt','missing_glyphs','undefined_refs','bib_warnings']:
    assert qa['after'][k]==0,k
assert hashlib.sha256((root/'RESEARCH_SA20_paper.pdf').read_bytes()).hexdigest()==qa['pdf_sha256']
for rel,digest in qa['source_sha256'].items():
    assert hashlib.sha256((root/rel).read_bytes()).hexdigest()==digest,rel
with (root/'RESEARCH_SA20_outcomes.csv').open(newline='') as f:outcomes=list(csv.DictReader(f))
assert len(outcomes)==70 and len({r['original_item'] for r in outcomes})==70
open_rows=[r['original_item'] for r in outcomes if 'unsettled' in r['current_outcome'].lower()]
assert open_rows==['A.1(b)','A.5 proper-map maximal locus and recursion','C.2(b) literature directions/hypotheses']
with (root/'RESEARCH_SA20_results.csv').open(newline='') as f:statements=list(csv.DictReader(f))
assert len({r['id'] for r in statements})==len(statements)
for p in ['RESEARCH_SA20_paper.tex','RESEARCH_SA20_references.bib','CHECK_EVENTS.tsv','PROGRESS_LEDGER.md','README.md']:
    assert (root/p).is_file(),p
check_count=len((root/'CHECK_EVENTS.tsv').read_text().splitlines())-1
status={
    'status':'INCOMPLETE',
    'credit':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)',
    'priority_claimed':False,
    'original_rows':len(outcomes),
    'determined_original_rows':len(outcomes)-len(open_rows),
    'open_original_rows':open_rows,
    'statement_records':len(statements),
    'check_events':check_count,
    'check_event_scope':'Includes proof audits, source checks, failed routes and executions; not a count of independent proofs.',
    'stopping_reviews':[previous,last],
    'pdf_pages':qa['pages'],
    'pdf_sha256':qa['pdf_sha256'],
    'visual_qa':'PASS',
    'compiled_source_files_checked':len(qa['source_sha256'])
}
(root/'notes/final_status.json').write_text(json.dumps(status,indent=2)+'\n')
(root/'README.md').write_text(
    '# RESEARCH_SA20 final package — INCOMPLETE\n\n'
    'AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). We claim no priority.\n\n'
    f'We return this package after scheduled reviews{previous["review"]} and{last["review"]} '
    'both recorded no qualifying movement, triggering the requested stopping rule. '
    f'The final review was recorded at {last["actual_utc"]}. '
    f'Of the{len(outcomes)} original rows,{len(outcomes)-len(open_rows)} have determinations '
    'and three remain open: A.1(b), A.5 proper-map maximal locus and recursion, '
    'and C.2(b) literature directions/hypotheses.\n\n'
    '## Read first\n\n'
    '`RESEARCH_SA20_report.md` begins with INCOMPLETE and the full70-row outcome table. '
    '`RESEARCH_SA20_outcomes.csv` contains the same original-row mapping. '
    f'`RESEARCH_SA20_results.csv` records{len(statements)} numbered statements; '
    f'`CHECK_EVENTS.tsv` records{check_count} check events, including audits and failed routes. '
    'These are not counts of independent proofs. The dated `PROGRESS_LEDGER.md` '
    'preserves earlier research states and the final stopping review.\n\n'
    f'The{qa["pages"]}-page `RESEARCH_SA20_paper.pdf` contains the numbered proofs '
    'and exact remaining gates. Its LuaLaTeX source and every included TeX dependency '
    'are present, with `RESEARCH_SA20_references.bib`. The PDF passed compilation '
    'and explicit visual inspection of every changed or overflow page and a spread. '
    '`logs/pdf_qa.json` gives the exact page list, warning counts and hashes.\n\n'
    '## Reproduce\n\n'
    'We provide the mathematical verification programs in `code/` and '
    '`agents/*/code/`, with actual outputs in `logs/` and `agents/*/logs/`. '
    'Finite certificates support their stated finite claims; they do not replace '
    'the all-arity or topological proofs. Run `python3 code/assemble_records.py` '
    'to assemble the current CSV, TSV and BibTeX records, then '
    '`python3 code/update_report.py` for the report and outcome CSV. '
    'The recorded build uses LuaLaTeX, BibTeX and two further LuaLaTeX passes. '
    'Any changed build requires its own warning and visual review.\n\n'
    'Downloaded original sources, manuscript scans, the supplied source archive, '
    'and previous checkpoint ZIPs are omitted. Their bibliographic URLs and '
    'inspection locators are retained. All authored research notes, code, '
    'logs, checks and deliverables are preserved subject to the documented '
    'exclusion of reproducible compiler auxiliary files. Pending or unnumbered '
    'method notes remain outside the checked statement inventory; inclusion '
    'does not promote them to proved original-row conclusions.\n\n'
    '`notes/final_status.json` records the final status, and '
    '`notes/final_file_manifest.json` lists the included files and SHA256 hashes. '
    'The archive integrity record and delivery receipt are created after the '
    'immutable archive, so they are provided separately.\n'
)
excluded=json.loads((root/'notes/external_originals_manifest.json').read_text())
original_text={item['path'] for item in excluded['excluded_from_archive']}
payload={}
for p in sorted(root.rglob('*')):
    if not p.is_file():continue
    rel=p.relative_to(root)
    if str(rel) in original_text:continue
    if rel==Path('notes/final_file_manifest.json'):continue
    if '__pycache__' in rel.parts or 'sources' in rel.parts:continue
    if p.suffix.lower() in {'.zip','.pyc','.tar','.gz'}:continue
    if p.suffix.lower() in {'.pdf','.png','.jpg','.jpeg'}:
        if not(p.name=='RESEARCH_SA20_paper.pdf' or rel.parts[0]=='qa'):continue
    if p.suffix.lower() in {'.aux','.toc','.out','.fls','.fdb_latexmk','.synctex'}:continue
    payload[str(rel)]=p.read_bytes()
manifest=[{'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()} for rel,data in payload.items()]
manifest_bytes=(json.dumps(manifest,indent=2)+'\n').encode()
(root/'notes/final_file_manifest.json').write_bytes(manifest_bytes)
payload['notes/final_file_manifest.json']=manifest_bytes
created=datetime.now(timezone.utc).isoformat()
with zipfile.ZipFile(out,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for rel,data in payload.items():z.writestr('RESEARCH_SA20/'+rel,data)
assert out.stat().st_size<500_000_000
started=time.perf_counter()
with zipfile.ZipFile(out) as z:
    assert z.testzip() is None
    assert len(z.infolist())==len(payload)
    for item in manifest:
        data=z.read('RESEARCH_SA20/'+item['path'])
        assert len(data)==item['bytes'],item['path']
        assert hashlib.sha256(data).hexdigest()==item['sha256'],item['path']
record={'archive':str(out),'created_utc':created,'verified_utc':datetime.now(timezone.utc).isoformat(),
        'status':'PASS','bytes':out.stat().st_size,'files':len(payload),
        'manifest_hashes_checked':len(manifest),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
        'verification_runtime_seconds':time.perf_counter()-started,
        'original_rows':70,'open_original_rows':open_rows,'statement_records':len(statements),
        'check_events':len((root/'CHECK_EVENTS.tsv').read_text().splitlines())-1,
        'pdf_pages':qa['pages'],'pdf_sha256':qa['pdf_sha256'],'stopping_review':last['review']}
(root/'logs/final_package_integrity.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
