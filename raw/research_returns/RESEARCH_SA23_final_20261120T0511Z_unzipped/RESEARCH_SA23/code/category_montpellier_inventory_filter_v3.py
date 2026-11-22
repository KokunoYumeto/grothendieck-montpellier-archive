from pathlib import Path
import csv,json,re
r=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
rows=list(csv.DictReader((r/'notes/category_montpellier_inventory_entries.tsv').open(encoding='utf-8'),delimiter='\t'))
terms=['fonctionnell','fredholm','hilbert','nucléair','nucleair','spectral','trace','schwartz','nachbin','tensoriel','banach','résumé','resume','thèse','these','1950','1951','1952','1953','1954','1955','1956']
hits=[]
for row in rows:
    text=' '.join(row[k] for k in ['date','title','notes']).casefold()
    hit=[t for t in terms if t in text]
    if hit: hits.append({'matched':hit,**row})
out={'correction':'v2 search included source-line numbers, causing a spurious 1954 match at cote 9; v3 searches only dates, descriptions and notes. The extracted inventory rows themselves are unchanged.','item_count':len(rows),'hits':hits}
(r/'notes/category_montpellier_inventory_filter_v3.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
for part,start in enumerate(range(0,len(rows),60),1):
    lines=[f"{x['cote']} | {x['date']} | {x['title']}" for x in rows[start:start+60]]
    (r/f'notes/category_montpellier_inventory_titles_{part}.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False,indent=2))
