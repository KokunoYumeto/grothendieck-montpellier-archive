"""Fetch public, documented Sudoc metadata and public exhibition brochure."""
import concurrent.futures, datetime, hashlib, json, pathlib, time, urllib.request
import fitz
base=pathlib.Path(__file__).resolve().parents[1]
targets=[
 ('thesis_multiwhere108391841','https://www.sudoc.fr/services/multiwhere/108391841','xml'),
 ('thesis_unimarc108391841','https://www.sudoc.fr/108391841.xml','xml'),
 ('thesis_exhibition_livret','https://exposition-grothendieck.org/wp-content/uploads/2025/05/Livret.pdf','pdf'),
]
def fetch(target):
 name,url,suffix=target;start=time.monotonic();rec={'name':name,'url':url,'utc_started':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(url,timeout=25) as response:
   raw=response.read();rec.update(http_status=response.status,final_url=response.url,content_type=response.headers.get('Content-Type'))
  path=base/f'sources/algebra_history_{name}.{suffix}';path.write_bytes(raw)
  rec.update(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),path=str(path.relative_to(base)))
  if suffix=='pdf':
   doc=fitz.open(path);rec['pdf_pages']=len(doc)
   texts=[p.get_text() for p in doc]
   (base/f'sources/algebra_history_{name}.txt').write_text('\n\f\n'.join(texts))
   rec['page_text_lengths']=[len(t) for t in texts]
  else:rec['text']=raw.decode('utf-8',errors='replace')
 except Exception as exc:rec['error']=repr(exc)
 rec['elapsed_seconds']=time.monotonic()-start;rec['utc_completed']=datetime.datetime.now(datetime.timezone.utc).isoformat()
 return rec
start=time.monotonic()
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:records=list(pool.map(fetch,targets))
out={'records':records,'elapsed_seconds':time.monotonic()-start}
payload=json.dumps(out,ensure_ascii=False,indent=2)
(base/'logs/algebra_history_thesis45.json').write_text(payload+'\n');print(payload)
