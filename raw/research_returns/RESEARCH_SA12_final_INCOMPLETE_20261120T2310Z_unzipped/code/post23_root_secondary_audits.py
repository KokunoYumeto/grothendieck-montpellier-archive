"""Record actual citation refresh and local-divisor input proof audit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

root = Path(__file__).resolve().parents[1]
directory = root / 'parts/D/post23_research'
now = datetime.now(timezone.utc).isoformat()

path = root / 'parts/C/post23_research/D_fixed_local_quotient_alternating.tex'
digest = hashlib.sha256(path.read_bytes()).hexdigest()
assert digest == 'a6dec7a80b91d2adf1d0ada63560b65e0bc8e65801ba935470bb91c415a3d48f'
audit_path = directory / 'audit_fixed_local_quotient_alternating_root.json'
audit = json.loads(audit_path.read_text())
assert audit['sha256'] == '65444607d39f82d410ffba2b673503c196ef8c0d04162eb7ad0464637c1009b8'
audit['original_full_audit_sha256'] = audit['sha256']
audit['sha256'] = digest
audit['citation_only_refresh'] = {
    'utc': now, 'verdict': 'PASS',
    'change': 'Known Suzuki2023 Theorem1.2 attribution added; no statement or formula changed.',
    'fresh_source': 'parts/D/sources/Suzuki2023/source.tex',
    'actual_read_scope': 'Full Introduction through Conjecture1.1 and Theorem1.2, including the exact dimension and connectedness hypotheses. Not a fresh full-paper proof audit.',
    'mathematical_scope': 'The previously fully checked elementary surface proof is retained to exhibit the fixed generator bound used in the count.'
}
audit_path.write_text(json.dumps(audit, indent=2) + '\n')

path = root / 'parts/B/post23_research/D_local_divisor_tame_H2_B.tex'
digest = hashlib.sha256(path.read_bytes()).hexdigest()
assert digest.startswith('3b2e2231')
audit = {
    'actor': 'root', 'model': 'GPT-6 Astra Pro', 'run': 'SA12 run1',
    'effort': 'setting not independently exposed',
    'recorded_utc': now, 'type': 'targeted proof check', 'verdict': 'PASS',
    'path': str(path.relative_to(root)), 'sha256': digest,
    'labels': ['D:local-divisor-tame-central-H2', 'D:horizontal-residue-order-at-node'],
    'actual_file_scope': 'Complete two-lemma candidate and proofs read in full.',
    'checks': [
        'Normal-crossings purity on the regular excellent resolution includes the horizontal branches. Their proper closed fibres are finite, so they contribute no H1. The node term is e+h and the H2 bound is the stated fixed power of n.',
        'The constant-coefficient group-to-etale degree-two comparison has zero degree-one term on the tower of finite covers.',
        'The wild-inertia normal closure need not be pro-p. Every prime-to-p character of it vanishes on each conjugate pro-p generator; the closed generated subgroup is the whole kernel. The five-term sequence therefore gives the claimed inflation injection.',
        'A horizontal strict transform is proper with finite fibres over its complete irreducible branch, hence finite. Henselianity, completeness and regularity make its integral coordinate ring one complete DVR with residue k.',
        'Kummer theory over k((z)) and Hensel divisibility of units identify its prime-to-p residue character with valuation modulo n. Consequently its order equals the unique secondary node-residue order.',
        'No object atlas, hereditary estimate or representation count is inferred from these two prerequisites.'
    ],
    'fresh_primary_reads': [
        {'source': 'sources/ILO2012/tex/exposes/gysin.tex', 'locator': 'Expose XVI Theorem3.1.1 and Corollary3.1.3, pp242--243', 'scope': 'Full statements and full normal-crossings corollary proof read in this same audit period; absolute purity itself remains a known input.'},
        {'source': 'https://stacks.math.columbia.edu/tag/095T', 'locator': 'Theorem59.91.11', 'scope': 'Full statement and entire written proof opened and read.'},
        {'source': 'https://stacks.math.columbia.edu/tag/03RQ', 'locator': 'Lemma59.69.1', 'scope': 'Full statement and entire written proof opened and read.'},
        {'source': 'https://stacks.math.columbia.edu/tag/02LS', 'locator': 'Lemma37.44.1', 'scope': 'Full four-way equivalence and entire written proof opened and read.'}
    ],
    'reused_inputs': 'Previously checked excellent surface resolution, Milne Cartan--Leray comparison, and elementary complete henselian finite-algebra facts. No fresh full Milne chapter read is claimed.',
    'certificate_scope': 'Pure proof audit; no numerical certificate required.',
    'research_movement': 'Prerequisite only; no independent main-gate reduction.'
}
out = directory / 'audit_B_local_divisor_tame_H2_root.json'
assert not out.exists()
out.write_text(json.dumps(audit, indent=2) + '\n')
print(json.dumps({'utc': now, 'citation_refresh': 'PASS', 'local_divisor_audit': str(out.relative_to(root)), 'local_divisor_sha256': digest}, indent=2))
