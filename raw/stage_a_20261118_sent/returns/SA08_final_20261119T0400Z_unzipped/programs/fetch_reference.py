"""Fetch one public research reference; retain an audit record and bytes locally."""
import argparse, pathlib, urllib.request, hashlib, json, datetime
p=argparse.ArgumentParser();p.add_argument('url');p.add_argument('destination');a=p.parse_args()
dest=pathlib.Path(a.destination);dest.parent.mkdir(parents=True,exist_ok=True)
try:
    with urllib.request.urlopen(a.url,timeout=45) as r:
        b=r.read();ctype=r.headers.get('Content-Type','');resolved=r.url
    dest.write_bytes(b)
    result={'url':a.url,'resolved':resolved,'destination':str(dest),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'content_type':ctype,'status':'downloaded'}
except Exception as e:
    result={'url':a.url,'destination':str(dest),'status':'failed','error':str(e)}
result['utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
print(json.dumps(result,ensure_ascii=False))
with (pathlib.Path(__file__).resolve().parents[1]/'logs/reference_fetches.jsonl').open('a') as f:f.write(json.dumps(result)+'\n')
