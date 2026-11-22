from pathlib import Path
from datetime import datetime, timezone
import csv, json

base = Path(__file__).resolve().parents[2]
root = base / 'work/root'
now = datetime.now(timezone.utc).isoformat()
rows = json.loads((root / 'rows.json').read_text())
assert not any(r['id'] == 'MT-M37' for r in rows)
with (root / 'section.tex').open('a') as f:
    f.write('\n' + (root / 'compatible_indentation_obstruction.tex').read_text())
rows.append(dict(
    id='MT-M37',
    statement='A single nonnegative indentation normalized both globally and on an initial subgroup G0 with G=HG0 vanishes outside G0. Its averaged product kills every external prime shell pointwise. Without local normalization, external orbital mass is exactly 1-sum_c A_c^2 and lies between 2delta(1-delta) and 2delta-delta^2; quantitative integral bounds identify sufficient vanishing conditions for varying-level repairs.',
    input='neither; elementary countable nonnegative sums and dominated convergence, applied to the actual rational idele filtration and the original indentation definition',
    status='proved here: the compatible-indentation replacement cannot supply the nonzero external-shell trace. The original zero-tail proposition is not refuted. An alternative varying-level family still requires explicit orbital weights and justified kernel/trace limits.',
    where_the_proof_is='GRH_NIGHT.tex MT-M37; work/root/compatible_indentation_obstruction.tex; original Masullo12.2.2.4 pp512-513, normalization12.2.1.2p505, lift12.2.2.2p508, dependency map11.3.2.1pp495-496',
    where_it_lives='Q-MAS-GEOMETRIC-NARROW; Q-MAS-INDENTATION; Q-MAS-COMPATIBLE-INDENTATION; cote1scans79-80/111-112 geometric trace route: a normalized lift must also preserve the required local orbital allocation'
))
(root / 'rows.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')

def event(path, sid, kind, outcome):
    with path.open('a', newline='') as f:
        csv.writer(f, delimiter='\t').writerow([
            sid, now, '/root', 'GPT-6 Astra Pro', 'not exposed',
            'GRH_NIGHT_20261121', kind, outcome])

event(root / 'events.tsv', 'MT-M37', 'targeted proof check',
      'Read the whole proof, including exact support, well-defined product, coset defect identity, both sharp inequalities, all fixed/varying diagonal convergence alternatives, actual rational idele filtration and the b_t example. Directly read original pp512-513 images in full and compared pp495/505/508 already inspected under MT-M36. No gap found. Verified the distinction between 11.3.2.1 citing12.2.2.2 and the proposed later12.2.2.4 replacement; the source zero-tail conclusion is not refuted.')
event(base / 'work/checks/source_events.tsv', 'Masullo12.2.2.4',
      'used and rechecked in this run',
      'Fresh direct visual reading of original pp512-513 confirms D subset G0, simultaneous alpha_k b indentation normalization, and the explicit extension by zero. MT-M37 derives a pointwise support consequence and tests its use as a replacement lift; no refutation of the original zero-tail proposition or of conditional M_H is claimed.')

path = root / 'questions.tsv'
with path.open(newline='') as f:
    rd = csv.DictReader(f, delimiter='\t')
    fields, qs = rd.fieldnames, list(rd)
for q in qs:
    if q['id'] in ('Q-MAS-GEOMETRIC-NARROW', 'Q-MAS-INDENTATION'):
        q['state'] += ' MT-M37 closes the single-compatible-indentation repair: global plus initial-local normalization forces support in G0 and kills every external prime shell. A varying-level replacement must specify its orbital weights and justify the trace limit; exact defect inequalities are now available.'
qs.append(dict(
    id='Q-MAS-COMPATIBLE-INDENTATION',
    source_and_locator='Masullo12.2.2.4 original pp512-513;11.3.2.1 original pp495-496; MT-M36',
    question='Can a single nonnegative indentation compatible with the full local subgroup filtration repair the external-shell trace normalization?',
    state='refuted as a repair by MT-M37: both normalizations force support in the initial subgroup, so external shell integrands vanish pointwise. The original zero-tail proposition remains unrefuted. Exact defect identity and integral inequalities give tests for the remaining varying-level alternative.'
))
with path.open('w', newline='') as f:
    wr = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
    wr.writeheader()
    wr.writerows(qs)
with (root / 'implications.md').open('a') as f:
    f.write('\n## Compatible normalization kills the external shells\n\nMT-M37 proves that the nonnegative indentation supplied by the simultaneous normalizations in original12.2.2.4 must vanish off G0. For the actual rational idele filtration every external-prime shell then vanishes before any trace limit. Thus this construction cannot replace the literal zero section-average in11.3.2.2 while retaining its asserted nonzero local orbital values. The original zero-tail conclusion is not refuted. A varying-level lift remains a distinct route; its exact external mass is1-sum A_c^2, with explicit defect and L1 bounds that any claimed limiting repair can be checked against. The cote1scans79-80/111-112 comparison gate now excludes the single-compatible-lift route.\n')
with (root / 'ledger_history.md').open('a') as f:
    f.write(f'\n### {now} — compatible-indentation repair closed\n\nMT-M37 passed an entire root proof reading after author and number-theory peer readings. Original512-513 were directly inspected. The exact support and defect theorems close one proposed repair, while preserving the original zero-tail proposition and conditional Hecke-GRH endpoint.\n')
print(json.dumps(dict(date=now, root_rows=len(rows), added=['MT-M37'])))
