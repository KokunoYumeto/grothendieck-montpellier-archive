"""Root residual-cycle proof audit and exact author-preserving rerun."""
from pathlib import Path
from contextlib import redirect_stdout
import csv,datetime,io,json,hashlib
w=Path(__file__).resolve().parents[1]
program=w/'agents/reduction_descent/code/verify_tame_residual_cycle.py'
author=program.with_suffix('.output.json');dest=w/'outputs/root_verify_tame_residual_cycle.json'
summary=w/'outputs/root_b53_audit.json'
assert not dest.exists() and not summary.exists()
before=author.read_bytes();old=Path.write_text;capture=io.StringIO()
def write(path,data,*args,**kwargs):
    assert path.resolve()==author.resolve()
    return old(dest,data,*args,**kwargs)
try:
    Path.write_text=write
    with redirect_stdout(capture):
        exec(compile(program.read_text(),str(program),'exec'),{'__name__':'__main__','__file__':str(program)})
finally:
    Path.write_text=old
    (w/'outputs/root_verify_tame_residual_cycle.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes()==before
out=json.loads(dest.read_text());assert out['status']=='PASS'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
events=[
 ('lem:B-RD53-leading','independent re-proof',
  'PASS: complete proof rederived. Normal wild p-subgroup invariants are nonzero by orbit counting and inertia-stable, so Fp-irreducibility kills wild inertia. A cyclic irreducible GL2(Fp) image is a subgroup of F_(p²)^units. Its tame p-division field and the faithful tame good field have compositum degree t dividingN=p²-1. Tate extends the descent maps as actual formal-model isomorphisms. Valuation subspaces of formal torsion are inertia-stable; irreducibility forces a common valuationA. The one-level Weierstrass product givesNA=(p-1)t. The leading-coordinate map is additive and injective because a nonzero difference cannot have higher valuation. Its field-action factor is zeta^((N/t)A)=zeta^(p-1), and its special tangent factor is zeta^c. Thus the residual orbit is{c+p-1,p(c+p-1)}. The special covariant orbit is{c,pc}; the previously audited covariant dictionary fixes the sign. This is irreducibility overFp, explicitly not absolute irreducibility.'),
 ('prop:B-RD53-cycle','independent re-proof',
  'PASS: full normalization, maximal-order and cycle proof rederived. The common nonsquare finite determinant differs from the level-one tame fundamental character by a square, so a common scalar twist makes c congruent1mod(p-1) and preserves residual irreducibility. Equal residual orbit with unequal special orbit forces c2=p*c1+(p-1)^2modN. The joint divisor gcd(N,c1,c2) divides(p-1)^2 and is coprime to(p-1), so is1. On c_j=1+(p-1)j, special Frobenius isj->1-j and the residual-match involution isj->-1-j. Their even representatives2k yield exactly neighborsk+1 ork-1 on the cycle of length(p+1)/2. Every abstract edge has the requisite residual eigenpair equality, but no BT or p²-congruence realization is inferred.'),
 ('cor:B-RD53-quadratic','independent re-proof',
  'PASS: entire parity proof and examples rederived. A quadratic twist addsn=(p+1)/2 to j. Ifn is even, it is the half-cycle translationk->k+n/2, not an edge forn>=4. Ifn is odd, it is the reflectionk->(1-n)/2-k with exactly one exchanged adjacent pair. Nonmaximal normalized joint degree is incompatible with irreducible residual inertia by the preceding maximal-order result. Thep7 order48 four-cycle andp5 triangle are correct; neitherp5 pattern is removed.'),
 ('rem:B-RD53-scope','targeted proof check',
  'PASS: all three mathematical statements and scope read. Reducible residual inertia remains allowed for potentially supersingular groups. The general least index stays in{1,2}, and no actual remaining pair is constructed. The code checks finite character and rational valuation arithmetic only.'),
 ('B53-EXACT-CERTIFICATE','computation or formal certificate',
  f"PASS: entire program read and independently rerun, author output unchanged, in {out['elapsed_seconds']}seconds. Checked {out['pair_count']} distinct type pairs and {out['valuation_cases']} rational valuation cases for all24primes5..101, including every cycle edge, maximal joint gcd, quadratic parity and exactp5/p7examples.")]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    for sid,kind,result in events:wr.writerow([sid,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort',kind,result])
record={'status':'FULL MATHEMATICAL AND CODE PASS','actual_utc':now,'elapsed_seconds':out['elapsed_seconds'],
        'events':len(events),'author_output_sha256_unchanged':hashlib.sha256(before).hexdigest(),
        'remaining_gate':'Irreducible residual inertia forces maximal joint good degree and adjacent normalized types; opposite quadratic types atp3mod4,p>=7 require reducible residual inertia. No exact unrestricted least index.',
        'source_scope':'B49 faithful-tame argument and the full B12 one-level valuation proof reread. Previously audited Tate extension and covariant comparison used, without claiming a new opening of those originals. New residual-cycle algebra proved directly; fresh searches recorded separately.'}
summary.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
