"""Full root proof/code audit and an unchanged, isolated B94 rerun."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil,subprocess,sys,time
w=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
candidate=w/'agents/reduction_descent/B_both_large_tracefree_rows_candidate.tex'
source=w/'agents/reduction_descent/code/verify_both_large_tracefree_rows.py'
author=source.with_suffix('.output.json')
expected='756e9cfc2b38369c603ff21f98dac6210bfc5f2d8bc1c3804f1b273eee2bc44f'
assert sha(candidate)==expected
assert sha(source)=='591eacd022e0ef5347029edf30d1c213b82f3f426297551bea8a175d141a548d'
assert sha(author)=='3cc008f3222d0297bff1e105998503876079e05b3e4cb36c147b2e7b908dc0fc'
before={str(p.relative_to(w)):sha(p) for p in [candidate,source,author]}
folder=w/'code/audit_snapshots/B94_root_independent'
assert not folder.exists();folder.mkdir(parents=True)
copy=folder/source.name;shutil.copy2(source,copy)
snapshot=w/'notes/root_B94_audited_candidate.tex'
out=w/'outputs/root_B94_audit.json'
assert not snapshot.exists() and not out.exists()
shutil.copy2(candidate,snapshot)
started=time.perf_counter()
run=subprocess.run([sys.executable,str(copy)],cwd=w,capture_output=True,text=True)
wall=time.perf_counter()-started
(w/'outputs/root_B94_independent.stdout.json').write_text(run.stdout)
(w/'outputs/root_B94_independent.stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
independent=copy.with_suffix('.output.json')
a=json.loads(author.read_text());b=json.loads(independent.read_text())
mathpart=lambda x:{k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
assert a['status']==b['status']=='PASS'
assert mathpart(a)==mathpart(b)
assert before=={str(p.relative_to(w)):sha(p) for p in [candidate,source,author]}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['lem:B-RD94-group','lem:B-RD94-ordering','lem:B-RD94-common-high','prop:B-RD94-profiles','lem:B-RD94-terminal','thm:B-RD94-six-rows','rem:B-RD94-scope']
r={
 'status':'FULL-PROOF-CODE-PASS','actual_utc':now,
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'read_scope':'Entire seven-label stable candidate and every line of the exact checker read. Complete B60 fixed-coefficient lemma, B49 coefficient proof, B69 actual quotient/Newton proof, B86 Cohen/cyclotomic lemma, B91 residual and layer proofs, and B92 common-high proof freshly reread. The earlier fully audited B93 conductor-restriction method is reused within its actual-field scope.',
 'proof_checks':[
  'The tracefree first congruence layer kills the determinant modulo25 on ker(v0). Its residual factor has the nontrivial upper-root tame weight, so invariance kills it on all W. The containing det=1 mod25 Iwahori group has order5^8, the actual order already proved in B91; equality follows. In the actual quotient lattice(e1/5,e2), the full25 images have coordinates(v0,w0,a0,v1) and(v0,w0,a0,w1). Their compositum has degree5^5 and terminal kernel(a1,v2,d1), with lower-left terminal entry zero.',
  'The actual determinant is cyclotomic up to inverse on the good field. Triviality modulo25 puts mu25 in L and then in K, since the missing cyclotomic degree divides5 while L/K is tame of degree24. The complete Cohen expansion proves K=K0(mu25) at absolute index20; the next actual cyclotomic quotient has break24 over K and576 over L. No finite-residue substitution or trivial-full-determinant inference is used.',
  'Residual upper-unipotent conjugation on sl2 has the displayed three-step formula. Invariance of conductor under t=1,-1 yields rho<=x<=C; the distinct tame weights and the injective ramification leading map make both inequalities strict. The point-field quotient on the second column is the actual degree25 additive group(v1,d0) over R; d0=-a0 there, so its last line is the canonical high line. The opposite quotient has the same typed argument.',
  'For x>r, choose a genuine maximal-break element g in a nontrivial residual coset. The exact quotient average identifies r=phi_H(M), because all coset breaks equal min(M,b(h)), also at ties by maximality. If M is at least the diagonal lower break D, a lower-root h has commutator with zero lower entry and nonzero diagonal entry, hence break D. The direct fixed-coefficient inequality gives break at least M+b(h)>D. This proves x>r without assigning a quotient break to an arbitrary lift. The opposite argument gives y>r-prime.',
  'Over S=RR-prime the diagonal characters agree up to sign, since v0=w0=0 and a0+d0=v0*w0. Restricting above the two smaller root conductors gives 5x-4rho=5y-4sigma and rho-sigma=5(r-prime-r), hence y=x+4(r-r-prime). The tame leading-coefficient congruences and strict B60 divisible-coordinate bounds have the actual R and R-prime bases; diagonal conductors are multiples24.',
  'The common-high coordinate data normalize by the actual point-field degree125 over L. For prime parameters the two fixed-coefficient strict regimes and boundary t=24m2 leave only t=24m1. For each mixed row the inequalities60000+630m1-3630m2>0 and630m2-750m1>0 force the leading ordinary exponent at the high break, then rule out t>=24m1, including the divisible-by25 leading exponent. Thus t is a positive multiple24 below24m1 and the other conductor is3000-126m2. No existence of an arithmetically compatible profile is inferred.',
  'For(5,13),(5,17), their quotient prime pairs force y=264,168 and r-prime=6. The only low diagonal solutions are(r,x)=(66,24),(42,24), whose sigma=5r-24 exceeds y. The mirrors use only the two available25 modules, never quotient125 torsion. For(5,9),(15,19), x>r or y>r-prime leaves exactly nine(r-small-diagonal) profiles per row. The actual common degree125 quotient and two independent kernel lines determine the compositum upper filtration at the union of the two lists, and direct Herbrand integration gives all five lower breaks.',
  'The high primitive125 point has single-segment inverse valuation j/125 because B>20; its compositum T_h with R has degree3125 over L and coordinate valuation25j. The actual group over S_h has additive(a1,w1). Every nonzero high-line element has displacement15625j and hence lower break<=15600j. Treating separately whether that line is last gives conductor(a1)<=(15600*j_min+4*z_h)/5. The same character restricts to E through the actual degree25 extension E/S_h; its possible nontrivial intersection is explicitly retained.',
  'The low primitive125 field has degree3125 over L, with coordinate value5b and actual relative coordinates(v2,d1). Every nontrivial d1 coset displaces outside the high line by3125b, so the exact quotient average bounds its conductor by3120b_min. E/E_low is the actual cyclic25 lower-root subgroup, whose fifth power is the terminal lower-root direction. Restricting through its inherited lower pair gives the two d1 bounds. No comparison uses a separately selected cyclic field.',
  'The same terminal determinant is exactly1+25(a1+d1). The actual cyclotomic break576 is above the last E/L break, so restriction has exact conductor psi_E(576)=803976-20X-2100R0. Each of the two diagonal character bounds is strictly below it in every one of the18 profiles. This excludes two additional rows, for six total. The finite-special orbit census correctly removes(7,11),(13,17) as already equal-character cases; exactly four different-character(3,4) rows remain.',
  'The unchanged exact supplement enumerates all390625 matrices,12 point/division images,125 terminal determinants,31250 relative quotient products,25 cyclic lower-root powers and625 conjugations. It reconstructs all18 conductor profiles and the ten-row finite-special census. The initial failed census-loop execution and exact correction remain retained; its failure is neither suppressed nor claimed as mathematical evidence.'
 ],
 'dependencies_freshly_reread':['lem:B-RD49-point','lem:B-RD60-break','lem:B-RD69-quotients','lem:B-RD86-cyclotomic','prop:B-RD91-divisibility','prop:B-RD91-parameters','thm:B-RD91-large','lem:B-RD92-common-high'],
 'source_scope':'No fresh external source opening claimed. Earlier complete original Hopkins-Gross, Stacks032A and Colmez proof readings are reused with their precise scopes. The new normality, point-field and conductor comparisons are fully written in B94.',
 'program_sha256':sha(source),'author_output_sha256':sha(author),'author_bytes_unchanged':True,
 'independent_program':str(copy.relative_to(w)),'independent_output':str(independent.relative_to(w)),
 'independent_output_sha256':sha(independent),'independent_runtime_seconds':b['runtime_seconds'],
 'author_runtime_seconds':a['runtime_seconds'],'subprocess_wall_seconds':wall,'all_mathematical_output_identical':True,
 'counts':b['counts'],'remaining_3_4_pairs':b['remaining_3_4_pairs'],
 'minimum_strict_gap':min(int(x['strict_gap']) for x in b['profiles']),
 'executed_failures_this_rerun':[],
 'retained_author_failure':'agents/reduction_descent/notes/B94_initial_pair_enumeration_failure',
 'scope_guard':'Only six of ten different-character both-large pairs in layer shape(3,4) are excluded. The four listed(3,4) pairs, all(4,4) pairs, irreducible residual orders5^5 through5^8 and the full least index in{2,3} remain undecided. No surviving pattern is realized.'
}
out.write_text(json.dumps(r,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:
  wr.writerow([label,now,r['reviewer'],'targeted proof check / computation or formal certificate','PASS: complete proof and unchanged isolated exact rerun; six rows only. See outputs/root_B94_audit.json.'])
 for label in r['dependencies_freshly_reread']:
  wr.writerow([label,now,r['reviewer'],'used and rechecked in this run','PASS: complete invoked coefficient, quotient, normality or cyclotomic proof reread; its scope checked for B94.'])
with (w/'notes/checkpoint35_changes.md').open('a') as f:
 f.write('\n## Root full B94 proof and exact-code audit\n\nThe stable seven-label candidate passed the complete root audit at '+now+'. Its unchanged isolated exact supplement took '+str(b['runtime_seconds'])+' seconds, with all mathematical output identical. It verifies390625 actual matrices,12 field-image maps,31250 relative-quotient products and18 conductor profiles. The smallest positive same-character contradiction margin is'+str(r['minimum_strict_gap'])+'. The author\'s initial census-loop failure and correction are preserved. Only six of ten both-large(3,4) parameter pairs are excluded; the four remaining pairs, all(4,4), the irreducible branch and the least-index interval{2,3} remain. Canonical promotion still requires the complete companion audit.\n')
print(json.dumps({k:r[k] for k in ['status','actual_utc','independent_runtime_seconds','all_mathematical_output_identical','counts','minimum_strict_gap','remaining_3_4_pairs']},indent=2))
