#!/usr/bin/env python3
"""Preserve post-checkpoint audits and import recovered result/source metadata."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re

ROOT = Path(__file__).resolve().parents[1]
stamp = datetime.now(timezone.utc).isoformat()
check_fields = ['statement_id', 'date', 'who', 'type', 'outcome']
root_checks = ROOT / 'notes/root_checks.tsv'
with root_checks.open(newline='') as stream:
    prior = list(csv.DictReader(stream, delimiter='\t'))
keys = {(r['statement_id'], r['date'], r['type'], r['outcome']) for r in prior}
with (ROOT / 'CHECK_EVENTS.tsv').open(newline='') as stream:
    for row in csv.DictReader(stream, delimiter='\t'):
        key = (row['statement_id'], row['date'], row['type'], row['outcome'])
        if 'root' in row['who'] and key not in keys:
            prior.append(row)
            keys.add(key)

audited = {
 'A.142': ('agents/singularities_duality/part_base_three_component_obstruction.tex', 'Literal promoted proof reread: relative normal realization, full side boundary, ordinary endpoint trace, finite projective base and distinction from block loops.'),
 'A.143': ('agents/singularities_duality/part_base_three_CS_homomorphism.tex', 'Literal promoted proof reread: relative formal class, trivial action, normalization and path invariance, typed naturality and only kernel containment.'),
 'A.144': ('agents/singularities_duality/part_finite_three_component_image.tex', 'Complete reconstructed proof reread: relative HMTW formula at (0,y), Sylow SK1 condition from periodic resolution, full labeled product boundary.'),
 'A.145': ('agents/singularities_duality/part_localized_three_component_image.tex', 'Complete reconstructed proof reread: punctured closed finite-group summands, exact collar compression, supported excision and double suspension, no ambient good-group assumption.'),
 'A.146': ('agents/singularities_duality/part_torus_three_obstruction.tex', 'Complete reconstructed proof reread: endpoint/lift corrections, actual relative homotopy equivalence, degree-five assembly, specified relative PL obstruction.'),
 'A.147': ('agents/higher_comparison/part_parameter_lipschitz_comparison.tex', 'Complete reconstructed proof reread plus quantifier-order clarification: constant input coloring Q fixed before K,M,xi; roof support, split marks, literal prisms and relative finite Alexander construction.'),
 'A.148': ('agents/singularities_duality/part_pair_factorization.tex', 'Complete reconstructed proof reread: common finite target choices, common marked ambient change, common E straightening and full-boundary homotopy extension.'),
 'A.150': ('agents/maximal_locus/A150_scalar_clock.tex', 'Complete reconstructed proof reread: compact spatial extension, bounded derivative choice, explicit variation clock, generic-line MVT, finite prescribed times and exact Hausdorff identity.'),
 'A.152': ('agents/singularities_duality/part_hausdorff_regularization.tex', 'Complete reconstructed proof reread: Euclidean finite join metric, connectivity, proper mapping theorem, based sphere approximation, literal boundary section and annulus repair.'),
 'A.154': ('agents/higher_comparison/part_spatial_lipschitz_factorization.tex', 'Complete reconstructed proof reread: exact finite variation, mixed coordinate bounds, standard-range refinement, actual PL cubical model, vector extension and tagged-graph conversion.'),
 'A.155': ('agents/higher_comparison/part_real_range_and_model_surjectivity.tex', 'Complete reconstructed proof reread: real comparison triangle, fixed spatial model, coefficient-cell continuity and reflection of a finite first-order witness; no PL coefficient-path inference.'),
 'A.156': ('agents/higher_comparison/part_relative_PL_filling.tex', 'Complete reconstructed proof reread: PL clock normalization and coefficient fields, individually fixed bottom, PL roof boundary track, original prescribed boundary cells, total prism coning and reverse PL collar.'),
}
receipts = []
for ident, (name, detail) in audited.items():
    digest = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
    note = 'PASS: ' + detail + ' New reconstructed/promoted source SHA256 ' + digest + '.'
    prior.append(dict(zip(check_fields, [ident, stamp, 'GPT-6 Astra (OpenAI, ChatGPT Pro mode), root; inherited configuration', 'targeted full literal proof check', note])))
    receipts.append({'id': ident, 'source': name, 'sha256': digest, 'outcome': 'PASS', 'detail': detail})
with root_checks.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=check_fields, delimiter='\t')
    writer.writeheader()
    writer.writerows(prior)

bib_paths = [ROOT / 'notes/root_references.bib', *sorted((ROOT / 'agents').glob('*/references.bib'))]
bib_text = '\n'.join(p.read_text() for p in bib_paths)
bib_keys = set(re.findall(r'@\w+\s*\{\s*([^,\s]+)', bib_text))
added = []
for name in ['agents/singularities_duality/logs/recovery_references_pending.bib', 'agents/maximal_locus/notes/recovered_original_sources.bib', 'agents/higher_comparison/recovery_references_pending.bib']:
    source = ROOT / name
    if not source.exists():
        continue
    for block in re.split(r'(?=@\w+\s*\{)', source.read_text()):
        match = re.match(r'@\w+\s*\{\s*([^,\s]+)', block)
        if match and match.group(1) not in bib_keys:
            with (ROOT / 'notes/root_references.bib').open('a') as stream:
                stream.write('\n\n' + block.strip() + '\n')
            bib_keys.add(match.group(1))
            added.append(match.group(1))

fields = ['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
record_file = ROOT / 'notes/root_results.csv'
with record_file.open(newline='') as stream:
    records = {r['id']: r for r in csv.DictReader(stream)}
extra_files = [name for name, detail in audited.values()] + [
 'parts/reconstructed_transfer_regularization.tex',
 'parts/whole_definable_effective_model.tex',
 'agents/singularities_duality/part_finite_join_resolution.tex',
 'agents/singularities_duality/part_compact_metric_resolution.tex',
 'agents/higher_comparison/A159_all_field_higher_surjectivity.tex',
 'agents/higher_comparison/A160_all_field_weak_comparison.tex',
 'agents/maximal_locus/part_A5_surface_family_sewing.tex',
 'agents/maximal_locus/part_A5_radial_angular_gate.tex',
 'agents/singularities_duality/part_angular_tent_counterexample.tex',
]
for name in dict.fromkeys(extra_files):
    p = ROOT / name
    if not p.exists():
        continue
    for match in re.finditer(r'\\begin\{saresult\}\{([^}]*)\}\{([^}]*)\}\{([^\n]*)\}', p.read_text()):
        ident, status, title = match.groups()
        records[ident] = dict(zip(fields, [ident, title, status, name,
          'Full dependencies and exact source locators in the numbered proof.', '',
          'Post-checkpoint14 source integrated. Complete proof and audit/provenance records are retained; original-row status is tracked separately.']))
with record_file.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(records[k] for k in sorted(records))
result = {'recorded_utc': stamp, 'literal_audits': receipts, 'bibliography_entries_added': added}
(ROOT / 'logs/recovered_integration_receipt.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'recorded_utc': stamp, 'literal_audits': len(receipts), 'bibliography_entries_added': added}))
