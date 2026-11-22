"""Record full actual-file/source audits of the scalar and wreath syntheses."""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib
root=Path(__file__).resolve().parents[1]
common=dict(actor='root',model='GPT-6 Astra Pro',effort='setting not independently exposed',run='SA12 run1',
 recorded_utc=datetime.now(timezone.utc).isoformat(),type='targeted proof check',verdict='PASS',
 certificate_scope='Mathematical proof audit; no numerical certificate.')
p='parts/B/post25_research/D_wild_field_scalar_determinants_B.tex'
sha=hashlib.sha256((root/p).read_bytes()).hexdigest()
assert sha=='a49af6e8cc451113520cb68951998d9152486a8bda86c96d726492200d75cbec'
delta=json.loads((root/'parts/B/post25_research/wild_field_scalars_typography_delta.json').read_text())
initial=(root/p).read_text().replace(delta['new'],delta['old'],1)
assert hashlib.sha256(initial.encode()).hexdigest()==delta['initial_sha256']
r=dict(common,path=p,sha256=sha,labels=['D:arbitrary-field-character-scalar-H1'],
 actual_file_scope='Complete actual initial10e8a0ed statement and every proof line read; sole corrected exponent a49af6e8 read and exact reversal independently verified.',
 checks=[
 'Finite cyclic Hilbert90 is proved directly from the cyclic group order q0^d-1. Inflation--restriction therefore injects twisted H1 into the q0-minus-deck kernel. The geometric deck action fixes k and is distinguished from its scalar field action.',
 'Minimal regular resolution uniqueness is proved with a minimal common point-blowup resolution, negative definiteness and the blowdown square formula. The image of a noncontracted last (-1)-curve would itself be a smooth rational (-1)-curve. Thus the deck group lifts coherently without inverting its order.',
 'The existing all-complete genus and resolution-size budgets give 2pg+v=O(td). In the regular case strict-local purity makes the prime-to-p H1 vanish.',
 'Proper base change and the degree-one localization sequence are equivariant for the deck action. Removing the finite stable singular/intersection locus allows regular codimension-one purity, with residue module a subgroup of the exceptional permutation module.',
 'The constant-sheaf normalization sequence gives a free integral graph-cohomology lattice and the product of smooth-component Jacobian n-torsion. Its graph cokernel has no torsion, so reduction mod composite n remains exact. All identifications and component/branch actions are equivariant.',
 'The coherent normalization defect at each singular point bounds the branch count, giving 2 sum genera+b1<=2h1(E)<=2pg. No bound on a smaller inertia group is substituted.',
 'Smith normal form bounds the finite-mod-n kernel by the absolute determinant on each free lattice. Finite-order complex eigenvalues have modulus1 even when d is divisible by p or by a coefficient prime.',
 'For the product Jacobian, ([q0]-T) times its geometric-sum factor equals [q0^d-1]; hence it is an isogeny. Milne degree/characteristic-polynomial and Tate-module theorems bound its degree by (q0+1)^(2g), and its n-torsion kernel by that degree.',
 'Kernel orders on equivariant short exact finite-module sequences multiply as upper bounds; no semisimplicity or surjectivity on kernels is assumed. The resulting exponent is 2pg+v.',
 'q0+1<=q0^2 and q0^d=q cancel the field-cover degree, giving q^(c_R t). The scalar determinant conclusion is exactly crossed-homomorphism H1 and is independent of matrix rank.',
 'This supplies only twisted scalar control for fixed field action. It does not use or claim a local all-field H1 theorem or an ordinary semilinear representation count.'
 ],
 fresh_primary_reads=[
 dict(url='https://www.jmilne.org/math/CourseNotes/AV.pdf',locator='Version2.0, printed pp46-48: Th10.9 complete written proof with Lem10.12 and Prop10.13; pp50-52: Prop10.20 complete written proof with Lem10.21 and Lem10.22.',refs=['turn119683969view0','turn844294220view1'],scope='All named written proofs actually read. Their earlier intersection/polarization/Tate prerequisites remain Known; no recursive full-source claim.'),
 dict(url='https://stacks.math.columbia.edu/tag/0C5R',locator='Lemma54.17.1',ref='turn465702635view0',scope='Complete statement and complete written proof read; the explicitly omitted elementary induction detail and linked dependencies remain Known.'),
 dict(url='https://stacks.math.columbia.edu/tag/03RQ',locator='Lemma59.69.1',ref='turn465702635view1',scope='Complete statement and complete written Kummer/Picard proof read.'),
 dict(url='https://stacks.math.columbia.edu/tag/095T',locator='Theorem59.91.11',ref='turn465702635view2',scope='Complete statement and complete written proof read, with its cited reduction lemmas kept as known inputs.')],
 movement_scope='Auxiliary scalar input; not an independent main-gate reduction. Its use in any full skew synthesis must be separately proved and audited.')
out=root/'parts/D/post25_research/audit_B_wild_field_scalar_determinants_root.json'; assert not out.exists()
out.write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'path':str(out.relative_to(root)),'sha256':sha,'verdict':'PASS'}))
p='parts/C/post25_research/D_iterated_wreath_alternating_orbits.tex'
sha=hashlib.sha256((root/p).read_bytes()).hexdigest()
assert sha=='f62b49ff08ea5971901a6fa454793528b944a38347570446b6900b0d55b40798'
r=dict(common,path=p,sha256=sha,
 labels=['D:hereditary-wreath-permutation-count','D:alternating-local-wreath-energy'],
 actual_file_scope='Complete actual candidate, both statements and every proof line read in full. The actual preceding matrix-model catalogue and primitive-recognition proofs were reread for their precise named-family scope.',
 checks=[
 'The arbitrary-cover ordinary count bounds actual P-valued Hom after one ambient |GL| orbit allowance; it does not confuse linear-conjugacy and permutation-conjugacy classes.',
 'For a transitive top action of degree T_i, its stabilizer has actual index T_i in the original fixed local group. Pure-permutation nonabelian Shapiro holds for every finite P_i, with no simplicity hypothesis; the written transport cancellation and inverse modulo base conjugacy are exact.',
 'Choosing one representative for each top wreath-conjugacy class loses no classes, since the top group embeds canonically in the next wreath product. Discarding nontransitive lifts and then enlarging conjugacy to the full symmetric group only lowers the count.',
 'Each modelled level costs O(T_i r_i^2 log q_i)<=O(N log(m_i+1)), and sum log(m_i+1)<=c log N. Each unrestricted symmetric level uses its faithful F_p permutation module and costs O(T_i m_i^2).',
 'Finite catalogue choices and ordered factorizations have logarithmic cost O(N log N). A fixed standard imprimitive action accounts for all block identifications; no extra factorial factor per tower level is omitted.',
 'Every transitive N-set has the one-level unrestricted certificate of energy N^2, and the minimum is over finite certificate choices. Arbitrary modelled height has zero energy. The new criterion therefore retains the earlier whole-orbit squared-energy scope.',
 'Affine catalogues have the existing (d+1)-dimensional block matrix model. The permitted primitive nonabelian-socle recognition supplies dimension O(log^2 m); fixed subgroup/point-stabilizer enumeration gives logarithmic model count O(log^8 m), uniformly bounded by B m log(m+1). No new classification claim is made.',
 'Minimal nontrivial blocks have primitive setwise-stabilizer action; transported restrictions give a faithful wreath embedding. Recursing on the block action realizes precisely the asserted qualifying primitive towers.',
 'For global finite-puncture counting, previous finitely-generated quotient/model types retain their factorial enumeration. There are at most wn remaining orbits; assigning total integer energy budget M costs at most (M+1)^(wn), with logarithm O_K(n log(n+1)). The local type product has the same factorial bound.',
 'The unchanged fixed-curve full-local-type fibre bound, degree-linear different estimate, disconnected assignments and finite-normalization descent multiply only factorial-order factors. The proof keeps whole local source actions and their true finite-index stabilizers, not curve inertia alone.',
 'Distinct natural alternating quotient kernels inject into the counted permutation classes. The previously checked factorial/simple-power/Goursat arguments give only the selected simple-product finite-generation claim, uniformly in n; unselected factors remain outside scope.',
 'The extension is limited to complete local punctures and the established finite-omitted-set dimensional/normalization transfer. No arbitrary-cover original-divisorial local-pair theorem is inferred.'
 ],fresh_primary_reads=[],
 primary_scope='New proof uses internal audited inputs only. The complete actual matrix-model and primitive-recognition dependency sources were reread; their already opened exact classification sources are reused, with no new external opening claim.',
 movement_scope='One concrete enlargement of the restricted-alternating criterion by weighted tower energy. Its two units, primitive examples and geometric transfers are grouped as one prospective scheduled-review reduction, not separate events.')
out=root/'parts/D/post25_research/audit_C_iterated_wreath_alternating_root.json'; assert not out.exists()
out.write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'path':str(out.relative_to(root)),'sha256':sha,'verdict':'PASS'}))
