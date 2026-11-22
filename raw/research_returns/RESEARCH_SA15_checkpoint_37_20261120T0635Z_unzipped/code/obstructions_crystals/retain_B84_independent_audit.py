"""Complete B84 proof audit and unchanged isolated certificate retention."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, sys

root = Path(__file__).resolve().parents[3]
own = root / 'agents/obstructions_crystals'
author = root / 'agents/reduction_descent'
source = author / 'B_tame_residual_one_prime_recovery_candidate.tex'
program = author / 'code/verify_tame_residual_one_prime_recovery.py'
author_output = program.with_suffix('.output.json')
expected = {
    source:'f08414cd26b408769ae16b0fcead57b758ea5e14df2569d396f077834f2950e9',
    program:'270960bfb0edf3a59d349b5bffd79956c3acdddaeffff0e1ee241cb047c711ac',
    author_output:'5a63821fe6a6a3ae37b91f90460f6a2a495e1f118cccb9b3bf4c18576acf796e'
}
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
for path,digest in expected.items():
    assert sha(path)==digest, str(path)
copied = own/'code/B84_independent_check.py'
assert not copied.exists()
copied.write_bytes(program.read_bytes())
run = subprocess.run([sys.executable,str(copied)],cwd=root,capture_output=True,text=True)
copied.with_suffix('.stdout.txt').write_text(run.stdout)
copied.with_suffix('.stderr.txt').write_text(run.stderr)
hashes = {str(path.relative_to(root)):{'before':digest,'after':sha(path)}
          for path,digest in expected.items()}
hash_path = own/'outputs/B84_author_hashes_preserved.json'
hash_path.write_text(json.dumps(hashes,indent=2)+'\n')
assert all(row['before']==row['after'] for row in hashes.values())
assert run.returncode==0,run.stderr
result = json.loads(copied.with_suffix('.output.json').read_text())
assert result['status']=='PASS'
assert result['counts']==json.loads(author_output.read_text())['counts']
now=datetime.now(timezone.utc).isoformat()
labels=['prop:B-RD84-tame','cor:B-RD84-first-wild','rem:B-RD84-scope']
record={
    'status':'FULL PASS','actual_utc':now,
    'candidate':str(source.relative_to(root)),'candidate_sha256':expected[source],
    'labels':labels,
    'proof_read_scope':'Entire final three-label B84 proof and complete standalone checker read. The full internal B69 actual inverse-polygon/quotient/line-character proof and B60 fixed-coefficient lower-break proof were freshly reread in the immediately preceding B82/B83 audits; their steps were rederived again here without a prime-to-p absolute-index assumption. B77 square exclusion and finite twisting, B82 direct determinant delta, and B83 common-point-field construction were checked in their exact already-read scope.',
    'checks':[
        'For arbitrary e with mu_p in K, s=(p+1)e is a multiple of N. Rational first-level modules give B_i=p*b_i and 0<b_i<e. The low-target inverse Newton segment gives b_i/q for every primitive second-level point above an outside-high residual vector.',
        'The actual comparison identifies stabilizers of a chosen outside-both primitive pair. Rational first-level torsion makes the common point field Galois with translation group of order at most q. One prime-to-p b1 gives denominator q and forces exact degree q, so every first-level translation occurs regardless of the divisibility of b2. No bound on the full division field is used.',
        'In that same actual point field, prime valuation b1 gives equality v(gx1-x1)=b1+r(g), while b2 only needs the unconditional lower bound. A high1/low2 translation would give a displacement gap increasing in both b_i with maximum -q(p+1) at e-1,e-1. This excludes distinct high lines at every absolute index.',
        'Once the lines align, low translation gives (q-1)(b2-b1)>=0 and high translation gives (p^3+1)(b1-b2)>=0. The two inequalities force equality, after which equality of actual high-line characters recovers c modulo N. This genuinely strengthens the earlier both-prime statement.',
        'At e=p(p-1), the third-level square-determinant exclusion and one-slope scalar-leading-action argument force two slopes in the tame reducible remaining branch. Applying the new proposition to the actual p^2 submodule forces both b_i divisible by p. The small interval k_i in[1,p-2] and common determinant show that different characters require exchanged high lines.',
        'For p5, a common finite tame twist is trivial over L and leaves the actual Newton parameters unchanged. c_i=1 modulo4 and B_i=c_i modulo6 force B_i in{25,75}. Directly solving the residual high/low character equality gives exactly (25,1;75,9) and (25,13;75,21), modulo interchange. The simultaneous quadratic twist interchanges finite types A,C and fixes B. No realization of the remaining pattern is inferred.'
    ],
    'primary_source_scope':'No new external original-source read claimed. The proof is an actual point-field and two-translation argument, with the established universal-coefficient, finite-flat and determinant bridges reused only after the stated complete internal rereads.',
    'independent_program':str(copied.relative_to(root)),
    'independent_output':str(copied.with_suffix('.output.json').relative_to(root)),
    'independent_runtime_seconds':result['runtime_seconds'],'counts':result['counts'],
    'author_bytes_unchanged':True,'hash_record':str(hash_path.relative_to(root)),
    'finite_scope':result['scope'],
    'scope':'Actual p2 tame-residual recovery when at least one b is prime to p, for arbitrary e. At first-wild p5 the residual-tame remaining necessary pattern is {25,75}, type A/B up to common quadratic twist, at every full-image size. No unrestricted actual p3 recovery, example, or exact first-wild index.'
}
audit=own/'B84_independent_audit.json'
with audit.open('x') as f:
    json.dump(record,f,indent=2);f.write('\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now,label,'independent_full_proof_code_audit',str(source.relative_to(root)),
                           'Complete common-point-field and both actual-translation arguments rederived; unchanged isolated certificate',
                           'PASS',str(audit.relative_to(root))])+'\n')
print(json.dumps({'status':record['status'],'actual_utc':now,'record':str(audit.relative_to(root)),
                  'runtime_seconds':result['runtime_seconds'],'labels':labels}))
