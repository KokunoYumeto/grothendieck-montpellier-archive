"""Compare the deposited image readings with the first pass and delivered pages."""
from pathlib import Path
import csv
import re
import sys
import runpy

root = Path(__file__).resolve().parent
def records(name):
    with (root/name).open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f,delimiter='\t'))
def canonical(s):
    return re.sub(r'\s+|\$', '', s)
def literal(s):
    return '<code>'+s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('|','&#124;').replace('\n',' ')+'</code>'
blind = records('K62-06_blind.tsv')
corrective = [row for row in blind if row['place'].startswith('corrective / ')]
blind = [row for row in blind if row not in corrective]
previous = runpy.run_path(str(root/'K62-06_corrective_versions.py'))['preceding_pages']()
anchors = {(r['scan'],r['place']):r for r in records('K62-06_blind_anchors.tsv')}
wfile = root/'K62-06_witness_anchors.tsv'
changes = records(wfile.name) if wfile.exists() else []
res = ['# Blind readings compared with the page files','',
       'The blind ledger was written from the images before each page was reopened. The first-pass column preserves the corresponding excerpt. Changes of wording or page state are listed individually; typographic equivalences and shorter blind excerpts also appear. Layout whitespace and math delimiters are ignored for matching. The full blind ledger includes the agreements. The final excerpt includes later decisions at frozen doubt marks. Its limits may expand to include a whole marked expression at its boundary.','',
       '| Scan | Place | Blind reading | First pass | After second reading | Final page excerpt | Crop decision |',
       '|---|---|---|---|---|---|---|']
missing=[]
pages={}
counts={}
for record in blind:
    n,place,b=record['scan'],record['place'],record['what_the_crop_shows']
    r=anchors[n,place]
    first,a=r['first_pass'],r['after_second_reading']
    if n not in pages:
        pages[n]=previous['pages/K62-06_62_scan%03d.tex'%int(n)].decode('utf8')
    current=r.get('final_anchor',a)
    if canonical(current) not in canonical(pages[n]):
        for w in changes:
            if w['scan']==n and w['frozen'] in current:
                current=current.replace(w['frozen'],w['final'])
        if canonical(current) not in canonical(pages[n]):
            replacement=r.get('final_anchor','')
            if not replacement or canonical(replacement) not in canonical(pages[n]):
                missing.append((n,place))
    if canonical(b)!=canonical(first) or canonical(a)!=canonical(first):
        counts[n]=counts.get(n,0)+1
        res.append('| '+' | '.join([n,place,literal(b),literal(first),literal(a),literal(current),r['resolution'].replace('|','&#124;')])+' |')
res+=['','%d blind passages. %d differences of reading, coverage or TeX form. %d unresolved anchor lookups.'%(len(blind),sum(counts.values()),len(missing)),'']
for n,place in missing: res.append('- Scan '+n+', '+place)
res.extend(['', 'Differences by scan','',
            '| Scan | Differences |', '|---|---:|']+
           ['| '+n+' | '+str(counts.get(n,0))+' |' for n in sorted(pages,key=int)])
res.extend(['', 'The audit also records changes outside the particular blind excerpts. On scan 44 the second inverse-image symbol was corrected from 0 to infinity after comparing both pairs of loops. The blind entry at that location quotes the first inverse image.',''])
res.extend(['', '## Independent corrective comparison', '',
    'The table above compares the first worker’s blind lines against the exact preceding issued page state, reconstructed from the current pages. The following independent observations were deposited before consulting each page file in the corrective pass. Each row names one literal locator in the current page. A locator covers only part of the longer observation. The scan audit gives the remaining decisions, including subsequent enlargements and the witness check.', '',
    '| Scan | Place | Independent observation | Current page locator | Decision |',
    '|---:|---|---|---|---|'])
cr = records('K62-06_corrective_comparison.tsv')
assert len(cr)==len(corrective)
for r,b in zip(cr,corrective):
    assert r['scan']==b['scan'] and 'corrective / '+r['place']==b['place']
    page=(root/'pages'/('K62-06_62_scan%03d.tex'%int(r['scan']))).read_text(encoding='utf8')
    assert r['current_locator'] in page, (r['scan'],r['place'],r['current_locator'])
    res.append('| '+' | '.join((r['scan'],r['place'],literal(b['what_the_crop_shows']),literal(r['current_locator']),r['decision'].replace('|','&#124;')))+' |')
res.extend(['',str(len(cr))+' additional independent observations checked against literal current-page locators.',''])
(root/'K62-06_blind_compare.md').write_text('\n'.join(res),encoding='utf8',newline='\n')
print('%d preceding blind passages, %d differences. %d unresolved earlier anchors. %d corrective observations with verified current-page locators.'%(len(blind),sum(counts.values()),len(missing),len(cr)))
if missing: sys.exit(1)
