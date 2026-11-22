"""Full root B93 proof/code audit and byte-preserving isolated rerun."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil,subprocess,sys,time
w=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
candidate=w/'agents/reduction_descent/B_residual_wild_last_crossing_candidate.tex'
source=w/'agents/reduction_descent/code/verify_residual_wild_last_crossing.py'
author=source.with_suffix('.output.json')
expected='50a83a2885ff0a8fb79dfce8abdca45e142b4d1fb2224993830e8086f57bea04'
assert sha(candidate)==expected
assert sha(source)=='56c7cab1f24540ff693aa8c526efbdff25a6768683806e4fd283293277217753'
assert sha(author)=='860e792a4c8f05621df62a16de3b892d61964032cf1ff719b01dc773bcfbebb3'
before={str(p.relative_to(w)):sha(p) for p in [candidate,source,author]}
folder=w/'code/audit_snapshots/B93_root_independent';assert not folder.exists();folder.mkdir(parents=True)
copy=folder/source.name;shutil.copy2(source,copy)
snapshot=w/'notes/root_B93_audited_candidate.tex';out=w/'outputs/root_B93_audit.json'
assert not snapshot.exists() and not out.exists();shutil.copy2(candidate,snapshot)
started=time.perf_counter();run=subprocess.run([sys.executable,str(copy)],cwd=w,capture_output=True,text=True);wall=time.perf_counter()-started
(w/'outputs/root_B93_independent.stdout.json').write_text(run.stdout)
(w/'outputs/root_B93_independent.stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
independent=copy.with_suffix('.output.json')
a=json.loads(author.read_text());b=json.loads(independent.read_text())
mathpart=lambda x:{k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
assert mathpart(a)==mathpart(b)
assert before=={str(p.relative_to(w)):sha(p) for p in [candidate,source,author]}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['lem:B-RD93-cyclotomic','prop:B-RD93-second-field','lem:B-RD93-terminal-bound','thm:B-RD93-crossing','rem:B-RD93-scope']
r={
 'status':'FULL-INDEPENDENT-PROOF-CODE-PASS','actual_utc':now,
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'read_scope':'Entire stable five-label candidate and entire exact checker actually read. Complete B60 fixed-representative proof, B86 Cohen/cyclotomic proof, and B92 actual25/parahoric/common-high/crossing proofs freshly read. Prior full B87-B91 root audits remain available with their precise hypotheses rechecked.',
 'proof_checks':[
  'The same-residue Cohen coefficient field gives a totally ramified degree5 extension K/K1. An Eisenstein uniformizer derivative has leading valuation24 and every other possible term has a different residue class modulo5, so cancellation cannot raise the different above24. This does not assume K/K1 Galois.',
  'The normal closure has a faithful transitive subgroup of S5. Its normal wild subgroup is the regular C5, hence the group is C5 semidirect C_m with m dividing4. Its complement is the point stabilizer, so T/K is tame of degree m. Transitivity of the different gives d=4+4b_T/m and last upper break at most5.',
  'The cyclotomic cyclic25 extension over K1 has lower breaks4,24 and upper breaks4,8. Its intersection with T is trivial: for m>1 the faithful tame action forbids an abelian order5 quotient, and for m=1 a nontrivial intersection would put mu25 in K. At upper8 the other factor has vanished, so subgroup Herbrand conversion gives m(44-d); tame descent divides by m. Thus the actual last cyclotomic break over K is44-d, at least20, and over L at least480.',
  'The actual mod25 field over R has the three independent character breaks24,96,1866, derived from the low primitive25 point and the two distinct cyclic fields A and R. Its subgroup lower counts are100,20,4 at24,384,44634. The exact quotient-coset average has unique maximum234, yielding full F2 upper breaks24,66,72,426. No arbitrary lift is assigned a quotient break.',
  'The quotient25 lower entry c is an actual independent additive character of break6. Thus E=F2C, with actual quotient coordinates(a0,d0,b mod25,c), and its upper/lower filtrations follow from the strictly separated first break. Subgroups fixing S=RA and the actual low25 point are u=a0=0 and b mod25=d0=0. Their inherited lower filtrations give E/S upper6,24,8946 and E/E_low upper6,384.',
  'The integral prime-to5 tame eigenprojector preserves the unique high inverse coset and supplies a primitive25 point in the first eigenline; a primitive125 eigenline lift exists by the same projector. The two actual inverse polygons give19/25 and3/25. The full parahoric stabilizers give a degree125 point field and a degree625 compositum T_h with R. Over S its actual translation group has coordinates(a1,c), with c-conductor6.',
  'In T_h the second coordinate has value75 and every nonzero high-line translation has displacement46875. The unconditional B60 inequality bounds each high-line lower break by46800, without a prime-to5 coordinate-value assumption. If that line is last, the upper bound is46824/5; otherwise c detects the last line and bounds it by6. Restriction to E gives the same terminal a1 character and bounds it by275496. T_h intersection E is SC, so disjointness is neither asserted nor needed.',
  'The actual low125 point has degree3125 over L, and over the low25 field its additive translation coordinates are(b2,d1). Its coordinate value is5, and every d1-nonzero translation has displacement3125. Applying the unconditional inequality and the exact cyclic quotient average bounds its d1 character by3120. Restriction through E/E_low then bounds the same terminal d1 character by70296. The point-field intersection with E is precisely E_low.',
  'The actual determinant on the good field is cyclotomic up to inverse. Its mod25 character a0+d0 has conductor72, so mu25 is absent. The cyclotomic last break is above426, the final upper break of E/L; its last subgroup survives restriction with exact conductor psi_E/L(v), at least391896. On Gal(F/E) it is exactly1+25(a1+d1), whose conductor is at most275496. The contradiction compares one actual character over one actual field.',
  'The exact supplement enumerates all390625 parahoric matrices and ten point/field images, checks the required stabilizer intersections, all125 terminal determinants and rational Herbrand arithmetic. Its35 normal-closure arithmetic rows are explicitly only identities, with no field existence inferred. All finite output is supplementary to the full field proof.'
 ],
 'dependencies_freshly_reread':['lem:B-RD60-break','lem:B-RD86-cyclotomic','lem:B-RD92-tame25','lem:B-RD92-parahoric','lem:B-RD92-common-high','thm:B-RD92-crossing'],
 'source_scope':'No fresh external primary-source opening claimed. The full Cohen and Colmez different, norm, subgroup and Herbrand proof readings already retained in this run are reused with their actual scope. The new normal-closure and cyclotomic argument is supplied in full in B93.',
 'program_sha256':sha(source),'author_output_sha256':sha(author),'author_bytes_unchanged':True,
 'independent_program':str(copy.relative_to(w)),'independent_output':str(independent.relative_to(w)),
 'independent_output_sha256':sha(independent),'independent_runtime_seconds':b['runtime_seconds'],
 'author_runtime_seconds':a['runtime_seconds'],'subprocess_wall_seconds':wall,'all_mathematical_output_identical':True,
 'counts':{'normal_closure_arithmetic_rows':len(b['normal_closure_arithmetic_rows']),'matrices':b['matrix_rows'],'point_images':len(b['point_image_sizes']),'terminal_determinants':b['terminal_determinant_rows']},
 'terminal_bounds':[b['terminal_a_bound'],b['terminal_d_bound']],'cyclotomic_lower':b['cyclotomic_terminal_lower_bound'],'strict_gap':b['strict_gap'],
 'executed_failures':[],
 'scope_guard':'Only the last residual-wild crossing(5,45) is excluded. Both-large residual-wild shapes(3,4),(4,4) and irreducible residual orders5^5 through5^8 remain undecided; the full first-wild least index remains in{2,3}. No625-torsion comparison is assumed.'
}
out.write_text(json.dumps(r,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:
  wr.writerow([label,now,r['reviewer'],'independent re-proof / computation or formal certificate','PASS: full proof/code; actual same-character conductor contradiction and unchanged isolated output. See outputs/root_B93_audit.json.'])
 for label in r['dependencies_freshly_reread']:
  wr.writerow([label,now,r['reviewer'],'used and rechecked in this run','PASS: complete invoked actual field, fixed-representative or cyclotomic proof read and hypotheses checked for B93.'])
with (w/'notes/checkpoint34_changes.md').open('a') as f:
 f.write('\n## Root full audit of the last residual-wild crossing\n\nB93 passed the complete independent root proof/code audit at '+now+'. The unchanged isolated exact supplement ran in '+str(b['runtime_seconds'])+' seconds, with all mathematical output identical:390625 matrices, ten point/field images,35 normal-closure arithmetic rows and125 terminal determinants. The same actual terminal determinant has upper bound275496 and lower bound391896. The candidate is not canonical until the companion audit and promotion are complete. Both-large and irreducible branches remain open.\n')
print(json.dumps({k:r[k] for k in ['status','actual_utc','independent_runtime_seconds','all_mathematical_output_identical','counts','strict_gap']},indent=2))
