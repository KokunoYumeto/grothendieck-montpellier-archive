"""Check the brief's explicit status labels against active numbered statements."""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, re, time

R = Path(__file__).resolve().parents[1]
start = time.perf_counter()
target = R/'code/root_statement_status_audit_output.json'
assert not target.exists()
active = []
seen = set()
def visit(path):
    path = path.resolve()
    if path in seen:
        return
    seen.add(path)
    source = path.read_text()
    active.append((path,source))
    for name in re.findall(r'\\input\{([^}]+)\}',source):
        child = R/name
        if not child.suffix:
            child = child.with_suffix('.tex')
        visit(child)
visit(R/'RESEARCH_SA22_paper.tex')
envs = 'theorem|proposition|lemma|corollary|claim|definition|example|counterexample|remark|question'
headers = []
for path,source in active:
    for m in re.finditer(r'\\begin\{('+envs+r')\}\s*(?:\[([\s\S]*?)\])?',source):
        body = source[m.end():].split('\\end{'+m[1]+'}',1)[0]
        label = re.search(r'\\label\{([^}]+)\}',body)
        headers.append({'file':str(path.relative_to(R)), 'line':source[:m.start()].count('\n')+1,
                        'environment':m[1], 'heading':' '.join((m[2] or '').split()),
                        'id':label[1] if label else None})
rows = list(csv.DictReader((R/'RESEARCH_SA22_results.csv').open()))
issues = [x for x in headers if not re.search(r'\b(?:Proved|Refuted|Known)\b',x['heading'])]
bad_csv = [dict(id=x['id'],status=x['status']) for x in rows
           if not re.match(r'^(?:Proved|Refuted|Known)\b',x['status'])]
out = {'recorded_utc':datetime.now(timezone.utc).isoformat(),
       'scope':'Formatting and record semantics only: every active numbered environment has an explicit proof/refutation/known status; no proof or mathematical certificate is rerun.',
       'active_tex_files':len(active),'numbered_headers':len(headers),'csv_rows':len(rows),
       'missing_explicit_header_status':issues,'unexpected_csv_status':bad_csv,
       'headers':headers,'seconds':time.perf_counter()-start}
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='headers'},indent=2))
