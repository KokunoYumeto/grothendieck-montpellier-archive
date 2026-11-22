from pathlib import Path
import csv, json, re, hashlib
from bs4 import BeautifulSoup

root=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
p=root/'sources/algebra_history_montpellier_index.html'
raw=p.read_text(encoding='utf-8')
soup=BeautifulSoup(raw,'html.parser')
rows=[]
for div in soup.select('div.cote[id^="cote-"]'):
    cote=div['id'][5:]
    a=div.select_one('a.cotelink')
    entry={k:(div.select_one('.'+css).get_text(' ',strip=True) if div.select_one('.'+css) else '') for k,css in [('date','date'),('title','titrecote'),('pages','nbpages')]}
    entry['cote']=cote
    entry['advertised_viewer']=a.get('data-src','') if a else ''
    icon=soup.select_one('#icon-'+cote)
    entry['notes']=icon.select_one('.notes').get_text(' ',strip=True) if icon and icon.select_one('.notes') else ''
    entry['source_line']=raw[:raw.index('id="cote-'+cote+'"')].count('\n')+1
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
    if terms: hits.append({'terms':terms,**row})
audit={'source_file':str(p),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'entry_count':len(rows),'cotes':[r['cote'] for r in rows],'terms':needles,'hits':hits,'links':[{'text':a.get_text(' ',strip=True),'href':a.get('href'),'src':a.get('data-src')} for a in soup.find_all('a') if re.search(r'invent|\.pdf|catalog|répertoire',a.get_text(' ',strip=True)+' '+str(a.get('href','')),re.I)]}
(root/'notes/category_montpellier_inventory_extract.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(audit,ensure_ascii=False,indent=2))
