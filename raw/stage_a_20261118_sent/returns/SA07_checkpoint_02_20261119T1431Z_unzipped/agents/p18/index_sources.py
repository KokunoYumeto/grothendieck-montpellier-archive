from pathlib import Path
import csv,json,re
root=Path(__file__).resolve().parents[2]
rows=[r for r in csv.DictReader((root/'work/SA07_notes/NOTES_INDEX.tsv').open(),delimiter='\t') if r['package']=='MPL_18_018-062']
text=(root/'work/SA07_notes/pro/MPL_18_018-062_notes.md').read_text()
heads=list(re.finditer(r'^### (.+)$',text,re.M))
entries=[]
for i,(row,h) in enumerate(zip(rows,heads)):
 body=text[h.start():heads[i+1].start() if i+1<len(heads) else len(text)]
 entries.append({**row,'note_line':text[:h.start()].count('\n')+1,'body':body})
assert len(rows)==len(heads)==129
out=Path(__file__).parent
(out/'source_entries.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2))
summary='\n'.join(f"{i+1:03} L{e['note_line']:03} {e['heading']}" for i,e in enumerate(entries))+'\n'
(out/'evidence/source_index.txt').write_text(summary)
print(summary)
