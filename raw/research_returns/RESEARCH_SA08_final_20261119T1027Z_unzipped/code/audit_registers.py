"""Verify that numbered paper statements and the result register correspond."""
from pathlib import Path
import csv,re,json,collections
root=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((root/'RESEARCH_SA08_results.csv').open(newline='')))
canonical=lambda x:re.sub(r'[^A-Za-z0-9]','',x).upper()
ids=[canonical(row['id']) for row in rows]
duplicates=[key for key,n in collections.Counter(ids).items() if n>1]
paper=(root/'RESEARCH_SA08_paper.tex').read_text()
files=[]
for match in re.finditer(r'\\(?:input|InputIfFileExists)\{(sections/[^}]+)\}',paper):
    path=root/match.group(1)
    if not path.suffix:path=path.with_suffix('.tex')
    if path.exists():files.append(path)
labels=[]
for path in files:
    text=path.read_text()
    for match in re.finditer(r'\\label\{sa08:([^}]+)\}',text):
        ident=canonical(match.group(1))
        if re.fullmatch(r'[ABCD]\d+[A-Z]*',ident):
            labels.append((ident,str(path.relative_to(root))))
    for match in re.finditer(r'\\paragraph\{([ABCD]-\d+[A-Z]*)[.:]',text):
        ident=canonical(match.group(1))
        labels.append((ident,str(path.relative_to(root))))
label_ids=[ident for ident,path in labels]
result={'result_rows':len(rows),'numbered_statement_labels':len(labels),
        'duplicate_result_ids':duplicates,
        'duplicate_labels':[key for key,n in collections.Counter(label_ids).items() if n>1],
        'paper_labels_without_rows':[(ident,path) for ident,path in labels if ident not in ids],
        'result_rows_without_paper_labels':[row['id'] for row in rows if canonical(row['id']) not in label_ids]}
(root/'logs/register_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
