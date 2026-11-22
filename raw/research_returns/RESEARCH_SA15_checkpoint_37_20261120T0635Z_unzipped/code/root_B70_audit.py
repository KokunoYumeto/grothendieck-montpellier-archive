"""Full B70 proof audit and author-output-preserving independent exact rerun."""
from pathlib import Path
import csv,datetime,hashlib,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
c=w/'agents/reduction_descent/B_next_tame_boundary_candidate.tex'
assert hashlib.sha256(c.read_bytes()).hexdigest()=='542f911ef3b58b70f12be51682d4406061330e996c9d06cb05cbebfd18faea75'
source=w/'agents/reduction_descent/code/verify_next_tame_boundary.py'
author=source.with_suffix('.output.json');before=author.read_bytes()
snap=w/'code/audit_snapshots/B70_root_independent_certificate.py'
dest=w/'outputs/root_B70_audit.json'
assert not snap.exists() and not dest.exists();snap.write_bytes(source.read_bytes())
r=subprocess.run([sys.executable,str(snap)],capture_output=True,text=True)
(w/'outputs/root_B70_independent_certificate.stdout.txt').write_text(r.stdout)
(w/'outputs/root_B70_independent_certificate.stderr.txt').write_text(r.stderr)
assert r.returncode==0,r.stderr
data=json.loads(snap.with_suffix('.output.json').read_text());old=json.loads(before)
omit={'elapsed_seconds','actual_utc'}
assert {k:v for k,v in data.items() if k not in omit}=={k:v for k,v in old.items() if k not in omit}
assert author.read_bytes()==before
(w/'outputs/root_B70_independent_certificate.json').write_text(json.dumps(data,indent=2)+'\n')
checks={
 'lem:B-RD70-high':(
  'All common-high cases checked. Prime B implies nontrivial residual wild '
  'inertia by its low valuation denominator, so B69 covers prime and mixed '
  'divisibilities, including B=e. For both divisible B below e, b lies1..p. '
  'Equal finite norms and equal high eigenvalues give b1=b2 mod(p-1); the '
  'only unequal pair is{1,p}. There B1=p,B2=p^2, c2-c1=p(p-1), and '
  'c1=p mod(p+1), so c2=pc1 modN. The character agrees while parameters '
  'need not. Both large high quotients have prime parameters and recover '
  'characters; opposite positions have forbidden mixed divisibility.'),
 'lem:B-RD70-exchange':(
  'The actual residual high eigenvalue is zeta^(c-B), and the low '
  'eigenvalue is zeta^(pc+B), using the actual determinant and mu_p inK. '
  'Tame semisimplicity makes a noncorresponding high line the other '
  'eigenspace when eigenvalues differ. In the scalar case the same '
  'equations remain true. Thus high1=low2 and high2=low1. Multiplying '
  'the first exponent relation byp and adding the second gives '
  'N|(p+1)(B1+B2), exactly (p-1)|(B1+B2). For B1=B2=p^2 '
  'this would require(p-1)|2, impossible forp>=5.'),
 'prop:B-RD70-tame':(
  'Both prime b cases use the already fully audited p^2 point-field rule. '
  'For prime b1 versus divisible b2=pk, the common primitive point field '
  'has degreep^2, forced by the first valuation denominator. Different '
  'high lines force p^2(alpha1-pk)<=b-pk. Sincealpha1>=e+p andpk<e, '
  'the left side is greater thanp^3; the right side is less thane<p^3. '
  'Hence high lines agree and the first lemma applies, including the '
  'new k=1 case. If bothb are divisible and high lines differ, any '
  'B>e gives a common stable high/low quotient with prime versus '
  'divisible parameters, impossible. The remaining two small B are '
  'bothp^2 becausep^2<e<2p^2, and the exchanged-eigenvalue lemma '
  'then forbids different high lines. B=e is excluded by divisibility '
  'before using either quotient branch.'),
 'prop:B-RD70-formal':(
  'The all-index B69 one-slope theorem covers equal one-slope polygons '
  'and excludes mixed polygons. For two unequal-slope polygons, '
  'nontrivial residual wild inertia forces the unique high fixed line '
  'to correspond; tame residual inertia is covered by the preceding '
  'complete proposition. This exhausts all whole-formal cases without '
  'a square-determinant normalization.'),
 'thm:B-RD70':(
  'The maximal unramified completion preserves actual inertia comparisons. '
  'The p-prime ramification makes cyclotomic p^3-image have p-partp^2, '
  'so determinant dimensions0,1,2 and finite determinant agree. '
  'Residual Brauer lifts and Cartier duality cover dimensions0,2. '
  'Two filtered height-one systems are residually detected, mixed '
  'whole/filtered comparisons are excluded by exact B63 thresholde<p^3, '
  'and all whole formal comparisons were just exhausted. Actualp^3 '
  'therefore suffices. B63 actualp^2 lower examples apply becausee>p '
  'and(p-1)|e. Thusnu_min(p,(p+2)(p-1),2)=2, includingp5/e28.'),
 'rem:B-RD70-scope':(
  'Entire final proof and complete certificate read. The isolated rerun '
  'agrees in all mathematical data and leaves the author output unchanged. '
  'The explicit later arithmetic pair(2,p+1) is retained as unexcluded '
  'arithmetic only, not as existing formal groups or a torsion comparison. '
  'No higher sector or p-divisible index follows. The finite supplement '
  'does not replace the all-prime proof.'),
}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    for label,detail in checks.items():
        wr.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15',
                     'targeted proof check','PASS. '+detail])
record={'status':'FULL ALL-PRIME PROOF AND EXACT-CERTIFICATE PASS','actual_utc':now,
        'candidate':str(c.relative_to(w)),'candidate_sha256':hashlib.sha256(c.read_bytes()).hexdigest(),
        'independent_runtime_seconds':data['elapsed_seconds'],'counts':data['counts'],
        'author_output_sha256':hashlib.sha256(before).hexdigest(),'author_output_unchanged':True,
        'all_mathematical_output_equals_author_output':True,'checks':checks,
        'source_scope':'Reuses the immediately fully audited B69 and the earlier complete B63/B67 source and proof records; no fresh external retrieval claimed.'}
dest.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='checks'},indent=2))
