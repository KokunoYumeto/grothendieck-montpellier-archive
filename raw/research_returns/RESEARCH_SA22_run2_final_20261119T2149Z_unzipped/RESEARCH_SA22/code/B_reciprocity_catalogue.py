#!/usr/bin/env python3
"""Read the explicitly linked public catalogue; no login or posting."""
import datetime,hashlib,html,json,re,time,urllib.request
from pathlib import Path
r=Path(__file__).resolve().parents[1];u='https://reciprocity-archive.imj-prg.fr/allarticles';t=time.monotonic()
a=urllib.request.urlopen(u,timeout=25);b=a.read();s=b.decode('utf-8');body=html.unescape(re.sub('<[^>]+>',' ',s));body=re.sub(r'\s+',' ',body)
d={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':u,'status':a.status,'final_url':a.geturl(),'sha256':hashlib.sha256(b).hexdigest(),'article_links':sorted(set(re.findall(r'href=[\"\'](/article/\d+)',s))),'text':body,'target_term_occurrences':{q:len(re.findall(q,body,re.I))for q in ['Gabber','Fujiwara','tubular','Affine analog']},'seconds':round(time.monotonic()-t,3)}
(r/'logs/B_reciprocity_catalogue.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in d.items()if k!='text'},indent=2))
