"""Integrate fully audited post-checkpoint13 proofs; never create an archive."""
from pathlib import Path
from datetime import datetime, timezone
import ast, csv, hashlib, json, re

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
paths = [
    'parts/D/D_cross_characteristic_H2.tex',
    'parts/B/post09_reconstruction/D_bounded_centre_projective_B.tex',
    'parts/B/post09_reconstruction/D_bounded_centre_nonnormal_B.tex',
    'parts/C/D_local_cross_characteristic_H2.tex',
    'parts/B/post09_reconstruction/D_bounded_scalar_classical_B.tex',
    'parts/B/post09_reconstruction/D_local_bounded_scalar_B.tex',
    'parts/D/D_symplectic_orthogonal_scalar_lifts.tex',
    'parts/B/post09_reconstruction/D_exceptional_arithmetic_and_Frobenius_B.tex',
    'parts/C/D_exceptional_graph_core.tex',
]
pattern = re.compile(r'\\begin\{(theorem|proposition|lemma|corollary|example)\}\[([^\]]+)\]\s*\\label\{([^}]+)\}')
records = []
for rel in paths:
    body = (root / rel).read_text()
    for match in pattern.finditer(body):
        title, sid = match.group(2), match.group(3)
        assert title.startswith(('Proved:', 'Proved under stated hypotheses:', 'Refuted:', 'Known:')), (rel, title)
        records.append(dict(id=sid, statement=title.split(':', 1)[1].strip(),
            status=title.split(':', 1)[0], where_proved=f'{rel}: label {sid}',
            depends_on='; '.join(sorted(set(re.findall(r'\\ref\{([^}]+)\}', body)))),
            manuscript_pages='29/061,066', notes='Complete post-checkpoint13 proof audited on the actual file by root and independent agents. General D.1, D.2(ii), and residual L8 remain open.'))

paper = root / 'parts/D/paper_D.tex'
s = paper.read_text()
for rel in paths:
    line = '\\input{' + rel + '}'
    if line not in s:
        s += '\n' + line + '\n'
paper.write_text(s)

p = root / 'parts/D/results_D.csv'
with p.open() as f:
    rows = list(csv.DictReader(f))
known = {row['id'] for row in rows}
added = [row for row in records if row['id'] not in known]
cols = ['id', 'statement', 'status', 'where_proved', 'depends_on', 'manuscript_pages', 'notes']
with p.open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows + added)

p = root / 'parts/D/CHECK_EVENTS_D.tsv'
with p.open() as f:
    events = list(csv.DictReader(f, delimiter='\t'))
for row in added:
    sid = row['id']
    agents = ['/root', '/root/part_b', '/root/part_d']
    if sid != 'D:nonnormal-bounded-centre-projective-growth':
        agents.append('/root/part_c')
    for agent in agents:
        auxiliary = sid in ('D:exceptional-arithmetic-genus-bound', 'D:normalization-Frobenius-saturation', 'D:exceptional-degree-linear-core')
        events.append(dict(statement_id=sid, date=now,
            who=f'GPT-6 Astra Pro; {agent}; SA12 run1; effort setting not independently exposed',
            type='complete actual-file proof audit',
            outcome=('PASS. Complete actual-file audit of the arithmetic exceptional-fibre and nonreduced-divisor bounds, trace-dual Frobenius saturation and actual-image extension, or weighted canonical and Schur-complement core bounds, as applicable. Long rational (-2)-blocks and the missing hereditary object atlas remain explicitly uncontrolled. This is auxiliary, not requested-row movement.' if auxiliary else 'PASS. Exact continuous-cohomology injection and Leray direction, or bounded-centre finite-field lifting and projective descent count, checked in the complete actual file. All open-scope limitations retained. Source audit details are in parts/D/H2_source_audit_notes.md and parts/B/post09_reconstruction/integration_manifest_B_post13.json.')))
    if sid == 'D:normalization-Frobenius-saturation':
        events.append(dict(statement_id=sid, date=now,
            who='GPT-6 Astra Pro; /root; SA12 run1; effort setting not independently exposed',
            type='fresh primary-source check',
            outcome='PASS. Complete Stacks Project section49.8 (Tag0BW0, trace-dual lattice and different), Lemma10.128.1 with proof (Tag00R4, miracle flatness), and Lemma31.13.12 with proof (Tag0EBJ, extension of reflexive sheaves across depth-at-least-two complement), read at10:25UTC on2026-11-20. The rational inverse extends between vector bundles; an unproved reflexive-image substitution is not used.'))
    if sid.startswith('D:surface-tame-'):
        events.append(dict(statement_id=sid, date=now,
            who='GPT-6 Astra Pro; /root; SA12 run1; effort setting not independently exposed',
            type='fresh primary-source check',
            outcome='PASS. Milne LEC12.7 statement/proof pp82–83;14.9 full proof and14.10 pp96–97;14.13 statement/proof p98;17.7 statement p116 and17.10 statement/derivation pp116–117. CFTII1.18(b)/1.19 pp65–66,1.34 full proof/1.35 pp71–72,4.2 full continuous-cochain proof including footnote6 p87. Hu–Teyssier arXiv2502.11060v1 Theorem7.34 and complete proof p41, finite fields and j=2. No full-proof read of17.7 is claimed.'))
    if sid in ('D:local-surface-constant-H2', 'D:local-bounded-central-obstructions', 'D:strict-local-open-cohomology-finite', 'D:local-bounded-scalar-simple-product'):
        events.append(dict(statement_id=sid, date=now,
            who='GPT-6 Astra Pro; /root; SA12 run1; effort setting not independently exposed',
            type='fresh primary-source check',
            outcome='PASS. ILO ExposeXVI Theorem3.1.1 statement and Corollary3.1.3 with COMPLETE normal-crossings proof, preserved gysin.tex1294–1375 and printedpp242–243; not a reread of the full absolute-purity proof. ExposeXIII Theorem1.1.1(i) and COMPLETE constructibility proof sections2.1–2.2, finitude.tex throughCQFD, freshly read by root. Exact noetherian quasi-excellent/invertible-coefficient hypotheses match strict-local opens in every dimension. Milne exact-stalk/Leray and continuous cocycle inputs separately checked.'))
    if sid in ('D:bounded-centre-unitary-simple-product', 'D:symplectic-orthogonal-simple-product'):
        events.append(dict(statement_id=sid, date=now,
            who='GPT-6 Astra Pro; /root; SA12 run1; effort setting not independently exposed',
            type='fresh primary finite-group source check',
            outcome='PASS. Taylor author-hosted corrected2021 text: unitary orders/scalar kernels printed117–118 and Theorem10.20 complete proof127–128. For Sp/Omega, scalar/order69–70, Theorem8.7 complete proof72–74 and8.8p74; definitions136–137; Theorem11.9 complete proof143–144; Theorem11.48 proof162; Theorem11.51 complete proof164–165 and order derivations165–166. Natural matrix lifts, all small exceptions and rank-uniform order inequalities checked. This is recognition inside the already-proved bounded-scalar criterion, not additional post-review08 movement.'))
ecols = ['statement_id', 'date', 'who', 'type', 'outcome']
with p.open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=ecols, delimiter='\t'); w.writeheader(); w.writerows(events)

bib = root / 'parts/D/references_D.bib'
s = bib.read_text()
extra = (root / 'parts/D/references_H2_D.bib').read_text()
if 'MilneLEC2013H2D,' not in s:
    s += '\n\n' + extra + '\n'
bib.write_text(s)

bib = root / 'parts/B/references_B.bib'; s = bib.read_text()
if 'Taylor1992ClassicalB,' not in s:
    s += '\n\n' + (root / 'parts/B/post09_reconstruction/references_classical_B.bib').read_text() + '\n'
bib.write_text(s)

# Preserve the existing ILO bibliography identity while adding the exact new scope.
bib = root / 'parts/A/references_A.bib'; s = bib.read_text()
keypos = s.find('{A_ILO2014,')
if keypos >= 0:
    note = s.find('note', keypos)
    start = s.find('{', note)
    level = 1; end = start + 1
    while level:
        if s[end] == '{' and s[end - 1] != '\\': level += 1
        elif s[end] == '}' and s[end - 1] != '\\': level -= 1
        end += 1
    extra = ' Also freshly read: Expose XVI, Theorem 3.1.1 statement and complete normal-crossings Corollary 3.1.3 proof, preserved arXiv printed pp. 242--243; Expose XIII, Theorem 1.1.1(i) and complete constructibility proof in sections 2.1--2.2. The arbitrary regular and quasi-excellent base hypotheses were checked; no claim of rereading the entire absolute-purity proof is made.'
    if extra not in s:
        s = s[:end - 1] + extra + s[end - 1:]
    bib.write_text(s)

p = root / 'code/assemble.py'; s = p.read_text(); tree = ast.parse(s)
node = next(n for n in tree.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'outcomes' for t in n.targets))
outcomes = ast.literal_eval(node.value)
for i, (item, status, loc) in enumerate(outcomes):
    if item in ('D.1', 'D.2(ii)'):
        old_suffix = '; all-rank bounded-centre defining-characteristic type-A simple-product quotients are finitely generated'
        status = status.replace(old_suffix, '')
        suffix = '; all-rank defining-characteristic simple-product bounds include bounded-centre PSL and PSU, and natural symplectic and orthogonal groups'
        if suffix not in status:
            status += suffix
        labels = ['D:surface-bounded-centre-simple-product', 'D:bounded-centre-unitary-simple-product', 'D:symplectic-orthogonal-simple-product'] if item == 'D.1' else ['D:nonnormal-bounded-centre-projective-growth', 'D:local-bounded-scalar-simple-product', 'D:bounded-centre-unitary-simple-product', 'D:symplectic-orthogonal-simple-product']
        loc = '; '.join(dict.fromkeys(labels + [x.strip() for x in loc.split(';')]))
    elif item == 'L8':
        loc = '; '.join(dict.fromkeys(['D:surface-bounded-centre-simple-product', 'D:nonnormal-bounded-centre-projective-growth'] + [x.strip() for x in loc.split(';')]))
    outcomes[i] = (item, status, loc)
lines = s.splitlines(keepends=True)
lines[node.lineno - 1:node.end_lineno] = ['outcomes=[\n' + ',\n'.join(repr(x) for x in outcomes) + '\n]\n']
s = ''.join(lines)
s = s.replace('Nonabelian crown multiplicities, alternating factors and the remaining projective or semilinear Lie families require geometric control;', 'Nonabelian crown multiplicities, alternating factors, projective linear or unitary families with unbounded natural centre, and the remaining semilinear Lie cases require geometric control;')
paragraph = 'Cross-characteristic H2 now has a rank-linear surface bound. It gives finitely many central lifting classes at every bounded centre order. One fixed normal open subgroup kills these classes, so all-rank bounded-centre type-A projective representation counts are quadratic and their simple-product quotients are finitely generated. Finite normalization and PGL-torsor descent give the same conclusion for nonnormal proper-surface punctures. These conclusions do not control unrestricted central order or general nonabelian crowns.'
if paragraph not in s:
    s = s.replace("'','## Files and continuation','',", repr(paragraph) + ",\n'','## Files and continuation','',")
p.write_text(s)

p = root / 'parts/D/unresolved_D.tex'; s = p.read_text()
marker = '% Audited post-checkpoint13 bounded-central-order reduction'
if marker not in s:
    s += '\n\n' + marker + r'''
\paragraph{The remaining projective and crown gate.}
Theorem~\ref{D:surface-tame-cross-characteristic-H2} proves
rank-linear second cohomology in coefficient characteristics distinct
from the ground characteristic. Corollary~\ref{D:surface-tame-central-obstructions}
controls the central lifting classes. For every fixed bound on the natural
centre, Corollary~\ref{D:surface-bounded-centre-simple-product} removes
all ranks of the stated type-A simple-product family. The same conclusion
holds for nonnormal proper-surface punctures by
Corollary~\ref{D:nonnormal-bounded-centre-projective-growth}.
The constant is allowed to depend on that centre bound. Unbounded central
order, alternating multiplicities, semilinear actions, general nonabelian
crowns, and the unrestricted-dimensional global reduction remain unresolved.
'''
    p.write_text(s)

marker = '% Local and natural classical recognition after the same criterion'
if marker not in s:
    s += '\n\n' + marker + r'''
\paragraph{Local and named-family scope.}
Corollary~\ref{D:strict-local-open-cohomology-finite} gives the
invertible-coefficient finiteness input in arbitrary local dimension.
Corollary~\ref{D:local-bounded-scalar-simple-product} applies the
bounded-scalar criterion to complete equicharacteristic normal punctures
in every dimension. Corollaries~\ref{D:bounded-centre-unitary-simple-product}
and \ref{D:symplectic-orthogonal-simple-product} verify the named natural
classical families, including their scalar kernels and small exceptions.
This recognition does not turn a simple-product statement into a bound
for general crowns and does not cover the remaining cross-characteristic
families or unbounded linear and unitary centres.
'''
    p.write_text(s)

marker = '% Auxiliary exceptional core and Frobenius saturation'
if marker not in s:
    s += '\n\n' + marker + r'''
\paragraph{What the new exceptional estimates leave open.}
Proposition~\ref{D:exceptional-arithmetic-genus-bound} bounds the
arithmetic genus of the full reduced exceptional fibre and its graph cycles
linearly in cover degree. Proposition~\ref{D:exceptional-degree-linear-core}
also bounds the core components, their negative squares, genera and all
attachments to the remaining rational $(-2)$-blocks. The numbers of
vertices inside these blocks remain unrestricted. Lemma
\ref{D:normalization-Frobenius-saturation} supplies a degree-independent
pole bound for the inverse Frobenius map on the actual finite
normalization lattice. These auxiliary bounds do not yet supply a
hereditary object atlas with parameter count linear in cover degree,
a factorial cover-count bound, or full nonabelian-crown control.
'''
    p.write_text(s)

manifest = {'utc': now, 'labels': [r['id'] for r in records], 'added_rows': len(added),
    'files': [{'path': rel, 'sha256': hashlib.sha256((root / rel).read_bytes()).hexdigest()} for rel in paths],
    'archive_created': False, 'requested_open': ['D.1', 'D.2(ii)', 'residual L8']}
(root / 'code/output/integrate_post13.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps({'statements_integrated': len(records), 'added_rows': len(added), 'archive_created': False}))
