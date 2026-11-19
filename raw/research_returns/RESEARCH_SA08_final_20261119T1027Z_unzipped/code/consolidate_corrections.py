"""Merge independently verified input corrections without changing the inputs."""
from pathlib import Path
import csv, json
root=Path(__file__).resolve().parents[1]
rows=[]
for path in sorted((root/'notes').glob('*_CORRECTIONS.tsv')):
    for n,row in enumerate(csv.DictReader(path.open(newline=''),delimiter='\t'),1):
        if 'attached_file_line_locators' in row:
            record={'id':row['id'],'input_locator':row['attached_file_line_locators'],
                    'original_claim':row['original_claim'],'correction':row['correction'],
                    'proof':row['proof_file_line_locators'],'source_register':str(path.relative_to(root))}
        else:
            record={'id':row.get('id',f'{path.stem.split("_")[0]}-C{n:02d}'),
                    'input_locator':row['file']+':'+row['line'],
                    'original_claim':row['old_claim'],'correction':row['correction'],
                    'proof':row['statement'],'source_register':str(path.relative_to(root))}
        rows.append(record)
fields=['id','input_locator','original_claim','correction','proof','source_register']
with (root/'RESEARCH_SA08_corrections.tsv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fields,delimiter='\t');writer.writeheader();writer.writerows(rows)
table=['| Input file and line | Claim corrected | Proved correction | Statement / proof |',
       '|---|---|---|---|']
def safe(text):return text.replace('|','\\|').replace('\n',' ')
for row in rows:
    table.append('| '+' | '.join(safe(row[key]) for key in
                ['input_locator','original_claim','correction','proof'])+' |')
(root/'notes/CORRECTIONS_table.md').write_text('\n'.join(table)+'\n')
print(json.dumps({'correction_rows':len(rows),'source_registers':sorted(set(x['source_register'] for x in rows))},indent=2))
