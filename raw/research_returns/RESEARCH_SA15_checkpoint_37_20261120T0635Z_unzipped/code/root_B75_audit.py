"""Retain root's full B75 read and an isolated author-preserving exact rerun."""
from pathlib import Path
import datetime,hashlib,json,shutil,subprocess,sys
w=Path(__file__).resolve().parents[1]
candidate=w/'agents/reduction_descent/B_terminal_frobenius_pair_candidate.tex'
source=w/'agents/reduction_descent/code/verify_terminal_frobenius_pair.py'
author=source.with_suffix('.output.json')
dest=w/'outputs/root_B75_audit.json';assert not dest.exists()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(candidate)=='5475144072763f8e9869ac63030d9b550f5eaf507428ded08cc50dc08879a4ff'
before=sha(author)
snapshot=w/'code/audit_snapshots/B75_root_independent_certificate.py'
assert not snapshot.exists();shutil.copy2(source,snapshot)
with (w/'outputs/root_B75_independent_certificate.stdout.txt').open('w') as stdout, (w/'outputs/root_B75_independent_certificate.stderr.txt').open('w') as stderr:
    run=subprocess.run([sys.executable,str(snapshot)],cwd=w,stdout=stdout,stderr=stderr)
assert run.returncode==0
a=json.loads(author.read_text());b=json.loads(snapshot.with_suffix('.output.json').read_text())
omit={'elapsed_seconds','actual_utc','program_sha256'}
assert {k:v for k,v in a.items() if k not in omit}=={k:v for k,v in b.items() if k not in omit}
assert before==sha(author) and sha(source)==sha(snapshot)
data={'status':'FULL PROOF AND EXACT CERTIFICATE PASS',
      'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'candidate_sha256':sha(candidate),
      'checks':{
       'lem:B-RD75-terminal':'Complete all-prime calculation rederived: the common determinant and high character give b congruence modulo p-1 and c2-c1=p(b2-b1) modulo N. B69.2 gives c_i=pb_i modulo p+1 from the Fp-valued high character; its complete local derivation was freshly reread. On1..p only the unequal pair1,p remains. Multiplying c1=p modulo p+1 by p-1 gives c2=pc1 modulo N, preserving the exact unordered eigenvalue multiset even if it has multiplicity. No equality of parameters is claimed.',
       'prop:B-RD75-formal':'Entire B74 proof reread in this audit. Its alignment, marked low line, finite-flat quotients, prime-parameter and mixed tame/wild stopping cases do not use the terminal e bound. Actual level n-j remains at least2 when aligning, and only1 remains at the final comparison. The enlarged bound gives b<p+1; the preceding original-character calculation closes the extra pair. This is a whole-formal result for n>=3.',
       'thm:B-RD75':'Full filtered bound correctly restricted to n>=4. Then p^(n-1)(p+1)<p^(2n-3), so the already audited mixed threshold is excluded; determinants and height-one cases are unchanged. Upper n4 with actual p3 lower examples gives exact index3 on p3<e<p3(p+1), with prime-to-p ramification and all stated hypotheses. Atp5 the permitted endpoints128,748 and next752 are correct.',
       'rem:B-RD75-scope':'The next abstract pair2,p+1 genuinely can have different unordered characters, but no actual torsion comparison is constructed. Entire program read and exact rerun preserves all author data and matches mathematical fields. The n3 formal/full counter-scope witness prevents an incorrect index2 extension. No fresh external theorem, source read, or finite-to-uniform existence inference is claimed.'},
      'independent_runtime_seconds':b['elapsed_seconds'],
      'counts':b['counts'],'program_sha256':sha(source),
      'author_output_sha256':before,'author_output_unchanged':True,
      'all_mathematical_fields_equal_author':True,
      'checkpoint_scope':'Audited after the CP27 paper freeze. This candidate and audit remain outside its frozen PDF and current outcome table; any canonical promotion belongs to subsequent integration.'}
dest.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))
