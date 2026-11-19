#!/usr/bin/env python3
"""Download an explicitly selected public source, recording URL/hash only in deliverable log."""
import argparse,urllib.request,hashlib,json,datetime
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('url');p.add_argument('destination');a=p.parse_args()
dest=Path(a.destination);dest.parent.mkdir(parents=True,exist_ok=True)
with urllib.request.urlopen(a.url,timeout=50) as r: data=r.read()
dest.write_bytes(data)
print(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':a.url,'destination':str(dest),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}))
