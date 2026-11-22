"""Full B60/B61 proof audit and author-preserving arithmetic rerun."""
from pathlib import Path
import json,csv,datetime,hashlib,io,contextlib
w=Path(__file__).resolve().parents[1]
source=w/'agents/reduction_descent/code/verify_tame_reducible_recovery.py'
author=source.with_suffix('.output.json')
before=hashlib.sha256(author.read_bytes()).hexdigest()
program=source.read_text()
needle="Path(__file__).with_suffix('.output.json').write_text"
assert program.count(needle)==1
target=w/'outputs/root_b60_b61_exact_arithmetic.json'
assert not target.exists()
executed=program.replace(needle,'Path('+repr(str(target))+').write_text')
snapshot=w/'code/audit_snapshots/verify_tame_reducible_recovery_at_root_audit.py'
assert not snapshot.exists()
snapshot.write_text(executed)
stream=io.StringIO()
with contextlib.redirect_stdout(stream):
    exec(compile(executed,str(snapshot),'exec'),{'__file__':str(source),'__name__':'__main__'})
(w/'outputs/root_b60_b61_exact_arithmetic_stdout.txt').write_text(stream.getvalue())
assert before==hashlib.sha256(author.read_bytes()).hexdigest()
run=json.loads(target.read_text())
assert run['status']=='PASS'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
checks={
 'lem:B-RD60-break':'The complete fixed-coefficient uniformizer expansion was independently checked. Residue representatives lie in the smaller field and are fixed by g. The degree-A term changes at A+b exactly when p does not divide A; for p dividing A, its linear binomial coefficient has positive valuation and all higher terms change strictly later. Higher expansion terms cannot cancel the unique first term in the prime-to-p case. The bound concerns each actual lower break and uses no upper/lower identification.',
 'lem:B-RD60-Newton':'The normalized nonsquare determinant, tame field of degree N, and universal series from the previously source-audited B49 were checked. A single Newton slope makes leading coordinates injective, kills wild inertia, and gives an irreducible or scalar tame plane; scalar would have square residual determinant, impossible since mu_p lies in K. Two slopes give the invariant high line, rational over L, hence integral alpha=N-B and b=(p-1)B, with 0<B<p(p-1). Averaging preserves the degree-p coefficient valuation b<e. Compatibility gives sigma(a_p)=zeta^((p-1)c)a_p, B=c mod(p+1), and high character zeta^(c-B). The low primitive p-squared points have one Newton slope B/p^3. All coordinate changes preserve positive valuations.',
 'prop:B-RD60-residual-break':'Residual reducibility gives a triangular group and residual wild image either trivial or C_p. In the wild case the unique fixed line is the high line. A low point has v_R=B and its nonzero wild displacement has v_R=p(N-B), so the exact or strict lower-break formula follows. Equal high-line characters recover c when both B are prime to p or both divisible by p. In the mixed case the common break strictly forces B_nondivisible>B_divisible.',
 'lem:B-RD61-point-field':'Over the full p-division field, the actual p-squared action is contained in 1+pM_2(Fp), an elementary abelian group. Therefore every point field is Galois, of order at most p squared; at that order the translation map g->gP-P is an isomorphism onto M[p]. An equivariant torsion-module isomorphism identifies actual stabilizer subgroups and hence the embedded point fields, not merely abstract degrees. The formal coordinate has exactly the point field of definition.',
 'prop:B-RD61-wild':'For the only remaining mixed-divisibility case, the prime-to-p numerator in v_R(P)=B_1/p squared forces the common point field to have degree p squared over R. Normalized coordinates have valuations B_i and a common low translation has displacement p squared times B_i. Its actual lower break is N B_1 in the prime-to-p model. The universal inequality in the other model contradicts B_1>B_2. All fields and valuation multipliers were checked explicitly.',
 'prop:B-RD61-tame':'With B_i=p b_i and 1<=b_i<=p-2, choose a residual vector outside both high lines and then its p-squared lifts. Their common point field has degree p squared by the reduced denominator. A translation outside both lines equates N b_1 and N b_2. A translation high only in one model would equate p squared times (N-pb) and p squared times b, forcing excluded b=p-1. Thus the high lines and then actual tangent exponents agree.',
 'thm:B-RD61':'The full theorem was checked against B49, B50, B53 and the already completely audited B59. Completed maximal unramified base change preserves the inertia question and e. The common finite height-one twist normalizes the nonsquare determinant without confusing it with mod-p cyclotomic inertia. Irreducible residuals are excluded by B59 and the two reducible branches by B61. The actual B18 first-level example supplies the lower bound. This proves exactly nu_min(p,p-1,2)=1 for all p>=5 under the stated height-two and monodromy hypotheses; other e and heights remain open.',
 'rem:B-RD61-scope':'The entire exact arithmetic program was read and separately rerun. It checks Newton inequalities, tame characters, reduced valuation denominators, both mixed-divisibility bounds, tame line comparisons and integer-binomial valuations. These finite checks do not construct a formal group, Galois point field, or congruent pair, and are not the proof of the uniform theorem.'
}
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    for lab,detail in checks.items():
        wr.writerow([lab,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15','targeted proof check','PASS. '+detail])
    wr.writerow(['rem:B-RD61-scope',now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15','computation or formal certificate','PASS. Author-preserving rerun of exact arithmetic supplement; original author output hash unchanged. Runtime and counts in outputs/root_b60_b61_audit.json.'])
files=['agents/reduction_descent/B_tame_reducible_newton.tex','agents/reduction_descent/B_tame_reducible_recovery.tex']
record={'status':'FULL MATHEMATICAL AND CODE PASS','actual_utc':now,'events':len(checks)+1,
 'root_rerun_seconds':run['runtime_seconds'],'author_output_sha256_unchanged':before,
 'candidate_sha256':{rel:hashlib.sha256((w/rel).read_bytes()).hexdigest() for rel in files},
 'counts':{k:v for k,v in run.items() if isinstance(v,int)},
 'source_scope':'Complete B60/B61 proofs and program read, with B49 and B53 dependencies freshly rechecked. Hopkins--Gross coefficient propositions are the original passages already source-audited for B49; no new source theorem is imported. B59 was fully audited separately after the original Serre and Colmez reads.',
 'remaining_gate':'B.4 least-index formula at other ramification indices or heights. The p>=5,e=p-1,height2 comparison is closed by these proofs if the independent audit also passes.'}
p=w/'outputs/root_b60_b61_audit.json'
assert not p.exists()
p.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
