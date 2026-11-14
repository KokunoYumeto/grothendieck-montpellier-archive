"""Record explicit visual judgments for cote 134-2; no automatic visual inference.

Run from the task workspace. Input files are addressed relative to the archives.
"""
from pathlib import Path
import csv, json, re, hashlib

BASE = Path(__file__).resolve().parents[2]
PROJECT = BASE / 'PS_READERS_WORK'
TEXT = BASE / 'inputs/text'
FIELDS = ['key','cote','site','line','transcription_reading','image_reading','arxiv_reading','decision','reason','source_id']

def macro_occurrences(text, name):
    out=[]
    for m in re.finditer(r'\\'+name+r'\s*\{',text):
        a=m.end(); n=1; j=a
        while j<len(text) and n:
            if text[j]=='\\': j+=2; continue
            if text[j]=='{':n+=1
            if text[j]=='}':n-=1
            j+=1
        out.append({'start':m.start(),'end':j,'argument':text[a:j-1], 'source':text[m.start():j], 'line':text.count('\n',0,m.start())+1})
    return out

def append_tsv(path, fields, rows):
    old=list(csv.DictReader(path.open(),delimiter='\t')) if path.exists() else []
    keys={r['key'] for r in rows}
    old=[r for r in old if r['key'] not in keys]
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');
        w.writeheader();w.writerows(old+rows)

def review(key, *, changes, doubts, notes, summary, differences=None):
    source=TEXT/'transcription'/('brown_pages' if key.startswith('brown_') else 'ps_pages')/(key+'.tex')
    original=source.read_text(); corrected=original
    meta=next(r for r in json.loads((TEXT/'records/PAGES_PS.json').read_text()) if r['key']==key)
    rows=[]
    def row(line,before,after,decision,reason,sid,arxiv=''):
        rows.append(dict(key=key,cote=meta['cote'],site=meta['site'],line=line,transcription_reading=before,image_reading=after,arxiv_reading=arxiv,decision=decision,reason=reason,source_id=sid))
    for i, change in enumerate(changes,1):
        before,after,reason=change
        if corrected.count(before)!=1:raise ValueError((key,'nonunique change',i,before,corrected.count(before)))
        line=original.count('\n',0,original.find(before))+1 if before in original else ''
        corrected=corrected.replace(before,after,1)
        row(line,before,after,'our transcription corrected',reason,f'CHANGE:{key}:{i}')
    for name in ['unsure','illegible']:
        occ=macro_occurrences(original,name)
        supplied=doubts.get(name,[])
        if len(occ)!=len(supplied):raise ValueError((key,name,len(occ),len(supplied)))
        for i,(o,d) in enumerate(zip(occ,supplied),1):
            after,decision,reason=d
            row(o['line'],o['source'],after,decision,reason,f'{name.upper()}:{key}:{i}')
    nfile=TEXT/'transcription'/('brown_NOTES.tsv' if key.startswith('brown_') else 'ps_NOTES.tsv')
    n=next(r for r in csv.DictReader(nfile.open(),delimiter='\t') if r['key']==key)
    items=[s for s in n['notes'].split(' | ') if not s.lstrip('- ').startswith('LONG-HANDWRITING:') and s!='none']
    if len(items)!=len(notes):raise ValueError((key,'notes',len(items),len(notes)))
    for i,(before,observation) in enumerate(zip(items,notes),1):
        row('',before,observation,'note checked',observation,f'NOTE:{key}:{i}')
    if differences:
        allrows=list(csv.DictReader((TEXT/'records/PS_ARXIV_DIFF.tsv').open(),delimiter='\t'))
        for id,d in differences.items():
            r=allrows[int(id)-1]
            if r['page_key']!=key:raise ValueError((key,id))
            after,decision,reason=d
            row('',r['page_reading'],after,decision,reason,f'DIFF:{id}',r['arxiv_text'])
    if '; not yet checked by eye.' in corrected:
        corrected=corrected.replace('; not yet checked by eye.', '; reviewed against both supplied scan halves; see CHECK_DECISIONS.tsv.')
        row(3,'not yet checked by eye.','reviewed against both supplied scan halves; see CHECK_DECISIONS.tsv.','review metadata updated','Both supplied image halves have now been inspected and all required decisions for this page recorded.',f'META:{key}:reviewheader')
    (PROJECT/'checked_pages'/(key+'.tex')).write_text(corrected)
    append_tsv(PROJECT/'records/CHECK_DECISIONS_134_2.tsv',FIELDS,rows)
    append_tsv(PROJECT/'records/PAGE_REVIEW_134_2.tsv',['key','both_halves_viewed','status','issues_remaining','notes'],[dict(key=key,both_halves_viewed='yes',status='visually reviewed',issues_remaining=sum(len(macro_occurrences(corrected,n)) for n in ['unsure','illegible']),notes=summary)])
    (PROJECT/'review_notes'/(key+'.txt')).write_text(summary+'\n\n'+'\n'.join(f'{r["source_id"]}: {r["reason"]}' for r in rows)+'\n')
    print(key,len(rows),'decisions; remaining doubt marks',sum(len(macro_occurrences(corrected,n)) for n in ['unsure','illegible']))

if __name__=='__main__':
    import sys
    for record in json.loads(Path(sys.argv[1]).read_text()):
        review(**record)
