import json
from pathlib import Path
p=Path('/tmp/SA04_root_external/Groth1966_manifest.json')
d=json.loads(p.read_text())
out=[]
out.append({'top_keys':list(d),'rendering':d.get('rendering'),'seeAlso':d.get('seeAlso')})
def walk(x):
 if isinstance(x,dict):
  if 'label' in x and ('Groth' in str(x['label']) or 'homomorph' in str(x['label'])):out.append(x)
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
walk(d.get('structures',[]))
pages=d.get('sequences',[{}])[0].get('canvases',d.get('items',[]))
out.append({'page67':pages[66] if len(pages)>66 else None})
text=json.dumps(out,indent=2,ensure_ascii=False)
(Path(__file__).resolve().parents[1]/'outputs/root_gdz_extract.json').write_text(text+'\n')
print(text)
