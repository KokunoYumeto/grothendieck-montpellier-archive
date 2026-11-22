"""Retain an unchanged, isolated rerun after a complete independent proof/code read."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,subprocess,sys,time,csv

agent=Path(__file__).resolve().parents[1];work=agent.parents[1]
other=work/'agents/obstructions_crystals'
proof=other/'post_CP30_Moore_singular_parameter_classification_candidate.tex'
expected='234608ae83437e80577d715b17f43bcc075c8fef479d444e2c2cf52c1a343067'
source=other/'code/verify_Moore_singular_parameter_classification.py'
author=source.with_suffix('.output.json')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(proof)==expected
before={str(p.relative_to(work)):sha(p) for p in [proof,source,author]}
dest=agent/'outputs/independent_Moore_singular_parameters';assert not dest.exists();dest.mkdir()
copied=dest/source.name;copied.write_bytes(source.read_bytes())
start=time.perf_counter()
run=subprocess.run([sys.executable,str(copied)],cwd=dest,capture_output=True,text=True,timeout=60)
wall=time.perf_counter()-start
(dest/'stdout.txt').write_text(run.stdout);(dest/'stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
result=json.loads(copied.with_suffix('.output.json').read_text())
expected_result=json.loads(author.read_text())
math=lambda d:{k:v for k,v in d.items() if k not in ('actual_utc','runtime_seconds')}
assert math(result)==math(expected_result)
after={str(p.relative_to(work)):sha(p) for p in [proof,source,author]}
assert before==after
now=datetime.now(timezone.utc).isoformat()
labels=['lem:DE-Moore-support','lem:DE-Moore-six-matching','thm:DE-Moore-singular-parameters','rem:DE-Moore-classification-scope']
record={'status':'PASS','actual_utc':now,'auditor':'monodromy','proof':str(proof.relative_to(work)),'proof_sha256':expected,'labels':labels,
 'source_and_author_output_hashes_before':before,'source_and_author_output_hashes_after':after,
 'unchanged_isolated_runtime_seconds':result['runtime_seconds'],'external_wall_seconds':wall,'isolated_directory':str(dest.relative_to(work)),
 'complete_read_scope':'Entire candidate and entire standalone checker read; all support, factor, matching, phase and sufficiency arguments independently rederived before the isolated run.',
 'checks':['Four-bit exponent encoding is safe because both total degrees equal9; the complete362880 permutation parity reconstruction is exact.',
 'All400 support exclusions are literal nonzero monomial coefficients on the corresponding coordinate torus; affine covariance reaches precisely the111 remaining supports.',
 'All eight coefficient factorizations, four opposite-cube binomials and all81 root-of-unity phase cases are polynomial identities, not sampling.',
 'The six-support matching proof covers all27 edge choices; its nonzero-product and characteristic-two square-root steps are valid.',
 'The direct row permutation and character scaling gives an alternating odd matrix on each of81 planes, including smaller supports.',
 'Different missing centers and different character ratios give81 distinct projective3-spaces.',
 'Set-theoretic scope and the rejected40-basis shortcut are explicit; no scheme-ideal equality or Cartier identification is inferred from this classification alone.'],
 'source_scope':'No external theorem is required for this direct algebraic classification; no fresh external source access claimed.',
 'counts':result['counts'],'all_mathematical_output_equal_to_author':True}
out=agent/'outputs/independent_Moore_singular_parameter_audit.json';assert not out.exists();out.write_text(json.dumps(record,indent=2)+'\n')
with (agent/'CHECK_EVENTS_post_CP16.tsv').open('a',newline='') as f:
 writer=csv.writer(f,delimiter='\t')
 for label in labels:writer.writerow([label,now,'/root/monodromy','PASS-independent-full-proof-code',str(out.relative_to(agent))])
print(json.dumps({k:record[k] for k in ['status','actual_utc','proof_sha256','unchanged_isolated_runtime_seconds','all_mathematical_output_equal_to_author','counts']},indent=2))
