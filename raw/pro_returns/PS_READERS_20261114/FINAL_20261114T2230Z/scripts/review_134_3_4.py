"""Record explicit image-based collation decisions for cotes 134-3/134-4.

Run from the directory containing inputs/ and PS_READERS_WORK/.  This utility
does not perform visual review.  Its JSON inputs are the reviewer's decisions.
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path.cwd()
TEXT = ROOT / 'inputs/text'
OUT = ROOT / 'PS_READERS_WORK'
FIELDS = ['key','cote','site','line','transcription_reading','image_reading',
          'arxiv_reading','decision','reason','source_id']
DIFF = list(csv.DictReader((TEXT/'records/PS_ARXIV_DIFF.tsv').open(), delimiter='\t'))
NOTES = {r['key']:r for r in csv.DictReader((TEXT/'transcription/ps_NOTES.tsv').open(), delimiter='\t')}
REQUIRED = {'wording','formula','addition','omission','other','unparsed',
 'handwritten note added on the page, absent from arXiv (or handwritten deletion not applied)',
 'handwritten note rewritten in arXiv',
 'struck text printed in arXiv (handwritten deletion not applied)'}

def occurrences(s, macro):
    results=[]
    for m in re.finditer(r'\\'+macro+r'\{',s):
        j=m.end(); level=1
        while level and j<len(s):
            if s[j]=='{' and (j==0 or s[j-1]!='\\'): level+=1
            if s[j]=='}' and (j==0 or s[j-1]!='\\'): level-=1
            j+=1
        results.append((s[m.start():j],s[:m.start()].count('\n')+1))
    return results

def page_packet(key):
    s=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text()
    print('\nPAGE',key)
    print('\n'.join(f'{i:03} {l}' for i,l in enumerate(s.splitlines(),1)))
    print('NOTES',NOTES[key]['notes'])
    for i,r in enumerate(DIFF,1):
        if r['page_key']==key:
            print('DIFF',i,{q:r[q] for q in ['kind','arxiv_text','page_reading','note']})
    for name in ['unsure','illegible']:
        for i,(v,l) in enumerate(occurrences(s,name),1):print(name,i,l,v)

def save_review(conf):
    key=conf['key']; cote,site=key.split('_')[1:]
    original=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text()
    s=original; records=[]
    def row(sid,before,after,reason,decision='retain',arxiv='',line=''):
        if line=='':
            pos=original.find(before)
            line=original[:pos].count('\n')+1 if before and pos>=0 else ''
        records.append(dict(zip(FIELDS,[key,cote,int(site),line,before,after,arxiv,decision,reason,sid])))
    for n,edit in enumerate(conf.get('edits',[]),1):
        before,after,reason=edit
        if s.count(before)!=1: raise ValueError((key,before,s.count(before)))
        s=s.replace(before,after,1)
        row(f'EDIT:{key}:{n}',before,after,reason,'correct transcription')
    for extra in conf.get('extra_records', []):
        row(extra['source_id'], extra['before'], extra['after'], extra['reason'],
            extra.get('decision', 'mechanical correction'), line=extra.get('line', ''))
    supplied={int(i):v for i,v in conf.get('diffs',{}).items()}
    required={i for i,r in enumerate(DIFF,1) if r['page_key']==key and r['kind'] in REQUIRED}
    if not required.issubset(supplied):raise ValueError(('missing diff decisions',key,required-supplied.keys()))
    for i,v in supplied.items():
        r=DIFF[i-1]
        if r['page_key']!=key:raise ValueError(('wrong page',i,key))
        after,reason,*decision=v
        row(f'DIFF:{i}',r['page_reading'],after,reason,decision[0] if decision else 'retain',r['arxiv_text'])
    for macro in ['unsure','illegible']:
        occ=occurrences(original,macro)
        decisions=conf.get(macro,[])
        if len(decisions)!=len(occ):raise ValueError((key,macro,'expected',len(occ),'supplied',len(decisions)))
        for i,((before,line),v) in enumerate(zip(occ,decisions),1):
            after,reason=v
            row(f'{macro.upper()}:{key}:{i}',before,after,reason,
                'retain doubt' if after==before or '\\unsure{' in after or '\\illegible{' in after else 'settled on image',line=line)
    issues=[x.strip() for x in NOTES[key]['notes'].split(' | ') if not x.strip().lstrip('- ').startswith('LONG-HANDWRITING:')]
    nd=conf.get('notes',[])
    if len(nd)!=len(issues):raise ValueError((key,'notes','expected',len(issues),'supplied',len(nd)))
    for i,(before,reason) in enumerate(zip(issues,nd),1):
        row(f'NOTE:{key}:{i}',before,'See checked page and review evidence.',reason,'note checked')
    s=s.replace('not yet checked by eye.','image review recorded in records/CHECK_DECISIONS_134_3_4.tsv.')
    # Header-only provenance update is itself documented.
    row(f'META:{key}', 'not yet checked by eye.',
        'image review recorded in records/CHECK_DECISIONS_134_3_4.tsv.',
        'Provenance comment updated after both supplied image halves were inspected.','metadata update',line=3)
    (OUT/'checked_pages'/f'{key}.tex').write_text(s)
    (OUT/'review_notes'/f'{key}.json').write_text(json.dumps(conf,ensure_ascii=False,indent=2)+'\n')
    path=OUT/'records/CHECK_DECISIONS_134_3_4.tsv'
    old=list(csv.DictReader(path.open(),delimiter='\t')) if path.exists() else []
    with path.open('w') as f:
        w=csv.DictWriter(f,fieldnames=FIELDS,delimiter='\t');w.writeheader()
        w.writerows([x for x in old if x['key']!=key]+records)
    path=OUT/'records/PAGE_REVIEW_134_3_4.tsv'
    fields=['key','both_halves_viewed','status','issues_remaining','notes']
    old=list(csv.DictReader(path.open(),delimiter='\t')) if path.exists() else []
    entry={'key':key,'both_halves_viewed':'yes','status':'image reviewed; unresolved marks retained',
           'issues_remaining':len(occurrences(s,'unsure'))+len(occurrences(s,'illegible')),
           'notes':conf['evidence']}
    with path.open('w') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows([x for x in old if x['key']!=key]+[entry])
    print(key,'written',len(records),'decisions;',entry['issues_remaining'],'doubt marks retained')

if __name__=='__main__':
    import sys
    if sys.argv[1]=='packet':
        for key in sys.argv[2:]: page_packet(key)
    elif sys.argv[1]=='save':
        for p in sys.argv[2:]:save_review(json.loads(Path(p).read_text()))
