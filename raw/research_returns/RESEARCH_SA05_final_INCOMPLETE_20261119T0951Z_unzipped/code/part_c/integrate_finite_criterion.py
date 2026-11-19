"""Integrate independently audited finite criteria and record exact source numbering."""
from pathlib import Path
import csv
import json
import time

start = time.perf_counter()
root = Path(__file__).resolve().parents[2]
section = root / 'sections/part_c.tex'
text = section.read_text()
for filename, label, marker in [
    ('c1_finite_even_criterion.tex', 'c:finite-even-criterion',
     '\\begin{theorem}[The narrow K3 ring already detects finite-dimensionality]'),
    ('c1_k3_transcendental_gate.tex', 'c:k3-transcendental-gate',
     '\\begin{corollary}[The unconditional K3 range]'),
]:
    if '\\label{' + label + '}' not in text:
        assert marker in text
        text = text.replace(marker, (root/'part_c'/filename).read_text()+'\n'+marker)
text = text.replace('Proposition 2.5 and \\S2.6, arXiv version',
                    'Proposition 3.5 and \\S3.6, pp.~508--510')
text = text.replace('\\citet[\\S1.4]{c_yin2015}',
                    '\\citet[\\S2.4, p.~506]{c_yin2015}')
text = text.replace('unnumbered main Theorem and \\S\\S1.5, 2.1--2.6',
                    'unnumbered main Theorem, p.~503, and \\S\\S2.5, 3.1--3.6')
section.write_text(text)

bibpath = root/'part_c/references.bib'
bib = bibpath.read_text()
bib = bib.replace(
    'url={https://arxiv.org/pdf/1404.0171},\n'
    ' note={Opened: full arXiv PDF. Locators in the paper use the arXiv numbering: '
    'unnumbered main Theorem; Sections 1.2--1.5; Proposition 2.5; Section 2.6.}',
    'doi={10.4171/CMH/362}, url={https://ems.press/content/serial-article-files/43396},\n'
    ' note={Opened: full published PDF and earlier arXiv version. Locators now use '
    'published numbering: unnumbered main Theorem, p.~503; Sections 2.2--2.5; '
    'Proposition 3.5 and Section 3.6, pp.~508--510.}')
if '{c_procesi2021tensor,' not in bib:
    bib += r'''
@misc{c_procesi2021tensor,
 author={Procesi, Claudio},
 title={Tensor fundamental theorems of invariant theory},
 year={2021}, eprint={2011.10820}, archivePrefix={arXiv},
 url={https://arxiv.org/pdf/2011.10820},
 note={Opened version 3, February 4, 2021; Theorems 1.2--1.5, author pp.~4--5. The general tensor-variable use in Part C is proved by polarization and restitution.}
}
'''
bibpath.write_text(bib)

path = root/'part_c/results.csv'
with path.open(newline='') as f:
    rows = list(csv.DictReader(f))
fields = list(rows[0])
entries = [
['c:abelian-invariant-weights',
 'Frobenius on inertia invariants of pure weight-j abelian-type local realizations has weights at most j',
 'Proved for finite residue fields and ell different from residue characteristic',
 'sections/part_c.tex, Proposition label c:abelian-invariant-weights',
 'Original SGA7 I IX2.1.8,2.2.5,2.4,3.5,3.5.2,3.6; tensor-string proof',
 '12:118-120; C.4',
 'Settles the trait lower endpoint for abelian-type coefficients without the 2026 rationality theorem.'],
['c:chow-unramified-purity-reduction',
 'A single-weight unramified realization of a homogeneous Chow summand implies unramifiedness for all ell',
 'Proved conditional implication',
 'sections/part_c.tex, Proposition label c:chow-unramified-purity-reduction',
 'Saito2003 Theorems0.1,3.1; finite inertia; Frobenius-monodromy relation',
 '12:140; C.6',
 'Ambient weight-monodromy at the one prime suffices; algebraic projector required.'],
['c:chow-purity-scope',
 'Exact relation of the Chow reduction to Serre C7 and the projector condition',
 'Proved scope clarification; general-motive claim remains unresolved',
 'sections/part_c.tex, Remark label c:chow-purity-scope',
 'Serre1970 section2.3 C7; Saito2003 algebraic-correspondence hypothesis',
 '12:140; C.6',
 'No converse to a named conjecture claimed.'],
['c:finite-even-criterion',
 'Finite necessary-and-sufficient Chow cycle criterion for all powers of any complex variety with pure-even cohomology',
 'Proved in the pure-even case',
 'sections/part_c.tex, Theorem label c:finite-even-criterion',
 'Orbit ideal elimination; exact GL_d times Gm invariants; Procesi2021 Theorems1.2-1.5; graph normalization',
 '11:51-57; C.1(c)',
 'Finite covariant relations plus exterior vanishing and two normalization identities; does not decide their rational equivalence algorithmically.'],
['c:finite-criterion-scope',
 'Pure-even finite criterion does not silently settle arbitrary mixed-parity pairs',
 'Proved scope clarification; general classification remains unresolved',
 'sections/part_c.tex, Remark label c:finite-criterion-scope',
 'Nonexact invariants for GL supergroup; parity splitting distinction',
 '11:51-57; C.1(c)',
 'D supplies an explicit odd-derivation certificate for the marked cohomology of E times P1.'],
['c:k3-transcendental-gate',
 'Narrow K3 all-relations assertion is equivalent to exterior power23-rho of the transcendental Chow motive vanishing',
 'Proved smaller equivalent test; general vanishing unresolved',
 'sections/part_c.tex, Corollary label c:k3-transcendental-gate',
 'Explicit NS intersection projector; exterior direct-sum formula; Yin published2.5 equation7',
 '11:51-57; Lead C1; C.1(c)',
 'Picard rank1 gives44 factors with divisor projectors outside the narrow ring; narrow first determinant remains on46 factors.'],
]
for entry in entries:
    if not any(r['id']==entry[0] for r in rows): rows.append(dict(zip(fields,entry)))
for r in rows:
    if r['id']=='c:pair-ranks':
        r['depends_on']='Orthogonal/symplectic invariant theory; Yin published3.5; Tavakol6.1-6.4'
    if r['id']=='c:k3-gate':
        r['notes']='First missing narrow determinant is on46 factors; equivalent transcendental test is on2(23-rho) factors, using divisor projectors; general vanishing not proved.'
    if r['id']=='c:lic-endpoint':
        r['notes']='General mixed-characteristic local-invariant-cycle gate remains; abelian-type trait coefficients now satisfy the upper weight-j endpoint unconditionally.'
with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)

events=root/'part_c/CHECK_EVENTS.tsv'
previous=events.read_text()
records=[
['c:abelian-invariant-weights','2026-11-19','GPT-6 Astra (OpenAI), /root/part_c','targeted proof check','Original SGA7 scan pages328,332-333,335-336,338,350-351 opened and theorem statements verified; tensor monodromy filtration and finite-extension descent supplied.'],
['c:abelian-invariant-weights','2026-11-19','GPT-6 Astra (OpenAI), /root/part_d','independent re-proof','Passed weights -2,-1,0 on Tate filtration, imN=kerN orthogonal, SL2-string tensor stability, and finite-residue Frobenius descent.'],
['c:chow-unramified-purity-reduction','2026-11-19','GPT-6 Astra (OpenAI), /root/part_c','independent re-proof','Opened Saito0.1 includes every Weil element; common Frobenius polynomial excludes N by the q^-1 eigenvalue shift; finite inertia traces then force identity.'],
['c:finite-even-criterion','2026-11-19','GPT-6 Astra (OpenAI), /root/part_c','targeted proof check','Constructed finite orbit-ideal covariants; normalized Chow graph reduction proves equivalence with the requested narrow rings, not merely a larger diagram category.'],
['c:finite-even-criterion','2026-11-19','GPT-6 Astra (OpenAI), /root','independent re-proof','Passed exact ambient reductive invariants, tensor-ideal lifting, normalization of all diagrams; requested explicit fixed Tate identities and terminating intertwiner search, now included.'],
['c:finite-even-criterion','2026-11-19','GPT-6 Astra (OpenAI), /root/part_d','independent re-proof','Passed both implications and finite covariant construction; no stabilizer reductivity needed. Mixed-parity extension kept unresolved.'],
['c:k3-transcendental-gate','2026-11-19','GPT-6 Astra (OpenAI), /root/part_c','targeted proof check','Explicit NS projector composition and exterior direct-sum decomposition prove equivalent lower-rank gate; generic Picard rank1 test uses44 factors outside the narrow ring.'],
['c:k3-gate','2026-11-19','GPT-6 Astra (OpenAI), /root/part_c','source correction','Opened published Yin PDF; replaced arXiv1.4,1.5,2.5,2.6 numbering by published2.4,2.5,3.5,3.6 and recorded both versions.'],
]
with events.open('a',newline='') as f:
    w=csv.writer(f,delimiter='\t')
    for row in records:
        if row[-1] not in previous:w.writerow(row)

sources=root/'part_c/sources.tsv'
src=sources.read_text()
src=src.replace('yin2015\topened\thttps://arxiv.org/pdf/1404.0171\tmain unnumbered Theorem;§§1.2–1.5;relation(7)',
 'yin2015\topened full published and arXiv PDFs\thttps://ems.press/content/serial-article-files/43396\tmain unnumbered Theorem p503;Sections2.2-2.5;Proposition3.5;Section3.6;relation7')
for line in [
 'sga7original\topened original scanned pages; rendered and read\thttps://library.slmath.org/nonmsri/sga/sga/pdf/sga7-1.pdf\tIX2.1.8 p328;2.2.5 pp332-333;2.2.9 pp335-336;2.4 p338;3.5 p350;3.5.2 and3.6 p351\n',
 'procesi2021tensor\topened full primary v3 PDF\thttps://arxiv.org/pdf/2011.10820\tTheorems1.2-1.5 authorpp4-5; general tensor-variable application independently proved by polarization\n',
 'saito2003weights\topened full author PDF; independently reread exact scope\thttps://www.ms.u-tokyo.ac.jp/~t-saito/pp/wmr2r.pdf\tTheorems0.1,3.1; any Weil element including inertia\n',
 'serre1970local\topened author original PDF; exact formulas visually checked by Part D\thttps://www.college-de-france.fr/media/jean-pierre-serre/UPL7750118224972622059_Serre_facteurs_locaux.pdf\tSection2.3 printed19-07 C3,C6,C7;19-08 Remark2\n',
]:
    if line.split('\t')[0]+'\t' not in src:src+=line
sources.write_text(src)

notes=root/'part_c/part_c_notes.md'
prior=notes.read_text()
header='## Finite pure-even criterion and further endpoint progress (04:45 UTC)\n'
if header not in prior:
    addition='''
The all-powers classification now has a finite necessary-and-sufficient criterion for every complex variety with pure-even cohomology, constructed from its marked Frobenius algebra by a polynomial orbit-ideal computation. Root and Part D independently re-proved it. The ambient group is GL_d times Gm; its reductivity is used, while no reductivity of the Frobenius stabilizer is assumed. The mixed-parity extension remains a separate genuine gate; Part D saved an explicit odd-superderivation certificate for H*(E times P1).

The K3 test can be reduced from the narrow determinant on46 factors to the exterior power23-rho of t2, a correspondence on2(23-rho) factors. At Picard rank1 this gives44 factors, using divisor projectors outside the narrow ring. This is a smaller equivalent gate, not its vanishing proof. The generic and every-K3 claims remain unresolved.

C4's lower trait endpoint is proved for all pure abelian-type coefficients directly from the original SGA7 semistable filtration and tensor-string argument; the general mixed-characteristic local invariant cycle gate remains. C6 now includes a proved conditional implication for homogeneous algebraic Chow projectors from single-weight purity at one unramified prime, using Saito's common traces. No exact general named-conjecture equivalence is asserted.

The Yin locators were migrated to the published version after opening it: main theorem p503, finite-dimensionality2.4, transcendental reduction2.5, matching proposition3.5 and proof3.6. Original SGA7 pages are also now verified, superseding the earlier text-edition-only record.
'''
    notes.write_text(prior.replace('# Part C research ledger\n','# Part C research ledger\n\n'+header+addition))
out={'section_lines':len(text.splitlines()),'result_rows':len(rows),
     'events':sum(1 for _ in events.open())-1,
     'runtime_seconds':time.perf_counter()-start}
(root/'code/part_c/integrate_finite_criterion_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
