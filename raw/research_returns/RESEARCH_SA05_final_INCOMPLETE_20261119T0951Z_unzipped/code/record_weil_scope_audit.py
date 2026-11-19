"""Record the actually completed arbitrary-Weil-field criterion audit."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import time

ROOT = Path(__file__).resolve().parents[1]
started = time.monotonic()
now = datetime.now(timezone.utc).replace(microsecond=0)
specs = [
    ('c:finite-weil-criterion', 'Root read the complete arbitrary-Weil-field corollary. The rational kernel of the orbit pullback is a stable noetherian ideal because it is the kernel of a Q-comodule map. It captures precisely rational diagram relations. The finite criterion requires C+ and no rational form of cohomology; effectiveness additionally requires a finite presentation of Q[structure constants]. The separate K-linear convention is explicitly distinguished.'),
    ('c:finite-field-sign', 'Root read the complete finite-field sign proof. Rational Frobenius characteristic polynomials in distinct absolute weights are coprime, and Chinese remaindering gives algebraic degree projectors without assuming semisimplicity. Katz–Messing hypotheses are retained for abstract Weil theories; ell-adic and characteristic-zero crystalline cohomology are included. The base descent of X and o is finite.')
]
path = ROOT / 'ROOT_CHECK_EVENTS.tsv'
with path.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
added = 0
for identifier, outcome in specs:
    if not any(row['statement_id'] == identifier and row['outcome'] == outcome for row in rows):
        rows.append(dict(statement_id=identifier, date=now.isoformat().replace('+00:00','Z'),
                         who='GPT-6 Astra / root / current run', type='targeted proof check', outcome=outcome))
        added += 1
with path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t')
    writer.writeheader()
    writer.writerows(rows)

marker = '### Arbitrary Weil coefficient scope checked'
ledger = ROOT / 'PROGRESS_LEDGER.md'
if marker not in ledger.read_text():
    ledger.write_text(ledger.read_text() + f'\n{marker}\n\nChecked at {now:%H:%M:%S} UTC. The C.1 finite criterion now holds for rational relations over any algebraically closed base and any characteristic-zero Weil coefficient field, assuming C+ for that realization. The rational orbit-kernel construction removes the former rational-Betti restriction. Finite existence is proved; effectiveness requires the stated finite coefficient-algebra presentation. Over Fbar_p the sign hypothesis is supplied by algebraic Frobenius projectors for the specified cohomology theories. This removes the coefficient-field scope obstruction but does not remove C+ in general or prove the finite Chow vanishings.\n')
report = ROOT / 'RESEARCH_SA05_report.md'
if marker not in report.read_text():
    report.write_text(report.read_text() + f'\n{marker}\n\nThe finite criterion extends to rational relations for any characteristic-zero Weil coefficient field by taking the rational kernel of the super-orbit pullback. This requires no rational form of the cup algebra. A finite presentation of its coefficient algebra suffices for effective elimination; an opaque coefficient field gives finite existence only. The criterion remains conditional on algebraic parity C+, except in the stated finite-field cases where the Katz–Messing Frobenius-projector argument supplies it. Relations after extending Chow coefficients to the Weil field are explicitly treated as a separate convention.\n')
result = {'new_events': added, 'root_events': len(rows), 'checked_at': now.isoformat(),
          'seconds': round(time.monotonic()-started, 6)}
(ROOT / 'code/record_weil_scope_audit_output.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
