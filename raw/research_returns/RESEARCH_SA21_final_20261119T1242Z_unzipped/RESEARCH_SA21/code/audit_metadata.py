"""Check final statement/event/source registers and add printed locators.

This is an operational consistency audit, not a mathematical proof checker.
Run after merge_metadata.py and the final LuaLaTeX pass.
"""
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

root = Path(__file__).resolve().parents[1]
seen_files = set()
statements = {}
envs = r'theorem|proposition|lemma|corollary|counterexample|definition|remark'

def visit(path):
    path = path.resolve()
    if path in seen_files:
        return
    seen_files.add(path)
    source = path.read_text()
    for match in re.finditer(r'\\begin\{(' + envs + r')\}(.*?)\\end\{\1\}', source, re.S):
        labels = re.findall(r'\\label\{(SA21-[^}]+)\}', match.group(2))
        assert len(labels) == 1, (str(path), match.group(1), labels)
        label = labels[0]
        assert label not in statements, label
        statements[label] = {'environment': match.group(1), 'file': str(path.relative_to(root))}
    for name in re.findall(r'\\input\{([^}]+)\}', source):
        visit(root / (name if name.endswith('.tex') else name + '.tex'))

visit(root / 'RESEARCH_SA21_paper.tex')
with (root / 'RESEARCH_SA21_results.csv').open(newline='') as file:
    reader = csv.DictReader(file)
    fields = reader.fieldnames
    rows = list(reader)
counts = Counter(row['id'] for row in rows)
assert all(count == 1 for count in counts.values()), counts
assert set(counts) == set(statements), {'missing_rows': sorted(set(statements)-set(counts)), 'extra_rows': sorted(set(counts)-set(statements))}

aux = (root / 'logs/RESEARCH_SA21_paper.aux').read_text()
locators = {m[0]: (m[1],m[2]) for m in re.findall(r'\\newlabel\{(SA21-[^}]+)\}\{\{([^}]+)\}\{([^}]+)\}', aux)}
assert set(statements) <= set(locators), sorted(set(statements)-set(locators))
status_map = {'proved': 'Proved', 'refuted': 'Refuted', 'known': 'Known', 'definition verified': 'Known', 'proved under stated hypotheses': 'Proved under stated hypotheses'}
for row in rows:
    row['status'] = status_map[row['status'].lower()]
    number, page = locators[row['id']]
    row['where_proved'] = f"{statements[row['id']]['file']}; {statements[row['id']]['environment'].capitalize()} {number}; PDF p. {page}; label {row['id']}"
with (root / 'RESEARCH_SA21_results.csv').open('w',newline='') as file:
    writer = csv.DictWriter(file,fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

with (root / 'CHECK_EVENTS.tsv').open(newline='') as file:
    events = list(csv.DictReader(file,delimiter='\t'))
covered = {event['statement_id'] for event in events}
assert set(statements) <= covered, sorted(set(statements)-covered)
assert all(event['date'] and event['who'] and event['type'] and event['outcome'] for event in events)
effort_missing = sorted({event['who'] for event in events if 'effort' not in event['who'].lower()})
assert not effort_missing, effort_missing

bib = (root/'RESEARCH_SA21_references.bib').read_text()
entries = re.split(r'(?m)^@',bib)[1:]
keys = []
for entry in entries:
    key = entry.split('{',1)[1].split(',',1)[0]
    keys.append(key)
    assert re.search(r'opened',entry,re.I), (key,'missing source-access marker')
assert len(keys) == len(set(keys))
all_tex = '\n'.join(p.read_text() for p in seen_files)
cited = set()
for group in re.findall(r'\\cite\w*(?:\[[^\]]*\])*\{([^}]+)\}',all_tex):
    cited.update(x.strip() for x in group.split(','))
assert cited <= set(keys), sorted(cited-set(keys))

locator_checks = {'status': 'not run: supplied attachment tree unavailable'}
attachment_root = root.parent/'SA21_input'
correction_file = root/'RESEARCH_SA21_corrections.tsv'
if attachment_root.exists() and correction_file.exists():
    with correction_file.open(newline='') as file:
        correction_rows = list(csv.DictReader(file,delimiter='\t'))
    locator_errors = []
    for row in correction_rows:
        name = row['file']
        if name.startswith('upload/'):
            path = root.parent/name
        elif name.startswith('PROMPT'):
            path = root.parent/'upload'/name
        else:
            path = attachment_root/name
        if not path.is_file():
            locator_errors.append([row['id'],'source path absent',name])
            continue
        line_count = len(path.read_text().splitlines())
        first = re.search(r'\d+',row['line_or_locator'].split(';',1)[0])
        if first and int(first.group())>line_count:
            locator_errors.append([row['id'],'leading line out of range',row['line_or_locator'],line_count])
    locator_checks = {'status':'checked source paths and leading line bounds; semantic source checks are separate', 'records':len(correction_rows),'errors':locator_errors}
    assert not locator_errors, locator_errors

log = (root/'logs/RESEARCH_SA21_paper.log').read_text()
overflows = [float(x) for x in re.findall(r'Overfull \\[hv]box \(([\d.]+)pt too (?:wide|high)\)',log)]
forbidden = ['There were undefined references', 'There were undefined citations', 'Missing character:', 'Fatal error occurred', 'LaTeX Error:', 'Package natbib Warning: Citation']
errors = [x for x in forbidden if x in log]
summary = {
    'scope': 'Operational consistency only; proofs are checked separately in CHECK_EVENTS.tsv.',
    'numbered_statements': len(statements),
    'result_rows': len(rows),
    'check_events': len(events),
    'distinct_checked_ids_including_prior_claims': len(covered),
    'bib_entries_with_access_markers': len(keys),
    'citation_keys_used': len(cited),
    'included_tex_files': sorted(str(p.relative_to(root)) for p in seen_files),
    'all_statement_ids_have_events': True,
    'all_who_fields_disclose_effort': True,
    'source_locator_checks': locator_checks,
    'overfull_boxes': overflows,
    'overfull_boxes_above_2pt': sum(x>2 for x in overflows),
    'build_errors_or_undefined_references': errors,
    'rerun_requested': 'Rerun to get' in log or 'Label(s) may have changed' in log,
    'pdf_sha256': hashlib.sha256((root/'logs/RESEARCH_SA21_paper.pdf').read_bytes()).hexdigest(),
    'printed_locators': {key: {'number': value[0], 'page':value[1]} for key,value in sorted(locators.items()) if key in statements},
}
dest = root/'code/outputs/final_metadata_audit.json'
dest.write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='printed_locators'},indent=2))
assert not errors and not summary['rerun_requested'] and not summary['overfull_boxes_above_2pt'], 'Final typesetting pass is not yet clean.'
