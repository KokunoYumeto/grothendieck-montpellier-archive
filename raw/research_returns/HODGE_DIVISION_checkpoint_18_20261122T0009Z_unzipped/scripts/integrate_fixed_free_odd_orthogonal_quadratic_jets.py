"""Integrate three completely reviewed, strictly stronger necessary gates."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re

R = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
proofs = {
    'HD-ALT-07': ('research/ordinary_alternating_fixed_free_section.tex',
                  '78ffa543eacf6f88a656c2bc37f673b75acca4eba98671cbba9f564f4885c9b7'),
    'D-OL-12--13': ('agents/imprimitive/orthogonal_lowlevels/orthogonal_odd_nonselfdual_section.tex',
                    '0ed85dfb4a94ac000e411e22a2c9735157c2bd8fa606ff4d7c507c66cf8f2921'),
    'SF-E838': ('agents/sixfolds/rm_quadratic_jet_obstruction_section.tex',
                '934bf4e4142c4994d31f55458a5370124adc569c9f8cc76bf5ae4212dc5560f3'),
}
reports = {
    'HD-ALT-07': ('agents/g34_eightfolds/bireflection/ORDINARY_ALTERNATING_FIXED_FREE_PEER_AUDIT.md',
                  'c404aa43986bfd316a18e597e94f9a83841e1dc981969aa76fbc951eaa1f3304'),
    'D-OL-12--13': ('agents/g34_eightfolds/bireflection/ORTHOGONAL_ODD_NONSELFDUAL_PEER_AUDIT.md',
                    '2ee041f08c81648143a2061bc31c7c6954ca474df52aa06131959d7b43775188'),
    'SF-E838': ('agents/imprimitive/audit_quadratic_jet/PEER_AUDIT.md',
                '2887abac5cc07b2f30a82cad0565a6f5d1e58b3fdb0e5d767198c3039148d612'),
}
for path, sha in list(proofs.values()) + list(reports.values()):
    assert hashlib.sha256((R/path).read_bytes()).hexdigest() == sha, path

def change(s, old, new):
    assert s.count(old) == 1, (old, s.count(old))
    return s.replace(old, new)

p = R/proofs['HD-ALT-07'][0]
s = p.read_text()
s = change(s, 'This is a complete new root derivation, submitted for independent\nwhole-proof review.',
           'This complete new root derivation has passed the full root and\nindependent /root/g34\\_eightfolds proof reviews, with separate exact\narithmetic supplements.')
p.write_text(s)
p = R/proofs['D-OL-12--13'][0]
s = p.read_text()
s = change(s, 'proof and exact supplement pass the author check; independent\nwhole-proof review is pending.',
           'proof and exact supplement pass the author check; whole-proof\nreviews by /root and /root/g34\\_eightfolds have also passed, with\na separate exact peer supplement.')
p.write_text(s)
p = R/proofs['SF-E838'][0]
before = s = p.read_text()
s = change(s, 'complete new proof checked in full by the author and /root;\nindependent peer review is pending.',
           'complete new proof checked in full by the author, /root and\n/root/imprimitive. Both reviewers also read the entire canonical\nconversion; all twenty-one displays are unchanged.')
s = change(s, 'Stacks Lemma 27.22.1, tag 089R',
           'Stacks Section 27.22, tag 089R, Lemma 27.22.1')
assert re.findall(r'\\\[(.*?)\\\]', before, re.S) == re.findall(r'\\\[(.*?)\\\]', s, re.S)
p.write_text(s)
p = R/'agents/sixfolds/rm_quadratic_jet_bibitems.tex'
s = p.read_text()
s = change(s, 'sequences; Lemma 27.22.1, tag \\texttt{089R}, complete Grassmannian',
           'sequences; Section 27.22, tag \\texttt{089R}, Lemma 27.22.1, complete Grassmannian')
p.write_text(s)

alt = ('HD-ALT07a/b removes the sole fixed-point-free involution loss by the published Fomin-Lulov exact rim-hook bound. '
       'Every long ordinary Specht factor has full-normalizer support beta(n,k)=k(n-1-k)/((n-1)(n-2)); '
       'the actual two multiplier marks force beta<=1/10+3/(5e). Thus every remaining ordinary transitive An label, n>=15, '
       'has a row or column>((1+sqrt(3/5))/2)n, about0.8872983346n. '
       'The exact (88,12) label atn100 satisfies the stronger old finite inequality and violates the new one, proving strictness. '
       'Still longer shapes and separately unexcluded standard tensors remain; no source existence is asserted. ')
orth = ('D-OL12--13 excludes all ordinary nonselfdual odd-dimensional orthogonal factors over oddq>=5 atd>=1135, '
        'including arbitrary compatible linear/field/scalar normalizers and mixed such tensor factors. '
        'Signed line-radical action permits rank1; its actual norm-level fixed fraction is<1/4 atq>=5. '
        'Without a signed fixed hyperbolic pair, LST restricted mu2 support>=567 gives support>delta*a, '
        'delta=(1-(19/20)^9)/2>1/6 and actual source degree<28, below the factor floor. '
        'Full-O reality and Clifford restriction show compatible linear normalizers are scalar-inner without assuming an extension. '
        'Together with the selfdual d<=21 result, every remaining transitive ordinary odd-dimensional factor over oddq>=5 has d<=1133. '
        'The q3 rank-one fixed-fraction29525/88574>1/3 refutes that shortcut only; q3 odd-natural, odd-field even-natural and genuine spin cases retain earlier gates. ')
quad = ('SF-E838 excludes every common complete-intersection point defect whose regular quadratic jets have some bracket pencil '
        'spanning the six-dimensional quadratic quotient, including every higher-order formal perturbation and all positive multiplicities. '
        'For a commutative Artin algebra with h2>embeddingdimension, a square matrix whose cokernel is killed by the maximal-ideal square is invertible; '
        'the actual companion pencil then forces proportional leading bracket tuples, contradicting the Jacobian socle. '
        'A ten-by-ten determinant gives seven degree16 coefficient equations defining a necessary residual closed locus in the regular Gr(4,10) locus. '
        'An explicit nonsquare length16 algebra has nonzero pure endpoints and admits no commuting-triple presentation for either bivector; '
        'a24-dimensional open family exceeds the dimension<=15 square-orbit closure. Thus this strictly reduces Q5i beyond E836/E837. '
        'Actual rank32 coherent balanced examples exist before imposing semiregularity; no successful finite action or seed is asserted. ')

q = R/'QUESTIONS.tsv'
rows = list(csv.DictReader(q.open(), delimiter='\t')); fields = list(rows[0])
assert not {'Q2bz','Q2ca','Q5al'} & {r['id'] for r in rows}
(R/'research/gates_before_fixed_free_odd_orthogonal_quadratic_jets.json').write_text(
    json.dumps({r['id']:r for r in rows if r['id'] in ('Q2i','Q5i')}, indent=2)+'\n')
for r in rows:
    if r['id'] == 'Q2i':
        s = r['finding_ids_or_current_gate']
        a = s.index('HD-ALT06a/b strengthens this')
        b = s.index('The all-degree scalar single-factor', a)
        s = s[:a] + alt + s[b:]
        s = change(s, 'Odd-field nonselfdual ordinary and genuine spin cases retain their earlier bounds. ', orth)
        r['finding_ids_or_current_gate'] = s
    if r['id'] == 'Q5i':
        r['finding_ids_or_current_gate'] += ' '+quad
rows.extend([
    dict(zip(fields, ['Q2bz','Prompt target2; actual normalizer support for long alternating labels',
                      'Can a remaining ordinary transitive alternating factor lie between the old87percent bound and the new radical threshold?',
                      'refuted',alt+'Whole root/G34 proof/source reviews PASS; distinct exact signed-domino supplements retained.'])),
    dict(zip(fields, ['Q2ca','Prompt target2; odd-dimensional ordinary nonselfdual orthogonal cores',
                      'Can oddq>=5 and odd natural dimensiond>=1135 supply the actual rank-nine source?',
                      'refuted',orth+'Whole author/root/G34 proof/source/code reviews PASS; independent norm-distribution supplement retained.'])),
    dict(zip(fields, ['Q5al','Prompt target5; common Artin complete intersections and actual companion pencils',
                      'Can a regular quadratic complete-intersection point defect with a full-rank leading bracket pencil be a balanced weakly semiregular repair?',
                      'refuted',quad+'Whole author/root/imprimitive proofs and canonical readings PASS; distinct exact determinant/Hilbert supplements retained.'])),
])
with q.open('w', newline='') as f:
    w=csv.DictWriter(f, fields, delimiter='\t'); w.writeheader(); w.writerows(rows)

p = R/'HODGE_DIVISION.tex'; s = p.read_text()
for anchor, extra in [
    ('research/ordinary_alternating_87_section.tex',proofs['HD-ALT-07'][0]),
    ('agents/imprimitive/orthogonal_lowlevels/orthogonal_nonextendible_section.tex',proofs['D-OL-12--13'][0]),
    ('agents/sixfolds/rm_square_artin_matrix_obstruction_section.tex',proofs['SF-E838'][0]),
    ('research/root_bibitems.tex','research/ordinary_alternating_fixed_free_bibitems.tex'),
    ('agents/sixfolds/rm_ci_point_quantization_bibitems.tex','agents/sixfolds/rm_quadratic_jet_bibitems.tex')]:
    x = r'\input{'+anchor+'}'
    s = change(s,x,x+'\n'+r'\input{'+extra+'}')
s = change(s, '''The latter bound does not cover odd-field nonselfdual ordinary
characters or genuine spin characters; their previous bounds remain.''', r'''D-OL-12--13 further reduces ordinary odd-dimensional factors over odd
$q\ge5$ to $d\le1133$. In the nonselfdual case, compatible linear
normalizers are scalar-inner by full-$O$ reality and Clifford restriction.
Signed line-radical actions, including moving rank one, have fixed weight
fraction below $1/4$; the remaining inner cases have restricted natural
support at least $567$. The published spin-group bound then gives
$\nu>\{1-(19/20)^9\}a/2$, and twelve genuine inertias force degree
below $28$, contrary to the factor floor. Arbitrary mixed field components
are included. At $q=3$ the proposed quarter fixed-weight shortcut is
explicitly false. The ordinary odd-$q$ even-natural case, this $q=3$
boundary, and genuine spin characters retain their previous bounds.''')
anchor = 'precise cubic degree floor, and $e<54$ at the fifteen smaller endpoints.'
s = change(s, anchor, anchor+r'''
HD-ALT-07 now removes the fixed-point-free involution loss with the
published Fomin--Lulov rim-hook estimate. Its common full-normalizer
support fraction is exactly $k(n-1-k)/((n-1)(n-2))$, giving the stronger
necessary inequality with this fraction in place of $\delta(n,k)$.
Every remaining row or column must consequently exceed
$\tfrac12(1+\sqrt{3/5})n$. The label $(88,12)$ at $n=100$ passes
the old finite-degree gate but fails this new one, proving strictness.''')
anchor = 'to the scalar inference. It does not extend to arbitrary Artin modules.'
s = change(s, anchor, anchor+r'''
SF-E838 next excludes a nonempty open family of regular quadratic
complete intersections and every higher-order perturbation of those
jets. A full-rank bracket pencil forces its actual companion matrix
invertible, using the strict Hilbert inequality $6>4$; the resulting
proportional leading tuples contradict the nonzero Jacobian socle.
Seven degree-six-pencil coefficients, each of degree sixteen in the
quadratic data, cut out a necessary residual locus. The explicit
nonsquare example has nonzero pure endpoints and no commuting-triple
presentation, so this is strict progress beyond both E836 and E837.
It asserts no module deformation on the residual locus.''')
p.write_text(s)

events = [
    ('HD-ALT-07 peer audit','targeted proof check',
     'Root read whole final G34 report c404aa43. Frozen proof78ffa543, all source/code reviews PASS. Separate signed-domino certificate15578partitions,158long shapes, corrected88,12 witness PASS0.644287s22:05:08UTC. Initial witness22,3 did not satisfy old stronger finite gate and was corrected before freeze. Root has not whole-read peer code. Source binary/visual limitations retained.', reports['HD-ALT-07'][0]),
    ('D-OL-12--13 root whole proof and computation reading','targeted proof check',
     'Root whole frozen proof0ed85dfb, every author checker line, full JSON, exact source interfaces and status read. Signed epsilon action/rank1, all-rank Gauss bound, restricted mu2 support567, Clifford nonselfduality, mixed-field descent and actual source inequality PASS. Author104510vectors certificate0.118284012s22:05:08UTC read; not freshly executed by root. q3 failed shortcut retained.', proofs['D-OL-12--13'][0]),
    ('D-OL-12--13 peer audit','targeted proof check',
     'Root whole final G34 report2ee041f0 read. Independent216norm distributions and13D signed-radical/twelve-reflection supplement PASS0.070781199s22:10:14UTC. Initial SymPy integer JSON serialization failure repaired only in output, full rerun retained. Root has not whole-read peer code.', reports['D-OL-12--13'][0]),
    ('SF-E838 root whole proof and canonical conversion','targeted proof check',
     'Root entire244-line frozen draft43e434ab and all483 canonical lines934bf4e4 read. Every arbitrary-Artin/filtered/pencil/Jacobian/Grassmannian/strictness/global step PASS. Complete author checker, full25-check JSON and conversion certificate read;21displays byte-identical. Exact author run2.329530127s22:06:03UTC read, not rerun. Earlier slow interrupted attempt not counted as PASS. No whole conversion-diff or TeX compilation claim.', proofs['SF-E838'][0]),
    ('SF-E838 Stacks source interfaces','used and rechecked in this run',
     'Root fresh complete Stacks00NQ Lem10.106.3,02JN Lem10.104.2,00N6 Prop10.103.4 and Section27.22/tag089R including Lem27.22.1 proof read. Web refs turn119289315view0..3. Previously entire E-U Th7.1/AppA1/A3/A5 scope reused; no claim to reread all upstream sources. Section tag locator clarified editorially.', 'agents/sixfolds/rm_quadratic_jet_bibitems.tex'),
    ('SF-E838 peer audit','targeted proof check',
     'Root whole imprimitive report2887abac read. Peer whole frozen draft, canonical, author code/output and primary proofs PASS; independent Fraction/sparse-polynomial/interpolation determinant, covariance, Hilbert, socle16 and12perturbed jets PASS0.064329775s22:09:08UTC first run. Root has not whole-read peer code.', reports['SF-E838'][0]),
    ('HD-ALT-07 D-OL-12--13 SF-E838 integration','targeted proof check',
     'Three completely reviewed frozen proofs integrated; only status and precise Stacks section locator edits. E83821displays unchanged. Q2bz,Q2ca,Q5al refuted; Q2i,Q5i strictly reduced. No extra checkpoint, source existence, or TeX compilation claimed.', 'scripts/integrate_fixed_free_odd_orthogonal_quadratic_jets.py'),
]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
    w=csv.writer(f,delimiter='\t')
    for sid,typ,out,evidence in events:
        w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,evidence])
with (R/'LEDGER.md').open('a') as f:
    f.write('\n## Fixed-free involutions, odd orthogonal cores and quadratic jets\n\n'+now+
            ' — Q2bz, Q2ca and Q5al refuted; Q2i and Q5i strictly reduced. '+alt+orth+quad+
            'This is after review09/checkpoint15 and before the next scheduled review/checkpoint; no unscheduled archive.\n')
with (R/'IMPLICATIONS.md').open('a') as f:
    f.write('\n## Three stricter actual supplier restrictions\n\n'+alt+orth+quad+
            'The group results restrict actual finite local systems and weight-one period maps; the local result restricts actual Artin-scheme point modifications and their perfect resolutions. '
            'They constrain condition-A suppliers (cote16 scan050; SIGN_NEXT SN-C03/C04), while condition I (scan049/cote44 Th4) still supplies no cycles. '
            'The Cayley-Hamilton resultant projector in scans048-049 and the common scheme-over-Z, lambda/K-theory, SGA/EGA/FGA, realization, weight and motivic/L-function framework remain as stated. '
            'No new Markman, Severn or032 premise is introduced.\n')
out = {'date_utc':now,'frozen_proofs':proofs,'whole_read_peer_reports':reports,
       'canonical_sha256':{k:hashlib.sha256((R/v[0]).read_bytes()).hexdigest() for k,v in proofs.items()},
       'new_rows':{'Q2bz':'refuted','Q2ca':'refuted','Q5al':'refuted'},
       'strictly_reduced_main_gates':['Q2i','Q5i'],'E838_displays_unchanged':21}
(R/'research/fixed_free_odd_orthogonal_quadratic_jets_integration.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
