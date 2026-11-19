"""Refresh the fourth-checkpoint report from proofs and explicit PDF approval."""
from pathlib import Path
import csv, hashlib, json

root = Path(__file__).resolve().parents[1]
path = root / 'RESEARCH_SA08_report.md'
text = path.read_text()
lines = text.splitlines()
for i, line in enumerate(lines):
    if line.startswith('| C.3 |'):
        lines[i] = ('| C.3 | Not fully settled; finite-prime case proved | '
                    'C07 refutes strict equalization; C08–C10 and C16–C17 prove common sources and terminal localization whenever only finitely many rational primes are noninvertible. C11–C15 and D022–D023 exclude the specified globalization and free replacement routes. Rings with infinitely many noninvertible primes remain, beginning with Z. |')
    elif line.startswith('| B.2 |'):
        lines[i] = '| B.2 | Lead refuted; exact action proved | B-05–B-07: the complete action is coefficient substitution, with all semilinearity retained; the determinant alone does not determine it |'
    elif line.startswith('| B.3 |'):
        lines[i] = '| B.3 | Proved in the stated strict shadow category | B-08–B-10: the specified automorphisms induce the identity and no positive Steenrod square; the proposed sphere test is refuted |'
    elif line.startswith('| B.4 |'):
        lines[i] = '| B.4 | Proved, with manuscript decomposition corrected | B-12–B-13: the exact rescaling monoid, its units, torsion intersection and corrected split automorphism extension |'
    elif line.startswith('| B.5 |'):
        lines[i] = '| B.5 | Lead refuted; coefficient scope corrected | B-11: unnormalized semilinear maps are not ordinary cohomology operations; the normalized identity is shared by both operation algebras |'
    elif line.startswith('| L4 |'):
        lines[i] = '| L4 | Refuted; corrected action proved | B-06–B-07: nonlinear coefficient substitutions can have determinant one and act nontrivially |'
text = '\n'.join(lines) + '\n'

source_marker = '## Computation record'
source_addition = ("Further source checks for the integral replacement question include Dokas–Frankland–Ikonicoff's primary arXiv source and Caradot–Lin's primary source. Their operadic and cochain-degree hypotheses are recorded explicitly; no positive-cochain lifting theorem is imported from the latter's nonpositive-cochain construction. The finite-prime gluing proof is written out in C16–C17 and was independently re-derived by two runs.\n\n")
if source_addition not in text:
    text = text.replace(source_marker, source_addition + source_marker)

computation_marker = 'Source download, source inspection, OCR, registry consolidation, and packaging scripts are also retained.'
start_marker = 'Additional mathematical computations completed before checkpoint 04:'
extra = '''Additional mathematical computations completed before checkpoint 04:

- D_filtered_lattice_gate.py: exhaustive enumeration of all 3-local filtered lattices through weight five for the first tail and weight six for the second; three lattices of each type, all nine pairings, 2,005 exact membership checks, and zero compatible pairings; 0.067539 seconds. The enumeration allows every lower-coefficient choice and does not assume evaluation ideals.
- B_check_prime_pd_ideal.py: 79 cutoff/prime pairs, 1,520 binomial-product checks and 35,431 divided-power partition checks, with primes through 43; 0.140874 seconds. This checks the finite arithmetic cases of the symbolic all-prime C15 obstruction.
- D_tail_differential_image.py: 264 actual face-matrix calculations over the indicated finite fields, processing 92,938 generators, for cutoffs two through four and weights through 24; 0.308046 seconds. The degree-one horizontal homology vanishes in every tested weight at least twice the cutoff. These tests concern the nonfree differential image, and do not establish admissibility in all rows or settle C.3.
- D_tail_differential_H2.py: 45 exact second-horizontal-homology calculations for the form-one image, over F2, F3 and F5, cutoffs two and three, and weights through nine; 0.950811 seconds. All tested groups vanish.
- D_tail_vertical_multidegree.py: 194 exact integral two-variable image-lattice calculations with zero T-multidegree; 0.023249 seconds. No tested positive vertical cohomology survives.
- D_tail_vertical_threevars.py: 108 exact integral three-variable multidegree complexes; 3.032357 seconds. These also have no positive vertical cohomology in the tested scope. D-027 proves the stated first-row theorem and low vertical degrees symbolically; the higher-row computations are not extrapolated.
- D_tail_integral_horizontal.py: eleven exact normalized integral image complexes; 0.797149 seconds. The small cases include third horizontal homotopy Z/2 at cutoff two, weight four, and Z/3 at cutoff three, weight six. These finite-weight classes do not refute eventual acyclicity.
- D_tail_H3_certificate.py: the complete cutoff-two, weight-four integer certificate, including all 495 maximal minors of the fourth differential, their gcd two, a unit three-minor and a nonzero rank-eight minor of the third differential; 0.104394 seconds. The full matrices prove the Z/2 class without relying on field reduction.
- D_tail_integral_modp.py: 32 complete normalized complexes obtained from the actual integral image lattices and then reduced modulo the tested primes; 3.847327 seconds. This is deliberately distinguished from forming the image after reduction. The higher classes occur in the two indicated small cases; the subsequent tested weights vanish.
- B_pd_square_normalization.py: four exact normalized square-functor cases, K(Z,r) for r=1,2,3,4, with integral matrices and vertical comparison checks; 32.646618 seconds. They test the quadratic stage of the nonlinear repair.
- B_pd_square_next_obstruction.py: one exact tensor/dual Smith calculation, with normalized ranks 1,6,15,18,9 in degrees four through eight; 0.031828 seconds. The possible next relation-obstruction group is (Z/2)². The computation does not assert that a nonzero obstruction class actually occurs.

'''
if start_marker in text:
    begin = text.index(start_marker)
    end = text.index(computation_marker, begin)
    text = text[:begin] + extra + text[end:]
else:
    text = text.replace(computation_marker, extra + computation_marker)

table_begin = text.index('| Input file and line |')
table_end = text.index('## Typesetting status', table_begin)
text = text[:table_begin] + (root/'notes/CORRECTIONS_table.md').read_text() + '\n' + text[table_end:]

qa = json.loads((root/'logs/PDF_QA_APPROVED.json').read_text())
if 'Passed' not in qa.get('visual_review', ''):
    raise RuntimeError('An explicit visual approval is required.')
pdf = root/'RESEARCH_SA08_paper.pdf'
if hashlib.sha256(pdf.read_bytes()).hexdigest() != qa['pdf_sha256']:
    raise RuntimeError('The PDF does not match its explicit approval.')
for rel, expected in qa.get('source_sha256', {}).items():
    if hashlib.sha256((root/rel).read_bytes()).hexdigest() != expected:
        raise RuntimeError('A source changed after PDF approval: ' + rel)
qa_begin = text.index('## Typesetting status')
qa_end = text.index('## Proved obstructions, approaches and remaining gates', qa_begin)
qa_text = f'''## Typesetting status

The first complete warning baseline had {qa['overfull_before']} overfull boxes, all above 2 pt, with maximum {qa['maximum_before_pt']} pt. Adding D-027 later produced one further 16.1386 pt overflow in build23; its paragraph was corrected and its location added to the rendered inspection set. Visual inspection also found a proof-ending symbol stranded at the top of a page, which was moved into its closing display. The approved current LuaLaTeX build has {qa['overfull_after']} overfull boxes and no undefined references or citations. It has {qa['pages']} pages. Every previously corrected overflow location and a spread sample, together with the newly added proof pages, were rendered: {qa['rendered_page_count']} distinct pages were explicitly inspected, with no clipped text, overlap, missing glyphs or margin intrusion observed. The exact build, PDF hash, approved-page list and included-source hashes are recorded in logs/PDF_QA_APPROVED.json. Packaging requires those hashes to agree with the current PDF and sources. Failed builds and their corrections remain in the logs.

'''
text = text[:qa_begin] + qa_text + text[qa_end:]

begin = text.index('C.3: special universally flasque theories')
end = text.index('\n\nL7:', begin)
c_text = '''C.3: special universally flasque theories have contractible nerve; strict common-source equalization is false over every nonzero base. C16–C17 now prove common sources and terminal localization for every coefficient ring with only finitely many noninvertible rational primes, including the flat-term category and the optional q≤w support condition. Simplicial cotensors preserve both gradings; a pure arithmetic exact sequence, path pullbacks and filled marked squares provide the complete descent and loop-contraction proof. The bounds remain uniform because the prime set is finite.

The smallest remaining case is k=Z. Ordinary tensor products fail already for two standard theories, with prime-power Tor in unbounded weights. Independently marked free PD disks over Z fail except for the ordinary weight-one disk. C12 excludes arithmetic gluing that retains projections to local elementary sources with unbounded first flasque weights. C13 rules out a standard-tail initial family. C14 excludes degreewise-surjective replacements made from free linear disks, and C15 gives a nonzero prime-weight first differential-module homotopy class for free resolutions of a coefficient tail. These are obstructions to particular constructions, not counterexamples to localization uniqueness. The nonfree differential image of a standard tail removes the first low-row obstruction in the proved and computed scope; its higher rows and its usefulness for arbitrary targets are still being investigated. Further approaches examine common targets and nonlinear positive-cochain repairs, where coherent simplicial lifting is a specific outstanding step. The paper's separate unchecked appendix states the two remaining global assertions precisely.'''
text = text[:begin] + c_text + text[end:]
path.write_text(text)
print(json.dumps({
    'report': path.name,
    'statement_rows': len(list(csv.DictReader((root/'RESEARCH_SA08_results.csv').open()))),
    'correction_rows': len(list(csv.DictReader((root/'RESEARCH_SA08_corrections.tsv').open(), delimiter='\t'))),
    'approved_pdf_pages': qa['pages'],
    'visually_inspected_pages': qa['rendered_page_count'],
}, indent=2))
