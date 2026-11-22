"""Inspect existing public-source metadata without probing new file paths."""
from pathlib import Path
from html.parser import HTMLParser
from pypdf import PdfReader
import datetime, hashlib, json, re, subprocess, time

base=Path(__file__).resolve().parents[1]
start=time.perf_counter()
source=base/'sources/algebra_history_cirm_inventory.pdf'
reader=PdfReader(source)
pdf_links=[]
for i,page in enumerate(reader.pages,1):
 for ref in page.get('/Annots',[]):
  annotation=ref.get_object()
  action=annotation.get('/A')
  if action:
   action=action.get_object()
   pdf_links.append({'page':i,'action_type':str(action.get('/S')),'uri':str(action.get('/URI'))})

class Links(HTMLParser):
 def __init__(self):
  super().__init__();self.rows=[];self.active=None
 def handle_starttag(self,tag,attrs):
  if tag=='a':
   attrs=dict(attrs)
   if 'href' in attrs:self.active={'href':attrs['href'],'text':''}
 def handle_data(self,data):
  if self.active is not None:self.active['text']+=data
 def handle_endtag(self,tag):
  if tag=='a' and self.active is not None:
   self.active['text']=' '.join(self.active['text'].split())
   self.rows.append(self.active);self.active=None

html_records=[]
for name in ['algebra_history_montpellier_home.html','algebra_history_montpellier_index.html']:
 p=base/'sources'/name
 parser=Links();parser.feed(p.read_text(errors='replace'))
 html_records.append({'source':str(p.relative_to(base)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'all_links':parser.rows,'candidate_finding_aid_links':[r for r in parser.rows if re.search(r'inventaire|annexe|chemise|r[eé]pertoire|fonds|fonctionnelle',r['text']+' '+r['href'],re.I)]})

argv=['pdfimages','-f','12','-l','12','-list',str(source)]
run=subprocess.run(argv,capture_output=True,text=True)
image_info={'argv':argv,'returncode':run.returncode,'stdout':run.stdout,'stderr':run.stderr}

# The first broad rg result was truncated in the tool display. Preserve a
# complete rerun as a retrievable text cache, without printing it again.
paths=[*sorted((base/'notes').glob('algebra*')),*sorted((base/'code').glob('algebra*'))]
argv=['rg','-n','cirm|CIRM|chemise|boîte|A.C',*[str(p) for p in paths]]
run=subprocess.run(argv,capture_output=True,text=True)
cache=base/'sources/geometry_folders_initial_rg_full.txt'
cache.write_text(run.stdout)
rg_record={'argv':argv,'returncode':run.returncode,'stderr':run.stderr,'stdout_cache':str(cache.relative_to(base)),'stdout_bytes':cache.stat().st_size,'stdout_sha256':hashlib.sha256(cache.read_bytes()).hexdigest(),'scope':'Complete later rerun saved after the first display was truncated; not all returned source text was visually read.'}

out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-start,'pdf_source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'pdf_pages':len(reader.pages),'pdf_links':pdf_links,'html_link_records':html_records,'slide12_image_metadata':image_info,'initial_rg_rerun':rg_record,'network_requests':0,'private_paths_probed':0,'contacts_sent':0}
(base/'logs/geometry_folders_metadata.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps({'pdf_pages':len(reader.pages),'pdf_links':pdf_links,'html_counts':[{ 'source':r['source'],'links':len(r['all_links']),'candidates':r['candidate_finding_aid_links']} for r in html_records],'elapsed_seconds':out['elapsed_seconds'],'rg_full_output_bytes':rg_record['stdout_bytes']},ensure_ascii=False,indent=2))
