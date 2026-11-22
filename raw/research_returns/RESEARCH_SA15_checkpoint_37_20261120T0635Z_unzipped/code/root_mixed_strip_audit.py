"""Root full strip proof audit with an author-preserving exact graph rerun."""
from pathlib import Path
from contextlib import redirect_stdout
import csv,datetime,io,json,hashlib
w=Path(__file__).resolve().parents[1]
program=w/'agents/monodromy/code/mixed_strip_grid_checks.py'
author=w/'agents/monodromy/outputs/mixed_strip_grid_checks.json'
dest=w/'outputs/root_mixed_strip_grid_checks.json'
summary=w/'outputs/root_mixed_strip_audit.json'
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
    (w/'outputs/root_mixed_strip_grid_checks.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes()==before
out=json.loads(dest.read_text());assert out['status']=='PASS'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
events=[
 ('lem:mixed-strip-lifted-triple-candidate','independent re-proof',
  'PASS: entire statement and proof rederived. A general dual-plane transform avoids the finite flex-line set; the smooth sharp (3,3) curve therefore has only double-plus-simple branch fibres, giving transposition inertia without assuming a separable dual Gauss map. For its maximal or any connected elementary-two torsor, the normal inertia subgroup has a connected permutation graph; gauging a spanning tree gives sum-zero G0^3 semidirect S3. Its translation normalizer modulo that group has dimension dimG, so H/J is a two-group. The residual cover is everywhere etale on the supersingular elliptic target and hence trivial. Lifted transitivity forces G0=G.'),
 ('lem:mixed-strip-boundary-candidate','independent re-proof',
  'PASS: full proof rederived. Solving Q_m=[b]t-sum_(j<m)Q_j yields an integral ordered normalization cover and translation puts the union in the fixed system. The nodal rank is9+3m-1=3b-1, equal to the coherent relative dimension. Trace of degree3 splits the ambient unit line; r_j=a_j+a gives the actual relative constant body. The [b] cover has a radicial two-primary part and odd abelian etale part; the ordered/product/wreath lifted images have only two-primary abelianizations, so their images are unchanged. Node torsor evaluations give precisely all Hom(U plus A_j,T_j), with other columns zero. GL8 is independent of the graph/permutation quotient by its different nonabelian simple factors, and full H1 vanishing supplies an actual block. Every nonzero boundary-invariant subspace contains all graph summands.'),
 ('lem:mixed-strip-grid-candidate','independent re-proof',
  'PASS: all finite-Lang and dimension-transfer steps rederived. K3,b has graph dimension2b-2 and relative unit rank3b-3, two below generic. For every triple J, translating by tau with3tau=-sum_J Q recovers the same grid in the fixed normalized boundary. The constant graph spaces for columns outsideJ span all graph cohomology. An internal K3,3 graph class projects nontrivially to the generic relative GL8 block, whose whole inverse image belongs to S. Dualizing pullback of regular one-forms defines a coherent trace even across contracted vertical components; at the grid it is the sum on the three horizontal components and kills graph classes. Its constant-unit body maps are regular and Frobenius-equivariant. A finite Lang section with zero special constant-body coordinates has identically zero coordinates, so belongs to S; this uses kernels, not rank-drop surjectivity. Triple-supported pair vectors span sum-zero component classes. Their image on the fixed outside body has dimensionm for oddb andm-1 for evenb, giving8+2m+m or8+2m+(m-1). Thus V is irreducible for oddb, and the nonzero trace kernel is irreducible and belongs to every nonzero invariant subspace for evenb.'),
 ('thm:mixed-three-by-b-full-groups-candidate','independent re-proof',
  'PASS: full theorem including arbitrary perfect base rederived. The normal transvection subgroup is semisimple by its globally invariant socle; rank-one generation forces multiplicity one and excludes a fixed summand. The actual GL8 block and all graph shears lie in one simple summand; shears from every constant-body coordinate exclude every other summand. Kantor-Seress3.6 then gives GL on K since the actual natural GL8 block forbids an invariant nondegenerate alternating form. In the even case a proper translation kernel would split by H1(GL(K),K)=0 and give a fixed line, contradicting the invariant-subspace theorem. The trace target is a one-dimensional F2-space with trivial arithmetic action, so both arithmetic and geometric images equal the stated stabilizer; oddb is fullGL. Scope is exactly factor degrees(3,b), b>=3, not all balanced degrees.'),
 ('rem:mixed-strip-scope-candidate','targeted proof check',
  'PASS: complete scope remark read. Special rank3b-3 and generic rank3b-1 remain distinct. No all-balanced-degree conclusion or novelty claim is asserted. The finite certificate is supplementary to the uniform proof.'),
 ('STRIP-EXACT-GRAPH-CERTIFICATE','computation or formal certificate',
  f"PASS: entire program read and independently rerun with author output unchanged in {out['runtime_seconds']} seconds. Exact GF2 ranks cover b4..32, graph quotients, all column spans, pair-supported component spans, body images and recovered dimensions, and zero S3 coinvariants of the three-label heart. This does not replace the geometric proof or prove the infinite range by enumeration.")]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for sid,kind,result in events:writer.writerow([sid,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort',kind,result])
record={'status':'FULL MATHEMATICAL AND CODE PASS','actual_utc':now,
        'runtime_seconds':out['runtime_seconds'],'author_output_sha256_unchanged':hashlib.sha256(before).hexdigest(),
        'events':len(events),'scope':'Uniform(3,b) mixed products only; balanced degrees>=3 remain open.',
        'source_scope':'Root reread the full labelled-transposition, nodal-gluing and finite-Lang grid dependency proofs and entire H1 cocycle proof. Original Kantor-Seress Theorem3.6 printedp22 was actually viewed in the preceding root source audit; exact retained text reread now. No fresh new page-image view or unavailable McLaughlin-original read is claimed.'}
summary.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
