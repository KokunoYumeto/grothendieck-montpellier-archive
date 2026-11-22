#!/usr/bin/env python3
"""Seal or verify the ordered page files and their assembly, using SHA-256."""
from pathlib import Path
import argparse,hashlib
from tex_elements import stamp
root=Path(__file__).resolve().parent
pages=sorted((root/'pages').glob('*.tex')); assembled=root/'K58-03_transcription.tex'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def seal(label,line):
 assert len(pages)==15 and assembled.read_bytes()==b''.join(p.read_bytes() for p in pages)
 values=[(digest(p),str(p.relative_to(root))) for p in pages+[assembled]]
 path=root/'audit'/(label+'.sha256')
 with path.open('x') as f:
  for h,p in values:print(h,p,sep='  ',file=f)
 with (root/'progress.log').open('a') as f:
  for h,p in values: print(label,'SHA256',h,p,file=f)
  print(line,stamp(),file=f)
 print(line,(root/'progress.log').read_text().splitlines()[-1])
def verify(label):
 path=root/'audit'/(label+'.sha256')
 for line in path.read_text().splitlines():
  h,name=line.split('  ',1);assert digest(root/name)==h,name
 assert assembled.read_bytes()==b''.join(p.read_bytes() for p in pages)
 print('MATCH: 15 page files and concatenated fragment,',label)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('operation',choices=['seal','check']);ap.add_argument('stage',choices=['frozen','witness']);args=ap.parse_args()
 if args.operation=='seal':seal(args.stage,'transcription frozen' if args.stage=='frozen' else 'witness check done')
 else:verify(args.stage)
