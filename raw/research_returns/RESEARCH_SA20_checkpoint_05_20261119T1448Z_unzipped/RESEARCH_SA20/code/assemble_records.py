#!/usr/bin/env python3
"""Assemble current statement records without changing agents' source files."""
import csv, pathlib, re
ROOT=pathlib.Path(__file__).resolve().parents[1]
fields=['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
records={}
for p in sorted((ROOT/'agents').glob('*/results*.csv')):
    with p.open(newline='') as f:
        for row in csv.DictReader(f):
            if row.get('id'):
                rec={k:row.get(k,'') for k in fields}
                loc=rec['where_proved']
                if loc.startswith(('part_', 'unchecked_')):
                    rec['where_proved']=str(p.parent.relative_to(ROOT))+'/'+loc
                records[row['id']]=rec
p=ROOT/'notes/root_results.csv'
if p.exists():
    with p.open(newline='') as f:
        for row in csv.DictReader(f): records[row['id']]=row
for p in sorted([*(ROOT/'parts').glob('*.tex'), *(ROOT/'agents').glob('*/part_*.tex')]):
    if p.name.startswith('unchecked'): continue
    text=p.read_text()
    for m in re.finditer(r'\\begin\{saresult\}\{([^}]*)\}\{([^}]*)\}\{([^\n]*)\}',text):
        ident,status,title=m.groups()
        records.setdefault(ident,dict(zip(fields,[ident,title,status,str(p.relative_to(ROOT)),'','','Auto-extracted current author label; metadata and independent audit are being completed.'])))
with (ROOT/'RESEARCH_SA20_results.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
    for ident in sorted(records): w.writerow(records[ident])
checks=[]
for p in [ROOT/'notes/root_checks.tsv',*sorted((ROOT/'agents').glob('*/checks*.tsv'))]:
    if p.exists(): checks.extend(p.read_text().splitlines()[1:])
(ROOT/'CHECK_EVENTS.tsv').write_text('statement_id\tdate\twho\ttype\toutcome\n'+'\n'.join(dict.fromkeys(checks))+'\n')
bibs=[ROOT/'notes/root_references.bib',*sorted((ROOT/'agents').glob('*/references.bib'))]
(ROOT/'RESEARCH_SA20_references.bib').write_text('\n\n'.join(p.read_text() for p in bibs if p.exists()))
print(f'{len(records)} statements; {len(set(checks))} check events; {len(bibs)} bibliography inputs')
