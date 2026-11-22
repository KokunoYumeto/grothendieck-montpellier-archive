"""Record the complete root B72 proof audit and rerun its exact supplement."""
from pathlib import Path
import csv, datetime, hashlib, json, subprocess, sys
w=Path(__file__).resolve().parents[1]
c=w/'agents/reduction_descent/B_first_level_mixed_boundary_candidate.tex'
assert hashlib.sha256(c.read_bytes()).hexdigest()=='d903ca018de6ac14e0bffa767ce664f0589b04448d0135a5c63404ca2832548c'
s=w/'agents/reduction_descent/code/verify_first_level_mixed_boundary.py'
a=s.with_suffix('.output.json'); before=a.read_bytes()
snap=w/'code/audit_snapshots/B72_root_independent_certificate.py'
out=w/'outputs/root_B72_audit.json'
assert not snap.exists() and not out.exists()
snap.write_bytes(s.read_bytes())
r=subprocess.run([sys.executable,str(snap)],capture_output=True,text=True)
(w/'outputs/root_B72_independent_certificate.stdout.txt').write_text(r.stdout)
(w/'outputs/root_B72_independent_certificate.stderr.txt').write_text(r.stderr)
assert r.returncode==0,r.stderr
fresh=json.loads(snap.with_suffix('.output.json').read_text()); old=json.loads(before)
omit={'actual_utc','elapsed_seconds'}
assert {k:v for k,v in fresh.items() if k not in omit}=={k:v for k,v in old.items() if k not in omit}
assert fresh['status']=='PASS' and a.read_bytes()==before
(w/'outputs/root_B72_independent_certificate.json').write_text(json.dumps(fresh,indent=2)+'\n')
checks={
 'lem:B-RD72-first-mixed':'Complete first-level proof checked: the actual prime parameter yields a cyclic degree-p common division field and unique wild high line. The exact prime lower break and strict divisible-valuation bound in that SAME field force Cprime>Cdiv. No second-level representation is used.',
 'prop:B-RD72-mixed-quotients':'Actual p3 isomorphism descends to p2 after the first high subgroup quotient, with intrinsic marked low line. The nontrivial tame eigenvalue ratio forces the complementary high lines to correspond. The second quotient retains exactly p-torsion and has parameters p^3 b1 and s-p^2 b2. The first-level mixed rule gives the stated strict necessary inequality; no sufficiency or existence is asserted.',
 'prop:B-RD72-common-high':'At e=2(p^2-1), common norm gives b1 congruent b2 modulo p-1. The separated-high proof excludes minimum at least2. The pair {1,p} gives Frobenius-conjugate tame characters. The only remaining pair {1,2p-1} has second parameters p^3 and 3p^2-2p-2 in the wrong strict order, since their positive difference is p(p-1)(p-2)+2.',
 'prop:B-RD72-formal':'The tame cases retain e<2p^2<p^3. Mixed p-divisibility uses the common primitive point field inequality. Both small p^2-divisible parameters must equal p^2, and exchanged high lines would require p-1 dividing2, impossible for p>=5. One-slope and mixed-polygon cases retain the audited B69 reduction.',
 'thm:B-RD72':'The full filtered monodromy argument uses the audited B63 distinction of whole versus filtered representations for e<p^3, the determinant dimensions, and the now exhaustive formal comparison. The p2 lower example applies. Thus the manuscript index is exactly2 for p>=5 and e=2(p^2-1), extending the B71 sector to2<=t<=2p+2 with p not dividingt.',
 'rem:B-RD72-scope':'Entire final proof, entire exact program, candidate record and output scope read. The independent rerun matches every mathematical output field and preserves author output bytes. This is an all-prime proof with finite supplement, not an inference from the twelve tested primes. Other ramification sectors and higher heights remain open.'}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 writer=csv.writer(f,delimiter='\t')
 for label,detail in checks.items():
  writer.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15','targeted proof check','PASS. '+detail])
record={'status':'FULL ALL-PRIME PROOF AND EXACT-CERTIFICATE PASS','actual_utc':now,'candidate':str(c.relative_to(w)),'candidate_sha256':hashlib.sha256(c.read_bytes()).hexdigest(),'checks':checks,'independent_runtime_seconds':fresh['elapsed_seconds'],'counts':fresh['counts'],'author_output_sha256':hashlib.sha256(before).hexdigest(),'author_output_unchanged':True,'all_mathematical_output_equals_author_output':True,'source_scope':'Fresh B60 and B69 proof rereads in the immediately preceding B71 audit reused, together with previously checked B63 full filtered reduction; no fresh external source read claimed.'}
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='checks'},indent=2))
