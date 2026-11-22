"""Record completed actual-file mathematical audits; no theorem is promoted here."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

root = Path(__file__).resolve().parents[1]
common = dict(actor='root', model='GPT-6 Astra Pro',
              effort='setting not independently exposed', run='SA12 run1',
              type='targeted proof check', verdict='PASS',
              recorded_utc=datetime.now(timezone.utc).isoformat(),
              certificate_scope='Mathematical proof audit; no numerical certificate asserted.')

cp = 'parts/C/post24_research/D_primitive_defining_characteristic_orbits.tex'
cs = hashlib.sha256((root/cp).read_bytes()).hexdigest()
assert cs == 'bf43869e7c143256637d46d46f0b6409479406a0682a18b4e9e24f80fb435dc4'
c = dict(common, path=cp, sha256=cs,
 labels=['D:primitive-defining-characteristic-orbit-models'],
 actual_file_scope='Complete original candidate50d42ae9 read, followed by the exact sole binomial-typesetting correction and final hash. Both entire classical and exceptional automorphism-recognition proofs were freshly reread.',
 checks=[
  'The previous actual normal-subgroup embeddings and logarithmic order bounds give A0 inside PΓL_d(F_p^f), index at most six and d²f logp bounded by a constant times log|S|; the geometric radial-tameness hypotheses of their crown applications are not used for these finite-group facts.',
  'Conjugation with the field automorphism on the full matrix algebra is F_p-linear and faithful: the centre detects the field action and the full matrix algebra detects the projective class. This remains valid when p divides the automorphism order.',
  'Induction across the bounded index preserves faithfulness in arbitrary characteristic, since a kernel element must fix coset summands and act trivially on the identity-coset summand. No semisimplicity or division by the index is used.',
  'A finite group whose full socle is a product of nonabelian simple groups has trivial socle centralizer. Any nontrivial normal centralizer would contain a minimal normal subgroup and thus intersect the socle, contradicting its trivial centre. Block permutation modules embed the group with dimension O(log|G|).',
  'The exact known Maróti theorem has three alternatives. In its alternating product case each factor-orbit product of A_m factors is minimal normal in G when m>=5. Thus A_m must belong to the fixed finite list, so m is bounded. The remaining smaller m are bounded directly. N>=2^r controls r and gives log|G|=O((1+logN)²) in every case.',
  'No unproved alternating/Lie isomorphism classification is needed: unbounded defining-characteristic factors explicitly exclude alternating isomorphism types, with any fixed exceptions put in the fixed list.',
  'The existing intrinsic subgroup/stabilizer enumeration has fourth-power dimension cost, giving exp(O((1+log(N+1))^8)). Every fixed polylogarithm is bounded by a constant times Nlog(N+1), with the finite small degrees absorbed in the same constant. The prior global alternating criterion therefore applies in its unchanged geometric and residual-orbit scope.'
 ],
 fresh_primary_reads=[dict(
  url='https://www.renyi.hu/~maroti/primitive.pdf',
  locator='Theorem1.1, author p2; complete written Section2 proof, author pp4--8, including Lemmas2.1 and2.2.',
  scope='Full written passages freshly read and the p2 theorem page actually viewed. Classification, O\u0027Nan--Scott, cited minimal-degree results and calculations explicitly omitted in the paper remain known literature inputs.',
  retrieval_refs=['turn165443465view0','turn956148892view0','turn956148892view2'])],
 reused_previously_checked_inputs=[
  'Full freshly reread files parts/B/post22_research/D_classical_automorphism_crowns_B.tex and D_exceptional_automorphism_crowns_B.tex; their exact earlier Steinberg/Taylor source audits retained.',
  'Previously fully audited intrinsic matrix-model enumeration and original-boundary/global alternating transfer.'
 ],
 research_movement='Named recognition within the same enlarged alternating criterion; no independent movement and no requested-row closure.')
(root/'parts/D/post24_research/audit_C_primitive_defining_orbits_root.json').write_text(json.dumps(c,indent=2)+'\n')

bp = 'parts/B/post24_research/D_ordinary_unit_determinants_cycle_Hom_B.tex'
bs = hashlib.sha256((root/bp).read_bytes()).hexdigest()
assert bs == '9e5333c1ac7a0fa1e9d933dba006b9b79b3a9915fdc6fbe87b8ad96d74ad64e9'
b = dict(common, path=bp, sha256=bs,
 labels=['D:hereditary-ordinary-unit-determinants','D:hereditary-ordinary-unit-finite-cycle-Hom'],
 actual_file_scope='Complete final actual candidate read in sequential pieces, including separating-parameter, reflexive-determinant and absolute-Frobenius precision. Entire fixed-determinant finite-Hom proof and the retained relative-realization theorem freshly reread.',
 checks=[
  'One fixed henselian algebraization, separating parameter ideal and principalized base are chosen before covers. Enlarging the ideal-generator list by consecutive powers of algebraic coordinates ensures the generic differentials span; two general combinations simultaneously give a system of parameters and a separating normalization. This avoids assuming arbitrary ideal generators have independent differentials.',
  'The degree-linear resolution-size theorem is used on this fixed principalized base. Completion preserves the actual model. The chosen cover resolution thus simultaneously has v=O(t), the Cartier powers and the generation-cycle budgets; arbitrary later blowups are not allowed in the component enumeration.',
  'Regular purity gives the scalar-character localization bound. Proper strict-local base change identifies exceptional H1. The constant-sheaf normalization graph gives exponent2sum(g)+b1, and coherent normalization defects at s branches are at least s-1. Surjectivity H1(Y,O) to H1(E,O) therefore bounds the exponent by2pg. This works for composite n prime to p and nonsmooth exceptional components.',
  'For ordinary F_q systems a single F_q* determinant character determines all punctured phases by absolute Frobenius. Its number is at most q^{O(t)}. No twisted projective determinant is substituted for this ordinary character.',
  'The full determinants differ from the fixed full rank-one determinant by integral exceptional divisors. Nonnegative component degrees follow from generic generation. Negative definiteness makes those multidegrees injectively determine the divisor; the Cartier Frobenius recurrence bounds their sum by O(tr). Stars-and-bars with v=O(t) gives exp(O(tlog(r+1))) choices per phase.',
  'Globally generated lines have regular sections on the full nonreduced Cohen--Macaulay cycle. Their exact section sequences bound the four line-bundle blocks of the actual derived Hom complex by O_b(tr_ir_j), without a false H1 bound for an arbitrary lattice subsheaf.',
  'Generating tuples describe locally split exact quotient bundles over every coefficient algebra. Every globally generated geometric rank-r bundle is generated by r+1 general sections on the curve, giving the stated geometric coverage. No Artinian lifting of this choice is inferred.',
  'The fixed two-affine Cech contraction is k-linear and tensors with every coefficient algebra. The relation hδh=0 truncates the transfer, giving differential degree at most two and finite complexes of the claimed size. Actual morphisms are degree-zero cycles modulo explicit boundaries; transferred composition and inverse witnesses have bounded polynomial degree.',
  'The final scope paragraph correctly leaves arbitrary Artinian determinant coverage, coflat/full-module realization, prescribed unit-isomorphism lifting, twisted-PGL determinants and hereditary representation counts unproved.'
 ],
 fresh_primary_reads=[dict(
  url='https://stacks.math.columbia.edu/tag/095T', locator='Theorem59.91.11',
  scope='Complete statement and entire written proper-base-change proof freshly opened/read; cited prior reduction lemmas remain known inputs.',
  retrieval_refs=['turn165443465view1','turn956148892view1'])],
 reused_previously_checked_inputs=[
  'The same-interval full Artin/completion, fixed-base linear resolution-size, Cartier bridge and generation-cycle audits.',
  'ILO ExposéXVI Theorem3.1.1 statement and Corollary3.1.3 complete written proof, previously opened at the exact regular/quasi-excellent scope; no fresh reread of the complete absolute-purity proof asserted.',
  'SGA1 ExposéX Theorem2.6 and preceding argument, previously opened as the proper smooth-curve generation input.',
  'Full freshly reread parts/C/post18_research/D_fixed_determinant_finite_Hom.tex, with its earlier exact Stacks two-affine Cech and flat-base-change source audits retained.'
 ],
 research_movement='Auxiliary finite determinant and actual finite-cycle arrow budgets only; no independent main-gate movement or requested-row change.')
(root/'parts/D/post24_research/audit_B_ordinary_unit_determinants_Hom_root.json').write_text(json.dumps(b,indent=2)+'\n')
print(json.dumps({'verdict':'PASS','primitive_candidate_sha256':cs,'ordinary_unit_candidate_sha256':bs},indent=2))
