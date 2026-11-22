"""Record the exact structural-note and cycle rereads without promotion."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[1]
paths = [
    'parts/D/post29_research/note_minimal_anchor_residual_locality_D.tex',
    'parts/D/post29_research/minimal_anchor_residual_locality_source_scope_D.json',
    'parts/B/post29_research/note_generic_order_generation_duality_B.tex',
    'parts/B/post25_research/D_comparable_reduction_cycles_B.tex',
    'parts/C/post18_research/D_energy_reduction_cycles.tex',
]
record = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'actor': 'root',
    'kind': 'Exact actual-file and primary-source read, no promotion',
    'files': [dict(path=p, sha256=hashlib.sha256((root/p).read_bytes()).hexdigest(), complete_file_read=True) for p in paths],
    'residual_locality_verdict': 'PASS in the explicitly stated canonical height-one full-pullback scope; unpromoted',
    'independent_checks': [
        'A finite order inside the generic division algebra has no nontrivial idempotent. Successive lifting through the finite-dimensional radical and the complete base forces the residual semisimple algebra to be k.',
        'The scalar-plus-nilpotent property survives residue-field extension and nonzero unital quotients. The actual torsion-free pullback image at an original exceptional DVR gives the required quotient.',
        'A minimal-rank hypothesis alone therefore does not produce a full matrix residual action on multiplicity spaces of dimension greater than one. The radical action still controls invariant flags; no unbounded global family is inferred.',
        'The claimed scope deliberately excludes a newly created exceptional divisor over an old evaluation basepoint when only the old full bundle is pulled back.',
        'The conditional duality note retains the full nonreduced generic rings and the finite point-ideal restriction kernel. It does not prove the needed order-valued point-ideal vanishing.',
        'The two established reduction-cycle files were reread completely. Their specified relative-minimal model, all-subcycle inequalities and qualified realization/family scope remain essential.'
    ],
    'fresh_primary_source': {
        'apa': 'Leuschke, G. J., & Wiegand, R. (2011, March 9). Cohen–Macaulay representations [Author draft].',
        'url': 'https://www-users.cse.umn.edu/~reiner/ReadingSeminars/McKaySeminar2016/LeuschkeWiegandBookonMcKay.pdf',
        'retrieval_refs': ['turn254772165view0', 'turn815898981view0'],
        'complete_written_proofs_read': ['Proposition 1.4', 'Lemma 1.6', 'Theorem 1.7', 'Corollary 1.8'],
        'printed_pages': '6–9',
        'precision': 'Choose every approximate idempotent as a polynomial in one initial lift. The approximants then commute, so the written Cauchy-sequence argument applies without assuming uniqueness of arbitrary noncommutative lifts.',
        'recursive_known_inputs': ['Finite-module adic completeness', 'Wedderburn–Artin theorem', 'Nakayama lemma'],
        'no_full_book_download_or_image_inspection_claim': True
    },
    'other_source_scope': 'Previously audited cycle, curve-duality and formal-functions inputs are reused. This record does not claim fresh reopening of their recursive references.',
    'requested_status_changes': [],
    'strict_main_gate_reductions': [],
    'movement': False
}
out=root/'code/output/root_residual_locality_and_cycle_scope.json'
assert not out.exists()
out.write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps({'record': str(out.relative_to(root)), 'files': len(paths), 'movement': False}))
