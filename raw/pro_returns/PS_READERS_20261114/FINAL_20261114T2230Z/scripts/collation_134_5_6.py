"""Rebuild the 134-5/134-6 review ledger from explicit visual observations.

Run from the edition workspace; source archives have been extracted under
inputs/text. No review result is inferred from a transcription or image name.
"""
import csv, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
TEXT=ROOT/'inputs/text'
OUT=ROOT/'PS_READERS_WORK'
FIELDS=['key','cote','site','line','transcription_reading','image_reading','arxiv_reading','decision','reason','source_id']
SKIP={'normalization','silent correction','handwritten note merged (unmarked in arXiv)'}
DIFFS=list(csv.DictReader((TEXT/'records/PS_ARXIV_DIFF.tsv').open(),delimiter='\t'))
NOTES={r['key']:r for r in csv.DictReader((TEXT/'transcription/ps_NOTES.tsv').open(),delimiter='\t')}

def macros(text,name):
    result=[]
    for m in re.finditer(r'\\'+name+r'\{',text):
        i=m.end();depth=1
        while i<len(text) and depth:
            if text[i]=='{' and (i==0 or text[i-1]!='\\'):depth+=1
            elif text[i]=='}' and (i==0 or text[i-1]!='\\'):depth-=1
            i+=1
        result.append((m.start(),text[m.start():i]))
    return result

def packet(key):
    t=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text()
    print('PAGE',key)
    for n,l in enumerate(t.splitlines(),1):print(f'{n}: {l}')
    print('DIFFERENCES REQUIRING DECISIONS')
    for i,r in enumerate(DIFFS,1):
        if r['page_key']==key and r['kind'] not in SKIP:
            print(i,r['kind'],'TRANSCRIPTION:',r['page_reading'],'ARXIV:',r['arxiv_text'],'LOC:',r['note'])
    print('DOUBTS')
    for name in ['unsure','illegible']:
        for i,(p,s) in enumerate(macros(t,name),1):print(name,i,'line',t[:p].count('\n')+1,s)
    print('NOTES')
    for i,s in enumerate([s for s in NOTES[key]['notes'].split(' | ') if not s.startswith('LONG-HANDWRITING')],1):print(i,s)

def rebuild():
    reviews=[json.loads(l) for l in (OUT/'review_notes/134_5_6.jsonl').read_text().splitlines() if l.strip()]
    allrows=[];ledger=[]
    keys=set()
    for review in reviews:
        key=review['key']; assert key not in keys;keys.add(key)
        assert key.startswith(('ps_134-5_','ps_134-6_'))
        assert review['both_halves_viewed'] is True
        cote=key.split('_')[1];site=int(key.split('_')[2])
        original=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text()
        checked=original
        required={i:r for i,r in enumerate(DIFFS,1) if r['page_key']==key and r['kind'] not in SKIP}
        supplied={int(d[0]):d for d in review['diffs']}
        assert set(required)==set(supplied),(key,set(required)-set(supplied),set(supplied)-set(required))
        def row(source_id,old,new,decision,reason,arxiv='',line=''):
            if not line:
                pos=original.find(old) if old else -1
                line=str(original[:pos].count('\n')+1) if pos>=0 else 'see reason'
            allrows.append(dict(key=key,cote=cote,site=site,line=line,transcription_reading=old,image_reading=new,arxiv_reading=arxiv,decision=decision,reason=reason,source_id=source_id))
        for i,r in required.items():
            d=supplied[i]
            row(f'DIFF:{i}',r['page_reading'],d[2] if len(d)>2 else r['page_reading'], 'our transcription corrected' if len(d)>2 and d[2]!=r['page_reading'] else 'the typescript reads as our transcription',d[1],r['arxiv_text'])
        for name in ['unsure','illegible']:
            found=macros(original,name); assessment=review.get(name,[])
            assert len(found)==len(assessment),(key,name,len(found),len(assessment))
            for i,((pos,old),a) in enumerate(zip(found,assessment),1):
                new=a[1] if len(a)>1 else old
                decision=a[2] if len(a)>2 else ('doubt resolved from image' if new!=old else 'doubt retained')
                row(f'{name.upper()}:{key}:{i}',old,new,decision,a[0],line=str(original[:pos].count('\n')+1))
        note_text=[s for s in NOTES[key]['notes'].split(' | ') if not s.startswith('LONG-HANDWRITING')]
        assert len(note_text)==len(review['notes']),(key,'notes',len(note_text),len(review['notes']))
        for i,(old,reason) in enumerate(zip(note_text,review['notes']),1):
            row(f'NOTE:{key}:{i}',old,reason,'note checked',reason,line='scan location stated in note')
        for i,change in enumerate(review.get('changes',[]),1):
            old,new,reason=change
            assert old in checked,(key,old)
            assert checked.count(old)==1,(key,'nonunique change',old)
            checked=checked.replace(old,new,1)
            row(f'CHANGE:{key}:{i}',old,new,'our transcription corrected',reason)
        # A per-page metadata row distinguishes the new review from the input header.
        old_header='not yet checked by eye.'
        new_header='reviewed against both supplied scan halves; see CHECK_DECISIONS.tsv.'
        if old_header in checked:
            checked=checked.replace(old_header,new_header,1)
            row(f'META:{key}:1',old_header,new_header,'review metadata updated',
                'Both supplied original scan halves were opened and inspected before this page was committed; the page-specific evidence and decisions are recorded in the review ledgers.')
        (OUT/'checked_pages'/f'{key}.tex').write_text(checked)
        ledger.append(dict(key=key,both_halves_viewed='yes',status='checked; residual doubts explicitly retained' if re.search(r'\\(?:unsure|illegible)\{',checked) else 'checked',issues_remaining=len(macros(checked,'unsure'))+len(macros(checked,'illegible')),notes=review['general']))
    for file,rows,fields in [('records/CHECK_DECISIONS_134_5_6.tsv',allrows,FIELDS),('records/PAGE_REVIEW_134_5_6.tsv',ledger,['key','both_halves_viewed','status','issues_remaining','notes'])]:
        with (OUT/file).open('w') as f:
            w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
    print('Reviewed pages:',len(ledger),'Decision rows:',len(allrows),'Residual doubts:',sum(r['issues_remaining'] for r in ledger))

if __name__=='__main__':
    import sys
    if len(sys.argv)>1:
        for key in sys.argv[1:]:packet(key)
    else:rebuild()
