"""Serialize manually adjudicated cross-package comparisons; no verdict inference."""
import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/workspace/scratch/208fb206de03')
OUT = ROOT / 'work/outputs'
PARTS = ['cote62', 'cote63', 'cote64_early', 'cote64_late']
STAMP = datetime.now(timezone.utc).isoformat(timespec='seconds')
REVIEWER = 'GPT-6 Astra Pro; effort inherited/unspecified; SA16-2026-11-19-cote64-early'

def load(part, kind):
    return json.loads((ROOT / 'work/parts' / part / (kind + '.json')).read_text())

problems = {x['id']: x for part in PARTS for x in load(part, 'problems')}
claims = {x['id']: x for part in PARTS for x in load(part, 'claims')}

def source(name, ranges, observation):
    folder = 'pro' if name.startswith('MPL') else 'codex'
    return {'file': f'sources/SA16_texts/{folder}/{name}_transcription.tex',
            'physical_lines_1_based': ranges, 'observed': observation,
            'check_kind': 'used and rechecked in this run; passage comparison, not a new proof check'}

E = 'MPL_64_040-077'
A = 'MPL_64_078-115'
B = 'MPL_64_116-157'
D = 'MPL_64_002-039'
P = 'MPL_62_002-050'

root_passages = [
    source(E, [[806,843]], 'Quadratic specialization and the arbitrary-base J,t,T equivalence; source explicitly includes base change.'),
    source(A, [[395,464]], 'The same geometric equivalence, then a conditional reference root and its mu2 twists; the orientation datum is an additional choice.')]
pin_passages = [
    source(E, [[887,910]], 'Compatible squares, two geometric pinnings, and the extra orientation datum when J varies.'),
    source(A, [[124,154],[209,241]], 'Fixed alpha gives a mu2 torsor; varying alpha gives a separate mu4 torsor and quotient.'),
    source(B, [[149,158]], 'Fixed-alpha and varying-alpha formulations are distinguished again.')]
normalization_passages = [
    source(A, [[382,391],[623,652],[683,706]], 'The level-four construction is requested; the linear condition is separated from the deferred square equation.'),
    source(B, [[76,125],[222,289]], 'The relative level-four map is resumed; square condition 83c and choice independence remain deferred.')]
cohomology_passages = [
    source(P, [[12,61],[67,89],[141,155]], 'Smooth elliptic scheme, cohomology/base change and the pole graded lines.'),
    source('H63-03', [[12,115]], 'Integral reduced genus-one fibers may be nodal or cuspidal; duality/evaluation and the cubic construction are explicit.'),
    source(A, [[716,761]], 'Field-valued genus-one Riemann--Roch and the graded derivation, not the whole relative theorem.')]
coordinate_passages = [
    source(P, [[161,279],[289,330]], 'Smooth relative cubic atlas, primitive generator, inversion and the conditions on 2 and 3.'),
    source('H63-03', [[77,115],[210,316]], 'The genus-one normal forms include singular fibers; d6=0 requires 2 and c4 invertible.'),
    source(A, [[943,958],[1044,1077],[1286,1296]], 'Monic squarefree cubic over the stated field; centered choice only away from characteristic 3.')]
trace_passages = [
    source('K62-01', [[11,13],[53,58]], 'Barycenter divides by the section degree; 3 is explicitly inverted for the trisection.'),
    source(E, [[364,406]], 'Trace-square conic in P(p_*O_J) and trace-zero projective target are separate objects, with only 2 inverted.'),
    source(A, [[918,941],[984,997]], 'Branch-value injectivity/Vandermonde and trace-centering are different assertions; the latter explicitly excludes characteristic 3.')]
auto_passages = [
    source(P, [[739,775],[810,837],[860,889]], 'Anharmonic S3 normalizer and its characteristic 2/3 exceptions on a projective line.'),
    source(E, [[228,303],[327,343]], 'Bare octahedral stabilizer and opposition-reconstruction assertions affected by characteristic 5.'),
    source('H63-04', [[152,221]], 'Elliptic automorphism group schemes and their characteristic 2/3 specializations.'),
    source('K63-01', [[274,274]], 'A common order-24 subgroup claim, distinct from an order or extension-degree bound.')]
local_passages = [
    source('K63-02', [[189,229],[247,298],[302,327]], 'Distinct questions about divisor regularity, versal equations, branch tangents, effective action, and extending an automorphism of the universal family.')]
formal_passages = [
    source('H63-01', [[176,237]], 'Integral formal series and a sign-sensitive formal secant calculation.'),
    source('H63-04', [[269,281]], 'Separate margin requests for Hasse invariant, canonical lift, modular forms and explicit formal group.'),
    source('K62-01', [[435,443]], 'Complex Weierstrass/sigma/zeta addition formulas in the factor-4 convention.'),
    source('K62-03', [[33,77]], 'Analytic addition and duplication, with half-period normalization.'),
    source(A, [[1100,1123],[1184,1214],[1242,1256]], 'Algebraic monic-cubic third intersection, with distinctness and extension restrictions.')]
hodge_passages = [
    source('K63-01', [[279,354]], 'Canonical de Rham basis and questions about vanishing and algebraicity of the Hodge shift.'),
    source('K63-02', [[5,65],[147,158]], 'Conjugate-linear involution, pairing compatibility, proposed bound and phase invariant.'),
    source(B, [[546,573],[662,692],[855,879],[934,1010]], 'Complex structures on a real plane, sign convention and holomorphic framed-family reconstruction.')]
gerbe_passages = [
    source(P, [[304,306],[1084,1088],[1232,1256]], 'Pointed-trisection quotient and loss of the central elliptic involution.'),
    source('K62-01', [[11,13],[53,58]], 'The coefficient line uses centering and its additional invertibility hypothesis.'),
    *root_passages]
extension_passages = [
    source(D, [[1581,1603],[1608,1633],[1640,1688]], 'Projective mod-4 lift through its central extension and prescribed diagonal/codiagonal torsors.'),
    source(A, [[269,305]], 'Different central extension of S3, the order-12 pinning-change group.'),
    source(P, [[289,330]], 'Affine coefficient change with its central mu2; different quotient and moduli data.')]

def problem_link(n, ids, title, scope, reason, passages):
    return {'decision_id': f'XPL-{n:02d}', 'problem_ids': ids,
            'decision': 'link only; retain every problem identifier',
            'keep_ids': ids, 'aliases': [], 'title': title,
            'combined_scope_for_navigation_only': scope,
            'rationale': reason,
            'source_occurrences': {i: problems[i]['occurrences'] for i in ids},
            'passages_read': passages}

problem_links = [
    problem_link(1, ['MP-SA16-01','MP-SA16-02','MP-SA16-243','MP-SA16-244'],
        'Relative cohomology, duality and cubic embedding',
        'Cohomology supplies the pole filtration and embedding; duality identifies the invariant line.',
        'The cote62 requests concern smooth elliptic schemes and a length-two very-ampleness proof. The Deligne-formulary questions include integral singular genus-one fibers, dualizing sheaves and the canonical flex/basis. Neither all hypotheses nor requested conclusions coincide.', cohomology_passages),
    problem_link(2, ['MP-SA16-05','MP-SA16-08','MP-SA16-10','MP-SA16-244','MP-SA16-245'],
        'Coordinate atlases and distinct normalizations',
        'Relative cubic generation, atlas size, inversion, short form and d6 gauge are connected coordinate questions.',
        'Primitive ideal generation is not parameter minimality; inversion removes mixed terms when 2 is invertible, centering additionally needs 3, while d6=0 uses c4 invertible. The singular-fiber moduli scope in cote63 is retained.', coordinate_passages),
    problem_link(3, ['MP-SA16-11','MP-SA16-16','MP-SA16-17','MP-SA16-95','MP-SA16-161'],
        'Kummer and elliptic reconstruction with different target data',
        'Descent links invariant conditions, torsor quotients, general pointed tame covers and quadratic elliptic reconstruction.',
        'Cote62 asks which invariants extend over a normal base and about an S3 quotient. Early64 asks for an arbitrary-G tangential category whose literal target omits inertia compatibility. Late64 is the quadratic elliptic case plus a distinguished Q0 normalization. The general counterexample cannot be transferred to the proved quadratic geometric equivalence.',
        [source(P, [[338,440],[1125,1127],[1154,1160],[1232,1256]], 'Kummer invariant conditions and quotient-torsor description.'), source(E, [[744,804],[806,843]], 'General tame-G target followed by the quadratic specialization.'), *root_passages, source(A, [[146,154]], 'Explicit reconstruction from pinned branch data is deferred.')]),
    problem_link(4, ['MP-SA16-96','MP-SA16-97','MP-SA16-161','MP-SA16-163','MP-SA16-164','MP-SA16-165'],
        'Reference square, pinning torsors and the unfinished symmetric normalization',
        'Q0 and fixed-orientation root data precede the coordinate line, its square scale and the symmetric level-four map.',
        'The Q0 promise is fulfilled at scan78. Fixed-alpha mu2 torsor existence locally is established. The coordinate line is determined up to scalar. Recovering its exact square scale and constructing the symmetric base-change-compatible level-four map require further data and remain distinct tasks. A parent problem may link these dependencies but must not alias them or report all of them solved by the geometric category equivalence.',
        [source(E, [[848,910]], 'Q0 promise, root line and varying-J qualification.'),source(A, [[6,31],[146,154],[486,706]], 'Reference definition, deferred reconstruction and the linear/square distinction.'), *pin_passages, *normalization_passages]),
    problem_link(5, ['MP-SA16-18','MP-SA16-90','MP-SA16-91','MP-SA16-163','MP-SA16-166'],
        'Degree-three data: trace conic, centering and restriction',
        'Cubic etale data recur in a conic quotient, barycenter, pinning coordinates and branch evaluations.',
        'The trace form on a cubic etale algebra is nondegenerate without inverting3. Dividing the trace of constants to obtain a centered complement requires3 invertible. The conic Tr(y^2)=0 is not its trace-zero projective target, and the rank-two branch restriction is not the rank-three Vandermonde map. These different tasks cannot be consolidated as a single trace claim.', trace_passages + [source(A, [[486,706]], 'Pinning membership equations determine a line; their square scale is separate.')]),
    problem_link(6, ['MP-SA16-12','MP-SA16-13','MP-SA16-89','MP-SA16-246','MP-SA16-247','MP-SA16-264'],
        'Different automorphism problems and exceptional primes',
        'Track the marked object and the effective group before comparing stabilizer calculations.',
        'Anharmonic normalizers, octahedral bare/opposition stabilizers and elliptic automorphisms are different groups acting on different objects. Characteristic5 extra octahedral symmetries do not answer characteristic2/3 elliptic questions. An abstract group of the same order does not establish a common embedding. The disconnected-base group-scheme qualification is also independent.', auto_passages),
    problem_link(7, ['MP-SA16-81','MP-SA16-88','MP-SA16-162'],
        'Orientation conventions and distinct central extensions',
        'Orientation choices influence the mod-4 and pinning actions.',
        'Choosing an orientation comparison is not solving the D8 lift obstruction, and the order-12 pinning-change extension of S3 is not the mod-4/projective-octahedral extension. Preserve both kernels, quotients and obstruction problems.', [source(D, [[202,225]], 'Orientation comparison convention.'), *extension_passages, source(A, [[193,204],[248,263],[269,366]], 'Modular action on the pinned parameter space.')]),
    problem_link(8, ['MP-SA16-93','MP-SA16-94','MP-SA16-167','MP-SA16-241','MP-SA16-252'],
        'Doubling, algebraic secants and the formal group',
        'These use the elliptic group law in different coordinate categories.',
        'Intrinsic doubling on a four-point projective line, a particular final rational normalization, a monic affine secant formula, signs in a formal local calculation and the full universal formal group are not the same requested construction. Analytic half-period conventions do not transfer automatically to formal coordinates.', [source(E, [[545,569],[591,631]], 'Intrinsic quotient and final duplication formula.'), *formal_passages]),
    problem_link(9, ['MP-SA16-168','MP-SA16-169','MP-SA16-265','MP-SA16-266','MP-SA16-268','MP-SA16-269'],
        'Real structures, period conventions and Hodge questions',
        'A period normalization connects complex structures to the Hodge splitting, but does not identify their questions.',
        'The late64 questions concern choosing a complex structure and holomorphic naturality of framed families. Cote63 concerns the canonical second-kind Hodge coefficient, its zero locus, algebraicity, an erroneous bound and a phase invariant. In particular a complex-structure equivalence does not settle the algebraic-de-Rham CM converse.', hodge_passages),
    problem_link(10, ['MP-SA16-247','MP-SA16-264','MP-SA16-271','MP-SA16-272','MP-SA16-273','MP-SA16-275'],
        'Abstract automorphisms versus deformation and universal-family action',
        'Small-characteristic automorphisms control local level-three geometry only after retaining the effective action and branch stabilizers.',
        'An automorphism-group classification does not determine tangent directions. A versal ring, its group action, four branch tangents and extension of an automorphism over the glued family are separate claims. Central kernel versus coarse action, and stabilizing one branch versus every branch, must remain visible.', auto_passages[2:] + local_passages),
    problem_link(11, ['MP-SA16-249','MP-SA16-250','MP-SA16-251','MP-SA16-252','MP-SA16-271'],
        'Hasse invariant, ordinary lift and supersingular deformation',
        'These neighboring marginal requests refer to different constructions in characteristic p.',
        'The intrinsic Hasse section is not an explicit canonical-lift formula. The unique ordinary Serre--Tate lift is not a chosen supersingular lift; a supersingular versal deformation ring has a parameter. Integral modular-form base change and a universal formal group are further distinct targets.', [source('H63-04', [[224,281]], 'Integral modular-form discussion and four separate margin requests.'), source('K63-02', [[277,298]], 'The requested supersingular completed local rings and divisor equations.')]),
    problem_link(12, ['MP-SA16-253','MP-SA16-255','MP-SA16-260','MP-SA16-261'],
        'Congruence thresholds, eigenlines, uniqueness and coefficient rings',
        'Atkin congruence questions share a p-adic framework while keeping their quantifiers.',
        'An eventual threshold for each exponent is weaker than an additive uniform threshold. Literal uniqueness of functions differs from uniqueness of a residue class/eigenline, and an integral Fourier spanning assertion requires its own coefficient ring. These are distinct even within cote63 and are unrelated to elliptic square-root torsor uniqueness.', [source('H63-07', [[180,257],[263,292]], 'Conjectures1/2 and3, fixed-beta convergence, literal uniqueness, integral-Fourier spanning and distinct-spectrum criterion.')])
]

def claim_link(n, ids, title, reason, passages):
    return {'decision_id':f'XCL-{n:02d}', 'claim_ids':ids,
            'decision':'link only; do not merge whole claim records', 'title':title,
            'rationale':reason,
            'source_occurrences':{i:{k:claims[i].get(k) for k in ['cote','scans','lines','status_on_pages','class']} for i in ids},
            'passages_read':passages}

claim_links = [
    claim_link(1,['C-SA16-1','C-SA16-3','C-SA16-516','C-SA16-812','C-SA16-813'],
        'Field, relative smooth and singular genus-one cohomology',
        'The late64 record is a field Riemann--Roch/principal-part statement; cote62 includes arbitrary base change and negative n; cote63 includes nodal/cuspidal fibers and dualizing evaluation. Common specializations do not give identical hypotheses and conclusions.',cohomology_passages),
    claim_link(2,['C-SA16-2','C-SA16-6','C-SA16-7','C-SA16-814','C-SA16-816','C-SA16-528'],
        'Cubic models with different moduli scope',
        'Very-ampleness, primitive ideal generation, framed smooth atlas, singular genus-one normal form and algebraically closed monic-cubic reconstruction have different conclusions and base hypotheses. Preserve the singular compactification and smooth open separately.',coordinate_passages),
    claim_link(3,['C-SA16-5','C-SA16-517','C-SA16-518','C-SA16-519','C-SA16-521'],
        'Invariant derivative, graded symbol, full kernel and parity',
        'The common symbol is -n, but C5 also extends the relative derivation, C517 adds the Rees Leibniz rule, C518 refutes a multiplicatively normalized coefficient-one claim, C519 computes the full characteristic-p kernel, and C521 concerns parity. Zero graded symbol is not a zero full derivative. Stage1 item8/521 consolidation therefore does not identify these whole claim records.',
        [source(P,[[103,155]],'Correct characteristic-dependent symbol and intrinsic graded multiplication.'),source(A,[[716,795],[807,900]],'Field construction, coefficient-one arrows, kernel claim and parity.')]),
    claim_link(4,['C-SA16-12','C-SA16-14','C-SA16-526','C-SA16-817'],
        'Inversion, centering and c4-open gauge',
        'The inversion statement includes characteristic2 and a central coordinate-group extension; centering an n-section requires [n] invertible; the late trace complement is the n=3 field specialization; the d6=0 gauge instead needs 2 and c4 invertible. These are related, not equal.',coordinate_passages+trace_passages),
    claim_link(5,['C-SA16-14','C-SA16-269','C-SA16-524','C-SA16-526'],
        'Trace conic versus trace-centering and branch restriction',
        'C269 works with cubic etale algebras and only2 invertible, and constructs a smooth conic/degree4 quotient. C14 and C526 divide the trace of constants by3 for a barycenter/complement. C524 concerns rank-two evaluation and a separate rank-three Vandermonde statement. The same trace notation does not identify these objects.',trace_passages),
    claim_link(6,['C-SA16-27','C-SA16-293','C-SA16-512'],
        'Coefficient-line gerbe versus canonical tangent root',
        'C27 includes centered coefficients over6 invertible and splitting the Brauer obstruction using a degree-one line. C293/C512 give a canonical norm-convention tangent-root category over2 invertible and arbitrary cubic etale J. The shared mu2 mechanism is linked; the extra assertions and hypotheses forbid a whole-record merge.',gerbe_passages),
    claim_link(7,['C-SA16-291','C-SA16-391','C-SA16-293','C-SA16-512'],
        'General tangential Kummer target and quadratic specialization',
        'The arbitrary-G target is false without actual inertia compatibility; C391 records necessary compatibility, not a proved repaired general equivalence. The quadratic elliptic case has a proved geometric equivalence. Its truth does not repair every arbitrary-G category.',[source(E,[[744,843]],'General category, omitted compatibility and subsequent quadratic specialization.'),*root_passages]),
    claim_link(8,['C-SA16-296','C-SA16-502'],
        'Correct line twist specialization and missing tensor power',
        'The early square-root line construction and the later false formula for arbitrary modules share the scalar twist law, but the literal conclusions differ. Preserve the missing-power error at scan80 and the correct O(2) specialization at81.',[source(E,[[848,910]],'Line square and reference square twist.'),source(A,[[65,83],[98,106]],'General tensor formula missing a square and its correct line specialization.')]),
    claim_link(9,['C-SA16-297','C-SA16-501'],
        'Forward reference closure versus rotation-group correction',
        'The same Q0 item is merged at Stage1, but C297 records closure of a promised construction and C501 distinguishes the four-element group mu4 from the two-element torsor mu4*. They are different conclusions.',[source(E,[[848,883]],'Q0 construction postponed.'),source(A,[[6,31]],'Q0 definition and deleted star.')]),
    claim_link(10,['C-SA16-298','C-SA16-503','C-SA16-504','C-SA16-505','C-SA16-515','C-SA16-535'],
        'Fixed mu2 torsor, varying mu4 torsor and symmetric normalization',
        'Only C298/C503 are duplicates. The varying-alpha mu4 quotient, pinned fine-moduli identification, tensor-square scale and symmetric relative level-four map have additional data and conclusions. The current proof of the geometric root category does not complete those normalizations.',pin_passages+normalization_passages),
    claim_link(11,['C-SA16-244','C-SA16-245','C-SA16-507','C-SA16-12'],
        'Different central extensions',
        'The mod-4/projective-octahedral lift and its D8 cup-product obstruction have different quotient groups from the order-12 extension of S3 and the affine coefficient-coordinate group. Matching a central mu2 or an order is insufficient for identity.',extension_passages),
    claim_link(12,['C-SA16-507','C-SA16-821','C-SA16-841'],
        'An abstract order-12 isomorphism is not a common geometric action',
        'C507 computes a pinning-change extension. C821 classifies elliptic automorphisms in several characteristics, including an abstractly isomorphic C3 semidirect C4 at3. C841 refutes a common SL2(F3) embedding. The actions, bases and conclusions remain different.',[source(A,[[269,305]],'Pinning-change group.'),source('H63-04',[[152,221]],'Elliptic automorphism classification.'),source('K63-01',[[274,274]],'Common order24 subgroup assertion.')]),
    claim_link(13,['C-SA16-271','C-SA16-532'],
        'Klein extension and its elliptic translation formula',
        'C271 proves a unique relative V4 extension for any etale four-section; C532 identifies elliptic two-torsion translation and its fixed values in a particular monic coordinate, including the r=0 issue. The latter specializes the same geometric subgroup but adds different conclusions.',[source(E,[[348,360],[574,587]],'Relative Klein extension and coordinates.'),source(A,[[1332,1353]],'Two-torsion translation formula.'),source(B,[[4,49]],'Matrix and fixed-value continuation, including denominator issue.')]),
    claim_link(14,['C-SA16-8','C-SA16-801','C-SA16-815','C-SA16-840'],
        'Repeated invariant polynomial inside broader formularies',
        'The same discriminant polynomial is a common subclaim, but C8 asserts the smooth relative unit criterion, C801 is a field formulary with other invariants/differentials, C815 compares completed cubic invariants and C840 includes characteristic-specific normal forms, twists and repeated errors. Do not merge these compound records merely because one polynomial agrees; an atomized edition could extract that shared subclaim separately.',[source(P,[[211,225]],'Omitted discriminant and relative smoothness context.'),source('H63-01',[[25,84]],'Full invariant formulary.'),source('H63-03',[[117,194]],'Completed cubic invariants.'),source('H63-09',[[1,354]],'Repeated formulary already reviewed by its owner; comparison here uses its full claim record, not a claim of personally rereading all354 lines in this consolidation.')]),
    claim_link(15,['C-SA16-40','C-SA16-49','C-SA16-523','C-SA16-842'],
        'Factor-four, monic and analytic normalizations',
        'C40 includes relative Lie-frame scaling; C49 supplies analytic invariants and root identities; C523 isolates an unresolved manuscript principal-part convention and factor-four/monic rescaling; C842 identifies a specific complex de Rham basis. Normalization conversion links them without making the hypotheses and full conclusions identical.',[source('K62-01',[[103,183],[305,335]],'Relative Lie-frame calculation and analytic factor-four equation.'),source(A,[[878,900],[943,958],[1315,1329]],'Monic claim and normalization convention.'),source('K63-01',[[279,335]],'Canonical analytic coordinates and de Rham basis.')]),
    claim_link(16,['C-SA16-55','C-SA16-529','C-SA16-530','C-SA16-807'],
        'Analytic addition, algebraic secants and integral formal law',
        'The complex factor-four formula and sigma identity, the monic-cubic distinct-point criterion, its rational third-intersection extension and the integral formal power series law have different hypotheses and normalizations. They imply related specializations but are not whole-record duplicates.',formal_passages),
    claim_link(17,['C-SA16-17','C-SA16-71','C-SA16-803','C-SA16-849'],
        'Different normalized j invariants and twist/divisor questions',
        'Cote62 uses both i=1-j/1728 and J=j/1728; cote63 uses classical j, a generic representative with twists, and special-locus divisor/torsor counts. Preserve these coordinate conversions and the distinction between a representative and classification over the ground field.',[source(P,[[485,526],[571,602],[638,684]],'Cubic invariant normalization.'),source('K62-03',[[514,541]],'Analytic J normalization and special values.'),source('H63-01',[[123,131]],'Generic classical-j model.'),source('K63-02',[[189,229]],'Divisor multiplicities and special-locus torsors.')]),
    claim_link(18,['C-SA16-77','C-SA16-539','C-SA16-544','C-SA16-842'],
        'Individual uniformization versus a framed holomorphic family',
        'C77 includes elliptic-function degree and inverse integral; C539 states a single lattice-quotient correspondence; C544 is a relative holomorphic fine-moduli assertion with global framing; C842 selects coordinates and a second-kind basis. Their shared uniformization is only part of each conclusion.',[source('K62-01',[[263,343]],'Elliptic functions, degree and inverse integral.'),source(B,[[524,544],[934,1010]],'Individual real/complex quotient and framed-family construction.'),source('K63-01',[[279,335]],'Canonical analytic model.')]),
    claim_link(19,['C-SA16-540','C-SA16-542','C-SA16-543','C-SA16-843','C-SA16-844','C-SA16-845','C-SA16-847','C-SA16-848'],
        'Complex structures and the canonical Hodge coefficient',
        'Real-plane complex structures and holomorphic period conventions do not assert the zero locus, arithmetic algebraicity, pairing bound or phase of the canonical Hodge coefficient. In particular the unresolved algebraic splitting converse remains separate.',hodge_passages),
    claim_link(20,['C-SA16-263','C-SA16-363','C-SA16-821','C-SA16-850','C-SA16-851','C-SA16-852','C-SA16-853'],
        'Exceptional stabilizers and level-three deformation geometry',
        'Characteristic5 octahedral symmetries concern a six-point divisor. Characteristic2/3 elliptic automorphisms, versal equations, four branch tangents, the ineffective central kernel and gluing an automorphism concern a different level-three geometry. Even the two refutations of uniqueness/tangency do not share hypotheses.',auto_passages[1:]+local_passages)
]

# Omit an overbroad source-range claim in XCL14: this reviewer read the
# compound C840 record, not every line of its underlying repeat formulary.
claim_links[13]['passages_read'] = claim_links[13]['passages_read'][:-1]
claim_links[13]['record_only_comparison'] = {'claim':'C-SA16-840','scope':'Full structured claim record read; original H63-09 record was independently source-checked by the cote63 owner. No new whole-H63-09 passage-check event is asserted here.'}

claim_merges = [
    {'proposal_id':'XCM-01','claim_ids':['C-SA16-293','C-SA16-512'],'keep_id':'C-SA16-293','aliases':['C-SA16-512'],
     'identity_test':{'base':'Arbitrary scheme S with2 invertible','fixed_data':'Cubic etale J, its three-marked projective line Sigma_J and t disjoint from J','objects':'Elliptic double covers with identified branch data; invertible T with T^2 isomorphic to T_(Sigma_J,t)','morphisms':'Branch-compatible elliptic isomorphisms and square-compatible line isomorphisms','conclusion':'Equivalence of groupoids, compatible with base change, using the same norm convention'},
     'combined_statement':'Over S with2 invertible, for fixed cubic etale J and t disjoint from its trisection on Sigma_J, elliptic double covers with identified branch data form the same groupoid as invertible lines T with T^2≅T_(Sigma_J,t), using the fixed norm convention. Locally both are mu2 twist groupoids; deck -1 acts by -1 on the tangent line. Effective descent yields the arbitrary-J assertion.',
     'rationale':'The actual early source explicitly says arbitrary base and base change; the late source restates exactly the same J,t,T equivalence. The earlier structured phrase three labels is not a restriction to split J: the diplomatic passage and its present-status field both include cubic etale J.',
     'canonical_class_recommendation':'B','class_reason':'Root adjudication: retain B for the exact relative branch/root comparison supported by the modern Legendre atlas and this run\'s descent proof. Do not infer an exact first-publication date from that comparison.',
     'occurrence_assessments':{i:{k:claims[i].get(k) for k in ['class','status_on_pages','fate','fate_date','refs','confidence']} for i in ['C-SA16-293','C-SA16-512']},
     'refs_union':sorted(set(claims['C-SA16-293']['refs']+claims['C-SA16-512']['refs'])),
     'passages_read':root_passages,
     'proof_reference':'work/parts/cote64_early/proof_supplement.md §9; independently read and checked by cote64_late in this run.',
     'proof_convention_to_preserve':'For x=u y^n, N(y)=(-1)^(n-1)x/u; retain the explicit norm-versus-leading-jet sign. Neither geometric equivalence nor changing a chosen local sign identifies the distinguished symmetric mu4 normalization.',
     'excluded_claims':['C-SA16-504','C-SA16-505','C-SA16-515','C-SA16-535'],
     'agreement':'Late64 confirmed exact identity; root confirmed canonical class B with occurrence-level E retained.'},
    {'proposal_id':'XCM-02','claim_ids':['C-SA16-298','C-SA16-503'],'keep_id':'C-SA16-298','aliases':['C-SA16-503'],
     'identity_test':{'base':'Scheme with2 invertible','fixed_data':'E/S, branch data, fixed reference square and fixed orientation alpha','objects':'Isomorphisms of the two tangent root lines respecting their given squares','conclusion':'Finite etale mu2 torsor, locally nonempty, geometrically two elements; no global section asserted'},
     'combined_statement':'For fixed E/S and orientation alpha, compatible isomorphisms between the tangent root line and the reference root form an etale mu2 torsor. Over an algebraically closed field there are two; arbitrary bases need not admit a section. Inverting an isomorphism reconciles the two displayed arrow directions without changing the torsor.',
     'rationale':'Both occurrences state exactly the fixed-square Isom torsor. The later varying-alpha mu4 assertion is a distinct claim, not a different name for this mu2 torsor.',
     'canonical_class_recommendation':'E','class_reason':'Root adjudication: the fixed-square Isom torsor is elementary classical Kummer/descent. Preserve the earlier B comparison to a later Legendre atlas as occurrence provenance.',
     'occurrence_assessments':{i:{k:claims[i].get(k) for k in ['class','status_on_pages','fate','fate_date','refs','confidence']} for i in ['C-SA16-298','C-SA16-503']},
     'refs_union':sorted(set(claims['C-SA16-298']['refs']+claims['C-SA16-503']['refs'])),
     'passages_read':pin_passages,
     'excluded_claims':['C-SA16-504','C-SA16-505','C-SA16-515','C-SA16-535'],
     'agreement':'Late64 confirmed exact identity; root confirmed canonical class E with occurrence-level B retained.'}
]

def inventory(kind):
    result=[]
    for part in PARTS:
        path=ROOT/'work/parts'/part/(kind+'.json')
        records=json.loads(path.read_text())
        result.append({'part':part,'path':str(path.relative_to(ROOT)),
                       'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                       'count':len(records),'ids':[x['id'] for x in records]})
    return result

base={'reviewer':REVIEWER,'date':'2026-11-19','recorded_at':STAMP,
      'method':'Manual semantic review of all listed structured statements, hypotheses, conclusions and problem requests. Candidate overlaps were compared to actual transcript passages; explicit record-only exceptions are identified. Scripts only serialize these authored decisions, attach original occurrence data and validate identifiers/line ranges. No verdicts were inferred by keyword or script. No part files were edited.',
      'scope_boundary':'This is a consolidation audit, not a new literature search or proof certification. Source passage comparison is recorded as used and rechecked in this run.'}
problem_out={**base,'review_id':'SA16-global-problem-consolidation-early64',
             'inventory':inventory('problems'),'recommended_merges':[],
             'conclusion':'No exact cross-package problem duplicate was identified. Retain all problem IDs. Connected requests are linked below because their requested conclusions, fixed data or hypotheses differ.',
             'links_not_merges':problem_links,
             'reviewed_total':len(problems),'recommended_total_after_merges':len(problems)}
claim_out={**base,'review_id':'SA16-global-claim-consolidation-early64',
           'inventory':inventory('claims'),'recommended_merges':claim_merges,
           'links_not_merges':claim_links,
           'reviewed_total':len(claims),'recommended_total_after_merges':len(claims)-2,
           'supplement_boundary':'C859/C860 are included only after their complete authored records have been read by this reviewer; see supplemental_review field if present.',
           'classification_rule':'Keep manuscript proof status per occurrence. Canonical B/E recommendations are root-adjudicated mathematical fate labels; they do not assign exact historical priority.'}

# Supplemental files are incorporated only following an explicit manual review.
supplement_path=OUT/'cross_consolidation_supplement_review.json'
if supplement_path.exists():
    supplement=json.loads(supplement_path.read_text())
    claim_out['supplemental_review']=supplement

for name,value in [('cross_problem_merge_proposals.json',problem_out),('cross_claim_merge_proposals.json',claim_out)]:
    (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

events=[]
for kind,data in [('problem',problem_out),('claim',claim_out)]:
    for inv in data['inventory']:
        events.append({'recorded_at':STAMP,'kind':'catalogue read','target':inv['path'],
                       'ids':';'.join(inv['ids']),'detail':f"All {inv['count']} {kind} records read for hypotheses/request/conclusion comparison; no new proof check asserted."})
    for entry in data['recommended_merges']+data['links_not_merges']:
        key=entry.get('proposal_id',entry.get('decision_id'))
        ids=entry.get('claim_ids',entry.get('problem_ids',[]))
        events.append({'recorded_at':STAMP,'kind':'manual consolidation decision','target':key,'ids':';'.join(ids),
                       'detail':entry.get('rationale','')})
        for passage in entry['passages_read']:
            events.append({'recorded_at':STAMP,'kind':'used and rechecked in this run','target':passage['file']+':'+','.join(f'{a}-{b}' for a,b in passage['physical_lines_1_based']),
                           'ids':';'.join(ids),'detail':'Passage comparison, not proof certification. '+passage['observed']})

with (OUT/'cross_consolidation_review_log.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['recorded_at','kind','target','ids','detail'],delimiter='\t')
    w.writeheader();w.writerows(events)

statement_events={}
for kind,data in [('problem',problem_out),('claim',claim_out)]:
    for entry in data['recommended_merges']+data['links_not_merges']:
        key=entry.get('proposal_id',entry.get('decision_id'))
        for identifier in entry.get('claim_ids',entry.get('problem_ids',[])):
            row=statement_events.setdefault(identifier,{'statement_id':identifier,'date':'2026-11-19',
                'who':REVIEWER,'type':'used and rechecked in this run','outcome':[],
                'artifact':[], 'scope':'Manual source-passage and mathematical-identity comparison; not a new proof certification, literature search or ink decision.'})
            row['outcome'].append(key+': '+entry['rationale'])
            row['artifact'].append('work/outputs/cross_'+kind+'_merge_proposals.json:'+key)
            if identifier=='C-SA16-840':
                row['type']='carried as background without fault found'
                row['scope']='Full structured claim record compared for scope only; its owner checked the manuscript. This consolidation did not independently reread the full repeated formulary.'
with (OUT/'cross_consolidation_check_events.tsv').open('w',newline='') as f:
    fields=['statement_id','date','who','type','outcome','artifact','scope']
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader()
    for identifier,row in sorted(statement_events.items()):
        row['outcome']=' | '.join(row['outcome']);row['artifact']='; '.join(row['artifact'])
        w.writerow(row)

errors=[]
for kind,data,registry in [('problem',problem_out,problems),('claim',claim_out,claims)]:
    for entry in data['recommended_merges']+data['links_not_merges']:
        for i in entry.get('claim_ids',entry.get('problem_ids',[])):
            if i not in registry: errors.append('missing identifier '+i)
        for passage in entry['passages_read']:
            path=ROOT/passage['file']
            if not path.exists():errors.append('missing source '+str(path));continue
            n=len(path.read_text().splitlines())
            for a,b in passage['physical_lines_1_based']:
                if not (1<=a<=b<=n): errors.append(f'invalid lines {path}:{a}-{b}/{n}')
aliases=[i for m in claim_merges for i in m['aliases']]
assert len(aliases)==len(set(aliases))
validation={'recorded_at':STAMP,'result':'PASS' if not errors else 'FAIL','errors':errors,
            'problem_records':len(problems),'problem_merges':0,'problem_link_groups':len(problem_links),
            'claim_records':len(claims),'claim_merges':len(claim_merges),'claim_link_groups':len(claim_links),
            'review_log_events':len(events),'statement_check_events':len(statement_events),
            'limits':'Mechanical checks validate identifiers and source ranges only; the comparison decisions are manually authored.'}
(OUT/'cross_consolidation_validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(validation,ensure_ascii=False))
if errors: raise SystemExit(1)
