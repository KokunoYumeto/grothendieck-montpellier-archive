from pathlib import Path
import csv
from datetime import datetime, timezone

root = Path('/workspace/scratch/6b22741c5cd2/RESEARCH_SA20')
own = root / 'agents/singularities_duality'
now = datetime.now(timezone.utc).isoformat(timespec='seconds')
draft = (own / 'logs/A132_TOP_S3_counterexample_draft.tex').read_text()
proof = draft[draft.index(r'\begin{saresult}') :]
paper = root / 'parts/parametric_concordance.tex'
text = paper.read_text()
assert r'\begin{saresult}{A.132}' not in text
old = '''The remaining A.1(b) gates are higher PL-to-semialgebraic and
PL-to-arbitrary-definable comparison, the resulting higher model in
an arbitrary o-minimal expansion, and the low-dimensional real
PL--TOP comparison. An explicit presentation of both source and
target does not decide whether their comparison map is a weak
equivalence.'''
new = '''A.132 refutes the unrestricted real PL--TOP weak-equivalence
claim: for $S^3$ the TOP concordance space has $\pi_2=\mathbb Z/2$,
whereas the jointly PL space has $\pi_2=0$. The remaining A.1(b)
gates are higher PL-to-semialgebraic and PL-to-arbitrary-definable
comparison, the resulting higher model in an arbitrary o-minimal
expansion, and the precise low-dimensional real TOP comparison
beyond the computed three-sphere case. The three-sphere discrepancy
does not refute PL-to-semialgebraic comparison. An explicit
presentation of both source and target does not decide whether
their comparison map is a weak equivalence.'''
assert old in text
paper.write_text(text.replace(old, new) + '\n\n' + proof)

bib = own / 'references.bib'
text = bib.read_text()
assert '@article{Hatcher1983,' not in text
text += '\n' + (own / 'logs/A132_references_pending.bib').read_text()
text = text.replace(
    'The definition at p.64 requires level-preserving local normal charts.}',
    'The definition at p.64 requires level-preserving local normal charts. '
    'Theorem5.1 p.70 and the canonical extension construction in the proof of Corollary1.2 p.79 '
    'were also opened and independently read for A132: the deformation is continuous in the embedding '
    'and fixes the inclusion, allowing a single compact-parameter time mesh.}')
text = text.replace(
    'Published online3March2026; independently checked by root and singularities-duality, 2026-11-19.}',
    'Section1.1, Theorem1.3 and the preceding and following paragraphs, also opened: '
    'TOP(4) is the global origin-fixing homeomorphism group and its quotient by O(4) is the '
    'classifying-space homotopy fibre; the corrected theorem completes the 5-connected '
    'Freedman--Quinn stabilization. Published online3March2026; independently checked by '
    'root, singularities-duality and higher-comparison, 2026-11-19.}')
text = text.replace(
    'AnnexC printedp318 stable PL/O vanishing through degree6 also visually checked by both agents for A128.',
    'AnnexC printedp318 stable PL/O vanishing through degree6 also visually checked by both agents for A128. '
    'EssayV Theorem5.5(II), printedp251, stable TOP/O homotopy groups through degree6 visually checked '
    'by author and root for A132. EssayI Theorem5.1 p31 and EssayIV Proposition2.1 p164 visually '
    'read: the dimension-five boundary clauses require control of the entire boundary, '
    'so they do not directly treat a cylinder with a free four-dimensional top.')
bib.write_text(text)

results = own / 'results.csv'
with results.open(newline='') as stream:
    ids = {r['id'] for r in csv.DictReader(stream)}
assert 'A.132' not in ids
with results.open('a', newline='') as stream:
    csv.writer(stream).writerow([
        'A.132',
        'The unrestricted real PL-TOP concordance weak equivalence is false: S3 has pi2 zero in jointlyPL and Z/2 in TOP; exact TOP fibre model',
        'Refuted', 'parts/parametric_concordance.tex A.132',
        'A.128; Edwards-Kirby Th5.1 and Cor1.2 proof; Hatcher1983 Appendix16; FQ8.7A; GGHKP2026 Th1.3; KS V5.5',
        '119/148; 121/002-003; A.1(b); Lead L1',
        'Uniform relative germ lifting with one extension operator and one compact-diagonal time mesh; identity-component restriction avoids globalization; free outer face explicit. Author53 exact finite-base checks PASS; source-derived TOP family is not claimed computer-tested. PL-SA and other low-dimensional TOP data remain separate.'
    ])

events = [
    ('singularities_duality', 'full proof and original source audit',
     'PASS: exact horn equality and common radii, canonical E-K extension, compact-diagonal mesh, kernel colimit, identity-component global-germ comparison and radial orthogonal compatibility. Hatcher605-606, FQ128, KS251 viewed; modern GGHKP conventions opened.'),
    ('root', 'independent full proof and source audit received',
     'FULL PASS: every line read; E-K70/79, Hatcher605-606, FQ128, GGHKP1.1 and KS251 independently inspected. Sing typing added as requested. Parent authorized promotion after sibling PASS.'),
    ('higher_comparison', 'independent complete proof audit received',
     'FULL PASS: common parameter radii and mesh, exact horn conditions, free-top fibre, identity-component restriction, all map compatibilities and both homotopy calculations. See sibling A132_independent_audit.md.'),
    ('singularities_duality', 'exact finite base computation',
     'PASS53 checks0.036127275991020724s: boundary4-simplex f-vector, every link, integral Smith forms and primitive fundamental cycle. No TOP family or stabilization theorem claimed numerically tested.'),
]
with (own / 'checks.tsv').open('a') as stream:
    for who, kind, outcome in events:
        stream.write('\t'.join(['A.132', now, who, kind, outcome]) + '\n')
    stream.write('\t'.join([
        'A.1(b)', now, 'singularities_duality', 'scope correction after A132',
        'Unrestricted real PL-TOP weak equivalence now refuted on S3 in pi2. Higher PL-SA/arbitrary-definable comparison and precise low-dimensional TOP data beyond S3 remain open; the counterexample is not semialgebraic.'
    ]) + '\n')

with (own / 'report.md').open('a') as stream:
    stream.write(f'''\n## {now} — A.132: unrestricted PL–TOP weak equivalence refuted\n\n''')
    stream.write('''A.132 proves the actual free-top model P_TOP(S3) ≃ Ω(TOP(4)/O(4)), with TOP(4) the global compact-open homeomorphism group fixing the origin. Its π2 is Z/2; the jointly finite PL sphere model has π2=0. Both spaces have trivial π0 and π1 in this example. The unrestricted real PL-to-TOP weak-equivalence assertion is therefore false. This is not a counterexample to PL-to-SA or PL-to-definable comparison, and it does not compute all remaining low-dimensional TOP spaces.\n\n''')
    stream.write('''The relative germ proof supplies an actual continuous small-extension operator from Edwards–Kirby, one common source/image radius, and one compact-diagonal time mesh for all auxiliary parameters. It preserves the horn exactly. The disk kernel is the filtered union of fixed-inner-ball groups, giving the required free outer face. The global kernel contracts on each finite family; restricting to the identity components avoids any unsupported globalization of isolated germs. Hatcher’s original Appendix explicitly states the C0 TOP(S3) comparison. The original FQ stabilization page and the corrected 2026 GGHKP global-group convention were opened, as was KS EssayV5.5p251. Root and higher_comparison independently passed the full proof.\n\n''')
    stream.write('''The finite boundary-of-4-simplex certificate passed53 exact tests in0.036127275991020724s, covering all links, integral chain matrices and a fundamental cycle. This verifies the finite PL base, not the source-derived non-PL topological family. Pending draft and independent audit history remain saved. The separate direct dimension-five product-structure attempt is not promoted: KS I5.1p31 and IV2.1p164 require the entire four-dimensional boundary controlled, which the free top does not satisfy.\n''')

(own / 'logs/A132_promotion_receipt.txt').write_text(
    'A.132 promoted after root and higher_comparison full PASS\n' + now + '\n'
    'Changed: parts/parametric_concordance.tex; own references.bib, results.csv, checks.tsv, report.md\n'
)
print(now)
