#!/usr/bin/env python3
"""Page-review packets and explicit, auditable review commits.

Run from the directory containing transcription/, records/, and scans/.
No image decision is inferred by this program. A human/vision reviewer supplies
all findings in review/<page-key>.json; commit validates and applies those edits.
"""
import argparse, collections, csv, hashlib, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = json.loads((ROOT/'records/PAGES_PS.json').read_text())
PAGE_MAP = {p['key']:p for p in PAGES}
DIFFS = list(csv.DictReader((ROOT/'records/PS_ARXIV_DIFF.tsv').open(), delimiter='\t'))
for i, row in enumerate(DIFFS, 1):
    row['row_id'] = f'D{i:05d}'
AUTO_KINDS = {'normalization', 'silent correction', 'handwritten note merged (unmarked in arXiv)'}
NOTES = {}
for name in ('ps', 'brown'):
    NOTES.update({r['key']:r for r in csv.DictReader((ROOT/f'transcription/{name}_NOTES.tsv').open(), delimiter='\t')})

def source(key):
    return ROOT/'transcription'/('brown_pages' if key.startswith('brown_') else 'ps_pages')/(key+'.tex')

def groups(s, start):
    """Return one balanced TeX brace argument; escaped braces do not nest."""
    if start >= len(s) or s[start] != '{':
        raise ValueError(f'Expected brace at {start}')
    depth=1; i=start+1
    while i<len(s):
        if s[i]=='\\': i+=2; continue
        if s[i]=='{': depth+=1
        elif s[i]=='}':
            depth-=1
            if not depth: return s[start+1:i],i+1
        i+=1
    raise ValueError(f'Unbalanced argument at {start}')

def marks(s):
    result=[]
    for m in re.finditer(r'\\(unsure|illegible)\s*\{',s):
        try: arg,end=groups(s,m.end()-1)
        except ValueError: arg=s[m.end():m.end()+120]; end=m.end()+len(arg)
        result.append({'id':f'U{len(result)+1:03d}','kind':m.group(1),'line':s.count('\n',0,m.start())+1,'reading':s[m.start():end],'content':arg})
    return result

def packet(key, compact=False):
    p=PAGE_MAP[key]; s=source(key).read_text()
    rows=[r for r in DIFFS if r['page_key']==key]
    print(json.dumps({'page':p,'notes':NOTES.get(key),'doubts':marks(s)},ensure_ascii=False,indent=2))
    print('\nTRANSCRIPTION')
    for i,line in enumerate(s.splitlines(),1): print(f'{i:03}: {line}')
    print('\nARXIV DIFFERENCES')
    for r in rows:
        if compact and r['kind'] in AUTO_KINDS: continue
        print(json.dumps({k:r[k] for k in ('row_id','kind','arxiv_file','arxiv_line','arxiv_section','arxiv_text','page_reading','note')},ensure_ascii=False))
    print('IMAGE FILES',*[f'scans/{key}_{half}.jpg' for half in ('a','b')])

def commit(key):
    record_path=ROOT/'review'/(key+'.json')
    r=json.loads(record_path.read_text()); s=source(key).read_text()
    assert r['key']==key
    assert r.get('viewed_halves')==['a','b'], 'Both halves must actually be viewed'
    assert r.get('review_status')=='complete', 'Partial reviews cannot populate checked_pages'
    assert r.get('notes_review'), 'Record a response to page notes'
    assert r.get('known_error_review'), 'Record the known-error review'
    required={x['row_id'] for x in DIFFS if x['page_key']==key and x['kind'] not in AUTO_KINDS}
    supplied={x['id'] for x in r.get('diff_decisions',[])}
    assert required<=supplied, f'Missing decision rows: {required-supplied}'
    assert {x['id'] for x in marks(s)}=={x['id'] for x in r.get('doubt_decisions',[])}, 'Every initial doubt needs an explicit outcome'
    for x in r.get('diff_decisions',[])+r.get('doubt_decisions',[]):
        assert x.get('reason') and x.get('image_reading') and x.get('decision')
    for edit in r.get('changes',[]):
        old,new=edit['old'],edit['new']
        assert old!=new and edit.get('reason')
        assert s.count(old)==1, f'Edit must identify one occurrence: {old!r}, found {s.count(old)}'
        edit.setdefault('source_line',s.count('\n',0,s.index(old))+1)
        s=s.replace(old,new,1)
    r['source_sha256']=hashlib.sha256(source(key).read_bytes()).hexdigest()
    r['checked_sha256']=hashlib.sha256(s.encode()).hexdigest()
    r['doubts_before']=len(marks(source(key).read_text()))
    r['doubts_after']=len(marks(s))
    (ROOT/'checked_pages'/(key+'.tex')).write_text(s)
    record_path.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'committed':key,'changes':len(r.get('changes',[])),'doubts_before':r['doubts_before'],'doubts_after':r['doubts_after']}))

def status():
    done={p.stem for p in (ROOT/'checked_pages').glob('*.tex')}
    for cote in sorted({p['cote'] for p in PAGES}):
        keys=[p['key'] for p in PAGES if p['cote']==cote]
        print(cote,sum(k in done for k in keys),'/',len(keys))

if __name__=='__main__':
    a=argparse.ArgumentParser(); a.add_argument('action',choices=['packet','commit','status']); a.add_argument('keys',nargs='*'); a.add_argument('--compact',action='store_true'); ns=a.parse_args()
    if ns.action=='status': status()
    else:
        for key in ns.keys:
            (packet(key,ns.compact) if ns.action=='packet' else commit(key))
