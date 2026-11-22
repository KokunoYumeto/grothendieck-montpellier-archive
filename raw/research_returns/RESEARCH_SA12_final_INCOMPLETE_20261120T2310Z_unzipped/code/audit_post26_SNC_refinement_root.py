"""Record the author's complete actual-file and primary-source audit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

root = Path(__file__).resolve().parents[1]
path = 'parts/D/post26_research/D_controlled_SNC_refinement_root.tex'
sha = hashlib.sha256((root / path).read_bytes()).hexdigest()
assert sha == '58890bfe636388f2ade972484a6703277eef67ccbc781ab9afbdb8c233322d57'
out = root / 'parts/D/post26_research/audit_controlled_SNC_refinement_root.json'
assert not out.exists()
r = dict(
    actor='root', model='GPT-6 Astra Pro', effort='setting not independently exposed',
    run='SA12 run1', recorded_utc=datetime.now(timezone.utc).isoformat(),
    path=path, sha256=sha, verdict='PASS', type='targeted proof check',
    labels=['D:linear-SNC-refinement-centres', 'D:SNC-refinement-inherited-cycles'],
    actual_file_scope='Both complete saved statements, every proof paragraph, the final scope remark and the entire bibliography were read in two nontruncated chunks after the first combined read was truncated. The truncated output is not counted as an actual full read.',
    certificate_scope='Author construction and complete proof/source audit; no finite numerical certificate.',
    checks=[
        'For a multiplicity-m reduced Cartier boundary, the reduced total transform is pi*D-(m-1)F. The actual exceptional-twist direct images give the exact ideal-sequence quotient of length (m-1)(m-2)/2 and no R1 for the boundary.',
        'Connected components are unchanged. The h1 drop therefore holds also for disconnected proper reduced curves. Every high centre consumes at least one unit and m<=3(m-1)(m-2)/2.',
        'The degree-two tangent cone has total intersection length two. Distinct directions resolve; one direction has at most one unresolved child. A remaining low child consists of two smooth branches with intersection two, whose next blowup has a triple point. No characteristic restriction or division by two is used.',
        'Every initial non-SNC point contributes to normalization defect. Every high vertex has at most m children; deleting high vertices leaves at most delta+sum(m) paths of length at most two. Thus every finite prefix has at most 2delta+7G centres, proving termination.',
        'The exact normalization sequence gives delta=G-sum(g_i)+v-c and the endpoint node bound. Each blowup adds one rational component and preserves all prior normalization genera.',
        'The existing degree-linear cover budgets and coherent fibre-dimension H2 vanishing give h1(E)<=pg and hence degree-linear centres, components, nodes and genera.',
        'Only the old actual Cartier cycles are pulled back. Projection formula, Rrho*O=O and the ideal sequence preserve the full nonreduced cycle cohomology, weak-cycle H1 vanishings and canonical intersections.',
        'Specified generating surjections, determinant markings and actual Frobenius arrows pull back; the inverse retains the pC bound. No assertion of canonical fullness on the new model is made. Coefficient extensions are flat over k.',
        'At every stipulated non-SNC centre m>=2, pi*B-Bnew=(m-1)F>=F=Krelative. Induction and the Jacobian chain rule prove the stated divisor inequalities without redefining Z.',
        'No unsigned adjacent-coefficient product, uniformly controlled twisted anchor or hereditary projective presentation follows. This is an auxiliary geometric clarification, not an additional main-gate movement.'
    ],
    fresh_primary_reads=[
        dict(url='https://stacks.math.columbia.edu/tag/0AGQ', locator='Lemma54.3.1, complete statement and written proof', ref='turn897992424view0'),
        dict(url='https://stacks.math.columbia.edu/tag/0AGR', locator='Lemma54.3.2, complete statement and written proof', ref='turn897992424view1'),
        dict(url='https://stacks.math.columbia.edu/tag/0AGS', locator='Lemma54.3.4, all five parts and all written proof', ref='turn897992424view2')
    ],
    source_qualification='The right-vertical identification explicitly omitted in 0AGS(4), and recursively cited background, remain Known. These complete written primary proofs were actually read during this construction before the saved candidate was re-read; no recursive audit is claimed.',
    reused_dependencies='Previously fully audited all-complete cover budgets, comparable reduction cycles, coherent fibre-dimension vanishing and the Jacobian setup.',
    mathematical_corrections=[], movement_scope='Auxiliary only; no independent main-gate movement.'
)
out.write_text(json.dumps(r, indent=2) + '\n')
print(json.dumps(dict(path=str(out.relative_to(root)), sha256=sha, verdict='PASS')))
