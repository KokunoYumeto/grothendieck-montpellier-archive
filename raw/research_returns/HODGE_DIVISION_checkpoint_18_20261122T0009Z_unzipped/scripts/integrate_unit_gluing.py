"""Integrate complete root/peer-reviewed unit forms and first-overlap proof."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json

R = Path(__file__).resolve().parents[1]
proofs = {
    'agents/sixfolds/rm_unit_gluing_analysis_section.tex': '6166483dd5dc84ce1000b134f02bdb8376035f093fa71c8f3de9b03b786feae7',
    'agents/sixfolds/rm_unit_gluing_obstruction_section.tex': '0d9d4642484974604add5a6ccb961bde4eac65fba12354718a55bd2025861819',
}
for name, digest in proofs.items():
    assert hashlib.sha256((R/name).read_bytes()).hexdigest() == digest
now = datetime.now(timezone.utc).isoformat()
q = R/'QUESTIONS.tsv'
rows = list(csv.DictReader(q.open(), delimiter='\t'))
fields = list(rows[0])
assert not {'Q5v','Q5w'} & {r['id'] for r in rows}
(R/'research/gates_before_unit_gluing.json').write_text(json.dumps({r['id']:r for r in rows if r['id']=='Q5i'},indent=2)+'\n')
p = R/'HODGE_DIVISION.tex'
s = p.read_text()
anchor = r'\input{agents/sixfolds/rm_tensor_surface_obstruction_section.tex}'
assert anchor in s and all(name not in s for name in proofs)
s = s.replace(anchor, anchor+'\n'+'\n'.join(r'\input{'+name+'}' for name in proofs))
a = '''factor separately. Genuinely different global gluing, other unequal-degree
extensions, other support classes, nonreduced or singular surface modules,
and more general derived couplings remain open.'''
b = r'''factor separately. SF-UG then constructs actual nontensor forms of
the unit module, including at least $5823$ independent parameters in
one explicit summand for the same positive integral balanced character.
SF-E824 excludes every global form locally isomorphic to $M_0^r$,
including all this nontensor gluing. Its canonical first overlap
obstruction has a nonzero trace; the determinant correction vanishes
after the justified algebraic $B$ normalization. No trace on the full
derived self-Hom complex and no preservation of semiregularity under
isogeny is assumed. Added free summands, rank-deficient unit matrices,
other unequal-degree extensions, other support classes, nonreduced or
singular surface modules, and more general derived couplings remain open.'''
assert a in s
p.write_text(s.replace(a,b))

for row in rows:
    if row['id'] == 'Q5i':
        a = 'SF-US constructs an actual positive integral full-character example and local nullhomotopies, but no seed. Remaining:'
        b = ('SF-US constructs an actual positive integral full-character example and local nullhomotopies, but no seed. '
             'SF-UG constructs actual nontensor unit forms with at least5823 parameters in an explicit summand. '
             'SF-E824 excludes every global form locally M0^r on the smooth ample complete intersection, '
             'without a global tensor factor, by the canonical first-overlap trace and determinant correction; '
             'the rational B step transports ordinary obstruction vanishing only. Remaining:')
        assert a in row['finding_ids_or_current_gate']
        row['finding_ids_or_current_gate'] = row['finding_ids_or_current_gate'].replace(a,b)
        a = 'outsideE818/E821/E822/E823 (including genuinely different global gluing, other unequal-degree,'
        b = 'outsideE818/E821/E822/E823/E824 (including added free summands, rank-deficient or zero unit matrices, other unequal-degree,'
        assert a in row['finding_ids_or_current_gate']
        row['finding_ids_or_current_gate'] = row['finding_ids_or_current_gate'].replace(a,b)
for data in [
    ['Q5v','Prompt target5; global forms of the full-rank unequal-degree unit surface module',
     'Can different global gluing of local M0^r produce a balanced weakly equivariant semiregular seed?',
     'refuted',
     'SF-E824: the canonical first-overlap class has trace r times the nonzero unit obstruction; Pic of the split square-zero End thickening equals Pic(X), so the determinant correction vanishes for normalized hull c1=0. An etale isogeny and line tensoring handle rational B by transporting ordinary vanishing, not semiregularity. All global unit forms, including SF-UG nontensor objects, are excluded. Added free summands and other local models remain outside scope.'],
    ['Q5w','Prompt target5; actual nontensor unit-surface repairs',
     'Do actual nontensor global unit forms with the complete positive balanced character exist?',
     'proved',
     'SF-UG: complete End algebra O plus square-zero iO_S(-D)^2, both positive Ext sheaves/actions, chain-product homotopies and actual GL_r(End M0) gluing. The16-line integral hull of rank522387689472 has h1 parameter dimension>=19359-2*6768=5823 in one summand. Nonzero parameters give objects not isomorphic to any global H tensor M0. SF-E824 excludes all of them; the construction alone is not counted as main-gate movement.'],
]:
    rows.append(dict(zip(fields,data)))
with q.open('w',newline='') as f:
    w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)

events = [
    ('SF-UG','targeted proof check',
     'Root read every section of the294-line mathematical draft SHA16b9e88d5c5c5190628272560e4749daa475da6b585cbc80af56e199abeacc77 and all319 canonical TeX lines, plus the entire independent imprimitive report. PASS complete End algebra, left/right nilpotent Ext actions, global twists, chain multiplication homotopy, actual square-zero gluing, nontensor isomorphism test, all16 compensated characters and index-three parameter inequality. No full derived trace or semiregular seed is inferred.',
     'agents/sixfolds/rm_unit_gluing_analysis_section.tex; agents/imprimitive/audit_unit_gluing/PEER_AUDIT.md'),
    ('SF-E824','targeted proof check',
     'Root read the entire mathematical proof and all390 canonical TeX lines, plus the full independent peer report. Reviewed draftSHAf42a0232fbbcfbd21a1aa66516888b3d142658d7b3d1aff16c27df7d3f8c1ffe. PASS canonical truncation/first-overlap map, degree-one semiregularity annihilation on End(F), bar derivation independent of local splittings, normalized overlap identity, determinant derivative, flat determinant and exact B/isogeny transport of ordinary vanishing. Root requested only a theta-subscript typo fix and an explicit affine/stalk C-vector-space splitting clarification; both are present. Scope remains full-rank unit forms only.',
     'agents/sixfolds/rm_unit_gluing_obstruction_section.tex; agents/imprimitive/audit_unit_gluing/PEER_AUDIT.md'),
    ('SF-UG exact local/character certificate','computation or formal certificate',
     'Root read the complete author code and actually reran rm_unit_gluing_certificate.py: PASS, tool wall0.5184seconds. Chain lift/product homotopy, delta characteristic polynomial t^2(t^2-32t-32), index-three dimensions1071/6768/19359, lower bound5823 and positive-Ext Euler coefficient192 checked exactly. Peer independently used sparse polynomial matrices and Qsqrt2 arithmetic, imported neither author code nor Sympy, and checked all16 full hull characters/rank522387689472 and local corrections in0.004297seconds. Global descent and filtration are written proof checks, not computational conclusions.',
     'agents/sixfolds/rm_unit_gluing_certificate.py; agents/sixfolds/rm_unit_gluing_certificate_output.json; agents/imprimitive/audit_unit_gluing/independent_check.py'),
    ('SF-E824 published and supplied inputs','carried as background without fault found',
     'Root uses the previously fully read BF2008 characteristic/semiregularity identities at the exact author-copy statement/page locators in SF-E823/E824, the published Mumford Section16 index theorem at the stated nondegenerate Hermitian hypotheses, and supplied DEG_L S21.6--8 invariant/forgetting compatibility. Peer freshly reread the passages listed in its whole audit. This event claims no new root whole-source reread beyond the earlier recorded readings and no new proof of those published inputs.',
     'agents/sixfolds/rm_unit_gluing_obstruction_section.tex; agents/sixfolds/rm_unit_gluing_analysis_section.tex; agents/imprimitive/audit_unit_gluing/PEER_AUDIT.md'),
    ('SF-UGDC','targeted proof check',
     'Root read the complete local counterproof and its entire exact checker, then freshly reread the complete final draft. PASS: the linear part of Hom(P,P) has no arrow into/out of End(P0), whereas conjugation by1+delta has nonzero V-to-V linear block xE21. Thus no power-series homotopy exists although every cohomology action is identity. This rules out precisely a fixed-target identity-normalized full trace invariant under all inner frame changes; cyclic quotients, filtered traces and individual noncanonical traces are not ruled out. Not a premise of SF-E824 and not counted as main-gate movement.',
     'agents/sixfolds/rm_unit_derived_trace_countercheck.md'),
    ('SF-UGDC exact certificate','computation or formal certificate',
     'Actual root rerun PASS at19:12UTC, tool wall0.338621487seconds. Complex ranks2,6,9,6,2; chain automorphism determinant(y-1)^4; all linear differential arrows into/out of End(P0) zero; nonzero commutator xE21. The written minimal-order argument, rather than finite truncation alone, excludes every power-series homotopy.',
     'agents/sixfolds/rm_unit_derived_trace_certificate.py; agents/sixfolds/rm_unit_derived_trace_certificate_output.json'),
]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
    w=csv.writer(f,delimiter='\t')
    for sid,typ,out,ev in events:
        w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
with (R/'LEDGER.md').open('a') as f:
    f.write('\n## The non-tensor unit-gluing escape is closed\n\n'+now+' — Q5v refuted and Q5i strictly narrowed by SF-E824 after whole root/peer mathematical reviews and full canonical rereading. Every global form locally M0^r is excluded, including genuine nontensor gluing. SF-UG proves those nontensor objects actually exist and computes an explicit parameter lower bound5823; that construction alone is not gate movement. The first-overlap proof avoids the older full-derived-trace gap. A separately checked local counterexample explains why centrality on all self-Ext sheaves would not justify the proposed stronger trace. Added free summands, rank-deficient/zero unit matrices and different local models remain active. This is integration, not an hourly review.\n')
with (R/'IMPLICATIONS.md').open('a') as f:
    f.write('''\n## Global unit gluing cannot repair the balanced seed\n\nSF-UG supplies actual algebraic coherent perfect sheaves with the complete integral positive balanced character and genuine non-tensor global gluing. The square-zero endomorphism scheme and its vector bundles make the construction an ordinary algebraic gluing problem, with no assumed higher cocycle. SF-E824 proves that every global unit form still fails the required weak equivariant semiregularity. The obstruction lies in the first overlap class: its matrix trace is the rank times a fixed nonzero cubic obstruction, and the only determinant correction vanishes. This closes a strictly larger class than the global tensor theorem SF-E823.\n\nThe statement concerns actual K-classes and Atiyah/Ext obstruction maps in the SGA6 framework and DEG_L S-14/S-21. It restricts possible deformation suppliers for condition A, cote16 scan050, rather than giving a negative Hodge-conjecture statement. The exact scheme-spreading and etale realization locators remain in the framework section. Condition I at cote16 scan049 and cote44 Theorem4 cannot remove this obstruction, and the Cayley-Hamilton inverse of scans048--049 divides only classes already supplied. No new weight or motivic L-value assertion follows from the positive character or from the existence of the gluing family. The general balanced-RM seed and the nonsplit detector bound remain open in the precisely listed other local/derived scopes.\n''')
p=R/'research/frameworks.tex';s=p.read_text()
assert 'SF-US and SF-E811--823' in s
s=s.replace('SF-US and SF-E811--823','SF-US, SF-UG and SF-E811--824')
p.write_text(s)
out={'date_utc':now,'integrated':['SF-UG','SF-E824'],'canonical_proof_hashes':proofs,
     'new_refuted_row':'Q5v','actual_construction_row':'Q5w','main_gate':'Q5i',
     'full_derived_trace_used':False,'semiregularity_pulled_back':False}
(R/'research/unit_gluing_integration.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
