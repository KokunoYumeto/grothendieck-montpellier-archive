"""Full B87 proof/source audit and literal author-preserving exact rerun."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import subprocess
import sys

root = Path(__file__).resolve().parents[3]
own = root/'agents/obstructions_crystals'
author = root/'agents/reduction_descent'
source = author/'B_p5_tame_full_first_layer_candidate.tex'
program = author/'code/verify_p5_tame_full_first_layer.py'
output = program.with_suffix('.output.json')
expected = {
    source:'ec7c365f216d6f8d5d44f86dab22bee217f6a7eac6ca96cba03a36b999361bf5',
    program:'18440404e3b7986fcdff83dd6e3b527f1bdaca949571338e97f0f4199e82479e',
    output:'d5e9383836cb488b7ad210247bf36ea637a386e42baae2bd11b2090d4613ed15'
}
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert all(sha(p) == value for p,value in expected.items())
copied = own/'code/B87_independent_check.py'
assert not copied.exists()
copied.write_bytes(program.read_bytes())
run = subprocess.run([sys.executable,str(copied)],cwd=root,capture_output=True,text=True)
copied.with_suffix('.stdout.txt').write_text(run.stdout)
copied.with_suffix('.stderr.txt').write_text(run.stderr)
hashes = {str(p.relative_to(root)):{'before':value,'after':sha(p)}
          for p,value in expected.items()}
hash_path = own/'outputs/B87_author_hashes_preserved.json'
hash_path.write_text(json.dumps(hashes,indent=2)+'\n')
assert all(row['before'] == row['after'] for row in hashes.values())
assert run.returncode == 0, run.stderr
result = json.loads(copied.with_suffix('.output.json').read_text())
author_result = json.loads(output.read_text())
assert result['status'] == 'PASS'
strip_run = lambda data:{k:v for k,v in data.items() if k not in ('actual_utc','runtime_seconds')}
assert strip_run(result) == strip_run(author_result)
labels = re.findall(r'\\label\{((?:lem|prop|cor|rem):[^}]+)\}',source.read_text())
assert len(labels) == 5
now = datetime.now(timezone.utc).isoformat()
record = {
    'status':'FULL PROOF, SOURCE AND EXACT CODE PASS',
    'actual_utc':now,
    'candidate':str(source.relative_to(root)),
    'candidate_sha256':expected[source], 'labels':labels,
    'proof_read_scope':'Entire final five-label B87 source, entire standalone checker and full actual author output read. The complete canonical B84 proof and its exact normalized residual rows were freshly reread; the entire B60 fixed-representative lower-break lemma and the B81 fixed-coefficient expansion/first-prime-term proof were freshly reread. B83 and B85 actual quotient/evaluation arguments are the preceding complete independent audits, with the invoked steps independently rederived here.',
    'checks':[
        'Residue representatives may be chosen in O_L and are fixed by the Galois group. Below v_E(p), all binomial terms with coefficient divisible by p are absent. Since v_p(A)=1, the leading degree first changes at A+p*b; every later p-divisible degree changes strictly later. The first prime-to-p coefficient, if present, changes uniquely at J+b. Thus the minimum formula is valid at every relevant strict subthreshold valuation, with cancellation only in the tie case.',
        'When the high-displacement line differs from the last ramification line, its elements have the smaller lower break t but larger displacement D1. The last line has break u and displacement D0. Strict monotonicity gives m(t)<D0<D1, forcing J=A+(p-1)t. At u the prime term is uniquely first, giving D0=A+(p-1)t+u. This includes J initially infinite and uses no false lower/upper-break substitution.',
        'The norm-polynomial quotient formula averages i=b+1 over a nonzero coset. If the kernel differs from the last line, the coset contains one element of break u and p-1 of break t, giving the larger quotient break (u+(p-1)t)/p. The quotient killing the last line instead has break t.',
        'The fully proved B84 normalization gives B1=25,B2=75 and exchanged high lines; the possible common residual eigenvalue rows are (0,6) and (12,18), hence identical conjugation weights0,6,18. B83/B85 and tame projectors make W1 the sum of both off-diagonal axes and a diagonal line diag(a,b) with a*b nonzero.',
        'The actual second-level division field has additive group W1. Evaluation at e1 and e2 has kernels E12 and E21 and surjective two-dimensional images. The corresponding actual point fields have degree25 and their intersection is the same diagonal degree5 quotient. The kernels are stable under tame conjugation, so these fields and the indicated cyclic quotients are Galois over K. Their identity is not inferred merely from abstract dimensions.',
        'For a cyclic degree5 quotient, the tame leading multiplier eta satisfies eta^5=zeta. Conjugation of a break-b element scales its leading coefficient by eta^b=zeta^(5b). Thus diagonal and off-diagonal quotient breaks have residues0,6,18 modulo24. Distinct characters force a proper ramification line to be one of the two axes, and distinct quotient residues exclude a single break. In particular the common diagonal break is at least24.',
        'The exact inverse Newton polygons in both good models have their degree1 and degree5 vertices strictly above the target-to-degree25 segment. In the common degree25 point fields the primitive coordinate valuations are95,15,5,45. Actual formal addition gives low/high displacements125/2375 or375/1125 with the displayed diagonal/off-diagonal assignments. All four leading coordinate valuations have5-adic order one, and all displacements lie below the actual absolute index12000.',
        'If E1 has off-diagonal last line, its first row forces the larger break6>d>=24, impossible. Hence E1 has diagonal last line and its second row forces d=72. E2 diagonal last line forces d=24, while its off-diagonal last line forces the larger off-break66>d=72. These exhaust all possible last lines. No bounded search over unknown break sizes is used.',
        'B85 already gives dimW1>=3, so excluding3 forces W1=M2(F5); actual fifth powers then force W2=M2(F5). Order comparison inside the principal congruence kernel yields W=1+5M2(Z/125), of order5^8. The nonzero trace on W1 is the actual cyclotomic determinant modulo25 over the good field, so mu25 is absent from L and K. The full image is neither realized nor excluded; other residual sectors and the unrestricted least index remain undecided.'
    ],
    'primary_sources':[
        {
            'title':'Pierre Colmez, Corps locaux, notes du cours de M2',
            'url':'https://webusers.imj-prg.fr/~pierre.colmez/CL.pdf',
            'web_ref':'turn902110939view0',
            'retained_original_text':'agents/reduction_descent/sources/colmez_corps_locaux.txt',
            'retained_text_sha256':sha(author/'sources/colmez_corps_locaux.txt'),
            'actual_read_scope':'Original PDF freshly opened; its general complete-discrete-field definition and fixed-representative expansion read. Complete ramification filtration discussion and Proposition3.7 with the entire two-divisibility norm-polynomial proof on printedpp14-15 freshly read from the retained original text. No finite-residue assumption or new image-view claim.'
        }
    ],
    'additional_source_scope':'No fresh Serre original reading is claimed for this companion audit. The actual quotient formula is verified directly in the complete Colmez proof, and the tame-leading coefficient calculation is independently derived in the candidate.',
    'independent_program':str(copied.relative_to(root)),
    'independent_output':str(copied.with_suffix('.output.json').relative_to(root)),
    'independent_runtime_seconds':result['runtime_seconds'],
    'author_bytes_unchanged':True,
    'all_mathematical_output_identical':True,
    'hash_record':str(hash_path.relative_to(root)),
    'counts':result['counts'], 'finite_scope':result['scope'],
    'scope':'Only the p5/e20 tame reducible residual sector. It requires the full5^8 congruence image and excludes mu25 from the base, but supplies no existence or full recovery assertion.'
}
audit = own/'B87_independent_audit.json'
with audit.open('x') as f:
    json.dump(record,f,indent=2)
    f.write('\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now,label,'independent_full_proof_source_code_audit',
                           str(source.relative_to(root)),
                           'Complete fixed-coefficient, actual shared quotient and tame break proof; original quotient formula; literal isolated checker',
                           'PASS',str(audit.relative_to(root))])+'\n')
print(json.dumps({'status':record['status'],'actual_utc':now,
                  'record':str(audit.relative_to(root)),
                  'runtime_seconds':result['runtime_seconds'],'labels':labels}))
