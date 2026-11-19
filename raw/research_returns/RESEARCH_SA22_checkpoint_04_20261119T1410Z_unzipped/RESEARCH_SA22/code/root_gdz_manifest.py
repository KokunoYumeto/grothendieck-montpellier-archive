from pathlib import Path
import urllib.request,time,json
R=Path(__file__).resolve().parents[1];T=time.perf_counter();j=json.loads((R/'code/root_gdz_discovery_output.json').read_text());u=next(x for x in j['links'] if 'manifest' in x);out={'url':u}
try:
 with urllib.request.urlopen(u,timeout=45) as f:b=f.read();out.update(status=f.status,bytes=len(b))
 (R/'sources/koebe1907_volume_manifest.json').write_bytes(b);d=json.loads(b)
 out['keys']=list(d);out['rendering']=d.get('rendering');out['seeAlso']=d.get('seeAlso')
 def walk(o):
  if isinstance(o,dict):
   if any(w in str(o.get('label','')) for w in ['Uniformisierung','191','633']):out.setdefault('matches',[]).append({k:v for k,v in o.items() if k not in ['items','canvases','images','structures']})
   for k,v in o.items():
    if k in ['items','sequences','canvases','structures','ranges']:walk(v)
  elif isinstance(o,list):
   for v in o:walk(v)
 walk(d)
except Exception as e:out['error']=repr(e)
out['seconds']=time.perf_counter()-T
(R/'code/root_gdz_manifest_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
