"""Literal isolated rerun and retained complete proof audit of OC's Moore theorem."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil, subprocess, sys

own=Path(__file__).resolve().parents[1]
work=own.parents[1]
src=work/'agents/obstructions_crystals/post_CP30_Moore_singular_parameter_classification_candidate.tex'
program=work/'agents/obstructions_crystals/code/verify_Moore_singular_parameter_classification.py'
author_out=program.with_suffix('.output.json')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source_before,code_before,out_before=sha(src),sha(program),sha(author_out)
assert source_before=='234608ae83437e80577d715b17f43bcc075c8fef479d444e2c2cf52c1a343067'
dest=own/'outputs/independent_Moore_classification_run'
dest.mkdir(exist_ok=False)
copied=dest/program.name
shutil.copy2(program,copied)
assert sha(copied)==code_before
run=subprocess.run([sys.executable,str(copied)],cwd=dest,capture_output=True,text=True)
(dest/'stdout.txt').write_text(run.stdout)
(dest/'stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
result=json.loads(copied.with_suffix('.output.json').read_text())
author=json.loads(author_out.read_text())
ignore={'actual_utc','runtime_seconds'}
assert {k:v for k,v in result.items() if k not in ignore}=={k:v for k,v in author.items() if k not in ignore}
assert (sha(src),sha(program),sha(author_out))==(source_before,code_before,out_before)
labels=re.findall(r'\\label\{([^}]+)\}',src.read_text())
stamp=datetime.now(timezone.utc).isoformat()
record={
 'status':'FULL_INDEPENDENT_PROOF_AND_EXACT_CODE_AUDIT_PASS', 'actual_utc':stamp,
 'source':str(src),'source_sha256':source_before,'labels':labels,'complete_read':True,
 'program':str(program),'program_sha256':code_before,
 'author_output':str(author_out),'author_output_sha256':out_before,
 'author_bytes_preserved':True,'isolated_program':str(copied),
 'independent_output':str(copied.with_suffix('.output.json')),
 'independent_runtime_seconds':result['runtime_seconds'],
 'all_mathematical_output_equal':True,'counts':result['counts'],
 'proof_checks':[
  'All9! signed determinant terms reduce to unsigned terms in characteristic2. Four-bit exponent packing is exact because every coordinate exponent is at most9; parity cancellation reconstructs the entire universal coefficient table.',
  'Every excluded exact support has a retained single-monomial coefficient, hence is excluded over any algebraically closed characteristic2 field. The111 survivors are exactly the four affine orbits; covariance is a literal row/column/variable permutation.',
  'The two- and four-support cube-factor identities force character ratios. For six-support, the full cyclic matching lemma was independently rederived in the perfect-matching, rectangle and star cases; nonzero product is essential in the star case. Its reflection plus product phases gives the stated affine character about an actual missing center.',
  'On eight-support, the four uniform coefficient binomials force cube-root phases; all81 phases are substituted into polynomial coefficients with the independent d variables retained. Each72 noncharacter phase has an everywhere nonzero monomial witness, so this is not a finite-point inference.',
  'For each of the81 spaces, exact row scaling gives a symmetric matrix with zero diagonal in odd dimension. Distinct missing centers and distinct linear characters make all81 four-dimensional vector spaces distinct.',
  'Scheme structure and actual Cartier/geometric identifications are explicitly excluded. The prior forty-product shortcut is retained as rejected and is not used.'
 ],
 'source_scope':'No external classification theorem invoked or new literature read claimed; universal determinant and elementary finite-group/field algebra were checked directly.',
 'rerun_scope':'Literal unchanged complete author program rerun in a new isolated directory; its complete output and both streams retained. This is not represented as a separately written determinant implementation.'
}
(own/'outputs/independent_Moore_classification_audit.json').write_text(json.dumps(record,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 for label in labels:
  f.write('\t'.join((stamp,label,'FULL_INDEPENDENT_AUDIT_PASS','Complete Moore universal determinant/support/phase/matching proof and entire exact checker read; literal isolated run matches all mathematical data.','outputs/independent_Moore_classification_audit.json','No actual Cartier identification or new surface-rank assertion'))+'\n')
print(json.dumps({'status':record['status'],'actual_utc':stamp,'runtime_seconds':result['runtime_seconds'],'counts':result['counts'],'author_preserved':True},indent=2))
