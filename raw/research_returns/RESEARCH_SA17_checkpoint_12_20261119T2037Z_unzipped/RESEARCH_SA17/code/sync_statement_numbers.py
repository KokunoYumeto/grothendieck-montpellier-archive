"""Index numbered statements and add compiled numbers to the report table.

This is editorial consistency checking, not mathematical verification.
Run only after a successful build of the current sources.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import re
import time

started = time.perf_counter()
root = Path(__file__).resolve().parents[1]
aux = (root / 'RESEARCH_SA17_paper.aux').read_text()
numbers = dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}', aux))
seen = set()
statements = []

def visit(path):
    if not path.suffix:
        path = path.with_suffix('.tex')
    if path in seen:
        return
    seen.add(path)
    source = path.read_text()
    for match in re.finditer(
        r'\\begin\{(theorem|proposition|lemma|corollary|claim|remark|definition|example|counterexample)\}'
        r'(.*?)\\end\{\1\}', source, re.S
    ):
        labels = re.findall(r'\\label\{([^}]+)\}', match.group(2))
        labels = [label for label in labels if label in numbers]
        statements.append({
            'environment': match.group(1),
            'labels': labels,
            'number': numbers.get(labels[0]) if labels else None,
            'file': str(path.relative_to(root)),
            'line': source.count('\n', 0, match.start()) + 1,
        })
    for include in re.findall(r'\\input\{([^}]+)\}', source):
        visit(root / include)

visit(root / 'RESEARCH_SA17_paper.tex')
with (root / 'RESEARCH_SA17_results.csv').open(newline='') as stream:
    rows = list(csv.DictReader(stream))
row_ids = [row['id'] for row in rows]
issues = []
for statement in statements:
    hits = [key for key in statement['labels'] if key in row_ids]
    if len(hits) != 1:
        issues.append(dict(statement, result_ids=hits))
numbered_labels = {key for statement in statements for key in statement['labels']}
extras = [key for key in row_ids if key not in numbered_labels]

report = root / 'RESEARCH_SA17_report.md'
lines = report.read_text().splitlines()
for index, line in enumerate(lines):
    if line == '# Research report':
        break
    if not line.startswith('| '):
        continue
    cells = line.split('|')
    if len(cells) < 6 or cells[1].strip() == 'Item':
        continue
    labels = cells[3].strip()
    labels = re.sub(r' \(§?\d+(?:\.\d+)*\)', '', labels)
    cells[3] = ' ' + re.sub(
        r'(?<![\w:])([A-DL][A-Za-z0-9]*:[A-Za-z0-9_-]+)',
        lambda match: (match[0] + ' (' + numbers[match[0]] + ')')
        if match[0] in numbers else match[0], labels
    ) + ' '
    lines[index] = '|'.join(cells)
report.write_text('\n'.join(lines) + '\n')
result = {
    'timestamp': datetime.now(timezone.utc).isoformat(),
    'compiled_files': len(seen),
    'numbered_statements': len(statements),
    'result_rows': len(rows),
    'missing_or_ambiguous_numbered_rows': issues,
    'result_ids_without_a_numbered_statement': extras,
    'statements': statements,
    'seconds': time.perf_counter() - started,
}
(root / 'logs/finish_statement_inventory.json').write_text(
    json.dumps(result, indent=2) + '\n'
)
print(json.dumps({key: value for key, value in result.items() if key != 'statements'}))
