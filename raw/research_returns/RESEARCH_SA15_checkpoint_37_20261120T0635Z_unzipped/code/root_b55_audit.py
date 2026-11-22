"""Retain an isolated exact-arithmetic rerun and the completed root B55 proof audit."""
from pathlib import Path
import json,csv,datetime,hashlib,io,contextlib
w=Path(__file__).resolve().parents[1]
source=w/'agents/reduction_descent/code/verify_tame_minimal_wild_layer.py'
author=source.with_suffix('.output.json')
before=hashlib.sha256(author.read_bytes()).hexdigest()
text=source.read_text();needle="dest = Path(__file__).with_suffix('.output.json')"
assert text.count(needle)==1
target=w/'outputs/root_b55_exact_arithmetic.json';assert not target.exists()
executed=text.replace(needle,'dest = Path('+repr(str(target))+')')
snapshot=w/'code/audit_snapshots/verify_tame_minimal_wild_layer_at_root_audit.py'
assert not snapshot.exists();snapshot.write_text(executed)
stream=io.StringIO()
with contextlib.redirect_stdout(stream):
    exec(compile(executed,str(snapshot),'exec'),{'__file__':str(source),'__name__':'__main__'})
(w/'outputs/root_b55_exact_arithmetic_stdout.txt').write_text(stream.getvalue())
assert before==hashlib.sha256(author.read_bytes()).hexdigest()
run=json.loads(target.read_text());assert run['status']=='PASS'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
checks={
'lem:B-RD55-valuations': 'Complete valuation proof independently rederived. Residual irreducibility trivializes wild inertia modp; the common tame good-and-p-division field has degree t dividingp^2-1. The first-level Newton segment from(1,(p-1)t)to(p^2,0), after subtracting a nonzero first-level coordinate, has one slope giving all primitive second-level valuations t/((p+1)p^2). The finite division group over the tame field is exactly the wild elementary abelian matrix kernel, of rank<=4. Integral normalization forces its order divisiblebyp^2. At minimal orderp^2 the primitive valuation is A=t/(p+1), an integer prime top.',
'prop:B-RD55-minimal-wild': 'Complete proof independently rederived. For unequal normalized types, B53 forces the common faithful tame degreep^2-1, so primitive valuationA=p-1 and first-level valuationp^2A. Leading coefficients factor injectively throughR/pR and identify its image with a scalarF_(p^2), because multiplicationbyp raises leading coefficients tothep^2power and the first-level image is a scalarF_(p^2). Every wild automorphism fixesW(k). Its Teichmuller expansion change at any element of valuationA has exact leading valuationA+b and coefficientA*d_g*lead(x), sincep doesnotdivideA and allhigher degrees have valuation>=j+b. Thus every nonidentity wild element displaces every primitive point and all breaks equal(p^2-1)A. Formal subtraction and the p-series identify its matrix with multiplicationbykappa_i*d_g onF_(p^2). The faithful minimal wild image exhausts this field. The common second-level intertwiner induces the same map onR/pR andpR; unequal tame types force the nontrivial Frobenius-semilinear orientation by the fully rereadB53 leading-character lemma. It would identify Frobenius on the wholeF_(p^2)with scalar multiplication, impossible by evaluatingat1 and an elementoutsideF_p. Neither larger wild order is excluded.',
'rem:B-RD55-scope': 'Exact program fully read and isolated rerun retained. It checks3700 valuation cases,166 minimal integral cases,75984 field elements,75984 scalar candidates and1180 normalized orientation pairs forprimes5through101. The program gives only finite arithmetic support, no formal group or torsion-congruent pair. p5 excludeswild25 and leaves125/625 in the irreducible-residual branch; reducible residual cases remain. No CM or unrestricted least-index conclusion is imported.'
}
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for label,detail in checks.items():writer.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root','full mathematical/source/code audit','PASS. '+detail])
record={'status':'FULL MATHEMATICAL AND CODE PASS','actual_utc':now,'events':len(checks),
        'root_rerun_seconds':run['runtime_seconds'],'author_output_sha256_unchanged':before,
        'counts':{k:run[k] for k in ['valuation_cases','minimal_integral_cases','field_elements_checked','scalar_frobenius_candidates_excluded','distinct_type_orientation_pairs']},
        'source_scope':'Full B55 and B53 leading-coordinate and normalized-cycle proofs reread; prior actual Tate full-faithfulness and finite-tame-normalization source reads reused. The new Teichmuller and Newton arguments are proved directly.',
        'remaining_gate':'Irreducible-residual wild ordersp^3/p^4 and reducible-residual branch; no choice of unrestricted nu_min.'}
dest=w/'outputs/root_b55_audit.json';assert not dest.exists()
dest.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
