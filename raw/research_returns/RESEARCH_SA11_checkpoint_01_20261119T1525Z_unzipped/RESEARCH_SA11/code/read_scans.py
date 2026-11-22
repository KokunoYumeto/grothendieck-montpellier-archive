#!/usr/bin/env python3
"""Extract supplied transcription pages, retaining doubtful-reading macros.
Usage: read_scans.py filename scan[,scan...] [--figures]
The compact output omits TikZ pictures; figures must be checked separately.
"""
import sys, re, pathlib, datetime, json
src = pathlib.Path(sys.argv[1])
pages = set()
for part in sys.argv[2].split(','):
    if '-' in part:
        a,b=map(int,part.split('-')); pages.update(range(a,b+1))
    else: pages.add(int(part))
text=src.read_text()
marks=list(re.finditer(r'\\scanpage\{(\d+)\}',text))
out=[]
for i,m in enumerate(marks):
    page=int(m[1])
    if page not in pages: continue
    end=marks[i+1].start() if i+1<len(marks) else len(text)
    part=text[m.start():end]
    if '--figures' not in sys.argv:
        part=re.sub(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', '[TIKZ FIGURE OMITTED]', part, flags=re.S)
    startline=text[:m.start()].count('\n')+1
    out.append(f'\nSOURCE {src.name}, scan {page}, beginning at line {startline}\n'+part)
result=''.join(out)
root=pathlib.Path(__file__).resolve().parent.parent
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%f')
(root/'audit'/f'root_read_{stamp}.txt').write_text(result)
print(result)
