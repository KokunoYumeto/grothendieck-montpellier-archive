#!/usr/bin/env python3
"""Fetch frozen official mathematical table sources; execute none of them."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,urllib.request
R=Path(__file__).resolve().parent
COMMIT='87231738271ed548f62e7f1c98ff2bbfc1ed30d3'
PATHS=['A2/SL3.1.jl','A2/SL3.n1.jl','2A2/SU3.2.jl','2A2/SU3.n2.jl']
def fetch(path):
    url=f'https://raw.githubusercontent.com/oscar-system/GenericCharacterTables.jl/{COMMIT}/data/Tables/{path}'
    out=R/'cache'/Path(path).name;out.parent.mkdir(parents=True,exist_ok=True)
    if not out.exists():out.write_bytes(urllib.request.urlopen(url,timeout=20).read())
    raw=out.read_bytes()
    return {'path':'data/Tables/'+path,'url':url,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
def main():
    with ThreadPoolExecutor(max_workers=4) as pool:files=list(pool.map(fetch,PATHS))
    data={'commit':COMMIT,'files':files,'scope':'Frozen original mathematical data; no bound or theorem yet.'}
    (R/'retrieval.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data))
if __name__=='__main__':main()
