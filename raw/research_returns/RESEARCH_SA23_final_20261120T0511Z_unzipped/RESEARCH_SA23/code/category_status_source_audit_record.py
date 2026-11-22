"""Record the bounded source-use audit without inflating it into new proofs."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import io
import json

ROOT = Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
note = ROOT / 'notes/category_final_status_source_audit.md'
bib = ROOT / 'RESEARCH_SA23_references.bib'
events = ROOT / 'notes/category_CHECK_EVENTS.tsv'
who = 'GPT-6 Astra, inherited effort, crystalline_categories'
rows = [
    ('SA23-B1-1', 'Reopened NSW arXiv:1205.2119v3 Definitions 2.1,2.3,2.5 and Fact 2.6(a); verified that the exact minimal Cohen factorization existence used in B.1 is stated without the separability assumption of the distinct comparison Fact 2.6(c). Checked written degree0/1 derivation and explicit AFH-original-unopened qualification. Source-use audit, not a re-proof of AFH. notes/category_final_status_source_audit.md'),
    ('geo-Ke-unpolarized', 'Read exact retained Robert Theorem 2.3.2 p12 and current fppf-descent derivation. It supplies the abelian-algebraic-space-to-scheme step; the paper expressly discloses Faltings-Chai I.1.9 original page unopened. No dependence solely on the unopened original found. Source-use audit only. notes/category_final_status_source_audit.md'),
    ('cat:I6', 'Compared current relative-classifier derivation with opened-source record: Makkai-Reyes9.1.1,9.1.4-9.1.5 are exact operative inputs. No unopened Makkai-Pare or unread SGA4 theorem is used as a replacement. Dependency audit, not another independent proof. notes/category_final_status_source_audit.md'),
    ('cat:J5', 'Final dependency audit matched operative Fontaine §§3.6-3.7,3.10,5.2,6.2 and perfect-residue-field scope to current theorem and opened-source record. No unopened-only source dependency. notes/category_final_status_source_audit.md'),
    ('cat:J7', 'Final dependency audit matched Fontaine1.6(iii), crystalline comparison, CF4.1 and Kisin0.3/2.2.6 opened locators with rational BT-category uniqueness use; exact field/isogeny restrictions retained. No new proof check claimed. notes/category_final_status_source_audit.md'),
    ('cat:J8', 'Final source-use audit confirmed Ax1970 main theorem p417/proof§3 is the operative opened fixed-field source; unused Tate1967 remains explicitly unopened. No theorem supported solely by failed retrieval. notes/category_final_status_source_audit.md'),
    ('cat:J9', 'Final source-use audit matched direct ICM1970§5pp434-435 and CF Introductionp3/ref23 reading record to historical comparison; no transfer to false literal all-HT extension. notes/category_final_status_source_audit.md'),
    ('cat:L5', 'Final dependency audit matched BD1.4.14(ii)/1.4.15pp41-45 and written L3-L4 hypothesis derivation; unused IllusieVIII remains unopened. Pro-algebra/ordinary-sheaf-limit distinction preserved. No new independent proof check claimed. notes/category_final_status_source_audit.md'),
]
existing = events.read_text(encoding='utf-8')
buffer = io.StringIO()
writer = csv.writer(buffer, delimiter='\t', lineterminator='\n')
added = 0
for statement, outcome in rows:
    if outcome in existing:
        continue
    writer.writerow([statement, '2026-11-20', who, 'used and rechecked in this run', outcome])
    added += 1
with events.open('a', encoding='utf-8') as handle:
    handle.write(buffer.getvalue())
record = {'utc': datetime.now(timezone.utc).isoformat(),
          'bib_sha256': hashlib.sha256(bib.read_bytes()).hexdigest(),
          'note_sha256': hashlib.sha256(note.read_bytes()).hexdigest(),
          'events_added': added,
          'result': 'No unopened-only operative theorem dependency found in scoped audit',
          'core_files_edited': False}
(ROOT / 'notes/category_final_status_source_audit_record.json').write_text(
    json.dumps(record, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(record, ensure_ascii=False, indent=2))
