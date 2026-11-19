"""Fetch an explicitly supplied primary-source URL and preserve a receipt."""
from pathlib import Path
from urllib.request import Request,urlopen
import argparse,hashlib,json,subprocess,time
parser=argparse.ArgumentParser()
parser.add_argument('name')
parser.add_argument('url')
args=parser.parse_args()
base=Path(__file__).resolve().parents[1]
started=time.monotonic()
dest=base/'sources'/args.name
try:
    with urlopen(Request(args.url,headers={'User-Agent':'SA08 primary-source verification'}),timeout=55) as response:
        data=response.read()
    dest.write_bytes(data)
    record=dict(file=str(dest),url=args.url,bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    if dest.suffix=='.pdf':
        subprocess.run(['pdftotext','-layout',str(dest),str(dest.with_suffix('.txt'))],check=True)
except Exception as error:
    record=dict(file=str(dest),url=args.url,error=repr(error))
record['seconds']=time.monotonic()-started
(base/'logs'/(dest.stem+'_fetch.json')).write_text(json.dumps(record,indent=2))
print(json.dumps(record))
