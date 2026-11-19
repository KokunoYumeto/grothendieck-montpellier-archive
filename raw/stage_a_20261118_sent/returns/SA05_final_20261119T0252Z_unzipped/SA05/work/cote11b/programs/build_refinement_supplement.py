"""Materialize manually authored refinements after the independent audit.

All mathematical statements below were authored after reading the original
records, source passages, proofs and the indicated primary-reference passages.
This script only copies provenance and validates identifiers; it does not infer
judgments from headings or keywords. It never edits consolidated or old files.
"""
import csv
import hashlib
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[3]
OWN = BASE / 'work' / 'cote11b'
DATE = '2026-11-19'
claims = {x['id']:x for x in json.loads((BASE/'SA05_claims.json').read_text())}
items = {x['id']:x for x in json.loads((BASE/'SA05_items.json').read_text())}
claim_aliases = {alias:c['id'] for c in claims.values() for alias in c.get('aliases',[])}

def canonical(ident):
    return ident if ident in claims else claim_aliases.get(ident,ident)

specs = [
dict(n=4001, originals=[2010], title='Dimension of a marked partition locus', cls='E',
 statement='Let X be an equidimensional variety of dimension d over a field, with a chosen rational point a. Let R partition a finite index set I, with the empty set explicitly included as one block, and choose J in R. In Z_(R,J) impose equal coordinates on each block and x_i=a for i in J. Then Z_(R,J) is canonically a product of m copies of X, where m=|R|−1−1_(J≠empty). In particular J=empty gives dimension (|R|−1)d. The empty block contributes no coordinate.',
 fate='The explicit coordinate isomorphism proves the correction. The original source convention and the elementary counterexample were checked; no source-specific published erratum was located. This is a present reconstruction, not an emendation of the ink.',
 proof='Choose one coordinate for each nonempty block other than J; the inverse repeats that coordinate on the block and inserts a on J. These two morphisms are inverse.',
 basis='work/cote11b/outputs/proof_notes.md §2; source Pro11/055 lines452–477',
 refs=['StacksCorr'], reopened=[]),
dict(n=4002, originals=[2021], title='Nonzero separation in the span of a cone', cls='E',
 statement='Let C be a closed finitely generated convex cone spanning a finite-dimensional real vector space V. For x in V, x is outside the interior of C if and only if there is a nonzero linear functional ell on V with ell(C)≥0 and ell(x)≤0. For a cone in a larger ambient space, apply this statement in V=span(C) to x in V, using relative interior. The zero functional is never a separator.',
 fate='This is the standard supporting/separating-hyperplane criterion with the missing nonzero condition restored. The GIT cone argument and its zero-functional counterexample were checked. No unrestricted ambient-relative-interior identification is inferred.',
 proof='If x is interior, a nonzero nonnegative functional is strictly positive at x. Conversely, separation from the open convex interior gives a nonzero functional; the cone scaling and 0 in C force the stated signs. The separating-hyperplane step is invoked, not represented as newly proved here.',
 basis='work/cote11b/outputs/proof_notes.md §3; outputs/checks.json ordered_weight_cone is a separate elementary step',
 refs=['MumfordGIT1982'], reopened=[]),
dict(n=4003, originals=[2023], title='Parity character for a regular ordinary quadratic smoothing', cls='B',
 statement='Let S be a henselian trait with algebraically closed residue field of characteristic p≠2. Let f:X→S be proper, with X regular of pure dimension D+1, and smooth except at a single ordinary quadratic point of the special fibre. For rational ell-adic coefficients with ell≠p, the local vanishing-cycle space is a line in relative middle degree D. Inertia acts on that line by the nontrivial quadratic character when D is even, and trivially when D is odd. The regular-total-space hypothesis is essential for this conclusion; an even ramified base change can kill the character and leave a singular total space.',
 fate='Deligne, Weil I §4.2–4.3, gives the regular-total-space hypothesis and parity formula. Those exact passages were reopened during this audit. The ramified flat projective quadric example remains a refutation of the weaker original assumptions.',
 proof='The previously checked projective family sum(x_i²)=t²x_3² is generically constant and has singular total space. It therefore satisfies the old weaker hypotheses but lies outside the regular ordinary-smoothing theorem.',
 basis='work/cote11b/outputs/proof_notes.md §4, Regularity and inertia; outputs/checks.json ramified_quadric_smoothing_counterexample',
 refs=['DeligneWeilI'], reopened=['https://www.numdam.org/article/PMIHES_1974__43__273_0.pdf']),
dict(n=4004, originals=[2024], title='Retaining the degree-zero unit in affine-quadric specialization', cls='B',
 statement='Over C let C0 be the affine cone of the quadratic equation sum(z_i²)=0, and let U={sum(z_i²)=1} have complex dimension D≥1. The cone is contractible, while U deformation retracts onto S^D. Thus H⁰(C0,Z)=H⁰(U,Z)=Z and the only nonzero reduced integral cohomology of U is Z in degree D. A shifted vanishing-cycle comparison must retain the degree-zero specialization map or use reduced cohomology; an unmodified all-degree identification that discards H⁰ is false. This statement fixes the unit issue without choosing an unverified shift convention for the manuscript symbol Phi.',
 fate='The explicit tangent-bundle model and the local specialization sequence establish this correction. Deligne, Weil I §4, supplies the published vanishing-cycle context; the ordinary H⁰ term is not discarded there.',
 proof='Writing z=x+iy identifies U with TS^D by (x,y)↦(x/|x|,y), and fibre scaling gives the retraction. Radial scaling contracts C0. The unit maps to the unit.',
 basis='work/cote11b/outputs/proof_notes.md §4, Punctured cones and coefficients, Affine quadric and orientation',
 refs=['DeligneWeilI'], reopened=['https://www.numdam.org/article/PMIHES_1974__43__273_0.pdf']),
dict(n=4005, originals=[2027], title='Integral cohomology of the punctured odd-dimensional quadric cone', cls='B',
 statement='Let Q be a smooth complex projective quadric of odd complex dimension D=2nu−1 with nu≥1, embedded by its hyperplane bundle, and put E=O_Q(−1) with the zero section removed. Its integral singular cohomology is Z in degrees 0 and 4nu−1, Z/2 in degree 2nu, and zero otherwise. With Z_ell coefficients the middle torsion survives only for ell=2. A finite coefficient group with 2-torsion also gives the adjacent kernel term, so this integral table must not be relabelled as an unrestricted finite-coefficient table.',
 fate='Karpenko Theorem1.10 supplies the integral quadric ring and hyperplane map; the checked Gysin sequence gives the asserted groups. The source degree 2nu−2 is not adopted.',
 proof='Cup product with the Euler class −h is an isomorphism in each one-dimensional middle rank except for the middle multiplication by 2. The Gysin cokernel therefore lies in degree D+1=2nu.',
 basis='work/cote11b/outputs/proof_notes.md §4; outputs/checks.json integral_quadric_Gysin and finite_coefficients_qualification',
 refs=['KarpenkoQuadrics','StacksSelfIntersection'], reopened=[]),
dict(n=4006, originals=[2028], title='Integral cohomology of the punctured even-dimensional quadric cone', cls='B',
 statement='Let Q be a smooth complex projective quadric of even complex dimension D=2nu with nu≥1, and put E=O_Q(−1) with the zero section removed. Its integral singular cohomology is free of rank one in degrees 0, 2nu, 2nu+1 and 4nu+1, and zero otherwise. The lower middle degree is 2nu, not 2nu−1.',
 fate='The opened integral quadric ring and the checked Gysin sequence give the correction with the stated coefficients and dimension range.',
 proof='The middle hyperplane maps have forms Z→Z², 1↦(1,1), and Z²→Z, (a,b)↦a+b, up to choices of signs. Their cokernel and kernel are each Z; all remaining non-end maps are isomorphisms.',
 basis='work/cote11b/outputs/proof_notes.md §4; outputs/checks.json integral_quadric_Gysin and quadric_surface',
 refs=['KarpenkoQuadrics'], reopened=[]),
dict(n=4007, originals=[2034], title='Signed square of the primitive middle class of a quadric', cls='B',
 statement='For a smooth complex projective quadric Q^(2nu), nu≥1, let alpha,beta be the middle classes of the two families of maximal linear subspaces, h the hyperplane class, and lambda=alpha−beta. In the integral Chow ring, and hence in integral singular cohomology, h^nu=alpha+beta, h lambda=0, and lambda²=(−1)^nu h^(2nu). The sign depends on nu.',
 fate='Karpenko Theorem1.10 gives the ruling-intersection parity. The signed formula and the quadric-surface counterexample to a uniform positive sign were checked independently.',
 proof='If nu is even, alpha²=beta²=[point] and alpha beta=0; if nu is odd, alpha²=beta²=0 and alpha beta=[point]. Also h^(2nu)=2[point]. Expanding (alpha−beta)² gives the formula.',
 basis='work/cote11b/outputs/proof_notes.md §4, Integral quadric lattice; outputs/checks.json quadric_surface',
 refs=['KarpenkoQuadrics'], reopened=[]),
dict(n=4008, originals=[2079], title='Dual simple vectors use the inverse Gram matrix', cls='E',
 statement='In the essential Euclidean reflection representation of a finite real reflection group, let alpha_i be inward unit simple normals and let G be their positive-definite Gram matrix, with G_ij=−cos(pi/m_ij) for i≠j. The dual simple vectors have Gram matrix G^(−1); their normalized cosine is (G^(−1))_ij divided by sqrt((G^(−1))_ii(G^(−1))_jj). Every entry of G^(−1) is nonnegative, so two vectors in the same closed essential chamber have nonnegative scalar product. No equality of those dual cosines with cos(pi/m_ij) is asserted.',
 fate='The normal-angle formula is classical; the inverse-matrix identity and positivity argument are directly checked. The essential-space restriction excludes the free fixed orthogonal factor. The unidentified typescript is not silently attributed to Bourbaki.',
 proof='For b≥0 and Gx=b, write x=x_+−x_- with disjoint nonnegative supports. If x_-≠0, then x_-^T b=x_-^T Gx_+−x_-^T Gx_-<0, contradicting b≥0. Hence G^(−1) is entrywise nonnegative.',
 basis='work/cote11b/outputs/proof_notes.md §7; outputs/checks.json reflection_dual_angle_alarm',
 refs=['Coxeter1934'], reopened=[]),
dict(n=4009, originals=[3062], title='Special weight-zero coefficients and finite monodromy', cls='B',
 statement='Let S be connected and locally noetherian, with ell invertible, and interpret the source special-weight-zero class as Q_ell-subquotients of R⁰g_*Q_ell for smooth projective morphisms of relative dimension zero, allowing finite sums. A lisse Q_ell-sheaf belongs to this class if and only if its monodromy image is finite. Any finite-monodromy representation is a summand of finitely many copies of a finite-group regular representation, realized by a finite étale cover. Arbitrary lisse Q_ell-sheaves need not have finite monodromy.',
 fate='The finite-étale/permutation description and characteristic-zero finite-group representation theory prove the equivalence. The manuscript meaning of locally constant remains an ink/context question, so the corrected modern interpretation does not decide an author error.',
 proof='A relative-dimension-zero smooth projective map is finite étale, so its R⁰ is a finite permutation representation. Conversely use the finite quotient through which the given monodromy factors and average to split the regular representation.',
 basis='work/cote12c/proofs.md §2; outputs/calculations.json unipotent family; Pro12/111 lines318–322',
 refs=['SGA1','Deligne1980WeilII'], reopened=['https://publications.ias.edu/sites/default/files/Number40.pdf']),
dict(n=4010, originals=[3005], title='Geometric semisimplicity of a pure lisse sheaf', cls='B',
 statement='Let X0 be normal and of finite type over a finite field F_q, let ell be different from its characteristic, and let F0 be a lisse Q_ell-sheaf which is pointwise pure for the chosen weight embedding. Its pullback to X0 over the algebraic closure of F_q is semisimple. This is geometric semisimplicity; purity alone does not imply semisimplicity of the arithmetic representation, even on Spec F_q.',
 fate='Deligne, Weil II Theorem3.4.1(iii) and its proof3.4.5, gives exactly this statement. The theorem and proof were reopened in the independent audit. The rank-two unipotent arithmetic example does not refute the separate motivic semisimplicity conjecture.',
 proof='The published proof reduces to a smooth dense open and splits extensions geometrically using equal weights. Independently, a↦I+aN on the ell-primary coordinate of Zhat, with N²=0≠N, is continuous and pure of weight0 but arithmetically nonsplit.',
 basis='work/cote12c/proofs.md §2; outputs/calculations.json unipotent family',
 refs=['Deligne1980WeilII'], reopened=['https://publications.ias.edu/sites/default/files/Number40.pdf']),
dict(n=4011, originals=[3041], title='Bounded denominators suffice for finitely generated integral Hom', cls='E',
 statement='Let V be a finite-dimensional rational vector space and H an additive subgroup, such as the proposed integral Hom group. If there are an integer N≥1 and a finitely generated Z-lattice L in V with H contained in N^(−1)L, then H is a finitely generated Z-module. An integral reference-system axiom must actually supply this uniform denominator bound before the conclusion is used. The existence of a rationalization or Serre-quotient equivalence by itself does not supply the bound.',
 fate='This is the elementary noetherian-module argument. Tate’s integral Hom results are verified examples in their precise abelian-variety setting; they are not a theorem about an unspecified integral motive category. The weaker arbitrary-lattice model is refuted by the already checked all-prime denominator example.',
 proof='Multiplication by N identifies H with a subgroup of the finitely generated free abelian group L. Since Z is noetherian, every such subgroup is finitely generated. In contrast, a subgroup of Q containing 1/p for every prime p has no common denominator and is not finitely generated.',
 basis='work/cote12c/proofs.md §10; outputs/calculations.json lattice-denominator family; current audit explicitly adds the necessary uniform-bound hypothesis',
 refs=['Tate1966Endomorphisms','Faltings1986Finiteness'], reopened=[]),
dict(n=4012, originals=[3049], title='Extension from a puncture under the low-ramification hypothesis', cls='B',
 statement='Let (R,m) be a regular local ring of mixed characteristic (0,p), of dimension at least2, and suppose p is not in m^p. Every abelian scheme already given on Spec R minus its closed point extends uniquely to an abelian scheme over Spec R. This positive theorem requires both the punctured-base abelian scheme and the ramification hypothesis; it does not assert that arbitrary all-prime unramified generic realization data automatically produce that punctured-base object.',
 fate='Vasiu–Zink Corollary4 says that R is quasi-healthy; Definition2 states the exact extension property. Both were reopened. Their Theorem28 and the checked example R=W(k)[[x,y]]/(p−(xy)^(p−1)) show why the unrestricted source sufficiency statement fails.',
 proof='The positive result is the opened Corollary4, not a newly reproved extension theorem. The existing nonextension proof verifies all-prime nonramification using purity for ell≠p and the fact that S[1/p] lies in the puncture.',
 basis='work/cote12c/proofs.md §11; outputs/calculations.json ramification check',
 refs=['VasiuZink2010','Stacks0BMA','SerreTate1968GoodReduction'], reopened=['https://arxiv.org/pdf/0909.0969']),
dict(n=4013, originals=[3030], title='Local weight four in the split multiplicative elliptic case', cls='B',
 statement='For the Legendre smooth projective elliptic family over P¹_F5 minus {0,1,infinity}, let F=R¹g_*Q_ell, ell≠5. At either split multiplicative boundary point0 or1, local inertia cohomology is H¹(I,F)=F_I(−1)=Q_ell(−2), in geometric-Frobenius convention, and has weight4. Consequently a universal local bound for this exact strictly special coefficient class must allow weight4 at i=n=j=1. No general replacement for the manuscript coefficient bound is established by this example.',
 fate='The split local representation, its coinvariant twist and all geometric hypotheses were checked in the saved proof. Weil II1.8.4 supplies the monodromy-weight framework. A global ordinary-cohomology bound cannot replace this local assertion.',
 proof='At0 and1 the nodal tangent cones split over F5, the tame monodromy is nonzero unipotent, and F has an invariant Q_ell line with quotient Q_ell(−1). Taking coinvariants and the tame-cohomology twist gives Q_ell(−2).',
 basis='work/cote12c/proofs.md §4; outputs/calculations.json Legendre/Tate matrices',
 refs=['Deligne1980WeilII','Ito2020WeightMonodromy'], reopened=['https://publications.ias.edu/sites/default/files/Number40.pdf']),
dict(n=4014, originals=[3018,3026], title='Numerical Hodge-level bound with the coefficient shift', cls='B',
 statement='Let X be a smooth separated complex algebraic variety of dimension n and let g:Y→X be smooth projective of relative dimension j≥0. Let F be a rational direct summand of R^j g_*Q and assume the compatible relative Lefschetz splitting realizes H^i(X,F) as a direct summand of H^(i+j)(Y,Q) in mixed Hodge structures. Then its Hodge level is at most min(i+j,2n−i+j), with vanishing outside the possible cohomological range. This is a numerical Hodge-level bound under the stated realization/splitting hypotheses; it does not establish the manuscript geometric motivic level for arbitrary admissible coefficients or singular X.',
 fate='Deligne1968 Proposition2.4 supplies the relative splitting criterion; Hodge III8.2.4 gives the Hodge-coordinate bounds for the total space. These exact statements were reopened. The additional mixed-Hodge-compatible summand hypothesis is explicitly retained rather than inferred from a bare vector-space splitting.',
 proof='The total space has dimension N=n+j and cohomological degree k=i+j. The Hodge coordinates lie between max(0,k−N) and min(k,N), hence |p−q|≤min(k,2N−k)=min(i+j,2n−i+j). A mixed-Hodge direct summand inherits the bound.',
 basis='work/cote12c/proofs.md §§3–4; existing total-space argument for C3015; current independent coordinate-bound check',
 refs=['Deligne1968Lefschetz','Deligne1974HodgeIII'], reopened=['https://www.numdam.org/item/PMIHES_1968__35__107_0.pdf','https://numdam.org/item/PMIHES_1974__44__5_0.pdf']),
dict(n=4015, originals=[3029], title='The abutment uses E-infinity subquotients', cls='E',
 statement='For a bounded convergent cohomological spectral sequence in an abelian category, the induced filtration on H^n has associated graded pieces E_infinity^(p,n−p), and each such term is a subquotient of E_2^(p,n−p). Identifying a whole E_2 term with the abutment piece requires the relevant later differentials to vanish, as well as any compatibility needed to call that piece a specified weight piece. In the local double-blowup example the nonzero E_2^(0,2) is killed, so only a possible contribution through a subquotient survives as the defensible general formulation.',
 fate='The subquotient statement is the formal definition of passage between spectral-sequence pages and convergence. The checked local purity/SNC example shows the missing degeneration hypothesis. The Pro s’identifie/Codex intervient variant remains an undecided reading.',
 proof='Each E_(r+1) is ker(d_r) modulo im(d_r), so repeated passage gives a subquotient of E_2. Convergence identifies E_infinity with the associated graded. The existing double-blowup calculation has injective outgoing d_2 on E_2^(0,2).',
 basis='work/cote12c/proofs.md §6; outputs/calculations.json double-blowup matrix and ranks; Pro12/120 lines771–776 and Codex K12-08 line214',
 refs=['Riou2010Purity','Deligne1974HodgeIII'], reopened=['https://www.imo.universite-paris-saclay.fr/~joel.riou/doc/annulation.pdf']),
dict(n=4016, originals=[3036], title='Exact late untwisted type of a Tate local term', cls='B',
 statement='Over a finite field F_q with ell different from its characteristic, use the late untwisted dimension-type convention: type≤d is generated under finite sums, subquotients and extensions by untwisted cohomology of smooth projective varieties of dimension≤d. For r≥1, Q_ell(−r) has minimal type exactly r. It occurs as (R^r j_*Q_ell)_0 for j:G_m^r→A^r, and as H^(2r)(P^r,Q_ell). Thus the strict r−1 bound in this test cannot hold. This conclusion gives no general ordinary-direct-image theorem from the separate compact-support bound, and it does not concern the earlier Tate-stable D filtration.',
 fate='The opened SNC exterior formula gives the local term; Weil purity gives its weight2r and bounds every untwisted dimension≤r−1 generator by2r−2. The projective-space realization supplies the matching upper type.',
 proof='Weights≤2r−2 are preserved by the listed closure operations, whereas Q_ell(−r) has weight2r. Thus its type is at least r; H^(2r)(P^r)=Q_ell(−r) shows type at most r.',
 basis='work/cote12c/proofs.md §7; outputs/calculations.json SNC top Tate obstruction',
 refs=['Riou2010Purity','Deligne1980WeilII'], reopened=['https://www.imo.universite-paris-saclay.fr/~joel.riou/doc/annulation.pdf','https://publications.ias.edu/sites/default/files/Number40.pdf']),
]

def unique(seq):
    out=[]
    for value in seq:
        if value not in out: out.append(value)
    return out

new=[]
for spec in specs:
    originals=[claims[canonical(f'SA05-C{n}')] for n in spec['originals']]
    ident=f"SA05-C{spec['n']}"
    assert ident not in claims, ident
    item_ids=unique(i for c in originals for i in c['items'])
    assert all(i in items for i in item_ids), item_ids
    lines=unique(line for c in originals for line in (c['lines'] if isinstance(c['lines'],list) else [c['lines']]))
    source_scopes=unique(c.get('consolidation_scope','') for c in originals)
    original_ids=[c['id'] for c in originals]
    new.append(dict(
        id=ident,items=item_ids,cote=originals[0]['cote'],
        scans=unique(s for c in originals for s in c['scans']),lines=lines,
        his_statement='Original formulation being corrected, not the new assertion: '+' | '.join(c['his_statement'] for c in originals),
        statement=spec['statement'],status_on_pages='current reconstruction',
        computation={'existing_evidence':spec['basis'],'audit_argument':spec['proof'],
                     'execution_status':'Existing outputs reviewed; no new computation or formal certificate is claimed for this supplemental audit.'},
        **{'class':spec['cls']},fate=spec['fate'],
        fate_date='Current refinement registered 2026-11-19. Original source date record: '+' | '.join(c['fate_date'] for c in originals),
        present_status=f'As of {DATE}: Established in the explicitly stated corrected scope. '+('The broader source programme remains open or unidentified where expressly stated above.' if spec['n'] in [4011,4012,4013,4014] else 'No diplomatic reading is changed.'),
        refs=spec['refs'],confidence='high',origin='Current-run refinement of '+', '.join(original_ids),
        refines=original_ids,refined_statement=None,status_category='current-run refinement',
        title=spec['title'],author='Current audit reconstruction; see original_source_attribution',
        original_source_attribution=[{'id':c['id'],'attribution':c.get('author',c.get('attribution','Grothendieck manuscript, with the interpretation qualifications stated in the original record'))} for c in originals],
        source_scopes=source_scopes,consolidation_scope='cote11b-refinement-audit',aliases=[],
        search_ids=[f'REF-{ident}'],
        inherited_search_ids={c['id']:c.get('search_ids',[]) for c in originals},
        independent_audit='Source wording, hypotheses, existing proofs/outputs and stated primary passages compared; no unseen image or external proof is certified.',
    ))

corrections={}
for spec in specs:
    for original in spec['originals']:
        corrections[canonical(f'SA05-C{original}') ]={
            'refined_id':f"SA05-C{spec['n']}",
            'action':'replace invalid, self, or non-equivalent target',
            'reason':spec['title']+'. The replacement is the explicit corrected assertion, with its own scope and provenance; it is not the refuted source wording.',
        }
for original,target,reason in [
    (2008,2009,'Remove the .statement pseudo-ID. C2009 retains generation and the realization-kernel question, without universal linear independence.'),
    (2048,2049,'Remove the .statement pseudo-ID. C2049 is the actual separate maximal-torus refinement, with its additional hypothesis.'),
    (2060,2059,'Remove the .statement pseudo-ID. C2059 is the rank-bearing number-field theorem; the false rankless invariant is not the replacement.'),
    (3008,3007,'Confirm only the ordinary constant-coefficient weight/Hodge bound as the safe weaker statement. The exact stricter source quantifier remains an undecided reading.'),
    (3016,3015,'Confirm the coarser ordinary-cohomology bound under the same direct-summand family hypotheses; it does not restore the false sharper weight bound.'),
    (3017,3023,'Confirm the compact-support range with its precise direct-summand hypotheses, not the false uniform lower bound j.'),
    (3031,3028,'Confirm only the restricted positive-dimensional immersion/SNC local theorem using image dimension. No general d_y(f) theorem or actual-fibre-dimension substitution is certified.'),
    (3043,3042,'Confirm generic full faithfulness and conditional internal abelianness/subquotient behavior. Ambient extension closure is explicitly excluded.'),
]:
    key=canonical(f'SA05-C{original}')
    corrections[key]={'refined_id':canonical(f'SA05-C{target}'),'action':'use existing corrected claim','reason':reason}
    if key != f'SA05-C{original}':
        corrections[key]['premerge_statement_id']=f'SA05-C{original}'

new_ids={x['id'] for x in new}
for original,row in corrections.items():
    assert original in claims
    assert row['refined_id'] in claims or row['refined_id'] in new_ids
    assert row['refined_id'] != original

with (BASE/'SA05_searches.tsv').open() as f:
    prior_searches=list(csv.DictReader(f,delimiter='\t'))
search_rows=[]
events=[]
who='GPT-6 Astra Pro; inherited active effort; SA05/cote11b independent refinement audit'
for claim,spec in zip(new,specs):
    originals=set(claim['refines'])
    matched=[r for r in prior_searches if originals & set(re.findall(r'SA05-C\d+',r['claim_ids']))]
    assert matched,claim['id']
    prior=[]
    inherited_urls=[]
    queries=[]
    venues=[]
    for row in matched:
        record=json.loads(row['record_json'])
        prior.append({'scope':row['scope'],'search_id':row['search_id'],
                      'claim_ids':row['claim_ids'],'record':record})
        for field in ['queries','query','queries_normalized']:
            if record.get(field): queries.append(str(record[field]))
        for field in ['venue','venues']:
            if record.get(field): venues.append(str(record[field]))
        opened=record.get('opened_urls',[])
        if isinstance(opened,str): opened=opened.split(';')
        inherited_urls.extend(u.strip() for u in opened if u.strip())
    search_rows.append({
        'search_id':claim['search_ids'][0],'date':DATE,'claim_id':claim['id'],
        'original_claim_ids':';'.join(claim['refines']),
        'claim_scope':claim['statement'],'queries':'; '.join(unique(queries)),
        'venues':'; '.join(unique(venues)),
        'method':'Reuse of exact documented source-family searches plus independent scope/proof review; specified primary URLs reopened. The original queries were not re-issued merely to manufacture new search events.',
        'outcome':claim['fate'],'opened_urls':';'.join(unique(spec['reopened'])),
        'inherited_family_opened_urls':';'.join(unique(inherited_urls)),
        'url_scope':'opened_urls lists only primary URLs reopened in this independent audit. Inherited family URLs are preserved for provenance, not asserted to support every refinement; exact support is limited to reference_keys and checked_extent.',
        'reference_keys':';'.join(claim['refs']),
        'reopened_in_this_audit':';'.join(spec['reopened']),
        'checked_extent':spec['basis']+'; '+spec['proof'],
        'limits':'No new global theorem, unseen manuscript reading, full external-proof audit, or executed formal certificate is inferred.',
        'source_search_records':json.dumps(prior,ensure_ascii=False),
    })
    events.append({'statement_id':claim['id'],'date':DATE,'who':who,
        'type':'used and rechecked in this run',
        'outcome':'Explicit refinement checked against the original hypotheses, source wording and saved evidence. '+spec['proof']+' Evidence: '+spec['basis']+'. Existing outputs reviewed; no new execution claimed.'})
    events.append({'statement_id':claim['id'],'date':DATE,'who':who,
        'type':'carried as background without fault found',
        'outcome':'Provenance/search audit only, not a separate mathematical proof. Search mapping '+claim['search_ids'][0]+' retains the exact reused searches and marks any newly reopened primary passages. Original author wording is not replaced by this current reconstruction.'})

for original,row in corrections.items():
    events.append({'statement_id':original,'date':DATE,'who':who,
        'type':'carried as background without fault found',
        'outcome':'Refutation-event target audit only; not a new refutation or computation. Use refined statement '+row['refined_id']+'. '+row['reason']})

(OWN/'refinement_claims.json').write_text(json.dumps(new,ensure_ascii=False,indent=2)+'\n')
(OWN/'event_target_corrections.json').write_text(json.dumps(corrections,ensure_ascii=False,indent=2)+'\n')
for name,rows in [('refinement_search_log.tsv',search_rows),('refinement_CHECK_EVENTS.tsv',events)]:
    with (OWN/name).open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)

audit={'date':DATE,'new_claim_count':len(new),'new_ids':sorted(new_ids),
       'event_target_corrections':len(corrections),'search_rows':len(search_rows),
       'audit_events':len(events),'all_existing_item_and_refinement_ids_resolve':True,
       'old_records_modified':False,
       'input_claims_sha256':hashlib.sha256((BASE/'SA05_claims.json').read_bytes()).hexdigest(),
       'limitation':'Reference key aliases are intentionally left for the central bibliography consolidation.'}
(OWN/'outputs'/'refinement_validation.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(audit,ensure_ascii=False,indent=2))
