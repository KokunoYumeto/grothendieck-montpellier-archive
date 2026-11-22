"""Retain the complete all-prime B69 proof audit and author-preserving exact rerun."""
from pathlib import Path
import csv, datetime, hashlib, json, subprocess, sys
w=Path(__file__).resolve().parents[1]
candidate=w/'agents/reduction_descent/B_one_slope_quotient_candidate.tex'
assert hashlib.sha256(candidate.read_bytes()).hexdigest()=='d43b8cd138f2a854caedb5b92da4dfc37bc0c5aad11a004320fbdc39b2de2f17'
source=w/'agents/reduction_descent/code/verify_one_slope_boundary.py'
author=source.with_suffix('.output.json')
before=author.read_bytes()
snap=w/'code/audit_snapshots/B69_root_independent_certificate.py'
dest=w/'outputs/root_B69_audit.json'
assert not snap.exists() and not dest.exists()
snap.write_bytes(source.read_bytes())
run=subprocess.run([sys.executable,str(snap)],capture_output=True,text=True)
(w/'outputs/root_B69_independent_certificate.stdout.txt').write_text(run.stdout)
(w/'outputs/root_B69_independent_certificate.stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
data=json.loads(snap.with_suffix('.output.json').read_text())
old=json.loads(before);omit={'elapsed_seconds','actual_utc'}
assert {k:v for k,v in data.items() if k not in omit}=={k:v for k,v in old.items() if k not in omit}
assert before==author.read_bytes()
(w/'outputs/root_B69_independent_certificate.json').write_text(json.dumps(data,indent=2)+'\n')
checks={
 'lem:B-RD69-rules':(
  'The entire point-field argument was rederived without nonsquare normalization. '
  'The high line has Fp character and is L-rational, so its integral valuation gives '
  'integer B, slopes s-B,B/p, 0<B<pe and high character zeta^(c-B). All inverse '
  'low points have valuation B/p^3. Over the common wild degree-p field R, '
  'the exact break for prime B is ps-(p+1)B and the divisible case is strictly '
  'smaller, by fixed coefficient representatives. Mixed divisibility first forces '
  'B1>B2. The common primitive point field is a torsor under R-rational p-torsion, '
  'and the first valuation denominator forces degree p^2. A low translation '
  'then gives p^2 B2>=B2+N B1, the opposite inequality. In the tame case, '
  'two prime b=B/p similarly give equal b; a high-only translation excludes '
  'different high lines. No parity assumption occurs.'),
 'lem:B-RD69-quotients':(
  'The actual rank-p quotient coordinate is a unit times the product over its '
  'kernel; all valuation sums and multiplicities were independently checked. '
  'The old high formulas pB and s-B are retained, with B=e treated separately: '
  'the high-target inverse vertices are collinear of slope -e/p, hence the '
  'quotient has q-1 points of valuation e and one slope. A one-slope original '
  'has all q-1 points of valuation e. Its p-1 nonzero residual quotient classes '
  'have valuation pe, and the q-p classes above nonzero kernel targets have '
  'valuation e/p, since inverse roots have valuation e/q. Thus its parameter '
  'is exactly Bnew=e. The low quotient still has B/p. The special order-p '
  'subgroup is kerF, so quotient tangent exponent pc preserves {c,pc}. '
  'Tate full faithfulness extends actual semilinear descent to the schematic '
  'kernel and quotient; only the generic quotient is descended through the '
  'ramified extension. The exact p^2 group {P in M[p^3]:p^2 P in J}/J '
  'retains both lattice and actual Galois action.'),
 'prop:B-RD69-one-slope':(
  'Leading coefficients of T/pi_L^e inject the entire first-level Fp plane: '
  'a nonzero difference is again p-torsion of valuation e, so leading terms '
  'cannot coincide. Inertia over L fixes all leading coefficients and hence '
  'all p-torsion. Tame multiplication is lambda=zeta^(c+e) on this plane. '
  'An invariant Fp line forces lambda in Fp, so reducible means scalar. '
  'A comparison with a two-slope group is therefore scalar and has p|B. '
  'Transport its actual stable high line and quotient the p^3 comparison. '
  'Parameters are e and pB when B<e, a forbidden mixed divisibility, or '
  'e and s-B when B>e, whose necessary equality forces B=pe. The critical '
  'B=e is impossible since p|B but p does not divide e. For two one-slope '
  'groups the irreducible case uses the fully audited B67, while equal actual '
  'scalars identify c directly in the reducible case. This exclusion imposes '
  'no e<p^2 hypothesis.'),
 'prop:B-RD69-two-slope':(
  'The actual determinant comparison identifies the finite norm character, '
  'hence c1=c2 mod(p-1), without a square-class twist. All prime or mixed B '
  'cases, including B=e, are handled before quotienting. For both small '
  'divisible B, b=B/p lies in {1,...,p-1}, on which reduction mod(p-1) '
  'is injective; equal high characters and norms imply equal b and c. '
  'Both large high quotients have prime parameters; opposite sides give '
  'forbidden mixed divisibility. In the tame case, two prime b are covered. '
  'A prime b versus pk has B2=p^2 k>e. Distinct high lines force '
  'p^2(alpha1-pk)<=b-pk, while alpha1>=e+p,pk<e and e<p^2 give '
  'left side>p^3 and right side<p^2. The common high quotient then excludes '
  'both parameter positions. Two divisible b either give two prime high '
  'quotients or, with distinct high lines, a stable high/low pair of opposite '
  'quotient divisibility. All cases are exhaustive; B=e is never silently '
  'treated by a two-slope quotient formula.'),
 'thm:B-RD69':(
  'Completion of the maximal unramified base preserves inertia and e. '
  'For height two, determinant chi_p^d epsilon has d in {0,1,2}. The '
  'cyclotomic p-part modulo p^3 has order p^2 when p does not divide e, '
  'so actual comparison separates d and then epsilon. Dimension zero '
  'is the residual Brauer case, dimension two its Cartier dual. In '
  'dimension one, filtered height-one pairs are detected residually, '
  'mixed whole/filtered pairs are excluded by B63 since e<p^2<p^3, '
  'and the two whole cases are exhausted above. This proves the full '
  'monodromy upper bound at every allowed e<p^2. At e=p^2-1>p '
  'the previously fully audited B63 n=2 construction supplies actual '
  'p^2 ambiguity, so the least manuscript index is exactly2.'),
 'rem:B-RD69-scope':(
  'The full exact program and current final candidate were read. The root '
  'copied source byte for byte and reran it without touching the author '
  'output. All mathematical records agree. The finite Newton, quotient '
  'multiplicity, tame-weight and branch-inequality checks supplement '
  'the symbolic all-prime proof; they are not an existence test. '
  'No p-divisible e or e>=p^2 two-slope recovery is asserted.'),
}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for label,detail in checks.items():
        writer.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15',
                         'targeted proof check','PASS. '+detail])
record={'status':'FULL ALL-PRIME PROOF AND EXACT-CERTIFICATE PASS','actual_utc':now,
        'candidate':str(candidate.relative_to(w)),
        'candidate_sha256':hashlib.sha256(candidate.read_bytes()).hexdigest(),
        'independent_runtime_seconds':data['elapsed_seconds'],'counts':data['counts'],
        'author_output_sha256':hashlib.sha256(before).hexdigest(),
        'author_output_unchanged':True,'all_mathematical_output_equals_author_output':True,
        'checks':checks,
        'source_scope':'Previously fully audited B49 Newton/inertia, B60 break, B63 actual threshold/construction, B67 and B68 dependencies are reused. No new external source retrieval is claimed.',
        'publication_scope':'Audit completed after CP25 PDF freeze; integration/promotion is a separate subsequent action.'}
dest.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
