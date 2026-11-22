"""Create a compact title list and exact keyword contexts from fetched metadata."""
from pathlib import Path
from html.parser import HTMLParser
import hashlib,json,re,csv
ROOT=Path(__file__).resolve().parents[1]
class Text(HTMLParser):
 def __init__(self):super().__init__();self.parts=[]
 def handle_data(self,data):
  if data.strip():self.parts.append(data.strip())
records={};manifest=[]
for path in sorted((ROOT/'sources').glob('category_aronszajn_price_wp_*.json')):
 data=path.read_bytes();payload=json.loads(data)
 manifest.append({'path':str(path.relative_to(ROOT)),'sha256':hashlib.sha256(data).hexdigest(),'count':len(payload)})
 for uri,html in payload.items():
  parser=Text();parser.feed(html);parts=parser.parts
  stop=next((i for i,t in enumerate(parts) if re.match(r'^(Collection|Series|Sub-Series|File)(?:\s|$)',t)),len(parts))
  records[uri]={'title':' '.join(parts[:stop]),'text':'\n'.join(parts)}
with (ROOT/'notes/category_price_inventory_titles.tsv').open('w') as handle:
 writer=csv.writer(handle,delimiter='\t');writer.writerow(['uri','title'])
 writer.writerows((u,r['title']) for u,r in records.items())
pattern=re.compile(r'Groth|Arons|Fredholm|genus|trace|tensor|Hilbert|eigenvalue',re.I)
hits={u:r for u,r in records.items() if pattern.search(r['text'])}
result={'catalogue_record_count':len(records),'keyword_pattern':pattern.pattern,'hits':hits,'sources':manifest,
 'scope':'Public finding-aid metadata only; no original manuscript or correspondence content read.'}
(ROOT/'notes/category_price_inventory_contexts.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'catalogue_record_count':len(records),'keyword_hits':hits,'source_count':len(manifest)},ensure_ascii=False,indent=2))
