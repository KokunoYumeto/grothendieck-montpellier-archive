#!/usr/bin/env python3
"""Integrate the independently audited threefold cofinal-diagram example."""
from pathlib import Path
import csv
import datetime
import json
import re
import time

started = time.perf_counter()
base = Path(__file__).resolve().parents[1]
source = base.parent / 'C' / 'B2_threefold_cofinal_counterexample.tex'
fragment = source.read_text()
fragment = re.sub(r'B\.2\.(7|8|9|10|11)(?!\d)',
                  lambda match: 'B.2.' + str(int(match[1]) + 2), fragment)
fragment += r'''

\begin{remark}[The two assertions in the prompt]
The cohomological assertion in B.2 is true over every ground field.
The asserted equivalent formulation as a constant domination-cofinal
Picard diagram is false by the preceding theorem.  Moreover B.2i shows
that the indicated model category need not be filtered.  A weaker
replacement asks only for one model above which all permitted pullbacks
are isomorphisms, without cofinality in the entire category.  This is
proved in B.2h over perfect fields and in B.2o in dimension at most two;
over imperfect fields in dimension at least three it remains a separate
unresolved strengthening.  We do not infer its failure from this example.
\end{remark}
'''
(base / 'B2_threefold_cofinal_counterexample.tex').write_text(fragment)
path = base / 'paper_B.tex'
paper = path.read_text()
assert 'Statement B.2q ' not in paper
needle = r'\tag{B.2.3}'
assert paper.count(needle) == 2
first = paper.index(needle)
second = paper.index(needle, first + len(needle))
paper = paper[:second] + r'\tag{B.2.J}' + paper[second + len(needle):]
path.write_text(paper + '\n\n' + fragment)

path = base / 'results_B.csv'
with path.open() as stream:
    reader = csv.DictReader(stream)
    fields = reader.fieldnames
    rows = list(reader)
assert len(fields) == 7
for row in rows:
    if row['id'] == 'B.2':
        row['notes'] += ' The literal h1 question is proved; the claimed equivalent constant cofinal Picard diagram is separately refuted in B.2q.'
    if row['id'] == 'B.2-U':
        row['statement'] = 'Additional weak upper-cone replacement: existence of one stable geometrically normal model over an imperfect field in dimension at least3'
        row['depends_on'] = 'B.2h proves every perfect-field case; B.2o proves every dimension-at-most2 case; B.2q refutes the stronger cofinal formulation'
        row['notes'] = 'This is a retained additional strengthening, not the unresolved literal h1/constant-cofinal pair. Only a stable upper cone without cofinality is asked here. Degree kernels are bounded by B.2m; the geometric realization and finite-image quotient bound remain open. B.2p refutes the unrestricted abelian-target graph method.'
    if row['id'] == 'B.2o':
        row['notes'] = row['notes'].replace('cofinal diagram remains separately formulated.', 'the strong cofinal diagram is separately refuted in dimension3 by B.2q.')
rows.append(dict(
    id='B.2q',
    statement='Over arbitrary imperfect fields the Pic^tau diagram of proper geometrically normal models is constant on some domination-cofinal collection',
    status='Refuted with explicit threefold counterexample',
    where_proved='paper_B.tex Statement B.2q',
    depends_on='B.1g; characteristic3 cone triple cover of a product of two nonisogenous elliptic curves; A2 resolution; ACMV2026 Theorem3.2 and Remark3.3; exact certificates',
    manuscript_pages='29/075',
    notes='Every model over either of two allowed partial graphs retains its own geometric reduced elliptic Picard identity component. These elliptic curves are not geometrically isogenous. Refutes the claimed equivalence with bounded h1 under constant-cofinal interpretation; does not refute the separate weak upper-cone replacement.'))
with path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

events = [
    ('/root/part_c', 'refuted, with the refined statement', 'C supplied the complete written threefold proof with explicit36-term generic section, normal partial graphs, regular A2 resolution, Picard comparison and incompatible elliptic upper cones.'),
    ('/root/part_b, actual-file reading', 'targeted proof check', 'B read the complete C fragment and verified geometric S2/R1, normalized image of D via Stein factorization, projective-bundle cohomology, A2 resolution, finite-separable Albanese origins and nonisogeny. C incorporated the requested explicit basis and dual-isogeny refinements.'),
    ('/root, actual-file reading', 'targeted proof check', 'Root read the complete C fragment and checked the main chain, then requested the precise normalized image of D and dual-isogeny details. Both were inserted. Root independently opened ACMV and Conrad for the Albanese duality input. No gap found.'),
    ('/root/part_b', 'computation or formal certificate', 'elliptic_branch_certificate_B.py passed11 exact assertions with SymPy1.14.0 in0.056450278s. Smoothness, tangent substitution and characteristic3 flex schemes were checked. An initial harness incorrectly compared a nonreduced full ideal with its reduction; the retained successful certificate distinguishes them.'),
    ('/root/part_c', 'computation or formal certificate', 'parts/C/code/check_threefold_local_geometry.py passed11 exact assertions in0.040636211s: all A2 blowup charts, their smooth coordinate derivatives, q-to-q+aW^2 change, cube shift, exceptional multiplicity2 and36 section-basis count.'),
]
with (base / 'CHECK_EVENTS_B.tsv').open('a') as stream:
    for who, event, detail in events:
        stream.write('B.2q\t2026-11-20\tGPT-6 Astra (OpenAI), ' + who + '\t' + event + '\t' + detail + '\n')

path = base / 'corrections_B.tsv'
lines = path.read_text().splitlines()
for i, line in enumerate(lines):
    if line.startswith('B-C06\t'):
        fields = line.split('\t')
        fields[-2] = 'Uniform h1 boundedness is proved, but a constant domination-cofinal Picard diagram is refuted by an explicit geometrically normal threefold example over an imperfect field. Thus the asserted equivalence is false in this precise sense. A weaker stable upper cone without cofinality is separately formulated and remains open only in dimension at least3 over imperfect fields.'
        fields[-1] = 'B.2; B.2i; B.2q; B.2-U'
        lines[i] = '\t'.join(fields)
path.write_text('\n'.join(lines) + '\n')

(base / 'unresolved_B.tex').write_text(r'''% Only the additional unchecked strengthening remains here.
\section{Additional unresolved strengthening attached to Part B}
\subsection*{B.2-U: weak upper-cone stabilization over an imperfect field}
The literal cohomological question in B.2 is proved over every ground
field.  The asserted equivalent formulation as a constant
domination-cofinal Picard diagram is refuted by B.2q.  Statement B.2i
also proves that the category of geometrically normal proper models
need not be filtered.  These two counterexamples are distinct:
B.2i is categorical and has trivial torsion Picard groups, whereas
B.2q has two incompatible elliptic Picard branches.

We retain the following weaker replacement as a separate unresolved
strengthening.  Does there exist one geometrically normal proper
model $X_0$ such that every geometrically normal proper domination
$X\to X_0$ induces an isomorphism on $\operatorname{Pic}^{\tau}$?
Its upper cone is not required to be cofinal in the entire model
category.  Statement B.2h proves this over every perfect field;
B.2o proves it over every field in transcendence degree at most two.
Only imperfect ground fields and transcendence degree at least three
remain.  The threefold counterexample B.2q does not refute this weaker
question: its theorem separates the two branches without claiming
that either branch fails to stabilize internally.

The infinitesimal-height issue is resolved over perfect fields by
B.2d--h, not assumed from tangent boundedness.  Over an arbitrary
field, B.2l gives weak stabilization after one finite purely
inseparable extension of the constants.  Its model and birational
marking descend from the perfect closure by finite presentation.
Thus the residual gate concerns descent to the original field and
realization of a maximal allowed Picard image, rather than a finite
field-of-definition issue.

Statements B.2j--m remove the alteration-kernel obstruction.
A fixed smooth alteration over a finite extension $l/k$ yields a
comparison into
$\operatorname{Res}_{l/k}(\operatorname{Pic}^{\tau}_{Y/l})$.
The entire fppf Picard-sheaf kernel is killed by the generic degree
$d$, including on nonreduced test schemes.  The fixed-Jacobian
embedding bounds its rank by $d^{2g}$.  Normal graph modifications
of the regular alteration have the same Picard group by B.1g,
even when those graphs are not geometrically normal.  What remains
is the image: we have not proved a uniform bound on finite quotients
of these images over the image of one permitted model.

A fixed abelian ambient group and a fixed tangent dimension do not
establish that image bound formally.  For an elliptic curve $E$ in
characteristic $p$, the increasing kernels of $F^r_{E/k}$ have
constant tangent dimension one and strictly increasing ranks $p^r$
\cite[Proposition 2.29]{MilneAG2022B}.  This is an abstract
group-scheme illustration; it has not been realized by the allowed
models as a counterexample to the weak replacement.

An attempted realization by an unrestricted normalized graph to an
abelian variety is refuted by B.2p, even for a surface and an
elliptic target.  The graph acquires a geometrically nonnormal
divisorial valuation that no permitted refinement can retain.
A controlled realization contracting the offending valuations, or
a different image argument, is required.  The purely inseparable
Albanese comparison and Weil-restriction results in
\cite[Theorem 6.1 and Proposition 6.2, pp.~18--23 of the revised
manuscript]{Schroer2024} do not assert geometric normality of a graph
and do not supply this missing step.

Statement L6c now proves $R^1f_*\mathcal O=0$ for every proper
birational normal-to-regular morphism in characteristic $p$, in all
dimensions.  This further fixes the coherent cohomology of normal
graphs over a regular alteration.  It does not supply descent at
the singular target, nor vanishing of the higher direct images
that would reproduce the surface maximal-length argument.
''')

with (base / 'notes.md').open('a') as stream:
    stream.write('\n## 2026-11-20 03:43: literal B.2 pair decided; additional weak gate retained\n\nB.2q gives a fully checked threefold counterexample to constant domination-cofinal Picard diagrams over an imperfect field. The generic triple cover of the cone over E1 times E2 has two geometrically normal partial graphs. All allowed models dominating the first retain E1 as geometric reduced Picard identity, and those dominating the second retain E2; the curves are not geometrically isogenous. The complete proof supplied by C was read by B and root; exact elliptic and A2 certificates each passed11 assertions. The literal h1 question is true, whereas the asserted equivalent cofinal constancy is false. A stable upper cone without cofinality is a separate weaker replacement that we continue to investigate for imperfect fields in dimension at least3. No failure of that weak replacement is inferred from the two branches. Equation tags in the copied fragment were made unique; the previously duplicate fixed-Jacobian tag was corrected to B.2.J.\n')
with (base / 'sources' / 'search_log.md').open('a') as stream:
    stream.write('\n## 2026-11-20 03:43 — primary sources for the threefold cofinal counterexample\n\n- Opened Stacks Tags045M (tensor products of fields are Cohen–Macaulay in the stated Noetherian scope),0339 (flat ascent of Serre conditions),031S (normal iff R1 and S2). These justify geometric S2 and the partial-graph normality argument; they do not assert that every normal scheme is geometrically normal.\n- Opened Milne, Elliptic Curves, second edition2021, official EC2.pdf, ChapterI§3 Theorem3.1 printed25–27: chord-and-tangent group law. The characteristic3 flex calculation is proved and program-checked here, not inferred from an unverified Hasse invariant.\n- Reopened Achter–Casalaina-Martin–Vial author manuscript alb.pdf, Theorem3.2 printed12 and Remark3.3 printed13: proper geometrically connected geometrically reduced schemes have Albanese data compatible with field extension; the Albanese is dual to the maximal abelian subvariety of Pic. Bibliography key C_ACMV2026 is supplied in the shared C bibliography. This applies to the normal geometrically integral comparison graph even though it need not be geometrically normal.\n- Exploratory only: opened Cossart–Piltant2019 author draft Theorem1.1 printed3–4 (regular resolution of quasi-excellent threefolds); Laurent–Schroer2024 primary Springer article on maximal abelian subvarieties and Albanese; Nagamachi–Takamatsu arXiv2110.03917 on imperfect-field Picard groups. None is cited as proving the residual weak image gate.\n')
record = dict(operation='integrate_cofinal_counterexample_B',
              utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              statements=['B.2q'],
              checked='literal h1 true; constant cofinal diagram false',
              unresolved='additional weak upper-cone replacement over imperfect fields in dimension at least3',
              elapsed_seconds=time.perf_counter()-started)
(base / 'code' / 'output' / 'integrate_cofinal_counterexample_B.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
