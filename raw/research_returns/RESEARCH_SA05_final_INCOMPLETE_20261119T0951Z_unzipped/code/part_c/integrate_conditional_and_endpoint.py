"""Integrate two audited Part C refinements without overwriting other work."""
from pathlib import Path
import json
import re
import time

start = time.perf_counter()
root = Path(__file__).resolve().parents[2]
main = root / 'sections/part_c.tex'
text = main.read_text()
chow = (root / 'part_d/c6_chow_conditional.tex').read_text()
chow = chow.replace('\\label{c:chow-unramified-purity-reduction}',
                    '\\label{c:chow-unramified-purity-reduction}\n'
                    '\\status{Proved conditional implication}')
chow = chow.replace('\\label{c:chow-purity-scope}',
                    '\\label{c:chow-purity-scope}\n'
                    '\\status{Proved scope clarification; the general claim remains unresolved}')
if '\\label{c:chow-unramified-purity-reduction}' not in text:
    marker = '\\begin{remark}[The remaining general-motive claim]'
    assert marker in text
    text = text.replace(marker, chow + '\n' + marker)
endpoint = (root / 'part_c/c4_abelian_endpoint.tex').read_text()
if '\\label{c:abelian-invariant-weights}' not in text:
    marker = 'The preceding results prove the requested upper-weight inequality'
    assert marker in text
    text = text.replace(marker, endpoint + '\n' + marker)
text = text.replace(
    'They also settle the top coefficient endpoint. Proposition~\\ref{c:lic-endpoint}',
    'They also settle the top coefficient endpoint and, for abelian-type '
    'coefficients over a trait, the lower endpoint. Proposition~\\ref{c:lic-endpoint}')
main.write_text(text)

bibpath = root / 'part_c/references.bib'
bib = bibpath.read_text()
extra = (root / 'part_d/c6_general_sources.bib').read_text()
for key in ['c_saito2003weights', 'c_serre1970local']:
    if '{' + key + ',' not in bib:
        match = re.search(r'@\w+\{' + re.escape(key) + r',[\s\S]*?\n\}', extra)
        assert match, key
        bib += '\n' + match.group() + '\n'
bib = bib.replace(
    'url={https://grothendiecksga.com/read/sga7/fr/9-2.html},\n'
    ' note={Opened: text edition of Expos\\\'e IX, Sections 2 and 5; '
    'Proposition 2.2.5, Corollary 2.2.9, and Theorem 5.2. Original scan '
    'verification remains to be recorded if obtained.}',
    'url={https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-1.pdf},\n'
    ' note={Opened original scan and verified Expos\\\'e IX, formula (2.1.8), '
    'p.~328; Proposition 2.2.5, pp.~332--333; Corollary 2.2.9, pp.~335--336; '
    'Theorem 2.4, p.~338; Proposition 3.5, p.~350; Corollary 3.5.2 and '
    'Theorem 3.6, p.~351. The text edition of Section 5 was also opened.}')
bibpath.write_text(bib)
output = {'integrated_labels': ['c:chow-unramified-purity-reduction',
          'c:chow-purity-scope', 'c:abelian-invariant-weights'],
          'section_lines': len(text.splitlines()),
          'runtime_seconds': time.perf_counter()-start}
(root / 'code/part_c/integrate_conditional_and_endpoint_output.json').write_text(
    json.dumps(output, indent=2) + '\n')
print(json.dumps(output))
