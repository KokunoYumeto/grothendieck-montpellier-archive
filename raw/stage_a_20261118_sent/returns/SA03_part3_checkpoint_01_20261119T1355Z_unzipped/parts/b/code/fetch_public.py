"""Fetch a public source URL already observed in web search, preserving a checksum.
No access controls, credentials, or browser state are used.
"""
import argparse, hashlib, urllib.request
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument('url'); p.add_argument('path')
a=p.parse_args()
try:
    with urllib.request.urlopen(a.url,timeout=30) as response:
        data=response.read()
    Path(a.path).parent.mkdir(parents=True,exist_ok=True)
    Path(a.path).write_bytes(data)
    print(a.url, len(data), hashlib.sha256(data).hexdigest(), a.path, sep='\t')
except Exception as e:
    print(type(e).__name__,str(e))
    raise SystemExit(1)
