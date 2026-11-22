"""Record the exact known-input recognition added to the checked closure."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
root = Path(__file__).resolve().parents[1]
path = root / 'parts/C/post23_research/D_alternating_dimensional_normalization_closure.tex'
digest = hashlib.sha256(path.read_bytes()).hexdigest()
assert digest == '23b57511aaf79095b8943a54c9e36dffe8d87afb2ffdded337db839091364ea1'
record_path = root / 'parts/D/post23_research/audit_C_alternating_dimensional_closure_root.json'
record = json.loads(record_path.read_text())
assert record['sha256'] == '36f2ed219d01ae2bcb7adb57d7871674666ae248b86d398825403b631d10e144'
record['original_full_audit_sha256'] = record['sha256']
record['sha256'] = digest
record['known_input_refresh'] = {
    'utc': datetime.now(timezone.utc).isoformat(), 'verdict': 'PASS',
    'scope': 'The full mathematical closure was audited at the original SHA. The exact diff changes only the concrete choice to the two fixed quotients and adds its known published input; disconnected-cover and normalization proofs are unchanged.',
    'input': 'Grothendieck--Murre1971, Section9.1 and Theorem9.2, printed pp122--123',
    'source': 'parts/C/post23_research/sources/Grothendieck_Murre_1971_ch9_preview.pdf',
    'source_sha256': '8875d99455752dfe6a9b7274ea98e81f2e5138ccffae4f8e15da90693c40ce29',
    'actual_source_scope': 'Both original publisher-preview page images actually viewed at full size: complete hypotheses9.1, full Theorem9.2 and definition of prime-to-p finite presentation, complete reduction9.3 and start of9.4. The rest of the proof is absent and is not claimed read.',
    'images_actually_viewed': ['qa/GM1971_ch9_root_p122.webp', 'qa/GM1971_ch9_root_p123.webp'],
    'deduction': 'The stated pro-prime-to-p finite presentation includes a finite topological generating set. Each fixed complete normal local surface ring meets the theorem hypotheses. A finite orbit action factors through that quotient exactly when its image has order prime to p. Thus the two fixed quotients control the union of nilpotent and prime-to-p image classes.',
    'new_priority_claim': False, 'separate_movement': False
}
record_path.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'record': str(record_path.relative_to(root)), 'sha256': digest, 'verdict': 'PASS'}, indent=2))
