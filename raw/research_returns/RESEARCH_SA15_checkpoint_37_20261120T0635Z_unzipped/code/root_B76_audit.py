"""Record the complete wild-index proof audit and isolated exact certificate."""
from pathlib import Path
import datetime,hashlib,json,shutil,subprocess,sys
w=Path(__file__).resolve().parents[1]
candidate=w/'agents/reduction_descent/B_wild_cyclic_point_candidate.tex'
source=w/'agents/reduction_descent/code/verify_wild_cyclic_point.py'
author=source.with_suffix('.output.json')
dest=w/'outputs/root_B76_audit.json';assert not dest.exists()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(candidate)=='200539e96e129979c28c346f503143dbd45f9e4b8ebc949cbca0451bb96b9a93'
before=sha(author)
snapshot=w/'code/audit_snapshots/B76_root_independent_certificate.py'
assert not snapshot.exists();shutil.copy2(source,snapshot)
with (w/'outputs/root_B76_independent_certificate.stdout.txt').open('w') as stdout, (w/'outputs/root_B76_independent_certificate.stderr.txt').open('w') as stderr:
    run=subprocess.run([sys.executable,str(snapshot)],cwd=w,stdout=stdout,stderr=stderr)
assert run.returncode==0
a=json.loads(author.read_text());b=json.loads(snapshot.with_suffix('.output.json').read_text())
omit={'runtime_seconds','actual_utc'}
assert {k:v for k,v in a.items() if k not in omit}=={k:v for k,v in b.items() if k not in omit}
assert before==sha(author) and sha(source)==sha(snapshot)
data={'status':'FULL PROOF, DEPENDENCY AND EXACT CERTIFICATE PASS',
 'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'candidate_sha256':sha(candidate),
 'checks':{
  'lem:B-RD76-point':'All five branches independently derived from the freshly reread complete B63 Newton/inverse-polygon proof and B49 integral coefficient derivation. Every successive rational valuation is integral. The high recurrence gives a=p^j(b+(p-1)Z_j), hence j<=v_p(a). The uniform stopping bound is a>=N p^(2n-3-j); equality at j=v forces a different valuation because j<=n-2. The low step uses the strict opposite inequality, and the all-high bound a>=p^n is strictly stronger. Initial low and one-slope branches are explicitly exhausted, including b infinity and Newton equality. Negative right-hand exponents are interpreted rationally.',
  'prop:B-RD76-mixed':'Fresh full B49 finite subgroup, actual quotient and finite-twist construction read, together with complete B63 mixed proof. None of the steps constructing a rational point of order p^n uses prime-to-p absolute index. B49 tame-inertia proof is stated for arbitrary e: finite subgroup of height-two division-algebra units embeds in F_(p2)^*, and the fully audited actual-lattice descent supplies good degree m dividingN. The point extends into the connected formal special fibre. Since v_p(me)=v_p(e), dividing the new necessary point bound by m<=N gives the stated strict mixed inequality.',
  'lem:B-RD76-determinant':'The completed unramified base preserves e and gives algebraically closed residue. Primitive cyclotomic difference valuation is e p^r/[p^(n-1)(p-1)], so integrality forces r>=n-1-v. With n>=v+2 the image has nontrivial p-part. Since the finite determinant is mu_(p-1)-valued and total dimensions differ by at most2<p, the dimensions agree; residual reduction then identifies the finite determinant. No unjustified exact cyclotomic degree is claimed at wild e.',
  'cor:B-RD76':'The full filtered classification is rechecked: dimensions0/2 are residual and dual cases; two height-one filtered dimension1 groups are residual because mu_p is present. The new inequality excludes only the mixed whole/filtered case. Atp5,e20,v1,n3,20<=25 andn=v+2 hold, leaving exactly the two-whole-potentially-supersingular comparison. No upper index2 theorem is inferred.',
  'rem:B-RD76-scope':'Entire finite program read. The exact Fraction branches and all integer equality/degree/cyclotomic checks are numerical necessary conditions only. Independent unchanged-program rerun reproduces all mathematical fields and preserves author output. All five finite modes occur. The source chain uses previously audited original Hopkins-Gross statements; no new original-source read or formal-group existence claim is made.'},
 'independent_runtime_seconds':b['runtime_seconds'],
 'counts':b['counts'],'terminal_modes':b['terminal_modes'],
 'program_sha256':sha(source),'author_output_sha256':before,
 'author_output_unchanged':True,'all_mathematical_fields_equal_author':True,
 'source_scope':'Fresh complete internal B49 coefficient/tame-inertia/quotient/twist/determinant and B63 Newton/mixed proofs read; previously audited original source passages reused without a fresh-read claim.',
 'scope_limit':'This shrinks the wild p5/e20 comparison gate, but does not recover the remaining whole-formal character or determine its exact least index.'}
dest.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))
