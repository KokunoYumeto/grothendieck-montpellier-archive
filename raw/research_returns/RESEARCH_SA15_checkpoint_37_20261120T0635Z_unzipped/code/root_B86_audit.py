"""Retain the full root B86 audit, original-source readings, and isolated rerun."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil,subprocess,sys,time
w=Path(__file__).resolve().parents[1]
candidate=w/'agents/reduction_descent/B_first_wild_cyclotomic_quotient_candidate.tex'
source=w/'agents/reduction_descent/code/verify_first_wild_cyclotomic_quotient.py'
author=source.with_suffix('.output.json')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected='ad8b70dc7b353f54ac8833794a2f962d916ec6f663f31f616fef85ddb33ddee6'
assert sha(candidate)==expected
assert sha(source)=='f8084e1c2e0780e20fe9939857c38c6aceb5560d8188be038f009673f50854c2'
before=sha(author)
dest=w/'code/audit_snapshots/B86_root_independent_certificate.py'
snapshot=w/'notes/root_B86_audited_candidate.tex';out=w/'outputs/root_B86_audit.json'
assert not dest.exists() and not snapshot.exists() and not out.exists()
shutil.copy2(source,dest);shutil.copy2(candidate,snapshot)
start=time.perf_counter()
run=subprocess.run([sys.executable,str(dest)],cwd=w,capture_output=True,text=True)
wall=time.perf_counter()-start
(w/'outputs/root_B86_independent_stdout.json').write_text(run.stdout)
(w/'outputs/root_B86_independent_stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
original=json.loads(author.read_text());independent=json.loads(dest.with_suffix('.output.json').read_text())
mathematical=lambda x:{k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
assert mathematical(original)==mathematical(independent)
assert sha(author)==before and sha(dest)==sha(source)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
reads=[
 {'title':'The Stacks Project, Theorem10.160.8, Tag032A','url':'https://stacks.math.columbia.edu/tag/032A','web_refs':['turn728936992view0'],'actual_scope':'Entire displayed theorem and full proof, including the mixed-characteristic coefficient-ring induction and surjectivity conclusion. Linked formal-smoothness dependency proofs were not freshly reread.'},
 {'title':'Pierre Colmez, Corps locaux, notes du cours de M2','url':'https://webusers.imj-prg.fr/~pierre.colmez/CL.pdf','web_refs':['turn728936992view1','turn742152063view0','turn742152063view1','turn290026742view0','turn290026742view1'],'actual_scope':'Opening definition of local field, complete Proposition2.12 with proof on printedp11, Section3 hypotheses allowing arbitrary perfect residue, and complete Proposition3.7 with its two divisibility proof on printedpp14-15. The immediately following Herbrand proof and Proposition3.13 were also displayed and read, but are not needed for this direct quotient-average argument.'}]
record={'status':'PASS','actual_utc':now,'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,
 'labels':['lem:B-RD86-cyclotomic','prop:B-RD86-traceless','cor:B-RD86-tame','rem:B-RD86-scope'],
 'proof_scope':'Entire four-label candidate and exact checker read. All field-degree, coefficient-ring, cyclotomic, point-stabilizer and norm-quotient steps independently rederived after opening the cited original proofs.',
 'proof_checks':[
  'As mu_p is already inK, adjoining mu_p² has degree1 orp. Its inclusion in the tame degreeN good field forces inclusion inK. The Cohen ring injects into the mixed-characteristic DVR; the shifted cyclotomic Eisenstein polynomial has degree exactlye_K=p(p-1), and its root has valuation1 inK. The complete coefficient ring plus that uniformizer recovers all ofO_K by successive expansions, so K=K0(zeta_p²).',
  'The next shifted cyclotomic polynomial gives a degree-p cyclic extension K3/K with uniformizerpi=zeta_p³-1. A nonidentity automorphism changes pi by a unit timeszeta_p-1 of normalized valuationp², hence has lower breakN=p²-1.',
  'The compositumC=LK3 is the unique tame degreeN extension ofK3, since the residue field is algebraically closed. Hensel extraction of all Nth roots of units permits a uniformizert witht^N=pi. The order-p action fixingL is wild, so sigma(t)/t has residue1; raising toN preserves its displacement valuation. Thus the break overL is exactlyN².',
  'If W1=W2=sl2, det modp² is trivial, givingmu_p² inL; the last cyclotomic extension is still nontrivial. Terminal trace zero only makes the determinant factor throughW1. Its resulting nonzero linear functional is tame invariant, so it killsE12,E21 and is nonzero onH. The argument does not mistake zero terminal trace for zero full determinant.',
  'A second-level point abovee1 has Galois point fieldE/L of degreeq, because evaluation sl2 on e1 is the full two-space and all first-level translations are rational. Its stabilizer consists of the terminal layer and the kernel lineE12 modulo that layer; both are in the determinant kernel. Hence the actual cyclotomic fieldC is contained inE.',
  'Every lift of a nontrivial cyclotomic quotient element translates byae1+ce2 witha nonzero. In the second model this is low; the point coordinate and its displacement inE have valuationspk2 andp³k2. The unconditional lower-break bound gives b_E<=pNk2<=pN(p-2)<N² for every such lift.',
  'The exact norm-polynomial quotient formula is b_C+1=(1/p)sum(b_E+1), sinceE/C is totally ramified degreep. The two divisibility proof in the original source has no finite residue assumption. Averaging the strict bounds contradicts the actual cyclotomic breakN².',
  'Forp=1mod4, B85 suppliesr1>=3 andpowersr2>=r1. If total dimension<=6, both dimensions equal3 and both spaces agree. The two off-diagonals and their bracket force this common space to besl2, already excluded. Thus only the tame reducible sector acquires thep7 bound; other sectors and the unrestricted index{2,3} remain unchanged.'
 ],
 'dependencies_read_scope':'Complete B85 audit retained at outputs/root_B85_audit.json, including fresh B60/B69/B83 proof reads. The good-field determinant identity is the already audited B76/B77 convention, not a new independent source claim.',
 'original_reads':reads,
 'program':str(source.relative_to(w)),'program_sha256':sha(source),'isolated_program':str(dest.relative_to(w)),
 'author_output_sha256_before_and_after':before,'independent_output_sha256':sha(dest.with_suffix('.output.json')),
 'independent_runtime_seconds':independent['runtime_seconds'],'wall_seconds':wall,
 'author_runtime_seconds':original['runtime_seconds'],'all_mathematical_fields_equal':True,
 'counts':independent['counts'],'p5':independent['p5'],'executed_failures':[],
 'checkpoint_scope':'Audited post-build candidate only; no edit to frozen CP30 canonical paper and no premature promotion.'}
out.write_text(json.dumps(record,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 writer=csv.writer(f,delimiter='\t')
 for label in record['labels']:
  writer.writerow([label,now,record['reviewer'],'targeted proof check / opened original-source proofs / unchanged independent exact-program rerun','PASS: whole candidate and checker read; actual cyclotomic subfield, point stabilizer, uniformizer break and exact quotient average rederived. Original Stacks032A and Colmez2.12,3.7 full proofs read. Exact scope and unchanged matching outputs in outputs/root_B86_audit.json.'])
with (w/'notes/ROOT_SEARCH_LOG_30.md').open('a') as f:
 f.write('\n## Post-freeze B86 original-source verification at '+now+'\n\nRoot opened and read the complete displayed proof of Stacks Theorem10.160.8 (Tag032A), '+reads[0]['url']+', and Colmez, Corps locaux, '+reads[1]['url']+', Proposition2.12 with full proof on printedp11 and Proposition3.7 with its full two-divisibility proof on printedpp14-15. The opening field definition and Section3 perfect-residue hypothesis were checked: finite residue is not required. These are freshly read original passages, not theorem statements inferred from snippets. Linked Stacks formal-smoothness proofs were not newly read. The actual quotient-average formula applies to the totally ramified degree-p subextension of the genuine point field. Exact root web references, all source scopes and the separate candidate audit are retained in outputs/root_B86_audit.json. No frozen paper or bibliography was changed.\n')
print(json.dumps(record,indent=2))
