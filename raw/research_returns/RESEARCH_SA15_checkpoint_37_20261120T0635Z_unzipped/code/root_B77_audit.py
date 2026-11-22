"""Record the first-wild finite-character audit and isolated exact rerun."""
from pathlib import Path
import datetime, hashlib, json, shutil, subprocess, sys
w=Path(__file__).resolve().parents[1]
candidate=w/'agents/reduction_descent/B_first_wild_finite_patterns_candidate.tex'
source=w/'agents/reduction_descent/code/verify_first_wild_finite_patterns.py'
author=source.with_suffix('.output.json')
dest=w/'outputs/root_B77_audit.json'
assert not dest.exists()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(candidate)=='4ba07b6ebed9e8d72c8a9520e68b1a070c7df4446d8fc9de078b9a5fba43824a'
before=sha(author)
snapshot=w/'code/audit_snapshots/B77_root_independent_certificate.py'
assert not snapshot.exists()
shutil.copy2(source,snapshot)
with (w/'outputs/root_B77_independent_certificate.stdout.txt').open('w') as stdout, (w/'outputs/root_B77_independent_certificate.stderr.txt').open('w') as stderr:
    run=subprocess.run([sys.executable,str(snapshot)],cwd=w,stdout=stdout,stderr=stderr)
assert run.returncode==0
a=json.loads(author.read_text())
b=json.loads(snapshot.with_suffix('.output.json').read_text())
omit={'runtime_seconds','actual_utc'}
assert {k:v for k,v in a.items() if k not in omit}=={k:v for k,v in b.items() if k not in omit}
assert before==sha(author) and sha(source)==sha(snapshot)
data={
 'status':'FULL PROOF, INTERNAL DEPENDENCY AND EXACT CERTIFICATE PASS',
 'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'candidate_sha256':sha(candidate),
 'checks':{
  'lem:B-RD77-kernel':'Fresh complete B64 weighted-kernel and B50 closed-boundary proofs reread. The unweighted invariant-differential identity forces p-divisibility when any monomial exponent is prime to p. All remaining nonlinear degrees below p squared have positive uniformizer valuation by the actual target special fibre. Thus the minimum is min(a+q,1+pq), and the normalized logarithm inequality is coefficientwise valid at the closed threshold. The bounded projection, integral Cartier action, source intersection and special-kernel saturation argument apply exactly as in the fully stated B64 proof. No source thickness is transferred to a quotient.',
  'prop:B-RD77-square':'A simultaneous actual finite scalar twist kills the common square norm and preserves the actual torsion comparison and inequality of special characters. Both good degrees then divide p+1 at arbitrary absolute index. Disjoint norm-one Frobenius orbits give a tame integral projector. Perfect actual BT pairings and self-orthogonality give exactly ker(F^3) in each factor of the graph closure. The graph-plus-projection map has zero generic kernel and target special fibre a product of three actual height-two groups. For a=p(p-1)m, m dividing p+1, q1=p+1 and both entries of q2=min(a+p+1,p squared+p+1) are at least a/(p-1). The image of F squared on ker(F cubed) has rank p, giving the contradiction. The m=1 minimum is explicitly retained.',
  'cor:B-RD77':'B76 actual dimension detection applies at n=3,v_p(e)=1 and excludes mixed comparisons because e=p(p-1)<=p squared. B63 actual level-two lower examples give index at least2. At n=4 the complete B64 weighted recurrence on the actual quotient gives q3=2p cubed-1>p(p squared-1), hence index at most3. The procyclic square-class normalization and primitive norm fibre calculation use no tame absolute-index restriction. At p5, distinct normalized orbits A,B,C all have joint degree24; the simultaneous quadratic twist fixes B and swaps A,C, giving pairs AB and AC only. No actual congruence realizing a pair is inferred.',
  'rem:B-RD77-scope':'Complete exact code read and unchanged independent rerun performed. All mathematical output fields match; author output is unchanged. The arithmetic certificate does not prove geometric existence or an exact least index at the first wild ramification.'},
 'independent_runtime_seconds':b['runtime_seconds'],
 'counts':b['counts'],
 'program_sha256':sha(source),
 'author_output_sha256':before,
 'author_output_unchanged':True,
 'all_mathematical_fields_equal_author':True,
 'source_scope':'Fresh complete internal B64 and B50 proofs read; B76 audited earlier this checkpoint. Previously fully audited original Bondarko and Tate passages are reused, with no fresh original-source read claimed.',
 'scope_limit':'Only the square finite-determinant branch is eliminated at actual p cubed torsion. The remaining normalized nonsquare AB/AC cases at p5,e20 remain open, and the least-index interval is {2,3}.'}
dest.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
