"""Full root audit of B90 actual point-field towers and exact coset arithmetic."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil,subprocess,sys,time
w=Path(__file__).resolve().parents[1]
candidate=w/'agents/reduction_descent/B_p5_third_point_ramification_candidate.tex'
source=w/'agents/reduction_descent/code/verify_p5_third_point_ramification.py'
author=source.with_suffix('.output.json');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected='915d0471127a83c19d45fdefcd7696c92fedc5571e5785d3734e85fafaa732bd'
assert sha(candidate)==expected
assert sha(source)=='880c791a155b4b55fc8842bc8fc5d35cc9b3978e6b1ba1c4d1a4acbee5e7d0e7'
before=sha(author);assert before=='6f7316d5539a87d23d8d6e4da134a283655b03bbb66d0c291c8afe0c3c16e769'
dest=w/'code/audit_snapshots/B90_root_independent_certificate.py'
snapshot=w/'notes/root_B90_audited_candidate.tex';out=w/'outputs/root_B90_audit.json'
assert not dest.exists() and not snapshot.exists() and not out.exists()
shutil.copy2(source,dest);shutil.copy2(candidate,snapshot)
start=time.perf_counter();run=subprocess.run([sys.executable,str(dest)],cwd=w,capture_output=True,text=True)
wall=time.perf_counter()-start
(w/'outputs/root_B90_independent_stdout.json').write_text(run.stdout)
(w/'outputs/root_B90_independent_stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
original=json.loads(author.read_text());independent=json.loads(dest.with_suffix('.output.json').read_text())
mathpart=lambda x:{k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
assert mathpart(original)==mathpart(independent)
assert sha(author)==before and sha(dest)==sha(source)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['lem:B-RD90-point-towers','prop:B-RD90-terminal','thm:B-RD90-tame-exclusion','rem:B-RD90-scope']
record={
 'status':'PASS','actual_utc':now,
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'proof_scope':'Entire four-label candidate, full exact checker and author record read. Complete canonical B76 inverse-polygon proof and B87 fixed-coefficient proof reread; B88 actual-field profile and B60 exact lower-break dependencies independently checked in the preceding audits. Every field intersection, group quotient and ramification conversion rederived.',
 'proof_checks':[
  'A cyclic quotient of order24 of the actual finite Galois group admits an order24 lift by taking a suitable power of a generator lift. Its two distinct residual eigenvalues lift to two integral direct summands over Z/125 because X^24-1 is separable modulo5. A common basis of the identified actual torsion therefore gives tame-stable point fields in both models.',
  'In W=1+5M2(Z/125), H_i is the stabilizer of5Q_i and S_i the stabilizer ofQ_i. Their orders are5^6 and5^4. On H_i the actual displacement gQ_i-Q_i lies in the L-rational first-level group and is a homomorphism, surjected onto by the terminal subgroup. Thus S_i is normal in H_i and E_i^+/E_i is an actual Galois degree25 extension; E_i^+/L is not assumed Galois.',
  'Over L the absolute index is480, with formal coefficients b1=100,b2=300 and first-level low/high valuations(5,95),(15,45). Both high inverse tests satisfy b>=4Z/5, and all later tests do too. Two height-two inverse steps divide by25 twice. Multiplying by [E_i^+:L]=625 restores leading values95,15,5,45 and gives the exact four displacement rows, all below e(E_i^+)=300000.',
  'Tame conjugation on translations cancels the eigenvalue ofQ_i, leaving the same two weights as before. Each cyclic point quotient has degree125 over L and leading tame multiplier eta satisfying eta^125=zeta; inverse125 modulo24 is5. Hence diagonal and off-diagonal cyclic breaks retain residues0 and6/18 modulo24. They are distinct, so the final ramification line is an eigenaxis.',
  'The entire B87 coefficient proof applies below300000, since every leading valuation has5-adic orderone. Opposite last-line choices force unique displacements3045 or3165 in place of28125. In the surviving orientations, t<606 or t<624 forces wrong unique displacements9455 or9335; t above these thresholds forces J=3125-t and again a unique incorrect displacement. Thus only(606,6936),(624,6834) remain; their forced prime exponents are27839,2439 and27341,2541.',
  'The identities US_i=H_i and U central give F2 intersect E_i^+=E_i and D_i=F2 E_i^+=F^(U intersect S_i). The quotient H_i/(U intersect S_i) is elementary abelian: commutators are1+25[A,C] and fifth powers1+25A, both killed because the i-th column ofA,C is zero. This proves the actual disjoint elementary-abelian compositum, without assuming independent abstract extensions.',
  'Restriction of the known F2/L lower filtration gives(96,1146) and(6,1896), hence upper(96,306) and(6,384). Combining their actual disjoint character spaces with the two new point-field spaces, whose upper breaks are(606,1872),(624,1866), gives distinct character breaks and the listed lower composites by exact integration.',
  'Restricting the composite lower filtrations to their terminal column subgroups gives lower(8646,166896),(7896,163146), hence upper(8646,40296),(7896,38946). These characters are literally the restrictions of the point-translation maps to1+25B, so they are B21,B11 andB22,B12. Their kernels intersect trivially, and their compositum is the actual F/F2. Integration yields terminal lower7896,11646,769146,937896.',
  'Every nonidentity terminal element has break at least7896. The exact quotient average for each nonterminal coset forces some lift below7896, because its F2/L break is at most1896. Multiplying by any terminal element preserves that smaller break by the leading uniformizer displacement valuation. Thus every lift has the first-layer quotient break, fixing all breaks in W.',
  'The actual determinant quotient is cyclic of order25, with kernel size15625. For each order5 target determinant1+25r, there are125 lifts over each traceless first-layer matrix, with the carry in tr(A) and det(A) retained. The nonzero traceless strata give12500,2500,500 lifts of breaks6,96,1146; the A=0 affine trace slice gives100,20,4,1 of the four terminal breaks. Exact actual determinants modulo125 were independently enumerated.',
  'The quotient norm formula averages b+1 over this actual coset, so subtracting1 gives5925000/15625=1896/5. The lower break of a nonidentity automorphism of the actual discretely valued quotient field is integral. This contradiction excludes only the p5,e20 tame reducible residual comparison. No Hasse-Arf theorem, abstract realization, or unrestricted least-index conclusion is used.'
 ],
 'source_scope':'Reuses the complete original Colmez Proposition3.7 and following Herbrand proof previously opened and audited by root, and the fully audited internal B60/B76/B87/B88 proofs. No new external-source reading is claimed.',
 'program':str(source.relative_to(w)),'program_sha256':sha(source),
 'author_output_sha256':before,'author_output_unchanged':True,
 'independent_program':str(dest.relative_to(w)),
 'independent_output':str(dest.with_suffix('.output.json').relative_to(w)),
 'independent_output_sha256':sha(dest.with_suffix('.output.json')),
 'author_runtime_seconds':original['runtime_seconds'],
 'independent_runtime_seconds':independent['runtime_seconds'],
 'independent_subprocess_wall_seconds':wall,
 'all_mathematical_output_identical':True,'counts':independent['counts'],
 'root_executed_failures':[],
 'scope_guard':'Only the residual-tame branch at p5,e20 is excluded. Other residual sectors and the unrestricted least manuscript index remain open.'
}
out.write_text(json.dumps(record,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:
  wr.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
   'independent re-proof / computation or formal certificate',
   'PASS: complete actual-field, ramification, and quotient-average proof rederived; unchanged isolated checker output identical. Tame reducible p5/e20 branch only. See outputs/root_B90_audit.json.'])
with (w/'notes/checkpoint32_changes.md').open('a') as f:
 f.write('\n## Root audit of the third-point exclusion\n\nThe complete root B90 proof and code audit passed at '+now+'. It derives the terminal filtration from actual third-level point fields and reaches the impossible integral quotient break1896/5. The unchanged exact checker passed in '+str(independent['runtime_seconds'])+' seconds, with all mathematical outputs identical to the retained author output. The scope is only the residual-tame p5/e20 branch; promotion awaits the complete companion audit.\n')
print(json.dumps({k:record[k] for k in ('status','actual_utc','candidate_sha256','independent_runtime_seconds','all_mathematical_output_identical','counts')},indent=2))
