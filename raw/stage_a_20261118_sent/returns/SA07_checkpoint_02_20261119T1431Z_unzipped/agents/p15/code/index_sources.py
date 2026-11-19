from pathlib import Path
import re,json,csv,sys
root=Path('/workspace/scratch/9c0c54a66f6c')
pkg='MPL_15_195-228+18_002-017'
p=root/'work/SA07_notes/pro'/f'{pkg}_notes.md'
s=p.read_text(); starts=list(re.finditer(r'^### (.*)$',s,re.M))
entries=[]
for i,m in enumerate(starts):
    e=s[m.start():starts[i+1].start() if i+1<len(starts) else len(s)]
    entries.append(dict(entry_id=f'{pkg}#{i+1}',heading=m.group(1),source_line=s[:m.start()].count('\n')+1,text=e))
(root/'agents/p15/entries_source.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2))
tex=(root/'work/SA07_texts/pro'/f'{pkg}_transcription.tex').read_text().splitlines()
pages=[]; cote=None
for i,line in enumerate(tex,1):
    m=re.search(r'\\cotefile\{([^}]+)\}',line)
    if m:cote=m.group(1)
    m=re.search(r'\\scanpage\{([^}]+)\}',line)
    if m:
        if pages:pages[-1]['end_line']=i-1
        pages.append(dict(cote=cote,scan=int(m.group(1)),start_line=i))
pages[-1]['end_line']=len(tex)
(root/'agents/p15/page_map.json').write_text(json.dumps(pages,indent=2))
print('entries',len(entries),'pages',len(pages))
for e in entries: print(e['entry_id'].split('#')[1],e['source_line'],e['heading'])
print(json.dumps(pages))
