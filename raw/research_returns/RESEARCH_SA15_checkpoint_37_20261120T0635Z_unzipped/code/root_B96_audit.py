"""Record the complete root actual-field proof and exact-code audit of B96."""
from pathlib import Path
import csv, datetime, hashlib, json, shutil, subprocess, sys, time
w=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
candidate=w/'agents/reduction_descent/B_full_Iwahori_selected_point_candidate.tex'
source=w/'agents/reduction_descent/code/verify_full_Iwahori_selected_point.py'
author=source.with_suffix('.output.json')
expected='a56221d040b93f4550b5dcd1cd78fe0ad8dcd833aba3020ed04299da5157778e'
assert sha(candidate)==expected
assert sha(source)=='37f77e0e5eb715602a7c9e63b5ce10f294d974a9b7de21d944a1fc25647f4da5'
assert sha(author)=='7f100c57ea15a459f73de7fa1d06278aa660d4d6e6738845ecd541438fb721ea'
before={str(p.relative_to(w)):sha(p) for p in [candidate,source,author]}
folder=w/'code/audit_snapshots/B96_root_independent';assert not folder.exists();folder.mkdir(parents=True)
copy=folder/source.name;shutil.copy2(source,copy)
snapshot=w/'notes/root_B96_audited_candidate.tex';out=w/'outputs/root_B96_audit.json'
assert not snapshot.exists() and not out.exists();shutil.copy2(candidate,snapshot)
started=time.perf_counter();run=subprocess.run([sys.executable,str(copy)],cwd=w,capture_output=True,text=True);wall=time.perf_counter()-started
(w/'outputs/root_B96_independent.stdout.json').write_text(run.stdout)
(w/'outputs/root_B96_independent.stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
independent=copy.with_suffix('.output.json')
a=json.loads(author.read_text());b=json.loads(independent.read_text())
mathpart=lambda x:{k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
assert a['status']==b['status']=='PASS' and mathpart(a)==mathpart(b)
assert before=={str(p.relative_to(w)):sha(p) for p in [candidate,source,author]}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['lem:B-RD96-selected','lem:B-RD96-opposite','prop:B-RD96-conductor','lem:B-RD96-gap','thm:B-RD96-residual-wild','rem:B-RD96-scope']
r={
 'status':'FULL-INDEPENDENT-PROOF-CODE-PASS','actual_utc':now,
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'read_scope':'Entire six-label actual-field candidate fully read; exact total-ramification repair and final certificate paragraph read against retained diffs. Entire unchanged exact supplement read. Full B94 common-high proof and B87 coefficient/quotient lemma freshly reread. The complete B94/B95 root audits, including their B49/B60/B69 actual Newton and fixed-coefficient dependencies, were already performed and retained.',
 'proof_checks':[
  'B91-B95 leave an actual subgroup of the displayed Iwahori group whose exact order is5^9, the order of that group. Equality is therefore justified; there is no trace or determinant relation among the nine digits. For the original selected high125 point the exact stabilizer is a=w=0; for its25 multiple it is a0=w0=0. Adjoining the residual v0 field gives S and T of degrees125 and3125 over L. On the S subgroup, direct multiplication makes a1,w1 independent additive homomorphisms with the asserted joint kernel, proving Galois normality of T/S as well as the degrees.',
  'The quotient orientation uses only the actual image M[125]/H of type125 plus25. The selected point q(e2/125) has order125 because its25 multiple was outside H, and its resulting first-level point is the old canonical high line. In the reordered quotient lattice(e2,e1/5), the first column is(1+5d,5v), known modulo125 from the original comparison. Its stabilizer is exactly v0=v1=d0=d1=0; its25 multiple has v0=d0=0. Adjoining quotient residual w0 gives the same S,T degrees, and d1,v1 are the actual independent relative translations. No full Q[125] representation is supplied or used.',
  'Both successive high inverse polygons are single segments: target values are5(24-b), then(24-b)/5 and(24-b)/125 over L. The degree5 coefficient value20b lies strictly above the chords since b>4; the full other-vertex bound is the previously audited coefficient lemma. Rescaling to T gives A=25(24-b), low displacement3125b, high displacement15625(24-b), and v_T(5)=1500000. Formal-coordinate subtraction has the same valuation as translation by the torsion point.',
  'The opposite low25 point field is an actual degree125 field over L and elementary abelian of degree25 over its residual field. Its two tame weights are distinct. A single ramification break would put the two different eigenvalues in the same leading-coefficient scalar eigenspace, impossible. If both parameters are prime to5 and the last line were not high, the complete B87 coefficient lemma would force the same maximal cyclic quotient conductor24m for two unequal m.',
  'For the mixed opposite pair(15,19), the leading exponent75 has5-adic order2. The exact candidate change at h is min(75+25h,N+5h,J+h), allowing missing N,J. The prime row gives u+4t=2280. Every possible tie at the first break then forces the last displacement of the mixed row strictly above1875, including the three-way and missing-coefficient cases. Thus its last line is also high. The numerical B94 common-high argument depends only on these actual coordinate rows and high-last property, not tracefreeness. It gives the five stated t-prime,C-prime values; in the mixed row0<t-prime<360 and tame invariance gives multiples24 through336.',
  'On the subgroup over the opposite residual field R_*, the three original-orientation functions v0,a0,w1 are independent additive characters. The low25 field uses a0,w1 and S uses v0,a0. Outer opposite-root conjugation adds a multiple of v0 to a0, so conductor invariance gives sigma<=t-prime; distinct tame weights exclude equality. High-last gives t-prime<C-prime. The quotient orientation has the exactly analogous actual functions w0,d0,v1; its availability comes from the selected point, not an unprovided torsion level.',
  'The actual three-character compositum has distinct upper breaks sigma,t-prime,C-prime. Restriction of the off-diagonal character to S has conductor psi_S/R*(C-prime)=25C-prime-20t-prime-4sigma>25C-prime-24t-prime. Its actual field is SZ=S(w1), or S(v1), which is exactly the cyclic quotient of T/S killing the high translation line. Thus the Herbrand conversion is performed on the correctly identified character and base. The five lower bounds7086,8814,11118,16266,28866 are obtained from these actual opposite fields.',
  'The abstract gap lemma now explicitly assumes total ramification, as required for fixed residue representatives in O_S and as satisfied in every application. Below v_T(5), every5-divisible exponent changes no earlier than A+5h; the first ordinary exponent J changes uniquely at J+h when first. A single break larger than all Delta/5 would give the same low and high displacement, impossible.',
  'With two breaks t<u and last line different from H, choose minimal Delta. The unconditional coordinate bound gives u<=Delta; if t>Delta/5, the unique ordinary term at u is already uniquely first at t and contradicts the high displacement. Therefore t<=Delta/5 and the quotient-average formula gives z=(u+4t)/5<=9Delta/25, contradicting the first strict hypothesis. Hence the last line is H and t=z. The second strict hypothesis makes the ordinary term uniquely first at t and then at u, since all divisible terms increase at least5 times as fast. Thus D1-D0=u-t in every coordinate, including missing early ordinary coefficients and cutoff endpoints.',
  'For each of the five orientations the actual lower bound for z is strictly above both9minDelta/25 and maxDelta/5, as displayed. The forced equal gaps are375000-18750b_i, unequal for different b_i. The necessary finite-character census has exactly ten rows, paired by sorted opposite orientation into these five cases. This excludes every remaining full-Iwahori residual-wild comparison, together with the earlier reductions. It leaves the residual-irreducible wild orders5^5 through5^8 unexcluded and makes no unrestricted least-index claim.',
  'The finite supplement enumerates all1953125 actual Iwahori matrices and15 actual field-image maps; its direct vector tests and literal relative products verify both stabilizer constructions, with independent binomial and rational Herbrand arithmetic. The program is unchanged and all mathematical output agrees in the isolated rerun. These checks supplement the complete actual-field proof and do not infer existence or ramification from a finite sample.'
 ],
 'dependencies_rechecked':['lem:B-RD94-common-high','lem:B-RD87-coefficient'],
 'source_scope':'No fresh external primary-source opening is claimed. Complete Colmez Proposition3.7, Theorem3.10 and Proposition3.13(ii), pp14-16, were opened/read in the retained prior ramification audits; their actual-field quotient and subgroup uses have been rederived here.',
 'scope_repair':'The general coefficient lemma was restricted explicitly to totally ramified extensions, at root request. Exact prior and diff: agents/reduction_descent/notes/B96_total_ramification_scope_repair/. Every actual application already has algebraically closed residue field.',
 'program_sha256':sha(source),'author_output_sha256':sha(author),'author_bytes_unchanged':True,
 'independent_program':str(copy.relative_to(w)),'independent_output':str(independent.relative_to(w)),
 'independent_output_sha256':sha(independent),'independent_runtime_seconds':b['runtime_seconds'],
 'author_runtime_seconds':a['runtime_seconds'],'subprocess_wall_seconds':wall,
 'all_mathematical_output_identical':True,'counts':b['counts'],'executed_failures':[],
 'scope_guard':'At p5,e20, residual-wild actual125 comparisons of the normalized whole potentially supersingular height-two groups with different finite special characters are excluded. The irreducible-residual sector and unrestricted least index in{2,3} remain open; general B.4 is not closed.'
}
out.write_text(json.dumps(r,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:
  wr.writerow([label,now,r['reviewer'],'independent re-proof / computation or formal certificate','PASS: full selected-point actual-field proof and unchanged isolated exact supplement. See outputs/root_B96_audit.json.'])
 for label in r['dependencies_rechecked']:
  wr.writerow([label,now,r['reviewer'],'used and rechecked in this run','PASS: full numerical coefficient proof reread; actual rows/high-last hypotheses verified without a tracefree relation.'])
print(json.dumps({k:r[k] for k in ['status','actual_utc','candidate_sha256','independent_runtime_seconds','all_mathematical_output_identical','counts']},indent=2))
