"""Navigate structured A source locators; flag empty exact lines for manual review.

This does not judge mathematical statements or change any locator automatically.
"""
from pathlib import Path
import csv,json,re

WORK=Path(__file__).resolve().parents[1]
OUT=WORK/'parts/a'
SOURCE=WORK.parent/'source/SA04_texts'
P='pro/MPL_93_047-091_transcription.tex'
LOC=r'\d+(?:[–-]\d+)?(?:;\d+(?:[–-]\d+)?)*'
full=re.compile(r'((?:pro|codex)/[\w+.-]+\.tex)(?::|,\s*scans?[^;]*?,\s*lines?)('+LOC+r')')
short=re.compile(r'(?:Codex\s+(K\d+-\d+)|\b(Pro)):('+LOC+r')')
records=[]

def inspect(text,label):
    for match in full.finditer(text):
        records.append((label,match.group(1),match.group(2)))
    for match in short.finditer(text):
        file='codex/'+match.group(1)+'_transcription.tex' if match.group(1) else P
        records.append((label,file,match.group(3)))

def walk(value,label):
    if isinstance(value,str):inspect(value,label)
    elif isinstance(value,list):
        for n,part in enumerate(value):walk(part,label+f'[{n}]')
    elif isinstance(value,dict):
        label=value.get('id',label)
        for key,part in value.items():walk(part,label+'.'+key)

for name in ['items.json','claims.json','problems.json']:
    walk(json.loads((OUT/name).read_text()),name)
for name in ['readings.tsv','links.tsv','c100_witness_readings.tsv']:
    for n,row in enumerate(csv.DictReader((OUT/name).open(),delimiter='\t'),1):
        walk(row,f'{name}:row{n}')

exact=[];ranges=[];issues=[];cache={}
for label,file,loc in records:
    if file not in cache:cache[file]=(SOURCE/file).read_text().splitlines()
    lines=cache[file]
    for segment in loc.split(';'):
        numbers=re.split('[–-]',segment)
        start=int(numbers[0]);end=int(numbers[-1])
        if not 1<=start<=end<=len(lines):
            issues.append(dict(label=label,file=file,segment=segment,issue='out of bounds'));continue
        excerpt=lines[start-1:end]
        record=dict(label=label,file=file,line=start,text=excerpt[0])
        if start==end:
            exact.append(record)
            if not excerpt[0].strip():issues.append(dict(**record,issue='exact line is blank'))
        else:
            ranges.append(dict(label=label,file=file,start=start,end=end))
            if not any(s.strip() for s in excerpt):
                issues.append(dict(label=label,file=file,segment=segment,issue='entire range is blank'))

result=dict(scope='items, claims, problems, readings, links, supplementary cote100 readings; explicit source paths and Pro/Codex shorthand',exact_locator_occurrences=len(exact),unique_exact_lines=len({(r['file'],r['line']) for r in exact}),range_locator_occurrences=len(ranges),issues=issues,exact_lines=exact,limitation='Navigation check only; a nonblank line is not certification that its mathematical statement matches the record.')
(OUT/'locator_audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='exact_lines'},ensure_ascii=False,indent=2))
