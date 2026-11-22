"""Retain the complete actual B83 proof audit and unchanged isolated exact rerun."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil,subprocess,sys,time
w=Path(__file__).resolve().parents[1]
candidate=w/'agents/reduction_descent/B_first_wild_swapped_quotients_candidate.tex'
source=w/'agents/reduction_descent/code/verify_first_wild_swapped_quotients.py'
author=source.with_suffix('.output.json')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected='453ca8011e454fcb1360ccf27195d7b8a5db633d6383cd3048a9bae8d9b83d40'
assert sha(candidate)==expected
assert sha(source)=='8e4e4decea77980e34a32f2d83d37e1c24aa2a49b2faa55faf47fd1fb7276fc4'
before=sha(author)
dest=w/'code/audit_snapshots/B83_root_independent_certificate.py'
snapshot=w/'notes/root_B83_audited_candidate.tex';out=w/'outputs/root_B83_audit.json'
assert not dest.exists() and not snapshot.exists() and not out.exists()
shutil.copy2(source,dest);shutil.copy2(candidate,snapshot)
start=time.perf_counter()
run=subprocess.run([sys.executable,str(dest)],cwd=w,capture_output=True,text=True)
wall=time.perf_counter()-start
(w/'outputs/root_B83_independent_stdout.json').write_text(run.stdout)
(w/'outputs/root_B83_independent_stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
original=json.loads(author.read_text());independent=json.loads(dest.with_suffix('.output.json').read_text())
def mathematical(x):return {k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
assert mathematical(original)==mathematical(independent)
assert sha(author)==before and sha(dest)==sha(source)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={'status':'PASS','actual_utc':now,'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,
 'labels':['lem:B-RD83-tame','lem:B-RD83-quotients','prop:B-RD83-Lie','cor:B-RD83','rem:B-RD83-scope'],
 'proof_scope':'Entire final five-assertion candidate and exact checker read. Earlier draft also read before the checkpoint29 archive; final p-group and old-p-line clarifications checked. Actual quotient, point-field, integral-lattice and weight arguments rederived.',
 'proof_checks':[
  'For rational first-level modules, a primitive second-level point over a low target has a Galois point field embedded in the full first-level translation group. The denominator of b/p^2 with p not dividing b forces the degree to be exactly p^2, so every translation occurs and the common low translation break is (p^2-1)b.',
  'The two distinct high lines are stable under the same actual residual representation. Schematic closure, finite-flat quotient and semilinear generic descent give actual quotients; no integral good model over K is inferred.',
  'With B=p^2k, 1<=k<=p-2, one has B>e. The exact Weierstrass product gives high quotient parameter p(N-pk), low quotient parameter pk. The positive inverse slopes and old first-level image valuations reproduce both formulas without using p not dividing e.',
  'The identity (M/J)[p^2]={P in M[p^3]:p^2P in J}/J is an identity of finite etale generic group schemes and Galois modules. Their images over L are p-groups, being subquotients of the original third-level image. If the quotient residual action were tame it would therefore be trivial; the point-field lemma contradicts N-pk_i>=2p-1>k_j. The actual old-p image also gives an invariant line.',
  'Under rational Tate-lattice identification the first quotient lattice is T+Z_p(e1/p), giving the conjugate matrix [[rho11,p rho12],[rho21/p,rho22]]. Its residual wild lower entry is the original A21. The opposite quotient detects A12. This uses original actual coefficients, not independent choices of lifts.',
  'The finite determinant is nonsquare and mu_p lies in K, so the residual eigenvalue ratio alpha/beta is nonsquare. For p=1 modulo4 it is neither1 nor-1, hence its two off-diagonal weights and the diagonal weight are distinct. Polynomial spectral projectors preserve W1 and produce E12 and E21 separately.',
  'Actual pth powers place W1 in W2, and actual commutators put [W1,W1] in W2. The bracket diag(1,-1) is independent of E12,E21; hence dimW1>=2,dimW2>=3 and wild order>=p^5.',
  'The final corollary exhausts square determinant (B77), irreducible residual (B81), residual wild (B82) and tame reducible cases. One-slope tame reducibility forces scalar residual action and square determinant. A prime b forces order>=p^4 and B82 excludes equality. Divisible b gives k in1..p-2; common high lines recover characters directly, otherwise the quotient proposition applies.',
  'For p=3 modulo4 an off-diagonal weight can equal its inverse; that branch is explicitly excluded and retained in exact output. No order>=p^5 is excluded or constructed and the unrestricted first-wild index remains in{2,3}.'
 ],
 'dependencies_read_scope':'Fresh full B69 quotient/Weierstrass/descent proof and full B79 layer proof. Full B82 candidate and B60-break were read immediately beforehand in the root B82 audit; full B77-square and B76-determinant were likewise read then. B81 uses its already recorded complete root audit, not an asserted new complete reread.',
 'primary_source_scope':'No new original-source reading for B83. The actual quotient and fixed-coefficient source bridges retain their previously audited scope. New lattice and weight arguments are direct.',
 'program':str(source.relative_to(w)),'program_sha256':sha(source),
 'isolated_program':str(dest.relative_to(w)),'author_output_sha256_before_and_after':before,
 'independent_output_sha256':sha(dest.with_suffix('.output.json')),
 'independent_runtime_seconds':independent['runtime_seconds'],'wall_seconds':wall,
 'author_runtime_seconds':original['runtime_seconds'],'all_mathematical_fields_equal':True,
 'counts':independent['counts'],'weight_rows':independent['weight_rows'],'executed_failures':[]}
out.write_text(json.dumps(record,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 writer=csv.writer(f,delimiter='\t')
 for label in record['labels']:
  writer.writerow([label,now,record['reviewer'],'targeted proof check / unchanged independent exact-program rerun',
    'PASS: complete proof and checker read; actual quotient and point-field proofs, integral lattice direction and distinct tame spectral projectors rederived. Literal isolated rerun agrees in all mathematical fields and preserves author output. See outputs/root_B83_audit.json.'])
 for label in ['lem:B-RD69-quotients','lem:B-RD79-layers','lem:B-RD82-terminal','prop:B-RD82-recovery','thm:B-RD82']:
  writer.writerow([label,now,record['reviewer'],'used and rechecked in this run',
    'Full invoked actual quotient/layer/terminal proofs freshly read in this and the immediately preceding root audit; precise scope in outputs/root_B83_audit.json.'])
print(json.dumps({k:v for k,v in record.items() if k!='weight_rows'},indent=2))
