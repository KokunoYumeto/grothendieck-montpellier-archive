"""Complete root proof/source audit and unchanged isolated B98 exact rerun."""
from pathlib import Path
import csv,datetime,hashlib,json,re,shutil,subprocess,sys,time
w=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
candidate=w/'agents/reduction_descent/B_first_wild_cyclotomic_different_candidate.tex'
source=w/'agents/reduction_descent/code/verify_first_wild_cyclotomic_different.py'
author=source.with_suffix('.output.json')
colmez=w/'agents/reduction_descent/sources/colmez_corps_locaux.txt'
expected='0b8f978f9cfa246cfc0f6b1f2fb99212912cd4b4cfd1df86b0f04d7a8a868dc1'
assert sha(candidate)==expected
assert sha(source)=='154100c1a72927764be6657cee78140b1ae7def7abd4938e1db5d1c8b0856c2e'
assert sha(author)=='27f2a52e50e9359d0cabcc1d947bcb5e6d85cd87936a1d7f1886fff0f36d361c'
assert sha(colmez)=='795ebafb9326f68ed625c2f44b7f4a220e0209c489530ace62cda3de357ca419'
before={str(p.relative_to(w)):sha(p) for p in [candidate,source,author,colmez]}
folder=w/'code/audit_snapshots/B98_root_independent';assert not folder.exists();folder.mkdir(parents=True)
copy=folder/source.name;shutil.copy2(source,copy)
snapshot=w/'notes/root_B98_audited_candidate.tex';out=w/'outputs/root_B98_audit.json'
assert not snapshot.exists() and not out.exists();shutil.copy2(candidate,snapshot)
start=time.perf_counter();run=subprocess.run([sys.executable,str(copy)],cwd=w,capture_output=True,text=True);wall=time.perf_counter()-start
(folder/'stdout.txt').write_text(run.stdout);(folder/'stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
independent=copy.with_suffix('.output.json')
a=json.loads(author.read_text());b=json.loads(independent.read_text())
mathpart=lambda x:{k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
assert a['status']==b['status']=='PASS' and mathpart(a)==mathpart(b)
assert before=={str(p.relative_to(w)):sha(p) for p in [candidate,source,author,colmez]}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=re.findall(r'\\label\{([^}]+)\}',candidate.read_text());assert len(labels)==4
r={'status':'FULL-INDEPENDENT-PROOF-SOURCE-CODE-PASS','actual_utc':now,
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'read_scope':'Entire four-label proof, complete final field-scope and certificate diffs, and complete unchanged standalone checker read. Fresh full Colmez3.17,3.18 including continuation,3.19 proofs read in retained original text. Complete B76 point/dimension/mixed proofs and B63 lower-example proof freshly reread; full B97 root proof audit completed immediately before this audit.',
 'proof_checks':[
  'The Cohen field K0 has [K:K0]=e_K even for infinite algebraically closed residue: uniformizer powers give a residue basis modulo p, repeated p-adic coefficient lifting gives spanning, and distinct valuations modulo e_K give independence. Thus K1=K0(mu_p) lies in K with [K:K1]=p. The unique degree-p subfield of C0/K1=K0(mu_(p^3))/K1 is K0(mu_(p^2)). Its absence from K gives K intersection C0=K1, [C:K]=p^2 and [C:C0]=p. All named extensions are actually totally ramified.',
  'For a uniformizer of the degree-p extension K/K1, the Eisenstein derivative leading term has valuation e_K+p-1=p^2-1. The other terms have pairwise distinct residues i-1 modulo p, different from the leading residue-1. Thus its least valuation cannot cancel and d(K/K1)<=p^2-1. For C/C0 every nonleading derivative term has valuation>=p, and the leading term>=p-1, so d(C/C0)>=p-1. Monogenicity follows from the same complete uniformizer-expansion argument.',
  'In C0/K1 the nonterminal cyclotomic automorphisms have displacement valuation p, and the p-1 terminal ones have displacement valuation p^2. Their exact sum is2p^2(p-1). Different transitivity on the two actual towers gives d(C/K)+p^2 d(K/K1)=d(C/C0)+p d(C0/K1), with these ramification factors. Therefore d(C/K)>=p^2(p-1)^2+p-1.',
  'A totally ramified cyclic p^2 extension has two positive lower breaks, since the nontrivial pth-power subgroup has strictly later first ramification coefficient. In upper notation its different is(p-1)(delta1+p delta2+p+1). This yields delta1+p delta2>=p(p^2-p-1), and if delta1<=p-1 then delta2>=p^2-p-2+1/p. The proof retains the rational endpoint and uses no Hasse--Arf theorem.',
  'B97 supplies actual first point fields of degree p^2 and third-point extensions of relative degree p^2, with c1=(p^2-1)(p-1), c2=(p^4-1)(p-1). For two actual primitive basis columns, F2 intersection T_i=E_i and F2T1T2=F3. The two terminal maps B->Be1 and B->Be2 have zero common kernel. Hence their quotient character spaces span the full terminal dual, including determinant, and every terminal character has conductor<=p^(r1-2)c2. This is exactly the previously audited actual-field subgroup proof, not a direct-sum hypothesis.',
  'B97 excludes traceless first layers and forces r1=3 or4 with nonzero trace. On the good field determinant is cyclotomic, so mu_(p^2) is absent from L and K. The degree-N tame good extension scales both upper breaks of C/K by N. Its first cyclotomic quotient lies in F2, so N delta1<=c1 and delta1<=p-1. The field lemma thus makes d2=N delta2>c1, with p^2(d2-c1)-c2>=N(p^4-3p^3+1)>0 for p>=5.',
  'The cyclic p^2 field LC and elementary-abelian F2 have intersection exactly L(mu_(p^2)), not L. The remaining extension F2C/F2 is an actual nontrivial cyclic quotient of F3/F2. Above c1 the ramification of the compositum lies entirely over F2 and projects to the final cyclic line of LC until d2. Quotient compatibility and subgroup conversion therefore give exactly psi_F2/L(d2)=psi_F2/L(c1)+p^r1(d2-c1)>p^r1(d2-c1), contradicting the terminal upper bound. This treats the shared first cyclotomic layer explicitly.',
  'The all-prime theorem is limited to the irreducible-residual whole height-two branch with algebraically closed residue and e=p(p-1). At p5,e20, B76 applies at actual level n3 because n=v5(e)+2 and20<=25. After completed maximal unramified extension, mu5 is automatic: 5=u*pi^20, a fourth root of u exists by Hensel, and the unique tame degree4 extension of the Cohen field is K0(mu5). Thus the determinant and mixed reductions apply to every permitted base.',
  'For the exact(5,20,2) corollary, irreducible residual comparisons are excluded by this theorem, residual-wild reducible ones by B96, and tame reducible/scalar/trivial ones by B82--B84 and B87--B90. These exhaust height-two residual possibilities after the whole/filtered reductions. The freshly reread B63 construction applies at n2 since20>5 and4 divides20; one may take A1,Q25,d480,b380. Its explicit Eisenstein arc and finite-flat quotient/Kummer lifting give actual common25-torsion and unequal prime-to5 special characters. Thus n3 suffices and n2 fails, yielding manuscript nu=n-1=2.',
  'The entire checker was read and rerun unchanged in isolation. It verifies nine symbolic identities, all stated rational upper-break samples without assuming integrality, derivative residue distinctions, cyclotomic exponent counts, terminal determinant formulas and dual spanning for all stated basis pairs. Every mathematical output equals the author output. Finite profiles are not asserted to classify fields or to construct a BT group; the complete written proof supplies those logical steps.'
 ],
 'primary_source':{'path':str(colmez.relative_to(w)),'sha256':sha(colmez),
  'actually_read':'Proposition3.17 complete trace-dual proof; Proposition3.18 complete derivative proof including continuation; Corollary3.19 complete different/ramification proof, printed17--18.',
  'scope':'These algebraic proofs apply to the displayed complete DVRs. No new web opening, PDF image inspection, finite-residue class field theorem or upper-break integrality theorem is claimed.'},
 'program_sha256':sha(source),'author_output_sha256':sha(author),'author_bytes_unchanged':True,
 'independent_program':str(copy.relative_to(w)),'independent_output':str(independent.relative_to(w)),
 'independent_output_sha256':sha(independent),'independent_runtime_seconds':b['runtime_seconds'],
 'author_runtime_seconds':a['runtime_seconds'],'subprocess_wall_seconds':wall,
 'all_mathematical_output_identical':True,'counts':b['counts'],'executed_failures':[],
 'scope_guard':'The exact full B.4 index equality is only nu_min(5,20,2)=2. General B.4, other first-wild primes, arbitrary ramification and higher height remain open.'}
out.write_text(json.dumps(r,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:
  wr.writerow([label,now,r['reviewer'],'independent re-proof / computation or formal certificate','PASS: full actual-field/different proof, exact p5/e20 scope and unchanged isolated supplement; outputs/root_B98_audit.json.'])
 for label in ['lem:B-RD76-determinant','prop:B-RD76-mixed','cor:B-RD76','thm:B-RD63-arc']:
  wr.writerow([label,now,r['reviewer'],'used and rechecked in this run','PASS: complete canonical proof freshly reread and the p5/e20 specialization verified in the B98 full audit.'])
print(json.dumps({k:r[k] for k in ['status','actual_utc','candidate_sha256','independent_runtime_seconds','counts','all_mathematical_output_identical']},indent=2))
