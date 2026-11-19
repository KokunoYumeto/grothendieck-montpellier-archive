"""Serialize manually selected source-identity findings; never score/select merges."""
from pathlib import Path
import json
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'p2'
records = {}
for shard in ('p2', 'p4', 'root_codex'):
    for kind, filename in [('item', 'items.json'), ('claim', 'claims.json'), ('problem', 'problems.json')]:
        for record in json.loads((ROOT / shard / filename).read_text()):
            records[record['id']] = (shard, kind, record)

# Each row below is a human-reviewed decision based on the quoted source joins.
aliases = [
    ('item', 'SA13-503', 'SA13-63',
     'The same five local schemes of §4 are explicitly resumed in §6.1; the later quasi-isomorphism reduces five cohomological spaces to four.',
     'Keep C875–877 as distinct construction, continuity and equivariance claims. Keep the general five-space setup and the later isolated-support hypothesis as separate occurrences.'),
    ('item', 'SA13-505', 'SA13-63',
     'Triangle B in §4.5 becomes exactly the triangle (6.2.2) after substituting the equivariant quasi-isomorphism (6.1.4).',
     'Keep C882 as the explicit open/closed triangle and C609 as the additional four-space reconstruction. Triangle A and its premise defect remain SA504, C878–881 and MP242.'),
    ('claim', 'C-SA13-872', 'C-SA13-605',
     'The lower bound explicitly promised au §5 in §3.2(a), scan142, is the lower endpoint of Corollary5.4 on154.',
     'Retain the earlier fibre-lci/relative-lci and rectified-depth premise as an explicit statement component. Keep earlier open/promise status distinct from the later proof sketch. Preserve the pinching example C873 under SA501.'),
    ('claim', 'C-SA13-625', 'C-SA13-190',
     'The strict-local normal-crossing Abhyankar/Kummer prime-to-p fundamental-group theorem of Lemma8.5(c) is invoked again in Remark3.2.1.',
     'Add the explicit Kummer construction and derivative check, but retain the missing −t_i as a reading alarm. Keep regularity, strict henselianity and the prime-to-p quotient explicit; never promote the claim to the full wild fundamental group. Add SA64 to the canonical claim items.'),
    ('claim', 'C-SA13-823', 'C-SA13-228',
     'The §5.4 promise on82 names the next exposé; Corollary3.9 on101 explicitly cites réduction II5.4 and repeats the same exponent2/exponent3 assertion.',
     'Retain the smooth-curve bound2, normal-case bound2, general draft bound3 and the stronger published bound2 for general finite type as separate historical clauses. Preserve the H2/H1 reading alarm on81.'),
]
merges = []
for kind, old, new, reason, preserve in aliases:
    assert old in records and new in records
    assert records[old][1] == records[new][1] == kind
    merges.append({
        'kind': kind, 'from': old, 'canonical': new,
        'reason': reason, 'required_preservation': preserve,
        'from_source_locators': records[old][2].get('lines', records[old][2].get('occurrences', [])),
        'canonical_source_locators': records[new][2].get('lines', records[new][2].get('occurrences', [])),
        'status': 'proposed; root assembly owns application',
    })

component_links = [
    {'from': 'C-SA13-609', 'to': 'C-SA13-881', 'relation': 'repeated premise, then new reconstruction',
     'evidence': 'K34-09 §6.1.1–6.1.4, global298–323, repeats the quasi-isomorphism; §6.2 adds K→L and the cone. Preserve both claims.'},
    {'from': 'C-SA13-658', 'to': 'C-SA13-831', 'relation': 'same exterior-power formula with support shift',
     'evidence': 'K34-12 scan205 identifies H_Y^q with R^(q−1)j_*; K34-06 scans107,109 proves exterior powers. Retain the new local-support indexing and twist alarm in C658.'},
    {'from': 'C-SA13-660', 'to': 'C-SA13-831', 'relation': 'same exterior-power input, new weight conclusion',
     'evidence': 'K34-12 scan207 uses the normal-crossing formula to derive weights p+2q and E3 degeneration; that consequence is absent from C831.'},
    {'from': 'C-SA13-621', 'to': 'C-SA13-217', 'relation': 'same dense-open fundamental-group input',
     'evidence': 'K34-10 scan175 uses normal dense-open surjectivity, then generic curves and a stable marked model. Retain the compound reduction and model theorem in C621.'},
    {'from': 'C-SA13-621', 'to': 'C-SA13-223', 'relation': 'generic-curve input with extra marked-model construction',
     'evidence': 'K34-10 scans175–176 add stable marked models and blowups; K34-04 generic-curve argument does not assert that model theorem.'},
    {'from': 'C-SA13-814', 'to': 'C-SA13-169', 'relation': 'same finite prime-to-ell image input',
     'evidence': 'K34-05 global239 explicitly refers to exposé I; global243–247 generalizes the invariant construction to Q. Retain that construction and finite-extension application as additional clauses.'},
    {'from': 'C-SA13-822', 'to': 'C-SA13-184', 'relation': 'conditional proof occurrence of the earlier monodromy conjecture',
     'evidence': 'K34-06 Cor3.7 and Rem3.8, global6–20, add finiteness, partial-purity scope and resolution restrictions; K34-02 §7.1–7.2 announces this geometric proof. Keep the extra finiteness and proof-hypothesis statements.'},
    {'from': 'C-SA13-651', 'to': 'C-SA13-138', 'relation': 'relative abelian-scheme version of degree-one comparison',
     'evidence': 'C651 concerns a local system on a base and differentiation; C138 concerns a connected smooth commutative group over a field and a disconnectedness correction. Retain both scopes.'},
]
updates = [
    {'id': 'MP-SA13-240', 'add_occurrence_claim': 'C-SA13-605',
     'action': 'Add K34-09 scan154 Cor5.4 as the explicitly promised later lower-bound result; distinguish historical proof conditions from current trait theorem. No root problem has identical scope.'},
    {'id': 'MP-SA13-242', 'add_occurrence_claims': ['C-SA13-600', 'C-SA13-609'],
     'action': 'Add K34-09 §5.1 and §6.1.1 as later passages explicitly imposing all strict generizations/punctured-fibre vanishing. Keep the earlier defective formulation and local reading alarm.'},
    {'id': 'SA13-502', 'link_to': 'SA13-62',
     'action': 'Record the explicit §5.0 backward reference to §3.3/3.2 as programme→execution; do not alias the historical prerequisite list to the later package of distinct geometric-depth problems.'},
]
nonmerges = [
    {'ids': ['MP-SA13-195', 'MP-SA13-175', 'MP-SA13-168', 'MP-SA13-236'],
     'reason': 'Marked nodal curve models with disjoint boundary sections, abelian-variety semistable/good reduction, generic H1 curve reduction, and all-characteristic resolution/full nearby cycles are different assertions.'},
    {'ids': ['MP-SA13-190', 'MP-SA13-191', 'MP-SA13-240'],
     'reason': 'Geometric-depth localization/flat-map lemmas use regular presentations and ideal generators; the earlier rectified étale depth is prof_et plus dimension of point closure. No equality of these invariants is asserted.'},
    {'ids': ['MP-SA13-192', 'MP-SA13-193', 'MP-SA13-240'],
     'reason': 'Nonabelian and arbitrary excellent-local-base extensions have stronger scopes than the trait lci lower bound deferred in MP240.'},
    {'ids': ['MP-SA13-194', 'MP-SA13-234'],
     'reason': 'The beta/cone boundary compatibility and the normal-crossing cup-product residue square are different diagrams.'},
    {'ids': ['MP-SA13-196', 'MP-SA13-168', 'MP-SA13-169'],
     'reason': 'A fixed square of an ample line bundle with a prescribed section is not ordinary sufficiently-ample generic-curve reduction.'},
    {'ids': ['MP-SA13-198', 'MP-SA13-199', 'MP-SA13-160'],
     'reason': 'All-representation analytic/algebraic envelopes and their dimensions are distinct from the fixed-open-subgroup envelope for commutative-unipotent representations.'},
    {'ids': ['MP-SA13-200', 'MP-SA13-166'],
     'reason': 'Arithmetic-model descent of geometric local systems is not the nonproper constructibility/base-change premise in spreading.'},
    {'ids': ['MP-SA13-201', 'MP-SA13-172'],
     'reason': 'The Tate homomorphism/commutant theorem is an input to, not the same assertion as, the solvable-Tate-image CM criterion.'},
    {'ids': ['MP-SA13-202', 'MP-SA13-204', 'MP-SA13-164'],
     'reason': 'Ranks of normal-crossing correspondence complexes, false purity of inertia invariants/coinvariants, and common rational Weil representations have different quantifiers and outcomes.'},
    {'ids': ['MP-SA13-205', 'MP-SA13-90', 'MP-SA13-91'],
     'reason': 'Hilbert–Mumford/numerical-criterion proof references differ from flat quotient and finite-type quotient questions.'},
    {'ids': ['C-SA13-618', 'C-SA13-224'],
     'reason': 'Finite presentation is stronger than topological finite generation; preserve a strengthening link, not a theorem alias.'},
    {'ids': ['C-SA13-623', 'C-SA13-218'],
     'reason': 'Arbitrary extension between separably closed fields is not the same invariance assertion as a radicial universal homeomorphism.'},
    {'ids': ['C-SA13-606', 'C-SA13-866'],
     'reason': 'The same d=0 monodromy conclusion comes from different hypotheses: lci special fibre and local depth versus smooth proper generic fibre and duality. Keep both formulations.'},
    {'ids': ['SA13-504', 'SA13-505'],
     'reason': 'Triangle A uses support cohomology; triangle B uses extension by zero. The latter is an occurrence under canonical SA63, but that does not identify these two triangles.'},
]
for row in component_links:
    assert row['from'] in records and row['to'] in records
for row in nonmerges:
    assert all(x in records for x in row['ids']), row

result = {
    'date': '2026-11-19',
    'who': 'GPT-6 Astra Pro; configured effort not exposed; SA13 part 2/p2',
    'scope': 'Root supplementary versus p2 and p4 Codex; additional exact p2/p4 recurrence checked; no source shard rewritten.',
    'reviewed_counts': {'root_items': 8, 'root_claims': 71, 'root_problems': 16,
                        'p2_items': 108, 'p2_claims': 142, 'p2_problems': 49,
                        'p4_codex_items': 29, 'p4_codex_claims': 83, 'p4_codex_problems': 13},
    'rules': ['Keep all379 original Pro verdict rows.', 'Union sources, locators, bibliographic evidence and check events.',
              'Keep page statuses at occurrence level.', 'Item aliases do not merge their distinct claims.',
              'Component links below are not whole-claim aliases; preserve the extra conclusions.'],
    'merges': merges, 'problem_merges': [], 'component_identity_links': component_links,
    'later_occurrence_updates': updates, 'do_not_merge': nonmerges,
}
(OUT / 'supplementary_merge_map.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
validation = {'aliases': len(merges), 'item_aliases': 2, 'claim_aliases': 3,
              'problem_aliases': 0, 'component_links': len(component_links),
              'later_occurrence_updates': len(updates), 'nonmerge_groups': len(nonmerges),
              'missing_ids': [], 'source_shards_modified': False}
(OUT / 'outputs/supplementary_merge_validation.json').write_text(json.dumps(validation, indent=2) + '\n')
marker = 'root/p2/p4 supplementary semantic consolidation'
reading_log = OUT / 'reading_log.tsv'
if marker not in reading_log.read_text():
    with reading_log.open('a') as handle:
        handle.write('\t'.join([
            '2026-11-19', result['who'], marker,
            'All root8items/71claims/16problems; p4Codex29items/83claims/13problems; p2 counterpart records; actual candidate passages K34-08 §§3–4, K34-09 §§5–6, K34-10 174–179, K34-11 180, K34-02 42–44, K34-04 81–82 and K34-06 100–101',
            'Five manually selected aliases, eight component links, three later-occurrence updates, fourteen nonmerge groups; both sides of each alias read. No source shard rewrite or new proof/literature claim.'
        ]) + '\n')
progress = OUT / 'progress.log'
progress_marker = 'Supplementary semantic audit complete'
if progress_marker not in progress.read_text():
    with progress.open('a') as handle:
        handle.write(datetime.now(timezone.utc).isoformat() + ' ' + progress_marker + ': root/p2/p4 comparison;2item+3claim aliases,0problem aliases,8component links,3later-occurrence updates; ID validation passed; parent owns assembly.\n')
print(json.dumps(validation, indent=2))
