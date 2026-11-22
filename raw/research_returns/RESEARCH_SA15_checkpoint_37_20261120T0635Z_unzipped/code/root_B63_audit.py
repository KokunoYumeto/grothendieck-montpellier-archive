"""Record the complete Newton/arc audit and an isolated exact finite rerun."""
from pathlib import Path
import contextlib,csv,datetime,hashlib,io,json
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/root_B63_audit.json';assert not dest.exists()
src=w/'agents/reduction_descent/code/verify_cyclic_torsion_threshold.py'
author=src.with_suffix('.output.json');before=hashlib.sha256(author.read_bytes()).hexdigest()
target=w/'outputs/root_B63_independent_certificate.json'
snap=w/'code/audit_snapshots/B63_root_independent_certificate.py'
assert not target.exists() and not snap.exists()
needle="Path(__file__).with_suffix('.output.json').write_text"
text=src.read_text();assert text.count(needle)==1
executed=text.replace(needle,'Path('+repr(str(target))+').write_text');snap.write_text(executed)
stream=io.StringIO()
with contextlib.redirect_stdout(stream):
    exec(compile(executed,str(snap),'exec'),{'__file__':str(src),'__name__':'__main__'})
target.with_suffix('.stdout.txt').write_text(stream.getvalue())
run=json.loads(target.read_text());assert run['status']=='PASS'
assert before==hashlib.sha256(author.read_bytes()).hexdigest()
checks={
 'lem:B-RD63-point':'Complete forward and inverse Newton-polygon proof independently rederived. The integral universal coordinate gives no terms in degrees2 throughp-1, pth coefficient a unit timesu, intermediate coefficients in(p,u), and a unit p-squared coefficient. For every positive-slope root, all later integral coefficients are above the hull. For inverse input valuation Z<a, the linear term is above the hull(0,Z),(p,b),(p²,0); the same coefficient ideals exclude hidden vertices. All inverse valuations decrease. A uniform step stays uniform thereafter, and the beta branch likewise thereafter divides byp². Each of the four rational-chain cases was checked: one-slope contradicts p not dividinga; beta gives the stronger bound; alpha followed by uniform steps gives a>=N p^(2n-3) with equality excluded; alpha followed by a high step implies a=p(b+(p-1)A), so only beta is rational and gives the strict threshold. No cancellation or slope multiplicity is omitted.',
 'prop:B-RD63-mixed':'The entire B49 point, finite formal-inertia and mixed-comparison proofs were freshly reread. Completing the maximal unramified extension preserves the comparison and absolute index. A height-one filtered subgroup has character epsilon or cyclotomic times epsilon. In the first case finite twisting gives a rational primitive point; in the second, the image after quotienting by the cyclic subgroup has the finite determinant-quotient character, and a finite twist again gives a rational point. Finite-flat closure preserves the good one-dimensional supersingular quotient. The actual lattice good-reduction argument supplies tame degree m dividingN=p²-1; a=me is prime top. Connected special torsion makes the rational point formal. The point bound and m<=N force e>p^(2n-3).',
 'thm:B-RD63-arc':'Full arc proof rederived. For x0=e/Q>1/p, A=floor(x0)+1 with a possible single increment avoidsN and lies strictly betweenx0 andp x0. When x0<1 useA=1; whenx0>=1 useA<=x0+2<p x0. The difference b-(p²-p)A p^(2n-4) is exactlyN(e-A p^(2n-3))>0, and AQ<pe<Ne<NAQ. The earlier complete B62 coefficient argument applies to inputX^A, so P_A has constantp and mod-p initial monomialX^(Ne). Weierstrass gives a complete Eisenstein DVR, and the strict actual valuation inequalities protect the exact orderp^n ofx^A. The homogeneous logarithm identity yields sigma(x)=zeta x and semilinear coordinate aT, a=zeta^-A, fixing the point and satisfying the cocycle. The field extension has orderN even if its special representation is not faithful. Its fixed field has indexe and containsmu_p by the same unique tame-extension/Hensel argument. The already completely audited cyclic quotient, determinant twist and compatible Kummer extension give the common truncation; the two finite special trace functions differ by-(lambda-1)(lambda^p-1), nonzero becauseN does not divideA. Only a prime-to-p finite inertia quotient element is used.',
 'cor:B-RD63':'The exact mixed iff is an existence assertion over some permitted field of indexe, with necessity restricted to p not dividinge. The index arithmetic is p^(2n-3)<=e-1, so the largest actual exponentn is floor((floor(log_p(e-1))+3)/2). A failure atp^n=M(n-1) gives nu_min>=n. In the residual bound1 range, the full B18 first-level construction was freshly reread: its arithmetic hypotheses hold for every positive multiple ofp-1 atn1, and it gives the asserted unequal characters. Equal good summands preserve the counterexample in all h>=2.',
 'rem:B-RD63-scope':'All scope restrictions were checked. Necessity assumes p not dividinge and the whole-supersingular versus filtered-height-one comparison. The existence theorem removes the former upper bound on e and does not assume p not dividinge. Neither assertion is an unrestricted upper bound for whole-supersingular comparisons. The whole finite program was read and rerun without changing its author output; its433130 polygons,1299390 chain steps,943 arcs,5706 weights and14360 integer-index checks supplement the universal proofs only.'}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    for label,detail in checks.items():wr.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15','targeted proof check','PASS. '+detail])
    wr.writerow(['rem:B-RD63-scope',now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15','computation or formal certificate','PASS. Isolated author-preserving exact rerun; full source and output retained in outputs/root_B63_audit.json.'])
p=w/'agents/reduction_descent/B_cyclic_torsion_threshold_candidate.tex'
record={'status':'FULL PROOF SOURCE AND CODE PASS','actual_utc':now,'candidate_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'checks':checks,'run':run,'author_output_sha256_unchanged':before,'executed_source':str(snap.relative_to(w)),
 'fresh_primary_reading':{'title':'Hopkins--Gross, Equivariant vector bundles, original indexed PDF','url':'https://math.bu.edu/people/jsweinst/AWS/Files/GrossHopkinsEquivariantVectorBundles.pdf','locators':'5.3--5.7, complete coefficient congruence;12.3--12.10 and the complete printed proof of12.10, including arbitrary residue-field extension','root_refs':['turn933431751view0','turn933431751view2','turn933431751view3'],'retrieval_failure_retained':'Direct URL open initially returned502 atturn222428674view0; opening the already indexed original reference then succeeded. No PDF image inspection is claimed.'}}
dest.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'actual_utc':now,'candidate_sha256':record['candidate_sha256'],'runtime_seconds':run['runtime_seconds'],'counts':run['counts'],'author_output_preserved':True},indent=2))
