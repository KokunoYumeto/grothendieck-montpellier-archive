"""Record completed root mathematical/source reads; no theorem promotion."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()

def record(name, path, expected, labels, checks, fresh, reused):
    data = (root / path).read_bytes()
    assert hashlib.sha256(data).hexdigest() == expected
    out = root / 'parts/D/post23_research' / name
    assert not out.exists()
    audit = {
        'actor': 'root', 'model': 'GPT-6 Astra Pro',
        'effort': 'setting not independently exposed', 'run': 'SA12 run1',
        'recorded_utc': now, 'type': 'targeted proof check',
        'path': path, 'sha256': expected, 'labels': labels, 'verdict': 'PASS',
        'actual_file_scope': 'Complete actual candidate proof read and its displayed maps, quantifiers, edge cases and constants checked.',
        'checks': checks, 'fresh_primary_reads': fresh,
        'reused_previously_checked_inputs': reused,
        'certificate_scope': 'A mathematical proof audit; no numerical certificate is asserted.',
        'research_movement': 'Not counted separately; any main-gate change belongs to a completed theorem and the next formal review.'
    }
    out.write_text(json.dumps(audit, indent=2) + '\n')
    return str(out.relative_to(root))

records = []
records.append(record(
    'audit_global_finite_puncture_projective_growth_root.json',
    'parts/D/post23_research/D_global_finite_puncture_projective_growth_root.tex',
    'a4dc93accb491adf249ef68706ca295a3914c28c5be3635b8130582ec857454a',
    ['D:global-finite-puncture-projective-growth',
     'D:global-projective-finite-puncture-closure',
     'D:global-unrestricted-projective-simple-products'],
    [
        'Original completed-local PGL classes restrict to actual full local curve types. Repeated local sources may be counted independently as an overcount. Their realized highest-break bound is fixed.',
        'The fixed-local-type curve constant is uniform over the local types, q and rank. Restriction along the original-group surjection is injective on ambient conjugacy classes. No global Brauer assertion is used.',
        'The generic surface is fixed once. The controlled-centre theorem is used only in its codimension-at-least-two clause. Finite normalization preserves the dimension/codimension scope; lower-dimensional components meet no omitted set.',
        'For a fixed tuple of PGL torsors, equivariant Isom is finite etale of degree |PGL|. A section is determined at one point on each connected double-product component. Effective finite-proper descent yields at most |PGL|^a classes.',
        'Distinct simple quotient kernels stay distinct under ambient conjugacy. Polynomial multiplicity, the exact generating-tuple estimates, Goursat and compactness prove only the stated simple-product conclusion.',
        'The classical and exceptional projective embeddings/order estimates are purely finite-group inputs. Their crown geometry and radial-tameness hypotheses are not imported into these embeddings. Fixed finite exceptions are harmless.'
    ],
    [
        {'path': 'parts/C/sources/sga1/smf_doc-math_3_01.tex', 'locator': 'Expose IX Theorem4.7, original pp238--239', 'scope': 'Full theorem and entire written proof reread.'},
        {'path': 'parts/C/sources/sga1/smf_doc-math_3_01.tex', 'locator': 'Expose X Theorem2.6, original pp272--273', 'scope': 'Full curve-generator statement and preceding lifting/specialization proof reread.'},
        {'path': 'parts/D/sources/FiniteGroups/LMT2020_published.txt', 'locator': 'Lemma2.5 and Proposition2.6, pp10--13; equations2.1--2.2 onp12', 'scope': 'Full statements and complete written proofs reread. The older arXiv numbering differs and is not used.'}
    ],
    [
        'Exact detecting-curve/local-type proof and its fresh Stacks/Hu--Teyssier audits in this post23 session.',
        'Three fixed-local curve units and their complete root audit at candidate750f4a06; final promotion changes status only.',
        'Arbitrary-SNC local PGL theorem, all-dimensional local closure, finite-puncture generic surface and controlled-boundary theorem: actual dependency statements and relevant full transfer proofs reread.',
        'Classical and exceptional embedding/order proofs and their exact original-primary audits from post22; no new original Steinberg source read is claimed here.'
    ]
))

records.append(record(
    'audit_fixed_local_quotient_alternating_root.json',
    'parts/C/post23_research/D_fixed_local_quotient_alternating.tex',
    '65444607d39f82d410ffba2b673503c196ef8c0d04162eb7ad0464637c1009b8',
    ['D:fixed-local-quotient-alternating-count'],
    [
        'The p-characteristic constant H1 bound and prime-to-p SNC purity bound give one finite generator bound for all maximal pro-ell quotients.',
        'The Frattini argument assumes no prior finite generation: a proper closed generated subgroup has proper image in a finite ell-group and is annihilated by a nonzero elementary character.',
        'Finite nilpotent images factor through the product of the maximal pro-ell quotients. Coprime-order subdirectness and compactness prove both surjectivity and the simultaneous bounded generating tuple.',
        'Assigning controlled orbits to a fixed quotient and joining them costs at most (n+1)^J(n!)^d0. Only the remaining full completed-local orbits enter the square-sum. The representation-to-permutation loss from the preceding lemma is retained.',
        'The complete local algebras and different bound are unchanged. Multiplication by the fixed-formal curve fibre estimate preserves n^(A n). The A_n kernel/product argument is the already checked one.',
        'Nilpotent, rather than solvable, is the justified concrete local image class. No local maximal-prosolvable finite-generation assertion is used.'
    ],
    [
        {'path': 'sources/ILO2012/tex/exposes/gysin.tex', 'locator': 'Expose XVI Theorem3.1.1 and Corollary3.1.3, printed pp242--243', 'scope': 'Full statements and complete normal-crossings corollary proof reread. The absolute-purity theorem itself is a known input, not independently reproved here.'}
    ],
    [
        'Complete relevant local-p-H1 proof and local constant-H2 proof reread; their earlier primary-source audits are reused.',
        'The full local-orbit/factorial theorem, fixed-formal fibre proof, and LMT simple-product argument were independently checked earlier in this post23 session.'
    ]
))

search = {
    'recorded_utc': now,
    'queries': [
        '"punctured" "normal surface" "projective representations" finite field',
        '"fundamental group" "local" "alternating" "nilpotent" surface singularity',
        'normal proper surfaces punctured fundamental groups finite generation representations characteristic p Langer',
        'etale fundamental group surface singularity representation growth projective finite fields'
    ],
    'coverage': 'Both available search engines were used; the second pass targeted arXiv and author/university primary domains.',
    'outcome': 'No exact global PGL growth theorem or restricted alternating factorial theorem was identified in these returned results. Broadly related characteristic-zero, quotient-singularity, and projective-variety results do not identify the statements proved here.',
    'qualification': 'This is a scoped search log, not evidence of novelty or priority. Search snippets are not used as mathematical authority. Known inputs retain their exact opened primary locators.'
}
(root / 'parts/D/post23_research/root_global_and_local_quotient_literature_search.json').write_text(json.dumps(search, indent=2) + '\n')
print(json.dumps({'utc': now, 'audit_records': records, 'status': 'PASS; no promotion or archive created'}, indent=2))
