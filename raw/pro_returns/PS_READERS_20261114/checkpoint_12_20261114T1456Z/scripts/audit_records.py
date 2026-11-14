"""Merge review records and maintain an explicit, non-certifying coverage audit."""
from pathlib import Path
import csv,json,re,collections,difflib
P=Path(__file__).resolve().parents[1];I=P.parent/'inputs/text';R=P/'records'
FIELDS=['key','cote','site','line','transcription_reading','image_reading','arxiv_reading','decision','reason','source_id']
def read(p):return list(csv.DictReader(p.open(),delimiter='\t'))
def write(p,fields,rows):
    with p.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
def canonical(s):return re.sub(r'\s+',' ',s.replace(r'\n','\n')).strip()
def sortkey(key):
    a,c,n=key.split('_');return (a=='brown',int(c.split('-')[1]),int(n))
decisions=[];ledger=[]
for p in sorted(R.glob('CHECK_DECISIONS_*.tsv')):decisions.extend(read(p))
for p in sorted(R.glob('PAGE_REVIEW_*.tsv')):ledger.extend(read(p))
decisions.sort(key=lambda r:(sortkey(r['key']),r['source_id']))
ledger.sort(key=lambda r:sortkey(r['key']))
write(R/'CHECK_DECISIONS.tsv',FIELDS,decisions)
write(R/'PAGE_REVIEW.tsv',list(ledger[0]) if ledger else ['key'],ledger)
ids=collections.Counter(r['source_id'] for r in decisions)
duplicates=[k for k,v in ids.items() if v>1]
bydiff={r['source_id']:r for r in decisions if r['source_id'].startswith('DIFF:')}
bykey=collections.defaultdict(list)
for r in decisions:bykey[r['key']].append(r)
reviewed={r['key'] for r in ledger if r.get('both_halves_viewed')=='yes'}
checked={p.stem for p in (P/'checked_pages').glob('*.tex')}
complete=reviewed&checked
diffs=read(I/'records/PS_ARXIV_DIFF.tsv')
required={'wording','formula','addition','omission','other','handwritten note added on the page, absent from arXiv (or handwritten deletion not applied)','handwritten note rewritten in arXiv','struck text printed in arXiv (handwritten deletion not applied)','unparsed'}
missing_required=[];concordance=[];followups=[]
for n,r in enumerate(diffs,1):
    item=dict(r);key=r['page_key'];d=bydiff.get(f'DIFF:{n}')
    if key not in complete:
        outcome='pending visual review';reason='This page has not yet completed the recorded two-half image review.'
    elif d:
        decision=d['decision'].lower()
        if 'our transcription corrected' in decision or decision.startswith(('correct ','settled on')):outcome='our transcription corrected'
        elif 'arxiv addition' in decision or decision=='the arxiv text adds':outcome='the arXiv text adds'
        elif 'arxiv omission' in decision:outcome='the arXiv text omits'
        else:outcome='the typescript reads as our transcription'
        reason=d['reason']+' [CHECK_DECISIONS '+d['source_id']+']'
    elif r['kind'] in required:
        outcome='pending individual decision';reason='The page has been reviewed, but this required difference does not yet have its individual decision row.';missing_required.append(n)
    else:
        matched=[];reading=canonical(r['page_reading'])
        for e in bykey[key]:
            if e['source_id'].split(':')[0] not in {'CHANGE','EDIT'}:continue
            before=canonical(e['transcription_reading']);after=canonical(e['image_reading'])
            if before!=after and len(before)>=7 and (before in reading or (len(reading)>=12 and reading in before and reading not in after)):
                matched.append(e)
        if matched:
            outcome='our transcription corrected';reason='Image-grounded changes affect the reading quoted in this comparison: '+'; '.join(e['reason']+' ['+e['source_id']+']' for e in matched[:4])
        else:
            outcome={'normalization':'the arXiv text normalizes','silent correction':'the arXiv text corrects','handwritten note merged (unmarked in arXiv)':'the arXiv text merges handwriting'}.get(r['kind'],'pending concordance adjudication')
            detail=r.get('kind_detail','').strip().rstrip('.')
            reason='The completed image review retains the source reading and its provenance for this comparison.'+(' '+detail+'.' if detail else '')
            if r['kind']=='handwritten note merged (unmarked in arXiv)' and r'\inserted[typed]' in reading and not re.search(r'\\(?:hand|deleted|margin)\b|\\(?:over|inserted)(?!\[typed\])',reading):
                outcome='the typescript reads as our transcription'
                reason='The image review retains a typed interlinear insertion. The witness incorporates its wording without a placement mark; the original comparison label incorrectly called this insertion handwriting.'
            if outcome=='pending concordance adjudication':followups.append(n)
    item['outcome']=outcome;item['reason']=reason;concordance.append(item)
write(R/'ARXIV_CONCORDANCE.tsv',list(diffs[0])+['outcome','reason'],concordance)
metadata=json.loads((I/'records/PAGES_PS.json').read_text())
coverage=[];unrecorded_doubts=[];unrecorded_notes=[]
for m in metadata:
    key=m['key'];d='brown' if key.startswith('brown_') else 'ps'
    original=(I/'transcription'/(d+'_pages')/(key+'.tex')).read_text()
    final=(P/'checked_pages'/(key+'.tex')).read_text() if key in complete else None
    before={name:len(re.findall(r'\\'+name+r'\s*\{',original)) for name in ['unsure','illegible']}
    after={name:len(re.findall(r'\\'+name+r'\s*\{',final)) if final is not None else '' for name in before}
    if key in complete:
        for name,num in before.items():
            for i in range(1,num+1):
                sid=f'{name.upper()}:{key}:{i}'
                if not ids[sid]:unrecorded_doubts.append(sid)
    coverage.append({'key':key,'cote':m['cote'],'site':m['site'],'pdf_page':m['pdf_page'],'review_complete':key in complete,'unsure_before':before['unsure'],'illegible_before':before['illegible'],'unsure_after':after['unsure'],'illegible_after':after['illegible'],'decisions':len(bykey[key])})
write(R/'REVIEW_COVERAGE.tsv',list(coverage[0]),coverage)
for d in ['ps','brown']:
    for n in read(I/'transcription'/(d+'_NOTES.tsv')):
        if n['key'] not in complete:continue
        notes=[x for x in n['notes'].split(' | ') if x and x!='none' and not x.lstrip('- ').startswith('LONG-HANDWRITING:')]
        for i,_ in enumerate(notes,1):
            sid=f'NOTE:{n["key"]}:{i}'
            if not ids[sid]:unrecorded_notes.append(sid)
audit={'source_pages':706,'checked_page_files':len(checked),'pages_with_complete_ledger':len(complete),'decision_rows':len(decisions),'concordance_rows':len(concordance),'required_differences_without_decisions_on_reviewed_pages':missing_required,'original_doubts_without_decisions_on_reviewed_pages':unrecorded_doubts,'notes_without_decisions_on_reviewed_pages':unrecorded_notes,'duplicate_source_ids':duplicates,'concordance_followups':followups,'outcome_counts':dict(collections.Counter(r['outcome'] for r in concordance)),'complete':len(complete)==706 and not (missing_required or unrecorded_doubts or unrecorded_notes or duplicates or followups)}
(R/'COVERAGE_AUDIT.json').write_text(json.dumps(audit,indent=2)+'\n')
print(json.dumps({k:v for k,v in audit.items() if not isinstance(v,list)}))
print(json.dumps({'missing_required':missing_required[:30],'missing_doubts':unrecorded_doubts[:20],'missing_notes':unrecorded_notes[:20],'duplicates':duplicates[:20]}))
