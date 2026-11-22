"""Clarify the polarity of Refuted records without changing mathematical claims."""
from datetime import datetime, timezone
from pathlib import Path
import csv, hashlib, json, time

ROOT = Path(__file__).resolve().parents[1]
started = time.perf_counter()
started_utc = datetime.now(timezone.utc).isoformat()
output_path = ROOT / 'code/root_refuted_record_wording_output.json'
assert not output_path.exists(), 'This recorded edit is applied once.'
assembler = ROOT / 'code/assemble_records.py'
owned = ROOT / 'checks/part_a567_results.csv'
before = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in [assembler, owned]}
paper = ROOT / 'RESEARCH_SA22_paper.pdf'
paper_sha = hashlib.sha256(paper.read_bytes()).hexdigest()
old = "    if original_status!=row['status']:row['notes']+=' Contributor status detail: '+original_status+'.'\n    normalized[lab]=row\n"
new = "    if original_status!=row['status']:row['notes']+=' Contributor status detail: '+original_status+'.'\n    if row['status']=='Refuted':\n        caption=' '.join(title.split())\n        row['statement']='Proved refutation and corrected scope (active caption: '+caption+'): '+row['statement']\n        row['notes']+=' Refuted classifies the original manuscript claim addressed here; the statement field records its proved refutation and any corrected scope.'\n    normalized[lab]=row\n"
text = assembler.read_text()
assert text.count(old) == 1
assembler.write_text(text.replace(old, new))
with owned.open(newline='') as handle:
    reader = csv.DictReader(handle)
    fields = reader.fieldnames
    rows = list(reader)
target = [r for r in rows if r['id'] == 'A1-toric-nondescent']
assert len(target) == 1 and target[0]['status'] == 'Refuted'
old_statement = target[0]['statement']
assert old_statement == 'Raw canonical toric surgery is not invariant under replacing an actual cut by an isotopic toric cut in the same labelled four-punctured surface'
target[0]['statement'] = 'Raw canonical toric surgery is invariant under replacing an actual cut by an isotopic toric cut in the same labelled four-punctured surface'
target[0]['notes'] += ' The statement field now gives the positive original invariance claim to which Refuted applies; its proved counterexample is in the numbered theorem.'
with owned.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
assert hashlib.sha256(paper.read_bytes()).hexdigest() == paper_sha
after = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in [assembler, owned]}
note = '''# Clarification of Refuted-record polarity

The final handoff check found that the contributor row for `A1-toric-nondescent` paired the proved negative fact with the status **Refuted**, although the active theorem caption refutes the positive invariance claim. The aggregate assembler also intentionally reproduces each theorem body, so changing a contributor summary alone would not clarify the aggregate record.

Two record-only changes address that ambiguity. The contributor summary now states the positive invariance claim. For every aggregate row whose status is Refuted, the assembler prefixes the unchanged theorem body with “Proved refutation and corrected scope”, identifies its actual active caption, and adds a standard explanatory note: Refuted classifies the original manuscript claim; the statement field records its proved refutation and any corrected scope.

This uniform schema explanation does not reinterpret descriptive counterexample captions, change a mathematical status, rewrite a theorem or proof, or promote any source requirement. The unchanged PDF hash is recorded in the edit output. The next ordinary record refresh applies the aggregate wording; no PDF rebuild is needed. This is not substantive movement under the hourly-review rule.
'''
(ROOT / 'notes/root_refuted_record_wording.md').write_text(note)
record = dict(started_utc=started_utc, seconds=time.perf_counter()-started, before=before, after=after,
              changed_contributor_row='A1-toric-nondescent', changed_contributor_fields=['statement','notes'],
              aggregate_rule='Every Refuted row receives its actual caption, unchanged theorem body and explicit polarity note on the next assembly.',
              mathematical_status_changes=0, tex_changes=0, pdf_sha256_unchanged=paper_sha,
              scope='One-time CSV/schema wording correction; no mathematical proof or finite-certificate rerun.')
output_path.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
