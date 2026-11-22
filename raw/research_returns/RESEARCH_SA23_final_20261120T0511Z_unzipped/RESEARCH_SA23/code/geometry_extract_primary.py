"""Reproduce retained page renderings and OCR from a public primary scan.

Example: python geometry_extract_primary.py SOURCE.pdf 214 geometry_PTT_p214
Optional URL downloads SOURCE.pdf only if it is absent. No credentials.
"""
from pathlib import Path
from time import perf_counter
import argparse, subprocess, urllib.request

p=argparse.ArgumentParser()
p.add_argument('pdf',type=Path)
p.add_argument('page',type=int)
p.add_argument('output_prefix',type=Path)
p.add_argument('--url')
p.add_argument('--dpi',type=int,default=150)
args=p.parse_args(); start=perf_counter()
if not args.pdf.exists():
    if not args.url: p.error('absent PDF requires its public --url')
    with urllib.request.urlopen(args.url,timeout=180) as response:
        data=response.read()
    if not data.startswith(b'%PDF'): raise ValueError('response is not PDF')
    args.pdf.write_bytes(data)
    print('downloaded',args.url,len(data),'bytes')
subprocess.run(['pdftoppm','-f',str(args.page),'-l',str(args.page),
                '-scale-to','1800','-png','-singlefile',str(args.pdf),
                str(args.output_prefix)],check=True)
subprocess.run(['tesseract',str(args.output_prefix)+'.png',
                str(args.output_prefix),'-l','eng'],check=True)
print('rendered and OCRed',args.pdf,'PDF page',args.page,'to',args.output_prefix)
print('elapsed_seconds',round(perf_counter()-start,3))
