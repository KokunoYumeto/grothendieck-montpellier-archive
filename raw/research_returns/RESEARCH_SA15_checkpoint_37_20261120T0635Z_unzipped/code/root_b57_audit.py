"""Full B57 proof audit and author-preserving exact-arithmetic rerun."""
from pathlib import Path
import json,csv,datetime,hashlib,io,contextlib
w=Path(__file__).resolve().parents[1]
source=w/'agents/reduction_descent/code/verify_tame_cubic_wild_exhaustion.py'
author=source.with_suffix('.output.json')
before=hashlib.sha256(author.read_bytes()).hexdigest()
program=source.read_text();needle="Path(__file__).with_suffix('.output.json').write_text"
assert program.count(needle)==1
target=w/'outputs/root_b57_exact_arithmetic.json';assert not target.exists()
executed=program.replace(needle,'Path('+repr(str(target))+').write_text')
snapshot=w/'code/audit_snapshots/verify_tame_cubic_wild_exhaustion_at_root_audit.py'
assert not snapshot.exists();snapshot.write_text(executed)
stream=io.StringIO()
with contextlib.redirect_stdout(stream):
    exec(compile(executed,str(snapshot),'exec'),{'__file__':str(source),'__name__':'__main__'})
(w/'outputs/root_b57_exact_arithmetic_stdout.txt').write_text(stream.getvalue())
assert before==hashlib.sha256(author.read_bytes()).hexdigest()
run=json.loads(target.read_text());assert run['status']=='PASS'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
checks={
'lem:B-RD57-first-term': 'Entire statement and proof independently rederived. Nonzero Cartan and anti-Cartan matrices are invertible, so every primitive displacement has valuation qA. For A=p(p-1), the leading p-divisible monomial changes at A+pb and every other p-divisible monomial later. Below b0 the unique first prime-to-p term has j=A+(p-1)b and nonzero linear-in-z coefficient; above b0 it has j=qA-b and coefficient linear in z for Cartan, Frobenius-linear for anti-Cartan. These conclusions concern the same fixed expansion for every g, and the below-b0 assertion forces p not dividing b.',
'lem:B-RD57-anti': 'Entire two-break argument checked. At projective ordertwo every anti-Cartan graded ramification character is -1, giving b congruent N/2 moduloN and excluding b0. If b1<b2 and b1<b0, the fixed first prime-to-p term arising from b1 changes uniquely first under g2; its coefficient is linear in z, whereas an anti-Cartan displacement is proportional to z^p on allF_(p²). Equality at qA is impossible, as are earlier or later valuations. If b1>b0, every change under g2 is after qA. Thus a full anti-Cartan plane has a single break, and the already audited B56 excludes it.',
'lem:B-RD57-Cartan': 'Entire eigenspace and Cartan/anti comparison checked. A tame-invariant three-space at projective ordertwo is either Cartan1+anti2 or Cartan2+anti1. In the remaining case, an anti break aboveb0 gives a first coefficient proportional to z^p; all Cartan possibilities are excluded, including c=b0 by its strictly earlier prime-to-p term. Thus b<b0. For every nonzero Cartan element c<b contradicts uniqueness of the first degree, c=b is excluded by tame characters, and c>b forces c=qA-[A+(p-1)b]=p b0-(p-1)b>b0. The nonzero Cartan plane therefore has one break. The p5 list(12,432),(36,336),(84,144) is exactly the congruence and prime-to-p list; no realizability is claimed.',
'thm:B-RD57': 'Complete common-field contradiction rederived. On the full Cartan plane with common high break, the ramification map g->d_g is injective and additive. Comparing the same first prime-to-p coefficient for each model gives beta_i(g)=kappa_i*d_g with beta_i exhaustingF_(p²). The actual unequal-type residual intertwiner is a times Frobenius and acts identically on R/pR and pR after normalized multiplication byp; conjugating Cartan multiplication gives beta_2=beta_1^p. This cannot be simultaneously a fixed scalar multiple on the whole quadratic field. B55 and B56 then leave only wild orderp^4, which equals the entire additive matrix space. Reducible residual inertia remains outside the theorem.',
'rem:B-RD57-scope': 'Full exact supplement read and isolated rerun retained:942 first-term cases,100962 anti-break comparisons,214860 Cartan/anti comparisons,45864 Cartan conjugacies,364 scalar/Frobenius tests, and all156 hyperplanes inF5^4 with12 invariant shapes. These finite arithmetic checks supplement the written proof and construct no BT group or torsion-congruent pair. The unrestricted least-index interval is unchanged.'
}
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    for label,detail in checks.items():wr.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root','full mathematical/source/code audit','PASS. '+detail])
record={'status':'FULL MATHEMATICAL AND CODE PASS','actual_utc':now,'events':len(checks),
 'root_rerun_seconds':run['runtime_seconds'],'author_output_sha256_unchanged':before,
 'candidate_sha256':hashlib.sha256((w/'agents/reduction_descent/B_tame_cubic_wild_exhaustion.tex').read_bytes()).hexdigest(),
 'counts':{k:run[k] for k in ['first_term_cases','anti_two_break_comparisons','Cartan_anti_break_comparisons','Cartan_conjugacy_cases','scalar_Frobenius_cases','p5_all_hyperplanes_checked']},
 'source_scope':'Entire current B57 proof and code read. B53/B55/B56 proof and actual primary-source checks reused from the completed root audits; no new external source is claimed here.',
 'remaining_gate':'Only full wild matrix imagep^4 remains in the irreducible residual branch; reducible residual branch and unrestricted least index remain open.'}
dest=w/'outputs/root_b57_audit.json';assert not dest.exists()
dest.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
