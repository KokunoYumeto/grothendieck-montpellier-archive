from pathlib import Path
import csv,json
r=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
rows=list(csv.DictReader((r/'notes/category_montpellier_inventory_entries.tsv').open(encoding='utf-8'),delimiter='\t'))
terms=['déterminant','determinant','genre','entières','entieres','weyl','neumann','lidsk','opérateur','operateur','compact','normé','norme','analyse','mémoire','memoir','papiers prêtés','documents isolés']
hits=[]
for row in rows:
    body=' '.join(row[k] for k in ['date','title','notes']).casefold()
    found=[t for t in terms if t in body]
    if found:hits.append({'matched':found,**row})
result={'terms':terms,'entry_count':len(rows),'hits':hits}
(r/'notes/category_montpellier_inventory_additional_terms.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
