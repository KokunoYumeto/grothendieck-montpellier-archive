"""Record completed full proof reviews and isolated author-preserving reruns."""
from pathlib import Path
import contextlib,csv,datetime,hashlib,io,json
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/root_powers_three_degree_two_audits.json'
assert not dest.exists()
runs={}
for key,rel,authorrel,needle in [
 ('powers_three','agents/reduction_descent/code/verify_nonordinary_powers_three_graphs.py','agents/reduction_descent/code/verify_nonordinary_powers_three_graphs.output.json',"Path(__file__).with_suffix('.output.json').write_text"),
 ('degree_two','agents/monodromy/code/nonordinary_degree_two_six_theta_graph.py','agents/monodromy/outputs/nonordinary_degree_two_six_theta_graph.json',"out=Path(__file__).resolve().parent.parent/'outputs/nonordinary_degree_two_six_theta_graph.json'")]:
    src=w/rel; author=w/authorrel; before=hashlib.sha256(author.read_bytes()).hexdigest()
    target=w/f'outputs/root_{key}_independent_certificate.json'
    snap=w/f'code/audit_snapshots/{key}_root_independent_certificate.py'
    assert not target.exists() and not snap.exists()
    text=src.read_text(); assert text.count(needle)==1
    replacement=('Path('+repr(str(target))+').write_text' if key=='powers_three' else 'out=Path('+repr(str(target))+')')
    executed=text.replace(needle,replacement);snap.write_text(executed)
    stream=io.StringIO()
    with contextlib.redirect_stdout(stream):
        exec(compile(executed,str(snap),'exec'),{'__file__':str(src),'__name__':'__main__'})
    target.with_suffix('.stdout.txt').write_text(stream.getvalue())
    result=json.loads(target.read_text())
    assert result.get('status',result.get('verdict'))=='PASS'
    assert before==hashlib.sha256(author.read_bytes()).hexdigest()
    runs[key]={'runtime_seconds':result['runtime_seconds'],'author_output_sha256_unchanged':before,
               'output':str(target.relative_to(w)),'executed_source':str(snap.relative_to(w)),
               'scope':result['scope']}
checks={
 'lem:RD-A4-three-power-groups':
 'Complete proof rederived: for r=m squared minus1 and s=2m squared, v2(GLr)=r(r-1)/2 exceeds2r and hence v2(As), so the simple GLr cannot be the sole nonabelian composition factor of Ss. The cocycle square and commuting-transvection identities kill all coordinates except the i coordinate of z(tij); the three-index commutator then makes its coefficient depend only on j, giving a coboundary. Inverse transpose handles the dual. This works uniformly, without retaining the prime31 argument in higher rank.',
 'lem:RD-A4-many-theta-graph':
 'Full universal graph proof rederived. For k=9, E=m squared k minus m, graph dimension=m squared k minus2m+1, selected doubled-complete subgraph dimension=(m-1) squared, and kernel dimension=m squared(k-1). Anchored loops and pair differences span the total-edge-sum-zero hyperplane. The all-ones vector is a cycle. A node-product-invariant subspace in every shifted kernel has only type-constant vectors; the shift(-u,0,u,0,...) triangle forces their coefficients to vanish. Code checks only the explicitly declared finite cases and retained shift subsets.',
 'prop:RD-A4-three-step-boundary':
 'All proof read and independently rederived. The fixed target translation removes the norm Pic0 discrepancy and gives the actual complete target system. Descent bundles are products of the already proved globally generated ample three-theta descents, so their maps remain finite. Chord exceptions have dimension at most2; joint incidence and the transferred three-value and first-jet estimates imply two-transitivity and generic nodality. For m>=5 three translating parameters are independent with an unused one absorbing their sum; all finitely many kernel shifts have a common clean theta boundary. Distinct shifted difference branch supports give factor-supported transpositions and the full four symmetric groups. Composition-factor separation and uniform H1 vanishing give the actual natural block. The quotient splitting extends as a finite etale torsor section over each normal Lang component, without identifying generic and special ranks. Local component torsor trivializations give the exact pair vector qij; summing at a vertex produces4(m-1) ones and2m squared minus4(m-1) zeroes in each type, forcing every heart and all asserted gluing translations.',
 'thm:RD-A4-three-step':
 'The common clopen Lang closure and universal shifted graph prove every nonzero invariant subspace has dimension at least R-1. Odd-degree covector vanishing rules out a proper hyperplane. The normal transvection subgroup has semisimple socle by global irreducibility and multiplicity one by rank-one generation. The actual natural GLr block lies in one constituent; the type-heart translations enlarge it to dimension R-4>R/2, and conjugacy forces one constituent. The already source-checked transvection classification has only the full linear or invariant alternating-form alternatives here; the actual natural block has no invariant bilinear form or functionals, excluding the latter. Thus the full group is GL_R, R=9m squared minus1.',
 'cor:RD-A4-powers-three':
 'Induction uses the already proved degree1 base, existence of a nonproduct polarized three-neighbour for every nonproduct nonordinary surface, and the uniform step. All choices are geometric and arithmetic equality follows by containing the full geometric group; ambient hypersurface transfer is only under the proved restriction-surjectivity bound. Every degree d=3^j on every fixed nonordinary principal surface has GL_(9d squared minus1). Product cases are supplied by their prior all-degree theorem.',
 'rem:RD-A4-powers-three-scope':
 'Scope and the added certificate paragraph actually read after their clarification. Only kernels killed by3 are used. The exact supplement checks m3,5,9,27 graph arithmetic, computes heart spans onlym3,5,9 with retained admissible shifts, and eight order/dimension cases. Root read the complete program and reran it with original output unchanged. Neither arbitrary odd degrees nor even degrees follow from this induction alone.',
 'lem:nonordinary-ppav-two-lifted-intersections-candidate':
 'Complete proof rederived and both entire earlier surface-jet proof and labelled-wreath proof freshly reread. Restriction image has projective dimension8 or7, with integral affine pullback fibres. Surface second jets give three curve jets; double-tangency strata have dimensions/ranks(2,4),(1,3),(0,2), since the finite union of exceptional theta translates meets the sharp curve finitely. Higher contact has codimension2. The generic discriminant contact is quadratic with independent b,c; in characteristic2 inertia still exchanges the two roots when the generic residue extension is inseparable. Etale torsors locally trivialize, so inertia is a labelled transposition. Lifted point incidence is irreducible and finite over coefficient projective space. Divisorial-inertia generation follows from purity and simple connectivity. The spanning-tree labelled-transposition proof then gives exactly ker(sum:G^18->G) semidirect S18. No generic-modulus assumption enters.',
 'lem:nonordinary-ppav-two-boundary-gluing-candidate':
 'Boundary ranks and maps type-checked: T=F2^18/<1> has dimension17, heart16, R=(HC plus HD)/diag A0 has dimension16+f. Each component representation is either a split natural GL8 plus ambient constant line or its full irreducible extension, by H1=0. Its image is perfect with only GL8 nonabelian factors. Goursat separates S18 and the two natural factors. The explicit direct-sum module Hom(R,T) is semisimple for the actual Levi, so cocycle elimination supplies actual complementary blocks. Fixing C, its maximal elementary torsor wreath image has only A18 as nonabelian factor, independent of the D cohomology image. Sum-zero node translations with D identity exhaust Hom(HC,T0); reversing C,D and separating the explicit isotypic summands gives all Hom(R,T0), including ambient columns. Every nonzero invariant subspace contains T0; known covectors give the exact32-dimensional kernel.',
 'lem:nonordinary-ppav-two-six-theta-comparison-candidate':
 'Six general theta translates with sum zero give doubled K6, graph25 and relative stable rank25+5f. The two partitions123|456 and124|356 have cross hearts16. Pair vectors e13,0+e23,0 and e45,0+e46,0 lie in the second heart and project independently nonzero to the first two internal doubled triangles; parallel-edge cycles certify nonzero graph classes. Ambient cohomology injects into each theta component and misses the graph. The full Lang closure is clopen over the normal six-theta parameter base even at rank drop. Each finite etale node-heart section extends; over the strict henselization of the first boundary each retained point lifts uniquely and belongs generically to the invariant subspace. A regular quotient-bundle section nonzero at the special point is nonzero generically. The two natural blocks then force both rank8 projections; together with heart16 they force the entire rank32 kernel. No full stable-rank specialization is assumed.',
 'thm:every-nonordinary-ppav-degree-two-full-candidate':
 'Full proof rederived. Irreducibility of K gives semisimplicity for the socle of the normal transvection subgroup, multiplicity1 follows from rank-one generation, and no fixed summand can persist. An actual natural rank8 block and its gluing shears put heart16 in the same constituent; the other natural block and reverse shears force the remaining8 dimensions into it. The resulting irreducible transvection group has no invariant nondegenerate alternating form, because the actual natural block has no invariant pairing or functional. Hence it is GL32. For Q=V/K constant of rank1+f, the translation kernel has form K tensor Qprime. H1(GL32,K)=0 gauges the quotient cocycle; if Qprime is proper an annihilator vector has an invariant lift, contradicting that every nonzero invariant subspace contains the16-dimensional heart. Thus the entire Hom(Q,K) occurs. Covectors are pointwise fixed over the perfect base, so arithmetic image equals the same geometric full stabilizer. Product cases use their prior all-degree proof.',
 'rem:nonordinary-ppav-degree-two-scope-candidate':
 'The entire exact doubled-K6 program was read and independently rerun, preserving the original output. It proves only graph25, cross17, heart16, two independent internal projections, and the stated f0/f1 rank arithmetic. Every fixed nonordinary principal surface in characteristic2 is covered at degree2; no higher-degree assertion is inferred.'}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    for label,detail in checks.items():
        wr.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15','targeted proof check','PASS. '+detail])
    for label,key in [('rem:RD-A4-powers-three-scope','powers_three'),('rem:nonordinary-ppav-degree-two-scope-candidate','degree_two')]:
        wr.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15','computation or formal certificate','PASS. Full source read and isolated author-preserving rerun, scope and exact runtime in outputs/root_powers_three_degree_two_audits.json.'])
files=['agents/reduction_descent/A_nonordinary_powers_three_candidate.tex','agents/monodromy/nonordinary_ppav_degree_two_wreath_theta_candidate.tex']
record={'status':'FULL MATHEMATICAL PROOF AND CODE PASS','actual_utc':now,'events':len(checks)+2,
 'candidate_sha256':{p:hashlib.sha256((w/p).read_bytes()).hexdigest() for p in files},
 'checks':checks,'runs':runs,
 'sources':'Previously completely checked source dependencies are reused with their exact existing check records; root freshly reread the full surface-jet, fixed-point finite-exception and labelled-wreath proofs. OC independently freshly reopened purity0BMB, Entin Prop3.1/Theorem2 complete proof and Kantor--Seress3.6 in its degree2 audit. No new root external retrieval or image inspection is asserted.'}
dest.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k not in ('checks','sources')},indent=2))
