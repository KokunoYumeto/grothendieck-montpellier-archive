from pathlib import Path
import shutil
own = Path(__file__).resolve().parents[1]
hist = own/"notes/B100_promotion_audit_key_failure"
hist.mkdir(exist_ok=False)
p = own/"code/promote_B100.py"
shutil.copy2(p, hist/"promote_B100.executed.py")
(hist/"stderr.txt").write_text("KeyError: 'all_mathematical_output_identical'\nThe companion record uses mathematical_fields_equal. Failure occurred before any canonical/prior/record mutation.\n")
old = p.read_text()
assert old.count('run["all_mathematical_output_identical"]') == 1
new = old.replace('run["all_mathematical_output_identical"]', 'run["mathematical_fields_equal"]')
new = new.replace('"retained_failures":"No mathematical checker failure; root and companion original-source access failures retained in their full audit records."',
                  '"retained_failures":"No mathematical checker failure. One promotion-controller audit-key mismatch aborted before writing; exact failed program/stderr retained. Root/companion original-source access failures retained in their audits."')
p.write_text(new)
