"""Read the author's DVI despite missing TeX rendering assets.
Retain DVItype character output; mathematical glyphs require source collation.
This does not repair or claim a successful PDF conversion.
"""
from pathlib import Path
import subprocess,re
p=Path(__file__).resolve().parents[1]/'work/middle/references'
for name in ['dejong1998','dejong1999err']:
 r=subprocess.run(['dvitype',str(p/(name+'.dvi'))],capture_output=True,text=True)
 (p/(name+'_dvitype.log')).write_text(r.stdout+r.stderr)
 blocks=[]
 for line in r.stdout.splitlines():
  if 'beginning of page' in line:blocks.append('\nPAGE '+line.split('beginning of page ')[-1])
  elif line.startswith('[') and line.endswith(']'):blocks.append(line[1:-1])
 (p/(name+'_extracted.txt')).write_text('\n'.join(blocks))
 print(name,'returncode',r.returncode,'blocks',len(blocks))
