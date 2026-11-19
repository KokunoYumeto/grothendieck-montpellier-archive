"""Retain the opened characteristic-zero theorem and exact category map."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import re

BASE = Path(__file__).resolve().parent.parent
OUT = BASE / 'output' / 'RESEARCH_SA07'
WORK = BASE / 'work'

path = OUT / 'sections' / 'F_audit.tex'
content = path.read_text()
snippet = (WORK / 'F3_36_integrated_text.tex').read_text().strip()
token = r'\begin{result}{F.3.36}'
assert snippet.startswith(token)
if token not in content:
    content += '\n\n' + snippet + '\n'
path.write_text(content)

path = OUT / 'code' / 'integrate_records.py'
content = path.read_text()
anchor = "         WORK/'audit_after14_CHECK_EVENTS.tsv',"
addition = "         WORK/'audit_after14b_CHECK_EVENTS.tsv',"
if addition not in content:
    assert anchor in content
    content = content.replace(anchor, anchor + '\n' + addition)
anchor = "             'audit_after14_computation_records.json',"
addition = "             'audit_after14b_source_checks.csv','audit_after14b_validation.json',"
if addition not in content:
    assert anchor in content
    content = content.replace(anchor, anchor + '\n' + addition)
path.write_text(content)

def bib_entries(content):
    for part in re.split(r'(?=@\w+\s*\{)', content):
        match = re.match(r'@\w+\s*\{\s*([^,]+),', part)
        if match:
            yield match.group(1), part.strip()

path = OUT / 'RESEARCH_SA07_references.bib'
content = path.read_text()
current = dict(bib_entries(content))
incoming = dict(bib_entries((WORK / 'audit_postcheckpoint_references.bib').read_text()))
key = 'AuditKleiman1968'
assert key in current and key in incoming
content = content.replace(current[key], incoming[key])
duplicate = 'EllBakkerPilaTsimerman2026Jets'
if duplicate in current:
    content = content.replace(current[duplicate], '')
path.write_text(content)

path = WORK / 'root_after11_references.bib'
content = path.read_text()
if 'RootLieberman1968Attempt' not in content:
    content += r'''

@article{RootLieberman1968Attempt,
  author = {Lieberman, David I.},
  title = {Numerical and homological equivalence of algebraic cycles on Hodge manifolds},
  journal = {American Journal of Mathematics},
  volume = {90}, number = {2}, year = {1968}, pages = {366--374},
  doi = {10.2307/2373533},
  url = {https://www.jstor.org/stable/2373533},
  note = {Not obtained as an original full text. The JSTOR landing and PDF links exposed only HTML through web retrieval; the direct PDF request also returned HTTP200 text/html,3038bytes, rather than a PDF. Search by full title, DOI and Theorem4 found bibliographic or later citations. No statement in F.3.36 depends on an uninspected theorem in this paper: the complete original Kleiman1968 PDF was obtained and its Theorem2A11 p377 and Remark3.10 p380 explicitly supply the used all-dimensional abelian and dimension-at-most-four results.}
}
'''
    path.write_text(content)

path = WORK / 'root_postcheckpoint11_CHECK_EVENTS.tsv'
with path.open() as file:
    rows = list(csv.reader(file, delimiter='\t'))
additions = [
    ('F.3.36', 'targeted proof check',
     'Root read the complete snippet and independently checked the finite-extension trace factor, spreading and flat refined intersection degree, faithful Betti-etale comparison, all-product Hom codimension, idempotent lifting, tensor products and h(A)^dual=h(A)(dim A). The general all-smooth-projective kernel-annihilation gate remains. No finite computation is required for this exact map derivation.'),
    ('F.3.36-source', 'used and rechecked in this run',
     'Root obtained original Kleiman1968 complete28-page PDF from Mainz, SHA256 e96e2465e0fb3a05084cc7472e6edec44a4cff920b199b271caed9251cab825a; read and visually inspected Theorem2A11 p377 and Prop3.8/Cor3.9/Remark3.10 p380. Reopened and visually inspected original Kleiman1994 Prop5-1 p17. Lieberman1968 JSTOR original was not obtained; exact HTML responses and source-search attempts are retained separately. The result uses the opened original Kleiman statement.'),
    ('F.3.31-F.3.33', 'used and rechecked in this run',
     'Root reread the complete original Nakamura1996 printed pp115-117 images: degree-six endpoint ranks both1, Lemma4.5 actual fibre quotient surjectivity and invariance under finite base extension, and exact geometric/arithmetic quotient maps4.7.1-4.7.2. Checked these against the specific nonzero proper-homology class and full-logarithm inner correction in F.3.31/F.3.33. This retains the already credited review06 conclusion and is not new movement.'),
]
for claim, kind, detail in additions:
    row = [claim, '2026-11-19', 'OpenAI GPT-6 Astra /root', kind, detail]
    if row not in rows:
        rows.append(row)
with path.open('w', newline='') as file:
    csv.writer(file, delimiter='\t', lineterminator='\n').writerows(rows)

path = OUT / 'RESEARCH_SA07_report.md'
content = path.read_text()
heading = '## Characteristic-zero cycle scope added before checkpoint12'
if heading not in content:
    content += '\n\n' + heading + '\n\n'
    content += ('F.3.36 records the opened original theorem for all abelian varieties in '
                'characteristic zero, with no dimension bound, and for every smooth '
                'projective variety of dimension at most four. The field-extension '
                'argument proves the assertion for the actual rational cycles over any '
                'fixed k contained in C. The identity on correspondences is then a tensor '
                'equivalence on the entire category generated by abelian varieties and '
                'Tate twists, including every product and every numerical projector. '
                'This full characteristic-zero statement is supplied by Kleiman1968 '
                'Theorem2A11 and Remark3.10, and does not require the 2026 fourfold preprint. '
                'F.3.35 retains its arbitrary-characteristic fourfold scope.\n\n'
                'The earlier treatment did not state this full known characteristic-zero '
                'range explicitly. This addition repairs that omission; it supplies no '
                'cycle-surjectivity theorem for general smooth projective varieties and '
                'no fixed-frame Mumford-Tate equality. The two corresponding historical '
                'OPEN rows retain their statuses and now cite both results. Root and '
                'the triangle agent checked the original pp377 and379-380. The separate '
                'Lieberman article was not obtained from JSTOR; its original theorem is '
                'not treated as inspected.\n')
    path.write_text(content)
print(json.dumps({'actual_utc': datetime.now(timezone.utc).isoformat(),
                  'integrated': 'F.3.36', 'review_performed': False,
                  'checkpoint_created': False}))
