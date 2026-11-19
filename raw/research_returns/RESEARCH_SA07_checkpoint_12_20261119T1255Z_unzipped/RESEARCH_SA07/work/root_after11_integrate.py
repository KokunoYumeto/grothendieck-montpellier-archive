"""Integrate audited post-checkpoint11 material without performing a review."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'output' / 'RESEARCH_SA07'
WORK = ROOT / 'work'

section = OUT / 'sections' / 'E_integral_image.tex'
text = section.read_text()
snippet = (WORK / 'E2_30_integrated_text.tex').read_text().strip()
assert snippet.startswith(r'\begin{result}{E.2.30}')
if r'\begin{result}{E.2.30}' not in text:
    text += '\n\n' + snippet + '\n'
text = text.replace('left coset \\(Ht\\) meets \\(F\\)',
                    'open coset \\(Ht\\) meets \\(F\\)')
text = text.replace('is a nonempty left coset of\n',
                    'is a nonempty orbit for left multiplication by\n')
text = text.replace('F_{\\mathrm{CM}}', 'F_{\\mathrm{cm}}')
section.write_text(text)

section = OUT / 'sections' / 'F_audit.tex'
text = section.read_text()
snippet = (WORK / 'F3_35_integrated_text.tex').read_text().strip()
assert snippet.startswith(r'\begin{result}{F.3.35}')
if r'\begin{result}{F.3.35}' not in text:
    text += '\n\n' + snippet + '\n'
section.write_text(text)

old = WORK / 'root_postcheckpoint10_audit.md'
text = old.read_text().replace('## Searches and review scope\n\n', '')
old.write_text(text)

integration = OUT / 'code' / 'integrate_records.py'
text = integration.read_text()
anchor = "         WORK/'root_postcheckpoint10_CHECK_EVENTS.tsv']"
replacement = ("         WORK/'root_postcheckpoint10_CHECK_EVENTS.tsv',\n"
               "         WORK/'root_postcheckpoint11_CHECK_EVENTS.tsv']")
if replacement not in text:
    assert anchor in text
    text = text.replace(anchor, replacement)
    integration.write_text(text)

eventpath = WORK / 'root_postcheckpoint11_CHECK_EVENTS.tsv'
header = ['claim_id', 'date', 'who', 'check', 'details']
rows = []
if eventpath.exists():
    rows = list(csv.reader(eventpath.open(), delimiter='\t'))[1:]
additions = [
    ('F.3.35', 'targeted proof check',
     'Root proved the lower-dimensional projection/zero-section transfer and exact correspondence-space consequence from opened Broe Cor8.2. Triangle independently read the full snippet, source Cor8.2/Prop6.2, Ancona Cor3.19, both explicit elliptic equations, the contravariant Hom codimension, product dimension bound, composition and idempotent lift. The named external preprint theorem remains an external input; no full tensor closure or general numerical equivalence is claimed.'),
    ('E.2.30', 'independent re-proof',
     'Read PC1-PC6 and complete production draft. Checked the actual compactified kernel, virtually abelian residual finiteness, inverse-limit embedding, every original proper lattice, zero deck-invariant space, Smith normal form self-normalizers, all peripheral quotient maps, compatible solution torsors, single conjugator, exact H_c h0 orbit and determinant-unit generator criterion. The mixed-sign peripheral exponent proves strict H_int inclusion; it gives no Galois counterexample.'),
    ('H1-work-50', 'independent re-proof',
     'Checked the actual connected-depth factorization of cyclic ordinary p-power isogenies, differential valuation m, formula max(0,2m-n-b), complete primitive-line counts and both exact parity sums. Opened original Lombardo2015 final PDF Cor9.3 pp2348/2393; finite-index orbit bound is applied to actual G_K orbits. The quantity is the indicated local Neron-frame norm; no global scalar height or H1 conclusion is inferred.'),
    ('F.3.35-source', 'used and rechecked in this run',
     'Downloaded original Broe arXiv2608.28651v1; read Th1.1 p1, Cor1.2 p2, Prop6.2 p17, final proof pp18-19 and Cor8.2 proof p20; visually read original p20. Opened Ancona arXiv1806.03216v3 Th3.18/Cor3.19 p13 and Markman arXiv2502.03415v2 Th1.5.1/Cor1.6.1 p9. Retain dimension-four and specialization directions; no full-power numerical quotient or embedded MT equality asserted.'),
    ('E.2-fourfold-source-search', 'targeted proof check',
     'Primary arXiv2609.27916v2 HTML retrieved successfully after web DisabledError; title metadata and withdrawal banner/comments/history confirm withdrawal08October2026. Its v1 all-powers claims are not used. Broe source is a 2026 preprint; exact original retrieved metadata and hashes retained in work/code_root/fetch_fourfold_sources.json. The initial helper failed for missing requests and was repaired to standard urllib; its successful current source is retained.'),
]
for claim, kind, detail in additions:
    row = [claim, '2026-11-19', 'OpenAI GPT-6 Astra /root', kind, detail]
    if row not in rows:
        rows.append(row)
with eventpath.open('w', newline='') as f:
    writer = csv.writer(f, delimiter='\t', lineterminator='\n')
    writer.writerow(header)
    writer.writerows(rows)

report = OUT / 'RESEARCH_SA07_report.md'
text = report.read_text()
heading = '## Work after checkpoint11'
if heading not in text:
    text += '\n\n' + heading + '\n\n'
    text += (
        'E.2.30 gives the embedded proper-homology completion H_c, its exact '
        'self-normalizer, and an equivalence between all-cover proper lattice '
        'transport and preservation of H_c after one actual inner adjustment. '
        'The aligning elements form exactly H_c h0. Every profinite peripheral '
        'power belongs to H_c, and the explicit mixed-sign unit proves '
        'H_int is strictly contained in H_c. These are actual maps and an '
        'equivalent formulation of the existing premise. The Galois '
        'boundary-extension and discrete-representative gates remain.\n\n'
        'Two coset descriptions in E.2.27-E.2.28 were repaired without '
        'changing any formula: Ht is called an open coset, and B_N u is '
        'described as the orbit for left multiplication by B_N. Earlier '
        'wording had reversed the conventional coset side.\n\n'
        'Root independently checked the cyclic-isogeny denominator average '
        'and the exact finite-index Galois-orbit bound in elliptic work '
        'section50. The single connected branch has linear denominator '
        'growth, while the average of the nonnegative local Neron-frame '
        'denominator norms over all branches tends to zero. These two '
        'proved estimates supply no contradiction and no global height '
        'bound for the actual Hodge coefficient.\n\n'
        'A current original-source search retrieved Broe arXiv2608.28651v1 '
        'and checked its finite-field Tate and arbitrary-field standard-D '
        'fourfold statements at their exact locators. Primary Ancona and '
        'Markman source maps were checked. The direct primary arXiv v2 '
        'record for Li2609.27916 confirms its withdrawal on8October2026; '
        'the all-powers claims in stale search summaries are not used. '
        'No arithmetic Mumford-Tate equality in the fixed Betti frame '
        'was inferred from these cycle results.\n'
    )
    report.write_text(text)
print(json.dumps({'actual_utc': datetime.now(timezone.utc).isoformat(),
                  'integrated': ['E.2.30', 'F.3.35'],
                  'review_performed': False,
                  'checkpoint_created': False}))
