"""Reproducible source reader. It indexes locators, never assigns verdicts."""
from pathlib import Path
import argparse, csv, re, json, datetime
BASE=Path(__file__).resolve().parents[2]
WORK=BASE/'SA21_work'
def main():
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['entries','text','doubts','index']);p.add_argument('start',type=int,nargs='?',default=1);p.add_argument('end',type=int,nargs='?',default=999999);a=p.parse_args()
    if a.mode=='entries':
        f=BASE/'sources/notes/pro/MPL_156-1+156-2_notes.md';lines=f.read_text().splitlines();starts=[i for i,s in enumerate(lines) if s.startswith('### ')];rows=list(csv.DictReader((BASE/'sources/notes/NOTES_INDEX.tsv').open(),delimiter='\t'))
        out=[]
        for k,i in enumerate(starts):
            if a.start<=k+1<=a.end:
                j=starts[k+1] if k+1<len(starts) else len(lines)
                out.append('\nENTRY '+str(k+1)+' '+rows[k]['entry_id'])
                out.extend(f'{n+1:04d}: {lines[n]}' for n in range(i,j))
        result='\n'.join(out)
    elif a.mode in ('text','doubts'):
        f=BASE/('sources/texts/pro/MPL_156-1+156-2_transcription.tex' if a.mode=='text' else 'sources/notes/pro/MPL_156-1+156-2_doubts.md')
        lines=f.read_text().splitlines(); result='\n'.join(f'{i+1:04d}: {s}' for i,s in enumerate(lines) if a.start<=i+1<=a.end)
    else:
        rows=[]
        for f in sorted((BASE/'sources/texts').rglob('*_transcription.tex')):
            cote='';scan='';counts={};marks=[]
            for n,s in enumerate(f.read_text().splitlines(),1):
                c=re.search(r'\\cotefile\{([^}]+)\}',s)
                if c:cote=c.group(1)
                q=re.search(r'\\scanpage\{([^}]+)\}',s)
                if q:scan=q.group(1);marks.append({'cote':cote,'scan':scan,'line':n})
            rows.append({'file':str(f.relative_to(BASE/'sources/texts')),'lines':n,'scan_markers':marks})
        result=json.dumps(rows,ensure_ascii=False,indent=2)
    fn=f'{a.mode}_{a.start}_{a.end}.txt'
    (WORK/'outputs'/fn).write_text(result)
    with (WORK/'audit'/'commands.log').open('a') as log:log.write(datetime.datetime.now(datetime.timezone.utc).isoformat()+f'\tpython code/read_sources.py {a.mode} {a.start} {a.end}\toutputs/{fn}\n')
    print(result)
if __name__=='__main__':main()
