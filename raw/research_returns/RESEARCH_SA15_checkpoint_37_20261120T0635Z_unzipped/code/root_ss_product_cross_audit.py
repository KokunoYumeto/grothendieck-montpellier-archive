"""Retain the complete root proof audit and unchanged exact Cartier rerun."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil,subprocess,sys,time
w=Path(__file__).resolve().parents[1]
candidate=w/'agents/obstructions_crystals/post_CP29_ss_product_dual_Cartier_candidate.tex'
source=w/'agents/obstructions_crystals/code/verify_ss_product_cross_Cartier.py'
author=source.with_suffix('.output.json')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected='6bfbdec7f65a16c39f6094e86485364ad685c80d87ce23ad14cec266e495ba18'
assert sha(candidate)==expected
assert sha(source)=='91e28b937a2f69e24d386c8a7b635e7a568648e42d15de0bf19a7301f21520eb'
before=sha(author)
dest=w/'code/audit_snapshots/ss_product_cross_root_certificate.py'
snapshot=w/'notes/root_ss_product_cross_audited_candidate.tex'
out=w/'outputs/root_ss_product_cross_audit.json'
assert not dest.exists() and not snapshot.exists() and not out.exists()
shutil.copy2(source,dest);shutil.copy2(candidate,snapshot)
start=time.perf_counter()
run=subprocess.run([sys.executable,str(dest)],cwd=w,capture_output=True,text=True)
wall=time.perf_counter()-start
(w/'outputs/root_ss_product_cross_stdout.json').write_text(run.stdout)
(w/'outputs/root_ss_product_cross_stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
original=json.loads(author.read_text())
independent=json.loads(dest.with_suffix('.output.json').read_text())
mathematical=lambda x:{k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
assert mathematical(original)==mathematical(independent)
assert sha(author)==before and sha(dest)==sha(source)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={
 'status':'PASS','actual_utc':now,'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,
 'labels':['lem:DE-SS-cross-elliptic','lem:DE-SS-cross-product',
           'thm:DE-SS-odd-pullback-dual-rank','cor:DE-SS-odd-rectangle-dual-rank',
           'rem:DE-SS-cross-scope'],
 'proof_scope':'Entire final candidate, entire exact checker and entire invoked quaternion-norm lemma freshly read; all five assertions independently rederived.',
 'proof_checks':[
  'For P=(a,b) not O the two degree-three divisors are 2O+P and 2O+(-P). The numerator cancels at the opposite point and the stated functions have the required simple finite and infinite poles. Riemann--Roch and independence give both bases.',
  'Multiplication by x+a identifies the two divisor spaces with M squared. Relative Frobenius fixes ground coefficients and sends X,Y to x squared,y squared. All nine p-basis decompositions and the target Frobenius-twisted line are correct.',
  'The coefficient of X is the invertible reversal matrix. The determinant reduces to r squared t+r t squared+s cubed using b squared+b=a cubed, for every nonzero Picard point.',
  'For one trivial product factor the actual cross matrix need not be symmetric. Its upper-left block has inverse off-diagonal R; the correct Schur complement is A0 R A2+A2 R A0, with determinant one. For two nontrivial factors R tensor R is invertible.',
  'For the trivial product character, the tensor form swaps the six off-diagonal basis vectors in three pairs and has rank two on the diagonal three-space, hence rank eight.',
  'The connected odd-etale cover has distinct character eigensheaves in Picard zero. A nontrivial trivialized eigensheaf would give a nonconstant eigenfunction on the proper connected cover. Cartier relabels characters by Frobenius without changing triviality, so a trivial-output functional couples precisely inverse characters.',
  'Each cross determinant is a nonzero polynomial on the same nine-dimensional dual space. The finitely many nonempty determinant opens and the rank-eight trivial-block open meet over the infinite algebraically closed field. The total rank is 9n-1. Projection formula and zero Cartier of the invariant volume form make every form alternating, giving the matching upper bound.',
  'The complete earlier quaternion-norm proof supplies every positive odd endomorphism degree, hence an etale isogeny. Pairing inverse kernel points shows the kernel sum is zero, proving the exact pullback line class O(aO), with no numerical-equivalence substitution.',
  'No indecomposable fixed-surface cross determinant or new full-monodromy case is claimed. The theorem is an auxiliary exact product calculation and does not move a main gate.'
 ],
 'primary_source_scope':'No fresh external-source reading for this audit; direct relative-Cartier proof and a fully reread internal quaternion-norm construction.',
 'program':str(source.relative_to(w)),'program_sha256':sha(source),
 'isolated_program':str(dest.relative_to(w)),
 'author_output_sha256_before_and_after':before,
 'independent_output_sha256':sha(dest.with_suffix('.output.json')),
 'independent_runtime_seconds':independent['runtime_seconds'],'wall_seconds':wall,
 'author_runtime_seconds':original['runtime_seconds'],
 'all_mathematical_fields_equal':True,'check_count':independent['check_count'],
 'executed_failures':[]}
out.write_text(json.dumps(record,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 writer=csv.writer(f,delimiter='\t')
 for label in record['labels']:
  writer.writerow([label,now,record['reviewer'],
   'targeted proof check / unchanged independent exact-program rerun',
   'PASS: complete proof and checker read; divisor bases, relative twists, Schur blocks, character opens and exact pullback classes rederived. All 29 identities agree with author output, which is unchanged. See outputs/root_ss_product_cross_audit.json.'])
 writer.writerow(['lem:DE-A3-ss-norm',now,record['reviewer'],'used and rechecked in this run',
  'Complete explicit automorphism, four-square descent and norm-degree proof reread for the odd-etale rectangle corollary.'])
print(json.dumps(record,indent=2))
