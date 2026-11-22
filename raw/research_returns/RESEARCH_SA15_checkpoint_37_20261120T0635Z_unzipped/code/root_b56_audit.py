"""Retain the completed root proof/code audit of the strengthened B56 candidate."""
from pathlib import Path
import json,csv,datetime,hashlib,io,contextlib
w=Path(__file__).resolve().parents[1]
source=w/'agents/reduction_descent/code/verify_tame_cubic_wild_layer.py'
author=source.with_suffix('.output.json')
before=hashlib.sha256(author.read_bytes()).hexdigest()
program=source.read_text()
needle="Path(__file__).with_suffix('.output.json').write_text"
assert program.count(needle)==1
target=w/'outputs/root_b56_exact_arithmetic.json'
assert not target.exists()
executed=program.replace(needle,'Path('+repr(str(target))+').write_text')
snapshot=w/'code/audit_snapshots/verify_tame_cubic_wild_layer_at_root_audit.py'
assert not snapshot.exists()
snapshot.write_text(executed)
stream=io.StringIO()
with contextlib.redirect_stdout(stream):
    exec(compile(executed,str(snapshot),'exec'),{'__file__':str(source),'__name__':'__main__'})
(w/'outputs/root_b56_exact_arithmetic_stdout.txt').write_text(stream.getvalue())
assert before==hashlib.sha256(author.read_bytes()).hexdigest()
run=json.loads(target.read_text())
assert run['status']=='PASS'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
checks={
'lem:B-RD56-anti-layer': 'Full current statement and proof read and independently rederived. For a cyclic irreducible residual representation on F_(p^2), End_Fp is the direct sum of the fixed Cartan plane and the anti-Cartan plane, on which conjugation has order h. For h>2 this plane is irreducible, so any invariant wild subspace of dimension three contains it and its lower filtration has one break. The elementary abelian extension by the tame cyclic group splits by the explicitly checked averaging correction. Primitive valuation A=p(p-1), first-level valuation p^2 A and e_F=(p^2-1)p^2 A follow from the fully reread B55 valuation lemma and B53 maximal joint degree. The tame multiplier eta=zeta^p satisfies eta^(p^3)=zeta. Averaging a uniformizer and the actual integral semilinear descent coordinates gives exact eigen-coordinates without assuming CM or changing the special Honda p-series.',
'prop:B-RD56-cubic-wild': 'Complete strengthened proof read and independently rederived, including the conditional h=2 extension. Fixed residue representatives from the base coefficient ring permit characteristic-p monomial calculations to precision qA because e_F>qA. Primitive expansions modulo pi^(qA) depend only on R/pR. On a full anti-Cartan plane with one break, g maps injectively and additively to d_g; nontrivial tame conjugation excludes b0=(p^2-1)(p-1). Every nonzero anti-Cartan matrix is invertible, so each primitive displacement has exact valuation qA. If b<b0, the unique possible cancellation degree is j0=A+(p-1)b; fixing nonzero z forces d_g^(p-1) constant on p^2-1 distinct nonzero values, impossible by the degree-p-1 polynomial root bound. If b>b0, only the first prime-to-p monomial j=qA-b can contribute, forcing beta_i(g)=kappa_i d_g. The unequal-type residual intertwiner is c times Frobenius by B53, and induces the same map on R/pR and pR under normalized p multiplication. Conjugation gives beta_2=c^(1-p) beta_1^p, contradicting scalar Frobenius on the entire F_(p^2). At h=2 the same proof applies only under the stated full-plane and single-break hypotheses; conjugation is -1 and still excludes b=b0. No lower/upper-break identification is used.',
'cor:B-RD56-p5': 'All six oriented normalized p=5 cases checked independently and by the retained exact program. The A/B comparison has residual projective order six and requires wild order625; the A/C comparison has projective order two and retains the necessary list125/625 unless the additional full-plane single-break hypothesis applies. The corollary makes no existence claim.',
'rem:B-RD56-scope': 'Current complete source and full finite program read. Isolated author-preserving rerun passed all2498 monomial first terms,2494 lower-break cases,2336 tame-weight cases,45864 explicit anti-Cartan conjugacies, and360 nonzero elements in four quadratic fields for the low-break cardinality diagnostic. These are finite arithmetic supplements only. Reducible residual representations, full wild orderp^4, and the unexcluded projective-order-two wild configurations remain open.'
}
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for label,detail in checks.items():
        writer.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root','full mathematical/source/code audit','PASS. '+detail])
record={
 'status':'FULL MATHEMATICAL AND CODE PASS',
 'actual_utc':now,'events':len(checks),
 'root_rerun_seconds':run['runtime_seconds'],
 'author_output_sha256_unchanged':before,
 'candidate_sha256':hashlib.sha256((w/'agents/reduction_descent/B_tame_cubic_wild_layer.tex').read_bytes()).hexdigest(),
 'counts':{k:run[k] for k in ['monomial_first_terms','lower_break_cases','tame_weight_cases','anti_Cartan_conjugacy_cases','low_break_cardinality_fields','low_break_nonzero_values']},
 'source_scope':'Complete strengthened B56, exact finite program, B53 leading-coordinate/cycle proof and B55 valuation proof actually read. Prior actual Tate full-faithfulness and Stacks032A coefficient-ring source reads reused; no new external source read is asserted by this audit.',
 'remaining_gate':'Irreducible residual projective order>2 requires full wild orderp^4. Projective ordertwo may also have orderp^3 outside the full anti-Cartan single-break case. Reducible residual branch remains; no unrestricted least-index value or pair existence proved.'
}
dest=w/'outputs/root_b56_audit.json'
assert not dest.exists()
dest.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
