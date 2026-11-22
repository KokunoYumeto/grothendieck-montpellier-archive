from pathlib import Path
import csv, json, re, hashlib, html

root=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
p=root/'sources/algebra_history_montpellier_index.html'
raw=p.read_text(encoding='utf-8')
def plain(s):
    return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]*>',' ',s))).strip()
rows=[]
for m in re.finditer(r'<div id="cote-([^"]+)" class="cote">(.*?)</a>\s*</div>',raw,re.S):
    cote,body=m.group(1),m.group(2)
    entry={'cote':cote}
    for key,cls in [('date','date'),('title','titrecote'),('pages','nbpages')]:
        found=re.search(r'<div class="'+cls+r'\b[^\"]*">(.*?)</div>',body,re.S)
        entry[key]=plain(re.sub(r'<!--.*?-->','',found.group(1),flags=re.S)) if found else ''
    src=re.search(r'data-src="([^"]*)"',body)
    entry['advertised_viewer']=html.unescape(src.group(1)) if src else ''
    icon=re.search(r'<span class="mymodal ui sticky" id="icon-'+re.escape(cote)+r'">(.*?)</span>',raw,re.S)
    notes=re.search(r'<div class="notes hyphenate">(.*)</div>\s*$',icon.group(1),re.S) if icon else None
    entry['notes']=plain(notes.group(1)) if notes else ''
    entry['source_line']=raw[:m.start()].count('\n')+1
    rows.append(entry)
out=root/'notes/category_montpellier_inventory_entries.tsv'
with out.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['cote','date','title','pages','notes','advertised_viewer','source_line'],delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(rows)
needles=['fonctionnell','fredholm','hilbert','nucléair','nucleair','spectral','trace','schwartz','nachbin','tensoriel','banach','résumé','resume','thèse','these','1950','1951','1952','1953','1954','1955','1956']
hits=[]
for row in rows:
    s=' '.join(str(v) for v in row.values()).casefold()
    terms=[term for term in needles if term in s]
    if terms:hits.append({'terms':terms,**row})
audit={'source_file':str(p),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'entry_count':len(rows),'cotes':[r['cote'] for r in rows],'terms':needles,'hits':hits}
(root/'notes/category_montpellier_inventory_extract.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(audit,ensure_ascii=False,indent=2))
