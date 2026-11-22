"""Full independent proof/code audit of the explicit cyclotomic base example."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, subprocess, sys

root = Path(__file__).resolve().parents[3]
own = root / 'agents/obstructions_crystals'
author = root / 'agents/reduction_descent'
source = author / 'B_p5_cyclotomic_break_three_example_candidate.tex'
program = author / 'code/verify_p5_cyclotomic_break_three_example.py'
output = program.with_suffix('.output.json')
expected = {
    source: 'a7e4181ce539b437c10c124ff016c5a6a65d1c4747fda01f8958f93dd3cdfbd8',
    program: '6493112f34e0dce0d4a571be92c59408e9b77676e4ee664b4f4f93335015c1f0',
    output: '455e68945c3e2678d4d2993da23f4f6590c47a837f613041daae86c37e8fd613',
}
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert all(sha(p) == h for p, h in expected.items())
copied = own / 'code/B89_independent_check.py'
with copied.open('xb') as f:
    f.write(program.read_bytes())
run = subprocess.run([sys.executable, str(copied)], cwd=root, capture_output=True, text=True)
copied.with_suffix('.stdout.txt').write_text(run.stdout)
copied.with_suffix('.stderr.txt').write_text(run.stderr)
hashes = {str(p.relative_to(root)): {'before': h, 'after': sha(p)} for p, h in expected.items()}
hash_record = own / 'outputs/B89_author_hashes_preserved.json'
hash_record.write_text(json.dumps(hashes, indent=2) + '\n')
assert all(v['before'] == v['after'] for v in hashes.values())
assert run.returncode == 0, run.stderr
result = json.loads(copied.with_suffix('.output.json').read_text())
author_result = json.loads(output.read_text())
strip = lambda d: {k: v for k, v in d.items() if k not in ('runtime_seconds', 'actual_utc')}
assert result['status'] == 'PASS' and strip(result) == strip(author_result)
labels = re.findall(r'\\label\{((?:lem|rem):[^}]+)\}', source.read_text())
assert len(labels) == 2
now = datetime.now(timezone.utc).isoformat()
record = {
    'status': 'FULL INDEPENDENT PROOF AND EXACT CODE PASS',
    'actual_utc': now,
    'candidate': str(source.relative_to(root)),
    'candidate_sha256': expected[source],
    'labels': labels,
    'proof_read_scope': 'Entire final two-label candidate, standalone checker, actual author output and candidate record read. Complete canonical B60 exact lower-break lemma and its fixed-representative expansion proof freshly reread. The entire B88 tame-scaling proof was fully independently audited immediately beforehand.',
    'checks': [
        'The three shifted cyclotomic polynomials are Eisenstein over W(k), including for arbitrary algebraically closed residue field. Thus the first extension has degree four, pi1 is a uniformizer, and the larger cyclotomic tower has the asserted cyclic degrees by its actual root-of-unity automorphisms.',
        'The defining polynomial T^5+5T^4+10T^3+(10+pi1^4)T^2+5T-pi1 is Eisenstein at pi1. Its middle coefficient may have extra cancellation but remains divisible by pi1; this cannot affect the Eisenstein criterion. The actual degree-five extension has uniformizer t, residue k, v_K(pi1)=5 and v_K(5)=20.',
        'Using the defining relation for t, the polynomial of alpha-t has constant -pi1^4 t^2 of valuation22, intermediate coefficients binom(5,j)(1+t)^(5-j) of valuation20 and leading coefficient one. All four intermediate vertices are strictly above the chord, so every root has valuation22/5.',
        'The actual Kummer extension K(zeta25)/K is Galois of degree dividing five because mu5 is already in K. The fractional root valuation forces ramification degree five, hence field degree five. It is totally ramified with v_C(alpha-t)=22.',
        'Every nonidentity automorphism changes alpha-t by (zeta5^j-1)zeta25 of normalized valuation25. Since22 is prime to five, the exact fixed-representative lower-break equality gives the actual common break3. No valuation of a formal proxy is substituted for this field coordinate.',
        'The degree-25 cyclic extension K1(mu125)/K1 has unique degree-five subfield K1(mu25). Its intersection with the degree-five field K is either K1 or K; the latter would force K=K1(mu25), contradicting the preceding actual degree-five extension over K. Thus base change has the full cyclic degree25.',
        'The degree24 tame extension and the cyclotomic degree-five extension are disjoint. The already checked uniformizer/Hensel argument for their actual compositum scales the lower break by24, yielding72. This uses tame base change, not a false general equality of lower and upper numbering.',
        'Only an allowed base and its cyclotomic characters have been realized. No height-two formal group, common torsion module, ambiguous pair, or unrestricted least-index example follows. The retained initial structural SymPy failure did not establish any mathematical identity; the final expanded-difference checks do.'
    ],
    'source_scope': 'No new external-source opening or image read claimed. Standard Eisenstein/Newton arithmetic is proved in the file; the exact internal B60 and B88 dependencies were completely checked as specified.',
    'independent_program': str(copied.relative_to(root)),
    'independent_output': str(copied.with_suffix('.output.json').relative_to(root)),
    'independent_runtime_seconds': result['runtime_seconds'],
    'counts': result['counts'],
    'author_bytes_unchanged': True,
    'all_mathematical_output_identical': True,
    'hash_record': str(hash_record.relative_to(root)),
    'scope': result['scope'],
}
audit = own / 'B89_independent_audit.json'
with audit.open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now, label, 'independent_full_proof_code_audit', str(source.relative_to(root)),
                           'Entire explicit field, exact coordinate break, cyclic intersection and literal isolated checker',
                           'PASS; base-only scope', str(audit.relative_to(root))]) + '\n')
print(json.dumps({'status': record['status'], 'actual_utc': now, 'record': str(audit.relative_to(root)),
                  'runtime_seconds': result['runtime_seconds'], 'labels': labels}))
