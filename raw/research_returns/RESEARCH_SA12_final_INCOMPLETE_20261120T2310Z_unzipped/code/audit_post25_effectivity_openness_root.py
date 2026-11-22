"""Record completed actual root proof checks for finite objects and generated families."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
root=Path(__file__).resolve().parents[1]
common={'actor':'root','model':'GPT-6 Astra Pro','effort':'setting not independently exposed',
 'run':'SA12 run1','recorded_utc':datetime.now(timezone.utc).isoformat(),
 'type':'targeted proof check','verdict':'PASS',
 'actual_file_scope':'Complete actual candidate, all statements and every proof line read in full.',
 'certificate_scope':'Mathematical proof audit; no numerical certificate.',
 'research_movement':'Auxiliary effectivity/openness input only; no count or requested-row closure inferred before the complete quantitative synthesis is proved and audited.'}
cases=[
 {'path':'parts/C/post25_research/D_finite_Frobenius_object_effectivity.tex',
  'sha256':'4baf47a07187c9c2174d874be319528676ed1683c9ecb01aaead44a17ebe0ac6',
  'out':'parts/D/post25_research/audit_C_finite_Frobenius_object_effectivity_root.json',
  'labels':['D:finite-Frobenius-object-effectivity'],
  'checks':[
   'Absolute Frobenius on LC is well defined and compatible with restriction of an actual formal bundle. Both finite inverse equations are maps into the bC twist; no inversion or injectivity of the Cartier map on LC is assumed.',
   'With L=N+b, the lifted local matrix products are t^b times I+t^N R and I+t^N Rprime. Both corrections are invertible by complete geometric series over arbitrary coefficient rings, so the forward matrix has an inverse with exactly the asserted pole bound b.',
   'Finite arrow compatibility gives overlap defect in I^L; multiplication by the inverse loses at most b, leaving I^N. The correction j -> pj-b is strictly contracting at N, remains integral, and preserves all specified N-jets.',
   'Matrix products on triple overlaps satisfy the same fixed-point equation by exact cancellation of the middle inverse. Equality of their N-jets and separatedness prove genuine cocycles, identities and inverses. This constructs the objects rather than independently extending bundles and hoping arrows lift.',
   'The inverse arrow agrees modulo N because t^b Ainv differs from the chosen B by I^N. Both forward and inverse maps retain the prescribed lower data. No assertion preserves the entire LC object.',
   'Comparisons between choices and morphisms of the finite data have the same residual order N, giving unique integral unit comparisons, composition compatibility and formal base-change compatibility. Infinite limits are interpreted through compatible finite-level restrictions.',
   'Formal affine frames exist by the finite-order affine-thickening theorem, freshly read. On Noetherian completed coefficient bases, proper Grothendieck existence algebraizes bundles and maps; no algebraization over arbitrary coefficient rings is asserted.',
   'The explicit O(-C) example has the natural forward O(-pC)->O(-C), inverse pole (p-1)C, and trivial punctured unit line. Its noncanonical extension correctly shows that fullness is not a consequence of object effectivity.'
  ],
  'fresh_primary_reads':[{'url':'https://stacks.math.columbia.edu/tag/06AD','locator':'Lemma37.2.3','scope':'Complete statement and complete written finite-order proof. The general limit proof is not claimed read or used here.','ref':'turn756827794view0'}],
  'reused_previously_checked_inputs':['Earlier in this same interval root freshly read all written proof of Stacks088E, Theorem30.27.1.','Intrinsic integral unit-Hom contraction, now independently reproved at the object-gluing level.'],
  'precision_scope':'Root fully read candidate83d99ac4c17cef56f7cc9a39161c4de323ff797bace49876f9cf328a8d0a7fde, then actually read the sole added06AD citation block in the final4baf47a0 candidate. Exact citation reversal checked by this recorder.'},
 {'path':'parts/D/post25_research/D_generated_fixed_determinant_unit_openness.tex',
  'sha256':'a8fb3a29b9c6d25cf8b53265c2412dedf67615f627a669713b7fc712de32b581',
  'out':'parts/D/post25_research/audit_generated_fixed_determinant_unit_openness_root.json',
  'labels':['D:weak-cycle-generated-determinant-lifting','D:generated-fixed-determinant-unit-openness'],
  'checks':[
   'A proper projective curve admits a two-affine cover with affine intersection; extension over a field preserves that cover. The fixed scalar H1 vanishings and H2=0 applied to the locally split generating quotient give H1(V(-jZ))=0 for every coefficient ring.',
   'The exact layer sequences lift each specified generator recursively to all thickenings. Nilpotent Nakayama proves generation at every level. The proof needs no unspecified cohomology/base-change theorem for the variable bundle.',
   'The unit kernel at each successive thickening is the additive O_Z(-jZ), whose H1 vanishes. Thus an existing line-bundle isomorphism lifts; Picard restriction is injective on isomorphism classes, but the chosen isomorphism is not claimed unique. A fixed determinant line on Y is retained.',
   'Only the comparison target is canonical. Constant MCM/reflexive targets satisfy Hartogs after flat finite Artinian coefficient extension; the nonreduced coefficient ring is not declared normal.',
   'Global generators of F(-Z) map on U into the fixed target, and their sections extend by target Hartogs. Generator relations vanish globally because the target has no Cartier torsion. Thus F->P(Z) exists for every punctured isomorphism without source fullness.',
   'Relative to one fixed exceptional determinant isomorphism tau, the determinant ratio and its inverse both extend as functions by Hartogs. Their product remains1, giving a genuine A tensor T unit. Nilpotent coefficients therefore do not increase exceptional orders.',
   'The adjugate bound is (r-1)Z plus div(tau)^+. Composing with the fixed closed comparison bounds both directions between F and F0 by rZ+eC. This bound may depend on the fixed object but is uniform in all Artinian nilpotence orders.',
   'Shifting Hom by dC changes the Frobenius loss to c+(p-1)d. Endomorphism products lie in the 2dC lattice; a common depth above its contraction threshold also exceeds2d. Thus products and the identity have meaningful finite jets and uniqueness gives exact inverses.',
   'Proper-cycle Hom representability yields an affine finite-presentation bounded meromorphic Isom scheme. No quantitative bound on that comparison scheme is used in the component argument.',
   'Finite-etale nilpotent invariance lifts every specified punctured isomorphism; the determinant estimate places it in the same bound dC. The finite-presentation Artinian criteria then give etaleness at all closed points and hence everywhere.',
   'Fixed-class images are disjoint opens, cover all closed points and hence the whole finite-type parameter scheme, and are therefore clopen. Their number is bounded by the number of irreducible components. The proof allows noncanonical geometric lattices in the parameter space.',
   'This removes the coflat/fullness requirement for openness of these actual generated fixed-determinant families. It does not itself provide a polynomial all-object atlas or a representation count.'
  ],
  'fresh_primary_reads':[],
  'reused_previously_checked_inputs':['All exact Stacks08JY/08K6/08K9/088E/0BQB/02HT/02HM/00UR statements and complete written proofs were freshly read by root earlier in this same interval; exact scopes and explicitly omitted dependencies are recorded in audit_intrinsic_unit_Isom_root.json.','Fixed weak/strong-cycle scalar vanishings and the normal-surface Hartogs property.']}
]
for a in cases:
 p=root/a['path'];s=p.read_text()
 assert hashlib.sha256(s.encode()).hexdigest()==a['sha256']
 if 'finite_Frobenius_object_effectivity' in a['path']:
  old=(root/'parts/C/post25_research/finite_Frobenius_object_effectivity_pre_citation.source.txt').read_text()
  before='opens are affine. Their inverse systems have surjective'
  after='opens are affine\n\\citep[Lemma 37.2.3, Tag 06AD]{C_StacksFiniteObjectAffineness}.\nTheir inverse systems have surjective'
  assert s.replace(after,before)==old
 out=root/a.pop('out');assert not out.exists()
 out.write_text(json.dumps({**common,**a},indent=2)+'\n')
 print(json.dumps({'audit':str(out.relative_to(root)),'sha256':a['sha256'],'verdict':'PASS'}))
