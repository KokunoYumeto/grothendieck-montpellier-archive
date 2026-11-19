"""Render selected pages of a public reference for visual verification."""
import argparse,json,subprocess
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('pdf');p.add_argument('pages',nargs='+',type=int);a=p.parse_args()
src=Path(a.pdf).resolve()
for page in a.pages:
 out=src.parent/(src.stem+f'-p{page}')
 subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-scale-to','1700','-png','-singlefile',str(src),str(out)],check=True)
 print(json.dumps({'pdf':str(src),'page':page,'image':str(out)+'.png'}))
