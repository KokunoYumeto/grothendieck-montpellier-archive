"""Record root's completed actual-file and exact primary-source proof audits."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

root = Path(__file__).resolve().parents[1]
common = {
    'actor': 'root', 'model': 'GPT-6 Astra Pro',
    'effort': 'setting not independently exposed', 'run': 'SA12 run1',
    'recorded_utc': datetime.now(timezone.utc).isoformat(),
    'type': 'targeted proof check', 'verdict': 'PASS',
    'actual_file_scope': 'Complete actual candidate, every statement and proof line read in full; exact source passages below freshly opened and read.',
    'certificate_scope': 'Mathematical proof audit; no numerical certificate.',
    'research_movement': 'Auxiliary proof input only. No requested-row change or independent main-gate movement.',
}
cases = [
    {
        'path': 'parts/B/post25_research/D_comparable_reduction_cycles_B.tex',
        'sha256': 'c80e280bd42457b5840b5c7638a2201b3c6599df0fd5ee5441d63da8fcb62639',
        'output': 'parts/D/post25_research/audit_B_comparable_reduction_cycles_root.json',
        'labels': ['D:strict-Cartier-separating-parameters', 'D:uniform-comparable-reduction-cycle'],
        'checks': [
            'The positive definite Z-matrix minimization gives a strictly positive rational anti-nef cycle. Proper-curve component degrees and the local-base fibre criterion give relative ampleness on the entire fixed resolution.',
            'The complete-local descending-ideal argument is valid: the stable images modulo every maximal-ideal power form a surjective inverse system; a nonzero compatible lift contradicts Krull intersection for each fixed ideal. Thus eventual ample powers lie in the actual ideal J, without an integral-closure substitution.',
            'The two-section incidence has codimension two at each point of a proper curve and hence is a proper closed subset of the pair space. Properness over a local base propagates fibre generation to all Y. Adding t,ut,vt ensures a nonempty separating differential open, and the two opens meet.',
            'The existing complete-to-henselian equivalence permits the fixed-model different estimate. The exact D.LR.1--5 maximum-principle proof was freshly reread: radial different ratios are bounded, point-mapped relative-minimal curves have nonnegative canonical intersection, and the ratio maximum propagates to a radial component. No arbitrary blowups are allowed.',
            'For Z=alpha C-beta R, coefficientwise C<=Z<=alpha C follows from the actual Jacobian bound. The radial intersection formula and adjunction handle canonical intersection -1. Every nonreduced cycle is treated by the three cases A_B>0, A_B=0<n_B, and A_B=n_B=0 with even negative square.',
            'Both automatic-adjunction inequalities hold on every effective exceptional subcycle, including nilpotent layers. The full internal uniform-generation proof was freshly reread, including point-ideal Tor, duality, and proper formal-functions steps. The previously audited CFHR source input is reused.',
            'The two anti-nef comparisons have the correct signs: -Z^2<=-alpha Z.C<=alpha^2(-C^2). Projection bounds the canonical term through 0<=f_*Z<=alpha t C0; no invalid coefficientwise squaring is used.',
            'The genus bound and H2 vanishing bound h1 on bZ, and cycle Riemann--Roch bounds h0. The conclusion aligns actual Cartier levels but retains every coflat, split-boundary and independent-relation hypothesis.'
        ],
        'fresh_primary_reads': [
            {'url': 'https://stacks.math.columbia.edu/tag/0B5Y', 'locator': 'Lemma 33.44.15', 'scope': 'Complete statement and all written proof; omitted finite-surjective decomposition is the finite disjoint union of the closed reduced components and isolated points.', 'ref': 'turn384591404view0'},
            {'url': 'https://stacks.math.columbia.edu/tag/0D2N', 'locator': 'Lemma 30.21.4', 'scope': 'Complete statement and all written proof.', 'ref': 'turn384591404view1'},
            {'url': 'https://stacks.math.columbia.edu/tag/09MW', 'locator': 'Lemma 32.11.4', 'scope': 'Complete statement and all written proof.', 'ref': 'turn384591404view2'},
            {'url': 'https://stacks.math.columbia.edu/tag/01PR', 'locator': 'Proposition 28.27.13', 'scope': 'All nine conditions and the complete written proof, through implication (9) to (6); condition (7) checked explicitly.', 'refs': ['turn152032087view0', 'turn599391744view0']}
        ],
        'reused_previously_checked_inputs': ['Fixed henselian algebraization and all-complete geometric budgets.', 'First-power Noether-different factorization and separating regular normalization.', 'CFHR automatic adjunction source; current internal uniform-generation proof freshly reread.', 'Later parts of the linear-resolution proof are not a new source-read claim.'],
    },
    {
        'path': 'parts/D/post25_research/D_intrinsic_unit_Isom_for_full_families.tex',
        'sha256': 'c0835bb7a3d245c118cb3ba8720a312dc84086925862ac545c5b63a57ed99e30',
        'output': 'parts/D/post25_research/audit_intrinsic_unit_Isom_root.json',
        'labels': ['D:intrinsic-integral-unit-Hom-jets', 'D:canonical-family-unit-Isom-openness'],
        'checks': [
            'The lattice injection H/I^N H -> H(cC)/I^(N+c)H(cC) is exact because I^(N+c)H(cC)=I^N H. Frobenius of an N-jet has pN precision in the twisted target. No division by a nilpotent Cartier equation occurs.',
            'The finite equation is equivalent to an actual local integral lift having residual order N. Additivity and j -> pj-c then keep all iterates integral and preserve the N-jet; pN-c>N forces the stated orders to infinity.',
            'Formal affine trivializations provide local matrix lifts without global H0 surjectivity. Separatedness gives uniqueness; uniqueness gives overlap gluing and arbitrary coefficient-base functoriality. Reverse jets with finite inverse equations become genuine inverses by the same uniqueness on endomorphisms.',
            'All finite cycles are proper and flat over the parameter base, and the restricted vector bundles meet the exact 08K6 hypotheses. Frobenius gives natural polynomial maps of affine finite-presentation Hom schemes; their equalizer and paired-inverse fibres are affine of finite presentation.',
            'Arbitrary-ring conclusions are formal only. For finite-type or finite local Artinian coefficient algebras, the completed base is Noetherian and cofinal topologies permit full faithfulness of Grothendieck existence. No use of existence on an uncompleted tensor product is made.',
            'The finite-etale frame equivalence retains morphisms, so nilpotent invariance lifts each specified punctured unit isomorphism uniquely. The explicit relative Hartogs module identities and canonical double dual extend it integrally, with reduction compatibility supplied by the hypothesis itself.',
            'The Artinian lifting criterion gives smoothness at every closed point of the finite-type Isom scheme; uniqueness gives zero tangent space and hence etaleness. An open etale locus containing every closed point is the entire finite-type scheme.',
            'Fixed-object Isom images are disjoint opens covering all closed points and hence all S; their complements are unions of the other opens. Each nonempty clopen class contains an irreducible component, proving the stated component bound.',
            'The ordinary canonical forward arrow is regular, while x^p,y^p factorization extends the inverse with pole at most pC. Thus c=p and N=3 satisfy pN-c>N for all p>=2. This uses actual canonical families and does not claim nilpotent gauge control from arbitrary bounded poles.',
            'No effective coordinate/degree bound for the object-family locus, cohomology strata, split-boundary equations, or hereditary representation count follows from this qualitative result.'
        ],
        'fresh_primary_reads': [
            {'url': 'https://stacks.math.columbia.edu/tag/08JY', 'locator': 'Lemma 99.3.9', 'scope': 'Complete statement and complete written proof, including perfect approximation and all-base derived Hom argument.', 'ref': 'turn708043498view3'},
            {'url': 'https://stacks.math.columbia.edu/tag/08K6', 'locator': 'Proposition 99.3.10', 'scope': 'Complete statement and complete written proof; the expressly omitted set-theoretic footnote verification remains a Known input.', 'ref': 'turn152032087view1'},
            {'url': 'https://stacks.math.columbia.edu/tag/08K9', 'locator': 'Proposition 99.4.3', 'scope': 'Complete statement and all written paired-inverse proof; source-omitted routine details remain Known.', 'ref': 'turn152032087view2'},
            {'url': 'https://stacks.math.columbia.edu/tag/088E', 'locator': 'Theorem 30.27.1', 'scope': 'Complete statement and complete written proof through the final Serre-subcategory argument; recursively cited projective and approximation inputs remain Known.', 'refs': ['turn152032087view3', 'turn599391744view1']},
            {'url': 'https://stacks.math.columbia.edu/tag/0BQB', 'locator': 'Lemma 58.8.3', 'scope': 'Complete statement and all written proof, including the general-thickening affine reduction.', 'ref': 'turn599391744view2'},
            {'url': 'https://stacks.math.columbia.edu/tag/02HT', 'locator': 'Lemma 10.141.2', 'scope': 'Complete statement and all written proof, including Artinian quotients, Artin--Rees and split-injection conclusion.', 'refs': ['turn599391744view3', 'turn708043498view0']},
            {'url': 'https://stacks.math.columbia.edu/tag/02HM', 'locator': 'Lemma 37.8.10', 'scope': 'Complete statement and all written proof.', 'ref': 'turn708043498view1'},
            {'url': 'https://stacks.math.columbia.edu/tag/00UR', 'locator': 'Lemma 10.150.3', 'scope': 'Complete statement and all written proof.', 'ref': 'turn708043498view2'}
        ],
        'reused_previously_checked_inputs': ['Finite-etale Lang-frame equivalence for unit cycles.', 'Qualified relative full-pullback realization and module Hartogs.', 'Canonical Cartier-generation and Frobenius pole arguments.'],
    },
]
for case in cases:
    assert hashlib.sha256((root/case['path']).read_bytes()).hexdigest() == case['sha256']
    out = root/case.pop('output')
    assert not out.exists()
    out.write_text(json.dumps({**common, **case}, indent=2)+'\n')
    print(json.dumps({'audit':str(out.relative_to(root)), 'verdict':'PASS', 'sha256':case['sha256']}))
