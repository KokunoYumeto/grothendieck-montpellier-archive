"""Record root's completed actual-file proof and source reading checks."""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import hashlib
import json

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
base = {
    'actor': 'root', 'model': 'GPT-6 Astra Pro',
    'effort': 'setting not independently exposed', 'run': 'SA12 run1',
    'recorded_utc': now, 'type': 'targeted proof check', 'verdict': 'PASS',
    'actual_file_scope': 'Complete actual candidate and all proofs read in full; final precision edits separately checked by exact file comparison.',
    'certificate_scope': 'Mathematical proof audit; no numerical certificate is asserted.'
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

path = root / 'parts/C/post24_research/D_matrix_model_alternating_orbits.tex'
old = root / 'parts/C/post24_research/matrix_model_alternating_orbits_initial_audited.source.txt'
assert sha(old) == 'bc7ad88571056e692d21475400f073375090c498cac142be923839ac8199ca4e'
assert sha(path) == 'e73f6444e457c4dfd901fd89145ea6bf910a29777eddfffc752222935b6c0aca'
expected = old.read_text().replace('r_{N,j}^{,2}', 'r_{N,j}^{2}')
expected = expected.replace(
    'most $n^{wn+1}$ and bounds the product of connected\n',
    'most $n^{b_C n+1}$, where $b_C$ is the number of marked\n'
    'points on this particular detecting curve, and bounds the\n'
    'product of connected\n')
assert expected == path.read_text()
record = dict(base, path=str(path.relative_to(root)), sha256=sha(path),
    labels=['D:permutation-matrix-model-count', 'D:alternating-compressed-local-orbits'],
    checks=[
        'An embedding of each fixed permutation model into GL or PGL injects actual Hom sets. Multiplication of the checked conjugacy-class bound by ambient group order gives the actual-Hom bound. The disjoint union of these actual Hom sets surjects onto covered permutation isomorphism classes, without asserting a false injection of permutation classes into linear conjugacy classes.',
        'The affine block matrix is faithful. For every nonempty proper flag type, forgetting flags surjects onto a Grassmannian; the elementary Gaussian-product estimate gives N >= q^(d-1). Fixing every such flag forces a linear map to be scalar. Both model costs are O(log(N)^2), and the number of possible models of degree N is polynomial.',
        'Fixed finitely generated local quotient orbits are joined before counting. Remaining ordered compositions and modelled/uncontrolled choices overcount valid local types. Whole local group orbit energy, not merely curve inertia, pays for uncontrolled orbits.',
        'The disconnected fixed-curve fibre count uses the number b_C of marked curve points, distinguished from w whole local source groups. The full local formal types and degree-linear discriminant bound are unchanged.',
        'Finite normalization and higher-dimensional closure are used only in the previously proved scope. Polynomial natural alternating-kernel multiplicity and the selected simple-product generator bound use the previously audited LMT/Goursat/compactness deduction.',
        'No assertion that every orbit has a small model, that every listed model occurs geometrically, or that the full local prosolvable or global group is finitely generated is made.'
    ],
    fresh_primary_reads=[],
    reused_previously_checked_inputs=[
        'Exact local GL/PGL quadratic-count theorems, whole-orbit permutation count, fixed-formal-curve fibre count and dimensional/normalization closure remain the previously fully audited inputs.',
        'No new external result is invoked by the model enumeration; its affine realization and Gaussian flag counting are proved in the candidate.'
    ],
    exact_delta='Two squared-rank comma typos and the b_C marked-point notation only; exact substitution verified.',
    research_movement='Potential further enlargement of the same restricted alternating criterion; not an independent recognition-family movement and not a requested-row closure.')
(root / 'parts/D/post24_research/audit_C_matrix_model_alternating_root.json').write_text(json.dumps(record, indent=2)+'\n')

path = root / 'parts/D/post24_research/D_hereditary_Cartier_cycle_bridge.tex'
assert sha(path) == '82c9061eaaacbfbf0b22dba8cd1099be214221626043bcfd77819da25404b857'
record = dict(base, path=str(path.relative_to(root)), sha256=sha(path),
    labels=['D:hereditary-Cartier-parameter-jets', 'D:hereditary-Cartier-generation-budget'],
    checks=[
        'Principalizing one fixed separating parameter ideal on the base makes its pullback Cartier on every regular covering model. Local generators x=su,y=sv with (u,v)=1 give (x^b,y^b)=(s^b) for every b, without assuming that the covering morphism is flat.',
        'The Cartier cycle has full support and is anti-nef by its two global generators. Projection gives C^2=t C0^2. The fully reread two-level canonical-module recovery applies on this exact model, with the same fixed saturation level and functorial maps.',
        'The scalar and module cohomology bounds hold for arbitrary complete covers in the prior theorem. Adjunction bounds the absolute canonical intersection with C using these scalar cohomology bounds. No bound on the number of resolution blowups is inserted.',
        'The second assertion retains the separate energy-family hypothesis. Under a point blowup, the arithmetic-genus formula for B=rho^*B0-kE is valid for every integer k, and the pure exceptional case has nonpositive genus. Thus the all-subcycle generation inequality survives pullback and addition of C.',
        'Negative-intersection Cauchy--Schwarz and canonical projection bound the energy of W=rho^*Z0+C. The uniform-generation theorem, reread in full including its Tor term and nonreduced automatic-adjunction proof, applies.',
        'The fixed-ideal Frobenius defect becomes the invertible ideal O(-pC). Cycling its determinant recurrence cancels p^f-1 and yields a period-independent O(tr) degree on C. A regular section of the globally generated determinant and the exact quotient chart give O_b(tr^2) coordinates on each finite Cartier cycle.',
        'Pointwise jet recovery and actual finite-cycle object charts do not imply arbitrary-family realization, a uniform unit-Isom criterion, a hereditary representation count, or a main-gate reduction.'
    ],
    fresh_primary_reads=[
        {'url':'https://stacks.math.columbia.edu/tag/01OF', 'locator':'Lemmas31.33.4--31.33.5', 'scope':'Complete statements and all written proof text freshly opened and read. The source explicitly omits the final local verification in Lemma31.33.4; it is retained as a known input.', 'retrieval_ref':'turn600853793view0'},
        {'url':'https://stacks.math.columbia.edu/tag/0C5H', 'locator':'Lemma54.4.3', 'scope':'Complete statement and entire written proof freshly opened and read.', 'retrieval_ref':'turn600853793view1'},
        {'url':'https://stacks.math.columbia.edu/tag/0C5R', 'locator':'Lemma54.17.1', 'scope':'Complete statement and entire written proof freshly opened and read. Its explicitly omitted reduction details are not claimed independently reconstructed.', 'retrieval_ref':'turn600853793view2'}
    ],
    reused_previously_checked_inputs=[
        'parts/B/post17_research/D_canonical_module_two_level_jets_B.tex: complete271-line file freshly reread.',
        'parts/C/post17_research/D_uniform_generation_cycle_charts.tex: complete334-line file freshly reread.',
        'parts/C/post16_research/D_integral_antinef_energy_cycle.tex: complete154-line file freshly reread.',
        'The underlying Noether-different/canonical-defect, surface-resolution and energy-family inputs retain their prior exact audited scopes.'
    ],
    research_movement='Auxiliary Cartier realization of the existing pointwise parameter jets. Not a hereditary count or independent main-gate movement.')
(root / 'parts/D/post24_research/audit_hereditary_Cartier_bridge_root.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps({'utc':now, 'audits_written':2, 'verdict':'PASS'}, indent=2))
