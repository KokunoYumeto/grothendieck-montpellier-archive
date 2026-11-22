#!/usr/bin/env python3
"""Apply final INCOMPLETE framing only after the actual mandatory stopping review.

Preparation of this program does not perform a review or authorize stopping.
It refuses a premature or inconsistent trigger and preserves pre-edit sources.
"""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import argparse
import csv
import hashlib
import json
import re
import time

p=argparse.ArgumentParser()
p.add_argument('--review',type=int,required=True)
p.add_argument('--archive-name',default='RESEARCH_SA22_final.zip')
a=p.parse_args()
root=Path(__file__).resolve().parents[1]
begin=time.perf_counter()
now=datetime.now(timezone.utc)
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def read_json(path): return json.loads(path.read_text())
assert a.review>=4
assert re.fullmatch(r'RESEARCH_SA22_final(?:_INCOMPLETE)?\.zip',a.archive_name)
status_path=root/'logs/final_status.json'
assert not status_path.exists(), 'Final framing already recorded; do not overwrite it.'
assert not (root.parent/a.archive_name).exists(), 'Final archive already exists.'
review_paths=sorted((root/'logs').glob('progress_review_[0-9][0-9].json'))
review_path=root/f'logs/progress_review_{a.review:02d}.json'
prior_path=root/f'logs/progress_review_{a.review-1:02d}.json'
assert review_paths and review_paths[-1]==review_path, 'Use the actual latest review.'
review=read_json(review_path)
prior=read_json(prior_path)
assert review['review']==a.review and prior['review']==a.review-1
assert review['movement'] is False and prior['movement'] is False
assert review['consecutive_stagnant_reviews']>=2
assert prior['consecutive_stagnant_reviews']>=1
assert review['stop_required'] is True and review['next_review_utc'] is None
assert review['baseline_review']==prior['review']
assert review['baseline_actual_utc']==prior['actual_utc']
assert review['due_utc']==prior['next_review_utc']
assert review['consecutive_stagnant_reviews']==prior['consecutive_stagnant_reviews']+1
for record in (prior,review):
    actual=datetime.fromisoformat(record['actual_utc'])
    due=datetime.fromisoformat(record['due_utc'])
    assert due<=actual<=now
    evidence=root/record['assessment_note']
    assert evidence.is_file() and sha(evidence)==record['assessment_sha256']
assert review['open_rows']==2, 'Reassess the prepared two-obligation wording.'
ledger=(root/'PROGRESS_LEDGER.md').read_text()
assert review['actual_utc'] in ledger and prior['actual_utc'] in ledger

# Framing may change only after a current, actually inspected source build.
build=read_json(root/'logs/integrated_build_summary.json')
qa=read_json(root/'logs/paper_visual_qa.json')
assert build['pdf_sha256']==qa['pdf_sha256']==sha(root/'RESEARCH_SA22_paper.pdf')
assert qa['inspection'].startswith('PASS')
assert not build['overfull_above_2pt'] and not build['source_changed_during_build']
assert not build['undefined_warnings'] and not build['missing_glyphs']
assert not build.get('rerun_warnings',[])
for name,digest in build['source_hashes_after'].items():
    assert sha(root/name)==digest, f'Stale pre-framing build: {name}'

# Read every count-bearing input before changing any publication source.
results=list(csv.DictReader((root/'RESEARCH_SA22_results.csv').open()))
events=list(csv.DictReader((root/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
access=list(csv.DictReader((root/'SOURCE_ACCESS_EVENTS.tsv').open(),delimiter='\t'))
assert [r['id'] for r in results if r['status']=='Open']==['U:henselian-comparison']
checkpoints=sorted(root.parent.glob('RESEARCH_SA22_checkpoint_[0-9][0-9].zip'))

master=root/'RESEARCH_SA22_paper.tex'
unresolved=root/'sections/unresolved.tex'
changes={
 master:[
  ('This is an active, incomplete research draft.',
   "This is the final incomplete research record of this run. We stopped the research phase under the user's rule after two consecutive scheduled reviews without qualifying movement; the unfulfilled original-source obligations remain explicit."),
  ('Research working paper','Research record: incomplete'),
 ],
 unresolved:[
  ('We continue to attack these obligations under the\ndated review rule in the accompanying progress ledger.',
   "We stopped the research phase after two consecutive scheduled reviews\nwithout qualifying movement, as required by the dated review rule in the\naccompanying progress ledger. The obligations below were not completed."),
 ],
}
prepared={}
for path,replacements in changes.items():
    text=path.read_text()
    for old,new in replacements:
        assert text.count(old)==1, f'Unexpected final-framing anchor in {path}'
        text=text.replace(old,new,1)
    prepared[path]=text
history=root/'notes/final_framing_before'
assert not history.exists(), 'Preserve the earlier final-framing history.'
history.mkdir()
before={str(path.relative_to(root)):sha(path) for path in prepared}
for path,text in prepared.items():
    relative=path.relative_to(root)
    backup=history/relative
    backup.parent.mkdir(parents=True,exist_ok=True)
    backup.write_bytes(path.read_bytes())
    path.write_text(text)

record={
 'status':'INCOMPLETE',
 'research_stopped_utc':review['actual_utc'],
 'framing_applied_utc':now.isoformat(),
 'stopping_review':a.review,
 'stopping_review_path':str(review_path.relative_to(root)),
 'stopping_review_sha256':sha(review_path),
 'preceding_review_path':str(prior_path.relative_to(root)),
 'preceding_review_sha256':sha(prior_path),
 'stagnant_review_actual_times':[prior['actual_utc'],review['actual_utc']],
 'consecutive_stagnant_reviews':review['consecutive_stagnant_reviews'],
 'assessment_note':review['assessment_note'],
 'assessment_sha256':review['assessment_sha256'],
 'reason':'Required stop after two consecutive scheduled reviews without a changed open-row status or a strictly smaller proved main gate.',
 'remaining_obligations':[
  {'task':'B.3 / subject 21','source':'Gabber (1994)','locator':'Section 5, Corollary 1',
   'required':'Original statement, relevant definitions, hypotheses and used proof dependencies, followed by the requested direct derivation.',
   'state':'Original passages not obtained; separate modern scoped derivation remains proved.'},
  {'task':'B.3 / subject 21','source':'Fujiwara (1995)','locator':'Corollary 6.6.4',
   'required':'Original statement, relevant definitions, hypotheses and used proof dependencies, followed by the requested direct derivation.',
   'state':'Original passages not obtained; separate modern scoped derivation remains proved.'},
 ],
 'original_locator_qualification':'Original theorem locators are identified by the opened later primary literature; they were not checked against unobtained original pages.',
 'numbered_open_question':'U:henselian-comparison',
 'counts_at_research_stop':{
  'numbered_statements':len(results),'statement_statuses':dict(Counter(r['status'] for r in results)),
  'canonical_check_events':len(events),'source_access_events':len(access),
 },
 'latest_checkpoint':checkpoints[-1].name if checkpoints else None,
 'final_archive_name':a.archive_name,
 'source_hashes_before':before,
 'source_hashes_after':{str(path.relative_to(root)):sha(path) for path in prepared},
 'pre_framing_pdf_sha256':build['pdf_sha256'],
 'post_framing_publication_state':'Fresh compilation and actual visual inspection required; the old PDF approval does not approve these changed sources.',
 'elapsed_seconds':time.perf_counter()-begin,
}
status_path.write_text(json.dumps(record,indent=2)+'\n')
(history/'README.md').write_text(
 '# Preserved pre-final-framing sources\n\n'
 'These are the exact source bytes before the final INCOMPLETE framing. '
 'They are historical records, not inputs to the final master. Mathematical '
 'content and statement labels were not changed by this operation. '
 'The actual stop evidence and source hashes are in `logs/final_status.json`.\n')
print(json.dumps(record,indent=2))
