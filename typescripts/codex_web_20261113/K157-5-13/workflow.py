#!/usr/bin/env python3
"""Local transcription bookkeeping; no image recognition and no TeX compilation."""
from pathlib import Path
import csv, re, sys, datetime, hashlib

OUT = Path(__file__).resolve().parent
TASK = OUT.parent.name
def utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def log(s):
    with (OUT/'progress.log').open('a',encoding='utf-8') as f: f.write(s+'\n')
def argument(s,start):
    depth=1; i=start
    while i<len(s):
        if s[i]=='\\':
            i+=2; continue
        if s[i]=='{': depth+=1
        elif s[i]=='}':
            depth-=1
            if not depth:return s[start:i],i+1
        i+=1
    raise ValueError('Unclosed macro argument')
def inventory():
    rows=[]
    for p in sorted((OUT/'pages').glob('*.tex')):
        scan=int(re.search(r'scan(\d+)',p.name)[1]); s=p.read_text(); serial=0; pos=''; kind='text'; skip_macro=None
        for match in re.finditer(r'^% element: ([^|]+)\|([^|]+)\|([^\n]+)|\\(inserted|deleted|margin|handwritten)\{',s,re.M):
            if match.group(1):
                kind,pos,first=[x.strip() for x in match.group(1,2,3)]
                serial+=1;rows.append(['157-5',scan,'text','Grothendieck',f'{scan}.{serial:02}',kind,pos,first,'yes'])
                skip_macro={'margin note':'margin','deletion':'deleted','insertion':'inserted','handwritten':'handwritten'}.get(kind)
            else:
                macro=match.group(4)
                if macro==skip_macro:
                    skip_macro=None
                    continue
                value,_=argument(s,match.end()); k={'inserted':'insertion','deleted':'deletion','margin':'margin note','handwritten':'handwritten'}[macro]
                serial+=1; rows.append(['157-5',scan,'text','Grothendieck',f'{scan}.{serial:02}',k,pos+'; TeX line '+str(s[:match.start()].count('\n')+1),value[:240],'yes'])
    with (OUT/f'{TASK}_inventory.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['cote','scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']);w.writerows(rows)
    return len(rows)
if __name__=='__main__':
    action=sys.argv[1]
    if action=='done':
        n=inventory();log(f'scan {int(sys.argv[2]):03} done {utc()}');print(f'Inventory: {n} elements; page {sys.argv[2]} saved.')
    elif action=='inventory':print(inventory())
    elif action=='assemble':
        pages=sorted((OUT/'pages').glob('*.tex'))
        (OUT/f'{TASK}_transcription.tex').write_text('\n'.join(p.read_text().rstrip()+'\n' for p in pages),encoding='utf-8')
        (OUT/f'{TASK}_standalone.tex').write_text('\\input{PREAMBLE.tex}\n\\begin{document}\n\\input{'+TASK+'_transcription}\n\\end{document}\n',encoding='utf-8')
        print(f'Assembled {len(pages)} pages.')
