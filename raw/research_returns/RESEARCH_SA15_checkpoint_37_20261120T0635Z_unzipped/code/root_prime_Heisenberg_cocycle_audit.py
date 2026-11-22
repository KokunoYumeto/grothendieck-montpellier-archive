"""Retain the actual root read of the explicit invariant-algebra precision patch."""
from pathlib import Path
import csv,datetime,hashlib,json
w=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=w/'agents/monodromy/post_CP35_prime_Heisenberg_rank_candidate.tex'
new=w/'agents/monodromy/notes/prime_Heisenberg_cocycle_precision/proposed_candidate.tex'
diff=w/'agents/monodromy/notes/prime_Heisenberg_cocycle_precision/proposed.diff'
assert sha(old)=='1a03b3733ace0faf2b6e4419b2a079e9439fb95699deb3be386258564ed4c59d'
assert sha(new)=='ffd95f40966e14c3db8937bec99206e944c38521f12c42390fac537788752ce2'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={'status':'FULL-PRECISION-PATCH-PASS','actual_utc':now,
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'base_audit':'outputs/root_prime_Heisenberg_rank_audit.json',
 'frozen_candidate_sha256':sha(old),'proposed_candidate_sha256':sha(new),
 'patch_sha256':sha(diff),'entire_patch_actually_read':True,
 'check':'CS=zeta SC. Ad(S) sends C to zeta^-1 C, cancelling sigma_A(A)=zeta A; Ad(C) sends S to zeta S, cancelling sigma_B(B^-1)=zeta^-1 B^-1. Thus both actions fix X=AC and Y=B^-1 S. Their powers and commutator are exactly X^p=a,Y^p=b^-1,XY=zeta YX. The matrix monomials C^i S^j are linearly independent over the splitting field, so the p^2 invariant monomials are independent over F and fill the descended algebra. Setting u=Y^-1 gives u^p=b and uX=zeta Xu, exactly the written cyclic algebra. Weight-r lifts raise the cocycle to r, giving the source/target ratio-2. No change to the polynomial certificates, hypotheses or conclusions.',
 'numerical_run':'None needed or claimed; this is a direct complete algebra calculation.',
 'retention':'Frozen source and proposed source/diff remain separately retained; original full audit is not overwritten.'}
out=w/'outputs/root_prime_Heisenberg_cocycle_audit.json';assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 csv.writer(f,delimiter='\t').writerow(['lem:prime-Heisenberg-projective-dominance',now,record['reviewer'],'independent re-proof / computation or formal certificate','PASS: complete explicit invariant-algebra precision patch read and independently derived; outputs/root_prime_Heisenberg_cocycle_audit.json.'])
print(json.dumps(record,indent=2))
