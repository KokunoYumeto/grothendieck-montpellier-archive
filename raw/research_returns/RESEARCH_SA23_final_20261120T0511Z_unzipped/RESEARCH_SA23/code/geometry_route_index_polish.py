from pathlib import Path
import csv,re,json,hashlib
from datetime import datetime,timezone
b=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
p=b/'notes/manuscript_date_attempts.tsv'
rows=list(csv.DictReader(p.open(),delimiter='\t'))
for r in rows:
 if r['route'].startswith('Bourbaki187'):
  r.update(route='Bourbaki 187 / NBR090',evidence='All seven original pages visually read; the first typed page has pencil Schwartz / sept53, with authorship and inscription time unverified.',failed_step='Complete inspected text has no determinant, trace or genus-zero argument and no cote 1 or dated-enclosure identification.',next_step='This exact source check is complete; only a separate explicit connection could date the Montpellier proof.',record='notes/category_bourbaki_r187_r230_date_audit.md')
 if r['route'].startswith('Bourbaki230'):
  r['record']='notes/category_bourbaki_r187_r230_date_audit.md'
 for k in ['route','evidence','failed_step','next_step']:
  s=r[k]
  s=re.sub(r'(?<=[a-z])(?=[A-Z])',' ',s)
  s=re.sub(r'(?<=[A-Za-z])(?=\d)',' ',s)
  s=re.sub(r'(?<=\d)(?=[A-Za-z])',' ',s)
  for a,c in {'physicalPDF':'physical PDF','PDFpages':'PDF pages','PDF/HTML':'PDF / HTML','lowresolution':'low resolution','fulltext':'full text','typedpage':'typed page','genuszero':'genus zero','SaoPaulo':'São Paulo','Sao Paulo':'São Paulo','Szego':'Szegő','Dieudonne':'Dieudonné','Kothe':'Köthe','foliochat':'folio chat','singularvalue':'singular value','old-draft':'older draft','trace-preview':'trace preview','date/enclosure':'date / enclosure','sourcePDF':'source PDF','articlePDF':'article PDF','all-redactions':'all rédactions','item-level':'item-level','datelink':'date link','most1953':'most 1953','note179':'note 179','letters/two':'letters / two','CNPq':'CNPq','toSzego':'to Szegő','after403':'after 403','full6':'full 6','public447':'public 447','endnote':'endnote'}.items(): s=s.replace(a,c)
  r[k]=s
bad=[]
for r in rows:
 for name in r['record'].split('; '):
  if not (b/name).exists():bad.append(name)
# A nonexistent provisional note name is replaced by its actual stable record.
for r in rows:
 if 'notes/algebra_history_Lidskii_audit.md' in r['record']:
  r['record']=r['record'].replace('notes/algebra_history_Lidskii_audit.md','notes/algebra_history_progress.md')
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['route','evidence','failed_step','next_step','record'],delimiter='\t');w.writeheader();w.writerows(rows)
remaining=[n for r in rows for n in r['record'].split('; ') if not (b/n).exists()]
out={'utc':datetime.now(timezone.utc).isoformat(),'rows':len(rows),'corrected_nonexistent_provisional_records':bad,'missing_records_after_correction':remaining,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'pending':[r['route'] for r in rows if 'pending' in r['route']]}
(b/'logs/geometry_route_index_polish.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
