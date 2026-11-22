#!/usr/bin/env python3
"""Extract the topical and positional formula register from the diplomatic leaves."""
import csv,re
from pathlib import Path
from tex_elements import arguments
root=Path(__file__).resolve().parent
mathrows=[];indexrows=[]
def clean(v):return re.sub(r'\s+',' ',v).strip()
def add(n,j,lin,typ,s):
 mathrows.append([n,j,lin,typ,clean(s)])
 for pos in re.finditer(r'(?P<pos>[_^])\s*(?P<val>[ij](?![A-Za-z])|(?<!\\)\{(?:[^{}]|\{[^{}]*\})*\})',s):
  val=pos['val']; glyphs=re.findall(r'(?<![A-Za-z\\])([ij])(?![A-Za-z])',val)
  for k in glyphs:indexrows.append([n,j,lin,typ,'superscript' if pos['pos']=='^' else 'subscript',k,clean(val),clean(s)])
for p in sorted((root/'pages').glob('*.tex')):
 n=int(p.stem[-3:]);raw=p.read_text()
 s=re.sub(r'(?m)(?<!\\)%[^\n]*',lambda m:' '*len(m[0]),raw)
 spans=re.compile(r'\\\[(?P<disp>.*?)\\\]|\\begin\{tikzcd\}(?:\[[^\]]*\])?(?P<dia>.*?)\\end\{tikzcd\}|(?<!\\)\$(?P<sm>.*?)(?<!\\)\$',re.S)
 j=0
 for m in spans.finditer(s):
  j+=1;lin=1+s.count('\n',0,m.start())
  if m['dia'] is not None:
   for y,line in enumerate(re.split(r'\\\\',m['dia']),1):
    for x,cell in enumerate(re.split(r'\\&',line),1):
     obj=cell.split(r'\arrow',1)[0]
     add(n,f'{j}.{y}.{x}',lin,'diagram cell',obj)
     for ar in re.findall(r'\\arrow\[([^\]]+)\]',cell):
      add(n,f'{j}.{y}.{x}',lin,'diagram arrow and label',ar)
  else:add(n,j,lin,'display' if m['disp'] is not None else 'inline',m['disp'] if m['disp'] is not None else m['sm'])
for fn,head,rows in [('formulas.tsv',['scan','ordinal','source line','kind','formula or label'],mathrows),('indexed_i_j.tsv',['scan','formula ordinal','source line','kind','position','letter','script content','containing formula or label'],indexrows)]:
 with (root/'audit'/fn).open('w',newline='') as f:
  w=csv.writer(f,delimiter='\t');w.writerow(head);w.writerows(rows)
print(len(mathrows),'formula entries and diagram components;', len(indexrows),'indexed i or j occurrences')
