#!/usr/bin/env python3
"""Rebuild the audit tables from explicit page-review records.

Unreviewed rows remain visibly pending. --require-complete rejects every pending
page or comparison row. It never fabricates a visual-review outcome.
"""
import argparse, collections, csv, hashlib, json, re, zipfile
from pathlib import Path
from review import ROOT, PAGES, DIFFS, NOTES, AUTO_KINDS, source, marks

OUTCOME_TS='the typescript reads as our transcription'
OUTCOME_CORRECTED='our transcription corrected'
OUTCOME_EDITION='the arXiv text normalizes, corrects, merges handwriting, adds or omits'

def write_tsv(name,fields,rows):
    with (ROOT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore')
        w.writeheader();w.writerows(rows)

def locate(s,reading):
    if reading and reading in s: return str(s.count('\n',0,s.index(reading))+1),'exact reading'
    # A location aid only; the reading and outcome are never inferred here.
    bits=re.findall(r'[A-Za-z][A-Za-z ,;:\-]{12,}',reading or '')
    for bit in sorted(bits,key=len,reverse=True):
        bit=bit.strip()
        if bit and s.count(bit)==1:return str(s.count('\n',0,s.index(bit))+1),'unique literal fragment'
    return '', 'page-level location; exact line not yet supplied'

def main(require_complete=False):
    decisions=[]; concordance=[]; reviews={}; pending=[]; coverage=[]
    for p in PAGES:
        key=p['key']; rp=ROOT/'review'/(key+'.json'); cp=ROOT/'checked_pages'/(key+'.tex')
        if not (rp.exists() and cp.exists()): pending.append(key);continue
        r=json.loads(rp.read_text());s=source(key).read_text();checked=cp.read_text()
        assert r['review_status']=='complete' and r['viewed_halves']==['a','b']
        assert hashlib.sha256(source(key).read_bytes()).hexdigest()==r['source_sha256']
        assert hashlib.sha256(cp.read_bytes()).hexdigest()==r['checked_sha256']
        reviews[key]=r
        common={'key':key,'cote':p['cote'],'site':p['site'],'source_file':str(source(key).relative_to(ROOT)),
                'scan_upper':f'scans/{key}_a.jpg','scan_lower':f'scans/{key}_b.jpg'}
        by_id={x['row_id']:x for x in DIFFS if x['page_key']==key}
        ms={x['id']:x for x in marks(s)}
        for item in r.get('diff_decisions',[]):
            d=by_id[item['id']];line,method=locate(s,d['page_reading'])
            decisions.append(dict(common,decision_id=key+'-'+item['id'],kind=d['kind'],
                line=str(item.get('line',line)),transcription_reading=d['page_reading'],image_reading=item['image_reading'],
                arxiv_reading=d['arxiv_text'],decision=item['decision'],reason=item['reason'],location_method=method))
        for item in r.get('doubt_decisions',[]):
            m=ms[item['id']]
            decisions.append(dict(common,decision_id=key+'-'+item['id'],kind=m['kind'],line=m['line'],
                transcription_reading=m['reading'],image_reading=item['image_reading'],arxiv_reading='',
                decision=item['decision'],reason=item['reason'],location_method='initial macro occurrence'))
        for i,e in enumerate(r.get('changes',[]),1):
            line=e.get('source_line',locate(s,e['old'])[0])
            decisions.append(dict(common,decision_id=f'{key}-E{i:03d}',kind=e.get('kind','source correction'),line=line,
                transcription_reading=e['old'],image_reading=e['new'],arxiv_reading=e.get('arxiv_reading',''),
                decision=OUTCOME_CORRECTED,reason=e['reason'],location_method='unique explicit edit'))
        for label,field in [('N','notes_review'),('K','known_error_review')]:
            decisions.append(dict(common,decision_id=key+'-'+label,kind=field,line='4',
                transcription_reading=NOTES.get(key,{}).get('notes','') if label=='N' else '',
                image_reading=r[field],arxiv_reading='',decision='page review recorded',reason=r[field],
                location_method='whole page'))
        coverage.append({'key':key,'cote':p['cote'],'site':p['site'],'status':'complete',
            'source_sha256':r['source_sha256'],'checked_sha256':r['checked_sha256'],
            'doubts_before':len(marks(s)),'doubts_after':len(marks(checked)),'source_changes':len(r.get('changes',[]))})
    for d in DIFFS:
        row={k:v for k,v in d.items() if k!='row_id'};r=reviews.get(d['page_key'])
        row['review_id']=d['row_id']
        if r is None:
            row.update(outcome='pending image review',reason='No complete visual review record exists for this page.')
        else:
            decision=next((x for x in r.get('diff_decisions',[]) if x['id']==d['row_id']),None)
            if decision:
                explicit=decision.get('outcome')
                if explicit in (OUTCOME_TS,OUTCOME_CORRECTED,OUTCOME_EDITION):outcome=explicit
                elif any(t in decision['decision'].lower() for t in ('correct','revis','recover','layer')):outcome=OUTCOME_CORRECTED
                else:outcome=OUTCOME_TS
                row.update(outcome=outcome,reason=decision['reason'])
            else:
                assert d['kind'] in AUTO_KINDS,(d['row_id'],d['page_key'])
                row.update(outcome=OUTCOME_EDITION,reason='Page visually reviewed; supplied comparison class: '+d['kind']+'. '+d['note'])
        concordance.append(row)
    fields=['decision_id','key','cote','site','line','transcription_reading','image_reading','arxiv_reading','decision','reason','kind','location_method','source_file','scan_upper','scan_lower']
    write_tsv('CHECK_DECISIONS.tsv',fields,decisions)
    write_tsv('ARXIV_CONCORDANCE.tsv',[k for k in DIFFS[0] if k!='row_id']+['outcome','reason','review_id'],concordance)
    write_tsv('PAGE_REVIEW_COVERAGE.tsv',['key','cote','site','status','source_sha256','checked_sha256','doubts_before','doubts_after','source_changes'],coverage)
    source_counts=collections.Counter();after_counts=collections.Counter()
    for p in PAGES:
        source_counts.update(m['kind'] for m in marks(source(p['key']).read_text()))
        target=ROOT/'checked_pages'/(p['key']+'.tex')
        if target.exists():after_counts.update(m['kind'] for m in marks(target.read_text()))
    stats={'total_pages':len(PAGES),'reviewed_pages':len(reviews),'pending_pages':pending,
        'concordance_rows':len(concordance),'concordance_outcomes':dict(collections.Counter(r['outcome'] for r in concordance)),
        'decision_rows':len(decisions),'source_changes':sum(len(r.get('changes',[])) for r in reviews.values()),
        'all_source_doubts':dict(source_counts),'reviewed_page_doubts_after':dict(after_counts),
        'decision_rows_without_exact_line':sum(not r['line'] for r in decisions)}
    (ROOT/'REVIEW_STATUS.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in stats.items() if k!='pending_pages'},ensure_ascii=False,indent=2))
    if require_complete and (pending or any(r['outcome']=='pending image review' for r in concordance)):
        raise SystemExit('INCOMPLETE: visual-review gate has not passed.')
    return stats

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--require-complete',action='store_true');ns=ap.parse_args();main(ns.require_complete)
