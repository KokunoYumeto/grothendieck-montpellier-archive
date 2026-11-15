"""Record supplemental Brown/witness differences only after visual page review."""
from pathlib import Path
import csv
from review_root import BASE, PROJECT, TEXT, FIELDS

def record(key, exceptions=None):
    exceptions=exceptions or {}
    review=list(csv.DictReader((PROJECT/'records/PAGE_REVIEW_134_2.tsv').open(),delimiter='\t'))
    assert any(r['key']==key and r['both_halves_viewed']=='yes' for r in review)
    original=list(csv.DictReader((TEXT/'transcription/brown_DIFFERENCES.tsv').open(),delimiter='\t'))
    path=PROJECT/'records/BROWN_CONCORDANCE.tsv'
    old=list(csv.DictReader(path.open(),delimiter='\t')) if path.exists() else []
    old=[r for r in old if r['key']!=key]
    ledger=PROJECT/'records/CHECK_DECISIONS_134_2.tsv'
    decisions=list(csv.DictReader(ledger.open(),delimiter='\t'))
    decisions=[r for r in decisions if not (r['key']==key and r['source_id'].startswith('BROWN-DIFF:'))]
    rows=[]
    for i,r in enumerate(original,1):
        if r['key']!=key:continue
        kind=r['class'];outcome='the typescript reads as our transcription'
        if kind=='addition':outcome='the arXiv text adds'
        elif kind=='omission':outcome='the arXiv text omits'
        elif kind=='normalization':outcome='the arXiv text normalizes'
        elif kind=='hand-unmarked':outcome='the arXiv text merges handwriting'
        reason='Both supplied scan halves inspected. '+r['note'].rstrip('.')+'. The visible Brown copy retains the recorded page reading; the later revised witness is not substituted for it.'
        if kind=='addition':reason='Both scan halves inspected: this wording or annotation is absent from the supplied Brown page. '+r['note'].rstrip('.')+'. Where it belongs to the later 1983 version, this is a difference of textual state, not evidence of an erroneous addition to that later version.'
        after=r['page']
        if i in exceptions:after,outcome,reason=exceptions[i]
        rows.append(dict(r,source_id=f'BROWN-DIFF:{i}',outcome=outcome,reason=reason))
        decisions.append(dict(key=key,cote=r['cote'],site=r['site'],line='',transcription_reading=r['page'],image_reading=after,arxiv_reading=r['draft'],decision=outcome,reason=reason,source_id=f'BROWN-DIFF:{i}'))
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(original[0])+['source_id','outcome','reason'],delimiter='\t');w.writeheader();w.writerows(old+rows)
    with ledger.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=FIELDS,delimiter='\t');w.writeheader();w.writerows(decisions)
    print(key,len(rows),'supplemental witness decisions')
