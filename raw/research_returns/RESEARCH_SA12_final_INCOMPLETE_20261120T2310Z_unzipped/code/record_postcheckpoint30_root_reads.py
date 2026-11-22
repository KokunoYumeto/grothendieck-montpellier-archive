"""Record exact read scopes after CP30; no promotion or central count change."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[1]
items = [
    (
        'parts/D/post29_research/note_thick_A_chain_end_framing_D.tex',
        'Entire actual file read after the earlier truncated tool response. Checked the free basis over k[[u,v]], the two fat-end coordinate rings for a,b<=N, the independent normal-degree restrictions, the common leading coefficient condition, and the sum giving a(a-1)/2+b(b-1)/2+min(a,b). The existing fully audited rational-double-point H1 vanishing is reused. This is a local exact diagnostic, not a global count counterexample.'
    ),
    (
        'parts/B/post29_research/note_mixed_end_quantum_A_chain_B.tex',
        'Entire actual file read. Checked the character-lattice index NL^2, the diagonalizable kernel of size N(L/h)^2, extension of kernel characters, the h-dimensional weight-one blocks, residual end-inertia descent by homogeneous bases, retention of interior sectors, the first-coarse-end restriction estimate, and the multiplicity-list binomial budget. The preceding exact-model full-category and fat-end proofs are reused. Arbitrary gerbe identification, thick-core gluing and the global object atlas remain outside this note.'
    ),
]
record = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'actor': 'root',
    'kind': 'Actual-file research verification, no promotion',
    'files': [dict(path=path, sha256=hashlib.sha256((root/path).read_bytes()).hexdigest(), scope=scope) for path, scope in items],
    'source_scope': 'No new external source read is claimed. Existing audited full-RDP inputs and explicit algebra in the actual files are the inputs.',
    'strict_main_gate_reductions': [],
    'requested_status_changes': [],
    'movement': False,
}
out = root/'code/output/root_postcheckpoint30_mixed_and_thick_scope.json'
assert not out.exists()
out.write_text(json.dumps(record, indent=2)+'\n')
guard = {
    'observed_utc': '2026-11-20T22:38:54+00:00',
    'kind': 'Early scheduling guard rejection before any archive creation',
    'command': 'python3 code/scheduled_checkpoint30.py',
    'exit_code': 1,
    'error': 'AssertionError: Start this scheduled wrapper in the final minute before22:40UTC.',
    'effect': 'The first guard stopped the attempt before size metadata or an archive was written. The wrapper was started again within the permitted final minute and created CP30 at its scheduled22:40 slot.',
    'successful_archive_verification': 'code/output/checkpoint30_archive_verification.json',
    'successful_saved_receipt': 'code/output/checkpoint30_saved_receipt.json',
    'note': 'The clock value is the tool-observed second immediately before the rejected invocation, not an invented subsecond process timestamp.'
}
guard_out = root/'code/output/checkpoint30_early_guard_event.json'
assert not guard_out.exists()
guard_out.write_text(json.dumps(guard, indent=2)+'\n')
print(json.dumps({'read_scope_record': str(out.relative_to(root)), 'files': len(items), 'movement': False, 'guard_record': str(guard_out.relative_to(root))}))
