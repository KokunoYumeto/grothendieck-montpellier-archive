"""Full six-assertion proof audit and author-preserving exact universal checks."""
from pathlib import Path
from contextlib import redirect_stdout
import csv,datetime,io,json
w=Path(__file__).resolve().parents[1]
summary_path=w/'outputs/root_mixed_uniform_degree_one_audit.json'
assert not summary_path.exists()
verified=[]
for name in ['verify_mixed_degree_one_pfaffians','explore_mixed_universal_Q_pencil']:
    program=w/'agents/monodromy/code'/f'{name}.py'
    author=w/'agents/monodromy/outputs'/f'{name}.json'
    dest=w/'outputs'/f'root_{name}.json'
    assert not dest.exists()
    before=author.read_bytes();old_write=Path.write_text;capture=io.StringIO()
    def write(path,data,*args,**kwargs):
        assert path.resolve()==author.resolve()
        return old_write(dest,data,*args,**kwargs)
    try:
        Path.write_text=write
        with redirect_stdout(capture):
            exec(compile(program.read_text(),str(program),'exec'),
                 {'__name__':'__main__','__file__':str(program)})
    finally:
        Path.write_text=old_write
        (w/'outputs'/f'root_{name}.stdout.txt').write_text(capture.getvalue())
    assert author.read_bytes()==before
    out=json.loads(dest.read_text());assert out['status']=='PASS'
    verified.append({'program':str(program.relative_to(w)),
                     'output':str(dest.relative_to(w)),
                     'runtime_seconds':out['runtime_seconds']})
rank=json.loads((w/'outputs/mixed_lang_rank_compatibility.json').read_text())
assert rank['status']=='PASS'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events=[
('prop:mixed-uniform-degree-one-Hasse-candidate','independent re-proof','PASS: all Cartier identities independently rederived from y²+xy=x³+a and dx/x, with root removal and the nonsymmetric R orientation kept. Tensor symmetry makes RM alternating; the full nine Pfaffian polynomial identities and detR=a^6 imply adjM=D² s s^tR. The exact Euler relative map is M^t from ann(s²) to ann(s), so its determinant is D² s^tRs². The Frobenius cubic is smooth, irreducible, and distinct from the determinant. At the displayed symbolic Q point, M u=s² and s^tR u² is the nonzero rational function stated for every a!=0. On the relative Cartier quotient, kernel line ku misses the first image exactly when u² is outside imM, proving first=stable rank7 there and at the generic Q point.'),
('lem:moving-kernel-full-root-inertia-candidate','independent re-proof','PASS: full imperfect-residue argument independently rederived. The strict henselian Lang finite part gives r-1 regular fixed sections, completed to a frame with F=[[I,b],[0,tc]]. The ambient kernel line is e²+sum b0_i w_i². Differentiating in a constant ambient bundle kills all squared frame entries; the given rank condition makes the db0_i independent, since the classes of w_i² modulo the kernel line are independent. Every nonzero F2 combination of b_i/(tc)² has valuation-2 and nonsquare leading coefficient (its differential is nonzero). It cannot be Artin-Schreier of an element of the henselian fraction field: valuation forces a pole of order1 and hence a square leading coefficient. Thus all r-1 AS classes are independent, giving the entire root group, including extensions with inseparable residue. No algebraically closed-residue replacement is made. Fresh Stacks0BTN and09ZS statements and written proofs read in full.'),
('cor:mixed-every-modulus-full-root-inertia-candidate','independent re-proof','PASS: on an affine chart the Euler bundle is an actual subbundle of the constant nine-space. Along Q away from D, its Frobenius-domain kernel is k R^t s, and its projective map is a linear immersion of the smooth seven-dimensional cubic. Its differential therefore has rank7. The simple determinant and stable-rank hypotheses all hold. The local subgroup is geometric and persists on the dense smooth-curve open, giving all2^7 roots with a fixed hyperplane for every ordinary a.'),
('lem:mixed-degree-one-exceptional-ranks-candidate','independent re-proof','PASS: root supplied the complete uniform dimension argument, then read the assembled proof. detB is a smooth plane cubic for every a!=0, so B has ranks3/2 and no two-plane is contained in its determinant. A rank2 tensor has a frame with B(u1) invertible and rankA6; compatibility is T H_col1=C T H_col2. The Frobenius Gram map has surjective four-dimensional differential, hence smooth relative dimension2. The generic three-equation case gives compatible-frame dimension9, while the two-equation locus has T-dimension<=5 by the uniform witness T=(e0,e1), C e0=e2. The open GL2 fibre has dimension4, giving compatible-v dimension<=5 and incidence<=8. Rank1 gives rankA6 off the cubic and rankA4 on it; in the latter case q^tJq²=0 reduces compatible-v dimension to<=3, again incidence<=8. All choices and frame quotients are in the needed direction.'),
('lem:mixed-degree-one-Lang-transitive-candidate','independent re-proof','PASS: the nonzero Lang scheme over the nine-dimensional affine coefficient unit open is finite etale of degree255. Full tensor symmetry changes its equations exactly into A(R^-t v²)s=v; the relative orthogonality follows automatically from alternation. For full-rank v, solvability is the smooth dual Frobenius cubic and solutions form an affine-line torsor. This cubic has a nonempty full-rank open since its squared-variable monomials cannot equal the determinant cubic. That incidence is irreducible dimension9; the exceptional incidence has dimension<=8. Every finite-etale cover component is dimension9 and surjects onto the connected base, so all meet the single irreducible main open and only one component exists. Transitivity on255 vectors and irreducibility follow; passage from the cone to projective coefficients can only enlarge image.'),
('thm:mixed-every-fixed-modulus-degree-one-candidate','independent re-proof','PASS: the geometric module is irreducible and contains a complete root group U_phi. Its conjugate functionals span the dual module; choose8 independent ones. Their root groups contain every elementary matrix in the dual basis, giving SL8(F2)=GL8(F2) without classification. Every ordinary elliptic curve and every supersingular elliptic curve become the normalized pair over the algebraic closure, compatibly with origin and degree3 line bundles. Arithmetic contains this full geometric group and therefore equals it over every stated perfect base. The theorem is degree1 only; all-degree fixed algebraic modulus remains a separate gate.'),
('rem:mixed-uniform-inertia-scope-candidate','targeted proof check','PASS: the complete scope remark was read. The exact polynomial programs support the universal identities; the smoothness, dimension, finite-cover and elementary group arguments are separately proved. Earlier failed point choices remain retained. The root auxiliary program checks Gram block-minor identities and does not purport to prove the geometric dimension argument. The conclusion is every fixed mixed modulus in degree1 only.'),
('MIXED-UNIFORM-DEGREE1-CERTIFICATES','computation or formal certificate',f"PASS: both full agent programs were read and author-preserving reruns passed: {verified}. Root's separately retained symbolic rank-strata/Gram certificate passed in {rank['elapsed_seconds']}s. It verifies detB, the smoothness partial cases, the uniform exceptional T witness and all Gram differential/block-minor identities; finite computations are not used as a substitute for the general dimension or inertia proof.")]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for sid,kind,result in events:writer.writerow([sid,now,who,kind,result])
with (w/'notes/ROOT_SEARCH_LOG_17.md').open('a') as f:
    f.write(f'''\n## {now}: every fixed mixed modulus in degree one\n\nRoot fully read and independently rederived all six assertions plus the scope remark in the uniform degree-one assembly. Root supplied the exceptional-rank dimension proof via the smooth Frobenius Gram map; the monodromy agent independently rederived it and reran the auxiliary certificate. Root read and reran both universal Pfaffian/pencil programs without changing their original outputs. Exact runtimes and paths are retained in outputs/root_mixed_uniform_degree_one_audit.json.\n\nThe local-inertia input was checked directly over the strict henselian generic divisor, keeping its imperfect separably closed residue field. Seven differential-independent nonsquare leading AS coefficients yield the entire2^7 root group. Fresh original Stacks0BTN and09ZS pages and their complete written proofs were opened and read. The nonzero Lang cover has one nine-dimensional main incidence and exceptional incidence dimension at most8, so it is connected. Irreducibility plus conjugates of the full root group supplies every elementary matrix and proves GL8 for every ordinary modulus.\n\nLiterature searches actually made before promotion: Hasse Witt monodromy characteristic two product ordinary supersingular elliptic curves GL8 Cartier; Lang local system moving kernel line fierce ramification Artin Schreier inertia full transvections; then stronger-engine searches for monodromy/Hasse/product/elliptic/characteristic2 linear system and Lang/moving-kernel/inertia. They returned related Cartier computations, general monodromy and ramification references, but no exact fixed-product degree-one theorem was located. No claim of priority follows; no unexamined search snippet is an input to the proof. Higher degrees at fixed algebraic ordinary modulus remain open.\n''')
summary={'status':'PASS','actual_utc':now,'complete_mathematical_assertions':6,
         'scope_remark_checked':True,'exact_verifications':verified,
         'root_rank_certificate_seconds':rank['elapsed_seconds'],
         'events':len(events),'conclusion':'Every mixed elliptic product, every perfect characteristic-two field, degree1 geometric=arithmetic GL8(F2).'}
summary_path.write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
