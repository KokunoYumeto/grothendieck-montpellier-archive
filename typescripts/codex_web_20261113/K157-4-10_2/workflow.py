from pathlib import Path
from datetime import datetime, timezone
import csv

OUT = Path(__file__).resolve().parent
TASK = OUT.parent.name
def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def append_tsv(name, header, rows):
    p = OUT / name
    new = not p.exists()
    with p.open('a', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t')
        if new: w.writerow(header)
        w.writerows(rows)

def save_page(scan, text, elements, notation=(), doubts=(), kind='text', hand='Grothendieck'):
    p = OUT / 'pages' / f'{TASK}_157-4_scan{scan:03}.tex'
    p.write_text(text.strip()+'\n', encoding='utf-8')
    inv = OUT / f'{TASK}_inventory.csv'
    new = not inv.exists()
    with inv.open('a', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        if new: w.writerow(['cote','scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'])
        for i, (k, pos, words) in enumerate(elements, 1):
            w.writerow(['157-4',scan,kind,hand,f'{scan:03}-{i:02}',k,pos,words,'yes'])
    append_tsv('notation_entries.tsv',['scan','position','LaTeX','visible_strokes_and_comparison'],[(scan,*r) for r in notation])
    append_tsv('reading_doubts.tsv',['scan','position','reading','alternatives','confidence','context_and_ink'],[(scan,*r) for r in doubts])
    with (OUT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'scan {scan:03} done {utc()}\n')
    print(f'scan {scan:03} saved; {len(elements)} inventory elements; {utc()}')
