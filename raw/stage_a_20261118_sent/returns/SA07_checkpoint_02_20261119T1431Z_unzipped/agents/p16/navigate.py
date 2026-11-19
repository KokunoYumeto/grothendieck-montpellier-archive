from pathlib import Path
import re,json,sys,datetime
BASE=Path('/workspace/scratch/9c0c54a66f6c')
OUT=BASE/'agents/p16'
OUT.mkdir(exist_ok=True)
notes=(BASE/'work/SA07_notes/pro/MPL_16+47+54+44_notes.md').read_text()
tex=(BASE/'work/SA07_texts/pro/MPL_16+47+54+44_transcription.tex').read_text()
entries=[]
matches=list(re.finditer(r'^### (.+)$',notes,re.M))
for i,m in enumerate(matches):
 end=matches[i+1].start() if i+1<len(matches) else len(notes)
 entries.append({'n':i+1,'heading':m.group(1),'line':notes[:m.start()].count('\n')+1,'text':notes[m.start():end]})
(OUT/'entries_source.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2))
pages=[]; cote='?'
for n,line in enumerate(tex.splitlines(),1):
 cm=re.search(r'\\cotefile\{([^}]+)\}',line)
 if cm:cote=cm.group(1)
 sm=re.search(r'\\scanpage\{([^}]+)\}',line)
 if sm:pages.append({'cote':cote,'scan':sm.group(1),'line':n})
for p,q in zip(pages,pages[1:]+[{'line':len(tex.splitlines())+1}]):p['end']=q['line']-1
(OUT/'scan_map.json').write_text(json.dumps(pages,indent=2))
if len(sys.argv)==1:
 print('ENTRIES');print('\n'.join(f"{e['n']:02} L{e['line']}: {e['heading']}" for e in entries))
 print('PAGES');print(json.dumps(pages,ensure_ascii=False))
elif sys.argv[1]=='entries':
 for e in entries[int(sys.argv[2])-1:int(sys.argv[3])]:print(f"ENTRY {e['n']} NOTE-LINE {e['line']}\n{e['text']}")
elif sys.argv[1]=='tex':
 lines=tex.splitlines()
 for n in range(int(sys.argv[2]),min(int(sys.argv[3]),len(lines))+1):print(f'{n}: {lines[n-1]}')
