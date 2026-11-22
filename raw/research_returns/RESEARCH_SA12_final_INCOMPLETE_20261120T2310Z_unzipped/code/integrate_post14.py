"""Integrate audited post-checkpoint14 units; no archive is created here."""
from pathlib import Path
from datetime import datetime, timezone
import ast
import csv
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
paths = [
    'parts/B/post14_research/D_superperfect_quadratic_obstruction_B.tex',
    'parts/C/D_RDP_block_compression.tex',
    'parts/D/D_Chow_surface_boundary_obstruction.tex',
    'parts/D/D_generic_surface_finite_punctures.tex',
    'parts/B/post14_research/D_nonnormal_finite_puncture_transfer_B.tex',
    'parts/D/D_generic_surface_controlled_boundary.tex',
    'parts/B/post14_research/D_nonnormal_controlled_boundary_B.tex',
    'parts/C/D_weighted_exceptional_chain_compression.tex',
    'parts/D/D_codimension_one_projective_model.tex',
    'parts/B/post14_research/D_punctured_resolution_linear_size_B.tex',
    'parts/D/D_finite_normal_tame_descent.tex',
]
main_labels = {
    'D:generic-surface-finite-punctures',
    'D:normal-finite-puncture-quantitative-transfer',
    'D:nonnormal-finite-puncture-quantitative-transfer',
    'D:generic-surface-controlled-boundary',
    'D:nonnormal-controlled-boundary-quantitative-transfer',
    'D:codimension-one-projective-model',
    'D:complete-toric-fixed-boundary',
}
pattern = re.compile(r'\\begin\{(theorem|proposition|lemma|corollary|example)\}\[([^\]]+)\]\s*\\label\{([^}]+)\}')
records = []
for rel in paths:
    body = (root / rel).read_text()
    for match in pattern.finditer(body):
        title, sid = match.group(2), match.group(3)
        assert title.startswith(('Proved:', 'Proved under stated hypotheses:', 'Refuted:', 'Known:')), (rel, title)
        records.append(dict(
            id=sid, statement=title.split(':', 1)[1].strip(),
            status=title.split(':', 1)[0], where_proved=f'{rel}: label {sid}',
            depends_on='; '.join(sorted(set(re.findall(r'\\ref\{([^}]+)\}', body)))),
            manuscript_pages='29/061,066',
            notes=('Main dimensional reduction for finite omitted loci; complete actual-file proofs and independent source audits. General D.1, D.2(ii), and residual L8 remain open.' if sid in main_labels else 'Auxiliary result; complete actual-file proof and actual finite certificates where applicable. This does not count as requested-row movement.'),
        ))

p = root / 'parts/D/paper_D.tex'
s = p.read_text()
for rel in paths:
    line = '\\input{' + rel + '}'
    if line not in s:
        s += '\n' + line + '\n'
p.write_text(s)

cols = ['id', 'statement', 'status', 'where_proved', 'depends_on', 'manuscript_pages', 'notes']
p = root / 'parts/D/results_D.csv'
with p.open() as f:
    rows = list(csv.DictReader(f))
known = {r['id'] for r in rows}
added = [r for r in records if r['id'] not in known]
with p.open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows + added)

p = root / 'parts/D/CHECK_EVENTS_D.tsv'
with p.open() as f:
    events = list(csv.DictReader(f, delimiter='\t'))
def event(sid, actor, kind, outcome):
    events.append(dict(statement_id=sid, date=now,
        who=f'GPT-6 Astra Pro; /root{actor}; SA12 run1; effort setting not independently exposed',
        type=kind, outcome=outcome))

audit_details = {
    'D:superperfect-quadratic-obstruction': 'Universal-central-extension superperfectness, the repaired central-composition argument, low-degree product cohomology, all-field devissage, support dimension and q^(76r^2) counts, smallness, open prosolvable finiteness and failure of finite generation all checked. No geometric realization or priority claim.',
    'D:contract-zero-cost-blocks': 'Negative-even cycle arithmetic genus, Artin scheme contraction on an algebraic surface compactification, rational-double-point criterion, and descent of the map checked. Arbitrary nonalgebraic complete local surfaces are expressly outside this contraction statement.',
    'D:RDP-uniform-local-generators': 'Complete rational-double-point puncture groups and the uniform six-generator bound checked against the cited full table, including wild/non-taut characteristic-two cases.',
    'D:RDP-branch-gluing-obstruction': 'The characteristic-two A2 singularity, C3 full-puncture group, branch deletion and independent Artin-Schreier odd-pole classes checked. This example does not impose the inherited different or global extension constraints and is not a counterexample to D.1 or D.2(ii).',
    'D:Chow-surface-boundary-obstruction': 'Blowup incidence charts, O(1,1)=2H-E, seven-dimensional linear system, explicit smooth quadric through the line, and positive intersection with every exceptional fibre checked. Nonample pullback-plane repair is restricted to this example.',
    'D:generic-surface-finite-punctures': 'Exact Stacks Bertini hypotheses on each finite etale cover, fixed geometric generic coefficient tower, all-original-cover simultaneous quantifier, finite-transcendence extension, proper image, finite normalization, finite omitted locus and original-k target checked. No assertion onto the entire base-changed fundamental group.',
    'D:normal-finite-puncture-quantitative-transfer': 'H1 inflation, open-subgroup Shapiro bound, prosolvable quotient, direct injection on linear and ambient projective representation classes, and simple-product transfer checked. The five-term obstruction to an unconditional H2 injection is explicit.',
    'D:nonnormal-finite-puncture-quantitative-transfer': 'Finite normalization component scope, codimension condition, H1 cocycle subquotient, GL/PGL torsor Isom-section count on finitely many double-product components, ambient conjugacy relation and simple-product consequence checked. No H2 or full-generation claim.',
    'D:generic-surface-controlled-boundary': 'Divisorial/nondivisorial decomposition of the inverse boundary, exceptional point images, geometric-generic dimension cuts, smooth original-divisor open, transverse Kummer pullback including residue separability, normalized image and original-boundary quotient surjectivity checked. The projective-modification hypothesis is explicit; no claim for arbitrary positive-dimensional omitted loci.',
    'D:nonnormal-controlled-boundary-quantitative-transfer': 'Finite normalization preserves componentwise codimension; each component satisfies the explicit controlled-centre hypothesis. Fixed surface surjections and H1/GL/PGL finite-proper descent give the stated quantitative conclusions for positive-dimensional omitted loci. No H2 transfer or full-generation assertion.',
    'D:weighted-exceptional-chain-compression': 'Weighted canonical and anti-nef budgets, Nm=T-transpose times core multiplicities, elementary spectral-radius ADE shape, D/E branch-weight estimates, integral affine progressions and virtual-zero endpoints checked. Constants31/93/3/95 are verified algebraically. Unrestricted constant-multiplicity chain lengths still prevent an object-atlas inference; this remains auxiliary.',
    'D:codimension-one-projective-model': 'Refreshed full one-sided common-open audit: only the projective-model complement must have codimension at least two; the complement on the original variety is unrestricted. Identical original boundary DVRs, connected-cover restriction and quotient direction checked. The source is the already proved projective fixed-boundary group. Finite normalization and SGA1IX5.2 give the nonnormal D2 extension. Full finite generation holds under this explicit hypothesis, without an actual morphism to the projective model.',
    'D:complete-toric-fixed-boundary': 'Current Fujino--Sato theorem supplies a projective toric model agreeing in codimension one in every characteristic. The common zero-cone-and-rays subfan gives exactly the required opens; arbitrary non-torus-invariant boundaries and nonnormal schemes with toric normalized components are covered. The unrestricted proper case remains open.',
    'D:punctured-cover-linear-resolution': 'Non-Galois different transitivity, weighted maximum principle for the Jacobian divisor, scheme contraction and map descent, arbitrary-characteristic A_n equation, explicit proper resolution charts and gluing, continuous two-form Jacobian ideal, middle valuation, and degree-linear summation all checked. The exceptional fibre is explicitly nonempty. This bounds punctured-cover resolution size but supplies no hereditary object atlas or finite generation.',
    'D:finite-normal-tame-descent': 'Original boundary DVRs under finite dominant normal maps, tame base change including inseparable extensions, absolute-Galois image index at most the separable field degree, and adjoining coset representatives checked. This is closure of the review09 proved projective-model class, not separate movement or a generically-finite alteration theorem.',
}
for row in added:
    sid = row['id']
    for actor in ['', '/part_b', '/part_c', '/part_d']:
        event(sid, actor, 'complete actual-file proof check',
            'PASS. ' + audit_details[sid] + ' Checks were actually performed in the post-checkpoint14 integration period; exact author and independent provenance is retained in the part manifests.')
    if sid == 'D:punctured-cover-linear-resolution':
        for actor in ['', '/part_b', '/part_c', '/part_d']:
            event(sid, actor, 'fresh exact source check', 'PASS. Enriques Surfaces I author text19April2024, Proposition0.4.8 full proof printed69 and Theorem0.4.13 arbitrary-characteristic equation table printed72. Root actually viewed the entire rendered page72, including characteristic5. The classification theorem is a cited known input; no claim to have reread Artin classification proof. Explicit charts, Jacobian ideal and middle valuation are proved in the new file. No new finite program or computational certificate is claimed.')
    if sid == 'D:finite-normal-tame-descent':
        for actor in ['', '/part_b', '/part_c', '/part_d']:
            event(sid, actor, 'fresh exact source check', 'PASS. Complete Stacks0EXY Lemma15.116.9,0BQM Proposition58.11.3,0BQI Lemma58.10.7 proofs freshly read for this file. Tame arbitrary-DVR base change and normal generic-point surjectivity have exactly the required scope.')
    if sid in ('D:generic-surface-finite-punctures', 'D:normal-finite-puncture-quantitative-transfer'):
        for actor in ['', '/part_b', '/part_c', '/part_d']:
            scope = ('Complete Stacks37.32.1--3/0G4C and33.47.3/0FD6 proofs; Landesman2005.10708v1 Remark1.5 and Proposition2.1/Lemma2.2/Corollary2.3 complete proofs pp4--6.' if actor == '/part_c' else 'Complete Stacks37.32.1--3/0G4C,33.47.3/0FD6,Chow30.18.1/0200,normalization29.55.8--11/035E proofs. Landesman Remark1.5 and Proposition2.1/Lemma2.2/Corollary2.3 checked by root and D; B does not claim a fresh Landesman read.')
            event(sid, actor, 'fresh primary-source check', 'PASS. ' + scope)
    if sid == 'D:superperfect-quadratic-obstruction':
        for actor in ['', '/part_b', '/part_c', '/part_d']:
            event(sid, actor, 'fresh primary-source check',
                'PASS. Weibel1994 chapter6,6.9.2--6.9.10 printed199--202, and GKKL2007 Lemma4.1 complete proof printed481 and the written Section6 proofs supporting Theorem6.2 printed487--493. The Schur multiplier is a cited known calculation; GKKL reference[42] computational cases were not rerun. Exact read scopes and dates are in the B/D manifests.')
        for actor, runtime, output in [('',0.845041883,'parts/B/post14_research/output/superperfect_product_root.json'),('/part_b',0.898178641,'parts/B/post14_research/output/superperfect_product_author.json'),('/part_d',0.913874638,'parts/D/output/superperfect_product.json')]:
            event(sid, actor, 'actual finite certificate execution', f'PASS.112276 exact assertions in{runtime:.9f}s. Program SHA256aec4d45e5ec438025ae7415a433da0370951907c804e37e2d496264179d6ad73. Output:{output}. Finite permutation/counting/tensor checks only; no Schur-multiplier computation or GKKL base-case rerun.')
    if sid == 'D:generic-surface-controlled-boundary':
        for actor in ['', '/part_c', '/part_d']:
            event(sid, actor, 'fresh primary-source check', 'PASS. Complete Stacks0BFP Lemma33.17.3 proof and primary SGA1 ExposeXIII Propositions5.1--5.2, their full proofs, and Corollary5.3 printed428--430, preserved smf_doc-math_3_01.tex25225--25410. Kummer regularity, absolute Abhyankar extension, purity step and strict-local consequence checked. B reused prior exact source inputs and does not claim a fresh source read here.')
    if sid in ('D:codimension-one-projective-model', 'D:complete-toric-fixed-boundary'):
        for actor in ['', '/part_b', '/part_c', '/part_d']:
            event(sid, actor, 'fresh primary-source check', 'PASS. Fujino--Sato current author version0.27,12July2025, matching arXiv2412.02392v2: arbitrary-characteristic convention, Theorems1.1/1.3 pp1--2, complete Lemma3.1 and Section3 proof pp6--7. Root independently verified publisher DOI10.1080/10586458.2025.2536032 and online publication11August2025. Earlier author09/version0.20 is distinguished from the cited current author11/version0.27. This is an exact theorem/proof read, not a reread of every toric Mori-theory reference used in that proof.')
        for actor in ['', '/part_d']:
            event(sid, actor, 'fresh proper-descent source check', 'PASS. SGA1IX4.7 statement and complete proof pp238--239; IX5.1/5.2 statements and preceding generator construction pp247--248. No fresh reread of all earlier Section5 path construction is claimed in this event. Finite normalizations and their double products have finitely many components as required.')
    if sid == 'D:contract-zero-cost-blocks':
        for actor in ['', '/part_c']:
            event(sid, actor, 'fresh primary-source check', 'PASS. Artin1962 published Russian translation Theorem2.3 complete proof printed9--10; root also actually viewed both page images. Enriques Surfaces I author text19April2024 Proposition0.4.8 complete proof printed69/PDFindex84. Exact algebraic surface and scheme contraction hypotheses checked; no claim of opening the inaccessible original English paper.')
    if sid == 'D:RDP-uniform-local-generators':
        for actor in ['', '/part_c']:
            event(sid, actor, 'fresh primary-source check', 'PASS. Matsumoto2022 Journal of Singularities24, Convention1.3(2) printed81 and complete Table7 printed93; unbounded cyclic/dihedral/binary-dihedral families and all residual orders at most120 checked.')
    if sid == 'D:RDP-branch-gluing-obstruction':
        for actor, runtime, output in [('',0.000212327,'parts/C/output/RDP_branch_obstruction_root.json'),('/part_c',0.000229973,'parts/C/output/RDP_branch_obstruction.json'),('/part_d',0.000223133,'parts/D/output/RDP_branch_obstruction.json')]:
            event(sid, actor, 'actual finite certificate execution', f'PASS.1643 exact assertions in{runtime:.12f}s. Program SHA256ccc9ed54bed4fc65d5c48958e8fa0fc1e39c303f4d5b6906ec2eda94c786c939. Output:{output}. Finite field action/monomial/valuation checks only; infinite Artin-Schreier independence has a separate proof.')
    if sid == 'D:Chow-surface-boundary-obstruction':
        for actor in ['', '/part_d']:
            event(sid, actor, 'fresh primary-source check', 'PASS. Complete Stacks0804 blowup charts,01WD Segre embedding, and01XT projective-space cohomology, including the contracting-homotopy footnote, freshly read.')
        for actor, runtime, output in [('',0.042671849,'parts/D/output/Chow_surface_boundary_root.json'),('/part_d',0.069992541,'parts/D/output/Chow_surface_boundary.json'),('/part_b',0.042904115,'parts/B/post14_research/integration_manifest_B_post14.json')]:
            event(sid, actor, 'actual finite certificate execution', f'PASS.1705 exact assertions in{runtime:.9f}s. Program SHA2561c0876f45927c5b598f4c27eb9ae5f25eb9722064834e4fba50438a0bdc08537. Output or exact run receipt:{output}. Symbolic integer identities and finite F2/F3/F5 incidences only; generic geometry is separately proved.')
ecols = ['statement_id', 'date', 'who', 'type', 'outcome']
with p.open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=ecols, delimiter='\t'); w.writeheader(); w.writerows(events)

for dest, source, key in [
    ('parts/B/references_B.bib','parts/B/post14_research/references_superperfect_B.bib','Weibel1994SuperperfectB'),
    ('parts/C/references_C.bib','parts/C/references_C_post14.bib','C_Matsumoto2022RDP'),
    ('parts/D/references_D.bib','parts/D/references_Chow_section_D.bib','StacksDChowSection'),
    ('parts/D/references_D.bib','parts/D/references_generic_surface_D.bib','StacksDGenericSurface'),
    ('parts/D/references_D.bib','parts/D/references_controlled_boundary_D.bib','StacksDControlledBoundary'),
    ('parts/D/references_D.bib','parts/D/references_codimension_one_D.bib','FujinoSato2025D'),
    ('parts/D/references_D.bib','parts/D/references_finite_tame_descent_D.bib','StacksDFiniteTameDescent'),
]:
    p = root / dest; s = p.read_text()
    if '{' + key + ',' not in s:
        p.write_text(s + '\n\n' + (root / source).read_text() + '\n')

p = root / 'code/assemble.py'
s = p.read_text(); tree = ast.parse(s)
node = next(n for n in tree.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'outcomes' for t in n.targets))
outcomes = ast.literal_eval(node.value)
for i, (item, status, loc) in enumerate(outcomes):
    if item in ('D.1', 'D.2(ii)'):
        suffix = '; a fixed geometric-generic surface now detects every original cover for finite omitted loci in all dimensions, transferring all-field linear H1, defining-characteristic quadratic counts and bounded-scalar simple-product bounds'
        if suffix not in status:
            status += suffix
        labels = ['D:generic-surface-finite-punctures', 'D:normal-finite-puncture-quantitative-transfer']
        if item == 'D.2(ii)':
            labels += ['D:nonnormal-finite-puncture-quantitative-transfer']
        controlled_suffix = '; the same surface reduction holds with positive-dimensional boundary when every exceptional divisor of the chosen projective modification centred inside the boundary has point image'
        if controlled_suffix not in status:
            status += controlled_suffix
        labels += ['D:generic-surface-controlled-boundary']
        if item == 'D.2(ii)':
            labels += ['D:nonnormal-controlled-boundary-quantitative-transfer']
        full_suffix = '; full finite generation proved when a dense open is identified with an open in a projective normal model whose complement has codimension at least two, in particular every complete toric variety with arbitrary closed boundary'
        if full_suffix not in status:
            status += full_suffix
        labels += ['D:codimension-one-projective-model', 'D:complete-toric-fixed-boundary']
        loc = '; '.join(dict.fromkeys(labels + [x.strip() for x in loc.split(';')]))
    elif item == 'L8':
        status = 'Incomplete only through residual D.1/D.2(ii); finite omitted loci and controlled exceptional centres have the stated dimensional reduction; full finite generation holds for codimension-one projective models and complete toric compactifications, with the specified nonnormal descent'
        loc = '; '.join(dict.fromkeys(['D:generic-surface-finite-punctures', 'D:nonnormal-finite-puncture-quantitative-transfer', 'D:generic-surface-controlled-boundary', 'D:nonnormal-controlled-boundary-quantitative-transfer', 'D:codimension-one-projective-model', 'D:complete-toric-fixed-boundary'] + [x.strip() for x in loc.split(';')]))
    outcomes[i] = (item, status, loc)
lines = s.splitlines(keepends=True)
lines[node.lineno - 1:node.end_lineno] = ['outcomes=[\n' + ',\n'.join(repr(x) for x in outcomes) + '\n]\n']
s = ''.join(lines)
s = s.replace('unrestricted-dimensional nonprojective global reduction remains open.', 'the nonprojective global reduction with positive-dimensional omitted loci remains open. For finite omitted loci, the new fixed geometric-generic surface theorem supplies a surjection onto the original fundamental group in every dimension; the quantitative conclusions also descend through finite normalization for nonnormal proper schemes.')
s = s.replace('Next formal review09 is due11:10 UTC; next immutable checkpoint14 is due10:40 UTC. Checkpoint13 was saved with verified252-page build76.', 'Next formal review09 is due11:10 UTC; next immutable checkpoint15 is due11:25 UTC. Checkpoint14 was saved with verified268-page build85 and five explicitly identified checked source units awaiting assembly.')
new_paragraphs = [
    'After review08, the complete generic-surface theorem removes the dimensional reduction gate for finite omitted loci: one normal proper surface over a fixed algebraically closed extension detects all covers of the original scheme. The fixed surface does not depend on rank, field, or cover. All-field linear H1, defining-characteristic q^(C r^2) counts, bounded-scalar projective counts, prosolvable finite generation and the stated simple-product bounds transfer. Finite normalization and explicit Isom-section counting give the same quantitative conclusions for nonnormal proper schemes with finite componentwise-codimension-two omitted loci. This dimensional reduction was counted at formal review09 and is not additional movement after that review. It does not imply H2 injection, full finite generation, or control for positive-dimensional omitted loci.',
    'The five checked auxiliary units first archived as source at checkpoint14 are now assembled. A superperfect alternating-cover product shows that smallness, linear H1 and H2, all-field quadratic representation counts and finite open prosolvable quotients still do not force finite generation abstractly. Rational (-2)-blocks contract to rational double points in the stated algebraic surface setting, with at most six local puncture generators, but removing a branch can leave infinitely many Artin-Schreier classes. The explicit blowup of P3 along a line refutes blanket codimension-two preservation by ample Chow sections. These auxiliary results do not count as requested-row movement.',
    'The same dimensional reduction now covers an explicit class of positive-dimensional boundaries. On a fixed normal projective modification, require every exceptional divisor whose centre lies inside the boundary to have point image. Generic sections meet every remaining bad subset only finitely, while their boundary curves arise transversely from the original divisors. Absolute Abhyankar then preserves exactly the original-boundary tameness conditions. This gives a surface quotient surjecting onto Q(S,T), and a finite-punctured surface quotient for codimension-at-least-two boundary. Finite normalization descends the quantitative conclusions to nonnormal schemes when the condition holds on each normalized component. Arbitrary positive-dimensional exceptional centres remain outside this theorem.',
    'A separate full-generation criterion now treats every normal proper variety with a dense open identified with an open in a projective normal model whose complement has codimension at least two. Only the projective complement is constrained; divisors may be omitted on the original side. Restriction preserves connectedness, and identical original boundary DVRs give a surjection from the projective fixed-boundary tame group. Fujino and Sato (2025), Theorem1.1 and its complete Section3 proof, supply this condition for every complete toric variety in arbitrary characteristic. No invariance condition is imposed on the omitted set. Finite normalization gives the full D.2 conclusion for proper schemes whose normalized components have such models. This criterion does not require an actual morphism to the projective model and does not establish that arbitrary proper schemes admit one.',
    'The auxiliary weighted exceptional-graph refinement bounds all nonconstant-multiplicity chain lengths linearly in cover degree, leaving at most3nc constant-multiplicity rational chains of unrestricted length. It uses an elementary positive-definite graph argument and does not supply the missing hereditary atlas or a further movement event.',
]
for para in new_paragraphs:
    if para not in s:
        s = s.replace("'','## Files and continuation','',", repr(para) + ",\n'','## Files and continuation','',")
s = s.replace('Arbitrarily many vertices in rational (-2)-blocks remain possible.', 'Those three estimates alone did not control the number of vertices in rational (-2)-blocks; the later punctured-cover resolution theorem now supplies that control for covers unramified outside an isolated point.')
s = s.replace('leaving at most3nc constant-multiplicity rational chains of unrestricted length.', 'leaving at most3nc constant-multiplicity rational chains before the subsequent punctured-cover Jacobian estimate is imposed.')
for para in [
    'The later auxiliary theorem D:punctured-cover-linear-resolution bounds the entire exceptional resolution graph, its genus sum and its negative-square sum linearly in cover degree for covers unramified outside an isolated surface point. A uniform ratio bound for the Jacobian divisor and an explicit A_n middle-valuation calculation also bound the constant-multiplicity chains. It still does not provide a degree-linear hereditary object atlas, a factorial cover-count estimate or general finite generation, and is not formal-review movement.',
    'Finite normal tame descent closes the review09 full-generation class under finite dominant normal images, including inseparable finite maps. The induced original-boundary quotient image has index at most the separable function-field degree. In particular arbitrary existing normal proper finite images of complete toric varieties are covered. This is a closure property of the proved criterion and is not a separate movement event.',
]:
    if para not in s:
        s = s.replace("'','## Files and continuation','',", repr(para) + ",\n'','## Files and continuation','',")
p.write_text(s)

p = root / 'parts/D/unresolved_D.tex'; s = p.read_text()
marker = '% Post-checkpoint14 finite omitted-locus dimensional reduction'
if marker not in s:
    s += '\n\n' + marker + r'''
\paragraph{The finite omitted-locus reduction and its limit.}
Theorem~\ref{D:generic-surface-finite-punctures} constructs one fixed
normal proper surface over an algebraically closed extension whose
punctured fundamental group surjects onto the original group whenever
the omitted locus is finite. Corollaries
\ref{D:normal-finite-puncture-quantitative-transfer} and
\ref{D:nonnormal-finite-puncture-quantitative-transfer} transfer the
linear first-cohomology and quadratic representation bounds, the
prosolvable conclusion and the bounded-scalar simple-product conclusions
in every dimension, including the stated nonnormal case. Positive-dimensional
omitted loci still need a global reduction, and full nonabelian-crown
control remains open even on punctured surfaces. No second-cohomology
injection is inferred from the group surjection.

\paragraph{Why the auxiliary repairs do not close that gate.}
Example~\ref{D:superperfect-quadratic-obstruction} adds rank-linear
second cohomology to the abstract non-generation obstruction.
Proposition~\ref{D:contract-zero-cost-blocks} and
Lemma~\ref{D:RDP-uniform-local-generators} compress the long rational
$(-2)$-blocks geometrically and bound full local puncture generators.
Example~\ref{D:RDP-branch-gluing-obstruction} shows that branch
deletion needs additional control; the inherited different and global
extension constraints remain relevant and are not refuted by that example.
Example~\ref{D:Chow-surface-boundary-obstruction} prevents an unrestricted
ample-slicing shortcut when the original omitted locus has positive
dimension. None of these auxiliary facts supplies the missing hereditary
cover-count atlas or full finite generation.
'''
    p.write_text(s)

marker = '% Post-checkpoint14 full generation through codimension-one projective models'
if marker not in s:
    s += '\n\n' + marker + r'''
\paragraph{A further full-generation class.}
Proposition~\ref{D:codimension-one-projective-model} proves full finite
generation when a dense open of a normal proper variety is identified
with an open of a projective normal model whose complement has
codimension at least two. No codimension condition is required on
the original side. Corollary~\ref{D:complete-toric-fixed-boundary}
applies this to every complete toric variety in arbitrary characteristic
and every closed boundary, including noninvariant boundaries. The stated
nonnormal descent is also full finite generation. A general proper
variety is not asserted to admit such a model; the surface problem and
the remaining unrestricted-dimensional cases therefore remain open.
Proposition~\ref{D:weighted-exceptional-chain-compression} further
compresses exceptional graphs but leaves constant-multiplicity chains
of unrestricted length and supplies no cover-count atlas.
'''
    p.write_text(s)

marker = '% Post-checkpoint14 controlled exceptional centres'
if marker not in s:
    s += '\n\n' + marker + r'''
\paragraph{An explicit extension to positive-dimensional boundaries.}
Theorem~\ref{D:generic-surface-controlled-boundary} gives the surface
reduction if a fixed normal projective modification has only point
images for exceptional divisors centred inside the omitted locus.
Its original-divisorial-boundary quotient maps surjectively to the
original quotient, using generic transversality and absolute Abhyankar.
For codimension-at-least-two boundary the surface has finite punctures.
Corollary~\ref{D:nonnormal-controlled-boundary-quantitative-transfer}
descends the quantitative conclusions through finite normalization.
This narrows the dimensional gate further, but the existence of such
a modification is not asserted for arbitrary pairs. Positive-dimensional
exceptional centres lying in the boundary remain uncontrolled.
'''
    p.write_text(s)

p = root / 'parts/D/unresolved_D.tex'
s = p.read_text().replace('compresses exceptional graphs but leaves constant-multiplicity chains\nof unrestricted length and supplies no cover-count atlas.', 'compresses exceptional graphs. The later\nProposition~\\ref{D:punctured-cover-linear-resolution} also bounds the\nconstant-multiplicity chains for covers unramified outside an isolated\nsurface point. Neither result supplies a cover-count atlas.')
marker = '% Post-review09 finite normal closure and punctured graph bound'
if marker not in s:
    s += '\n\n' + marker + r'''
\paragraph{Two further limits of the present conclusions.}
Proposition~\ref{D:finite-normal-tame-descent} closes the proved
full-generation classes under finite dominant normal images, including
inseparable finite maps. Its image-index estimate does not apply to
arbitrary merely generically finite modifications with new exceptional
boundary divisors. Proposition~\ref{D:punctured-cover-linear-resolution}
bounds the full exceptional graph size linearly in cover degree for
isolated punctures, using the Jacobian cost of a constant-multiplicity
chain. The remaining atlas problem includes formal-neighborhood and
gluing parameters; a graph-size bound alone does not settle it.
These are auxiliary or closure results, not further formal-review
movement after review09.
'''
p.write_text(s)

manifest = dict(utc=now, labels=[r['id'] for r in records],
    added_rows=len(added), main_reduction_labels=sorted(main_labels),
    files=[dict(path=rel, sha256=hashlib.sha256((root / rel).read_bytes()).hexdigest()) for rel in paths],
    archive_created=False, requested_open=['D.1', 'D.2(ii)', 'residual L8'])
(root / 'code/output/integrate_post14.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps(dict(statements_integrated=len(records), added_rows=len(added), archive_created=False)))
