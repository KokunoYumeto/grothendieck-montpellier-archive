#!/usr/bin/env python3
"""Promote the fully approved C.3br proof and append its canonical owner records."""
from pathlib import Path
from datetime import datetime, timezone
from time import perf_counter
import csv, hashlib, io, json

started = perf_counter()
base = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
draft = base / 'C3_triple_free_component_lifting_draft.tex'
final = base / 'C3_triple_free_component_lifting.tex'
original = draft.read_text()
if not original.startswith('% Reserved C.3br.'):
    raise SystemExit('Expected the complete approved draft; refusing to overwrite from a pointer.')
archive = base / 'output' / 'C3_triple_free_component_lifting_audited_draft.tex'
archive.write_text(original)
promoted = original.replace('% Reserved C.3br. Complete draft; unregistered pending independent audits.',
                            '% C.3br. Complete root and two independent peer proof/source audits passed.', 1)
promoted = promoted.replace('(complete draft).}', '(Proved).}', 1)
final.write_text(promoted)
draft.write_text('% Superseded after complete root and two-peer audits.\n'
                 '% Final proof: agents/real_weil/C3_triple_free_component_lifting.tex\n'
                 '% Complete audited pre-promotion text retained in output/C3_triple_free_component_lifting_audited_draft.tex.\n')

results = base / 'results.csv'
with results.open(newline='') as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)
if any(row['id'] == 'C.3br' for row in rows):
    raise SystemExit('C.3br already registered; no duplicate record written.')
row = dict.fromkeys(fields, '')
row.update({
    'id': 'C.3br',
    'statement': 'For a triple-free projective SNC surface over an algebraically closed characteristic-p field with surjective joint rational component-to-edge Picard restriction, its top gamma K0 is the direct sum of component CH0 and its actual proper-perfect-family quotient is exactly the component degrees; every resolved C3bm threefold with negative exceptional divisor and rational double curves has B2_Q=0',
    'status': 'Proved under the stated triple-free and Picard-restriction hypotheses; rational double curves imply the criterion in the negative exceptional setting',
    'where_proved': 'C3_triple_free_component_lifting.tex: C.3br, TF.1–TF.10',
    'depends_on': 'GH2011 A/C and TT8.1 closed-union descent; Quillen Section7 Props2.10/3.2; Pedrini–Weibel1994 Lem5.2; Levine1994 p258 arbitrary-scheme Adams naturality; WeibelII4.9/4.10/8.8.5; exact first-jet Bertini argument; C3bm ordinary exceptional presentation',
    'manuscript_pages_settled': '14:106-109',
    'notes': 'All positive characteristics, including2/3. Removes the entire component degree-zero Chow subgroup, with no condition on its Albanese kernel. Uses finitely many actual divisor-by-parameter-point corrections, not family Picard surjectivity. Two-component Pic0-surjectivity criterion included. No triples or higher-dimensional extension asserted. Root and both peers fully passed proof/source audits.33 bounded exact algebra checks0.078066052s; clean five-page four-pass draft build2.845914779s. Exact source scopes and failed bibliography-build repair retained.'
})
with results.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows([row] + rows)

identity = 'GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; RESEARCH_SA06; run /root/real_weil; effort setting not exposed'
events = [
    ('targeted proof check', 'Owner complete TF.1–TF.10 proof and all three saved root/peer full receipts inspected; exact normal strict-local scope and Levine p258 boundary-naturality repairs reread. Full proof PASS; triple-free/Picard-surjectivity restrictions preserved.'),
    ('targeted proof check', 'Exact primary-source ledger C3br_SOURCE_AUDIT.md finalized: fresh full PW5.2 and Quillen7 Props2.10/3.2; fresh GH/Weibel block, prior exact Levine/TT source receipts explicitly attributed. No metadata-only theorem input or unproved family Picard surjectivity.'),
    ('computation', 'Author finite program completed2026-11-19T18:11:05.596781UTC:33/33 exact rational projector/right-inverse/weighted-form samples pass; runtime0.07806605200312333s. No geometric realization or universal theorem inferred from samples.'),
    ('computation', 'Clean draft standalone assembly completed2026-11-19T18:11:33.771860UTC:four exits0, five pages171865bytes, no undefined/overfull diagnostics, runtime2.8459147789981216s. Earlier bibliography underscore/stale-bbl failures are preserved with their runtimes; no mathematics changed.')
]
with (base / 'CHECK_EVENTS.tsv').open('a', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    for kind, outcome in events:
        writer.writerow(['C.3br', now, identity, kind, outcome])

with (base / 'REPORT.md').open('a') as f:
    f.write(f'\n\n## C.3br finalized ({now})\n\n'
            'C3_triple_free_component_lifting.tex is fully root/two-peer proof/source audited and registered. '
            'Joint rational Picard restriction on a triple-free SNC surface permits actual fixed-product perfect families to remove every component degree-zero Chow class, including arbitrary Albanese kernels. '
            'Negative exceptional geometry with rational double curves supplies an explicit right inverse; the exceptional degree matrix then gives B²_Q=0 in exactly C.3bm\'s normal strict-local resolved threefold scope. '
            'The two-component Pic0-restriction criterion is included. No general triple-stratum or higher-dimensional conclusion follows. '
            'The full draft is archived and its old path is a supersession pointer. C3br_SOURCE_AUDIT.md preserves exact primary scopes, all three full reviews, the33-check finite certificate/runtime, and clean standalone build plus transparent bibliography-only failed attempts. '
            'COMPONENT_ALBANESE_KERNEL_RESEARCH.md retains the precise positive-genus product obstruction and the separate unproved triple-stratum extension. Root owns integration and movement assessment.\n')
with (base / 'SOURCE_AUDIT.md').open('a') as f:
    f.write('\n\n### C.3br: full component-family correction\n\n'
            'C3br_SOURCE_AUDIT.md records complete exact primary readings and their limits. '
            'The newly introduced Pedrini–Weibel1994 bibliography key is metadata-checked against Numdam and its full Lemma5.2 proof was freshly read. '
            'Quillen Section7 projection/localization originalpp126–128 was freshly reread. '
            'Singular-boundary Adams uses the already audited Levine p258 arbitrary-scheme construction, not the regular-only lemma. '
            'The final proof and all three full-review receipts pass in the stated triple-free surface scope.\n')

record = {'completed_utc': now, 'runtime_seconds': perf_counter() - started,
          'final': str(final), 'sha256': hashlib.sha256(final.read_bytes()).hexdigest(),
          'archived_draft': str(archive), 'result_id': 'C.3br', 'owner_events_added': len(events),
          'root_integration_changed': False}
(base / 'output' / 'C3br_promotion.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
