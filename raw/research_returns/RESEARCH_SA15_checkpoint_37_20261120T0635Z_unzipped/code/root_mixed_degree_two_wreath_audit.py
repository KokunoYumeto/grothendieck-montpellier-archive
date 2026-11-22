"""Complete root proof/source audit and author-preserving exact graph rerun."""
from pathlib import Path
from contextlib import redirect_stdout
import csv, datetime, io, json
w = Path(__file__).resolve().parents[1]
program = w/'agents/monodromy/code/mixed_degree_two_grid_checks.py'
author = w/'agents/monodromy/outputs/mixed_degree_two_grid_checks.json'
dest = w/'outputs/root_mixed_degree_two_grid_checks.json'
summary_path = w/'outputs/root_mixed_degree_two_wreath_audit.json'
assert not dest.exists() and not summary_path.exists()
before = author.read_bytes()
old_write, old_exists = Path.write_text, Path.exists
capture = io.StringIO()
def exists(path):
    return False if path.resolve()==author.resolve() else old_exists(path)
def write(path, data, *args, **kwargs):
    assert path.resolve()==author.resolve()
    return old_write(dest, data, *args, **kwargs)
try:
    Path.exists, Path.write_text = exists, write
    with redirect_stdout(capture):
        exec(compile(program.read_text(), str(program), 'exec'),
             {'__name__':'__main__','__file__':str(program)})
finally:
    Path.exists, Path.write_text = old_exists, old_write
    (w/'outputs/root_mixed_degree_two_grid_checks.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes()==before
out = json.loads(dest.read_text())
assert out['status']=='PASS'
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
who = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events = [
('lem:labelled-transposition-wreath-candidate','independent re-proof',
 'PASS: full proof independently rederived. The projected edge graph is connected; a spanning-tree change of fibre origins kills its labels. Bare tree transpositions generate S_N. Each remaining labelled transposition yields a pair-difference translation, and S_N conjugation gives every such pair difference for its label. The subgroup of labels G0 gives precisely the sum-zero G0 module, and its point-fibre orbits are the cosets of G0. Transitivity therefore forces G0=G. The conclusion is the full wreath sum-zero subgroup, not just its permutation quotient.'),
('lem:mixed-lifted-intersection-wreath-candidate','independent re-proof',
 'PASS: full incidence proof and all characteristic-two edges independently rederived. The restricted very ample linear system embeds C; a possible one-dimensional section kernel is removed by the projective linear projection, whose affine fibres preserve geometric finite-cover connectedness. The degree-three elliptic projections are separable. Generic second jets separate; simultaneous first jets have rank4 off a pair locus of dimension<=1, while rank2 tangent coincidences are finite because a Segre tangent with both derivatives nonzero contains no other Segre point. Explicit cubic polars show the older jet argument applies to every ordinary E_a and to E0, and Picard twists are translations. The double-tangency and higher-contact loci have codimension>=2, including finite jet exceptions. At generic tangency the quadratic root algebra z²+bz+c has independent b,c; the separably closed generic residue field is imperfect and c is nonsquare, so c/b² is a nontrivial Artin-Schreier class and inertia is a labelled transposition. Etaleness of the auxiliary curve cover makes every other lifted fibre fixed. The total lifted incidence is irreducible, projective and quasi-finite over the hyperplane space, hence finite and transitive. Purity of branch locus plus simple connectedness of projective space gives generation by divisorial inertia. Root freshly read full Stacks0BMB and the previously proved projective-space blowup argument.'),
('lem:mixed-degree-two-boundary-group-candidate','independent re-proof',
 'PASS: all normalization and group-extraction steps independently checked. Nodal p-rank is9+9+17=35, minus the ambient unit line gives34. Independent relative curve images are GL8 x GL8. Each full curve image and the body image are perfect extensions by the indicated natural-dual modules; H1 vanishing supplies actual complements. Their nonabelian factors GL8 share no quotient with S18 or the lifted-point wreath group, whose only nonabelian factor is A18 (11 divides the latter order but not GL8). Goursat therefore allows pure lifted-node translations with moving-component cohomology fixed. Extending an etale C-torsor by the trivial D-torsor proves the gluing-evaluation formula on the injected H1(C) inside the17-dimensional body. The additive matrix kernel is semisimple under actual GL8 x GL8; surjectivity of these restricted columns therefore supplies the C and ambient columns independently, and interchange gives the D columns. This yields all Hom(R,T0). Any nonzero body vector produces every heart vector under these shears; any nonconstant graph class produces a pair difference under a transposition. Thus every nonzero boundary invariant subspace contains the16-dimensional heart.'),
('lem:mixed-degree-two-common-grid-candidate','independent re-proof',
 'PASS: complete rank-dropping comparison independently checked. The K6,6 graph has rank25, its six ordinary components add6 and the ambient unit line subtracts1, giving30. Each three-plus-three row/column partition gives opposite Picard twists, rather than incorrectly demanding both triples lie in|3O|. Strict henselization of the regular coefficient local ring is an integral normal domain. The separated etale quasifinite affine Lang scheme has a constant finite etale subgroup with this special30-space. Membership of any such section in a global invariant S is clopen on the nonempty integral maximal-rank open, and hence constant. Each boundary cross-heart extends through the grid and coincides with those ambient finite Lang sections by uniqueness of etale sections with a common closed value. The two explicit cross-heart cochains project nontrivially to the two first-partition internal K3,3 graphs, as evaluated on the specified four-cycles. Coherent restriction and ambient quotient maps remain regular by antiample H1 vanishing and base change. A nonzero unit graph class cannot be ambient: the ambient unit has nonzero normalization-component projection and the remaining ambient part is nilpotent. The projections are therefore nonzero generically. Independent GL8 factors force16 body dimensions and the first cross-heart gives16 more, so S=K of dimension32. No identification of the special30-space with the generic34-space is made.'),
('thm:mixed-every-fixed-modulus-degree-two-candidate','independent re-proof',
 'PASS: all finite-group closure and arithmetic steps independently rederived. Every nonzero invariant space contains K, so V has no invariant vector. The two actual GL8 blocks plus the16-heart fill K. The normal transvection subgroup is semisimple by invariance of its socle; rank-one generators force multiplicity1 and exclude a trivial isotypic part. The first GL8 block lies in one simple summand, and every rank-one shear from it forces the whole heart into that summand. Shears from the second GL8 block force that block into the same summand, making the normal subgroup irreducible. The exact four alternatives in Kantor-Seress3.6 were read from retained original p22, also actually viewed; overF2 every proper alternative preserves a nondegenerate alternating form. An actual GL8 natural block fixing its complement rules out such a form. Hence the kernel image is GL32. The remaining translation module is K tensor U; H1(GL32,K)=0 makes a proper U produce a fixed lift of a nonzero quotient direction, impossible. Thus the full Hom(F2²,F2^32) semidirect GL32 occurs. Previously proved entire covectors descend over every perfect base and bound arithmetic image by the same group.'),
('lem:product-small-degree-jets','used and rechecked in this run',
 'PASS: entire older jet proof reread, with its required extension checked explicitly. For E_a the projective cubic polars have independent X²,Y²,XZ coefficients; for supersingular E0 the polars are X²,Z²,Y². Therefore no nonzero constant polar combination vanishes identically on either smooth cubic, and tangents through any fixed point are finite. The tensor-tangent intersection argument and finite crossed incidences consequently hold for arbitrary ordinary modulus and translated degree-three factor bundles.'),
('lem:char2-defect-one-inertia','used and rechecked in this run',
 'PASS for the dependencies used: entire finite-Lang and purity argument reread. Root freshly read full Stacks0BTN and09ZS, as well as04GK, establishing the finite etale summand and its unique constant sections over strict henselization. The elementary simple-connectedness proof of projective space by the point blowup and its P1-bundle was reread and rederived. No claim that the degree-two Hasse divisor has simple rank loss is imported.'),
('MIXED-DEGREE2-H1-DEPENDENCY','used and rechecked in this run',
 'PASS: root reread the complete elementary cocycle proof in quintic_exact.tex. For m>=4, t_ij²=1 and commuting auxiliary t_kell force c(t_ij)=a_ij e_i; the three-index Steinberg relation forces a_ij to depend only on j, yielding a coboundary. Inverse transpose gives the dual. Products with a second GL8 factor and direct sums/quotients of the displayed semisimple natural-dual/trivial modules preserve the asserted H1 vanishing.'),
('MIXED-DEGREE2-GRAPH-CERTIFICATE','computation or formal certificate',
 f"PASS: entire author graph program read and rerun, author output unchanged, in {out['runtime_seconds']} seconds. Exact binary elimination checks global graph rank25, both cross-heart dimensions16, both nonzero internal projections, both four-cycle evaluations1, and relative ranks34/30 and kernel32. This is only finite graph verification, not a computational proof of the geometric specialization or group assertions.")
]
with (w/'notes/root_check_events.tsv').open('a', newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for sid, kind, result in events:
        writer.writerow([sid,now,who,kind,result])
with (w/'notes/ROOT_SEARCH_LOG_18.md').open('a') as f:
    f.write(f'''\n## {now}: complete fixed-mixed degree-two wreath/grid audit\n\nRoot read the complete five-assertion candidate and its entire graph program, and independently rederived every proof. Fresh original Stacks0BMB,0BTN,09ZS and04GK statements and proofs were opened and read; their web refs were turn262867968view0/view1 and turn183462683view1/view2. The direct Kantor-Seress author URL https://pages.uoregon.edu/kantor/PAPERS/ksfinal.pdf returned a content-length error (57,682,627 bytes), retained as a failed fresh retrieval. Root instead read the previously downloaded original text and actually viewed its retained original printed-page22 image, agents/monodromy/outputs/kantor_seress_theorem_page22.png. The four exact alternatives of Theorem3.6 are SL, Sp, the two orthogonal groups overF2, and the stated symmetric groups; all proper alternatives in dimension32 preserve a nondegenerate alternating form. This is use of the opened Kantor-Seress statement, not a claim to have opened McLaughlin's unavailable original full text.\n\nRoot reread the complete elementary H1 cocycle proof in quintic_exact.tex, the product-small-degree-jets proof, and the finite-Lang/purity/projective-space argument in product_full_groups.tex. The extension of the old fixed-cubic jet proof to arbitrary E_a and E0 was explicitly checked through their polar partials. The common-grid proof keeps the rank30 finite part distinct from the generic rank34 fibre. The graph certificate rerun passed in {out['runtime_seconds']} seconds and preserved the author's output. Independent reduction/descent and obstruction/crystal mathematical audits also passed; their separately recorded source/code scopes remain distinct.\n''')
summary={'status':'PASS','actual_utc':now,'complete_mathematical_assertions':5,
         'events':len(events),'graph_runtime_seconds':out['runtime_seconds'],
         'special_grid_rank':30,'generic_relative_rank':34,'kernel_rank':32,
         'group':'Hom(F2²,F2^32) semidirect GL32(F2), geometric=arithmetic for every fixed mixed product over a perfect field',
         'scope':'Degree two only; all higher fixed-modulus degrees remain separate.'}
summary_path.write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
