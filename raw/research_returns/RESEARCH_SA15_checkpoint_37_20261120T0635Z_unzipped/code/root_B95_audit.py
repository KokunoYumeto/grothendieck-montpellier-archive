"""Full root proof/code audit of the remaining tracefree rows."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil,subprocess,sys,time
w=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
candidate=w/'agents/reduction_descent/B_remaining_tracefree_rows_candidate.tex'
source=w/'agents/reduction_descent/code/verify_remaining_tracefree_rows.py'
author=source.with_suffix('.output.json')
expected='7967d6fbaffaef6eb32fa250ae9e24d403fd0424ff013bdfd79fbca9e1461a86'
assert sha(candidate)==expected
assert sha(source)=='e229c00b9a5f8071f07a8ce9335844cd42de1c96471f383e399e627437d724bd'
assert sha(author)=='b30398a4d20e31630bc39fdff7527b2fab68890f439bcf3dd21217183542fd5e'
before={str(p.relative_to(w)):sha(p) for p in [candidate,source,author]}
folder=w/'code/audit_snapshots/B95_root_independent';assert not folder.exists();folder.mkdir(parents=True)
copy=folder/source.name;shutil.copy2(source,copy)
snapshot=w/'notes/root_B95_audited_candidate.tex';out=w/'outputs/root_B95_audit.json'
assert not snapshot.exists() and not out.exists();shutil.copy2(candidate,snapshot)
started=time.perf_counter();run=subprocess.run([sys.executable,str(copy)],cwd=w,capture_output=True,text=True);wall=time.perf_counter()-started
(w/'outputs/root_B95_independent.stdout.json').write_text(run.stdout)
(w/'outputs/root_B95_independent.stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
independent=copy.with_suffix('.output.json')
a=json.loads(author.read_text());b=json.loads(independent.read_text())
mathpart=lambda x:{k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
assert a['status']==b['status']=='PASS' and mathpart(a)==mathpart(b)
assert before=={str(p.relative_to(w)):sha(p) for p in [candidate,source,author]}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['lem:B-RD95-critical','prop:B-RD95-profiles','thm:B-RD95-tracefree','rem:B-RD95-scope']
r={
 'status':'FULL-PROOF-CODE-PASS','actual_utc':now,
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'read_scope':'Entire four-label candidate and complete exact verifier actually read. The corrected two-sentence direction of the compositum filtration was separately read. The entire B94 proof/code and all its explicitly recorded coefficient, quotient, normality and cyclotomic dependencies were freshly read in the immediately preceding full root audit.',
 'proof_checks':[
  'The two actual25 division fields may be named critical and opposite so their parameter pairs are(a,15) and(9,24-a), with a=7 or11. This is a relabeling of existing fields supplied by the original125 comparison. It supplies no quotient125 torsion.',
  'Normality from B94 makes the last translation line high. If the first break differs from24a, the prime-parameter strict coefficient regimes give z>15000-726a, hence z>5550. The second coordinate has value75 divisible by5 and high displacement5625, so the strict B60 bound gives z<5550. Thus t=24a, including the critical boundary rather than assuming its ordinary coefficient nonzero.',
  'If z>1110, the degree75 term has p-adic order2 and starts at75+25z below the mixed-characteristic cutoff, while every other5-divisible term can start no earlier than80+5z. Both exceed5625. The unique first ordinary exponent is therefore J=5625-z. At the smaller break, the leading degree75 change is later than1875 and all other divisible changes are at least80+5t<1875. If J+t were below this threshold it would be uniquely first, contradicting the displacement1875. Hence z<=5545-4t and C=(z+4t)/5<=1109. The case z<=1110 satisfies an even smaller bound.',
  'The off-diagonal character in the critical orientation has tame weight zeta^6. Its actual cyclic field over the residual field has total degree25 over L, so the tame uniformizer has eigenvalue zeta. The injective leading coefficient map therefore gives C=6 mod24, sharpening the bound to1086. The proof uses no distribution assumption about possible conductors.',
  'The opposite prime-parameter pair has diagonal216 and off-diagonal858 or1362. Equality of the two actual restricted diagonal characters gives216=24a+4(r-r-prime). Combining the two opposite tame residue classes with the strict actual residual bounds gives r in{30,54,78}, r-prime=r-12 for a7, and r in{6,30,54,78,102,126}, r-prime=r+12 for a11. All diagonal ordering inequalities hold on these necessary lists.',
  'The two field filtrations share their first three upper breaks and have last breaks beta,gamma. Equality would require C=810 for a7, incompatible with C=6 mod24; for a11 it would require C=1410, beyond the bound. Between the two last breaks only the kernel line with the larger break survives, and above both the group is trivial. Below both, their independent lines and the common degree125 quotient determine every order. Integrating1,5,25,125,625 yields the stated lower-break and conductor formulas; the largest upper break is at most1914/5<576.',
  'The actual original primitive125 point fields and stabilizers remain exactly those of B94. In either orientation E/S_h has the two root lower breaks V_o,W_o. The same high-point bound, after restriction above its last break, is78000*j_min-4V_o. The actual cyclic25 lower-root field E/E_low has lower breaks R_o,W_o and gives78000*b_min-4W_o-20R_o. No primitive125 point is taken from a quotient module that is only known at level25.',
  'All four uniform threshold bounds follow from the displayed linear formulas on the exact endpoint ranges, splitting a7 at810. They are strictly below their point-field bounds, validating every Herbrand restriction. The same terminal characters a1,d1 are thus bounded in every orientation, while their sum is the actual cyclotomic character with exact conductor psi_E(576).',
  'Direct symbolic subtraction gives all eight positive gap expressions. The a7 expressions agree on both sides of810. Their minima are positive using r<=78 or126 and C<=1086; the smallest a1 and d1 gaps are47880 and50400. Thus the remaining four(3,4) pairs are excluded. Together with B91-B94 this leaves residual-wild shape(4,4), whose actual order equals the5^9 order of the containing Iwahori group, proving equality of the image in that branch.',
  'The standalone verifier uses independent rational Herbrand integration for all654 necessary profiles, exact26 binomial coefficients and1736 critical-bound implications. It checks every closed gap and threshold formula. These finite arithmetic profiles remain necessary possibilities, not realizations; the field and coefficient arguments are supplied in the proof.'
 ],
 'dependencies_reused_from_immediately_preceding_full_audit':['lem:B-RD94-group','lem:B-RD94-ordering','lem:B-RD94-common-high','prop:B-RD94-profiles','lem:B-RD94-terminal','thm:B-RD94-six-rows'],
 'source_scope':'No fresh external primary-source opening claimed. The full B94 root audit records the freshly read complete B49/B60/B69/B86/B91/B92 dependencies, with their retained prior original-source readings.',
 'wording_correction':'agents/reduction_descent/notes/B95_filtration_wording_repair/record.json; the larger-break line survives between the two breaks, and above the larger break the group is trivial. Displayed mathematics and checker unchanged.',
 'program_sha256':sha(source),'author_output_sha256':sha(author),'author_bytes_unchanged':True,
 'independent_program':str(copy.relative_to(w)),'independent_output':str(independent.relative_to(w)),
 'independent_output_sha256':sha(independent),'independent_runtime_seconds':b['runtime_seconds'],
 'author_runtime_seconds':a['runtime_seconds'],'subprocess_wall_seconds':wall,'all_mathematical_output_identical':True,
 'profiles':b['profiles'],'critical_bound_checks':b['critical_bound_checks'],'binomial_checks':b['binomial_checks'],
 'minimum_a_gap':b['minimum_a_gap'],'minimum_d_gap':b['minimum_d_gap'],'executed_failures':[],
 'scope_guard':'The residual-wild(3,4) branch is excluded, leaving actual full Iwahori order5^9 in the residual-wild sector. That branch is neither excluded nor realized; irreducible residual orders5^5 through5^8 and the unrestricted least index in{2,3} remain open.'
}
out.write_text(json.dumps(r,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:
  wr.writerow([label,now,r['reviewer'],'targeted proof check / computation or formal certificate','PASS: full proof and unchanged exact654-profile rerun. Only residual-wild(3,4) eliminated. See outputs/root_B95_audit.json.'])
 for label in r['dependencies_reused_from_immediately_preceding_full_audit']:
  wr.writerow([label,now,r['reviewer'],'used and rechecked in this run','PASS: actual-field and conductor argument applies to both explicitly typed25-field orientations, without assuming quotient125 torsion.'])
with (w/'notes/checkpoint35_changes.md').open('a') as f:
 f.write('\n## Root full B95 proof and exact-code audit\n\nThe final four-label candidate passed at '+now+'. Its unchanged isolated verifier took '+str(b['runtime_seconds'])+' seconds for654 profiles,1736 critical-bound checks and26 binomial coefficients. The eight symbolic conductor gaps have minimum a1 margin47880 and minimum d1 margin50400. The exact filtration-wording repair is retained. This excludes the four remaining(3,4) rows once companion audit and promotion are complete. The full residual-wild Iwahori5^9 branch and irreducible residual branches remain undecided; no least-index equality is claimed.\n')
print(json.dumps({k:r[k] for k in ['status','actual_utc','independent_runtime_seconds','all_mathematical_output_identical','profiles','critical_bound_checks','binomial_checks','minimum_a_gap','minimum_d_gap']},indent=2))
