# Operations run at session start; preserved for reproducibility.
from pathlib import Path
import zipfile,csv,collections
r=Path('/workspace/scratch/95cd10054c54')
print((r/'upload/PROMPT(20261119-130101).md').read_text())
with zipfile.ZipFile(r/'upload/SA02_Gomtrie_et_topologie_combinatoire_part2.zip') as z:
 for i in z.infolist(): print(i.filename,i.file_size)
 # Extraction was executed once at session start into r/'source'.
print((r/'source/SA02_texts/TOPIC.md').read_text())
print((r/'source/SA02_texts/PREAMBLE.tex').read_text())
with (r/'source/SA02_notes/NOTES_INDEX.tsv').open() as f: rows=list(csv.DictReader(f,delimiter='\t'))
print('Entries',len(rows)); print(collections.Counter(x['package'] for x in rows))
